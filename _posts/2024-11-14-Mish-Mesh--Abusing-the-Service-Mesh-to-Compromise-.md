---
title: "Mish-Mesh: Abusing the Service Mesh to Compromise Kubernetes Environments - Hillai Ben-Sasson & Nir Ohfeld, Wiz"
categories: ["KubeCon + CloudNativeCon North America 2024"]
talk_title: "Mish-Mesh: Abusing the Service Mesh to Compromise Kubernetes Environments"
speakers: "Hillai Ben-Sasson & Nir Ohfeld, Wiz"
event: "KubeCon North America 2024"
series: "kubecon-na"
event_code: "KC-NA-24"
year: 2024
youtube_id: "wJGKVQmeDns"
sched_url: "https://kccncna2024.sched.com/event/f8354b8666aa2ec36294af95d1dfb510"
---

Service mesh solutions are common components in almost every large Kubernetes environment. Many engineers and security teams have adopted solutions like Linkerd and Istio to better segment and isolate their Kubernetes networks. In this talk, we will demonstrate how we were able to exploit common misconfigurations and insecure features in popular service mesh solutions, to escalate low-severity vulnerabilities to critical service takeovers. Our real-life examples include several major cloud service providers, where these vulnerabilities allowed us to gain unauthorized access to internal systems and sensitive secrets. This talk will help engineers understand whether their service mesh deployment acts as a proper security barrier, and how to make sure that it does. Security teams – both attackers and defenders – will learn new techniques for hacking Kubernetes environments, and how to properly defend against them.
