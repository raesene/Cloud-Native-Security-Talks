---
title: "IAM on Hybrid Cloud: Next Generation Security Model to Create an Interoperable Cloud [I] - Jeyappragash JJ & Kamil Pawlowski, padme.io"
categories: ["KubeCon + CloudNativeCon North America 2017"]
---

## Abstract

Those developing and operating modern software infrastructure face a myriad of complexity when trying to secure it.  While environments like amazon have vastly simplified the supply chain associated with brining up new physical and virtual infrastructure or services, complexity around managing access to and between these services has grown, and continues to expand.  The proliferation of configurations, management tools, and management schemes that exists in the modern datacenter has exploded when dealing with multi-cloud, hybrid (cloud + dc), or legacy systems.
Complexity is the enemy of security.  This heterogeneity is its embodiment. Having many different ways to configure access policies on different cloud providers or with different vendors, makes it impossible to understand whom has access to what in any given infrastructure.  Without this visibility it is impossible to have intelligibility, and hence security.  
Worse, today developers and operators must exist in and support a highly dynamic service environment.  That is to say existing services must evolve to support new functionality, and new services must be rapidly brought on line to support features in a highly competitive business environment.  The miasma of different configuration schemes creates a great deal of friction against this, and impedes security because it is difficult to holistically understand the impact of changes (let alone make them rapidly).  Security must be able to accommodate this temporality.
In this talk we introduce PADME as an architecture for policy admission aimed at solving these problems in a distributed environment.  PADME operates by normalizing access policy information across underlying clouds and system.  It allows policies to be operated up as known fixed building blocks in order to establish end to end security.  Finally, it attacks the problem of policy distribution in a distributed environment so that assertions can be made about the security of a system over time, and in the face of CAP theorem issues.

[Sched URL](https://kccncna17.sched.com/event/0d4f0a83629e0d236b14b7df75a8f28a)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/nXcXssv1rUs' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
