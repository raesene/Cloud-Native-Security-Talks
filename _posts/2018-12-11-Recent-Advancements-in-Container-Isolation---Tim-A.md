---
title: "Recent Advancements in Container Isolation - Tim Allclair & Adin Scannell, Google"
categories: ["KubeCon + CloudNativeCon North America 2018"]
talk_title: "Recent Advancements in Container Isolation"
speakers: "Tim Allclair & Adin Scannell, Google"
event: "KubeCon North America 2018"
series: "kubecon-na"
event_code: "KC-NA-18"
year: 2018
youtube_id: "E_jn2UiSWww"
sched_url: "https://kccna18.sched.com/event/3a30f7127b14bf7cb2eba74c351b0e39"
---

Container orchestration enables higher bin-packing and utilization of machines, but native linux containers do not offer the same degree of isolation between workloads as separate VM instances can. Attackers could abuse this lack of isolation to move through a Kubernetes cluster after gaining a foothold in a container. Fortunately, there are many tools in the defenders’ toolbox that can be applied across multiple levels of the stack.In this survey talk, we will look at several recent or upcoming advancements in container isolation. You will learn about new kernel features, several "sandboxing" approaches, and features being developed in Kubernetes to harden the Pod and Node boundaries. After the talk you will have a better understanding of how to secure your Kubernetes applications and clusters with the latest features.
