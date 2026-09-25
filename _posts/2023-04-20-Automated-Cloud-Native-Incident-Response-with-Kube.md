---
title: "Automated Cloud-Native Incident Response with Kubernetes and Service Mesh - Matt Turner, Tetrate & Francesco Beltramini, Control Plane"
categories: ["KubeCon + CloudNativeCon Europe 2023"]
talk_title: "Automated Cloud-Native Incident Response with Kubernetes and Service Mesh"
speakers: "Matt Turner, Tetrate & Francesco Beltramini, Control Plane"
event: "KubeCon Europe 2023"
series: "kubecon-eu"
event_code: "KC-EU-23"
year: 2023
youtube_id: "vor-xiV25xM"
sched_url: "https://kccnceu2023.sched.com/event/99b973ce5ba11a2e341b86003569794f"
---

Security incident response is a well-understood operation, with established best practices like the MITRE Att&ck Framework and the Lockheed Martin Kill Chain. Tooling to aid and automate incident response exists, but not all of it is applicable to cloud-native platforms. For example, playbook apps are generally applicable, but the steps to move compromised workloads to an isolated forensics network are platform-specific, and new implementations are needed for the cloud-native world. In this talk, Francesco and Matt will * Recap incident response 101 * Introduce some cloud-native tech including Kubernetes, Istio, and GitOps * Show an Operator built by Matt for dynamically adding complex layer-7 traffic rules in response to changes in the environment, which will be used as part of the demo * Walk you through a response to a log4shell attack against a workload in a k8s cluster: sensor alert, SIEM analysis, IRP automation (honeypots, isolation), building the IoC, and killing the attack.
