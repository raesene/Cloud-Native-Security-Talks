---
title: "Securing Data Applications at Pinterest With Finer Grained Access Control on Kubernetes - Soam Acharya & William Tom, Pinterest"
categories: ["KubeCon + CloudNativeCon North America 2025"]
talk_title: "Securing Data Applications at Pinterest With Finer Grained Access Control on Kubernetes"
speakers: "Soam Acharya & William Tom, Pinterest"
event: "KubeCon North America 2025"
series: "kubecon-na"
event_code: "KC-NA-25"
year: 2025
youtube_id: "jPS6P3mTbqo"
sched_url: "https://kccncna2025.sched.com/event/9248015d029bded98a02cef0e7f63f6f"
---

At Pinterest, our data processing platform runs nearly 90K jobs on 20K nodes ingesting about 200PB of data daily, powering ML models, user insights, data lakes, and more. This massive scale, while pushing the limits of cloud computing, requires secure, least-privileged data management that also has to meet evolving regulations. To address these needs, we introduced Finer Grained Access Control (FGAC) into Moka, our new Kubernetes-based processing platform. FGAC integrates Kubernetes and AWS features (namespaces, sidecars, service accounts, RBAC, STS, EKS, IRSA) to authenticate with internal services (servicemesh, mTLS, IAM proxy) for a secure multi-tenant environment supporting Spark, Ray, and Flink. In this talk, we detail our design for Moka FGAC and current migration status. We also share the trade-offs and design decisions that led to better data isolation, scale, improved resource utilization and an overall simpler approach compared to our previous Hadoop/Kerberos based solution.
