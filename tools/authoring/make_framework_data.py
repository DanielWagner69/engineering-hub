"""Authoring script: writes data/framework/ from Requirements v23 Annex A and B and
Data Schema v6 section 2.2. JSON under data/framework/ is the master once written;
this script is kept so the initial content is reproducible. Identifiers are permanent:
entries already used by the Project D worked example keep their identifiers."""
import json, os, sys, hashlib
sys.path.insert(0, os.path.dirname(__file__))
from checklists_draft import Q
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(ROOT, "data", "framework")
FWV = "Framework 1.0.0-rc.1"
PH = FWV + " (Annex A placeholder: generic, fictional)"
regs = {}
IDC = {"DISC_TYPE":"DISCTYPE","LINK_TYPE":"LINKTYPE","ORIGIN_KIND":"ORIGIN","VERIFICATION_STATUS":"VSTATUS","ENTRY_STATE":"ESTATE","ACCESS_MARKING":"ACCESS"}
def add(reg, code, label, definition="", **kw):
    e = {"id": None, "register": reg, "code": code, "label": label,
         "definition": definition or label, "state": "Active", "source": kw.pop("source", FWV)}
    e.setdefault("is_catch_all", False); e.update(kw); regs.setdefault(reg, []).append(e); return e
def number(reg, fixed=None):
    """Assign VR-REG-NNNN in list order; entries named in fixed keep their number."""
    fixed = fixed or {}; used = set(fixed.values()); n = 1
    for i, e in enumerate(regs[reg]):
        k = fixed.get(e["label"]) or fixed.get(e["code"])
        if k is None:
            while n in used: n += 1
            k = n; used.add(n)
        e["id"] = "VR-%s-%04d" % (IDC.get(reg, reg), k); e["sort_order"] = i + 1
# ---- Product Scope
for c, l, d in [("AC","Aircraft","The air vehicle and everything installed on it."),
                ("GE","Ground Equipment","Equipment used on the ground to handle, service or support the aircraft."),
                ("TE","Test Equipment","Rigs, test sets and instrumentation used to test the aircraft or its parts."),
                ("FAC","Facilities","Buildings, sites and fixed installations.")]:
    add("SCOPE", c, l, d, facet_level=0, is_catch_all=False)
number("SCOPE")
# ---- Major Units and Build Stations (A.1, A.2)
MUS = [("1","Front Fuselage","F"),("2","Centre Fuselage","C"),("3","Rear Fuselage","R"),("4","Wings","W"),("5","Fins","N"),("6","Final Assembly","FA")]
for c, l, p in MUS:
    add("MU", c, l, l + (" (catch-all: items fitted at final assembly that belong to no single Major Unit)" if c=="6" else ""),
        source=PH, placeholder=True, facet_level=1, is_catch_all=(c=="6"), applies_to_scopes=["VR-SCOPE-0001"], node_kind="Major Unit")
number("MU")
mu = {e["label"]: e["id"] for e in regs["MU"]}
BSN = ["Structural Assembly","Systems First-fix Installation","Equipping and Closure","Functional Test"]
FAN = ["Major Unit Join","Cross-join Systems Connection (pipes and looms)","Landing Gear and Propulsion Installation","Final Equipping and Closure","Ground Test and Delivery Preparation"]
for c, l, p in MUS[:5]:
    for i, n in enumerate(BSN):
        add("BS", "%s-BS%d" % (p, i+1), "%s BS%d %s" % (l, i+1, n), source=PH, placeholder=True, parent=mu[l], is_bench=False,
            is_catch_all=False, applies_to_scopes=["VR-SCOPE-0001"], node_kind="Build Station")
for i, n in enumerate(FAN):
    add("BS", "FA%d" % (i+1), "Final Assembly FA%d %s" % (i+1, n), source=PH, placeholder=True, parent=mu["Final Assembly"], is_bench=False,
        is_catch_all=False, applies_to_scopes=["VR-SCOPE-0001"], node_kind="Build Station")
for c, l, p in MUS:
    add("BS", "%s-BEN" % p, "%s Bench (off-aircraft assembly)" % l, "Off-aircraft assembly of Assembly Instances for %s (2C.12)." % l,
        source=PH, placeholder=True, parent=mu[l], is_bench=True, is_catch_all=False, applies_to_scopes=["VR-SCOPE-0001"], node_kind="Bench")
