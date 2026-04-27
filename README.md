# Dragutin Oreški Website

Static personal website deployed to GitHub Pages.

Custom domain:

```text
dragutinoreski.com
```

## Deployment

The site is deployed from this repository through `.github/workflows/pages.yml`.

The `UI Suputnik` course is intentionally kept outside this repository. During deploy, GitHub Actions checks out:

```text
dragutin-oreski/ui-suputnik
```

Local checkout:

```text
/Users/dragutinoreski/Documents/Data_surfers/Algebra/ui-suputnik
```

and publishes it under:

```text
/courses/ui-suputnik/
```

Do not commit `courses/ui-suputnik/` into this repository. It is ignored locally and only exists here as a preview mirror.

## Website TODOs

### Side Projects

- [ ] Add a dedicated `Side projects` section to the homepage.
- [ ] Decide whether side projects should be:
  - inline on `index.html`, or
  - separate pages under `/projects/`.
- [ ] Keep project cards concise: problem, what it does, stack, repo link, and optional demo link.
- [ ] Avoid turning the homepage into a long portfolio grid; prioritize 2-4 strong projects.

### Pokedex

- [ ] Add `pokedex` to side projects.
- [ ] Repository: https://github.com/dragutin-oreski/pokedex
- [ ] Create a landing page for it, likely:

```text
/projects/pokedex/
```

- [ ] Landing page should explain what the app is, show screenshots or live preview if available, and link to GitHub.
- [ ] Decide whether the project itself should be deployed separately or only described from this website.

### Strategy Performance Analyzer

- [ ] Add `strategy-performance-analyzer` to side projects.
- [ ] Repository: https://github.com/dragutin-oreski/strategy-performance-analyzer
- [ ] Create either:

```text
/projects/strategy-performance-analyzer/
```

or a strong homepage card if a full page is not needed yet.

- [ ] Summarize the core value clearly: analyzing and comparing strategy performance.
- [ ] Add charts/screenshots if they are available and safe to publish.

## Notes For Future Assistants

- Keep this repo as the personal website source, not a dumping ground for course/project source code.
- For separate projects, prefer linking or embedding deploy artifacts rather than copying whole source trees into this repo.
- If adding generated project landing pages, keep assets local and committed under the relevant project folder.
- Preserve the hidden-course behavior: `UI Suputnik` can be reachable by URL but should not be prominently linked unless explicitly requested.
