---
title: "Sentinel: A Platform for Fine-grained Application Security - Sudheendra Murthy, eBay, Inc."
categories: ["CloudNativeCon + KubeCon 2016"]
talk_title: "Sentinel: A Platform for Fine-grained Application Security"
speakers: "Sudheendra Murthy, eBay, Inc."
event: "KubeCon North America 2016"
series: "kubecon-na"
event_code: "KC-NA-16"
year: 2016
youtube_id: "uF8PX5VpC2M"
sched_url: "https://cnkc16.sched.com/event/d29a7302a0174f7cd2d2ba4b0224e059"
---

This talk presents Sentinel, a platform for security policy management that is currently being used to secure workloads running on eBay's cloud. Sentinel provides a robust declarative model to express policies between applications, security zones, subnets, etc. for workloads running on a variety of platforms, including Kubernetes, OpenStack and legacy infrastructures. The highly-scalable policy engine evaluates the policies and automatically enforces the rules on multiple types of endpoints, including OpenStack VMs, containers, legacy systems and vendor Firewall devices. The system continuously reacts to topology changes and seamlessly applies the rules on endpoints. In addition, the system provides near real-time monitoring, visualization of the policy violations on endpoints.  The Sentinel architecture is based on declarative programming. The implementation is based on the Kubernetes API, controller framework. In particular, the Kubernetes API and controller framework is used to represent the desired state of different objects, including policy, firewall state, etc. and to implement control loops to reconcile the current state with the desired state. Efforts are currently underway to opensource the project.  The talk will be organized as follows.  * Overview of Cloud architecture at eBay * Sentinel Architecture & Policy Language * Policy Evaluation & Enforcement * Use of Kubernetes API & controller framework for declarative programming * Monitoring & real-time visualization of policy violations * Challenges
