# Agent Notes

Read `README.md` first. It contains the current deployment notes and website TODOs.

Important points:

- This is the personal website repository.
- `UI Suputnik` source belongs in `dragutin-oreski/ui-suputnik`, not in this repo.
- `courses/ui-suputnik/` is ignored locally and should not be committed here.
- When editing a committed public/indexable `.html` page, update its same-path Markdown mirror too, e.g. `index.html` -> `index.html.md` and `side-projects/pokedex/index.html` -> `side-projects/pokedex/index.html.md`.
- Direct-link-only or noindex pages, such as archived job-application pages, should not be listed in `llms.txt`, `sitemap.xml`, or have `.html.md` mirrors unless explicitly requested.
- If page URLs change, update `llms.txt`, `sitemap.xml`, and relevant `<link rel="alternate" type="text/markdown">` tags.
- Side-project work should be added intentionally, preferably as project cards or pages under `/projects/`.
