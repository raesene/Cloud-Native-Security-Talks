---
title: "From Observability to Enforcement: Lessons Learned Implementing eBPF Runtime Security - Anna Kapuścińska & Kornilios Kourtis, Isovalent"
categories: ["KubeCon + CloudNativeCon North America 2024"]
talk_title: "From Observability to Enforcement: Lessons Learned Implementing eBPF Runtime Security"
speakers: "Anna Kapuścińska & Kornilios Kourtis, Isovalent"
event: "KubeCon North America 2024"
series: "kubecon-na"
event_code: "KC-NA-24"
year: 2024
youtube_id: "Hw469I5GKmY"
sched_url: "https://kccncna2024.sched.com/event/feed2a6eace40035acd26adf11b6d0b0"
---

eBPF is getting widely adopted in cloud native runtime security tools like Falco, KubeArmor, and Tetragon. Using eBPF we can collect relevant security events right in the kernel and pass them to Security Engineers for retroactive attack detection and response. Having reliable and complete visibility is great, but wouldn't it be even better to proactively prevent attacks in progress? This talk covers the Tetragon team’s experience moving from security observability to enforcement and lessons learned along the way: from defining security models to hardening interactions between the local kernel and distributed Kubernetes systems. It will deep dive into how eBPF-based enforcement works, why it differs from observability, and the challenges of implementing it. The audience will walk away understanding the inner workings and common pitfalls of eBPF-based runtime security.
