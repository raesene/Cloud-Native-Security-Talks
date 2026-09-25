---
title: "K8s Auth{N,Z} at Robinhood - Learning from Reductions, Migrations and Designing Automation - Sujith Katakam & Karen Tu, Robinhood Markets, Inc."
categories: ["KubeCon + CloudNative North America 2023"]
talk_title: "K8s Auth{N,Z} at Robinhood - Learning from Reductions, Migrations and Designing Automation"
speakers: "Sujith Katakam & Karen Tu, Robinhood Markets, Inc."
event: "KubeCon North America 2023"
series: "kubecon-na"
event_code: "KC-NA-23"
year: 2023
youtube_id: "aBUGtu-venk"
sched_url: "https://kccncna2023.sched.com/event/19a1d230193be16f8d7ea6298e3a5d87"
---

Kubernetes RBAC seems simple enough - specify the resource that you need access to and bind it to who needs it - what's the problem? In the quest of implementing least privilege company-wide, we ran into seemingly simple but practically complicated questions, for example: How do we figure out who needs what, for how long? How do we grant access in a timely and time-bound manner? How do we think about what permissions need what level of scrutiny? How do we clean up existing permissions and migrate to a different Identity Provider and authentication mechanism with as minimal user friction as possible? Work is still ongoing to clean up existing problematic permissions as well as design a sustainable solution going forward. Join us in this talk where we share the challenges and learnings we have on managing authentication and authorization at Robinhood. We'll also include a "fun" story of how our OIDC client got deleted!
