---
title: "Container Isolation at Scale (Introducing gVisor) - Dawn Chen & Zhengyu He, Google (Intermediate Skill Level) (Slides Attached)"
categories: ["KubeCon + CloudNativeCon Europe 2018"]
---

## Abstract

Containers are the modern way of running your services at scale because of the portability and lightweightness. However, due to the fact that they depend on OS multi-tenancy as they share the same host OS (usually Linux which represents a large attack surface), containers are considered providing weaker isolation than virtual machines.  We will start from discussing the security principles in running services in Google, and then summarize a list of best practices we have explored for preventing, auditing and mitigating security threats. Specifically, we will focus on the challenges we have faced at the host operating system level.

[Sched URL](https://kccnceu18.sched.com/event/207d612717989beb8787aad627a0540c)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/I4AchBfe49U' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
