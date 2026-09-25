---
title: "AuthZEN: The “OpenID Connect” for Authorization - Omri Gazitt, Aserto"
categories: ["KubeCon + CloudNativeCon North America 2024"]
talk_title: "AuthZEN: The “OpenID Connect” for Authorization"
speakers: "Omri Gazitt, Aserto"
event: "KubeCon North America 2024"
series: "kubecon-na"
event_code: "KC-NA-24"
year: 2024
youtube_id: "MTAXC0ZaXcE"
sched_url: "https://kccncna2024.sched.com/event/a6f0de81e8aa55fa0ad09546c2669092"
---

Today, the authorization world is fractured - each vendor supports its own APIs & protocols. But this is about to change. AuthZEN, a new OpenID Foundation working group, was created in late 2023 to establish authorization standards. OIDF is the home of OpenID Connect, the ubiquitous standard for federated login, and that’s where we’re setting our sights. In this talk, I'll describe the current state of cloud-native authorization, including the policy-as-code and policy-as-data approaches, and the various open source projects in each camp. I'll also share the progress we’ve made creating a single authorization API that works across both policy-as-code (OPA, Topaz) and policy-as-data (Zanzibar-style projects), present the API specs we've created so far, and show off the various interoperable implementations. With this foundation in place, engineering teams can be more confident in externalizing their authorization and picking a provider without being locked in to a proprietary API.
