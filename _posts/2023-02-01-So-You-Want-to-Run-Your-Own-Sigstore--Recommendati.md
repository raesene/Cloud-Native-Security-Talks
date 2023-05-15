---
title: "So You Want to Run Your Own Sigstore: Recommendations for a Secure Setup - Hayden Blauzvern, Google"
categories: ["CloudNativeSecurityCon North America 2023"]
---

## Abstract

Sigstore, an open-source standard for signing and verifying artifacts, provides free-to-use services that provide identity-based certificates and auditable signatures through a transparency log. These services work well for FOSS, giving maintainers the tooling needed to create signed builds. However, enterprise organizations may have additional needs that are not addressed by the public instances. This could include availability requirements such as regionalization, data residency requirements, privacy concerns with a public log, or requiring policy controls for admitting entries into a log. This talk will discuss motivations for operating private Sigstore services and expectations on the operators. The talk will discuss differences in the threat modeling between public and private instances. Finally, the talk will cover the requirements for operating private instances, including operating a root trust store and the necessary security properties of a private certificate authority and transparency log.

[Sched URL](https://cloudnativesecurityconna23.sched.com/event/080eb5eac300702a6c02e4bc110cd316)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/0OFVxF-Lvuk' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
