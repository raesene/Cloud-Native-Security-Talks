---
title: "From the Cluster to the Cloud: Lateral Movements in Kubernetes - Yossi Weizman & Ram Pliskin, Microsoft"
categories: ["CloudNativeSecurityCon North America 2023"]
---

## Abstract

As K8s clusters usually reside in the cloud, access to a container in the cluster can be a foothold to the entire cloud workload. In this session, we’ll present novel techniques used in recent real-world attacks which allowed adversaries to move laterally from a container in a K8s cluster to external cloud resources. We'll start with inner-cluster lateral movement: We'll talk about K8s RBAC configurations that unexpectedly allowed inner-cluster lateral movement and were the root-cause of vulnerabilities in containerized apps. We'll discuss how one can identify such activities by native K8s tools. We'll continue to cluster-to-cloud lateral movement. The key concept in this area is cluster-to-cloud authentication. We'll introduce the various authentication methods used by the major cloud providers: Azure, AWS and GCP. All of the methods fall into one of these 3 buckets: Direct\modified access to IMDS, using K8s as an OIDC identity provider or storing credentials on the underlying nodes. Every authentication method comes with its default configuration, many of those unknowingly grant excessive permissions. We'll present real-world recent incidents of cloud environment takeovers which originated in K8s clusters. We'll explain how users can prevent and detect such activities.

[Sched URL](https://cloudnativesecurityconna23.sched.com/event/6c40118384669160fff13b0c8b842785)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/9-F8oa85AU0' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
