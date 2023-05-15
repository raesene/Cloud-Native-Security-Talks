---
title: "Image Signing and Runtime Verification at Scale: Datadog's Journey - Ethan Lowman, Datadog"
categories: ["KubeCon + CloudNativeCon Europe 2023"]
---

## Abstract

The recent prevalance of software supply chain attacks has led to a flurry of new tools and approaches to secure the end-to-end integrity of container images, and image signing in open source is gradually reaching maturity through projects like SigStore. However, the path is largely uncharted for signing and verifying container images internally at scale. Internally, Datadog's engineering teams use a wide variety of languages and CI/CD configurations, constantly deploying images to tens of thousands of nodes across dozens of Kubernetes clusters, spanning multiple cloud providers and datacenters. To meet the challenges of this complex environment, we take a unique approach to image signing and verification. To ease adoption and maintenance of image signing across heterogenous build environments, we take a service-oriented approach, encapsulating cryptographic complexity within a gRPC signing service. For verification, motivated by both reliability and security, we buck the trend of using Kubernetes admission controllers, validating image signatures at runtime using an image verification plugin system we are contributing upstream to containerd. In this talk we discuss how we reached these designs, and share our experience operating this system in production.

[Sched URL](https://kccnceu2023.sched.com/event/4edae2493a4ef265096f524c0bfbf654)

## Video

<iframe src="https://www.youtube.com/embed/g7xgBzZ3t_A" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
