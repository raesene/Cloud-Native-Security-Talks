---
title: "Policy Engines for Kubernetes: Picking One Without Losing Your Mind - Nabarun Pal, Broadcom"
categories: ["KubeCon + CloudNativeCon Europe 2026"]
talk_title: "Policy Engines for Kubernetes: Picking One Without Losing Your Mind"
speakers: "Nabarun Pal, Broadcom"
event: "KubeCon Europe 2026"
series: "kubecon-eu"
event_code: "KC-EU-26"
year: 2026
youtube_id: "y5rrfSZBm1A"
sched_url: "https://kccnceu2026.sched.com/event/fb0ed098b1cf51eae85343720b2326af"
---

Enforcing Kubernetes policies sounds simple until you actually have to do it. Block privileged pods? Sure. Inject sidecars automatically? Easy, right? There's more to consider than you'd think.   This talk will explore the prominent options people use: native Validating/Mutating Admission Policies, Kyverno, OPA/Gatekeeper, Kubewarden. Each has its pros and makes different tradeoffs.   Native k8s policies need no extra services but require CEL knowledge. Kyverno uses simple YAML for validation and mutation. OPA offers maximum flexibility with Rego, but adds a learning curve. Kubewarden uses WebAssembly, allowing to write policies in any Wasm-compatible language and distribute via OCI registries.   We'll dig into performance at scale because that additional overhead matters when you're deploying 1000s of pods. I'll share lessons running them in production, beyond what usually doesn’t make it to elevator pitches. You'll leave knowing which engine fits your situation.
