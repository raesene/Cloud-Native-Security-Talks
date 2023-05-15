---
title: "Securing User to Service Access in Kubernetes - Maya Kaczorowski & Maisem Ali, Tailscale"
categories: ["CloudNativeSecurityCon North America 2023"]
---

## Abstract

Kubernetes makes it easy to run and scale your microservices, and Kubernetes automatically assigns the pods running your service an IP address and a DNS name for discovery and routing. Network security concerns for Kubernetes, however, seem to focus on user access to the control plane, using a bastion; or on service-to-service communication within a cluster, using a service mesh. So how should your development team secure access to the internal services you’re running on Kubernetes — is it enough to just use Kubernetes Ingress and a web proxy? In this talk, we’ll focus on the networking and security questions you should consider when exposing Kubernetes services to your users, including authentication and authorization, load balancing, traffic filtering, and encryption. We’ll discuss different options you have for managing access to these services, using Kubernetes Ingress, Kubernetes load balancer objects, service meshes, web proxies, IPsec, and WireGuard. You’ll come away with a better understanding of how to give service access to users, and how these complement other network solutions you might already have in your cluster.

[Sched URL](https://cloudnativesecurityconna23.sched.com/event/ac9f4748eed0389597e201ffb3ffb5c5)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/yvbNdZxonSs' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