number("BS", {"C-BEN": 31})
# ---- System Groups and Systems (2B.7, A.7)
SGS = [("AF","Airframe"),("PP","Propulsion & Power"),("FVM","Flight & Vehicle Management"),("ES","Environmental & Safety"),
       ("CI","Crew Interface"),("MS","Mission Systems"),("TI","Test & Instrumentation")]
for c, l in SGS: add("SG", c, l, facet_level=1, tier="upper", is_catch_all=False)
number("SG"); sg = {e["label"]: e["id"] for e in regs["SG"]}
SYS = [("0001","50","Primary Structure","Airframe",True),("0002","51","Secondary Structure","Airframe",True),
 ("0003","52","Skins, Doors & Panels","Airframe",True),("0004","56","Windscreen & Canopy","Airframe",True),
 ("0005","71","Propulsion","Propulsion & Power",False),("0006","72","Intake & Ducts","Propulsion & Power",False),
 ("0007","24","Electrical Power Generation & Distribution","Propulsion & Power",False),("0008","36","Pneumatics","Propulsion & Power",False),
 ("0009","27","Flight Control","Flight & Vehicle Management",False),("0010","28","Fuel","Propulsion & Power",False),
 ("0011","45","Vehicle Management","Flight & Vehicle Management",False),("0012","29","Hydraulics","Propulsion & Power",False),
 ("0013","32","Landing Gear","Flight & Vehicle Management",False),("0014","34","Navigation","Flight & Vehicle Management",False),
 ("0015","21","Environmental Control","Environmental & Safety",False),("0016","47","Thermal Management","Environmental & Safety",False),
 ("0017","26","Fire Protection","Environmental & Safety",False),("0018","95","Crew Escape & Safety","Environmental & Safety",False),
 ("0019","31","Cockpit & Controls","Crew Interface",False),("0020","61","Radar / Sensors","Mission Systems",False),
 ("0021","62","Electronic Warfare","Mission Systems",False),("0022","23","Communications","Mission Systems",False),
 ("0023","63","Data Links","Mission Systems",False),("0024","94","Stores Integration (incl. Armaments)","Mission Systems",False),
 ("0025","98","Flight Test Instrumentation","Test & Instrumentation",False)]
APP = {"Primary Structure":"YNNN","Secondary Structure":"YNNN","Skins, Doors & Panels":"YNNN","Windscreen & Canopy":"YNNN",
 "Propulsion":"YNYY","Intake & Ducts":"YNNN","Fuel":"YYYY","Electrical Power Generation & Distribution":"YYYY","Hydraulics":"YYYN",
 "Pneumatics":"YYYN","Flight Control":"YNYN","Vehicle Management":"YNYN","Navigation":"YNYN","Landing Gear":"YNNN",
 "Environmental Control":"YYNN","Thermal Management":"YYNN","Fire Protection":"YNNY","Crew Escape & Safety":"YNYN",
 "Cockpit & Controls":"YNYN","Flight Test Instrumentation":"YNYN"}
for n, c, l, g, st in SYS:
    a = APP.get(l, "YNNN")
    add("SYS", c, l, l + (" (electrical power only)" if c=="24" else ""), parent=sg[g], is_structural=st, facet_level=1, tier="lower",
        is_catch_all=False, applies_to_scopes=["VR-SCOPE-%04d" % (i+1) for i, y in enumerate(a) if y=="Y"], applicability_placeholder=True)
