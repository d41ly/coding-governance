# TOOL-dDerivedDocket-49 — one declared ladder decides which next: shape the plan prints

**Status:** CLOSED · rev-2 · 2026-09-21 · node d · Tier-2 · base fb07ca25 · streams tooling · order 15

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-21-build-TOOL-dDerivedDocket-49-1-acceptance-ledger.md](../build/2026-09-21-build-TOOL-dDerivedDocket-49-1-acceptance-ledger.md) | journal | — |
| [2026-09-20-review-TOOL-dDerivedDocket-48-spec-audit-g7-round1.md](../reviews/2026-09-20-review-TOOL-dDerivedDocket-48-spec-audit-g7-round1.md) | spec-audit | TOOL-dDerivedDocket-48 TOOL-dDerivedDocket-50 TOOL-dDerivedDocket-51 TOOL-dDerivedDocket-52 TOOL-dDerivedDocket-53 TOOL-dDerivedDocket-54 |

<!-- /gen:spec-records -->

## 1. Goal

`verb_plan` picks its `next:` line by first-wins accumulation across two loops
(`tools/unattended/unattended.sh:2773-2774` and `:2782`, read at `:2794-2800`, at this unit's
PARENT), so the precedence
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
  (`tools/unattended/unattended.test.sh:1816`) still hits. Observed by AC6.
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
  each observed RED with its fix unstaged, and whichever floor the added arms actually move moves in
  the same commit. AMENDED at rev-2: the draft named the `tools/unattended/unattended.sh` pair of
  `ARMS_FLOORS` in `.memory-tree.conf`, and that gate counts `fail <n> "` call sites, of which this
  unit adds none — the ladder has no refusal in it. What the added arms do move is the suite's own
  executed-assertion floor, so `FLOOR_ASSERTIONS` and `FLOOR_SHARD_2` carry the raise and the
  meta-gate's pair stays where it is, unchanged rather than unexamined. Observed by AC8.
- **S8** This unit's delta on every capped carrier is ZERO. It writes no conf key and no guide,
  Skill or dossier prose, and no claim key moves because the codebase map does not scan `.sh` at
  all. The dossier's own headroom is read off AC7's `figure:` line and is NOT restated here: the
  draft carried 20387 B of a 20480 B cap in this bullet as well, and a figure stated in two places
  is the one that goes stale in the copy nobody re-measures — which is exactly what happened to both
  between the base and this pass. Observed by AC7.

## 3. Non-goals (OUT)

- The ask rung's predicate — which asks are mandated, which are filed, which are disposed and which
  are covered — is unit 16's. This unit builds the rung's position and its input parameter, and
  nothing that decides what goes into it.
- Making `--status` and `--resume` read the same next as `--plan`. This is a RULED non-goal and §8
  F4 records the ruling rather than leaving it a boundary sentence. Two next-pickers exist at HEAD
  and this unit replaces one: `verb_plan`'s accumulation, and `verb_status`'s own
  `nonterminal_units ... | head -1` over the RENDERED units region
  (`tools/unattended/unattended.sh:3846`), which `--resume` inherits by calling that verb (`:4197`).
  The second keeps its own shape, a bare id carrying none of the ladder's five shape strings, so
  this unit changes neither verb's output. Unit 16 S8, AC17 and AC18 once asserted that those two
  verbs print the same `next:` as `--plan`, and no unit of this build builds that join; that parity
  clause is STRUCK at HEAD, logged in that spec's §9 at `:653-658`, and the question is routed to
  the open backlog row `TOOL-aBoundedVerdict-23`, which already carries the render-order half of
  it. What stays open after this unit is one question with one home, rather than a claim with no
  mechanism.
- Reordering within a rung. The live-unit rung keeps region order and the MISSING rung keeps
  whatever order `missing_units` prints (`tools/unattended/unattended.sh:2527-2545`), which today
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
  `tools/unattended/unattended.sh:2751-2800` at this unit's PARENT, and `missing_units` at
  `:2527-2545`, which this unit does not move. Both existed at the base and at the parent; this
  unit re-points the first and builds neither.
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

`tools/unattended/unattended.sh:2773-2774` and `:2782` at this unit's PARENT, printed at
`:2794-2800`. The precedence is
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

The table is `NEXT_RUNGS`, five `rung ` lines at column 0 between a lone opening quote and a lone
closing one, and `derive_next_shape` walks it in order and returns the first rung whose input is
non-empty. Rungs 1 and 3 declare a bare `<id>` and nothing more: the words inside those two shapes
belong to whoever supplies them, the state word being `verb_plan`'s and the undecided shape being
unit 16's, so what the table owns for those two is their POSITION. Rungs 2, 4 and 5 carry their
whole tail, which is where the three existing literals now live, byte for byte, and the `next: `
prefix is printed once at the single call site.
Rung 3's input is the empty string on every call until unit 16 supplies it, so the printed line is
byte-identical to today's for every tree that exists now — which is what makes this unit's own
arms a control on the refactor rather than a claim about the ask feature.

