---
title: "Securing Edge Workloads With Cert-Manager And SPIFFE - Sitaram IYER & Riaz Mohamed, Jetstack Ltd"
categories: ["KubeCon + CloudNative North America 2022"]
talk_title: "Securing Edge Workloads With Cert-Manager And SPIFFE"
speakers: "Sitaram IYER & Riaz Mohamed, Jetstack Ltd"
event: "KubeCon North America 2022"
series: "kubecon-na"
event_code: "KC-NA-22"
year: 2022
youtube_id: "Ft8pvHg8iI4"
sched_url: "https://kccncna2022.sched.com/event/3cb96acd398360a1b1ad31bffdaa6364"
---

Workloads are moving from data centers to the edge more than ever. As workloads migrate to the cloud many enterprise IT firms are seeing compute resources moving closer to where the data is created. Edge computing models have become far more attractive to many industries like telecom, farming, public safety, retail, medical, etc., because of the ability to minimize network latency and to put essential functions closer to the technology consumer. The rate at which Kubernetes has been adopted to run these workloads have been exponentially increasing as is seen with 5G network deployments. How do we secure these workloads? Be it ingress, pod to pod (mTLS) security, and trust domains. How do we manage certificates and renewals at scale? How do we enable security policies and postures on edge locations? The talk will go through how to manage security at the edge using cert-manager and utilizing SPIFFE as a way to manage and distribute trust. We will run cert-manager on a raspberry pi and look at provisioning and renewing certificates for both ingress and mTLS use cases.