number("SYS", {l: int(n) for n, c, l, g, st in SYS})
sysid = {e["label"]: e["id"] for e in regs["SYS"]}
# ---- Sub-systems and Sub-structures (A.3, 2B.11)
SUBS = {"Primary Structure":"Frames and Bulkheads; Spars and Ribs; Longerons and Stringers; Major Joints and Attachments",
 "Secondary Structure":"Brackets and Supports; Fairings; Floors and Platforms; Equipment Racks",
 "Skins, Doors & Panels":"Skins; Access Panels; Doors and Hatches","Windscreen & Canopy":"Transparencies; Canopy Frame; Canopy Actuation and Locking",
 "Propulsion":"Engine Installation; Engine Mounts; Engine Controls Interface","Intake & Ducts":"Intake Ducts; Exhaust and Nozzle; Auxiliary Air Inlets",
 "Fuel":"Fuel Storage; Fuel Feed; Refuel and Defuel; Vent and Pressurisation; Fuel Gauging",
 "Electrical Power Generation & Distribution":"Generation; Primary Distribution; Secondary Distribution; Energy Storage; External Power",
 "Hydraulics":"Hydraulic Generation; Hydraulic Distribution; Storage and Conditioning","Pneumatics":"Air Supply; Pneumatic Distribution",
 "Flight Control":"Primary Flight Control Actuation; Secondary Flight Control; Flight Control Computing and Sensors",
 "Vehicle Management":"Vehicle Management Computing; Health and Usage Monitoring; Data Networks",
 "Landing Gear":"Main Gear; Nose Gear; Wheels and Brakes; Steering; Extension and Retraction",
 "Navigation":"Inertial and Satellite Navigation; Air Data; Radio Navigation Aids",
 "Environmental Control":"Air Conditioning; Pressurisation; Ice and Rain Protection",
 "Thermal Management":"Liquid Cooling Loops; Heat Exchangers and Heat Sinks; Thermal Control",
 "Fire Protection":"Fire and Overheat Detection; Fire Suppression","Crew Escape & Safety":"Escape System; Life Support; Survival Equipment",
 "Cockpit & Controls":"Displays; Inceptors and Controls; Cockpit Furnishings and Seat Interface; Interior and Exterior Lighting",
 "Radar / Sensors":"Radar; Electro-optical Sensors; Sensor Processing","Electronic Warfare":"Warning Receivers; Countermeasures",
 "Communications":"Radio Communications; Intercom and Audio; Identification",
 "Data Links":"Line-of-sight Data Link; Beyond-line-of-sight Data Link",
 "Stores Integration (incl. Armaments)":"Carriage and Release Equipment; Stores Management; Internal Armament",
 "Flight Test Instrumentation":"Sensors and Transducers; Data Acquisition and Recording; Telemetry"}
for n, c, l, g, st in SYS:
    for i, s in enumerate(SUBS[l].split("; ")):
        add("SUB", str(i+1), s, "%s %s of the %s System." % (s, "Sub-structure" if st else "Sub-system", l), source=PH, placeholder=True,
            parent=sysid[l], is_catch_all=False, facet_level=1, mapping_level=True)
    add("SUB", "0", "%s General" % l, "Items that serve the %s System as a whole and cannot be placed in a single other %s of it (2B.11)." % (l, "Sub-structure" if st else "Sub-system"),
        source=PH, placeholder=True, parent=sysid[l], is_catch_all=True, facet_level=1, mapping_level=True)
FIXSUB = {"Frames and Bulkheads":1,"Brackets and Supports":5,"Engine Installation":12,"Fuel Storage":31,"Fuel Feed":32,
          "Secondary Distribution":35,"Hydraulic Distribution":41,"Vehicle Management Computing":50}
number("SUB", FIXSUB)
# ---- Design Teams and Sub-teams (A.4)
DTS = [("STR","Structures","Forward Structure; Centre Structure; Aft Structure; Wing and Fin Structure; Skins, Doors and Panels; Transparencies"),
       ("FLU","Fluid Systems","Fuel; Hydraulics and Pneumatics; Environmental and Thermal"),
       ("ELE","Electrical Systems","Power Systems; Looms and Harnesses"),
       ("PRI","Propulsion Integration","Engine Installation; Intakes and Exhausts"),
       ("MEC","Mechanical Systems","Landing Gear; Flight Control Mechanisms; Escape Systems"),
       ("AVM","Avionics and Mission Integration","Cockpit; Avionics Installation; Mission Systems Installation; Test Instrumentation")]
for c, l, s in DTS: add("DT", c, l, "Design Team " + l + ".", source=PH, placeholder=True, facet_level=1, is_catch_all=False)
number("DT", {"Structures":1,"Fluid Systems":2,"Propulsion Integration":5}); dt = {e["label"]: e["id"] for e in regs["DT"]}
DSTC = {"Forward Structure":"FST","Centre Structure":"CST","Aft Structure":"AST","Wing and Fin Structure":"WFS","Skins, Doors and Panels":"SDP",
 "Transparencies":"TRN","Fuel":"FUE","Hydraulics and Pneumatics":"HYP","Environmental and Thermal":"ENT","Power Systems":"PWR",
 "Looms and Harnesses":"LMH","Engine Installation":"ENG","Intakes and Exhausts":"INX","Landing Gear":"LGR","Flight Control Mechanisms":"FCM",
 "Escape Systems":"ESC","Cockpit":"CKP","Avionics Installation":"AVI","Mission Systems Installation":"MSI","Test Instrumentation":"TIN"}
