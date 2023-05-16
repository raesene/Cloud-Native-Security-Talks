---
title: "Replacing PSPs? Keep Bad Pods out of your cluster using Kyverno!- Shuting Zhao, Nirmata"
categories: ["Cloud Native Security Conference North America 2021"]
---

## Abstract

Securing sensitive aspects of the Pod specification has always been difficult but it has become more challenging now with the deprecation of PodSecurityPolicy (PSP). So how can you continue to ensure that “Bad Pods” stay out of your cluster and don’t compromise the security posture?   Kyverno, an admission controller, provides a Kubernetes native solution to set and validate security context, not only for pods but also for all the pod controllers. In addition to admission review, Kyverno can be run in audit mode. In this mode, Kyvero does not impact existing clusters but audits the cluster and reports any security violations in policy reports. Kyverno also provides the Command Line Tool (CLI) to support “dry run” so that you can easily execute policies in your CI/CD pipeline and generate reports without having to deploy Kyverno to your cluster.  In this talk, Shuting Zhao will provide an overview of Kyverno and present a set of Kyverno policies for Pod that is based on Pod Security Standards. She will demonstrate how to generate policy reports for existing clusters. She will also demonstrate how Kyverno can enforce best practices for Pod security. Lastly, she will show how Kyverno can help add default security context to Pods and improve the security posture of your clusters. 

[Sched URL](https://cloudnativesecurityconna21.sched.com/event/88ffeb6e533753365ab65b24586a28ac)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/AmJUFH7n33c' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
