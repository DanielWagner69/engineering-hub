# v1.0 rebuild (branch `rebuild`)

Plan: Hub Rebuild Plan v1 (11 Oct 2026), with Daniel's decisions of 12 Oct 2026. The live v0.8 site on `main` is unchanged and tagged `v0.8` for rollback. Builds go straight to the live site once their checks pass (decision 4); the previous version stays tagged.

| Phase | State |
| --- | --- |
| 0 Preparation | Done: `v0.8` tag, `rebuild` branch, folder scaffold, schema delta note (schema/README.md), scaffold site build |
| 1 Data layer and gate | Done: schema/, data/framework/ (all Annex A and B registers, 26 Design Considerations with Draft checklists, Framework Version record, framework lesson), tools/ (loader, schema check, carried rule checks, rebuild checks, purity, negative tests, bundle), CI validation |
| 2 to 5 | Not started |

## Layout

- `schema/`: machine-readable schema (see schema/README.md).
- `data/framework/registers/`: 40 value registers, 429 entries. Annex A lists are marked `placeholder: true` (generic, fictional starter values).
- `data/framework/considerations/`: one Design Consideration per Discipline (26), with checklist items for review stages A, B and C. Every item is `item_status: Draft` until reviewed with the framework owner.
- `data/framework/records/`: Framework Version FV-FW-0000001 (1.0.0-rc.1) and the generic framework lesson.
- `tools/`: `validate.py` (the gate), `neg.py` (negative tests), `bundle.py` (release bundle), `build_site.py` (Phase 0 scaffold), `checks/core.py` (the 82 checks carried from Worked Example v4, generalised: project values come from the project's config), `checks/late.py` (register, consideration, R-15 and R-18 checks), `purity.py`.
- `tools/authoring/`: scripts that wrote the initial framework data and schema (kept for reproducibility; the JSON is master).

## Running the gate

```
make check     # or: python3 tools/validate.py --framework data/framework --repo . && python3 tools/neg.py --framework data/framework
make bundle    # dist/framework-<version>.json, pinned by the Demo
```

The gate exits non-zero on any failure. Public builds never read a workbook: the v0.8 workbook import (scripts/build_data.py) is removed on this branch and the purity check fails if any tool reads a workbook or any workbook file is present.
