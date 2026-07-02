---
context: NSF biographical sketch — Synergistic Activities section (up to five examples of broader impact)
date: 2026-07-02
---

## Prompt

This was the Synergistic Activities section of Nick's NSF biographical sketch — not a self-evaluation. NSF asks each senior/key person for a one-page document listing up to five distinct examples that demonstrate the broader impact of their professional and scholarly activities, focused on the integration and transfer of knowledge as well as its creation. Named example categories include innovations in teaching and training, contributions to the science of learning, development or refinement of research tools, computational methodologies and algorithms for problem-solving, development of databases to support research and education, broadening the participation of groups underrepresented in STEM, international research collaborations, and national/international standards-development efforts.

Nick's opening ask was: "What are your initial thoughts of these examples for me?" After some back-and-forth, the assistant produced the version under "Claude's draft." Nick used it as inspiration and wrote his own version ("My revision") — it was not a line edit.

(The "Claude's draft" header is kept because it is the slot the Project reads as "avoid these patterns." The draft was produced by a separate AI assistant, not this Project.)

## Claude's draft

CIRRUS Platform Leadership. Hired specifically to lead CIRRUS, a cloud-native, Kubernetes-based research computing platform at NCAR, and directed its development from pilot through proof-of-concept into full production in May 2025. Built the technical team and GitOps-based operational discipline behind the platform, establishing it as a viable complement to NCAR's traditional HPC resources (Derecho, Casper) for long-running, always-on scientific workloads.

GDEX Migration. Led the migration of NCAR's GDEX data services and their databases from legacy VM infrastructure onto CIRRUS, coordinating directly with the GDEX team to containerize services, migrate databases, and execute a full production cutover. All services have run in production since September 2025, demonstrating the platform's readiness to support mission-critical, widely used NCAR data infrastructure.

RMACC Presentation. Presented on NCAR's on-premise, cloud-native research computing platform at the Rocky Mountain Advanced Computing Consortium (RMACC) symposium (2025), sharing CIRRUS's architecture and operational lessons with the broader regional research-computing community outside NCAR.

Technical Training Curriculum. Designed and delivered a recurring internal training curriculum introducing NCAR researchers to cloud-native computing and containerization — covering topics from running a Jupyter notebook as a containerized web service to CI/CD container builds with GitHub Actions and introductory Kubernetes/Argo CD using dev containers and GitHub Codespaces. Selected sessions are publicly recorded, and the curriculum has also been delivered directly to interns in NCAR's SIParCS summer program, mentoring at least six students in Kubernetes, GitOps, and CI/CD over the past two summers.

## My revision

I lead the team that manages the Kubernetes clusters known as CIRRUS at NSF NCAR. I was hired to lead this effort from inception as an on-premise cloud pilot, to a production system that has been running since May 2025. I helped build the technical team and architecture that provides a cloud native approach utilizing GitOps in order to create a platform that adheres to open science principles. CIRRUS is now established as a complement to NCAR's traditional HPC resources for long running, always available scientific workloads.

I was the technical product owner for the migration of NSF NCAR's RDA (Research Data Archive) to GDEX (Geoscience Data Exchange). I implemented a SCRUM methodology with the team to ensure we hit our end of fiscal year deadline to complete the migration. I helped the team better understand how to build containers, leverage CI/CD automation, and get a development version in place for testing before the cutover. We migrated 8 TBs of databases to a cloud native solution and cutover everything to GDEX in September 2025 with no downtime.

Presented on NCAR's on-premise cloud native research computing platform at the Rocky Mountain Advanced Computing Consortium (RMACC) in Boulder CO in May 2025, sharing CIRRUS's architecture and operational lessons with the broader regional research computing community outside NCAR.

Designed and delivered multiple internal training sessions which introduced NCAR researchers to cloud native computing and containerization by leveraging tools they were already familiar with (Jupyter Notebooks). These sessions built on top of each other to provide a gradual introduction into more advanced topics like building container images with GitHub Actions and adding Helm charts into Argo CD while navigating the Kubernetes API. Working through these training sessions has allowed me to understand the barriers to entry better and has led me to being more effective when working with over a half dozen SIParCS interns on introductions to Kubernetes and CI/CD.

## What changed

- Rewrote the headline-and-fragment CV style ("CIRRUS Platform Leadership. Hired specifically to lead...") into first-person prose ("I lead the team that manages..."). Kept the four distinct examples, but each in Nick's voice rather than as a labeled activity block.
- Dropped the bold section labels — plain prose, no headers.
- Cut marketing and editorializing: "viable," "full production," "mission-critical, widely used," "demonstrating the platform's readiness," "recurring... curriculum." The facts carry the weight instead.
- Replaced vague or imprecise specifics with the true ones only Nick knows: "GDEX data services" → "RDA (Research Data Archive) migrated to GDEX (Geoscience Data Exchange)"; "migrate databases" → "8 TBs of databases"; added "no downtime"; "(2025)" → "Boulder CO in May 2025."
- Removed specifics the AI added that didn't earn their place: "(Derecho, Casper)," "dev containers and GitHub Codespaces," "Selected sessions are publicly recorded."
- Corrected the technical detail to what actually happened: "introductory Kubernetes/Argo CD using dev containers" → "adding Helm charts into Argo CD while navigating the Kubernetes API."
- Surfaced the process the draft omitted: added the SCRUM methodology and the end-of-fiscal-year deadline that drove the migration.
- Credited the teaching approach, not just the topic list: started from tools researchers already knew (Jupyter) and built up gradually.
- Connected the activity to its broader impact — added what he learned and how it made him more effective with interns ("understand the barriers to entry better... more effective when working with interns"). That connection is exactly what the Synergistic Activities section asks for, and the draft left it out.
- Corrected the org name throughout: "NCAR" → "NSF NCAR."