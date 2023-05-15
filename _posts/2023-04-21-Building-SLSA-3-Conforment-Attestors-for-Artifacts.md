---
title: "Building SLSA 3 Conforment Attestors for Artifacts Generated on GitHub - Ian Lewis & Asra Ali, Google"
categories: ["KubeCon + CloudNativeCon Europe 2023"]
---

## Abstract

Supply chain Levels for Software Artifacts, or SLSA (salsa) is a security framework to reason about and improve the integrity of released artifacts. SLSA (slsa.dev) is seeing increased adoption, both from industry and open source projects. Besides released artifacts, SLSA provenance attestation may also be generated for other types of "artifacts", such as vulnerability scanner results, SBOMs, etc. This allows the generation of trustworthy supply-chain metadata about arbitrary artifacts. Implementing a SLSA compliant attestor is, however, hard work, and requires expertise in both SLSA and the underlying platform used to build it. Come to this talk to learn about a recent extension of the SLSA framework that allows you to wrap existing tools (in the form of a binary, a GitHub Action or a container) into a SLSA compliant attestor, with minimal effort. We will show how SLSA builders for several package managers, such as npm and maven, are implemented with this framework. We will also report the lessons learned and the challenges we faced, in the hope it will help others in the field. At the end of this talk, attendees will have enough background to make their tool attest to their output using SLSA provenance.

[Sched URL](https://kccnceu2023.sched.com/event/f4f10831dcb667e4629a4df79aa445b7)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/Aq3ND6xmkyU' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
