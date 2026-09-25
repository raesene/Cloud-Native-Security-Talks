---
title: "Securing Multi-Cloud Cross-Cluster Communication with SPIFFE and SPIRE - Evan Gilman, Scytale, Inc."
categories: ["KubeCon + CloudNativeCon Europe 2019"]
talk_title: "Securing Multi-Cloud Cross-Cluster Communication with SPIFFE and SPIRE"
speakers: "Evan Gilman, Scytale, Inc."
event: "KubeCon Europe 2019"
series: "kubecon-eu"
event_code: "KC-EU-19"
year: 2019
youtube_id: "sLN11qAFAC4"
sched_url: "https://kccnceu19.sched.com/event/9b6dd91afedabf694a47035a653ff812"
---

Securing network traffic that traverses multiple software stacks and platforms is challenging. Difficulties involving platform-aware applications, supporting multiple authentication schemes, and maintaining complex authorization logic are all commonplace, despite the fact that we'd really rather avoid these things.  SPIFFE provides a platform-agnostic identity layer that can be used to authenticate and secure workload communication regardless of where the workload lives. AWS, Azure, and on-prem? Ok! Kubernetes, Mesos, and bare metal? No problem! SPIFFE allows you to mix and match without the need to worry about how workloads within them will securely communicate with each other.  In this talk, we will leverage SPIRE to demonstrate automated issuance of SPIFFE identity across disparate orchestrators and platforms, allowing for seamless authentication of systems within and between them.
