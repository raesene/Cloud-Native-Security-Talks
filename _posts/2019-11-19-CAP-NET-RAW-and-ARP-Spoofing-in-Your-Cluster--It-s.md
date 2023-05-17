---
title: "CAP_NET_RAW and ARP Spoofing in Your Cluster: It's Going Downhill From Here - Liz Rice, Aqua Security"
categories: ["KubeCon + CloudNativeCon North America 2019"]
---

## Abstract

Did you know that by default, your applications running in Kubernetes can open raw network sockets? This talk demonstrates how, in the right circumstances, the CAP_NET_RAW capability that allows this can be abused by a compromised application.* ARP spoofing: pretending to represent the wrong IP address* If the app can ARP spoof the IP address of the DNS service, this potentially lets it spoof DNS addresses: pretending to represent the wrong domain nameSounds bad, doesn't it?These attacks, and their consequences, will be demonstrated live, along with preventative measures that you can take to ensure they aren't happening on your cluster.This talk explains CAP_NET_RAW and spoofing, but the audience is expected to be comfortable with Kubernetes concepts like pod specs and admission controllers.

[Sched URL](https://kccncna19.sched.com/event/22edc31a79af412ccce61096e6d39562)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/f-dN8Osm8z0' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
