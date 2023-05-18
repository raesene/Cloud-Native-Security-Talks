---
title: "The State of Your Supply Chain - Andrew Martin, ControlPlane & Maya Kaczorowski, Google"
categories: ["KubeCon + CloudNativeCon China 2018"]
---

## Abstract

Container security often focuses on runtime best-practices whilst neglecting the software shipped in the supply chain. Application or library vulnerabilities are a likely route to data exfiltration, and containers offer a new opportunity to mitigate this risk.   Treating containers as immutable artefacts allows us to "upgrade" images by rebuilding and shipping whole images, avoiding configuration drift and state inconsistencies. This makes it possible to constantly patch software, and to easily enforce what is deployed into our environments.  In this talk we detail an ideal software supply chain, describe the current state of the ecosystem, and dig into specific tools. Grafeas, Kritis, in-toto, Clair, Micro Scanner, TUF, and Notary are covered, and we demo how to identify a vulnerable image then automatically rebuild and redeploy it.

[Sched URL](https://kccncchina2018english.sched.com/event/9ead0b9cc37127d25bcac6b845387863)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/uDWXKKEO8NU' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
