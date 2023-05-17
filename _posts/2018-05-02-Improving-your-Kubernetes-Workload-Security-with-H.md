---
title: "Improving your Kubernetes Workload Security with Hardware Virtualization - Fabian Deutsch, Red Hat & Samuel Ortiz, Intel (Intermediate Skill Level) (Slides Attached)"
categories: ["KubeCon + CloudNativeCon Europe 2018"]
---

## Abstract

On any given node, all Kubernetes workloads are running through software-only isolation. The security concerns related to that level of isolation could be mitigated by using hardware virtualization for both pods and traditional (legacy?) workloads. This talk will present two complementary approaches for doing so: Kata Containers and KubeVirt. We'll be describing how both projects leverage CPU virtualization to implement a stronger security architecture for Kubernetes. When combining both approaches, one can run a wider range of workloads, from untrusted containers through Kata Containers to more traditional, lift and shift applications with KubeVirt.

[Sched URL](https://kccnceu18.sched.com/event/3aefc430123da2e3adc1b6cf05335239)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/T_NxDXAdbfo' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
