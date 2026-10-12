# Future Design Software: Requirements Prompt (Draft)

Status: working draft, version 24.6 (12 Oct 2026). Owner: Daniel Wagner. Scope: Future Design Software and its Engineering Hub. Pillars: 1) Fundamental use of data; 2) Iterative parametric design; 3) Design considerations.

All requirements in this version are settled; no requirements remain marked as proposals. The judgement calls of Data Schema - Draft v2 (section 6.1 of that document) are accepted, and are carried into Data Schema - Draft v3. The placement of the former Thermal, Environmental Impact and Sustainability, and Vibration and Shock considerations is settled (4.2), and refined in this version (Thermal split, 4.2). Daniel's decisions on all 50 findings of Worked Example - FDPS End-to-End v1 are applied in this version, and the example has been re-run against them (Worked Example - FDPS End-to-End v2). Daniel's decisions on the eight remaining findings of that re-run (R-01 to R-08) are applied in this version, and the example has been re-run again (Worked Example - FDPS End-to-End v3). Daniel's decisions on the six remaining findings of that re-run (R-09 to R-14) and on the Design Lead role were applied in v23, and the example has been re-run again (Worked Example - FDPS End-to-End v4). Daniel's decisions of 12 Oct 2026 on requirement documents (EDRs), document-level inheritance with line-item breaks, Lessons Learned tagging and the Engineering Hub page layout are applied in this version (EDR and TSM Inheritance change proposal, final). Annex B registers (Lifecycle Stage, Discipline, Verification method, Role, Dash number ranges) are framework registers and are not placeholders. Annex A lists remain Placeholder (generic, fictional) values but are the accepted starting values until replaced by the real lists of each project.

Revision history:

- v14 (5 Oct 2026): demo gap review.
- v15 (10 Oct 2026): data model fundamentals, three trees, configuration control, requirements and TSM inference, design reviews.
- v16 (10 Oct 2026): clean consolidation, renumbering, and proposed answers to all open questions.
- v17 (10 Oct 2026): Daniel's decisions applied.
- v18 (10 Oct 2026): all remaining proposals settled.
- v19 (10 Oct 2026): Data Schema v2 judgement calls accepted; Lifecycle Stage, Discipline and Verification method registers defined (2B.13 to 2B.15, Annex B); design review stages renamed A Initial System Design, B Preliminary, C Detail; design considerations (Pillar 3) driven by the Discipline register.
- v20 (10 Oct 2026): placement of former considerations settled (4.2): Thermal is a checklist item under Low Observability (moved from System Layout and Integration); Environmental Impact and Sustainability remains under Materials and Processes; Vibration and Shock remains under Structural Analysis (Stress). Remaining decision 4 removed as settled.
- v21 (11 Oct 2026): Daniel's decisions on the 50 findings of Worked Example v1 applied. Main changes: Requirements and TSMs flow down to FDPS level only, with Compliance Statements per FDPS per Requirement or TSM, carrying effectivity ranges (2.4, 6B); Requirements may be allocated to any System tree node (6B.2); TSMs link only to Design Types, with each Design Team listing its applicable Design Types (6B.5); interfaces defined on Sub-system pages and inherited by FDPSs, with interface agreement per interfacing System at reviews (6C.20 to 6C.23); Thermal split between Low Observability (heat signature) and System Layout and Integration (thermal environment), project non-applicability of a Discipline, and a new Fluid Systems Discipline, giving 26 Disciplines (2B.14, 4.2, Annex B.2); review templates limited to the checklist items listed on the Sub-team stage page, and No answers followed up (4.4, 4.5); Discipline agreement as Agree, Agree with conditions or Disagree, structured attendees, action closure acceptance, release gate over all A, B and C review actions enforced in PLM through the Hub, carry-forward of a C pass, and re-review stage and scope (6C); Role register (6C.14, Annex B.4); FDPS revision effectivity, frozen copies, baselines per FDPS revision, Retrofit and Concession records, and status for a selected effectivity (6A.10, 6A.11, 6A.15 to 6A.18); dash-number ranges, handedness, form-fit-function roll, shared stems, bought-in and catalogue numbering, and recorded number proposals (1.11, Annex B.5); fastener homing (1.6.6); highest Safety Classification of any use (1.10.2); Bench Build Stations (2C.12, Annex A.2); Issue impact options and Resolved by link (2E); Lesson origin and promotion (2G); editorial corrections.
- v22 (11 Oct 2026): Daniel's decisions on the remaining findings R-01 to R-08 of Worked Example v2 applied. Interfacing Systems: the interface of a structural Sub-system with every System does not cascade; an FDPS inherits interfacing Systems only from the Systems of its own parts plus Structure, and every break is approved by the FDPS's Design Lead (6C.20, 6C.21, 6C.14, R-01). TSMs: tagged with any of Design Type, Discipline and System, reaching an FDPS if any tag matches; TSMs are broad documents, and conformance is claimed only to the applicable statements; new Design Type Standard Part; Design Teams also list their applicable Disciplines (6B.5, 6B.7, 6B.11, 6C.13, Annex A.4, A.5, R-02; supersedes the v21 rule that TSMs link only to Design Types). Retrofit and as-embodied or as-manufactured configuration removed from current scope and moved to the new section 7 Future Development, with scan comparison of manufactured parts and assembled aircraft; Concessions remain (6A.16, 6A.17, 5.17, 7, R-03). Build Stations: only the item directly below the FDPS links to an aircraft Build Station; Part Instances within an Assembly link to a Bench Build Station, and the Assembly Instance links to the aircraft Build Station (1.4.1, 1.6.1, 2C.5, 2C.12, 2D.3, 2F.12, 6A.7, R-04). Substantial change wording confirmed: adversely affects compliance, or degrades form, fit, function or an interface (6C.17, R-05). Fasteners: Secures link to the part held, which sets the home Sub-system; no Supports link for structure-to-structure fasteners (1.6.6, 2I.2, R-06). Bought-in project control number Project + BI + sequence, stored with the supplier part number (1.11.11, Annex A.8, B.5, R-07). Parts and assemblies take the stem codes of their FDPS; their own home System is held only in the facet link (1.11.4, R-08).
- v23 (11 Oct 2026): Daniel's decisions on the remaining findings R-09 to R-14 of Worked Example v3 applied. Sub-structures: the Sub-systems of the structural Systems are Sub-structures; each Sub-structure page lists its interfacing Systems, which flow down to every Sub-structure FDPS with a Part Instance homed in it, with over-inclusion accepted; non-structural FDPSs inherit from their non-structural Sub-system pages and Supports links as before; no list may be 'interfaces with all', and interfaces are not derived from physical links (glossary, 2B.11, 6C.20, 6C.21, Annex A.3, R-09, R-10). Lead Sub-system: every FDPS records one lead Sub-system or Sub-structure (1.7.7). Design Team pages list applicable Disciplines alongside Design Types, and FDPSs owned by the team match TSMs tagged with any of them (6B.5, confirmed, R-11). Secures links may target a Part Instance in another FDPS and then count as an FDPS interface between the two FDPSs; the Fastener item property marks Parts that require a Secures link (1.6.6, 2I.2, 4.6, 6C.24, R-12). Concessions are part of the manufacturing standard, not the design standard: Concession records removed from the current scope and moved to section 7 with Retrofit and as-manufactured configuration; a Non-compliant Compliance Statement is linked to its Issue and blocks release of any FDPS revision for the effectivities concerned (glossary, 0.5, 2F.12, 6A.17, 6C.11, 7.4, Annex B.4, R-13). TSM conformance statements may be claimed for the FDPS as a whole; listing Parts is optional (6B.11, R-14). The FDPS Design Lead role is removed: breaks of inherited interfaces are approved by a Design Lead of the FDPS's lead Sub-system, or for a Sub-structure FDPS of its lead Sub-structure (6C.14, 6C.21, Annex B.4).
- v24.6 (12 Oct 2026): Daniel accepted the Annex B.6 access-role permission bundles as proposed; B.6 marked confirmed.
- v24.5 (12 Oct 2026): Daniel confirmed the Users points: access and approval roles stay separate, an approval role needs a matching access role and Admin may hold either (5A.6); Technical Authority for Design, Design Approver and Discipline Lead are approval roles held on top of the Engineer access role (5A.6); effectivity restriction covers seeing and editing, and data with no effectivity stays open (5A.4); the framework administrator flag is kept alongside per-project Admins (5A.8). Annex B.6 permission bundles remain proposed, pending Daniel's review.
- v24.4 (12 Oct 2026): Users, access roles and permissions (Daniel, 12 Oct 2026): new section 5A. Every person is a User; named access roles Admin, Design Lead, Design Authority, Engineer and Viewer bundle permissions (Annex B.6) and are assigned per project through Project Assignments; Users see all effectivities of their project unless an Admin restricts them; Admins may add one-off permission overrides; one accountable Owner plus optional Contributors on every work item; admin page with user list and edit panel; placeholder user pages. Access roles are kept separate from the authority roles of the Role register (5A.6).
- v24.3 (12 Oct 2026): Engineering Hub page layout (Daniel, approved with mockup v8): five page groups with their colours, contents and mobile order (5.24): Requirement left, Verification right (with Reviews), Product (FDPS list only on Sub-system pages, no Part Instances), Considerations (Interfacing Systems, Disciplines and Stakeholders), Working Data at the bottom (Issues and Lessons Learned separate); no dedicated Links area, links built into the data and the tree for navigation; structure and parent, Design Lead and Design Sub-team in the summary, and the summary tiles (5.23); FDPS pages follow the same groups, layout to be confirmed. Removes the earlier 'other' zone.
- v24.2 (12 Oct 2026): Link-maturity principle (6B.7A): high-level links flow down; defined links at the lowest level flow up and supersede them; flowed-down line items not reached by a defined link are Superseded (auto) once the level has defined links, with no manual break; TSM supersessions need a Design Authority bulk confirmation, EDR supersessions none; Kept, Broken and Superseded count as reviewed for the gates, and pending bulk confirmations block them (5.27, 6B.7A, 6C.11, 6C.13, 6C.15). Definitions and judgement calls P1 to P8 settled (accepted by Daniel).
- v24.1 (12 Oct 2026): Daniel's decisions R-15 and R-18, omitted from v24, added. R-15: the lead Sub-system is set by the owning Design Sub-team and approved by a Design Lead of that Sub-system; a later change is a Change Record of type Lead Sub-system change that re-runs interface inheritance and flags existing breaks for re-confirmation (1.7.7A). R-18: a cross-FDPS Secures link raises a flag to the other FDPS's owner, decided Accept or Query; a Query stays open, is shown on both FDPS pages and does not block the link (6C.24A).
- v24 (12 Oct 2026): EDRs and line-item inheritance. Requirements are line items grouped into Requirement Documents of kind EDR (Engineering Design Requirements); each line item is Part of exactly one EDR, keeps its own level, and an EDR may mix levels and cover several Systems (6B.1A). EDRs carry a document-level, many-to-many Sub-system tag; an FDPS inherits every EDR tagged to any Sub-system in which one of its Part Instances is homed, with all its line items, and the existing allocation of a line item to System tree nodes is kept as an optional narrowing (6B.2). TSMs gain a route Sub-system > Design Type > TSM alongside the existing Part Design Type match, with the Discipline and System tags kept unchanged; TSMs carry no Sub-system tag; each Sub-system page lists its Design Types (6B.5). Every inherited line item (EDR requirement or TSM statement) applies by default and is Kept or Broken as the design matures; breaks carry a reason and are approved by the Design Lead of the FDPS's lead Sub-system for EDR line items and by a Design Authority for TSM statements; a non-applicable TSM statement now needs a recorded break (6B.7, 6B.11, 6C.13). Compliance is claimed only on Kept line items. No unreviewed line items is a Stage C entry criterion and a release-gate condition (6C.11, 6C.15). A new EDR issue re-flags only changed line items, so line-item revisions are tracked (6B.10). Lessons Learned are tagged against every applicable facet, including Design Type and optionally Sub-system, and are matched by tag (2G.3, 2G.6). Engineering Hub page layout: level-appropriate display (documents above FDPS level, line items at FDPS level), EDR and TSM pages, a Sub-system page layout with filter and tree rail, model preview beside the summary, summary tiles, collapsed categories in data-type zones, a fixed AI bar, working filters, company colours with a theme setting, and the Sub-system owner shown as its Design Lead (5.21 to 5.30).

## 0. Purpose and Guiding Principles

0.1 Purpose. Build a design software whose foundation is rigorous, standardised data management, so that it can handle very large volumes of engineering data while remaining robust and efficient.

0.2 Problem addressed. Engineering work is slowed by data recorded in formats that must be manually read and re-entered before use (for example, specifications held in PDF documents), by a lack of standardisation and inconsistent categorisation across data sources, and by problems being escalated to the wrong level of attention. The software shall eliminate these.

0.3 Guiding principles:

- Structured, never transcribed. All data shall be held as structured, machine-readable records, never as free-form documents that must be re-read by a person to be used.
- Record once, reuse everywhere. Each piece of data shall be entered once, stored in a single authoritative location, and referenced by link wherever it is needed, rather than copied.
- Standardised by default. All data shall conform to defined standard schemas, so it can be combined, queried and scaled consistently.
- Categorised without ambiguity. Every facet shall have options that are exhaustive and mutually exclusive.
- Organised by facets. All data shall be classified by controlled facets. Every hierarchy (the Manufacturing, Design and System trees, the requirement breakdown and every navigation tree) is a view generated from facets and links, so the scope of any change or problem is always visible.
- Fundamentals first. Robustness, traceability and efficiency take priority over feature breadth.
- Humans in the loop by design. AI may in future be able to do most, if not all, of the work currently done by engineers. The software shall nevertheless deliberately keep meaningful work, decisions and purpose with people. Human involvement is retained by design, not only to verify AI output.
- Built for AI and human input. Data, tools and the Engineering Hub shall be optimised equally for input and use by AI and by people.

0.4 Glossary. These terms shall be used with these meanings throughout:

- Data object: anything stored in the software with a unique, permanent identifier (2A.4). Every item, record and page is a data object.
- Data type: the kind of data object, defining its schema (2A.1), for example Requirement, Part Definition, Part Instance, FDPS, Verification, Issue, Lesson Learned, Finish Specification, Hub page.
- Item: a physical product item, meaning a Part Instance or an Assembly Instance (1.8). Each Part Instance owns exactly one Build Station link and one Sub-system link; the item directly below the FDPS links to an aircraft Build Station, and a Part Instance within an Assembly Instance links to a Bench Build Station (1.6).
- Product data: Part Definitions, Assembly Definitions and items together.
- Record: a data object that is not an item, for example a Requirement, Verification, Issue, Lesson Learned or Finish Specification. Knowledge records (pages, lessons, issues and requirements) may take several options per facet (2F.3). A production record is a record holding project production data (6.3).
- Page: a Hub page (section 5), a data object that presents knowledge and links to other data objects.
- Facet, Category, Level, Register, Type, Link, Mapping level, Hub level and Product level: as defined in 1.1. Option: a Category of a Facet.
- Facet level: the position of a Facet in a tree (1.1 Level). Product Scope is facet level 0. Major Unit and System are alternative splits at facet level 1 (1.3).
- Tier: a level within one facet that has two tiers, for example System Group (upper tier) and System (lower tier) of the System facet.
- Link type: the controlled type of a link between data objects, which sets the direction and depth of change flags (2I.2).
- FDPS: a released installation design package of Part Instances, owned by one Design Sub-team (1.7).
- Assembly: a set of parts assembled off-aircraft before installation (1.8). An Assembly Definition defines an assembly once; an Assembly Instance is a single occurrence of it on the product, in the same way as a Part Definition and a Part Instance.
- Revision: a controlled change state of a Part Definition, Assembly Definition or FDPS (6A.6).
- Issue (of a document): a controlled change state of a document (6A.6). Not to be confused with the Issue data type (2E).
- Effectivity: the range of product effectivity numbers for which a link, Part Instance, FDPS revision, Compliance Statement or Verification applies (6A).
- Baseline: a frozen, read-only record of the configuration of one FDPS revision, taken at each FDPS release and at each review snapshot (6A.10).
- TSM: Technical Standards Manual, a requirement data type holding governing design standards (6B.4). A TSM is a broad document holding many statements (6B.11).
- EDR: Engineering Design Requirements, a Requirement Document grouping requirement line items. An EDR is tagged at document level to one or more Sub-systems; every FDPS with a Part Instance homed in one of those Sub-systems inherits all its line items by default (6B.1A, 6B.2).
- Line item: one Requirement within an EDR, or one statement (clause) within a TSM (6B.1A, 6B.11).
- Break (line item): a recorded and approved decision that an inherited line item does not apply to an FDPS (6B.7).
- Superseded (auto) (line item): an inherited line item not reached by any defined link once its document has defined links in the FDPS; set automatically, with no manual break (6B.7A).
- Defined link: a link made at the lowest level, to a Part Instance or Assembly Instance, that supersedes flowed-down links (6B.7A, P1).
- Kept (line item): an inherited line item reviewed for an FDPS and confirmed as applying; compliance is claimed only on Kept line items (6B.7, 6B.8).
- Structural System: a System of the Airframe System Group (Primary Structure; Secondary Structure; Skins, Doors & Panels; Windscreen & Canopy). Structure means the structural Systems.
- Sub-structure: a Sub-system of a structural System (2B.11). Sub-structures are the sections into which Structure is split; each Sub-structure page lists its interfacing Systems (6C.20). Sub-system, used alone, includes Sub-structures unless the text says non-structural.
- Lead Sub-system: the one Sub-system or Sub-structure recorded on an FDPS that sets which Design Lead approves breaks of its inherited interfaces (1.7.7). A Sub-structure FDPS is an FDPS whose lead Sub-system is a Sub-structure; any other FDPS is a non-structural FDPS.
- FDPS interface: an interface between two FDPSs, created by a Secures link from a fastener in one FDPS to a Part Instance in the other (1.6.6, 6C.24).
- Compliance Statement: the record of one FDPS's compliance position against one Requirement or TSM over one effectivity range (6B.8).
- Interfacing System: a System with which an FDPS interfaces, inherited from the interface lists of the Sub-system and Sub-structure pages that apply to it and from the Supports links of its items (6C.20, 6C.21).
- Non-compliance: a Compliance Statement with position Non-compliant (6A.17). Concession records, Retrofit records and as-embodied or as-manufactured configuration belong to the manufacturing standard and are not in the current scope (section 7).
- Role register: the record of which person holds which role, with what delegated authority, for which area (6C.14).

