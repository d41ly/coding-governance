# Skeptic return: run C, batch 2

**Serves:** research PLAY-dClosedLoop-1

Dispatch 193's return, verbatim, any H1 demoted to bold. Its handoff is `prompts/prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-34-skeptic.md`, and its use is in
`build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`.

---

- C2-F2: confirmed high
  The ending is real and has no row. `cl-dClosedLoop-0116` gives `close-incomplete` and `park-for-owner`. flow-steps `[transitions]` (fs:617-654) has no row from an open state on budget exhaustion, and its terminal list has no incomplete or parked-for-owner state. The only parked state there, `paused`, is reached only by `life.request`. `cl-dClosedLoop-0100` builds only the declared terminals, and the strict preset sets `park-for-owner` (v2:1452). `cl-dClosedLoop-0328` also speaks of "a parent ending incomplete", which is a state the table does not have.
- C2-F13: confirmed medium
  `cl-dClosedLoop-0118` reads "a raise of a loop bound" as a loosening, but its red list plants only "an unattended raise of the budget". stall-and-loop `[chain]` (s&l:310) plants "an unattended raise of a loop bound", and item 8 (s&l:244) names the budget, a round count, a retry count and a deadline. So v2 narrowed the planted case.
- C2-F10: confirmed medium. The rubric grades this above the walker's low.
  `leases.granularity` and `card.follows` appear in v2 only in the catalogue (v2:1031, 1042), the presets (1354, 1365) and line 62. Neither appears in any `[chain]` row, so neither is named in `cl-dClosedLoop-0120` or `cl-dClosedLoop-0121`. Velocity's `build` value has nothing to route it. That is a behaviour a spec writer would trip over, not a wording defect.
- C2-F7: confirmed medium
  fs:83 sends `entry.place` to `plan.triage-rule` and to Plan and Design re-entry. Those items are owned by dRankedPlan and dIndexedDesign, and neither is an ancestor of dPlacedRequest (v2:1639, 1648-1649). `cl-dClosedLoop-0122` and `cl-dClosedLoop-0123` declare no stand-in, while `cl-dClosedLoop-0125` does. v2 has no general stand-in rule outside the chain rows.
- C2-F5: refuted
  `cl-dClosedLoop-0124` only declares data on items; it reads nothing. The reader is `cl-dClosedLoop-0203` (dFurnishedOrders, a descendant), and it carries the stand-in: "rendering 'not installed' until dTotalRecall's renderer lands". project-map's own owners table (pm:717-718) deliberately puts the items' declarations in an earlier build than the slot. The sibling `cl-dClosedLoop-0126` (code seeds, read by 0208 with its stand-in) has the same shape. The missing `memory.map-unfold` reader is a K4 issue that C3-F5 already carries.
- C2-F4: confirmed medium
  `cl-dClosedLoop-0132` keys the budget to "the intake's content key". The design map has `record-kind.intake` owned by dWellOiledMachine, which is not an ancestor. `cl-dClosedLoop-0123` admits the same dependency, and fs:80 leaves intake absent when the hook never fires. The consequence is overstated: `flow.route-backs`, which is in Entry's policy list (fs:105), still caps returns to `entry.place`, so placement loops are not fully unbounded.
- C2-F15: confirmed medium
  `cl-dClosedLoop-0143` says only "read and disposed at every transition". No flow-steps item reads the mailbox at an exit; the only mailbox hit in an item is fs:374, on the release hold. layer-memory:438 says "writer item not named". Coordination item 6 (co:116-117) holds the refusal. `cl-dClosedLoop-0162` implies the hold ("past which … transitions go on") but does not refuse.
- C2-F11: confirmed medium
  No `[chain]` row names `deps.coordination`, `deps.early-build` or `orient.budget`; `cl-dClosedLoop-0145` and `cl-dClosedLoop-0147` are as quoted. The strict values are confirmed at v2:1361, 1362 and 1374. The consequence is overstated for the two `deps.*` keys: flow-steps lists `deps.coordination` in Plan's policies (fs:147) and `deps.early-build` in Design's (fs:200). It stands whole for `orient.budget`.
