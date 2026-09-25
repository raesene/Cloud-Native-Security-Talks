---
title: "How Yelp Moved Security From the App to the Mesh with Envoy and OPA - Daniel Popescu, Yelp & Ben Plotnick, Cruise"
categories: ["KubeCon + CloudNativeCon North America 2019"]
talk_title: "How Yelp Moved Security From the App to the Mesh with Envoy and OPA"
speakers: "Daniel Popescu, Yelp & Ben Plotnick, Cruise"
event: "KubeCon North America 2019"
series: "kubecon-na"
event_code: "KC-NA-19"
year: 2019
youtube_id: "Z6aN3Smt-9M"
sched_url: "https://kccncna19.sched.com/event/b8e6e0462d91e283d2f318fb8e357d28"
---

From its inception, Yelp's service infrastructure has treated security as a fundamental component. For many years, developers carried the burden of building security features directly into their services. By using standard cloud native building blocks, the service infrastructure now provides security features by default; this enables hundreds of developers to focus on shipping features for more than 100M monthly active Yelp users.This talk will cover Yelp’s journey from a legacy service proxy to a modern, secure service mesh based on Envoy and Open Policy Agent. It will discuss-Authn and Authz mechanisms using mTLS and JWT with Envoy and OPA-Migration from using an in-house policy decision engine to standardized open source tools (OPA)-Transpiling legacy policy data to rego and other best practices for policy maintenance-Strategies for quickly and safely rolling out policy changes
