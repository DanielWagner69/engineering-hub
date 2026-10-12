"""Apply Requirements Prompt v24.6 / Data Schema v7.6 to the machine-readable schema and the
framework registers: EDR and line-item types (from schema_delta_v7_edr.json), Users, access
roles and permissions (5A, Annex B.6), Owner and Contributors. Idempotent."""
import json, os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
S = os.path.join(ROOT, "schema"); RG = os.path.join(ROOT, "data", "framework", "registers")
def W(p, o): json.dump(o, open(p, "w"), indent=1, ensure_ascii=False); open(p, "a").write("\n")
str_ = lambda d: {"type": "string", "description": d}
date = lambda d: {"type": "string", "pattern": "^\\d{4}-\\d{2}-\\d{2}", "description": d}
T = {
 "Requirement Document": ({"doc_kind": {"enum": ["EDR"], "description": "reg(DOCKIND)"}, "doc_code": str_("Unique within the project, e.g. EDR-FUE"), "issue": {"type": "integer", "minimum": 1},
   "sub_system_tags": {"type": "array", "items": {"type": "string", "pattern": "^VR-SUB-\\d{4}$"}, "description": "Many-to-many document-level Sub-system tag (6B.2)"},
   "product_scope": {"type": "array"}, "issue_changes": {"type": "array", "description": "[{issue, changed: [line item ids]}] (6B.10)"}}, ["doc_kind", "doc_code", "issue", "sub_system_tags", "product_scope"], "3.13A"),
 "Line-item Review": ({"fdps": str_("ref(FDPS)"), "line_item": {"type": "object", "description": "{requirement} or {tsm, clause}"}, "line_item_revision": {"type": "integer", "minimum": 1},
   "state": {"enum": ["Kept", "Broken", "Superseded (auto)"], "description": "reg(LISTATE); Superseded (auto) is set by the system only (6B.7A)"}, "bases": {"type": "array"},
   "reason": str_("Required when Broken"), "author": str_("ref(User)"), "approved_by": str_("Broken EDR line item: Design Lead of the FDPS lead Sub-system; Broken TSM statement: Design Authority (6C.13)"),
   "approved_at": str_("datetime"), "superseded_by": {"type": "array", "description": "Defined links causing the supersession (6B.7A)"}, "bulk_confirmation": str_("ref(TSM Supersession Confirmation)")}, ["fdps", "line_item", "line_item_revision", "state", "bases"], "3.15A"),
 "TSM Supersession Confirmation": ({"tsm": str_("ref(TSM)"), "fdps": str_("ref(FDPS)"), "reviews": {"type": "array"}, "confirmed_by": str_("Design Authority (User)"), "confirmed_at": str_("datetime")}, ["tsm", "fdps", "reviews"], "3.15B"),
 "User": ({"display_name": str_("Name shown in the Hub"), "email": str_("Unique; directory identity"), "handle": str_("Directory handle used in references, e.g. user:p.hale"),
   "design_team": str_("reg(DT)"), "design_sub_team": str_("reg(DST)"), "user_status": {"enum": ["Active", "Suspended", "Left"], "description": "reg(USTATUS)"},
   "framework_admin": {"type": "boolean"}, "theme": {"enum": ["Company", "Dark", "Light"]}, "last_active_at": str_("datetime")}, ["display_name", "email", "handle", "user_status", "framework_admin"], "3.37"),
 "Project Assignment": ({"user": str_("ref(User)"), "project": str_("ref(Project)"), "access_role": {"enum": ["Admin", "Design Lead", "Design Authority", "Engineer", "Viewer"], "description": "reg(ACCROLE)"},
   "effectivity_access": {"enum": ["All", "Restricted"]}, "from_date": date("date"), "to_date": date("date"), "assigned_by": str_("ref(User), Admin on the project")}, ["user", "project", "access_role", "effectivity_access", "from_date", "assigned_by"], "3.39"),
 "Effectivity Restriction": ({"project_assignment": str_("ref(Project Assignment)"), "effectivity": {"type": "array", "description": "ref(Effectivity) 1..n"}, "set_by": str_("ref(User), Admin"), "set_at": str_("datetime")}, ["project_assignment", "effectivity", "set_by", "set_at"], "3.40"),
 "Permission Override": ({"user": str_("ref(User)"), "project": str_("ref(Project)"), "permission": {"type": "object", "description": "{data_type or *, action: reg(PERM)}"}, "effect": {"enum": ["Grant", "Deny"]},
   "reason": str_("Why"), "expires_on": date("date"), "approved_by": str_("ref(User), Admin")}, ["user", "project", "permission", "effect", "reason", "approved_by"], "3.41"),
}
idx = json.load(open(os.path.join(S, "index.json")))
for name, (props, req, ref) in T.items():
    fn = name.replace(" ", "_") + ".schema.json"
    props = dict(props, type={"const": name})
    W(os.path.join(S, "types", fn), {"$schema": "https://json-schema.org/draft/2020-12/schema", "$id": "types/" + fn, "title": "%s (schema v7.6 %s)" % (name, ref), "allOf": [{"$ref": "../common.schema.json"}], "type": "object", "properties": props, "required": req, "x-owned-links": []})
    idx["types"][name] = "types/" + fn
