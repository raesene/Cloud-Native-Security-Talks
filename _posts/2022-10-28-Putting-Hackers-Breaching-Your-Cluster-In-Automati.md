---
title: "Putting Hackers Breaching Your Cluster In Automatic Quarantine - Ziv Nevo, IBM"
categories: ["KubeCon + CloudNative North America 2022"]
talk_title: "Putting Hackers Breaching Your Cluster In Automatic Quarantine"
speakers: "Ziv Nevo, IBM"
event: "KubeCon North America 2022"
series: "kubecon-na"
event_code: "KC-NA-22"
year: 2022
youtube_id: "RF9X1XRJ5Ko"
sched_url: "https://kccncna2022.sched.com/event/f53615c61522ae4ae918f6542dea4c0a"
---

Engineers can’t really prevent hackers form eventually breaching Apps. It is not a question of IF but of WHEN. And unfortunately, a question of how much damage was done to our or our users’ resources, data and reputation. This does not happen only to small Apps and companies with small budgets and limited resources but to huge companies and government agencies (see SolarWinds attack). The solution - automatically isolating attackers when they breach one of the Apps in your cluster (or the App you develop), keeping the rest of the cluster’s components safe. This session will present a survey encompassing many commonly used cloud native apps, engineers all love and need (like Prometheus, Kafka, Jenkins, ClearML and much more) and demonstrate the built-in vulnerability most cluster deployments exercise and how to secure it. State of the art practices leave several, rather easily breached, back doors in many clusters. We will deep dive into several real-world scenarios and see the simple, yet very often missed, blueprint for making our cluster or our App-users’ clusters much more malicious-resistant.
