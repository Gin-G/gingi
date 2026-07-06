---
context: Talk abstract — HH Seminar Series at MMM (CIRRUS overview), July 15 2026
date: 2026-07-06
---

## Prompt

Nick signed up for the HH Seminar Series at MMM (July 15) and the organizer asked for a title and short abstract. He attached his CIRRUS deck (CIRRUS-EOL-05192026.pptx) and asked the assistant to draft a reply based on the presentation. The assistant produced a title (taken from the deck) and the abstract below, delivered inside a short email reply. The abstract is the unit that was revised — the title and email wrapper are not the subject of this counter-example.

## Claude's draft

CIRRUS is the cloud native, Kubernetes-based research computing platform I lead at NSF NCAR. The original ask was for an on-premise cloud, but after interviewing people across the community the real need became clear: a place to host interactive web applications, run tutorial-specific JupyterHubs, stand up data access APIs, and run workflow management tools that don't fit on traditional HPC, all with highly available and flexible compute that sits close to the data and adheres to open science principles. This talk covers how CIRRUS works, from the container and GitOps foundation up through the architecture running on our clusters, and shows real examples in production today, including interactive visualizations, tutorial JupyterHubs, workloads migrated off legacy hardware, and GitHub Actions runners connected to over two dozen repositories with access to GPUs and data. I'll close with where CIRRUS is headed, from Open OnDemand integration and our role in the AI initiative to onboarding more of the community's workloads.

## My revision

CIRRUS is the cloud native, Kubernetes based research computing platform hosted by CISL for NSF NCAR. This talk introduces how CIRRUS works, covering the container and GitOps foundation up through the cluster architecture. It also showcases real production examples such as interactive visualizations, tutorial specific JupyterHubs, GitHub Actions runners, and other workflow ideas, intending to spark new ideas on how CIRRUS can complement existing resources and NCAR's science. It will close with discussions on CIRRUS's future direction, covering integration with Open OnDemand, CIRRUS's role in the AI initiative, and onboarding more of the community's workloads.

## What changed

- Dropped first person entirely — "I lead / our clusters / I'll close / our role" became impersonal ("hosted by CISL for NSF NCAR," "the cluster architecture," "It will close," "CIRRUS's role"). A public talk abstract is written about the talk, not in first person. This is the opposite direction from the NSF biosketch counter-example, where first person was correct — the register depends on the document.
- Cut the origin-story sentence ("the original ask was for an on-premise cloud... after interviewing the community the real need became clear..."). An abstract states what the talk covers, not the platform's backstory — that narrative belongs in the talk itself.
- Removed the concrete quantifier from the examples ("connected to over two dozen repositories with access to GPUs and data" → just "GitHub Actions runners"). Numbers and specifics stay in the substantive documents and in the talk; the abstract keeps the example list short.
- Added an audience-facing purpose ("intending to spark new ideas on how CIRRUS can complement existing resources and NCAR's science") plus "and other workflow ideas" — reframed the examples as idea-fuel tied to the listener's science, not a catalog of what runs on the platform.
- Added hosting context ("hosted by CISL for NSF NCAR") — situates the platform in its organization rather than crediting himself.
- Left compound modifiers unhyphenated ("Kubernetes based," "tutorial specific") — matches his open-compound style ("cloud native," "long running," "always available").
- Tightened wording and length ("architecture running on our clusters" → "cluster architecture," "covers" → "introduces"); overall length down about a third.
