# Engineering Hub (Framework) – prototype v0.6

An interactive, linked engineering knowledge site (static HTML/CSS/JS, no build step, no external dependencies).

**Live site:** https://danielwagner69.github.io/engineering-hub/

**Core idea:** there is no fixed tree. Every item is stored once, in a flat list, with a permanent ID, and tagged with values from controlled facets (Lifecycle Stage, System Group › System, Design Type, Product Scope, Discipline, Skill, Trait). The navigation tree is a view generated from the tags: switch between the Lifecycle, System, Design Type and Discipline views and the same page is reached by different routes without duplication.

## Changelog
- **v0.6 (3 Oct 2026):** the site is now explicitly the **Framework Hub** (generic, project-independent content only). New *Framework vs Production* page with diagram and an illustrative, empty *Production Hub* page; empty *Production data links* tables (with configuration and effectivity columns) on System and Design Type pages; **Ask the Hub** bar with `js/ai.js` (`HubAI.askHub(query) -> {answer, citations}`, endpoint `window.HUB_AI_ENDPOINT`, null by default so it falls back to keyword search over Hub pages); page images and diagrams (`assets/img/`) with captions and a click-to-enlarge lightbox; `tests/ui_check.html`.
- **v0.5 (2 Oct 2026):** applied the Hub colour palette (primary #00405E, accent #46C1BE, light #9EDEDC, plus tints, blue-tinted neutrals and a sparing coral/amber accent for warnings, open issues and verification status). All colours are CSS custom properties in `css/style.css`; text and link colours meet WCAG AA.
- **v0.4 (2 Oct 2026):** removed personal competency-level content (the placeholder level sections on Knowledge, Skill and Trait pages, their styling, and the framework issue about mismatched rating scales; Framework issues now 19). The Hub now focuses on the engineering content; this may return later with a people / Subject Matter Expert focus.
- **v0.3:** Product Scope as Level 0, selectable at the top of the System and Design Type views; first public release.

## Running locally
Open `index.html` directly (the data is embedded in `data/hub.js`), or run `python3 -m http.server 8000` in this folder and browse to `http://localhost:8000/`.

## Structure
```
index.html             page shell
css/style.css          styling
js/ai.js               Ask the Hub module (askHub, keyword fallback, HUB_AI_ENDPOINT)
assets/img/            self-made SVG diagrams used in pages
js/app.js              hash router, tree generation from tags, page templates, search, backlinks, lessons filter
data/hub.js            generated data as window.HUB_DATA (what the site loads)
scripts/build_data.py  generator: workbook -> data/hub.json + data/hub.js
tests/check_data.js    static data checks
tests/crawl.html       runtime crawl of every page in every view
tests/ui_check.html    lightbox, Ask the Hub fallback and framework page checks
```

## Regenerating the data
```
python3 scripts/build_data.py /path/to/tracker.xlsx
node tests/check_data.js
```
The source workbook is not included in this repository. The script reads only the Knowledge_Register, Skills_Register, Traits_Register and Lookups sheets (Trait_Self_Assessment is ignored; no evidence, dashboard, pivot, aspirational or settings data is read). It also writes `data/hub.json`, a copy of the same data for other tools, which is not committed here.

## Adding content
- New tag value: add a row to the relevant register with a new, never-reused ID, then regenerate.
- New topic page or lesson: add an entry to `SAMPLES` (EX-xxxx) or `LESSONS` (LL-xxxx) in `scripts/build_data.py`, then regenerate and run the checks.
- New view: add an entry to `VIEWS`; the checks fail if one switcher group mixes facets of different levels.

IDs are permanent: never renumber or reuse them.

## Status
Prototype. Taxonomy names and IDs come from the knowledge/skills/traits registers. All guidance text, owners and review dates are placeholders, and all topic pages and lessons learned are clearly labelled, generic, fictional examples, not authoritative engineering guidance.
