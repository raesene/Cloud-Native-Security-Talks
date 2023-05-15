---
title: "Rotate Roots Right Round: Using Cert-Manager for Safer Private PKI - Ashley Davis, Jetstack"
categories: ["KubeCon + CloudNativeCon Europe 2023"]
---

## Abstract

There are plenty of benefits when you control your own certificate authority (CA), whether for just one Kubernetes cluster or for your whole organization. Putting a service mesh into production might require rolling your own CA, for example, but there are other use cases where a private PKI makes sense to avoid the headaches of rate limits, issuance costs or relying on third party services. Luckily for us, the concepts behind Public Key Infrastructure (PKI) have been around since at least the 70s and there are there's a tonne to learn from existing PKI deployments which we can apply to today's cloud native landscape. Plus, cert-manager is here to help! In this talk we'll discuss how to use cert-manager to safely deploy a private PKI at organizational scale and some the things we need to think about to ensure that we can run it safely - without causing a major outage down the road by failing to plan for rotation! Ash is a public key cryptography nerd with prior experience in administering PKI at large scale. As a cert-manager maintainer he's committed to improving the experience of anyone that runs private PKI in cloud native projects and beyond!

[Sched URL](https://kccnceu2023.sched.com/event/83986e253027b0fa76b03d95a07ad3f5)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/uvL7SHhVKUY' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
