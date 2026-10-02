#!/usr/bin/env python3
"""Generate data/hub.json and data/hub.js for the Engineering Hub prototype.

Reads ONLY these sheets of the tracker workbook:
  Knowledge_Register, Skills_Register, Traits_Register, Lookups
(Trait_Self_Assessment is ignored. Evidence, Dashboard, Pivot, Aspirational and
Settings sheets are never opened.)

Usage:  python3 scripts/build_data.py path/to/tracker.xlsx
"""
import json, re, sys, collections, warnings, datetime
from pathlib import Path

warnings.filterwarnings("ignore")
import openpyxl

ROOT = Path(__file__).resolve().parent.parent
ALLOWED_SHEETS = ["Knowledge_Register", "Skills_Register", "Traits_Register", "Lookups"]
# Only these lookup categories are published (others relate to evidence logging or programmes).
PUBLISHED_LOOKUPS = ["Knowledge_Category", "Trait_Category"]

# Workbook category -> hub facet
CATEGORY_TO_FACET = {"ASEL Stage": "stage", "Aircraft System": "srcsystem", "Discipline": "discipline"}

FACETS = [
    {"key": "stage", "level": "X-CROSS", "levelLabel": "Cross-cutting (not a product level; applies at every product level): lifecycle", "label": "Lifecycle Stage", "plural": "Lifecycle Stages", "source": "Knowledge_Register (Knowledge_Category = 'ASEL Stage')",
     "note": "ASEL = Air System Engineering Lifecycle. Register order is lifecycle order."},
    {"key": "sysgroup", "level": "L1", "levelLabel": "Level 1: directly below any Product Scope item, e.g. Full Aircraft (upper tier of the System facet)", "label": "System Group", "plural": "System Groups", "source": "Agreed System facet (2 Oct 2026), level 1",
     "note": "Upper level of the two-level System facet. An item's System Group is derived from its System tag(s)."},
    {"key": "system", "level": "L1", "levelLabel": "Level 1: directly below any Product Scope item, e.g. Full Aircraft", "label": "System", "plural": "Systems", "source": "Agreed System facet (2 Oct 2026), level 2; mapped from tracker Aircraft System list",
     "note": "Rule: a System is a set of items that work together to perform one function. Every item belongs to exactly one System, the one whose function it serves. The System facet applies across all Product Scopes (aircraft, ground equipment, test equipment and facilities), so a System such as Fuel links up across them. Assemblies take their System tag(s) from their components (derived tags), so an assembly such as a loom may show several."},
    {"key": "designtype", "level": "L1", "levelLabel": "Level 1: directly below any Product Scope item, e.g. Full Aircraft", "label": "Design Type", "plural": "Design Types", "source": "Agreed Design Type facet (2 Oct 2026)",
     "note": "The kind of design work. Status: agreed for now, subject to refinement."},
    {"key": "productscope", "level": "L0", "levelLabel": "Level 0: top level. Aircraft, Ground Equipment, Test Equipment and Facilities are peers; Full Aircraft is the top of the Aircraft scope", "label": "Product Scope", "plural": "Product Scopes", "source": "Agreed Product Scope facet (2 Oct 2026)",
     "note": "Which product the item belongs to; the top level (Level 0). The four options are peers. Each scope has Systems; connections between items in different scopes are shown as links (interfaces), not as a parent level."},
    {"key": "discipline", "level": "X-CROSS", "levelLabel": "Cross-cutting (not a product level; applies at every product level): knowledge area", "label": "Discipline", "plural": "Disciplines", "source": "Knowledge_Register (Knowledge_Category = 'Discipline')", "note": ""},
    {"key": "skill", "level": "PEOPLE", "levelLabel": "People register (not part of the product hierarchy)", "label": "Skill", "plural": "Skills", "source": "Skills_Register", "note": ""},
    {"key": "trait", "level": "PEOPLE", "levelLabel": "People register (not part of the product hierarchy)", "label": "Trait", "plural": "Traits", "source": "Traits_Register (Trait_Self_Assessment column not used)", "note": ""},
    {"key": "srcsystem", "level": "SOURCE", "levelLabel": "Source reference only (not used for tagging)", "label": "Tracker Aircraft System (source)", "plural": "Tracker Aircraft Systems (source)", "source": "Knowledge_Register (Knowledge_Category = 'Aircraft System')",
     "note": "The 28 original tracker entries, kept with their permanent KN IDs as source references. They are no longer used for tagging: each is mapped to the agreed System, Design Type or Product Scope values."},
]

# Facet levels: every facet is assigned to a defined level. Views are offered as alternatives only within the
# same level; a view's top facet must be at the view group's level. Levels for Lifecycle Stage, Discipline and
# Product Scope are provisional (only System and Design Type were stated: both directly below Full Aircraft).
VIEWS = [
    {"key": "lifecycle", "label": "Lifecycle", "group": "Cross-cutting", "levels": ["stage", "system"], "description": "Lifecycle Stage \u203a System \u203a content"},
    {"key": "system", "label": "System", "group": "Level 1: below a Product Scope item", "scopeSelectable": True, "levels": ["sysgroup", "system", "stage"], "description": "System Group \u203a System \u203a Lifecycle Stage \u203a content"},
    {"key": "designtype", "label": "Design Type", "group": "Level 1: below a Product Scope item", "scopeSelectable": True, "levels": ["designtype", "system"], "description": "Design Type \u203a System \u203a content"},
    {"key": "discipline", "label": "Discipline", "group": "Cross-cutting", "levels": ["discipline", "stage"], "description": "Discipline \u203a Lifecycle Stage \u203a content"},
]

