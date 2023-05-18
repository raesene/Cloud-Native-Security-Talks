---
title: "How Netflix Is Solving Authorization Across Their Cloud [I] - Manish Mehta & Torin Sandall, Netflix"
categories: ["KubeCon + CloudNativeCon North America 2017"]
---

## Abstract

Since 2008, Netflix has been on the cutting edge of cloud-based microservices deployments. In 2017, Netflix is recognized as one of the industry leaders at building and operating “cloud native” systems at scale. Like many organizations, Netflix has unique security requirements for many of their workloads. This variety requires a holistic approach to authorization to address “who can do what” across a range of resources, enforcement points, and execution environments.  In this talk, Manish Mehta (Senior Security Software Engineer at Netflix) and Torin Sandall (Technical Lead of the Open Policy Agent project) will present how Netflix is solving authorization across the stack in cloud native environments. The presentation shows how Netflix enforces authorization decisions at scale across various kinds of resources (e.g., HTTP APIs, gRPC methods, SSH), enforcement points (e.g., microservices, proxies, host-level daemons), and execution environments (e.g., VMs, containers) without introducing unreasonable latency. The presentation includes a deep dive into the architecture of the cloud native authorization system at Netflix as well as how authorization decisions can be offloaded to an open source, general-purpose policy engine (Open Policy Agent).  This talk is targeted at engineers building and operating cloud native systems who are interested in security and authorization. The audience can expect to take away fresh ideas about how to enforce fine-grained authorization policies across stackthe cloud environment.

[Sched URL](https://kccncna17.sched.com/event/ff6c4c12c50ab880ad529fde6a39a57b)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/R6tUNpRpdnY' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
