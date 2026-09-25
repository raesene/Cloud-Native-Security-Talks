---
title: "Identity-based Trust - Till Death Do We Part? - John Kjell, ControlPlane & Kairo De Araujo, Independent"
categories: ["KubeCon + CloudNativeCon Europe 2025"]
talk_title: "Identity-based Trust - Till Death Do We Part?"
speakers: "John Kjell, ControlPlane & Kairo De Araujo, Independent"
event: "KubeCon Europe 2025"
series: "kubecon-eu"
event_code: "KC-EU-25"
year: 2025
youtube_id: "26p_qvuCy-s"
sched_url: "https://kccnceu2025.sched.com/event/62185ac6b110e802ebd3bdcae47e6bc5"
---

With the rise in adoption of identity-based trust, it is increasingly important to understand the threats to such systems. PyPI, NPM, RubyGems, and Homebrew have all established models for “trusted publishing” attestation, based on OIDC. Many of these implementations rely on Project Sigstore’s projects Fulcio and Rekor.Sigstore’s Rekor is an append only log. There’s no way to remove entries, even if they’re illegitimate. In the case of an identity compromise, most individuals would prefer to avoid a divorce from their identity, allowing for recovery and the establishment in future trust of their name.In this session, we’ll examine a threat model and mechanisms for compromise in a Sigstore-based identity signing system. Once established, we’ll describe ways to mitigate and resolve the threats, leveraging the CNCF projects in-toto and The Update Framework (TUF). Beyond theoretical designs, we’ll look at how this system has been implemented in in-toto’s sub-project Archivista.
