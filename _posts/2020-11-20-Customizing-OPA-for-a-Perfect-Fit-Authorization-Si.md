---
title: "Customizing OPA for a Perfect Fit Authorization Sidecar - Patrick East, Styra"
categories: ["KubeCon + CloudNativeCon North America 2020 Virtual"]
---

## Abstract

The Open Policy Agent (OPA) has become widely used in the CNCF ecosystem and is a go-to option for application developers as the standardized decision engine for authorization. Many users rely on the existing integrations with Envoy/Istio, or the OPA REST API Server, but this doesn't always fit in an application cleanly. Common performance questions arise related to using the OPA HTTP API, plus management concerns around collecting decision logs, and requirements for integration with existing security infrastructure. Join Patrick East, an active OPA maintainer, to see how easy it is to use OPA's public Golang API's to create a tailored OPA binary with the following extensions: * Custom High Performance gRPC font-end API * Custom Kafka decision log plugin * Custom OAuth2 Rego builtin functions

[Sched URL](https://kccncna20.sched.com/event/ddd7728f0273dc748bcc82d1e5f9de84)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/uCra4Uq9bCM' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
