# Fold brief: writer 1

**Serves:** research PLAY-dClosedLoop-1

**Your task is to fold the whole-design audit's findings at the 34 places below into dClosedLoop's design
records, as one fold script.** This brief is your instructions, not a spec to review.

## What you fold, and against what

- **The subject is the working tree's design records** under `memory/builds/dClosedLoop/build/`, at commit `8222099f8a619eef461fe91e84bd9f74173be730`.
  The findings were made on a sealed copy into which twelve past defects were planted. The copy is not your subject;
  read nothing in it. The plants are listed in the round record's `[recall-scored]`
  (`build/2026-10-19-build-PLAY-dClosedLoop-1-whole-audit.md`). A finding that describes a plant points at a defect
  the working tree never had.
- **Your records:** architecture-v2's `[chain]` rows of dTrueNorth, dGroundRules, dSafePassage, dOrderedCharter, dFairHearing, dDeclaredLoop, dPlacedRequest, dKeptSession. Edit nothing else. When a place needs an edit in another record, list it under
  *Requests* in your return, with the exact change, and leave it out of your script.
- **Read freely** in the working tree: every design record, the gap register, the design map, `tools/`, `skills/` and
  `.githooks/`. Write only in your scratch folder, `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fold/w1/`. Nothing goes into the repository.

## How you fold

1. **For each place,** read its findings below, then read the place in the working tree. Give it exactly one
   disposition:
   - `fold`: the defect is in the working tree, and the fix follows from what the design already settles. Write it.
   - `fork`: the fix chooses between real options, or changes what the design means. Write no fold. Name the
     question, the options and your recommendation, for the owner.
   - `plant`: the finding describes one of the twelve plants, absent from the working tree. Cite the plant.
   - `not a defect`: the working tree already answers it. Quote where.
   - `duplicate`: another place carries the same defect. Name it, and fold it there.
2. **Write the folds as one Python script,** `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/fold/w1/fold-1.py`, using the build's fold library:

```python
import pathlib, sys
sys.path.insert(0, "C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/expansions")
from fold_lib import Record
R = Record("memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md")
R.sub("<exact old text, matching once>", "<new text>", "<place # and finding ids>")
R.insert_before("<exact anchor text, matching once>", "<text>", "<place # and finding ids>")
R.save()
```

   `sub` refuses unless its old text matches exactly once, so quote enough to be unique. Keep each record's own
   conventions: a clause keeps its `cl-dClosedLoop-NNNN` id and its build row, a new clause takes the next free id after
   the highest in `[clause-ids]` (never a renumber), and a record that logs revisions gets a line saying "Revised
   2026-10-20 by the whole-design audit's fold" with the finding ids. Write prose in the records' own register: short
   declarative sentences, no new terms where a defined one exists.
3. **Fold the smallest change that closes each defect,** as its finding's *Fix* and its skeptic's reading say. Where
   the skeptic narrowed a finding, fold the narrowed one.

## What you return

Your final message, nothing else:
1. **Dispositions,** one row per place: `| # | place | disposition | findings | evidence or the fold's one-line gist |`.
2. **Fold script:** its path, and how many edits it makes in which records.
3. **Forks,** each: `### FK-1-<k> — <question>`, then the options, your recommendation and the findings it rests on.
4. **Requests,** each naming the record, the exact change and the place it serves, or `none`.
5. **Read outside the list above:** `none`, or what and why.

Write nothing to the repository. Your effort is the one your role definition sets.

## The places

### Place 1: architecture-v2 · cl-dClosedLoop-0092 · worst blocker · critical

#### C2-F1 — Clause `cl-dClosedLoop-0093` is missing, so P23 is enforced by a clause that does not exist and gap-orient-05 is carried by no clause
- **Address:** architecture-v2 [chain], dDeclaredLoop row, between cl-dClosedLoop-0092 and cl-dClosedLoop-0094; architecture-v2 [enforcement], row P23
- **Class:** K5, c5
- **Severity:** blocker
- **Evidence:** [enforcement] (v2:1707) reads `| P23 | cl-dClosedLoop-0093 |`, the id's only occurrence. [chain] carries 495 distinct ids, 0093 is the one number missing, and [clause-ids] says "Retired: none". The walk record still lists "claims keyed and trusted by key and source" in dDeclaredLoop's roster (walk:893, walk:1081). P23 lets a claim be acted on only when its stored key recomputes equal and its weakest source is not agent-typed. dDeclaredLoop owns gap-orient-05 ("Claims carry no freshness keys"), and only cl-0092's "each claim's key and verdict printed" touches claim keys.
- **Consequence:** dTrueNorth's carries join and Stage 0's K5 go red on an id no clause carries. No dDeclaredLoop spec builds the trust-by-key rule, so the card, the position engine and every claim reader act on stale or agent-typed claims, the failure gap-orient-05 measured (4 of 17 run claims disagreed).
- **Fix:** Restore cl-dClosedLoop-0093, "claims keyed and trusted by key and source", between 0092 and 0094. Give it its seen-red arm: a planted claim whose key no longer recomputes, and one whose weakest source is agent-typed, are each re-derived and never acted on.
- **Skeptic:** confirmed blocker. Parsing [chain] gives 495 ids with 0093 the only gap, v2:1707 is the id's only occurrence, Stage 0 read 496 clauses on the working tree, and the design's own K5 rule (v2:1679) reds an id no clause carries.

### Place 3: architecture-v2 · cl-dClosedLoop-0016 · worst high · critical

