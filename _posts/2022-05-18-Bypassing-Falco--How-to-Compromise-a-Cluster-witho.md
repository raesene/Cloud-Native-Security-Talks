---
title: "Bypassing Falco: How to Compromise a Cluster without Tripping the SOC - Shay Berkovich, BlackBerry"
categories: ["KubeCon + CloudNativeCon Europe 2022"]
---

## Abstract

The explosive growth of Kubernetes has left security professionals scrambling to deploy innovative tools to address the inherent security risks. One such tool is The Falco Project - an incubating CNCF tool for detecting malicious activity at run time. Falco, like many security tools, has some gaps. This talk highlights these gaps by introducing various techniques to silently bypass the default Falco ruleset (based on Falco v0.30.0 release). The attendees will learn 9 different classes of bypasses, 7 of which are novel and have never been presented. The bypasses allow for stealthy target enumeration, privilege escalation and lateral movement. To aid with the bypass automation, Shay will introduce a special container image and multiple code snippets built specifically for Falco bypasses. To wrap up, we will apply the bypass techniques on securekubernetes cluster (presented on KubeCon NA 2019) and demonstrate how an attacker can achieve full cluster compromise without tripping the SOC.Click here to view captioning/translation in the MeetingPlay platform!

[Sched URL](https://kccnceu2022.sched.com/event/368d82b76e276cf6195b15edd3970e2d)

## Video

<iframe src="https://www.youtube.com/embed/2rSiSpaR6bI" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
