---
title: "OIDC and Workload Identity in Kubernetes - Ashutosh Kumar, Elastic & Anish Ramasekar, Microsoft"
categories: ["KubeCon + CloudNative North America 2023"]
---

## Abstract

Traditionally, when applications running in Kubernetes pods need to access public cloud services, they would use service account credentials or other forms of authentication. Workload identity provides a convenient and secure way to manage access to Cloud (e.g. Google, Azure etc) resources from within Kubernetes by mapping the service account to the associated cloud provider service account. It eliminates the need for managing and distributing individual service account keys or credentials, improving the overall security posture of your applications. The speakers will walk through the concepts of workload identity on the following lines: (1) Explain how OpenID Connect is used to achieve workload identity and the authentication workflow for the same, (2) How to set up workload identity on public clouds for managed and unmanaged Kubernetes clusters for public clouds. They will also do a demo on how to set up workload identity with an example of Azure/Google public cloud.

[Sched URL](https://kccncna2023.sched.com/event/22d5cf560179c3ffad6000ff2be67b9f)

## Video

<iframe src="https://www.youtube.com/embed/r15iZ4WrpFQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
