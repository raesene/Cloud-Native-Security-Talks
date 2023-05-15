---
title: "Good Fences Make Good Neighbors: Making Cross-Namespace References More Secure with ReferenceGrant - Nick Young, Isovalent"
categories: ["CloudNativeSecurityCon North America 2023"]
---

## Abstract

The Kubernetes security model is very reliant on namespacing for enclosing trust boundaries. But what happens when an resource or set of resources need to cross those trust boundaries? How can we be confident that both parties in cross-namespace communications agree to the relationship between objects? In the SIG-Network Gateway API subproject, we've found that this is a little tricky. The answer is that both parties have to agree. The owner of the resources in the target namespace has to agree to someone outside their control accessing their stuff, and the resource that wants to refer to that stuff has to explicitly ask. Come and learn about the solution the Gateway API subproject of SIG-Network has put in place, the ReferenceGrant resource, how it works, and how it can be used to ensure that a cross-namespace reference is agreed to by both parties. We've also used variants of the same approach in other parts of the Gateway API, and this talk will explain those as well. You will come away with some knowledge both of the ReferenceGrant resource, the history behind it, and how it fits into the Gateway API.

[Sched URL](https://cloudnativesecurityconna23.sched.com/event/9cea7c60b40d87cd54373276c36d6f6c)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/_0LuJZc4PZ8' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
