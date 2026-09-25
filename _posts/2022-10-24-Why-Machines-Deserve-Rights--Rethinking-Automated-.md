---
title: "Why Machines Deserve Rights: Rethinking Automated Infrastructure Access with OSS Teleport Machine ID - Kenneth DuMez, Teleport"
categories: ["Cloud Native SecurityCon North America 2022"]
talk_title: "Why Machines Deserve Rights: Rethinking Automated Infrastructure Access with OSS Teleport Machine ID"
speakers: "Kenneth DuMez, Teleport"
event: "CloudNativeSecurityCon North America 2022"
series: "securitycon"
event_code: "CNSC-NA-22"
year: 2022
youtube_id: "lBqiwrAhdXk"
sched_url: "https://cloudnativesecurityconna22.sched.com/event/0facc389ddd697abd8acbbf1a0068ec8"
---

This talk will focus on the problems of credentials for machines in moderninfrastructure and why it’s imperative you treat your bots the same way you treatyour humans. Typically when using automation for CI/CD or Microservices, teamswill have vaulted credentials shared between worker nodes. This introduceschallenges as these credentials are often long-lived, requiring frequent rotation,introducing both toil and security threats. Open-source Teleport Machine ID mitigatesthese problems by assigning a unique identity with attached RBAC roles baked intounique, short-lived certificates enabling bot users to connect to remote hosts whilecentrally audit-logging all of the machine’s activity. This identity-based access controlplane works seamlessly with all your cloud infrastructure including K8s clusters,databases, and any other remote compute resource. The talk will include anassessment of current legacy automated access solutions, an overview of Teleport,a Machine ID demo, and an in-depth discussion of the technology behind it. Withopen-source Teleport, managing and rotating shared credentials is a thing of thepast. Give the machines rights! Secure your infrastructure.