# ---- Agreed facets (decisions of 2 Oct 2026). New permanent IDs.
SYSTEM_GROUPS = [
    ("SG-0001", "Airframe", [("SYS-0001", "Primary Structure"), ("SYS-0002", "Secondary Structure"), ("SYS-0003", "Skins, Doors & Panels"), ("SYS-0004", "Windscreen & Canopy")]),
    ("SG-0002", "Propulsion & Power", [("SYS-0005", "Propulsion"), ("SYS-0006", "Intake & Ducts"), ("SYS-0007", "Fuel"), ("SYS-0008", "Electrical Power Generation & Distribution (electrical only)"), ("SYS-0009", "Hydraulics"), ("SYS-0010", "Pneumatics")]),
    ("SG-0003", "Flight & Vehicle Management", [("SYS-0011", "Flight Control"), ("SYS-0012", "Vehicle Management"), ("SYS-0013", "Landing Gear"), ("SYS-0014", "Navigation")]),
    ("SG-0004", "Environmental & Safety", [("SYS-0015", "Environmental Control"), ("SYS-0016", "Thermal Management"), ("SYS-0017", "Fire Protection"), ("SYS-0018", "Crew Escape & Safety")]),
    ("SG-0005", "Crew Interface", [("SYS-0019", "Cockpit & Controls")]),
    ("SG-0006", "Mission Systems", [("SYS-0020", "Radar / Sensors"), ("SYS-0021", "Electronic Warfare"), ("SYS-0022", "Communications"), ("SYS-0023", "Data Links"), ("SYS-0024", "Stores Integration (incl. Armaments)")]),
    ("SG-0007", "Test & Instrumentation", [("SYS-0025", "Flight Test Instrumentation")]),
]
DESIGN_TYPES = [
    ("DT-0001", "Metallic - Additive", None), ("DT-0002", "Metallic - Machined", None), ("DT-0003", "Metallic - Sheet", None),
    ("DT-0004", "Metallic - Cast / Forged", None), ("DT-0005", "Carbon Fibre Composite", None),
    ("DT-0006", "Other Composite", "Includes glass and aramid composites."),
    ("DT-0007", "Non-metallic - Moulded", "Includes seals, rubbers and plastics."),
    ("DT-0008", "Glazing", "Includes canopy and windscreen transparencies."),
    ("DT-0009", "Pipework", None),
    ("DT-0010", "Electrical Looms", "Looms are a Design Type, not a System: each wire takes the System it serves, and a loom shows the Systems of its wires (derived tags)."),
    ("DT-0011", "Coatings, Sealants & Treatments", "Includes paint, primers, surface treatments, sealants and adhesives."),
    ("DT-0012", "Standard Parts", "Catalogue fasteners, seals and fittings."),
    ("DT-0013", "Bought-in Equipment", "Includes pumps, LRUs and actuators."),
]
PRODUCT_SCOPES = [
    ("PS-0001", "Aircraft", "The aircraft product. Its top item is Full Aircraft."),
    ("PS-0002", "Ground Equipment", "Includes ground support equipment (tracker KN-0021). Its top items sit at the same level as Full Aircraft."),
    ("PS-0003", "Test Equipment", "Test equipment as a product in its own right. Flight test instrumentation installed on the aircraft is a System (Flight Test Instrumentation), not this scope."),
    ("PS-0004", "Facilities", "For example test rigs, hangars and fuel farms. Facilities have Systems like any other scope; their connections to other items are shown as links (interfaces), not as a parent level."),
]
# Tracker Aircraft System (KN) -> agreed facets. clean=False means the mapping is not one-to-one; note explains.
KN_MAP = {
    "KN-0009": ({"system": ["SYS-0024"]}, False, "Armaments merged with Stores Integration into one System, 'Stores Integration (incl. Armaments)'. Two tracker entries map to one value."),
    "KN-0010": ({"system": ["SYS-0019"]}, True, ""),
    "KN-0011": ({"system": ["SYS-0022"]}, True, ""),
    "KN-0012": ({"system": ["SYS-0018"]}, True, ""),
    "KN-0013": ({"system": ["SYS-0023"]}, True, ""),
    "KN-0014": ({"designtype": ["DT-0010"]}, False, "No longer a System. Maps to Design Type 'Electrical Looms'; the System of each wire is the System it serves, and a loom's Systems are derived from its wires."),
    "KN-0015": ({"designtype": ["DT-0013"], "system": ["SYS-0008"]}, False, "Split across two facets: Design Type 'Bought-in Equipment' plus System 'Electrical Power Generation & Distribution (electrical only)'. Electrical equipment that serves another function (e.g. a sensor's power supply) should take that function's System under the System rule, so this System tag is a default, not a certainty."),
    "KN-0016": ({"system": ["SYS-0021"]}, True, ""),
    "KN-0017": ({"system": ["SYS-0015"]}, True, ""),
    "KN-0018": ({"system": ["SYS-0011"]}, True, ""),
    "KN-0019": ({"system": ["SYS-0025"]}, True, "Flight Test Instrumentation is its own System (group Test & Instrumentation)."),
    "KN-0020": ({"system": ["SYS-0007"]}, True, ""),
    "KN-0021": ({"productscope": ["PS-0002"]}, True, "Moved out of the System list to Product Scope 'Ground Equipment'. Ground equipment items take Systems like any other scope."),
    "KN-0022": ({"system": ["SYS-0009"]}, True, ""),
    "KN-0023": ({"system": ["SYS-0006"]}, True, ""),
    "KN-0024": ({"system": ["SYS-0013"]}, True, ""),
    "KN-0025": ({"sysgroup": ["SG-0006"]}, False, "'Mission Systems' was one tracker entry but is now a System Group containing five Systems; it maps to the group, not to a single System."),
    "KN-0026": ({"system": ["SYS-0014"]}, True, ""),
    "KN-0027": ({"system": ["SYS-0010"]}, True, ""),
    "KN-0028": ({"system": ["SYS-0008"]}, True, ""),
    "KN-0029": ({"system": ["SYS-0005"]}, True, ""),
    "KN-0030": ({"system": ["SYS-0020"]}, True, ""),
    "KN-0031": ({"system": ["SYS-0003"]}, True, "Kept as one grouped System for now (Skins, Doors & Panels)."),
    "KN-0032": ({"system": ["SYS-0024"]}, False, "Merged with Armaments (KN-0009) into 'Stores Integration (incl. Armaments)'."),
    "KN-0033": ({"system": ["SYS-0001", "SYS-0002"]}, False, "'Structure' is split into Primary Structure and Secondary Structure. One tracker entry maps to two Systems, so existing items tagged 'Structure' would need individual re-tagging."),
    "KN-0034": ({"system": ["SYS-0016", "SYS-0017"]}, False, "'Thermal Management / Fire Protection' is split into two Systems, Thermal Management and Fire Protection."),
    "KN-0035": ({"system": ["SYS-0012"]}, True, ""),
    "KN-0036": ({"system": ["SYS-0004"]}, True, "System only. The related Design Type 'Glazing' describes the kind of work, not the System, so it is not part of the mapping."),
}

