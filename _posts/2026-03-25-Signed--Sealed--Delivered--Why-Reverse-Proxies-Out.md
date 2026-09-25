---
title: "Signed, Sealed, Delivered: Why Reverse Proxies Outperform VPNs - Peter ONeill, Teleport & Boris Kurktchiev, Independent"
categories: ["KubeCon + CloudNativeCon Europe 2026"]
talk_title: "Signed, Sealed, Delivered: Why Reverse Proxies Outperform VPNs"
speakers: "Peter ONeill, Teleport & Boris Kurktchiev, Independent"
event: "KubeCon Europe 2026"
series: "kubecon-eu"
event_code: "KC-EU-26"
year: 2026
youtube_id: "0tq06AAdKWQ"
sched_url: "https://kccnceu2026.sched.com/event/730d54bbb63ea74f750f8073626066db"
---

To use an analogy, traditional VPNs are like picking up a package from a shared storage room. Once you are inside, you can see and touch far more than the package meant for you. This model worked when networks were smaller and trust was implicit, but in cloud-native environments it creates excessive privilege, blind spots, and unnecessary risk.Reverse proxies in contrast act like signature on delivery. Access is granted only to the intended recipient, only for the right resource, and every handoff is logged. This session will explain how reverse proxies work, the evolution from forward proxies, and why they are a better fit than VPNs for securing modern systems.To make this concrete, we will walk through a demo using Envoy, Keycloak, and two sample applications. Attendees will see how a reverse proxy validates identity, enforces per-route authorization, and logs every action.
