# Walk return: run C, walker 3, dBoundRoles to dMindYourWords

**Serves:** research PLAY-dClosedLoop-1

Dispatch 187's return, verbatim, any H1 demoted to bold. Its handoff is `prompts/prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-28-spec-reviewer.md`, and its use is in
`build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`.

---

The chain shipped and failed because one of these clauses names a measured acceptance or a retirement but leaves out the bar or the by-value readers its settling record fixes, so the build passes on a test that cannot fail. Examples: the map replay with no loss bar (0228), the reuse benchmark with no threshold (0239), the `reuse_lookup` retirement with no by-value readers (0240), and the resolve check that is green on an empty population (0241).

### C3-F1 — P18's ranking of a fork's options is carried by no clause
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0176
- **Class:** K5, c5
- **Severity:** high
- **Evidence:** v2 [principles] P18 says: "Agents resolve forks by the most feature-rich option, then the most expandable, with a full record … only options the core admits are options". Clause 0176 says only: "every fork resolved by the role that meets it and recorded, or held as `run.on-owner-question` says (LR-3)". The other clause in P18's row is 0390, which says only "fork resolution by `design.forks`". `grep -c 'feature-rich'` on v2 returns 4 hits, none of them in a clause. Stage 0 raised this as its K5 lead.
- **Consequence:** dBoundRoles builds fork resolution with no ranking rule and no "admitted options only" check. An unattended role can pick any option and still pass. This is the principle's core rule.
- **Fix:** Add the ranking (most feature-rich, then most expandable), the core-admitted option set and the full record to 0176. Add a planted fork whose recorded pick is not the top-ranked admitted option, and see it red.

### C3-F2 — `instructions.task-charter` is read by no clause, though dBoundRoles owns it
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0180
- **Class:** K4
- **Severity:** medium
- **Evidence:** v2 [policies]: "`instructions.task-charter` | when-not-static, always | … the single-carry check refuses `always` on a backend that loads the static block … | dBoundRoles". systems [design-instruction] says: "The single-carry check reads `instructions.task-charter` and the harness kind". Clause 0180 says only: "the role static block carried once per spawn". Stage 0's K4 lists the key as "read by no chain clause and no item".
- **Consequence:** The single-carry check is built without its key. Either `always` is accepted where the charter loads twice, or the key's value never routes.
- **Fix:** Have 0180 name `instructions.task-charter` and its refusal of `always` on a static-block backend, seen red on a planted `always`.

### C3-F3 — gap-roles-20, the static block's budget covering only its base body, is carried by no clause
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0180
- **Class:** K8
- **Severity:** low
- **Evidence:** gap-register gap-roles-20 says: "The static block's budget covers its base body only". research-instruction-writing-b N3 says: "The 2,487–4,220 B charter blocks per role sit outside `BODY_CEILINGS`". In code, `tools/roles/check_roles.py:84` reads "Bytes of each slot's BASE body". dBoundRoles owns the gap, but no clause of 0166–0191 budgets the whole rendered block.
- **Consequence:** The gap stays open after its owner lands, and the rendered charter blocks remain unbudgeted.
- **Fix:** Extend 0180: the budget covers the whole rendered static block, seen red on a planted charter block that pushes a role over its ceiling.

### C3-F4 — Replacing the protocol pointers omits the same-unit re-point of the machinery that asserts them
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0199
- **Class:** K10
- **Severity:** medium
- **Evidence:** layer-roles [tags] says: "The unit that slices them re-points that machinery in the same unit: `CARRIED_SECTIONS`, `check_roles.py` R0 …, R5 and R10 …, and `render_agents.py`'s self-test arm 4". Clause 0199 says only: "the role files' re-verification orders and protocol pointers replaced by rendered slices". In code, `tools/roles/roles_lib.py:67` reads `CARRIED_SECTIONS = ("Protocols", "Facts")`. `check_roles.py:169` reads the carried Protocols body, and `render_agents.py:83,335` asserts the carried text.
- **Consequence:** Built from the clause, the slicing unit leaves R5, R10 and the self-test asserting the Protocols carry. The roles catalogue goes red, or the whole-document carry survives beside the slices.
- **Fix:** Name the four consumers in 0199 and require them re-pointed in the same unit.

### C3-F5 — Five keys dFurnishedOrders owns are read by none of its clauses, three of them guard-bearing
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0202
- **Class:** K4
- **Severity:** medium
- **Evidence:** v2 [policies] gives dFurnishedOrders `annotations.delivery` (work-order, on-demand, off), `roles.orientation.house-index` (handed, pointer, off), `instructions.slices` (handed, pointer), `retrofit.slot-bytes` (512, 1024, 2048) and `memory.map-unfold` (item-declared, none, all). Stage 0's K4 lists all five as unread, three of them guard-bearing. Clauses 0192–0211 name none of them. 0202 says "legacy slot in its four states" with no cap key, and 0203 says "the unfolds each item declares (PM-6)" with no key.
- **Consequence:** Each key's non-default value never routes. The legacy slot's 1 KB cap (systems [cross]) and the code-notes delivery have no switch.
- **Fix:** Name each key in the clause that builds its slot: 0202 for `retrofit.slot-bytes`, 0209 for `annotations.delivery`, 0199 for `instructions.slices`, 0203 for `memory.map-unfold`, and a slot clause for `roles.orientation.house-index`. Each value is routed and seen.

