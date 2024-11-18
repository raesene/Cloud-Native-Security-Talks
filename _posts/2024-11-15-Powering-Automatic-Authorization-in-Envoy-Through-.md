---
title: "Powering Automatic Authorization in Envoy Through Live Traffic Inspection - Dom Del Nano, Pixie core maintainer"
categories: ["KubeCon + CloudNativeCon North America 2024"]
---

## Abstract

The dynamic nature of today’s environments coupled with the importance of data privacy has made AuthN/Z crucial for safeguarding sensitive data. However, many large scale environments existed before these best practices and tooling were commonplace. Retrofitting systems requires a deep understanding of service to service access patterns and requires significant effort to achieve least privilege access. While service dependencies are often difficult to track, the rise of zero instrumentation Observability tools has eased access to this data, providing a potential baseline for AuthZ rules. Projects such as CNCF Pixie and Hubble expose language agnostic protocol traces providing full visibility of their environments. Pixie even supplies access to the span payloads making L7 analysis possible. In this talk, we present a case study of using Pixie to generate OPA policies for Envoy AuthZ using real traffic. This approach provides a starting point for scoping permissions on a L7 basis.

[Sched URL](https://kccncna2024.sched.com/event/845b660c756febe784e70e295b82084f)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/_d5ff8QTmX4' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
