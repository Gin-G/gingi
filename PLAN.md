# Digital Me — Project Plan

A staged approach to building a tool that captures your voice and writing style, evolves into a voice agent, and eventually has access to enough context to be useful as a thinking and drafting partner.

## Guiding Principles

- **Text quality first.** If the writing doesn't sound like you, the voice version won't either. Don't skip ahead.
- **Build what you'll actually use.** Validate each stage before investing in the next.
- **Refine continuously.** Every draft you rework is training data for the next iteration.
- **The goal is augmentation, not replacement.** This is a tool to help you draft, think, and prepare — not to substitute for you in real conversations with real consequences.

---

## Stage 1 — Writing Voice Foundation

**Goal:** Claude reliably produces drafts in your voice with minimal rework.

**Where this lives:** A Claude.ai Project with custom instructions and reference materials.

### Setup

Create a Project in claude.ai called something like "Voice & Drafts." Add these as project knowledge:

1. **Voice Guide** (the document below in the Appendix) — describes your patterns explicitly.
2. **Reference samples** — your final versions of writing you've done. Performance review comments are a goldmine here.
3. **Counter-examples** — drafts Claude produced that you significantly reworked, paired with your final version. Format: "Claude wrote → I changed to."

### Initial samples to add

From this conversation, these are good starter samples in your voice:

- The Observability & Access Control manager comment (the Traefik / multi-tenancy one)
- The Platform Security & Documentation manager comment (OpenBao / Velero / LetsEncrypt)
- Your Agile Implementation employee comment (the reordered one with ticket completion times)
- Your overall self-evaluation summary (CIRRUS production, GDEX migration, parental leave, LEAD training)

### Workflow once it's set up

- Every time you have Claude draft something and you rework it, save the before/after pair to the project.
- Once a month, review the samples and look for new patterns to add to the Voice Guide.
- After 10-15 reworked drafts, the voice should be noticeably more accurate.

### Success criteria

- Claude's first draft requires minor edits, not full rewrites.
- You can paste in a bullet list of facts and get back a paragraph that sounds like you.
- You stop noticing "this doesn't sound like me" as the dominant feedback.

**Estimated effort:** 1-2 hours initial setup, then ongoing refinement as a byproduct of normal work.

---

## Stage 2 — Context Expansion

**Goal:** The tool knows enough about your work, team, and ongoing projects to draft useful content without you having to explain everything from scratch.

**Where this lives:** Same Claude.ai Project, expanded with context documents.

### What to add

- **Team context:** Brief profiles of your direct reports and their work areas. What they're working on. Their growth goals. Their voice/style if drafting messages on their behalf.
- **Project context:** One-pagers on CIRRUS, GDEX, and any other ongoing initiatives. Architecture, stakeholders, status.
- **Stakeholder context:** Who's who in your org. HSG, AI Initiative, NWSC-4, executive contacts.
- **Recurring document templates:** Your standard formats for performance reviews, status updates, talk abstracts, etc.

### Workflow

- When you ask Claude to draft something, you can reference context naturally ("draft an update on Kevin's progress on the LLM hosting goal") and the tool has the underlying context loaded.
- Update context docs quarterly or after major changes.

### Success criteria

- You can ask for a draft about an internal topic without re-explaining background.
- Drafts include accurate names, project context, and stakeholder framing without prompting.

**Estimated effort:** 2-4 hours to build initial context docs, then quarterly updates.

---

## Stage 3 — Decision and Reasoning Capture

**Goal:** The tool starts to mirror not just how you write, but how you think and decide.

**Where this lives:** Same Project, with a new category of reference materials.

### What to capture

This is the hardest stage and the one most people skip. The idea is to capture your decision patterns:

- **Recorded thinking-out-loud:** When you make a non-trivial decision, record yourself explaining the reasoning (Voice Memos, then transcribe). What you considered. What you rejected. Why. Over time these become decision pattern examples.
- **Annotated past decisions:** Pick decisions you've made (org changes, technical choices, hiring calls, project priorities). Write up the context and your reasoning after the fact. "Here's what I decided and why" notes.
- **Counter-decisions:** Times you almost made one choice and went another way, and why. These are especially valuable because they show the actual decision boundary.

### Why this matters

A tool that sounds like you but makes decisions unlike you is worse than no tool. Stage 3 is what separates "drafting helper" from "actual digital extension."

### Workflow

- Once a week, spend 10 minutes recording or writing up a recent decision.
- Add notable ones to the project knowledge.

### Success criteria

