---
title: "Multi-Tenancy in Kubernetes: Best Practices Today, and Future Directions - David Oppenheimer, Google (Intermediate Skill Level) (Slides Attached)"
categories: ["KubeCon + CloudNativeCon Europe 2018"]
talk_title: "Multi-Tenancy in Kubernetes: Best Practices Today, and Future Directions"
speakers: "David Oppenheimer, Google"
event: "KubeCon Europe 2018"
series: "kubecon-eu"
event_code: "KC-EU-18"
year: 2018
youtube_id: "OVcFIOs5bz0"
sched_url: "https://kccnceu18.sched.com/event/240b865d737b48a98e315f6020d775f1"
---

Kubernetes offers a set of features which, when used in the right combination and configured properly, enable secure multi-tenant clusters. But it’s not always obvious how to map particular multi-tenancy requirements to those features and configurations. As a result, people often resort to spinning up one cluster per user and/or workload, thereby foregoing the utilization and management benefits they could achieve by using a single shared cluster. This talk will describe a taxonomy of various multi-tenancy models that are possible on Kubenetes today, and how to configure the existing security/multi-tenancy features to satisfy each of those use cases. We will then describe some features that are on the horizon to provide even stronger, easier-to-use multi-tenancy in Kubernetes.
