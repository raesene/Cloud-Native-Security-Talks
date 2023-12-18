---
title: "Forget Everything You Know About Image Vulnerability and Prioritization - Ben Hirschberg, ARMO"
categories: ["KubeCon + CloudNative North America 2023"]
---

## Abstract

In this talk, we will present research results that highlight the vulnerabilities introduced into a Kubernetes environment when using common public images (e.g. Nginx, Elasticsearch, Kafka, etc). These vulnerabilities are identified using image scanners. However, the resulting long to-do list can overwhelm a team, leaving CVEs that matter unattended for long periods of time. You will come away from this session with new and better practices for prioritizing vulnerability patching. The key being consideration of the actual impact of the identified vulnerabilities on your security posture. The solution leverages eBPF technology to identify and highlight vulnerabilities in running artifacts and libraries. The resulting filtered Software Bill of Materials (SBOM) enables users to automatically detect vulnerabilities whose patching will have an immediate and significant impact on the security posture.

[Sched URL](https://kccncna2023.sched.com/event/c68237b1a35d412e617a83182552936f)

## Video

<iframe src="https://www.youtube.com/embed/ewMbTAmTA-Y" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