#### A4-F1 — dGroundRules retires `.agent-cap.conf` before any upgrade step or step gate exists
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0016`
- **Class:** K7, c3
- **Severity:** high
- **Scenario:** S7
- **What is wrong:** `cl-dClosedLoop-0016` (dGroundRules) retires agent-cap's clamp of every bound to 1 to 5 "in the same unit with `.agent-cap.conf`", and the clause carries no upgrade step. The step kind (`cl-dClosedLoop-0018`) and the step gate (`cl-dClosedLoop-0027`) arrive with dSafePassage, the next build. Today `tools/hooks/agent-cap.js:68-72` lets `FANOUT_CAP=<n>` lower the cap to min(n, 5), and `runtime.agents-in-flight` defaults to 6.
- **Consequence:** An adopter whose conf lowers the cap to 2 updates past dGroundRules' release, and its limit silently rises to 6, against P38's "keeps working, or warns".
- **Fix:** Defer the retirement to a unit that lands after dSafePassage, shipped as an upgrade step that maps `FANOUT_CAP` to `runtime.agents-in-flight`, seen red on a planted conf. Otherwise keep the conf read as a lowering override until that step lands.
- **Skeptic:** Confirmed high, c3 (batch 1). Readers are re-pointed, but the adopter's value is never carried across.

#### C1-F5 — dGroundRules retires an adopter's `FANOUT_CAP` before any upgrade step exists, silently raising a lowered limit
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0016
- **Class:** K10, c3
- **Severity:** high
- **Evidence:** cl-0016 retires "agent-cap's slot ledger … with `.agent-cap.conf`", and v2:1003 retires `FANOUT_CAP` into `runtime.agents-in-flight`, whose default is 6 (v2:1089). P38 requires an upgrade step, but the step kind (cl-0018) and the first step (cl-0028) arrive in the child dSafePassage. `tools/hooks/agent-cap.js:68-72` honours a repo-lowered `FANOUT_CAP` in a tracked `.agent-cap.conf`.
- **Consequence:** An adopter that set `FANOUT_CAP=2` updates and is held to the default of 6. Its own limit is loosened with no step, order or warning.
- **Fix:** In cl-0016, translate a present `FANOUT_CAP` into `runtime.agents-in-flight`, or hold the conf as a read legacy home, until dSafePassage ships the step. Plant `FANOUT_CAP=2` and check it still caps at 2.
- **Skeptic:** confirmed high (c3). No clause translates an adopter's lowered value.

### Place 4: architecture-v2 · cl-dClosedLoop-0032 · worst high · critical

#### C1-F2 — Re-founding the charter breaks the roles kit's reader of the section-1 rule tags
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0032 (also cl-0042 and cl-0043)
- **Class:** K10, c1
- **Severity:** high
- **Evidence:** layer-instruction R-B requires that retiring a section number re-points its readers in the same unit, naming `roles_lib.py`'s `SECTION_ONE_RE` and the harness prompts that grade by section number. R-D reds a numbered heading. `tools/roles/roles_lib.py:61` is `SECTION_ONE_RE = re.compile(r"^## 1\. ")`, and lines 193-205 raise R0 when there are neither section-1 rule tags nor `## §<n> — ` headings. No [chain] clause carries the re-point; the only `roles_lib` clause is dConvergedCharter's `load_policy`.
- **Consequence:** The level-0 charter has no `## 1.` heading and cl-0042's grammar reds one, so every role render fails with R0 and dOrderedCharter cannot land green.
- **Fix:** In cl-0032, re-point `SECTION_ONE_RE` and the roles `rules:` join to the practice units' tags in the same unit, along with the harness prompts that grade by section number. Prove it with a role render on the re-founded charter.
- **Skeptic:** confirmed high (c1). layer-instruction:438-440 requires the same-unit re-point, no clause carries it, and the roles render legs are on the bar (`gate-legs.json`: "roles render wiring", "roles render selftest").

#### C1-F10 — The re-founded charter leaves out the core principles and the decision principles that outrank practices
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0032
- **Class:** K8
- **Severity:** medium
- **Evidence:** v2 [front-door] lists "the core principles, fixed; the decision principles that resolve unattended forks …, which outrank the practices". cl-0032's envelope list (front door, precedence and override rule, instruction map, active practices, hand-off to the loop, project block) leaves both out, and no clause names decision principles. gap-flow-02 ("nothing ranks them above the charter's adjustable practices") is dOrderedCharter's. P18's only enforcing clauses are cl-0176 and cl-0390 (v2:1702).
- **Consequence:** gap-flow-02 is owned but closed by no clause, and P18's ranking over practices never reaches the charter.
- **Fix:** Add the fixed core principles, rendered from cl-0037's registry, and the ranked decision principles to cl-0032's envelope list.
- **Skeptic:** confirmed medium.

#### C1-F11 — gap-found-18, the `up —` micro-format that asks for a password, is owned by dOrderedCharter but carried by no clause
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0032
- **Class:** K8
- **Severity:** medium
- **Evidence:** layer-expansions:506 records gap-found-18 ("The `up —` micro-format asks for a password value, inviting a secret into chat") under dOrderedCharter, and it is in the build's Gaps owned cell. No clause mentions the micro-format, a password, or keeping credentials out of it. cl-0003's coverage report counts clauses and owned nodes, not gaps, so nothing checks that the gap is carried.
- **Consequence:** The re-founded charter keeps a micro-format that asks for a secret in chat, against the charter's [security] rule.
- **Fix:** In cl-0032 or cl-0042, rewrite the `up —` micro-format to name where a credential lives, never its value. Add a grammar red on a micro-format that asks for one.
- **Skeptic:** confirmed medium.

#### C1-F12 — The override record and the exception register have no home, writer or door
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0032 and cl-dClosedLoop-0037
- **Class:** K3
- **Severity:** medium
- **Evidence:** foundations has the agent record each override ("the rule it set aside and the owner's words"), and every exception "carries its principle, the part it excuses and a reason". layer-memory:399-400 registers both kinds under dOrderedCharter with "writer item not named". cl-0032 and cl-0037 name no home or writer, and memory-plan [doors] lists neither.
- **Consequence:** Both records lack the one door P30 requires before dTotalRecall lands, and the Loop Review's audit of the exception register has nothing to read.
- **Fix:** Have cl-0032 and cl-0037 name each record's home, fields and writer, as stand-ins that dTotalRecall's registry adopts.
- **Skeptic:** confirmed medium, narrowed. Both kinds are registered, so the walker's "no kind" is wrong. The missing writer, home and door stand.

### Place 5: architecture-v2 · cl-dClosedLoop-0039 · worst high · critical

#### C1-F1 — The unit registry leaves out `required-by`, so the missing-unit refusal has nothing to read
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0039, read with cl-dClosedLoop-0041
- **Class:** K6, c3
- **Severity:** high
- **Evidence:** layer-instruction R-A lists the unit row's fields, including "`required-by`: the roles and items that require it, which R-C's 'too little' refusal reads", and systems [design-instruction-writing] lists `required-by` and `enforced-by`. cl-0039's field list copies R-A item for item except `required-by`, and [chain] has no hit for `required-by` at all. cl-0041 and cl-0015 still refuse "a load set missing a required unit".
- **Consequence:** The P27 load-set check has no declared list of required units, so it stays green over nothing or the builder invents the field. adopter-instructions item 6's exclusion refusal ("one another active unit requires") has nothing to read either.
- **Fix:** Add `required-by` and `enforced-by` to cl-0039's fields, and make cl-0041 read `required-by`. Plant a red: a unit named in `required-by` that is missing from a load set.
- **Skeptic:** confirmed high (c3). cl-0039 copies R-A (layer-instruction:383-393) except `required-by`, and no clause registers it.

