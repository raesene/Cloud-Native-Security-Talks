---
title: "Trampoline Pods: Node to Admin PrivEsc Built Into Popular K8s Platforms - Yuval Avrahami & Shaul Ben Hai, Palo Alto Networks"
categories: ["KubeCon + CloudNativeCon Europe 2022"]
talk_title: "Trampoline Pods: Node to Admin PrivEsc Built Into Popular K8s Platforms"
speakers: "Yuval Avrahami & Shaul Ben Hai, Palo Alto Networks"
event: "KubeCon Europe 2022"
series: "kubecon-eu"
event_code: "KC-EU-22"
year: 2022
youtube_id: "PGsJ4QTlKlQ"
sched_url: "https://kccnceu2022.sched.com/event/fd429d7bf869c1a0eaaa52d006fbc817"
---

Security teams work to prevent the next container escape while attackers do the opposite. Inevitably, we sometimes lose this battle, but we can still win the fight! It's all about *containing* the next container escape - making sure a rogue node cannot take over the entire cluster. K8s has done a great job at de-privileging the node agent, the Kubelet, but nodes also host other credentials - their pods' service account tokens. Following an escape, the attacker can easily harvest and abuse tokens of neighboring pods.In this talk, Yuval and Shaul will introduce the concept of Trampoline Pods - pods so powerful that if their node goes rogue, it could launch devastating attacks against the cluster and in some cases completely take over it. Covering managed K8s services and common cluster add-ons, they'll reveal the trampoline pods installed by popular K8s platforms. They'll also demo exploits, discuss mitigations, and release rbac-police: a tool that detects trampoline pods and K8s privEscs.Click here to view captioning/translation in the MeetingPlay platform!
