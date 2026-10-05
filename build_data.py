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
    {"key": "stage", "level": "X-CROSS", "levelLabel": "Cross-cutting (not assigned to a facet level; applies at every build level): lifecycle", "label": "Lifecycle Stage", "plural": "Lifecycle Stages", "source": "Knowledge_Register (Knowledge_Category = 'ASEL Stage')",
     "note": "ASEL = Air System Engineering Lifecycle. Register order is lifecycle order."},
    {"key": "sysgroup", "level": "L1", "levelLabel": "Facet level 1: directly below any Product Scope option, e.g. the Aircraft scope (upper tier of the System facet)", "label": "System Group", "plural": "System Groups", "source": "Agreed System facet (2 Oct 2026), upper tier",
     "note": "Upper tier of the two-tier System facet. A data object's System Group is derived from its System tag(s)."},
    {"key": "system", "level": "L1", "levelLabel": "Facet level 1: directly below any Product Scope option, e.g. the Aircraft scope (lower tier of the System facet)", "label": "System", "plural": "Systems", "source": "Agreed System facet (2 Oct 2026), lower tier; mapped from tracker Aircraft System list",
     "note": "Rule: a System is a set of items that work together to perform one function. Every Part Instance has exactly one home System, the System it is part of (a bracket is Secondary Structure), and may have typed supports links to the Systems it carries or serves. Assemblies derive their Systems from their parts (derived tags), so a loom shows the Systems of its wires. Part Definitions carry no System. One shared System list is used for all Product Scopes, and each System records the Product Scopes it applies to."},
    {"key": "designtype", "level": "L1", "levelLabel": "Facet level 1: directly below any Product Scope option, e.g. the Aircraft scope", "label": "Design Type", "plural": "Design Types", "source": "Agreed Design Type facet (2 Oct 2026; revised 4 Oct 2026)",
     "note": "The kind of design work: material, process or item kind only. Bought-in items normally have no Design Type. Coatings, sealants and treatments are not Design Types: they are finish-specification records linked to the parts they are applied to. Status: agreed for now, subject to refinement."},
    {"key": "productscope", "level": "L0", "levelLabel": "Facet level 0: the top facet. Aircraft, Ground Equipment, Test Equipment and Facilities are peers; Full Aircraft is the top item of the Aircraft scope", "label": "Product Scope", "plural": "Product Scopes", "source": "Agreed Product Scope facet (2 Oct 2026; boundaries 4 Oct 2026)",
     "note": "Which product an item belongs to; facet level 0. The four options are peers. Facilities are fixed infrastructure (buildings, fuel farms, fixed rigs); Test Equipment is movable test kit; Ground Equipment is movable support kit that is not test kit. Each System records the Product Scopes it applies to; connections between items in different scopes are links (interfaces), not a parent build level."},
    {"key": "majorunit", "level": "BUILD", "levelLabel": "Build Level 1 of the Aircraft scope (a build level, not a facet level; Aircraft scope only)", "label": "Major Unit", "plural": "Major Units", "source": "Agreed Major Unit facet (4 Oct 2026)",
     "note": "Which manufactured major unit an item is built into. Applies to the Aircraft scope only. Items not built into any Major Unit sit under Final Assembly, at the same build level as the Major Units, because they are assembled with the Major Units to form the Full Aircraft. Other Product Scopes will define their own build breakdown later."},
    {"key": "itemsource", "level": "X-CROSS", "levelLabel": "Cross-cutting (not assigned to a facet level; applies at every build level): how an item is obtained", "label": "Source", "plural": "Sources", "source": "Agreed Source facet (4 Oct 2026)",
     "note": "How an item is obtained: made in-house, a catalogue standard part, or bought-in equipment. Independent of Design Type; bought-in items normally have no Design Type."},
    {"key": "discipline", "level": "X-CROSS", "levelLabel": "Cross-cutting (not assigned to a facet level; applies at every build level): knowledge area", "label": "Discipline", "plural": "Disciplines", "source": "Knowledge_Register (Knowledge_Category = 'Discipline')", "note": ""},
    {"key": "skill", "level": "PEOPLE", "levelLabel": "Linked register (not a facet; not used to classify items)", "label": "Skill", "plural": "Skills", "source": "Skills_Register", "note": ""},
    {"key": "trait", "level": "PEOPLE", "levelLabel": "Linked register (not a facet; not used to classify items)", "label": "Trait", "plural": "Traits", "source": "Traits_Register (Trait_Self_Assessment column not used)", "note": ""},
    {"key": "srcsystem", "level": "SOURCE", "levelLabel": "Source reference only (not used for tagging)", "label": "Tracker Aircraft System (source)", "plural": "Tracker Aircraft Systems (source)", "source": "Knowledge_Register (Knowledge_Category = 'Aircraft System')",
     "note": "The 28 original tracker entries, kept with their permanent KN IDs as source references. They are no longer used for tagging: each is mapped to the agreed System, Design Type, Source or Product Scope options."},
]

