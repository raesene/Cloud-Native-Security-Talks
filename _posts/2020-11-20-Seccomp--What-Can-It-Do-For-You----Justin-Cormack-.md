---
title: "Seccomp: What Can It Do For You? - Justin Cormack, Docker"
categories: ["KubeCon + CloudNativeCon North America 2020 Virtual"]
talk_title: "Seccomp: What Can It Do For You?"
speakers: "Justin Cormack, Docker"
event: "KubeCon North America 2020 (Virtual)"
series: "kubecon-na"
event_code: "KC-NA-20"
year: 2020
youtube_id: "Ro4QRx7VPsY"
sched_url: "https://kccncna20.sched.com/event/013004107770c397f893808e4a987b5a"
---

Seccomp is a system call filtering tool built into Linux. It has been used as a security layer in Docker for coming up to five years, and is working through a long path to become on by default in Kubernetes. We look at what seccomp can usefully do to improve real world security, and how best to use it. This talk also covers a reworking of the widely used Docker default seccomp policy, based on experience of security vulnerabilities in the last five years. Seccomp can both be used as a policy in a runtime, and also directly by applications, so both aspects are covered. The policy has also caused a number of usability issues over the years, so we look at the pitfalls involved in using it as syscalls change over time.
