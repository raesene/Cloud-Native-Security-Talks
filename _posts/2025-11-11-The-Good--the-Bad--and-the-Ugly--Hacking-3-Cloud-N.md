---
title: "The Good, the Bad, and the Ugly: Hacking 3 Cloud Native AI Services With 1 Vulnerability - Hillai Ben-Sasson & Nir Ohfeld, Wiz"
categories: ["KubeCon + CloudNativeCon North America 2025"]
---

## Abstract

With rising demand for AI workloads, SaaS providers are evolving their K8s-based GPU offerings, often built on NVIDIA Container Toolkit: the industry-standard framework for running GPU-based containers. In this talk, we’ll show you how a single vulnerability in this fundamental framework impacted the entire cloud-native ecosystem – and how each environment handled a brand-new 0day.We’ll walk through our discovery of this Pod-to-Node escape vulnerability, and its impact across 3 different providers: Azure, DigitalOcean, and Replicate. Each case began with a weak Pod running our exploit – but outcomes varied widely. One led to minor impact; another with lateral movement that triggered blue teamers; and one with complete service takeover.Join us to gain a firsthand look on how major cloud-native companies build their K8s environments, and the anatomy of a container escape vulnerability in the wild. Finally, learn how to build stronger K8s guardrails by examining the flaws we exploited.

[Sched URL](https://kccncna2025.sched.com/event/a7d58f9388beca72d9f4314cd57731fe)

## Video

<iframe src="https://www.youtube.com/embed/ZTiWXqYg97U" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
