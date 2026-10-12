# Data Schema - Draft v7.6

Status: draft for review, version 7.6 (12 Oct 2026). Owner: Daniel Wagner. Derived from: Future Design Software: Requirements Prompt, version 24.6 (all requirements settled). The judgement calls of section 6.1 are accepted, the placement of the former consideration list (section 6.16) is settled, and Daniel's decisions on the 50 findings of Worked Example - FDPS End-to-End v1 are applied (section 6.17), as are his decisions on the remaining findings R-01 to R-08 of Worked Example - FDPS End-to-End v2 (section 6.18), his decisions on the remaining findings R-09 to R-14 of Worked Example - FDPS End-to-End v3 (section 6.19), his decisions of 12 Oct 2026 on EDRs, line-item inheritance, Lessons Learned tagging and Hub page layout (section 6.20), and his earlier decisions R-15 and R-18, omitted from v7 and added in v7.1 (section 6.21), and his link-maturity principle, with its settled definitions P1 to P8 (section 6.22), and his Hub page layout decisions (section 6.23), and his decisions on Users, access roles and permissions (section 6.24).

Revision history:

- v1 (10 Oct 2026): first proposed draft, derived from Requirements Prompt v18.
- v2 (10 Oct 2026): the eight judgement calls of section 6.1 accepted and marked settled; Lifecycle Stage, Discipline and Verification method registers defined (replacing placeholders), aligned with Requirements Prompt v19; review stages renamed A Initial System Design, B Preliminary, C Detail; Design Consideration driven by the Discipline register, with Discipline agreement recorded on Design Reviews. Scope: Future Design Software and its Engineering Hub.
- v3 (10 Oct 2026): aligned with Requirements Prompt v20. Placement of the former considerations settled (section 6.16, 3.22): Thermal checklist items sit in the Low Observability Design Consideration (moved from System Layout and Integration); Environmental Impact and Sustainability items stay in Materials and Processes; Vibration and Shock items stay in Structural Analysis (Stress). References updated from v19 to v20.
- v4 (11 Oct 2026): aligned with Requirements Prompt v21, applying Daniel's decisions on the 50 findings of Worked Example v1 (mapping in section 6.17). Main changes: Compliance Statement keyed by FDPS, Requirement or TSM and effectivity range, with multi-valued bases (3.15); Requirement allocation to any System tree node and flow to FDPSs (3.13); TSM Governs Design Type only (3.14); Verification effectivity (3.16); interface lists on Sub-system pages, inherited interfacing Systems and interface breaks on FDPS, interface agreements on Design Review (3.10, 3.18, 3.24); Discipline agreement positions, attendees, chair, re-review fields (3.18); Action raised_by and closure acceptance (3.20); FDPS Revision effectivity and baselines per FDPS revision pointing to frozen record versions (3.11, 3.27, 1.2); Change Record with several change types and per-FDPS substantial assessment (3.28); new data types Retrofit, Concession, Role Assignment and Risk (3.33 to 3.36); numbering fields for Part, Assembly and FDPS numbers (3.3, 3.7, 3.10); Fluid Systems Discipline (26 entries), Role, Dash range, Agreement, Compliance basis and Embodiment registers (2.2); Bench Build Stations; Thermal split; examples corrected (D2822001 stems, VR-SUB-0032 feed pipe, register ids).
- v5 (11 Oct 2026): aligned with Requirements Prompt v22, applying Daniel's decisions on the remaining findings R-01 to R-08 of Worked Example v2 (mapping in section 6.18). Main changes: is_structural flag on System entries; interfacing Systems inherited only from the Systems of the FDPS's own parts plus Structure, with structural Sub-system lists not cascading, and interface breaks approved by the FDPS's Design Lead (2.1, 3.10, 3.24, 3.35, 5); TSM restructured as a broad document holding statements, tagged by any of Design Type, Discipline and System through Governs links and reaching an FDPS if any tag matches; Compliance Statements list the claimed TSM statements and the Parts each applies to; Verification Demonstrates links name the TSM statements demonstrated; new Design Type Standard Part; Design Team pages list applicable Disciplines; Compliance basis register extended (2.2, 3.3, 3.14, 3.15, 3.16, 3.24, 4, 5); Retrofit data type and Embodiment register moved to section 7 (Future Development), Concession without Retrofit reference and with a mandatory expiry condition (3.2, 3.33, 3.34, 7); Assembly Instance owns one aircraft Build Station link and its Part Instances are Located at a Bench (3.5, 3.9, 4, 5); substantial-change criteria worded as adversely affects compliance, or degrades form, fit, function or an interface (3.28); Secures link and Fastener item property, fastener home Sub-system set from Secures (2.2, 3.5, 4, 5); bought-in project control number D-BI-nnnn (2.2, 3.3); stems take the FDPS's stem codes (3.3, 3.7).
- v6 (11 Oct 2026): aligned with Requirements Prompt v23, applying Daniel's decisions on the remaining findings R-09 to R-14 of Worked Example v3 and on the Design Lead role (mapping in section 6.19). Main changes: Sub-systems of structural Systems are Sub-structures (is_sub_structure derived from is_structural); Sub-structure pages carry finite interface lists that flow to every Sub-structure FDPS with a Part Instance homed in them, with no 'all Systems' list (2.1, 3.24, 5); new FDPS field lead_sub_system, which sets the break approver and whether the FDPS is a Sub-structure FDPS, and FDPS interfaces derived from cross-FDPS Secures links (3.10, 3.19, 3.27, 4, 5); the FDPS area kind and the FDPS Design Lead are removed from the Role Assignment (3.35); Fastener item property marks Parts requiring a Secures link (2.2, 3.3, 3.5); Concession data type moved to section 7, and a Non-compliant Compliance Statement references its Issue and blocks release for its range (3.11, 3.15, 3.34, 7); TSM claimed statements may omit parts, meaning the FDPS as a whole (3.15, 3.16); Design Team applicable_disciplines confirmed (3.24, R-11).
- v7.6 (12 Oct 2026): aligned with Requirements Prompt v24.6. Access-role permission bundles (Annex B.6) confirmed by Daniel; 3.38 and 6.24 updated.
- v7.5 (12 Oct 2026): aligned with Requirements Prompt v24.5. Daniel's confirmations on Users recorded in section 6.24 (separate access and approval roles; Technical Authority for Design, Design Approver and Discipline Lead on top of Engineer; restriction covers view and edit; framework administrator flag kept). Access Role may_hold_authority values set (3.38). Permission bundles remain proposed.
- v7.4 (12 Oct 2026): aligned with Requirements Prompt v24.4 (Users, section 5A; mapping in section 6.24). New data types User, Access Role, Project Assignment, Effectivity Restriction and Permission Override (3.37 to 3.41); People become User records and every ref(Person) is a ref(User); common field owner is a User and a new common field contributors is added (1.2); Role Assignment person is a User with a matching Project Assignment (3.35); registers ACCROLE, PERM and USTATUS and change type Access change added (2.2).
- v7.3 (12 Oct 2026): aligned with Requirements Prompt v24.3 (Hub page layout, mapping in section 6.23). Hub Page layout field rewritten for the five page groups (Requirement, Verification, Product, Considerations, Working Data), no Links area, summary fields and tiles (3.24).
- v7.2 (12 Oct 2026): aligned with Requirements Prompt v24.2 (link maturity, 6B.7A; mapping in section 6.22). LISTATE gains Superseded (auto); Line-item Review gains system-set Superseded (auto) records with superseded_by links and bulk_confirmation; new data type TSM Supersession Confirmation (3.15B); gate rules count Kept, Broken and Superseded as reviewed and block on pending confirmations (5). Definitions P1 to P8 settled.
- v7.1 (12 Oct 2026): aligned with Requirements Prompt v24.1. Daniel's decisions R-15 and R-18, previously held only in the repo delta schema_delta_R15_R18.json, written in (section 6.21): FDPS lead_sub_system_approval (3.10); change type Lead Sub-system change (2.2 CHG); Review Flag fdps_interface flag with Accept and Query decisions (3.31).
- v7 (12 Oct 2026): aligned with Requirements Prompt v24 (mapping in section 6.20). Main changes: new data type Requirement Document of kind EDR, with a many-to-many Sub-system tag (3.13A); every Requirement is Part of exactly one EDR, keeps its own level and carries a line-item revision, and Allocated to becomes an optional narrowing (3.13); TSM statements carry a revision, TSMs carry no Sub-system tag, and Sub-system pages list applicable Design Types giving the Sub-system > Design Type > TSM route alongside the existing tag matches (3.14, 3.24, 5); new data type Line-item Review recording Kept or Broken per FDPS per inherited line item, with reason and approver (Design Lead of the lead Sub-system for EDR line items, Design Authority for TSM statements) (3.15A); Compliance Statements only for Kept line items, and claimed TSM statements equal to the Kept statements (3.15); Stage C entry and release gate require no unreviewed line items (3.10, 3.11, 5); Lessons Learned gain mandatory design_type and optional sub_system tags and are matched by tag (3.21); Hub Page gains EDR and TSM page types, Sub-system applicable_design_types, the Design Lead as owner of Sub-system pages and the page layout settings (3.24, 2.2); registers DOCKIND and LISTATE added and BASIS extended (2.2); link types Part of, Tagged to and Reviews line item added (4).

Purpose of this document. It proposes a standard schema (2A.1) for every data type implied by the v23 requirements, so that each can be reviewed and agreed one at a time. Requirement references (for example 1.6.1, 6A.3) point to v24. Where v23 does not settle a point, the choice made here is listed in section 6, either as settled (accepted) or as a point for review. All values and examples are Placeholder (generic, fictional), drawn from Annex A or invented for Project D, except the Lifecycle Stage, Discipline and Verification method registers, which are the generic framework registers of v19 Annex B; none relate to any real programme.

How to review. Read section 1 (conventions) and section 2 (value registers) first, because every data type in section 3 relies on them. Then review each data type in section 3 together with its points in section 6. Sections 4 and 5 summarise the link types and inference rules used throughout.

Notation used in field tables:

- Types: string (short text), text (long text), int, decimal, bool, date, datetime (ISO 8601, stored in UTC), qty (value with explicit unit, 1.4), ref(X) (permanent identifier of a data object of type X), reg(X) (identifier of an entry in value register X, section 2), eff (structured effectivity range, 1.5), json (structured content with a published sub-schema).
- Cardinality: 1 = required, exactly one; 0..1 = optional; 1..n = required, one or more; 0..n = optional, any number. "1*" = required once the stated condition applies.
- "Common" = the common fields of 1.2, carried by every data type and not repeated in each table.
- Derived fields are never stored on the object (1.6.3, 1.7.3). They are computed on read, or cached in a rebuildable index that is never treated as master.

## 1. Conventions

### 1.1 Identifiers (2A.4)

- Every data object has a permanent identifier: PREFIX-SCOPE-NNNNNNN, for example PI-D-0004127. PREFIX is the data type code below. SCOPE is the project letter for production data, or FW for Framework Hub data. NNNNNNN is a sequence of seven digits, allocated by the software and never reused.
- The identifier is opaque. It never encodes a facet or Category (1.11.1) and never changes, even if the object's links, owner or title change.
- Business identifiers are held as separate fields: part number, FDPS number, requirement number, TSM clause, revision code and issue. They are unique within the project (1.11.6), but they are not the permanent identifier.
- Value register entries use VR-REGISTER-NNNN, for example VR-SUB-0031. The register codes are listed in section 2.

| Data type | Prefix | Data type | Prefix | Data type | Prefix |
| --- | --- | --- | --- | --- | --- |
| Project | PRJ | Requirement | REQ | Hub Page | PG |
| Effectivity | EFF | TSM | TSM | Production Link | PL |
| Part Definition | PD | Compliance Statement | CS | Authority Register Entry | AR |
| Part Revision | PR | Verification | VER | Baseline | BL |
| Part Instance | PI | Issue | ISS | Change Record | CR |
| Instance-Revision Link | IRL | Design Review | DR | AI Query Log | AIQ |
| Assembly Definition | AD | Review Snapshot | RS | Image | IMG |
| Assembly Revision | AV | Action | ACT | Review Flag | RF |
| Assembly Instance | AI | Lesson Learned | LL | Link (generic) | LNK |
| FDPS | FD | Design Consideration | DC | Checklist Response | CK |
| FDPS Revision | FR | Parameter | PAR | Tailoring Record | TR |
| Finish Specification | FS | Parameter Iteration | PIT | Framework Version | FV |
| Retrofit (reserved; section 7) | RT | Concession (reserved; section 7) | CON | Role Assignment | RA |
| User | USR | Project Assignment | PA | Effectivity Restriction | ER |
| Permission Override | PO | Access Role | register ACCROLE | | |
| Risk | RSK | | | | |

### 1.2 Common fields (carried by every data object)

| Field | Type | Card. | Values / register | Notes | Ref |
| --- | --- | --- | --- | --- | --- |
| id | string | 1 | 1.1 format | Permanent; never reused. | 2A.4 |
| type | reg(DATA_TYPE) | 1 | Section 3 types | Sets the schema. | 1.1 |
| schema_version | string | 1 | e.g. "1.0" | Version of this schema the record conforms to. | 2.2, 2A.1 |
| title | string | 1 | Max. 200 characters | Human-readable name. | 2A.1 |
| status | reg(STATUS_type), one register per data type | 1 | Per data type | Workflow state of this data type (see each section). Distinct from Lifecycle Stage and from verification status. | 2A.1 |
| owner | ref(User) | 1 | User with an active Project Assignment | Exactly one accountable Owner (5A.7). Replaces free-text owner names. On Sub-system and Sub-structure pages the shown owner is derived (5.30). | 5.5, 5A.7 |
| contributors | ref(User) | 0..n | Users with an active Project Assignment | Optional (added in v7.4). | 5A.7 |
| hub | ref(Project) or "FW" | 1 | FW or project id | Framework data versus production data. Production data never sits in FW. | 6.2, 6.10 |
| created_at / created_by | datetime / ref(Person or AI agent) | 1 / 1 | | Set by the software. | 3.12 |
| modified_at / modified_by | datetime / ref(Person or AI agent) | 1 / 1 | | Set by the software. | |
| record_version | int | 1 | 1, 2, 3 ... | Increments on every saved change. Every earlier version is kept unchanged as a frozen copy, referenced as id@record_version (for example IRL-D-0009101@1). Frozen records (Baselines, Review Snapshots, released FDPS Revisions) reference only frozen copies, never live records. Not a revision or an issue (1.6). | 2.6, 6A.15 |
| origin | json | 1 | {kind: reg(ORIGIN_KIND), source_ref, source_issue_or_revision, source_link} | kind is Human, AI, Derived or Imported. A source is required when kind is AI or Imported. | 2H.4, 2H.8 |
| verification_status | reg(VERIFICATION_STATUS) | 1 | Unverified; Verified; Rejected | Only a person may set Verified (0.5). AI-proposed records start Unverified. | 2H.6, 5.5 |
| verified_by / verified_at | ref(Person) / datetime | 1* | | Required when verification_status is Verified. | 2H.6 |
| confidence | decimal | 1* | 0.00 to 1.00 | Required when origin.kind is AI. The band is derived (1.7). | 2H.5 |
| access_marking | reg(ACCESS_MARKING) | 1 | Project classification markings | Enforced for people and for AI queries. | 5.18 |
| last_reviewed_at | date | 0..1 | | Required for Hub Pages (5.5). | 5.5 |
| tags | list of Tag | per type | See 1.3 | Facet tags, with mandatory tags set per type (2F.12). | 2F.2 |

### 1.3 Tags and links as structured sub-records

- Tag: {facet: reg(FACET), option: reg(facet register) or "ALL", origin, confidence, verification_status}. Each tag carries its own provenance, so that AI-proposed tags can be confirmed one at a time (2H.3, 2H.5). "ALL" is a single token meaning every option of the facet (2F.3). It is used only where 2F.12 permits it, and never on items.
- Link (LNK): {id, link_type: reg(LINK_TYPE), source: ref, target: ref, attributes (per link type, for example quantity or effectivity), origin, confidence, verification_status, created_at/by}. All links are held in a single link store (2F.1). Each data-type section lists the links that type owns, meaning the type that is the source of the link and controls it. Unconfirmed links never mark data as verified (2I.5).
- Owned tree links (Part Instance to Build Station and to Sub-system) are links in the link store, constrained to many-to-one (1.6.2).

### 1.4 Units (2A.3, 2A.9)

- Every numeric quantity is stored as qty: {value: decimal, unit: reg(UNIT)}. The UNIT register holds SI units and permitted derived units (for example kg, m, mm, Pa, K, N, h). Non-SI units are permitted only with a recorded rationale and a conversion factor (2A.9).
- The software converts units automatically. Values are stored as entered and compared in SI base units.
- Currency is a qty with unit GBP. Effort is a qty in person-days. Time durations are a qty in days or weeks.

### 1.5 Effectivity structure (eff) (6.7, 6A)

- eff: {effectivity_type: reg(EFFECTIVITY_TYPE), from: int, to: int, notes: text 0..1}. Ranges are inclusive at both ends.
- The upper value 999 means open-ended ("all later effectivities"). It is never allocated as a real effectivity number and is shown as open-ended in every view (6A.12).
- Serial ranges and build standards are entered through named mappings (Effectivity, 3.2), but are always resolved to and stored as effectivity numbers. effectivity_type then records how the range was entered (6A.11).

### 1.6 Revision, issue and record version (6A.6)

- Revision: a controlled change state of a Part Definition, Assembly Definition or FDPS, held as a separate Revision object (Part Revision, Assembly Revision, FDPS Revision). Revision codes are letters A, B, C and so on, omitting I, O, Q, S, X and Z, continuing AA, AB after Y. Work before first release sits in revision A with status In Work.
- Issue: a controlled change state of a document (for example an origin document, review documentation or a calculation document). Issues are held as integers (1, 2, 3) in source and production-link fields.
- Dash numbers are part of the part number and never indicate a revision (6A.6).
- Record version (1.2) is the automatic edit counter that every object carries. It does not replace revision or issue.
- Part Instances and Assembly Instances are positions and have no revisions (6A.6). Their changes are recorded as Change Records (6A.7).

### 1.7 Enumerations and value registers

- Every categorical field references a value register entry (2B.1). Free-text values are never permitted for categorical fields.
- Small fixed enumerations that are part of this schema (for example status values and origin kinds) are also held as value registers, flagged as framework-fixed, so that the software validates all of them in the same way.
- Confidence band (derived): Low if confidence is at most 0.50; Medium if over 0.50 and at most 0.80; High if over 0.80. The bands are exhaustive and do not overlap (2B.4).

### 1.8 General validation

- A record that fails its schema is rejected at entry. A record missing a mandatory tag or link is accepted but flagged Invalid (2A.2, 2F.12).
- Decisions reserved for people (0.5) are enforced in the schema: the fields that record them (approved_by, released_by, decision_by, verified_by, assigned_by) accept only a Person (a User, 3.37), never an AI agent.
- Framework pages, registers and schemas are never edited in a Production Hub. Changes made there are held as Tailoring Records (6.4).

## 2. Value registers (facets and controlled lists)

### 2.1 Fields of a register entry

| Field | Type | Card. | Notes | Ref |
| --- | --- | --- | --- | --- |
| id | string | 1 | VR-REGISTER-NNNN; permanent. | 2A.4 |
| register | reg(REGISTER) | 1 | The register the entry belongs to. | 1.1 |
| code | string | 1 | Short code, unique within the register (for example a System code aligned to ATA iSpec 2200 where an equivalent exists, or a Type code such as BR). | 2A.9, 1.11.5 |
| label | string | 1 | Display name. | |
| definition | text | 1 | Precise description of what the option includes and excludes. | 2B.9 |
| parent | reg(parent register) | 0..1 | Upper-tier entry, for example System to System Group, Sub-system to System, Build Station to Major Unit, Design Sub-team to Design Team. | 1.4, 2B.7 |
| facet_level | int or "cross-cutting" | 1* | For facet registers only. | 2F.8, 2F.9 |
| applies_to_scopes | reg(PRODUCT_SCOPE) | 1..n* | For System entries (2F.11) and Major Unit and Build Station entries. | 2F.11 |
| range | json | 0..1 | {lower, lower_inclusive, upper, upper_inclusive, unit}, for range-based options. Null ends are open-ended. | 2B.4 |
| is_catch_all | bool | 1 | True for precisely defined catch-alls (Final Assembly, General Sub-system). | 1.2.3, 2B.11 |
| is_structural | bool | 1* | For System entries: true for the structural Systems (Airframe System Group). Their Sub-systems are Sub-structures (derived, not stored on the Sub-system entry). | 0.4, 1.6.6, 2B.11, 6C.21 |
| is_bench | bool | 1* | For Build Station entries: true for the Bench Build Station of a Major Unit; false for aircraft Build Stations. | 1.6.1, 2C.12 |
| sequence_no | int | 1* | For Lifecycle Stage entries: 1 to 11, the order of the lifecycle. | 2B.13 |
| in_current_scope | bool | 1* | For Lifecycle Stage entries: true for stages 4 to 6 (Initial System Design to Detailed Design), false for the others until the scope is expanded. | 2B.13 |
| discipline_type | reg(DISC_TYPE) | 1* | For Discipline entries: Sign-off team or Consideration only. | 2B.14 |
| lifecycle_stage | reg(LCS) | 1* | For review stage entries: the aligned Lifecycle Stage (A to 4, B to 5, C to 6). | 6C.1 |
| state | reg(ENTRY_STATE) | 1 | Active; Deprecated; Retired. Deprecated entries remain readable and are flagged for reclassification. | 6.11 |
| replaced_by | reg(same register) | 0..n | For split or merged options. | 6.11 |
| source | string | 1 | Framework vN or Tailoring Record id. | 6.4 |
| sort_order | int | 1 | Display order. | |

