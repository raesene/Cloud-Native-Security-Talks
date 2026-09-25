---
title: "Bypass Falco - Leonardo Di Donato, Sysdig"
categories: ["KubeCon + CloudNativeCon North America 2020 Virtual"]
talk_title: "Bypass Falco"
speakers: "Leonardo Di Donato, Sysdig"
event: "KubeCon North America 2020 (Virtual)"
series: "kubecon-na"
event_code: "KC-NA-20"
year: 2020
youtube_id: "nGqWskXRSmo"
sched_url: "https://kccncna20.sched.com/event/53710b7e2c95f8968d9f69829eb11297"
---

The main goal of Falco is to detect malicious behaviors at runtime and alert you about anything undesirable happening inside your machines. Maybe you trust it as your last line of defense in today’s cloud-native environments, and as a consequence, you sleep like a log. Well, I’m a Falco maintainer, and I definitely wouldn’t. Ok, I generally don’t trust anything and still manage to sleep soundly, but that’s a topic for another conversation. You shouldn’t trust Falco. You shouldn’t trust any tool by default. During this session, we’re gonna explore how to bypass Falco and leave us like sitting ducks, defenseless. How? By circumventing the ability of the Falco kernel module or its eBPF probe to trace the syscalls happening into your Linux kernels. Join this talk to get to know the details, and participate in this next-level collective drama.
