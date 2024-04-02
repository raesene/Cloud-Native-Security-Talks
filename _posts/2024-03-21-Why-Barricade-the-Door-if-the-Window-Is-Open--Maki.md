---
title: "Why Barricade the Door if the Window Is Open? Making Sense of Kubernetes Initial Access Vectors - Shay Berkovich, Wiz"
categories: ["KubeCon + CloudNativeCon Europe 2024"]
---

## Abstract

Upon creation of Kubernetes cluster, the immediate security concern should be securing initial access. To achieve that, one needs to be clear on many ways malicious actors can gain access to a cluster. But how do you wrap your head around API server and data plane access, management interfaces, anonymous access, image poisoning and more? Toss on top of that different methods of authentication for every managed service and you get yourself a headache. In this talk we make sense of K8s initial access methods. In each case we list prerequisites (misconfigurations, vulnerabilities, or likeliest way an attacker can obtain credentials), compromised role permissions (impact) and mitigations. On top of that, we map these vectors to the real-world attacks observed recently and demo the most interesting scenarios. More importantly, we talk about how the access events manifest in cloud and audit logs and kernel-level visibility, so that the attendees can leave with a coherent detection strategy.

[Sched URL](https://kccnceu2024.sched.com/event/bc8dbf3d52bcc92b0490ef5d23ecab94)

## Video

<iframe src="https://www.youtube.com/embed/aeOKwTDAxj4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
