---
title: "Memory Armor for SPIRE: Fortifying SPIRE with Confidential Containers (CoCo) - Matthew Bates, Stealth Security Startup & Suraj Deshmukh, Microsoft"
categories: ["KubeCon + CloudNativeCon Europe 2024"]
---

## Abstract

SPIRE is a production-ready reference implementation of SPIFFE, a CNCF project for workload identity . In the SPIRE architecture, the SPIRE server holds considerable importance,hence securing and safeguarding it is critical. Security is never a done deal; following the principle of defense in depth, there is always a layer you can add to your systems . A lesser-known type of attack is where an adversary gains access to the host and tries to read the unencrypted memory of the application. With SPIRE server, this might mean access to highly sensitive signing keys for the trust domain. Confidential Containers (CoCo) is an emerging CNCF project that promises confidentiality for application memory. In this talk we will look at providing security to an essential frontier of the application - its memory. You will learn about the SPIRE trust model, CoCo and its ecosystem, and we will demonstrate how it can be used to protect SPIRE infrastructure and provide even further depths of security.

[Sched URL](https://kccnceu2024.sched.com/event/2f54dddbb1c1e63d77ac2bf0dda6e4d0)

## Video

<iframe src="https://www.youtube.com/embed/g0uBBGvf9w4" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
