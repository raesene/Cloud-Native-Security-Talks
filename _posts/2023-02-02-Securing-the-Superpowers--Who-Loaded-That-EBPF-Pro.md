---
title: "Securing the Superpowers: Who Loaded That EBPF Program? - John Fastabend & Natalia Reka Ivanko, Isovalent"
categories: ["CloudNativeSecurityCon North America 2023"]
talk_title: "Securing the Superpowers: Who Loaded That EBPF Program?"
speakers: "John Fastabend & Natalia Reka Ivanko, Isovalent"
event: "CloudNativeSecurityCon North America 2023"
series: "securitycon"
event_code: "CNSC-NA-23"
year: 2023
youtube_id: "UBVTJ0LeXxc"
sched_url: "https://cloudnativesecurityconna23.sched.com/event/503098372a0ec8059db8986da5c2d362"
---

eBPF has become an increasingly popular technology to build all sort of tools from networking CNIs to security tools. eBPF has the ability to inspect nearly any kernel data structure and modify networking packets and even user space data in some configurations. It has recently become cross platform with a Windows run-time and is now widely available on most Linux distributions and cloud platforms. It even has users at Blackhat (BlackHat USA 2021: With Friends Like eBPF, Who Needs Enemies?) and Defcon creating potential malicious uses for eBPF. Precisely because it is so powerful it is incredibly useful, but it raises the question who is watching eBPF. The Linux kernel community has been building a solution to securely monitor and enforce who can load eBPF programs and what kind of programs are allowed to be loaded on any given system. In this talk we discuss a design for eBPF auditing and security and use Tetragon's (an open source eBPF based security tool) to show an implementation. This will show security teams how to restrict what gets loaded on a Linux system and who is allowed to use it. As well as how to create an audit log and time series database so we can go back in time to discover the who did what, when type of questions that can not be answered today.
