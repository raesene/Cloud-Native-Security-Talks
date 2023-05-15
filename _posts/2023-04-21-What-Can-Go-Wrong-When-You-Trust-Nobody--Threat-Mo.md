---
title: "What Can Go Wrong When You Trust Nobody? Threat Modeling Zero Trust - James Callaghan & Richard Featherstone, ControlPlane"
categories: ["KubeCon + CloudNativeCon Europe 2023"]
---

## Abstract

With the prevalence of cloud-native technologies continually growing, and organisations increasingly adopting multi-cloud and hybrid architectures, it has never been more important to discuss the principles of Zero Trust. In order to fully apply the philosophy of ‘never trust, always verify’, we must build systems with a sound understanding of the adversaries who may wish to compromise our data, how such a compromise could occur, and how we can protect ourselves by implementing proportionate, layered security controls. The foundation on which we can construct this ‘secure by design’ approach is threat modeling. In this talk, we will: - introduce the fundamental concepts of threat modeling, and how they can be applied to systems made up of many distributed cloud-native workloads; - demonstrate a simple system built using Zero Trust principles, with workloads running on an Istio service mesh within a Kubernetes cluster; - show how cryptographically strong workload identities can be provided by a SPIRE server; - demonstrate how Istio External Authorization can delegate layer 7 authorization decisions to OPA sidecars; - build our threat model and introduce controls following the Zero Trust philosophy, including a demonstration of custom signing and verification of OPA bundles.

[Sched URL](https://kccnceu2023.sched.com/event/c1e4ab10ff0b4c4ccf9cb3e2801c4a38)

## Video

<iframe src="https://www.youtube.com/embed/TiDf_KpJgTM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
