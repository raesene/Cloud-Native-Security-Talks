---
title: "SBOM X-Ray Superpowers: Making Better SBOMs, Using SBOMs - Brandon Lum, Google & Chris Phillips, Anchore"
categories: ["KubeCon + CloudNative North America 2022"]
talk_title: "SBOM X-Ray Superpowers: Making Better SBOMs, Using SBOMs"
speakers: "Brandon Lum, Google & Chris Phillips, Anchore"
event: "KubeCon North America 2022"
series: "kubecon-na"
event_code: "KC-NA-22"
year: 2022
youtube_id: "earq775L4fc"
sched_url: "https://kccncna2022.sched.com/event/361ae1003061c0bb06562a1c2149741d"
---

Creating SBOMs (Software Bill of Materials) for our software artifacts is very important in understanding our software and responding to security attacks/vulnerabilities. However, creating SBOMs is challenging. To be effective, SBOMs must be as accurate and complete as possible, but at the same time be usable. Today, Software Composition Analysis (SCA) based SBOM generation tools strike a great balance in this regard. There are several great SCA-based SBOM generator tools today, but all of them have blind spots, such as finding an executable file that has no metadata associated with it. What if there was a way for SBOM tools to reliably fill in these gaps in order to produce a more complete SBOM? Enter the SBOM X-ray vision! In this talk, we demonstrate a novel way to peek into these opaque files through SBOM discovery and look-up. Through the use of the Rekor transparency log and In-toto attestations, we’ll show how easy it is for existing projects to share SBOM information with other projects using native CI integrations. We will then show our new superpowers in action through the Syft tool to generate more complete SBOMs!
