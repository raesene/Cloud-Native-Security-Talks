---
title: "Piloting Around the Rocks: Avoiding Threats in Kubernetes - Robert Tonic & Stefan Edwards, Trail of Bits"
categories: ["KubeCon + CloudNativeCon North America 2019"]
talk_title: "Piloting Around the Rocks: Avoiding Threats in Kubernetes"
speakers: "Robert Tonic & Stefan Edwards, Trail of Bits"
event: "KubeCon North America 2019"
series: "kubecon-na"
event_code: "KC-NA-19"
year: 2019
youtube_id: "ngOcy_FTPRU"
sched_url: "https://kccncna19.sched.com/event/e590e929056a27418462e04008d20fe8"
---

Over three months in 2019, Trail of Bits completed the first-ever security review of Kubernetes, consisting of source review, dynamic testing, and threat modeling. One artifact, the threat model, lets users understand the risks of any given feature or deployment. We’ll show attendees how to make the most of this invaluable resource.First, we’ll break down the architecture of Kubernetes into trust zones. These are security boundaries where controls should be enforced. Incorrectly implemented controls can result in catastrophic security failures.After we describe the trust zones, you’ll find the architectural issues are easy to identify. We’ll discuss a few! We’ll also situate vulnerabilities we found in our code review into each trust zone.Finally, we’ll teach you how to review your own Kubernetes environment using our threat model to get simple answers to your security questions.
