# knowledge/

Everything in this directory is uploaded as project knowledge to the claude.ai Project ("Voice & Drafts"). The Project is the deployment; this directory is the source of truth. When you change something here, re-upload to keep the Project in sync.

## What lives here

| Path | Purpose |
|---|---|
| `project-instructions.md` | The system prompt for the Project. Paste this into the Project's custom instructions field. |
| `voice-guide.md` | The living description of how Nick writes. Refined over time as new patterns are noticed. |
| `guardrails.md` | Non-overridable rules — disclosure, what the tool will and won't do. Referenced from `project-instructions.md`. |
| `samples/` | Reference samples: Nick's actual finished writing. Positive examples. |
| `counter-examples/` | Before/after pairs: a draft Claude produced and the version Nick revised it to. The most valuable training signal. |

## Update flow

1. Edit files here in the repo.
2. Re-upload the changed files to the claude.ai Project.
3. If `project-instructions.md` changed, also paste the new version into the Project's custom instructions.

## Future stages

Stage 2 will add `context/` (team, projects, stakeholders). Stage 3 will add `reasoning/` (decision-capture notes). Both live under this directory — additive only, no reorganization.
