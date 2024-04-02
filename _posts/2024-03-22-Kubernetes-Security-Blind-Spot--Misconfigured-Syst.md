---
title: "Kubernetes Security Blind Spot: Misconfigured System Pods - Shaul Ben Hai, Palo Alto Networks"
categories: ["KubeCon + CloudNativeCon Europe 2024"]
---

## Abstract

Misconfigurations are a serious security threat to Kubernetes clusters - services with overly permissive permissions can allow an attacker to gain unauthorized access to the cluster, steal data, or deploy malicious code. The risk increases when we talk about misconfigurations in built-in features of cloud vendors - these features are often trusted by users and are not typically inspected for any security misconfigurations. Sometimes a certain misconfiguration is not necessarily a security issue that can affect our protected cloud environment. However, chaining several misconfigurations can lead to the creation of a strong exploit chain. In this talk, Shaul will discuss about Kubernetes security blind spot, System Pods, and the security consequences of a misconfiguration in those pods. He will demonstrate a real case study of a dual privilege escalation chain that was found in default configurations of GKE that allow attackers to gain unauthorized access to Kubernetes clusters.

[Sched URL](https://kccnceu2024.sched.com/event/59ad9d00efe770bbce81c1ff5bbe2a88)

## Video

<iframe src="https://www.youtube.com/embed/5scIQkclPfk" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