### Place 6: architecture-v2 · cl-dClosedLoop-0049 · worst high · critical

#### C1-F3 — Three guard-bearing `tags.*` keys owned by dOrderedCharter have no reader, so cl-0014's arm goes red when it lands
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0049 (also cl-0040 and cl-0059)
- **Class:** K4, c1
- **Severity:** high
- **Evidence:** The v2 catalogue (v2:1220-1223) gives `tags.slice`, `tags.retired-cites` and `tags.bare-refs` the Owner dOrderedCharter. systems [design-tags] uses them for `gov tag show`'s leaf slice, the `retired` check and the `resolves` check. None of the three appears in any clause. cl-0049 names only "one resolver (`gov tag show`, `where`, `refs` and `check`) … the `tags` leg pack". cl-0014 is "an arm red when a key whose Owner build has landed has no reader".
- **Consequence:** At dOrderedCharter's landing, dGroundRules' own arm goes red on three keys. If the build lands anyway, `refuse-new` on retired cites and the `never`/`unique` bare-reference rules exist only as catalogue values.
- **Fix:** In cl-0049, name the `resolves` check under `tags.bare-refs`, the `retired` check under `tags.retired-cites` and `gov tag show`'s slice under `tags.slice`, each value with its planted case.
- **Skeptic:** confirmed high (c1). None of the three keys appears in any clause, so cl-0014's arm reds at dOrderedCharter's landing.

### Place 7: architecture-v2 · cl-dClosedLoop-0093 · worst high · critical

#### A2-F1 — P23's only enforcing clause, `cl-dClosedLoop-0093`, exists nowhere in the chain
- **Address:** architecture-v2 [enforcement] `P23`; architecture-v2 [chain] dDeclaredLoop `cl-dClosedLoop-0093`
- **Same as:** A1-F3
- **Skeptic:** Confirmed high, c5 (batch 1), as the same defect at the same addresses.

#### B1-F3 — P23's only enforcing clause, `cl-dClosedLoop-0093`, appears in no `[chain]` row
- **Address:** architecture-v2 [enforcement] (row `P23`, `cl-dClosedLoop-0093`)
- **Class:** K5, c5
- **Severity:** high
- **Scenario:** S2 (B4-F1: S7)
- **Defect:** P23's enforcement row names `cl-dClosedLoop-0093`, and no clause in [chain] carries that id. It is the one gap in 0001 to 0496: dDeclaredLoop's row runs from 0092 to 0094, and [clause-ids] says "Retired: none".
- **Consequence:** No chain build builds the claim-trust rule, that a claim is acted on only when its stored key recomputes equal. `entry.claim`'s own-key retry and every cross-node claim run unchecked. P29's "acted on" rule, which rests on P23's re-derivation, is unenforced too. dTrueNorth's carries join reads a ghost id.
- **Fix:** Restore `cl-dClosedLoop-0093` in dDeclaredLoop's row: the claim's key recomputed, its weakest source not agent-typed, otherwise re-derived or held as evidence. Make Stage 0's K5 arm red an enforcement row that names a ghost id.
- **Skeptic:** Confirmed high. v2:1707 is the only place 0093 appears, and 0092 only prints each claim's key and verdict, so nothing enforces P23.
- **Same as:** B4-F1

#### B4-F1 — P23's enforcement row names a clause id that no chain clause carries
- **Address:** architecture-v2 [enforcement] `cl-dClosedLoop-0093`
- **Class:** K5, c5
- **Severity:** high
- **Scenario:** S7
- **Skeptic:** Confirmed high, a twin of B1-F3. The item is under B1-F3.
- **Same as:** B1-F3

### Place 8: architecture-v2 · cl-dClosedLoop-0116 · worst high · critical

#### C2-F2 — Two of `flow.on-exhausted`'s endings lead to states the transition table does not have
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0116 (with cl-dClosedLoop-0098 and cl-dClosedLoop-0100)
- **Class:** K2, c2
- **Severity:** high
- **Evidence:** cl-0116 gives `park-for-owner` and `close-incomplete` ("closing the build incomplete with its branch and records kept"). flow-steps [transitions] (fs:617-654) refuses any transition the table lacks, has no row from an open state on budget exhaustion, and lists no incomplete or parked-for-owner terminal. Its only parked state, `paused`, is reached only by `life.request`. cl-0100 builds only the declared terminals, and P20 requires a build to end in one. The strict preset sets `park-for-owner` (v2:1452), and cl-0328 also speaks of "a parent ending incomplete".
- **Consequence:** A build that exhausts its budget under `close-incomplete`, or parks under strict's `park-for-owner`, asks for a transition the engine refuses. cl-0118's termination check finds no terminal, and the scenario ends with no terminal and no witness.
- **Fix:** Add rows that cl-0098 and cl-0100 carry: any open state → `incomplete` (terminal) on the exhaustion record, and any open state → `parked-for-owner` with the owner's disposition as its exit. Seed cl-0116's planted endings from those rows.
- **Skeptic:** confirmed high. The ending is real and the table has no row for it.

### Place 46: architecture-v2 · cl-dClosedLoop-0001 · worst medium

#### C1-F8 — Clause ids and the spec's `Carries` relation are registered as no address form or edge, and collide with the `carries` edge
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0001, read against cl-dClosedLoop-0058
- **Class:** K6
- **Severity:** medium
- **Evidence:** P33 addresses a node by "a tag, a section or a native id whose class is registered with its owner", with "typed edges from one closed set". cl-0058 registers native-id classes ("FAMILY-<slug>-<seq>", and later classes by the build that brings them) and pins only as `<tag>@<hash>`, legal only as an `amends` or `supersedes` target. memory-plan [frame] adds "no other edge carries a pin", and memory-plan:193 defines `carries` as "landing → unit, commit". cl-0001 parses `**Carries:** cl-…@<hash8>` lines, and no clause registers `cl-` ids.
- **Consequence:** Once the edge checks land, every chain spec's Carries line and every deviation pin either goes red or stays outside the closed set, as a prose relation P34 forbids.
- **Fix:** In cl-0058, register `cl-<slug>-NNNN` as a native-id class owned by dTrueNorth, with its `@hash8` pin form. Rename the spec relation (for example `carries-clause`), or widen `carries`'s from/to rows.
- **Skeptic:** confirmed medium. Nothing types the spec→clause relation, so it either clashes with `carries` or sits outside P33/P34's closed set.

