---
title: "Demonstration of Automatic Kubernetes Network Policies Generation - Boaz Michaely, Red Hat & Adi Sosnovich, IBM Research"
categories: ["KubeCon + CloudNativeCon North America 2025"]
---

## Abstract

Kubernetes networking by default is Malicious Actors’ heaven.Why? Because by default, any pod can send and receive traffic to and from any other pod, ignoring namespace and privilege boundaries. External traffic in both directions is allowed as well, as far as Kubernetes is concerned.Indeed, best practices rightfully dictate that this default be modified, using "Kubernetes Network Policies" .Yet most teams find this too difficult to implement.Authoring NetworkPolicy YAML is very challenging.Baseline/AdminNetworkPolicy fills a gap for cluster administrators, but authoring these policies and understanding their impact is a new, additional challenge.Furthermore, policy authors may not know what the application’s communication needs are.What if there was a way to automatically produce tight network policy rules, in YAML, and see the impact of applied B/ANP network policies?Join this session to see the magic yourself, and learn how you can leverage this technology today!

[Sched URL](https://kccncna2025.sched.com/event/e90814e6c4b2e7a73f590da3f17d68b1)

## Video

<iframe src="https://www.youtube.com/embed/MD9f9Y-kems" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