EXAMPLE_NOTE = ("Example text written for the Engineering Hub prototype to demonstrate multi-facet tagging. "
                "It is generic, illustrative and NOT authoritative engineering guidance.")

# Sample intersection content. Each item is stored once and tagged with several facets.
# Body text may reference any page with [[ID]].
SAMPLES = [
    {"id": "EX-0001", "title": "Fuel System in Detailed Design",
     "tags": {"stage": ["KN-0005"], "system": ["SYS-0007"], "designtype": ["DT-0009", "DT-0011"], "productscope": ["PS-0001"], "discipline": ["KN-0053", "KN-0049", "KN-0043"],
              "skill": ["SK-0003"], "trait": ["TR-0006", "TR-0007"]},
     "summary": "How fuel system design questions typically come together once the design moves into [[KN-0005]].",
     "sections": [
        ["Why this intersection matters",
         "In detailed design the routing, supports and fittings of the [[SYS-0007]] become fixed geometry. Decisions taken here are "
         "expensive to change later, so the system, structural and survivability viewpoints need to be considered together rather than in sequence."],
        ["Typical considerations (illustrative)",
         "- Route pipes and equipment so that a single event cannot disable redundant paths (see [[KN-0053]]).\n"
         "- Confirm material compatibility of pipes, seals and coatings with the fluid and environment (see [[KN-0049]]).\n"
         "- Consider sealing, drainage and protection treatments in and around tank areas (see [[KN-0043]]).\n"
         "- Record assumptions and trade-offs explicitly so they can be reviewed (see [[SK-0003]])."],
        ["Questions to ask at review",
         "- What are the knock-on effects of this routing on neighbouring systems and structure? ([[TR-0007]])\n"
         "- Has the design been considered as part of the whole aircraft rather than in isolation? ([[TR-0006]])"],
     ]},
    {"id": "EX-0002", "title": "Landing Gear in Preliminary Design",
     "tags": {"stage": ["KN-0004"], "system": ["SYS-0013"], "designtype": ["DT-0002", "DT-0013"], "productscope": ["PS-0001"], "discipline": ["KN-0050", "KN-0056", "KN-0058"],
              "skill": ["SK-0003", "SK-0005"], "trait": ["TR-0008"]},
     "summary": "An example of how a major mechanical system is shaped during [[KN-0004]].",
     "sections": [
        ["Why this intersection matters",
         "During preliminary design the space envelope, attachment strategy and kinematic concept of the [[SYS-0013]] are developed. "
         "These choices drive structure, systems installation and mass, so early integration is important."],
        ["Typical considerations (illustrative)",
         "- Agree the stowed and deployed envelopes with neighbouring systems (see [[KN-0056]]).\n"
         "- Compare mechanism concepts on complexity, reliability and maintainability (see [[KN-0050]]).\n"
         "- Track mass estimates and margins as the concept matures (see [[KN-0058]]).\n"
         "- Plan the later analysis and test evidence that will be needed (see [[SK-0005]])."],
        ["Questions to ask at review",
         "- Is the level of design risk being carried proportionate to the maturity of the information? ([[TR-0008]])"],
     ]},
    {"id": "EX-0003", "title": "Electrical Looms in Production Support",
     "derived": {"system": "Derived from the loom's wires: this example loom carries wires serving Electrical Power Generation & Distribution and Flight Control."},
     "tags": {"stage": ["KN-0007"], "system": ["SYS-0008", "SYS-0011"], "designtype": ["DT-0010"], "productscope": ["PS-0001"], "discipline": ["KN-0042", "KN-0040", "KN-0048"],
              "skill": ["SK-0009"], "trait": ["TR-0030", "TR-0055"]},
     "summary": "An example of the issues that arise once looms are being built and installed, during [[KN-0007]].",
     "sections": [
        ["Why this intersection matters",
         "Once the aircraft is in production, queries on [[DT-0010]] often concern installation, clearances and build sequence. "
         "Responding well needs an understanding of both the original design intent and the manufacturing reality.\n"
         "Under the derived-tags rule this loom is not given a System directly: each wire takes the System it serves, so the loom shows "
         "[[SYS-0008]] and [[SYS-0011]] because it carries wires for both."],
        ["Typical considerations (illustrative)",
         "- Check that bonding, screening and segregation intent is preserved by any change (see [[KN-0042]]).\n"
         "- Consider fit, interfaces and tolerances at each attachment point (see [[KN-0040]]).\n"
         "- Understand how the loom is manufactured and installed before proposing a fix (see [[KN-0048]]).\n"
         "- Look for the root cause of repeated queries rather than treating each one in isolation (see [[SK-0009]])."],
        ["Questions to ask at review",
         "- Is the change traceable to the original requirement and design intent? ([[TR-0055]])"],
     ]},
    {"id": "EX-0004", "title": "Hydraulics System in Qualification / Certification",
     "tags": {"stage": ["KN-0006"], "system": ["SYS-0009"], "designtype": ["DT-0009", "DT-0013", "DT-0007"], "productscope": ["PS-0001"], "discipline": ["KN-0057", "KN-0039", "KN-0052"],
              "skill": ["SK-0008", "SK-0010"], "trait": ["TR-0051", "TR-0053"]},
     "summary": "An example of the evidence-focused work typical of [[KN-0006]] for a fluid system.",
     "sections": [
        ["Why this intersection matters",
         "In qualification the question shifts from 'does the design work?' to 'can we demonstrate, with evidence, that it meets its requirements?'. "
         "For the [[SYS-0009]] this typically combines test, analysis and similarity arguments."],
        ["Typical considerations (illustrative)",
         "- Plan tests so that each requirement has a clear method of verification (see [[KN-0057]]).\n"
         "- Understand how the evidence will support the airworthiness case (see [[KN-0039]]).\n"
         "- Make sure safety assessment assumptions are consistent with the tested configuration (see [[KN-0052]]).\n"
         "- Write reports that state results, limitations and conclusions clearly (see [[SK-0010]]); follow the governance route (see [[SK-0008]])."],
        ["Questions to ask at review",
         "- Does the evidence actually support the claim being made? ([[TR-0051]])\n"
         "- Have safety implications been given proper priority? ([[TR-0053]])"],
     ]},
    {"id": "EX-0005", "title": "Aircraft-to-Ground Refuelling Interface",
     "tags": {"stage": ["KN-0005"], "system": ["SYS-0007"], "designtype": ["DT-0009", "DT-0012"], "productscope": ["PS-0001", "PS-0002"], "discipline": ["KN-0040", "KN-0052"],
              "skill": ["SK-0002"], "trait": ["TR-0055"]},
     "summary": "An example of one System, [[SYS-0007]], crossing two Product Scopes: [[PS-0001]] and [[PS-0002]].",
     "sections": [
        ["Why this example matters",
         "The System facet applies across all Product Scopes. The aircraft refuelling coupling and the ground refuelling equipment are different items in different scopes, "
         "but both belong to [[SYS-0007]]. The interface between them must be linked and traceable, so a change on one side flags the other for review."],
        ["Typical considerations (illustrative)",
         "- Record the interface as a link between the aircraft item and the ground equipment item, not as a parent-child relationship.\n"
         "- Agree fit, sealing and tolerances at the coupling (see [[KN-0040]]).\n"
         "- Consider the safety implications of the interface on both sides (see [[KN-0052]]).\n"
         "- Keep the interface data in one place and reference it from both items (see [[SK-0002]])."],
        ["Questions to ask at review",
         "- Can each side of the interface be traced to the other and to the requirement that governs it? ([[TR-0055]])"],
     ]},
]


