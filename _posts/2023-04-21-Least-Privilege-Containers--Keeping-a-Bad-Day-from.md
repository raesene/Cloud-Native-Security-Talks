---
title: "Least Privilege Containers: Keeping a Bad Day from Getting Worse - Greg Castle & Vinayak Goyal, Google"
categories: ["KubeCon + CloudNativeCon Europe 2023"]
---

## Abstract

“Don’t run containers as root”. The K8s security community has been saying this for years. There’s tools that can detect these types of misconfigurations. But detection, and knowing you have a problem, is just the start of the journey. How do you actually fix it? What can you do if those permissions are required for the container to work?We’ve run multiple de-privileging efforts for production containers. In 2020 we focused on converting containers from running as root to running as unprivileged users. In 2021 we moved containers to minimal distroless images. For some containers the solution was as simple as removing unused permissions. But sometimes we needed to do something more drastic, like charge the design of the container to segment out powerful permissions, or split functionality out into initContainers. We’ll share how we approached these tasks, what we learned working through problems with container owners, and describe how we put checks in place to prevent new privileged containers from appearing in the future.

[Sched URL](https://kccnceu2023.sched.com/event/eae7820102541e443e8fcb9a5e18ad14)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/uouH9fsWVIE' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
