---
title: "DevOps All the Things: Creating a Pipeline to Validate Your OPA Policies - Goran Osim & Karpagam Balan, Booz Allen Hamilton"
categories: ["KubeCon + CloudNativeCon North America 2020 Virtual"]
---

## Abstract

Open Policy Agent is quickly becoming the de facto tool for applying configuration governance as code to your Kubernetes clusters. It can be challenging to understand how to optimize your workflows after finishing the getting started guide. This talk will focus on how to streamline the validation of your Rego policies using unit, mock, and integration testing to validate your OPA policy changes against your application manifests prior to applying these changes to production using OPA Gatekeeper. This talk will feature a live demo of using a combination of Rego unit tests, using your application’s Kubernetes manifests as input data to your OPA test suite, and using Terratest to perform end-to-end integration testing to apply your proposed policy changes to an ephemeral cluster orchestrated. Once validated, policy changes will be deployed using a GitOps strategy to a live cluster.

[Sched URL](https://kccncna20.sched.com/event/1ecd29ef9c1a4e2703a64c057f51630c)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/OTLow5yN34c' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