### Place 47: architecture-v2 · cl-dClosedLoop-0002 · worst medium

#### A4-F12 — The product carries join reds two whole carriers only "and disagreeing"; the bootstrap instrument reds any two
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0002`
- **Class:** K10
- **Severity:** medium
- **Scenario:** S7
- **What is wrong:** `cl-dClosedLoop-0002` reds "two specs carrying one clause whole and disagreeing". carries.py:17 reds "two specs carrying one clause whole, or pinning it to two hashes", and its code (213-216) reds any second whole carrier. whole-audit [instruments] reads "a clause carried whole twice".
- **Consequence:** Once dTrueNorth's leg replaces the instrument, two agreeing whole carriers of one clause go green. The check silently loosens at the hand-over.
- **Fix:** Drop "and disagreeing", so any second whole carrier reds, matching the instrument.
- **Skeptic:** Confirmed medium (batch 1). A product spec written to the clause's wording would let two agreeing whole carriers pass.

#### B2-F11 — `cl-dClosedLoop-0002` reds two whole carriers only when they disagree
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0002`
- **Class:** K8
- **Severity:** medium
- **Scenario:** S7
- **Defect:** 0002 reds "two specs carrying one clause whole and disagreeing" without saying what they disagree on. carries.py reds any second whole carrier.
- **Consequence:** A product join built from the clause passes two units that carry one clause whole at the same pin, so one clause is built twice.
- **Fix:** Write "two specs carrying one clause whole, or pinning it to two hashes, red", as the instrument reads.
- **Skeptic:** Confirmed medium. research-final-coverage maps the case to "carried whole by 2 specs".

#### C1-F18 — "A ninth join": spec-tokens already has nine
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0002
- **Class:** K6
- **Severity:** low
- **Evidence:** cl-0002 calls the carries join "a ninth join of the spec tokens leg". `tools/check-spec-tokens.py:30-36` counts eight joins, and `:959-960` adds a ninth, "THE COVERS JOIN (TOOL-aMendedFleet-75)".
- **Consequence:** The count is stale, and a builder looking for the ninth slot finds `covers` there.
- **Fix:** Call it "a further join".
- **Skeptic:** confirmed low. The carries join would be the tenth.

### Place 48: architecture-v2 · cl-dClosedLoop-0003 · worst medium

#### B2-F10 — `cl-dClosedLoop-0003` can be read to refuse every chain build's first spec
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0003`
- **Class:** K7
- **Severity:** medium (the walker graded it high, c1)
- **Scenario:** S7
- **Defect:** 0003 refuses "a chain build's spec in progress while its build's coverage is red" without naming the status. Read as "being drafted", it refuses every first spec, since coverage stays red until specs carry the clauses.
- **Consequence:** A spec writer can build a refusal that blocks dTrueNorth's first spec and every later chain build's.
- **Fix:** Refuse a spec in progress only on the per-spec arms (ghost, unbound, stale, ambiguous, dropped). Keep the uncarried and unowned-node arms for the Design exit, as carries.py does. Seen-red the refusal on a planted ghost.
- **Skeptic:** Confirmed medium. TEMPLATE-SPEC defines `INPROGRESS` as "approved, build underway", under which the refusal applies only after the Design exit, as in carries.py. The blocking outcome follows only from the looser reading the wording allows.

### Place 49: architecture-v2 · cl-dClosedLoop-0004 · worst medium

#### A4-F10 — The deviation record is no registered kind
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0004`
- **Class:** K3
- **Severity:** medium
- **Scenario:** S7
- **What is wrong:** `cl-dClosedLoop-0004` joins "the deviation record, its kind" to check 21's kinds. Neither layer-memory nor memory-plan mentions a deviation kind, and none of the design map's 79 record-kind nodes is one.
- **Consequence:** dTrueNorth's deviation records have no owner, writer or reader in the kind registry. K3 and P16's register cannot see them, and dConvergedCharter's `cl-dClosedLoop-0480` has no row to move.
- **Fix:** Add a `deviation` row to layer-memory's kind table: owner dTrueNorth, writer the departing unit's commit, readers deviations.py, asbuilt.py, `cl-dClosedLoop-0119` and `cl-dClosedLoop-0412`.
- **Skeptic:** Confirmed medium (batch 1). The only deviation node in the design map is `policy-namespace.deviation`.

