---
title: "See It to Believe It: Bringing Observability to Otherwise Opaque Container Builds - Parth Patel, Kusari & Shripad Nadgowda, Intel"
categories: ["Cloud Native SecurityCon North America 2022"]
talk_title: "See It to Believe It: Bringing Observability to Otherwise Opaque Container Builds"
speakers: "Parth Patel, Kusari & Shripad Nadgowda, Intel"
event: "CloudNativeSecurityCon North America 2022"
series: "securitycon"
event_code: "CNSC-NA-22"
year: 2022
youtube_id: "5iyWcUsHMFM"
sched_url: "https://cloudnativesecurityconna22.sched.com/event/39e3733ecc513d6451d7ce97879f2db7"
---

Container build is arguably one of the most security sensitive operations in the whole application supply chain spectrum, which has largely remained opaque to date. It is typically implemented as a multi-stage process in the Continuous Integration (CI) pipeline that includes cloning the source code, resolving and downloading dependencies, compiling and packaging applications and finally publishing the built artifacts. To establish trust in the final built artifact, it is not sufficient to ensure security guarantees around just the built artifact, but it is critical to provide provenance and integrity assurance for every action in the pipeline that went into building that artifact. While tools, such as Tekton Chains, provide visibility into the steps that were performed and components that were used during the build process, we are still missing the lower level syscalls that were made. In this presentation, Parth and Shripad will present an open framework using tetragon to bring out-of-band runtime visibility and provide automated attestation for tekton based CI pipeline.