Register-level validation: when an entry is added or changed, the register is checked for exhaustiveness (a defined catch-all or full coverage), for non-overlap of definitions and ranges, and for ranges without gaps (2B.2 to 2B.5). Entries are never deleted, only retired.

### 2.2 Register list

| Register (code) | Kind | Facet level | Initial values (source) | Ref |
| --- | --- | --- | --- | --- |
| Product Scope (SCOPE) | Facet | 0 | Aircraft; Ground Equipment; Test Equipment; Facilities (with the boundary definitions of 2B.7). | 2B.7 |
| Major Unit (MU) | Facet | 1 | Front Fuselage; Centre Fuselage; Rear Fuselage; Wings; Fins; Final Assembly (catch-all). For other scopes, the same register holds End Item (Ground and Test Equipment) and Site (Facilities) entries, distinguished by a node_kind attribute. | A.1, 2C.13 |
| Build Station (BS) | Facet (mapping level) | 1 (mapping) | BS1 to BS4 for each of the five structural Major Units; FA1 to FA5 for Final Assembly; one Bench (off-aircraft assembly) per Major Unit, including Final Assembly (2C.12), flagged is_bench. Items directly below an FDPS are Located at aircraft Build Stations; Part Instances of an Assembly Instance at the Bench (1.6.1). Also holds Build Stage and Facility entries for other scopes (node_kind). | A.2, 2C.13 |
| System Group (SG) | Facet tier | 1 (upper tier) | Airframe; Propulsion & Power; Flight & Vehicle Management; Environmental & Safety; Crew Interface; Mission Systems; Test & Instrumentation. | 2B.7 |
| System (SYS) | Facet tier | 1 (lower tier) | The 25 Systems of 2B.7, each with applies_to_scopes from A.7. | 2B.7, A.7 |
| Sub-system (SUB) | Facet (mapping level) | 1 (mapping) | Annex A.3, plus one General Sub-system per System (catch-all). Entries whose parent System is_structural are Sub-structures. | A.3, 2B.11 |
| Design Team (DT) | Hub level, controlled list | 1 (Design tree) | Annex A.4: six teams. Not a facet tag on items (2B.8). | A.4, 2B.8 |
| Design Sub-team (DST) | Hub level, controlled list | 2 (Design tree) | Annex A.4 Sub-teams, each with a parent Design Team. | A.4 |
| Lifecycle Stage (LCS) | Facet | cross-cutting | Annex B.1 (framework register, not a placeholder): 1 Opportunity; 2 Concept Development; 3 Architecture/Configuration Design; 4 Initial System Design; 5 Preliminary Design; 6 Detailed Design; 7 Manufacture & Assembly; 8 Qualification; 9 Production; 10 Support & Upgrades; 11 Disposal. VR-LCS-0001 to VR-LCS-0011 in that order. Current scope of the software and Hub: stages 4 to 6 (in_current_scope true), to be expanded later. | 2F.2, 2F.9, 2B.13 |
| Discipline (DISC) | Facet | cross-cutting | Annex B.2 (framework register, not a placeholder): one list, no duplicates, each entry with a discipline_type. VR-DISC-0001 to VR-DISC-0025 in this order: Aerodynamics (Sign-off team); Affordability and Cost (Consideration only); Airworthiness and Certification (Sign-off team); Assembly, Interfaces, Tolerances and Interchangeability (Consideration only); Configuration Management (Sign-off team); Design (Sign-off team); Electrical Systems (Sign-off team); Electro-Magnetic Compatibility (Sign-off team); Environmental Factors (protection treatments, drainage, weather and tank sealing) (Consideration only); Future Upgrades and Obsolescence (Consideration only); Human Factors (Sign-off team); Low Observability (Sign-off team); Maintainability, Reliability and Ground Equipment (Sign-off team); Manufacturing Engineering (Sign-off team); Materials and Processes (Sign-off team); Mechanical Systems (Sign-off team); Model Based Systems Engineering (Digital Thread) (Consideration only); Quality (Sign-off team); Safety (Sign-off team); Segregation, Separation and Survivability (Consideration only); Standard Parts and Supply Chain (Sign-off team); Structural Analysis (Stress) (Sign-off team); System Layout and Integration (Consideration only); Test (Sign-off team); Weight (Sign-off team); and VR-DISC-0026 Fluid Systems (fuel, hydraulics and pneumatics) (Sign-off team), added in v4 and sorted between Environmental Factors and Future Upgrades and Obsolescence (sort_order), so that the identifiers of existing entries are unchanged. 26 entries. Every Discipline is also a design consideration with exactly one Design Consideration record (3.22). A project may mark a Discipline not applicable through a Tailoring Record approved by the Technical Authority for Design (2B.14). | 2F.2, 2B.14, 4.2 |
| Discipline type (DISC_TYPE) | Framework-fixed | none | Sign-off team (agreement required at each review stage it is listed against); Consideration only (checked by the designer). | 2B.14, 6C.19 |
| Source (SRC) | Facet | cross-cutting | Make; Standard Part; Bought-in Equipment. | 2B.7 |
| Design Type (DTY) | Part attribute (not a facet) | none | Annex A.5: 12 values, including Standard Part (VR-DTY-0012, added in v5) for catalogue items. | 1.10, A.5 |
| Safety Classification (SAF) | Part attribute (not a facet) | none | A Catastrophic; B Hazardous; C Major; D Minor; E No safety effect. | 1.10, A.6 |
| Common part Type code (TYC) | Controlled list | none | FS; SL; BR; CL; FT; EC; SP. For common parts designed by the project only; catalogue items are Standard Parts. BI is reserved for bought-in project control numbers and is not a Type code. | 1.11.5, 1.11.11, A.8 |
| Numbering scheme (NUMSCH) | Controlled list | none | Meaningful stem; Common part; Catalogue standard; Bought-in control number (VR-NUMSCH-0004, formerly Supplier controlled): project control number Project letter + BI + four-digit sequence, for example D-BI-0001, stored with the supplier part number. | 1.11.4 to 1.11.11 |
| Dash range (DASH) | Framework-fixed | none | Made part -001 to -399; Assembly -401 to -799; FDPS -801 and above. Odd: left-hand or unhanded; even: right-hand version of the odd number below. | 1.11.7, 1.11.8, B.5 |
| Access role (ACCROLE) | Framework-fixed | none | Admin; Design Lead; Design Authority; Engineer; Viewer. | 5A.2, B.6 |
| Permission (PERM) | Framework-fixed | none | View; Create; Edit; Approve; Release; Administer users; Comment. | 5A.10 |
| User status (USTATUS) | Framework-fixed | none | Active; Suspended; Left. | 5A.1 |
| Role (ROLE) | Framework-fixed | none | Technical Authority for Design (Design Licence Holder); Design Authority; Design Lead; Design Approver; Discipline Lead. | 6C.14, B.4 |
| Agreement position (AGREE) | Framework-fixed | none | Agree; Agree with conditions; Disagree. | 6C.19, 6C.22 |
| Compliance basis (BASIS) | Framework-fixed | none | Direct (Satisfied by to the FDPS or one of its items); Inherited via EDR Sub-system tag, narrowed where the line item has Allocated to links (Requirements); Inherited via Sub-system Design Type, Inherited via Design Type, Inherited via System and Inherited via Discipline (TSMs, one basis per matching route). | 6B.2, 6B.5, 6B.6 |
| Requirement document kind (DOCKIND) | Framework-fixed | none | EDR (Engineering Design Requirements). Extensible. | 6B.1A |
| Line-item state (LISTATE) | Framework-fixed | none | Inherited, not reviewed (derived default, never stored); Kept; Broken; Superseded (auto) (set by the system, added in v7.2, 6B.7A). Direct is shown alongside from Satisfied by links. | 6B.7 |
| Embodiment status (EMB) | Reserved (section 7) | none | Not in current scope: Planned; Embodied; Not embodied, for Future Development. | 7.1 |
| Checklist follow-up (CKFU) | Framework-fixed | none | Action; Risk; Approved justification. | 4.5 |
| Item Property (PROP) | Part attribute | none | Initial values from 4.1: Mechanical; Flexible; Kinematic; plus Fastener (VR-PROP-0004), which marks Parts whose Part Instances require a Secures link (1.6.6, 4.6). Extensible. | 4.1, 4.6, 1.6.6 |
| Link type (LINK_TYPE) | Controlled list | none | Section 4. | 2I.2 |
| Review stage (STAGE) | Controlled list | none | A Initial System Design; B Preliminary; C Detail. Aligned with Lifecycle Stages 4, 5 and 6 respectively. | 6C.1 |
| Escalation level (ESC) | Controlled list | none | 1 to 5, each with its forum: 1 to 2 Engineer (Issue owner); 3 Team Leader; 4 Chief Engineer; 5 Programme Board. | 2E.9 |
| Impact criterion (IMPACT) | Controlled list | none | Effort; Cost; Schedule; Safety or certification; Scope, with score bands 1 to 5. Effort and cost thresholds are tailorable per Project (3.1). | 2E.8 |
| Effectivity type (EFFTYPE) | Controlled list | none | Effectivity Number (primary); Serial Range; Build Standard. | 6A.11 |
| Finish category (FINCAT) | Controlled list | none | Paint; Primer; Surface Treatment; Sealant; Adhesive (from the examples in 2D.6). Extensible. | 2D.6 |
| Page type (PAGETYPE) | Controlled list | none | Lifecycle Stage; Major Unit; Build Station; Design Team; Design Sub-team; FDPS; System Group; System; Sub-system; Discipline (the page of each Discipline is its Design Consideration record, 3.22); Skill; Trait; Topic; Lesson Learned; EDR; TSM (added in v7: every EDR and TSM has its own page, 5.22). There is no separate Design Consideration page type, so that considerations are not a second list. | 5.2, 4.2 |
| Skill (SKILL), Trait (TRAIT) | Linked registers (not facets) | none | Not listed in v23; to be populated. | 2F.2 |
| Master system (MASTER) | Controlled list | none | PLM; CAD; Released Documents; Analysis Tool; Hub. Named systems to be confirmed (v23 remaining decision 3). | 2J.3 |
| Origin kind (ORIGIN_KIND) | Framework-fixed | none | Human; AI; Derived; Imported. | 2H.4, 3.6 |
| Verification status (VERIFICATION_STATUS) | Framework-fixed | none | Unverified; Verified; Rejected. | 2H.6 |
| Change type (CHG) | Controlled list | none | Link change; FDPS transfer; FDPS ownership change; Up-revision; New part number; Effectivity change; Improvement after review; Population change; Interface change; Lead Sub-system change (R-15); Access change (5A.8); Other. A Change Record may carry several. | 6A.7, 1.7.6, 6C.17 |
| Requirement level (REQLVL) | Controlled list | none | Air System; System; Sub-system; Item (Aircraft scope). Other scopes to be defined. | 2C.7 |
| Verification method (VMETH) | Controlled list | none | Annex B.3 (framework register, not a placeholder), VR-VMETH-0001 to VR-VMETH-0010 in this order: Analogy; Design Review; Calculation Analysis; Safety Assessment; Laboratory/Bench/Rig Tests; Product Ground Tests; Flight Tests; Design Inspection; Simulation; Equipment Qualification. | 2.5, 2B.15 |
| Unit (UNIT) | Controlled list | none | SI units and approved derived units. | 2A.3 |
| Access marking (ACCESS_MARKING) | Controlled list | none | Set per project. | 5.18 |

## 3. Data types

Each data type also carries the common fields of 1.2. Status values listed against a type form that type's STATUS register.

### 3.1 Project

Purpose: identifies one project and its Production Hub, and holds the project-level settings that the framework allows each project to tailor.

| Field | Type | Card. | Values / register | Notes | Ref |
| --- | --- | --- | --- | --- | --- |
| project_letter | string | 1 | One capital letter, e.g. D | First character of part and FDPS numbers. Unique. | 1.11.2 |
| name | string | 1 | | Fictional in all examples. | |
| framework_version | ref(Framework Version) | 1 | | The framework version the Production Hub currently uses. | 6.4, 6.9 |
| effectivity_max | int | 1 | Less than 999 | Highest effectivity number that may be allocated. | 6A.12 |
| default_existence | eff | 1 | Default 1 to 999 | Default existence range for new instances. | 6A.8 |
| impact_thresholds | json | 1 | {effort: 4 boundaries in person-days, cost: 4 boundaries in GBP} | Tailorable thresholds for criteria 1 to 5. Defaults to the 2E.8 values. | 2E.8 |
| retention_policy | string | 1 | | Records retention policy for AI logs and records. | 5.19 |
| ai_index_id | string | 0..1 | | Isolated AI index for this Hub. | 5.18 |
| status | reg | 1 | Set up; Active; Closed | | |

Owned links: none.

Derived: current master of each data type (from the latest Authority Register Entries); list of baselines; Disciplines marked not applicable to the project (from approved Tailoring Records, 2B.14).

Validation: project_letter unique across all projects; effectivity_max is below 999; each impact threshold set has ascending, gap-free boundaries (2B.4).

Example:

```json
{"id":"PRJ-D-0000001","type":"Project","title":"Project D","project_letter":"D","framework_version":"FV-FW-0000003","effectivity_max":120,"default_existence":{"effectivity_type":"VR-EFFTYPE-0001","from":1,"to":999},"impact_thresholds":{"effort_person_days":[1,5,20,60],"cost_gbp":[5000,50000,250000,1000000]},"status":"Active"}
```

### 3.2 Effectivity

Purpose: one allocated product effectivity number for a project, and the named mappings (serial ranges and build standards) that resolve to effectivity numbers.

| Field | Type | Card. | Values / register | Notes | Ref |
| --- | --- | --- | --- | --- | --- |
| project | ref(Project) | 1 | | | 6A.1 |
| kind | reg | 1 | Effectivity Number; Serial Range Mapping; Build Standard Mapping | | 6A.11 |
| number | int | 1* | 1 to effectivity_max | Required for Effectivity Number. Never 999. | 6A.12 |
| serial | string | 0..1 | | Manufacturer serial of the product unit, if allocated. | 6A.11 |
| mapping_name | string | 1* | e.g. "Initial release standard" | For mappings. | 6A.11 |
| maps_to | eff | 1* | | Effectivity number range that the mapping resolves to. | 6A.11 |
| status | reg | 1 | Planned; Allocated; Built; Retired | | |

Owned links: none.

Derived: the FDPS revisions effective at this number and their latest release baselines (6A.10); for mappings, the list of effectivity numbers covered.

Validation: numbers are unique per project; serials are unique per project; a Serial Range Mapping resolves only to allocated numbers; mappings of the same kind do not overlap unless they are explicitly marked as alternative names.

Example:

```json
{"id":"EFF-D-0000010","type":"Effectivity","project":"PRJ-D-0000001","kind":"Build Standard Mapping","mapping_name":"Initial release standard","maps_to":{"effectivity_type":"VR-EFFTYPE-0001","from":1,"to":2},"status":"Allocated"}
```

### 3.3 Part Definition

Purpose: the standardised design of a part, defined once, carrying its part number and attributes (2D.1). It has no tree links (2D.2).

| Field | Type | Card. | Values / register | Notes | Ref |
| --- | --- | --- | --- | --- | --- |
| part_number | string | 1 | Unique across parts, assemblies and FDPSs within the project; never reused | The accepted number. For Catalogue standard, the catalogue number or designation; for Bought-in control number, the project control number (for example D-BI-0001). | 1.11.6, 1.11.10, 1.11.11 |
| numbering_scheme | reg(NUMSCH) | 1 | Meaningful stem; Common part; Catalogue standard; Bought-in control number | | 1.11.3 to 1.11.11 |
| stem / dash | string / string | 1* | e.g. D2822002 / 001 | Required for Meaningful stem. The stem takes the Project, System, Sub-system and Major Unit codes of the FDPS the part is designed for, with its own sequence; the part's own home is held only in its instances' facet links. dash must lie in the made-part range of DASH. | 1.11.4, 1.11.7 |
| handedness | reg | 1* | Unhanded; Left-hand; Right-hand | Required for Meaningful stem. Odd dash for Unhanded or Left-hand; even dash (odd + 1) for Right-hand. | 1.11.8 |
| number_proposal | json | 1 | {proposed_number, proposed_by: software or Person, proposed_at, accepted_by: Person, accepted_at, rejected: [{number, proposed_by, reason}]} | The software-proposed number is kept alongside the accepted number. | 1.11.6 |
| type_code | reg(TYC) | 1* | | Required when the scheme is Common part (project-designed common parts only). | 1.11.5 |
| standard_designation | string | 1* | | Required when the scheme is Catalogue standard. | 1.11.5 |
| supplier_part_number / supplier_mod_standard | string / string | 1* / 0..1 | | Required when the scheme is Bought-in control number, stored with the project control number. | 1.11.11 |
| source | reg(SRC) | 1 | Make; Standard Part; Bought-in Equipment | Mandatory tag. | 2F.12 |
| design_type | reg(DTY) | 1 | | Standard Part if the Source is Standard Part; Bought-in Equipment if the Source is Bought-in Equipment, and for a modified bought-in Part. | 1.10, 2B.7, 2B.10 |
| modification_design_type | reg(DTY) | 1* | | Required for a modified bought-in Part (Derived from link): the Design Type of the modification. Its TSMs are inherited in addition to those of Bought-in Equipment. | 2B.10, 6B.5 |
| safety_classification | reg(SAF) | 1 | A to E | Assigned by a person only. The highest classification required by any use. | 1.10.2, 0.5 |
| safety_assigned_by | ref(Person) | 1 | | | 0.5 |
| safety_basis | text | 0..1 | | The use that sets the classification, where it is set by a use elsewhere. | 1.10.2 |
| lifecycle_stage | reg(LCS) | 1 | One option | Mandatory tag. | 2F.12 |
| item_properties | reg(PROP) | 0..n | | Design properties used to filter considerations. Fastener marks a Part whose Part Instances require exactly one Secures link. | 4.6, 1.6.6 |
| design_tables | json | 0..n | {variant_name, parameter values} | Each variant used on the product is a distinct revision or part number. | 3.10 |
| status | reg | 1 | Active; Obsolete | Definition-level state; release is held on Part Revision. | |

Owned links:

| Link type | Target | Card. |
| --- | --- | --- |
| Derived from | Part Definition (bought-in source) | 0..1; required when the part is a modified bought-in item (2B.10) |

Inbound links of note: Instance of (from Part Instance), Finish applied (from Finish Specification), Governs (from TSM, through Design Type; TSMs also reach the FDPS through System and Discipline tags, 6B.5).

Derived: all Part Instances and where each sits, which gives the many-to-many map to FDPSs, Build Stations and Sub-systems (2D.5, 1.9.1); the TSMs it brings to each FDPS through design_type and modification_design_type (6B.5); applicable Design Considerations (4.4); current released revision; highest Safety Classification required by its uses (shown against the stored value).

Validation: part_number unique across parts, assemblies and FDPSs within the project (1.11.10); no field is ever inferred from part_number (1.11.1); for Meaningful stem, the dash lies in the made-part range and its parity matches handedness, and a right-hand dash is used only for the mirror of the odd number below (1.11.8); a non-interchangeable successor keeps the stem and has dash + 2 (1.11.9); design_type always present, and Standard Part exactly when the Source is Standard Part; Bought-in control numbers match Project-BI-nnnn and carry supplier_part_number (1.11.11); a Meaningful stem shares the first five characters (Project, System, Sub-system and Major Unit codes) with the FDPS it was designed for (1.11.4); Source Make with a Derived from link only when the target's Source is Bought-in Equipment, and then design_type is Bought-in Equipment and modification_design_type is present; Common part only with a type_code; catalogue items are Standard Parts with a standard_designation (1.11.5); no direct link to any Major Unit, Build Station, System, Sub-system or FDPS (2D.2); the Safety Classification is flagged if lower than that required by any use (1.10.2).

