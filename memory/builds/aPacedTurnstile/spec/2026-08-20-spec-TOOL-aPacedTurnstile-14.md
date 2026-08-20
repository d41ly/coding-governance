# TOOL-aPacedTurnstile-14 — the authored roster is read with its refusal intact

**Status:** SPECCED · rev-3 · 2026-08-20 · node a · Tier-2 · base 43a6c13e · streams tooling · ratified 2026-08-20

## 1. Goal

`roster_ids` pipes `region` into `grep`, so `region`'s exit-3 refusal is discarded and a malformed
authored `roster:units` pair over-selects the rest of a build README, harvesting ids out of the
Records table as phantom planned units. Restore that refusal through both of its consumers, guard
the region `verb_plan` actually joins against rather than the one its message names, and give this
build a roster the plan verb can read.

## 2. Scope (IN)

- **S1** — `roster_ids` captures `region` into a variable and returns 3 when it refuses, mirroring
  `unit_rows`, which already has exactly this shape. The `grep -qF` presence test stays: deciding
  presence by `region`'s status is what `TOOL-cBriefedPilot-6` S1 forbade, and it was right, because
  `region` reports absent and malformed through one status. Presence is grep's question;
  well-formedness is `region`'s; today the second question is asked and its answer thrown away.
- **S2** — `missing_units` propagates that status instead of swallowing it in a command
  substitution. Both of its consumers must be able to tell "the plan names nothing" from "the plan
  could not be read".
- **S3** — `verb_plan` refuses by name when the authored pair is malformed, in the shape the kit
  already uses at its generated-pair site: a `fail` carrying a literal sentence, followed by a
  separate detail line that carries the interpolated path. The path never enters the `fail` message,
  because `check-arms.py` reads the literal text up to the first interpolation as a branch's
  signature and an interpolated path there makes the branch permanently unarmable. The guard runs
  where the generated-pair guard already runs — at the head of the verb, before the spec listing and
  before the missing-unit loop. Position is load-bearing: that loop spells
  `for miss in $(missing_units …)`, which discards the status a THIRD time, so S2's propagation buys
  `verb_plan` nothing on its own. This RESTORES a branch rather than inventing one:
  `TOOL-cBriefedPilot-6` S4 built exactly this refusal for the AUTHORED pair and its S7 shipped the
  arms and the `ARMS_FLOORS` raise, and `TOOL-aBoundedVerdict-11` S8 repointed that one branch at the
  generated pair instead of adding a second. So the branch count returns to what S4 already paid for,
  and the floor moves by one again. Codes 1 through 47 are contiguous and in use, so the new one is 48.
- **S4** — the `build-complete` Definition-of-Done item reports the same refusal through `DOD_OUT`
  rather than reporting a harvested Records-table id as a unit the build owes a spec.
- **S5** — `roster_refusal` is the one place that message is spelled, sibling to `units_refusal`.
  Its remedy differs and must say so: the generated region is repaired by a render, and the authored
  pair is repaired by hand, so pointing an operator at a render command here would be a lie.
- **S6** — the misnaming is corrected at every carrier, not at the one that is easiest to find. The
  same error — calling the GENERATED region the thing `--plan` joins against — sits at four places:
  the guard message at `unattended.sh:1092`, the arm asserting that literal at
  `unattended.test.sh:1399`, the verb-list comment at `unattended.sh:1378`, and check 21's header at
  `check-unattended.sh:865`. Both guards survive; only the sentences change. A rev-2 draft scoped
  this to the first two, which is the defect this build's README names as its own recurring one: a
  fix naming more than one carrier lands in one of them.
- **S7** — a test arm for the malformed AUTHORED pair, observed RED against the unfixed driver
  before the fix lands. The arm that exists today builds a second GENERATED pair, so the authored
  path has never been exercised, and its comment claims the coverage the fixture does not supply.
- **S8** — this build's README gets a readable roster: the authored units table moves to sit
  immediately above the generated region and is wrapped in the pair there, and it gains a row for
  THIS unit. The table was authored when the build had seven units and this spec makes eight, so a
  straight relocation would ship a plan that omits the unit which created it — green, because the
  join only refuses ids the roster has and specs lack, and wrong.
