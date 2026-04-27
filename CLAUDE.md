# Claude Notes

Read `README.md` first. It is the source of truth for current website TODOs and deployment notes.

Current priorities:

- Add a side-projects section to the website.
- Add `pokedex`: https://github.com/dragutin-oreski/pokedex
- Add `strategy-performance-analyzer`: https://github.com/dragutin-oreski/strategy-performance-analyzer

Keep course material and project source code out of this repository unless explicitly requested.

Maintenance rule:

- When changing any committed public/indexable `.html` page, update its same-path `.html.md` Markdown mirror in the same change.
- Direct-link-only or noindex pages, such as archived job-application pages, should not be listed in `llms.txt`, `sitemap.xml`, or have `.html.md` mirrors unless explicitly requested.
- If navigation or public URLs change, update `llms.txt`, `sitemap.xml`, and any relevant Markdown alternate links.
- `courses/ui-suputnik/` is a deploy-time checkout from another repository, so its Markdown mirror should be maintained in that source repo, not here.
