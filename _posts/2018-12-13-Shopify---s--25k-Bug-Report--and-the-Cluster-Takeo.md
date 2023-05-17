---
title: "Shopify’s $25k Bug Report, and the Cluster Takeover That Didn’t Happen - Greg Castle, Google & Shane Lawrence, Shopify"
categories: ["KubeCon + CloudNativeCon North America 2018"]
---

## Abstract

In May, a security researcher reported a vulnerability in a Shopify microservice and demonstrated how it could be used to access keys from the Google Cloud metadata API. This could have led to a cluster takeover, for which Shopify awarded $25k through its bug bounty program.  Shane will share his experience responding to the report, analyzing Kubernetes audit logs, and hardening the cluster to block the escalation path. Together, Greg and Shane will describe some example Kubernetes audit log queries that can help discover unusual activity in the form of Kubernetes API access, and assess the impact of credential exposure, such as in this report. The collection of example queries will be released for use by the Kubernetes community and we will also share some hardening best practices.

[Sched URL](https://kccna18.sched.com/event/50aeb0e28f476b506e83ae4117fff24d)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/2XCm7vveU5A' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
