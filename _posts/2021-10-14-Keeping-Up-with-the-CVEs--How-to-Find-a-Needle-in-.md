---
title: "Keeping Up with the CVEs: How to Find a Needle in a Haystack? - Pushkar Joglekar, VMware"
categories: ["KubeCon + CloudNative North America 2021"]
talk_title: "Keeping Up with the CVEs: How to Find a Needle in a Haystack?"
speakers: "Pushkar Joglekar, VMware"
event: "KubeCon North America 2021"
series: "kubecon-na"
event_code: "KC-NA-21"
year: 2021
youtube_id: "2cvWmY4xvLU"
sched_url: "https://kccncna2021.sched.com/event/580ae5dcf445dd481c58c5a98587175d"
---

An end user team bought a new product that ships as a set of container images. Their CISO requests a scan of the images before going live. The internal scan, to everyone’s surprise results in 314159 vulnerabilities. The CISO is furious & rejects any claims that the scanner is faulty, since it worked fine for VM images. After multiple back and forth exchanges with the product’s vendor, the vast majority of the detected vulnerabilities are false positives / do not have a fix / are not in the code execution path. Everyone breathes a sigh of relief until a few weeks later, the same thing happens for another product & the story repeats itself. It does not have to be this way! In this talk using the Kubernetes images as an example we will unravel how vulnerability scanners work, their blind spots and discuss how to implement a practical approach that allows end users to assess product’s security not by the raw vulnerability numbers & severity but by the risk it poses to their environment.