- **S9** — three stale map claims across two dossiers are corrected, not one across one:
  `build-readme-surface.md`'s seam line asserting the roster pair is being RETIRED, its Gaps bullet
  claiming this unit is already closed by another, and `unattended.md`'s claim that
  `build-complete` is a conjunction over the AUTHORED roster and a run-state copy — which is wrong
  on both halves, since it reads the generated region and the copy was removed. The one derived
  figure in that Gaps bullet is DELETED rather than decremented, because the population is
  derivable and a corrected count is the next commit's stale count.
- **S10** — the backlog row is closed with a note carrying its residual. The row's trailing
  suggestion to check the rest of the corpus is DECLINED by the first non-goal, not fixed, so the
  closure states that or the residual vanishes silently. Hygiene check 8 grades that a row carries
  one status token and never whether the token is true, so nothing else would catch it — and this
  exact row is the proof: another unit already declared it closed and it is still OPEN today.

## 3. Non-goals (OUT)

- **Wrapping the other forty-five unwrapped build READMEs.** Eight of fifty-four carry the pair. The
  rest are dormant, most are finished, and hand-wrapping is the exact operation that mints the
  malformed pairs S1 exists to catch. A corpus pass is a separate decision with a separate owner turn.
- **Gating the pair's PRESENCE.** That makes an authored region of a mutable file mandatory, which
  is the direction `TOOL-aBoundedVerdict-11` S6 moved the frozen authorization scope away from.
- **Retiring the authored roster.** It is the only carrier of a unit that is planned and has no
  spec, and `TOOL-aBoundedVerdict-11` S8 kept it deliberately after measuring that the generated
  region makes the join a tautology. Reversing a ratified mid-build correction is an owner decision
  and is not this unit's to take.
- **Changing the slot contract** that forces the pair to be the last authored slot. S8 obeys it; it
  does not renegotiate it.
- **Generalising the marker contract to the row selector.** That is `TOOL-aPromptedMandate-14`, and
  it is a wider change than one reader's discarded status.
- **Deciding whether `build-complete`'s missing-units term should exist at all.** That is a LIVE
  parked owner decision, recorded through the park verb in `memory/builds/aBoundedVerdict/RUN.md`
  and restated in that build's README: the authored pair was narrowed to the one question only it
  can answer, and dropping the term outright remains the owner's to prefer. This unit builds on the
  term as it stands and does not resolve its survival. S2 and S4 are scoped to that term, so if the
  owner drops it both revert cleanly and nothing else in this unit depends on them. Naming the park
  here rather than in section 8 keeps that section's first line machine-legal while leaving the
  question visible to the next reader, which is what a park is for.

## 4. Design

### Data model

Two marker pairs live in a build README and they answer different questions.

| Pair | Written by | Question it answers | Read by |
|---|---|---|---|
| `gen:build-units` | the render, `gen_build_index.py --write` | which units EXIST, from the specs on disk | authorization, the presence term, terminality, `unit_rows` |
| `roster:units` | a human, by hand | which units are PLANNED, including ones with no spec | `roster_ids`, and `missing_units` through it |

The split is the whole point. Pointing the planned-unit question at the generated region makes it a
tautology, because that region is rendered FROM the specs the question is asking about. That was
measured mid-build and corrected, and the correction is why an authored reader still exists.

**S8 reverses a ratified supersession, and the reversal is recorded here because the record it
reverses is CLOSED and must not be rewritten.** `TOOL-aBoundedVerdict-11` states in its own section 4
that this row's proposed remedy, wrapping the authored Units table in the marker pair, is
"SUPERSEDED here rather than adopted", on the ground that "wrapping keeps an AUTHORED region on the
authorization path". The same record declares this row closed. Both statements were true when
written and the first is now void: that spec's own S6 moved authorization onto the generated id set,
and its S8 then corrected itself mid-build to KEEP the authored reader rather than remove it. The
consequence is checkable and was checked — `ROSTER_OPEN` has exactly two occurrences in the whole
driver, the constant at `unattended.sh:151` and the reader at `:1008-1009`, both inside
`roster_ids`. No authorization reader touches the roster slice. Wrapping therefore cannot put an
authored region back on the authorization path, because there is no longer a path there to put it
on. The closure claim is void for the same reason: what S8 closed was the `build-complete` half, and
the read-path half this unit builds was never touched.

**The behaviour S3 restores is already a published promise.** `memory/guides/UNATTENDED-PROTOCOL.md`
describes `--plan` as reporting "a roster whose markers are malformed is a named refusal rather than
a complete-looking list". The contract is correct and needs no edit; the CODE drifted from it when
S8 repointed the guard. This unit is a contract restoration, not a contract extension, which is why
no protocol file appears under Files touched.

