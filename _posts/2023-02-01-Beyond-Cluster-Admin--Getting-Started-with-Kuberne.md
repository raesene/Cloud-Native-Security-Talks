---
title: "Beyond Cluster-Admin: Getting Started with Kubernetes Users and Permissions - Tiffany Jernigan, VMware"
categories: ["CloudNativeSecurityCon North America 2023"]
---

## Abstract

We've all done it: working on our Kubernetes clusters with "cluster-admin" access, the infamous equivalent of "root". It makes sense when we're just getting started and learning about Pods, Deployments, and Services and we're the only one accessing the clusters anyway; but soon enough, we have entire teams of devs and ops and CI/CD pipelines that require access to our precious clusters and namespaces. Are we going to YOLO and give them our admin certificate, token, or whatever else we use to authenticate? Hopefully not! In this talk, we're going to look at how to implement users and permissions on a new Kubernetes cluster. First, we'll review various ways to provision users, including certificates and tokens. We'll see examples showing how to provision users in both managed and self-hosted clusters, since the strategies tend to differ significantly. Then, we'll see how to leverage RBAC to give fine-grained permissions to these users. We'll put emphasis on repeatability, seeing each time how to script and/or generate YAML manifests to automate these tasks.

[Sched URL](https://cloudnativesecurityconna23.sched.com/event/ed98538bcaf2853ebf002728569e9df3)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/GUmot7xrY3g' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
