---
title: "Rogue No More: Securing Kubernetes with Node-Specific Restrictions - Anish Ramasekar, Microsoft & James Munnelly, Apple"
categories: ["KubeCon + CloudNativeCon North America 2024"]
---

## Abstract

Did you know that a component running across multiple nodes, such as in a daemonset, intended to perform node-specific actions, can pose a significant security risk? If any node the component is running on goes rogue, it can lead to attacks on the cluster, or even worse, a complete takeover of it. What if we could restrict the component's ability to write resources only to those belonging to the node it is running on to prevent such escalation attacks? In this talk, Anish and James will introduce new Kubernetes security enhancements to bound service account tokens, which can be used with validating admission policies to enforce per-node restrictions on service accounts. This session will provide you with practical implementation guidelines and show you how these enhancements can mitigate risks and protect your infrastructure with robust node isolation.

[Sched URL](https://kccncna2024.sched.com/event/856da8898cca90525655930826dbbbb1)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/kznxInpGet4' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