Rung 4 sits below rung 2 deliberately and that is today's behaviour, not a change: the MISSING loop
assigns the line whether or not anything graded, so a roster id with no spec outranks the
nothing-graded wording. Leg check 30 reads the conjunction of a NOT A UNIT row and rung 5's wording
(`tools/unattended/check-unattended.sh:3572`), so rungs 4 and 5 stay distinct strings and rung 4
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
| `NEXT_RUNGS` | driver source | `.lexicon.conf` declares no shell constant cell, so no naming arm grades its name; the spelling follows the driver's own `DIRECTIVES_CORE` and `HOLD_CODES_CORE` constants |

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
(`tools/memory-tree/check-memory-hygiene.sh:1926`) and unit 16 sits later, while unit 16's
reciprocal consumes-from reds only on a target LATER than that unit (`:1924`) and this one sits
earlier. Dispatch is strictly sequential including within a shared `order` value
(`tools/workflows/unattended-build.js:70`), and the harness sorts by step and then by id as a string
(`:314`, with the tiebreak at `:318`), which runs unit 15 first, unit 48 second and this unit third,
before unit 16. Disjointness is not proven for the group and is not claimed, and the DRIVER does not
supply the sequence either: `--dispatch`'s own order gate blocks only on a sibling at a STRICTLY
earlier order (`tools/unattended/unattended.sh:6373`), under a rule that reads a shared value as a
parallel group which does not block (`:6346`). What holds the sequence is the harness's roster order
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
  parent with `git cat-file -p`, each is byte-identical, and the terminal WORDING the existing
  assertion (`tools/unattended/unattended.test.sh:1816`) matches on is still present verbatim in the
  driver, as a whole line of the rung table, so that arm has something to hit when the suite next
  runs. The comparison is over source at both commits, so this criterion owes no suite run of its
  own — the runtime half is AC2's second arm.
  Red when: a literal is reflowed or re-punctuated, so leg check 30's predicate and every consumer
  matching on the wording stop matching while the ladder reports itself correct.
  AMENDED at rev-2, second clause only. It read "the string the ... assertion LOOKS FOR", and that
  string is `next: none - every tracked spec is terminal` — the printed line, prefix included, which
  was source text only because one of the three `echo`s carried both halves. S1 moves the prefix to
  the ONE print site and gives each rung the tail it owns, which IS the refactor, so nothing short of
  keeping three print sites preserves the prefixed string. What that arm actually reads is the
  driver's OUTPUT, unchanged and observed by AC2's second arm; what this criterion grades is the
  wording, verbatim, as a line of its own.
- **AC7** — When this unit's commit is compared with its parent, `git cat-file -s` at the parent
  equals `wc -c` at the commit for `memory/map/features/unattended.md`,
  `memory/guides/UNATTENDED-PROTOCOL.md` and `tools/unattended/PROTOCOL.template.md`, and the line
  count of each protocol copy, read with `git cat-file -p` piped to `wc -l` at both commits,
  matches.
  Red when: this unit spends the unattended dossier's headroom, whatever the `figure:` line below
  currently measures it at, or touches a protocol copy this build has priced for other units. The
  draft spelled the number here too and the `figure:` line's re-measurement left it standing at
  93 B; the number lives in one place now.
  figure: AMENDED at rev-2 and RE-MEASURED rather than re-cited. The pin read 93 B, measured
  2026-09-20 at `fb07ca25` as 20387 B against the `DOSSIER_CAP_BYTES` of
  `tools/memory-tree/check-memory-hygiene.sh:90`. At this unit's parent the dossier is 20467 B, so
  the headroom is 13 B — spent by units that landed between the base and this pass, the same fall
  `TOOL-dDerivedDocket-48` recorded. It moves no verdict here, because this unit opens no dossier at
  all, and it would have moved one for any unit that wrote a byte into it. That line declares the
  dossier's line half as 0, so it is off, while the guides' line half at `:84` is read here.
- **AC8** — When the driver suite runs, every branch this unit adds has an arm and the suite's
  executed-assertion floor holds, raised by the arms this unit adds; and when the `fail <n> "` call
  sites of `tools/unattended/unattended.sh` are counted at this commit and at its parent, the two
  counts are equal, so the `ARMS_FLOORS` pair in `.memory-tree.conf` is unchanged BECAUSE nothing it
  counts moved.
  Red when: a rung lands with no arm, so a ladder whose whole value is that every rung has a failing
  case ships with a rung that has none; or a floor is left where the arms found it, so removing one
  of them later costs nothing.
  AMENDED at rev-2. The draft required the `ARMS_FLOORS` pair to name a NEW count, which this unit
  cannot honestly do: that meta-gate counts refusal branches, the ladder adds none, and a pair moved
  to satisfy a criterion would be a number rather than a floor. The count is asserted equal instead,
  which is the same question asked in the direction this unit can answer, and the floor that does
  move is named.
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
suite's executed-assertion floor, raised by the arms this unit adds. AMENDED at rev-2: `ARMS_FLOORS`
was named here too and does not move, for the reason AC8 now states.

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
  reads every tracked spec of the build to have them (`tools/unattended/unattended.sh:2756` and
  `:2764`), while `verb_status` reads the run-state file and the rendered region and nothing else,
  so calling the ladder from it gives the cheap read-only verb the plan verb's whole scan and its
  refusals. It would also change a printed line, since that verb prints a bare id where the ladder
  prints a shape, which is the one property S4 and AC1 exist to hold. The join is a unit of its own,
  and the open backlog row `TOOL-aBoundedVerdict-23` is where the question already lives.

