---
title: "Entitlements: Understandable Container Security Controls - Justin Cormack & Nassim Eddequiouaq, Docker (Intermediate Skill Level) (Slides Attached)"
categories: ["KubeCon + CloudNativeCon Europe 2018"]
talk_title: "Entitlements: Understandable Container Security Controls"
speakers: "Justin Cormack & Nassim Eddequiouaq, Docker"
event: "KubeCon Europe 2018"
series: "kubecon-eu"
event_code: "KC-EU-18"
year: 2018
youtube_id: "76S7ZAwM0h4"
sched_url: "https://kccnceu18.sched.com/event/2ccda84b86fc5c476357e2dda3e68791"
---

In this talk Justin Cormack introduces a new system of security entitlements for container workloads. These specify the types of access a pod should have in a human readable way. He will also demonstrate an example implementation running in Kubernetes.  The current pod security configuration is very low level, and does not really make any sense to users of the system. How can we make security configuration understandable? One route comes from the model of application entitlements that Apple uses on the iPhone to control things like access to Push Notifcations and Payments. The open source libentitlement library, being developed at Docker, enables similarly high level controls to be used for managing containers. The talk will also cover the relationship with Open Policy Agent and other access control frameworks, and relation to Linux Security Modules and PodSecurityPolicy.