#### A4-F11 — dTrueNorth's deviation join needs approval rules that two later builds provide
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0004`
- **Class:** K7
- **Severity:** medium
- **Scenario:** S7
- **What is wrong:** `cl-dClosedLoop-0004` reds "an approver below the risk". The risk-to-approver mapping is the `deviation.approval` row (v2:1164, owner dDeclaredLoop), built later by `cl-dClosedLoop-0119` with dOrderedCharter's classifier. `cl-dClosedLoop-0004` names no stand-in, though the design names stand-ins elsewhere (`cl-dClosedLoop-0229`).
- **Consequence:** dTrueNorth's unit cannot state which mapping its join reads. A spec writer hard-codes one that `cl-dClosedLoop-0119` may later contradict; deviations.py:82-86 hard-codes the by-risk ranks today.
- **Fix:** State in `cl-dClosedLoop-0004` that the join reads by-risk with a fixed classifier until dDeclaredLoop lands `deviation.approval`, as deviations.py does, and add a tolerance row.
- **Skeptic:** Confirmed medium (batch 1).

#### C1-F9 — The deviation record has no home or writer, and lacks fields its settling record sets
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0004
- **Class:** K3
- **Severity:** medium
- **Evidence:** final-questions [deviation] sets the record's fields: "its id; the hand-off; … the approver and where the approval is recorded; … and its cause (P35)". cl-0004's fields are "the departure's address, before and after, cause class, reason, evidence, risk class, approver and follow-through". The id, the hand-off, the approval's location and the cause are missing, and no home or writer is named.
- **Consequence:** The record has no home or door, and a spec built from the clause lacks fields the design settled.
- **Fix:** Give the record a home and a writer in cl-0004, and add the id, the hand-off, the approval location and `caused-by`.
- **Skeptic:** confirmed medium, narrowed. cl-0004 does register the kind ("joined to check 21's kinds"), and cl-0006 reads the record. The by-risk join reads the risk class and the approver, both present, so the missing hand-off does not stop it picking the approver. The unnamed home and writer and the missing fields stand.

### Place 50: architecture-v2 · cl-dClosedLoop-0015 · worst medium

#### C1-F13 — Cap values have two homes, and `budgets.*` is read by no clause
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0015 and cl-dClosedLoop-0041
- **Class:** K4
- **Severity:** medium
- **Evidence:** The catalogue (v2:1217) and night-pass-two [p5-caps] (406-407) put each cap's value under `budgets.*`, the owner's. cl-0015 reads "each cap's value … from its one declaration" without naming it, and cl-0041 extends `template-size-limits.txt`. Stage 0's K4 lists `budgets.*` as unread. cl-0461 ("caps re-derived from evidence"), dCalibratedLens's only cap clause, does not name the key either.
- **Consequence:** Load-point caps are declared in `template-size-limits.txt` while the catalogue puts them under `budgets.*`. That is two answers to one fact, and the owner's policy write moves nothing a gate reads.
- **Fix:** Have cl-0015 name the one declaration: either `budgets.*`, with `template-size-limits.txt` migrated into it, or `template-size-limits.txt` alone, with `budgets.*` re-scoped to name it.
- **Skeptic:** confirmed medium.

#### C1-F14 — dGroundRules' witness needs load sets and a composition that only dOrderedCharter builds
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0015
- **Class:** K7
- **Severity:** medium
- **Evidence:** cl-0015 is "seen … on a load set missing a required unit and a composition over a harness's own limit, both still refused under `warn`". Load sets are cl-0041's and the composition is cl-0064's, both in the descendant dOrderedCharter.
- **Consequence:** dGroundRules' acceptance cannot be run when it lands.
- **Fix:** Plant today's consumer limit at dGroundRules (`CODEX_MAX=32768`, `tools/agent-instructions/adopt-agent-instructions.sh:31`), and move the load-set and composition cases to cl-0041 and cl-0064.
- **Skeptic:** confirmed medium. The consumer limit exists today at the cited line.

### Place 51: architecture-v2 · cl-dClosedLoop-0026 · worst medium

#### C1-F15 — `install.retired-edits`' `keep` and `delete` values have no arm, and `delete` loses edits
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0026
- **Class:** K9
- **Severity:** medium
- **Evidence:** The catalogue (v2:1277) allows `order`, `keep` and `delete`. research-supersession:175 says "`keep` is today's silent `patched`; `delete` loses edits". cl-0026 builds and plants only the order arm ("extended with the order arm"), and no clause or flow item gives the other two an arm.
- **Consequence:** The schema accepts two values that no code routes. If `delete` is ever wired, it removes an adopter's edited file (P19, P38).
- **Fix:** Give `keep` and `delete` their arms and planted cases in cl-0026, or drop them from the allowed values.
- **Skeptic:** confirmed medium.

### Place 52: architecture-v2 · cl-dClosedLoop-0028 · worst medium · includes an unverified finding

#### A4-F7 — The floor step is "the step kind's first step", but its progress field only arrives in the schema-4 step
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0028`
- **Claimed:** a kill after the floor step on a schema-3 receipt re-runs it or leaves the receipt unreadable.
- **Skeptic:** Refuted (batch 1). The clause does order the steps, with the schema-4 step after the floor step. `cl-dClosedLoop-0019` skips a step whose witness holds and keeps it re-runnable, `cl-dClosedLoop-0022` plants the kill and the converging re-run, and a schema-3 receipt already carries `gov_commit` (govkit.py:8020). A kill after the floor step re-runs as a witness skip, and nothing writes `steps` into a schema-3 receipt.
- **Second skeptic:** Confirmed medium. `cl-dClosedLoop-0028` makes the floor raise "the step kind's first step". `cl-dClosedLoop-0020` adds the per-step `steps` progress field to receipt schema 4, and that change is itself shipped as an upgrade step. No clause orders the two, or says where progress lands for a step completed on a schema-3 receipt. This collides with `cl-dClosedLoop-0019` ("the receipt advancing per completed step") and with `cl-dClosedLoop-0022` ("the k-th step made to exit 1 and the receipt naming step k-1"). One part of the stated consequence is overstated: a re-run of the floor step after a kill is skipped because its witness holds (0019).

#### C1-F16 — The floor's down step checks TOML only, while the up step removes the guard against newer Python syntax
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0028
- **Class:** K10
- **Severity:** medium
- **Evidence:** cl-0028's down restores the old declaration, "refusing while a tracked TOML file fails to parse under the floor it restores". The same clause retires "the PEP 701 text ban in `merge-rows.test.sh`" (`tools/memory-tree/merge-rows.test.sh:353-355`, "PEP 701, 3.12+"). gap-tool-22 gives the old floor as 3.11.
- **Consequence:** After the raise, 3.12+ syntax can land. A rollback then restores a 3.11 floor under tracked Python that will not compile.
- **Fix:** Make the down refuse while any tracked `.py` fails `compile()` under the floor it restores. Plant a PEP 701 f-string landed after the raise.
- **Skeptic:** confirmed medium.

### Place 53: architecture-v2 · cl-dClosedLoop-0048 · worst medium

#### C1-F6 — The inventory of by-path readers for the moved grammar misses readers
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0048
- **Class:** K10
- **Severity:** medium
- **Evidence:** cl-0048 builds "from an inventory of every reader of `extract.py` and `recall_conf.py` by path", and names check-verdict-epoch.sh, migrate_backlog.py and merge-rows.test.sh. `grep -rln 'extract\.py\|recall_conf' tools skills .githooks` also finds `skills/session-kickoff/manifest-check.test.sh:1325-1328` (it hides `extract.py` and expects the "id grammar lives in the memory-recall kit" NOTE), `.githooks/straggler-guard.test.sh:84` and `tools/unattended/check-unattended.sh:2035`.
- **Consequence:** After the move, the kickoff F1 arm hides a file that no longer holds the grammar. It either goes red on the bar or passes without testing the no-grammar path.
- **Fix:** Derive cl-0048's inventory from that grep and name every reader it finds. Each one gets re-pointed and its arm re-seen red.
- **Skeptic:** confirmed medium. The grep finds the three cited readers and others besides, such as `transition-audit.test.sh`.

