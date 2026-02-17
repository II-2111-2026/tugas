# Quarto auto-render on every push

This repo is configured to render Quarto documents on every push (in GitHub Actions):

- `submissions/wXX/laporan.qmd` -> `laporan.html`
- (optional) `weeks/wXX/quiz.qmd` -> `quiz.html`

## Where to find the rendered HTML
1. Open your repo on GitHub
2. Click **Actions**
3. Open the latest workflow run
4. Scroll to **Artifacts**
5. Download: `quarto-wXX`

The HTML is not committed back to the repo (so no infinite loop).
