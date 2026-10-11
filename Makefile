# Engineering Hub (Framework) v1.0 rebuild: build gate and tools. Python 3 standard library only.
PY ?= python3
VERSION ?= 1.0.0-rc.1
check:            ## schema, rule, register and purity checks, then framework negative tests
	$(PY) tools/validate.py --framework data/framework --repo . --out build/val.json
	$(PY) tools/neg.py --framework data/framework --out build/neg.json
bundle: check     ## framework release bundle for the Demo to pin
	$(PY) tools/bundle.py --version $(VERSION) --out dist/framework-$(VERSION).json
site: check       ## generate the Framework Hub into docs/ (served by GitHub Pages from main:/docs); site checks run first
	$(PY) tools/build_site.py --framework data/framework --repo . --out docs
site-check:       ## generate into build/site and fail if docs/ is out of date
	$(PY) tools/build_site.py --framework data/framework --repo . --out build/site
	diff -r -q build/site docs
schema:           ## regenerate schema/ from Data Schema v6 (path to the markdown export)
	$(PY) tools/authoring/make_schema.py $(SCHEMA_MD)
.PHONY: check bundle site site-check schema
