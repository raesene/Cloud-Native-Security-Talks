# CLAUDE.md

Guidance for agents working in this repo. The site is a Jekyll site on GitHub Pages that indexes cloud native security talks: https://talks.container-security.site

## Layout

- `_posts/`: one Markdown file per talk (~470). The body is only the abstract; everything else is front matter.
- `_layouts/`: `default` (masthead/footer), `home` (hero + filterable index), `talk`, `page`, `events` (`/categories/`), `years` (`/posts/`).
- `_includes/flap.html`: split-flap value cells. `_includes/talk-row.html`: one row in any talk list.
- `_data/series.yml`: the event series (id, name, code, plate image). `_data/navigation.yml`: the main nav.
- `assets/css/main.css`: all styles (plain CSS, no Sass). `assets/js/index.js`: home page filtering, with state in the query string.
- `search.json`: abstract text per URL, loaded lazily for full-text search.
- `scripts/enrich_posts.py`: turns old-format posts into structured front matter. It is idempotent and never overwrites existing fields.

## Adding talks

Follow "Adding talks from a new conference" in README.md. In short: import, then `python3 scripts/enrich_posts.py`, fix the warnings by hand, then `python3 scripts/enrich_posts.py --check` must report 0. A post without `series`/`event_code` won't appear in the series filters or on the Events page.

## Rules

- **Never change `categories` or `title` on existing posts.** Permalinks are `/:categories/:title/`, so either change breaks live URLs. Old `/categories/#<slug>` anchors are also kept working on the Events page.
- **Only use GitHub Pages–whitelisted plugins.** The site is built by the classic Pages builder: currently jekyll-sitemap, jekyll-feed and jekyll-seo-tag. Custom plugins (e.g. jekyll-archives) won't run, which is why there are no per-event pages. Events link to `/?event=<code>` instead.
- `_config.yml` pins `baseurl: ""`. Without it, jekyll-github-metadata rewrites asset paths locally.

## Design

- Design language: **Quadro** from the Katagami MCP (`mcp__katagami__get_library_entry` kind=design_language id=quadro). Use its tokens exactly (see `:root` in `main.css`): warm paper ground, ink text, square corners, hairline plus 2px top rules instead of boxed cards, Archivo + IBM Plex Mono only, and the one type scale (17px × 1.28ⁿ, `--fs-*`).
- Vermilion (`--color-accent`) marks position or the one value that matters (the active nav marker, the "Latest" event cell, the current event code, focus rings). Amber (`--color-accent-2`) marks a value in transit (the result count while filtered). Don't use either as decoration.
- After changing layout or CSS, run `mcp__katagami__check_page_against_language` (id=quadro) on the page HTML with the CSS inlined. Trim the talk list first so it fits.
- Images use the **Glacis Ink** art style (`get_library_entry` kind=art_style id=glacis-ink): fill its prompt template without paraphrasing, keep carbon-black ink with a single small vermilion square as the only colour, and generate with the `openrouter-image` skill. Save as WebP in `assets/images/` (series plates 720px wide, 4:3). `og-card.png` (1200×630) was composed with Pillow from the hero image.

## Local build

```sh
bundle install
bundle exec jekyll serve          # or: JEKYLL_ENV=production bundle exec jekyll build
```

Ruby 3.4+ needs the stdlib gems listed in the Gemfile (csv, base64, bigdecimal, logger); GitHub Pages ignores them. `Gemfile.lock` is gitignored. Analytics only render when `JEKYLL_ENV=production`.

To check pages visually, screenshot them with headless Chromium. Headless Chrome won't go below about 500px wide, so to test phone widths, load the page in a 390px iframe inside a wrapper page.
