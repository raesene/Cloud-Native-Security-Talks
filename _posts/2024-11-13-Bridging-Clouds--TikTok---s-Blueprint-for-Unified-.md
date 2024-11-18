---
title: "Bridging Clouds: TikTok’s Blueprint for Unified OIDC Access on Multi-Cloud Kubernetes - Naveen Mogulla, TikTok"
categories: ["KubeCon + CloudNativeCon North America 2024"]
---

## Abstract

As businesses embrace increasingly complex multi-cloud environments, managing access across diverse Kubernetes setups becomes paramount. At TikTok, we faced the challenge of unifying OpenID Connect (OIDC) access for Kubernetes clusters across GKE, EKS, OKE and on-prem clusters each providing different levels of support and integration. This talk will detail our journey to develop a scalable, centralized OIDC framework using a reverse proxy approach, ensuring seamless authentication and authorization across different cloud providers. We will discuss our architectural strategy, highlighting how we leveraged Envoy for request handling and dynamic configuration with external authorization filters to accommodate diverse OIDC implementations. Discover how TikTok overcame identifying OIDC discrepancies among providers to implementing a unified solution that not only simplifies k8s access management but also reinforces security and compliance across our global, multi-cloud infrastructure.

[Sched URL](https://kccncna2024.sched.com/event/ae744df5793743b9c1ae76d5ba8ad0b1)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/3flO98UANDU' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
