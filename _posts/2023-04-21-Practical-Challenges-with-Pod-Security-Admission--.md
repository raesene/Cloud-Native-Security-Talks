---
title: "Practical Challenges with Pod Security Admission - V Körbes & Christian Schlotter, VMware"
categories: ["KubeCon + CloudNativeCon Europe 2023"]
---

## Abstract

A big reason we love Pod Security Admission is that it's so easy and simple to use. But here's a challenge that comes with implementing Pod Security Admission: there's always a workload that needs too many privileges to run, and then it needs to get a pass from the security controls. One way to address this unsecured footprint is to break down all the different services, applications, and packages into their separate component parts, leaving the bits that need privileges privileged, and locking down everything else. There's a whole art to that – we'll talk about it. But 'principle of least privilege' doesn't mean zero privilege so... What do we do when that privilege gets exploited? We welcome it with a node that has nothing valuable whatsoever, is what! And there's a whole art to that too – we'll talk about it. In this presentation attendees will get an overview of the challenges that come with implementing Pod Security Admission in the real world, and tap on the speaker's experience working with partner companies to solve them.

[Sched URL](https://kccnceu2023.sched.com/event/c47fda525b082c547a0f92dfaa68810f)

## Video

<iframe src="https://www.youtube.com/embed/DO32j_MYbHU" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