`gen_build_index.py`'s own `PLAN_OPEN` comment still describes the roster pair as being RETIRED. It
is not, and that sentence is one of the stale carriers S9 corrects.

### Inventory

The defect, and where each piece of it sits.

| Site | State today | What changes |
|---|---|---|
| `roster_ids` | pipes `region` into `grep`, so exit 3 is lost to the pipeline | captures, returns 3 |
| `missing_units` | a command substitution discards the status again | propagates |
| the `verb_plan` guard | checks the GENERATED pair while its message names the authored one | message corrected, authored guard added |
| the `build-complete` term | a phantom id becomes "the build owes a spec" | named refusal through `DOD_OUT` |
| the malformed test arm | its fixture builds a second GENERATED pair | a second arm covers the authored pair |

Reproduced on a scratch fixture at base: a `roster:units` open marker with no close makes `region`
exit 3 while still printing every line to end of file, the pipeline returns 0, and an id belonging
to a review record in the Records table comes back as a roster unit. `verb_plan` then lists it as
MISSING and can name it as `next`, which is the line an unattended agent acts on. The direction of
failure differs by consumer and neither is acceptable: `verb_plan` sends an agent to write a spec
for a review record, and `build-complete` blocks a finished build against a unit that does not exist.

The generated-region reader is already hardened against precisely this, with a structural region
bound plus a link selector, two independent guards, written up in its own comment as protection
against the record-row defect. The authored reader has neither. Its region bound exists and is
discarded, and its selector is a bare id pattern, which is correct for the roster because roster
rows cite ids in backticks rather than as spec links. So the fix is the bound, not the selector.

### Migration

The README move is nine table rows and a heading. The units table currently sits mid-section, with
roughly ninety-five authored lines after it; the slot contract requires the pair to be the last
authored thing before the first generated marker, and every one of the eight wrapped READMEs in the
corpus has zero authored lines in that gap. Wrapping in place therefore reds the slot leg.

Measured at base, with the table excised and re-placed under its own heading immediately above the
generated region: the slot leg passes, the freshness check passes, the hygiene gate passes, and the
plan verb reports the roster as read with an empty difference. The diff is fourteen insertions and
ten deletions in one file. The narrative that surrounds the table today keeps its own subsection and
already tells the reader that live revs are in the generated table rather than in this one, so the
relocation costs a cross-reference, not a rewrite.

### Rollout

S1 through S7 land before S8. That order is not cosmetic: S8 is a hand-authored marker pair, and
hand-authored marker pairs are the population S1 exists to police. Landing the wrap first would put
a new instance of the guarded class into the tree while the guard is still discarded.

### Files touched (estimate)

| Path | Change |
|---|---|
| `tools/unattended/unattended.sh` | `roster_ids`, `missing_units`, `roster_refusal`, the `verb_plan` guard, the `build-complete` term |
| `tools/unattended/unattended.test.sh` | the authored-malformed arm, and the corrected message in the existing arm |
| `tools/unattended/check-unattended.sh` | check 21's header, one of the four misnaming carriers |
| `memory/builds/aPacedTurnstile/README.md` | the table relocation, the pair, and this unit's roster row |
| `memory/map/features/build-readme-surface.md` | the RETIRED seam line and the stale closure bullet |
| `memory/map/features/unattended.md` | the `build-complete` claim, stale on both of its halves |
| `memory/backlog/TOOL.md` | the row, closed with its residual named |
| `.memory-tree.conf` | the `ARMS_FLOORS` row, bumped in the same commit that earns it |

### Alternatives rejected

An id-only roster region placed above the generated block, leaving the narrative table where it is,
was the cheapest edit that satisfied both gates. Rejected: it is a second copy of the unit list in
the same file, which is the two-answers-to-one-question class the bug-class checklist names as
universal for exactly these paths.

Widening the existing guard to cover both pairs with one message was rejected because the two
refusals have different remedies. One is repaired by a render and the other by hand, and a shared
sentence could only name one of them or neither.

## 5. Production-readiness checklist

- security — N/A. No new write path, no untrusted input, no egress. The change narrows what a reader
  accepts.
- perf / scale — N/A. One command substitution replaces one pipeline over a file already read.
- a11y — N/A. No user interface.
- i18n — N/A. Operator-facing diagnostics in this repo's one language, as every sibling refusal is.
- error / empty / loading states — the substance of the unit. Absent, malformed and empty become
  three distinguishable outcomes where two of them are one today.
