---
title: "Zero Trust at Shopify Scale: Automating MTLS Across Thousands of Services - Dani Santos & Michelle Mali, Shopify"
categories: ["KubeCon + CloudNativeCon Europe 2025"]
---

## Abstract

Certificate management at scale presents critical challenges for securing service-to-service communication in zero trust architectures. We will demonstrate how Shopify automates mTLS across thousands of services, addressing certificate rotation without interruption, renewal failures, and cross-cluster distribution. Drawing from production experience, we'll explore our evolution from custom admission controllers to versatile patterns working across Kubernetes and non-Kubernetes environments, including mounting CA certificates at container startup with periodic Cronjob renewals. We'll share code examples for resilient rotation mechanisms, graceful certificate rollover, and RBAC. Attendees will learn practical patterns for scaling mTLS, with examples of monitoring certificate lifecycles and troubleshooting common failure modes.

[Sched URL](https://kccnceu2025.sched.com/event/9f16db022a3ec265e87ba5586aa2da1f)

## Video

<iframe src="https://www.youtube.com/embed/T-nN86wTebM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