LESSON_NOTE = ("EXAMPLE lesson written for the Engineering Hub prototype to demonstrate the Lessons Learned template and facet filtering. "
               "It is generic and fictional, does not describe a real event, and is NOT authoritative engineering guidance.")

# Example Lessons Learned. Same template for every lesson; tags use the three knowledge facets.
LESSONS = [
    {"id": "LL-0001", "title": "Pipe-to-structure clearances found late in the design",
     "tags": {"stage": ["KN-0005"], "system": ["SYS-0007", "SYS-0001"], "designtype": ["DT-0009", "DT-0002"], "productscope": ["PS-0001"], "discipline": ["KN-0056", "KN-0040"]},
     "summary": "Clearance problems between pipe runs and structure were only found when the full assembly model was checked.",
     "whatHappened": "Pipe routes and structural parts were developed in separate models. When they were combined for a design review, several locations had insufficient clearance once tolerances and pipe movement were included.",
     "rootCause": "No agreed space-allocation model or regular combined clash check during development; tolerance stack-ups were not included in the clearance criteria.",
     "recommendation": "Agree space allocation early, run combined clash checks at a set frequency, and define clearance criteria that include tolerances and in-service movement.",
     "applicability": "Any routed system (fuel, hydraulic, electrical) installed close to structure, from Preliminary Design onwards."},
    {"id": "LL-0002", "title": "Seal material not compatible with the operating fluid",
     "tags": {"stage": ["KN-0006"], "system": ["SYS-0009"], "designtype": ["DT-0007"], "productscope": ["PS-0001"], "discipline": ["KN-0049", "KN-0057"]},
     "summary": "A seal degraded during endurance testing because its compatibility with the fluid had been assumed rather than confirmed.",
     "whatHappened": "During an endurance test a seal swelled and leaked. Investigation showed the selected seal compound was not approved for the fluid at the tested temperature range.",
     "rootCause": "Material selection relied on a similar earlier design; the compatibility assumption was not recorded or checked against the actual fluid and temperature range.",
     "recommendation": "Record material compatibility as an explicit, checked requirement for every fluid-wetted part, and verify it against current fluid and temperature data before test.",
     "applicability": "All fluid systems; most relevant during Detailed Design and Qualification / Certification."},
    {"id": "LL-0003", "title": "Loom chafing at panel edges",
     "derived": {"system": "The loom's System tags (Electrical Power Generation & Distribution, Navigation) are derived from its wires; Skins, Doors & Panels is tagged because the panel is part of the lesson."},
     "tags": {"stage": ["KN-0007", "KN-0008"], "system": ["SYS-0008", "SYS-0014", "SYS-0003"], "designtype": ["DT-0010"], "productscope": ["PS-0001"], "discipline": ["KN-0040", "KN-0047"]},
     "summary": "Electrical looms rubbed against panel edges after repeated panel removal for maintenance.",
     "whatHappened": "Inspections found wear on loom sleeving near a frequently removed access panel. The loom was correctly installed but moved each time the panel was removed and refitted.",
     "rootCause": "Loom support design considered the installed state only, not the movement caused by maintenance access.",
     "recommendation": "Assess loom supports and clearances for maintenance actions as well as the installed state; add edge protection where panels are removed regularly.",
     "applicability": "Looms and pipes near removable panels and doors; check in Detailed Design and when maintenance procedures change."},
    {"id": "LL-0004", "title": "Mass growth from unrecorded assumptions",
     "tags": {"stage": ["KN-0004"], "system": ["SYS-0013"], "designtype": ["DT-0004", "DT-0013"], "productscope": ["PS-0001"], "discipline": ["KN-0058"]},
     "summary": "Early mass estimates grew significantly because the assumptions behind them were not recorded.",
     "whatHappened": "The mass of a mechanism grew steadily as the design matured. Reviewers could not tell which items had been included in the early estimate, so growth could not be predicted or challenged.",
     "rootCause": "Mass estimates were recorded as single numbers without their scope, assumptions or maturity.",
     "recommendation": "Store each mass estimate with its scope, assumptions and maturity level, and hold a growth allowance appropriate to that maturity.",
     "applicability": "All systems and structure from Initial System Design to Detailed Design."},
    {"id": "LL-0005", "title": "Maintenance access not considered for equipment replacement",
     "tags": {"stage": ["KN-0005"], "system": ["SYS-0009", "SYS-0007"], "designtype": ["DT-0013", "DT-0009"], "productscope": ["PS-0001"], "discipline": ["KN-0047", "KN-0045"]},
     "summary": "A replaceable item could only be removed after removing several other items.",
     "whatHappened": "During a maintainability review it was found that removing one line-replaceable item required disconnecting neighbouring pipes and equipment, increasing maintenance time and the risk of errors.",
     "rootCause": "Removal paths were not modelled or reviewed; maintainability was assessed after the installation layout had been fixed.",
     "recommendation": "Model removal and replacement paths for replaceable items as part of layout design, and include maintainers in early layout reviews.",
     "applicability": "Any replaceable equipment in congested bays; Preliminary and Detailed Design."},
    {"id": "LL-0006", "title": "Ambiguous requirement led to rework",
     "tags": {"stage": ["KN-0001"], "system": ["SYS-0011"], "productscope": ["PS-0001"], "discipline": ["KN-0051", "KN-0039"]},
     "summary": "A requirement that could be read two ways was implemented differently by two teams.",
     "whatHappened": "Two teams interpreted the same requirement differently. The difference was found at integration, and one design had to be reworked.",
     "rootCause": "The requirement used undefined terms and had no stated verification method, so its meaning was never tested before design started.",
     "recommendation": "Review each requirement for single interpretation and define its verification method when it is written; hold requirements as linked structured data rather than prose.",
     "applicability": "All systems; most important at Requirements Capture / Concept."},
]


