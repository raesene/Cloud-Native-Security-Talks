---
title: "OAuth2 Token Exchange for Microservice API Security - Ahmet Soormally & Letz Yaara, Tyk"
categories: ["KubeCon + CloudNativeCon Europe 2024"]
---

## Abstract

APIs need a way to authenticate, authorize and propagate identity between services. Load Balancers, API Gateways, ingress and chained microservice calls make propagating identity and authorization in a secure manner significantly more complex. In this session, we will dive into typical OAuth2.0 flows with practical examples using Keycloak. We will then illustrate some of the challenges you will face applying OAuth2 in a microservice environment, alongside the typical workarounds or hacks that are seen in the wild. We will discuss advantages and drawbacks of each approach, and most importantly highlight potential vulnerabilities. Finally, we will present a relatively new standard known as the OAuth2 Token Exchange RFC8693 as a recommended approach to authorization and propagating identity using Keycloak to demonstrate. Key Points:- OAuth 2.0 Essentials- Live Demo: with shortcomings applying OAuth2 in a microservice environment- Token Exchange RFC8693 ImportancePR we used for our demo: https://github.com/TykTechnologies/tyk/pull/6069Link to the API Gateway we used in the demo: tyk.io

[Sched URL](https://kccnceu2024.sched.com/event/ca7130a95d7a90bc877d029089bb3430)

## Video

<iframe src="https://www.youtube.com/embed/09GhdXhiv0Q" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
