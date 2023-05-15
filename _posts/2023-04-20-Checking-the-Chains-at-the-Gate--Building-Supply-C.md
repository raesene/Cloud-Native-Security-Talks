---
title: "Checking the Chains at the Gate: Building Supply Chain Policies with Gatekeeper and Ratify - Jeremy Rickard, Microsoft"
categories: ["KubeCon + CloudNativeCon Europe 2023"]
---

## Abstract

If you're running Kubernetes in production, you've probably thought about how to keep your clusters and their workloads in compliance with corporate or regulatory policies. In Kubernetes, you'll probably do this with an admission controller. An admission controller intercepts requests to the Kubernetes API server and allows you to validate or change it. Gatekeeper is an Open Polciy Agent based admission controller that enables enforcement of CRD-based policies. These policies normally act on data within the request or other static data within your cluster. However, sometimes that's not enough. As Software Supply Chain security becomes more important, our policies need to consider more external artifacts. Maybe you want to verify that images are signed or that the SBOM for a service doesn't have that latest OpenSSL CVE. Gatekeeper's external data feature allows you to do just this, through the use of plugin providers. Ratify is an open source project that enables verification of supply chain artifacts and can act provider for Gatekeeper. In this talk, Jeremy will show how to you can use Gatekeeper, Ratify, and OCI registries to develop supply chain security focused policies for your clusters, as well as how to write your own custom verifiers to meet evolving policy requirements.

[Sched URL](https://kccnceu2023.sched.com/event/9115867d0aab379e92b905fb376e22fc)

## Video

<iframe src="https://www.youtube.com/embed/pj8Q8nnMQWM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
