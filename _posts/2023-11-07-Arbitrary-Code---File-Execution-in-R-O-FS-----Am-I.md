---
title: "Arbitrary Code & File Execution in R/O FS – Am I Write? - Golan Myers, WithSecure"
categories: ["KubeCon + CloudNative North America 2023"]
---

## Abstract

In containerized environments, such as Kubernetes clusters, read-only filesystems are viewed as an additional layer of defense, as they allow for better control and management of containerized applications. Immutable containers are consistent and predictable, making compliance and auditing simpler, and allowing for more accurate threat detection. They are also easily replicated to ensure high availability and can be rolled back with ease when necessary. In this talk I will present my research on bypassing write and execution restrictions to ultimately execute arbitrary code and executable files in read-only filesystems. The three methods I used to successfully execute arbitrary code will be covered and demonstrated live. We will then cover ways to remediate these attacks where possible and monitor & alert where they are not.

[Sched URL](https://kccncna2023.sched.com/event/47f80c56c1c7365c1535a06648e4142a)

## Video

<iframe src="https://www.youtube.com/embed/jwdz-aYV5xE" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