### Place 54: architecture-v2 · cl-dClosedLoop-0070 · worst medium

#### C2-F6 — dFairHearing's breakpoint items depend on, and route to, items owned by a later build
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0070 and cl-dClosedLoop-0075
- **Class:** K6
- **Severity:** medium
- **Evidence:** flow-steps `review.pin` (fs:484), owned by dFairHearing, needs `review.trigger`, and `review.report` (fs:487) routes to `review.dispose`. Both are dDeclaredLoop's, a descendant. v2:483 requires "each new dependency on a later build gets a stand-in, a class row or a move". cl-0070 and cl-0075 declare none, and Stage 0 leaves the lead UNCLASSED.
- **Consequence:** dFairHearing's acceptance cannot run its items end to end in order, or it reaches into dDeclaredLoop's program.
- **Fix:** Add a stand-in to cl-0070 and cl-0075: until dDeclaredLoop lands, the harness is invoked directly with its pin arguments, and the report's dispositions are written to the review record.
- **Skeptic:** confirmed medium.

### Place 55: architecture-v2 · cl-dClosedLoop-0098 · worst medium

#### C2-F8 — The spine's transition table routes to and witnesses items owned by later builds
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0098 and cl-dClosedLoop-0100
- **Class:** K6
- **Severity:** medium
- **Evidence:** flow-steps [transitions] rows route on items owned by non-ancestors, such as "planning | `plan.exit` | designing" and "testing | `test.exit` | deploying". Stage 0 lists seven such leads for dDeclaredLoop (build.distill, build.ratify, deploy.notify, design.ready, plan.exit, plan.input, test.exit), all UNCLASSED. cl-0098 says only "the engine refusing any transition it lacks" and declares no stand-in, which v2:483 requires.
- **Consequence:** dDeclaredLoop's engine is specced against witnesses no ancestor produces, so its acceptance cannot be planted from real items.
- **Fix:** In cl-0098, have each row name its exit item by tag, with a fixture witness until that item's build lands. Class the seven Stage 0 leads in [stage0-classes].
- **Skeptic:** confirmed medium.

### Place 56: architecture-v2 · cl-dClosedLoop-0106 · worst medium

#### C2-F3 — The runaway ceiling gets two homes and two rules for a round count at the ceiling
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0106, against cl-dClosedLoop-0139
- **Class:** K9
- **Severity:** medium
- **Evidence:** cl-0106 moves `RUNAWAY_CEILING` "into the loop kit's definition" and refuses "a planted round count at the ceiling". The catalogue (v2:1127-1128) makes `review.max-rounds` the ceiling as a policy value. The pair rule (v2:1299) and cl-0139 hold `review.design.round-count` "at or below `review.max-rounds`". `tools/unattended/unattended.sh:783` refuses at or above the ceiling (`-lt`).
- **Consequence:** A repository that sets `round-count = max-rounds` passes dKeptSession's preset check and is refused by dDeclaredLoop's arm. The ceiling also ends up both a loop-kit constant and a policy key.
- **Fix:** In cl-0106, make the ceiling the policy key `review.max-rounds`. Plant a round count above it, refused, and one equal to it, admitted.
- **Skeptic:** confirmed medium.

### Place 57: architecture-v2 · cl-dClosedLoop-0115 · worst medium

#### A3-F6 — The shared rework budget has no declared home or writer once its build closes
- **Address:** architecture-v2 [chain] `cl-dClosedLoop-0115`, `cl-dClosedLoop-0440`
- **Class:** K10
- **Severity:** medium
- **Scenario:** S3
- **What is wrong:** `cl-dClosedLoop-0115` keeps the budget "in its transition record", which every step's exit item writes (layer-memory:436), and the originating build has no step exit after `deploy.close`. `cl-dClosedLoop-0440` has patch builds draw on that build's budget. No clause or row names who writes a patch's draw into the closed build's record, or how two concurrent draws serialise.
- **Consequence:** Concurrent patch builds read the same remaining budget and both draw on it. Either the draws go to an unwritten record, or one draw is lost.
- **Fix:** Add a budget ledger per root build, appended by compare-and-swap under the root's claim ref, each patch reaching its root through its `patches` edge. Show it red on two planted concurrent draws.
- **Skeptic:** Confirmed medium (batch 1).

### Place 58: architecture-v2 · cl-dClosedLoop-0118 · worst medium

#### C2-F13 — The termination check's red case plants only a raised budget
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0118
- **Class:** K10
- **Severity:** medium
- **Evidence:** stall-and-loop [design] item 8 (s&l:244) makes raising any loop bound (the budget, a round count, a retry count, a deadline) a loosening, and its [chain] (s&l:310) plants "an unattended raise of a loop bound". cl-0118 reads a raise of a loop bound as a loosening but plants only "an unattended raise of the budget".
- **Consequence:** An unattended raise of `review.max-rounds`, `flow.route-backs` or `flow.wait-ceiling` can pass a check only ever seen red on the budget, so the guard certifies more than it checks.
- **Fix:** Add one planted unattended raise each for a round count, a retry count and a deadline to cl-0118's red list.
- **Skeptic:** confirmed medium. v2 narrowed the settling record's planted case.

### Place 59: architecture-v2 · cl-dClosedLoop-0120 · worst medium

#### C2-F10 — dPlacedRequest's keys `leases.granularity` and `card.follows` are named by no clause
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0120 and cl-dClosedLoop-0121
- **Class:** K4
- **Severity:** medium (the walker said low)
- **Evidence:** Both keys appear in v2 only in the catalogue (v2:1031, 1042), the presets (1354, 1365) and line 62, never in [chain]. cl-0120 says only "one lease grammar for builds, units and cadence runs", and cl-0121 does not say when the card re-renders.
- **Consequence:** Presets set these keys (velocity sets `leases.granularity` to `build`), but nothing reads them.
- **Fix:** Name `leases.granularity` in cl-0120 and `card.follows` in cl-0121, each with one arm per value.
- **Skeptic:** confirmed medium, above the walker's low. Velocity's `build` value has nothing to route it, which a spec writer would trip over; it is not a wording defect.

### Place 60: architecture-v2 · cl-dClosedLoop-0122 · worst medium

