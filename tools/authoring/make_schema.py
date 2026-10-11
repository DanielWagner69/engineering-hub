"""Generate the machine-readable schema (JSON Schema 2020-12) from the tables of
Data Schema Draft v6 (sections 1.2, 2.1 and 3), plus the R-15 and R-18 deltas.
Usage: make_schema.py <path to schema_v6.md>. Output: schema/*.json."""
import re, json, os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
src = open(sys.argv[1]).read().splitlines()
def tables(lines):
    out, cur = [], None
    for l in lines:
        if l.startswith("|"):
            cells = [c.strip() for c in l.strip().strip("|").split("|")]
            if cur is None: cur = {"head": cells, "rows": []}
            elif set("".join(cells)) <= set("- :"): continue
            else: cur["rows"].append(cells)
        elif cur is not None: out.append(cur); cur = None
    if cur: out.append(cur)
    return out
def section(start_pat, stop_pat=r"^#{2,3} "):
    i = next(k for k, l in enumerate(src) if re.match(start_pat, l)); j = i + 1
    while j < len(src) and not re.match(stop_pat, src[j]): j += 1
    return src[i+1:j]
def jtype(t, card):
    t = t.lower(); s = {}
    if t.startswith("int"): s = {"type": "integer"}
    elif t.startswith("decimal"): s = {"type": "number"}
    elif t.startswith("bool"): s = {"type": "boolean"}
    elif t.startswith("datetime"): s = {"type": "string", "pattern": r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}(:\d{2})?Z$"}
    elif t.startswith("date"): s = {"type": "string", "pattern": r"^\d{4}-\d{2}-\d{2}"}
    elif t == "reg" or re.match(r"REG\((DATA_TYPE|STATUS|VERIFICATION_STATUS|ROLE|ORIGIN_KIND)", t.upper()):
        s = {"type": "string", "x-stored-as": "label of a framework-fixed register entry"}
    elif t.startswith("reg("): s = {"type": "string", "pattern": r"^(VR-[A-Z]+-\d{4}|ALL)$"}
    elif t.startswith(("string", "text")): s = {"type": "string"}
    elif t.startswith("ref"): s = {"type": "string"}
    elif t.startswith("eff"): s = {"$ref": "../common.schema.json#/$defs/eff"}
    elif t.startswith("qty"): s = {"$ref": "../common.schema.json#/$defs/qty"}
    elif t.startswith("json"): s = {}
    else: s = {}
    multi = re.search(r"\.\.n|\bn\b", card) is not None
    if (multi or (t.startswith("reg(") and "x-stored-as" not in s)) and s: s = {"anyOf": [{"type": "array", "items": s}, s]}
    return s
def required(card): return card.strip().split()[0] in ("1", "1..n")
def fields_of(tab):
    props, req = {}, []
    for row in tab["rows"]:
        name, typ, card = row[0], row[1], row[2]
        vals = row[3] if len(row) > 3 else ""
        names = [n.strip() for n in name.split("/")]; typs = [x.strip() for x in typ.split("/")]; cards = [x.strip() for x in card.split("/")]
        for k, n in enumerate(names):
            n = re.sub(r"[^a-z_0-9]", "", n.split(" ")[0].lower())
            if not n: continue
            t = typs[k] if k < len(typs) else typs[-1]; c = cards[k] if k < len(cards) else cards[-1]
            p = jtype(t, c); p["description"] = "%s; card. %s; %s" % (t, c, vals)[:300]
            if n == "verification_status": p["enum"] = ["Unverified", "Verified", "Rejected"]
            if n == "status" and vals and ";" in vals:
                p["enum"] = [v.strip().split(" (")[0] for v in vals.split(";") if v.strip()]
            props[n] = p
            if required(c) and "*" not in c: req.append(n)
    return props, req
os.makedirs(os.path.join(ROOT, "schema", "types"), exist_ok=True)
# common
ctab = [t for t in tables(section(r"^### 1\.2 ")) if t["head"][0] == "Field"][0]
cprops, creq = fields_of(ctab)
cprops["id"]["pattern"] = r"^(PRJ|EFF|PD|PR|PI|IRL|AD|AV|AI|FD|FR|FS|REQ|TSM|CS|VER|ISS|DR|RS|ACT|LL|DC|PAR|PIT|PG|PL|AR|BL|CR|RF|CK|RT|CON|RA|RSK|TR|FV|AIQ|IMG|LNK)-([A-Z]|FW)-\d{7}$"
cprops["hub"] = {"type": "string", "pattern": r"^(FW|PRJ-[A-Z]-\d{7})$", "description": "FW or project id; production data never sits in FW (6.2)"}
cprops["links"] = {"type": "array", "items": {"$ref": "#/$defs/link"}}
common = {"$schema": "https://json-schema.org/draft/2020-12/schema", "$id": "common.schema.json", "title": "Common fields (schema v6 1.2)",
  "type": "object", "properties": cprops, "required": [r for r in creq if r not in ("tags",)],
  "$defs": {"eff": {"type": "object", "required": ["effectivity_type", "from", "to"], "properties": {"effectivity_type": {"type": "string", "pattern": "^VR-EFFTYPE-\\d{4}$"}, "from": {"type": "integer", "minimum": 1}, "to": {"type": "integer", "maximum": 999}, "notes": {"type": "string"}}},
            "qty": {"type": "object", "required": ["value", "unit"], "properties": {"value": {"type": "number"}, "unit": {"type": "string"}}},
            "link": {"type": "object", "required": ["link_type", "target"], "properties": {"link_type": {"type": "string"}, "target": {"type": "string"}, "attributes": {"type": "object"}}}}}
