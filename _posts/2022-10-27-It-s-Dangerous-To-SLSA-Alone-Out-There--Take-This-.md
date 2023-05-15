---
title: "It's Dangerous To SLSA Alone Out There! Take This Artifact Knowledge Graph! - Mihai Maruseac, Google & Michael Lieberman, Independent"
categories: ["KubeCon + CloudNative North America 2022"]
---

## Abstract

By now, we’re getting bored of hearing the “am I affected by X vulnerability?” question. However, as supply chain attacks become more sophisticated, answering just this question is insufficient. Instead, we need to think about: “If TravisCI was compromised, which software is affected? With a bad actor in your supply chain, what's the blast radius?” There is a ton of information today in SBOMs, in-toto/SLSA attestations, etc. However, these documents observed individually provide limited information, but when put together and related, super-additively expand the knowledge base of our software supply chain. We built a supply chain knowledge graph tool to help better understand the relationships between artifacts and their metadata/identities. Through this high-fidelity graph, we not only answer the hard questions posed earlier, but also make new discoveries. For example, we found that most build-systems rely not only on obvious dependencies like gcc, but often overlooked projects like libpcre and sed.

[Sched URL](https://kccncna2022.sched.com/event/acf3ff8c7b802598cf6ed36e41a92eb8)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/xFRNgIEzbkA' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