0.5 Decisions reserved for people. The following decisions shall be made by people and shall never be made autonomously by AI: approval of AI-proposed records, tags, links and model changes; release of Parts, Assemblies and FDPSs; design review Pass or Fail; approval of non-applicability of inherited Requirements and TSMs; approval of breaks of inherited interfaces; approval of a project's non-applicability of a Discipline; acceptance of Action closure evidence; Design Authority assessment of substantial change; acceptance of Requirements and Requirement changes; assignment of Safety Classification; resolution of Issues above escalation level 2; adoption of a new framework version; and moving a data type to the Hub. AI may prepare, propose and check in each case.

## 1. Data Model Fundamentals

This section sets the fundamental rules of the data model. All later sections shall be read consistently with it, and where they conflict, this section prevails.

### 1.1 Definitions

The following terms shall have these meanings throughout:

- Level: one position in a tree, counted from the top node (Full Aircraft). Each level holds nodes of one kind only (for example every node at a given level of the System tree is a System).
- Category: one node at a level, into which data is classified. For example, Fuel is a Category at the System level. The Categories at a level are the options of that level's Facet.
- Register: a controlled list held in the software. There are two kinds, and they shall be kept distinct:
    - Record register: a list of data records, each with its own permanent identifier and attributes (for example the register of Part Instances or of Requirements).
    - Value register: a list of the permitted values of a field or Facet (for example the Categories of the System Facet, or the permitted values of Design Type). A value register defines what may be entered and holds no project data.
- Type: the kind of a data object, which sets its schema (for example Part, Part Instance, FDPS or Requirement). Type is distinct from the Design Type attribute (1.10).
- Link: a typed, directed relationship between two data objects, with a defined cardinality (one-to-one, many-to-one or many-to-many). Links are drawn from the controlled link types (2I.2).
- Facet: a classification dimension whose permitted values (Categories) are held in a value register. Each Facet sits at one level of one tree, or is cross-cutting (applying at every level, for example Lifecycle Stage).
- Mapping level: the level at which a Part Instance is linked to a tree (Build Station in the Manufacturing tree, Sub-system in the System tree, and FDPS in the Design tree). The Categories at all higher levels are inferred from that link and are not stored again.
- Hub level: a tree level that exists as Hub pages. Hub levels form the control framework and carry guidance, ownership, metadata and live model previews (5.16).
- Product level: a tree level that exists as product data records (for example Part and Part Instance). Product levels are not Hub pages.

### 1.2 Categorisation rule

1.2.1 The Categories at every level shall be exhaustive: together they shall cover everything that can be classified at that level.

1.2.2 Each Part Instance shall be homed in exactly one Category at the mapping level of each tree.

1.2.3 Catch-all Categories are legitimate where they are defined precisely. Final Assembly, for example, holds items that are not built into any other Major Unit.

### 1.3 Alternative splits

1.3.1 Facets at the same level below a common parent are alternative splits of the same data, not nested levels. For example, Major Unit and System are both split directly below Full Aircraft. A view shall use one split at a time, and the user shall be able to switch between them.

### 1.4 The three trees

1.4.1 The software shall provide three trees, each with Hub levels and Product levels:

| Tree | Hub levels (pages) | Product levels (data) |
| --- | --- | --- |
| Manufacturing | Full Aircraft > Major Unit > Build Station | Full Aircraft > Major Unit > Build Station > Part Instance or Assembly Instance; the Part Instances of an Assembly Instance sit under a Bench Build Station (2C.12) |
| Design | Full Aircraft > Design Team > Design Sub-team > FDPS | Full Aircraft > FDPS > Assembly Instance (optional) > Part Instance |
| System | Full Aircraft > System Group > System > Sub-system | Full Aircraft > System Group > System > Sub-system > Part Instance |

1.4.2 Design Team is a level of the Design tree. Design Type is a Part attribute, not a tree level (1.10).

1.4.3 Each tree is a view generated from links (2F.4). No tree is a fixed storage structure.

1.4.4 Parts in the Design tree. A Part (Part Definition) shall be reached in the Design tree only through its Part Instances. It is not a level of the Design tree and needs no single parent, because one Part may be used in many FDPSs (1.9.1). Within the view of one FDPS, Part Instances may be grouped by Part Definition for display.

### 1.5 Hub as control framework

1.5.1 The Hub shall be a control framework and metadata source. It shall hold pages for Hub levels only and shall not create a page for each data item. In particular, there shall be no pages for individual Part Instances.

1.5.2 Data items shall be reached through registers, searches and the live model previews of Hub pages (5.16).

### 1.6 Minimal-link inference

1.6.1 Each Part Instance shall own exactly two tree links, and both shall be many-to-one:

- one link to a Build Station, from which its Major Unit is inferred; and
- one link to a Sub-system, from which its System and System Group are inferred.

Only the item directly below the FDPS (a Part Instance that is not within an Assembly Instance, or an Assembly Instance) shall link to an aircraft Build Station. A Part Instance within an Assembly Instance shall link to the Bench Build Station (2C.12) of the Major Unit of that Assembly Instance. Each Assembly Instance shall own exactly one Build Station link, to the aircraft Build Station at which it is installed, which gives its Major Unit. An aircraft Build Station is any Build Station other than a Bench Build Station.

1.6.2 Only many-to-one links shall be permitted for these links. A Part Instance shall never link to more than one Build Station or more than one Sub-system, and an Assembly Instance shall never link to more than one Build Station.

1.6.3 Inferred Categories (Major Unit, System, System Group) shall not be stored on the Part Instance or Assembly Instance. They shall be calculated from the owned links and updated automatically when a link changes.

1.6.4 A Part Instance's Design tree position shall come from the population of FDPSs (1.7). It shall not be held as a separate owned link on the Part Instance.

1.6.5 Supports links to other Systems that a Part Instance carries or serves (2F.7) are typed links in addition to the owned Sub-system link and do not change the inferred System.

1.6.6 Fasteners. A fastener Part Instance (a Part Instance of a Part with the item property Fastener, 4.6) shall carry exactly one Secures link (2I.2) to the Part Instance it holds. The Secures link shall set the fastener's home Sub-system: the software shall set the fastener's Sub-system link to that of the held Part Instance and shall flag any difference. A fastener that secures a non-structural part shall also carry a Supports link to the System of the part to which it secures it. A fastener that joins structure to structure needs no Supports link. The held Part Instance may belong to the fastener's own FDPS or to another FDPS. A Secures link to a Part Instance in another FDPS is an FDPS interface between the two FDPSs (6C.24): it shall be shown on both FDPSs and flagged to both owning Design Sub-teams when it is created, changed or removed.

### 1.7 FDPS

1.7.1 An FDPS (a design package of Part Instances owned by a Design Sub-team) shall be independent of Major Unit and System.

1.7.2 The Part Instances in an FDPS may span several Major Units and several Systems.

1.7.3 The Systems of an FDPS shall be derived from its Part Instances, shall not be stored on the FDPS, and shall change automatically as the design matures and the population changes. The interfacing Systems of an FDPS shall be inherited as set out in 6C.20 to 6C.23.

1.7.4 Definition. An FDPS shall be a released installation design package: the Part Instances, their installation definition and the associated data that one Design Sub-team releases together under one FDPS number and revision.

1.7.5 Single membership. A Part Instance shall belong to exactly one FDPS. The software shall flag any Part Instance that belongs to no FDPS, and shall reject membership of a second FDPS.

1.7.6 Population control. Only the owning Design Sub-team shall add Part Instances to, or remove them from, its FDPS. Transfer of a Part Instance between FDPSs shall be a recorded change agreed by both owning Sub-teams. Each FDPS shall be owned by exactly one Design Sub-team, and a change of ownership shall be a recorded change approved by both Design Team leads.

1.7.7 Lead Sub-system. Each FDPS shall record exactly one lead Sub-system, which may be a Sub-structure, chosen when the FDPS is created and changed only by a recorded change. At least one Part Instance of the FDPS shall be homed in it once the FDPS is populated; the software shall flag an FDPS for which this is not so. The lead Sub-system sets which Design Lead approves breaks of the FDPS's inherited interfaces (6C.21) and whether the FDPS is a Sub-structure FDPS (6C.21). It does not change the Systems of the FDPS, which are still derived from its Part Instances (1.7.3), and it is not inferred from the FDPS number (1.11.1).

1.7.7A Setting and changing the lead Sub-system (R-15). The lead Sub-system shall be set by a person in the owning Design Sub-team and approved by a Design Lead whose area is that Sub-system (or Sub-structure); the FDPS shall record who set it and when, and who approved it and when. A change of lead Sub-system after creation shall be made only by a Change Record of change type Lead Sub-system change, approved in the same way by a Design Lead of the new lead Sub-system. The change shall re-run interface inheritance (6C.21) and flag every existing interface break and every EDR line-item break for re-confirmation, because the approving Design Lead has changed (6B.7, 6C.13).

### 1.8 Optional levels

1.8.1 The Assembly level shall be optional. An Assembly shall exist only where parts are assembled off-aircraft before installation (for example a bearing pressed into a bracket forms an assembly).

1.8.2 A Product level may be skipped wherever the tree allows it. A Part Instance may sit directly below an FDPS without an Assembly Instance.

1.8.3 Assembly Definitions and Assembly Instances. Assemblies shall mirror Part Definitions and Part Instances (1.9, 2D). An Assembly Definition shall define an assembly once, including its component Part Definitions and their quantities, and shall carry its own part number and revisions in the same way as a Part Definition (1.11, 6A.6). An Assembly Instance shall be a single occurrence of an Assembly Definition on the product. An Assembly Definition may have many Assembly Instances, which may be used in several FDPSs or several times within one FDPS. A set of parts shall form an Assembly only where it is built off-aircraft; parts that are first joined on the aircraft shall not form an Assembly.

1.8.4 Assemblies and FDPSs. Each Assembly Instance shall belong to exactly one FDPS, and all Part Instances of that Assembly Instance shall belong to the same FDPS. An Assembly Definition shall not be linked directly to an FDPS; it maps to FDPSs many-to-many through its Assembly Instances.

### 1.9 Parts and Part Instances

1.9.1 A Part (Part Definition) shall map many-to-many to FDPSs, Build Stations and Sub-systems through its Part Instances. For example, a common bracket or fastener may be used in many FDPSs.

1.9.2 The single-home rule (1.2.2, 1.6) applies to Part Instances and not to Parts.

### 1.10 Part attributes

1.10.1 Design Type (the kind of design work, for example a material or process kind) shall be an attribute of every Part, with its permitted values held in a value register. Catalogue items (Source Standard Part) shall take the Design Type Standard Part, so that they reach the TSMs tagged with it (6B.5).

1.10.2 Safety Classification shall be an attribute of a Part, with its permitted values held in a value register. A Part used in several places (for example a standard fastener) shall take the highest Safety Classification required by any of its uses. The software shall flag a Part whose classification is lower than that required by any use, for reassignment by a person (0.5).

1.10.3 Values. The permitted values of Design Type and Safety Classification shall initially be those in Annex A.5 and A.6.

### 1.11 Part numbering

1.11.1 A part number shall be an identifier only. Facet links held as data shall be the master. The software shall never infer a Facet or Category from a part number.

1.11.2 Meaningful part numbers may be retained because they support preliminary design, before links are fully populated. Illustrative example (generic): D2822001-801, read as Project D, System 28 (Fuel, as held in the System code register, 2A.9), Sub-system 2, Major Unit 2, sequence 001, with dash number 801 (an FDPS, 1.11.7).

1.11.3 Meaningful stems suit FDPSs and the parts and assemblies designed for them. Common parts designed by the project (for example common brackets) shall use the lighter convention of 1.11.5.

1.11.4 Stems. FDPS numbers, and the numbers of parts and assemblies designed by the project other than common parts, shall use the meaningful stem of 1.11.2: Project letter, two-digit System code, one-digit Sub-system code, one-digit Major Unit code and three-digit sequence, followed by a three-digit dash number (1.11.7). A part or assembly designed for an FDPS shall take the stem codes of that FDPS (its Project letter, System code, Sub-system code and Major Unit code), with its own sequence number; its own home System, Sub-system and Major Unit are held only in its facet links (1.6), even where they differ from those of the FDPS. A part later used in other FDPSs keeps the stem allocated for the FDPS it was first designed for. The stem shall be fixed when the number is allocated and shall not change if the owned links later change.

1.11.5 Common parts and catalogue items. Only common parts designed by the project shall be numbered Project letter, two-letter Type code and a sequential number (generic example: D-BR-00045, a common bracket). Type codes shall be held in a value register (Annex A.8). Catalogue items (for example fasteners, seals and clamps procured to a standard or from a supplier catalogue) are Standard Parts and shall keep the catalogue number or designation of the standard they are procured to. A change of issue of the standard or catalogue shall be recorded as a revision of the catalogue Part, with an interchangeability assessment (6A.9).

1.11.6 Allocation and uniqueness. The software shall propose a number for each new Part, Assembly and FDPS. The user shall accept the proposed number or propose an alternative. The software shall check every proposed number, whether proposed by the software or by the user, for uniqueness within the project, and shall never allow a number to be reused. The software-proposed number shall be recorded alongside the accepted number, with who proposed and who accepted each, and with every rejected alternative and the reason for its rejection.

1.11.7 Dash numbers. The dash number shall identify the kind of object, from the ranges in Annex B.5: -001 to -399 made parts; -401 to -799 assemblies; -801 and above FDPSs.

1.11.8 Handedness. An odd dash number shall identify a left-hand or unhanded item. The next even dash number shall be reserved for the handed right-hand version of the same item (for example -001 and -002; -401 and -402; -801 and -802), and shall not be used for any other item.

1.11.9 Non-interchangeable change. A change that is not interchangeable in form, fit and function (6A.9) shall keep the stem and roll the dash number by 2 (for example -001 to -003 to -005; -002 to -004 to -006; -401 to -403; -801 to -803). An interchangeable change shall create a new revision and shall never change the dash number (6A.6).

1.11.10 Shared stems and uniqueness. The full number (stem and dash number) shall be unique across FDPSs, assemblies and parts within a project. A stem may be shared to show that items belong together, for example a frame (-001) and the assembly of that frame with a pressed bearing (-401). Distinct items that do not belong together shall take different stems, so that the dash numbers of each stem remain free for handed versions (1.11.8) and non-interchangeable changes (1.11.9).