Example:

```json
{"id":"PD-D-0000231","type":"Part Definition","title":"Fuel feed pipe, tank outlet","part_number":"D2822002-001","numbering_scheme":"VR-NUMSCH-0001","stem":"D2822002","dash":"001","handedness":"Unhanded","number_proposal":{"proposed_number":"D2822002-001","proposed_by":"software","accepted_by":"user:dwagner","rejected":[]},"source":"VR-SRC-0001","design_type":"VR-DTY-0009","safety_classification":"VR-SAF-0003","safety_assigned_by":"user:dwagner","lifecycle_stage":"VR-LCS-0006","item_properties":["VR-PROP-0002"],"status":"Active","origin":{"kind":"Human"},"verification_status":"Verified"}
```

### 3.4 Part Revision

Purpose: one controlled change state of a Part Definition (6A.6). It is the object that Part Instances link to over effectivity ranges.

| Field | Type | Card. | Values / register | Notes | Ref |
| --- | --- | --- | --- | --- | --- |
| part_definition | ref(Part Definition) | 1 | | | 6A.6 |
| revision | string | 1 | A, B, C ... (1.6) | Unique per Part Definition. | 6A.6 |
| previous_revision | ref(Part Revision) | 0..1 | | | 6A.5 |
| change_record | ref(Change Record) | 1* | | Required from the second revision onwards. Holds the interchangeability assessment. | 6A.9 |
| mass | qty | 0..1 | | | 2A.3 |
| variant_name | string | 0..1 | | Design-table variant that this revision embodies. | 3.10 |
| issuing_master | reg(MASTER) | 1 | PLM or Hub | Who issued the revision. | 6A.13 |
| external_ref | string | 0..1 | | PLM identifier while PLM is master. For a catalogue Standard Part, the issue of the standard or catalogue that this revision follows. | 6A.13, 1.11.5 |
| released_at / released_by | datetime / ref(Person) | 1* | | Required when the status is Released. Person only. | 0.5 |
| status | reg | 1 | In Work; Released; Withdrawn | A released revision stays Released while it is effective at any effectivity; whether it applies at a selected effectivity is shown as Present or Not present (6A.18). | 6A.18 |

Owned links:

| Link type | Target | Card. |
| --- | --- | --- |
| Production link | Production Link (model, drawing) | 0..n |

Derived: the effectivity over which this revision is used (union of its Instance-Revision Links); the Verification records whose basis is this revision.

Validation: the revision code is unique and follows the code sequence; Released requires released_by (a Person); a new revision is permitted only if the Change Record's interchangeability is Interchangeable, otherwise a new part number is required (6A.9); a new issue of a catalogue standard is a new revision of the catalogue Part, with its interchangeability assessment (1.11.5).

Example:

```json
{"id":"PR-D-0000412","type":"Part Revision","title":"D2822002-001 rev B","part_definition":"PD-D-0000231","revision":"B","previous_revision":"PR-D-0000388","change_record":"CR-D-0000077","issuing_master":"VR-MASTER-0001","status":"Released","released_by":"user:dwagner","released_at":"2026-09-14T10:00:00Z"}
```

### 3.5 Part Instance

Purpose: a single occurrence (position) of a Part Definition on the product. It owns exactly two tree links and is never revised (2D.3, 6A.6). A Part Instance directly below the FDPS is Located at an aircraft Build Station; one within an Assembly Instance is Located at the Bench of the Assembly Instance's Major Unit (1.6.1).

| Field | Type | Card. | Values / register | Notes | Ref |
| --- | --- | --- | --- | --- | --- |
| position_name | string | 1 | | Human-readable position, e.g. "Tank 2 feed pipe, left-hand". | 2D.1 |
| existence | eff | 1 | Default from Project | Instance effectivity. | 6A.8 |
| replaces | ref(Part Instance) | 0..1 | | Previous position record when a non-interchangeable change creates a new part number. | 6A.9 |
| status | reg | 1 | Active; Cancelled | Cancelled only for a position never built. A closed existence range does not change the status; whether the instance is present at a selected effectivity is derived (Present, or Not present with the ranges where it exists). | 6A.8, 6A.18 |

Owned links:

| Link type | Target | Card. |
| --- | --- | --- |
| Instance of | Part Definition | 1 |
| Located at | Build Station (register entry): an aircraft Build Station if directly below the FDPS; the Bench of the Assembly Instance's Major Unit if within an Assembly Instance | 1, many-to-one |
| Homed in | Sub-system (register entry); for a fastener, set by the software from its Secures link to the Sub-system of the Part Instance it holds (1.6.6) | 1, many-to-one |
| Secures | Part Instance (the part a fastener holds), in the same FDPS or another FDPS; a cross-FDPS target creates an FDPS interface (3.10) | 1 for a Part Instance of a Part with item property Fastener; otherwise 0 |
| Effective revision | Part Revision, through an Instance-Revision Link (3.6) | 1..n |
| Supports | System (register entry); for a fastener that secures a non-structural part, the System of the part it secures it to; none needed for structure to structure (1.6.6) | 0..n |
| Interface | Part Instance or Assembly Instance in another Product Scope | 0..n |
| Finish applied (override) | Finish Specification, with {mode: Add or Replace, replaces, reason} | 0..n |

Inbound links of note: Contains (from FDPS, exactly one); Assembled from (from Assembly Instance, 0..1); Satisfied by (from Requirement, for traceability only; the Requirement is held by the FDPS, 6B.2); Verified by is owned here as item to Verification (0..n).

Derived (not stored): Major Unit from the Build Station; System and System Group from the Sub-system; Product Scope from the Build Station node; FDPS from FDPS population; Design Sub-team and Design Team through the FDPS; Source, Lifecycle Stage, Design Type and Safety Classification from the Part Definition; effective revision at a given effectivity; status at a selected effectivity (6A.18); Requirements and TSMs, through its FDPS only (6B.1); derived System tags; applicable considerations (section 5).

Validation: exactly one Located at and one Homed in link (1.6.2); Located at is an aircraft Build Station when directly below the FDPS and the Bench of the Assembly Instance's Major Unit when within an Assembly Instance (1.6.1, 2C.12); a fastener has exactly one Secures link and the same Homed in as the held Part Instance, and a Supports link when the held part is not structural (1.6.6); a Part Instance whose Part is not a Fastener has no Secures link (4.6); a held Part Instance in another FDPS is allowed and is flagged to both owning Sub-teams (1.6.6); the home System applies to the Product Scope (2F.11); member of exactly one FDPS, flagged if it belongs to none (1.7.5); it needs no Requirement of its own (2.4); Effective revision links have no overlaps or gaps across the existence range (6A.3); a link change to a released FDPS member requires a Change Record and a new FDPS revision (6A.7); if it is in an Assembly Instance, it is in the same FDPS as that Assembly Instance (1.8.4); no "ALL" tags.

Example:

```json
{"id":"PI-D-0004127","type":"Part Instance","title":"Tank outlet feed pipe","position_name":"Fuel feed pipe, tank outlet to shut-off valve","existence":{"effectivity_type":"VR-EFFTYPE-0001","from":1,"to":999},"links":[{"link_type":"Instance of","target":"PD-D-0000231"},{"link_type":"Located at","target":"VR-BS-0006"},{"link_type":"Homed in","target":"VR-SUB-0032"}],"status":"Active"}
```

### 3.6 Instance-Revision Link

Purpose: the link from an instance (Part Instance or Assembly Instance) to one revision of its definition, carrying the effectivity range over which that revision applies (6A.2, 6A.14). It is a first-class object because it carries data and history.

| Field | Type | Card. | Values / register | Notes | Ref |
| --- | --- | --- | --- | --- | --- |
| instance | ref(Part Instance or Assembly Instance) | 1 | | | 6A.2 |
| revision | ref(Part Revision or Assembly Revision) | 1 | | Must be a revision of the instance's definition. | 6A.2 |
| effectivity | eff | 1 | | Open-ended ranges use 999. | 6A.12 |
| change_record | ref(Change Record) | 1* | | Required when the link closes or opens a range after the first. | 6A.5 |
| set_by_master | reg(MASTER) | 1 | PLM or Hub | Reflects PLM until configuration moves (2J.6). | 6.7, 6A.13 |
| status | reg | 1 | Open-ended; Closed range | Closed range means the range has an upper bound; the link stays in force within its range (6A.18). | 6A.18 |

Owned links: none (it is itself the link).

Derived: whether it is open-ended (to = 999).

Validation: within one instance, ranges do not overlap and together cover the instance's existence range with no gaps (6A.3); the effectivity lies within existence; an up-revision closes the current range (replacing 999 with the last number) and opens a new range in one transaction (6A.5, 6A.12); closing a range saves a new record_version, and the earlier version stays as a frozen copy for the baselines that reference it (6A.15); the revision belongs to the definition named by Instance of.

Example (6A.4):

```json
[{"id":"IRL-D-0009001","type":"Instance-Revision Link","instance":"PI-D-0004127","revision":"PR-D-0000388","effectivity":{"effectivity_type":"VR-EFFTYPE-0001","from":1,"to":2},"record_version":2,"status":"Closed range"},
 {"id":"IRL-D-0009002","type":"Instance-Revision Link","instance":"PI-D-0004127","revision":"PR-D-0000412","effectivity":{"effectivity_type":"VR-EFFTYPE-0001","from":3,"to":999},"change_record":"CR-D-0000077","status":"Open-ended"}]
```

### 3.7 Assembly Definition

Purpose: the definition of an assembly built off-aircraft, defined once with its component Part Definitions and quantities (1.8.3).

| Field | Type | Card. | Values / register | Notes | Ref |
| --- | --- | --- | --- | --- | --- |
| part_number | string | 1 | Same rules as Part Definition | Unique across parts, assemblies and FDPSs within the project. | 1.8.3, 1.11.10 |
| numbering_scheme | reg(NUMSCH) | 1 | Normally Meaningful stem | | 1.11.12 |
| stem / dash / handedness | string / string / reg | 1* | dash in the assembly range -401 to -799 | The stem takes the stem codes of the FDPS (1.11.4) and may be shared with its main component (for example bracket -001, assembly -401). | 1.11.4, 1.11.7, 1.11.10 |
| number_proposal | json | 1 | As for Part Definition | | 1.11.6 |
| safety_classification | reg(SAF) | 1 | | Assigned by a person; at least the highest classification of its components. | 1.10.2 |
| lifecycle_stage | reg(LCS) | 1 | | Mandatory tag. | 2F.12 |
| off_aircraft_statement | text | 1 | | Confirms that the parts are built off-aircraft. | 1.8.1 |
| status | reg | 1 | Active; Obsolete | | |

Owned links:

| Link type | Target | Card. |
| --- | --- | --- |
| Comprises | Part Definition, with attribute quantity (int, at least 1) | 1..n |

Derived: Assembly Instances and their FDPSs (many-to-many, 1.8.4); Design Types and Safety Classifications of the components (highest classification shown).

Validation: at least one component; no direct link to an FDPS (1.8.4); a component change flags the Assembly Definition; numbering as for Part Definition, with the dash in the assembly range.

Example:

```json
{"id":"AD-D-0000044","type":"Assembly Definition","title":"Bracket with pressed bearing","part_number":"D5111005-401","numbering_scheme":"VR-NUMSCH-0001","stem":"D5111005","dash":"401","handedness":"Unhanded","lifecycle_stage":"VR-LCS-0006","off_aircraft_statement":"Bearing pressed into bracket at bench before installation","links":[{"link_type":"Comprises","target":"PD-D-0000301","attributes":{"quantity":1}},{"link_type":"Comprises","target":"PD-D-0000302","attributes":{"quantity":1}}],"status":"Active"}
```

### 3.8 Assembly Revision (added)

Purpose: one controlled change state of an Assembly Definition. It is the target of Assembly Instance revision links (6A.6, 6A.14). The fields are the same as Part Revision (3.4), with assembly_definition in place of part_definition, and with a component_revisions json listing the component Part Revisions where these are fixed.

Validation: as for Part Revision.

Example:

```json
{"id":"AV-D-0000051","type":"Assembly Revision","assembly_definition":"AD-D-0000044","revision":"A","issuing_master":"PLM","status":"Released","released_by":"user:dwagner"}
```

### 3.9 Assembly Instance

Purpose: a single occurrence of an Assembly Definition on the product, belonging to exactly one FDPS (1.8.3, 1.8.4).

| Field | Type | Card. | Values / register | Notes | Ref |
| --- | --- | --- | --- | --- | --- |
| position_name | string | 1 | | | 1.8.3 |
| existence | eff | 1 | Default from Project | | 6A.14 |
| status | reg | 1 | Active; Cancelled | As for Part Instance (6A.18). | |

Owned links:

| Link type | Target | Card. |
| --- | --- | --- |
| Instance of | Assembly Definition | 1 |
| Located at | Build Station (aircraft Build Station where the assembly is installed; never a Bench) | 1, many-to-one |
| Assembled from | Part Instance | 1..n |
| Effective revision | Assembly Revision, through an Instance-Revision Link | 1..n |
| Interface | item in another Product Scope | 0..n |
| Verified by | Verification | 0..n |

Derived: Major Unit from its Build Station (1.6.1); derived System tags from its Part Instances' home Systems, shown with a derived badge (2F.7); FDPS from FDPS population.

Validation: exactly one Located at link, to an aircraft Build Station, and every Part Instance Assembled from is Located at the Bench of the same Major Unit (1.6.1, 2C.12); exactly one FDPS, and all its Part Instances are in the same FDPS (1.8.4); its Part Instances correspond in Part Definition and quantity to the Comprises links of the definition; revision-link ranges have no gaps or overlaps (6A.14); it needs no Requirement of its own, because it reaches its Requirements through its FDPS (2.4, 6B.1).

Example:

```json
{"id":"AI-D-0000210","type":"Assembly Instance","title":"Pump bracket assembly, frame 14 LH","position_name":"Pump bracket assembly, frame 14 left-hand","existence":{"effectivity_type":"VR-EFFTYPE-0001","from":1,"to":999},"links":[{"link_type":"Instance of","target":"AD-D-0000044"},{"link_type":"Located at","target":"VR-BS-0006"},{"link_type":"Assembled from","target":"PI-D-0004501"},{"link_type":"Assembled from","target":"PI-D-0004502"}],"status":"Active"}
```

### 3.10 FDPS

Purpose: a released installation design package of Part Instances (and Assembly Instances) owned by one Design Sub-team, independent of Major Unit and System (1.7).

| Field | Type | Card. | Values / register | Notes | Ref |
| --- | --- | --- | --- | --- | --- |
| fdps_number | string | 1 | Meaningful stem, e.g. D2822001-801; dash in the FDPS range | Fixed at allocation and never changed if links change. Unique across parts, assemblies and FDPSs. | 1.11.4, 1.11.7, 1.11.10 |
| number_proposal | json | 1 | As for Part Definition | | 1.11.6 |
| stem_breakdown | json | 1 | {project, system_code, subsystem_code, major_unit_code, sequence, dash} | Informational only; never used for inference. | 1.11.1 |
| owning_sub_team | reg(DST) | 1 | | Mandatory. A change of owner requires a Change Record approved by both Design Team leads. | 1.7.6 |
| lead_sub_system | reg(SUB) | 1 | A Sub-system or Sub-structure | Chosen at creation; changed only by a Change Record. Sets the Design Lead who approves interface breaks and whether the FDPS is a Sub-structure FDPS (parent System is_structural). At least one member Part Instance is homed in it once populated. Not inferred from fdps_number. | 1.7.7, 6C.21 |
| lead_sub_system_approval | json | 1 | {set_by: Person in the owning Design Sub-team, set_at, approved_by: a Design Lead whose area is lead_sub_system at approved_at, approved_at, change_record: Change Record of type Lead Sub-system change when changed after creation} | R-15. A change re-runs interface inheritance and flags existing interface breaks and EDR line-item breaks for re-confirmation. | 1.7.7A |
| interface_breaks | json | 0..n | {system: reg(SYS), reason, by: Person (author), at, approved_by: Person (a Design Lead whose area is lead_sub_system), approved_at, reconfirm_required: bool} | Inherited interfacing Systems that do not apply to this FDPS. Never deletes the inheritance. | 6C.21, 6C.14 |
| lifecycle_stage | reg(LCS) | 1 | | Mandatory tag. | 2F.12 |
| status | reg | 1 | Open; In Review; Released; Withdrawn | | |

Owned links:

| Link type | Target | Card. |
| --- | --- | --- |
| Contains | Part Instance | 0..n (each Part Instance in exactly one FDPS) |
| Contains | Assembly Instance | 0..n |
| Describes (inbound) | FDPS Hub Page | 0..1 |

Derived: Systems and System Groups, and Major Units, from its Part Instances (1.7.3); interfacing Systems: the interface lists of the Sub-system pages of its Part Instances' non-structural Sub-systems, plus, for a Sub-structure FDPS, the interface lists of the Sub-structure pages of every Sub-structure in which its Part Instances are homed, plus the Supports-link Systems of its items, less its own home Systems and interface_breaks; a non-structural FDPS never inherits a Sub-structure page list (6C.21); FDPS interfaces: the other FDPSs reached by Secures links from or to its Part Instances, with the fastener and held Part Instance of each (6C.24); its break approver, the Design Lead of lead_sub_system in the Role register (6C.14); Design Team through the Sub-team; review stage status (highest stage passed, from Design Reviews, with carry-forward, 6C.12); inherited Requirements, from every System tree node at or above its Part Instances' Sub-systems (6B.2), plus direct Satisfied by links; inherited TSMs: every TSM with at least one matching tag (Design Type of a Part or Assembly in it, including modification Design Types and Standard Part; System of a home Sub-system of its Part Instances; Discipline listed by the owning Design Team), with one basis per matching tag (6B.5); applicable checklist items, from the Sub-team stage page less project-N/A Disciplines (4.4); effective FDPS Revision at a given effectivity.

Validation: exactly one owning Sub-team; exactly one lead_sub_system, in which at least one member Part Instance is homed (1.7.7); every interface break approved, with a reason, by a person holding a Design Lead role whose area is lead_sub_system at the date of approval (6C.21); at least one Requirement, inherited or direct (2.4); every Part's Design Type is on the owning Design Team's list (6B.5); every inherited Requirement and TSM has Compliance Statements covering the effectivity of its released revisions (6B.8); only members of the owning Sub-team add or remove members (1.7.6); a second FDPS membership for the same instance is rejected (1.7.5); a transfer between FDPSs needs a Change Record agreed by both Sub-teams (1.7.6); a population change while Released requires a new FDPS Revision (6A.7).

Example:

```json
{"id":"FD-D-0000017","type":"FDPS","title":"Centre fuselage fuel feed installation","fdps_number":"D2822001-801","stem_breakdown":{"project":"D","system_code":"28","subsystem_code":"2","major_unit_code":"2","sequence":"001","dash":"801"},"owning_sub_team":"VR-DST-0007","lead_sub_system":"VR-SUB-0032","lifecycle_stage":"VR-LCS-0006","status":"Open"}
```

### 3.11 FDPS Revision

Purpose: one controlled change state of an FDPS, freezing its population and the revisions it releases (6A.6, 6A.11).

