#!/usr/bin/env python3
"""
seed_samples_from_mbox.py

Turn a Google Takeout "Sent" .mbox export into candidate sample files for the
Voice & Drafts project's samples/ directory.

For each sent message it:
  - pulls the plaintext body (prefers text/plain, falls back to de-HTML'd text/html)
  - strips quoted reply chains, forwarded headers, and signatures
  - drops anything too short to be useful voice signal
  - writes one candidate  <YYYY-MM-DD-slug>.md  with stubbed frontmatter

Output is deliberately over-inclusive: it produces *candidates*. You still
hand-pick and delete the ones that don't earn a spot. Nothing here is authoritative.

stdlib only. Usage:
    python seed_samples_from_mbox.py Sent.mbox -o ./samples_candidates
    python seed_samples_from_mbox.py All.mbox  -o ./out --from you@ucar.edu --min-words 40
"""
from __future__ import annotations

import argparse
import mailbox
import re
from datetime import datetime
from email import message_from_bytes
from email.header import decode_header, make_header
from email.utils import parsedate_to_datetime
from html.parser import HTMLParser
from pathlib import Path


# --- HTML -> text (lightweight, stdlib only) --------------------------------

class _DeHTML(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self._chunks: list[str] = []
        self._skip = False

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self._skip = True
        if tag in ("br", "p", "div", "tr", "li"):
            self._chunks.append("\n")

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self._skip = False

    def handle_data(self, data):
        if not self._skip:
            self._chunks.append(data)

    def text(self) -> str:
        return "".join(self._chunks)


def html_to_text(html: str) -> str:
    p = _DeHTML()
    try:
        p.feed(html)
    except Exception:
        return html
    return p.text()


# --- body extraction --------------------------------------------------------

def _decode(part) -> str:
    payload = part.get_payload(decode=True)
    if payload is None:
        return ""
    charset = part.get_content_charset() or "utf-8"
    try:
        return payload.decode(charset, errors="replace")
    except LookupError:
        return payload.decode("utf-8", errors="replace")


def get_body(msg) -> str:
    """Best-effort plaintext body. Prefer text/plain; fall back to text/html."""
    plain, html = None, None
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_maintype() == "multipart":
                continue
            if part.get_content_disposition() == "attachment":
                continue
            ctype = part.get_content_type()
            if ctype == "text/plain" and plain is None:
                plain = _decode(part)
            elif ctype == "text/html" and html is None:
                html = _decode(part)
    elif msg.get_content_type() == "text/html":
        html = _decode(msg)
    else:
        plain = _decode(msg)

    if plain and plain.strip():
        return plain
    if html:
        return html_to_text(html)
    return ""


# --- stripping quotes / replies / signatures --------------------------------

_REPLY_CUTS = [
    re.compile(r"\nOn .{0,300}?wrote:", re.DOTALL),                # Gmail (1- or 2-line)
    re.compile(r"\n-{2,}\s*Original Message\s*-{2,}", re.I),       # Outlook
    re.compile(r"\n_{5,}"),                                        # Outlook rule line
    re.compile(r"\nFrom:.{0,400}?\nSubject:.*", re.DOTALL | re.I), # forwarded header block
]

_SIG_CUTS = [
    re.compile(r"\n-- \n.*", re.DOTALL),                # RFC 3676 signature delimiter
    re.compile(r"\nSent from my .*", re.DOTALL | re.I), # mobile
    re.compile(r"\nGet Outlook for .*", re.DOTALL | re.I),
]


def _cut_earliest(text: str, patterns) -> str:
    earliest = len(text)
    for pat in patterns:
        m = pat.search(text)
        if m and m.start() < earliest:
            earliest = m.start()
    return text[:earliest]


def strip_reply_and_sig(text: str) -> str:
    text = _cut_earliest(text, _REPLY_CUTS)
    text = _cut_earliest(text, _SIG_CUTS)
    # drop any leftover quoted lines
    lines = [ln for ln in text.splitlines() if not ln.lstrip().startswith((">", "|"))]
    return "\n".join(lines)


def normalize(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+\n", "\n", text)   # trailing whitespace
    text = re.sub(r"\n{3,}", "\n\n", text)   # collapse blank runs
    return text.strip()


def word_count(text: str) -> int:
    return len(re.findall(r"\S+", text))


# --- header helpers ---------------------------------------------------------

def header(msg, name: str) -> str:
    raw = msg.get(name, "")
    try:
        return str(make_header(decode_header(raw)))
    except Exception:
        return raw


def msg_date(msg) -> datetime | None:
    raw = msg.get("Date")
    if not raw:
        return None
    try:
        return parsedate_to_datetime(raw)
    except (TypeError, ValueError):
        return None


def slugify(text: str, max_len: int = 40) -> str:
    text = re.sub(r"^(re|fwd|fw):\s*", "", text.strip(), flags=re.I)
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text).strip("-").lower()
    return text[:max_len].strip("-") or "untitled"


# --- main -------------------------------------------------------------------

FRONTMATTER = (
    "---\n"
    "context: {context}\n"
    "audience: \n"
    "date: {date}\n"
    "---\n\n"
)


def main() -> None:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("mbox", type=Path, help="path to the .mbox export (e.g. Sent.mbox)")
    ap.add_argument("-o", "--out", type=Path, default=Path("samples_candidates"),
                    help="output directory for candidate .md files")
    ap.add_argument("--from", dest="from_addr", default=None,
                    help="only keep messages whose From contains this string "
                         "(use on non-Sent exports)")
    ap.add_argument("--min-words", type=int, default=40,
                    help="skip messages shorter than this after cleaning (default 40)")
    args = ap.parse_args()

    args.out.mkdir(parents=True, exist_ok=True)
    box = mailbox.mbox(str(args.mbox))

    written = skipped_short = skipped_from = 0
    seen: set[str] = set()
    rows: list[tuple[str, int, str]] = []

    for key in box.iterkeys():
        msg = message_from_bytes(box.get_bytes(key))

        if args.from_addr and args.from_addr.lower() not in header(msg, "From").lower():
            skipped_from += 1
            continue

        body = normalize(strip_reply_and_sig(get_body(msg)))
        wc = word_count(body)
        subject = header(msg, "Subject") or "(no subject)"

        if wc < args.min_words:
            skipped_short += 1
            continue

        dt = msg_date(msg)
        date_str = dt.date().isoformat() if dt else "0000-00-00"

        base = f"{date_str}-{slugify(subject)}"
        name, i = base, 2
        while name in seen or (args.out / f"{name}.md").exists():
            name = f"{base}-{i}"
            i += 1
        seen.add(name)

        (args.out / f"{name}.md").write_text(
            FRONTMATTER.format(context=f'Email — "{subject}"', date=date_str) + body + "\n",
            encoding="utf-8",
        )
        written += 1
        rows.append((f"{name}.md", wc, subject))

    # triage summary
    print(f"\nWrote {written} candidate(s) to {args.out}/")
    print(f"Skipped {skipped_short} (under {args.min_words} words)"
          + (f", {skipped_from} (From filter)" if args.from_addr else ""))
    if rows:
        print("\n  words  file / subject")
        print("  -----  " + "-" * 52)
        for fname, wc, subject in sorted(rows, key=lambda r: r[1], reverse=True):
            print(f"  {wc:5d}  {fname}")
            print(f"         {subject[:60]}")
    print("\nNext: hand-pick the keepers, fill in context/audience, delete the rest.")


if __name__ == "__main__":
    main()