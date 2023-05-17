---
title: "Fine-Grained Permissions in Kubernetes: What’s Missing, and How to Fix That - Vallery Lancey, Lyft & Seth McCombs, Triller"
categories: ["KubeCon + CloudNativeCon Europe 2019"]
---

## Abstract

In this talk, we will walk through a number of common scenarios where Kubernetes lacks sufficient access control tools, or where access control is often not properly applied. For example, it is common for a team to own a subset of services in a namespace, yet RBAC permissions grant that team access to other pods within the namespace.  We will demonstrate a number of solutions available for specific problems, such as pod network policies, the open policy agent, custom controllers that gate API functionality.  We will also discuss problems with the namespace permission model, and possible alternatives. Namespaces create an arbitrary boundary around resources, which creates the need to then bridge those boundaries. We will demonstrate ideas for bridging namespace networks, and posix-style objection permissions within a namespace.

[Sched URL](https://kccnceu19.sched.com/event/8795d700c00ade4fe49923db8dc5df0f)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/TZ73EBP2a9Q' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
