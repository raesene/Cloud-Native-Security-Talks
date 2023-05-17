---
title: "Using eBPF to Bring Kubernetes-Aware Security to the Linux Kernel - Dan Wendlandt, Isovalent"
categories: ["KubeCon + CloudNativeCon Europe 2019"]
---

## Abstract

eBPF is a powerful Linux kernel technology that has recently become available in mainstream Linux distributions, enabling radically deeper visibility into and control over many aspects of operating system behavior.   In this talk, we will cover the basics of eBPF and then dive into a hands-on exploration of use cases where eBPF-based technologies like Cilium and BCC can enable security visibility and isolation well beyond what is possible with traditional Linux security primitives, Examples include:   1. Auditing the set of syscalls made by users who access pods via "kubectl exec".  2. Network visibility and access control that distinguishes between a sidecar and primary container inside a single pod.  3. API-layer visibility into inter-service connectivity, even if the connection is encrypted using TLS.

[Sched URL](https://kccnceu19.sched.com/event/2692b58cd8b2a0f97ae704b3c4f20112)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/7PXQB-1U380' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
