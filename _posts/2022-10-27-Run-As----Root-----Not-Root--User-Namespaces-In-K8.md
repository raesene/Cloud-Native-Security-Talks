---
title: "Run As “Root”, Not Root: User Namespaces In K8s - Marga Manterola, Isovalent & Rodrigo Campos Catelin, Microsoft"
categories: ["KubeCon + CloudNative North America 2022"]
---

## Abstract

What if I told you that there's a bool you can set in your pod yaml that mitigates many CVEs out there? Not just any CVEs, but some HIGH and CRITICAL ones! This feature is coming to Kubernetes, thanks to user namespaces, and we'll tell you all about it.User namespaces is a kernel feature that isolates the user in the container from the one in the host. A process running as root in a container can run as a different (non-root) user in the host. This is a HUGE improvement: if a process escapes the container, the privileges on the host are significantly reduced. Furthermore, some capabilities are void and others are only valid inside the user namespace.Many container workloads that run as root today can benefit from this already: enable user namespace in their pod yaml and be more secure without additional changes.This talk will explain how to use this feature in your cluster, how it is implemented, the current state of the KEP and future work and challenges in this area.

[Sched URL](https://kccncna2022.sched.com/event/74f303be0d04d3c2426382828dd60441)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/uRp0YltujVE' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
