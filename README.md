# Kubernetes Security Site


This is a Github pages site based on the [minimal mistakes template](https://github.com/mmistakes/minimal-mistakes). It hosts videos on Kubernetes security from various conferences, along with talk abstracts

## Adding a Talk

Generally talks are added via an automated process extracts the abstract and Youtube links. If you want to manually add a talk, you can do so by adding a file to the `_posts` directory.

To add a talk, create a new file in the `_posts` directory. The format of the file should be [Date of talk]-[Title of talk].md. The file should contain the following front matter:

```
---
title: "Talk Title"
categories:
  - [Conference Name]

---
```

Then the post should include  the Abstract and ideally the embedded Youtube video. 


