---
title: "Avoiding IAC Potholes with Policy + Cloud Controllers - Andrew Martin, ControlPlane"
categories: ["CloudNativeSecurityCon North America 2023"]
---

## Abstract

In large organisations, enabling and securing self-serve cloud infrastructure for teams hosting their applications on Kubernetes is hard. Most large organisations implement Enterprise Security Architectures featuring IAC pipelines with Policy as Code frameworks at the outset of their cloud journey, which are found to be not fit for purpose when teams use Kubernetes to provision infrastructure either natively, through services of type Loadbalancer, or using hosted cloud controllers such as Crossplane. In this talk, Rowan will demonstrate how infrastructure and security teams can use policy engines (Kyverno) to secure a model that uses Kubernetes native and hosted cloud controllers (such as Crossplane) to provision infrastructure. This model enables application teams to self-serve, whilst preventing the launch of insecure infrastructure and enforcing compliance and security requirements centrally. To ease adoption of the model, Rowan will open source an example library of policies integrated with OSCAL for commonly used services across AWS, enforcing controls aligned with NIST800-53 in a manner that can be audited by compliance teams, and simplifying the developer experience by enabling the dynamic generation of cloud resources with secure defaults.

[Sched URL](https://cloudnativesecurityconna23.sched.com/event/9b9f2d33b858e61368ec34ac87cbea9c)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/cvoWlwftbEE' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