# Facet levels: every facet is assigned to a defined facet level. Views are offered as alternatives only within the
# same group; a view's top facet must be at the group's facet level. Build levels (Major Unit) are not facet levels.
VIEWS = [
    {"key": "lifecycle", "label": "Lifecycle", "group": "Cross-cutting", "levels": ["stage", "system"], "description": "Lifecycle Stage \u203a System \u203a content"},
    {"key": "discipline", "label": "Discipline", "group": "Cross-cutting", "levels": ["discipline", "stage"], "description": "Discipline \u203a Lifecycle Stage \u203a content"},
    {"key": "productscope", "label": "Product Scope", "group": "Facet level 0: Product Scope", "levels": ["productscope", "sysgroup", "system"], "description": "Product Scope \u203a System Group \u203a System (applicable Systems only) \u203a content"},
    {"key": "system", "label": "System", "group": "Facet level 1: below a Product Scope option", "scopeSelectable": True, "levels": ["sysgroup", "system", "stage"], "description": "System Group \u203a System \u203a Lifecycle Stage \u203a content"},
    {"key": "designtype", "label": "Design Type", "group": "Facet level 1: below a Product Scope option", "scopeSelectable": True, "levels": ["designtype", "system"], "description": "Design Type \u203a System \u203a content"},
    {"key": "majorunit", "label": "Major Unit", "group": "Build Level 1: Aircraft scope only", "fixedScope": "PS-0001", "levels": ["majorunit", "system"], "description": "Full Aircraft \u203a Major Unit or Final Assembly (Build Level 1) \u203a System \u203a content"},
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
    ("DT-0010", "Electrical Looms", "Looms are a Design Type, not a System: each wire's home System is the System it serves, and a loom shows the Systems of its wires (derived tags)."),
]
# DT-0011 (Coatings, Sealants & Treatments), DT-0012 (Standard Parts) and DT-0013 (Bought-in Equipment) were retired on
# 4 Oct 2026 (v0.7). IDs are permanent, so these three are never reused. Standard parts and bought-in equipment are now
# options of the Source facet; coatings, sealants and treatments are finish-specification records (HUB-FINISH).
RETIRED_DESIGN_TYPES = {"DT-0011": "Coatings, Sealants & Treatments", "DT-0012": "Standard Parts", "DT-0013": "Bought-in Equipment"}
SOURCES = [
    ("SRC-0001", "Make", "Designed and made by or for the project to its own design (machined, sheet, composite, moulded, looms, pipework and so on)."),
    ("SRC-0002", "Standard Part", "Catalogue parts to a published standard, such as fasteners, seals and fittings."),
    ("SRC-0003", "Bought-in Equipment", "Equipment bought from a supplier to a specification, such as pumps, LRUs and actuators. Normally has no Design Type."),
]
MAJOR_UNITS = [
    ("MU-0001", "Front Fuselage", "Items built into the front fuselage major unit before final assembly."),
    ("MU-0002", "Centre Fuselage", "Items built into the centre fuselage major unit before final assembly."),
    ("MU-0003", "Rear Fuselage", "Items built into the rear fuselage major unit before final assembly."),
    ("MU-0004", "Wings", "Items built into the wing major units before final assembly."),
    ("MU-0005", "Fins", "Items built into the fin major units before final assembly."),
    ("MU-0006", "Final Assembly", "Not a Major Unit: holds the items that are not built into any Major Unit, such as pipes and looms installed at final assembly to connect Major Units. They sit at Build Level 1 because they are assembled with the Major Units to form the Full Aircraft."),
]
# System -> applicable Product Scopes (PS-0001 Aircraft, PS-0002 Ground Equipment, PS-0003 Test Equipment, PS-0004 Facilities).
# Fuel and Mission Systems were stated by Daniel Wagner (4 Oct 2026); the rest is an initial proposal to be confirmed.
_A, _G, _T, _F = "PS-0001", "PS-0002", "PS-0003", "PS-0004"
SYSTEM_SCOPES = {
    "SYS-0001": [_A, _G, _T, _F], "SYS-0002": [_A, _G, _T, _F], "SYS-0003": [_A, _G, _T], "SYS-0004": [_A],
    "SYS-0005": [_A], "SYS-0006": [_A], "SYS-0007": [_A, _G, _F], "SYS-0008": [_A, _G, _T, _F], "SYS-0009": [_A, _G, _T], "SYS-0010": [_A, _G, _T],
    "SYS-0011": [_A], "SYS-0012": [_A], "SYS-0013": [_A], "SYS-0014": [_A],
    "SYS-0015": [_A, _G], "SYS-0016": [_A, _G, _T], "SYS-0017": [_A, _F], "SYS-0018": [_A],
    "SYS-0019": [_A],
    "SYS-0020": [_A], "SYS-0021": [_A], "SYS-0022": [_A], "SYS-0023": [_A], "SYS-0024": [_A],
    "SYS-0025": [_A],
}
SYSTEM_SCOPES_CONFIRMED = {"SYS-0007", "SYS-0020", "SYS-0021", "SYS-0022", "SYS-0023", "SYS-0024"}
PRODUCT_SCOPES = [
    ("PS-0001", "Aircraft", "The aircraft product. Its top item is Full Aircraft."),
    ("PS-0002", "Ground Equipment", "Movable support kit that is not test kit, including ground support equipment (tracker KN-0021). Its top items sit at Build Level 0, alongside Full Aircraft."),
    ("PS-0003", "Test Equipment", "Movable test kit, as a product in its own right. Flight test instrumentation installed on the aircraft is a System (Flight Test Instrumentation), not this scope; fixed test rigs are Facilities."),
    ("PS-0004", "Facilities", "Fixed infrastructure, for example buildings, fuel farms and fixed test rigs. Facilities have Systems like any other scope; their connections to other items are links (interfaces), not a parent build level."),
]
# Tracker Aircraft System (KN) -> agreed facets. clean=False means the mapping is not one-to-one; note explains.
KN_MAP = {
    "KN-0009": ({"system": ["SYS-0024"]}, False, "Armaments merged with Stores Integration into one System, 'Stores Integration (incl. Armaments)'. Two tracker entries map to one value."),
    "KN-0010": ({"system": ["SYS-0019"]}, True, ""),
    "KN-0011": ({"system": ["SYS-0022"]}, True, ""),
    "KN-0012": ({"system": ["SYS-0018"]}, True, ""),
    "KN-0013": ({"system": ["SYS-0023"]}, True, ""),
    "KN-0014": ({"designtype": ["DT-0010"]}, False, "No longer a System. Maps to Design Type 'Electrical Looms'; each wire's home System is the System it serves, and a loom's Systems are derived from its wires."),
    "KN-0015": ({"itemsource": ["SRC-0003"], "system": ["SYS-0008"]}, False, "Split across two facets: Source 'Bought-in Equipment' plus System 'Electrical Power Generation & Distribution (electrical only)'. Electrical equipment that serves another function (e.g. a sensor's power supply) takes that function's System as its home System, so this System tag is a default, not a certainty. (Until 4 Oct 2026 this mapped to the retired Design Type DT-0013.)"),
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
     "tags": {"stage": ["KN-0005"], "system": ["SYS-0007"], "designtype": ["DT-0009"], "itemsource": ["SRC-0001"], "productscope": ["PS-0001"], "majorunit": ["MU-0002", "MU-0004"], "discipline": ["KN-0053", "KN-0049", "KN-0043"],
              "skill": ["SK-0003"], "trait": ["TR-0006", "TR-0007"]},
     "summary": "How fuel system design questions typically come together once the design moves into [[KN-0005]].",
     "sections": [
        ["Why this intersection matters",
         "In detailed design the routing, supports and fittings of the [[SYS-0007]] become fixed geometry. Decisions taken here are "
         "expensive to change later, so the system, structural and survivability viewpoints need to be considered together rather than in sequence."],
        ["Typical considerations (illustrative)",
         "- Route pipes and equipment so that a single event cannot disable redundant paths (see [[KN-0053]]).\n"
         "- Confirm material compatibility of pipes, seals and coatings with the fluid and environment (see [[KN-0049]]).\n"
         "- Consider sealing, drainage and protection treatments in and around tank areas (see [[KN-0043]]); these are finish specifications linked to the parts (see [[HUB-FINISH]]).\n"
         "- Record assumptions and trade-offs explicitly so they can be reviewed (see [[SK-0003]])."],
        ["Questions to ask at review",
         "- What are the knock-on effects of this routing on neighbouring systems and structure? ([[TR-0007]])\n"
         "- Has the design been considered as part of the whole aircraft rather than in isolation? ([[TR-0006]])"],
     ]},
    {"id": "EX-0002", "title": "Landing Gear in Preliminary Design",
     "tags": {"stage": ["KN-0004"], "system": ["SYS-0013"], "designtype": ["DT-0002"], "itemsource": ["SRC-0001", "SRC-0003"], "productscope": ["PS-0001"], "majorunit": ["MU-0002"], "discipline": ["KN-0050", "KN-0056", "KN-0058"],
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
     "tags": {"stage": ["KN-0007"], "system": ["SYS-0008", "SYS-0011"], "designtype": ["DT-0010"], "itemsource": ["SRC-0001"], "productscope": ["PS-0001"], "majorunit": ["MU-0006"], "discipline": ["KN-0042", "KN-0040", "KN-0048"],
              "skill": ["SK-0009"], "trait": ["TR-0030", "TR-0055"]},
     "summary": "An example of the issues that arise once looms are being built and installed, during [[KN-0007]].",
     "sections": [
        ["Why this intersection matters",
         "Once the aircraft is in production, queries on [[DT-0010]] often concern installation, clearances and build sequence. "
         "Responding well needs an understanding of both the original design intent and the manufacturing reality.\n"
         "Under the derived-tags rule this loom is not given a System directly: each wire's home System is the System it serves, so the loom shows "
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
     "tags": {"stage": ["KN-0006"], "system": ["SYS-0009"], "designtype": ["DT-0009", "DT-0007"], "itemsource": ["SRC-0001", "SRC-0002", "SRC-0003"], "productscope": ["PS-0001"], "discipline": ["KN-0057", "KN-0039", "KN-0052"],
              "skill": ["SK-0008", "SK-0010"], "trait": ["TR-0051", "TR-0053"]},
     "all": ["majorunit"],
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
     "tags": {"stage": ["KN-0005"], "system": ["SYS-0007"], "designtype": ["DT-0009"], "itemsource": ["SRC-0001", "SRC-0002"], "productscope": ["PS-0001", "PS-0002"], "majorunit": ["MU-0004"], "discipline": ["KN-0040", "KN-0052"],
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
    {"id": "EX-0006", "title": "Home System and Supports Links: a Pipe Bracket",
     "tags": {"stage": ["KN-0005"], "system": ["SYS-0002"], "designtype": ["DT-0002"], "itemsource": ["SRC-0001"], "productscope": ["PS-0001"], "majorunit": ["MU-0002"], "discipline": ["KN-0040"],
              "skill": ["SK-0002"], "trait": ["TR-0007"]},
     "supports": {"system": ["SYS-0007", "SYS-0009"]},
     "exampleItem": {"name": "Pipe support bracket (example Part Instance)",
                     "tags": {"productscope": "PS-0001", "majorunit": "MU-0002", "system": "SYS-0002", "designtype": "DT-0002", "itemsource": "SRC-0001"},
                     "supports": ["SYS-0007", "SYS-0009"]},
     "summary": "An example of the home System rule: a bracket is [[SYS-0002]], with typed supports links to the Systems whose pipes it carries.",
     "sections": [
        ["The rule",
         "Each Part Instance has exactly one home System, the System it is part of. A bracket is part of the structure, so its home System is [[SYS-0002]]. "
         "It also carries a fuel pipe and a hydraulic pipe, so it has typed supports links to [[SYS-0007]] and [[SYS-0009]]. "
         "Supports links are not extra System tags: they are shown separately, and a change to the bracket flags the Systems it supports for review, but no further."],
        ["One option per facet for items",
         "As a physical item, the bracket takes exactly one option per facet (see the example item table below). Knowledge records such as this page may carry several options per facet, or All. "
         "The Part Definition of the bracket carries no System, because the same design may be used in other places and Systems."],
        ["Questions to ask at review",
         "- If this bracket changes, which Systems does it support, and have their owners been told? ([[TR-0007]])\n"
         "- Is the bracket's interface with each pipe recorded once and referenced from both sides? (see [[KN-0040]], [[SK-0002]])"],
     ]},
]


LESSON_NOTE = ("EXAMPLE lesson written for the Engineering Hub prototype to demonstrate the Lessons Learned template and facet filtering. "
               "It is generic and fictional, does not describe a real event, and is NOT authoritative engineering guidance.")

# Example Lessons Learned. Same template for every lesson. Lessons are knowledge records, so they may carry several
# options per facet, or "all" (every option of a facet). Mandatory tags: >=1 Lifecycle Stage and >=1 System.
LESSONS = [
    {"id": "LL-0001", "title": "Pipe-to-structure clearances found late in the design",
     "tags": {"stage": ["KN-0005"], "system": ["SYS-0007", "SYS-0001"], "designtype": ["DT-0009", "DT-0002"], "itemsource": ["SRC-0001"], "productscope": ["PS-0001"], "majorunit": ["MU-0002", "MU-0004"], "discipline": ["KN-0056", "KN-0040"]},
     "summary": "Clearance problems between pipe runs and structure were only found when the full assembly model was checked.",
     "whatHappened": "Pipe routes and structural parts were developed in separate models. When they were combined for a design review, several locations had insufficient clearance once tolerances and pipe movement were included.",
     "rootCause": "No agreed space-allocation model or regular combined clash check during development; tolerance stack-ups were not included in the clearance criteria.",
     "recommendation": "Agree space allocation early, run combined clash checks at a set frequency, and define clearance criteria that include tolerances and in-service movement.",
     "applicability": "Any routed system (fuel, hydraulic, electrical) installed close to structure, from Preliminary Design onwards."},
    {"id": "LL-0002", "title": "Seal material not compatible with the operating fluid",
     "all": ["majorunit"],
     "tags": {"stage": ["KN-0006"], "system": ["SYS-0009"], "designtype": ["DT-0007"], "itemsource": ["SRC-0002"], "productscope": ["PS-0001"], "discipline": ["KN-0049", "KN-0057"]},
     "summary": "A seal degraded during endurance testing because its compatibility with the fluid had been assumed rather than confirmed.",
     "whatHappened": "During an endurance test a seal swelled and leaked. Investigation showed the selected seal compound was not approved for the fluid at the tested temperature range.",
     "rootCause": "Material selection relied on a similar earlier design; the compatibility assumption was not recorded or checked against the actual fluid and temperature range.",
     "recommendation": "Record material compatibility as an explicit, checked requirement for every fluid-wetted part, and verify it against current fluid and temperature data before test.",
     "applicability": "All fluid systems; most relevant during Detailed Design and Qualification / Certification."},
    {"id": "LL-0003", "title": "Loom chafing at panel edges",
     "derived": {"system": "The loom's System tags (Electrical Power Generation & Distribution, Navigation) are derived from its wires; Skins, Doors & Panels is tagged because the panel is part of the lesson."},
     "tags": {"stage": ["KN-0007", "KN-0008"], "system": ["SYS-0008", "SYS-0014", "SYS-0003"], "designtype": ["DT-0010"], "itemsource": ["SRC-0001"], "productscope": ["PS-0001"], "majorunit": ["MU-0001"], "discipline": ["KN-0040", "KN-0047"]},
     "summary": "Electrical looms rubbed against panel edges after repeated panel removal for maintenance.",
     "whatHappened": "Inspections found wear on loom sleeving near a frequently removed access panel. The loom was correctly installed but moved each time the panel was removed and refitted.",
     "rootCause": "Loom support design considered the installed state only, not the movement caused by maintenance access.",
     "recommendation": "Assess loom supports and clearances for maintenance actions as well as the installed state; add edge protection where panels are removed regularly.",
     "applicability": "Looms and pipes near removable panels and doors; check in Detailed Design and when maintenance procedures change."},
    {"id": "LL-0004", "title": "Mass growth from unrecorded assumptions",
     "tags": {"stage": ["KN-0004"], "system": ["SYS-0013"], "designtype": ["DT-0004"], "itemsource": ["SRC-0001", "SRC-0003"], "productscope": ["PS-0001"], "majorunit": ["MU-0002"], "discipline": ["KN-0058"]},
     "summary": "Early mass estimates grew significantly because the assumptions behind them were not recorded.",
     "whatHappened": "The mass of a mechanism grew steadily as the design matured. Reviewers could not tell which items had been included in the early estimate, so growth could not be predicted or challenged.",
     "rootCause": "Mass estimates were recorded as single numbers without their scope, assumptions or maturity.",
     "recommendation": "Store each mass estimate with its scope, assumptions and maturity level, and hold a growth allowance appropriate to that maturity.",
     "applicability": "All systems and structure from Initial System Design to Detailed Design."},
    {"id": "LL-0005", "title": "Maintenance access not considered for equipment replacement",
     "tags": {"stage": ["KN-0005"], "system": ["SYS-0009", "SYS-0007"], "designtype": ["DT-0009"], "itemsource": ["SRC-0003", "SRC-0001"], "productscope": ["PS-0001"], "majorunit": ["MU-0003"], "discipline": ["KN-0047", "KN-0045"]},
     "summary": "A replaceable item could only be removed after removing several other items.",
     "whatHappened": "During a maintainability review it was found that removing one line-replaceable item required disconnecting neighbouring pipes and equipment, increasing maintenance time and the risk of errors.",
     "rootCause": "Removal paths were not modelled or reviewed; maintainability was assessed after the installation layout had been fixed.",
     "recommendation": "Model removal and replacement paths for replaceable items as part of layout design, and include maintainers in early layout reviews.",
     "applicability": "Any replaceable equipment in congested bays; Preliminary and Detailed Design."},
    {"id": "LL-0006", "title": "Ambiguous requirement led to rework",
     "all": ["majorunit"],
     "tags": {"stage": ["KN-0001"], "system": ["SYS-0011"], "productscope": ["PS-0001"], "discipline": ["KN-0051", "KN-0039"]},
     "summary": "A requirement that could be read two ways was implemented differently by two teams.",
     "whatHappened": "Two teams interpreted the same requirement differently. The difference was found at integration, and one design had to be reworked.",
     "rootCause": "The requirement used undefined terms and had no stated verification method, so its meaning was never tested before design started.",
     "recommendation": "Review each requirement for single interpretation and define its verification method when it is written; hold requirements as linked structured data rather than prose.",
     "applicability": "All systems; most important at Requirements Capture / Concept."},
    {"id": "LL-0007", "title": "Refuelling coupling tolerances agreed separately on each side",
     "tags": {"stage": ["KN-0005"], "system": ["SYS-0007"], "designtype": ["DT-0009"], "itemsource": ["SRC-0001", "SRC-0002"], "productscope": ["PS-0001", "PS-0002", "PS-0004"], "majorunit": ["MU-0004"], "discipline": ["KN-0040", "KN-0052"]},
     "summary": "Aircraft, ground refuelling equipment and the fuel farm were each designed to their own tolerances at a shared coupling.",
     "whatHappened": "During an interface check the aircraft refuelling coupling, the ground equipment nozzle and the fuel farm connection were found to have been toleranced separately, so some combinations would not connect reliably.",
     "rootCause": "The interface between items in different Product Scopes was not recorded as one linked interface record, so no single owner saw all three sides.",
     "recommendation": "Record cross-scope interfaces once, as typed interface links between the items on each side, so a change on one side flags the others for review.",
     "applicability": "Any System that crosses Product Scopes (for example Fuel across Aircraft, Ground Equipment and Facilities)."},
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
                           "group": gid, "agreed": True, "scopes": SYSTEM_SCOPES[sid], "scopesConfirmed": sid in SYSTEM_SCOPES_CONFIRMED})
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
    for xid, xname, xdesc in SOURCES:
        values.append({"id": xid, "facet": "itemsource", "title": xname, "description": xdesc, "sourceCategory": None, "category": None, "agreed": True, "agreedV13": True})
    for mid, mname, mdesc in MAJOR_UNITS:
        values.append({"id": mid, "facet": "majorunit", "title": mname, "description": mdesc, "sourceCategory": None, "category": None, "agreed": True, "agreedV13": True,
                       "buildLevel": 1, "scopes": ["PS-0001"]})
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
        for k in ("group", "members", "mapsTo", "mappingClean", "mappingNote", "sources", "agreed", "status", "scopes", "scopesConfirmed", "buildLevel"):
            if k in v:
                pg[k] = v[k]
        if v.get("agreedV13"):
            pg["origin"] = {"document": "Facet decisions agreed by Daniel Wagner, 4 Oct 2026 (recorded in 'Requirements Prompt - Draft', sections 1B.7, 1C and 1F)", "issue": "Draft v13", "url": None, "references": []}
        elif v.get("agreed"):
            pg["origin"] = {"document": "Facet decisions agreed by Daniel Wagner, 2 Oct 2026 (recorded in 'Requirements Prompt - Draft', sections 1B.7 and 1F)", "issue": "Draft v11", "url": None, "references": []}
        else:
            pg["origin"] = {"document": "Tracker workbook, " + {"skill": "Skills_Register", "trait": "Traits_Register"}.get(v["facet"], "Knowledge_Register"),
                            "issue": "not recorded in source", "url": None, "references": []}
        pages.append(pg)
    for s in SAMPLES:
        pages.append({"id": s["id"], "type": "content", "title": s["title"], "summary": s["summary"],
                      "sections": [{"heading": h, "body": b} for h, b in s["sections"]],
                      "tags": s["tags"], "derived": s.get("derived", {}), "example": True, "exampleNote": EXAMPLE_NOTE, "recordKind": "knowledge",
                      **{k: s[k] for k in ("all", "supports", "exampleItem") if k in s},
                      "origin": {"document": "Engineering Hub prototype (example text)", "issue": "Draft 0.1", "url": None, "references": []}})

    for l in LESSONS:
        pages.append(dict(l, type="lesson", example=True, exampleNote=LESSON_NOTE, recordKind="knowledge",
                          origin={"document": "None (example lesson written for the Engineering Hub prototype)", "issue": "n/a", "url": None, "references": []}))
    pages.append({"id": "HUB-LESSONS", "type": "special", "title": "Lessons Learned",
                  "summary": "All lessons learned, filterable by any combination of Lifecycle Stage, Product Scope, System, Design Type and Discipline."})
    # ---- Framework Hub pages (v0.6): generic, project-independent; no production data ----
    pages.append({"id": "HUB-FRAMEWORK", "type": "special", "title": "Framework vs Production",
                  "summary": "This site is the Framework Hub: the standard, project-independent Engineering Hub. Each project gets a Production Hub, "
                             "an instance of the framework tailored to that project, which adds the project's working data and links to its production data.",
                  "sections": FRAMEWORK_SECTIONS, "images": [IMG_RPV]})
    pages.append({"id": "HUB-PRODEX", "type": "special", "title": "Production Hub (illustrative)", "example": True,
                  "summary": "An illustration of what a project's Production Hub adds on top of the framework. Every panel is an empty placeholder: "
                             "the Framework Hub never holds project data."})
    pages.append({"id": "HUB-BUILDLEVELS", "type": "special", "title": "Build levels",
                  "summary": "Build levels are the levels of the product-build hierarchy within a Product Scope. They are numbered separately from facet levels.",
                  "sections": BUILD_SECTIONS, "images": [IMG_BUILD]})
    pages.append({"id": "HUB-FINISH", "type": "special", "title": "Finish specifications",
                  "summary": "Coatings, sealants and treatments are recorded as Finish Specification records linked to the parts they are applied to, not as a Design Type.",
                  "sections": FINISH_SECTIONS})
    pages.append({"id": "HUB-GLOSSARY", "type": "special", "title": "Glossary",
                  "summary": "The terms used throughout the Hub and the requirements (section 0.4 of the requirements draft v13), each with one meaning.",
                  "glossary": GLOSSARY})
    for pg in pages:
        if pg["type"] == "majorunit":
            pg["images"] = [IMG_BUILD]
        if pg["type"] == "productscope":
            pg["images"] = [IMG_FACETS]
    issues = find_issues(values, raw, lookups, rows)
    pages.append({"id": "HUB-ISSUES", "type": "special", "title": "Framework issues",
                  "summary": "Inconsistencies found in the source tracker framework. They are recorded here, not silently fixed, "
                             "so that the controlled lists can be corrected at source."})

    data = {
        "meta": {"title": "Engineering Hub", "hubKind": "Framework", "version": "0.7.1 (prototype)",
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


# ---- Framework vs Production content (v0.6) ----
IMG_FACETS = {"src": "assets/img/facet-levels.svg",
              "caption": "Facet levels: Product Scope is facet level 0; System and Design Type sit at facet level 1, directly below any Product Scope option; Lifecycle Stage, Source and Discipline are cross-cutting. Items below are organised by build levels (see Build levels).",
              "alt": "Diagram of facet levels. Four Product Scope boxes (Aircraft, Ground Equipment, Test Equipment, Facilities) at facet level 0, System and Design Type boxes at facet level 1, items organised by build levels below, and vertical bands for the cross-cutting facets Lifecycle Stage, Source and Discipline."}
IMG_BUILD = {"src": "assets/img/build-levels.svg",
             "caption": "Build levels of the Aircraft scope: Build Level 0 Full Aircraft; Build Level 1 the Major Units plus Final Assembly; then Assembly, Sub-assembly and Part. Build levels are separate from facet levels.",
             "alt": "Diagram of build levels. Full Aircraft at Build Level 0; six boxes at Build Level 1 (Front Fuselage, Centre Fuselage, Rear Fuselage, Wings, Fins and Final Assembly, the last drawn differently because it is not a Major Unit); Assembly, Sub-assembly and Part below; a side note that facet levels are numbered separately."}
IMG_RPV = {"src": "assets/img/req-prod-ver-links.svg",
           "caption": "Typed links: a Requirement is satisfied by Product data, Product data is supported by Verification data, and Verification demonstrates the Requirement. Each link type sets the direction of change flags; by default a change flags directly linked objects only and the reviewer decides whether to pass it on. AI-proposed links need human confirmation.",
           "alt": "Diagram with three boxes, Requirement, Product and Verification, joined by labelled arrows, a Hub page box linked to all three with dashed arrows, and a change-flag note."}
BUILD_SECTIONS = [
    {"heading": "Build levels of the Aircraft scope",
     "body": "- Build Level 0: Full Aircraft, the top item of the Aircraft scope.\n"
             "- Build Level 1: the Major Units ([[MU-0001]], [[MU-0002]], [[MU-0003]], [[MU-0004]], [[MU-0005]]) and [[MU-0006]].\n"
             "- Build Level 2: Assembly. Build Level 3: Sub-assembly. Build Level 4: Part.\n"
             "In the product-build view every item sits at exactly one build level and has exactly one parent at the build level above. Other views may show the same data object under several branches."},
    {"heading": "Final Assembly",
     "body": "Items that are not built into any Major Unit, for example pipes and looms installed at final assembly to connect Major Units, sit under [[MU-0006]]. "
             "Final Assembly is at Build Level 1 alongside the Major Units because those items are assembled with the Major Units to form the Full Aircraft. It is an option of the Major Unit facet but is not itself a Major Unit."},
    {"heading": "Build levels are not facet levels",
     "body": "Facet levels place facets relative to each other: Product Scope is facet level 0 and System and Design Type are facet level 1, directly below any Product Scope option. "
             "Build levels place items in the product-build hierarchy of one Product Scope. Major Unit is the facet behind Build Level 1 and applies to the Aircraft scope only. See [[HUB-GLOSSARY]]."},
    {"heading": "Other Product Scopes",
     "body": "The top items of [[PS-0002]], [[PS-0003]] and [[PS-0004]] sit at Build Level 0, alongside Full Aircraft. Their lower build levels will be defined later. "
             "Connections between items in different Product Scopes are interface links, not parent build levels."},
    {"heading": "Requirements have their own breakdown",
     "body": "Requirements follow a functional breakdown per Product Scope (for the Aircraft scope: Air System \u203a System \u203a Sub-system \u203a Item), not the build levels. Each Requirement links to the items that meet it."},
]
FINISH_SECTIONS = [
    {"heading": "Why finishes are not a Design Type",
     "body": "A part is designed as one kind of design work (for example [[DT-0002]]) but may be painted, primed, treated and sealed. If coatings were a Design Type option, a part would need several options from one facet, which breaks the one-option rule for items. "
             "So coatings, sealants and treatments are recorded as Finish Specification records and linked to the parts they are applied to. A part may have several Finish Specifications."},
    {"heading": "What a Finish Specification record holds (framework template)",
     "body": "- Permanent ID, title and finish kind (coating, primer, surface treatment, sealant, adhesive).\n"
             "- The specification it is made to, with issue/revision, and its origin.\n"
             "- Typed 'finish applied' links to the parts it is applied to. A change to the Finish Specification flags those parts for review.\n"
             "- Verification status, owner and last reviewed date, like every other record."},
    {"heading": "In the Framework Hub",
     "body": "The Framework Hub defines the template and link type only. Project Finish Specification records belong to a Production Hub. "
             "Related knowledge areas: [[KN-0043]] and [[KN-0049]]."},
    {"heading": "Retired Design Type IDs",
     "body": "Until 4 Oct 2026 the Design Type facet also had DT-0011 Coatings, Sealants & Treatments, DT-0012 Standard Parts and DT-0013 Bought-in Equipment. "
             "These IDs are retired and never reused. Standard parts and bought-in equipment are now options of the Source facet ([[SRC-0002]], [[SRC-0003]]); coatings, sealants and treatments are Finish Specification records."},
]
GLOSSARY = [
    ["Data object", "Anything stored with a unique, permanent identifier. Every item, record and page is a data object."],
    ["Data type", "The kind of data object, which defines its schema: for example Requirement, Part Definition, Part Instance, Verification, Issue, Lesson Learned, Finish Specification, Hub page."],
    ["Item", "A physical product item: a Part Instance, or an assembly of Part Instances. Items take exactly one option per applicable facet; derived tags are kept separate."],
    ["Record", "A data object that is not an item, for example a Requirement, Verification, Issue, Lesson Learned or Finish Specification. Knowledge records (pages, lessons, issues, requirements) may take several options per facet, or All."],
    ["Page", "A Hub page: a data object that presents knowledge and links to other data objects."],
    ["Facet / option", "A facet is a controlled classification dimension, such as System or Design Type. An option is one controlled value of a facet. Options never overlap and together cover every case."],
    ["Facet level", "The position of a facet in the hierarchy of facets. Product Scope is facet level 0; System and Design Type are facet level 1. Lifecycle Stage, Source and Discipline are cross-cutting."],
    ["Build level", "The position of an item in the product-build hierarchy of a Product Scope. Aircraft scope: Build Level 0 Full Aircraft; 1 Major Unit or Final Assembly; then Assembly, Sub-assembly, Part. Build levels are not facet levels."],
    ["Tier", "A level within one facet that has two tiers: System Group is the upper tier and System the lower tier of the System facet."],
    ["Link type", "The controlled type of a link between data objects (for example satisfied by, verified by, supports, interface). It sets the direction and depth of change flags."],
    ["Home System", "The one System a Part Instance is part of (a bracket is Secondary Structure)."],
    ["Supports link", "A typed link from an item to a System it carries or serves, shown separately from its home System. A change flags the supported System, but no further."],
    ["Derived tag", "A tag calculated from other tags, never stored as a fact: an assembly's Systems come from its parts, and System Group comes from System."],
    ["Authority register", "A Production Hub's record of the current master of each data type and the date it moved to the Hub."],
]
FRAMEWORK_SECTIONS = [
    {"heading": "Framework data",
     "body": "Framework data is the same for every project and never contains project data:\n"
             "- Controlled facets and their options (Lifecycle Stage, Product Scope, Major Unit, System, Design Type, Source, Discipline), the glossary and the link-type table.\n"
             "- Page templates, permanent page IDs and typed link definitions.\n"
             "- Generic, unchanging descriptions and guidance written so that they hold for any project.\n"
             "- Generic lessons learned and the Skills and Traits linked registers.\n"
             "This Framework Hub may be hosted openly because it holds framework data only (proposed security rule)."},
    {"heading": "Production data",
     "body": "Production data belongs to one project and lives only in that project's Production Hub, on internal, access-controlled infrastructure:\n"
             "- Points of contact, project statistics and live views of the product models.\n"
             "- Links to part models, calculation documents, test and verification records.\n"
             "- Configuration and effectivity records: version or issue, baseline, and applicability by build standard, serial number or configuration.\n"
             "- Project lessons learned and the project's tailoring of the framework."},
    {"heading": "How production data connects to framework pages",
     "body": "- A Production Hub is a versioned instance of the framework: it is created from a numbered framework version and records which version it uses.\n"
             "- Production records are tagged with the same controlled facets and reference framework page IDs (for example a pipe model tagged with System [[SYS-0007]] and Design Type [[DT-0009]]). The production Hub shows them alongside the framework page; the framework page itself never stores them.\n"
             "- Tailoring is recorded as project data that points at the framework page IDs it changes, so framework updates can be adopted in a controlled way without losing the tailoring. Conflicts go to a person to decide.\n"
             "- A superseded record or changed effectivity flags the directly linked pages for review."},
    {"heading": "Authority register: the Production Hub becomes master",
     "body": "- End goal: once a Production Hub is set up for a project, it is master of all of that project's data, including configuration and effectivity.\n"
             "- It integrates with CAD, PLM and analysis tools through an API. Once a data type has moved to the Hub, those tools sync to the Hub rather than holding a master.\n"
             "- An authority register records, for each data type, its current master (for example PLM or released documents) and the date it moved to the Hub.\n"
             "- Data types move one at a time, once their records are verified. Until then the Hub links to the current master, recording each record's identifier and version.\n"
             "- Released documents stay master until they are converted to verified records, which then become master with the document kept as their origin."},
    {"heading": "AI and people",
     "body": "- AI identifies candidate links between data and pages, typed by what they connect (Requirement, Product, Verification and so on), so updates can flow through the whole product rapidly. Each link type sets the direction of change flags; by default a change flags directly linked objects only and the reviewer decides whether to pass it on.\n"
             "- AI-proposed links and records stay unverified until a person confirms them.\n"
             "- People keep meaningful work by design, not only verification: models are parametric so that people can modify them directly.\n"
             "- The Ask the Hub assistant answers only from controlled Hub sources, cites them, and respects access control."},
]


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
        "The agreed two-tier System facet (2 Oct 2026) and the System rule resolve these overlaps (one function per System; each Part Instance has exactly one home System). "
        "Looms moved to Design Type and bought-in electrical equipment to Source; Mission Systems became a System Group; Structure split into Primary and Secondary; "
        "Armaments merged into Stores Integration; Thermal Management and Fire Protection separated. See the tracker-to-facet mapping issue below.")
    add("Ground Support Equipment and Flight Test Instrumentation were listed as Aircraft Systems",
        "The tracker listed 'Ground Support Equipment' and 'Flight Test Instrumentation' as Aircraft Systems, mixing product scope with aircraft function.",
        ["KN-0021", "KN-0019", "PS-0002", "SYS-0025"], "Curated", "Resolved",
        "Ground Support Equipment is now Product Scope 'Ground Equipment'. Flight Test Instrumentation is installed on the aircraft, so it is its own System "
        "(SYS-0025, new group Test & Instrumentation). One shared System list is used for all Product Scopes, and each System records the scopes it applies to.")
    add("Tracker mapping questions answered (Ground Support Equipment, Flight Test Instrumentation, Power Generation & Distribution)",
        "Earlier mapping notes asked how Systems apply to ground equipment, whether on-aircraft test installations need a System, and whether 'Power Generation & Distribution' covered non-electrical power.",
        ["KN-0021", "KN-0019", "KN-0028", "SYS-0025", "SYS-0008"], "Curated", "Resolved",
        "One shared System list applies across Product Scopes, so ground equipment takes Systems like the aircraft; Flight Test Instrumentation is its own System; the System is renamed "
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
        "'Standard Parts & Supply Chain' (KN-0054) overlaps Source option 'Standard Part' (formerly Design Type DT-0012, retired 4 Oct 2026); 'Environmental Factors / Protection Treatments / ... Tank Sealing' (KN-0043) overlaps "
        "Finish Specification records (formerly Design Type DT-0011, retired); 'Materials Engineering' (KN-0049) and 'Manufacturing Methods' (KN-0048) overlap the material/process basis of Design Type.",
        ["KN-0050", "KN-0054", "SRC-0002", "KN-0043", "HUB-FINISH", "KN-0049", "KN-0048"], "Curated", "Open")
    unconf = [v["id"] for v in values if v["facet"] == "system" and not v.get("scopesConfirmed")]
    add("System applicability to Product Scopes is a first proposal (%d of %d Systems unconfirmed)" % (len(unconf), sum(1 for v in values if v["facet"] == "system")),
        "Each System records the Product Scopes it applies to (decision of 4 Oct 2026). Fuel (Aircraft, Ground Equipment, Facilities) and the Mission Systems (Aircraft only) were stated; "
        "the scopes shown for the other Systems are an initial proposal for confirmation. Systems for other scopes, such as Building Services, may be added later.",
        unconf, "Curated", "Open")
    return issues


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1])
