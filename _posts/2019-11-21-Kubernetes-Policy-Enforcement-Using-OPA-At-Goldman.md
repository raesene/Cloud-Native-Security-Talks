---
title: "Kubernetes Policy Enforcement Using OPA At Goldman Sachs - Miguel Uzcategui, Goldman Sachs & Tim Hinrichs, Styra"
categories: ["KubeCon + CloudNativeCon North America 2019"]
talk_title: "Kubernetes Policy Enforcement Using OPA At Goldman Sachs"
speakers: "Miguel Uzcategui, Goldman Sachs & Tim Hinrichs, Styra"
event: "KubeCon North America 2019"
series: "kubecon-na"
event_code: "KC-NA-19"
year: 2019
youtube_id: "lYHr_UaHsYQ"
sched_url: "https://kccncna19.sched.com/event/5ef792fd5b3f84fa5147ca7f5a98decf"
---

Managing state on multiple shared Kubernetes clusters may sound scary. The Goldman Sachs Kubernetes team uses OPA to manage that state using two different applications of policy. The first is the validating admission control policies that prevent unsafe resources on the cluster. The second, and novel, application goes beyond simple yes/no decisions and uses OPA policy to provision new resources on the cluster to implement a common baseline, e.g. RBAC, Volumes, ResourceQuotas, and LimitRanges.This talk focuses on the architectural design that allows GS to run OPA at scale in production. Along the way we discuss best practices and lessons learned, highlighting how GS reduced policy deployment times from days to under 10 minutes. The audience will learn how to create their own policy pipelines using popular open-source tools to enforce OPA policy across multiple Kubernetes clusters.
