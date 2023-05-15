---
title: "Armoring Cloud Native Workloads With LSM Superpowers - Barun Acharya, Accuknox"
categories: ["KubeCon + CloudNative North America 2022"]
---

## Abstract

Containers are not protected by default as the various tools for security into place provides perimeter security at the host, or the network and not necessarily the workload itself. LSMs(Linux Security Modules) provide with security hooks necessary to set up least permissive perimeter for various workloads. KubeArmor is a cloud-native runtime security enforcement system that leverages various LSMs to secure your workloads. LSMs are a really powerful system but they come with a high barrier of entry, steep learning curve and do not provide enough metadata for modern cloud native workloads. This talk will be about how KubeArmor leverages LSM superpowers to abstract away the complexities to help protect modern cloud native workloads, how we leverage eBPF to provide context about what's happening in the containers, how various kernel primitives fair with each to protect modern container workloads and what design considerations/challenges for integrating various LSM into KubeArmor.

[Sched URL](https://kccncna2022.sched.com/event/5c2faf35de9628291fb31986d4cde9b0)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/8jXuBelV3-0' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
