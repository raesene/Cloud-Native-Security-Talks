---
title: "Securing Self-Hosted GitHub Actions with Kubernetes and Actions-Runner-Controller - Natalie Somersall, GitHub"
categories: ["CloudNativeSecurityCon North America 2023"]
talk_title: "Securing Self-Hosted GitHub Actions with Kubernetes and Actions-Runner-Controller"
speakers: "Natalie Somersall, GitHub"
event: "CloudNativeSecurityCon North America 2023"
series: "securitycon"
event_code: "CNSC-NA-23"
year: 2023
youtube_id: "Ax4VPm2KrqQ"
sched_url: "https://cloudnativesecurityconna23.sched.com/event/8b839ee3ac3a22b4a664b20bfeb3128e"
---

Self-hosted GitHub Actions runners and Kubernetes are a natural fit, but there's not a lot of guidance on how to put the two together. The leading solution is actions-runner-controller, an open-source community project which provides a controller for autoscaling, ephemeral, and version-controlled compute. It does not, unfortunately, show off how to design and deploy it securely. Natalie leverages her experience building, securing, and advising others in regulated environments to highlight key places where security can be compromised unwittingly. Natalie will overview typical deployment architectures, then cover 3 distinct places where security risk and ease of use collide with insight and resources for navigating these design choices. First the cluster settings are examined to show methods to limit the "blast radius" of a potential bad actor and provide insight into the why and how of using privileged pods. Next, the controller settings are reviewed for how to scope runner deployments and grant permissions within GitHub to provide least-privilege. Lastly, the runner pod is taken apart to show how to build supply chain security into the image and the software it builds for you.
