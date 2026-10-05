# Engineering Hub (Framework) – prototype v0.8

An interactive, linked knowledge site supporting the education of engineers, the verification and validation of information, and navigation. The former Design Hub becomes one part of it.

**Core idea:** there is no fixed tree. Every item is stored **once**, in a flat list, with a **permanent ID**, and tagged with values from controlled facets. The navigation tree is a **view generated from the tags**. Switch between the Lifecycle, Discipline, Product Scope, System, Design Type and Major Unit views; the same page is reached by different routes and is never duplicated.

**v0.8 (5 Oct 2026):** Production data links table gains a **Requirement** column (ID + short title); **derived** badge on derived System items in the Major Unit tree; Design Type restores **Bought-in Equipment** as DT-0014 (with Source still used); Standard Parts remain Source-only unless a material kind applies; structured **effectivity** (type / from / to / notes) in the production-links schema; Issue pages can show Product Scopes of linked items. Demo gaps 1–3, 5, 7 closed; gap 4 (authority history) skipped.

**v0.7.1 (5 Oct 2026):** one-line link on the home page to the [Demo Production Hub](https://danielwagner69.github.io/engineering-hub-demo/) (fictional Sparrow Light Trainer).

**v0.7 changes (4 Oct 2026, requirements draft v13 decisions):** new **Source** facet (SRC-0001 Make, SRC-0002 Standard Part, SRC-0003 Bought-in Equipment); Design Type now holds only material, process and item kinds (10 options; DT-0011 to DT-0013 retired, never reused) and a *Finish specifications* page (HUB-FINISH) explains that coatings, sealants and treatments are records linked to parts. New **Major Unit** facet (MU-0001 to MU-0006: Front, Centre and Rear Fuselage, Wings, Fins, Final Assembly), Aircraft scope only, with a **Major Unit view** and a *Build levels* page (HUB-BUILDLEVELS, diagram `assets/img/build-levels.svg`): build levels are numbered separately from facet levels. New **Product Scope view** and a Product Scope filter on Lessons Learned (new example LL-0007). Each System records the Product Scopes it applies to (`scopes`; Fuel and Mission Systems confirmed, the rest a first proposal, see the new framework issue), shown on System pages, and the System and Product Scope views show only applicable Systems. System facet wording is now upper tier / lower tier, and "facet level" is used throughout. New *Glossary* page (HUB-GLOSSARY). Knowledge records may carry several options per facet or All (`all`); tags, derived tags and typed supports links are shown separately (new example EX-0006, a pipe bracket with home System Secondary Structure). The illustrative Production Hub page gains an authority-register panel. Checks extended in `tests/check_data.js` and `tests/ui_check.html`.

**v0.6 changes (3 Oct 2026):** this site is now explicitly the **Framework Hub** (header "Engineering Hub – Framework"): generic, project-independent content only. New pages: *Framework vs Production* (HUB-FRAMEWORK, with an inline SVG diagram) and *Production Hub (illustrative)* (HUB-PRODEX, empty placeholder panels for points of contact, project stats, live model view, configuration & effectivity). System and Design Type pages have an empty *Production data links* table (record, type, authoritative system, version/issue, baseline, effectivity, status). New **Ask the Hub** bar and panel: `js/ai.js` exposes `HubAI.askHub(query) -> Promise<{answer, citations, mode, note}>`; set `window.HUB_AI_ENDPOINT` to the internal AI service URL (null by default, so it falls back to keyword search over Hub pages, with citations). Pages can carry `images` (`src`, `caption`, `alt`), rendered as figures with a click-to-enlarge lightbox; self-made diagrams are in `assets/img/`. New UI test `tests/ui_check.html`.

**v0.5 changes (2 Oct 2026):** applied the Hub colour palette: primary #00405E, accent #46C1BE and light #9EDEDC, with tints, blue-tinted neutral greys and a sparing warm coral/amber accent for warnings, open issues and verification status. All colours are CSS custom properties in `css/style.css`; text and link colours meet WCAG AA (4.5:1).

**v0.4 changes (2 Oct 2026):** removed personal competency-level content: the placeholder level sections on Knowledge, Skill and Trait pages, their styling, and the framework issue about mismatched rating scales (Framework issues now 19). That material is for personal tracking; the Hub now focuses on the engineering content. It may return later with a people / Subject Matter Expert focus.

**v0.3 changes:** Product Scope is Level 0 (Aircraft, Ground Equipment, Test Equipment, Facilities as peers; PS-0004 Facilities added) and is selectable at the top of the System and Design Type views (`&s=PS-xxxx` in the hash); the System rule applies across all scopes; Flight Test Instrumentation is a System (SYS-0025, group SG-0007 Test & Instrumentation); SYS-0008 renamed 'Electrical Power Generation & Distribution (electrical only)'; example EX-0005 shows a cross-scope interface (aircraft to ground refuelling).

**v0.2 changes (agreed 2 Oct 2026):** two-level System facet (System Group › System, SG-/SYS- IDs) with the System rule; new Design Type (DT-) and Product Scope (PS-) facets; the 28 tracker Aircraft System entries (KN-0009 to KN-0036) are kept as source references, each mapped to the new values and shown as "Source: KN-xxxx" on the new pages; derived tags (System Group from System; an assembly such as a loom shows the Systems of its components); facet levels (each facet has a defined level, shown in its metadata panel; the view switcher groups alternatives by level, so only views whose top facet sits at the same level are offered side by side: System | Design Type at Level 1 below Full Aircraft, Lifecycle | Discipline as cross-cutting).

## Running it
- Open `index.html` directly (works from `file://`, because the data is embedded as `data/hub.js`), or
- serve the folder: `python3 -m http.server 8000` and browse to `http://localhost:8000/`.

No build step, no server-side code, no external/CDN dependencies (plain HTML, CSS and JavaScript).

## Structure
```
index.html            page shell (top bar, sidebar with view switcher + tree, main area)
css/style.css         styling
js/app.js             hash router, tree generation from tags, page templates, search, backlinks, lessons filter
data/hub.json         generated data (taxonomy, pages, framework issues), for other tools
data/hub.js           same data as `window.HUB_DATA = {...}` (what the site loads)
scripts/build_data.py generator: workbook -> data/hub.json + data/hub.js
tests/check_data.js   static checks (unique IDs, every tag/link resolves to an existing page of the right facet)
tests/crawl.html      runtime crawl: renders every page in every view and checks every link resolves
screens/              screenshots
```

### Page types (one template per type)
| Type | IDs | Source |
|---|---|---|
| Lifecycle Stage | KN-0001 to KN-0008 | Knowledge_Register, category "ASEL Stage" |
| System Group | SG-0001 to SG-0007 | agreed System facet, level 1 (`SYSTEM_GROUPS` in build_data.py) |
| System | SYS-0001 to SYS-0025 | agreed System facet, level 2 |
| Design Type | DT-0001 to DT-0013 | agreed Design Type facet (`DESIGN_TYPES`) |
| Product Scope | PS-0001 to PS-0004 | agreed Product Scope facet (`PRODUCT_SCOPES`) |
| Tracker source entry | KN-0009 to KN-0036 | Knowledge_Register, category "Aircraft System"; source reference only, mapped via `KN_MAP` |
| Discipline | KN-0037 to KN-0059 | Knowledge_Register, category "Discipline" |
| Skill | SK-0001 to SK-0011 | Skills_Register |
| Trait | TR-0001 to TR-0059 | Traits_Register (Trait_Self_Assessment ignored) |
| Topic (example) | EX-xxxx | defined in `build_data.py` (SAMPLES) |
| Lesson Learned (example) | LL-xxxx | defined in `build_data.py` (LESSONS) |
| Hub pages | HUB-ISSUES, HUB-LESSONS | generated |

Facet value pages show: ID and title, description, metadata panel (including hierarchy level, source and origin), key considerations (placeholder), lessons learned tagged with the value, related pages (derived from shared tags), learning resources (placeholder), backlinks, and verification status / owner / last reviewed (placeholder).

Lessons Learned template: ID, title, summary, what happened, root cause, recommendation, applicability, tags (Lifecycle Stage, System, Design Type, Product Scope, Discipline), origin (document, issue, link) and verification status. The Lessons Learned page filters by any combination of facet values (OR within a facet, AND across facets).

### Routing
`#/home`, `#/f/<facet>` (facet index), `#/p/<ID>?v=<view>&s=<Product Scope ID>&c=<context IDs>&f=<filter IDs>`. `v` is the view (lifecycle | system | designtype | discipline), `c` the tree path used for breadcrumbs, `f` the lessons filter.

## Regenerating the data
```
python3 scripts/build_data.py /path/to/tracker.xlsx
node tests/check_data.js
```
The script reads only Knowledge_Register, Skills_Register, Traits_Register and Lookups (and only the Knowledge_Category and Trait_Category lookups). It never reads the evidence, dashboard, pivot, aspirational or settings sheets. It also re-runs the automatic framework checks shown on the Framework issues page.

## Adding things
- **New tag value** (e.g. a new discipline): add a row to the relevant register in the workbook with a new, never-reused ID, then regenerate. It appears in every view automatically.
- **New topic page:** add an entry to `SAMPLES` in `scripts/build_data.py` with a new `EX-xxxx` ID and `tags` per facet (`stage`, `system`, `discipline`, `skill`, `trait`) using existing IDs. Body text can link to any page with `[[ID]]` (e.g. `[[KN-0020]]`). Regenerate and run `node tests/check_data.js`.
- **New lesson:** add an entry to `LESSONS` with a new `LL-xxxx` ID, the template fields, `tags` and an `origin` (document, issue, url). Regenerate.
- **New view:** add an entry to `VIEWS` (key, label, `group` = the facet level of its top facet, and any number of facet levels). `tests/check_data.js` fails if one switcher group mixes facets of different levels.
- **New facet value (agreed facets):** add it to `SYSTEM_GROUPS`, `DESIGN_TYPES` or `PRODUCT_SCOPES` with a new, never-reused ID; if it replaces a tracker entry, update `KN_MAP`.
- **Derived tags:** tag only the lowest-level facts. System Group is computed from System; for an assembly, list the Systems of its components and record how they were derived in the item's `derived` note.

IDs are permanent: never renumber or reuse them.

## Status
Prototype. Taxonomy names and IDs come from the tracker. All guidance text, owners and review dates are placeholders or clearly labelled examples, not authoritative engineering guidance. Known issues with the source framework are listed on the Framework issues page.
