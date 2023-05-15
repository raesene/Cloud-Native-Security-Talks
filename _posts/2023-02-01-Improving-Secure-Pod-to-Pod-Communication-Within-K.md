---
title: "Improving Secure Pod-to-Pod Communication Within Kubernetes Using Trust Bundles - Thomas Edward Hahn, TCB Technologies, Inc & Mark Hahn, Qualys"
categories: ["CloudNativeSecurityCon North America 2023"]
---

## Abstract

New features are being added to Kubernetes which allow for roots of trust to be specified for applications on a cluster. These mechanisms are being added as “trust bundles” (or trust anchor sets). We demonstrate the updates to our previous work in creating convenient mechanisms to provide certificates to every pod, allow pods access to them and use them for mutual authentication. Our work leverages work being done by the cert-manager project, the SPIFFE project and KEP-3257 for trust anchor sets to automate the creation of TLS certificates for every pod and establish patterns for mTLS. Finally, we compare and contrast this to current methods for providing cluster communication security (service meshes) and present areas for refinement. This is a significant rework of our previous presentation and software to work with changes to the Kubernetes Ecosystem as the concepts have been refined and evolved.

[Sched URL](https://cloudnativesecurityconna23.sched.com/event/e788f39e3daa046848fbd397b3c6849f)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/hPVOl111R-M' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
