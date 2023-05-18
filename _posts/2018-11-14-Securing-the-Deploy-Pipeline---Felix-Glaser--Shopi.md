---
title: "Securing the Deploy Pipeline - Felix Glaser, Shopify"
categories: ["KubeCon + CloudNativeCon China 2018"]
---

## Abstract

Imagine taking arbitrary code, deploying it to production, and hoping everything is secure. When we don’t lock down our deployment pipelines and deploy arbitrary containers, we do exactly that. Join us to discover Shopify’s solution.  After a container is built, we run checks to determine its state: Is it free from vulnerabilities and outdated software? Does it originate from the correct deploy pipeline?  For every successful test, the container is signed and the signature stored in Grafeas. During deploy time, the Kritis admission controller enforces the presence of the signatures.  Because the security state of a container can change, we log the metadata created during a container’s lifetime; if it becomes vulnerable, it can be recalled, fixed, and redeployed.  With Grafeas and Kritis, two new tools join Kubernetes, allowing everyone to prevent privilege escalation via code deployment.

[Sched URL](https://kccncchina2018english.sched.com/event/525d3c280dbb98bf4f232e35d016a739)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/CZi9zV7OcyM' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
