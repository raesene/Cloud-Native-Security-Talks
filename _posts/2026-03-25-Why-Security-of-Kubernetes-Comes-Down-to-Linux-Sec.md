---
title: "Why Security of Kubernetes Comes Down to Linux Security - Marina Moore, Edera"
categories: ["KubeCon + CloudNativeCon Europe 2026"]
talk_title: "Why Security of Kubernetes Comes Down to Linux Security"
speakers: "Marina Moore, Edera"
event: "KubeCon Europe 2026"
series: "kubecon-eu"
event_code: "KC-EU-26"
year: 2026
youtube_id: "gaNCXj2j-0Q"
sched_url: "https://kccnceu2026.sched.com/event/c6e0ccec5b3fdef3a7d12d0faa4388cc"
---

Have you ever wondered why so many container escape vulnerabilities stem from vulnerabilities in the Linux kernel? This talk will take you beneath Kubernetes and into the Linux kernel to explore how the underlying kernel impacts your containers. We will look at the history of containers to see how they evolved from Linux containers to today’s cloud native world. We will then dive into Linux features still at work in containers today, with a demo showing these features at work in an unprivileged container. We’ll start with cgroups and namespaces: what do these actually do, and what’s in and out of scope for their protection? We’ll then move on to looking at devices, system calls, and processes in the container to explore what you can see, what you can change, and how OCI runtimes masks work. You’ll walk away with a clearer understanding of Kubernetes security rooted in an understanding of the underlying Linux kernel and how you can access it from within a container.
