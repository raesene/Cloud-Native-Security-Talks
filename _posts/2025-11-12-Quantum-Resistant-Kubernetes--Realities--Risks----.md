---
title: "Quantum-Resistant Kubernetes: Realities, Risks & (Versioning) Pitfalls - Fabian Kammel, ControlPlane"
categories: ["KubeCon + CloudNativeCon North America 2025"]
---

## Abstract

Post-Quantum Cryptography (PQC) is no longer theoretical. With Go 1.24+ enabling ML-KEM by default, Kubernetes v1.33+ inherits significant quantum resistance for key exchange. This talk dives into the practical realities. We'll briefly cover the current state of PQC standardization, such as ML-KEM (FIPS-203) and then critically examine real-world implications: how K8s "accidentally" already benefits from PQC key exchange, the subtle but critical downgrade risks from mismatched Go versions (e.g., Go 1.23's `X25519Kyber768Draft00` vs. 1.24's `X25519MLKEM768`), and the "tldr.fail" issue where large PQC key shares can break TLS handshakes due to packet size limits. We'll explore these challenges with evidence from the K8s ecosystem, offering insights for maintainers and advanced users navigating the PQC transition.

[Sched URL](https://kccncna2025.sched.com/event/18f775687be4e97fd48a0e5eca4a63e4)

## Video

<iframe src="https://www.youtube.com/embed/3yOwAIpbuQ0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
