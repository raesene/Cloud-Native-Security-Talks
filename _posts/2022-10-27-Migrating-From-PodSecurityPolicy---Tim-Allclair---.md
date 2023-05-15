---
title: "Migrating From PodSecurityPolicy - Tim Allclair & Sam Stoelinga, Google"
categories: ["KubeCon + CloudNative North America 2022"]
---

## Abstract

Pod Security Policy (PSP) has been completely removed in Kubernetes v1.25, making it essential for users to migrate their clusters before upgrading to v1.25. The good news is that the Pod Security admission controller, designed as a simpler successor to PSP, just graduated to stable. The bad news is that the migration is not always straightforward. In this talk, you will see the quick-and-dirty migration path, and then dive deep into the nuances and challenges of migrating off PSP. We will also explore a couple of alternatives to the Pod Security admission controller, and when and why you might choose those alternatives instead. The goal of this talk is to empower you to confidently and safely begin upgrading your clusters, and bid farewell to PSP.

[Sched URL](https://kccncna2022.sched.com/event/b4ca8d656626383b43be7e368578640c)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/OIQrp_LyFDk' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
