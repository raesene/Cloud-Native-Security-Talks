---
title: "When Multitenancy Goes Wrong: A Deep Dive Into Kcp’s First CVE - Marvin Beckers, ClickHouse"
categories: ["KubeCon + CloudNativeCon Europe 2026"]
---

## Abstract

kcp, a CNCF Sandbox project, is a control plane for serving Kubernetes-style APIs built on top of Kubernetes core libraries with a strong focus on multitenancy. But what happens when isolation, a core pillar of multitenancy, begins to crumble?   Meet CVE-2025-29922, initially rated with “Medium” severity, turning into a “High” 9.6 scored beast. We'll explore virtual workspaces, a kcp feature that provides a "single pane of glass" for service providers to see and manage their resources across many different tenants. The flaw in the implementation, however, was that service providers could create and delete resources they had no permissions for.   In this deep dive, we’ll demonstrate how an innocent looking vulnerability, discovered because of a discrepancy between docs and code, can lead to a total takeover of tenants and their data. We’ll show the complete thought process behind discovering this attack vector. At the end, we’ll talk about what measures we took to protect kcp users.

[Sched URL](https://kccnceu2026.sched.com/event/12467c3e009b6f26575b8c551ef1067c)

## Video

<iframe src="https://www.youtube.com/embed/6pFY8lrTOKw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
