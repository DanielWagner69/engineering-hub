"""Authoring script: writes the framework's rule and reference Hub Pages (PG-FW-) and the
seven generic v0.8 example lessons (LL-FW-) into data/framework/. Clause text is taken from
Requirements v23 (generic framework requirements). Usage: make_pages.py <v23.md> <old v0.8 hub.json>"""
import json, os, re, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
v23 = open(sys.argv[1]).read().splitlines(); old = json.load(open(sys.argv[2]))
CL = {}
for l in v23:
    m = re.match(r"^((?:\d+[A-Z]?\.)+\d+) (.*)", l)
    if m: CL[m.group(1)] = m.group(2)
GL = [re.match(r"^- ([^:]+): (.*)", l).groups() for l in v23[v23.index(next(x for x in v23 if x.startswith("0.4 Glossary"))) + 1:] if False]
gl = []; on = False
for l in v23:
    if l.startswith("0.4 Glossary"): on = True; continue
    if on and l.startswith("0.5"): break
    m = re.match(r"^- ([^:]+): (.*)", l) if on else None
    if m: gl.append({"term": m.group(1), "definition": m.group(2)})
for l in v23:  # 1.1 definitions
    m = re.match(r"^- (Level|Category|Register|Type|Link|Facet|Mapping level|Hub level|Product level): (.*)", l)
    if m and not any(g["term"] == m.group(1) for g in gl): gl.append({"term": m.group(1), "definition": m.group(2)})
TS = "2026-10-12T00:00:00Z"
def page(n, slug, title, intro, clauses, ptype="VR-PAGETYPE-0013", extra=None):
    blocks = [{"text": intro}] + [{"clause": c, "text": CL[c]} for c in clauses if c in CL]
    missing = [c for c in clauses if c not in CL]
    assert not missing, missing
    r = {"id": "PG-FW-%07d" % n, "type": "Hub Page", "schema_version": "6.0", "title": title, "status": "Published", "owner": "user:framework_owner", "hub": "FW",
         "created_at": TS, "created_by": "user:framework_owner", "modified_at": TS, "modified_by": "user:framework_owner", "record_version": 1,
         "origin": {"kind": "Imported", "source_ref": "Requirements Prompt Draft v23", "source_issue_or_revision": "23"}, "verification_status": "Unverified",
         "access_marking": "VR-ACCESS-0000", "page_type": ptype, "framework_node": "ALL", "template": "TPL-RULES", "slug": slug, "body": {"blocks": blocks},
         "lifecycle_stage": ["ALL"], "discipline": ["ALL"], "last_reviewed_at": "2026-10-12"}
    if extra: r.update(extra)
    return r