#### C2-F7 — Entry's placing items route to Plan and Design items no ancestor builds
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0122 and cl-dClosedLoop-0123
- **Class:** K6
- **Severity:** medium
- **Evidence:** flow-steps `entry.place` (fs:83) routes "new → `entry.claim`, then Plan, or `plan.triage-rule`". Those items are owned by dRankedPlan and dIndexedDesign, neither an ancestor of dPlacedRequest (v2:1639, 1648-1649). cl-0125 declares "a stand-in for each later part it rests on"; cl-0122 and cl-0123 declare none.
- **Consequence:** A request placed after dPlacedRequest lands, but before dRankedPlan and dIndexedDesign land, routes to items that do not exist.
- **Fix:** Give cl-0123 cl-0125's stand-in sentence: until Plan's and Design's items land, a `new` or `amend` placement files an owner item carrying the claim.
- **Skeptic:** confirmed medium. v2 has no general stand-in rule outside the chain rows.

### Place 61: architecture-v2 · cl-dClosedLoop-0132 · worst medium

#### C2-F4 — The pre-claim budget is keyed to an intake record that does not exist until a later build
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0132
- **Class:** K7
- **Severity:** medium
- **Evidence:** cl-0132 keys the budget "to the intake's content key". The design map gives `record-kind.intake` to dWellOiledMachine, which is not an ancestor of dPlacedRequest, and cl-0123 admits the same dependency. flow-steps `entry.intake` (fs:80) leaves intake absent when the hook crashes or never fires.
- **Consequence:** Before dWellOiledMachine lands, and whenever the intake hook never fired, the budget has no key.
- **Fix:** Key the budget to a content key cl-0132 computes from the request text, which the claim commit already carries, and key an absent intake the same way. Plant one red case with no intake record.
- **Skeptic:** confirmed medium, narrowed. `flow.route-backs`, in Entry's policy list (fs:105), still caps returns to `entry.place`, so placement loops are not fully unbounded.

### Place 62: architecture-v2 · cl-dClosedLoop-0134 · worst medium

#### A2-F6 — Only lease expiry has a declared clock; every other S2 deadline reads a node's raw clock
- **Address:** architecture-v2 [chain] dPlacedRequest `cl-dClosedLoop-0134`, `cl-dClosedLoop-0138`; dKeptSession `cl-dClosedLoop-0162`
- **Class:** K10
- **Severity:** medium
- **Scenario:** S2
- **What is wrong:** Only `cl-dClosedLoop-0135`, the `leases.expiry-hours` row and cloud-and-scale:211-214 declare a clock, and all three apply it to lease expiry alone. `cl-dClosedLoop-0138`'s `leases.offer-seconds`, `cl-dClosedLoop-0162`'s `flow.wait-ceiling` and `cl-dClosedLoop-0134`'s `leases.queued-claim-days` name none.
- **Consequence:** With node x's clock ahead, x claims units offered to d before the offer expires, and Y writes its default answer while d still counts the wait as live.
- **Fix:** State one rule for every cross-node deadline: elapsed time measured by the observer since it first saw the record, or a stamp corrected by the registered offset. See each deadline red on a reader planted a day ahead.
- **Skeptic:** Confirmed medium (batch 1).

### Place 63: architecture-v2 · cl-dClosedLoop-0143 · worst medium

#### C2-F15 — The mailbox message kind names no writer, and no reader carries the transition refusal
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0143
- **Class:** K3
- **Severity:** medium
- **Evidence:** Coordination item 6 (co:116-117) refuses every transition while a message "is neither answered nor acknowledged". cl-0143 says only "read and disposed at every transition". No flow-steps item reads the mailbox at an exit (the only item hit is fs:374, on the release hold), and layer-memory:438 says "writer item not named". cl-0162 implies the hold ("past which … transitions go on") but does not refuse.
- **Consequence:** The refusal that makes a transition wait on an unanswered message has no item to carry it, so a spec can build the mailbox without it.
- **Fix:** In cl-0143, name the writer (the posting command per kind) and the reader: each exit item refuses on an undisposed message until `flow.wait-ceiling`. Plant one red case.
- **Skeptic:** confirmed medium.

### Place 64: architecture-v2 · cl-dClosedLoop-0145 · worst medium

#### C2-F11 — dKeptSession's keys `deps.coordination`, `deps.early-build` and `orient.budget` are named by no clause
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0145 and cl-dClosedLoop-0147
- **Class:** K4
- **Severity:** medium
- **Evidence:** No [chain] row names any of the three keys. cl-0145 says "dependency coordination by the parent's lease, interfaces confirmed at Design's exit", and cl-0147 "orientation cost recorded per stage". Coordination item 8 reads both `deps.*` keys, and strict sets its own values for all three (v2:1361, 1362, 1374).
- **Consequence:** strict's orientation ceiling is never read, and no clause carries strict's dependency posture.
- **Fix:** Name all three keys in cl-0145 and cl-0147, each seen on its strict value.
- **Skeptic:** confirmed medium, narrowed. flow-steps lists `deps.coordination` in Plan's policies (fs:147) and `deps.early-build` in Design's (fs:200), so "strict behaves like standard" holds whole only for `orient.budget`.

### Place 65: architecture-v2 · cl-dClosedLoop-0150 · worst medium

#### C2-F12 — Two clauses give two rules for when a fresh session is recommended
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0150, against cl-dClosedLoop-0121
- **Class:** K9
- **Severity:** medium
- **Evidence:** cl-0121 (dPlacedRequest) recommends a fresh session "by `resume.context`". cl-0150 (dKeptSession) recommends "a fresh session in the build's worktree … until the card-import fixture passes", with no key and no precedence. Velocity sets `resume.context` to `always-resume` (v2:1373).
- **Consequence:** Under velocity, while the fixture is red, one build recommends resuming and the other a fresh session, so the policy key is bypassed.
- **Fix:** Make cl-0150 a gate on cl-0121's key: while the card-import fixture is red, `always-resume` reads as `fresh-when-idle`, and that is reported.
- **Skeptic:** confirmed medium.

### Place 66: architecture-v2 · cl-dClosedLoop-0154 · worst medium