### C3-F6 — Role metrics are written into the value ledger, which a later build registers, with no stand-in
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0201
- **Class:** K6
- **Severity:** medium
- **Evidence:** Clause 0201 says: "role metrics per role and item into the value ledger". layer-memory [contract] says: "value ledger | dCalibratedLens | a generated library view". 0459 (dCalibratedLens) builds "the shared value ledger". dCalibratedLens is no ancestor of dFurnishedOrders, whose only parent is dBoundRoles.
- **Consequence:** dFurnishedOrders cannot be specced or landed in order (c1-like). Its writer has no registered kind to write.
- **Fix:** Have 0201 write a metrics record dFurnishedOrders owns, which dCalibratedLens's ledger reads later. Alternatively, add a stand-in until 0459 lands.

### C3-F7 — The memory slices read a sibling build's index and keys with no stand-in
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0202
- **Class:** K6
- **Severity:** medium
- **Evidence:** Clause 0202 says: "the work order's memory slices … each under its own budget and its own answer (systems `[cross]`)". systems [cross] says the slices are "priced by `memory.item-budget`. Over it, they are answered by `memory.over-budget`", both owned by dTotalRecall, and sections resolve through dTotalRecall's `record show` (0220). dTotalRecall is a sibling, not an ancestor. Sibling clauses carry stand-ins ("not installed until dTotalRecall's renderer lands" in 0203, the same for 0208), but 0202 has none.
- **Consequence:** The slot cannot be built in order, or it is built against a section index that does not exist yet.
- **Fix:** Add a stand-in: the memory slot renders "not installed" until dTotalRecall's section extractors land, the same way 0203 and 0208 do.

### C3-F8 — The answered-call hook omits the verifier exemption, so the default `refuse` blocks a verifier reading its subject
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0197
- **Class:** K10
- **Severity:** medium
- **Evidence:** layer-roles [trust] item 10 says: "A verifier's read of its subject is never an answered call, and neither is a read the packet does not cover". It also says: "Below CLI 2.1.295, a rule on an ungated tool … stays open when its hook fails … a failure is recorded". Clause 0197 says only: "the answered-call hook (`roles.answered-calls`)". `roles.answered-calls` defaults to `refuse`.
- **Consequence:** A reviewer's or tester's read of its handed subject at the same blob is refused, and verification stalls. The fail-open window also goes unrecorded.
- **Fix:** Carry both rules in 0197. See it green on a planted verifier read of its subject, and see a recorded failure on a planted hook crash.

### C3-F9 — Typed relations drop the `depends-on` cycle check and the pending-target rule
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0217
- **Class:** K10, c3
- **Severity:** medium
- **Evidence:** layer-memory [relations] says: "every relation's target must exist, and `depends-on` must form no cycle … A target found nowhere is pending, not red, until its build lands". gap-mem-07 says: "… no cycle check". Clause 0217 says: "typed relations (…), inverted, checked both ways and rendered as the relation graph".
- **Consequence:** A `depends-on` cycle passes the check, leaving gap-mem-07 open. Otherwise a target on another node's unlanded branch is red, refusing legitimate work.
- **Fix:** Add both rules to 0217: red on a planted two-build cycle, and pending on a planted target on another node's branch.

### C3-F10 — The slug grammar omits "binds new mints only", BUILD_SLUG_RE's derivation and the named flips
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0216
- **Class:** K10
- **Severity:** medium
- **Evidence:** layer-memory [names] says: "A changed grammar binds new mints only. Existing slugs and ids keep their form, every reader accepts both, and the grammar in force at minting is recorded with each slug". It also says "`BUILD_SLUG_RE` … becomes derived from the `builds.slug-*` keys" and "The flips are named: `slug-words` 1 and 3, …". Clause 0216 says only: "proven by flipping the grammar in a scratch clone".
- **Consequence:** A grammar flip makes every reader reject existing slugs and ids across the tree (a migration across a drain). The flip test is also unspecified, so it can pass on one flip.
- **Fix:** Carry the new-mints-only rule, the recorded grammar per slug, the derived `BUILD_SLUG_RE` and the named flip set in 0216.

### C3-F11 — The code record's re-timing has no losing bound
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0219
- **Class:** K10
- **Severity:** medium
- **Evidence:** v2 [owed] says: "the code record's cold derivation re-timed at dTotalRecall's first unit: over 30 s or over 1 MB loses, on gov's tree and on a planted adopter-scale fixture". Clause 0219 says only: "re-timed on a planted adopter-scale fixture (the shape audit)".
- **Consequence:** The re-timing cannot fail, so an over-budget derivation ships.
- **Fix:** Put the 30 s and 1 MB loss bound, on both trees, into 0219.

### C3-F12 — The acceptance re-measure has no target or window
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0223
- **Class:** K10
- **Severity:** medium
- **Evidence:** systems [design-memory-structure] says: "Thirty days after landing, the median memory bytes per agent that reads memory are below 33 KB … Why the first measure could not fail". Clause 0223 says only: "the acceptance re-measure counted over every read channel".
- **Consequence:** The measure has no pass bar, which repeats the "could not fail" defect the record already corrected.
- **Fix:** Add "median below 33 KB, 30 days after landing" to 0223.