- observability — the refusal names the file and the repair. The plan verb's roster line already
  distinguishes read from unread and keeps doing so.
- risks — the failure direction changes for `build-complete`: a malformed pair moves from a wrong
  block to a named block. No path becomes more permissive. The relocation is reversible by one
  revert; nothing is generated from the moved table.
- testing + left-shift gates — the authored-malformed arm is the left-shift, and it lands only after
  being observed RED. Adding a branch costs an `ARMS_FLOORS` bump and may renumber
  `unarmed-branches.txt` rows below the insertion point; both are read from the gate, never guessed.
- migration / rollback — one README, one commit, revertible in isolation from the driver change.
- user docs — N/A. No user-facing feature; the affected surface is a kit-internal diagnostic.

## 6. Acceptance criteria

- **AC1** — When a build README carries a `roster:units` open marker with no close, `roster_ids`
  exits `3` and prints no ids, where at base it exits `0` and prints ids drawn from the Records table.
- **AC2** — When that same README is passed to `--plan`, the verb exits non-zero, its output names
  the authored pair and the README path, and it lists no unit at all. The refusal is asserted as a
  refusal: a criterion phrased as "contains no id from outside the region" would pass by finding
  nothing, because a refusing verb prints no ids either way.
- **AC3** — When that same README is judged by the `build-complete` Definition-of-Done item, the
  unmet text is the named roster refusal and not the sentence about a plan naming a unit no tracked
  spec carries.
- **AC4** — When the new arm in `unattended.test.sh` is run against the driver at base `43a6c13e`,
  it FAILS, and that failure is recorded in the build record before the fix lands.
- **AC5** — When `grep -rn "roster join\|roster this verb" tools/unattended/` runs after the change,
  every surviving hit names the region it actually describes, and the count of hits that call the
  generated region a roster join is zero. The criterion is a scoped grep over all four carriers
  rather than an assertion about the arm, because an arm proves one carrier and this finding was
  that a fix reaches one carrier.
- **AC6** — When `bash tools/unattended/unattended.sh --plan aPacedTurnstile` runs after the README
  change, its roster line reports the region as READ rather than fallen back to, and the id count it
  names equals the row count of the generated `gen:build-units` region, with none missing. The count
  is compared against that region and is not written here: this build gained a unit when this very
  spec landed, and a figure typed into an acceptance criterion would already be the old one.
- **AC7** — When `python tools/memory-tree/gen_build_index.py --check-format` runs after the README
  change, it exits `0`, and its status is read from the process rather than through a `tail` pipe.
- **AC8** — When `python tools/memory-tree/check-arms.py` runs after the driver change, it passes
  with the `ARMS_FLOORS` row for `tools/unattended/unattended.sh` bumped in the same commit, and any
  `unarmed-branches.txt` row whose ordinal moved corrected in that commit too.
- **AC9** — When both dossiers are read after the change, `build-readme-surface.md` no longer says
  the roster pair is being RETIRED and no longer claims this unit is closed by another, and
  `unattended.md` no longer describes `build-complete` as reading the authored roster or a
  run-state copy. All three are checked, because the rev-2 draft checked one of the three.
- **AC11** — When `memory/backlog/TOOL.md` is read after the change, the row for this unit carries a
  terminal status and a closure note naming the corpus-wide residual as declined rather than done.
  The row is asserted directly: hygiene check 8 grades that a row has one status token and never
  whether that token is true, so no gate observes this.
- **AC10** — When `GATE_FULL=1 bash tools/run-gates/run-gates.sh` runs, every leg is green.

## 7. Gates

The merge bar, read from `tools/gate-legs.json` and not from any list typed elsewhere. The legs this
unit is expected to move or to keep green, named because they are the ones its diff reaches:

```bash
GATE_FULL=1 bash tools/run-gates/run-gates.sh
```

- the unattended driver selftest, which owns the new arm and the corrected one
- the build README slot contract, which the relocation must leave clean
- the build-index freshness check, which the relocation must not disturb
- the memory-tree hygiene gate, which grades this spec file and the backlog row
- the arms check, whose floor this unit raises

The codebase-map legs are deliberately NOT in that list. A rev-1 draft claimed the dossier edit
moves them; measured at base with the corrected bullet in place, `gen_map.py --check` stays green,
because coverage keys on a dossier's CLAIMS and this edit changes prose. The legs must stay green
like every other; they are not legs this unit moves.

