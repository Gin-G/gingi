# evaluation/

The feedback loop. Each "run" is a held-out test: take a real message Nick has already responded to, have the Project draft a response without seeing the answer, then compare.

This is how we tell whether Stage 1 is actually working. The bar isn't perfect match — it's whether the divergences shrink over time.

## How a run works

1. Pick a recent message Nick has already responded to (email, text, chat, review comment, whatever).
2. Create a folder: `runs/YYYY-MM-DD-short-topic/`.
3. Write `prompt.md` — the incoming message, plus minimal context Claude would need (sender, relationship, situation). **Do not include the actual response.**
4. Paste `prompt.md` into the claude.ai Project. Save the output as `generated.md`.
5. Paste Nick's actual reply as `actual.md`.
6. Write `notes.md`: what diverged, what patterns the Project missed or invented, what should be added to the Voice Guide or captured as a counter-example.
7. If a divergence is significant, also create a counter-example in `../knowledge/counter-examples/`.

## File format

Each run folder contains four files:

```
runs/2026-05-15-cirrus-status-question/
├── prompt.md      # incoming message + context, no answer
├── generated.md   # what the Project produced
├── actual.md      # what Nick actually sent
└── notes.md       # divergences + follow-ups
```

### `prompt.md`

```markdown
---
sender: <name and relationship — "Direct report Kevin", "VP of Eng", etc.>
medium: <email | text | chat | review comment | other>
date_received: 2026-05-14
---

## Context

<one or two sentences of situational context Claude would not have>

## Incoming message

<the message itself, verbatim>
```

### `notes.md`

```markdown
## Divergences

- <pattern Claude got wrong — be specific, not "tone was off">
- <missing context Claude assumed instead of asking about>
- <anything Claude invented>

## What worked

- <patterns Claude got right — equally important to record>

## Follow-ups

- [ ] Add counter-example: `knowledge/counter-examples/2026-05-15-...md`
- [ ] Update voice-guide.md: <which section, what rule>
- [ ] Add to samples: `knowledge/samples/2026-05-15-...md` (the *actual* response)
```

## Cadence

Aim for one run per week. More if Nick is in a writing-heavy period. The point is consistency, not volume — a single thoughtful run beats five rushed ones.

## When Stage 1 is "done"

When three runs in a row produce a `generated.md` that Nick would have sent with only minor edits. At that point, move on to Stage 2.
