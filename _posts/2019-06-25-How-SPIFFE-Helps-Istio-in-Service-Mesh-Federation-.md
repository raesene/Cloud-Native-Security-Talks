---
title: "How SPIFFE Helps Istio in Service Mesh Federation - Yonggang Liu & Wencheng Lu, Google"
categories: ["KubeCon + CloudNativeCon | Open Source Summit China 2019"]
talk_title: "How SPIFFE Helps Istio in Service Mesh Federation"
speakers: "Yonggang Liu & Wencheng Lu, Google"
event: "KubeCon China 2019"
series: "kubecon-china"
event_code: "KC-CN-19"
year: 2019
youtube_id: "SCBksDnA2rU"
sched_url: "https://kccncosschn19eng.sched.com/event/0b3605c1ac7779a01fa7488692cde322"
---

This proposal resolves the fundamental identity federation problem between different trust domains, using the trust domain and bundle standard proposed by SPIFFE. As an important collaborator of SPIFFE/SPIRE, Istio adopts this standard to support federations with SPIRE and other identity systems.  The newly proposed standard enables multiple service meshes to securely establish trusts for cross-mesh secure communications. In this talk, we will explain how this new standard can help on federated service meshes and how Istio supports the standard. Finally, we will demonstrate how the federation can be set up between Istio and SPIRE systems.
