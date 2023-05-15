---
title: "Spicing up Container Image Security with SLSA & GUAC - Ian Lewis, Google"
categories: ["CloudNativeSecurityCon North America 2023"]
---

## Abstract

Understanding and verifying the content of images that you deploy in production environments is difficult and error prone. Images could be built in an insecure environment, by a malicious actor, or include dependencies that are insecure. Users often don't have enough information to determine if images are trustworthy. Two new tools can help; Supply chain Levels for Software Artifacts (SLSA), and Graph for Understanding Artifact Composition (GUAC). In this talk attendees will learn how to add SLSA provenance metadata to their container images and strongly link images back to their source code on multiple build systems including GitHub Actions and Google Cloud Build. We will also cover how to verify images and their metadata before use; both when running locally and when running images in Kubernetes. Using policy engines like Kyverno and Sigstore policy-controller we can verify an image's source code repository, builder identity, build entry points, and more to protect production environments from malicious images. Finally we'll discuss how to understand your image's supply chain using GUAC. We'll discuss how we can combine SLSA with GUAC to better understand the contents and build provenance of your images from the base layers on down.

[Sched URL](https://cloudnativesecurityconna23.sched.com/event/e23128c94281acaa2b072c499cf6c94e)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/32IhwdAe0yI' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
