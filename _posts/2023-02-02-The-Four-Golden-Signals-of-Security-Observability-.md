---
title: "The Four Golden Signals of Security Observability - Duffie Cooley, Isovalent"
categories: ["CloudNativeSecurityCon North America 2023"]
---

## Abstract

Migrating to Kubernetes has exposed significant gaps in the security observability of running workloads. This gap in visibility not only provides a major advantage to sophisticated threat actors; it provides a serious disadvantage to cluster operators as well. Without security observability, an attacker can achieve and maintain a persistent foothold in your cluster - indefinitely and invisibly. Observability tools today collect metrics and event data, but how do we provide insights into threat detection, or to help create a least-privilege security policy for your workloads? We’ll answer these questions by introducing the "Four Golden Signals of Security Observability." These signals are essential to understanding your cloud-native environment's behavior and include: 1. Process Execution 2. Network Sockets 3. File Access, and 4. Layer 7 Network Identity Using eBPF, we can provide native visibility in the kernel for your workloads and remove the visibility gap that cluster operators are challenged with by collecting security observability data. This talk will also provide a walkthrough of each of the "Four Golden Signals" to detect a real-world attack in real-time using eBPF-based open source tools, such as Cilium's Hubble and Tetragon.

[Sched URL](https://cloudnativesecurityconna23.sched.com/event/a778deb310797181d123a2cddcf68d63)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/BQIJo2Lahb4' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
