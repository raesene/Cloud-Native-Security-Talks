---
title: "Secure Policy Distribution With OPA - Ash Narkar, Styra"
categories: ["KubeCon + CloudNativeCon North America 2020 Virtual"]
---

## Abstract

OPA can download bundles of policy and data from remote HTTP servers. Once the policies and data have been loaded, they are enforced immediately. But how does OPA know that these bundles are coming from a trusted source ? How does OPA verify the authenticity or integrity of the policies and data included in the bundle ? An attacker can potentially include corrupt policies and data in the bundle and OPA would end-up enforcing those policies, thereby compromising the entire system. In this talk, we will describe how OPA can assist in the secure distribution of policies and data by creating a “Signed Bundle” - a bundle that is digitally signed so that industry-standard cryptographic primitives can verify its authenticity. Our demo will show an end-to-end flow of generating and validating a “signed bundle” and also how this reduces OPA’s attack surface.

[Sched URL](https://kccncna20.sched.com/event/cd4ab24798a04c5eb9c057df4ae9ac35)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/IhP-dWGqwU8' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
