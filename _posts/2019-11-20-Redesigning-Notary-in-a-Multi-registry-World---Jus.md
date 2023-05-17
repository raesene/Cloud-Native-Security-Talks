---
title: "Redesigning Notary in a Multi-registry World - Justin Cormack, Docker"
categories: ["KubeCon + CloudNativeCon North America 2019"]
---

## Abstract

Notary, used to secure container image updates, is the most widely adopted implementation of the TUF protocol. However, since Notary’s design around Docker Hub in 2015, container registries have proliferated and some of the design decisions don’t support the needs of a multi-registry world. This talk looks at redesigning the model to allow portability of container images between registries with signature data stored alongside the image data allowing it to be pushed and pulled alongside the image. This reworking of Notary will enable easier portability of images, and improve supply chain security by enabling mirrors and users of mirrors to validate image data, allowing users to easily work with cloud and local registries, offline caches and other common architectures.

[Sched URL](https://kccncna19.sched.com/event/3ee5d41422f504b4fce0124cc8d93d59)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/rB8-rUtrtXM' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
