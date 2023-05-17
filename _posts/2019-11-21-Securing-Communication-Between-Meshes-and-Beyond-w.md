---
title: "Securing Communication Between Meshes and Beyond with SPIFFE Federation - Evan Gilman, Scytale & Oliver Liu, Google"
categories: ["KubeCon + CloudNativeCon North America 2019"]
---

## Abstract

One of the hottest features that Istio brings to the table is transparent, mutually-authenticated TLS between all workloads running on it. Under the covers, it relies on SPIFFE to provide the cryptographic identity that is used to perform this mutual authentication.SPIFFE relies on an authority to issue identity. In an Istio mesh, Istio Citadel (CA) issues certificates to workloads by default... but, what happens when you have more than one Istio mesh, and hence more than one Citadel? Or Istio workloads talking to external services?Enter SPIFFE federation. It allows SPIFFE identity issuers to peer with each other, enabling workloads in disparate domains to securely authenticate and communicate with each other. In this talk, we will describe the challenges involved here and how SPIFFE addresses them, as well as demonstrate SPIFFE federation between Istio mesh and SPIRE.

[Sched URL](https://kccncna19.sched.com/event/cec81509cf09a2ea0f275760b16cd2f1)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/cx_NnvbsCP4' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
