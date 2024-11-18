---
title: "SPIFFE the Easy Way: Universal X509 and JWT Identities Using cert-manager - Tim Ramlot & Ashley Davis, Venafi"
categories: ["KubeCon + CloudNativeCon North America 2024"]
---

## Abstract

SPIFFE is incredible. Each workload is assigned its own universal identity, simplifying the security and management of communications in distributed systems. While SPIRE (the reference SPIFFE implementation) is exceptionally powerful, it is also quite complex. Deploying SPIRE on Kubernetes requires StatefulSets, which can be challenging and frustrating. Many cloud vendors are starting to offer turnkey SPIFFE solutions, but that comes with risk of vendor lock-in. In this talk, we will demonstrate how to use the Cloud Native cert-manager solution to implement SPIFFE (x509 and JWT) with low operational overhead for all Kubernetes workloads. The session includes all you need to know to issue X.509 SVIDs, use them and validate them. Additionally, we will introduce an experimental solution to convert x509 SVIDs into JWT SVIDs. The demo will highlight how to authenticate to third-party APIs (such as AWS, GCP, Azure, and others) using these JWT SVIDs.

[Sched URL](https://kccncna2024.sched.com/event/f52c427fe74a8d5c59c8f47735caba2a)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/De2o-urGpQk' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
