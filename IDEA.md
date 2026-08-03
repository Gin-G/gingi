---
status: active
progress: 20
---

# Gingi

A staged build of "Digital Me" — a tool that drafts in Nick's voice, then grows into a voice agent and eventually a thinking partner with real context access. Six stages, in PLAN.md.

Stage 1 (Writing Voice Foundation) is underway. The repo is the source of truth for a claude.ai Project called "Voice & Drafts": instructions, voice guide, guardrails, samples, counter-examples. The knowledge base is scaffolded and seeded; the evaluation loop has not run yet.

<!--
IdeaBRD parses this file. It is the source of truth for this idea's tile:
the app re-reads it on every open and commits its own edits back here, so
the shape below matters more than it looks. Anything the parser
(backend/app/ideafile.py) can't read is dropped silently.

  frontmatter  status: one of idea, active, paused, done. progress: 0-100.
               Any other key is ignored.
  # heading    The idea title (first H1).
  prose        Everything outside the Todos section becomes the tile's
               notes, shown on the board — so keep it short. Documentation
               written here is published, not filed away.
  ## Todos     That heading exactly (or "## To-Dos"); "## ToDo", "## TODO"
               and "## Tasks" do not match and the whole list is lost.
               Inside it, only "- [ ] open" / "- [x] done" lines survive:
               sub-headings and blank-line grouping are discarded, and a
               wrapped item is cut at the line break, so keep each to-do on
               one line. The next "## " heading ends the list.

To-dos are matched to the board by exact text, so rewording one replaces it
rather than editing it in place — expect a checked item to come back
unchecked if you reword it.

HTML comments are stripped on read, so this block never reaches the board.
-->

## Todos

- [x] Write PLAN.md — the six-stage roadmap from writing voice through real context access
- [x] Scaffold the repo: knowledge/ and evaluation/ with READMEs and file-format specs
- [x] Draft project-instructions.md — the system prompt for the Voice & Drafts Project
- [x] Draft guardrails.md — AI disclosure rule plus hard limits on what the tool will not do
- [x] Draft voice-guide.md — living description of Nick's sentence, structure, and tone patterns
- [x] Add the four starter samples (two manager comments, two self-eval sections) with full frontmatter
- [x] Write seed_samples.py — turn a Gmail Sent .mbox export into candidate sample files
- [x] Seed ~1,263 candidate samples from the mbox export, 2006–2026, untriaged
- [x] Capture five counter-examples: NSF synergistic activities, CIRRUS abstract, NSF key personnel, flood scheduling reply, recruiter reply
- [x] Promote the first batch of counter-example patterns into voice-guide.md
- [ ] Triage the seeded samples — delete transactional and auto-generated mail (~180 order/shipment/reservation files) and the one dated 0000-00-00
- [ ] Review the 436 dedupe-suffixed (-2, -3) files and keep only the version actually sent
- [ ] Fill in context and audience frontmatter on the samples that survive triage (1,262 are still stubs)
- [ ] Promote the scheduling-closer rule to voice-guide.md — "just let me know" carries the flexibility, now at the two-instance threshold
- [ ] Watch for a second casual-register instance before splitting the sentence-length rule into formal vs. casual
- [ ] Create the "Voice & Drafts" Project on claude.ai, paste project-instructions.md, and upload knowledge/
- [ ] Decide how a thousand-plus sample files fit the Project's knowledge limits — bundle, subset, or curate hard
- [ ] Run the first evaluation cycle; evaluation/runs/ is still empty
- [ ] Hold the weekly cadence: one eval run per week, one counter-example after every heavy rework
- [ ] Stage 1 exit gate: three eval runs in a row Nick would send with only minor edits
- [ ] Stage 2, after the gate: build knowledge/context/ for team, projects, and stakeholders
