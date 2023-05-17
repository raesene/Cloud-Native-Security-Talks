---
title: "Securing Kubernetes with Trusted Platform Module (TPM) - Alex Tcherniakhovski & Andrew Lytvynov, Google"
categories: ["KubeCon + CloudNativeCon Europe 2019"]
---

## Abstract

TPM is a discrete tamper-resistant device soldered to the motherboard and it operates independently of its host.  TPM devices are designed to protect sensitive credentials at the hardware level: credentials created and stored within TPM devices cannot be extracted, even if host is compromised. Additionally, TPM devices provide a suite of cryptographic operations for applications to leverage.  In this demo heavy session, we will review core TPM capabilities and how they could be used in for extending Kubernetes security.   Attendees will leave with understanding how to utilize TPM in the context of Kubernetes. Concretely, the following scenarios will be covered: - Bootstrap trusted identity of cluster nodes  - Seal sensitive data  - Generate cryptographically protected logs - Generate unexportable TLS credentials

[Sched URL](https://kccnceu19.sched.com/event/29a844aba546e4393319fe0153f23e56)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/_kxmkI8Kc8Y' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
