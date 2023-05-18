---
title: "Nabla Containers: A New Approach to Container Isolation - Brandon Lum & Ricardo Koller, IBM"
categories: ["KubeCon + CloudNativeCon China 2018"]
---

## Abstract

Horizontal attacks are an important security concern for cloud providers and its tenants. Despite its many advantages, containers have not been accepted as isolated sandboxes, which is crucial for container-native clouds. The exposure of the syscall interface directly to untrusted workloads has greatly increased the number of exploits possible to the host.  We present Nabla containers, which uses library OS/unikernel techniques to avoid system calls and thereby reduce the attack surface on the host kernel. Using our OCI runtime, runnc (https://github.com/nabla-containers/runnc), we show the running of popular applcations: Node.js, python, redis, etc. permitting use of < 9 syscalls via seccomp. In this talk, we will discuss and demo how we have leveraged libOS ideas in a novel way and compare isolation and performance metrics against other technologies such as gvisor and Kata Containers.

[Sched URL](https://kccncchina2018english.sched.com/event/35c5cf52ac9d2b09b2281c5454673596)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/YIsM0zoRzrE' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
