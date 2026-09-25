---
title: "Enhancing Software Composition Analysis Resilience Against Container Image Obfuscation - Agathe Blaise, Thales & Jacopo Bufalino, CNAM"
categories: ["KubeCon + CloudNativeCon Europe 2025"]
talk_title: "Enhancing Software Composition Analysis Resilience Against Container Image Obfuscation"
speakers: "Agathe Blaise, Thales & Jacopo Bufalino, CNAM"
event: "KubeCon Europe 2025"
series: "kubecon-eu"
event_code: "KC-EU-25"
year: 2025
youtube_id: "G24upbAXVd8"
sched_url: "https://kccnceu2025.sched.com/event/336523eb10e38c3edc9346b018f0affb"
---

Malicious compliance has been highlighted in previous KubeCon talks as a challenge for software composition analysis, as it conceals OS and package information in container images and hides vulnerabilities. In this talk, we analyze how the landscape evolved over the past two years and propose improvements for SBOM generation. We found that open-source and cloud providers' tools remain vulnerable, which is even more visible in compressed images from public container registries. We uncover another form of malicious compliance with no standardization of package identifier format, resulting in inconsistencies in detected vulnerabilities between SBOM tools. To address this, we introduce an open-source methodology for layer-by-layer container image analysis, reconstructing complete history of file modifications and retrieving package metadata and package-related content, improving file coverage and SBOM accuracy. We finally outline concrete steps for advancing SBOM resilience and accuracy.
