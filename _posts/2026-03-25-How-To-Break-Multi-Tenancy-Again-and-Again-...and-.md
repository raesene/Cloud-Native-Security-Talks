---
title: "How To Break Multi-Tenancy Again and Again ...and What We Can Learn From It - Lorin Lehawany & Sven Nobis, ERNW"
categories: ["KubeCon + CloudNativeCon Europe 2026"]
---

## Abstract

Namespace-based multi-tenancy is challenging to implement and less effective than control-plane isolation. Thus, the latter is the standard today. But is this really true? Workloads such as machine learning, pipelines, or scripting capabilities can introduce unobvious multi-tenancy in clusters and become increasingly popular.   So the question is: How to isolate those workloads from each other securely? Pod Security Standards, Network Policies, and Admission Controller are well-adopted, but is it enough?   The answer is no: This talk presents real-world exploits in Kubeflow, Istio, and Traefik to bypass threat boundaries between namespaces and workloads.   Based on these examples, this talk presents a methodology for assessing complex environments with isolation problems and guides how to address them.

[Sched URL](https://kccnceu2026.sched.com/event/4c91dd5347986bdb6c6934c49252121a)

## Video

<iframe src="https://www.youtube.com/embed/PEU4uDzurvc" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
