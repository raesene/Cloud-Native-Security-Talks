---
title: "Using OpenTelemetry for Application Security, with a Real Life Example - Ron Vider, Oxeye"
categories: ["KubeCon + CloudNativeCon Europe 2023"]
---

## Abstract

The composition of application vulnerabilities has changed as a result of the shift from monolithic applications to cloud native applications, but application security testing hasn't kept up, and the security of cloud native applications is at risk. In this presentation, we’ll explore how vulnerabilities have evolved in the shift from monolithic to cloud native and microservices. We’ll see how cloud native vulnerabilities are executed, and how they look like vulnerable flows rather than just a static bug. Starting with an overview of OpenTelemetry, we’ll explore what observability is, why it’s needed in modern software development, and how it works. We’ll then dive into a real life example of a ‘cloud native vulnerability’, and how OpenTelemetry helps us detect it. We will: • Demonstrate a Kubernetes application with two microservices, and a message queue in between them. One microservice exposes an API to the internet, and a payload continues through the MQ up to the internal microservice. • Deploy the application & show the attack • Install OpenTelemetry manually on the environment, and show a vulnerable flow in Jaeger We will also look at the challenges: • Additional security related instrumentation • Test coverage - you don’t know what you don’t know • Installation process

[Sched URL](https://kccnceu2023.sched.com/event/6deed6a395be2fe23132a4d3be92da93)

## Video

<iframe src="https://www.youtube.com/embed/hz3ncpPKzUs" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
