---
title: "Leveraging OCI 1.1 for Enhanced SBOM Integration and Vulnerability Scanning in Harbor - Anais Urlichs, Aqua Security & Shengwen Yu, VMware"
categories: ["KubeCon + CloudNativeCon Europe 2024"]
talk_title: "Leveraging OCI 1.1 for Enhanced SBOM Integration and Vulnerability Scanning in Harbor"
speakers: "Anais Urlichs, Aqua Security & Shengwen Yu, VMware"
event: "KubeCon Europe 2024"
series: "kubecon-eu"
event_code: "KC-EU-24"
year: 2024
youtube_id: "ABbds5-zSqk"
sched_url: "https://kccnceu2024.sched.com/event/f212e4fd5faada1cf1d947266bb1e58d"
---

With the rise in software supply chain attacks, stakeholders in the software industry become more interested in the supply chain security utilizing SBOM (Software Bill of Materials). This talk will focus on the SBOM integration between Harbor project and Aqua Trivy scanner. Currently, Harbor supports manually attaching SBOM artifacts to its subject image as an accessory. Leveraging OCI distribution-spec 1.1, SBOM can be auto-generated and auto-associated, which enhances the visibility of the software building process. Additionally, the SBOM scanning capability in Harbor will streamline vulnerability scanning by eliminating the procedure of repeatedly analyzing container images, making the scanning process more efficient. Furthermore, the new Harbor scanner pluggable spec provides compatibility and flexibility. This session will give a demo to show SBOM generation and SBOM scanning for vulnerabilities, providing practical insights for large-scale containers security management.
