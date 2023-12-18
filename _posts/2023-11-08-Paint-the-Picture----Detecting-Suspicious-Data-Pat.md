---
title: "Paint the Picture! - Detecting Suspicious Data Patterns in Encrypted Traffic with eBPF and KTLS - Natalia Reka Ivanko & John Fastabend, Isovalent"
categories: ["KubeCon + CloudNative North America 2023"]
---

## Abstract

Using eBPF to detect malicious events on Cloud Native environments continues to rise because it provides a wide range of options to monitor for suspicious runtime execution, network connections, and file access. However, detecting sensitive data patterns, like social security or credit card numbers in encrypted L7 network traffic has traditionally been done in user space. By leveraging in-kernel HTTP visibility and kTLS, we now have the ability to paint a complete security picture and monitor sensitive data flows between Kubernetes workloads, even if they are encrypted. Using Tetragon, this talk will demonstrate how eBPF can be applied to solve the technical challenge of decrypting TLS traffic by using kTLS and showcase how Security Teams can detect sensitive data patterns, like social security numbers or exploit signatures in encrypted L7 traffic. By using eBPF, this solution avoids operational complexity, overhead, and is fully transparent to the application as well as the CNI.

[Sched URL](https://kccncna2023.sched.com/event/745732d7c20673344164817495327271)

## Video

<iframe src="https://www.youtube.com/embed/-2FykHaqvlg" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
