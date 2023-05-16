---
title: "Fine-Grained User Authorization for Kubernetes with OPA and LDAP - Cagri Cetin & Quentin Long, Yelp Inc."
categories: ["KubeCon + CloudNative North America 2021"]
---

## Abstract

Yelp recently migrated their container-orchestration system from Mesos to Kubernetes. However, existing Kubernetes authorization mechanisms were insufficient to implement least-privilege access control rules. Yelp needed to authorize its users to hundreds of services owned by hundreds of different teams. By leveraging the Open Policy Agent (OPA), Yelp has implemented an authorization system that allows defining fine-grained authorization rules: These can rely on service ownerships, resources’ or actions’ sensitivity levels. This talk covers Yelp’s journey to a fine-grained Kubernetes authorization using OPA and LDAP. It will discuss: - Shortcomings of existing Kubernetes authorization mechanisms - Design details of the new OPA-based system - Strategies for provisioning authorization rules at scale - Migration to the new system with zero downtime - Issues encountered along the way and lessons learned

[Sched URL](https://kccncna2021.sched.com/event/43248181d58f65b88a4a5367afc39f5f)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/VFE6D30Qhx0' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
