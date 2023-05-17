---
title: "Using Application Identity to Correlate Metrics: A Look at SPIFFE and SPIRE - Priyanka Sharma, GitLab"
categories: ["KubeCon + CloudNativeCon North America 2018"]
---

## Abstract

In an ideal world, we would have a standardized way to identify running software systems that our monitoring tools could easily lean on, even when spread over multiple teams, geographies, and platforms. But real-world deployments are rarely so simple. I will explain how application identity can be used as the basis for correlating metrics from multiple sources (with the help of OpenTracing) and detail some of the challenges inherent in defining application identity in different contexts (such as virtual machines, functions, and different Kubernetes primitives). I then offer an overview of open source projects like SPIFFE and SPIRE, which have modernized identity authentication across microservices, and demonstrates how SPIRE, Fluentd, Prometheus, and Jaeger can be used together to precisely correlate logs, metrics, and traces to improve and diagnose real-world production issues.

[Sched URL](https://kccna18.sched.com/event/b81b58f72548050dbfd68e37ee83d3db)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/icvjuNCYi7c' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
