---
title: "Can You Keep a Secret? on Secret Management in Kubernetes - Liav Yona & Gal Cohen, Firefly"
categories: ["KubeCon + CloudNativeCon Europe 2023"]
---

## Abstract

Our applications today need to interface and communicate with many different services, and many times authenticate to these. This means just to be able to function in a modern cloud native system, applications needs to store and use sensitive data constantly - such as passwords, access keys, certificates (among other private keys), and these sensitive keys have become a core part of the code we write. We’ve learned a long time ago that we can’t have hard-coded secrets, and that’s where tools like Vault or practices like environment variables have come into play. When it comes to Kubernetes, most organizations use Kubernetes secrets by default to secure their private keys and data. However, by design and even in the docs it is clearly stated that these are stored unencrypted in the API server’s underlying data store etcd. Because we have learned the hard way that we need to protect our secrets at all costs, we will take a deep dive on the Secret Store CSI Drive. We’ll understand how it works under the hood, and with multiple credential provider support we’ll demonstrate through code examples how the CDI Driver ensures robust security, least privilege access, and integrates seamlessly into code.

[Sched URL](https://kccnceu2023.sched.com/event/a61cc7881ad822c97e7578299f034ad3)

## Video

<iframe src="https://www.youtube.com/embed/dLOXMEOkLHM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
