---
title: "Insights into Unsecured Kubernetes in the Wild - Jay Chen & Aviv Sasson, Palo Alto Networks"
categories: ["KubeCon + CloudNative North America 2021"]
---

## Abstract

As much as the cloud-native community devoted to building a rock-solid platform, the weakest link has always been the users who inadvertently introduced insecure configurations. Jay and Aviv will share their findings of misconfigured Kubernetes clusters in the wild and malware campaign that exploited these misconfigurations. Their research found 2,100 unsecured Kubernetes clusters that consist of 5,300 nodes, 31,340 CPUs, and 75,270 pods on the internet. Many sensitive data leaked from these clusters, including access credentials, source code, and PII. The researchers will share how they architected their honeypot infrastructure to collect and monitor malicious activities targeting Kubernetes environments. The research also uncovered the first malware that exploited Kubelets to compromise Kubernetes. The malware used sophisticated tactics to evade detection, harvest credentials, move laterally, and perform cryptojacking operations in compromised clusters.

[Sched URL](https://kccncna2021.sched.com/event/df26e5f2bfefb2709bc92a9387d41aa7)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/VGv32or8nmU' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
