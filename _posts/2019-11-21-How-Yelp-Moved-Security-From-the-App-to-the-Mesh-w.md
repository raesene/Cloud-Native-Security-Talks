---
title: "How Yelp Moved Security From the App to the Mesh with Envoy and OPA - Daniel Popescu, Yelp & Ben Plotnick, Cruise"
categories: ["KubeCon + CloudNativeCon North America 2019"]
---

## Abstract

From its inception, Yelp's service infrastructure has treated security as a fundamental component. For many years, developers carried the burden of building security features directly into their services. By using standard cloud native building blocks, the service infrastructure now provides security features by default; this enables hundreds of developers to focus on shipping features for more than 100M monthly active Yelp users.This talk will cover Yelp’s journey from a legacy service proxy to a modern, secure service mesh based on Envoy and Open Policy Agent. It will discuss-Authn and Authz mechanisms using mTLS and JWT with Envoy and OPA-Migration from using an in-house policy decision engine to standardized open source tools (OPA)-Transpiling legacy policy data to rego and other best practices for policy maintenance-Strategies for quickly and safely rolling out policy changes

[Sched URL](https://kccncna19.sched.com/event/b8e6e0462d91e283d2f318fb8e357d28)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/Z6aN3Smt-9M' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