- You can ask "how should I think about X" and the tool's reasoning matches what you'd actually consider.
- The tool can defensibly explain trade-offs the way you would.

**Estimated effort:** Ongoing, ~30 minutes per week.

---

## Stage 4 — Voice Prototype

**Goal:** A working voice agent that you can talk to, that responds in a synthesized version of your voice.

**Where this lives:** A managed voice agent platform (Vapi, Retell, or similar).

### Setup

1. **Voice cloning:** Record 30+ minutes of clean audio of yourself speaking (varied content, single speaker, no background noise). Upload to ElevenLabs Professional Voice Clone.
2. **System prompt:** Use the Voice Guide from Stage 1 plus a behavioral prompt for spoken interaction (shorter sentences, conversational pauses, no markdown).
3. **Context loading:** Pull in the most-used context from Stages 1-3 as the system prompt.
4. **Voice agent platform:** Configure Vapi or similar to use Claude API + your ElevenLabs voice + your system prompt. They handle the speech-to-text and real-time streaming.

### Use cases to validate

- Drafting emails out loud while driving or walking.
- Talking through a decision before a meeting.
- Preparing for a difficult conversation by rehearsing.
- Quick "what do I think about X" check-ins.

### Success criteria

- You actually use it more than once after the novelty wears off.
- The responses are useful enough to influence what you do next.
- The voice quality doesn't pull you out of the conversation.

**Estimated effort:** 1 weekend to prototype, ~$50-100 in API costs to validate.

**Important:** If anyone other than you ever talks to this agent, they need to know it's an AI version of you. Don't deploy it in any context where it could be mistaken for you.

---

## Stage 5 — Custom Build and Real Context Access

**Goal:** A tool you control fully, with access to your real work context (calendar, email, past reviews, ongoing projects).

**Where this lives:** A custom application you build, with MCP servers exposing your data sources.

### Trigger for moving to this stage

Move to Stage 5 when:
- You've used the Stage 4 prototype for at least a month.
- You're hitting specific limits ("if it could read my calendar this would be 10x more useful").
- The cost of building exceeds the cost of staying on a managed platform.

### Components

- **Frontend:** Web or mobile app where you interact with the agent (text and voice).
- **Backend:** Orchestrator that handles audio I/O, Claude API calls, and tool use.
- **MCP servers** for context access:
  - Email integration
  - Calendar integration
  - Past performance reviews and drafts
  - Project documentation
  - Team data
- **Voice pipeline:** Whisper for STT, Claude for reasoning, ElevenLabs for TTS.

### What this enables

- "Draft a response to that email from [person]" — and it knows the email, the relationship, the context.
- "What did I commit to in last quarter's planning?" — and it reads your past notes.
- "Help me prepare for tomorrow's 1:1 with Kevin" — and it pulls recent context.

### Realistic timeline

- Initial build: 2-4 weekends if comfortable with web development.
- MCP servers: 1 weekend each as needed.
- Don't build speculatively — build each integration when you hit a specific need.

---

## Stage 6 — Decision Boundaries

**Goal:** Clarity on what the tool should and shouldn't do.

This is less a build stage and more a continuous discipline. Worth thinking about now:

### Things the tool should do
- Draft anything you'd normally draft yourself.
- Help you think through decisions.
- Recall facts and context faster than you can.
- Prepare you for conversations and meetings.

### Things the tool shouldn't do
- Send messages on your behalf without your review (at least not until trust is very well established).
- Make commitments to people in your voice.
- Be exposed to anyone who might mistake it for actually being you.
- Make hiring, firing, performance, or financial decisions.
- Replace the human work of being present in conversations.

The 85% problem is real: a tool that sounds like you 85% of the time can be worse than no tool, because the 15% where it gets you wrong erodes trust. Keep the human in the loop until the failure mode of automation is genuinely acceptable.

---

## Appendix — Voice Guide

The Voice Guide has moved to [`knowledge/voice-guide.md`](knowledge/voice-guide.md) as the living document. The version originally drafted here is preserved there as the starting point and gets refined as new patterns surface.

---

## Next Steps

1. **This week:** Set up the Claude.ai Project. Add the four reference samples from this conversation. Drop in the Voice Guide.
2. **Next month:** Build context docs for Stage 2 — your team, your projects, your stakeholders.
3. **Ongoing:** For every draft you rework, save the before/after pair to the project.
4. **Decide later:** Whether and when to move to Stages 3-5.

The first stage alone is going to save you meaningful time on performance reviews next year, status updates, and any other recurring written communication. Everything after that is incremental.