idx["schema_version"] = "7.6"; idx["deltas"] = ["schema_delta_R15_R18.json", "schema_delta_v7_edr.json (applied in 7.6)"]
W(os.path.join(S, "index.json"), idx)
c = json.load(open(os.path.join(S, "common.schema.json")))
c["properties"]["owner"]["description"] = "ref(User) (handle of a User record in a Production Hub, 5A.7); card. 1; exactly one accountable Owner"
c["properties"]["contributors"] = {"type": "array", "items": {"type": "string"}, "description": "ref(User); card. 0..n; optional Contributors (5A.7, added in v7.4)"}
W(os.path.join(S, "common.schema.json"), c)
# registers
def reg(name, code, labels, prefix=None, defs=None):
    p = os.path.join(RG, name + ".json"); prefix = prefix or name.replace("_", "")
    old = json.load(open(p))["entries"] if os.path.exists(p) else []
    have = {e["label"] for e in old}; n = len(old)
    for l in labels:
        if l in have: continue
        n += 1; old.append({"id": "VR-%s-%04d" % (prefix, n), "register": name, "code": str(n), "label": l, "definition": (defs or {}).get(l, l), "state": "Active", "source": "Framework 1.0.0-rc.3 (Requirements v24.6, Data Schema v7.6)", "is_catch_all": False, "framework_fixed": True, "sort_order": n})
    W(p, {"register": name, "entries": old})
B6 = {"Admin": "Engineer permissions plus administer users, Project Assignments, effectivity restrictions and permission overrides on the project; view the audit trail (B.6).",
      "Design Lead": "Engineer permissions; may hold Design Lead authority roles; approve EDR line-item breaks and interface breaks within the Role register area (B.6).",
      "Design Authority": "Engineer permissions; may hold Design Authority authority roles; approve TSM statement breaks and bulk-confirm TSM supersessions within the area; approve for release where delegated (B.6).",
      "Engineer": "View all project data within the allowed effectivities; create and edit the items owned or contributed to; raise review flags. May hold Technical Authority for Design, Design Approver and Discipline Lead roles (B.6, 5A.6).",
      "Viewer": "View only, within the allowed effectivities; may comment and use the AI bar (B.6)."}
