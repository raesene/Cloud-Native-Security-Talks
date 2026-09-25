---
title: "Envoy SDS: Fortifying Istio Security - Yonggang Liu & Quanjie Lin, Google"
categories: ["KubeCon + CloudNativeCon Europe 2019"]
talk_title: "Envoy SDS: Fortifying Istio Security"
speakers: "Yonggang Liu & Quanjie Lin, Google"
event: "KubeCon Europe 2019"
series: "kubecon-eu"
event_code: "KC-EU-19"
year: 2019
youtube_id: "QlQyqCaTOh0"
sched_url: "https://kccnceu19.sched.com/event/2322814ecbe2d3cd24e1155dcef8317c"
---

In Istio 1.1, Citadel Agent is introduced to dynamically provision x.509 certificates and private keys to workloads through the Envoy Secret Discovery Service (SDS) API. Running on Kubernetes nodes as DaemonSets and standalone on VMs, Citadel Agents improve security by making sure the generated private keys never leave the node and can be securely delivered to workloads via UDS. Citadel Agent also offers flexibility on local workload identity attestation and various adapters to integrate with custom CAs.In this talk we will demonstrate how SDS makes this model really efficient, and citadel working independently from other Istio components for both K8s and non-K8s workloads.
