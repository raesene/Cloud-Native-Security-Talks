---
title: "Rogue No More: Securing Kubernetes with Node-Specific Restrictions - Anish Ramasekar, Microsoft & James Munnelly, Apple"
categories: ["KubeCon + CloudNativeCon North America 2024"]
talk_title: "Rogue No More: Securing Kubernetes with Node-Specific Restrictions"
speakers: "Anish Ramasekar, Microsoft & James Munnelly, Apple"
event: "KubeCon North America 2024"
series: "kubecon-na"
event_code: "KC-NA-24"
year: 2024
youtube_id: "kznxInpGet4"
sched_url: "https://kccncna2024.sched.com/event/856da8898cca90525655930826dbbbb1"
---

Did you know that a component running across multiple nodes, such as in a daemonset, intended to perform node-specific actions, can pose a significant security risk? If any node the component is running on goes rogue, it can lead to attacks on the cluster, or even worse, a complete takeover of it. What if we could restrict the component's ability to write resources only to those belonging to the node it is running on to prevent such escalation attacks? In this talk, Anish and James will introduce new Kubernetes security enhancements to bound service account tokens, which can be used with validating admission policies to enforce per-node restrictions on service accounts. This session will provide you with practical implementation guidelines and show you how these enhancements can mitigate risks and protect your infrastructure with robust node isolation.
