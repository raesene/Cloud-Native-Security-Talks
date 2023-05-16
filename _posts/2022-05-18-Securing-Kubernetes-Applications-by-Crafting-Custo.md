---
title: "Securing Kubernetes Applications by Crafting Custom Seccomp Profiles - Sascha Grunert, Red Hat"
categories: ["KubeCon + CloudNativeCon Europe 2022"]
---

## Abstract

Applying seccomp profiles to Kubernetes workloads is one of the most efficient ways in securing containers. The profiles have to be created with care and need to be maintained over the complete lifecycle of the application. This manual effort causes that many applications either stick to the runtime default profile or turn the feature off at all. In this talk, Sascha will demonstrate how to create a custom seccomp profile for a specific containerized application. It will cover the basic techniques of collecting the required syscalls by hand, and also advanced ways of utilizing eBPF and automatic audit log tracing. The session will also discuss the drawbacks of relying on automations. In the end, Sascha will show how to create multi architecture profiles and utilizes in-cluster enhancements like the Security Profiles Operator to create an application specific profile. Join this talk to learn more about seccomp in Kubernetes and how to secure your applications!Click here to view captioning/translation in the MeetingPlay platform!

[Sched URL](https://kccnceu2022.sched.com/event/5004b063bcf5cab2b637dfd5dfedd9dd)

## Video

<iframe src="https://www.youtube.com/embed/alx38YdvvzA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