| Field | Type | Card. | Values / register | Notes | Ref |
| --- | --- | --- | --- | --- | --- |
| fdps | ref(FDPS) | 1 | | | 6A.6 |
| revision | string | 1 | A, B ... | | 6A.6 |
| population | json | 1* | List of {instance, irl: id@record_version} | Frozen at release, as references to frozen copies; working list while In Work. | 6A.10, 6A.15 |
| effectivity | eff | 1* | | Set at release: the range over which its exact content applies. Releasing the next revision closes this range (to = first effectivity of the next revision - 1). | 6A.11 |
| baselines | ref(Baseline) | 0..n | | Baselines of this revision, numbered 1, 2, 3 ... (review snapshots and release). | 6A.10 |
| carried_forward_review | json | 0..1 | {review: ref(Design Review), assessed_by: Person (Design Authority), at, rationale} | Records that a C pass carries forward to this revision. | 6C.12 |
| change_record | ref(Change Record) | 1* | | From the second revision onwards. | 6A.7 |
| passed_reviews | ref(Design Review) | 0..n | | | 6C.11 |
| release_assessment | json | 1* | {assessed_by: Person (Design Authority), at, against_snapshot: ref(Review Snapshot), change_records: [ref(Change Record)], substantial: bool (true if any Change Record's assessment for this FDPS is substantial), rationale} | Required at release. Rolls up the per-FDPS assessments of the Change Records (3.28). | 6C.12, 6C.17 |
| gate_confirmation | json | 1* | {confirmed_by: Hub, at, open_actions: [], non_compliant_statements: []} | Hub confirmation that the release gate is met, obtained by the PLM release workflow while PLM issues releases. | 6C.11, 6A.13 |
| released_at / released_by | datetime / ref(Person) | 1* | | Person only. | 0.5, 6C.14 |
| status | reg | 1 | In Work; Submitted; Released; Superseded | | |

Owned links: Production link to release documentation (0..n).

Derived: Systems and interfacing Systems at release (also frozen in Baselines).

Validation: Submitted requires a passed C review (direct or carried forward) and every Action raised at any review covering any revision of the FDPS closed, with closure accepted, a Cancelled Action counting only with a reason and the chair's approval (6C.11), and no Compliance Statement of the FDPS Non-compliant at any effectivity of the revision's range (6A.17); if release_assessment.substantial is true, a re-review is required before release (6C.12); the released revisions of the FDPS have effectivity ranges that neither overlap nor leave gaps, and the configuration is the same at every effectivity in each range (6A.11); a release issued by PLM without gate_confirmation is flagged as a discrepancy (6C.11); released records are read-only.

Example:

```json
{"id":"FR-D-0000033","type":"FDPS Revision","fdps":"FD-D-0000017","revision":"B","population":[{"instance":"PI-D-0004127","irl":"IRL-D-0009002@1"}],"effectivity":{"effectivity_type":"VR-EFFTYPE-0001","from":3,"to":999},"change_record":"CR-D-0000077","passed_reviews":["DR-D-0000009"],"carried_forward_review":{"review":"DR-D-0000009","assessed_by":"user:da_fuel","at":"2026-09-14","rationale":"No substantial change since RS-D-0000009"},"release_assessment":{"assessed_by":"user:da_fuel","against_snapshot":"RS-D-0000009","change_records":["CR-D-0000077"],"substantial":false,"rationale":"Wall thickness increase restores margin"},"status":"Released"}
```

### 3.12 Finish Specification

Purpose: a coating, sealant or treatment, recorded once and linked to the parts it is applied to (2D.6, 2D.7).

| Field | Type | Card. | Values / register | Notes | Ref |
| --- | --- | --- | --- | --- | --- |
| finish_code | string | 1 | Unique within the hub | | 2D.6 |
| category | reg(FINCAT) | 1 | | | 2D.6 |
| discipline | reg(DISC) | 1 | | Mandatory tag. | 2F.12 |
| specification | text | 1 | Structured description | Process, thickness, cure and similar, with values as qty where numeric. | 2A.3 |
| properties | json | 0..n | {name, qty} | | 2A.3 |
| status | reg | 1 | Draft; Released; Superseded | | |

Owned links:

| Link type | Target | Card. |
| --- | --- | --- |
| Finish applied | Part Definition | 0..n (at least one link or one instance override once in use) |

Instance overrides are owned by the Part Instance (3.5).

Derived: effective finishes for a Part Instance (definition finishes, with overrides applied); usage count.

Validation: once Released and in use, at least one Finish applied link to a Part Definition or at least one instance override referencing it; a finish used only through overrides is valid (2D.7); an override with mode Replace names the finish it replaces, and every override has a reason.

Example:

```json
{"id":"FS-D-0000008","type":"Finish Specification","title":"Fuel-resistant primer","finish_code":"FIN-PR-002","category":"VR-FINCAT-0002","discipline":"VR-DISC-0015","specification":"Two coats, 15 to 25 micrometre dry film each","status":"Released"}
```

### 3.13 Requirement

Purpose: a structured requirement record and the root of the data structure (2.3). It keeps its own functional breakdown (2C.7).

| Field | Type | Card. | Values / register | Notes | Ref |
| --- | --- | --- | --- | --- | --- |
| req_number | string | 1 | Unique within the hub | Business identifier. | 2A.4 |
| statement | text | 1 | One "shall" statement | Atomic: one requirement per record. | 0.3 |
| rationale | text | 0..1 | | | |
| level | reg(REQLVL) | 1 | | Kept on each line item; one EDR may mix levels. | 2C.7, 6B.1A |
| line_item_revision | int | 1 | 1, 2, 3 ... | Revision of this line item; a new EDR issue raises it only for changed line items, and only those are re-flagged. | 6B.10 |
| criteria | json | 0..n | {quantity_name, comparator, limit: qty} | Machine-checkable limits that feed Parameter constraints. | 3.9, 2A.3 |
| verification_method | reg(VMETH) | 0..n | | | 2.5 |
| product_scope | reg(SCOPE) | 1..n | | Mandatory tag. | 2F.12 |
| lifecycle_stage | reg(LCS) or ALL | 1..n | | Mandatory tag. | 2F.12 |
| discipline | reg(DISC) or ALL | 1..n | | Mandatory tag. | 2F.12 |
| acceptance | json | 1* | {state: Proposed, Accepted, Rejected; accepted_by: Person; accepted_at} | Acceptance of a Requirement or of a Requirement change is by a person only. | 0.5 |
| status | reg | 1 | Draft; Accepted; Superseded; Withdrawn | | |

Owned links:

| Link type | Target | Card. |
| --- | --- | --- |
| Part of | Requirement Document (EDR) | 1 |
| Allocated to | System tree node: Sub-system, System or System Group (register entry): optional narrowing of the EDR Sub-system tag | 0..n |
| Decomposes into | Requirement (lower level) | 0..n |
| Satisfied by | FDPS, or Part Instance or Assembly Instance for traceability (direct) | 0..n |
| Constrains | Parameter | 0..n |

Derived: inheriting FDPSs, which are all FDPSs with at least one Part Instance homed in a Sub-system tagged on its EDR, narrowed, where the line item has Allocated to links, to those with a Part Instance homed at or below an allocated node (6B.2), plus the FDPSs of directly linked items; the Line-item Review state per inheriting FDPS (3.15A); these form the compliance set (6B.3); coverage, meaning FDPSs, their Compliance Statements by effectivity range, and Verifications (2.8); parent Requirement.

Validation: exactly one Part of link to an EDR (6B.1A); any Allocated to node is at or above at least one Sub-system tagged on its EDR, and each Product Scope option is one the Allocated to nodes, or the EDR's Sub-systems, apply to; Decomposes into has no cycles and points to the same or a lower level; a change raises flags down Decomposes into and to the Compliance Statements of every inheriting or directly linked FDPS (2.6, 6B.10); changes to an Accepted Requirement re-enter Proposed until accepted.

Example:

```json
{"id":"REQ-D-0000140","type":"Requirement","title":"Usable fuel, tank 2","req_number":"D-FUE-STO-012","statement":"Tank 2 shall provide usable fuel of not less than 450 kg.","level":"VR-REQLVL-0003","criteria":[{"quantity_name":"usable_fuel_mass","comparator":">=","limit":{"value":450,"unit":"kg"}}],"product_scope":["VR-SCOPE-0001"],"lifecycle_stage":["ALL"],"discipline":["VR-DISC-0026"],"acceptance":{"state":"Accepted","accepted_by":"user:dwagner"},"line_item_revision":1,"links":[{"link_type":"Part of","target":"RD-D-0000001"},{"link_type":"Allocated to","target":"VR-SUB-0031"}],"status":"Accepted"}
```

### 3.13A Requirement Document (added in v7)

Purpose: a document grouping requirement line items. The only kind now is EDR (Engineering Design Requirements). An EDR is tagged at document level to Sub-systems, so that work can be linked before it is fully defined; FDPSs inherit all of its line items by default and break those that do not apply (6B.1A, 6B.2, 6B.7).

| Field | Type | Card. | Values / register | Notes | Ref |
| --- | --- | --- | --- | --- | --- |
| doc_kind | reg(DOCKIND) | 1 | EDR | | 6B.1A |
| doc_code | string | 1 | e.g. EDR-FUE | Unique within the project. | 6B.1A |
| issue | int | 1 | 1, 2, 3 ... | Issue of the document; each issue records which line items changed. | 6A.6, 6B.10 |
| sub_system_tags | reg(SUB) | 1..n | Sub-systems or Sub-structures | Many-to-many document-level tag. Intended to follow one System, but may span several. | 6B.2 |
| issue_changes | json | 0..n | [{issue, changed: [ref(Requirement)], added: [...], removed: [...]}] | Drives re-flagging of changed line items only. | 6B.10 |
| product_scope | reg(SCOPE) | 1..n | | Mandatory tag. | 2F.12 |
| acceptance | json | 1* | As for Requirement | | 0.5 |
| status | reg | 1 | Draft; Released; Superseded; Withdrawn | | |

Owned links: Tagged to, to Sub-system entries (held as sub_system_tags). Line items link to it by Part of (3.13).

Derived: line items (inbound Part of); inheriting FDPSs (every FDPS with a Part Instance homed in a tagged Sub-system); per FDPS, counts of Kept, Broken and unreviewed line items and a compliance summary (5.21, 5.27); its Hub page (5.22).

Validation: at least one line item; at least one Sub-system tag; a new issue lists its changed, added and removed line items, and only those are flagged on inheriting FDPSs (6B.10).

Example (demo data):

```json
{"id":"RD-D-0000001","type":"Requirement Document","title":"Fuel System Engineering Design Requirements","doc_kind":"VR-DOCKIND-0001","doc_code":"EDR-FUE","issue":1,"sub_system_tags":["VR-SUB-0031","VR-SUB-0032","VR-SUB-0043","VR-SUB-0044","VR-SUB-0045","VR-SUB-0046"],"product_scope":["VR-SCOPE-0001"],"status":"Released"}
```

### 3.14 TSM

Purpose: a Technical Standards Manual: a requirement data type holding governing design standards (6B.4). It is a broad document holding many statements, tagged by any of Design Type, Discipline and System, and reaching an FDPS if any tag matches (6B.5, 6B.11). Changed in v5: one record per manual (with its statements), not one record per clause.

| Field | Type | Card. | Values / register | Notes | Ref |
| --- | --- | --- | --- | --- | --- |
| manual_code | string | 1 | e.g. TSM-FLU | Unique within the project or framework. | 6B.4 |
| issue | int | 1 | 1, 2, 3 ... | Issue of the manual. | 6A.6 |
| statements | json | 1..n | [{clause, statement, revision, criteria: as for Requirement, governing_source: {body, standard, clause, issue}}] | clause unique within the manual. Each statement is a line item with its own revision (6B.10). A statement may be Kept for some FDPSs reached and Broken for others (6B.7, 6B.11). | 6B.11, 3.9 |
| acceptance | json | 1* | As for Requirement | | 0.5 |
| status | reg | 1 | Draft; Accepted; Superseded; Withdrawn | | |

Owned links:

| Link type | Target | Card. |
| --- | --- | --- |
| Governs | Design Type, Discipline or System (register entries): the TSM's tags. Never a Sub-system. | 1..n in total; each kind optional (6B.5) |
| Informed by | Lesson Learned | 0..n |
| Constrains | Parameter | 0..n |

Derived: inheriting FDPSs, which are those with at least one matching route: a Part Instance homed in a Sub-system whose page lists a tagged Design Type (Sub-system > Design Type > TSM, added in v7); a Part or Assembly of a tagged Design Type (including a modification Design Type and Standard Part); a Part Instance homed in a Sub-system of a tagged System; or a tagged Discipline listed on the owning Design Team page (6B.5). Tags combine with OR. Compliance status across the inheriting FDPSs.

Validation: at least one Governs link, to Design Type, Discipline or System entries only, never a Sub-system (2F.12, 6B.5); at least one statement; a new issue flags, on every inheriting FDPS, only the statements whose revision changed or that were added or removed (6B.10).

Example:

```json
{"id":"TSM-D-0000065","type":"TSM","title":"Fluid Systems Technical Standards Manual","manual_code":"TSM-FLU","issue":3,"statements":[{"clause":"5.1","statement":"Every component installed in a fuel-wetted or fuel-vapour zone shall be electrically bonded to structure with a resistance of not more than 10 milliohm."},{"clause":"6.2","statement":"Hydraulic components shall be compatible with the hydraulic fluid specification of the project."}],"links":[{"link_type":"Governs","target":"VR-DISC-0026"},{"link_type":"Governs","target":"VR-SYS-0010"},{"link_type":"Governs","target":"VR-SYS-0012"},{"link_type":"Governs","target":"VR-DTY-0009"}],"status":"Accepted"}
```

### 3.15 Compliance Statement (added)

Purpose: records one FDPS's compliance position against one Requirement or TSM over one effectivity range (6B.8). From v7, statements exist only for Kept line items (3.15A); a Requirement whose line item is Broken, or a TSM all of whose statements are Broken, needs no statement, and Not applicable is kept only for records made before v7. This includes approved non-applicability (6B.7, 6C.13), the compliance stated at the C review (6C.15), and known non-compliance of the design, which blocks release for its range (6A.17). Concessions are not in the current scope (section 7). Compliance is never stated per Part Instance.

| Field | Type | Card. | Values / register | Notes | Ref |
| --- | --- | --- | --- | --- | --- |
| fdps | ref(FDPS) | 1 | | | 6B.8 |
| requirement | ref(Requirement or TSM) | 1 | | | 6B.7 |
| effectivity | eff | 1 | | The range over which this position applies. | 6B.8 |
| bases | json | 1..n | [{basis: reg(BASIS), node: reg(SUB, SYS or SG) for System tree inheritance, design_type: reg(DTY), system: reg(SYS) or discipline: reg(DISC) for TSM tags, via: [Part Instance or Part Definition ids, or the Design Team page for a Discipline], item: ref for Direct}] | Every route by which the Requirement or TSM reaches the FDPS is recorded; for a TSM, one basis per matching tag. | 6B.5, 6B.6 |
| statements_claimed | json | 1* | [{clause, parts: [ref(Part Definition or Assembly Definition)] 0..n}] | For a TSM with position Compliant or Non-compliant: the statements that apply to the FDPS. parts is optional: when present, the Parts the statement applies to; when absent or empty, the statement is claimed for the FDPS as a whole. Changed in v7: the claimed statements must equal the Kept statements of the TSM for the FDPS (3.15A); every other statement is Broken. | 6B.11 |
| position | reg | 1 | Not yet stated; Compliant; Non-compliant; Not applicable | | 6C.4 |
| evidence | ref(Verification) | 0..n | | For Compliant: their effectivity ranges together cover this statement's range. | 2.5, 6B.9 |
| margin_note | text | 0..1 | | Recorded margin change where a margin has reduced but remains compliant. | 6C.17 |
| issue | ref(Issue) | 1* | | Required for Non-compliant: the Issue that records the non-compliance. No FDPS revision may be released for an effectivity in this range while the position is Non-compliant. | 6A.17, 6C.11 |
| reason | text | 1* | | Required for Non-compliant and Not applicable. | 6B.7 |
| approved_by / approved_at | ref(Person) / datetime | 1* | | Required for Not applicable: for a Requirement, a Design Lead whose area covers every Sub-system through which it reaches the FDPS; for a TSM (only where none of its statements applies), a Design Authority whose area covers the owning Design Team or a Design Type through which it reaches the FDPS. | 6C.13, 6B.11 |
| status | reg | 1 | Open; Approved; Flagged | | |

Owned links: Demonstrated by, which is a reference to Verification held in the evidence field.

Derived: the Part Instances through which it reaches the FDPS (from bases, for display); whether its evidence is current.

Validation: for each FDPS and Requirement or TSM, the ranges of its statements neither overlap nor leave gaps over the effectivity of the FDPS's released revisions (6B.8); one statement per FDPS, Requirement or TSM and range; the bases list every route; evidence Demonstrates the Requirement and is valid over the whole range (6B.9); for a TSM, every claimed statement is demonstrated, at every effectivity, by passing evidence whose basis revisions include every claimed Part present, or, for a statement claimed for the FDPS as a whole, by passing evidence that demonstrates the statement and is valid there (6B.11); a Non-compliant statement references its Issue, and no released FDPS revision's release baseline holds a Non-compliant statement over its range (6A.17, 6C.11); a Not applicable statement never deletes the inheritance (6B.7); the approver holds the required role and area in the Role register at approved_at (6C.13, 6C.14).

Example:

```json
{"id":"CS-D-0001200","type":"Compliance Statement","fdps":"FD-D-0000017","requirement":"TSM-D-0000062","effectivity":{"effectivity_type":"VR-EFFTYPE-0001","from":1,"to":999},"bases":[{"basis":"Inherited via Design Type","design_type":"VR-DTY-0009","via":["PD-D-0000231"]}],"statements_claimed":[{"clause":"3.1.4","parts":["PD-D-0000231"]}],"position":"Compliant","evidence":["VER-D-0000301"],"status":"Approved"}
```

### 3.15A Line-item Review (added in v7)

Purpose: records, for one FDPS, the review of one inherited line item: an EDR Requirement or a TSM statement. Inherited, not reviewed is the derived default and is never stored (6B.7).

| Field | Type | Card. | Values / register | Notes | Ref |
| --- | --- | --- | --- | --- | --- |
| fdps | ref(FDPS) | 1 | | | 6B.7 |
| line_item | json | 1 | {requirement: ref(Requirement)} or {tsm: ref(TSM), clause} | | 6B.7 |
| line_item_revision | int | 1 | | The revision reviewed. A later revision re-flags this record. | 6B.10 |
| state | reg(LISTATE) | 1 | Kept; Broken; Superseded (auto) | Superseded (auto) is set by the system, author 'system', when the document has defined links in the FDPS and this line item has none (P1 to P3). | 6B.7, 6B.7A |
| superseded_by | ref(Link) | 0..n | | Superseded (auto) only: the defined links of the same document in the FDPS that caused the supersession. | 6B.7A |
| bulk_confirmation | ref(TSM Supersession Confirmation) | 0..1 | | TSM statements in Superseded (auto) only; empty means pending. EDR line items need none. | 6B.7A, 6C.13 |
| bases | json | 1..n | As for Compliance Statement bases | The routes at the time of review. | 6B.6 |
| reason | text | 1* | | Required for Broken. | 6B.7 |
| author / approved_by / approved_at | ref(Person) / ref(Person) / datetime | 1* | | Required for Broken: for an EDR line item, a Design Lead whose area is the FDPS's lead Sub-system or lead Sub-structure; for a TSM statement, a Design Authority whose area covers the owning Design Team or a Design Type through which the TSM reaches the FDPS. | 6C.13, 6C.14 |
| status | reg | 1 | Current; Flagged for re-confirmation | | 6B.7 |

Derived: the FDPS maturity indicator (reviewed of total, counting Kept, Broken and Superseded (auto); numbers broken and superseded) (5.27); pending bulk confirmations; whether the FDPS meets the Stage C entry criterion and the release-gate condition of no unreviewed line items (6C.11, 6C.15).

Validation: at most one current record per FDPS and line item; a Broken record has reason, author, approver and date, and the approver holds the required role and area in the Role register at approved_at; no Compliance Statement exists for a Broken or Superseded (auto) line item; Superseded (auto) records are created and removed only by the system (P4, P5); a manual Kept or Broken record is never overwritten by supersession (P3); a record is flagged when the FDPS population, its lead Sub-system, the EDR's Sub-system tags, the Sub-system's Design Types or the line item's revision change.

Example (demo data):

```json
{"id":"LIR-D-0000001","type":"Line-item Review","fdps":"FD-D-0000017","line_item":{"tsm":"TSM-D-0000067","clause":"1.1"},"line_item_revision":1,"state":"Broken","bases":[{"basis":"Inherited via System","system":"VR-SYS-0010"}],"reason":"No item of this FDPS is installed in a designated fire zone.","author":"user:p.hale","approved_by":"user:k.osei","approved_at":"2026-05-08T09:00:00Z","status":"Current"}
```

### 3.15B TSM Supersession Confirmation (added in v7.2)

Purpose: the Design Authority's bulk confirmation of the Superseded (auto) statements of one TSM for one FDPS (6B.7A, 6C.13).

| Field | Type | Card. | Values / register | Notes | Ref |
| --- | --- | --- | --- | --- | --- |
| fdps | ref(FDPS) | 1 | | | 6B.7A |
| tsm | ref(TSM) | 1 | | | 6B.7A |
| statements | json | 1..n | [{clause, revision}] | The full set of Superseded (auto) statements at confirmation (P6). | 6B.7A |
| rejected | json | 0..n | [{clause, reason}] | Statements the Design Authority returns to Inherited, not reviewed (P6). | 6B.7A |
| confirmed_by / confirmed_at | ref(Person) / datetime | 1 | | A Design Authority whose area covers the owning Design Team or a Design Type through which the TSM reaches the FDPS. | 6C.13, 6C.14 |
| status | reg | 1 | Current; Lapsed | Lapses when the set of superseded statements changes (P4 to P6). | 6B.7A |

Validation: at most one Current record per FDPS and TSM; statements equals the current Superseded (auto) set minus rejected; a pending confirmation (Superseded (auto) statements with no Current record) blocks Stage C entry and the release gate.

Example (demo data):

```json
{"id":"TSC-D-0000001","type":"TSM Supersession Confirmation","fdps":"FD-D-0000017","tsm":"TSM-D-0000067","statements":[{"clause":"2.3","revision":1},{"clause":"2.4","revision":1}],"confirmed_by":"user:k.osei","confirmed_at":"2026-10-12T12:00:00Z","status":"Current"}
```

### 3.16 Verification

Purpose: the analysis or other evidence that supports Product data, linked to the items it supports and the Requirements it demonstrates (2.5).

| Field | Type | Card. | Values / register | Notes | Ref |
| --- | --- | --- | --- | --- | --- |
| method | reg(VMETH) | 1 | Annex B.3 of v23 | Mandatory. | 2.5, 2B.15 |
| summary | text | 1 | | | |
| results | json | 0..n | {quantity_name, value: qty, margin: qty} | Structured results, not only a document. | 0.3, 3.11 |
| outcome | reg | 1 | Not run; Pass; Fail; Inconclusive | Fail flags upwards. | 2I.2 |
| basis_revisions | ref(Part Revision, Assembly Revision or FDPS Revision) | 1..n | | The revisions analysed. | 2.7 |
| effectivity | eff | 1 | | The range over which it is valid evidence. At every effectivity in the range, each basis revision is the effective revision of the instances of its definition that exist there. | 6B.9 |
| supersedes | ref(Verification) | 0..n | | The Verification whose range this one closes. | 6B.9 |
| document | json | 0..1 | {source_ref, issue, link} | Calculation document, if any. | 2A.7 |
| discipline | reg(DISC) | 1 | | Mandatory tag. | 2F.12 |
| lifecycle_stage | reg(LCS) | 1 | | Mandatory tag. | 2F.12 |
| status | reg | 1 | Draft; Checked; Approved; Superseded | | |

Owned links:

| Link type | Target | Card. |
| --- | --- | --- |
| Demonstrates | Requirement or TSM, with attribute statements: [clause] when the target is a TSM (6B.11); for a statement claimed for the FDPS as a whole, the Verification covers the installation and its basis revisions are those inspected | 1..n |

Inbound: Verified by (from item, at least one); Drives (from Parameter).

Derived: whether it is current over its range; open flags against it.

Validation: at least one item and at least one Requirement (2F.12); the effectivity range is consistent with the basis revisions (6B.9); it does not overlap the range of a Verification it supersedes for the same FDPS and Requirement; a change, or a change of outcome to Fail, flags the linked items, Requirements and Compliance Statements (2I.2, 6B.10).

Example:

```json
{"id":"VER-D-0000301","type":"Verification","title":"Feed pipe burst pressure analysis","method":"VR-VMETH-0003","results":[{"quantity_name":"burst_margin","value":{"value":0.42,"unit":"1"}}],"outcome":"Pass","basis_revisions":["PR-D-0000412"],"effectivity":{"effectivity_type":"VR-EFFTYPE-0001","from":3,"to":999},"document":{"source_ref":"CALC-D-0088","issue":2},"discipline":"VR-DISC-0022","lifecycle_stage":"VR-LCS-0006","links":[{"link_type":"Demonstrates","target":"REQ-D-0000141"}],"status":"Approved"}
```

### 3.17 Issue

Purpose: a recorded problem, scored against fixed impact criteria so that its escalation level and forum are set by rule (2E).

| Field | Type | Card. | Values / register | Notes | Ref |
| --- | --- | --- | --- | --- | --- |
| description | text | 1 | | | 2E.1 |
| effort_estimate | qty (person-days) | 1 | | Scored against the project thresholds. | 2E.8 |
| cost_estimate | qty (GBP) | 1 | | Scored against the project thresholds. | 2E.8 |
| schedule_delay | qty (weeks) | 1 | 0 = none | Delay to the earliest affected programme milestone. | 2E.8 |
| safety_score | int | 1 | 1 to 5 (option of the criterion) | The highest option that fits. The software checks it against the classifications of affected Parts. | 2E.2, 2E.8 |
| scope_score | int | 1 | 1 to 5 | The highest option that fits, judged by the affected objects, not the FDPS footprint. The software proposes a value. | 2E.2, 2E.8 |
| product_scope | reg(SCOPE) | 0..n | | Optional tags on the Issue itself. | 2E.7 |
| lifecycle_stage | reg(LCS) or ALL | 1..n | | Mandatory tag. | 2F.12 |
| resolution | json | 0..1 | {summary, resolved_by: Person, resolved_at} | A person is required at level 3 or above. | 0.5 |
| status | reg | 1 | Open; In Progress; Resolved; Closed | | |

Owned links:

| Link type | Target | Card. |
| --- | --- | --- |
| Affects | Requirement, item, Verification (any data object) | 1..n |
| Resolved by | Change Record | 0..n (required when Resolved) |

Derived: scores for effort, cost and schedule from the thresholds; escalation level, which is the highest of the five scores (2E.3); forum, from the band for that level (2E.9); rank within the forum, by escalation level then the sum of scores (2E.6); Product Scopes of the affected items (2E.7).

Validation: all five criteria must be present (2F.12); at least one Affects link; at least one Resolved by link when resolved by a change (2E.10); no field allows the escalation level to be entered by hand. An Issue in a Lifecycle Stage outside the current scope is stored and tagged without stage-specific rules (2B.13).

Example:

```json
{"id":"ISS-D-0000058","type":"Issue","title":"Feed pipe clash with frame 14 clip","effort_estimate":{"value":3,"unit":"person-day"},"cost_estimate":{"value":2000,"unit":"GBP"},"schedule_delay":{"value":0,"unit":"week"},"safety_score":1,"scope_score":2,"lifecycle_stage":["VR-LCS-0006"],"links":[{"link_type":"Affects","target":"PI-D-0004127"}],"status":"Open"}
```

Derived on read for this example: scores 2, 1, 1, 1 and 2, so escalation level 2, forum Engineer (Issue owner).

### 3.18 Design Review

Purpose: a Scheme Review at stage A, B or C covering one or more whole FDPSs, with a Pass or Fail by the Technical Authority for Design (6C).

| Field | Type | Card. | Values / register | Notes | Ref |
| --- | --- | --- | --- | --- | --- |
| stage | reg(STAGE) | 1 | A; B; C | | 6C.1 |
| review_date | date | 1 | | | 6C.7 |
| material_issued_at | date | 1* | At least 14 days before review_date | Required before the review is held. | 6C.7 |
| chair | ref(Person) | 1 | | Normally the Technical Authority for Design. | 6C.10 |
| attendees | json | 1 | [{person, represents: reg(DISC), Sub-team or System, role: reg(ROLE) or text}] | Structured attendee list. | 6C.4 |
| introduction | json | 1 | {scope} | | 6C.4 |
| entry_check | json | 1* | {criterion, met: bool, evidence} for each criterion | Required before the review is scheduled. Union of generic and Design-Type criteria. | 6C.15, 6C.16 |
| content | json | 1* | Generated template sections with responses | | 6C.3, 6C.4 |
| known_risks | ref(Risk) | 0..n | | Structured Risk records (3.36). | 6C.4 |
| minutes | text | 1* | | Required after the review. | 6C.8 |
| discipline_agreements | json | 1* | {discipline: reg(DISC) of type Sign-off team, position: reg(AGREE), reasons, conditions: [ref(Action)], by: Person, at, carried_forward_from: ref(Design Review) 0..1} for each Sign-off team Discipline listed against the stage, less project-N/A Disciplines | Required before the decision. Each condition is an Action. Consideration only Disciplines have no entry; their record is the designer's Checklist Responses. | 6C.19, 2B.14 |
| interface_agreements | json | 1* | {system: reg(SYS), position: reg(AGREE), reasons, conditions: [ref(Action)], by: Person (Design Lead for that System or one of its Sub-systems), at, carried_forward_from 0..1} for each interfacing System of the covered FDPSs that is not broken | Required before the decision. | 6C.22 |
| re_review | json | 0..1 | {follows_review: ref(Design Review), change_records: [ref(Change Record)], scope: changed areas, affected_disciplines, affected_systems, identified_by: Person (Design Authority)} | Present for a re-review: held at the FDPS's current stage, scoped to the changed areas. | 6C.12 |
| decision | reg | 1 | Pending; Pass; Fail | | 6C.10 |
| decision_by / decision_at | ref(Person) / datetime | 1* | | The Technical Authority for Design only. | 6C.10, 0.5 |
| status | reg | 1 | Planned; Material Issued; Held; Closed | | |

Owned links:

| Link type | Target | Card. |
| --- | --- | --- |
| Covers | FDPS Revision | 1..n |
| Production link | review documentation | 0..n |

Derived: review template, from the stage sections of the covered FDPSs' Sub-team pages (checklist items, Sign-off team Disciplines, entry criteria) and the inferred Requirements, TSMs and interfacing Systems of the FDPSs (6C.6); required Sign-off team Disciplines (union over the covered FDPSs' Sub-team stage sections, less project-N/A Disciplines); required interfacing Systems; applicable Design Types; open Actions.

Validation: the review cannot be scheduled until the entry check passes (6C.15); a Pass requires a position of Agree or Agree with conditions from every required Sign-off team Discipline (6C.19) and every required interfacing System (6C.22), given directly or, for a re-review, carried forward where the area is not affected (6C.12); every condition has an Action; every No Checklist Response has its follow-up (4.5); each agreement is given by a person whose Role register entry covers the Discipline or System (6C.14); material is issued at least 14 days before the review (6C.7); a Pass or Fail requires a decision_by Person; the review links to every FDPS it covers (6C.2); a Snapshot exists before the decision (6C.9).

Example:

```json
{"id":"DR-D-0000009","type":"Design Review","title":"Scheme Review C, tank 2 feed","stage":"VR-STAGE-0003","review_date":"2026-09-01","material_issued_at":"2026-08-14","chair":"user:tad_d","decision":"Pass","decision_by":"user:tad_d","links":[{"link_type":"Covers","target":"FR-D-0000032"}],"status":"Closed"}
```

### 3.19 Review Snapshot

Purpose: a read-only structured record of the design as reviewed, used for the substantial-change assessment (6C.9, 6C.18).

| Field | Type | Card. | Values / register | Notes | Ref |
| --- | --- | --- | --- | --- | --- |
| design_review | ref(Design Review) | 1 | | | 6C.9 |
| taken_at | datetime | 1 | | | 6C.9 |
| content | json | 1 | {fdps_revisions, instances, revision links, owned links, interfacing Systems, interface breaks, FDPS interfaces, interface agreements, compliance statements}, all as id@record_version | Frozen; references frozen copies only. | 6C.18, 6C.23, 6A.15 |
| baseline | ref(Baseline) | 1 | | The baseline frozen for each covered FDPS revision at the snapshot. | 6C.9, 6A.10 |
| content_hash | string | 1 | | Integrity check. | 6A.10 |
| status | reg | 1 | Frozen | Never edited. | |

Owned links: Records, pointing to the Design Review (1).

Derived: a structured difference against the current design, highlighting changes that may degrade form, fit, function, interfaces or compliance (6C.18).

Validation: no update is permitted once created; there is one snapshot per review.

Example:

```json
{"id":"RS-D-0000009","type":"Review Snapshot","design_review":"DR-D-0000009","taken_at":"2026-09-01T08:00:00Z","content":{"fdps_revisions":["FR-D-0000032"],"instances":[{"id":"PI-D-0004127","irl":"IRL-D-0009001","build_station":"VR-BS-0006","sub_system":"VR-SUB-0031"}],"interfacing_systems":["VR-SYS-0003"]},"content_hash":"sha256:...","status":"Frozen"}
```

### 3.20 Action

Purpose: a structured review action from the action tracker template, tagged against the FDPSs covered (6C.8).

| Field | Type | Card. | Values / register | Notes | Ref |
| --- | --- | --- | --- | --- | --- |
| description | text | 1 | | | 6C.8 |
| due_date | date | 1 | | Mandatory. | 2F.12 |
| raised_by | ref(Person) | 1 | | Mandatory. | 6C.8 |
| source | json | 0..1 | {kind: Review, Condition of agreement or Checklist No; ref} | Where the Action came from. | 6C.19, 4.5 |
| closure | json | 1* | {evidence, closed_by: Person, closed_at, accepted_by: Person (raiser or review chair), accepted_at} | Required when Closed. Closed only once accepted. | 6C.8, 6C.11 |
| status | reg | 1 | Open; Closed; Cancelled | | |

Owner (common field) is mandatory (2F.12).

Owned links:

| Link type | Target | Card. |
| --- | --- | --- |
| Raised at | Design Review | 1 |
| Tagged to | FDPS | 1..n |

Derived: overdue (due date passed and still Open).

Validation: each tagged FDPS is covered by the review; closure.accepted_by is the raiser or the review chair; a Cancelled action requires a reason and the chair's approval (6C.11).

Example:

```json
{"id":"ACT-D-0000101","type":"Action","title":"Confirm clip relocation","description":"Confirm frame 14 clip relocation with Structures","owner":"user:eng_fuel","raised_by":"user:stress_d","due_date":"2026-09-20","closure":{"evidence":"Layout PLM-778800 iss 2","closed_by":"user:eng_fuel","closed_at":"2026-09-18","accepted_by":"user:stress_d","accepted_at":"2026-09-19"},"links":[{"link_type":"Raised at","target":"DR-D-0000009"},{"link_type":"Tagged to","target":"FD-D-0000017"}],"status":"Closed"}
```

### 3.21 Lesson Learned

Purpose: a lesson stored once in the standard template, and shown as a page of page type Lesson Learned, without a separate Hub Page object (2G).

| Field | Type | Card. | Values / register | Notes | Ref |
| --- | --- | --- | --- | --- | --- |
| summary | text | 1 | | | 2G.2 |
| what_happened | text | 1 | | | 2G.2 |
| root_cause | text | 1 | | | 2G.2 |
| recommendation | text | 1 | | | 2G.2 |
| applicability | text | 1 | | Free description; the tags carry the controlled applicability. | 2G.2 |
| lifecycle_stage | reg(LCS) or ALL | 1..n | | Mandatory tag. | 2G.3 |
| system | reg(SYS) or ALL | 1..n | | Mandatory tag. | 2G.3 |
| discipline | reg(DISC) or ALL | 1..n | | Mandatory tag. | 2F.12 |
| design_type | reg(DTY) or ALL | 1..n | | Mandatory tag (added in v7). | 2G.3 |
| sub_system | reg(SUB) | 0..n | | Optional finer tag (added in v7). | 2G.3 |
| product_scope | reg(SCOPE) | 0..n | | | 2F.2 |
| origin_record | ref(any data object, for example Issue, Design Review or Verification) | 0..1 | | The project record the lesson came from, where there is one. Held in the Production Hub only. | 2G.2 |
| promotion | json | 0..1 | {proposed_by, proposed_at, generic_lesson: ref(Lesson Learned in the Framework Hub), approved_by, approved_at, project_data_removed: bool} | Promotion of a project lesson to a generic framework lesson, with project data removed. | 2G.5 |
| status | reg | 1 | Draft; Published; Archived | | |

Origin (common field) must give a source document with its issue or revision and a link, or the origin record (2G.2).

Owned links: Describes, to related data objects (0..n).

Derived: the TSMs and Design Considerations that are informed by it (inbound links); the pages and FDPSs it is shown on, matched by tag only, never by keyword: a lesson matches when its tags match the page's or FDPS's Lifecycle Stage, Discipline, Design Type, System or Sub-system, with ALL matching every value (2G.6).

Validation: all template fields are present; the origin source or origin record is present unless the origin kind is Human; framework lessons contain no project data and no origin_record (6.2); a promotion is approved before the generic lesson is published (2G.5).

Example:

```json
{"id":"LL-FW-0000012","type":"Lesson Learned","title":"Clip spacing on long feed pipes","summary":"Insufficient clip spacing led to vibration fatigue in test","root_cause":"Spacing set from static loads only","recommendation":"Include vibration spectrum in clip spacing analysis","lifecycle_stage":["VR-LCS-0008"],"system":["VR-SYS-0010"],"discipline":["VR-DISC-0022"],"design_type":["VR-DTY-0009","VR-DTY-0012"],"origin":{"kind":"AI","source_ref":"Fictional report R-001","source_issue_or_revision":"Issue 1"},"confidence":0.78,"verification_status":"Unverified","status":"Draft"}
```

### 3.22 Design Consideration

Purpose: the design consideration record of one Discipline (4.2), with guidance and detailed checklists for each review stage (4.3 to 4.5). There is exactly one Design Consideration per Discipline register entry, so considerations are driven by the Discipline register and never held as a separate list. It extends Hub Page (3.24) and is the Hub page of its Discipline (page type Discipline).

| Field | Type | Card. | Values / register | Notes | Ref |
| --- | --- | --- | --- | --- | --- |
| discipline | reg(DISC) | 1 | Discipline register (Annex B.2 of v23) | Unique: one record per Discipline. The title is the Discipline label. Its discipline_type is read from the register, not stored. | 4.2, 2B.14 |
| description | text | 1 | Generic | | 4.3, 5.8 |
| guidance | text | 1 | Generic | | 4.3 |
| checklists | json | 0..n | {stage: reg(STAGE), items: [{item_id, question, applies_to: [Design Type, Design Sub-team or item property] 0..n}]} | Detailed checklists for the Discipline. An item with no applies_to applies to all designs. | 4.4, 4.5 |
| property_filters | reg(PROP) | 0..n | | | 4.6 |

Owned links:

| Link type | Target | Card. |
| --- | --- | --- |
| Governed by | TSM | 0..n |
| Informed by | Lesson Learned | 0..n |
| Applies to | Design Type, Design Sub-team, review stage | 0..n (refines which checklist items apply; the consideration itself applies to all designs) |

Derived: discipline_type (from the register); the applicable checklist items for each Part and FDPS (inferred in the same way as TSMs, 4.4); checklist feeds into review templates.

Former considerations (settled, v23 4.2): Thermal is split. Heat signature items are held in the Low Observability record (VR-DISC-0012); thermal environment items, such as fuel heat soak and equipment temperature limits, are held in the System Layout and Integration record. Environmental Impact and Sustainability items are held in the Materials and Processes record (VR-DISC-0015), and Vibration and Shock items in the Structural Analysis (Stress) record (VR-DISC-0022). Each such item carries a topic label (Thermal, Environmental Impact and Sustainability, or Vibration and Shock) so that it can be filtered. Fluid Systems (VR-DISC-0026) has its own record.

Validation: exactly one Design Consideration per active Discipline entry, and none without a Discipline; checklist item ids are stable across versions. Responses are held as Checklist Responses (3.32), and any Not applicable response carries a reason.

Example:

```json
{"id":"DC-FW-0000013","type":"Design Consideration","page_type":"VR-PAGETYPE-0010","framework_node":"VR-DISC-0013","discipline":"VR-DISC-0013","title":"Maintainability, Reliability and Ground Equipment","checklists":[{"stage":"VR-STAGE-0002","items":[{"item_id":"MRG-B-01","question":"Are line-replaceable items reachable without removing primary structure?","applies_to":["VR-DTY-0011"]}]}],"hub":"FW"}
```

### 3.23 Parameter

Purpose: a named, structured design parameter held as data, readable and writable by people and AI, and forming a dependency graph (3.1 to 3.9).

| Field | Type | Card. | Values / register | Notes | Ref |
| --- | --- | --- | --- | --- | --- |
| name | string | 1 | Unique within its owner | | 3.6 |
| description | text | 1 | | | 3.6 |
| value | qty | 1 | | | 3.6 |
| expression | string | 0..1 | Expression over other parameter ids | Present for derived parameters. | 3.7 |
| limits | json | 0..1 | {min: qty, max: qty, inclusive flags} | | 3.6 |
| constraints | json | 0..n | {kind: limit, ratio or relationship; expression; governing: ref(Requirement or TSM)} | | 3.9 |
| owning_object | ref(Part Definition, Assembly Definition, FDPS or Project) | 1 | | | 3.1 |
| status | reg | 1 | Draft; Confirmed; Released | | 3.6 |

Origin kind: Human, AI or Derived (3.6). AI changes require confirmation by a person before release (3.5).

Owned links:

| Link type | Target | Card. |
| --- | --- | --- |
| Drives | Parameter, model (Part Revision or Production Link), Verification | 0..n |

Inbound: Constrains (from Requirement or TSM).

Derived: upstream and downstream sets (3.7); constraint check results; regeneration status (3.11).

Validation: no circular dependencies (3.7); the unit is compatible with the limits; every constraint cites a Requirement or TSM; a breach is flagged with that citation (3.9).

Example:

```json
{"id":"PAR-D-0000550","type":"Parameter","title":"Feed pipe outside diameter","name":"feed_pipe_od","value":{"value":19.05,"unit":"mm"},"limits":{"min":{"value":12.7,"unit":"mm"},"max":{"value":25.4,"unit":"mm"}},"owning_object":"PD-D-0000231","origin":{"kind":"Human"},"status":"Confirmed","links":[{"link_type":"Drives","target":"PAR-D-0000551"}]}
```

### 3.24 Hub Page

Purpose: a page for a Hub level or other page type, holding generic guidance (in the Framework Hub) or project content and links (in a Production Hub). There are no pages for individual items (1.5, 5.2).

| Field | Type | Card. | Values / register | Notes | Ref |
| --- | --- | --- | --- | --- | --- |
| page_type | reg(PAGETYPE) | 1 | | Mandatory. | 2F.12 |
| framework_node | reg(any tree register) | 1 | | Mandatory. For example VR-SYS-0010 for the Fuel page. | 2F.12 |
| template | string | 1 | Template id of the page type | | 5.2 |
| body | json | 1 | Structured blocks: text, image refs, link lists | No embedded production data on framework pages. | 6.5 |
| stage_sections | json | 0..n | {stage, checklist_items: [{discipline, item_id}], sign_off_disciplines: reg(DISC) of type Sign-off team, type_specific_entry_criteria} | Design Sub-team pages only. Stages A Initial System Design, B Preliminary, C Detail. Tailored per Production Hub from the framework templates. Requirements, TSMs and interfacing Systems are inferred, not listed. | 6C.6, 6C.15, 6C.19, 4.4 |
| interfaces | reg(SYS) | 0..n | Finite list; never 'all Systems' | Sub-system and Sub-structure pages only. A non-structural Sub-system page lists the Systems its items interface with, naming the structural Systems or Sub-structures its items attach to; it is inherited by every FDPS with a Part Instance homed in the Sub-system. A Sub-structure page lists the Systems whose items are installed on or attach to it; it is inherited by every Sub-structure FDPS with a Part Instance homed in it (over-inclusion accepted), and never by a non-structural FDPS. | 6C.20, 6C.21 |
| applicable_design_types | reg(DTY) | 0..n | | Design Team pages: the Design Types the team uses, always including Standard Part. Sub-system and Sub-structure pages (added in v7): the Design Types used in that Sub-system, giving the route Sub-system > Design Type > TSM. | 6B.5, A.4 |
| applicable_disciplines | reg(DISC) | 0..n | | Design Team pages only, alongside applicable_design_types: the Disciplines through which TSM Discipline tags reach the FDPSs owned by the team's Sub-teams (confirmed, R-11). | 6B.5, A.4 |
| lifecycle_stage | reg(LCS) or ALL | 1..n | | Mandatory tag. | 2F.12 |
| discipline | reg(DISC) or ALL | 1..n | | Mandatory tag. | 2F.12 |
| last_reviewed_at | date | 1 | | | 5.5 |
| owner_rule | derived | - | | Sub-system and Sub-structure pages: the owner shown is the Design Lead for that area from the Role register, displayed as Design Lead (owner); the common owner field is not shown (added in v7). | 5.30 |
| layout | reg | 1 | Tree page layout v2 | Left rail (filters above the collapsible tree, for navigation); model preview top left beside the summary (status chips; parent System and System Group, Design Lead (owner), Design Sub-team and ID, each a link; tiles); categories collapsed by default in five groups: Requirement (EDRs, TSMs), Verification (Compliance, Verifications, Reviews), Product (Sub-system pages: FDPSs only, no Part Instances), Considerations (Interfacing Systems, Disciplines and Stakeholders), Working Data at the bottom (Issues, Lessons Learned); no Links area, links built into the data; fixed AI bar; theme setting. Documents above FDPS level, line items on FDPS pages; FDPS page layout follows the same groups, to be confirmed (changed in v7.3). | 5.21 to 5.29 |
| status | reg | 1 | Draft; Published; Retired | | |

Owned links:

| Link type | Target | Card. |
| --- | --- | --- |
| Describes | any data object | 0..n |
| Cross-link | Hub Page | 0..n |
| Production link | Production Link | 0..n (Production Hub only) |

Derived: backlinks (5.3); live model preview filter (1.12); production data shown alongside it (6.5); position in each view.

Validation: there is one page per framework node and page type; framework pages carry hub FW and contain no project data (6.10); in a Production Hub, framework pages are read-only and changes go to Tailoring Records (6.4).

Example:

```json
{"id":"PG-FW-0000210","type":"Hub Page","title":"Fuel System","page_type":"VR-PAGETYPE-0008","framework_node":"VR-SYS-0010","template":"TPL-SYSTEM-1","lifecycle_stage":["ALL"],"discipline":["ALL"],"last_reviewed_at":"2026-10-01","status":"Published","hub":"FW"}
```

### 3.25 Production Link

Purpose: the typed link from an item or page to a production record held in another master, carrying its identifier and revision or issue (2J.4, 6.6).

| Field | Type | Card. | Values / register | Notes | Ref |
| --- | --- | --- | --- | --- | --- |
| source_object | ref(item, page or other data object) | 1 | | | 2I.2 |
| record_kind | reg | 1 | Part model; Drawing; Calculation document; Test report; Other | | 6.3 |
| external_system | reg(MASTER) | 1 | | | 2J.3 |
| external_id | string | 1 | | | 2J.4 |
| revision_or_issue | string | 1 | | | 2J.4 |
| effectivity | eff | 0..1 | | Reflects the master. | 6.7 |
| baselines | ref(Baseline) | 0..n | | | 6.7 |
| last_synced_at | datetime | 1 | | | 2J.2 |
| status | reg | 1 | Current; Superseded; Broken | | 6.8 |

Owned links: none (it is the link object).

Derived: supported Requirements, shown in the Requirement column as permanent identifier and short title, through the source item's links (6.5); whether the master is still external (Authority Register).

Validation: hub is a project (never FW); a superseded record or changed effectivity flags the source object (6.8).

Example:

```json
{"id":"PL-D-0002001","type":"Production Link","title":"Feed pipe CAD model","source_object":"PR-D-0000412","record_kind":"Part model","external_system":"VR-MASTER-0001","external_id":"PLM-778812","revision_or_issue":"B","last_synced_at":"2026-10-09T23:00:00Z","status":"Current"}
```

### 3.26 Authority Register Entry

Purpose: one append-only event recording the master of a data type in a Production Hub and any move to the Hub, with its evidence (2J.3, 2J.8).

| Field | Type | Card. | Values / register | Notes | Ref |
| --- | --- | --- | --- | --- | --- |
| project | ref(Project) | 1 | | | 2J.3 |
| data_type | reg(DATA_TYPE) | 1 | | | 2J.3 |
| event | reg | 1 | Master recorded; Parallel run started; Moved to Hub | | 2J.7 |
| master | reg(MASTER) | 1 | | | 2J.3 |
| effective_date | date | 1 | | Date of the move for Moved to Hub. | 2J.3 |
| reconciliation_report | ref(Production Link or attachment) | 1* | | For Moved to Hub. | 2J.7 |
| sign_off | json | 1* | {by: Person (data type owner), at} | | 2J.7 |
| parallel_run | json | 1* | {release_cycle, from, to, unresolved_discrepancies: 0} | | 2J.7 |
| approved_by | ref(Person) | 1* | | Moving a data type to the Hub is a decision for people. | 0.5 |

Owned links: none.

Derived: the current master per data type, from the latest event.

Validation: append-only, so entries are never edited; Moved to Hub requires all the evidence fields and zero discrepancies; the move order follows 2J.6 (a data type cannot move before its predecessors).

Example:

```json
{"id":"AR-D-0000003","type":"Authority Register Entry","project":"PRJ-D-0000001","data_type":"Requirement","event":"Moved to Hub","master":"VR-MASTER-0005","effective_date":"2026-11-02","sign_off":{"by":"user:req_owner","at":"2026-10-30"},"parallel_run":{"release_cycle":"RC-04","unresolved_discrepancies":0},"approved_by":"user:dwagner"}
```

### 3.27 Baseline

Purpose: a frozen, read-only record of one FDPS revision's configuration, frozen at each release of that revision and at each review snapshot of it (6A.10). Baselines are numbered 1, 2, 3 ... within the FDPS revision.

| Field | Type | Card. | Values / register | Notes | Ref |
| --- | --- | --- | --- | --- | --- |
| fdps_revision | ref(FDPS Revision) | 1 | | | 6A.10 |
| sequence_no | int | 1 | 1, 2, 3 ... | Unique within the FDPS revision. | 6A.10 |
| trigger | json | 1 | {kind: Release or Review snapshot; ref: release event or Review Snapshot} | | 6A.10, 6C.9 |
| effectivity | eff | 1 | | The FDPS revision's effectivity range at the time of freezing. | 6A.11 |
| frozen_at | datetime | 1 | | | 6A.10 |
| content | json | 1 | {instances, revision links, owned links, population, compliance statements, interfacing Systems, FDPS interfaces, derived: {fdps_systems, inferred categories}}, each record as id@record_version | References frozen copies only (6A.15). Derived views are frozen as stored values. | 6A.10, 6A.15 |
| content_hash | string | 1 | | | |
| status | reg | 1 | Frozen | | |

Owned links: none.

Derived: comparison between any two baselines (6A.10); the configuration at any effectivity number in the range, read from the frozen content.

Validation: never edited; every reference resolves to a frozen copy; the content resolves each instance to exactly one revision at every effectivity number in the range.

Example:

```json
{"id":"BL-D-0000002","type":"Baseline","fdps_revision":"FR-D-0000033","sequence_no":2,"trigger":{"kind":"Release","ref":"REL-D-003"},"effectivity":{"effectivity_type":"VR-EFFTYPE-0001","from":1,"to":999},"frozen_at":"2026-10-01T12:00:00Z","content_hash":"sha256:...","status":"Frozen"}
```

### 3.28 Change Record

Purpose: a recorded change with its author, date and reason. It covers link changes, transfers, ownership changes, up-revisions, new part numbers, effectivity changes, population changes, interface changes and improvements after review, and may carry several change types (6A.7, 1.7.6, 6A.9, 6C.17).

| Field | Type | Card. | Values / register | Notes | Ref |
| --- | --- | --- | --- | --- | --- |
| change_types | reg(CHG) | 1..n | | | 6A.7 |
| reason | text | 1 | | | 6A.7 |
| affected_objects | ref | 1..n | | | |
| before / after | json | 1 | Field and link values | | 6A.7 |
| interchangeability | json | 1* | {form, fit, function: bool each; all_uses_assessed: bool; outcome: Interchangeable or Not interchangeable} | Required for revision and part number changes. | 6A.9 |
| follows_review | ref(Design Review) | 0..1 | | For improvements after review. | 6C.17 |
| approvals | json | 0..n | {role, by: Person, at} | For example both Sub-teams for a transfer, or both Design Team leads for an ownership change. | 1.7.6 |
| fdps_revision_required | ref(FDPS Revision) | 0..1 | | Set when a member of a released FDPS changes. | 6A.7 |
| fdps_assessments | json | 0..n | {fdps, substantial: bool, criteria: [adversely affects compliance; degrades form, fit or function; degrades an interface; adds a new interface with another System], margin_note, assessed_by: Person (Design Authority), at} | One per affected FDPS: whether the change is substantial for that FDPS (6C.17). | 6C.12, 6C.17 |
| status | reg | 1 | Proposed; Approved; Implemented; Rejected | | |

Owned links: none beyond the reference fields.

Derived: Review Flags raised by the change.

Validation: the required approvals for each change type are present before Implemented; an Interchangeable outcome requires form, fit and function all true; every affected FDPS has an assessment before its next release; a reduced margin that remains compliant is recorded in margin_note and is not by itself substantial (6C.17); substantial is true if and only if at least one criterion is recorded; a change that improves or restores compliance does not adversely affect it; added parts are substantial only if they create a new interface with another System or adversely affect compliance (6C.17).

Example:

```json
{"id":"CR-D-0000077","type":"Change Record","title":"Increase feed pipe wall thickness","change_types":["VR-CHG-0004"],"reason":"Burst margin below target in rev A","affected_objects":["PD-D-0000231"],"interchangeability":{"form":true,"fit":true,"function":true,"all_uses_assessed":true,"outcome":"Interchangeable"},"fdps_assessments":[{"fdps":"FD-D-0000017","substantial":false,"criteria":[],"assessed_by":"user:da_fuel"}],"status":"Implemented"}
```

### 3.29 AI Query Log

Purpose: an access-controlled, append-only log of every AI query and answer (5.19).

| Field | Type | Card. | Values / register | Notes | Ref |
| --- | --- | --- | --- | --- | --- |
| user | ref(Person) | 1 | | | 5.19 |
| asked_at | datetime | 1 | | | 5.19 |
| hub | FW or ref(Project) | 1 | | | 5.19 |
| query | text | 1 | | | 5.19 |
| answer | text | 1 | | | 5.19 |
| cited_sources | ref | 0..n | Permanent identifiers | | 5.13 |
| no_answer_in_sources | bool | 1 | | | 5.13 |
| permissions_context | string | 1 | | The access scope used for the query. | 5.18 |
| saved_as | ref(Saved AI Answer) | 0..1 | | | 5.20 |
| retention_until | date | 1 | | From the project's retention policy. | 5.19 |

Owned links: none.

Validation: append-only; readable only by authorised roles; cited sources must be within the user's permissions.

Example:

```json
{"id":"AIQ-D-0100231","type":"AI Query Log","user":"user:eng_fuel","asked_at":"2026-10-10T09:12:00Z","hub":"PRJ-D-0000001","query":"Which TSMs apply to FDPS D5322001-801?","cited_sources":["TSM-D-0000062"],"no_answer_in_sources":false,"retention_until":"2033-10-10"}
```

### 3.30 Image

Purpose: an image or diagram used on pages, held as a data object with accessibility text and, for product views, the configuration shown (5.10).

| Field | Type | Card. | Values / register | Notes | Ref |
| --- | --- | --- | --- | --- | --- |
| caption | string | 1 | | | 5.10 |
| alt_text | text | 1 | | | 5.10, 5.11 |
| file | string | 1 | Stored file reference or Production Link | | 5.10 |
| is_product_view | bool | 1 | | | 5.10 |
| configuration | json | 1* | {project, effectivity_number, baseline: ref(Baseline) 0..1} | Required for product views. | 5.10, 6.7 |
| status | reg | 1 | Draft; Published; Retired | | |

Owned links: Describes, to the objects shown (0..n).

Validation: product views appear only in Production Hubs; alt_text is not empty.

Example:

```json
{"id":"IMG-D-0000090","type":"Image","title":"Tank 2 feed routing","caption":"Tank 2 feed routing, effectivity 3","alt_text":"Isometric view of the fuel feed pipe running from tank 2 to the engine feed bay","is_product_view":true,"configuration":{"project":"PRJ-D-0000001","effectivity_number":3,"baseline":"BL-D-0000002"},"status":"Published"}
```

### 3.31 Review Flag (added)

Purpose: a "needs review" flag raised on a data object by a change propagating through a typed link (2.6, 2.7, 2I.3, 2I.6).

| Field | Type | Card. | Values / register | Notes | Ref |
| --- | --- | --- | --- | --- | --- |
| flagged_object | ref | 1 | | | 2I.3 |
| triggering_object | ref | 1 | | | 2I.2 |
| trigger_change | ref(Change Record) or record_version | 1 | | | 2I.2 |
| via_link | ref(Link) | 1 | | | 2I.2 |
| link_confirmed | bool | 1 | | Unconfirmed-link flags are shown separately. | 2I.6 |
| decision | reg | 1 | Open; No impact; Updated; Passed on; Accept; Query | Accept and Query are used only when fdps_interface is true (R-18). | 2I.3, 6C.24A |
| fdps_interface | bool | 0..1 | | R-18: true for a flag raised to the owner of the other FDPS by a cross-FDPS Secures link. A Query stays open, is shown on both FDPS pages and does not block the link; no link confirmation is required. | 6C.24A |
| passed_on_to | ref(Review Flag) | 0..n | | One action by the reviewer. | 2I.3 |
| decided_by / decided_at | ref(Person) / datetime | 1* | | | 0.3 |

Validation: by default flags are raised only on directly linked objects (2I.3); derived-tag recalculations never raise flags (2I.2).

Example:

```json
{"id":"RF-D-0003311","type":"Review Flag","flagged_object":"VER-D-0000301","triggering_object":"PR-D-0000412","via_link":"LNK-D-0081200","link_confirmed":true,"decision":"Open"}
```

### 3.32 Supporting types (brief)

| Data type | Purpose | Key fields | Ref |
| --- | --- | --- | --- |
| Checklist Response | Response to one consideration checklist item for an FDPS at a stage | fdps_revision, stage, consideration (one per Discipline), item_id, response (Yes, No, Not applicable), reason (required for Not applicable and No), responder (the designer: a Person), follow_up for No: {kind: reg(CKFU), ref: Action or Risk, or justification approved_by the Discipline Lead} | 4.5, 2B.14 |
| Parameter Iteration | One set of parameter changes | changes [{parameter, from, to}], author, date, reason, branch (main or what-if), merged_by | 3.12 |
| Tailoring Record | A project change to the framework | project, framework_version, target framework id, action (add option, add page, hide section, modify, mark Discipline not applicable), payload, reason, approved_by (the Technical Authority for Design for a Discipline marked not applicable) | 6.4, 6.11, 2B.14 |
| Framework Version | A numbered release of the framework | version, released_at, change list, content_review {by, at, confirmed no project data} | 6.9, 6.10 |
| Saved AI Answer | An AI answer saved by a user, as an unverified record | query_log, answer, cited sources as origin, verification_status Unverified | 5.20 |

### 3.33 Retrofit (moved to section 7)

Retrofit is not in the current scope (v23 6A.16, 7.1). Its proposed fields (fdps, from_revision, to_revision, effectivity, change_records, instruction_ref, embodiment per effectivity, status) are kept in section 7 for Future Development. The prefix RT stays reserved.

### 3.34 Concession (moved to section 7)

Concession is not in the current scope (v23 6A.16, 6A.17, 7.4): Concessions are part of the manufacturing standard, not the design standard. Its proposed fields are kept in section 7 for Future Development, and the prefix CON stays reserved. In the current scope a known non-compliance of the design is a Compliance Statement with position Non-compliant, referencing its Issue (3.15), which blocks release for its range.

### 3.35 Role Assignment (added)

Purpose: one entry in the Role register: a person holding a role over an area for a period (6C.14).

| Field | Type | Card. | Values / register | Notes | Ref |
| --- | --- | --- | --- | --- | --- |
| person | ref(User) | 1 | | Must hold an active Project Assignment whose access role may hold this authority role (5A.6; changed in v7.4). | 6C.14, 5A.6 |
| role | reg(ROLE) | 1 | | | 6C.14, B.4 |
| area | json | 1 | {kind: Project, Design Team, Design Sub-team, Design Type, System Group, System, Sub-system (including Sub-structure) or Discipline; ref} | There is no FDPS area kind and no FDPS Design Lead (v23 6C.14). | 6C.14 |
| delegations | json | 0..n | {authority, e.g. FDPS release; to: Person; from_date; to_date} | | 6C.14 |
| from_date / to_date | date / date | 1 / 0..1 | | | 6C.14 |
| status | reg | 1 | Active; Ended | | |

Validation: every approval, agreement and release checks the Role register at its date; a Design Lead's area for a Requirement non-applicability covers every Sub-system through which the Requirement reaches the FDPS (6C.13); each interface break of an FDPS is approved by a person holding an active Design Lead assignment whose area is the FDPS's lead_sub_system (6C.14, 6C.21).

### 3.36 Risk (added)

Purpose: a structured known risk, raised at a review or from a Checklist Response of No (6C.4, 4.5).

| Field | Type | Card. | Values / register | Notes | Ref |
| --- | --- | --- | --- | --- | --- |
| description | text | 1 | | | 6C.4 |
| likelihood / consequence | int / int | 1 / 1 | 1 to 5 | | 6C.4 |
| owner | ref(Person) | 1 | | | 6C.4 |
| mitigation | text | 0..1 | | | 6C.4 |
| source | json | 0..1 | {kind: Review or Checklist No; ref} | | 4.5 |
| tagged_fdps | ref(FDPS) | 0..n | | | |
| status | reg | 1 | Open; Mitigated; Closed; Accepted | | |

### 3.37 User (added in v7.4)

Purpose: a person who uses a Production Hub (5A.1). Replaces the directory-only Person of earlier versions; every ref(Person) in this schema is a ref(User).

| Field | Type | Card. | Values / register | Notes | Ref |
| --- | --- | --- | --- | --- | --- |
| id | string | 1 | USR-NNNNNNN | Not project-scoped; one User may be assigned to several projects. | 5A.1 |
| display_name | string | 1 | | | 5A.1 |
| email | string | 1 | Unique | Directory identity used for sign-in. | 5A.1 |
| design_team / design_sub_team | reg(DT) / reg(DST) | 0..1 / 0..1 | | | 5A.1 |
| user_status | reg(USTATUS) | 1 | Active; Suspended; Left | Suspended or Left removes all access but keeps every link. | 5A.1 |
| framework_admin | bool | 1 | default false | Administers framework users and all project admin pages. | 5A.8 |
| theme | reg | 0..1 | Company; Dark; Light | User setting (5.28). | 5.28 |
| last_active_at | datetime | 0..1 | | Set by the software. | 5A.8 |

Validation: an AI agent cannot be a User. Ending a User (Left) requires every item it owns to be reassigned or flagged.

### 3.38 Access Role (added in v7.4)

Purpose: a framework-fixed named bundle of permissions (5A.2, Annex B.6). Held as register ACCROLE.

| Field | Type | Card. | Values / register | Notes | Ref |
| --- | --- | --- | --- | --- | --- |
| name | reg(ACCROLE) | 1 | Admin; Design Lead; Design Authority; Engineer; Viewer | | 5A.2 |
| permissions | json | 1..n | [{data_type or "*", action: reg(PERM)}]; bundles per Annex B.6 of the Requirements Prompt, confirmed by Daniel, 12 Oct 2026 | PERM: View; Create; Edit; Approve; Release; Administer users; Comment. | 5A.10 |
| may_hold_authority | reg(ROLE) | 0..n | Admin: all; Design Lead: Design Lead; Design Authority: Design Authority; Engineer: Technical Authority for Design, Design Approver, Discipline Lead; Viewer: none | Authority roles of the Role register that a holder of this access role may be given (5A.6; confirmed v7.5). | 5A.6 |

### 3.39 Project Assignment (added in v7.4)

Purpose: gives one User one access role on one project (5A.3).

| Field | Type | Card. | Values / register | Notes | Ref |
| --- | --- | --- | --- | --- | --- |
| user | ref(User) | 1 | | | 5A.3 |
| project | ref(Project) | 1 | | | 5A.3 |
| access_role | reg(ACCROLE) | 1 | | Exactly one per active assignment. | 5A.3 |
| effectivity_access | reg | 1 | All; Restricted | Default All. | 5A.4 |
| from_date / to_date | date / date | 1 / 0..1 | | | 5A.3 |
| assigned_by | ref(User) | 1 | Admin on the project | Person only. | 5A.8 |
| status | reg | 1 | Active; Ended | | |

Validation: at most one active assignment per User per project; Restricted requires at least one Effectivity Restriction.

### 3.40 Effectivity Restriction (added in v7.4)

Purpose: narrows a Project Assignment to listed effectivities (5A.4).

| Field | Type | Card. | Values / register | Notes | Ref |
| --- | --- | --- | --- | --- | --- |
| project_assignment | ref(Project Assignment) | 1 | | | 5A.4 |
| effectivity | ref(Effectivity) | 1..n | Of the same project | Data is visible if its effectivity range overlaps any listed effectivity; data with no effectivity is not restricted. | 5A.4 |
| set_by / set_at | ref(User) / datetime | 1 / 1 | Admin | | 5A.8 |

### 3.41 Permission Override (added in v7.4)

Purpose: a one-off grant or deny of a single permission for a User on a project (5A.5).

| Field | Type | Card. | Values / register | Notes | Ref |
| --- | --- | --- | --- | --- | --- |
| user / project | ref(User) / ref(Project) | 1 / 1 | | | 5A.5 |
| permission | json | 1 | {data_type or "*", action: reg(PERM)} | | 5A.10 |
| effect | reg | 1 | Grant; Deny | Deny prevails over the access role. | 5A.5 |
| reason | string | 1 | | | 5A.5 |
| expires_on | date | 0..1 | | Expired overrides lapse automatically. | 5A.5 |
| approved_by | ref(User) | 1 | Admin | Person only. | 5A.8 |

Example: {"id":"PO-D-0000003","type":"Permission Override","user":"USR-0000014","project":"PRJ-D-0000001","permission":{"data_type":"Lesson Learned","action":"Approve"},"effect":"Grant","reason":"Covers Lessons review while lead on leave","expires_on":"2026-11-30","approved_by":"USR-0000001"}

## 4. Link types

"v23" marks link types listed in 2I.2. "Added" marks link types this schema proposes, which are needed by the requirements but not named in 2I.2 (2I.2 is an initial list). Flags follow the flag depth rule: direct objects only, with the reviewer able to pass a flag on (2I.3).

| Link type | Source | Target | Cardinality | Change-flag direction | Origin |
| --- | --- | --- | --- | --- | --- |
| Decomposes into | Requirement | Requirement (lower) | many-to-many | Changed source flags the lower Requirements (down). | v23 |
| Satisfied by | Requirement | FDPS, or Part Instance or Assembly Instance (traceability) | many-to-many | Changed Requirement flags the Compliance Statements of the FDPS (down). | v23 |
| Part of | Requirement | Requirement Document (EDR) | many-to-one | Changed line item flags the EDR's inheriting FDPSs for that line item only (down). | Added in v7 (6B.1A) |
| Tagged to | Requirement Document | Sub-system (register entry) | many-to-many | Changed tags flag the FDPSs gaining or losing the EDR. | Added in v7 (6B.2) |
| Reviews line item | Line-item Review | Requirement, or TSM statement | many-to-one | Changed line item revision flags the review. | Added in v7 (6B.7) |
| Verified by | item | Verification | many-to-many | Changed item flags the Verifications (down). | v23 |
| Demonstrates | Verification | Requirement or TSM | many-to-many | Failed or changed Verification flags its items and Requirements (up). | v23 |
| Instance of | Part Instance or Assembly Instance | Part Definition or Assembly Definition | many-to-one | Changed definition flags every instance (2D.4). | v23 |
| Supports | Part Instance | System | many-to-many | Changed item flags the Systems it supports (their Hub pages and owners), and no further. | v23 |
| Secures | Part Instance (fastener) | Part Instance (the part held), in the same or another FDPS | many-to-one | A re-homed or removed held Part Instance flags its fasteners; the fastener's Homed in follows the held part (1.6.6). Across two FDPSs it is an FDPS interface: a change to either Part Instance flags the other FDPS (6C.24). | v23 (2I.2, 1.6.6) |
| Interface | item | item in another Product Scope | many-to-many, symmetric | Both ways. | v23 |
| Finish applied | Finish Specification, or Part Instance (override) | Part Definition, or Finish Specification | many-to-many | Changed Finish Specification flags the linked parts. | v23 |
| Affects | Issue | any data object | many-to-many | New or changed Issue flags the affected objects. | v23 |
| Production link | item or page | Production Link record | one-to-many | Superseded record or changed effectivity flags the source. | v23 |
| Describes | Hub Page, Lesson Learned or Image | any data object | many-to-many | Changed target flags the describing page. | v23 |
| Derived from | Part Definition (modified) | Part Definition (bought-in) | many-to-one | Changed source Part flags the derived Part. | v23 |
| Drives | Parameter | Parameter, model or Verification | many-to-many (acyclic) | Changed Parameter flags its dependants. | v23 |
| Located at | Part Instance or Assembly Instance | Build Station (aircraft, or Bench for Part Instances within an Assembly Instance) | many-to-one | None (change is a Change Record; derived Categories recalculate without flags). | Added (1.6) |
| Homed in | Part Instance | Sub-system | many-to-one | Re-homing flags the Compliance Statements of its FDPS (the inherited set and the interfacing Systems change). | Added (1.6) |
| Contains | FDPS | Part Instance or Assembly Instance | one-to-many (single membership) | Population change flags the FDPS owner and, if released, requires a new FDPS revision. | Added (1.7) |
| Assembled from | Assembly Instance | Part Instance | one-to-many | Changed Part Instance flags the Assembly Instance (up). | Added (1.8) |
| Comprises | Assembly Definition | Part Definition (with quantity) | many-to-many | Changed component Part Definition flags the Assembly Definition (up). | Added (1.8.3) |
| Effective revision | Part Instance or Assembly Instance | Part Revision or Assembly Revision (with effectivity) | one-to-many | Changed range flags the instance's Verifications and Production Links. | Added (6A.2) |
| Allocated to | Requirement | System tree node (Sub-system, System or System Group) | many-to-many | Optional narrowing of the EDR Sub-system tag (v7). Changed Requirement flags the Compliance Statements of inheriting FDPSs. | v23 (2I.2) |
| Governs | TSM | Design Type, Discipline or System (tags) | many-to-many | Changed TSM flags the Compliance Statements of inheriting FDPSs. | v23 (2I.2) |
| Interfaces with | Sub-system or Sub-structure page | System | many-to-many | Changed list flags the FDPSs whose interfacing Systems change. | v23 (2I.2, 6C.20) |
| Resolved by | Issue | Change Record | many-to-many | Changed Change Record flags the Issue. | v23 (2I.2, 2E.10) |
| Constrains | Requirement or TSM | Parameter | many-to-many | Changed Requirement or TSM flags the Parameter (down). | Added (3.4, 3.9) |
| Informed by | TSM or Design Consideration | Lesson Learned | many-to-many | Changed lesson flags the TSM or consideration. | Added (4.3, 6B.4) |
| Governed by | Design Consideration | TSM | many-to-many | Changed TSM flags the consideration. | Added (4.3) |
| Applies to | Design Consideration checklist item | Design Type, Design Sub-team or review stage | many-to-many | None. | Added (4.4) |
| Covers | Design Review | FDPS Revision | many-to-many | A change to a covered FDPS after review flags the review for substantial-change assessment. | Added (6C.2) |
| Records | Review Snapshot | Design Review | one-to-one | None (frozen). | Added (6C.9) |
| Raised at | Action | Design Review | many-to-one | None. | Added (6C.8) |
| Tagged to | Action | FDPS | many-to-many | None. | Added (6C.8) |
| Cross-link | Hub Page | Hub Page | many-to-many | None (backlinks are derived). | Added (5.3) |

## 5. Inference rules summary

| Rule | Inputs (stored) | Output (derived, never stored) | Rule | Ref |
| --- | --- | --- | --- | --- |
| Major Unit | Part Instance or Assembly Instance, Located at a Build Station | Major Unit | The parent of the Build Station register entry. For an Assembly Instance, its aircraft Build Station; its Part Instances are at the Bench of the same Major Unit. | 1.6.1 |
| Fastener home Sub-system | Fastener Part Instance, Secures link | Expected Homed in | The Sub-system of the held Part Instance; any difference is flagged. | 1.6.6 |
| Product Scope of an item | Build Station (or Build Stage or Facility) entry | Product Scope | The Product Scope of the Manufacturing node. | 2C.13 |
| System and System Group | Part Instance, Homed in a Sub-system | System; System Group | The parent and grandparent of the Sub-system entry. The home System is never altered by Supports links. | 1.6.1, 2F.7 |
| FDPS and Design tree position | FDPS Contains links | FDPS; Design Sub-team; Design Team | The single FDPS whose population contains the instance; then the owner and owner's parent. | 1.6.4 |
| FDPS Systems | FDPS population | Set of Systems, System Groups and Major Units | The union over member Part Instances (including those in member Assembly Instances). | 1.7.3 |
| Assembly derived System tags | Assembly Instance, Assembled from | Derived System tags | The union of the home Systems of its Part Instances, shown with a derived badge. | 2F.7 |
| Inherited Requirements | Requirement Part of an EDR; EDR sub_system_tags; optional Allocated to; Satisfied by links | Requirement line items per FDPS, with bases and state | An FDPS inherits every line item of every EDR tagged to a Sub-system in which any of its Part Instances is homed; a line item with Allocated to links flows only where a Part Instance is homed at or below an allocated node; plus Requirements whose Satisfied by link targets the FDPS or one of its items (Direct). State per line item from Line-item Review, default Inherited, not reviewed. Parts and Assemblies reach Requirements only through their FDPS. | 6B.1A, 6B.2, 6B.6, 6B.7 |
| Inherited TSMs | TSM Governs links (Design Type, Discipline, System); Sub-system page applicable_design_types; Design Team applicable_design_types and applicable_disciplines | TSMs and their statements per FDPS, with bases and state | An FDPS inherits a TSM when any route matches (OR): a Part Instance is homed in a Sub-system whose page lists a tagged Design Type (added in v7); a Part or Assembly in it has a tagged design_type or modification_design_type; a Part Instance is homed in a Sub-system of a tagged System; or a tagged Discipline is on the owning Design Team page. One basis per matching route. Every statement is inherited, default Inherited, not reviewed. Part Design Types not listed by the owning Design Team, or not listed on the home Sub-system page, are flagged. | 6B.5, 2B.10, 6B.7 |
| Line-item supersession (auto) | Defined links (Satisfied by to a Part or Assembly Instance; claimed TSM statements naming parts) per FDPS per document | Superseded (auto) Line-item Reviews | When a document has at least one defined link in the FDPS (P2), every line item of it still Inherited, not reviewed with no defined link becomes Superseded (auto); reversed when the last defined link goes (P4). Defined links roll up to FDPS, Sub-system and System pages (P8). | 6B.7A |
| FDPS line-item maturity | Inherited line items; Line-item Reviews; TSM Supersession Confirmations | Reviewed of total; numbers Broken and Superseded; unreviewed count; pending confirmations | Kept, Broken and Superseded (auto) count as reviewed. Stage C entry and the release gate require zero unreviewed line items and zero pending TSM bulk confirmations. | 5.27, 6B.7A, 6C.11, 6C.15 |
| Interfacing Systems | Sub-system and Sub-structure page interfaces; Supports links; System is_structural; FDPS lead_sub_system and interface_breaks | Interfacing Systems per FDPS | The union of (a) the interface lists of the non-structural Sub-systems of its Part Instances; (b) for a Sub-structure FDPS only, the interface lists of every Sub-structure in which its Part Instances are homed; and (c) the Supports-link Systems of its items; less its own home Systems and broken Systems. Never derived from Secures links or geometry. | 6C.20, 6C.21 |
| FDPS interfaces | Secures links; FDPS Contains links | Pairs of FDPSs, with fastener and held Part Instance | A Secures link whose fastener and held Part Instance are in different FDPSs is an FDPS interface, shown on both FDPSs. | 1.6.6, 6C.24 |
| Break approver | FDPS lead_sub_system; Role register | Design Lead | The person holding an active Design Lead assignment whose area is the lead Sub-system (for a Sub-structure FDPS, the lead Sub-structure). | 6C.14, 6C.21 |
| Release block | Compliance Statements; FDPS Revision effectivity | Release allowed or refused | Refused while any Compliance Statement of the FDPS over the revision's range is Non-compliant (6A.17), in addition to the Action gate (6C.11). | 6A.17, 6C.11 |
| Required interface agreements | Interfacing Systems of the covered FDPSs | Systems that must agree at a review | One agreement per interfacing System. | 6C.22 |
| Applicable checklist items | Sub-team stage_sections; project-N/A Disciplines | Checklist items per FDPS and stage | The items listed for the stage on the owning Sub-team page, less those of Disciplines marked not applicable. | 4.4 |
| Applicable considerations | Discipline register; Design Consideration checklist items and their Applies to links | Considerations and checklist items per Part, FDPS and stage | Every Discipline's consideration applies to all designs. Checklist items apply by the same rule as TSMs, filtered by review stage and item properties; items with no Applies to link apply to all. | 4.2, 4.4 |
| Required Discipline agreements | Design Sub-team stage sections of the covered FDPSs | Sign-off team Disciplines that must agree at a review | The union of sign_off_disciplines for the review's stage over the covered FDPSs, less project-N/A Disciplines. | 6C.19 |
| Effective revision lookup | Instance-Revision Links, instance existence | Revision at effectivity E | If E is outside existence, the instance is not shown. Otherwise, return the single link whose range contains E (to = 999 means no upper limit). Zero or several matches is a data error, and is flagged. | 5.17, 6A.3 |
| FDPS Revision effectivity | FDPS Revision effectivity (stored at release) | Effective FDPS revision at E | The single released revision whose range contains E. Releasing a new revision closes the previous range. | 6A.11 |
| Status at effectivity | Existence and revision-link ranges | Present or Not present (with ranges) | Derived for the selected effectivity; never changes the stored status. | 6A.18 |
| Compliance coverage | Compliance Statements, Verification effectivity | Coverage per FDPS and Requirement or TSM | The statements' ranges must tile the released effectivity; each Compliant range must be covered by valid evidence. | 6B.8, 6B.9 |
| Escalation | Issue criteria | Level; forum; rank | Level = the maximum of the five scores; the forum comes from the band; ranking is within the forum. | 2E.3, 2E.9 |

Display rule: inherited Requirements and TSMs are always shown separately from direct links (6B.6). Recorded non-applicability is shown on the inheritance without removing it (6B.7).

## 6. Settled points and points for Daniel to review

### 6.1 Conventions and registers: the eight judgement calls (settled, accepted 10 Oct 2026)

1. Settled: opaque permanent identifiers (PREFIX-SCOPE-NNNNNNN) are kept separate from part numbers and FDPS numbers.
2. Settled: every record carries an automatic record_version, in addition to revision (for Parts, Assemblies and FDPSs) and issue (for documents).
3. Settled: revision letter sequence omitting I, O, Q, S, X and Z, with no separate pre-release revision codes.
4. Settled: confidence held as 0.00 to 1.00, with Low, Medium and High bands derived at 0.50 and 0.80.
5. Settled: "ALL" is held as a single token rather than as a list of every option, so that it automatically includes options added later.
6. Settled: Lifecycle Stage, Discipline and Verification method registers are now defined (v19 Annex B, section 2.2), replacing the v1 placeholders.
7. Settled: Major Unit and Build Station registers also hold End Item, Build Stage, Site and Facility entries for other Product Scopes, rather than having separate registers.
8. Settled: people are directory identities, not a data type.

### 6.2 Project and Effectivity

- Effort and cost impact thresholds are held on Project as tailorable values.
- Serial ranges and build standards are Effectivity mapping records. Stored ranges are always in effectivity numbers.

### 6.3 Part Definition and Part Revision

- Revisions are separate objects, rather than fields on the Part Definition.
- Source and Lifecycle Stage are held on the Part Definition and inherited by its Part Instances. This satisfies "one option of each cross-cutting facet" (2F.3) without storing them twice. Discipline is not applied to items.
- The interchangeability assessment is held on the Change Record linked to each revision.

### 6.4 Part Instance and Instance-Revision Link

- A non-interchangeable change (new part number) closes the old Part Instance's existence range and creates a new Part Instance, linked by replaces. This keeps "exactly one Part Definition" per instance (2D.3).
- Settled (11 Oct 2026, F-11): the Requirement check of 2.4 applies at FDPS level; Part and Assembly Instances need no Requirement of their own.
- Instance-Revision Link is one data type serving both Part Instances and Assembly Instances.
- Superseded (11 Oct 2026, R-04): an Assembly Instance owns one Build Station link, to the aircraft Build Station where it is installed; its Part Instances are Located at the Bench (1.6.1).

### 6.5 Assembly Definition, Assembly Revision and Assembly Instance

- Assembly Revision is added as a data type (6A.14 needs it).
- Assembly part numbers share the part numbering space, with dashes -401 to -799, and may share the stem of their main component (settled, F-36, F-37).

### 6.6 FDPS and FDPS Revision

- FDPS membership is held as Contains links owned by the FDPS, not by the revision. Each FDPS Revision freezes the population at release.
- Review stage status (mandatory in 2F.12) is derived from Design Reviews, not stored.
- The stem breakdown is held as informational fields.

### 6.7 Finish Specification

- Instance overrides are held as links owned by the Part Instance, with mode Add or Replace.
- The finish category register is drawn from the 2D.6 examples.

### 6.8 Requirement, TSM and Compliance Statement

- Settled (11 Oct 2026, F-10, F-11, F-12): Compliance Statement holds compliance, non-compliance and approved non-applicability for each FDPS, Requirement or TSM and effectivity range, with every basis recorded.
- A changed Requirement or TSM flags the Compliance Statements of inheriting FDPSs.
- Settled (F-15): Requirements may be allocated to any System tree node. The v4 rule that TSMs govern Design Types only is superseded (R-02): TSMs are tagged with any of Design Type, Discipline and System and reach an FDPS if any tag matches.
- Superseded (R-02): one TSM record per manual, holding its statements; conformance is claimed per applicable statement on the Compliance Statement.
- A Requirement allocated to a System or higher node is inherited by all Sub-systems below it.
- A change to an Accepted Requirement returns it to Proposed until it is accepted again.

### 6.9 Verification

- basis_revisions records which revisions were analysed, and effectivity records where the Verification is valid evidence (settled, F-12).

### 6.10 Issue

- Effort, cost and schedule are stored as estimates with units and scored by rule. Safety and scope are stored as the selected option (score), with software checks and proposals.
- Ranking within a forum is by level, then by the sum of scores.

### 6.11 Design Review, Review Snapshot and Action

- Reviews cover FDPS Revisions (not just FDPSs), so that the snapshot is unambiguous.
- There is one snapshot per review, with a content hash.
- Action keeps "one design review" as mandatory, following 2F.12. Actions from a Checklist No are raised against the review of that stage. Closure is accepted by the raiser or the chair (settled, F-29).

### 6.12 Lesson Learned and Design Consideration

- A Lesson Learned record is itself the page (page type Lesson Learned). There is no separate Hub Page object.
- Design Consideration extends Hub Page and is the page of its Discipline (one record per Discipline, page type Discipline). Checklist responses are a separate supporting type.

### 6.13 Parameter

- Each parameter has a single owning object. Parameter Iteration is a supporting type, and what-if work is a branch flag.

### 6.14 Hub Page, Production Link and Image

- Design Sub-team stage sections are held as structured blocks on the page.
- The Requirement column of the Production data links table is derived through the source item, not stored.

### 6.15 Authority Register, Baseline, Change Record, AI Query Log and Review Flag

- Authority Register entries are append-only events, and the current master is derived from them.
- Baselines are frozen per FDPS revision, at each release and review snapshot, numbered within the revision, and reference frozen copies (settled, F-32, F-33). They store derived views as frozen values; this is the only place derived values are stored.
- One Change Record type serves all recorded changes, with a change-type register.
- Review Flag is added as a data type, so that flag decisions and pass-on are auditable.
- Saved AI answers are a separate Saved AI Answer type.

### 6.16 Points arising in v2 (for review, except where marked settled)

- Review stage alignment: review stages A, B and C are aligned with Lifecycle Stages 4 Initial System Design, 5 Preliminary Design and 6 Detailed Design, held as a lifecycle_stage field on each review stage entry.
- Lifecycle scope: all eleven Lifecycle Stages are held in the register now, with in_current_scope true for stages 4 to 6 only, so that expanding the scope later needs no data change.
- Discipline and Design Consideration: there is no separate Design Consideration page type; each Discipline's page is its Design Consideration record. Applies to links now refine checklist items rather than the applicability of the consideration, because every Discipline applies to all designs.
- Discipline agreement: Sign-off team agreement is held as a discipline_agreements field on Design Review (one entry per required Discipline), rather than as a separate data type. Consideration only Disciplines are recorded only through the designer's Checklist Responses.
- Settled (10 Oct 2026, Requirements Prompt v20 4.2): Former consideration list. Thermal, Environmental Impact and Sustainability, and Vibration and Shock have no Discipline of their own. They are held as checklist items in existing Design Consideration records: Thermal under Low Observability (moved from System Layout and Integration); Environmental Impact and Sustainability under Materials and Processes; and Vibration and Shock under Structural Analysis (Stress). v19 remaining decision 4 is closed.
- Example register identifiers have been updated to the new register orders (for example Detailed Design is VR-LCS-0006, Structural Analysis (Stress) is VR-DISC-0022, Calculation Analysis is VR-VMETH-0003).
- Superseded (11 Oct 2026): the Thermal placement above is replaced by the split in v23 4.2 (F-01, F-03).

### 6.17 Decisions on Worked Example v1 findings (settled, 11 Oct 2026)

| Findings | Decision | Where applied |
| --- | --- | --- |
| F-01, F-02, F-03 | Thermal split between Low Observability (heat signature) and System Layout and Integration (thermal environment); a project may mark a Discipline not applicable with approval of the Technical Authority for Design. | 3.22, 3.32 Tailoring Record, 2.2 DISC |
| F-04, F-05 | Templates show only the checklist items listed on the Sub-team stage page; a No requires an Action, a Risk or an approved justification before a Pass. | 3.24, 3.32 Checklist Response, 3.36 |
| F-06, F-07, F-08 | Interfaces listed on Sub-system pages, inherited by FDPSs, breakable with reason; one interface agreement per interfacing System. | 3.10, 3.18, 3.24 |
| F-09 | Fastener homing and Supports. | 3.5 |
| F-10, F-11, F-13, F-16 | Requirements and TSMs flow to FDPS level only; compliance per FDPS; all bases recorded. | 3.10, 3.13, 3.15 |
| F-12 | Effectivity on Compliance Statements and Verifications, no gaps or overlaps. | 3.15, 3.16 |
| F-14 | Retrofit and Concession records (Retrofit moved to section 7 by R-03; Concession moved to section 7 by R-13). | 3.33, 3.34, 7 |
| F-15, TSM rule | Allocation to any System tree node; TSMs govern Design Types only (TSM rule superseded by R-02, section 6.18); Design Teams list their Design Types. | 3.13, 3.14, 3.24 |
| F-17 | Modified bought-in Parts carry the modification Design Type. | 3.3 |
| F-18 | Fluid Systems Discipline. | 2.2 DISC |
| F-19, F-20 | Non-applicability approvers; Role register. | 3.15, 3.35 |
| F-21, F-22 | Agreement positions with conditions as Actions; attendees list. | 3.18 |
| F-23, F-29 | Release gate over all Actions, enforced in PLM through Hub confirmation; closure acceptance. | 3.11, 3.20 |
| F-24 to F-28 | Carry-forward, margin notes, added-part rule, several change types with per-FDPS assessment, scoped re-review at the current stage. | 3.11, 3.18, 3.28 |
| F-30 | Stage pages tailored per Production Hub. | 3.24 |
| F-31 to F-34 | FDPS revision effectivity; baselines per FDPS revision with frozen copies; status at a selected effectivity. | 1.2, 3.4, 3.5, 3.6, 3.11, 3.27 |
| Finding 35 | Out-of-scope stages stored and tagged. | 3.17 |
| F-36 to F-41 | Dash ranges and handedness; uniqueness of the full number; bought-in numbering; catalogue clamps as Standard Parts; stored proposals; Assembly numbering fields. | 2.2, 3.3, 3.7, 3.10 |
| F-42, F-43 | Highest Safety Classification; catalogue revisions. | 3.3, 3.4 |
| F-44 | Bench Build Station per Major Unit. | 2.2 BS, 3.5 |
| F-45, F-46 | Override-only Finish Specification valid; highest score applies. | 3.12, 3.17 |
| F-47, F-48, F-49 | Issue Resolved by link; lesson origin and promotion; Part reaches FDPS only through instances. | 3.17, 3.21, 3.3 |
| F-50 | Editorial fixes to examples. | 3.3, 3.5, 3.10, 3.13 |

### 6.18 Decisions on Worked Example v2 remaining findings (settled, 11 Oct 2026)

| Finding | Decision | Where applied |
| --- | --- | --- |
| R-01 | The interface of a structural Sub-system with every System does not cascade. An FDPS inherits interfacing Systems only from the Systems of its own parts plus Structure. Every break of an inherited interface is approved by the FDPS's Design Lead and recorded with its reason (approver superseded by the Design Lead decision of 6.19). | 2.1 is_structural, 3.10, 3.24, 3.35, 5 |
| R-02 | TSMs are tagged with any of Design Type, Discipline and System (each optional, at least one) and reach an FDPS if any tag matches. TSMs are broad documents; conformance is claimed only to the applicable statements, and no non-applicability record is needed for a TSM that applies in part. New Design Type Standard Part. Design Teams list applicable Design Types and Disciplines. Supersedes the v4 rule that TSMs govern Design Types only. | 2.2 DTY and BASIS, 3.3, 3.14, 3.15, 3.16, 3.24, 4, 5 |
| R-03 | Retrofit records and as-embodied or as-manufactured configuration moved to Future Development, with scan comparison; Concessions remain in scope (superseded by R-13: Concessions also moved to section 7). | 2.2 EMB, 3.2, 3.33, 3.34, 7 |
| R-04 | Only the item directly below the FDPS links to an aircraft Build Station; Part Instances within an Assembly link to a Bench Build Station; the Assembly Instance links to the aircraft Build Station, which gives its Major Unit. | 2.1 is_bench, 2.2 BS, 3.5, 3.9, 4, 5 |
| R-05 | Substantial means adversely affects compliance, or degrades form, fit, function or an interface (with the added-interface rule of F-26 retained). | 3.28 |
| R-06 | Fastener instances carry a Secures link to the part they hold, which sets their home Sub-system; structure-to-structure fasteners need no Supports link. | 2.2 PROP, 3.5, 4, 5 |
| R-07 | Bought-in project control number = Project + BI + sequence (for example D-BI-0001), stored with the supplier part number. | 2.2 NUMSCH and TYC, 3.3 |
| R-08 | A part takes its FDPS's stem codes; its own home System is held only in the facet link. | 3.3, 3.7 |

### 6.19 Decisions on Worked Example v3 remaining findings (settled, 11 Oct 2026)

| Finding | Decision | Where applied |
| --- | --- | --- |
| R-09, R-10 | Structure is split into Sub-structures (the Sub-systems of the structural Systems). Each Sub-structure page lists its interfacing Systems, which flow down to all Sub-structure FDPSs in it, over-inclusion accepted. Non-structural FDPSs inherit from their non-structural Sub-system pages (which name the structure they attach to) and Supports links as before. No list is 'interfaces with all'; interfaces are not derived from physical links. | 2.1, 2.2 SUB, 3.10 lead_sub_system, 3.24, 4, 5 |
| R-11 | Design Team pages list applicable Disciplines alongside Design Types; FDPSs owned by the team match TSMs tagged with any of those Disciplines (confirmed). | 3.24, 5 |
| R-12 | Secures links may target a Part Instance in another FDPS, which is an FDPS interface between the two FDPSs. The Fastener item property marks Parts that require a Secures link. | 2.2 PROP, 3.3, 3.5, 3.10, 3.19, 3.27, 4, 5 |
| R-13 | Concessions are part of the manufacturing standard, not the design standard: the Concession data type is moved to section 7 with Retrofit and as-manufactured configuration. A Non-compliant Compliance Statement references its Issue and blocks release for its range. Chosen for the example: non-compliance blocks release for effectivities 1 to 2, rather than making rev B effective for them (Worked Example v4, 5.5). | 3.15, 3.34, 5, 7 |
| R-14 | A claimed TSM statement may omit parts, meaning it is claimed for the FDPS as a whole. | 3.15, 3.16 |
| Role | The FDPS Design Lead role and the FDPS area kind are removed. Breaks are approved by the Design Lead of the FDPS's lead Sub-system; for a Sub-structure FDPS, of its lead Sub-structure. | 3.10, 3.35, 5 |

### 6.20 Decisions on EDRs, line-item inheritance, Lessons Learned and Hub layout (settled, 12 Oct 2026)

| Topic | Decision | Where applied |
| --- | --- | --- |
| EDR | Requirements are line items grouped into Requirement Documents of kind EDR; each line item is Part of exactly one EDR, keeps its own level, and an EDR may mix levels and cover several Systems. | 2.2 DOCKIND, 3.13, 3.13A, 4 |
| EDR Sub-system tag | Many-to-many document-level Sub-system tag; an FDPS inherits EDRs from every Sub-system its Part Instances are homed in, with all line items by default. Allocated to on a line item is kept as an optional narrowing. | 3.13, 3.13A, 5 |
| TSM route | TSMs are not tagged to Sub-systems. The route Sub-system > Design Type > TSM is added alongside the existing Part Design Type match, with the mismatch flag kept; the TSM Discipline and System tags are kept unchanged. | 3.14, 3.24, 5 |
| Breaks | Every inherited line item applies by default and is Kept or Broken; EDR line-item breaks are approved by the Design Lead of the lead Sub-system, TSM statement breaks by a Design Authority. Every non-applicable TSM statement needs a recorded break (replaces the v6 'no record' rule). | 2.2 LISTATE, 3.15, 3.15A, 6C.13 |
| Compliance | Compliance Statements only for Kept line items; claimed TSM statements equal the Kept statements. | 3.15 |
| Maturity gate | No unreviewed line items is both a Stage C entry criterion and a release-gate condition. | 3.15A, 5 |
| Revisions | Line items carry revisions; a new EDR or TSM issue re-flags only changed line items. | 3.13, 3.13A, 3.14, 3.15A |
| Lessons Learned | Mandatory design_type tag and optional sub_system tag; lessons are matched by tag only. | 3.21 |
| Hub layout | Level-appropriate display (documents above FDPS level, line items on FDPS pages); EDR and TSM pages; tree page layout with filter and tree rail, model preview beside the summary, tiles, collapsed categories in page groups (Reviews in the verification group; superseded by 6.23), fixed AI bar, working filters; company colours with dark and light themes as a user setting; Sub-system owner shown as its Design Lead. | 2.2 PAGETYPE, 3.24 |

### 6.21 Decisions R-15 and R-18 (settled; omitted from v7, added in v7.1)

| Finding | Decision | Where applied |
| --- | --- | --- |
| R-15 | The lead Sub-system is set by the owning Design Sub-team and approved by a Design Lead of that Sub-system; a later change is a Change Record of type Lead Sub-system change, which re-runs interface inheritance and flags existing breaks for re-confirmation. | 2.2 CHG, 3.10 |
| R-18 | A cross-FDPS Secures link raises a flag to the owner of the other FDPS, decided Accept or Query; a Query stays open, is shown on both FDPS pages and does not block the link; no link confirmation is required. | 3.31 |

### 6.22 Link maturity (principle and definitions P1 to P8 settled, 12 Oct 2026)

Principle (settled): high-level links (EDR to Sub-systems, TSM via Design Types) flow down; defined links at the lowest level flow up and supersede them; once a level has defined links, unlinked flowed-down line items are Superseded (auto) with no manual break; TSM supersessions need a Design Authority bulk confirmation, EDR supersessions none; manual breaks remain possible before defined links exist; Kept, Broken and Superseded count as reviewed, and pending bulk confirmations block Stage C entry and release. Applied in 2.2 LISTATE, 3.15A, 3.15B, 5.

Settled definitions and judgement calls (accepted by Daniel as written, 12 Oct 2026):
- P1 Defined link. A defined link is: for an EDR line item, a Satisfied by link from that Requirement to a Part Instance or Assembly Instance of the FDPS; for a TSM statement, the statement claimed on a Compliance Statement of the FDPS with at least one named Part Instance or Assembly Instance of the FDPS (3.15 statements_claimed parts). A Satisfied by link to the FDPS as a whole is not a defined link.
- P2 A level has defined links. For one FDPS and one document (EDR or TSM), the level has defined links when at least one line item of that document has a defined link within that FDPS. Supersession is evaluated per FDPS per document; a defined link in one document never supersedes line items of another document, and a defined link in one FDPS never affects another FDPS.
- P3 Manual decisions prevail. A line item already Kept or Broken by a manual review keeps that state; automatic supersession applies only to line items still Inherited, not reviewed. A Kept line item without a defined link, in a level that has defined links, is flagged for the FDPS owner.
- P4 Reversal. If the last defined link of a document in an FDPS is removed, its Superseded (auto) line items return to Inherited, not reviewed, and any DA bulk confirmation covering them lapses.
- P5 New and changed line items. A line item added or changed by a new issue (6B.10) in a level that already has defined links is Superseded (auto) unless it gets a defined link, and is listed on the FDPS page as newly superseded; for a TSM it needs a fresh DA bulk confirmation.
- P6 DA bulk confirmation scope. One confirmation record per FDPS per TSM, covering the full current set of Superseded (auto) statements. Any change to the set (a new supersession, or a statement regaining a link) requires a new confirmation. The Design Authority may reject individual statements from the set; a rejected statement returns to Inherited, not reviewed and must be Kept or Broken manually.
- P7 Superseded line items need no Compliance Statement, and are shown on FDPS pages greyed, with the defined links that superseded them.
- P8 Roll-up. Defined links roll up (flow UP) from Part and Assembly Instances to the FDPS, its Sub-systems and Systems as derived data; pages above FDPS level show, per document, how many FDPSs have defined links (document maturity).

### 6.23 Hub page layout (settled, 12 Oct 2026, mockup v8)

| Topic | Decision | Where applied |
| --- | --- | --- |
| Page groups | Five groups with colour key: Requirement (navy, left: EDRs, TSMs); Verification (teal, right: Compliance, Verifications, Reviews); Product (grey: on Sub-system pages an FDPS list only, each FDPS a link with status chip and Build Stations, no Part Instances); Considerations (violet #5B3F8C / dark #C7B3EE: Interfacing Systems, Disciplines and Stakeholders); Working Data (amber #7A4E00 / dark #F0C674, at the bottom: Issues, Lessons Learned as separate categories). | 3.24 layout |
| Links | No dedicated Links area or 'Other' group; every item with a page is a link in place; the tree is for navigation. | 3.24 layout |
| Summary | Structure and parent, Design Lead (owner), Design Sub-team and ID in the summary, each a link; tiles FDPS, EDRs, TSMs, Non-compliant, Open Issues, Lessons (no Part Instances tile). | 3.24 layout |
| Mobile | Groups stack Requirement, Verification, Product, Considerations, Working Data. | 3.24 layout |
| FDPS pages | Same five groups at FDPS level (line items, Part Instances); layout to be confirmed when the FDPS page is designed. | 3.24 layout |

### 6.24 Users, access roles and permissions (settled and confirmed by Daniel, 12 Oct 2026, including permission bundles)

| Topic | Decision | Where applied |
| --- | --- | --- |
| Access roles | Named roles Admin, Design Lead, Design Authority, Engineer, Viewer bundle permissions, assigned per project; Admin may add one-off grant or deny overrides. | 3.38, 3.39, 3.41 |
| Effectivity | All effectivities of the project by default; Admin may restrict. Confirmed: a restriction limits both viewing and editing; data with no effectivity stays open. | 3.39, 3.40 |
| Ownership | One accountable Owner plus optional Contributors on every work item; free-text owners replaced by Users. | 1.2, 3.37 |
| Authority roles | Confirmed: kept as the separate Role register; an authority role needs a matching access role; Admin may hold either; Technical Authority for Design, Design Approver and Discipline Lead sit on top of Engineer. | 3.35, 3.38 |
| Pages | Admin page (user list, edit panel, audit); user page placeholder. Confirmed: framework administrator flag kept alongside per-project Admins. | 3.37 framework_admin |
| Permission bundles | Requirements Prompt Annex B.6, confirmed by Daniel, 12 Oct 2026. | 3.24 (page types Admin and User) |

## 7. Future Development (not in current scope)

These data types are reserved for the capabilities of Requirements Prompt v23 section 7. They are not implemented or validated in the current scope.

| Data type | Purpose | Proposed key fields | Ref |
| --- | --- | --- | --- |
| Concession (CON) | Accepts a known non-conformance of a built aircraft with its design standard (manufacturing standard, v23 7.4). If it needs a re-design, that design solution applies to the serial-number aircraft concerned; if not, Design is one of the signing authorities | fdps; requirement or design data not met; effectivity (serial-number aircraft); description; limitations; expires; redesign: ref(Change Record or FDPS Revision) 0..1; approvals [{authority, by, at}], including Design where no re-design is needed; status: Proposed, Approved, Expired, Withdrawn | 7.4 |
| Retrofit (RT) | Applies a later revision or added Part Instances to built effectivities | fdps; from_revision and to_revision (FDPS Revision); effectivity; change_records; instruction_ref (Production Link); embodiment [{effectivity_number, status: reg(EMB), date, recorded_by}]; status | 7.1 |
| As-embodied configuration (derived view) | The as-designed configuration plus embodied Retrofits, per built effectivity | derived from Retrofit embodiment and baselines; never stored except in frozen records | 7.2 |
| Manufacturing deviation | An accepted as-manufactured difference on one effectivity | effectivity_number; affected Part Instances; description; disposition; approved_by | 7.2 |
| Scan | A scan of a manufactured part or assembled aircraft | effectivity_number; scanned item (Part Instance, Assembly Instance or FDPS); origin (scanner, file, issue); taken_at | 7.3 |
| Scan Difference | One difference between a Scan and the design standard | scan; Part Instance; measured deviation (qty); tolerance (qty); within_tolerance (bool); review flag | 7.3 |

