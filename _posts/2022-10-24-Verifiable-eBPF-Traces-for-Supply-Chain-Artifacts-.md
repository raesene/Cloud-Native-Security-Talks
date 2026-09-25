---
title: "Verifiable eBPF Traces for Supply Chain Artifacts with Witness and Tetragon - Cole Kennedy, TestifySec"
categories: ["Cloud Native SecurityCon North America 2022"]
talk_title: "Verifiable eBPF Traces for Supply Chain Artifacts with Witness and Tetragon"
speakers: "Cole Kennedy, TestifySec"
event: "CloudNativeSecurityCon North America 2022"
series: "securitycon"
event_code: "CNSC-NA-22"
year: 2022
youtube_id: "zCznRGlsYvo"
sched_url: "https://cloudnativesecurityconna22.sched.com/event/16d0ca164af7a650c1758240d62bbd8a"
---

Until now, validating the build environment and detecting tampered tooling in a build has been very difficult. This talk will show how Cillium Tetragon and Witness integration simplifies this process for developers and security engineers. Witness is a framework for supply chain security that implements the in-toto specification. It has a modular design, easily extendable for various attestors, backends, and key providers (including SPIFFE/SPIRE). This talk will show an attestation plugin that programs Cillum Tetragon to provide detailed eBPF traces of a build step. Additionally, we will create a build policy that verifies the trace and blocks the execution of workload compiled by a malicious compiler when the compiled workload is executed.
