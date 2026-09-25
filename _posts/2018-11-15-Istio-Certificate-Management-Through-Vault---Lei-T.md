---
title: "Istio Certificate Management Through Vault - Lei Tang & Yonggang Liu, Google"
categories: ["KubeCon + CloudNativeCon China 2018"]
talk_title: "Istio Certificate Management Through Vault"
speakers: "Lei Tang & Yonggang Liu, Google"
event: "KubeCon China 2018"
series: "kubecon-china"
event_code: "KC-CN-18"
year: 2018
youtube_id: "U4AJTEnUdkU"
sched_url: "https://kccncchina2018english.sched.com/event/be6b41fab438842391f8c95c6bea71f3"
---

In this talk, we present the design and implementation of a new Istio certificate management system that uses Vault to securely manage Istio certificates. First, we introduce the identity system in Istio and the current architecture of Istio certificate management system. Next, we present the architecture of the new Vault-based Istio identity system with the details of its authentication and authorization mechanisms for issuing Istio certificates. We will go through a detailed example flow from a pod in Istio requesting a certificate to Vault signing the certificate request. Lastly, we will make a demo of the new Istio certificate management system.
