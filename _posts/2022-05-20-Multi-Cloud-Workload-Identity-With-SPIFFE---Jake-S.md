---
title: "Multi-Cloud Workload Identity With SPIFFE - Jake Sanders & Charlie Egan, Jetstack"
categories: ["KubeCon + CloudNativeCon Europe 2022"]
talk_title: "Multi-Cloud Workload Identity With SPIFFE"
speakers: "Jake Sanders & Charlie Egan, Jetstack"
event: "KubeCon Europe 2022"
series: "kubecon-eu"
event_code: "KC-EU-22"
year: 2022
youtube_id: "vKRUq56xDiE"
sched_url: "https://kccnceu2022.sched.com/event/a2943bd8b232c4008f6a983f208f445b"
---

Within a single cloud provider, accessing secured APIs using your own workload identity is simple. Cloud SDKs used by application developers know how to retrieve identities and credentials from the cloud environment for each workload based on its context. A cloud administrator can then assign permissions to these identities which allow access to the required APIs. This is seamless for developers - simply calling an API in their code just works, while behind the scenes the network call is cryptographically authenticated / authorized. Unfortunately for the user, this identity is cloud-specific. With few alternatives, this often leads to long-lived credentials being mounted into workloads instead. This is less secure and harder to use. This presentation will show an alternative solution which combines features of open source CNCF projects Kubernetes, cert-manager, cert-manager-csi-driver-spiffe, cert-manager-trust and spiffe-connector to expand your SPIFFE trust domain to any cloud.Click here to view captioning/translation in the MeetingPlay platform!
