---
title: "Mind the Gap! Bringing Together Cloud Services and Managed K8s Environments - Christophe Tafani-Dereeper, Datadog & Diego Comas, Sourcegraph"
categories: ["KubeCon + CloudNativeCon Europe 2023"]
---

## Abstract

Many organizations run Kubernetes as part of managed offerings such as AWS EKS, Azure AKS or GCP GKE. But that’s only one part of the story; other pieces of infrastructure such as databases, object storage or legacy workloads generally live outside the cluster. In this context comes the need to bridge the gaps between what runs inside a managed Kubernetes cluster, and what is deployed in other services of the cloud provider. In this talk, we start by reviewing how the different cloud providers tackle authenticating and authorizing humans to the managed Kubernetes control plane, as well as individual workloads to the cloud provider API. Then, we dive into the different techniques to bring external secrets (e.g., from AWS Secrets Manager) inside the cluster. Along the way we cover how practitioners can leverage these mechanisms to architect cloud-native applications that benefit from the full power of cloud services, while avoiding complete vendor lock-in. We also describe how an attacker can abuse these mechanisms to pivot from exploiting a single containerized workload to compromising full cloud environments, and how to best protect against these attack vectors.

[Sched URL](https://kccnceu2023.sched.com/event/23196f9c2a480b30b1bad8034a8dea60)

## Video

<iframe src="https://www.youtube.com/embed/5luByA7hakc" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