json.dump(common, open(os.path.join(ROOT, "schema", "common.schema.json"), "w"), indent=1)
# register entry
rtab = [t for t in tables(section(r"^### 2\.1 ")) if t["head"][0] == "Field"][0]
rprops, rreq = fields_of(rtab)
rprops["id"]["pattern"] = r"^VR-[A-Z]+-\d{4}$"
rprops["register"] = {"type": "string", "pattern": r"^[A-Z_]+$", "description": "Register code (schema 2.2)"}
rprops["facet_level"] = {"anyOf": [{"type": "integer"}, {"const": "cross-cutting"}]}
rprops["state"] = {"type": "string", "enum": ["Active", "Deprecated", "Retired"]}
json.dump({"$schema": "https://json-schema.org/draft/2020-12/schema", "$id": "register_entry.schema.json", "title": "Register entry (schema v6 2.1)",
  "type": "object", "properties": rprops, "required": rreq}, open(os.path.join(ROOT, "schema", "register_entry.schema.json"), "w"), indent=1)
# data types
index = {}
heads = [(k, l) for k, l in enumerate(src) if re.match(r"^### 3\.\d+ ", l)]
for k, l in heads:
    name = re.sub(r"^### 3\.\d+ ", "", l); name = re.sub(r" \((added|brief|moved.*)\)$", "", name).strip()
    if name in ("Supporting types", "Retrofit", "Concession"): continue
    body = section(re.escape(l) + "$")
    tabs = tables(body); ft = [t for t in tabs if t["head"][0] == "Field"]; lt = [t for t in tabs if t["head"][0] == "Link type"]
    props, req = fields_of(ft[0]) if ft else ({}, [])
    links = sorted({re.sub(r" \(.*", "", r[0]) for t in lt for r in t["rows"]})
    s = {"$schema": "https://json-schema.org/draft/2020-12/schema", "$id": "types/%s.schema.json" % name.replace(" ", "_"), "title": name + " (schema v6 3.x)",
         "allOf": [{"$ref": "../common.schema.json"}], "type": "object", "properties": dict(props, type={"const": name}), "required": req,
         "x-owned-links": links}
    index[name] = s["$id"]
    json.dump(s, open(os.path.join(ROOT, "schema", s["$id"]), "w"), indent=1)
# supporting types (3.32): key fields as properties, none required beyond common
for row in [r for t in tables(section(r"^### 3\.32 ")) for r in t["rows"]]:
    name = row[0]; keys = [re.sub(r"[^a-z_]", "", x.strip().split(" ")[0].lower()) for x in re.sub(r"\{[^}]*\}|\([^)]*\)", "", row[2]).split(",")]
    s = {"$schema": "https://json-schema.org/draft/2020-12/schema", "$id": "types/%s.schema.json" % name.replace(" ", "_"), "title": name + " (schema v6 3.32, brief)",
         "allOf": [{"$ref": "../common.schema.json"}], "type": "object", "properties": dict({k: {} for k in keys if k}, type={"const": name}), "required": []}
    index[name] = s["$id"]; json.dump(s, open(os.path.join(ROOT, "schema", s["$id"]), "w"), indent=1)
# ---- late decisions R-15 and R-18 (to be written into Data Schema v7)
delta = {"R-15": {"type": "FDPS", "add_fields": {"lead_sub_system_approval": {"type": "object",
    "required": ["set_by", "set_at", "approved_by", "approved_at"],
    "properties": {"set_by": {"type": "string", "description": "Person in the owning Design Sub-team who set the lead Sub-system"},
                   "set_at": {"type": "string"}, "approved_by": {"type": "string", "description": "A Design Lead whose area is lead_sub_system, at approved_at"},
                   "approved_at": {"type": "string"}, "change_record": {"type": "string", "description": "Change Record (change type Lead Sub-system change) when the lead was changed after creation"}},
    "description": "R-15: the lead Sub-system is set by the owning Design Sub-team and approved by a Design Lead of that Sub-system. A change is a Change Record (VR-CHG-0011) that re-runs interface inheritance and flags existing breaks for re-confirmation."}},
    "add_required": ["lead_sub_system_approval"]},
  "R-18": {"type": "Review Flag", "decision_enum": ["Open", "No impact", "Updated", "Passed on", "Accept", "Query"],
    "add_fields": {"fdps_interface": {"type": "boolean", "description": "R-18: true for a flag raised to the owner of the other FDPS by a cross-FDPS Secures link. Its decision is Accept or Query; a Query stays open, is shown on both FDPS pages and does not block the link. No confirmation of the link is required."}}}}
json.dump(delta, open(os.path.join(ROOT, "schema", "schema_delta_R15_R18.json"), "w"), indent=1)
for ref, d in delta.items():
    fn = os.path.join(ROOT, "schema", index[d["type"]]); sc = json.load(open(fn))
    sc["properties"].update(d.get("add_fields", {})); sc["required"] += d.get("add_required", [])
    if "decision_enum" in d: sc["properties"]["decision"]["enum"] = d["decision_enum"]
    sc.setdefault("x-deltas", []).append(ref); json.dump(sc, open(fn, "w"), indent=1)
json.dump({"schema_version": "6.0", "deltas": "schema_delta_R15_R18.json", "types": index}, open(os.path.join(ROOT, "schema", "index.json"), "w"), indent=1)
print(len(index), "types")
