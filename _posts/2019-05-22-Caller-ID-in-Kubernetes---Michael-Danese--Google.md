---
title: "Caller ID in Kubernetes - Michael Danese, Google"
categories: ["KubeCon + CloudNativeCon Europe 2019"]
talk_title: "Caller ID in Kubernetes"
speakers: "Michael Danese, Google"
event: "KubeCon Europe 2019"
series: "kubecon-eu"
event_code: "KC-EU-19"
year: 2019
youtube_id: "A4geWDqKNYw"
sched_url: "https://kccnceu19.sched.com/event/4c3abe092f8e7177f07d981a20cfac1e"
---

Kubernetes lets every Pod have a Service Account identity, but previously, that identity has only really been usable to authenticate to the Kubernete API server. The newly-released pod proof of identity can be used to securely establish trusted communication between workloads running in a Kubernetes cluster, to external services, or even to bootstrap the identity of higher level services like Istio. This talk will delve into the design of workload identity in Kubernetes and how you can use it to build more secure systems.
