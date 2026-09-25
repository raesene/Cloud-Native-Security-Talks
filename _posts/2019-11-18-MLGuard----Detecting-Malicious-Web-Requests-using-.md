---
title: "MLGuard -- Detecting Malicious Web Requests using a Serverless-based Machine Learning System - Abhinav Srivastava, Frame.io"
categories: ["Cloud Native Security Day 2019"]
talk_title: "MLGuard -- Detecting Malicious Web Requests using a Serverless-based Machine Learning System"
speakers: "Abhinav Srivastava, Frame.io"
event: "Cloud Native Security Day 2019"
series: "security-day"
event_code: "CNSD-19"
year: 2019
youtube_id: "T7C0qtA8Mww"
sched_url: "https://cloudnativesecurityday2019.sched.com/event/b61462b3e712cdf2ffbd8773673b33d9"
---

Web Application Firewall (WAF) blocks incoming web requests using a variety of signatures such as SQL injection, Cross-Site Scripting, and Bots. Proactively identifying and blocking bad requests, which avoid exhibiting the known malicious patterns, is both challenging and essential from security operations perspective. In this talk, I will describe a serverless-based end-to-end system called MLGuard that ingests AWS load-balancers log data, creates a machine-learning model (Isolation Forest) with the frequency distribution of cumulative HTTP response code using Amazon SageMaker, invokes the model using the HTTP API to detect unusual requests, and sends alerts to Slack for the security team to block IPs. MLGuard utilizes various Serverless technologies such as Function-as-a-Service, DynamoDb, and API Gateway, and since its deployment a year ago, it has helped block thousands of bad IPs.
