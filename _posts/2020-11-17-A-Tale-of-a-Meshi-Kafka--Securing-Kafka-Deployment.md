---
title: "A Tale of a Meshi Kafka: Securing Kafka Deployment When Istio Is Used - Ariel Shuper, Portshift & Nikolas Mousouros, Marlow Navigation"
categories: ["Cloud Native Security Day North America 2020"]
---

## Abstract

Kafka is a commonly used message broker for microservices real-time data feeds. A standard setup allows any micro-service to read or write any messages to/from any topic. The need for security typically starts when multiple applications use the same Kafka broker in a cluster, or when confidential information is shared in the Kafka topics. Common security practices to use are authenticating subscribers and publishers, authorization policies for access control and data encryption. When Istio is being used with microservices that access Kafka topics, the envoy proxies is expected to offload these security elements.  However, creating sustainable and consistent authorization policies when Istio is deployed isn't feasible, and tracking the microservices based on their IPs isn’t feasible because of their replacement.   The session will present how to build an external authorization mechanism and simplify policy management for Kafka topics by using open source tools, like OPA and others

[Sched URL](https://cnsdna20.sched.com/event/d5d2e49bbfff81d4bdae550a5342576e)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/Ku6gKTLbD78' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