## 9. Revision log

- rev-2 · 2026-09-21 · §1 · §2 · §3 · §4 · §6 · §8 · §10 · the build pass, written BEFORE the code as the brief
  requires. Three kinds of change and no fourth.

  CITATIONS. Every `tools/unattended/unattended.sh` line citation in the draft was taken before the
  regrounding merge and every one had moved: the accumulation the unit retires sits at `:2773-2774`
  and `:2782` at this unit's PARENT, printed at `:2794-2800`, and the citations that name it now say
  PARENT, because after this commit that code is gone and a bare number would point at the
  replacement. The ones naming code this unit does not move name THIS commit: `missing_units` at
  `:2527-2545`, `verb_status`'s own pick at `:3846` with `--resume` inheriting it at `:4197`,
  `verb_plan`'s two spec reads at `:2756` and `:2764`, and the dispatch order gate at `:6373` under
  the rule at `:6346`. Three citations into files this unit does not touch had moved too and are
  re-pinned: leg check 30 at `tools/unattended/check-unattended.sh:3572`, check 12's two edge arms at
  `tools/memory-tree/check-memory-hygiene.sh:1926` and `:1924`, and the terminal-wording assertion at
  `tools/unattended/unattended.test.sh:1816`. Every CLAIM each citation carries was re-read at the
  line it now names and stands; none of them changed a verdict, and `tools/workflows/unattended-build.js`
  and the `TOOL-dDerivedDocket-16` and `cBriefedPilot` citations were re-checked and had not moved.

  AC6, second clause only. The clause asked that the string the existing terminal-wording assertion
  LOOKS FOR stay present verbatim in the driver, and that string is the whole printed line, `next: `
  included. It was source text only because one of the three `echo` branches carried the prefix and
  the tail together, and collapsing those three branches into one call is the refactor S1 names. The
  criterion now grades the terminal WORDING, verbatim and as a line of its own in the rung table,
  which is what leg check 30 and that arm both actually match on; the prefixed line is still what the
  verb PRINTS, and AC2's second arm observes it.

  AC7's pinned figure, re-measured rather than re-cited. 93 B of dossier headroom at the base is
  13 B at this parent, the same fall `TOOL-dDerivedDocket-48` recorded at its own pass. It moves no
  verdict here: this unit opens no dossier, and the three carriers are byte-equal and line-equal at
  both commits.

  §4 also names the table `NEXT_RUNGS` and says what rungs 1 and 3 declare, because the draft's Shape
  column read as though the table owned the state word and the undecided shape, and it owns neither.
  What it owns for those two rungs is their position, which is the whole point of the unit.

  AC8's `ARMS_FLOORS` clause IS amended, together with S7 and §7's new-arm line, which is the half
  the first cut of this entry left standing. That gate counts `fail <n> "` call sites, measured at
  256 in `tools/unattended/unattended.sh` at this commit and 256 at its parent, and this unit adds
  no refusal at all, so the pair cannot name a new count without being moved to satisfy a criterion
  rather than to record a measurement. The criterion asserts the two counts EQUAL instead. The
  suite's own executed-assertion floors DO move, by the 26 assertions the new arms add, all of them
  in region two.

  Extended on the same pass, same base and rev · S7 · S8 · §7 · AC7 · AC8 · the bug-class
  checklist's fold, run over this unit's own commit. Two of its classes bit this diff and both are
  closed here rather than reported. `amendment-leaves-its-other-half-standing`, twice: AC7's
  `figure:` line was re-measured to 13 B while its Red-when and S8 both went on spelling the base's
  93 B, and AC8 was recorded as amended in the ledger while its text and S7's and §7's were not
  touched at all. The headroom figure now lives only on the `figure:` line, and AC8, S7 and §7 say
  the same thing about `ARMS_FLOORS` in one voice. `two-answers-to-one-question`: the AC6 arms
  retype two driver literals in the suite, which is deliberate and is now claimed in the arm's own
  comment — sourcing them from the driver, which is the fix the sibling `RB_TAIL_` pins took at
  `TOOL-dDerivedDocket-48`, would make this particular pair compare a value against itself.

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
  blocks only on a STRICTLY earlier sibling (`tools/unattended/unattended.sh:6373`) under the rule
  stated at `:6346`, so the sequence is the harness's roster order and not a driver refusal.
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
(`tools/unattended/unattended.sh:2773-2774`, `:2782` at this unit's PARENT), which is the code
this unit replaces rather
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
