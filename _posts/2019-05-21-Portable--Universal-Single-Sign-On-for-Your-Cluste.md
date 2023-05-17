---
title: "Portable, Universal Single Sign-On for Your Clusters - Miguel Martinez, Bitnami"
categories: ["KubeCon + CloudNativeCon Europe 2019"]
---

## Abstract

In order to enable Single Sign-On in your cluster you need to configure the Kubernetes API server. This is an issue if you are using services where the control plane is managed for you. Some managed services like GKE support SSO out of the box, but are not configurable. Others like AKS allow you to configure it, but only with Active Directory. These options might not fit some of your requirements such as using your company’s existing Identity provider, to use other protocols such as LDAP or SAML or when applications (e.g the Kubernetes Dashboard) need access to the API server.   In this session, I will present some workarounds that leverage other native AuthN/AuthZ mechanisms such as service accounts or impersonation via auth proxies. I will also demo how to use these methods to enable SSO for the Kubernetes dashboard that can be used across different managed and on-prem environments.

[Sched URL](https://kccnceu19.sched.com/event/ade2d0c140d70cf3a1056d769555c343)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/p5x1btmD2Yw' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
