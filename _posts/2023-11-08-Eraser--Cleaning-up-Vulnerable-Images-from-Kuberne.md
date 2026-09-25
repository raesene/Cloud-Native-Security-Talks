---
title: "Eraser: Cleaning up Vulnerable Images from Kubernetes Nodes - Peter Engelbert & Ashna Mehrotra, Microsoft"
categories: ["KubeCon + CloudNative North America 2023"]
talk_title: "Eraser: Cleaning up Vulnerable Images from Kubernetes Nodes"
speakers: "Peter Engelbert & Ashna Mehrotra, Microsoft"
event: "KubeCon North America 2023"
series: "kubecon-na"
event_code: "KC-NA-23"
year: 2023
youtube_id: "LjDzn7qI5SE"
sched_url: "https://kccncna2023.sched.com/event/9fa76fe780c4c1ac53f607c1585d89d5"
---

Supply chain security is an increasingly important issue in cloud-native computing: the number of attacks has grown by over 300% since 2021. It is common for pipelines to build and push images to the cluster, but uncommon for those images to be removed from a node’s local store once a CVE has been disclosed. Kubernetes has no built-in solution to this problem: its garbage collection only responds to disk pressure. As images become outdated, they present a risk as users may run a vulnerable container. Eraser, a CNCF sandbox project, is an open source solution that automates the scanning and removal of images. What distinguishes Eraser is that it gives more control over removal: the developer decides what gets removed and when. By default, Eraser uses Trivy to scan images based on a given threshold of vulnerability. Images can also be removed based on custom logic. The talk will begin with a demo of Eraser in action, before showing an example of customizing the removal process.
