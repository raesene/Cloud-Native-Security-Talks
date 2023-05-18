---
title: "Sentinel: A Platform for Fine-grained Application Security - Sudheendra Murthy, eBay, Inc."
categories: ["CloudNativeCon + KubeCon 2016"]
---

## Abstract

This talk presents Sentinel, a platform for security policy management that is currently being used to secure workloads running on eBay's cloud. Sentinel provides a robust declarative model to express policies between applications, security zones, subnets, etc. for workloads running on a variety of platforms, including Kubernetes, OpenStack and legacy infrastructures. The highly-scalable policy engine evaluates the policies and automatically enforces the rules on multiple types of endpoints, including OpenStack VMs, containers, legacy systems and vendor Firewall devices. The system continuously reacts to topology changes and seamlessly applies the rules on endpoints. In addition, the system provides near real-time monitoring, visualization of the policy violations on endpoints.  The Sentinel architecture is based on declarative programming. The implementation is based on the Kubernetes API, controller framework. In particular, the Kubernetes API and controller framework is used to represent the desired state of different objects, including policy, firewall state, etc. and to implement control loops to reconcile the current state with the desired state. Efforts are currently underway to opensource the project.  The talk will be organized as follows.  * Overview of Cloud architecture at eBay * Sentinel Architecture & Policy Language * Policy Evaluation & Enforcement * Use of Kubernetes API & controller framework for declarative programming * Monitoring & real-time visualization of policy violations * Challenges

[Sched URL](https://cnkc16.sched.com/event/d29a7302a0174f7cd2d2ba4b0224e059)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/uF8PX5VpC2M' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
