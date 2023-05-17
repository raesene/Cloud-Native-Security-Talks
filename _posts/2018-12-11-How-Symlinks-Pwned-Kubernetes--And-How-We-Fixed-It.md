---
title: "How Symlinks Pwned Kubernetes (And How We Fixed It) - Michelle Au, Google & Jan Šafránek, Red Hat"
categories: ["KubeCon + CloudNativeCon North America 2018"]
---

## Abstract

Ever wonder how Kubernetes deals with security vulnerabilities? This talk illustrates the process by walking through the discovery, patching, and disclosure of CVE-2017-1002101.  In Nov 2017, we received a report about how misusing the volume subpath feature could result in access to host files. A team was assembled to investigate the vulnerability, develop a patch, and release it to all supported versions of Kubernetes -- ALL in secret.  As we walk through the story from discovery to disclosure, we will also deep dive into the technical details of how this feature allowed a container to escape to the host filesystem, and how it was fixed.  You will walk away with techniques for secure file handling in multi-tenant environments, best practices for restricting volume access in your Kubernetes clusters, and an understanding of how a large open source project manages security issues.

[Sched URL](https://kccna18.sched.com/event/8d2fbb4fc138f490d265bbe5012e346f)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/o8hQ4WFd75U' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
