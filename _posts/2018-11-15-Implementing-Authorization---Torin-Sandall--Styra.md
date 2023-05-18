---
title: "Implementing Authorization - Torin Sandall, Styra"
categories: ["KubeCon + CloudNativeCon China 2018"]
---

## Abstract

Whether you build software for enterprises, mobile, or internal microservices, security is important. Standards like SAML, OIDC, and SPIFFE help you solve identity and authentication, but for them authorization is out of scope. When you need to control "who can do what" in your app, you are on your own.  To solve authorization, you may be tempted to hardcode logic against SAML assertions, scopes, or X.509 certificate attributes. But, approaches like this lead to systems that are hard to understand and painful to maintain.  This talk shows how to leverage the Open Policy Agent (which is used by companies like Netflix and Chef) to build a powerful authorization system on top of industry-standard authentication protocols. The talk showcases how decoupling leads to authorization solutions that are easier to understand while enabling fine-grained control over the app.

[Sched URL](https://kccncchina2018english.sched.com/event/899c6555002f1c72eba9f21230da71b3)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/hvDrpDEu2L4' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
