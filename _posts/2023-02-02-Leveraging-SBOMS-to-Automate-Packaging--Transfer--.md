---
title: "Leveraging SBOMS to Automate Packaging, Transfer, and Reporting of Dependencies Between Secure Environments - Ian Dunbar-Hall & Jerod Heck, Lockheed Martin"
categories: ["CloudNativeSecurityCon North America 2023"]
---

## Abstract

Software Bill of Materials are being touted for tracking software build dependencies and security of a built application. Often delivered with built applications for transparency. In this talk we’ll explore a different use for Software Bill of Materials, where it is used as a packaging standard to validate and transfer assets across network boundaries. At Lockheed Martin, we’re using CycloneDX Specification to automate transfers into secure environments with strict controls to allow development teams to update build dependencies without network connectivity. We also use the CycloneDX Specification to create “seeding” deployments for Cloud Native infrastructure deployments. We’ll be demoing Hoppr, an open source tool with an extendable plugin architecture to do security validation and multi team transfers. It used CycloneDX SBOMs to collect items based on purls, run validation, and create transfers to be brought into these environments.

[Sched URL](https://cloudnativesecurityconna23.sched.com/event/b0ee7051c0a3b790cf3583ee973a8334)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/8gp255Tfz_4' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
