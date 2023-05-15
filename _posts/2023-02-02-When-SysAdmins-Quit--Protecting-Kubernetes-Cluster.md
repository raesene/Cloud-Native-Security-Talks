---
title: "When SysAdmins Quit: Protecting Kubernetes Clusters When the Owner of Multiple Admin KUBECONFIGs Quits - Arun Krishnakumar, VMware"
categories: ["CloudNativeSecurityCon North America 2023"]
---

## Abstract

Suppose there is a sysadmin who owns a few dozen Kubernetes Clusters. They have access to the VMs of the cluster. They also naturally have access to the admin KUBECONFIG files to each of the clusters. Suppose they quit and make a copy of these KUBECONFIG files. If the api-server of any of the clusters is accessible, there is a serious problem. Suppose there is a non-admin KUBECONFIG user and suppose they quit or change teams. We have a similar requirement of removing access to the cluster for that user as well. These are real world problems that are faced by customers who want us to provide guidance and best practices in this matter. Ideally we would like to revoke access to these users with minimal interruption to the cluster. In this talk we will discuss the problem of revoking access to clusters in general at both the admin level, and at the user level. This will include removal of access to resources of interest and the parts of the certificate chain-of-trust that need to be changed. We will discuss how our customers can make use of these schemes and cleanly remove users from the cluster. We will also discuss pre-requisites for setting up a cluster that is amenable to the solution, general gaps in our current implementation and in the general Kubernetes ecosystem as well.

[Sched URL](https://cloudnativesecurityconna23.sched.com/event/20d71e54d1984443b7886693405edc5c)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/arWcFwwGNbw' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