- C2-F12: confirmed medium
  `cl-dClosedLoop-0121` routes the recommendation by `resume.context`. `cl-dClosedLoop-0150` recommends a fresh session until the card-import fixture passes, with no key and no precedence. Velocity's `always-resume` (v2:1373) conflicts with it while the fixture is red.
- C3-F29: confirmed low
  layer-roles `[roster]` (lr:462, 466) and fs `[consequences]` ("it registers under both") register the deployer under distribution and integrations. `cl-dClosedLoop-0166` names only "the integrations and observability layer contracts", which covers the deployer and the maintainer. Distribution is missing.
- C3-F1: confirmed medium. The rubric grades this below the walker's high, and it is not c5.
  `cl-dClosedLoop-0390` names `design.forks`, and that key's default value `agents-feature-rich-expandable` (v2:1019) carries the ranking. P18 also has two enforcing clauses (v2:1702). The part with no clause is "only options the core admits are options", and nothing checks that a pick is the top admitted option.
- C3-F2: confirmed medium
  `cl-dClosedLoop-0180` reads only "the role static block carried once per spawn". `instructions.task-charter` (v2:1231, owned by dBoundRoles) appears in no `[chain]` row. The single-carry check that reads it is at systems:410-413.
- C3-F3: confirmed low
  gap-register:171 lists gap-roles-20, and dBoundRoles owns it (v2:1641's gaps cell). layer-instruction:458 makes `BODY_CEILINGS` the role block's only budget carrier. The cited code is true: `tools/roles/check_roles.py:84` reads "Bytes of each slot's BASE body". No `[chain]` clause budgets the whole rendered block.
- C3-F8: confirmed medium
  `cl-dClosedLoop-0197` is only "the answered-call hook (`roles.answered-calls`)", with a default of `refuse` (v2:1057). Neither the verifier exemption nor the recorded fail-open below CLI 2.1.295 (lr:331-336) is in 0197, and `cl-dClosedLoop-0205` defers its details to unit specs. P29 (v2:875-878) implies the exemption but does not carry it.
- C3-F4: confirmed medium
  lr:376-380 requires the same-unit re-point. `cl-dClosedLoop-0199` omits it. The code is as cited: `roles_lib.py:67` `CARRIED_SECTIONS = ("Protocols", "Facts")`, `check_roles.py:169` reading Protocols, and `render_agents.py:335-338`'s arm 4 asserting the carried text.
- C3-F6: confirmed medium
  `cl-dClosedLoop-0201` writes "into the value ledger". The design map has `record-kind.value-ledger` owned by dCalibratedLens, built by `cl-dClosedLoop-0459`. That build is not an ancestor of dFurnishedOrders, whose only parent is dBoundRoles (v2:1642), and there is no stand-in.
- C3-F5: confirmed medium
  All five keys have dFurnishedOrders as owner (v2:1228, 1229, 1234, 1247, 1261), and none appears in any `[chain]` row. `cl-dClosedLoop-0202` and `cl-dClosedLoop-0203` are as quoted.
- C3-F7: confirmed medium
  `cl-dClosedLoop-0202` has no stand-in. Its slices are priced by `memory.item-budget` and answered by `memory.over-budget` (systems:214-215), both dTotalRecall's, and dTotalRecall is not an ancestor of dFurnishedOrders. `cl-dClosedLoop-0195`'s three-state rule covers only optional components and expansions, and memory is core.
- C3-F10: confirmed medium
  layer-memory `[names]` (lm:518-528) holds the derived `BUILD_SLUG_RE`, the named flips and the new-mints-only rule. `cl-dClosedLoop-0216` says only "proven by flipping the grammar in a scratch clone".
- C3-F9: confirmed medium
  lm:547-550 holds the `depends-on` no-cycle rule and the pending-target rule. `cl-dClosedLoop-0217` has neither, while dTotalRecall owns gap-mem-07 (gap-register:189, "no cycle check").
- C3-F11: confirmed medium
  v2 `[owed]` (v2:1894-1896) holds "over 30 s or over 1 MB loses, on gov's tree and on a planted adopter-scale fixture". `cl-dClosedLoop-0219` has only "re-timed on a planted adopter-scale fixture": no bound, and no gov tree.
- C3-F16: confirmed medium
  `memory.over-budget`, `memory.superseded-slices` and `memory.map-overflow` (v2:1242, 1250, 1246) appear in no `[chain]` row. `cl-dClosedLoop-0220` and `cl-dClosedLoop-0225` are as quoted.
- C3-F12: confirmed medium
  systems:550-559 holds the bar: "median … below 33 KB" 30 days after landing, with "Why the first measure could not fail". `cl-dClosedLoop-0223` is only "the acceptance re-measure counted over every read channel".
- C3-F13: confirmed high
  project-map `[test]` (pm:699-702) holds the three loss conditions against the twin runs. `cl-dClosedLoop-0228` says only "so a losing map is never built", and `cl-dClosedLoop-0253` extends the same undefined test.
- C3-F14: confirmed high
  memory-plan:293, 297 and 331 require the `journal` alias and its adopter upgrade step. `cl-dClosedLoop-0229` renames the kind, and `cl-dClosedLoop-0231`'s steps omit the alias. The finder's count is slightly off: memory-plan:125 says 1,443 records, not 1,436, which does not change the finding.
- C3-F17: confirmed high
  lm:717-718 says the acceptance "must meet M1c's 16". `cl-dClosedLoop-0239` re-runs the benchmark and the twelve held-out cases with no bar.

- `cl-dClosedLoop-0161` dKeptSession: holds
- `cl-dClosedLoop-0475` dConvergedCharter: holds
- `cl-dClosedLoop-0482` dConvergedCharter: holds
- `cl-dClosedLoop-0162` dKeptSession: holds
- `cl-dClosedLoop-0096` dDeclaredLoop: holds
- `cl-dClosedLoop-0160` dKeptSession: defect

  ### CS2-F1 — A message retried from a new session is not refused as a duplicate
  - **Address:** architecture-v2 [chain] `cl-dClosedLoop-0160` (with `cl-dClosedLoop-0150` and `cl-dClosedLoop-0143`)
  - **Class:** K10
  - **Severity:** medium
  - **Evidence:**
    - 0160 derives a message's id "from its sender's session, and its act once Runtime mints acts". Acts are dWellOiledMachine's, and that build is not an ancestor of dKeptSession.
    - 0143 keys each mail ref by session.
    - 0150, in the same build, recommends a fresh session, and the `resume.context` default is `fresh-when-idle`.
  - **Consequence:** A post retried after a crash from a fresh session gets a new id and lands in a new ref, so the duplicate lands. The "post retried after a crash" case passes only when the retry runs in the same session.
  - **Fix:** Until acts are minted, derive the id from the build, the item instance key 0092 computes, the pass, the kind, the subject and the answered id, not from the session. Plant the retry from a new session and see it refused.
- `cl-dClosedLoop-0151` dKeptSession: holds
- `cl-dClosedLoop-0126` dPlacedRequest: holds

- Instrument defect: Stage 0's K4 says `deps.coordination` and `deps.early-build` are read by "no chain clause and no item", but flow-steps' step policy lists (fs:147, fs:200) name both. K4 does not read step-level policy lists.
- **Read outside the list above:** none. I listed the folder names under `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/scratch/`, which shows the other skeptics' and walkers' folders, but read nothing in them. My one probe script is `C:/Users/d41ly/AppData/Local/Temp/claude/seed-dcl/scratch/skeptic-c2/cl.py`.
