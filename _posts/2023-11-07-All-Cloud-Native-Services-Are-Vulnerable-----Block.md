---
title: "All Cloud-Native Services Are Vulnerable — Block Exploits with Security Behavior Analytics - David Hadas, IBM Research & Roland Huß, Red Hat"
categories: ["KubeCon + CloudNative North America 2023"]
---

## Abstract

It's known that no service is immune to vulnerabilities, even when following the best security practices. This demands a shift in our approach – we need robust methods that can block existing exploits, future exploit mutations, exploits developed immediately after a CVE is published, and even exploits of vulnerabilities we are unaware of. This talk introduces how Security Behavior Analytics (SBA) technology can detect exploit delivery sent during client interactions. Guard, a CNCF Knative component running on Kubernetes, uses SBA to detect unusual behavior that indicates potential exploit delivery. Guard applies Machine Learning (ML) to establish per-service criteria and does not rely on specific signatures that can be outdated or missed. We cover the benefits and disadvantages of using SBA with ML. We demonstrate Guard in action, blocking an actual exploit, and discuss security operations in production, and the relationship with Zero-Trust Architecture.

[Sched URL](https://kccncna2023.sched.com/event/dcbbedd737f2f6f34f421552646a6022)

## Video

<iframe src="https://www.youtube.com/embed/3-0zVtWqwCE" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
