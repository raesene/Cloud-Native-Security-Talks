---
title: "Securing Identity and Authorization in Microservices - Atul Tulshibagwale, SGNL"
categories: ["KubeCon + CloudNative North America 2023"]
talk_title: "Securing Identity and Authorization in Microservices"
speakers: "Atul Tulshibagwale, SGNL"
event: "KubeCon North America 2023"
series: "kubecon-na"
event_code: "KC-NA-23"
year: 2023
youtube_id: "k4tusY8-pXs"
sched_url: "https://kccncna2023.sched.com/event/e8c73c064b5bdf8012b047a300f406d8"
---

External API calls to a service in a microservices architecture results in a call chain that invokes several microservices within a trusted domain. Software supply chain, privileged user compromise or other attacks can compromise individual microservices in a trusted domain. Compromised microservices, malicious insiders or software errors can cause spurious calls to microservices. They can impersonate users in such calls and modify or augment parameters of such calls. Transaction Tokens (TraTs) is a new proposal in the IETF OAuth working group. TraTs complement existing security protocols such as SPIFFE and assure user identity and context information in a call chain. TraTs allow nesting, enabling intermediate services to assert that they have processed a call to downstream services in a call chain. In this talk we will explain TraTs with examples and use cases, and show how they can help defend against a number of attacks in microservice architectures.
