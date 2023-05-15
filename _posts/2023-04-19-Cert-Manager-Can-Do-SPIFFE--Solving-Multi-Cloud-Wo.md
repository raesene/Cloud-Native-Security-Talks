---
title: "Cert-Manager Can Do SPIFFE? Solving Multi-Cloud Workload Identity Using a De Facto Standard Tool - Thomas Meadows, Jetstack & Joshua Van Leeuwen, Diagrid"
categories: ["KubeCon + CloudNativeCon Europe 2023"]
---

## Abstract

If you’re like me, your Kubernetes journey started well. Booting up a cluster and deploying a demo application, only to find the dreaded “Your connection is not private” message in your web browser. Attackers could be stealing your information, credit cards and passwords? Frankly, your sock shopping addiction should be nobody's business. Luckily I found the cert-manager project. As if by magic, this clever controller made my security woes fold away. What about secrets? API and service account keys. This highly sensitive data must be bolted to your pod to ensure it can access databases, api-servers and more. After accidentally committing raw secrets to Github (nobody got time for that), I grew tired. I crawled away into the wonders of Google Cloud Workload Identity. But wait? Haven't I given up on the wonder of multi-cloud Kubernetes? If only identity could come batteries included. As an encore in the machine identity space, cert-manager now leverages SPIFFE to solve this problem. Pods are empowered to enter the VIP lounge of their choice in whatever cloud, provided they are on the guest list. Don't believe me? Call me on my bluff. Join me as I explore how this industry problem has been solved using the same magic that gave us TLS on Kubernetes only a few short years ago.

[Sched URL](https://kccnceu2023.sched.com/event/4d185617132e16b85a65903e0ff08382)

## Video

<iframe src="https://www.youtube.com/embed/Z7WSo-K0xuA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