R = lambda a, b, n=None: ["%s.%d" % (a, i) for i in range(b, (n or b) + 1)]
P = [
 page(101, "rules/requirements", "Requirements and flow-down", "How Requirements are allocated to the System tree and flow to FDPSs. Compliance is claimed once per FDPS, never per part.", R("6B", 1, 3) + ["6B.6", "6B.7", "6B.10"]),
 page(102, "rules/tsms", "TSMs: Technical Standards Manuals", "A TSM is a broad document holding many statements. It is tagged with Design Types, Disciplines and Systems, and reaches an FDPS when any one tag matches (OR). Over-tagging is preferred to under-tagging; the designer claims conformance only to the statements that apply.", ["6B.4", "6B.5", "6B.11"]),
 page(103, "rules/compliance", "Compliance Statements", "One Compliance Statement per FDPS per Requirement or TSM per effectivity range. A Non-compliant statement references its Issue and blocks release over its range.", ["6B.8", "6A.17"]),
 page(104, "rules/verification", "Verification and methods", "Each Verification carries its effectivity and the revisions it is based on. Methods come from the Verification method register.", ["6B.9", "2.5"]),
 page(105, "rules/effectivity", "Effectivity and the effectivity selector", "Effectivity is held on links, ranges never overlap or leave gaps, and 999 means open-ended. Presence at a selected effectivity is derived, never stored.", R("6A", 1, 3) + ["6A.8", "6A.11", "6A.12", "6A.14", "6A.18"]),
 page(106, "rules/revisions-and-numbering", "Revisions, part numbers and dash numbers", "Part numbers are identifiers only. Dash ranges: -001 to -399 made parts, -401 to -799 assemblies, -801 and above FDPSs; odd numbers left-hand or unhanded, even numbers the right-hand version; a non-interchangeable change rolls the dash number by two.", R("1.11", 1, 12) + ["6A.5", "6A.6", "6A.9"]),
 page(107, "rules/baselines", "Baselines and frozen copies", "A baseline is frozen at each FDPS release and review snapshot; frozen records reference only frozen copies (id@version).", ["6A.10", "6A.15", "6A.13"]),
 page(108, "rules/interfaces", "Interfaces: lists, inheritance, breaks and FDPS interfaces", "Interfaces are set on Sub-system and Sub-structure pages as finite lists. FDPSs inherit them; a break is recorded with a reason and approved by a Design Lead of the FDPS's lead Sub-system. Late decisions applied: R-15 (the lead Sub-system is set by the owning Design Sub-team and approved by a Design Lead of that Sub-system; a change re-runs inheritance and flags breaks for re-confirmation) and R-18 (a cross-FDPS Secures link needs no confirmation; the other FDPS's owner gets a Review Flag and records Accept or Query).", R("6C", 20, 24) + ["1.7.7"]),
 page(109, "reviews", "Design reviews: stages A, B and C", "Every FDPS passes three review stages, aligned with Lifecycle Stages 4, 5 and 6. Sign-off team Disciplines listed against a stage give their agreement; Consideration only Disciplines are checked by the designer through the checklist.", R("6C", 1, 10) + ["6C.19"], "VR-PAGETYPE-0013"),
 page(110, "reviews/release-gate", "Release gate, carry-forward and re-review", "An FDPS revision is released only after a C pass and with every Action from reviews A, B and C closed and accepted, and with no Non-compliant Compliance Statement over its range.", ["6C.11", "6C.12", "6C.13", "6C.14", "6C.17", "6A.17"]),
 page(111, "issues/escalation", "Issue escalation", "Every Issue is scored 1 to 5 on five criteria; its escalation level is the highest score, which sets its forum.", R("2E", 1, 10)),
 page(112, "lessons", "Lessons Learned", "One template for every lesson, tagged from the controlled facets and filterable by any combination. Framework lessons are generic; project lessons may be proposed for promotion without project data.", R("2G", 1, 5), "VR-PAGETYPE-0014"),
 page(113, "framework-vs-production", "Framework vs Production", "The Framework Hub holds only generic, project-independent content and is public. Each Production Hub is a versioned instance of a framework release; project changes to the framework are Tailoring Records. The Demo Production Hub is entirely fictional.", R("6", 1, 11)),
 page(114, "part-attributes", "Part attributes: Design Type, Source, Safety Classification, Item Property", "Design Type, Safety Classification and Item Property are Part attributes and filters, not trees. Source is a cross-cutting facet.", ["2B.7", "2B.10", "1.10.1", "1.10.2", "4.6"]),
 page(115, "retired", "Retired v0.8 pages", "This v0.8 page has been retired in Framework v1.0. Skill and Trait pages are dropped until their registers are populated; tracker source entries, the illustrative Production Hub page, worked examples and the v0.8 framework issues list are retired. Use the trees, registers or search instead.", []),
]
gpage = page(116, "glossary", "Glossary", "Terms used with these meanings throughout (Requirements v23 0.4 and 1.1).", [], "VR-PAGETYPE-0013", {"glossary": gl})
P.append(gpage)
os.makedirs(os.path.join(ROOT, "data", "framework", "pages"), exist_ok=True)
for p in P: json.dump(p, open(os.path.join(ROOT, "data", "framework", "pages", p["id"] + ".json"), "w"), indent=1, ensure_ascii=False)
# ---- seven generic example lessons from v0.8, re-tagged to v1.0 registers
regs = {}
for f in os.listdir(os.path.join(ROOT, "data", "framework", "registers")):
    for e in json.load(open(os.path.join(ROOT, "data", "framework", "registers", f)))["entries"]: regs[e["id"]] = e
