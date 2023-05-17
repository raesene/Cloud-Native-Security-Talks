---
title: "How Kubernetes Components Communicate Securely in Your Cluster - Maya Kaczorowski, Google"
categories: ["KubeCon + CloudNativeCon North America 2019"]
---

## Abstract

How *do* your cluster components talk to each other?In this expository talk, we'll first cover the main Kubernetes components that need trusted communication - that is, the API server, kubelet, and etcd, and how this communication is protected. Then, we'll go over how the cluster certificate authority (CA) works, and how this grants certificates to Kubernetes components. Furthermore, we'll explain what authentication, integrity, and encryption means, and what options are available in Kubernetes, and what you need to configure to address these pieces of CIS benchmarks. Lastly, we'll explain how you can protect other communications within your cluster, if needed for your workload - like node to node and pod to pod.You'll come away with a better understanding of how communications in Kubernetes work, cluster trust, and default protections.

[Sched URL](https://kccncna19.sched.com/event/6eb8df099473c17704b5305012af0b5f)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/bXnVI_hUAbk' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
