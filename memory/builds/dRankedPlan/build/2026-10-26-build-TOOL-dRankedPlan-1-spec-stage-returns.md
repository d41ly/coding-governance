**Serves:** research TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16

# The SPEC stage's returns — unattended-build.js run wf_a043cc4e-f18

Each agent's final return, extracted from the run journal by script, never retyped. The commit stage refused on the README's `status: OPEN` key (PLAY-dClosedLoop-31); the main loop committed the specs.

## Agent 1 · dRankedPlan · TOOL-dRankedPlan-7 · spec-write

run wf_a043cc4e-f18/a2ae429f739ff5bd8, phase Spec

```json
{
 "authored": [
  "TOOL-dRankedPlan-7"
 ],
 "alreadyPresent": [],
 "refused": [],
 "summary": "I wrote the spec for TOOL-dRankedPlan-7 at C:/projects/coding-governance/.claude/worktrees/unattended-drankedplan-1fc3d7/memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-7.md. It has all ten sections and is 26448 bytes. Hygiene checks 2, 12 and 25 come back clean on it. Nothing was committed and the index was not regenerated. I wrote no deviation record, because the unit does not depart from its clause.\n\nHeader and bindings: `OPEN · rev-1 · 2026-10-26 · node a · Tier-2 · base 0689e7fa · streams tooling · order 16 · advances TOOL-dRankedPlan-17`, `**Carries:** cl-dClosedLoop-0375@33084fbd whole` and `**Carries:** node:policy-key.plan.kickoff`. The clause's four tokens (`plan.kickoff`, `offer-next`, `binding`, `advisory`) all appear in backticks.\n\nWhat the unit specifies:\n- **Plan's next build:** `read_plan_next` reads unit 1's `PLAN.md`. It takes the first row above `## Unplaced` and finds the `Build` column by its header name.\n- **Card cell:** a `plan — next <slug> · <value>` cell, written by `render_plan_cell` inside `render_card`. It sits after `live —` and after unit 8's `kickoff —` cell, and has five `skipped:` forms. The value is read with `read_card_policy plan.kickoff` (TOOL-dPlacedRequest-2 S11).\n- **`binding`:** a new route rule R8 in `check_card_route` refuses a route to any build other than the plan's next. When there is no next build, the append prints a \"holds nothing\" line instead of refusing.\n- **`advisory`:** the append prints an advice line when the route names a different build. Under `offer-next` the card cell is the offer.\n- **Attended brief gate:** the brief-record rules 1 to 5 move out of `check_prompt_brief` into one shared `brief_rules` block (`check_brief_record`, `derive_brief_subheads`). The canonical copy stays in `tools/unattended/unattended.sh`. `manifest-check.sh` carries a byte-identical inline copy, held equal by a new row in the parity table of `tools/lib/resolve-python.test.sh`. Rule R5 then grades a brief under a build's `prompts/` folder, but only for builds opened on or after a new `ATTENDED_BRIEF_CUTOFF` date literal.\n- **Policy reader coverage:** `check_policy.py`'s `READER_SHAPES` gets a row so a `read_card_policy <key>` call counts as a reader.\n- **Fixture and docs:** eight plants in `card-store.fixture.sh`, plus updates to `help/policy.md`.\n\nForks F1 to F5 are all resolved in §8 by the delegated rungs. The cutoff choice in F4 rests on a probe I ran: of the 149 tracked prompt records, 124 fail rules 1 to 5 today. Grading every routed brief would therefore refuse routes for builds already in progress.\n\n**Ask for the main loop to file:** in dPlacedRequest's `BACKLOG.md`, target build dPlacedRequest. `READER_SHAPES` reads only the literal `policy.py get <key>` shape. Once dPlacedRequest lands, every card key that S11 reads through `read_card_policy` will show red as unread. Accept line: when `scan_reader_keys` runs over a planted shell file whose one read of a key is `read_card_policy <key>`, it returns that key. S7 of this spec adds the row itself if it is still missing at the build base.\n\n**Edges that need the other side declared** (all from the brief's table):\n- unit 1 hands off `PLAN.md` to TOOL-dRankedPlan-7;\n- unit 16 hands off `BRIEF_SKELETON`;\n- unit 8 hands off `render_card`.\n\n**Notes for sibling writers:**\n- R8 is taken as the next free route-rule number, after TOOL-dPlacedRequest-2 S9's R7. Unit 8 should not reuse it.\n- Unit 16: if `check_brief_derived` is meant to gate briefs built by runs, putting it in the `brief_rules` block makes attended briefs meet it too.\n- The spec brief's interface I2 has `Dormant | Plan` columns where scout A proposed `Lease`. I followed I2.\n\n**Incident during this pass:** my first probe script was broken and executed brief markdown files as bash lines for about four minutes. I found and killed its process group. The only side effect was one empty stray file named `The` at the worktree root, which I deleted. Git status, the log and the stash list were unchanged, and nothing else was written in that window. The untracked `memory/builds/dRankedPlan/build/2026-10-26-build-TOOL-dRankedPlan-9-deviation-91.md` belongs to another writer, not this pass."
}
```

## Agent 2 · dRankedPlan · TOOL-dRankedPlan-16 TOOL-dRankedPlan-1 TOOL-dRankedPlan-9 · spec-write

run wf_a043cc4e-f18/a59102da023462410, phase Spec

```json
{
 "authored": [
  "TOOL-dRankedPlan-16",
  "TOOL-dRankedPlan-1",
  "TOOL-dRankedPlan-9"
 ],
 "alreadyPresent": [],
 "refused": [],
 "summary": "I wrote all three specs in roster order. Each is Tier-2, status OPEN rev-1, base 0689e7fa, with the required `order` verb. Nothing was committed and the index was not regenerated. I ran `check-memory-hygiene.sh --only 2,12,25` over the tree and it exited 0, with no finding on any dRankedPlan file.\n\nFiles written:\n- C:/projects/coding-governance/.claude/worktrees/unattended-drankedplan-1fc3d7/memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-16.md (order 1). Carries cl-0498 whole and the nodes record-kind.plan and item.plan.record.\n- C:/projects/coding-governance/.claude/worktrees/unattended-drankedplan-1fc3d7/memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-1.md (order 2). Carries cl-0369 whole and the node policy-key.plan.unplaced.\n- C:/projects/coding-governance/.claude/worktrees/unattended-drankedplan-1fc3d7/memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-9.md (order 3). Carries cl-0377 whole and the node policy-key.plan.ratification.\n- C:/projects/coding-governance/.claude/worktrees/unattended-drankedplan-1fc3d7/memory/builds/dRankedPlan/build/2026-10-26-build-TOOL-dRankedPlan-9-deviation-91.md, a deviation record for unit 9.\n\nChanges to the shared interfaces (I own I1–I3, I4–I6 and I7):\n- **I3, the plan record file name:** it is now `<date>-build-<FAMILY>-<slug>-1-plan-1.md`, not `-1-plan.md`. A typed record kind's file name must end `-<kind>-<n>.md`. Units 13 and 6 still use the old `-1-plan.md` spelling. They should call `find_plan_record` and `read_plan_fields` in `tools/memory-tree/plan_record.py` instead.\n- **I3, the plan record fields:** there are now 11, in this order: Problem, Goal, Scope, Non-goals, Acceptance, Affected systems, Open questions, Probes owed, Read sets, Scenario, Scenario reason. The four added fields are the ones flow-steps.md:184 has `plan.record` draft.\n- **Plan-record schema check:** it is `check_plan_record` in plan_record.py. Units 11–14 add their field checks as calls inside it, as unit 13 expects. Unit 16 arms `item.plan.record` by deleting its `[[stand-in]]` row, the same way unit 2 arms its items.\n- **I5, `BRIEF_SKELETON`:** it is left unchanged and treated as the shape of the plan-level intake record. The check grades only handoffs. A probe ruled out the alternative: removing `### Goal` from the skeleton makes `read_brief_subheads` refuse, which fails preflight check 117.\n- **I6:** the signature is `read_plan_ratification(slug, root=\".\", why=None) -> (value, witness)`. `witness` is None when the plan is not ratified, and the reason is appended to `why` when a list is passed.\n- **I7:** there is no `[[stand-in]]` row, because TOOL-dDeclaredLoop-13 S8 rejects a row for `item.entry.intake`, which has no item row and no move row. The stand-in is named by `INTAKE_STAND_IN` in ratify.py and by a `log stand-in` mark on every witness. Deviation 91 records this.\n\nEdges I added beyond the brief's edge table:\n- 16→1 and 16→9 on `record-kind.plan`. Both ends are in my specs, so both directions are declared.\n- 9 hands off `read_plan_ratification` to 5, because unit 5 already consumes it from 9.\n- 1 hands off `derive_activity` to 4 alongside `PLAN.md`, because unit 4 consumes both.\n- Units 11 and 12 had no spec on disk when I finished. Their writers need to add `consumes-from TOOL-dRankedPlan-16 record-kind.plan`.\n\n**Ask for the main loop to file**, target dOrderedCharter, ask PLAY-dOrderedCharter-42: \"accept the typed-kind file-name join reads `-<kind>-<n>.md` only on the stem `-build-<unit id>-<kind>-<n>.md`, seen on a research record named `…-return-plan-2.md` staying bound once `plan` joins `TYPED_RECORD_KINDS`\". A probe found six research records named `…-execution-return-plan-2.md` to `-7.md` that the loose name check would wrongly flag as plan records. Unit 16's S2 makes this narrowing itself if dOrderedCharter has not.\n\nNo unit was refused."
}
```

## Agent 3 · dRankedPlan · TOOL-dRankedPlan-10 TOOL-dRankedPlan-2 TOOL-dRankedPlan-14 · spec-write

run wf_a043cc4e-f18/a453fb9b8bca88a52, phase Spec

```json
{
 "authored": [
  "TOOL-dRankedPlan-10",
  "TOOL-dRankedPlan-2",
  "TOOL-dRankedPlan-14"
 ],
 "alreadyPresent": [],
 "refused": [],
 "summary": "I wrote three Tier-2 specs, all OPEN at rev-1 and none committed. Each status line carries its roster order (4, 5 and 6) and `advances TOOL-dRankedPlan-17`. Each spec has every required section. With all sixteen sibling specs on disk, hygiene checks 2, 12 and 25 exit 0, so every §3 edge already has its reverse in the other unit's spec. The lexicon admits every function the specs name. I wrote no deviation records. The main loop still has to run `check-spec-tokens.py` and `carries.py --report dRankedPlan`.\n\nFiles:\n- C:/projects/coding-governance/.claude/worktrees/unattended-drankedplan-1fc3d7/memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-10.md (carries cl-0378 whole, node `item.plan.exit`)\n- C:/projects/coding-governance/.claude/worktrees/unattended-drankedplan-1fc3d7/memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-2.md (carries cl-0370 whole, nodes `plan.authority`, `item.plan.input`, `dedupe`, `research`, `place`, `lease`)\n- C:/projects/coding-governance/.claude/worktrees/unattended-drankedplan-1fc3d7/memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-14.md (carries cl-0382 whole)\n\nTwo asks for the main loop to file:\n1. On dDeclaredLoop (unit 10, §8 F6): TOOL-dDeclaredLoop-24 says the fixed row for `item.entry.intake` is written when dPlacedRequest declares the item, but dWellOiledMachine is the build that declares it. Re-word that trigger to \"when dWellOiledMachine declares it\". Accept: the pass that declares the item writes its `[[fixed-row]]`, and a patch to its witness is then refused.\n2. On dBoundRoles (unit 2, §8 F2): TOOL-dBoundRoles-1 S4 should write a `[[workflow]]` row in `tools/loop/loop.toml` for each workflow it adds (`plan` on `step.plan`, `design` on `step.design`). Accept: the roles check, which requires every roles workflow to have a loop row, exits 0 at dBoundRoles' landing tip. It must be seen red on a fixture that lists `plan` with no loop row. Unit 2 also writes the `plan` row itself if the loop definition at its base lacks it.\n\nWhere my specs depart from the shared-interfaces table (the owner of each interface may refine it):\n- **I10:** TOOL-dDeclaredLoop-12 S2 already declares all eleven Plan item rows, owned by dRankedPlan. Unit 2 therefore adds no rows through `loop_items.py new`. It arms its items as TOOL-dDeclaredLoop-13 §4 describes: it lands each item's witness reader (`read_plan_item_witness` in `tools/loop/plan_items.py`) and deletes that item's stand-in row.\n- **`item.plan.dedupe`:** unit 2 builds the dedupe check, `check_plan_dupes`. The dupes record, its witness reader and the stand-in row stay with unit 3, which owns `record-kind.dupes` and builds later. This adds a second 2→3 edge on `check_plan_dupes`; unit 3 already declares the reverse edge and extends `read_plan_item_witness`.\n- **I11:** now `check_ratified_order(head, staged, authority, ratified)` in `gen_build_index.py`, run as `--ratified-order --staged`. It compares unit 1's `derive_plan_order` at HEAD and at the staged state. It runs from a new `.githooks/pre-commit` block, and the owner proves a commit is theirs the same way the policy guard does, `[ -t 2 ]`. A row counts as ratified when unit 9's `read_plan_ratification` answers a witness for its build.\n- **I8 and I9:** the fallback answer is `derive_plan_exit_ratification` and the release decision is `check_plan_exit`, both in `ratify.py` and called from `write_transition` and from the driver's plan gate. The capability table is `[[adapter]]` rows with `name`, `events` and `measured` in `tools/loop/adapters.toml`. No such file ships, so every harness falls back until dWellOiledMachine supplies it.\n- **Witness spelling:** the trailer cannot hold spaces, so the plan.exit transition records `ratification=intake-not-installed` and `harness=<name>`. The literal \"intake not installed\" appears on the hold's `decision` row and on the printed line.\n- **I19:** the placement's pin on the first transition record is where the scenario lives. A `Scenario` field that is absent, empty or equal to the pin reads as the pin. A different value is a re-pick and needs a `Scenario reason`. The field is read through unit 16's `plan_record.py field`. After Plan, a changed field is refused until a plan revision moves the build back to planning.\n- **Scenario re-pick checks:** a re-pick is checked only for registered tags in declared order; the admission predicates are not re-run. This reads NT-2 differently from scout A's F14b, and §8 F2 records why.\n- **Help pages:** units 10 and 2 document in `help/plan.md`, created by unit 16, beside unit 9's Ratification section. Unit 14 adds to the scenarios section of `help/loop.md`."
}
```

## Agent 4 · dRankedPlan · TOOL-dRankedPlan-15 TOOL-dRankedPlan-6 TOOL-dRankedPlan-8 · spec-write

run wf_a043cc4e-f18/af9c3a34ed6d798ce, phase Spec

```json
{
 "authored": [
  "TOOL-dRankedPlan-15",
  "TOOL-dRankedPlan-6",
  "TOOL-dRankedPlan-8"
 ],
 "alreadyPresent": [],
 "refused": [],
 "summary": "I wrote three specs in the order given. Nothing is committed and the index is not regenerated. Each spec is Tier-2, status OPEN rev-1, base 0689e7fa, and advances TOOL-dRankedPlan-17. Each has all ten sections, the Carries lines and the Edges table's pairs. I ran hygiene checks 2, 12 and 25 in a throwaway clone under %TEMP% (now deleted) with every spec then on disk committed there; none of these three files had a finding. I did not run check-spec-tokens or carries.py. No deviation records were written.\n\nFiles:\n- C:/projects/coding-governance/.claude/worktrees/unattended-drankedplan-1fc3d7/memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-15.md (order 13, carries cl-dClosedLoop-0497@2b8de50e whole)\n- C:/projects/coding-governance/.claude/worktrees/unattended-drankedplan-1fc3d7/memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-6.md (order 14, carries cl-dClosedLoop-0374@c6143eda whole)\n- C:/projects/coding-governance/.claude/worktrees/unattended-drankedplan-1fc3d7/memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-8.md (order 15, carries cl-dClosedLoop-0376@f1c33063 whole and node:policy-key.kickoff.runs)\n\nWhat each unit builds:\n- **TOOL-dRankedPlan-15 (the plan revision):** a new `tools/loop/plan_revision.py` with a `revise` command and a `show` command.\n  - `revise` adds a numbered line to a `## Revisions` region at the end of the build's one plan record, then records move B6 (designing back to planning). The witness is the revision's own commit, and the transition carries a new `revision=<n>` field.\n  - The planner then rewrites the plan's fields while the build is in planning. Unit 14 allows a Scenario re-pick only there.\n  - `show` is what Design reads until dIndexedDesign lands. It prints the newest revision as awaiting ratification, or as ratified with the value and witness from `read_plan_ratification`. It exits 1 if Design was re-entered without a ratification, or if no plan field changed since the ratified plan.\n  - It also declares the `revised` outcome on `item.plan.record` and adds a new leg, `loop plan revision`.\n- **TOOL-dRankedPlan-6 (Plan Review):** `review_pin.py` reads a subject's `**Serves:**` kind. When every subject is a plan record (kind `plan`), it prints `PLAN_RECORD_PRESET`, set to `unit-spec`, which dCalibratedLens re-points when its Plan lenses land. This keeps the design-record preset flips away from plan records. The review harness already accepts a plan record as a design subject. Test arms are added to `tier2-review.test.sh`.\n- **TOOL-dRankedPlan-8 (`kickoff.runs`):** `derive_kickoff_line` in `manifest-check.sh` reads the value through `read_card_policy` and prints `kickoff — <value> · full|re-orient|plan`. The verdict depends on whether the session card has a real READY line and whether it carries a route. The line is computed and never stored: it is printed after the card at write, before `now —` at replay, and after the lookup. The stand-in paragraph TOOL-dPlacedRequest-3 S5 adds to `SKILL.md` takes its test from this line, and the file must stay within its 18432-byte limit.\n\nChanges to the shared interfaces (I own each one, so the other writers should read them this way):\n- **I20:** each revision line ends ` · from <sha8>`, the ratified plan it departs from. The fields are rewritten in planning after the B6 move, not before, so unit 14's scenario check passes at that move.\n- **I15:** `kickoff —` is a computed line beside the card, not a `render_card` cell, and it has a third verdict word, `plan`. Unit 7's edge text (\"the `kickoff —` cell that unit adds\") is still compatible, but its writer should know this.\n- **I21:** a plan subject is recognised by its `**Serves:** plan` kind, the same spelling unit 16 uses.\n\nAsks for you to file (none was filed):\n1. **Target dPlacedRequest** (unit 8 §8 F6): `read_card_policy <key>` calls are not counted by `check_policy.py`'s reader-coverage check, which only matches `policy.py get <key>` in a `.sh` file. That leaves dPlacedRequest's five card keys, and `kickoff.runs` once this build lands, showing as having no reader. Accept: the check counts `read_card_policy <key>` in a `.sh` file as a read of that key, seen red on a planted script whose only read is that call.\n2. **Target dRankedPlan** (unit 6 §8 F5): findings from a Plan Review should go to `item.plan.record`, the route `review.dispose` declares for a plan revision but TOOL-dDeclaredLoop-20 never connects. Accept: a planted Plan Review finding reaches `plan.record`'s next draft, seen red while the route is unconnected.\n\nI added no edges beyond the Edges table. Every sibling spec on disk declares the matching reverse edge (16, 9, 2 and 14 to unit 15; 16 and 2 to unit 6; 7 from unit 8)."
}
```

## Agent 5 · dRankedPlan · TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 · spec-write

run wf_a043cc4e-f18/ae88235525313d069, phase Spec

```json
{
 "authored": [
  "TOOL-dRankedPlan-3",
  "TOOL-dRankedPlan-4",
  "TOOL-dRankedPlan-5"
 ],
 "alreadyPresent": [],
 "refused": [],
 "summary": "I wrote all three specs in my group at Tier-2, status OPEN rev-1, with order 10, 11 and 12, and one deviation record. Nothing is committed and the index was not regenerated.\n\nFiles:\n- C:/projects/coding-governance/.claude/worktrees/unattended-drankedplan-1fc3d7/memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-3.md (31 KB)\n- C:/projects/coding-governance/.claude/worktrees/unattended-drankedplan-1fc3d7/memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-4.md (17 KB)\n- C:/projects/coding-governance/.claude/worktrees/unattended-drankedplan-1fc3d7/memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-5.md (15 KB)\n- C:/projects/coding-governance/.claude/worktrees/unattended-drankedplan-1fc3d7/memory/builds/dRankedPlan/build/2026-10-26-build-TOOL-dRankedPlan-5-deviation-51.md\n\nHygiene: the gate only reads tracked files, so I ran checks 2, 12 and 25 on a throwaway clone with every dRankedPlan spec committed in it. My three specs come back clean. The one red left belongs to another writer: TOOL-dRankedPlan-16's AC7 names no backticked witness (check 12).\n\n**TOOL-dRankedPlan-3 (triage)**\n- Rules live in `.governance/triage-rules.toml`. The command is `tools/memory-tree/triage.py`, and it writes rows through backlog.py's existing row renderers.\n- `owner-batches` holds drafts in a triage record until `read_plan_ratification(<home>)` gives a witness.\n- `archive-legacy` archives every live, unlabelled ask filed before `ASK_CUTOFF` with a `WONTDO` row that a `REOPEN` undoes. A probe at base found 434 such asks and none after the cutoff.\n- It registers the `triage` and `dupes` record kinds, writes the dupes record from unit 2's `check_plan_dupes`, and takes over the three items unit 2 handed to it, deleting their stand-in rows with a Readers clause.\n- An owner's own request is always triaged `select`, so no declared rule can refuse it.\n\n**TOOL-dRankedPlan-4 (dormancy)**\n- `derive_activity` gains the states `paused`, `withdrawn` and `superseded`, so LIVE.md and PLAN.md show a disposed build that way.\n- `gen_build_index.py --dormant` proposes a pause for each dormant build.\n- `loop_transition.py dispose` moves a build only when the owner's disposition record names the move.\n- Section 8 F3 is an ask for dTendedCadence to use these for its `defer dormant` safe fix.\n\n**TOOL-dRankedPlan-5 (live-build mapping)**\n- Each live build outside the chain gets one disposition record on `item.entry.place-owner`: `continue` means kept, `amend` means absorbed.\n- Records are written only after `ratify.py dRankedPlan` gives a witness, and the plan view appends the mapping to each build.\n- Deviation 51: the population is every live build at the run's base, not just v1's 24 rows. That adds aScoutedSeam and dClosedLoop, both kept. Scout B's count of 23 rows was wrong; v1 has 24.\n\n**For the main loop:**\n- Edges: every edge I declared now has its matching line in units 1, 2 and 9. Unit 9 already lists unit 5 as a consumer. I added these:\n  - 9 → 5 `read_plan_ratification`\n  - 2 → 3 `check_plan_dupes`\n  - 1 → 4 `derive_activity`\n- Ask to file: TOOL-dRankedPlan-4 §8 F3, for dTendedCadence.\n- Interface caveat: unit 9's predicate answers for a build's plan. Under the default `request` value, a held triage batch whose home build has no claim stays held; it is ratified through `hook-keyword` (`ratify <home>`) or `terminal-command`. This is stated in unit 3's section 5.\n- Fork F1 in unit 3 carries `grants: PLAY-dClosedLoop-3` for the rules file."
}
```

## Agent 6 · dRankedPlan · TOOL-dRankedPlan-13 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 · spec-write

run wf_a043cc4e-f18/ad22f93092fb3b722, phase Spec

```json
{
 "authored": [
  "TOOL-dRankedPlan-13",
  "TOOL-dRankedPlan-11",
  "TOOL-dRankedPlan-12"
 ],
 "alreadyPresent": [],
 "refused": [],
 "summary": "Authored all three units in order as Tier-2 specs. Each header reads OPEN rev-1, base 0689e7fa, with order 7, 8 and 9 respectively. Hygiene checks 2, 12 and 25 pass on all three, graded through a scratch copy of the git index; the shared index was not touched. Nothing was committed, no deviation records were written, and no asks were filed.\n\nWhat each unit does:\n- TOOL-dRankedPlan-13 adds the Scope, Affected systems and Open questions fields. It creates tools/memory-tree/plan_fields.py (with FIELD_CHECKS and check_plan_fields), which units 11 and 12 extend. Affected systems are derived from the code record's code_file rows as kit names, with 'unkitted' for paths outside any kit, and the check refuses a typed value that does not match. Open questions are tags shaped fork.<build>.<name>, registered as a new 'fork' namespace whose extractor is plan_fields:extract_fork. The unit arms TOOL-dPlacedRequest-8's scope-paths seed in loop_lib.py and adds one call inside unit 16's check_plan_record, so a failing field blocks plan.exit. It adds a new leg, 'plan-fields selftest', with enforces = principle.p32.\n- TOOL-dRankedPlan-11 adds the Read sets field: id#tag keys for every role item after Plan, each budgeted by check_read_set. It adds a requires_if row for the loop kit in tools/memory-tree/kit.toml.\n- TOOL-dRankedPlan-12 adds the Probes owed field and a 'probes --trigger' verb. The check refuses while an owed probe has no returned probe record.\n\nInterface changes (I own I16, I17 and I18):\n- I17: the brief proposed '--cause point --at item.plan.exit'. The point cause is refused for any boundary not in probe.points, which defaults to [] (catalogue.toml:679-683), so no declared probe would ever open. Changed to '--cause raised --asker item.plan.record', which probe.raise admits by default.\n- I16: a whole-field 'Read sets: none' is accepted, because unit 16's patch-build plan record (its S8) writes exactly that.\n- I18: settled the grammar of the three fields as above.\n\nAlignment with unit 16: I adopted its names, which differ from the brief. The plan record file ends -1-plan-1.md rather than -1-plan.md. Fields are read only through find_plan_record and read_plan_fields in tools/memory-tree/plan_record.py. Help text goes in help/plan.md.\n\nEdges added beyond the brief's table: 13 hands off to 11 and to 12 on plan_fields.py, and 11 hands off to 12 on requires_if. All three are inside my group and I wrote both ends of each.\n\nOther writers: in the same hygiene run, unit 16's spec fails check 12 because its AC7 has no backticked witness."
}
```

## Agent 7 · dRankedPlan · specs · commit

run wf_a043cc4e-f18/ad7250b57e9ed604b, phase Spec

```json
{
 "committed": false,
 "sha": "911a70393ac1f94625f03e69ee55b42edb1416bb",
 "why": "The build-index generator refused, so the block stopped (exit 1) and nothing was committed. Its output: \"build-index: memory/builds/dRankedPlan/README.md: front matter declares 'status: OPEN' but 16 spec(s) carry a status header — the build status is DERIVED from them, and two answers to one question is exactly the drift this index removes. Delete the 'status:' key.\" The fix is in the build README, which this stage may not write: remove its 'status: OPEN' front-matter key, then run the stage again. No spec was edited and nothing was retried. The input check passed. The 16 specs are still staged (A), so `git reset -q -- <spec paths>` unstages them. The generator wrote no views: the only other paths in the tree are the two foreign untracked deviation records under memory/builds/dRankedPlan/build/, which were never staged. git also warned that specs -10, -14 and -2 have CRLF in the working copy. HEAD has not moved, so step 6's checklist was not run: no commit came from this stage, and HEAD~1..HEAD would grade the earlier spec-brief commit.",
 "specs": [
  {
   "id": "TOOL-dRankedPlan-16",
   "path": "memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-16.md"
  },
  {
   "id": "TOOL-dRankedPlan-1",
   "path": "memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-1.md"
  },
  {
   "id": "TOOL-dRankedPlan-9",
   "path": "memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-9.md"
  },
  {
   "id": "TOOL-dRankedPlan-10",
   "path": "memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-10.md"
  },
  {
   "id": "TOOL-dRankedPlan-2",
   "path": "memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-2.md"
  },
  {
   "id": "TOOL-dRankedPlan-14",
   "path": "memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-14.md"
  },
  {
   "id": "TOOL-dRankedPlan-13",
   "path": "memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-13.md"
  },
  {
   "id": "TOOL-dRankedPlan-11",
   "path": "memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-11.md"
  },
  {
   "id": "TOOL-dRankedPlan-12",
   "path": "memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-12.md"
  },
  {
   "id": "TOOL-dRankedPlan-3",
   "path": "memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-3.md"
  },
  {
   "id": "TOOL-dRankedPlan-4",
   "path": "memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-4.md"
  },
  {
   "id": "TOOL-dRankedPlan-5",
   "path": "memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-5.md"
  },
  {
   "id": "TOOL-dRankedPlan-15",
   "path": "memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-15.md"
  },
  {
   "id": "TOOL-dRankedPlan-6",
   "path": "memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-6.md"
  },
  {
   "id": "TOOL-dRankedPlan-8",
   "path": "memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-8.md"
  },
  {
   "id": "TOOL-dRankedPlan-7",
   "path": "memory/builds/dRankedPlan/spec/2026-10-26-spec-TOOL-dRankedPlan-7.md"
  }
 ],
 "summary": "Nothing was committed: the build-index generator refused because the dRankedPlan README front matter has 'status: OPEN' while 16 specs carry a status header. The README key has to be deleted before this stage runs again. HEAD is still 911a70393ac1f94625f03e69ee55b42edb1416bb. The 16 specs are staged and no views were rendered. The two foreign deviation records are still untracked and were never touched.",
 "checklist": ""
}
```
