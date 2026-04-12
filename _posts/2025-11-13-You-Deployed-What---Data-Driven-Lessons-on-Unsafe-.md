---
title: "You Deployed What?! Data-Driven Lessons on Unsafe Helm Chart Defaults - Yossi Weizman, Microsoft"
categories: ["KubeCon + CloudNativeCon North America 2025"]
---

## Abstract

Most breach post-mortems start with “Which CVE?” However, ours usually end with “There wasn’t one.” We analyzed 10 B Kubernetes audit events and scanned over 3000 clusters to map compromise paths that rely solely on insecure defaults shipped by default in widely trusted Helm charts. The pattern is painfully consistent: world-reachable Service/Ingress, authentication set to “off by default,” and a pod that have permissions to go wild. We’ll chain those three defaults against Apache Pinot, Selenium Grid and Meshery all without a single vulnerability.To flip the script, we’ll walk through hardening the same workloads using existing community tools like OPA Gatekeeper, Kyverno, Pod Security Admission, and GitHub Actions to enforce guardrails before someone in your organization is going to deploy an "official" Helm chart.

[Sched URL](https://kccncna2025.sched.com/event/631d858dc3de962ad5a246e5dbf56233)

## Video

<iframe src="https://www.youtube.com/embed/tssAofKij6g" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
