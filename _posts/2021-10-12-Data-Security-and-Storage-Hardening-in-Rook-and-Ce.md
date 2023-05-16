---
title: "Data Security and Storage Hardening in Rook and Ceph- Federico Lucifredi, Red Hat"
categories: ["Cloud Native Security Conference North America 2021"]
---

## Abstract

This talk will be presented by Federico Lucifredi, but features his collaborative work with Ana McTaggart (Red Hat) and Michael Hackett (Red Hat).We explore the security model exposed by Rook with Ceph, the leading software-defined storage platform of the Open Source world. Digging increasingly deeper in the stack, we examine hardening options for Ceph storage appropriate for a variety of threat profiles. Options include defining a threat model, limiting the blast radius of an attack by implementing separate security zones, the use of encryption at rest and in-flight and FIPS 140-2 validated ciphers, hardened builds and default configuration, as well as user access controls and key management. Data retention and secure deletion are also addressed. The very process of containerization creates additional security benefits with lightweight separation of domains. Rook makes the process of applying hardening options easier, as this becomes a matter of simply modifying a .yaml file with the appropriate security context upon creation, making it a snap to apply the standard hardening options of Ceph to a container-based storage system.

[Sched URL](https://cloudnativesecurityconna21.sched.com/event/a870730790be0932ce6b0aa36f053c1a)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/N27rwr0rttM' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
