---
title: "Exploring NRI for Automated CA Trust Injection - Tsuzuki Tsuchiya & Kento Kubo, LY Corporation"
categories: ["KubeCon + CloudNativeCon Europe 2026"]
---

## Abstract

Large organizations use private CAs, but public container images lack their certificates. Today, fixing this means operators must manually build new images, or use Init Containers. However, manually installing these CAs in thousands of containers is complex and unreliable. In addition, many OS and programming languages often installs certificates differently. We will demonstrate a novel approach using the Node Resource Interface (NRI) to automatically inject private CA certificates into every relevant container upon startup. This eliminates per-pod customization, enforces organization-wide trust policies, and streamlines operations for secure, large-scale Kubernetes deployments without modifying base images. Attendees will learn how NRI can solve real-world security and operations challenges and we'll explore the potential of NRI as the new extension point for automating tasks.

[Sched URL](https://kccnceu2026.sched.com/event/1223b15626477edd2abba339367132e4)

## Video

<iframe src="https://www.youtube.com/embed/6qvsce4t2_w" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