for c, l, s in DTS:
    for x in s.split("; "):
        add("DST", DSTC[x], x, "Design Sub-team %s of the %s Design Team." % (x, l), source=PH, placeholder=True, parent=dt[l], facet_level=2, is_catch_all=False)
number("DST", {"Centre Structure":2,"Fuel":7,"Hydraulics and Pneumatics":8,"Engine Installation":16})
# ---- Lifecycle Stage (B.1)
LCS = ["Opportunity","Concept Development","Architecture/Configuration Design","Initial System Design","Preliminary Design","Detailed Design",
       "Manufacture & Assembly","Qualification","Production","Support & Upgrades","Disposal"]
for i, l in enumerate(LCS): add("LCS", str(i+1), l, facet_level="cross-cutting", sequence_no=i+1, in_current_scope=4<=i+1<=6, is_catch_all=False)
number("LCS")
# ---- Discipline type and Discipline (B.2)
add("DISC_TYPE","SOT","Sign-off team","Agreement required at each review stage it is listed against (6C.19).",framework_fixed=True)
add("DISC_TYPE","CON","Consideration only","Checked by the designer through its checklist (4.5); no separate sign-off.",framework_fixed=True)
number("DISC_TYPE")
DISC = [("AER","Aerodynamics",1),("AFF","Affordability and Cost",2),("AWC","Airworthiness and Certification",1),
 ("AIT","Assembly, Interfaces, Tolerances and Interchangeability",2),("CM","Configuration Management",1),("DES","Design",1),
 ("ELE","Electrical Systems",1),("EMC","Electro-Magnetic Compatibility",1),
 ("EF","Environmental Factors (protection treatments, drainage, weather and tank sealing)",2),
 ("FUO","Future Upgrades and Obsolescence",2),("HF","Human Factors",1),("LO","Low Observability",1),
 ("MRG","Maintainability, Reliability and Ground Equipment",1),("MFG","Manufacturing Engineering",1),("MP","Materials and Processes",1),
 ("MEC","Mechanical Systems",1),("MBSE","Model Based Systems Engineering (Digital Thread)",2),("QUA","Quality",1),("SAF","Safety",1),
 ("SEG","Segregation, Separation and Survivability",2),("SPS","Standard Parts and Supply Chain",1),("SA","Structural Analysis (Stress)",1),
 ("SLI","System Layout and Integration",2),("TST","Test",1),("WGT","Weight",1),("FLU","Fluid Systems (fuel, hydraulics and pneumatics)",1)]
for c, l, t in DISC: add("DISC", c, l, facet_level="cross-cutting", discipline_type="VR-DISCTYPE-%04d" % t, is_catch_all=False)
number("DISC")
order = sorted(regs["DISC"], key=lambda e: e["label"].lower())
for i, e in enumerate(order): e["sort_order"] = i + 1
def simple(reg, items, **kw):
    for i, it in enumerate(items):
        c, l = it if isinstance(it, tuple) else (str(i+1), it)
        add(reg, c, l, **kw)
    number(reg)
simple("SRC", [("MAKE","Make"),("STD","Standard Part"),("BI","Bought-in Equipment")], facet_level="cross-cutting", is_catch_all=False)
simple("DTY", ["Metallic - Additive","Metallic - Machined","Metallic - Sheet","Metallic - Cast / Forged","Carbon Fibre Composite",
  "Other Composite (glass, aramid)","Non-metallic - Moulded (seals, rubbers, plastics)","Glazing (canopy, windscreen)","Pipework",
  "Electrical Looms","Bought-in Equipment (pumps, LRUs, actuators)","Standard Part (catalogue items such as fasteners, seals, fittings and clamps)"],
  source=PH, placeholder=True, part_attribute=True)
simple("SAF", [("A","Catastrophic"),("B","Hazardous"),("C","Major"),("D","Minor"),("E","No safety effect")], source=PH, placeholder=True, part_attribute=True)
for e, m in zip(regs["SAF"], ["Loss of aircraft or loss of life","Serious injury or large reduction in safety margins",
    "Significant reduction in safety margins or crew capability","Slight reduction in safety margins","No effect on safety"]): e["definition"] = m
simple("TYC", [("FS","Fastener"),("SL","Seal"),("BR","Common bracket"),("CL","Clip or clamp"),("FT","Fluid fitting"),
  ("EC","Electrical connector or component"),("SP","Spacer or shim")], source=PH, placeholder=True)
