---
title: "Authenticating and Authorizing Every Connection at Uber - Yangmin Zhu & Matt Mathew, Uber"
categories: ["KubeCon + CloudNativeCon North America 2025"]
---

## Abstract

Uber operates one of the world’s largest and most complex microservice architectures, composed of thousands of services built in diverse languages and maintained by independent teams. Ensuring consistent, secure service-to-service communication, without requiring code changes, posed a massive challenge.In this talk, we’ll share how we built and scaled a platform-level authentication and authorization solution based on Envoy, SPIRE, and the SPIFFE standard. Over a 3-year journey, we rolled out a Zero Trust architecture securing every service interaction with mTLS, authenticating workloads using SPIFFE identities, and enforcing fine-grained policies through a unified control plane.Attendees will learn about the architectural decisions, operational hurdles, and user-experience tradeoffs we faced along the way. Whether you’re starting your Zero Trust journey or looking to scale Envoy/SPIRE across a large org, this talk will offer practical insights from real-world deployment at scale.

[Sched URL](https://kccncna2025.sched.com/event/42e9e881d8c30eaa25d2c5149949ae61)

## Video

<iframe src="https://www.youtube.com/embed/GYVNg0_FpwQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
