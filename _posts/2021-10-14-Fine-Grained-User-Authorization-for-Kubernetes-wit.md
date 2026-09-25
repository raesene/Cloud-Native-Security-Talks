---
title: "Fine-Grained User Authorization for Kubernetes with OPA and LDAP - Cagri Cetin & Quentin Long, Yelp Inc."
categories: ["KubeCon + CloudNative North America 2021"]
talk_title: "Fine-Grained User Authorization for Kubernetes with OPA and LDAP"
speakers: "Cagri Cetin & Quentin Long, Yelp Inc."
event: "KubeCon North America 2021"
series: "kubecon-na"
event_code: "KC-NA-21"
year: 2021
youtube_id: "VFE6D30Qhx0"
sched_url: "https://kccncna2021.sched.com/event/43248181d58f65b88a4a5367afc39f5f"
---

Yelp recently migrated their container-orchestration system from Mesos to Kubernetes. However, existing Kubernetes authorization mechanisms were insufficient to implement least-privilege access control rules. Yelp needed to authorize its users to hundreds of services owned by hundreds of different teams. By leveraging the Open Policy Agent (OPA), Yelp has implemented an authorization system that allows defining fine-grained authorization rules: These can rely on service ownerships, resources’ or actions’ sensitivity levels. This talk covers Yelp’s journey to a fine-grained Kubernetes authorization using OPA and LDAP. It will discuss: - Shortcomings of existing Kubernetes authorization mechanisms - Design details of the new OPA-based system - Strategies for provisioning authorization rules at scale - Migration to the new system with zero downtime - Issues encountered along the way and lessons learned
