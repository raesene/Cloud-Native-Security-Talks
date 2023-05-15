---
title: "CNI or Service Mesh? Comparing Security Policies Across Providers - Rob Salmond, SuperOrbital & Christine Kim, Google"
categories: ["CloudNativeSecurityCon North America 2023"]
---

## Abstract

Up or down the network stack? Kernel space or userland? How about a side order of sidecars? Would you like eBPF with that? The Cilium project began life concerned about enforcing policies at the CNI level, while Linkerd2 and Istio provided policy enforcement by way of sidecar injection. Now Cilium and Linkerd2 have added support for Layer 7 policies, while Istio has introduced a sidecarless model that pushes some of their policy enforcement out of the pod and back onto the node. And everyone is adding a pinch of eBPF for good measure! This talk will briefly summarize these technologies, explore recent changes in popular cloud native networking solutions, compare their implementations, and highlight the trade offs.

[Sched URL](https://cloudnativesecurityconna23.sched.com/event/b18bc8d74ce4b89be02a5770c03f68f3)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/L5UifNZCKhA' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