### C3-F13 — The map's losing replay has no loss conditions
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0228
- **Class:** K10, c3
- **Severity:** high
- **Evidence:** project-map [test] says: "The map loses, and is not built, if any of these holds: the recall of the known set rises by less than the twin runs' difference plus 5 items; the median of existence searches per lens falls by less than one; the bytes read before the first act rise by more than the map's own bytes". Clause 0228 says only: "the replay with the map and without at its first unit … so a losing map is never built".
- **Consequence:** "Losing" is undefined, so the replay certifies the map whatever it scores, and the routed loss path never runs.
- **Fix:** Carry the three loss conditions, and the twin runs they compare against, in 0228. The same applies to 0253's extension to code.

### C3-F14 — Renaming the Serves kind `journal` to `log` ships with no adopter alias step
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0231
- **Class:** K10
- **Severity:** high
- **Evidence:** memory-plan [integration] says: "distribution | dTotalRecall's upgrade steps in each adopter: the `journal` alias, and the retag step". [migration] says: "the `journal` kind is read through its alias". Clause 0229 says: "the Serves kind `journal` renamed `log`". Clause 0231 lists only "the `--new-build` and `--new-spec` scaffold verbs …, an adopter's README front matter graded …, and the retag step".
- **Consequence:** After update, an adopter's records carrying `**Serves:** journal` (1,436 such records in gov) fail the Serves grading or lose their kind. This breaks P38.
- **Fix:** Add the `journal` alias upgrade step to 0231, seen on a planted adopter record with `Serves: journal`.

### C3-F15 — dTotalRecall owns gap-mem-23 (touch-drop wired to nothing), but no clause of it carries the gap
- **Address:** architecture-v2 [chain] dTotalRecall row, Gaps owned (`gap-mem-23`)
- **Class:** K8
- **Severity:** medium
- **Evidence:** gap-mem-23 says: "`--drop-affordance-exempt` has no caller in `tools/` …". Grepping tools/, skills/ and .githooks/ finds it only inside `tools/codebase-map/map_diff.py` and its README. retrofit's chain table says: "dScopedBuild | … the touch join as `build.scope`'s one check …, calling the map's touch-drop". None of 0212–0237 mentions the touch-drop.
- **Consequence:** The gap's owner lands without closing it, and its actual closer (dScopedBuild) does not own it.
- **Fix:** Move gap-mem-23 to dScopedBuild, which completes the closure and descends from dTotalRecall, by the register's own rule. Alternatively, add a dTotalRecall clause wiring the drop.

### C3-F16 — Memory keys dTotalRecall owns are read by no clause, one of them guard-bearing
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0220
- **Class:** K4
- **Severity:** medium
- **Evidence:** v2 [policies] lists `memory.over-budget` (refuse, report, off, exempt from `budgets.enforce`), `memory.superseded-slices` (refuse, mark) and `memory.map-overflow` (degrade, refuse), all dTotalRecall's. systems' checks table gives "superseded slices | a superseded decision handed to a builder". Clause 0220 says "reported when exceeded, MS-3" without the key. No clause carries superseded slices, and 0225 says "degraded in a fixed order" without the key or `refuse`. Stage 0's K4 lists all three.
- **Consequence:** `refuse` and `off` never route, the superseded-slice check is never built, and the exemption from `budgets.enforce` is lost.
- **Fix:** Name the three keys with their values and checks, in 0220 and 0225.

### C3-F17 — The reuse scout's acceptance re-runs the benchmark with no threshold
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0239
- **Class:** K10, c3
- **Severity:** high
- **Evidence:** layer-memory [reuse] says: "acceptance re-runs aScoutedSeam's 24-case benchmark against the built index and entries, and must meet M1c's 16". research-scoutedseam-apply measured "held-out set … m1c 8/12". Clause 0239 says: "accepted by re-running aScoutedSeam's benchmark and its twelve held-out cases …", with no bar.
- **Consequence:** The acceptance passes at any score, so a house index that loses to today's 13/24 checklist scout ships.
- **Fix:** Put the pass bar in 0239, on the tuning set and on the 12 held-out cases.

### C3-F18 — `reuse_lookup.py` is retired without its by-value readers
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0240
- **Class:** K10, c3
- **Severity:** high
- **Evidence:** layer-memory [reuse] lists the by-value readers: "hygiene check 12's §10 arm accepts the token `reuse_lookup` as reuse evidence (`SPEC10_EVIDENCE_CUTOFF`) … `MAP_CLI` … the `reuse-probed` DoD item". In code, `tools/memory-tree/check-memory-hygiene.sh:2474` reads `index(s10p, "reuse_lookup") > 0`, `tools/unattended/kit.toml:174` declares `MAP_CLI`, and `tools/unattended/PROTOCOL.template.md:356` declares `reuse-probed`. Clause 0240 says only "with their readers rewritten".
- **Consequence:** After the tool retires, check 12 still certifies a spec's reuse audit on a citation of a retired tool.
- **Fix:** Name the by-value readers in 0240. See red a planted spec citing `reuse_lookup` after the new cutoff.

### C3-F19 — The resolve check can go green on an empty population
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0241
- **Class:** K10, c3
- **Severity:** high
- **Evidence:** layer-memory [annotations] says: "Its first green proves nothing … the population is empty. Three planted red cases are owed … a dangling `refs=` id, a dangling `refs=` path, and a `gov:feature` tag with no entry … The check asserts a non-empty population once the first annotation lands". Clause 0241 says: "the generated annotation index and its resolve check (`annotations.grammar`), the shipped-evidence signal re-checked first".
- **Consequence:** A gate never seen red, over an empty population, is read as coverage, against the charter's [gate] rule.
- **Fix:** Carry the three planted reds and the non-empty assertion in 0241.

