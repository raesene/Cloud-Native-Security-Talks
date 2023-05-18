---
title: "Introducing SPIFFE: An Open Standard for Identity in Cloud Native Environments [I] - Evan Gilman, Scytale"
categories: ["KubeCon + CloudNativeCon North America 2017"]
---

## Abstract

Modern infrastructure patterns like microservices, container orchestration, and hybrid/multi-cloud deployments have turned conventional models for datacenter authentication and security on their heads. In the face of highly dynamic compute and network resources, a new challenge has risen: how to authenticate and secure service-to-service traffic in this brave new world? Enter the problem known as service identity.  Getting service identity right is surprisingly hard, with requirements extending well beyond simple secret management. What kind of credentials to settle on, how to rotate them, how to automatically (and securely) bootstrap them... and even more importantly, how to make sure a wide variety of external systems can authenticate them appropriately? These questions represent only a subset of the points that must be solved for.  In this talk, we introduce both SPIFFE and SPIRE - a new open source project designed to solve exactly these problems. SPIRE, backed by the SPIFFE open standard, performs seamless node and workload attestation across various platforms, and automatically issue short-lived certificates based on those attestations in a controlled manner. Even better, these certificates work across organizational boundaries and heterogeneous environments thanks to SPIFFE, which introduces a standardized identity format and validation methodology for X.509 certificates.

[Sched URL](https://kccncna17.sched.com/event/776bd8551fdda807ee0fc392a49ad77a)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/ikmxZdZRTio' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
