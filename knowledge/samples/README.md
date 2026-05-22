# samples/

Reference samples: things Nick has actually written and shipped. These are positive examples — pattern-match against them when drafting.

## What belongs here

- Final, sent versions of writing Nick is happy with.
- Variety: manager comments, self-evaluations, emails, status updates, talk abstracts, technical write-ups.
- Both short and long pieces. Both formal and casual.

## What does not belong here

- Drafts Nick had to rework heavily — those go in `../counter-examples/` instead.
- Other people's writing, even if Nick likes it.
- Writing that's mostly someone else's words (forwarded content, quoted material).

## File format

One sample per file. Use this frontmatter:

```markdown
---
context: Manager comment for direct report's annual review
audience: HR, the employee, skip-level
date: 2025-03-12
---

<the actual text, exactly as sent, no edits>
```

The body is the shipped version with no commentary. If you want to explain why a sample is notable, put it in a `## Notes` section at the bottom — but keep it short.

## Naming

`YYYY-MM-DD-short-topic.md` — e.g. `2025-03-12-manager-comment-observability.md`. The date is when it was written/sent, not when it was added to the repo.

## Starter samples to add

From the conversation that produced `PLAN.md`, four samples were called out as good starters:

- Observability & Access Control manager comment (Traefik / multi-tenancy)
- Platform Security & Documentation manager comment (OpenBao / Velero / LetsEncrypt)
- Agile Implementation employee comment (the reordered one with ticket completion times)
- Overall self-evaluation summary (CIRRUS production, GDEX migration, parental leave, LEAD training)

Add these when you have access to the originals.
