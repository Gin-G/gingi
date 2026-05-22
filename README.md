# gingi

A staged build of "Digital Me" — a tool that captures Nick's voice and writing style, then evolves into a voice agent and eventually a thinking/drafting partner with real context access.

Roadmap: [PLAN.md](PLAN.md).

## Where we are

**Stage 1 — Writing Voice Foundation.** Everything in this repo right now supports a single goal: drafts produced in Nick's voice with minimal rework. The deployment target for Stage 1 is a claude.ai Project called "Voice & Drafts."

## Repo layout

```
gingi/
├── PLAN.md                  # roadmap across all 6 stages
├── README.md                # this file
├── knowledge/               # source of truth for what's uploaded to the claude.ai Project
│   ├── project-instructions.md   # the Project's system prompt
│   ├── voice-guide.md            # how Nick writes — living doc
│   ├── guardrails.md             # non-overridable rules (disclosure, etc.)
│   ├── samples/                  # Nick's finished writing (positive examples)
│   └── counter-examples/         # before/after pairs (the most valuable signal)
└── evaluation/              # the feedback loop
    └── runs/                # one folder per evaluation case
```

Later stages will add `knowledge/context/` (Stage 2), `knowledge/reasoning/` (Stage 3), and a top-level `apps/` directory (Stages 4–5).

## Stage 1 workflow

**To set up the Project:**

1. Create a claude.ai Project called "Voice & Drafts."
2. Paste the contents of `knowledge/project-instructions.md` into the Project's custom instructions.
3. Upload everything in `knowledge/` (voice-guide, guardrails, all samples, all counter-examples) as project knowledge.

**Day to day:**

- When you produce something with the Project and revise it heavily, save the pair to `knowledge/counter-examples/`.
- When you ship something you're happy with, save it to `knowledge/samples/`.
- Once a week, run one evaluation cycle (see `evaluation/README.md`).
- After every 5–10 counter-examples, scan them for repeated patterns and promote rules into `knowledge/voice-guide.md`.
- Re-upload changed files to the Project so it stays in sync with the repo.

## When to move on from Stage 1

When three evaluation runs in a row produce drafts you would have sent with only minor edits. Then start Stage 2.