#### CS4-F1 — The policy namespaces' purposes are reviewed under a key no ancestor of dKeptSession registers
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0154
- **Class:** K6
- **Severity:** medium
- **Evidence:** cl-0154: "the policy namespaces' purposes, reviewed". project-map:660-666 reviews an existing node "under `memory.map-purpose: review` (PM-5)", by "the unit that adds its namespace's purpose field". v2:1248 gives `memory.map-purpose` to dTotalRecall, which is neither ancestor nor descendant of dKeptSession (whose parents are dDeclaredLoop and dPlacedRequest). project-map:668 covers only "Builds after dTotalRecall", and project-map:657 still names dDeclaredLoop as the owner of the policy namespace's purpose.
- **Consequence:** A dKeptSession spec carrying the clause has no review rule and no ask route, and it may land before the key exists.
- **Fix:** Name `memory.map-purpose` in cl-0154 with a stand-in until dTotalRecall lands, or move the review to cl-0227's reviewers. Correct project-map:657.
- **Skeptic:** raised by skeptic batch 4 on re-walking cl-0154, which walker 2 had passed as holding. No second skeptic judged it.

### Place 67: architecture-v2 · cl-dClosedLoop-0160 · worst medium

#### CS2-F1 — A message retried from a new session is not refused as a duplicate
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0160 (with cl-dClosedLoop-0150 and cl-dClosedLoop-0143)
- **Class:** K10
- **Severity:** medium
- **Evidence:** cl-0160 derives a message's id "from its sender's session, and its act once Runtime mints acts". Acts are dWellOiledMachine's, and that build is not an ancestor of dKeptSession. cl-0143 keys each mail ref by session. cl-0150, in the same build, recommends a fresh session, and the `resume.context` default is `fresh-when-idle`.
- **Consequence:** A post retried after a crash from a fresh session gets a new id and lands in a new ref, so the duplicate lands. The "post retried after a crash" case passes only when the retry runs in the same session.
- **Fix:** Until acts are minted, derive the id from the build, the item instance key cl-0092 computes, the pass, the kind, the subject and the answered id, not from the session. Plant the retry from a new session and see it refused.
- **Skeptic:** raised by skeptic batch 2 on re-walking cl-0160, which walker 2 had passed as holding. No second skeptic judged it.

### Place 153: architecture-v2 · cl-dClosedLoop-0006 · worst low

#### C1-F7 — The deviation clauses rely on a later build's overlay grammar and approval rule, and name no stand-in
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0006 (also cl-0004)
- **Class:** K7
- **Severity:** low (the walker said medium)
- **Evidence:** final-questions [spine] puts each deviation's `amends` or `supersedes <clause-id>@<hash8>` row "in dOrderedCharter's overlay grammar". cl-0006 applies those rows, and cl-0004 reds "an approver below the risk", whose rule is `deviation.approval` (dDeclaredLoop's). dTrueNorth is the chain's root, and neither clause names a stand-in.
- **Consequence:** A dTrueNorth spec writer has to find the interim forms outside the clauses.
- **Fix:** Have cl-0004 and cl-0006 name their stand-ins, a fixed by-risk table and a local row form, each re-pointed when dOrderedCharter and dDeclaredLoop land.
- **Skeptic:** confirmed low. "Cannot be built" is refuted by this build's own instruments: `asbuilt.py` defines a local row form (`**Follow-through:** amends <clause-id>@<hash8>`), `deviations.py` hard-codes the by-risk table, and final-questions [bootstrap] turns them into product code with today's tools. What remains is the unnamed stand-in.

### Place 154: architecture-v2 · cl-dClosedLoop-0038 · worst low

#### C1-F20 — The card for other harnesses goes through Runtime harness adapters, which dWellOiledMachine builds later
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0038
- **Class:** K6
- **Severity:** low
- **Evidence:** cl-0038 delivers "another harness's [card] through its Runtime harness adapter". `runtime.harnesses` is owned by dWellOiledMachine (v2:1093), not an ancestor of dOrderedCharter, and no stand-in is named.
- **Consequence:** There is no adapter to deliver through when the build lands.
- **Fix:** Name agent-instructions' wiring as the stand-in until the adapters land.
- **Skeptic:** confirmed low.

### Place 155: architecture-v2 · cl-dClosedLoop-0045 · worst low

#### C1-F19 — "Instruction packs … into the preset catalogue" reads against the rule that presets never touch `charter.practices`
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0045
- **Class:** K9
- **Severity:** low
- **Evidence:** cl-0045: "instruction packs extending `charter.practices` into the preset catalogue". v2:1301-1302: "Presets never touch … `charter.practices`".
- **Consequence:** A builder may add packs to the policy presets, against the never-touch rule.
- **Fix:** Name it "a pack catalogue", separate from the policy presets.
- **Skeptic:** confirmed low. layer-instruction:584's "a preset catalogue" is a different thing from the policy presets, so this is wording only.

### Place 156: architecture-v2 · cl-dClosedLoop-0078 · worst low

#### C2-F16 — "The panel's internals" does not carry the untyped harness agent gap that dFairHearing owns
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0078
- **Class:** K1
- **Severity:** low
- **Evidence:** gap-review-13 ("The review harness spawns an untyped agent that no stage declares") is dFairHearing's (systems:1000). cl-0078 says only "the panel's internals". The only "every stage naming its role" clause is cl-0187, in the later dBoundRoles.
- **Consequence:** A spec writer cannot tell from cl-0078 that the untyped spawn must be typed and declared.
- **Fix:** Add to cl-0078: "every agent the harness spawns typed and declared in a stage, seen red on a planted untyped spawn".
- **Skeptic:** confirmed low.

### Place 157: architecture-v2 · cl-dClosedLoop-0087 · worst low

#### C2-F9 — dDeclaredLoop's guard-bearing keys `floor` and `transitions.record` are named by no clause
- **Address:** architecture-v2 [chain] cl-dClosedLoop-0087 and cl-dClosedLoop-0088
- **Class:** K4
- **Severity:** low (the walker said medium)
- **Evidence:** Stage 0's K4 lists `floor` and `transitions.record` as unread and guard-bearing. cl-0087 reads "the guard, the TTY CLI and the default floor", and cl-0088 "the transition record three ways"; neither names its key. [floor] makes each invariant "switchable only under the policy guard".
- **Consequence:** The switch that turns a floor invariant off, and the subset choice of transition-record channels, have no specced reader.
- **Fix:** Name `floor` in cl-0087 and `transitions.record` in cl-0088, each with a planted value seen red: an invariant switched off without the guard is refused, and an empty channel set is refused.
- **Skeptic:** confirmed low. The walker's "fails open" does not follow: hard-wiring the floor all on and all three channels is the stricter state, and cl-0014's arm reds an unread key once its Owner has landed.