def clean(v):
    return v.strip() if isinstance(v, str) else v


def slug(s):
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


def main(xlsx):
    wb = openpyxl.load_workbook(xlsx, read_only=True, data_only=True)
    rows = {s: [r for r in wb[s].iter_rows(values_only=True)] for s in ALLOWED_SHEETS}

    values = []  # taxonomy values (pages)
    raw = {}     # raw strings, kept for issue checks
    for r in rows["Knowledge_Register"][1:]:
        if not r or not r[0]:
            continue
        kid, cat, area, desc = r[:4]
        values.append({"id": kid, "facet": CATEGORY_TO_FACET.get(cat, "UNMAPPED"), "title": clean(area),
                       "description": clean(desc) or None, "sourceCategory": cat, "category": None})
        raw[kid] = {"name": area, "desc": desc, "cat": cat}
    for r in rows["Skills_Register"][1:]:
        if not r or not r[0]:
            continue
        sid, name, desc = r[:3]
        values.append({"id": sid, "facet": "skill", "title": clean(name), "description": clean(desc) or None,
                       "sourceCategory": None, "category": None})
        raw[sid] = {"name": name, "desc": desc, "cat": None}
    for r in rows["Traits_Register"][1:]:
        if not r or not r[0]:
            continue
        tid, cat, name, desc = r[:4]  # r[4] = Trait_Self_Assessment: deliberately ignored
        values.append({"id": tid, "facet": "trait", "title": clean(name), "description": clean(desc) or None,
                       "sourceCategory": cat, "category": clean(cat)})
        raw[tid] = {"name": name, "desc": desc, "cat": cat}

    lookups = collections.OrderedDict()
    for r in rows["Lookups"][1:]:
        if not r or not r[0] or r[0] not in PUBLISHED_LOOKUPS:
            continue
        lookups.setdefault(r[0], []).append({"value": r[1], "description": r[2], "sortOrder": r[3], "active": r[4]})

    # Agreed facets (new IDs)
    for gid, gname, systems in SYSTEM_GROUPS:
        values.append({"id": gid, "facet": "sysgroup", "title": gname, "description": None, "sourceCategory": None, "category": None,
                       "members": [x[0] for x in systems], "agreed": True})
        for sid, sname in systems:
            values.append({"id": sid, "facet": "system", "title": sname, "description": None, "sourceCategory": None, "category": None,
                           "group": gid, "agreed": True})
    SYSTEM_DESCRIPTIONS = {
        "SYS-0008": "Electrical power only: generation and distribution of electrical power. Hydraulic and pneumatic power belong to Hydraulics and Pneumatics.",
        "SYS-0025": "Flight test instrumentation installed on the aircraft. Off-aircraft test equipment is Product Scope 'Test Equipment'.",
    }
    for v in values:
        if v["id"] in SYSTEM_DESCRIPTIONS:
            v["description"] = SYSTEM_DESCRIPTIONS[v["id"]]
    for did, dname, ddesc in DESIGN_TYPES:
        values.append({"id": did, "facet": "designtype", "title": dname, "description": ddesc, "sourceCategory": None, "category": None,
                       "agreed": True, "status": "Agreed for now, subject to refinement"})
    for pid, pname, pdesc in PRODUCT_SCOPES:
        values.append({"id": pid, "facet": "productscope", "title": pname, "description": pdesc, "sourceCategory": None, "category": None, "agreed": True})
    # Source references: tracker KN Aircraft System entries -> agreed values
    vids = {v["id"] for v in values}
    for v in values:
        if v["facet"] == "srcsystem":
            m, clean_, note = KN_MAP[v["id"]]
            for ids in m.values():
                for t in ids:
                    assert t in vids, t
            v["mapsTo"], v["mappingClean"], v["mappingNote"] = m, clean_, note
    srcs = collections.defaultdict(list)
    for v in values:
        for ids in (v.get("mapsTo") or {}).values():
            for t in ids:
                srcs[t].append(v["id"])
    for v in values:
        if v["id"] in srcs:
            v["sources"] = srcs[v["id"]]

    for i, v in enumerate(values):
        v["order"] = i

    pages = []
    for v in values:
        pg = {"id": v["id"], "type": v["facet"], "title": v["title"], "description": v["description"],
              "category": v["category"], "sourceCategory": v["sourceCategory"], "order": v["order"],
              "tags": {}, "placeholder": True}
        for k in ("group", "members", "mapsTo", "mappingClean", "mappingNote", "sources", "agreed", "status"):
            if k in v:
                pg[k] = v[k]
        if v.get("agreed"):
            pg["origin"] = {"document": "Facet decisions agreed by Daniel Wagner, 2 Oct 2026 (recorded in 'Requirements Prompt - Draft', sections 1B.7 and 1F)", "issue": "Draft v11", "url": None, "references": []}
        else:
            pg["origin"] = {"document": "Tracker workbook, " + {"skill": "Skills_Register", "trait": "Traits_Register"}.get(v["facet"], "Knowledge_Register"),
                            "issue": "not recorded in source", "url": None, "references": []}
        pages.append(pg)
    for s in SAMPLES:
        pages.append({"id": s["id"], "type": "content", "title": s["title"], "summary": s["summary"],
                      "sections": [{"heading": h, "body": b} for h, b in s["sections"]],
                      "tags": s["tags"], "derived": s.get("derived", {}), "example": True, "exampleNote": EXAMPLE_NOTE,
                      "origin": {"document": "Engineering Hub prototype (example text)", "issue": "Draft 0.1", "url": None, "references": []}})

    for l in LESSONS:
        pages.append(dict(l, type="lesson", example=True, exampleNote=LESSON_NOTE,
                          origin={"document": "None (example lesson written for the Engineering Hub prototype)", "issue": "n/a", "url": None, "references": []}))
    pages.append({"id": "HUB-LESSONS", "type": "special", "title": "Lessons Learned",
                  "summary": "All lessons learned, filterable by any combination of Lifecycle Stage, Aircraft System and Discipline."})
    issues = find_issues(values, raw, lookups, rows)
    pages.append({"id": "HUB-ISSUES", "type": "special", "title": "Framework issues",
                  "summary": "Inconsistencies found in the source tracker framework. They are recorded here, not silently fixed, "
                             "so that the controlled lists can be corrected at source."})

    data = {
        "meta": {"title": "Engineering Hub", "version": "0.5 (prototype)",
                 "generated": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                 "source": "Tracker workbook: " + ", ".join(ALLOWED_SHEETS),
                 "exampleNote": EXAMPLE_NOTE},
        "facets": FACETS, "views": VIEWS, "lookups": lookups,
        "pages": pages, "issues": issues,
    }
    (ROOT / "data").mkdir(exist_ok=True)
    js = json.dumps(data, ensure_ascii=False, indent=1)
    (ROOT / "data" / "hub.json").write_text(js, encoding="utf-8")
    (ROOT / "data" / "hub.js").write_text("/* Generated by scripts/build_data.py - do not edit by hand. */\nwindow.HUB_DATA = " + js + ";\n", encoding="utf-8")
    counts = collections.Counter(p["type"] for p in pages)
    print("Wrote data/hub.json and data/hub.js:", dict(counts), "issues:", len(issues))


