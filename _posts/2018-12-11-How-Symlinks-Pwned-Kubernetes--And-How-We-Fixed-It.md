---
title: "How Symlinks Pwned Kubernetes (And How We Fixed It) - Michelle Au, Google & Jan Šafránek, Red Hat"
categories: ["KubeCon + CloudNativeCon North America 2018"]
talk_title: "How Symlinks Pwned Kubernetes (And How We Fixed It)"
speakers: "Michelle Au, Google & Jan Šafránek, Red Hat"
event: "KubeCon North America 2018"
series: "kubecon-na"
event_code: "KC-NA-18"
year: 2018
youtube_id: "o8hQ4WFd75U"
sched_url: "https://kccna18.sched.com/event/8d2fbb4fc138f490d265bbe5012e346f"
---

Ever wonder how Kubernetes deals with security vulnerabilities? This talk illustrates the process by walking through the discovery, patching, and disclosure of CVE-2017-1002101.  In Nov 2017, we received a report about how misusing the volume subpath feature could result in access to host files. A team was assembled to investigate the vulnerability, develop a patch, and release it to all supported versions of Kubernetes -- ALL in secret.  As we walk through the story from discovery to disclosure, we will also deep dive into the technical details of how this feature allowed a container to escape to the host filesystem, and how it was fixed.  You will walk away with techniques for secure file handling in multi-tenant environments, best practices for restricting volume access in your Kubernetes clusters, and an understanding of how a large open source project manages security issues.
