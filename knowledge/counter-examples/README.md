# counter-examples/

Before/after pairs. Each file captures one case where Claude produced a draft and Nick revised it — showing both versions side by side, plus what changed and why.

These are the most valuable training signal in the whole repo. A sample shows what good looks like; a counter-example shows the *boundary* — where Claude was wrong and how to be right.

## What belongs here

- Drafts Claude produced that Nick reworked significantly (not just typo fixes).
- Cases where the revision reveals a pattern Claude got wrong — voice, structure, tone, factual framing.

## What does not belong here

- Cases where Nick agreed with Claude's draft and sent it as-is — those go in `../samples/` if notable.
- Trivial edits (a single word swap, punctuation, formatting).

## File format

```markdown
---
context: <what was being drafted>
date: 2026-05-15
---

## Prompt

<the request given to Claude, with enough context to reproduce>

## Claude's draft

<exactly what Claude produced, no edits>

## My revision

<the version Nick actually sent>

## What changed

- <one bullet per pattern that changed — name the pattern, not just the words>
- e.g. "Removed 'at scale' (marketing language)"
- e.g. "Re-led with the outcome instead of the tool name"
- e.g. "Cut the closing summary sentence — Nick closes with implications, not recap"
```

## Naming

`YYYY-MM-DD-short-topic.md` — e.g. `2026-05-15-status-update-cirrus.md`.

## When to update the Voice Guide

If a "What changed" bullet appears in two or more counter-examples, promote it to a rule in `../voice-guide.md`. The counter-example stays as the evidence; the guide gets the rule.
