---
title: "The Next Log4jshell?! Preparing for CVEs with eBPF! - Natalia Reka Ivanko & John Fastabend, Isovalent"
categories: ["KubeCon + CloudNativeCon Europe 2023"]
talk_title: "The Next Log4jshell?! Preparing for CVEs with eBPF!"
speakers: "Natalia Reka Ivanko & John Fastabend, Isovalent"
event: "KubeCon Europe 2023"
series: "kubecon-eu"
event_code: "KC-EU-23"
year: 2023
youtube_id: "u8HKg5pENj4"
sched_url: "https://kccnceu2023.sched.com/event/cc3dafbcc991f0b1b842ef96552a1f69"
---

Log4jshell, which has been considered the biggest 0 day vulnerability of this decade, is still affecting thousands of servers worldwide. If you were affected, would it have been any different if you had used eBPF? Could you observe the malicious external connection, the JNDI lookup, the Java class download, or the remote code execution? Or even better, could you prevent it? Since eBPF provides us with a unique visibility directly into any Kubernetes workload on a single shared kernel - the answer is yes. This talk will take Log4jshell as a learning lesson and show you how it could have been detected and blocked in real time inside the kernel using eBPF. We will walk you through how open source eBPF based tools can give full network and process-level visibility to detect and prevent Log4jshell and your next CVE. We’ll finish by showcasing how Security Teams can easily put these tools in place to protect their critical Kubernetes environment and by giving Security best practices on how to prepare for their next CVE with eBPF.
