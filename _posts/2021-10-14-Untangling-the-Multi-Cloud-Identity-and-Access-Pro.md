---
title: "Untangling the Multi-Cloud Identity and Access Problem With SPIFFE Tornjak - Brandon Lum & Mariusz Sabath, IBM"
categories: ["KubeCon + CloudNative North America 2021"]
---

## Abstract

When an organization moves to a multi-cloud environment, one of the first questions a developer will ask is “How do I access my S3 bucket in AWS from my GCP cluster?” (or any other permutations thereof cloud services/providers). This is an unsurprising request. However, the solutions to these problems today are surprisingly inadequate, especially when security and compliance are considered. This problem stems from cloud providers/services each having their own notion of workload identity and schema, which makes federation difficult. This talk proposes a shift in the perspective of workload identity from being “platform specific” to “organization wide” using SPIFFE/SPIRE and the new SPIFFE Tornjak project to provide a consistent and secure organization-wide management plane for workload identity and access across multiple clouds. After all, user identities are managed on the organization level (e.g. LDAP, etc.), why should our handling of workload identities be any different?

[Sched URL](https://kccncna2021.sched.com/event/a5e6781ddb6e4df01a5e52d5ae89b491)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/Voy_8wifB0E' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