1.11.11 Bought-in equipment. Bought-in Equipment shall keep the supplier part number, with the supplier's modification standard where one applies, and shall also carry a project control number allocated under 1.11.6. The project control number shall be the Project letter, the code BI and a four-digit sequence (generic example: D-BI-0001), and shall be stored together with the supplier part number. It has no dash number. A bought-in item modified in-house is a new made Part (2B.10) and is numbered under 1.11.4.

1.11.12 Assemblies. Assembly Definitions shall be numbered under the same rules as Parts, and each shall record its numbering scheme.

### 1.12 Live model preview

1.12.1 Every Hub tree page shall show a live model preview filtered by that page's framework node. For example, the Fuel System page shall show the Part Instances linked to the Sub-systems of Fuel, and a Build Station page shall show the Part Instances linked to that Build Station.

1.12.2 Model source. The preview shall use lightweight tessellated models (for example JT or glTF) generated from the PLM-managed CAD models, never the native CAD models themselves.

1.12.3 Performance. The preview shall stream geometry with level-of-detail control, and filtering by node and effectivity (5.17) shall be performed on the server. A node of up to 100,000 Part Instances shall show a first usable view within 5 seconds and remain interactive on a standard engineering workstation.

## 2. Data Model

2.1 The software shall organise all information into data objects of defined data types. The initial data types are Requirement, Product (Part Definitions and items) and Verification.

2.2 The set of data types shall be extensible, so new data types can be added later without restructuring existing data.

2.3 Requirement data shall be created first and forms the root of the data structure.

2.4 Every FDPS shall have at least one Requirement, inherited (6B.2) or directly linked. An FDPS with no Requirement shall be flagged as invalid. Parts, assemblies and items shall reach their Requirements through the FDPS that contains them (6B.1); an item needs no Requirement of its own, and an item that belongs to no FDPS is flagged under 1.7.5. An FDPS may have any number of Requirements.

2.5 Verification data shall hold the analysis that supports Product data. Every Verification record shall be linked both to the item(s) it supports and to the Requirement(s) it demonstrates are met, shall state its verification method from the Verification method register (2B.15), and shall carry the effectivity range over which it is valid evidence (6B.9).

2.6 When a Requirement changes, the software shall flag as needing review the Compliance Statements of every FDPS that inherits it or is directly linked to it (6B.10), and the Verification records that demonstrate it. Further propagation follows the link-type table (2I.2) and the reviewer's decision (2I.3).

2.7 When an item changes, the software shall flag the Verification records linked to it as needing review.

2.8 Requirement coverage. The software shall report requirement coverage, showing for each Requirement its directly linked and inheriting FDPSs (6B.2), their Compliance Statements by effectivity range, and its Verification records, and highlighting any Requirement with no FDPS or no Verification. The report shall be filterable by any facet and by effectivity.

## 2A. Data Format and Standardisation

2A.1 Every data type shall have a defined standard schema: its named fields, the data type and units of each field, and which fields are mandatory.

2A.2 Data that does not conform to its schema shall be rejected or flagged at the point of entry.

2A.3 Numerical values shall always be stored with explicit units, and the software shall handle unit conversion automatically.

2A.4 Every data object shall have a unique, permanent identifier so it can be referenced from anywhere without ambiguity.

2A.5 Any data object shall be retrievable automatically by other parts of the software, and by external tools through a documented interface, without manual re-entry.

2A.6 Data shall be exportable in open, structured formats (for example CSV, JSON or spreadsheet) and importable from them.

2A.7 Documents generated from the data (for example PDF reports) are outputs and shall never be the master of the data. An existing released document remains master of its content only until it is converted into verified structured records, which then become master with the document kept as their origin (2H.8, 2J).

2A.8 The software shall scale to very large numbers of data objects and links without loss of responsiveness.

2A.9 Industry standards. Schemas shall align with recognised industry standards where they exist, and shall otherwise be defined within the software and published in the Framework Hub. References include ATA iSpec 2200 and S1000D-style system numbering for System and Sub-system codes, ISO 10303 (STEP) for geometry exchange, and SI units. Any deviation from a referenced standard shall be recorded with its rationale.

## 2B. Categorisation Framework

2B.1 Every categorical field shall be a facet with a controlled, defined list of options. Free-text entry shall not be permitted for facets.

2B.2 Exhaustive. The options of every facet shall together cover every possible value within the Product Scopes the facet applies to, so that no data object is left without a valid option.

2B.3 Mutually exclusive. The options of every facet shall not overlap. How many options a data object may take is set by 2F.3.

2B.4 Range-based options shall use explicit, unambiguous boundaries with defined inclusive or exclusive limits, and shall have no gaps between them. The first and last ranges shall be open-ended where needed to cover all values.

- Poor practice (weight): 0.1 kg to 1 kg; 1 kg to 10 kg; 11 kg to 100 kg. This leaves values below 0.1 kg, between 10 kg and 11 kg, and above 100 kg uncovered, and places 1 kg in two options.
- Correct practice (weight): less than or equal to 1 kg; greater than 1 kg and less than or equal to 10 kg; greater than 10 kg.

2B.5 The software shall validate every facet definition against 2B.2 to 2B.4 when it is created or changed, and shall reject definitions that leave gaps or overlaps.

2B.6 Independent dimensions shall be recorded in separate facets. A single facet shall never mix two different classification dimensions.

2B.7 Product scope, location, function and source shall be separate dimensions, each recorded as its own facet. The kind of design work is recorded as the Design Type attribute of a Part (1.10), not as a facet.

- Product Scope (which product an item belongs to). Product Scope is facet level 0. Options, which are peers: Aircraft; Ground Equipment; Test Equipment; Facilities. Boundaries: Facilities are fixed infrastructure (for example buildings, fuel farms and fixed test rigs); Test Equipment is movable test kit; Ground Equipment is movable support kit that is not test kit. Full Aircraft is the top item of the Aircraft scope, and the top items of Ground Equipment, Test Equipment and Facilities sit at the same level as Full Aircraft. Connections between items in different Product Scopes are links (interfaces, 2F.10), not parent levels.
- Major Unit (location: which manufactured major unit the item is built into). Major Unit applies only to the Aircraft scope. Options: Front Fuselage, Centre Fuselage, Rear Fuselage, Wings, Fins, Final Assembly. Final Assembly holds the items that are not built into any Major Unit, because they are assembled with the Major Units to form the Full Aircraft (2C.4). Each Major Unit is divided into Build Stations, which form the mapping level of the Manufacturing tree (1.4, 1.6). Completeness rule: see 2C.11.
- System (function). Rule: a System is a set of items that work together to perform one function. The System facet has a third tier, Sub-system, which is the mapping level. Every Part Instance links to exactly one Sub-system, from which its System is inferred (1.6). One shared System list is used for all Product Scopes, and each System shall record the Product Scopes it applies to (2F.11). The facet has two tiers, System Group (upper tier) > System (lower tier):
    - Airframe: Primary Structure; Secondary Structure; Skins, Doors & Panels; Windscreen & Canopy.
    - Propulsion & Power: Propulsion; Intake & Ducts; Fuel; Electrical Power Generation & Distribution (electrical only); Hydraulics; Pneumatics. The electrical System covers electrical power only; hydraulic and pneumatic power belong to Hydraulics and Pneumatics.
    - Flight & Vehicle Management: Flight Control; Vehicle Management; Landing Gear; Navigation.
    - Environmental & Safety: Environmental Control; Thermal Management; Fire Protection; Crew Escape & Safety.
    - Crew Interface: Cockpit & Controls.
    - Mission Systems: Radar / Sensors; Electronic Warfare; Communications; Data Links; Stores Integration (incl. Armaments).
    - Test & Instrumentation: Flight Test Instrumentation (installed on the aircraft, so it is a System, not a Product Scope).
- Electrical installation is not a System. Looms are a Design Type, and each wire takes the System it serves as its home System. Skins, Doors & Panels is kept as one grouped System. Systems for other Product Scopes (for example Building Services or Ground Handling) may be added later.
- Source (how the item is obtained). Options: Make; Standard Part (catalogue items such as fasteners, seals, fittings and clamps, 1.11.5); Bought-in Equipment (pumps, LRUs, actuators). Bought-in items take Design Type Bought-in Equipment as well as Source Bought-in Equipment. Catalogue items take Design Type Standard Part as well as Source Standard Part (1.10.1).

2B.8 Design Teams and Design Sub-teams shall be Hub levels of the Design tree (1.4). They shall not be facet tags on Part Instances: a Part Instance reaches a Design Team only through the FDPS that contains it (1.6.4, 1.7).

2B.9 Every facet shall have a single authoritative definition in the software, with a precise description of each option, and all data shall reference that definition.

2B.10 Modified bought-in items. A bought-in item that is modified in-house shall be recorded as a new Part with Source Make, and shall carry a Derived from link (2I.2) to the bought-in source Part. A change to the source Part shall flag the modified Part for review. A modified bought-in Part shall keep the Design Type Bought-in Equipment, and with it the TSMs of that Design Type, and shall also record the Design Type of the modification (for example Metallic - Machined), whose TSMs it shall also bring to its FDPS (6B.5).

2B.11 Sub-systems. Every System shall be divided into Sub-systems, initially as listed in Annex A.3. Each System shall include a General Sub-system, defined as holding only items that serve the System as a whole and cannot be placed in a single other Sub-system of that System. The Sub-systems of the structural Systems are Sub-structures: Structure is split into Sub-structure sections, each with its own Hub page listing its interfacing Systems (6C.20). A project may split Structure more finely (for example by zone or frame bay) so that each Sub-structure lists fewer interfacing Systems.

2B.12 Design Teams. Design Teams and Design Sub-teams shall initially be as listed in Annex A.4. Each Design Sub-team shall own its FDPSs under the rules of 1.7.6.

2B.13 Lifecycle Stage. The Lifecycle Stage facet shall use the register in Annex B.1: 1 Opportunity; 2 Concept Development; 3 Architecture/Configuration Design; 4 Initial System Design; 5 Preliminary Design; 6 Detailed Design; 7 Manufacture & Assembly; 8 Qualification; 9 Production; 10 Support & Upgrades; 11 Disposal. The current scope of the software and the Engineering Hub is Lifecycle Stages 4 (Initial System Design) to 6 (Detailed Design). The scope shall be expanded to the other stages later; all eleven stages shall be held in the register now, so that the facet is exhaustive and the expansion needs no restructuring of existing data. Records in Lifecycle Stages outside the current scope (for example an Issue raised during stage 8 Qualification) may be stored and tagged now; no stage-specific rules shall be enforced for them until the scope is expanded.

2B.14 Discipline. The Discipline facet shall use the single Discipline register in Annex B.2. Each Discipline shall appear once only, with no duplicates, and each entry shall carry a Discipline type field with one of two values: Sign-off team or Consideration only.

- Every Discipline is also a design consideration that all designs shall address (4.2).
- A Sign-off team Discipline listed against a review stage (6C.6) shall give its agreement at that review (6C.19).
- A Consideration only Discipline shall be checked by the designer, through its checklist (4.5), and has no separate sign-off.
- A project may mark a Discipline not applicable to the project, through a Tailoring Record (6.4) with a reason, approved by the Technical Authority for Design. The checklist items of a Discipline marked not applicable shall not be shown in the project's review templates, and its agreement shall not be required at the project's reviews (6C.19). The Design Consideration record itself is kept unchanged in the Framework Hub.

2B.15 Verification method. The verification method of every Verification record (2.5) shall be one option of the Verification method register in Annex B.3: Analogy; Design Review; Calculation Analysis; Safety Assessment; Laboratory/Bench/Rig Tests; Product Ground Tests; Flight Tests; Design Inspection; Simulation; Equipment Qualification.

## 2C. Trees and Levels

2C.1 Within the Aircraft Product Scope, items shall be organised in the three trees of 1.4 (Manufacturing, Design and System), each with Hub levels and Product levels.

2C.2 Full Aircraft shall be the top node of every tree. Major Unit and System shall be alternative splits directly below Full Aircraft (1.3), not options within the same facet.

2C.3 The Manufacturing tree shall follow the manufacturing build: Full Aircraft > Major Unit > Build Station > Part Instance. Each Major Unit contains only items built within it before final assembly.

2C.4 Items that are not built into any Major Unit, for example pipes or looms installed at final assembly to connect Major Units, shall sit under Final Assembly, which is a Major Unit-level Category (catch-all, 1.2.3) with its own Build Stations.

2C.5 Assemblies shall exist only where parts are assembled off-aircraft first (1.8). The Part Instances of an Assembly Instance shall sit at a Bench Build Station, and the Assembly Instance at the aircraft Build Station where it is installed (1.6.1).

2C.6 In each tree, every Part Instance shall have exactly one parent at its mapping level (1.2.2, 1.6). Other views (see 2F) may show the same data object under several branches.

2C.7 Requirements shall follow their own functional breakdown within each Product Scope (for the Aircraft scope: Air System > System > Sub-system > Item). Each Requirement shall be linked by typed links (2I) to the System tree nodes it is allocated to and, through them, to the FDPSs that meet it (6B.2).

2C.8 The software shall show, for any data object, its position in each tree and everything above and below it, so the scope of a change can be seen immediately.

2C.9 Every tree, including the requirement breakdown, is a view generated from links, as set out in sections 1 and 2F. No tree is a fixed storage structure.

2C.10 The trees in 1.4 apply within the Aircraft Product Scope. The top nodes of the other Product Scopes correspond to Full Aircraft.

2C.11 Major Unit completeness. Any item not built into Front Fuselage, Centre Fuselage, Rear Fuselage, Wings or Fins (for example landing gear units, engines and separately supplied control surfaces) shall sit under a Final Assembly Build Station. A new Major Unit (for example Tailplane or Nacelles) shall be added only where a separately built structural unit is delivered to final assembly.

2C.12 Build Stations. Each Major Unit, including Final Assembly, shall be divided into Build Stations, initially as listed in Annex A.2. Each Major Unit shall also have one Bench Build Station for off-aircraft assembly (1.8.1): the Part Instances of an Assembly Instance shall be Located at the Bench of the Major Unit of that Assembly Instance, and the Assembly Instance shall be Located at the aircraft Build Station where it is installed, which gives its Major Unit (1.6.1).

2C.13 Other Product Scopes. Ground Equipment and Test Equipment shall use the Manufacturing tree Scope top node > End Item > Build Stage > Part Instance. Facilities shall use Scope top node > Site > Facility > Part Instance. All Product Scopes shall use the same Design and System trees, limited to the Systems that apply to them (2F.11).

## 2D. Part Definitions and Part Instances

2D.1 The software shall distinguish between a Part Definition (the standardised design of a part, defined once) and a Part Instance (a single occurrence of that part in a specific place on the product).

2D.2 A Part Definition shall not be linked directly to a Major Unit, Build Station, System, Sub-system or FDPS. It maps to these many-to-many through its Part Instances (1.9). Design Type and Safety Classification are attributes of the Part Definition (1.10).

2D.3 Each Part Instance shall reference exactly one Part Definition and shall own exactly one Build Station link and exactly one Sub-system link (1.6). The Build Station is an aircraft Build Station for a Part Instance directly below the FDPS, and a Bench Build Station for a Part Instance within an Assembly Instance (1.6.1). Its Major Unit, System and System Group are inferred, and its FDPS comes from FDPS population.

2D.4 A change to a Part Definition shall apply to, and flag for review, every Part Instance that references it, wherever it sits.

2D.5 The software shall report, for any Part Definition, every instance of it and where each instance sits.

2D.6 Finish specifications. Coatings, sealants and treatments (for example paint, primers, surface treatments, sealants and adhesives) shall be recorded as Finish Specification records and linked to the parts they are applied to. A part may have several Finish Specifications, and a change to a Finish Specification shall flag the linked parts for review.

2D.7 Finish Specification links. Finish Specifications shall be linked to Part Definitions. A Part Instance may carry an instance-level override (an added or replacing Finish Specification, with a reason), which takes precedence for that Part Instance only. A Finish Specification applied only through instance-level overrides is in use and valid (2F.12).

## 2E. Issues and Escalation

2E.1 The software shall include an Issue data type for recording problems, linked to the Requirements, items and Verification records it affects.

2E.2 Every Issue shall be assessed against a defined, standard set of impact criteria. Each criterion shall use exhaustive, mutually exclusive options as set out in 2B, worded so that they do not overlap. Where more than one option of a criterion fits an Issue, the highest shall apply.

2E.3 The software shall determine the escalation level of each Issue from its impact assessment using defined rules, not from the judgement or confidence of the person raising it. An Issue's escalation level shall be its highest score on any single impact criterion.

