---
title: "Stop Leaking Kubernetes Service Information via DNS! - John Belamaric, Google & Yong Tang, Ivanti"
categories: ["KubeCon + CloudNativeCon Europe 2024"]
---

## Abstract

Most Kubernetes distributions implement role-based access control (RBAC) to keep nosy users from poking around in other people’s applications. Well, maybe for more serious reasons than that, since a fundamental principle of security is keeping information “need to know”. What cluster administrators may not realize is that even when visibility is tightly restricted by RBAC in the Kubernetes API, it is completely unrestricted in DNS! By default, the Kubernetes DNS specification exposes all services to all clients via DNS. In this talk, you will learn how to use CoreDNS to fix that…and why you may not want to!

[Sched URL](https://kccnceu2024.sched.com/event/6f243abc3125fd0e1a3c15544b4e129b)

## Video

<iframe src="https://www.youtube.com/embed/Nfc4CiLUxUU" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
