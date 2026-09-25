---
title: "Mind the Gap! Bringing Together Cloud Services and Managed K8s Environments - Christophe Tafani-Dereeper, Datadog & Diego Comas, Sourcegraph"
categories: ["KubeCon + CloudNativeCon Europe 2023"]
talk_title: "Mind the Gap! Bringing Together Cloud Services and Managed K8s Environments"
speakers: "Christophe Tafani-Dereeper, Datadog & Diego Comas, Sourcegraph"
event: "KubeCon Europe 2023"
series: "kubecon-eu"
event_code: "KC-EU-23"
year: 2023
youtube_id: "5luByA7hakc"
sched_url: "https://kccnceu2023.sched.com/event/23196f9c2a480b30b1bad8034a8dea60"
---

Many organizations run Kubernetes as part of managed offerings such as AWS EKS, Azure AKS or GCP GKE. But that’s only one part of the story; other pieces of infrastructure such as databases, object storage or legacy workloads generally live outside the cluster. In this context comes the need to bridge the gaps between what runs inside a managed Kubernetes cluster, and what is deployed in other services of the cloud provider. In this talk, we start by reviewing how the different cloud providers tackle authenticating and authorizing humans to the managed Kubernetes control plane, as well as individual workloads to the cloud provider API. Then, we dive into the different techniques to bring external secrets (e.g., from AWS Secrets Manager) inside the cluster. Along the way we cover how practitioners can leverage these mechanisms to architect cloud-native applications that benefit from the full power of cloud services, while avoiding complete vendor lock-in. We also describe how an attacker can abuse these mechanisms to pivot from exploiting a single containerized workload to compromising full cloud environments, and how to best protect against these attack vectors.