### C3-F20 — README routing and the relation graph are each built by two builds
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0242
- **Class:** K8
- **Severity:** medium
- **Evidence:** Clause 0242 (dLinkedLibrary) says: "the generated views: README routing, the relation graph, …". 0215 (dTotalRecall) says: "a generated routing region by purpose", and 0217 (dTotalRecall) says: "… rendered as the relation graph". memory-plan [practice] says: "every node gov ships names one owning build".
- **Consequence:** Two specs build one view, and the one-owner check reds, or two renderers diverge.
- **Fix:** Drop the two views from 0242, or have 0242 say it consumes dTotalRecall's renders.

### C3-F21 — The touched-block comment budget is carried by no clause
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0244
- **Class:** K8
- **Severity:** medium
- **Evidence:** systems [design-annotations] says: "Budget. A block a commit touches is at most 12 lines, and a head line at most 160 B". The annotations leg's checks include "the touched-block budget; history inside a note's body; one anchor per feature tag". gap-mem-18 says: "Comment load is unbudgeted". Clause 0244 says only: "the `annotations` leg, the marker query … and the read hook". 0248 covers only the untouched blocks.
- **Consequence:** New long comment blocks pass, and gap-mem-18 stays open.
- **Fix:** List the leg's checks in 0244, the touched-block cap among them, each seen red on a planted case.

### C3-F22 — `annotations.resolve-scope` and `annotations.lookup` are not named
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0244
- **Class:** K4
- **Severity:** low
- **Evidence:** v2 [policies] lists `annotations.resolve-scope` (notes, every-comment-ref) and `annotations.lookup` (query-and-map, query, map-index), both dLinkedLibrary's. Stage 0's K4 lists both as unread. 0244 carries AN-1's default in prose only, and no clause carries resolve-scope.
- **Consequence:** `notes` and `map-index` never route.
- **Fix:** Name both keys in 0241 and 0244.

### C3-F23 — dLinkedLibrary owns gap-mem-11 and gap-mem-12, but no clause of it carries either
- **Address:** architecture-v2 [chain] dLinkedLibrary row, Gaps owned (`gap-mem-11`, `gap-mem-12`)
- **Class:** K8
- **Severity:** low
- **Evidence:** gap-mem-11 covers records that contradict code: the map README path, `backlog.py`'s claim, the DEPL rows, `ANNOTATION-STYLE` saying no gate reads comment citations, and `HYGIENE.md`'s unused `note` kind. gap-mem-12 says: "the annotation follow-through test decides nothing: it has no threshold, sample size or window". layer-memory [annotations] says: "follow-through after landing, against today's 11.0% … The test's threshold, sample and window are dTotalRecall's to set". No clause of 0238–0261 carries either gap.
- **Consequence:** Both gaps survive their owner's landing, and the pushed-at-read fallback has no deciding test.
- **Fix:** Add a clause correcting gap-mem-11's records, including the ANNOTATION-STYLE guide and template pair. Set gap-mem-12's threshold, sample and window in 0244.

### C3-F24 — The forced-name packs contradict the rule that closed sets apply by name
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0263
- **Class:** K10
- **Severity:** medium
- **Evidence:** lexicon [forced] item 1 says: "A namespaced closed set applies by name, and its rows carry a namespace pattern … (`pytest_*`, `__*__`)". Clause 0263 says: "packs keyed by base member, base prefix and host namespace, applied only where the site resolves statically through its imports to that base". The clause also omits the three outcome cases: unresolved base, in-repo parent and marker.
- **Consequence:** Module-level pytest hooks and dunders on classes with no outside base stay debt and are refused at commit under `lexicon.at-commit: refuse`, which leaves gap-lex-01 open.
- **Fix:** Split the rule in 0263: member and prefix rows resolve statically, and namespace closed sets apply by name. Add the three cases, each with its fixture.