2E.4 Each escalation forum or owner shall cover a defined band of escalation levels. The bands shall not overlap and shall together cover every level.

2E.5 Every Issue shall appear on the agenda of exactly one forum, the one whose band contains its escalation level, whoever raised it. Issues shall be visible read-only to all other forums.

2E.6 The software shall rank Issues within each forum by impact, so that limited senior attention goes to the highest-impact topics first.

2E.7 Every Issue page shall show the Product Scopes of the items it links to (and any Product Scope tags on the Issue itself). There shall be no separate cross-scope badge.

2E.8 Impact criteria. Every Issue shall be scored 1 to 5 on each of the following five criteria: effort, cost, schedule, safety or certification, and scope. Lower limits are exclusive and upper limits inclusive. Threshold values for effort and cost shall be tailorable per Production Hub as project data (6.4); the criteria and scores shall be fixed in the framework.

| Criterion | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| Effort: effort to resolve (person-days) | up to 1 | over 1, up to 5 | over 5, up to 20 | over 20, up to 60 | over 60 |
| Cost: cost to resolve (GBP) | up to 5k | over 5k, up to 50k | over 50k, up to 250k | over 250k, up to 1M | over 1M |
| Schedule: delay to earliest affected programme milestone | none | over 0, up to 1 week | over 1, up to 4 weeks | over 4, up to 13 weeks | over 13 weeks |
| Safety or certification: effect on safety or certification | no effect | compliance evidence only, with no design change and no re-verification | requires re-verification, or a design change affecting only Parts classified D or E | affects a Part classified C, or puts compliance with a certification requirement at risk | affects a Part classified A or B, or could prevent certification or clearance |
| Scope: extent of the affected objects | one Part or Part Instance | more than one Part or Part Instance, within one FDPS or one Sub-system | several FDPSs within one Design Sub-team, or several Sub-systems within one System | several Design Sub-teams, Systems or Major Units | Full Aircraft, or more than one Product Scope |

Safety Classification codes are those of Annex A.6. Scope shall be judged by the objects the Issue affects, not by the extent of the FDPS that contains them.

2E.9 Escalation bands. The forums and their bands shall be:

| Escalation level | Forum or owner |
| --- | --- |
| 1 to 2 | Engineer (Issue owner) |
| 3 | Team Leader |
| 4 | Chief Engineer |
| 5 | Programme Board |

2E.10 Resolution link. An Issue shall be linked to each Change Record that resolves it, by a Resolved by link (2I.2).

## 2F. Metadata Tagging and Views

2F.1 All data shall be stored once, in a flat store, with each data object holding a unique, permanent identifier (2A.4). Data shall not be stored inside, or copied into, any fixed tree.

2F.2 Every data object shall be tagged with options drawn from controlled facets. The initial facets are Lifecycle Stage (2B.13), Product Scope, Major Unit (with Build Station), System (with Sub-system), Source and Discipline (2B.14) (see 2B.7). Design Type and Safety Classification are Part attributes, not facets (1.10). Skill and Trait are linked registers, not facets: pages and other knowledge records may link to Skills and Traits, but they are not used to classify items.

2F.3 One-option rule. The rules of 2B (2B.2 to 2B.5) apply to the options of every facet. Part Instances shall take their tree Categories only through the owned links of 1.6, and shall take exactly one option of each cross-cutting facet; derived tags (2F.7) shall be stored and shown separately from these. Knowledge records (pages, lessons, issues and requirements) may take several options per facet, or All, meaning every option of that facet. Each data type shall define its mandatory tags (2F.12).

2F.4 Every hierarchy or tree shall be a view generated from the tags, not a stored structure. Initial views: the Manufacturing, Design and System trees (1.4), Lifecycle (by Lifecycle Stage), Product Scope and Discipline. Design Type is available as a filter on Part attributes, not as a tree.

2F.5 The user shall be able to switch between views at any time.

2F.6 The same data object shall appear in every view in which it is tagged, without duplication. Any change to the object shall be visible in every view at once, because each view links to the single stored object.

2F.7 Home System and supports links. Each Part Instance shall have exactly one home System, inferred from its owned Sub-system link (1.6), and may have typed supports links to the other Systems it carries or serves. For example, a bracket carrying a fuel pipe and a hydraulic pipe has Secondary Structure as its home System and supports links to Fuel and Hydraulics; each wire's home System is the System it serves. An Assembly Instance shall take its System tags from its Part Instances' home Systems (derived tags), so a loom shows the Systems of its wires. Derived tags shall update automatically when parts change, and shall be shown distinctly from home Systems and supports links. In the Manufacturing tree view, a derived badge shall appear next to items whose System tags are derived, so they are not mistaken for dual-tagged items.

2F.8 Facet levels. Every facet shall be assigned to a defined facet level. Several independent facets may exist at the same facet level, for example Major Unit and System both sit directly below Full Aircraft as alternative splits (1.3), and a view may be restructured by any facet at that facet level. Facets at different facet levels shall not be mixed as alternatives in one view level.

2F.9 Assigned facet levels. Product Scope is facet level 0, the top. Major Unit and System are facet level 1, directly below Full Aircraft; Build Station and Sub-system (with System Group above System) are their mapping levels. Design Team (Design tree) is also at level 1. Lifecycle Stage, Discipline and Source are cross-cutting facets: they are not assigned to a facet level and apply at every level. Design Type is not a facet (1.10).

