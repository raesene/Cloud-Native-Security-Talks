---
title: "From Bespoke To Bulletproof: SPIFFE/SPIRE With ESO for Enterprise Zero Trust - May Large & Ivy Alkhaz, State Farm"
categories: ["KubeCon + CloudNativeCon North America 2025"]
talk_title: "From Bespoke To Bulletproof: SPIFFE/SPIRE With ESO for Enterprise Zero Trust"
speakers: "May Large & Ivy Alkhaz, State Farm"
event: "KubeCon North America 2025"
series: "kubecon-na"
event_code: "KC-NA-25"
year: 2025
youtube_id: "EVbFeCipis8"
sched_url: "https://kccncna2025.sched.com/event/c6eb3d7f2c9053ff9258d7926198d621"
---

At State Farm, securing microservices across multi-cluster K8s environments demanded a robust zero-trust architecture. Our initial “bespoke” SPIFFE/SPIRE deployment provided workload identities but faltered under scale. To achieve enterprise-grade resilience, we transitioned to an HA nestedSpire architecture, enabling seamless integration with ESO for secure secret retrieval. This talk shares our journey, from debugging 500 errors in ESO’s webhook-based SecretStore to scaling SPIRE agents. We’ll detail how we configured nestedSpire for HA, integrated SPIFFE SVIDs with ESO’s webhook authentication, and automated secret rotation to remove credential leaks. Attendees will learn steps for deploying nestedSpire, troubleshooting common issues (like attestation failures). We’ll share lessons from our bespoke-to-bulletproof evolution. Whether you’re adopting SPIRE or optimizing an existing setup, this talk offers a blueprint for building scalable, secure zero-trust systems in Kubernetes.
