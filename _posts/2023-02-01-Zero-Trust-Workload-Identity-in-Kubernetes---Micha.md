---
title: "Zero Trust Workload Identity in Kubernetes - Michael Peters, Red Hat"
categories: ["CloudNativeSecurityCon North America 2023"]
---

## Abstract

Zero Trust principles proscribe that no interactions between services are to be done with any implicit trust. Most current solutions to explicit authorization involve passwords or secret keys, but it's almost impossible to count the number of security breaches that happen because service passwords or keys are improperly stored, not rotated frequently enough or exposed during rollouts. Every new service added has the potential to exponentially complicate how we secure and deploy those secrets. But what if there was a simpler solution? What if we didn't need those secrets at all? What if the authorization was tied to the workload's identity itself? This is the goal of SIFFE (the spec) and Spire (the implementation). In this talk we'll show how to implement a Zero Trust system that uses workload identity across a service mesh in Kubernetes to provide explicit authorization between services. We'll explore centralized policy enforcement between those services as well as integrations with up and coming projects like Keylime (for identity tied to hardware attestation) and Sigstore (for identity during software builds).

[Sched URL](https://cloudnativesecurityconna23.sched.com/event/9afbeaa9a33452aac45f7c1e7c252702)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/eyj0UCmJfjo' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
