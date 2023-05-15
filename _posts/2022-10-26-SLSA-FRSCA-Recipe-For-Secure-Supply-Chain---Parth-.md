---
title: "SLSA FRSCA Recipe For Secure Supply Chain - Parth Patel & Michael Lieberman, Kusari"
categories: ["KubeCon + CloudNative North America 2022"]
---

## Abstract

There are multiple tools out in the ecosystem trying to deal with parts of the software supply chain threat but what does an end-to-end solution look like? The OpenSSF - FRSCA is an implementation of the CNCF best practices that aims to protect the build system, secure ingestion and enforce policy in the production environment to minimize the attack vectors associated with software supply chain. With the integration of Tekton Pipelines/Chains, Sigstore, SPIFFE/SPIRE, and Kyverno, we can create a holistic approach that can meet SLSA Level 3 from beginning to end. Utilizing CUE, admission controller and short-lived certificates, we can cryptographically and based on policy protect the cluster. Building off binary authorization, FRSCA can validate the signature and attestation to authorize until the next release cycle. FRSCA aims to be an implementable architecture that the open source community and end-user organizations can utilize to ingest and produce SLSA compliant artifacts.

[Sched URL](https://kccncna2022.sched.com/event/6095274e8dea0d5ad1ac691f98f0e40a)

## Video

<iframe src="https://www.youtube.com/embed/pZzQHLPNh-U" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
