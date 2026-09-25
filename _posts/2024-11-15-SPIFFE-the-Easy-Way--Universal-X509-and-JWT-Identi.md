---
title: "SPIFFE the Easy Way: Universal X509 and JWT Identities Using cert-manager - Tim Ramlot & Ashley Davis, Venafi"
categories: ["KubeCon + CloudNativeCon North America 2024"]
talk_title: "SPIFFE the Easy Way: Universal X509 and JWT Identities Using cert-manager"
speakers: "Tim Ramlot & Ashley Davis, Venafi"
event: "KubeCon North America 2024"
series: "kubecon-na"
event_code: "KC-NA-24"
year: 2024
youtube_id: "De2o-urGpQk"
sched_url: "https://kccncna2024.sched.com/event/f52c427fe74a8d5c59c8f47735caba2a"
---

SPIFFE is incredible. Each workload is assigned its own universal identity, simplifying the security and management of communications in distributed systems. While SPIRE (the reference SPIFFE implementation) is exceptionally powerful, it is also quite complex. Deploying SPIRE on Kubernetes requires StatefulSets, which can be challenging and frustrating. Many cloud vendors are starting to offer turnkey SPIFFE solutions, but that comes with risk of vendor lock-in. In this talk, we will demonstrate how to use the Cloud Native cert-manager solution to implement SPIFFE (x509 and JWT) with low operational overhead for all Kubernetes workloads. The session includes all you need to know to issue X.509 SVIDs, use them and validate them. Additionally, we will introduce an experimental solution to convert x509 SVIDs into JWT SVIDs. The demo will highlight how to authenticate to third-party APIs (such as AWS, GCP, Azure, and others) using these JWT SVIDs.
