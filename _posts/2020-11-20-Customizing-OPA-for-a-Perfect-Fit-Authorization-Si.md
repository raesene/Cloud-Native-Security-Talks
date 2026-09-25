---
title: "Customizing OPA for a Perfect Fit Authorization Sidecar - Patrick East, Styra"
categories: ["KubeCon + CloudNativeCon North America 2020 Virtual"]
talk_title: "Customizing OPA for a Perfect Fit Authorization Sidecar"
speakers: "Patrick East, Styra"
event: "KubeCon North America 2020 (Virtual)"
series: "kubecon-na"
event_code: "KC-NA-20"
year: 2020
youtube_id: "uCra4Uq9bCM"
sched_url: "https://kccncna20.sched.com/event/ddd7728f0273dc748bcc82d1e5f9de84"
---

The Open Policy Agent (OPA) has become widely used in the CNCF ecosystem and is a go-to option for application developers as the standardized decision engine for authorization. Many users rely on the existing integrations with Envoy/Istio, or the OPA REST API Server, but this doesn't always fit in an application cleanly. Common performance questions arise related to using the OPA HTTP API, plus management concerns around collecting decision logs, and requirements for integration with existing security infrastructure. Join Patrick East, an active OPA maintainer, to see how easy it is to use OPA's public Golang API's to create a tailored OPA binary with the following extensions: * Custom High Performance gRPC font-end API * Custom Kafka decision log plugin * Custom OAuth2 Rego builtin functions
