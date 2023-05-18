---
title: "Layers of Isolation in Kubernetes - Tim Allclair, Google"
categories: ["KubeCon + CloudNativeCon China 2018"]
---

## Abstract

How much isolation can you reasonably expect between two applications in the same cluster? Should every application have its own namespace? Every service? Between containers, pods, nodes, namespaces, and even clusters, it can be hard to know how to architect a secure system, and what layers of isolation can be depended on.  In this talk we will start at the bottom and build up. You will learn which resources are isolated between two containers in the same pod, and which are not. From there we will explore what changes as the workloads are increasingly separated. You will see examples of real-world attacks, and how these attacks are mitigated at different layers of the stack. By the end, you will have a better understanding of how workloads can and should be separated for your own threat models.

[Sched URL](https://kccncchina2018english.sched.com/event/3c36d8932d1663b217514cf6223c3547)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/dM0lyNmt2L8' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
