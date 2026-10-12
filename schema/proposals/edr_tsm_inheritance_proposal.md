# Change proposal: EDR documents, document-level inheritance and line-item breaks

Status: FINAL for D1 to D16 (settled by Daniel, 12 Oct 2026); link-maturity definitions P1 to P8 settled (accepted by Daniel as written). Applied in Requirements Prompt v24.2 and Data Schema v7.2. Against: Requirements Prompt v23 and Schema v6. Mockup: /workspace/style-mockups/subsystem/v5.html, tsm/*.html, fdps/fd-d-0000017-line-items.html (all local, demo data marked).

## 1. Decisions this proposal records (settled by Daniel, 12 Oct 2026)

- D1. Requirement line items are grouped into documents called EDRs (Engineering Design Requirements). One EDR may cover several Systems (intended to be split by System, overlap allowed).
- D2. EDRs carry a document-level tag to one or more Sub-systems (many-to-many).
- D3. TSMs are NOT tagged to Sub-systems. TSMs are tagged to Design Types. Design Types are linked to Sub-systems; an FDPS reaches TSMs by the route FDPS › Sub-system › Design Type › TSM.
- D4. The TSM Discipline and System tags are KEPT, unchanged from the current rules (v23 6B.5): a TSM still also reaches an FDPS by a System tag (a Part Instance homed in a Sub-system of that System) or a Discipline tag (listed on the owning Design Team's page). Settled; not an open question.
- D5. Each FDPS inherits ALL line items (EDR requirements, TSM statements) of every document that reaches it, by default. As the design matures the FDPS breaks links to irrelevant line items, each with a recorded reason, approved for EDR line items by the Design Lead of the FDPS's lead Sub-system (or lead Sub-structure), and for TSM statements by a Design Authority (see D10).
- D6. Page-level display rule: above FDPS level (Sub-system, System, Group pages) requirement data is shown as documents (EDR and TSM lists linking to their own pages), and verification as summaries per document and per FDPS. Only FDPS pages list line items. Reviews stay in the Verification group.
- D7. TSMs get their own pages, like EDR pages.

## 2. Schema changes (v6 -> v7)

### 2.1 New record type: Requirement Document (3.x)
| Field | Type / card. | Notes |
|---|---|---|
| doc_kind | reg(DOCKIND); 1 | EDR (only value now; extensible) |
| doc_code | string; 1 | e.g. EDR-FUE; unique in hub |
| title, issue, status, owner | as common | status Draft / Released / Superseded |
| sub_system_tags | reg(SUB); 1..n | document-level tag, many-to-many (D2) |
| links | Contains -> Requirement; 1..n | inverse of Part of |

### 2.2 Requirement (3.13)
- New link `Part of` -> Requirement Document, card. exactly 1.
- `Allocated to` (6B.2): kept as an optional narrowing of the EDR Sub-system tag (D8).

### 2.3 TSM (3.14)
- Design Type tags (`Governs` -> DTY) become the primary inheritance route (D3). Discipline and System tags kept (D4). No Sub-system tag on TSMs.
- TSM statements get a stable id (clause) so they can be line items with their own status.

### 2.4 New link or register: Sub-system -> Design Type
- Each Sub-system page lists its applicable Design Types (`Uses Design Type`, 0..n). Owned by the Sub-system Design Lead.

### 2.5 New record type: Line-item Applicability (break record)
One record per FDPS per inherited line item whose status is not the default.
| Field | Notes |
|---|---|
| fdps | ref FDPS |
| line_item | ref Requirement, or TSM + clause |
| state | Kept (reviewed, applies) / Broken (does not apply) |
| reason | text; required when Broken |
| author, approved_by, approved_at | approver checked against Role register: Design Lead of the FDPS lead Sub-system |
| basis | the inheritance routes at the time (Sub-system tag; Sub-system › Design Type; System tag; Discipline) |
| reconfirm_flag | set when population, lead Sub-system, document issue or tags change |

Derived state with no record: `Inherited, not reviewed`. `Direct` (Satisfied by link) remains as today and is shown alongside.

### 2.6 Compliance Statement (3.15)
- For an EDR line item: one statement per FDPS, requirement and effectivity range (unchanged), only for Kept items.
- For a TSM: `statements_claimed` must equal the set of Kept statements (D11).
- Broken items need no Compliance Statement; a whole Requirement or TSM with all items broken replaces the current "Not applicable" statement (D10).

## 3. Rules (new or changed requirement text)

- R-A Inheritance (replaces 6B.2 flow-down for EDRs): an FDPS inherits every EDR tagged to a Sub-system in which at least one of its Part Instances is homed (Q2), with all its line items.
- R-B TSM inheritance (amends 6B.5): a TSM reaches an FDPS if any route matches (OR, as now): (i) Design Type route: the TSM's Design Type is linked to a Sub-system in which the FDPS has a Part Instance homed (new, D3); (ii) Design Type of a Part in the FDPS population, including modification Design Types (2B.10, F-17) and Standard Part (1.10.1) (current); (iii) System tag (current, kept, D4); (iv) Discipline tag via the owning Design Team page (current, kept, D4, R-11). All matching routes are bases (6B.6). See Q5 on (i) vs (ii).
- R-C Default all line items; maturity = reviewed (Kept + Broken) / total, shown on FDPS pages and in review templates. Stage C entry criterion and release-gate condition: "no line item Inherited, not reviewed" (D13).
- R-D Breaks: reason, author, approver (Design Lead of lead Sub-system or Sub-structure), date. Broken items stay visible; flagged for re-confirmation when the FDPS population, lead Sub-system, the document issue or the tags change. New line items added by a document issue arrive as Inherited, not reviewed, and flag the FDPS.
- R-E Compliance only on Kept items; release gate (6A.17) counts Kept items only, and blocks release while any item is unreviewed at stage C (if R-C adopted).
- R-F Page-level display (D6): Sub-system and higher pages list EDRs and TSMs as documents with route chips (e.g. "Fuel Feed › Pipework", "System tag: Fuel"), compliance summarised per document per FDPS, verifications per document, reviews per FDPS. FDPS pages list line items with status Kept / Inherited, not reviewed / Broken / Direct.
- R-G TSM pages and EDR pages: code, title, issue, tags, statements or line items, FDPSs inheriting it with compliance summary.

## 4. Relationship to settled rules

- Design Teams list Design Types and Disciplines (6B.5, R-11): kept. The new Sub-system › Design Type link is an additional list on Sub-system pages. A Part whose Design Type is on neither its Design Team list nor its home Sub-system list should be flagged (extends the existing 6B.5 flag).
- TSMs reach an FDPS on any matching Design Type / Discipline / System tag (6B.5, R-02): kept, OR-combined; the Sub-system › Design Type route is added (D3, D4).
- Inherited interface breaks (6C.21, R-01, R-15): the line-item break reuses the same approver and re-confirmation pattern.
- TSM conformance to applicable statements only (6B.11, R-14): becomes explicit per statement (Kept / Broken) instead of implicit.
- Non-applicability (6B.7, 6C.13): superseded for line items by breaks (D10).

## 5. Former open questions, now settled (Daniel, 12 Oct 2026)

- D8 (was Q1). Line-item allocation to System tree nodes is kept as an OPTIONAL narrowing of the EDR Sub-system tag.
- D9 (was Q2). An FDPS inherits EDRs from EVERY Sub-system its Part Instances are homed in.
- D10 (was Q3). EDR line-item breaks are approved by the Design Lead of the FDPS's lead Sub-system; TSM statement breaks by the Design Authority. 6C.13 rewritten accordingly.
- D11 (was Q4). Every non-applicable TSM statement needs a recorded break; this replaces the 6B.11 "no record" rule.
- D12 (was Q5). The Sub-system > Design Type > TSM route is ADDED alongside the existing Part Design Type match (union); the mismatch flag is kept.
- D13 (was Q6). "No unreviewed line items" is both a Stage C entry criterion and a release-gate condition.
- D14 (was Q7). The level stays on each line item; an EDR may mix levels.
- D15 (was Q8). A new EDR issue re-flags only CHANGED line items; line-item revisions are tracked.

## 5A. Link maturity (Daniel, 12 Oct 2026)

- D16. High-level links (EDR to Sub-systems, TSM via Design Types) let work be linked before it is defined and flow DOWN. As the design matures, defined links are made at the lowest level (Part and Assembly Instances); they flow UP and SUPERSEDE the flowed-down links. Once a level has defined links, flowed-down line items nothing links to are Superseded (auto), with no manual break. TSM supersessions need a Design Authority BULK confirmation; EDR supersessions need none. Manual breaks (reason and approver) stay possible before defined links exist. The gate (Stage C entry and release) counts Kept, Broken and Superseded as reviewed; pending DA bulk confirmations block it. New state Superseded (auto) on the Line-item Review; new record TSM Supersession Confirmation.

Settled definitions and judgement calls (accepted by Daniel as written, 12 Oct 2026):
- P1 Defined link. A defined link is: for an EDR line item, a Satisfied by link from that Requirement to a Part Instance or Assembly Instance of the FDPS; for a TSM statement, the statement claimed on a Compliance Statement of the FDPS with at least one named Part Instance or Assembly Instance of the FDPS (3.15 statements_claimed parts). A Satisfied by link to the FDPS as a whole is not a defined link.
- P2 A level has defined links. For one FDPS and one document (EDR or TSM), the level has defined links when at least one line item of that document has a defined link within that FDPS. Supersession is evaluated per FDPS per document; a defined link in one document never supersedes line items of another document, and a defined link in one FDPS never affects another FDPS.
- P3 Manual decisions prevail. A line item already Kept or Broken by a manual review keeps that state; automatic supersession applies only to line items still Inherited, not reviewed. A Kept line item without a defined link, in a level that has defined links, is flagged for the FDPS owner.
- P4 Reversal. If the last defined link of a document in an FDPS is removed, its Superseded (auto) line items return to Inherited, not reviewed, and any DA bulk confirmation covering them lapses.
- P5 New and changed line items. A line item added or changed by a new issue (6B.10) in a level that already has defined links is Superseded (auto) unless it gets a defined link, and is listed on the FDPS page as newly superseded; for a TSM it needs a fresh DA bulk confirmation.
- P6 DA bulk confirmation scope. One confirmation record per FDPS per TSM, covering the full current set of Superseded (auto) statements. Any change to the set (a new supersession, or a statement regaining a link) requires a new confirmation. The Design Authority may reject individual statements from the set; a rejected statement returns to Inherited, not reviewed and must be Kept or Broken manually.
- P7 Superseded line items need no Compliance Statement, and are shown on FDPS pages greyed, with the defined links that superseded them.
- P8 Roll-up. Defined links roll up (flow UP) from Part and Assembly Instances to the FDPS, its Sub-systems and Systems as derived data; pages above FDPS level show, per document, how many FDPSs have defined links (document maturity).

## 6. Validation checks (gate)
1. Every Requirement has exactly one Part of link; every Requirement Document has >= 1 line item and >= 1 Sub-system tag.
2. No TSM carries a Sub-system tag; every TSM has at least one tag (Design Type, Discipline or System).
3. Every Broken record has reason, author, approver and date; approver holds Design Lead for the FDPS's lead Sub-system at that date (Role register).
4. No Compliance Statement for a Broken item; every Kept item has Compliance Statements covering the released effectivity with no gaps (6B.8).
5. TSM statements_claimed equals the Kept statements of that TSM for the FDPS.
6. Flag: Part Design Type on neither its Design Team list nor its home Sub-system's Design Type list.
7. Flag: items Inherited, not reviewed at stage C (blocks Stage C entry and release, D13).
8. Re-confirmation flags raised on population, lead Sub-system, tag or document-issue change.

## 7. Glossary
- EDR (Engineering Design Requirements): a Requirement Document grouping requirement line items, tagged at document level to one or more Sub-systems; FDPSs in those Sub-systems inherit all its line items by default and break those that do not apply.
- Line item: one requirement of an EDR, or one statement (clause) of a TSM.
- Break (line item): a recorded, approved decision that an inherited line item does not apply to an FDPS.

## 8. Demo data used in the mockup (not in Project D)
- data/Requirement_Document.v5.demo.json: EDR-FUE, EDR-PP, EDR-STR, EDR-SST grouped by number prefix, with demo Sub-system tags.
- data/SubSystem_DesignType.v5.demo.json: demo Sub-system › Design Type links (Fuel Feed: Pipework, Bought-in Equipment, Standard Part, Metallic - Machined).
- Line-item statuses derived from existing Compliance Statements: claimed or Compliant = Kept; Not applicable = Broken (approver shown as the lead Sub-system Design Lead user:m.ellis, original approver noted); other TSM statements = Inherited, not reviewed. Result for D2822001-801: 15 of 21 reviewed, 3 broken, 6 not reviewed.
