---
title: "Kubernetes + Encrypted Memory = Security * Privacy - Harshal Patil & Pradipta Banerjee, IBM"
categories: ["KubeCon + CloudNativeCon Europe 2019"]
---

## Abstract

The Memory Encryption on hardware is coming soon. From Intel's TME/MKTME[1] to IBM's Ultravisor[2], hardware manufacturers are aiming to make sure 'what's written by the process stays within the process'. Once the hardware is out, it will change the way we perceive the security and privacy in the cloud.   In this talk, we will discuss briefly on the upcoming memory encryption technologies and how we modified kata container runtime to handle kubernetes' Ephemeral Volumes (aka, EmptyDir volumes) to keep your data and application protected from the container image registry (encrypted at rest) to runtime (protected by memory encryption). For the demonstration, we run a container image with the encrypted TensorFlow model using kubernetes such that even the root user on the worker node won’t be able to read the model parameters.  [1] https://goo.gl/Xt3MJf [2] https://goo.gl/X2A5yx

[Sched URL](https://kccnceu19.sched.com/event/8240a0b1edf76c33818e80a7304f45a0)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/pGMdSFlD0_E' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
