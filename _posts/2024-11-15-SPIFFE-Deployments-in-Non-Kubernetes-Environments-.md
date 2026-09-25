---
title: "SPIFFE Deployments in Non-Kubernetes Environments - Nadin El-Yabroudi & Eli Nesterov, SPIRL"
categories: ["KubeCon + CloudNativeCon North America 2024"]
talk_title: "SPIFFE Deployments in Non-Kubernetes Environments"
speakers: "Nadin El-Yabroudi & Eli Nesterov, SPIRL"
event: "KubeCon North America 2024"
series: "kubecon-na"
event_code: "KC-NA-24"
year: 2024
youtube_id: "sflwuM_baG4"
sched_url: "https://kccncna2024.sched.com/event/43726c572a5c29c47fce104a02591fb9"
---

The SPIFFE ideology is that workloads running in all types of environments can be issued an identity. However, in practice most deployments have focused on workloads in Kubernetes and there are few examples of SPIFFE being used in non-cloud native environments. In this talk we’ll explore SPIFFE deployments on a Linux environment. What does attestation for these types of workloads look like? How can you provide an identity to a bash script that cannot open a socket connection to the Workload API? We’ll focus on describing some of the existing challenges to non-Kubernetes SPIFFE deployments and provide some ideas for how to solve them.
