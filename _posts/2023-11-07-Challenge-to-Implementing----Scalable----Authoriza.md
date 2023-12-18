---
title: "Challenge to Implementing “Scalable” Authorization with Keycloak - Yoshiyuki Tabata, Hitachi, Ltd."
categories: ["KubeCon + CloudNative North America 2023"]
---

## Abstract

In the OWASP API Security Top 10 2023, three of the top 5 vulnerabilities include the word "authorization (authz)", authz is becoming more important for security considerations. Authz is often developed from scratch, however, along with the expanded service, the authz logic often becomes low scalability due to the increase in authz targets, attributes, and combinations. In such cases, it is common to introduce an authz service. Keycloak, an IAM OSS, also has an authz service. Keycloak has OAuth2 authz server capabilities, too, so by using the authz service, it is possible to centrally manage data related to authentication (authn) and authz. In this session, Yoshiyuki Tabata explains how to implement scalable authz using Keycloak and how to combine it with OPA to avoid Keycloak becoming SPOF and improve authz performance. Furthermore, by combining with CockroachDB, he introduces an authn and authz solution that withstands regional failures and operates in multi-cloud environments.

[Sched URL](https://kccncna2023.sched.com/event/31a2be78845005f12b51839ea60b071c)

## Video

<iframe src="https://www.youtube.com/embed/-m8FUNX1DP0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