reg("ACCROLE", "", list(B6), defs=B6)
reg("PERM", "", ["View", "Create", "Edit", "Approve", "Release", "Administer users", "Comment"])
reg("USTATUS", "", ["Active", "Suspended", "Left"])
reg("DOCKIND", "", ["EDR"], defs={"EDR": "Engineering Design Requirements document: a group of Requirement line items with a Sub-system tag (6B.1A)"})
reg("LISTATE", "", ["Inherited, not reviewed", "Kept", "Broken", "Superseded (auto)", "Direct"])
reg("BASIS", "", ["Inherited via EDR Sub-system tag", "Inherited via Sub-system Design Type"])
reg("PAGETYPE", "", ["EDR", "TSM", "Admin", "User"])
reg("LINK_TYPE", "", ["Part of", "Reviews line item"], prefix="LINKTYPE")
reg("CHG", "", ["Access change"])
print("schema", idx["schema_version"], len(idx["types"]), "types")
# ---- rules pages quoting Requirements Prompt v24.6 (path to the markdown export in REQ_MD)
import re, copy
md = os.environ.get("REQ_MD")
if md:
    L = open(md, encoding="utf-8").read().split("\n")
    def cl(prefixes): return [{"clause": l.split(" ", 1)[0], "text": l.split(" ", 1)[1]} for l in L if any(l.startswith(p + " ") for p in prefixes)]
    base = json.load(open(os.path.join(ROOT, "data", "framework", "pages", "PG-FW-0000101.json")))
    def page(i, title, slug, intro, blocks, extra=None):
        p = copy.deepcopy(base); p.update(id=i, title=title, slug=slug, page_type="VR-PAGETYPE-0013", origin={"kind": "Imported", "source_ref": "Requirements Prompt Draft v24.6", "source_issue_or_revision": "24.6"},
            modified_at="2026-10-12T14:00:00Z", created_at="2026-10-12T14:00:00Z", body={"blocks": [{"text": intro}] + blocks + (extra or [])})
        W(os.path.join(ROOT, "data", "framework", "pages", i + ".json"), p)
    b6 = [l for l in L[L.index(next(x for x in L if x.startswith("### B.6"))):] if l.startswith("| ") and not l.startswith("| ---") and not l.startswith("| Access role")]
    page("PG-FW-0000117", "Users, access roles and permissions", "rules/users-and-access", "How people get access to a Production Hub: Users, named access roles per project, effectivity restrictions, one-off permission overrides, and one accountable Owner with optional Contributors on every work item. Access roles are separate from the authority (approval) roles of the Role register. Clauses quoted from Requirements Prompt v24.6, section 5A and Annex B.6 (confirmed by Daniel, 12 Oct 2026).",
         cl(["5A.%d" % n for n in range(1, 11)]), [{"text": "Annex B.6 access role %s: %s" % tuple(c.strip() for c in r.strip("|").split("|")[:2])} for r in b6])
    page("PG-FW-0000118", "EDRs, line items and link maturity", "rules/edrs-and-line-items", "Requirements are line items grouped into Requirement Documents (EDRs) tagged to Sub-systems; TSMs reach FDPSs through Design Types. Pages above FDPS level list the documents; FDPS pages list each line item with its state. Clauses quoted from Requirements Prompt v24.6.",
         cl(["6B.1A", "6B.2", "6B.5", "6B.7", "6B.7A", "6B.10", "5.21", "5.22", "5.23", "5.24", "5.27", "5.30"]))
    fvp = os.path.join(ROOT, "data", "framework", "records", "FV-FW-0000001.json"); fv = json.load(open(fvp))
    if fv["version"] != "1.0.0-rc.3":
        fv["record_history"].append({"record_version": fv["record_version"], "modified_at": fv["modified_at"], "version": fv["version"], "title": fv["title"]})
        fv.update(version="1.0.0-rc.3", title="Framework 1.0.0-rc.3", record_version=fv["record_version"] + 1, modified_at="2026-10-12T14:00:00Z", schema_version_supported="7.6")
        fv["change_list"] += ["Requirements Prompt v24.6 and Data Schema v7.6 applied (rc.3): Requirement Document (EDR), Line-item Review and TSM Supersession Confirmation types; User, Project Assignment, Effectivity Restriction and Permission Override types; Owner and Contributors; registers ACCROLE, PERM, USTATUS, DOCKIND, LISTATE",
                              "Sub-system pages in the v8 layout (rc.3): filters and System tree in the left rail, model preview beside the summary, five collapsed page groups (Requirement, Verification, Product, Considerations, Working Data), fixed Ask the Hub bar, Company, Dark and Light themes",
                              "Rules pages: Users, access roles and permissions; EDRs, line items and link maturity (rc.3)"]
        W(fvp, fv)
