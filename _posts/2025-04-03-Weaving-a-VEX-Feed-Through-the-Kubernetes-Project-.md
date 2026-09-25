---
title: "Weaving a VEX Feed Through the Kubernetes Project - Adolfo García Veytia, Stacklok"
categories: ["KubeCon + CloudNativeCon Europe 2025"]
talk_title: "Weaving a VEX Feed Through the Kubernetes Project"
speakers: "Adolfo García Veytia, Stacklok"
event: "KubeCon Europe 2025"
series: "kubecon-eu"
event_code: "KC-EU-25"
year: 2025
youtube_id: "oCbJdcy3zzA"
sched_url: "https://kccnceu2025.sched.com/event/47d0169c3b4a3314b8b1d78b277736bd"
---

Vulnerability triaging is an expensive process, often plagued with false positives that cause organizations to waste thousands of dollars in engineering time handling and suppressing them to conform with compliance frameworks.   Here to the rescue comes VEX - the Vulnerability Exploitability eXchange - a new metadata format, designed as a companion to SBOMs that communicates the impact of a vulnerability on a piece of software.   False positives come in many forms: From vulnerabilities found in other platforms, non-exploitable code paths, to simple mitigations pre applied to artifacts. Using VEX, software authors can communicate downstream that software is safe to use despite security scanners going brrrr..   In this talk, we dive into VEX, explore the new Kubernetes VEX feed instrumented through collaboration from SIG Release, the Security Response Committee and SIG Security to understand the source of the data, how to use it and do some cool demos with real vulnerability scanners!
