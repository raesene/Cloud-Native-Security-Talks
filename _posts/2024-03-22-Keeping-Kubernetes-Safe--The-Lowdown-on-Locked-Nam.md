---
title: "Keeping Kubernetes Safe: The Lowdown on Locked Namespaces - Marco De Benedictis, ControlPlane"
categories: ["KubeCon + CloudNativeCon Europe 2024"]
---

## Abstract

Kubernetes namespaces are widely used by developers and infrastructure maintainers to group resources within clusters, yet their role as pivotal security boundaries often gets overlooked. Many well-established and upcoming Kubernetes features rely on secure namespace management, from in-cluster DNS resolution to Network Policies, Limit Ranges, Pod Security Standards, and Gateway API Cross-Namespace Routing. The talk will investigate the implications of compromise within a cluster if an adversary successfully tampers existing namespaces or crafts new ones by delving into real-world use cases, including multi-tenancy and cluster-native policy enforcement. A spectrum of mitigations and best practices to lock down namespaces effectively will be presented, covering strategies from Role-Based Access Control (RBAC) to advanced object validation using admission controllers, including secure approaches with namespace templating in multi-tenant environments.

[Sched URL](https://kccnceu2024.sched.com/event/0f3638042442bf8d6fbc290f9128ef2a)

## Video

<iframe src="https://www.youtube.com/embed/8Zwftqf8g8w" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
