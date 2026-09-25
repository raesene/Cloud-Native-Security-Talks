---
title: "Cluster Grey Zone: Risks in Managed Cluster Middleware - Shay Berkovich & Barak Sharoni, Wiz"
categories: ["KubeCon + CloudNativeCon Europe 2023"]
talk_title: "Cluster Grey Zone: Risks in Managed Cluster Middleware"
speakers: "Shay Berkovich & Barak Sharoni, Wiz"
event: "KubeCon Europe 2023"
series: "kubecon-eu"
event_code: "KC-EU-23"
year: 2023
youtube_id: "S2rrQGtfobk"
sched_url: "https://kccnceu2023.sched.com/event/0cdb928d5659cf360f4113c1dffa8f6f"
---

With the increase in K8s and cloud popularity, cloud security providers (CSPs) realized the advantages of offering Kubernetes as a PaaS to their users. Today the default deployment of production workloads is through the cloud-managed Kubernetes services, where the responsibility for securing the cluster is shared between the user and the CSP. While users are generally aware of their own workloads, there is a less-documented set of components, automatically deployed by the CSPs and running on worker nodes. We call it Managed Cluster Middleware (abbreviated MCM). A freshly deployed EKS node will typically have 3 additional pods, AKS and GKE deploy even more pods. The number increases depending on the features and plugins one chooses to add to the defaults. MCM can introduce an additional threat surface, with a footprint on every node and carrying high privileges, additional network exposure and vulnerabilities. Therefore, MCM can be an attractive target for attackers, while frequently omitted by scanners and configuration tools. This talk follows up on our previous research on cloud grey zone. We analyze the MCM security posture as we would approach the non-trusted deployments. Consequently, we review how users should adjust their K8s threat model in light of this research.