No new gate leg. A new arm inside an existing suite is the cheaper form, and this unit does not need
a leg of its own.

## 8. Open questions

none — every fork below is RESOLVED in place, each naming its resolver and the date. This lead line
is the machine-read one: `plan_state` reads only the FIRST non-blank line of this section, so a
section whose resolutions live in the bullets alone classifies as FORKED. Observed on this very
spec at rev-1, which the plan verb reported FORKED with both forks already resolved.

- **Fork A — how far to take the fix.** The options were: repair the read path only; repair it and
  wrap this README; retire the authored roster; or make the pair mandatory across the corpus.
  RESOLVED (owner, 2026-08-20): repair the read path and wrap this README. Retiring reverses a
  ratified mid-build correction, and mandating taxes a corpus that does not use the feature.
- **Fork B — how to wrap, given the slot contract.** An in-place wrap reds the slot leg, so the
  options were: drop the wrap and record why; relocate the table above the generated region and wrap
  it there; or add an id-only region and leave the narrative table alone. RESOLVED (owner,
  2026-08-20): relocate and wrap. The id-only form was the cheapest and duplicates the unit list,
  which the rejected-alternatives subsection above explains.

## 9. Revision log

- rev-1 · 2026-08-20 · initial draft. Both forks were resolved by the owner during the design pass,
  so the spec is written with them folded rather than carrying them open.
- rev-2 · 2026-08-20 · folded a self-review of the draft, six findings. Section 8 gained the
  machine-read lead line, without which the plan verb classified this spec FORKED with both forks
  resolved — observed, not reasoned. The gates section dropped a false claim that the dossier edit
  moves the codebase-map legs; measured green. AC6 stopped naming a count of a derived population
  and AC2 stopped asserting an absence that a refusing verb satisfies for free. S3 gained the
  guard's position and its code, because the missing-unit loop discards the status a third time. S8
  gained the roster row for this unit, which the relocation would otherwise have omitted.
- rev-3 · 2026-08-20 · folded the M4 spec audit, seven confirmed findings of thirty-five raised at
  0.57 precision, every one re-verified against source before folding. The load-bearing one is that
  S8 REVERSES a ratified supersession: `TOOL-aBoundedVerdict-11` names this exact remedy as
  superseded and declares this row closed, and section 4 now records the reversal and the checkable
  fact that retires the objection. S3 stopped presenting a restored branch as a new one, S6 grew
  from two carriers to the four that actually hold the misnaming, S9 grew from one stale map claim
  to three across two dossiers, S10 appeared because closing a row was in scope with nothing
  observing it, section 3 gained the live parked owner decision the audit found, and AC5 became a
  scoped grep because an arm proves one carrier and the finding was about reaching all of them.

## 10. Reuse audit

A `tools/codebase-map/reuse_lookup.py` pass over the region-read question ranks the memory-tree
python readers first, and none of them is the seam: the subject here is a shell function inside the
driver. The seam that fits is already in the file and is used verbatim.

`region` is the reuse. It reports malformation today and its report is discarded; S1 wires the
existing contract through rather than adding a parser. `unit_rows` is the shape to copy — capture,
return 3, let the caller spell the message — and copying its shape is what makes the two readers
answer their questions the same way.

`units_refusal` is the reuse for S5, and its call site is the reuse for S3: a `fail` with a literal
sentence, then a separate detail line carrying the path. That split exists because of the arms
signature rule, and re-deriving it here would re-derive the bug it was written to avoid.

`unattended.test.sh` already ships the fixture writer S7 needs. `roster()` at `:275-285` appends an
authored pair to a build README and is deliberately pure shell, because a python launcher is
unresolved there and `mkconf` leaves the tree dirty. The authored-malformed arm drives that helper;
writing a second fixture writer beside it would be the two-answers class in the test suite.

No new seam is created. The one new function is a message spelling, which is the pattern the kit
already declares for the sibling region.

The prior art this unit sits on, all of it verified against source rather than taken from prose:
`TOOL-cBriefedPilot-6` S4 and S7 built the authored refusal and its arms, `TOOL-aBoundedVerdict-11`
S8 repointed that branch at the generated pair, and `memory/guides/UNATTENDED-PROTOCOL.md` still
promises the behaviour S8 repointed away. So this unit restores a contract rather than writing one,
and the reuse question it had to answer was not "what seam fits" but "what already existed here".