simple("NUMSCH", [("MS","Meaningful stem"),("CP","Common part"),("CAT","Catalogue standard"),
  ("BIC","Bought-in control number (Project letter + BI + four-digit sequence, e.g. D-BI-0001)")])
simple("DASH", [("PART","Made part -001 to -399"),("ASM","Assembly -401 to -799"),("FDPS","FDPS -801 and above")], framework_fixed=True)
for e, r in zip(regs["DASH"], [(1,399),(401,799),(801,None)]): e["range"] = {"lower": r[0], "lower_inclusive": True, "upper": r[1], "upper_inclusive": True, "unit": None}
simple("ROLE", ["Technical Authority for Design (Design Licence Holder)","Design Authority","Design Lead","Design Approver","Discipline Lead"], framework_fixed=True)
simple("AGREE", ["Agree","Agree with conditions","Disagree"], framework_fixed=True)
simple("BASIS", ["Direct","Inherited via System tree node","Inherited via Design Type","Inherited via System","Inherited via Discipline"], framework_fixed=True)
simple("EMB", ["Planned","Embodied","Not embodied"], framework_fixed=True, reserved="Future Development (section 7)")
simple("CKFU", ["Action","Risk","Approved justification"], framework_fixed=True)
simple("PROP", ["Mechanical","Flexible","Kinematic","Fastener"], part_attribute=True)
LT = ["Decomposes into","Satisfied by","Verified by","Demonstrates","Instance of","Supports","Secures","Interface","Finish applied","Affects",
 "Production link","Describes","Derived from","Drives","Located at","Homed in","Contains","Assembled from","Comprises","Effective revision",
 "Allocated to","Governs","Interfaces with","Resolved by","Constrains","Informed by","Governed by","Applies to","Covers","Records","Raised at",
 "Tagged to","Cross-link"]
simple("LINK_TYPE", LT)
simple("STAGE", [("A","Initial System Design"),("B","Preliminary"),("C","Detail")])
for e, n in zip(regs["STAGE"], (4,5,6)): e["lifecycle_stage"] = "VR-LCS-%04d" % n
simple("ESC", [("1","Level 1: Engineer (Issue owner)"),("2","Level 2: Engineer (Issue owner)"),("3","Level 3: Team Leader"),("4","Level 4: Chief Engineer"),("5","Level 5: Programme Board")])
simple("IMPACT", ["Effort","Cost","Schedule","Safety or certification","Scope"])
simple("EFFTYPE", ["Effectivity Number","Serial Range","Build Standard"])
simple("FINCAT", ["Paint","Primer","Surface Treatment","Sealant","Adhesive"])
simple("PAGETYPE", ["Lifecycle Stage","Major Unit","Build Station","Design Team","Design Sub-team","FDPS","System Group","System","Sub-system",
 "Discipline","Skill","Trait","Topic","Lesson Learned"])
for e in regs["PAGETYPE"]:
    if e["label"] in ("Skill","Trait"): e["reserved"] = "Page type kept for later; register not yet populated (decision 6)"
simple("MASTER", ["PLM","CAD","Released Documents","Analysis Tool","Hub"])
simple("ORIGIN_KIND", ["Human","AI","Derived","Imported"], framework_fixed=True)
simple("VERIFICATION_STATUS", ["Unverified","Verified","Rejected"], framework_fixed=True)
simple("CHG", ["Link change","FDPS transfer","FDPS ownership change","Up-revision","New part number","Effectivity change",
 "Improvement after review","Population change","Interface change","Other","Lead Sub-system change"])
regs["CHG"][-1]["definition"] = "Change of an FDPS's lead Sub-system or lead Sub-structure (R-15). Re-runs interface inheritance and flags existing interface breaks for re-confirmation."
simple("REQLVL", ["Air System","System","Sub-system","Item"])
simple("VMETH", ["Analogy","Design Review","Calculation Analysis","Safety Assessment","Laboratory/Bench/Rig Tests","Product Ground Tests",
 "Flight Tests","Design Inspection","Simulation","Equipment Qualification"])
