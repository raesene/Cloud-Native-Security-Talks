---
title: "Secure Container with SGX: Protecting Secret in Cloud Environment - Isaku Yamahata, Intel & Xiaoning Li, Alibaba"
categories: ["KubeCon + CloudNativeCon | Open Source Summit China 2019"]
talk_title: "Secure Container with SGX: Protecting Secret in Cloud Environment"
speakers: "Isaku Yamahata, Intel & Xiaoning Li, Alibaba"
event: "KubeCon China 2019"
series: "kubecon-china"
event_code: "KC-CN-19"
year: 2019
youtube_id: "GMjtChZLb8Y"
sched_url: "https://kccncosschn19eng.sched.com/event/2c4bdf3fe90cea6eea8f31346eac2cd3"
---

In cloud computing container is widely adapted, but its isolation is weak. It's important to protect secrets even from cloud service provider. Software Guard Extention(SGX) provides Trusted Execution Environment(TEE) where only Intel and SGX implementation is trusted with untrusted OS/VMM/BIOS. It requires to modify applications which is sometimes difficult for various reasons. Ideally unmodified user binary can run in SGX enclave.  In this talk, Library OS to allow unmodified binary to run within SGX TEE is introduced. It hooks system call by replacing shared library. Go is most popular language for cloud native applications with uniqueness to use static link. We enhanced Graphene LibOS to support golang binary and hardened it for production use. We will share our experience to add golang support to Graphene-SGX LibOS and our future plan.
