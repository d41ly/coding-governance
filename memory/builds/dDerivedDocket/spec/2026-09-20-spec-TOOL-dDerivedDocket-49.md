# TOOL-dDerivedDocket-49 — one declared ladder decides which next: shape the plan prints

**Status:** SPECCED · rev-1 · 2026-09-20 · node d · Tier-2 · base fb07ca25 · streams tooling · order 15

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-20-review-TOOL-dDerivedDocket-48-spec-audit-g7-round1.md](../reviews/2026-09-20-review-TOOL-dDerivedDocket-48-spec-audit-g7-round1.md) | spec-audit | TOOL-dDerivedDocket-48 TOOL-dDerivedDocket-50 TOOL-dDerivedDocket-51 TOOL-dDerivedDocket-52 TOOL-dDerivedDocket-53 TOOL-dDerivedDocket-54 |

<!-- /gen:spec-records -->

## 1. Goal

`verb_plan` picks its `next:` line by first-wins accumulation across two loops
(`tools/unattended/unattended.sh:2253-2254` and `:2262`, read at `:2274-2280`), so the precedence
between the shapes is an artefact of iteration order and exists only in prose. Unit 16 adds a third
shape whose position that prose pins and whose own fixture CONTRADICTED it, which is the defect
this unit is promoted from. That fixture has since moved: unit 16's AC18 carries the two-arm
replacement wording at HEAD
(`memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-16.md:480-502`, logged in
that spec's §9 at `:640-644`). What remains is to make the precedence a DECLARED ladder with one
rung per shape, give every rung that exists today a failing case, pin the position the new rung
takes, and keep that landed criterion in step with it.

## 2. Scope (IN)

- **S1** One selector, `derive_next_shape`, in `tools/unattended/unattended.sh` beside `plan_row`
  and `missing_units`. It takes the first live unit and its state, the first MISSING roster id, the
  first undecided ask id and the graded flag, and returns exactly one shape string. `verb_plan`
  stops accumulating: no branch of its two loops assigns the next line any more. Observed by AC1.
- **S2** The rung table is DECLARED, in rung order, in one block the selector walks, with one line
  per rung naming the rung and the shape it prints. Five rungs: a live unit, a MISSING roster unit,
  an undecided ask, nothing graded, everything terminal. Observed by AC5.
- **S3** The ask rung's POSITION is pinned here and its PREDICATE is not built here. It sits third,
  after both unit rungs and before both terminal rungs, which is the ordering unit 16's design
  states and which that unit's own fixture contradicted until AC18's fold landed. Its input is
  empty on every call until unit 16 fills it, so the ladder prints exactly what the driver prints
  today. Observed by AC5 and AC6.
- **S4** The three existing shape literals are byte-identical after this unit, so leg check 30's
  conjunction stays reachable and the driver suite's existing terminal-wording arm
  (`tools/unattended/unattended.test.sh:1802`) still hits. Observed by AC6.
- **S5** Every rung that exists today gets a failing case: a fixture in which it fires and a fixture
  in which the rung above it takes the line instead. The MISSING-against-terminal pair is the same
  boundary the promoted finding names one rung lower, observed where it can be observed at this
  unit's order. Observed by AC2, AC3 and AC4.
- **S6** Unit 16's AC18 is kept IN STEP with this ladder, and is no longer handed over as a
  cross-edit: that text is already landed. At HEAD AC18 asserts the MISSING shape over the fixture
  that holds two MISSING units, and a second arm over the same fixture with both MISSING units
  retired asserts the flip to the undecided one
  (`memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-16.md:480-502`, logged in
  that spec's §9 at `:640-644`). This unit asserts that text rather than writing it, so a later
  re-fold of AC18 cannot silently re-open the rung order S3 pins. The runtime FLIP stays unit 16's:
  it needs the ask rung's predicate, which that unit builds, and is observed by its own second arm
  at its own pass. Observed by AC9.
- **S7** Every new refusal or shape branch gets an arm in `tools/unattended/unattended.test.sh`,
  each observed RED with its fix unstaged, and the `tools/unattended/unattended.sh` pair of
  `ARMS_FLOORS` in `.memory-tree.conf` moves in the same commit. Observed by AC8.
- **S8** This unit's delta on every capped carrier is ZERO. It writes no conf key and no guide,
  Skill or dossier prose; the unattended dossier held 20387 B of a 20480 B cap when this spec was
  written, and no claim key moves because the codebase map does not scan `.sh` at all. Observed by
  AC7.

## 3. Non-goals (OUT)

- The ask rung's predicate — which asks are mandated, which are filed, which are disposed and which
  are covered — is unit 16's. This unit builds the rung's position and its input parameter, and
  nothing that decides what goes into it.
- Making `--status` and `--resume` read the same next as `--plan`. This is a RULED non-goal and §8
  F4 records the ruling rather than leaving it a boundary sentence. Two next-pickers exist at HEAD
  and this unit replaces one: `verb_plan`'s accumulation, and `verb_status`'s own
  `nonterminal_units ... | head -1` over the RENDERED units region
  (`tools/unattended/unattended.sh:2910`), which `--resume` inherits by calling that verb (`:3080`).
  The second keeps its own shape, a bare id carrying none of the ladder's five shape strings, so
  this unit changes neither verb's output. Unit 16 S8, AC17 and AC18 once asserted that those two
  verbs print the same `next:` as `--plan`, and no unit of this build builds that join; that parity
  clause is STRUCK at HEAD, logged in that spec's §9 at `:653-658`, and the question is routed to
  the open backlog row `TOOL-aBoundedVerdict-23`, which already carries the render-order half of
  it. What stays open after this unit is one question with one home, rather than a claim with no
  mechanism.
- Reordering within a rung. The live-unit rung keeps region order and the MISSING rung keeps
  whatever order `missing_units` prints (`tools/unattended/unattended.sh:2007-2024`), which today
  is the STRING order its two `sort -u` inputs and `comm -23` impose — the order that puts `-10`
  before `-2`. `TOOL-dDerivedDocket-16` §4 is the unit that re-sorts MISSING ids by numeric
  sequence, at a later order; this unit neither depends on that nor blocks it, because the rung
  takes whichever id that function prints first and states no opinion about which one that is.
  The rank of an ask, including the hold edges between asks, is unit 16's.
- The `--plan --asks` output mode, its ASK rows and the three-field `--paths` shape are unit 16's.
- Changing any of the three shape literals. They are pinned by S4 precisely so this unit is
  invisible to every existing consumer of the plan output.
- The companion guide and Skill prose that describe the plan verb are unit 20's.

### Edges

- **consumes-from** external — `verb_plan`'s two loops and the `next:` block they feed at
  `tools/unattended/unattended.sh:2231-2280`, and `missing_units` at `:2007-2024`, all of which
  exist at HEAD. This unit re-points them and builds neither.
- **hands-off** `TOOL-dDerivedDocket-16` — the rung the undecided-ask shape occupies and the input
  that fills it, so that unit adds a predicate to a declared ladder rather than a branch to an
  accumulation, and its `next:` contract for `--plan` has a rung position it can point at. Both
  edits this unit once owed that spec are landed at HEAD and neither is re-made here. That spec's
  AC18 now carries both arms in its own words: a first run over its fixture printing the MISSING
  `next:` shape while a unit shape remains, and a second run over the same fixture with both MISSING
  units retired, printing the UNDECIDED `next:` shape naming the earlier-listed mandated ask — the
  ordering this unit's ladder declares, which had no failing case in the consuming spec before. And
  the `--status` and `--resume` parity that §3 rules a non-goal is STRUCK from that spec's S8, AC17
  and AC18, its own revision log routing the question to the backlog row `TOOL-aBoundedVerdict-23`.
  AC9 asserts the first of the two at this unit's commit.

## 4. Design

### The ladder today, and why it cannot be reasoned about

The line is built by three assignments, each guarded by whether something already wrote it:

```
THIN|FORKED) [ -n "$next" ] || next="$id ($state)" ;;
READY)       [ -n "$next" ] || next="$id (READY - build it)" ;;
...
[ -n "$next" ] || next="$miss (MISSING - spec it first)"
```

`tools/unattended/unattended.sh:2253-2254` and `:2262`, printed at `:2274-2280`. The precedence is
real and correct, and it is stated nowhere: it is whichever loop runs first. A fourth shape is
therefore added by writing a fourth guarded assignment and arguing in prose about where it goes,
which is what produced a design sentence and a fixture that cannot both hold.

### The ladder after

| # | Rung | Fires when | Shape |
|---|---|---|---|
| 1 | live unit | a graded unit's state is THIN, FORKED or READY | `<id> (<state>)`, or `<id> (READY - build it)` |
| 2 | missing unit | a roster id has no tracked spec | `<id> (MISSING - spec it first)` |
| 3 | undecided ask | an ask has no covering unit and no disposition | unit 16's undecided shape |
| 4 | nothing graded | no tracked spec graded as a unit | `none - no tracked spec grades as a unit (see the NOT A UNIT rows above)` |
| 5 | terminal | every tracked spec is terminal | `none - every tracked spec is terminal` |

`derive_next_shape` walks that table in order and returns the first rung whose input is non-empty.
Rung 3's input is the empty string on every call until unit 16 supplies it, so the printed line is
byte-identical to today's for every tree that exists now — which is what makes this unit's own
arms a control on the refactor rather than a claim about the ask feature.

Rung 4 sits below rung 2 deliberately and that is today's behaviour, not a change: the MISSING loop
assigns the line whether or not anything graded, so a roster id with no spec outranks the
nothing-graded wording. Leg check 30 reads the conjunction of a NOT A UNIT row and rung 5's wording
(`tools/unattended/check-unattended.sh:3284`), so rungs 4 and 5 stay distinct strings and rung 4
stays reachable.

### Why the rung the promoted finding names is pinned and not built

The finding is that one spec's design sentence puts the undecided shape after every unit shape while
its own fixture — two MISSING units present — DEMANDED the undecided shape from the same run. Both
halves could not hold. This unit rules for the design sentence, because that sentence is the one the
other consumers of the plan output were written against and because the opposite rule makes a run
report an ask as next while a planned unit has no spec at all, which is the wrong instruction for
whoever reads the line. The fixture was the half that moved, and it has moved already: unit 16's
AC18 carries the two-arm replacement wording at HEAD
(`memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-16.md:480-502`, logged at
`:640-644`). So S6 is not an edit this unit makes but a property it keeps, and AC9 grades it: the
obligation that outlives the fold is that a later re-fold of AC18 cannot silently re-open the rung
order this unit exists to pin.

Pinning the position here rather than in the consuming spec is the point of the unit: a position in
a declared table is gradeable by a source-level arm, and a sentence in a design section is not.

### Data model

`derive_next_shape` takes four inputs and holds no state: the first live unit id with its state, the
first MISSING roster id, the first undecided ask id, and whether anything graded. Every one of them
is derived by the caller from data it already has, so the selector runs once per `--plan` and
performs no read of its own.

### Inventory

| Identifier | Cell | Verb, and why |
|---|---|---|
| `derive_next_shape` | `sh.function` | `derive`: the shape is computed from the caller's four values so it never has to be authored; `python tools/lexicon/lexicon.py --suggest derive_next_shape --as sh.function` answered OK on 2026-09-20 |
| the rung table block | driver source | `.lexicon.conf` declares no shell constant cell, so no naming arm grades its name |

### Files touched (estimate)

`tools/unattended/unattended.sh` · `tools/unattended/unattended.test.sh` · `.memory-tree.conf` for
`ARMS_FLOORS`. No protocol copy, no guide, no Skill and no dossier (S8). This unit makes no
cross-edit at all: the consuming spec's criterion text is already landed at HEAD, and AC9 asserts
it rather than writing it.

### Rollout

Order 15, shared with units 15 and 48, and shared deliberately rather than for want of a number.
Orders 1 to 38 are all occupied, so no free integer sits between unit 15's step and unit 16's, and
unit 16 consumes the rung position this unit pins, so this unit cannot sit later than that step. The
co-tenancy itself is graded by nothing, because this unit declares no edge to unit 15 or unit 48.
What check 12's edge arm does grade is the pair this unit shares with unit 16, and both ends hold: a
hands-off reds only on a target EARLIER than this unit
(`tools/memory-tree/check-memory-hygiene.sh:1798`) and unit 16 sits later, while unit 16's
reciprocal consumes-from reds only on a target LATER than that unit (`:1796`) and this one sits
earlier. Dispatch is strictly sequential including within a shared `order` value
(`tools/workflows/unattended-build.js:70`), and the harness sorts by step and then by id as a string
(`:314`, with the tiebreak at `:318`), which runs unit 15 first, unit 48 second and this unit third,
before unit 16. Disjointness is not proven for the group and is not claimed, and the DRIVER does not
supply the sequence either: `--dispatch`'s own order gate blocks only on a sibling at a STRICTLY
earlier order (`tools/unattended/unattended.sh:5010`), under a rule that reads a shared value as a
parallel group which does not block (`:4983`). What holds the sequence is the harness's roster order
and nothing else. This unit reads nothing the other two write, so a renumber may move it to any step
at or before unit 16's.

The refactor is live from this commit and is invisible: rung 3 is inert, the literals are unchanged,
and the only reader that can tell the difference is a source-level arm.

### Alternatives rejected

- **Leaving the accumulation and adding a fourth guarded assignment.** That is what produced the
  contradiction: the precedence stays unstated, the new rung's position is an artefact of where the
  line was typed, and no arm can see it move.
- **Deciding the clash inside the consuming spec's own criterion.** The sentence and the fixture
  would still be the only two statements of the rule, with nothing between them that a gate reads,
  and the next shape added would reopen the same argument.
- **Ruling the other way, so an undecided ask outranks a MISSING unit.** It makes the plan tell a
  resuming agent to dispose an ask while a planned unit has no spec, and it contradicts the design
  section that three other specs of this build were written against.
- **Giving the ladder its own module or moving it to the kit library.** `verb_plan` is the only
  caller and the library is the home of what two readers share; a second file for one function is
  cost without a consumer.

## 5. Production-readiness checklist

- security — none. No input is trusted, no path is written and no command is run.
- perf / scale — one function call per `--plan` replacing three guarded assignments; no new read and
  no new process, which matters because leg check 30 already pays for a `--plan` per candidate build.
- error / empty / loading states — every rung has an empty input as its normal case, and the fall
  through to rungs 4 and 5 is the ladder's only terminal answer.
- observability — the printed line is unchanged, so nothing new is emitted; what becomes observable
  is the ORDER, read by a source-level arm rather than inferred from output.
- risks — a refactor of a line agents read to pick up work. It is bounded by S4's byte-identical
  literals and by AC1's end-to-end control, and rung 3 stays inert so this unit cannot change any
  verdict on any tree that exists today.
- testing — one arm per rung, one arm per adjacent-rung boundary, a source-level arm on the declared
  order, a read of unit 16's AC18 at this unit's commit (AC9), and the existing terminal-wording arm
  kept green.
- migration — none. No file format, conf key or record field changes.
- user docs — none owed. The output is byte-identical, so no guide or Skill sentence goes stale;
  the plan verb's prose carriers are unit 20's.

## 6. Acceptance criteria

- **AC1** — When `bash tools/unattended/unattended.sh --plan` runs over a scratch fixture holding
  one READY unit, its output is byte-identical to the same run at this unit's parent commit, and a
  source-level arm finds no guarded next assignment left in `verb_plan` and exactly one call to
  `derive_next_shape`.
  Red when: the refactor changes a printed byte, or an accumulation survives beside the selector so
  two writers can set the line and the declared order is not the one that decides.
- **AC2** — When `--plan` runs over a scratch fixture whose roster names `EXMP-tRun-2` with no
  tracked spec while every tracked spec of the build is terminal, it prints
  `next: EXMP-tRun-2 (MISSING - spec it first)`; when the same fixture's roster is emptied of that
  id, the same run prints `next: none - every tracked spec is terminal`.
  Red when: the terminal wording is printed while a unit shape remains, which is the boundary the
  promoting record found stated in prose and observed by nothing.
- **AC3** — When `--plan` runs over a scratch fixture holding both a READY unit and a roster id with
  no tracked spec, it prints the READY shape naming the unit and not the MISSING shape.
  Red when: the MISSING rung outranks the live-unit rung, so a build with work ready to do reports a
  missing spec as next.
- **AC4** — When `--plan` runs over a scratch fixture whose only spec carries a status header that
  does not parse, it prints a NOT A UNIT row and
  `next: none - no tracked spec grades as a unit (see the NOT A UNIT rows above)`, never the
  terminal wording.
  Red when: the two terminal rungs collapse into one string, so a build nothing graded is reported
  finished and leg check 30's conjunction has nothing to catch.
- **AC5** — When a source-level arm reads the declared rung block out of
  `tools/unattended/unattended.sh`, it finds exactly five rungs in the declared order with the
  undecided-ask rung third, after both unit rungs and before both terminal rungs.
  Red when: a rung is added or moved without the arm moving, so the position this unit exists to pin
  is decided again by whoever types the next assignment. The arm is observed RED by moving the ask
  rung above the MISSING rung before it is allowed to pass.
- **AC6** — When the three existing shape literals are compared between this unit's commit and its
  parent with `git cat-file -p`, each is byte-identical, and the string the existing
  terminal-wording assertion (`tools/unattended/unattended.test.sh:1802`) looks for is still
  present verbatim in the driver, so that arm has something to hit when the suite next runs. The
  comparison is over source at both commits, so this criterion owes no suite run of its own — the
  runtime half is AC2's second arm.
  Red when: a literal is reflowed or re-punctuated, so leg check 30's predicate and every consumer
  matching on the wording stop matching while the ladder reports itself correct.
- **AC7** — When this unit's commit is compared with its parent, `git cat-file -s` at the parent
  equals `wc -c` at the commit for `memory/map/features/unattended.md`,
  `memory/guides/UNATTENDED-PROTOCOL.md` and `tools/unattended/PROTOCOL.template.md`, and the line
  count of each protocol copy, read with `git cat-file -p` piped to `wc -l` at both commits,
  matches.
  Red when: this unit spends the unattended dossier's headroom, which was 93 B when this spec was
  written, or touches a protocol copy this build has priced for other units.
  figure: the 93 B of dossier headroom is PINNED, measured 2026-09-20 at `fb07ca25` as 20387 B
  against the `DOSSIER_CAP_BYTES` of `tools/memory-tree/check-memory-hygiene.sh:90`; that line
  declares the dossier's line half as 0, so it is off, while the guides' line half at `:84` is read
  here.
- **AC8** — When the driver suite runs, every branch this unit adds has an arm, the suite's
  executed-assertion floor holds, and the `tools/unattended/unattended.sh` pair of `ARMS_FLOORS` in
  `.memory-tree.conf` names the new count.
  Red when: a rung lands with no arm, so a ladder whose whole value is that every rung has a failing
  case ships with a rung that has none.
  permission: the suite run and the `harness arms (fail branches armed or pinned)` leg over the real
  tree are runs this pass may not make, so both are deferred to the run the main loop makes at
  VERIFYING after the last unit. In the pass each new arm is observed RED by hand against a scratch
  fixture with its fix unstaged, which is this criterion's direct check.
- **AC9** — When `memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-16.md` is
  read at this unit's commit with `git show`, that spec's AC18 asserts `next:` reads the MISSING
  shape on its first run, a second arm over the same fixture with both MISSING units retired
  asserts the flip to the UNDECIDED shape, and that spec's §9 carries the revision entry naming
  AC18 and this unit. The comparison is over tracked text at one commit, so this criterion owes no
  suite run and no leg.
  Red when: unit 16's AC18 names ONE shape only, so a later re-fold of the consuming spec silently
  re-opens the rung order S3 pins and the ordering this unit declares has no failing case in the
  spec that consumes it; or that spec's §9 carries no entry naming AC18, so the two halves can drift
  with nothing recording that they were ever joined.

## 7. Gates

`unattended kit gate` · `harness arms (fail branches armed or pinned)` · `shell hygiene (a loop fed by a command substitution)` · `memory hygiene` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: `tools/unattended/unattended.test.sh` · moving the ask rung above the MISSING rung in the
declared block, and separately emptying the roster of the fixture that grades AC2 · the driver
suite's executed-assertion floor, and `ARMS_FLOORS` for `tools/unattended/unattended.sh`

## 8. Open questions

- **F1 — which of the two contradicting statements yields.** The consuming spec's design sentence
  prints the undecided shape only when no unit shape remains; its fixture holds two MISSING units
  and demands the undecided shape from the same run. RESOLVED (agent, 2026-09-20, delegated): the
  design sentence holds and the fixture moves. It is the statement the other consumers of the plan
  output were written against, and the opposite rule reports an ask as next while a planned unit has
  no spec at all, which is the wrong instruction for whoever reads the line.
- **F2 — whether this unit builds the ask rung's predicate or only its position.** Options: build a
  dark predicate here; pin the position and leave the predicate to the consuming unit; or leave both.
  RESOLVED (agent, 2026-09-20, delegated): pin the position, leave the predicate. A predicate built
  here would need the mandate, the filing home and the disposition rows, none of which exist at this
  order, so it would be a layer that stays inert while its own suite reads green — the failure this
  build files elsewhere. The position is the half that is gradeable now.
- **F3 — where the ladder lives.** Options: `tools/unattended/unattended.sh` beside `plan_row`, or
  `tools/unattended/lib-unattended.sh`. RESOLVED (agent, 2026-09-20, delegated): the driver, because
  `verb_plan` is the only caller and the library is the home of what two readers share. Should the
  status verb later take the same ladder, moving it is a rename and a source line.
- **F4 — whether this unit widens to own the `--status` and `--resume` join.** Options: widen S1 so
  `verb_status` calls `derive_next_shape` in place of its own pick; leave the join to the consuming
  unit; or rule it out of this unit and route it to the open backlog row. RESOLVED (agent,
  2026-09-20, delegated): rule it out and route it. What F3 prices at a rename and a source line is
  the LADDER's move; the join is the CALLER's four inputs, which is a different cost. `verb_plan`
  reads every tracked spec of the build to have them (`tools/unattended/unattended.sh:2148` and
  `:2156`), while `verb_status` reads the run-state file and the rendered region and nothing else,
  so calling the ladder from it gives the cheap read-only verb the plan verb's whole scan and its
  refusals. It would also change a printed line, since that verb prints a bare id where the ladder
  prints a shape, which is the one property S4 and AC1 exist to hold. The join is a unit of its own,
  and the open backlog row `TOOL-aBoundedVerdict-23` is where the question already lives.

## 9. Revision log

- rev-1 · 2026-09-20 · initial draft. Promoted from the G3 round-2 spec audit's H1 (raw id 1) at the
  review's bounded exit. Section 8 F1 rules which half of the contradiction yields, the design
  section turns the prose precedence into a declared table with a rung per shape, section 6 gives
  every rung that exists at this order a failing case, and S6 hands the consuming spec the
  replacement criterion text as a cross-edit rather than editing it in place.
- rev-1 · 2026-09-20 · §3 §4 §8 · close-out of the same rev, folding the two p1 verifier problems
  that name this spec. The Rollout states why order 15 is shared rather than chosen and which edge
  the shared step is actually graded against. §8 F4 rules the `--status` and `--resume` join out of
  this unit and prices what widening would cost, §3's non-goal names both next-pickers at HEAD and
  the open backlog row the parity question goes to, and the Edges bullet names the second cross-edit
  unit 16 is owed.
  Extended by the close-out's verifier, same base and rev · §4 · the Rollout no longer says a shared
  `order` is not a parallel instruction. `--dispatch`'s own order gate reads it as exactly that: it
  blocks only on a STRICTLY earlier sibling (`tools/unattended/unattended.sh:5010`) under the rule
  stated at `:4983`, so the sequence is the harness's roster order and not a driver refusal.
- rev-1 · 2026-09-20 · §1 · §2 · §3 · §4 · §5 · §6 · §10 · fold of the G7 round-1 spec audit
  (`memory/builds/dDerivedDocket/reviews/2026-09-20-review-TOOL-dDerivedDocket-48-spec-audit-g7-round1.md`),
  findings H1 (1, 16) and L4 (47), both disposed FOLD by the orchestrator. H1: the cross-edit S6
  handed unit 16 was already discharged, and no criterion of either spec graded it. At HEAD that
  spec's AC18 carries the two-arm replacement wording
  (`memory/builds/dDerivedDocket/spec/2026-09-14-spec-TOOL-dDerivedDocket-16.md:480-502`, logged at
  `:640-644`) and the `--status` / `--resume` parity clause is struck (logged at `:653-658`), so
  §1, S3, S6, the Edges bullet, §3's non-goal and §4 now describe HEAD rather than the moment the
  draft was written, S6 asserts the landed text instead of handing it over, and a new AC9 grades it
  at this unit's commit in the shape unit 51's AC5 uses. The obligation that survives the fold is
  named in S6 and §4: a later re-fold of AC18 must not silently re-open the rung order S3 pins.
  L4: §10's prior art is in that build's round-TWO record and is now cited by path and line. No
  left-shift gate proposed by that report is wired or cited here, because only one of its eleven
  candidates was ever run over the tree and this fold ran none.
  Extended once more on the same pass, same base and rev · §3 Edges · the `hands-off` bullet to
  `TOOL-dDerivedDocket-16` stopped citing that spec's own line numbers. A hand-off payload is read
  against the TARGET's text, and a citation of the target's own lines can never occur there, so the
  two landed edits are now named in that unit's own words: AC18's two runs over one fixture and the
  shape each prints, and the struck `--status` and `--resume` parity with the backlog row its
  revision log routes the question to. Every backticked token left in the bullet occurs in that
  spec. §9's own citations above are untouched — they are a revision log's record of where the text
  landed, not a payload anybody joins.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "the plan verb chooses one next line from ranked
candidates"` returned `plan` in `tools/memory-tree/gen_build_index.py`, `rank_with` in
`tools/memory-recall/bench.py` and `derive_candidates` in `tools/lexicon/scaffold_lexicon.py`, none
of which selects a shape from ordered rungs, and its header line reports that `.sh` is an unscanned
layer, so the map cannot see the driver at all. No existing seam fits: the selection this unit
declares exists today only as three guarded assignments inside `verb_plan`
(`tools/unattended/unattended.sh:2253-2254`, `:2262`), which is the code this unit replaces rather
than a seam it extends. The `unattended` dossier names no second next-picker.

Recall returned `TOOL-dHonouredPark-4`, which closed the earlier disagreement between `--plan` and
`--status` about which unit is next by making `--plan` read the rendered region, and
`TOOL-aBoundedVerdict-23`, still open on the same pair choosing by render order rather than
dependency order. Both are named in section 3 as the boundary this unit does not cross. The
`cBriefedPilot` round-TWO review record,
`memory/builds/cBriefedPilot/reviews/2026-08-16-review-TOOL-cBriefedPilot-1-2.md:309`, supplied the
third prior instance: a phantom `MISSING` row becoming the next line once every earlier spec is
terminal, which is the exact rung boundary AC2 grades. The round-1 record of that build names
MISSING only as a stale master-overview count and carries no phantom at all.

Recall terms used: `verb_plan next MISSING roster missing_units terminal precedence shape plan_row
NOT A UNIT graded undecided`
