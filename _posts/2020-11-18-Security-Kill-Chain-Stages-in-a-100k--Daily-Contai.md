---
title: "Security Kill Chain Stages in a 100k+ Daily Container Environment with Falco - Natch Ruengsakulrach & Eric Hollis, MathWorks"
categories: ["KubeCon + CloudNativeCon North America 2020 Virtual"]
talk_title: "Security Kill Chain Stages in a 100k+ Daily Container Environment with Falco"
speakers: "Natch Ruengsakulrach & Eric Hollis, MathWorks"
event: "KubeCon North America 2020 (Virtual)"
series: "kubecon-na"
event_code: "KC-NA-20"
year: 2020
youtube_id: "L-5RYBTV010"
sched_url: "https://kccncna20.sched.com/event/5b2cfac220b2b22a3ffa2a38986552ab"
---

Security is a vital aspect of a Cloud Native infrastructure. In this talk, Eric and Natch will show how they set up monitoring to identify anomalous system calls and abnormal Kubernetes API events in MathWorks cloud infrastructure hosting 100K+ daily MATLAB containers with Falco, a CNCF Container Runtime Security project. They have mapped their detections to Security Kill Chain to detect threats in the attack lifecycle. The first part of the talk focuses on Falco, including eBPF integration and Falco rules. The second part covers a walkthrough of the event pipeline and how Falco is used to identify activity related to recon, weaponization, delivery, exploitation, installation, command & control, and actions on objectives. Attendees will leave knowing how to integrate Falco, write and test Falco rules to improve their systems’ security observability and detection.