2F.10 Cross-scope interfaces. Interfaces between items in different Product Scopes within the same System (for example the aircraft fuel system and ground refuelling equipment, or the aircraft and a facility's fuel farm) shall be recorded as links and shall be traceable in both directions, so that a change on one side flags the linked items on the other side for review.

2F.11 System applicability. Each System shall record the Product Scopes it applies to (for example Fuel: Aircraft, Ground Equipment, Facilities; Mission Systems: Aircraft only). Items shall only be tagged with Systems that apply to their Product Scope, and views filtered by Product Scope shall show only the applicable Systems. The initial applicability shall be as in Annex A.7.

2F.12 Mandatory tags. Each data type shall have the mandatory tags and links below. A data object missing any of them shall be flagged as invalid. All may be used only where marked, and only where the content genuinely applies to every option; it shall never be used on items.

| Data type | Mandatory tags and links | All permitted for |
| --- | --- | --- |
| Requirement | Product Scope; Lifecycle Stage; Discipline; at least one System tree node (Sub-system, System or System Group, 6B.2) | Lifecycle Stage, Discipline |
| TSM | at least one tag of Design Type, Discipline or System (6B.5); at least one statement (6B.11) | None |
| Part Definition | Source; Design Type (Standard Part for catalogue items, 1.10.1); Safety Classification; Lifecycle Stage | None |
| Part Instance | one Part Definition; one Build Station (aircraft, or Bench within an Assembly Instance, 1.6.1); one Sub-system; one FDPS; effectivity (6A); for a fastener, one Secures link (1.6.6) | None |
| Assembly Definition | its component Part Definitions and quantities; Lifecycle Stage | None |
| Assembly Instance | one Assembly Definition; its Part Instances; one aircraft Build Station (1.6.1); one FDPS | None |
| FDPS | owning Design Sub-team; lead Sub-system (1.7.7); Lifecycle Stage; review stage status (6C); at least one Requirement (2.4) | None |
| Verification | at least one item; at least one Requirement; Verification method (2B.15); Discipline; Lifecycle Stage | None |
| Issue | at least one affected data object; full impact assessment (2E.8); Lifecycle Stage | Lifecycle Stage |
| Lesson Learned | at least one Lifecycle Stage; at least one System; Discipline | Lifecycle Stage, System, Discipline |
| Finish Specification | Discipline; at least one Part Definition or Part Instance override once in use (2D.7) | None |
| Review Action | one design review; at least one FDPS; owner; raised by; due date | None |
| Compliance Statement | one FDPS; one Requirement or TSM; effectivity range; position; at least one basis (6B.6, 6B.8); for Non-compliant, the Issue that records it (6A.17) | None |
| Hub page | page type; owner; framework node; Lifecycle Stage; Discipline | Lifecycle Stage, Discipline |

## 2G. Lessons Learned

2G.1 The software shall include a Lessons Learned data type, stored once with a unique, permanent identifier (2A.4).

2G.2 Every Lesson Learned shall use one standard template: title, summary, what happened, root cause, recommendation, applicability, origin (a source document with its issue or revision and a link, or a data object such as an Issue, by its permanent identifier) and verification status.

2G.3 Every Lesson Learned shall be tagged from the controlled facets of 2F. Its mandatory tags are at least one Lifecycle Stage, at least one System (or All), at least one Discipline (or All) and at least one Design Type (or All), per 2F.3 and 2F.12; it may also be tagged to one or more Sub-systems. A lesson shall be tagged against every applicable value of each facet, and a lesson without its mandatory tags shall be flagged as invalid.

2G.4 Users shall be able to filter Lessons Learned by any combination of facets, so that they see all applicable lessons and only applicable lessons.

2G.6 Matching by tag. A Lesson Learned shall be shown on a page or for an FDPS when its tags match that page's or FDPS's Lifecycle Stage, Discipline, Design Type, System or Sub-system (All matches every value). Lessons shall be matched by tag only, never by keyword.

2G.5 Promotion to the framework. A project lesson may be proposed for promotion to the framework. It shall first be rewritten in generic form with all project data removed, and shall pass the framework content review (6.10) before it is published as a framework lesson, which may then inform framework Design Considerations and TSMs. The project lesson shall record the framework lesson it was promoted to; the framework lesson shall not reference the project lesson.

## 2H. AI-Assisted Data Extraction

2H.1 The software shall use AI to extract information from existing unstructured sources (for example specifications, reports and notes).

2H.2 For each extraction, the software shall propose structured records that conform to the standard schema of the relevant data type (2A.1).

2H.3 The software shall propose tags for each proposed record, drawn only from the controlled facets (2B and 2F).

2H.4 The software shall record the source document as the origin of each record, with a link to it.

2H.5 The software shall assign a confidence level to each proposed record and to each proposed tag.

2H.6 A proposed record shall require human confirmation before it becomes verified. Unconfirmed records shall be clearly marked as unverified.

2H.7 Extraction shall be scalable to very large legacy data sets.

2H.8 Once a source document (for example a PDF) has been extracted and the structured records verified, the structured records shall become master in place of the document, as recorded in the authority register (2J), and shall reference the original document as their origin. The structured records shall retain the source's issue or revision and its references.

## 2I. Typed Links and AI-Identified Links

2I.1 Every link between data objects, including links to and from pages, shall be a typed link. The link type shall be defined by the data types it connects and shall be drawn from the controlled list of link types in 2I.2.

2I.2 Link types and change flags. The initial link types, and the direction in which a change raises review flags, are:

| Link type | Connects | Change flags |
| --- | --- | --- |
| Decomposes into | Requirement to lower-level Requirement | A changed Requirement flags its lower-level Requirements (down). |
| Satisfied by | Requirement to FDPS, or to an item for traceability (6B.2) | A changed Requirement flags the Compliance Statements of the FDPS concerned (down, 6B.10). |
| Allocated to | Requirement to System tree node (6B.2) | A changed Requirement flags the Compliance Statements of every inheriting FDPS (6B.10). |
| Governs | TSM to Design Type, Discipline or System (its tags, 6B.5) | A changed TSM flags the Compliance Statements of every inheriting FDPS (6B.10). |
| Interfaces with | Sub-system or Sub-structure page to System or Sub-system (6C.20) | A changed interface list flags the FDPSs that inherit it (6C.21). |
| Verified by | item to Verification | A changed item flags its Verification records (down). |
| Demonstrates | Verification to Requirement | A failed or changed Verification flags its item and its Requirement (up). |
| Instance of | Part Instance to Part Definition | A changed Part Definition flags every Part Instance of it (2D.4). |
| Supports | item to the Systems it carries or serves | A changed item flags the Systems it supports, and no further. |
| Secures | fastener Part Instance to the Part Instance it holds, in the same or another FDPS (1.6.6) | A re-homed or removed held Part Instance flags its fasteners, whose home Sub-system follows it. Across two FDPSs, a change to either Part Instance flags the other FDPS (FDPS interface, 6C.24). |
| Interface | item to item in another Product Scope | A change on either side flags the other side (both ways, 2F.10). |
| Finish applied | Finish Specification to Part Definition (or Part Instance override) | A changed Finish Specification flags the linked parts (2D.6, 2D.7). |
| Affects | Issue to Requirements, items and Verification records | A new or changed Issue flags the affected data objects (up). |
| Production link | item or page to production record | A superseded record or changed effectivity flags the linked data objects (6.8). |
| Describes | page to data object | A changed data object flags the pages that describe it. |
| Derived from | modified Part to bought-in source Part | A changed source Part flags the derived Part (2B.10). |
| Drives | parameter to dependent parameter or model | A changed parameter flags its dependants (3.8). |
| Resolved by | Issue to Change Record (2E.10) | A changed or rejected Change Record flags the Issue. |

Derived tags (2F.7) are recalculated automatically and do not raise review flags.

2I.3 Flag depth. By default a change shall flag only directly linked data objects. The reviewer of each flagged object decides whether the change needs to be passed on to the objects linked to it; the software shall make that one action. Rationale: complete, typed links allow an update to flow through the whole product rapidly while keeping people in control of how far it goes.

2I.4 The software shall use AI to identify candidate links between data objects, including pages, that have not yet been recorded.

2I.5 AI-proposed links shall follow the same rules as AI-extracted records (2H.5 and 2H.6): each shall carry a confidence level and shall require human confirmation before it is treated as verified. Unconfirmed links shall be clearly marked and shall not by themselves mark data as verified.

2I.6 Change flags raised through unconfirmed links shall be shown separately from flags raised through confirmed links, so that reviewers can see which impacts are certain and which are suggested.

2I.7 The software shall report data objects that are missing a mandatory link type (for example an item with no Requirement, see 2.4) and shall offer AI-proposed candidates for each gap.

## 2J. Authority Register and Integration

2J.1 End goal. Once a Production Hub is set up for a project, it shall become the master of all of that project's data, including configuration and effectivity.

2J.2 The software shall integrate with other tools (for example CAD, PLM and analysis tools) through a documented API (2A.5). Once a data type has moved to the Production Hub, those tools shall synchronise with the Hub rather than hold a master copy.

2J.3 Each Production Hub shall keep an authority register recording, for each data type, its current master (for example the PLM system, released documents or the Hub) and the date it moved to the Hub.

2J.4 Data types shall move to the Hub one at a time, and only once their records are verified. Until a data type has moved, its current master remains authoritative and the Hub shall hold a typed production link (2I.2) to each record, with its identifier and revision or issue.

2J.5 A released document shall remain master of its content until it has been converted into verified structured records; those records then become master, with the document kept as their origin (2A.7, 2H.8).

2J.6 Order of moves. Data types shall move to the Hub in this order: (1) Requirements, including TSMs; (2) Lessons Learned; (3) Issues; (4) Part data (Part Definitions, Part Instances, FDPS population and Verification records); (5) Configuration (effectivity and baselines).

2J.7 Verification before a move. Before a data type moves, the software shall produce a reconciliation report against the current master showing that every record is present, conforms to its schema and has its mandatory tags and links. The data type owner shall sign off the report, and the Hub and current master shall run in parallel for one release cycle with no unresolved discrepancies.

2J.8 Register history. The authority register shall keep an append-only history of each move, with its reconciliation report and sign-off as evidence.

## 3. Iterative Parametric Design

3.1 Product models shall be heavily parametric: their geometry and properties shall be driven by named, structured parameters held as data (2A), so that the model can be changed by changing its parameters.

3.2 Parameters shall be easy for a human user to understand and modify directly, without needing to rebuild the model. Rationale: supports the principle of keeping meaningful design work with people (0.3).

3.3 Parameters shall be equally readable and writable by AI through the documented interface (2A.5), so that AI and people can work on the same model.

3.4 Each parameter shall be linkable by typed links (2I) to the Requirements that drive it and the Verification records that depend on it, so that a parameter change flags the affected Verification records for review (2.7).

3.5 Changes made by AI to a model or its parameters shall be recorded with their origin and shall require human confirmation before being released, consistent with 2H.6 and 2I.5.

3.6 Parameter register. Each project shall hold a record register of parameters. Each parameter shall have a permanent identifier, name, description, value with units, permitted limits, owner, origin (human, AI or derived) and status (draft, confirmed or released).

3.7 Dependency graph. Relationships between parameters shall be held as expressions forming a dependency graph. The software shall reject circular dependencies and shall show, for any parameter, everything upstream and downstream of it.

3.8 Change flags. A changed parameter shall flag its dependent parameters, models and Verification records through the Drives link type (2I.2), following the flag depth rule of 2I.3.

3.9 Constraints. Parameters shall carry constraints (limits, ratios or relationships) traced to the Requirements or TSMs they come from. The software shall check constraints on every change and flag any breach, citing the governing Requirement or TSM.

3.10 Design tables and variants. A Part may hold design tables of named variants, each a set of parameter values. Each variant used on the product shall be a distinct revision or part number under the interchangeability rule (6A.9) and shall be linked by effectivity in the same way as any other revision (6A).

3.11 Regeneration and validation. After a parameter change, affected models shall regenerate automatically or on request. Regeneration failures shall be reported against the parameter that caused them, and validation checks (constraints, interference and mass properties) shall run with their results recorded as data.

3.12 Iteration history. Every set of parameter changes shall be recorded as an iteration with author, date and reason. Users shall be able to compare any two iterations and to explore what-if branches that cannot be released until merged and confirmed.

## 4. Design Considerations

4.1 Item properties. Mechanical, flexible, kinematic and similar aspects are design properties (considerations) that an item may have, not facet options. They shall not be used as facet options; they shall be recorded under Design Considerations as properties of an item, alongside the design considerations of 4.2 (for example Maintainability, Reliability and Ground Equipment, and Low Observability).

4.2 Considerations register. The design considerations (Pillar 3) shall be driven by the Discipline register (2B.14, Annex B.2), not held as a separate list. Every Discipline is a design consideration that all designs shall address, and the Framework Hub shall hold exactly one Design Consideration record for each Discipline. Each Design Consideration record shall hold the detailed guidance and checklists for its Discipline (4.3, 4.5). A new consideration shall be added by adding a Discipline to the register, with its Discipline type, which the register shall allow without restructuring existing data. The considerations listed in earlier versions are covered as follows: Maintainability and Reliability by Maintainability, Reliability and Ground Equipment; Manufacturability and Assembly by Manufacturing Engineering and by Assembly, Interfaces, Tolerances and Interchangeability; Weight by Weight; Safety by Safety; Electromagnetic Compatibility by Electro-Magnetic Compatibility; Low Observability by Low Observability; Environmental Conditions by Environmental Factors (climatic protection) and Structural Analysis (Stress) (vibration and shock); Human Factors by Human Factors; Cost by Affordability and Cost. Thermal, Environmental Impact and Sustainability, and Vibration and Shock have no Discipline of their own and shall be held as checklist items in the Design Consideration records of existing Disciplines, as follows. Thermal shall be split: heat signature items (for example infrared signature and hot surfaces seen externally) under Low Observability, and thermal environment items (for example fuel heat soak, fluid temperature limits and heat rejection) under System Layout and Integration; each keeps the topic label Thermal, so that all Thermal items can be filtered together. Environmental Impact and Sustainability shall be held under Materials and Processes, and Vibration and Shock under Structural Analysis (Stress). Fluid systems (fuel, hydraulics and pneumatics) are covered by the Fluid Systems Discipline. A project may mark a Discipline not applicable (2B.14).

4.3 Consideration content. Each consideration shall be a Hub page with a generic description and guidance, linked to its governing TSMs and relevant Lessons Learned.

4.4 Applicability. Every design consideration applies to all designs (4.2). Individual checklist items shall be linked to the Design Types and review stages (6C.1) to which they apply. The checklist items used for an FDPS at a review stage shall be those listed for that stage on its Design Sub-team stage page (6C.6), excluding the items of any Discipline that the project has marked not applicable (2B.14).

4.5 Checklists. Each consideration shall have a structured checklist per review stage. The applicable checklists shall feed the review template for an FDPS (6C.6). Responses shall be recorded as structured data against the FDPS, and any checklist item marked not applicable shall carry a reason. The designer shall complete every checklist item listed for the stage on the Design Sub-team stage page (4.4). Before the review can record a Pass, every No response shall either raise an Action or a Risk linked to the response, or carry a justification approved by the Discipline Lead (6C.14) of that Discipline. For Consideration only Disciplines the designer's check is the only check; for Sign-off team Disciplines the sign-off team's agreement is also required at each review stage against which it is listed (6C.19).

4.6 Property values. Item properties under 4.1 shall be recorded as structured attributes of the Part, drawn from a value register, and may be used to filter considerations and checklists. The item property Fastener shall mark the Parts whose Part Instances require a Secures link (1.6.6). The software shall flag any Part Instance of a Fastener Part that has no Secures link, and any Part Instance with a Secures link whose Part is not a Fastener Part.

## 5. Engineering Hub

5.1 The software shall include an Engineering Hub: an interactive, linked knowledge site that supports the education of engineers, the verification and validation of information, and navigation of the engineering knowledge base.

5.2 Every page shall be a data object stored once and tagged per 2F. Pages of the same page type (for example Lifecycle Stage, Major Unit, Build Station, Design Team, Design Sub-team, FDPS, System Group, System, Sub-system, Discipline (whose page is its Design Consideration record, 4.2), Skill, Trait, topic or lesson learned) shall use one consistent template. Pages exist for Hub levels only; there are no pages for individual Part Instances or other data items (1.5).

5.3 Pages shall cross-link to related pages in other facets, and every page shall show backlinks (the pages that link to it).

5.4 The Hub navigation shall use the switchable views of 2F, so the same page can be reached through any of the views in 2F.4.

5.5 Every page shall show its verification status, owner (a User, 5A.7) and contributors, and last reviewed date, to support verification and validation of its content.

5.6 The earlier Design Hub becomes one part (section or view) of the Engineering Hub.

5.7 The Engineering Hub shall exist as a standard Framework Hub and as Production Hubs, as defined in section 6. Requirements 5.1 to 5.6 apply to both.

5.8 Generic framework content. Framework Hub page descriptions shall be generic and project-independent, so that they remain valid unchanged for any project. Project-specific content shall be held only in Production Hubs (6.3).

5.9 Store or link to everything. Once a Production Hub is set up for a project, it shall store or link to all of the project's engineering information, including production data such as part models and calculation documents. It shall link to records whose master is still another system, and become their master as each data type moves to the Hub (2J).

5.10 Images and diagrams. Pages shall be able to include images and diagrams, including views of the product itself. Each image shall be a data object (2A.4) with a caption, alternative text for accessibility, an origin and, for product views, the configuration it shows (6.7).

5.11 Usability. The Hub shall be intuitive and aesthetically pleasing, using one consistent visual style and page templates (5.2). Text and interface colours shall meet recognised accessibility contrast standards (for example WCAG 2.1 AA).

5.12 AI assistant. The Hub shall include an AI search bar and assistant that connects through a documented API to an internal AI service. The interface shall be provisioned now; full function shall follow once the Hub holds the controlled data.

5.13 The AI assistant shall answer only from the controlled data sources within the Hub, shall cite the source pages or records (by permanent identifier) for every answer, and shall state when the controlled sources do not contain an answer.

5.14 The AI assistant shall respect the access controls of the Hub it serves: it shall never return, cite or use data that the asking user is not permitted to see, and an assistant in the Framework Hub shall have no access to production data (6.10). Until an AI service is connected, the search bar shall fall back to keyword search over pages.

5.15 Control framework. The Hub shall act as a control framework and metadata source (1.5). It shall not generate a page per data item; data items shall be shown in registers, search results and live model previews.

5.16 Live model preview. Every Hub tree page shall show a live model preview filtered by that page's framework node (1.12).

5.17 Effectivity selector. Hub model views and filtered pages shall have an effectivity selector (project and effectivity number). The model shall show each Part Instance at the revision valid for the selected effectivity (6A). Part Instances that do not exist at the selected effectivity (6A.8) shall not be shown in the model; in registers and lists they shall be shown as Not present, with a note of the effectivity ranges over which they exist (6A.18). The view shall also show the FDPS revision effective at the selected effectivity (6A.11). The view shows the as-designed configuration only; as-embodied configuration is not in the current scope (section 7).

5.18 AI access control. The AI assistant shall run every query with the permissions of the asking user, inherited from the Hub's access controls, including any data classification markings. Each Production Hub shall have its own isolated index and context; one AI service may serve several Hubs only if that isolation is enforced and tested so that no data crosses between projects.

5.19 AI logging. Every AI query and answer shall be logged with the user, time, Hub and cited sources. Logs shall be access-controlled and retained according to the project's records retention policy.

5.20 AI answers. AI answers shall not be stored as data objects unless a user explicitly saves one. A saved answer shall become an unverified record, subject to 2H.6, with its cited sources as its origin.

5.21 Level-appropriate display. The information shown on a page shall suit the level of the page. Above FDPS level (Sub-system, System, System Group and Design tree pages above the FDPS), requirement data shall be shown as documents (the applicable EDRs and TSMs, each linking to its own page) and verification data as summaries per document and per FDPS. Only FDPS pages shall list individual EDR line items and TSM statements, with their status (5.27).

5.22 EDR and TSM pages. Every EDR and every TSM shall have its own Hub page showing its code, title, issue, tags (Sub-system tags for an EDR; Design Type, Discipline and System tags for a TSM, and the Sub-systems it is reached from), its line items or statements, and the FDPSs inheriting it with a compliance summary.

5.23 Page layout. Hub tree pages shall use one layout: a left rail holding the page filters above the collapsible Hub tree, with the current page highlighted, the tree being for quick navigation; a content area that starts with the model preview window at the top left (1.12, 5.16), which can be expanded, beside a generic summary of the node; then all the data of the page in the five page groups of 5.24. The summary shall show what the node is, its status chips, and its structure and parent (parent System and System Group, each a link), its Design Lead as owner (5.30), its Design Sub-team and its permanent ID, each a link to its page or register entry; there shall be no separate Structure and parent category. Summary tiles shall show key counts, each linking to its category and updating with the filters; on a Sub-system page the tiles are FDPS, EDRs, TSMs, Non-compliant, Open Issues and Lessons, with no Part Instances tile.

5.24 Page groups and categories. Categories shall be grouped into five page groups, each with its own accessible colour family from the palette (5.28) and shown in a colour key: (a) Requirement (navy #00405E family), on the left: EDRs and TSMs, as documents above FDPS level; (b) Verification (teal #46C1BE family), on the right beside Requirement: Compliance, Verifications and Reviews; (c) Product (neutral grey family), full width below them: on a Sub-system page an FDPSs category only, listing the linked FDPSs, each a link to its FDPS page with a status chip and its Build Stations, and no Part Instances (5.21); (d) Considerations (violet family, light #5B3F8C on #F4F0FA, dark #C7B3EE on #1E1830): Interfacing Systems and Disciplines and Stakeholders; (e) Working Data (amber family, light #7A4E00 on #FBF5E9, dark #F0C674 on #2A2111), at the bottom of the page: Issues and Lessons Learned as separate categories. Every category shall be collapsed by default, with a header showing its name and a count or status chip, and shall expand on selection; an Expand all control shall open or close every category. Selecting or hovering a requirement document shall highlight its compliance and verification rows. There shall be no dedicated Links area: links shall be built into the data, so that every data item that has a page is a link in place (FDPS rows to FDPS pages, EDR and TSM names to their pages, Interfacing Systems to System pages, Issues and Lessons to their records, roles to the Role register, reviews to their Design Reviews, registers from the relevant category), and every page reachable from the former Links list shall stay reachable from the page data, the summary or the tree. On narrow screens the groups shall stack in the order Requirement, Verification, Product, Considerations, Working Data. FDPS pages shall use the same five groups at FDPS level (line items with their status in Requirement, Part Instances in Product); the detailed FDPS page layout is to be confirmed when the FDPS page is designed.

5.25 Filters. Page filters (Product Scope, Effectivity, Lifecycle Stage, Discipline, Design Type) shall filter the page: Effectivity shall change the FDPSs (and, on FDPS pages, the Part Instances), Compliance Statements, Verifications and Issues shown; Lifecycle Stage, Discipline and Design Type shall narrow the categories whose data carries those tags; counts and summary tiles shall update; the active filters shall be shown clearly, each removable, with a reset; and a category that a filter cannot narrow shall say so.

5.26 AI bar. The AI search bar (5.12) shall be fixed to the bottom of the screen without covering content, and shall be usable on mobile.

5.27 FDPS line items. FDPS pages shall list every inherited EDR line item and TSM statement, grouped by document, with its inheritance route and its status (Inherited, not reviewed; Kept; Broken, with reason and approver; Superseded (auto), with any pending Design Authority bulk confirmation; Direct), and a maturity indicator (line items reviewed of total, counting Kept, Broken and Superseded (auto), and numbers broken and superseded) (6B.7A).

5.28 Visual style and themes. The Hub shall use the company colour palette (primary #00405E, accent #46C1BE, light #9EDEDC, with their tints and neutral greys, plus the violet and amber group colours of 5.24) as its default theme, and shall offer dark and light themes as a user setting (the ⚙ control in the header) saved per user or device. All themes shall meet 5.11.

5.29 Mobile. Every page shall be usable on a phone: the left rail shall become a drawer, tables shall scroll within their category, the page groups shall stack in the order of 5.24, and the model preview, summary and AI bar shall remain available.

5.30 Owner of tree pages. The owner shown on a Sub-system (or Sub-structure) page shall be its Design Lead from the Role register (6C.14), shown as Design Lead (owner); there is no separate owner field for these pages.

## 5A. Users, Access Roles and Permissions

5A.1 Users. Every person who uses a Production Hub shall be a User record with a permanent identifier, name, email, Design Team and Design Sub-team (where applicable), status (Active, Suspended, Left) and a user page. People shall no longer be referenced as free-text names: every owner, contributor, approver, author, attendee and Role register entry shall link to a User. AI agents are not Users and can never hold an access role or an authority.

5A.2 Access roles. Access is given by named access roles, each bundling a set of permissions. The framework access roles are Admin, Design Lead, Design Authority, Engineer and Viewer (Annex B.6). Access roles are framework-fixed; a project may not add or edit them, but may grant one-off permission overrides (5A.5).

5A.3 Project assignment. A User shall have access to a project only through a Project Assignment, which records the project, one access role for that project, the validity dates and who assigned it. A User may hold different access roles on different projects. A User with no active assignment to a project shall not see that project's Production Hub data.

5A.4 Effectivity access. By default a User shall see every effectivity of each project to which they are assigned. An Admin may restrict a Project Assignment to listed effectivities; the user then sees, filters and edits only data whose effectivity overlaps the allowed effectivities, and the effectivity filter (5.25) offers only those; this applies to both viewing and editing (confirmed by Daniel, 12 Oct 2026). Data with no effectivity (for example EDRs, TSMs and framework pages) is not restricted.

5A.5 Permission overrides. An Admin may grant or deny a single permission to a User on a project, in addition to the permissions of the access role, with a reason, an expiry date (optional) and the approving Admin recorded. A deny override prevails over the role. Overrides shall be listed on the admin page and on the user page.

5A.6 Access roles and authority roles. Access roles control what a User may see and edit in the Hub. The authority roles of the Role register (6C.14, Annex B.4) control who may approve, agree, break and release, over a stated area. The two are separate: an authority role assignment shall require an active Project Assignment on that project whose access role includes the matching approval permission (Design Lead access role for a Design Lead authority, Design Authority access role for a Design Authority authority; Admin may hold either). The approval roles Technical Authority for Design, Design Approver and Discipline Lead have no access role of their own and are held on top of the Engineer access role (or Admin). The software shall check both at the date of each decision. Confirmed by Daniel, 12 Oct 2026.

5A.7 Owner and contributors. Every work item (FDPS, Issue, Action, Lesson Learned, Design Review, Hub Page, Requirement Document, TSM, Verification, Risk and any task record) shall have exactly one accountable Owner, a User, and may have any number of Contributors, also Users. The Owner shall hold an active Project Assignment with edit permission for the item's data type. Ownership changes shall be recorded with who changed it and when. Sub-system and Sub-structure pages keep the derived owner of 5.30 (the Design Lead from the Role register, itself a User).

5A.8 Admin page. Each Production Hub shall have an admin page, visible only to Users holding the Admin access role on that project, or to a framework administrator, who administers users across all projects (both kept, confirmed by Daniel, 12 Oct 2026), with: a searchable, filterable list of Users (name, Design Team, project, access role, effectivity access, overrides, status, last active); an edit panel per User to add or end Project Assignments, set the access role per project, restrict effectivities, add or remove permission overrides and suspend the User; and an audit trail of every access change. Access changes take effect immediately and are logged as Change Records of type Access change.

5A.9 User pages. Each User shall have a user page. In this version it shows only the name, Design Team and Sub-team, status, access role per project with effectivity access, authority roles from the Role register, and the items for which the User is Owner or Contributor, grouped by data type. Further content is to be defined.

5A.10 Permissions. Permissions are per data type and action: View, Create, Edit, Approve (per the authority checks of 6C.14), Release, Administer users. The permission bundle of each access role is set out in Annex B.6.

## 6. Framework Hub and Production Hubs

6.1 There shall be one standard Engineering Hub framework (the Framework Hub). It defines the page types, templates, controlled facets, link types and generic descriptions that every project uses.

6.2 Framework data is the project-independent content of the Framework Hub: the controlled facets and their options (2B, 2F), page templates (5.2), generic page descriptions (5.8), link types (2I.2), schemas (2A.1), and generic guidance and lessons learned that apply to any project. Framework data shall contain no project data.

6.3 Production data is the project-specific working data of one project: for example points of contact, project statistics, live views of the product models, part models, calculation documents, project lessons learned, configuration and effectivity records, and the project's tailoring of the framework (6.4).

6.4 A Production Hub is a versioned instance of the Framework Hub, created from a numbered framework version and tailored to the project it serves. Tailoring (for example a project's added facet options, page additions or hidden sections) shall be stored as separate project data that references the framework version and the framework page identifiers it modifies; framework pages shall never be edited in a Production Hub. Rationale: keeps framework content stored once (0.3) and lets framework updates be applied without losing tailoring.

6.5 Production data shall link to framework pages through the same controlled facets (2F) and by referencing framework page identifiers (2A.4). Framework pages shall never contain or embed production data; a Production Hub shall display the production data linked to each framework page alongside that page. The Production data links table shall include a Requirement column showing the permanent identifier and short title of each Requirement the record supports, as a click-through link.

6.6 Production Hub mastery. A Production Hub shall become master of the project's production data data type by data type, as recorded in its authority register (2J). Until a data type has moved, its current master (for example a PLM or CAD system, or released documents) remains authoritative and the Hub holds a typed production link to each record with its identifier and revision or issue.

6.7 Configuration control and effectivity. The Production Hub shall manage configuration control and effectivity for the production data it stores or links to: each production record shall carry its revision or issue, the baseline(s) it belongs to, and its applicability (effectivity). Effectivity shall be structured, not free text: a type, a from value, a to value (the placeholder upper value 999 for an open-ended range, 6A.12), and optional notes. Effectivity shall be filterable (for example all records effective for a given effectivity number). Until configuration and effectivity have moved to the Hub (2J), the Hub shall reflect the effectivity set by their current master; afterwards the Hub is master and the integrated tools synchronise with it. The Hub shall show which revision and effectivity apply in each view, including image views of the product (5.10). The detailed configuration control model is set out in 6A.

6.8 When a linked production record is superseded or its effectivity changes, the Production Hub shall flag the linked pages and data objects for review, following the link-type table (2I.2).

6.9 Framework updates. Updates to the Framework Hub shall be released as numbered framework versions. Each Production Hub shall record the framework version it uses, and shall be able to adopt a newer version in a controlled way: the changes shall be shown, the project's tailoring (6.4) shall be preserved, conflicts shall be flagged for human decision, and adoption shall require human approval.

6.10 Security. The Framework Hub shall be hosted publicly. Production Hubs shall be hosted on internal, access-controlled infrastructure, and production data shall never be placed in the Framework Hub. Before each framework version is published, its owner shall complete a content review confirming that it contains no project data or sensitive information.

6.11 Framework merge rules. When a Production Hub adopts a new framework version:

- a framework page that the project has tailored and that has changed shall be shown with both versions and the tailoring, and the project shall choose to keep, adopt or merge;
- a retired framework page shall remain visible as retired, with its tailoring and production links kept and flagged for re-pointing to its replacement;
- a facet option that is split shall be kept as deprecated, and every record using it shall be flagged for reclassification into one of the new options, with AI-proposed choices under 2H.5 and 2H.6 and no automatic reclassification;
- facet options that are merged shall be remapped automatically and the remapping logged;
- adoption shall not complete while any conflict on a mandatory facet or link remains unresolved.

## 6A. Configuration Control

6A.1 Product effectivities. A project shall have multiple product effectivities, identified by project and effectivity number. For example, Project D effectivities 1 to 2 are built to the initial design release standard, and later changes apply to later effectivities.

6A.2 Effectivity on the link. Effectivity shall be held on the link between a Part Instance (a position) and a Part revision, not on the Part itself. One Part Instance may link to different revisions over different effectivity ranges.

6A.3 Complete, non-overlapping ranges. For any one Part Instance, the effectivity ranges of its revision links shall not overlap and shall together cover the full effectivity range over which the Part Instance exists (6A.8), with no gaps. The software shall reject or flag any overlap or gap.

6A.4 Example. A problem is found in part D2822002-001 revision A. The part is modified and up-revised to revision B. Revision A is effective for 1 to 2, and revision B for 3 to 999.

6A.5 Up-revision. An up-revision shall close the current effectivity range and open a new one for the new revision.

6A.6 Terms. Part Definitions, Assembly Definitions and FDPSs shall have revisions; documents shall have issues. Part Instances and Assembly Instances are positions and shall not themselves be revised; changes to a Part Instance are recorded link changes (6A.7). A dash number is part of the part number and shall never be used to indicate a revision.

6A.7 Link changes. A change to a Part Instance's Build Station or Sub-system link, or to an Assembly Instance's Build Station link, shall be a recorded change (with author, date and reason), not a new Part revision. If the instance belongs to a released FDPS, the change shall require a new revision of that FDPS.

6A.8 Instance effectivity. A Part Instance shall carry its own existence range (instance effectivity), so that Part Instances can be added or removed by effectivity. By default the range is the full effectivity range of the project (for example 1 to 999, 6A.12). Effectivity shall therefore be held on the Part Instance to Part revision link (6A.2) together with the Part Instance's existence range.

6A.9 Interchangeability. A change that keeps a Part interchangeable in form, fit and function in every one of its uses shall create a new revision. A change that does not shall create a new part number, by rolling the dash number under 1.11.9. The software shall record the interchangeability assessment against each change.

6A.10 Baselines. A baseline shall be frozen for an FDPS at each FDPS release and at each review snapshot (6C.9). Baselines shall be numbered in sequence within each FDPS revision (for example D2822001-801 rev A, baseline 3). Each baseline shall record the FDPS revision, its effectivity range (6A.11), its population, the revision links and owned links of every member, its Compliance Statements, its interfacing Systems, its FDPS interfaces and the derived views at the time of freezing (for example the Systems of the FDPS and the inferred Categories). A baseline shall point only to frozen copies of records (6A.15), never to live records. Baselines shall never be edited, and the software shall compare any two baselines. The configuration of a product effectivity shall be given by the latest release baselines of the FDPS revisions effective at that effectivity.

6A.11 Effectivity types. Effectivity numbers shall be the primary effectivity type. Serial ranges and build standards shall be defined as named mappings to effectivity numbers. Each FDPS revision shall carry the effectivity range over which its exact content applies. Releasing a new FDPS revision shall close the range of the previous revision (6A.5, 6A.12), so that the released revisions of an FDPS neither overlap nor leave gaps. The software shall check that the configuration of the FDPS is the same at every effectivity within a revision's range.

6A.12 Open-ended ranges. An open-ended range shall be written with the placeholder upper value 999 (for example "3 to 999"). The value 999 shall mean "all later effectivities", shall never be allocated as a real effectivity number, and shall be shown as an open-ended range in every view. Closing an open-ended range (6A.5) shall replace 999 with the last effectivity number of that range.

6A.13 Release master. Until configuration data moves to the Hub (2J.6), the PLM system shall issue revisions and releases, and the Hub shall reflect them. Afterwards the Hub shall issue them and PLM shall synchronise with it.

6A.14 Assembly Instance effectivity. An Assembly Instance shall carry its own existence range (instance effectivity), with the same rules as a Part Instance: effectivity shall be held on the link between the Assembly Instance and its Assembly Definition revision (6A.2); the ranges of those revision links shall not overlap and shall together cover the Assembly Instance's existence range with no gaps (6A.3); by default the existence range is the full effectivity range of the project (6A.8); and open-ended ranges shall follow 6A.12. Assembly Instances shall not themselves be revised (6A.6).

6A.15 Frozen copies. Every saved change to a record shall create a new record version, and earlier versions shall be kept unchanged. Baselines, review snapshots and released FDPS revisions shall reference records by identifier and record version, so that a later change (for example closing the effectivity range of a revision link) never changes what a frozen record shows.

6A.16 Retrofit, Concession and as-embodied configuration. Retrofit records, Concession records (6A.17), and the as-embodied and as-manufactured configuration of built effectivities, are not in the current scope. They are held in section 7 (Future Development) for later development. The configuration held and shown by the software is the as-designed configuration (6A.10, 5.17).

6A.17 Non-compliance and release. Concessions are part of the manufacturing standard, not the design standard, and Concession records are not in the current scope (section 7). A known non-compliance of the design with a Requirement or TSM shall be recorded as a Compliance Statement with position Non-compliant over the effectivity range concerned, linked to the Issue that records it (2E). No FDPS revision shall be released for any effectivity at which a Compliance Statement of the FDPS is Non-compliant (6C.11). Where a non-compliance is found after a revision has been released, that released revision and its baselines shall stay unchanged as the as-designed record of the effectivities built to it; the Non-compliant statement shall be shown at those effectivities in every view and report (5.17, 2.8), and release for those effectivities shall stay blocked until a Compliance Statement restores compliance. How a built aircraft is recovered or accepted is outside the software until section 7 is in scope.

6A.18 Status for a selected effectivity. Status words shall not imply that an object is out of force when it is only limited by effectivity. The status of a Part Instance, revision or revision link shall be shown for the selected effectivity (Present or Not present, with a note of the ranges over which it applies), and closing a range shall not mark a record as removed.

## 6B. Requirements and TSM Inference

6B.1 Requirements shall be stored as data records and tagged to framework nodes in the Engineering Hub. Requirements shall keep their own levels (2C.7) according to what they are written against. Requirements and TSMs shall flow down to FDPS level only: Parts, Assemblies and items reach their Requirements and TSMs through the FDPS that contains them.

6B.1A Requirement documents. Requirements shall be held as line items grouped into Requirement Documents of kind EDR (Engineering Design Requirements). Every Requirement shall be Part of exactly one EDR. An EDR shall have its own code, title, issue and status, and may cover several Systems (EDRs are intended to be split by System, but overlap is allowed). Each line item shall keep its own level (2C.7), and one EDR may hold line items of different levels.

6B.2 Allocation. Each EDR shall be tagged at document level to one or more Sub-systems (or Sub-structures); one EDR may be tagged to many Sub-systems and one Sub-system may carry many EDRs. An FDPS shall inherit every EDR tagged to any Sub-system in which at least one of its Part Instances is homed, with all of its line items, by default. A line item may additionally be allocated to one or more nodes of the System tree (a Sub-system, a System or a System Group) as an optional narrowing: where it is, it shall flow only to inheriting FDPSs that have at least one Part Instance homed in a Sub-system at or below an allocated node. Example: a Fuel System usable storage requirement is allocated to the Fuel Storage Sub-system, and every FDPS containing a Part Instance homed in Fuel Storage inherits it. A Requirement may also be linked directly to an FDPS, or to an item for traceability, by a Satisfied by link; the FDPS concerned then holds the Requirement directly.

6B.3 The FDPSs that inherit a Requirement or are directly linked to it shall form the set that must claim compliance against it.

6B.4 Technical Standards Manuals (TSMs) shall be a requirement data type: the governing design standards, built from lessons learned and governing body standards (for example those of civil or military airworthiness authorities).

6B.5 TSM inheritance. Each TSM shall be tagged with one or more of Design Type, Discipline and System; TSMs shall not be tagged to Sub-systems. Each Sub-system (and Sub-structure) page shall list its applicable Design Types, and a TSM tagged with one of those Design Types shall reach every FDPS with a Part Instance homed in that Sub-system (the route Sub-system > Design Type > TSM). This route is in addition to the matches below. Each kind of tag is optional, but every TSM shall carry at least one tag. A TSM shall reach an FDPS if any one of its tags matches (tags are combined with OR, never AND): a Design Type tag matches when a Part or Assembly in the FDPS's population has that Design Type, including the modification Design Type of a modified bought-in Part (2B.10) and the Design Type Standard Part of catalogue items (1.10.1); a System tag matches when a Part Instance of the FDPS is homed in a Sub-system of that System; and a Discipline tag matches when the Discipline is listed on the Hub page of the FDPS's owning Design Team (the Design Team of its owning Design Sub-team). Matching is never against the Discipline register as a whole, because every Discipline applies to every design (4.2). Where there is doubt, a TSM shall be over-tagged rather than under-tagged. Each Design Team shall list its applicable Design Types and its applicable Disciplines on its Hub page. A Part in an FDPS whose Design Type is not on the owning Design Team's list, or not on the Design Type list of its home Sub-system, shall be flagged. Every matching tag is a basis of the Compliance Statement (6B.6).

6B.6 Display and bases. Inherited Requirements and TSMs shall be shown distinctly from directly linked ones. Where a Requirement or TSM reaches an FDPS by several routes (for example directly, and through a Sub-system), every route shall be recorded as a basis of its Compliance Statement.

6B.7 Line-item review and breaks. Every line item inherited by an FDPS (each Requirement of an inherited EDR and each statement of an inherited TSM) shall apply by default, with status Inherited, not reviewed. As the design matures, each line item shall be reviewed and either Kept (it applies) or Broken (it does not apply). A break shall record its reason, author, approver and date, and shall be approved under 6C.13. The inheritance shall not be deleted: a Broken line item stays visible and shall be flagged for re-confirmation when the FDPS population, its lead Sub-system, the document's tags or the line item itself change. A Requirement or TSM all of whose line items are Broken does not apply to the FDPS. Directly linked Requirements (6B.2) are shown as Direct alongside their status. Once the FDPS has defined links for a document, 6B.7A applies.

6B.7A Link maturity: flow down, define, flow up and supersede. Early, high-level links (EDRs tagged to Sub-systems, 6B.2; TSMs reached through Design Types, 6B.5) let work be linked before it is defined, and flow DOWN to every FDPS below as inherited line items (6B.7). As the design matures and Part Instances are known, defined links shall be made at the lowest level (to Part Instances or Assembly Instances); defined links flow back UP and SUPERSEDE the flowed-down links. Once a level has defined links (P2 below), every flowed-down line item of that document in that FDPS that no defined link reaches shall be superseded AUTOMATICALLY, with status Superseded (auto), and no manual break is needed. Superseded EDR line items need no confirmation. Superseded TSM statements shall require a BULK confirmation by the Design Authority (6C.13) for each FDPS and TSM; until confirmed they are shown as Superseded (auto), pending confirmation. Before a level has defined links, line items may still be Kept or Broken manually under 6B.7, a break still requiring reason and approver. For the gates (6C.11, 6C.15), Kept, Broken and Superseded (auto) line items count as reviewed; a pending Design Authority bulk confirmation of TSM supersessions blocks both gates.

Settled definitions and judgement calls (accepted by Daniel as written, 12 Oct 2026):
- P1 Defined link. A defined link is: for an EDR line item, a Satisfied by link from that Requirement to a Part Instance or Assembly Instance of the FDPS; for a TSM statement, the statement claimed on a Compliance Statement of the FDPS with at least one named Part Instance or Assembly Instance of the FDPS (3.15 statements_claimed parts). A Satisfied by link to the FDPS as a whole is not a defined link.
- P2 A level has defined links. For one FDPS and one document (EDR or TSM), the level has defined links when at least one line item of that document has a defined link within that FDPS. Supersession is evaluated per FDPS per document; a defined link in one document never supersedes line items of another document, and a defined link in one FDPS never affects another FDPS.
- P3 Manual decisions prevail. A line item already Kept or Broken by a manual review keeps that state; automatic supersession applies only to line items still Inherited, not reviewed. A Kept line item without a defined link, in a level that has defined links, is flagged for the FDPS owner.
- P4 Reversal. If the last defined link of a document in an FDPS is removed, its Superseded (auto) line items return to Inherited, not reviewed, and any DA bulk confirmation covering them lapses.
- P5 New and changed line items. A line item added or changed by a new issue (6B.10) in a level that already has defined links is Superseded (auto) unless it gets a defined link, and is listed on the FDPS page as newly superseded; for a TSM it needs a fresh DA bulk confirmation.
- P6 DA bulk confirmation scope. One confirmation record per FDPS per TSM, covering the full current set of Superseded (auto) statements. Any change to the set (a new supersession, or a statement regaining a link) requires a new confirmation. The Design Authority may reject individual statements from the set; a rejected statement returns to Inherited, not reviewed and must be Kept or Broken manually.
- P7 Superseded line items need no Compliance Statement, and are shown on FDPS pages greyed, with the defined links that superseded them.
- P8 Roll-up. Defined links roll up (flow UP) from Part and Assembly Instances to the FDPS, its Sub-systems and Systems as derived data; pages above FDPS level show, per document, how many FDPSs have defined links (document maturity).

6B.8 Compliance Statements. Compliance shall be stated per FDPS per Requirement or TSM, not per Part Instance, and only for Kept line items; a Broken line item needs no Compliance Statement. Each Compliance Statement shall carry an effectivity range. For any one FDPS and Requirement or TSM, the ranges of its Compliance Statements shall not overlap and shall together cover, with no gaps, the effectivity over which the FDPS's released revisions apply. There shall be one Compliance Statement per FDPS, Requirement or TSM and effectivity range, whatever the number of routes or Part Instances through which the Requirement or TSM reaches the FDPS.

6B.9 Verification effectivity. Each Verification shall carry the effectivity range over which it is valid evidence. At every effectivity in that range, each of its basis revisions shall be the effective revision of the instances of its definition that exist there. The evidence of a Compliant statement shall cover its range with no gaps. A Verification that supersedes another for the same FDPS and Requirement shall close the range of the one it supersedes, so that their ranges do not overlap.

6B.10 Change flags. Line items shall carry their own revisions. A new issue of an EDR or TSM shall flag, for every inheriting FDPS, only the line items that changed, were added or were removed in that issue, together with their Compliance Statements and Kept or Broken status; unchanged line items keep their status. Added line items arrive as Inherited, not reviewed. A changed item, revision or Verification shall flag the Compliance Statements whose evidence it affects.

6B.11 TSM statements. A TSM is a broad document holding many statements (for example, bonding of fuel system components sits within a Fluid Systems TSM, alongside statements that apply only to hydraulic or pneumatic systems). The Compliance Statement of an FDPS against a TSM shall list the statements of that TSM that apply to the FDPS, and shall claim conformance to those statements only. Each claimed statement may list the Parts to which it applies; listing Parts is optional, and a statement with no Parts listed is claimed for the FDPS as a whole (for example a routing or clearance statement that applies to the installation rather than to a Part). Every statement that does not apply shall be recorded as Broken under 6B.7; the claimed statements shall be exactly the Kept statements. The evidence of a Compliant statement shall cover, at each effectivity in its range (6B.9), every listed Part present there for a statement that lists Parts, and the FDPS for a statement claimed for the FDPS as a whole.

## 6C. Design Reviews

6C.1 Every FDPS shall pass three review stages: A Initial System Design, B Preliminary and C Detail (Scheme Reviews A, B and C). The review stages align with Lifecycle Stages 4 (Initial System Design), 5 (Preliminary Design) and 6 (Detailed Design) respectively (2B.13).

6C.2 A design review shall cover whole FDPSs. Review documentation shall be linked to every FDPS it covers.

6C.3 One review may cover several FDPSs. Its template shall be generated from all the FDPSs it covers.

6C.4 Review content shall include: an introduction, with a structured attendee list giving each person, the Discipline or team represented and the role held, and the review scope; the status of the FDPS's Requirements, with any non-compliances; confirmation of TSMs adhered to, with any non-conformances; agreement from each interfacing System (6C.22); agreement from every Sign-off team Discipline listed against the stage (6C.19); the designer's checklist responses, including the checks of Consideration only Disciplines (4.5); and known risks, held as structured Risk records.

6C.5 The content required at each stage shall vary as the design matures, and shall be defined in the Engineering Hub.

6C.6 Each Design Sub-team page shall be split into Initial System Design, Preliminary and Detail stages. Each stage shall list the checklist items to be answered at that stage (4.4), the Sign-off team Disciplines (2B.14) whose agreement is required at that stage and the stage-specific entry criteria (6C.15), and shall link to the relevant guidance and stakeholders. The Requirements, TSMs and interfacing Systems of each FDPS are inferred (6B, 6C.21) and are not listed on the stage page. Together these shall generate the review template for an FDPS at that stage. Design Sub-team stage pages shall be framework templates (generic stage guidance and default item lists) held in the Framework Hub, and shall be tailored for each project in its Production Hub through Tailoring Records (6.4); the tailored pages are production data.

6C.7 Review material shall be issued to supporting disciplines at least 2 weeks before the review.

6C.8 Every review shall be minuted. Actions shall be recorded as structured records using the action tracker template and tagged against the FDPSs covered. Each Action shall record who raised it. An Action shall be closed only when its closure evidence has been accepted by the person who raised it or by the review chair; the acceptance shall be recorded with the person and the date.

6C.9 Each review shall record a snapshot of the relevant design at that point in time, covering content and interfacing Systems, and shall freeze a baseline of each FDPS revision it covers (6A.10).

6C.10 The exit criterion shall be a Pass or Fail decision by the Technical Authority for Design. Each review shall record its chair.

6C.11 Release gate. An FDPS revision shall only be submitted to the release lifecycle once the FDPS has passed a C (Detail) review, carried forward where 6C.12 allows, and every Action raised at any A, B or C review covering the FDPS, including re-reviews and Actions raised from conditions of agreement (6C.19, 6C.22), is closed, every Compliance Statement of the FDPS over the revision's effectivity range is Compliant or an approved Not applicable (6A.17), and no inherited line item of the FDPS is Inherited, not reviewed (6B.7), Kept, Broken and Superseded (auto) counting as reviewed, and no Design Authority bulk confirmation of TSM supersessions is pending (6B.7A). A Cancelled Action shall count as closed only with a reason and the approval of the review chair. While PLM issues releases (6A.13), the PLM release workflow shall obtain the Hub's confirmation that the gate is met before releasing, through the documented interface (2J.2); a release without that confirmation shall be flagged as a discrepancy.

6C.12 Carry-forward and re-review. A later design change shall invalidate a review only if it is substantial (6C.17). A passed C review shall carry forward to later revisions of the FDPS unless the Design Authority for the area judges a change since the review snapshot to be substantial. The Design Authority shall assess every change against the snapshot when approving the FDPS revision for release, and the carry-forward shall be recorded with that assessment (assessor, date and reasons). If a change is judged substantial, a re-review shall be held at the FDPS's current review stage (normally C), scoped to the affected FDPS and the changed areas. At a re-review, the agreements required (6C.19, 6C.22) are those of the Disciplines and interfacing Systems whose areas the change affects, as identified by the Design Authority; the other agreements are carried forward from the review it follows and recorded as carried forward. The re-review's snapshot then becomes the reference for later assessments.

6C.13 Approval of breaks and supersessions. Superseded (auto) EDR line items need no approval; the Superseded (auto) statements of a TSM for an FDPS shall be confirmed in bulk by a Design Authority, as for a TSM statement break (6B.7A).  A break of an inherited EDR line item (6B.7) shall be approved by a Design Lead whose area is the FDPS's lead Sub-system, or for a Sub-structure FDPS its lead Sub-structure (1.7.7). A break of a TSM statement (6B.7, 6B.11) shall be approved by a Design Authority whose area covers the FDPS's owning Design Team, or a Design Type through which the TSM reaches the FDPS.

6C.14 Roles. The Technical Authority for Design (also known as the Design Licence Holder) is responsible for the design and gives the Pass or Fail at each review. The Technical Authority for Design may delegate release authority to Design Leads, Design Approvers or Design Authorities, who approve FDPSs and parts for release within their area. There is no FDPS Design Lead role: breaks of an FDPS's inherited interfaces are approved by a Design Lead whose area is the FDPS's lead Sub-system (1.7.7), which for a Sub-structure FDPS is its lead Sub-structure (6C.21). Each Production Hub shall hold a Role register recording, for each User (5A.1), each role held (Annex B.4: Technical Authority for Design, Design Authority, Design Lead, Design Approver, Discipline Lead), the delegated authority it carries, the area it covers (for example a Sub-system or Sub-structure, System, Design Sub-team, Design Team, Design Type or Discipline), who delegated it, and its validity dates. The software shall check every approval, agreement, release and decision against the Role register at the date it is given.

6C.15 Entry criteria. Each stage shall have the generic minimum entry criteria below. Design-Type-specific additions shall be held in the Engineering Hub on the relevant stage page, and the software shall check entry criteria before a review can be scheduled.

| Stage | Generic minimum entry criteria |
| --- | --- |
| A Initial System Design | Requirements flowing to the FDPS identified (6B.2); initial system layout and space allocation defined; interfacing Systems identified, with any broken interfaces recorded (6C.21). |
| B Preliminary | Preliminary geometry; TSM compliance plan; draft interface agreements; initial analysis. |
| C Detail | Full detail design; no inherited line item Inherited, not reviewed (6B.7; Kept, Broken and Superseded (auto) count as reviewed) and no pending Design Authority bulk confirmation of TSM supersessions (6B.7A); Compliance Statements for every Kept Requirement and TSM of the FDPS over its full effectivity (6B.8); analysis complete; all interfacing Systems agreed. |

6C.16 Multiple Design Types. When one review covers FDPSs containing several Design Types, all relevant criteria shall apply: the entry criteria shall be the union of the generic criteria and every applicable Design-Type-specific addition, and the substantial change assessment (6C.17) shall apply the criteria relevant to every Design Type covered.

6C.17 Substantial change. A change shall be substantial if, judged against the review snapshot (6C.9), it adversely affects compliance with any Requirement or TSM, degrades form, fit or function, degrades an interface, or adds a new interface with another System. A change that improves or restores compliance does not adversely affect it. A reduced margin that remains compliant shall not count as adversely affecting compliance, but the margin change shall be recorded. Added Part Instances or interfaces shall be substantial only if they add a new interface with another System or adversely affect compliance with a Requirement or TSM. A change that is not substantial shall not require a new review, but shall be recorded against the affected FDPS, with its author, date and reason, and linked to the review it follows. A Change Record may carry several change types, and the substantial assessment shall be recorded for each affected FDPS.

6C.18 Snapshot comparison. The review snapshot (6C.9) shall be held as structured data, and the software shall produce a structured difference between the snapshot and the current design (Part Instances, revisions, links, interfaces and compliance statements), highlighting changes that may degrade form, fit, function, interfaces or compliance under 6C.17, to support the assessment under 6C.12.

6C.19 Discipline agreement. Each Sign-off team Discipline listed against a review stage on the Design Sub-team page (6C.6), other than a Discipline the project has marked not applicable (2B.14), shall record its position before the Technical Authority for Design gives the Pass or Fail decision (6C.10): Agree; Agree with conditions; or Disagree, with reasons. Each condition shall be raised as an Action, to be closed before release (6C.11). The position shall be recorded as structured data on the review, with the person giving it and the date. A Pass shall not be recorded while any required position is missing or is Disagree. Consideration only Disciplines need no agreement at the review; the designer's checklist responses (4.5) are their record.

6C.20 Interface definition. Interfaces shall be defined at Sub-system level, on the Sub-system pages and Sub-structure pages: each page shall list the Systems, or the Sub-systems, with which the items of that Sub-system or Sub-structure interface. Every list shall be finite and decided per System; there shall be no 'interfaces with all' entry. A non-structural Sub-system page shall name the structural Systems or Sub-structures to which its items attach, so that every non-structural FDPS inherits its structural interfaces (R-10). A Sub-structure page shall name the Systems whose items are installed on or attach to that Sub-structure. Interfacing Systems shall be taken from these lists and from Supports links only; they shall not be derived from physical links such as Secures links or geometry (a cross-FDPS Secures link gives an FDPS interface instead, 6C.24). A Sub-structure list may include Systems that some of its FDPSs do not interface with; this over-inclusion is accepted and handled by breaks (6C.21).

6C.21 Inherited interfacing Systems. An FDPS shall inherit as interfacing Systems: (a) the Systems listed on the Sub-system pages of the non-structural Sub-systems in which its Part Instances are homed; (b) for a Sub-structure FDPS (1.7.7), the Systems listed on the Sub-structure pages of every Sub-structure in which its Part Instances are homed, so that a Sub-structure's list flows down to all the Sub-structure FDPSs in it; and (c) the Systems named in the Supports links of its items. A non-structural FDPS does not inherit the list of a Sub-structure page: its Part Instances homed in a Sub-structure (for example a bracket) contribute only through (c), as before. No inheritance goes beyond what each page lists (R-01). The FDPS's own home Systems are not interfacing Systems. An inherited interface may be broken for an FDPS where it does not apply. Every break shall be approved by a Design Lead whose area is the FDPS's lead Sub-system, or for a Sub-structure FDPS its lead Sub-structure (6C.14), and recorded with its reason, its author, the approver and the date. A broken interface stays visible and shall be flagged for re-confirmation when the FDPS population changes. A change to the interface list of a Sub-system or Sub-structure page shall flag the FDPSs that inherit from it.

6C.22 Interface agreement. At each review, the position of each interfacing System of the FDPS that is not broken shall be recorded as structured data, with the same positions as Discipline agreement (6C.19), by a person holding a Design Lead role for that System or one of its Sub-systems (6C.14), with the date. Each condition shall be raised as an Action. A Pass shall not be recorded while any required interface position is missing or is Disagree.

6C.23 Interfaces in snapshots. The review snapshot (6C.9) and the structured difference (6C.18) shall include the FDPS's interfacing Systems, its broken interfaces, its FDPS interfaces (6C.24) and the recorded interface agreements.

6C.24 FDPS interfaces. Each FDPS shall show its FDPS interfaces, derived from Secures links between its Part Instances and those of other FDPSs (1.6.6), with the other FDPS, the fastener and the held Part Instance. FDPS interfaces shall be included in the review template of each FDPS concerned, for information, and in its snapshots and baselines (6A.10, 6C.23). An FDPS interface is not an interfacing System and needs no interface agreement of its own (6C.22); the interfacing Systems of each FDPS are still set by 6C.21.

6C.24A Cross-FDPS fastener flags (R-18). When a Secures link is created or changed between a fastener in one FDPS and a Part Instance in another, the software shall raise a review flag to the owner of the other FDPS. Its decision shall be Accept or Query. A Query shall stay open, shall be shown on both FDPS pages, and shall not block the link; no confirmation of the link is required.

## 7. Future Development (not in current scope)

This section records capabilities that are planned but are not in the current scope. The requirements below shall not be implemented, enforced or checked until Daniel brings them into scope. They are recorded now so that the data model (2.2) can take them later without restructuring existing data.

7.1 Retrofit records. Where a new revision, or an added or replaced Part Instance, is to be applied to effectivities already built, a Retrofit record shall reference the Change Records and revisions it applies, carry its own effectivity range, and record for each effectivity in that range an embodiment status (Planned, Embodied or Not embodied), with the date and the person recording it. A Retrofit shall not change the effectivity ranges of the as-designed configuration. (Moved from v21 6A.16.)

7.2 As-embodied and as-manufactured configuration. The software shall hold, for each built effectivity, its as-embodied configuration (the as-designed configuration plus embodied Retrofits) and its as-manufactured configuration (including accepted manufacturing deviations), and shall show either alongside the as-designed configuration in the effectivity selector (5.17). A Concession (7.4) shall then be able to end for one effectivity of its range on embodiment.

7.3 Scan comparison. Scans of manufactured parts and of assembled aircraft shall be compared with the design standard (the as-designed configuration of the effectivity concerned) to show the differences. Each scan shall be a data object with its origin, the effectivity and item scanned, and the date. Differences shall be held as structured data against the Part Instances concerned, and differences outside tolerance shall be flagged for review.

7.4 Concessions. Concessions are part of the manufacturing standard, not the design standard (moved from v22 6A.17). A known non-conformance of a built aircraft with its design standard shall be recorded as a Concession, with the serial-number aircraft (effectivities) concerned, the Requirement, TSM or design data not met, any limitations, its expiry condition and its approvals. If the Concession needs a re-design, that design solution shall apply to the serial-number aircraft concerned and shall be released as design data effective for those effectivities. If it does not, Design shall be one of the authorities that sign off the solution.

7.5 Until 7.1 to 7.4 are in scope, Concessions, Retrofits and the recovery of built aircraft are recorded outside the software. The software holds the as-designed configuration only, and a non-compliance of the design is shown as a Non-compliant Compliance Statement that blocks release for the effectivities concerned (6A.17).

## Annex A. Starter Value Registers: Placeholder (generic, fictional)

Every list in this annex is a Placeholder (generic, fictional). The lists are illustrative starting points for a fictional project, are not derived from any specific programme, and shall be replaced by the real lists of each project, held as project data in its Production Hub (6.4).

### A.1 Major Units: Placeholder (generic, fictional)

Front Fuselage; Centre Fuselage; Rear Fuselage; Wings; Fins; Final Assembly (catch-all, 2C.4 and 2C.11).

### A.2 Build Stations: Placeholder (generic, fictional)

| Major Unit | Build Stations |
| --- | --- |
| Front Fuselage, Centre Fuselage, Rear Fuselage, Wings, Fins (each) | BS1 Structural Assembly; BS2 Systems First-fix Installation; BS3 Equipping and Closure; BS4 Functional Test |
| Final Assembly | FA1 Major Unit Join; FA2 Cross-join Systems Connection (pipes and looms); FA3 Landing Gear and Propulsion Installation; FA4 Final Equipping and Closure; FA5 Ground Test and Delivery Preparation |
| Every Major Unit, including Final Assembly (each) | Bench: off-aircraft assembly (1.8.1, 2C.12) |

### A.3 Sub-systems: Placeholder (generic, fictional)

Every System also has a General Sub-system (2B.11). The Sub-systems of the four structural Systems are Sub-structures (2B.11). The interfacing Systems of each Sub-system and Sub-structure are listed on its page as project data (6C.20); no list is 'all Systems'.

| System | Sub-systems (Sub-structures for the four structural Systems) |
| --- | --- |
| Primary Structure | Frames and Bulkheads; Spars and Ribs; Longerons and Stringers; Major Joints and Attachments |
| Secondary Structure | Brackets and Supports; Fairings; Floors and Platforms; Equipment Racks |
| Skins, Doors & Panels | Skins; Access Panels; Doors and Hatches |
| Windscreen & Canopy | Transparencies; Canopy Frame; Canopy Actuation and Locking |
| Propulsion | Engine Installation; Engine Mounts; Engine Controls Interface |
| Intake & Ducts | Intake Ducts; Exhaust and Nozzle; Auxiliary Air Inlets |
| Fuel | Fuel Storage; Fuel Feed; Refuel and Defuel; Vent and Pressurisation; Fuel Gauging |
| Electrical Power Generation & Distribution | Generation; Primary Distribution; Secondary Distribution; Energy Storage; External Power |
| Hydraulics | Hydraulic Generation; Hydraulic Distribution; Storage and Conditioning |
| Pneumatics | Air Supply; Pneumatic Distribution |
| Flight Control | Primary Flight Control Actuation; Secondary Flight Control; Flight Control Computing and Sensors |
| Vehicle Management | Vehicle Management Computing; Health and Usage Monitoring; Data Networks |
| Landing Gear | Main Gear; Nose Gear; Wheels and Brakes; Steering; Extension and Retraction |
| Navigation | Inertial and Satellite Navigation; Air Data; Radio Navigation Aids |
| Environmental Control | Air Conditioning; Pressurisation; Ice and Rain Protection |
| Thermal Management | Liquid Cooling Loops; Heat Exchangers and Heat Sinks; Thermal Control |
| Fire Protection | Fire and Overheat Detection; Fire Suppression |
| Crew Escape & Safety | Escape System; Life Support; Survival Equipment |
| Cockpit & Controls | Displays; Inceptors and Controls; Cockpit Furnishings and Seat Interface; Interior and Exterior Lighting |
| Radar / Sensors | Radar; Electro-optical Sensors; Sensor Processing |
| Electronic Warfare | Warning Receivers; Countermeasures |
| Communications | Radio Communications; Intercom and Audio; Identification |
| Data Links | Line-of-sight Data Link; Beyond-line-of-sight Data Link |
| Stores Integration (incl. Armaments) | Carriage and Release Equipment; Stores Management; Internal Armament |
| Flight Test Instrumentation | Sensors and Transducers; Data Acquisition and Recording; Telemetry |

### A.4 Design Teams and Design Sub-teams: Placeholder (generic, fictional)

| Design Team | Design Sub-teams |
| --- | --- |
| Structures | Forward Structure; Centre Structure; Aft Structure; Wing and Fin Structure; Skins, Doors and Panels; Transparencies |
| Fluid Systems | Fuel; Hydraulics and Pneumatics; Environmental and Thermal |
| Electrical Systems | Power Systems; Looms and Harnesses |
| Propulsion Integration | Engine Installation; Intakes and Exhausts |
| Mechanical Systems | Landing Gear; Flight Control Mechanisms; Escape Systems |
| Avionics and Mission Integration | Cockpit; Avionics Installation; Mission Systems Installation; Test Instrumentation |

Each Design Team lists its applicable Design Types and its applicable Disciplines on its Hub page (6B.5). Every Design Team list includes Standard Part. Placeholder Design Type lists (each also including Standard Part): Structures: Metallic - Machined; Metallic - Sheet; Metallic - Cast / Forged; Metallic - Additive; Carbon Fibre Composite; Other Composite (glass, aramid); Glazing. Fluid Systems: Pipework; Bought-in Equipment; Metallic - Machined; Metallic - Sheet; Non-metallic - Moulded. Electrical Systems: Electrical Looms; Bought-in Equipment; Metallic - Sheet. Propulsion Integration: Pipework; Metallic - Machined; Metallic - Sheet; Carbon Fibre Composite; Bought-in Equipment. Mechanical Systems: Metallic - Machined; Metallic - Cast / Forged; Non-metallic - Moulded; Bought-in Equipment. Avionics and Mission Integration: Bought-in Equipment; Metallic - Sheet; Electrical Looms; Other Composite (glass, aramid). Placeholder Discipline lists: Structures: Structural Analysis (Stress). Fluid Systems: Fluid Systems. Electrical Systems: Electrical Systems. Propulsion Integration: Fluid Systems; Mechanical Systems. Mechanical Systems: Mechanical Systems. Avionics and Mission Integration: Electrical Systems; Electro-Magnetic Compatibility.

### A.5 Design Type: Placeholder (generic, fictional)

Metallic - Additive; Metallic - Machined; Metallic - Sheet; Metallic - Cast / Forged; Carbon Fibre Composite; Other Composite (glass, aramid); Non-metallic - Moulded (seals, rubbers, plastics); Glazing (canopy, windscreen); Pipework; Electrical Looms; Bought-in Equipment (pumps, LRUs, actuators, used together with Source Bought-in Equipment); Standard Part (catalogue items such as fasteners, seals, fittings and clamps, used together with Source Standard Part, 1.10.1). Coatings, sealants and treatments are not Design Types; they are Finish Specification records (2D.6). A modified bought-in Part keeps Bought-in Equipment and also records the Design Type of its modification (2B.10).

### A.6 Safety Classification: Placeholder (generic, fictional)

| Code | Classification | Meaning (worst credible effect of failure) |
| --- | --- | --- |
| A | Catastrophic | Loss of aircraft or loss of life |
| B | Hazardous | Serious injury or large reduction in safety margins |
| C | Major | Significant reduction in safety margins or crew capability |
| D | Minor | Slight reduction in safety margins |
| E | No safety effect | No effect on safety |

### A.7 System applicability: Placeholder (generic, fictional)

| System | Aircraft | Ground Equipment | Test Equipment | Facilities |
| --- | --- | --- | --- | --- |
| Primary Structure; Secondary Structure; Skins, Doors & Panels; Windscreen & Canopy | Yes | No | No | No |
| Propulsion | Yes | No | Yes | Yes |
| Intake & Ducts | Yes | No | No | No |
| Fuel | Yes | Yes | Yes | Yes |
| Electrical Power Generation & Distribution | Yes | Yes | Yes | Yes |
| Hydraulics; Pneumatics | Yes | Yes | Yes | No |
| Flight Control; Vehicle Management; Navigation | Yes | No | Yes | No |
| Landing Gear | Yes | No | No | No |
| Environmental Control; Thermal Management | Yes | Yes | No | No |
| Fire Protection | Yes | No | No | Yes |
| Crew Escape & Safety; Cockpit & Controls | Yes | No | Yes | No |
| Mission Systems (all) | Yes | No | No | No |
| Flight Test Instrumentation | Yes | No | Yes | No |

Systems specific to other Product Scopes (for example Ground Handling, including stores loading, and Building Services) shall be added when those scopes' breakdowns are defined (2C.13).

### A.8 Common part Type codes: Placeholder (generic, fictional)

FS Fastener; SL Seal; BR Common bracket; CL Clip or clamp; FT Fluid fitting; EC Electrical connector or component; SP Spacer or shim. The code BI is reserved for bought-in project control numbers (1.11.11) and shall not be used as a Type code. Type codes apply only to common parts designed by the project; catalogue items (for example catalogue clamps and fasteners) are Standard Parts and keep their catalogue numbers (1.11.5).

## Annex B. Framework Value Registers

These registers are framework registers held in the Framework Hub. They are generic and are not placeholders. A project may extend them only through Tailoring Records (6.4).

### B.1 Lifecycle Stage

| No. | Lifecycle Stage | In current scope |
| --- | --- | --- |
| 1 | Opportunity | No |
| 2 | Concept Development | No |
| 3 | Architecture/Configuration Design | No |
| 4 | Initial System Design | Yes |
| 5 | Preliminary Design | Yes |
| 6 | Detailed Design | Yes |
| 7 | Manufacture & Assembly | No |
| 8 | Qualification | No |
| 9 | Production | No |
| 10 | Support & Upgrades | No |
| 11 | Disposal | No |

The current scope of the software and the Engineering Hub is Initial System Design to Detailed Design (stages 4 to 6), and shall be expanded later (2B.13).

### B.2 Discipline

Every Discipline is also a design consideration that all designs shall address (4.2). Sign-off team Disciplines listed against a review stage shall give agreement at that review (6C.19); Consideration only Disciplines are checked by the designer (4.5).

| Discipline | Discipline type |
| --- | --- |
| Aerodynamics | Sign-off team |
| Affordability and Cost | Consideration only |
| Airworthiness and Certification | Sign-off team |
| Assembly, Interfaces, Tolerances and Interchangeability | Consideration only |
| Configuration Management | Sign-off team |
| Design | Sign-off team |
| Electrical Systems | Sign-off team |
| Electro-Magnetic Compatibility | Sign-off team |
| Environmental Factors (protection treatments, drainage, weather and tank sealing) | Consideration only |
| Fluid Systems (fuel, hydraulics and pneumatics) | Sign-off team |
| Future Upgrades and Obsolescence | Consideration only |
| Human Factors | Sign-off team |
| Low Observability | Sign-off team |
| Maintainability, Reliability and Ground Equipment | Sign-off team |
| Manufacturing Engineering | Sign-off team |
| Materials and Processes | Sign-off team |
| Mechanical Systems | Sign-off team |
| Model Based Systems Engineering (Digital Thread) | Consideration only |
| Quality | Sign-off team |
| Safety | Sign-off team |
| Segregation, Separation and Survivability | Consideration only |
| Standard Parts and Supply Chain | Sign-off team |
| Structural Analysis (Stress) | Sign-off team |
| System Layout and Integration | Consideration only |
| Test | Sign-off team |
| Weight | Sign-off team |

The register holds 26 Disciplines. Fluid Systems was added in v21; Mechanical Systems does not cover fluid systems. A project may mark a Discipline not applicable (2B.14).

### B.3 Verification method

Analogy; Design Review; Calculation Analysis; Safety Assessment; Laboratory/Bench/Rig Tests; Product Ground Tests; Flight Tests; Design Inspection; Simulation; Equipment Qualification.

### B.4 Role

Roles held in each project's Role register (6C.14). Each assignment records the person, the role, the delegated authority, the area covered, who delegated it, and its validity dates.

| Role | Authority (summary) | Typical area |
| --- | --- | --- |
| Technical Authority for Design (Design Licence Holder) | Responsible for the design; Pass or Fail at reviews (6C.10); approves a project's non-applicability of a Discipline (2B.14); delegates release authority (6C.14) | Project |
| Design Authority | Assesses substantial change and approves FDPSs and parts for release within the area (6C.12, 6C.14); approves breaks of TSM statements for FDPSs of its Design Team or reached through its Design Types (6C.13) | Design Team; Design Type |
| Design Lead | Approves breaks of EDR line items for FDPSs whose lead Sub-system or lead Sub-structure is its area (6C.13); is the owner shown on its Sub-system page (5.30); gives interface agreement for its System (6C.22); approves breaks of the inherited interfaces of FDPSs whose lead Sub-system or lead Sub-structure is its area (6C.21); may hold delegated release authority (6C.14) | Sub-system or Sub-structure; System |
| Design Approver | Approves FDPSs and parts for release within the area, where delegated (6C.14) | Design Sub-team; Design Team |
| Discipline Lead | Gives or delegates Discipline agreement at reviews (6C.19); approves justifications of No checklist responses (4.5) | Discipline |

### B.5 Dash number ranges

| Dash numbers | Kind of object | Handedness |
| --- | --- | --- |
| -001 to -399 | Made parts | Odd: left-hand or unhanded; next even: right-hand version (1.11.8) |
| -401 to -799 | Assemblies | As above |
| -801 and above | FDPSs | As above |

A non-interchangeable change rolls the dash number by 2 within the same stem (1.11.9). Bought-in project control numbers (Project letter, BI and a four-digit sequence, for example D-BI-0001) have no dash number (1.11.11).

### B.6 Access roles (framework-fixed, 5A.2)

Status: permission bundles confirmed by Daniel, 12 Oct 2026.

| Access role | Permissions (summary) |
| --- | --- |
| Admin | Everything an Engineer can do; administer users, Project Assignments, effectivity restrictions and permission overrides on the project (5A.8); view the audit trail. |
| Design Lead | Engineer permissions; may hold Design Lead authority roles (5A.6); approve EDR line-item breaks and interface breaks within the Role register area. |
| Design Authority | Engineer permissions; may hold Design Authority authority roles (5A.6); approve TSM statement breaks and bulk-confirm TSM supersessions within the area; approve for release where delegated. |
| Engineer | View all project data within the allowed effectivities; create and edit FDPSs, line-item reviews, compliance, verifications, issues, actions, lessons and pages they own or contribute to; raise review flags. |
| Viewer | View only, within the allowed effectivities; may comment and use the AI bar. |

## Background observations (for context, not requirements)

- Specification data is often held in PDFs and must be manually read and re-typed before use.
- Terminology is used inconsistently. For example, design teams (Centre Fuselage Primary Structure, Front Fuselage Primary Structure, Skins and Panels, Fluid Systems, Electrical Systems) are used interchangeably with major units, so a project management list may show one part under Centre Fuse, another under Fluids and another under Electrical. Some teams work within one major unit while others work across the whole aircraft within one system, which mixes two dimensions in one field.
- Minor problems that one engineer could resolve in a few hours are raised at chief engineers' meetings, where hours are spent discussing them and who will pay for the work. Meanwhile, high-impact topics are sometimes not raised appropriately because the originator is less confident.
- Lessons learned are recorded in inconsistent formats (notes, Word reports), so finding relevant ones means reading whole reports, and in practice they go unused.
- The right top-level breakdown depends on perspective: someone working through the lifecycle wants stages at the top, whereas someone working on an aircraft system wants that system at the top. No single fixed structure suits everyone, so the structure must be variable (2F).
- AI may in future be able to do most of the current engineering work. People still need meaningful work and purpose, so human involvement is kept deliberately (0.3, 0.5).

## Remaining decisions

1. Real lists: replace the Placeholder (generic, fictional) lists in Annex A (Major Units, Build Stations, Sub-systems, Design Teams and Design Sub-teams, Design Types, Safety Classification, System applicability and common part Type codes) with the real lists of the first project, held as Production Hub data. Until then, the placeholder lists are the accepted starting values.
2. Safety Classification: confirm the scheme (1.10.2, Annex A.6) against the safety assessment process of the applicable airworthiness authority.
3. Integration: confirm the PLM and CAD systems in scope and the timing of the first data type move (2J.6).
4. Worked example: confirm or decide the remaining findings in section 12 of Worked Example - FDPS End-to-End v4, which arose when the example was re-run against this version.