def find_issues(values, raw, lookups, rows):
    """Automatic checks + curated observations. Returns a list of issue dicts."""
    issues = []
    def add(title, detail, refs=(), kind="Auto-detected", status="Open", resolution=""):
        issues.append({"id": "FI-%02d" % (len(issues) + 1), "title": title, "detail": detail, "refs": list(refs), "kind": kind,
                       "status": status, "resolution": resolution})

    # 1. Trait categories missing from Lookups
    lk = {x["value"] for x in lookups.get("Trait_Category", [])}
    used = collections.OrderedDict()
    for v in values:
        if v["facet"] == "trait":
            used.setdefault(v["category"], []).append(v["id"])
    for cat, ids in used.items():
        if cat not in lk:
            add("Trait category '%s' is not in Lookups (Trait_Category)" % cat,
                "Traits_Register uses category '%s', which is missing from the controlled list in Lookups. "
                "The controlled list is therefore not exhaustive for the data that uses it." % cat, ids)
    # Knowledge categories vs lookups
    kc = {x["value"] for x in lookups.get("Knowledge_Category", [])}
    for v in values:
        if v["sourceCategory"] and v["facet"] in ("stage", "srcsystem", "discipline") and v["sourceCategory"] not in kc:
            add("Knowledge category '%s' not in Lookups" % v["sourceCategory"], "", [v["id"]])

    add("Controlled lists for Lifecycle Stage, Aircraft System and Discipline are not in Lookups",
        "Lookups defines only the three Knowledge_Category values; the actual options of each category exist only as rows in Knowledge_Register, "
        "which has no Sort_Order or Active flag (unlike Lookups). There is therefore no single authoritative controlled list per facet.", [], "Curated")

    # 2. Missing descriptions
    for facet, label in (("stage", "Lifecycle Stage (ASEL Stage)"), ("srcsystem", "tracker Aircraft System"), ("discipline", "Discipline")):
        ids = [v["id"] for v in values if v["facet"] == facet and not v["description"]]
        if ids:
            add("Missing descriptions: %s (%d of %d)" % (label, len(ids), sum(1 for v in values if v["facet"] == facet)),
                "Knowledge_Description is blank for these entries, so the meaning and boundaries of each option are not defined. "
                "Without definitions the options cannot be checked for overlap (mutual exclusivity) or gaps (exhaustiveness).", ids)
    for facet in ("skill", "trait"):
        ids = [v["id"] for v in values if v["facet"] == facet and not v["description"]]
        if ids:
            add("Missing descriptions: %s" % facet, "", ids)
    for cat, items in lookups.items():
        if all(not x["description"] for x in items):
            add("Lookups: no descriptions for %s values" % cat,
                "Lookup_Description is blank for every %s value, so the categories are not defined in the controlled list itself." % cat, [], "Auto-detected")

    # 3. Bundled options
    bundled = [v["id"] for v in values if v["facet"] in ("stage", "srcsystem", "discipline", "skill") and re.search(r" & | / |, | - ", v["title"])]
    add("Bundled options covering several topics",
        "Many options combine several topics in one value (joined by '&', '/', ',' or ' - '), for example "
        "'Assembly & Interfaces & Tolerances & Interchangeability', 'Environmental Factors / Protection Treatments / Drainage / Weather & Tank Sealing', "
        "'Skins, Doors & Panels' and 'Decision Making / Assumptions / Risk Analysis / Trade Off'. Some bundles are synonyms or a close family, "
        "others are distinct topics, which makes tagging ambiguous and works against single-topic, mutually exclusive options.", bundled, "Auto-detected (pattern) + curated")

    # 4. Duplicate / near-duplicate names
    seen = collections.defaultdict(list)
    for v in values:
        seen[slug(v["title"])].append(v["id"])
    mapped = {v["id"]: set(sum((v.get("mapsTo") or {}).values(), [])) for v in values if v["facet"] == "srcsystem"}
    def _is_mapping_pair(ids):  # tracker entry + the agreed value it maps to (same name by design)
        return len(ids) == 2 and any(a in mapped and b in mapped[a] for a in ids for b in ids)
    dups = [ids for ids in seen.values() if len(ids) > 1 and not _is_mapping_pair(ids)]
    if dups:
        add("Duplicate names", "Identical names after normalisation.", sum(dups, []))

    # 5. Curated overlaps (mutual exclusivity concerns)
    add("Possible overlaps within the Aircraft System list",
        "Several options appear to overlap rather than being mutually exclusive: 'Electrical - Equipment' vs 'Power Generation & Distribution'; "
        "'Structure' vs 'Skins, Doors & Panels' vs 'Windscreen & Canopy'; 'Mission Systems' vs 'Radar / Sensors', 'Electronic Warfare', 'Communications' and 'Data Links'; "
        "'Vehicle Management Systems' vs 'Flight Control Systems'; 'Armaments' vs 'Stores Integration'; "
        "'Thermal Management / Fire Protection' vs 'Environmental Control Systems'.",
        ["KN-0015", "KN-0028", "KN-0033", "KN-0031", "KN-0036", "KN-0025", "KN-0030", "KN-0016", "KN-0011", "KN-0013",
         "KN-0035", "KN-0018", "KN-0009", "KN-0032", "KN-0034", "KN-0017"], "Curated", "Resolved",
        "The agreed two-level System facet (2 Oct 2026) and the System rule resolve these overlaps (one function per System; each item in exactly one System). "
        "Electrical equipment and looms moved to Design Type; Mission Systems became a System Group; Structure split into Primary and Secondary; "
        "Armaments merged into Stores Integration; Thermal Management and Fire Protection separated. See the tracker-to-facet mapping issue below.")
    add("Ground Support Equipment and Flight Test Instrumentation were listed as Aircraft Systems",
        "The tracker listed 'Ground Support Equipment' and 'Flight Test Instrumentation' as Aircraft Systems, mixing product scope with aircraft function.",
        ["KN-0021", "KN-0019", "PS-0002", "SYS-0025"], "Curated", "Resolved",
        "Ground Support Equipment is now Product Scope 'Ground Equipment'. Flight Test Instrumentation is installed on the aircraft, so it is its own System "
        "(SYS-0025, new group Test & Instrumentation). The System facet applies across all Product Scopes.")
    add("Tracker mapping questions answered (Ground Support Equipment, Flight Test Instrumentation, Power Generation & Distribution)",
        "Earlier mapping notes asked how Systems apply to ground equipment, whether on-aircraft test installations need a System, and whether 'Power Generation & Distribution' covered non-electrical power.",
        ["KN-0021", "KN-0019", "KN-0028", "SYS-0025", "SYS-0008"], "Curated", "Resolved",
        "Systems apply across all Product Scopes, so ground equipment takes Systems like the aircraft; Flight Test Instrumentation is its own System; the System is renamed "
        "'Electrical Power Generation & Distribution (electrical only)' (hydraulic and pneumatic power belong to Hydraulics and Pneumatics). These three now map cleanly.")
    add("Overlaps between facets",
        "Some options repeat across facets: Discipline 'Maintainability / Reliability / Ground Equipment' vs Aircraft System 'Ground Support Equipment'; "
        "Discipline 'Safety' vs Aircraft System 'Crew Escape & Safety'; Discipline 'Mechanical Systems' vs individual mechanical Aircraft Systems; "
        "Discipline 'Cost' vs 'Affordability'; Skill 'Leadership / People' vs the trait category 'Leadership'; Skill 'Collaboration / Talent Recognition' vs "
        "trait category 'Collaboration and Influence'; Skill 'Time Management' vs trait 'Prioritisation'; Skill 'Decision Making / Assumptions / Risk Analysis / Trade Off' "
        "vs traits 'Decisiveness' and 'Comfortable making decisions with incomplete information'.",
        ["KN-0047", "KN-0021", "KN-0052", "KN-0012", "KN-0050", "KN-0041", "KN-0038", "SK-0001", "SK-0007", "SK-0011", "TR-0058", "SK-0003", "TR-0013", "TR-0002"], "Curated", "Partly resolved",
        "Partly resolved: Ground Support Equipment is now Product Scope 'Ground Equipment', so it is no longer a System; the Discipline name still includes 'Ground Equipment'. "
        "The other overlaps remain open.")
    add("Aircraft System list differs from the requirements doc's System facet",
        "The tracker's Aircraft System list does not match the System facet in the requirements draft (e.g. 'Structure' vs 'Primary Substructure'; "
        "'Hydraulics System' vs 'Hydraulics'; 'Skins, Doors & Panels' grouped vs Skins / Panels / Doors). The two lists need reconciling into one controlled facet.",
        ["KN-0033", "KN-0022", "KN-0031"], "Curated", "Resolved",
        "Resolved: the tracker list has been reconciled into the agreed System facet (Primary Structure / Secondary Structure, Hydraulics, Skins, Doors & Panels kept grouped for now). "
        "The KN entries remain as source references and each shows its mapping.")

    # 6. Naming inconsistencies
    add("Naming inconsistencies",
        "Mixed conventions: 'Hydraulics System' and 'Fuel System' (singular 'System'), 'Flight Control Systems', 'Navigation Systems', 'Mission Systems' (plural) "
        "and 'Pneumatics', 'Propulsion' (no suffix); separators vary between ' - ', ' / ', ' & ' and ','; 'Electro-Magnetic Compatibility' is usually written "
        "'Electromagnetic Compatibility'. The facet is called 'ASEL Stage' in the workbook but 'Lifecycle Stage' in the requirements; trait categories use 'and' "
        "('Collaboration and Influence') while knowledge areas use '&'.",
        ["KN-0022", "KN-0020", "KN-0018", "KN-0026", "KN-0025", "KN-0027", "KN-0029", "KN-0042"], "Curated", "Partly resolved",
        "Partly resolved: the agreed System facet uses consistent names without 'System(s)' suffixes (e.g. Fuel, Hydraulics, Flight Control). "
        "The remaining points (separators, 'Electro-Magnetic', 'ASEL Stage', 'and' vs '&') are open.")
    order_disc = [v["title"] for v in values if v["facet"] == "discipline"]
    if order_disc != sorted(order_disc):
        add("Discipline list not in a consistent order",
            "The Aircraft System list is alphabetical, but the Discipline list is not: 'Quality' (KN-0059) has been appended after 'Weight'. "
            "Harmless for IDs (which are permanent) but suggests a list that is extended ad hoc; a Sort_Order field would make intent explicit.", ["KN-0059"])
    # 7. Text quality
    txt = []
    for vid, r in raw.items():
        d = r["desc"]
        if isinstance(d, str) and (d != d.strip() or not d.strip().endswith(".")):
            txt.append(vid)
        if isinstance(d, str) and "detremental" in d:
            txt.append(vid)
    add("Description wording and style",
        "TR-0059 description contains a spelling error ('detremental' for 'detrimental') and is written in the first person ('my own ... my priorities') "
        "unlike the other third-person descriptions; TR-0058 has a trailing space and a different style ('Ability to ...'); SK-0011 lacks a closing full stop; "
        "apostrophes mix straight (TR-0009) and curly (SK-0007, TR-0014) forms; trait names TR-0058/TR-0059 use 'Ability to...' phrasing and quotation marks "
        "unlike other trait names. Skills_Register has no category column, unlike Traits_Register.",
        sorted(set(txt + ["TR-0059", "TR-0058", "SK-0011", "TR-0009", "SK-0007", "TR-0014"])), "Auto-detected + curated")
    # 8. Tracker -> agreed facet mapping (auto from KN_MAP)
    unclean = [v for v in values if v["facet"] == "srcsystem" and not v.get("mappingClean")]
    add("Tracker Aircraft System entries that do not map cleanly to the agreed facets (%d of 28)" % len(unclean),
        " ".join("%s %s: %s" % (v["id"], v["title"], v["mappingNote"]) for v in unclean),
        [v["id"] for v in unclean], "Auto-detected (from mapping table)", "Open",
        "For review: each mapping is shown on the tracker entry's page. The other entries map one-to-one.")
    nodesc = [v["id"] for v in values if v["facet"] in ("sysgroup", "system") and not v["description"]]
    add("Agreed System facet values have no descriptions yet",
        "The System Groups and Systems were agreed by name and rule only. Each needs a precise description of its function and boundary (1B.9) so items can be placed in exactly one System.",
        nodesc, "Auto-detected")
    add("Discipline options overlapping the new Design Type facet or treated as design properties",
        "Discipline 'Mechanical Systems' (KN-0050) conflicts with the decision that mechanical, flexible, kinematic and similar aspects are design properties, not categories. "
        "'Standard Parts & Supply Chain' (KN-0054) overlaps Design Type 'Standard Parts'; 'Environmental Factors / Protection Treatments / ... Tank Sealing' (KN-0043) overlaps "
        "'Coatings, Sealants & Treatments'; 'Materials Engineering' (KN-0049) and 'Manufacturing Methods' (KN-0048) overlap the material/process basis of Design Type.",
        ["KN-0050", "KN-0054", "DT-0012", "KN-0043", "DT-0011", "KN-0049", "KN-0048"], "Curated", "Open")
    return issues


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1])