lab = {}
for e in regs.values(): lab.setdefault((e["register"], e["label"].split(" (")[0].lower()), e["id"])
oldp = {p["id"]: p for p in old["pages"]}
def mapold(oid):
    p = oldp.get(oid); t = (p["title"] if p else "").split(" (")[0].lower()
    pre = oid.split("-")[0]
    reg = {"SYS": "SYS", "DT": "DTY", "SRC": "SRC", "PS": "SCOPE", "MU": "MU"}.get(pre)
    if reg: return next((v for (r, l), v in lab.items() if r == reg and (l == t or l.startswith(t) or t.startswith(l))), None)
    return None
KNLC = {"KN-0001": 2, "KN-0002": 3, "KN-0003": 4, "KN-0004": 5, "KN-0005": 6, "KN-0006": 8, "KN-0007": 9, "KN-0008": 10}
KNDISC = {"KN-0037": "AER", "KN-0038": "AFF", "KN-0039": "AWC", "KN-0040": "AIT", "KN-0041": "AFF", "KN-0042": "EMC", "KN-0043": "EF", "KN-0044": "FUO", "KN-0045": "HF",
 "KN-0046": "LO", "KN-0047": "MRG", "KN-0048": "MFG", "KN-0049": "MP", "KN-0050": "MEC", "KN-0051": "MBSE", "KN-0052": "SAF", "KN-0053": "SEG", "KN-0054": "SPS",
 "KN-0055": "SA", "KN-0056": "SLI", "KN-0057": "TST", "KN-0058": "WGT", "KN-0059": "QUA"}
dcode = {e["code"]: e["id"] for e in regs.values() if e["register"] == "DISC"}
for i, oid in enumerate(sorted(k for k in oldp if k.startswith("LL-"))):
    o = oldp[oid]; tg = o["tags"]
    r = {"id": "LL-FW-%07d" % (i + 1), "type": "Lesson Learned", "schema_version": "6.0", "title": o["title"], "status": "Published", "owner": "user:framework_owner", "hub": "FW",
         "summary": o["summary"], "what_happened": o["whatHappened"], "root_cause": o["rootCause"], "recommendation": o["recommendation"], "applicability": o["applicability"],
         "lifecycle_stage": sorted({"VR-LCS-%04d" % KNLC[k] for k in tg.get("stage", []) if k in KNLC}) or ["ALL"],
         "system": sorted({x for x in map(mapold, tg.get("system", [])) if x}) or ["ALL"],
         "discipline": sorted({dcode[KNDISC[k]] for k in tg.get("discipline", []) if k in KNDISC}) or ["ALL"],
         "design_type": sorted({x for x in map(mapold, tg.get("designtype", [])) if x}), "source": sorted({x for x in map(mapold, tg.get("itemsource", [])) if x}),
         "product_scope": sorted({x for x in map(mapold, tg.get("productscope", [])) if x}), "major_unit": sorted({x for x in map(mapold, tg.get("majorunit", [])) if x}),
         "example_note": "Generic, fictional example lesson (from v0.8, re-tagged to the v1.0 registers). Not authoritative engineering guidance.",
         "alias_of": oid, "origin": {"kind": "Human", "source_ref": "Framework Hub v0.8 example lesson " + oid}, "verification_status": "Unverified",
         "access_marking": "VR-ACCESS-0000", "record_version": 1, "created_at": TS, "created_by": "user:framework_owner", "modified_at": TS, "modified_by": "user:framework_owner"}
    json.dump(r, open(os.path.join(ROOT, "data", "framework", "records", r["id"] + ".json"), "w"), indent=1, ensure_ascii=False)
print(len(P), "pages;", len(gl), "glossary terms")