### C3-F25 — The noun canon's source contradicts the amended design
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0271
- **Class:** K10
- **Severity:** medium
- **Evidence:** lexicon [drift] (amended by the debt fold's `nouns-table` row) says: "noun clusters, written exogenously, such as `sha` against `oid` … The corpus decides only which clusters are live". Clause 0271 says: "a noun canon seeded from the corpus and frozen", which is L-3's pre-fold offer wording.
- **Consequence:** A corpus-seeded canon makes today's variants canonical, the opposite of the fix.
- **Fix:** Reword 0271: clusters written exogenously, with liveness from the corpus.

### C3-F26 — `ratified` is retired without its readers by value
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0272
- **Class:** K10
- **Severity:** medium
- **Evidence:** lexicon [vocabulary] says: "`ratified` gives way to that path's record, and its readers move with it … `adopt-lexicon.sh --check`, the kit's `lexicon-pins` hole and the scaffold read that record too. The leg pack's arm is seen red on a planted LANGS change newer than the record". The debt fold classes this `retirement-inventory-misses-readers-by-value`. In code, `ratified` is read in `tools/lexicon/{adopt-lexicon.sh,kit.toml,lexicon.py,lexicon_conf.py,scaffold_lexicon.py,selftest.py}` and `tools/drift-audit/{drift_report.py,drift_signals.py}`. Clause 0272 says only: "with `ratified` replaced by its record".
- **Consequence:** The drift signal and adopt check keep reading a dead field, and their signal silently stops moving.
- **Fix:** Name the readers in 0272, with the planted LANGS red.

### C3-F27 — The "one pin over three seams" rule is carried by no clause
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0262
- **Class:** K10
- **Severity:** low
- **Evidence:** lexicon [classes] says: "`VERB_OFFENDER_PIN` becomes the debt pin. `SUFFIX_OFFENDER_PIN` folds into it … The per-cell `PINS:` block retires". It also says "Two cells re-arm. `py.file` and `py.constant`". In code, `tools/lexicon/lexicon.py:121` reads `PIN_KEYS = {"verb": "VERB_OFFENDER_PIN", "suffix": "SUFFIX_OFFENDER_PIN"}`. Clause 0262 names only "the shrink-only pin".
- **Consequence:** The suffix pin and the per-cell pins survive as separate waivers beside the debt pin.
- **Fix:** Carry the fold, the `PINS:` retirement and the two cells' re-arming in 0262 and 0276.

### C3-F28 — P29's enforcement row names one clause, though P29 has six rules
- **Address:** architecture-v2 [enforcement] P29
- **Class:** K5
- **Severity:** medium
- **Evidence:** P29 has six rules beyond handed and keyed inputs: verifiers alone, cold (`roles.verifier-context`); answered calls (`roles.answered-calls`); false facts (`roles.on-contradiction`); acting on keyed facts (`roles.trust`); "Recall: recall is re-verified once, by the orientation scout at entry". Its row names only `cl-dClosedLoop-0178`. 0196, 0197, 0198 and 0205 carry the keys, but they sit in no row, and no clause carries the orientation scout's one recall re-verification (0192 and 0204 only compose the card).
- **Consequence:** The principle registry certifies P29 from a clause that carries one of its rules. The recall boundary is never built.
- **Fix:** Add 0196, 0197, 0198 and 0205 to P29's row. Add the recall re-verification to 0192.

### C3-F29 — The deployer's registration omits distribution's contract
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0166
- **Class:** K10
- **Severity:** low
- **Evidence:** layer-roles [roster] says: "deployer | distribution, integrations | … The deployer acts for two expansions: release notes for distribution, and verify judgment for integrations". Clause 0166 says: "registered through the integrations and observability layer contracts".
- **Consequence:** The release-notes item has a role that its expansion never registers, so P28's no-expansion-role-in-core arm may red on it.
- **Fix:** Add distribution's contract to 0166.

### C3-F30 — The lexicon declaration kind has no declared writer or reader in any clause
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0269
- **Class:** K3
- **Severity:** low
- **Evidence:** layer-memory [contract] says: "lexicon declaration | dMindYourWords | … dMindYourWords builds the declaration and its packs; writer item not named". Stage 0's K3 lists it as both "no writer item" and "no reader". Clause 0269 says: "declared by the owner, custom packs included (`lexicon.packs`)".
- **Consequence:** The kind's registry row has no door, and the one-door check cannot grade it.
- **Fix:** Name the declaration as a registered kind in 0269, its door `instructions.edit` and its reader the lexicon's pack loader.

### C3-F31 — The span rule's owed re-measure is not carried
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0254
- **Class:** K10
- **Severity:** low
- **Evidence:** v2 [owed] says: "the span share re-measured with the map's own extractors: the hybrid loses if 80% or more of a feature's outside spans sit in a derivable definition (point 4)". Clause 0254 builds the span rule with no losing test.
- **Consequence:** The hybrid span rule is built with no test that could reject it.
- **Fix:** Add the re-measure and its 80% bound to 0254.

| clause | build | read against | verdict |
|---|---|---|---|
| cl-dClosedLoop-0166 | dBoundRoles | layer-roles [roster], [settled]; gap-roles-01, -07, -14; v2 [owed] expansion roles | C3-F29 |
| cl-dClosedLoop-0167 | dBoundRoles | layer-roles [tags]; gap-roles-03; v2 P25 | holds |
| cl-dClosedLoop-0168 | dBoundRoles | layer-roles [settled] two blocks; night-pass-two [p4] contradiction 1; gap-roles-05, -08 | holds |
| cl-dClosedLoop-0169 | dBoundRoles | v2 P26; layer-roles [roster] cycle role; gap-roles-02, -05 | holds |
| cl-dClosedLoop-0170 | dBoundRoles | v2 P26; policies `roles.retries`; gap-roles-04 | holds |
| cl-dClosedLoop-0171 | dBoundRoles | gap-roles-06, gap-orient-07; tools/hooks/agent-cap.js | holds |
| cl-dClosedLoop-0172 | dBoundRoles | gap-roles-03; layer-roles [tags] | holds |
| cl-dClosedLoop-0173 | dBoundRoles | gap-orient-09; tools/hooks/scratch-guard.js | holds |
| cl-dClosedLoop-0174 | dBoundRoles | gap-orient-09; check_roles.py WRITES | holds |
| cl-dClosedLoop-0175 | dBoundRoles | policies `driver.reads`, `prompts.author`, `roles.no-spawn`; v2 P25 | holds |
| cl-dClosedLoop-0176 | dBoundRoles | v2 P18, [enforcement] P18; policies `run.on-owner-question`; stage0 K5 lead | C3-F1 |
| cl-dClosedLoop-0177 | dBoundRoles | policies `placement.check`; layer-roles [matrix] entry.place | holds |
| cl-dClosedLoop-0178 | dBoundRoles | v2 P29; layer-roles [trust] items 1–3; gap-roles-11 | holds |
| cl-dClosedLoop-0179 | dBoundRoles | layer-roles [tags]; systems tags owners | holds |
| cl-dClosedLoop-0180 | dBoundRoles | systems [agree-instruction-writing], [design-instruction] keys; policies `instructions.task-charter`; gap-roles-19, -20; check_roles.py:84 | C3-F2, C3-F3 |
| cl-dClosedLoop-0181 | dBoundRoles | systems [design-role-shapes]; night-pass-two [p7]; RS-2 answers; gap-roles-18 | holds |
| cl-dClosedLoop-0182 | dBoundRoles | memory-plan [sites], [gates], [chain]; gap-roles-23 | holds |
| cl-dClosedLoop-0183 | dBoundRoles | v2 P38; night-pass-two [p4] contradiction 2 | holds |
| cl-dClosedLoop-0184 | dBoundRoles | v2 P38; memory-plan [doors] upgrade-step door | holds |
| cl-dClosedLoop-0185 | dBoundRoles | gap-roles-24, -25; check_roles.py BODY_CEILINGS, WORKFLOW_NAMES; layer-roles [matrix] composition revision | holds |
| cl-dClosedLoop-0186 | dBoundRoles | policies `roles.effort.*`, `roles.model.<role>`; systems [design-role-shapes]; roles_lib.py:561 | holds |
| cl-dClosedLoop-0187 | dBoundRoles | systems kinds bullet (NT-8); `runtime.agents-in-flight` | holds |
| cl-dClosedLoop-0188 | dBoundRoles | night-pass-two [p2] items 4–5, [answers] NT-12; gap-roles-27; house/policy.toml | holds |
| cl-dClosedLoop-0189 | dBoundRoles | night-pass-two [p4] contradiction 11; gap-roles-28 | holds |
| cl-dClosedLoop-0190 | dBoundRoles | night-pass-two [p7] rule table; gap-roles-30 | holds |
| cl-dClosedLoop-0191 | dBoundRoles | stall-and-loop [design] item 7; v2 P39; gap-roles-31 | holds |
| cl-dClosedLoop-0192 | dFurnishedOrders | project-map [delivery]; gap-orient-15; v2 P29 recall | holds |
| cl-dClosedLoop-0193 | dFurnishedOrders | policies `prompts.batch` | holds |
| cl-dClosedLoop-0194 | dFurnishedOrders | policies `notices.record`; gap-roles-09 | holds |
| cl-dClosedLoop-0195 | dFurnishedOrders | night-pass-two [p6]; gap-mem-44 | holds |
| cl-dClosedLoop-0196 | dFurnishedOrders | layer-roles [trust] items 4–6; policies `roles.trust`, `roles.verifier-context`; gap-roles-10, -16 | holds |
| cl-dClosedLoop-0197 | dFurnishedOrders | layer-roles [trust] item 10; policies `roles.answered-calls`; gap-roles-13 | C3-F8 |
| cl-dClosedLoop-0198 | dFurnishedOrders | layer-roles [trust] item 7; policies `roles.on-contradiction`; gap-roles-17 | holds |
| cl-dClosedLoop-0199 | dFurnishedOrders | layer-roles [tags] pointers' source; gap-roles-10, -12; roles_lib.py:67, check_roles.py, render_agents.py | C3-F4 |
| cl-dClosedLoop-0200 | dFurnishedOrders | layer-roles [matrix]; gap-roles-15 | holds |
| cl-dClosedLoop-0201 | dFurnishedOrders | layer-roles [trust] item 11; layer-memory [contract] value ledger; 0459 | C3-F6 |
| cl-dClosedLoop-0202 | dFurnishedOrders | systems [cross] one budget per slot; policies `retrofit.slot-bytes`, `annotations.delivery`, `instructions.slices`, `roles.orientation.house-index`; dTotalRecall 0220 | C3-F5, C3-F7 |
| cl-dClosedLoop-0203 | dFurnishedOrders | project-map [tiers], [delivery], [keys]; policies `memory.map-unfold` | holds |
| cl-dClosedLoop-0204 | dFurnishedOrders | project-map [delivery] orientation scout row | holds |
| cl-dClosedLoop-0205 | dFurnishedOrders | v2 RC-7; layer-roles [trust] items 7, 10 | holds |
| cl-dClosedLoop-0206 | dFurnishedOrders | gap-roles-21; layer-memory probe kind (dPlacedRequest) | holds |
| cl-dClosedLoop-0207 | dFurnishedOrders | night-pass [p1-unattended] item 2; v2 P4 | holds |
| cl-dClosedLoop-0208 | dFurnishedOrders | project-map [placement]; policies `memory.code-budget`, `memory.code-roles`; v2 P32; gap-roles-22 | holds |
| cl-dClosedLoop-0209 | dFurnishedOrders | systems annotations delivery; NP-13 | holds |
| cl-dClosedLoop-0210 | dFurnishedOrders | night-pass-two [p4] contract; gap-roles-29 | holds |
| cl-dClosedLoop-0211 | dFurnishedOrders | night-pass-two [p4] problems; memory-plan refs: problems; gap-conc-10 | holds |
| cl-dClosedLoop-0212 | dTotalRecall | v2 P16, P30; layer-memory [contract]; gap-mem-01 | holds |
| cl-dClosedLoop-0213 | dTotalRecall | v2 P30; memory-plan [doors] | holds |
| cl-dClosedLoop-0214 | dTotalRecall | gap-mem-13; policies `leases.offline`; gen_build_index.py check_slug_claimed | holds |
| cl-dClosedLoop-0215 | dTotalRecall | layer-memory [build]; policies `builds.agent-root`; gap-mem-05, -40 | holds |
| cl-dClosedLoop-0216 | dTotalRecall | layer-memory [names]; policies `builds.slug-*`; gap-mem-06 | C3-F10 |
| cl-dClosedLoop-0217 | dTotalRecall | layer-memory [relations]; gap-mem-07; v2 P30 | C3-F9 |
| cl-dClosedLoop-0218 | dTotalRecall | layer-memory [asks]; policies `asks.acceptance` | holds |
| cl-dClosedLoop-0219 | dTotalRecall | layer-memory [map]; v2 [owed] re-timing; v2 P32; gap-mem-04, -28 | C3-F11 |
| cl-dClosedLoop-0220 | dTotalRecall | systems [design-memory-structure]; policies `memory.*`; gap-mem-20, -21 | C3-F16 |
| cl-dClosedLoop-0221 | dTotalRecall | systems [design-memory-structure] repeated heading (M35) | holds |
| cl-dClosedLoop-0222 | dTotalRecall | systems [design-role-shapes] metric; layer-memory [contract] shape-run; flow-steps review.cost | holds |
| cl-dClosedLoop-0223 | dTotalRecall | systems [design-memory-structure] acceptance re-measure | C3-F12 |
| cl-dClosedLoop-0224 | dTotalRecall | lexicon [integration]; LX-2 | holds |
| cl-dClosedLoop-0225 | dTotalRecall | project-map [placement], [fit], [keys]; gap-mem-26, -30, gap-design-01 | holds |
| cl-dClosedLoop-0226 | dTotalRecall | project-map [checks], [owners] | holds |
| cl-dClosedLoop-0227 | dTotalRecall | project-map [purpose], PM-5; gap-mem-27 | holds |
| cl-dClosedLoop-0228 | dTotalRecall | project-map [test] | C3-F13 |
| cl-dClosedLoop-0229 | dTotalRecall | memory-plan [pockets], [integration]; gap-mem-37, -38 | holds |
| cl-dClosedLoop-0230 | dTotalRecall | memory-plan [doors], [sites], [migration], [gates]; v2 P34, P35; gap-mem-36 | holds |
| cl-dClosedLoop-0231 | dTotalRecall | memory-plan [integration] distribution row, [migration]; v2 P38 | C3-F14 |
| cl-dClosedLoop-0232 | dTotalRecall | night-pass-two [p3] item 2; systems [cross]; gap-mem-41 | holds |
| cl-dClosedLoop-0233 | dTotalRecall | night-pass-two [p3] item 3; gap-mem-42 | holds |
| cl-dClosedLoop-0234 | dTotalRecall | night-pass-two [p3] item 2; gap-mem-43 | holds |
| cl-dClosedLoop-0235 | dTotalRecall | memory-plan [pockets] change feed; night-pass-two [answers-folded] NT-14 | holds |
| cl-dClosedLoop-0236 | dTotalRecall | layer-memory [contract] stream plan; whole-audit [readings] CL-3 | holds |
| cl-dClosedLoop-0237 | dTotalRecall | final-questions [atlas], FQ-8; policies `help.atlas`; v2 P42; gap-mem-48 | holds |
| cl-dClosedLoop-0238 | dLinkedLibrary | layer-memory [decisions]; gap-mem-02 | holds |
| cl-dClosedLoop-0239 | dLinkedLibrary | layer-memory [reuse]; night-pass-two [p2] item 7; research-scoutedseam-apply; gap-mem-03 | C3-F17 |
| cl-dClosedLoop-0240 | dLinkedLibrary | layer-memory [reuse] readers by value; check-memory-hygiene.sh:2474; unattended kit.toml:174; gap-mem-09 | C3-F18 |
| cl-dClosedLoop-0241 | dLinkedLibrary | layer-memory [annotations]; policies `annotations.grammar`; gap-mem-08, -17, -32 | C3-F19 |
| cl-dClosedLoop-0242 | dLinkedLibrary | dTotalRecall 0215, 0217; memory-plan [practice] one owner | C3-F20 |
| cl-dClosedLoop-0243 | dLinkedLibrary | layer-library [research-view]; gap-mem-15 | holds |
| cl-dClosedLoop-0244 | dLinkedLibrary | systems [design-annotations] budget, checks, keys; AN-1, AN-2; gap-mem-18, -19 | C3-F21, C3-F22 |
| cl-dClosedLoop-0245 | dLinkedLibrary | flow-steps [adopt]; policies `retrofit.*`; gap-mem-24, -25 | holds |
| cl-dClosedLoop-0246 | dLinkedLibrary | retrofit record origin; gap-mem-25 | holds |
| cl-dClosedLoop-0247 | dLinkedLibrary | gap-mem-24 | holds |
| cl-dClosedLoop-0248 | dLinkedLibrary | systems [cross] retrofit ledger populations | holds |
| cl-dClosedLoop-0249 | dLinkedLibrary | systems marker registration | holds |
| cl-dClosedLoop-0250 | dLinkedLibrary | gap-mem-15 (72 at `1b759b620`); layer-memory [contract] research return | holds |
| cl-dClosedLoop-0251 | dLinkedLibrary | v2 P32; project-map [placement] counted code line | holds |
| cl-dClosedLoop-0252 | dLinkedLibrary | policies `memory.code-enrich`; v2 P32; gap-mem-29 | holds |
| cl-dClosedLoop-0253 | dLinkedLibrary | project-map [test]; dTotalRecall 0228 | holds |
| cl-dClosedLoop-0254 | dLinkedLibrary | v2 [owed] span re-measure; v2 P33; gap-mem-31 | C3-F31 |
| cl-dClosedLoop-0255 | dLinkedLibrary | gap-mem-33; check_roles.py and render_playbook.py REGION constants | holds |
| cl-dClosedLoop-0256 | dLinkedLibrary | NP-16; memory-plan [pockets] dossiers | holds |
| cl-dClosedLoop-0257 | dLinkedLibrary | NP-13; memory-plan [cycle] | holds |
| cl-dClosedLoop-0258 | dLinkedLibrary | policies `memory.code-languages`; NP-10; gap-mem-34 | holds |
| cl-dClosedLoop-0259 | dLinkedLibrary | memory-plan [cycle], [migration]; v2 P37; gap-mem-39, gap-tool-17 | holds |
| cl-dClosedLoop-0260 | dLinkedLibrary | policies `instructions.legacy`; IA-5; gap-deploy-26 | holds |
| cl-dClosedLoop-0261 | dLinkedLibrary | night-pass-two [p6] items 3–4; gap-mem-45 | holds |
| cl-dClosedLoop-0262 | dMindYourWords | lexicon [classes]; policies `lexicon.pin`; lexicon.py:121; gap-mem-10 | C3-F27 |
| cl-dClosedLoop-0263 | dMindYourWords | lexicon [forced] item 1, L-1; policies `lexicon.forced`; gap-lex-01 | C3-F24 |
| cl-dClosedLoop-0264 | dMindYourWords | lexicon [forced] item 2, LX-3 | holds |
| cl-dClosedLoop-0265 | dMindYourWords | lexicon [forced] item 3 | holds |
| cl-dClosedLoop-0266 | dMindYourWords | lexicon [forced] item 4; gap-lex-06 | holds |
| cl-dClosedLoop-0267 | dMindYourWords | lexicon [forced] `--suggest`; gap-lex-02 | holds |
| cl-dClosedLoop-0268 | dMindYourWords | lexicon [packs]; v2 [owed] adopter census | holds |
| cl-dClosedLoop-0269 | dMindYourWords | lexicon [packs] selection, L-5; layer-memory [contract] lexicon declaration; stage0 K3 lead | C3-F30 |
| cl-dClosedLoop-0270 | dMindYourWords | lexicon [enforcement] items 1–3; policies `lexicon.at-commit`; gap-lex-03 | holds |
| cl-dClosedLoop-0271 | dMindYourWords | lexicon [drift], debt-fold `nouns-table`, L-3; gap-lex-05 | C3-F25 |
| cl-dClosedLoop-0272 | dMindYourWords | lexicon [vocabulary], debt-fold `ratified-readers`; tools/lexicon and drift-audit readers of `ratified`; gap-lex-06 | C3-F26 |
| cl-dClosedLoop-0273 | dMindYourWords | lexicon [integration], LX-2; dTotalRecall 0224 | holds |
| cl-dClosedLoop-0274 | dMindYourWords | lexicon [integration] tag vocabulary; gap-lex-10 | holds |
| cl-dClosedLoop-0275 | dMindYourWords | lexicon [fixes]; gap-lex-07 | holds |
| cl-dClosedLoop-0276 | dMindYourWords | lexicon [classes] out of scope, [fixes]; gap-lex-04 | holds |
| cl-dClosedLoop-0277 | dMindYourWords | lexicon [enforcement] item 6; gap-lex-08 | holds |
| cl-dClosedLoop-0278 | dMindYourWords | gap-lex-09 | holds |

| Build | Verdict |
|---|---|
| dBoundRoles | C3-F1, C3-F2, C3-F3, C3-F28, C3-F29 |
| dFurnishedOrders | C3-F4, C3-F5, C3-F6, C3-F7, C3-F8, C3-F28 |
| dTotalRecall | C3-F9, C3-F10, C3-F11, C3-F12, C3-F13, C3-F14, C3-F15, C3-F16 |
| dLinkedLibrary | C3-F17, C3-F18, C3-F19, C3-F20, C3-F21, C3-F22, C3-F23, C3-F31 |
| dMindYourWords | C3-F24, C3-F25, C3-F26, C3-F27, C3-F30 |

**Read outside the list above:** Three of my greps over `*.md` in the copy's `build/` folder were not filtered, so their output showed a few lines of excluded records. One showed lines 2214 and 2217 of the copy's `2026-10-14-build-PLAY-dClosedLoop-1-session-log.md`, on RS-2. Another showed one line of `2026-10-16-build-PLAY-dClosedLoop-1-layers-reviews-compared-instruments.md`, on BODY_CEILINGS. No finding rests on those lines. I did not open the files, and read nothing else outside the list.

**Defect in the brief or instruments:** none. My probe scripts (`split.py`, `owners.py`) are under `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/scratch/walk-c3/`, and nothing was written to the repository.
