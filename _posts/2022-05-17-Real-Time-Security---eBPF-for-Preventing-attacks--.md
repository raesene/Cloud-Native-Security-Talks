---
title: "Real Time Security - eBPF for Preventing attacks - Liz Rice, Isovalent"
categories: ["Cloud Native SecurityCon Europe 2022"]
talk_title: "Real Time Security - eBPF for Preventing attacks"
speakers: "Liz Rice, Isovalent"
event: "CloudNativeSecurityCon Europe 2022"
series: "securitycon"
event_code: "CNSC-EU-22"
year: 2022
youtube_id: "Xs3MBK17kCk"
sched_url: "https://cloudnativesecurityconeu22.sched.com/event/1358868f12a98401769314858b1fb40c"
---

eBPF is used in several cloud native security tools. In some respects it is already being used for preventative security: - Cilium uses eBPF to enforce NetworkPolicy - Default seccomp profiles - more properly called seccomp-bpf - limit the system calls that applications can use When it comes to runtime security, Falco today uses eBPF to detect suspicious application behavior, but this isn’t preventative - it generates alerts that are used asynchronously to react to malicious events. Is this really the best we can do with eBPF? The answer is a resounding “no”. In this talk we’ll dive into demos and code to explore how eBPF can be used for the next generation of security enforcement tooling. This talk will cover: - Why enforcing NetworkPolicy with eBPF has been in place for years, but preventative security for applications has taken longer - How Phantom attacks can compromise the use of basic system call hooks - How other eBPF attachment points, such as BPF LSM, can be used for preventative security You don’t need to know about eBPF to get the most out of this talk, but you will need a basic understanding of kernel and user space, and a willingness to see some C code.Click here to view captioning/translation in the MeetingPlay platform!
