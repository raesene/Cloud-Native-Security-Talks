# Cloud Native Security Talks Site

The site is published at [talks.container-security.site](https://talks.container-security.site)

This is a GitHub Pages (Jekyll) site that indexes cloud native security talks from various conferences, with their abstracts and videos. It uses its own layouts, built on the [Quadro](https://katagami.ai/language/en-019f707a-483d-7733-974a-4617c7566e66) design language.

## Adding a Talk

For talks which were given either at a KubeCon security track or at a Cloud Native Security con/day, they are added via an automated process which extracts the abstract and YouTube links. If you want to manually add a talk that wasn't given at either of those venues, you can do so by opening a pull request to add a file to the `_posts` directory.

The site is generally for things which fall into the realm of cloud native security, including things like containerization.

To add a talk, create a new file in the `_posts` directory. The format of the file should be `[Date of talk]-[Title of talk].md`, with this front matter:

```yaml
---
title: "Talk Title - Speaker Name, Company"
categories: ["KubeCon + CloudNativeCon Europe 2026"]
talk_title: "Talk Title"
speakers: "Speaker Name, Company"
event: "KubeCon Europe 2026"
series: "kubecon-eu"        # kubecon-eu | kubecon-na | kubecon-china | securitycon | security-day
event_code: "KC-EU-26"
year: 2026
youtube_id: "y5rrfSZBm1A"    # the 11-character ID from the YouTube URL
sched_url: "https://kccnceu2026.sched.com/event/..."
---

The talk abstract goes here.
```

The talk layout renders the video, Sched link and metadata from the front matter, so the body is just the abstract.

### Posts in the old format

Posts in the old format are still accepted: `title` and `categories` only, with `## Abstract`, a `[Sched URL](...)` link and a `## Video` YouTube embed in the body. Run the enrichment script to convert them:

```sh
python3 scripts/enrich_posts.py          # convert any posts that need it
python3 scripts/enrich_posts.py --check  # exit 1 if any post needs converting
```

The script only adds fields that are missing, so hand edits (for example a speaker list the title parser split wrongly) are kept. It prints a warning for any post where it couldn't find speakers or a video. To add a new conference series, add it to `SERIES` in the script and to `_data/series.yml`.

## Adding talks from a new conference (maintainer workflow)

Use this checklist when a new KubeCon or security conference is added in bulk:

1. **Import the talks** with the automated importer. It writes posts to `_posts/` in the old format (`title`, `categories`, and a body with `## Abstract`, `[Sched URL](...)` and a `## Video` embed).
2. **Check the conference name** in `categories`. It must stay the same for every talk from that event, because it forms the talk URLs (`/:categories/:title/`) and groups the talks.
3. **Enrich the posts:**
   ```sh
   python3 scripts/enrich_posts.py
   ```
   Read the warnings it prints:
   - `no speakers parsed` means the title didn't end in ` - Speaker, Company`. Edit `talk_title` and `speakers` in that post by hand. The script won't overwrite your fix if you re-run it.
   - `no video` means there was no YouTube embed. That's fine if the recording isn't out yet: add `youtube_id` later.
   - An `unknown conference` error means the conference name didn't match any series. Add a pattern to `SERIES` in `scripts/enrich_posts.py`. For a brand-new series, also add an entry to `_data/series.yml` with a plate image in `assets/images/series/`.
4. **Confirm nothing is left to convert:**
   ```sh
   python3 scripts/enrich_posts.py --check   # should print "0 post(s) need updating"
   ```
5. **Preview** with `bundle exec jekyll serve`. Check that the new event shows at the top of the home page and on `/categories/`, and that the "Latest" code in the header has updated.
6. **Commit and push to `main`.** GitHub Pages rebuilds the site.

Adding a recording later: set `youtube_id` in the post's front matter (the 11 characters after `v=` in the YouTube URL).

## Local development

```sh
bundle install
bundle exec jekyll serve
```

## Images

The plates in `assets/images/` are drawn in the [Glacis Ink](https://katagami.ai/art-styles/en-019ef8ac-0a88-7910-bc05-845eed0508fe) art style. `og-card.png` is the social sharing card.
