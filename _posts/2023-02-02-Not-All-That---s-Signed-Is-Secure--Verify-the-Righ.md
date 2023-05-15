---
title: "Not All That’s Signed Is Secure: Verify the Right Way with TUF and Sigstore - Zachary Newman, Chainguard, Inc. & Marina Moore, New York University"
categories: ["CloudNativeSecurityCon North America 2023"]
---

## Abstract

It’s easy to think that because more developers are signing software, the consumers of that software are necessarily more secure. However, a signature is only useful if verified correctly. One common failure mode is to verify that some software was signed, but not check who signed it. This means that you’ll treat a signature from evil@hacker.com the same as a signature from yourself! We want to check that software came from the right person, but how do we know who that is? In this talk, Marina Moore and Zachary Newman will show how you can answer that question, securely. First, use Sigstore to make signing easy. Then, use CNCF projects The Update Framework (TUF) and in-toto to concretely improve security of open source package repositories, internal container registries, and everything in between. Cut through the hype and see how to sign software in order to increase security. Learn what signing can do—and what it can’t. With this knowledge, you can design appropriate verification policies for your project or organization. You’ll also learn how the open source software repositories you depend on are adopting these techniques to ensure that the code you download comes from the authors you expect.

[Sched URL](https://cloudnativesecurityconna23.sched.com/event/b1a31fc36281ac8af531b478004df38e)

## Video

<iframe width='560' height='315' src='https://www.youtube.com/embed/8PdAigPPVH0' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>
