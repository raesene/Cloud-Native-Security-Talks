---
title: "Living off the Land Techniques in Managed Kubernetes Clusters - Ronen Shustin & Shay Berkovich, Wiz"
categories: ["KubeCon + CloudNativeCon Europe 2024"]
talk_title: "Living off the Land Techniques in Managed Kubernetes Clusters"
speakers: "Ronen Shustin & Shay Berkovich, Wiz"
event: "KubeCon Europe 2024"
series: "kubecon-eu"
event_code: "KC-EU-24"
year: 2024
youtube_id: "aAxl90o910g"
sched_url: "https://kccnceu2024.sched.com/event/eb153ab17151b29bfa74177e8e2c7cd1"
---

Managed Kubernetes services offer the luxury of leveraging K8s without the burdens of control plane maintenance. But this convenience comes with compromises – notably, a reduction in control and, more critically, the introduction of CSP-specific cluster middleware that expands attack surface. This includes elements like DaemonSets, DNS services, and integral system processes in worker node images. Recently-issued CISA guidance on LotL techniques recognizes the problem and offers a solution directions, albeit in a general cloud and on-prem environments. In this talk, we demonstrate a series of LotL techniques that, in the absence of other methods, utilize middleware functionality to elevate RBAC privileges, move laterally, bypass security controls, evade detections, and cause a headache to security teams that often can't differentiate between legitimate component and malicious behavior. Examples include abusing fluent-bit for PI exfiltration; achieving cluster admin via an obscure system node-problem-detector host service; leveraging webhooks for persistency etc. We establish taxonomy, talk about the techniques in the context of CISA guidance, and map them onto the K8s threat matrix.
