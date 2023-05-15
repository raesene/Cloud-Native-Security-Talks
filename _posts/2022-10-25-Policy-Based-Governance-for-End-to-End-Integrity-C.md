---
title: "Policy-Based Governance for End-to-End Integrity Control of Policies - Yuji Watanabe, IBM Research & Jayashree Ramanathan, Red Hat"
categories: ["Cloud Native SecurityCon North America 2022"]
---

## Abstract

Open Cluster Management (OCM) is a CNCF sandbox project aimed at simplifying and streamlining multi-cluster and multi-cloud management of Kubernetes environments. OCM policy framework simplifies complex and time consuming processes to meet enterprise standards for security and regulatory compliance requirements. The integrity of policies is critical because any modification, maliciously or accidentally, can negatively impact your cluster. This talk describes how you can manage the integrity of the policy resources using the OCM policy framework. We will use manifest signing to protect the integrity of policies. To enable signing, secret values such as the signing key or some sort of access credentials managed on Vault are securely delivered to the signing pipeline by using the policy with a new function called templated secret. The secret values are embedded into the policy and delivered from the hub to the cluster in an encrypted form, and decrypted at the clusters. Admission control to enforce signature verification of policy resources at the cluster is also enabled by using the policy.

[Sched URL](https://cloudnativesecurityconna22.sched.com/event/d97529ca4e86ca918dac5ecac5ea6e60)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/1grSrQ2daxI' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
