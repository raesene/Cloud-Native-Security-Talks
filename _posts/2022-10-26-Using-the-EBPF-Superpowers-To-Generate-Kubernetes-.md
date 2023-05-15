---
title: "Using the EBPF Superpowers To Generate Kubernetes Security Policies - Mauricio Vásquez Bernal & Alban Crequy, Microsoft"
categories: ["KubeCon + CloudNative North America 2022"]
---

## Abstract

Kubernetes has several security mechanisms that can be used to secure your applications: - limit network connectivity with network policies - block some system calls with seccomp profiles - restrict access to some Linux capabilities in security contexts Defining those policies is difficult. It usually happens that the team defining them is not the one that created the application, hence they might not have a good enough view of the architecture to know how to write them. We will present and demo different ways to automatically generate the 3 different kind of policies mentioned above by monitoring the application's events with the following eBPF-based tools: - Inspektor Gadget - Kubernetes Security Profiles Operator - oci-seccomp-bpf-hook We'll discuss the limitations of this approach and the future ahead of these tools. Finally, we will explain how applications can be audited to see if the security policies are respected.

[Sched URL](https://kccncna2022.sched.com/event/4094ebef89a6cbc7b7929fbc6aad68d0)

## Video

<iframe src="https://www.youtube.com/embed/3dysej_Ydcw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
