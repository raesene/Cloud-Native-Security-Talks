# Kubernetes Security Site


This is a Github pages site based on the [minimal mistakes template](https://github.com/mmistakes/minimal-mistakes). It hosts videos on Cloud native security from various conferences, along with talk abstracts

## Adding a Talk

For talks which were given either at a Kubecon security track or at a Cloud Native Securrity con/day, they are added via an automated process which extracts the abstract and Youtube links. If you want to manually add a talk that wasn't given at either of those venues, you can do so by opening a pull request to add a file to the `_posts` directory.

The site is generally for things which fall into the realm of cloud native security, including things like containerization.

To add a talk, create a new file in the `_posts` directory. The format of the file should be [Date of talk]-[Title of talk].md. The file should contain the following front matter:

```
---
title: "Talk Title"
categories:
  - ["CONFERENCENAME"]

---
```

Then the post should include the talk Abstract and ideally the embedded Youtube video (you can get this from the "Share" button in Youtube)


