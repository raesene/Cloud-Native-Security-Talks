---
title: "Building a Secure, Multi-Protocol and Multi-Tenant Cluster for Internet-Facing Services [A] - Bich Le, Platform9"
categories: ["KubeCon + CloudNativeCon North America 2017"]
---

## Abstract

Exposing internal HTTP-based services to the Internet is a well supported and documented feature of Kubernetes. What's less well understood is how to do it for thousands of services running on behalf of hundreds of possibly competing customers, in particular how to do it securely, protect the privacy of each customer, and support binary protocols other than HTTP. This is the problem that our company solved for our SaaS business which requires hosting and operating the control plane of popular infrastructure management software (e.g. Openstack, Big Data, and Kubernetes itself) as a service for our customers. Those control planes contain services exposing protocols as varied as MySQL and AMQP. This talk describes the challenges we faced and how we solved them using multiple technologies from the Kubernetes ecosystem. The solution includes a system that automatically creates namespaces, provisions certificate hierarchies, and manages ingress controllers for new customers, then wraps services with a set of side-car containers to handle tasks such as TLS termination. We describe how we employed Kubernetes native constructs such as Custom Resource Definitions to automate those tasks. For network communications, we discuss how to securely handle ingress, outgress, pod-to-pod, and cross-namespace traffic. To support both HTTP and TCP-based protocols, we describe a two-level network routing system consisting of both a "k8sniff" and an nginx ingress controller. For ensuring customer data privacy we compare these approaches: (1) Network Policy + Layer 2 virtualization; (2) TLS encryption of all pod-to-pod traffic; (3) a combination of the two. Finally, we debate whether the process isolation model of Linux containers is sufficient, and discuss our experience with stronger virtualization-based mechanisms such as Frakti / HyperContainer.

[Sched URL](https://kccncna17.sched.com/event/f4c004fb3425daae28396f7174137f78)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/tFdcrncaxD4' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
