---
title: "How Attackers Use Exposed Prometheus Server to Exploit Kubernetes Clusters - David de Torres Huerta & Miguel Hernández, Sysdig"
categories: ["KubeCon + CloudNativeCon Europe 2022"]
talk_title: "How Attackers Use Exposed Prometheus Server to Exploit Kubernetes Clusters"
speakers: "David de Torres Huerta & Miguel Hernández, Sysdig"
event: "KubeCon Europe 2022"
series: "kubecon-eu"
event_code: "KC-EU-22"
year: 2022
youtube_id: "5cbbm_L6n7w"
sched_url: "https://kccnceu2022.sched.com/event/dda1b6dd2bb1c7e0885079ee9e13a042"
---

Prometheus has become the standard for monitoring Kubernetes services. It comes with a set of helpful exporters, and Kubernetes offers several metrics endpoints directly through the API. These features enable monitoring and troubleshooting of most situations that SREs face on a daily basis. But, what if an attacker accesses your Prometheus server? How much information can they get for fingerprinting the cluster? Kernel versions, IP addresses, instance types, library versions…the list goes on and on. In this session, you will learn how attackers use this information in the first part of reconnaissance, to see if you are vulnerable. The speakers will share - What secrets they collect to fingerprint your Kubernetes cluster (hint: they're not after your timeseries) - How to leverage this information internally to secure your cluster - How to prevent the exposition of sensitive information No matter how many safety best practices you apply, you must be aware of every link of the chain.Click here to view captioning/translation in the MeetingPlay platform!