simple("UNIT", ["m","mm","kg","N","Pa","K","s","h","A","V","ohm","GBP","person-day","day","week"])
simple("ENTRY_STATE", ["Active","Deprecated","Retired"], framework_fixed=True)
simple("RFDEC", [("UPD","Updated"),("NI","No impact"),("PASS","Passed on"),("ACC","Accept"),("QRY","Query")], framework_fixed=True)
for e in regs["RFDEC"]:
    if e["code"] in ("ACC","QRY"): e["definition"] = e["label"] + ": decision on an FDPS-interface Review Flag raised by a cross-FDPS Secures link (R-18). " + ("A Query stays open and is shown on both FDPS pages; it does not block the link." if e["code"]=="QRY" else "The other FDPS's owner accepts the interface.")
    e["applies_to"] = "FDPS-interface flags only" if e["code"] in ("ACC","QRY") else "Other Review Flags"
add("ACCESS_MARKING", "PUB", "Public (framework)", "Generic framework content with no access restriction."); number("ACCESS_MARKING", {"PUB": 0})
os.makedirs(os.path.join(OUT, "registers"), exist_ok=True)
for r, es in regs.items():
    json.dump({"register": r, "entries": es}, open(os.path.join(OUT, "registers", r + ".json"), "w"), indent=1, ensure_ascii=False)
# ---- Design Considerations (one per Discipline, 3.22) with Draft checklists (decision 7)
STG = {"A": "VR-STAGE-0001", "B": "VR-STAGE-0002", "C": "VR-STAGE-0003"}
TS = "2026-10-12T00:00:00Z"
def common(id_, typ, title, **kw):
    r = {"id": id_, "type": typ, "schema_version": "6.0", "title": title, "status": kw.pop("status", "Draft"), "owner": "user:framework_owner",
         "hub": "FW", "created_at": TS, "created_by": "user:framework_owner", "modified_at": TS, "modified_by": "user:framework_owner",
         "record_version": 1, "origin": {"kind": "Human"}, "verification_status": "Unverified", "access_marking": "VR-ACCESS-0000"}
    r.update(kw); return r
os.makedirs(os.path.join(OUT, "considerations"), exist_ok=True)
dname = {e["id"]: e["label"] for e in regs["DISC"]}
for disc, (pre, name, stages) in Q.items():
    n = int(disc[-4:]); cls = []
    for s, qs in stages.items():
        items = []; k = 1; ids = set()
        for q in qs:
            parts = q.split("|"); text = parts[0]; it = {"question": text, "item_status": "Draft"}
            iid = None
            for p in parts[1:]:
                if p.startswith("topic="): it["topic"] = p[6:]
                elif p.startswith("applies_to="): it["applies_to"] = p[11:].split(",")
                else: iid = p
            if not iid:
                while "%s-%s-%02d" % (pre, s, k) in ids or any(("%s-%s-%02d" % (pre, s, k)) in x for x in qs): k += 1
                iid = "%s-%s-%02d" % (pre, s, k); k += 1
            ids.add(iid); it["item_id"] = iid; items.append(dict(item_id=iid, **{x: y for x, y in it.items() if x != "item_id"}))
        cls.append({"stage": STG[s], "items": items})
    rec = common("DC-FW-%07d" % n, "Design Consideration", name, page_type="VR-PAGETYPE-0010", framework_node=disc, discipline=disc,
                 description="%s as a design consideration that every design shall address (4.2). Generic framework content." % dname[disc],
                 guidance="Answer each item for the review stage. A No needs an Action, a Risk or a justification approved by the Discipline Lead (4.5). Items are Draft starter content for review.",
                 checklists=cls, lifecycle_stage=["VR-LCS-0004","VR-LCS-0005","VR-LCS-0006"], last_reviewed_at="2026-10-12",
                 draft_note="Starter checklist items, Draft: to be reviewed with the framework owner before Framework v1.0 release.")
    json.dump(rec, open(os.path.join(OUT, "considerations", rec["id"] + ".json"), "w"), indent=1, ensure_ascii=False)
# ---- Framework Version record and framework lesson
os.makedirs(os.path.join(OUT, "records"), exist_ok=True)
fv = common("FV-FW-0000001", "Framework Version", "Framework 1.0.0-rc.1", version="1.0.0-rc.1", schema_version_supported="6.0",
            change_list=["Rebuild on Requirements v23 and Data Schema v6, with late decisions R-15 and R-18",
                         "Full Annex A (placeholder) and Annex B registers", "26 Design Considerations with Draft checklists per stage"],
            content_review={"state": "Not yet reviewed", "due": "before release 1.0.0"})
json.dump(fv, open(os.path.join(OUT, "records", fv["id"] + ".json"), "w"), indent=1)
print({r: len(es) for r, es in regs.items()})
