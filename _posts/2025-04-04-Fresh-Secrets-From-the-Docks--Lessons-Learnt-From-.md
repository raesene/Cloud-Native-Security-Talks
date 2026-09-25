---
title: "Fresh Secrets From the Docks: Lessons Learnt From Analyzing 180,000 Public DockerHub Images - Guillaume Valadon, GitGuardian"
categories: ["KubeCon + CloudNativeCon Europe 2025"]
talk_title: "Fresh Secrets From the Docks: Lessons Learnt From Analyzing 180,000 Public DockerHub Images"
speakers: "Guillaume Valadon, GitGuardian"
event: "KubeCon Europe 2025"
series: "kubecon-eu"
event_code: "KC-EU-25"
year: 2025
youtube_id: "2r92tTuFYg8"
sched_url: "https://kccnceu2025.sched.com/event/c762760b6a40b1df87cd665de8a7b645"
---

Hardcoded secrets remain a common practice in containerized environments, often used for convenience during testing or deployment, despite their significant, well-known security risks.   Docker images are not immune and can inadvertently leak secrets through Dockerfiles, configuration files, or image layers. Once pushed to registries such as DockerHub, these secrets become discoverable to attackers, putting environments at risk.   In this session, we will share insights from an extensive analysis of 180,000 public Docker images retrieved from DockerHub, uncovering a staggering number of 35,000 secrets from 18,000 images. More than 6,000 of these secrets were valid when the study was conducted in late 2024, including AWS keys, GCP keys, OpenAI tokens, and GitHub tokens belonging to Fortune 500 companies.   Finally, we will discuss common misuses and pitfalls in Dockerfile files that lead to secrets being leaked, and describe best practices for handling secrets in Docker images.
