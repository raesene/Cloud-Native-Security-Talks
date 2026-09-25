---
title: "Getting More Confident with Your Security Helper Libraries Thanks to Go Fuzzing - Jeremy Matos, Grafana Labs"
categories: ["Cloud Native SecurityCon North America 2022"]
talk_title: "Getting More Confident with Your Security Helper Libraries Thanks to Go Fuzzing"
speakers: "Jeremy Matos, Grafana Labs"
event: "CloudNativeSecurityCon North America 2022"
series: "securitycon"
event_code: "CNSC-NA-22"
year: 2022
youtube_id: "2xT40DLGjMU"
sched_url: "https://cloudnativesecurityconna22.sched.com/event/b86c19af36779bdf790e1582a695dd35"
---

Security helper libraries are often hard to unit test because they should make sure “bad” inputs are not considered valid, but how can we know we are not forgetting one kind of “bad” input? In cases where we don’t have an explicit definition of a good input, Go Fuzzing can be really helpful to gain confidence we are not missing some corner cases. Using a real-life example of a path traversal vulnerability in Grafana OSS, this talk will show how Go Fuzzing can be used to improve the test coverage of the corresponding security fix. Additionally, it will cover how this technique helped validate more complex security helpers and enabled us to detect some bypasses.
