---
title: "The Eye of Falco: You Can Escape but Not Hide - Stefano Chierici & Lorenzo Susini, Sysdig"
categories: ["Cloud Native SecurityCon North America 2022"]
talk_title: "The Eye of Falco: You Can Escape but Not Hide"
speakers: "Stefano Chierici & Lorenzo Susini, Sysdig"
event: "CloudNativeSecurityCon North America 2022"
series: "securitycon"
event_code: "CNSC-NA-22"
year: 2022
youtube_id: "j3PcSGlJcZI"
sched_url: "https://cloudnativesecurityconna22.sched.com/event/67a115c1cfb7d4ad80b2b80b3c0d4ea9"
---

Container technologies rely on features like namespaces, cgroups, SecComp filters, and capabilities to isolate different services running on the same host. However, SPOILER ALERT: container isolation isn’t bulletproof. Similar to other security environments, isolation is followed by red-teamer questions such as, “How can I de-isolate from this?” Designed with the principle of least privilege in mind, capabilities provide a way to isolate containers, splitting the power of the root user into multiple units. However, having lots of capabilities introduces complexity and a consequent increase of excessively misconfigured permissions and container escape exploits, as we have seen in recently discovered CVEs. Fortunately using Falco, a CNCF container runtime security tool, it’s possible to monitor Linux capabilities, detect misconfigured containers, and proactively respond to secure environments. In this talk, we explain how you can use Falco to detect and monitor container escaping techniques based on capabilities. We walk through show real-world scenarios based on recent CVEs to show where Falco can help in detection and automatically respond to those behaviors
