# Personal website

Static site for Dragutin Oreški, built with vanilla HTML/CSS and deployed via GitHub Pages.

## Project structure
- `index.html` – landing page with profile, experience timeline, and latest posts.
- `blog/` – standalone HTML posts plus the `blog/index.html` archive.
- `img/` – profile and company logos referenced in the layout.
- `CNAME` – custom domain pointer used by GitHub Pages.

## Run locally
1. Install Python 3 if it is not already available.
2. From the project root, start a lightweight server:
   ```
   python3 -m http.server 8000
   ```
3. Open `http://localhost:8000` in your browser. Changes to HTML files only require a refresh.

If you prefer another static server (for example, `npx serve`), feel free to use it instead—there are no build steps.

## Adding a blog post
1. Duplicate an existing post in `blog/` or create a new HTML file using the same structure (title, date, sections).
2. Add the new file to `blog/index.html` so it appears in the archive list.
3. Surface the post on the homepage by updating the list inside the `Posts` section of `index.html`.
4. Commit and push the changes; GitHub Pages will publish the update automatically.

Keep posts minimal: a short header, a few sections, and optional lists for takeaways keep the design inline with the rest of the site.
