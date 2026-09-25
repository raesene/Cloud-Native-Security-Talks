---
title: "Everything Wrong with K8s Authentication and How We Worked Around It - Mo Khan & Margo Crawford, VMware"
categories: ["KubeCon + CloudNative North America 2021"]
talk_title: "Everything Wrong with K8s Authentication and How We Worked Around It"
speakers: "Mo Khan & Margo Crawford, VMware"
event: "KubeCon North America 2021"
series: "kubecon-na"
event_code: "KC-NA-21"
year: 2021
youtube_id: "OCkTnElNE9M"
sched_url: "https://kccncna2021.sched.com/event/6ae9a81923d3a44b3bb27953cf33ea69"
---

Kubernetes provides many flexible authentication options, but they are inaccessible to a large portion of Kubernetes users in practice. When enterprise cluster administrators have clusters across many providers or distributions of Kubernetes, they struggle to unify them under a single identity platform. Kubernetes authentication options are often not available on managed cloud provider platforms, and even on self-hosted clusters it is non-trivial to integrate with common identity technologies such as OIDC or LDAP. This session will describe common pitfalls and limitations of Kubernetes authentication and show how to work around them. We will describe how to integrate identities from OIDC/LDAP into any Kubernetes cluster, provide nice login flows for cluster users, and enable federated logins across multiple clusters. Attend this session to learn about the latest Kubernetes auth integration techniques and see what’s coming in future Kubernetes versions.
