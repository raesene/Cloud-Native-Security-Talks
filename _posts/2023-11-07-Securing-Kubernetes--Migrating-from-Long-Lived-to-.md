---
title: "Securing Kubernetes: Migrating from Long-Lived to Time-Bound Tokens Without Disrupting Existing Apps - Yuan Chen & James Munnelly, Apple Inc."
categories: ["KubeCon + CloudNative North America 2023"]
---

## Abstract

In earlier versions of Kubernetes, secrets containing long-lived tokens are automatically generated for service accounts, posing security risks as these tokens do not expire and could be shared among pods and users. Recent updates have introduced TokenRequestAPI to obtain time-bound tokens with bounded lifetimes, enhancing security practices and discouraging the use of long-lived tokens. Yuan Chen and James Munnelly will delve into the details of these changes, shedding light on their impact and providing strategies for migrating existing long-lived tokens to time-bound tokens without disrupting current customer applications. Additionally, they will share best practices for tracking and monitoring different token uses within a Kubernetes cluster. This includes legacy long-lived tokens, time-bound tokens created via TokenRequestAPI, and manually managed long-lived tokens. They will also address effective management of time-bound token expiry in large-scale Kubernetes clusters.

[Sched URL](https://kccncna2023.sched.com/event/743545aab046bb8fb96b0d320c12c744)

## Video

<iframe src="https://www.youtube.com/embed/URGPfegNz64" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
