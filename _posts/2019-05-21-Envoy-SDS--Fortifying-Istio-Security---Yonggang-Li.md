---
title: "Envoy SDS: Fortifying Istio Security - Yonggang Liu & Quanjie Lin, Google"
categories: ["KubeCon + CloudNativeCon Europe 2019"]
---

## Abstract

In Istio 1.1, Citadel Agent is introduced to dynamically provision x.509 certificates and private keys to workloads through the Envoy Secret Discovery Service (SDS) API. Running on Kubernetes nodes as DaemonSets and standalone on VMs, Citadel Agents improve security by making sure the generated private keys never leave the node and can be securely delivered to workloads via UDS. Citadel Agent also offers flexibility on local workload identity attestation and various adapters to integrate with custom CAs.In this talk we will demonstrate how SDS makes this model really efficient, and citadel working independently from other Istio components for both K8s and non-K8s workloads.

[Sched URL](https://kccnceu19.sched.com/event/2322814ecbe2d3cd24e1155dcef8317c)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/QlQyqCaTOh0' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
