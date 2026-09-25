---
title: "Friends Don’t Let Friends Leave Their Kubernetes Data Unprotected - Rita Zhang, Microsoft"
categories: ["KubeCon + CloudNativeCon North America 2018"]
talk_title: "Friends Don’t Let Friends Leave Their Kubernetes Data Unprotected"
speakers: "Rita Zhang, Microsoft"
event: "KubeCon North America 2018"
series: "kubecon-na"
event_code: "KC-NA-18"
year: 2018
youtube_id: "fkCbq_MhLxo"
sched_url: "https://kccna18.sched.com/event/0aa127e3d317ac5be6d1422868f3a006"
---

In recent headlines, there are increasing news about cloud resources getting hacked caused by attacks on Kubernetes clusters. Failing to properly secure your Kubernetes data can result in cloud resources getting hacked and your application secrets getting stolen. The etcd database contains information that may grant an attacker significant visibility into the state of your cluster.  This presentation focuses on how to use the encryption at rest feature to encrypt secret resources in etcd, preventing parties from gaining access to view the content in etcd and etcd backups. Starting from Kubernetes v1.10, we have added --experimental-encryption-provider-config that controls how API data is encrypted in etcd by KMS providers. We will also look at how you can securely leverage KMS providers as stores for your application secrets, keys, and certs.
