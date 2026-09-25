---
title: "Zero Trust Service Mesh with Calico, SPIRE, and Envoy - Shaun Crampton, Tigera & Evan Gilman, Scytale"
categories: ["KubeCon + CloudNativeCon Europe 2019"]
talk_title: "Zero Trust Service Mesh with Calico, SPIRE, and Envoy"
speakers: "Shaun Crampton, Tigera & Evan Gilman, Scytale"
event: "KubeCon Europe 2019"
series: "kubecon-eu"
event_code: "KC-EU-19"
year: 2019
youtube_id: "rKOEYoINdOE"
sched_url: "https://kccnceu19.sched.com/event/7570ff5b41389be8a4de33607dc5812e"
---

The promise of a service mesh is to be able to delegate the hard networking problems to a uniform set of proxies and controllers. An extremely important networking problem is securing traffic within the mesh. Service meshes based on the Envoy proxy are very popular and there is a large diversity of implementations, including many home-grown solutions that focus on routing but may not include security. Shaun and Evan will demonstrate how to enhance your service mesh to follow the Zero Trust network security model using SPIRE and Calico.  A Zero Trust Network emphasizes resilience to compromised services, hosts, and the network itself by treating every network connection as potentially hostile. Secure connections are established only when backed by strong cryptographic identity and approved by fine grained policies---provided by SPIRE and Calico respectively.
