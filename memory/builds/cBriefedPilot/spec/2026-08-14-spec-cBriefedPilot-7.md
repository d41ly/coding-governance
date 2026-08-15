# TOOL-cBriefedPilot-7 — `build-complete`, and the roster every unattended build now owes

**Status:** DEFERRED · rev-3 · 2026-08-16 · node c · Tier-2 · base 37c05e1b · streams tooling · ratified 2026-08-15

## 1. Goal

Give the owner's "merge and push only when the entire build is fully done" a checker. `--close`
blocks while the build's authored roster names a unit that is unspecced or unfinished, and every
unattended build's README carries that roster inside the marker pair so the check has a population
to select from.

## 2. Scope (IN)

- **S1** — `build-complete:machine` appended to `DOD_CORE` in `tools/unattended/unattended.sh`,
  making the kit-owned core seven items.
- **S2** — a `dod_met` case arm for it, in the SAME commit as S1. Without the arm the item falls to
  the `*)` default, which is `grep -qE "^$item: (yes|true)"` — a machine item satisfiable by the run
  writing one line into the file it owns.
- **S3** — the arm is a five-term conjunction, all terms required:
  1. the build README carries exactly one well-formed roster pair;
  2. `roster_ids` names at least one id;
  3. `missing_units` is empty;
  4. `unit_rows` over the run-state file's copied generated region is non-empty;
  5. `nonterminal_units` over that same region is empty.
- **S4** — `CORE_FLOOR` in `.unattended.conf` moves `10:6` to `10:7`. Unit 8 moves it `10:7` to
  `10:8`; the two halves of the 6-to-8 move are one unit each, so a partial landing is a floor that
  matches its own core set.
- **S5** — the authoring obligation, per P3: an unattended build's README carries its authored roster
  inside `<!-- roster:units -->` and its closing marker. It is enforced by term 1 blocking `--close`,
  and stated in the protocol by unit 18.
- **S6** — `memory/builds/cBriefedPilot/README.md` gains the pair around its Units table, in
  whichever shape §8 resolves to: under the recommended Option A the `State` column moves outside the
  markers, under Option B the table is enclosed as authored. The pair is ABSENT at this build's BASE,
  so `check_authorization` takes its opt-in-by-presence branch and adding it mid-run is safe here —
  which is exactly the property §8 says the next build will not have.
- **S7** — arms in `unattended.test.sh` for each term, plus the override path.

## 3. Non-goals (OUT)

- **The roster reader.** `roster_ids`, `missing_units`, `unit_rows` and `nonterminal_units` are unit
  6's, built there and consumed here unchanged. This unit adds no helper.
- **A new `fail` branch.** The item reports through `verb_close`'s existing `fail 13`, whose text
  already prints the exact `--override` spelling. `ARMS_FLOORS` is untouched by this unit, which is
  worth saying because every other unit in this build moves it.
- **A per-term diagnostic.** Five conjuncts collapse into one unmet item, and the diagnostic is one
  verb away: `--plan` names the missing units by id. That is why unit 6 is sequenced first.
- **Blocking an abort.** `verb_abort` evaluates the two agent-attested items and no machine item, by
  design and in writing — an aborted run landed nothing, so a completeness item asserts an obligation
  it does not have. Adding a machine item cannot change that, and this unit does not touch the loop.
- **Retrofitting the roster into the other build READMEs.** S5 binds an unattended build. A build that
  never runs under a mandate is unaffected, and no gate leg reads the roster outside this item and
  `check_authorization`.

## 4. Design

### Data model

The roster region holds the PLAN — the unit ids and what each one is. The generated region and
`--plan` hold the STATE. That split is not stylistic: `check_authorization` byte-compares the roster
slice at the pinned BASE against the working copy and refuses on any difference, so a byte inside the
pair that legitimately moves during a run makes `authorization-reachable` unmet — and that item is
the one the protocol says has no override. A per-unit status column inside the pair is therefore a
wedge with no exit, and the status it would carry is already derived twice elsewhere.

Term 4 exists because term 5 is vacuously true over an empty selection. `region` returns exit 0 with
empty stdout for a well-formed pair enclosing nothing, so a run-state file whose generated region was
spliced empty would satisfy "no unit row is non-terminal" by having no unit rows. Terms 1 and 2 are
the same guard one level up, against a roster that is absent or names nothing.

Term 3 is the only one that can see the case D8 exists for. The generated region is rendered from the
specs that EXIST, so a planned unit nobody specced produces no row and terms 4 and 5 are blind to it.

### Why the roster is required rather than opt-in

`check_authorization` reads the roster opt-in by presence, which is right for an integrity check: a
build predating the marker pair must still authorize. A COMPLETENESS check cannot borrow that
disposition. Measured on this tree, 1 of 35 tracked build READMEs carries the pair, so an opt-in
`build-complete` would be vacuously true for 34 of them and blind in exactly the case it exists for.
The cost is two lines per build, and the owner accepted it as P3.

### The interaction with the waiver

`land-once-done` is the directive handle that points at M8's landing rule; `build-complete` is the
DoD item that blocks the close. A waiver relaxes the directive and never the item, so a run that
waived `land-once-done` still owes `--override build-complete --reason "<text>"` at close. `fail 13`
prints that spelling already, and unit 9's table carries it forward at the one moment the owner is
present. This is also why the unit depends on unit 1: `--override` is a scalar today, so a run
overriding both this item and unit 8's could never reach `park`.

### Files touched (estimate)

| File | Change |
|---|---|
| `tools/unattended/unattended.sh` | `DOD_CORE` plus one `dod_met` case arm |
| `.unattended.conf` | `CORE_FLOOR` `10:6` to `10:7` |
| `memory/builds/cBriefedPilot/README.md` | the roster marker pair around the Units table |
| `tools/unattended/unattended.test.sh` | six arms |

### Alternatives rejected

- **Grepping the literal `MISSING` out of `--plan`'s stdout.** That stream also carries the driver's
  own refusal prose — `fail 19` in `verb_plan` spells `MISSING` inside a sentence — so the check
  would answer a different question and flip silently on a reword.
- **Reading unit state from the build README's generated region rather than the run-state file's
  copy.** The two are byte-compared by `records-current` and by leg check 8, so reading the second
  source would be a third answer to a question that already has one and a checker.

## 5. Production-readiness checklist

- security — N/A. Every input is a tracked file the run already writes; the honest limit is that this
  is internal consistency over run-written status tokens, not a verdict.
- perf / scale — one `region` per side at close.
- a11y · i18n — N/A.
- error / empty / loading states — the vacuous-selection cases are terms 1, 2 and 4, and each has its
  own arm.
- observability — one unmet item at `--close`, with `--plan` as the diagnostic.
- risks — the item reads spec status tokens the run writes, routed through a region the run
  re-renders. Flipping one header to `CLOSED` per unspecced unit satisfies it end to end. It is worth
  having because it forces an explicit per-unit lie instead of silence, and it is labelled internal
  consistency rather than `machine` wherever it is described.
- testing + left-shift gates — the six arms in S7; the roster reader's own arms are unit 6's.
- migration / rollback — the `CORE_FLOOR` raise and the `DOD_CORE` addition land together or the
  `unattended kit gate` floor no longer matches the set it pins. A build with no roster pair does not
  regress: it simply cannot close a mandated run without an override.
- user docs — protocol §4's table row and §1's roster sentence are unit 18.

## 6. Acceptance criteria

- **AC1** — When a fixture's roster names two ids, both carry specs, and one spec's status header is
  `OPEN`, `--close` blocks and names `build-complete`.
- **AC2** — When every roster id carries a spec and every unit row is `CLOSED` or `WONTDO`, `--close`
  proceeds past the item.
- **AC3** — When the build README carries no roster pair, `--close` blocks on `build-complete`.
- **AC4** — When the roster names an id that no tracked spec carries, `--close` blocks, even though
  every unit row present in the generated region is terminal.
- **AC5** — When the run-state file's generated region is a well-formed pair enclosing nothing,
  `--close` blocks rather than passing on an empty selection.
- **AC6** — When `--override build-complete --reason "<text>"` is supplied, `--close` proceeds and one
  parked `override · item build-complete` line is written.
- **AC7** — With `DOD_CORE` grown and `CORE_FLOOR` left at `10:6`, the `unattended kit gate` is green
  and the floor is slack; with `CORE_FLOOR` at `10:7` and the item removed, it reds. Both observed.

## 7. Gates

`unattended driver selftest` (`tools/unattended/unattended.test.sh`) · `unattended kit gate`
(`tools/unattended/check-unattended.sh`, for the `CORE_FLOOR` pin) · `unattended gate selftest` ·
`memory hygiene (20 checks)` for the edited build README · the full bar at the push boundary.

## 8. Open questions

none — the fork below is RESOLVED (agent, 2026-08-15, delegated): option A — the roster marker pair encloses the PLAN only; the `State` column moves outside it.

  Option C was VETOED under M3 rule 3: it weakens an integrity check that landed for a reproduced
  reason, inside a unit that is not about authorization. Between A and B, A is the only one under
  which both rules — the roster is the scope, and the scope may not move — hold without an author
  remembering anything, and the column it removes is a third spelling of a state already derived twice.

**What may live inside the roster marker pair, given that `check_authorization` byte-compares the
slice across the pinned BASE?** This build's own Units table carries a `State` column that moves as
units land, and `memory/builds/aStandingWrit/README.md` — the one build that ships the pair today —
carries `BUILT` markers inside it. Once a build's roster exists at BASE, any edit inside the pair
makes `authorization-reachable` unmet, and that item has no override.

- **Option A: the pair encloses the plan only.** The `State` column moves outside the markers, or is
  dropped, since `gen:build-index` and `--plan` already report it. Two lines per build, and the
  roster becomes immutable for a run's whole life by construction.
- **Option B: the pair encloses the table as authored, and the rule is that a run may not touch it
  mid-flight.** No README surgery, but the rule is authorial and the failure is a wedge with no exit.
- **Option C: relax `check_authorization` to compare only the id set rather than the slice bytes.**
  Cheapest for authors and the largest change: it weakens an integrity check that landed for a
  reproduced reason, in a unit that is not about authorization.

Recommendation: **A**. It is the only option under which the two rules — the roster is the scope and
the scope may not move — are both true without an author remembering anything, and the column it
removes is the third spelling of a state that is already derived twice. Resolver: owner.

## 9. Revision log

- rev-1 · 2026-08-14 · initial draft, from the design panel recorded at
  `build/2026-08-14-build-cBriefedPilot-1-design-pass.md`. Folds FG-4, FG-6, FG-11, FG-12 and C11.
  Carries the owner's P3 resolution of 2026-08-14. The roster-immutability fork in §8 was found at
  authoring, against `check_authorization`'s source, and is in neither the design pass nor the build
  README.
- rev-2 · 2026-08-14 · S6 made conditional on §8 rather than pre-empting it. As written it named the
  pair "around its own Units table", which is Option B — the shape §8 recommends AGAINST, on the
  measured wedge at `tools/unattended/unattended.sh:503-505`. A builder reading the scope list alone
  would have landed the losing option and left the next unattended run on this repo with no exit. S6
  also now records that this build's own BASE predates the pair, so the wedge does not fire here.

- rev-3 · 2026-08-15 · §8 resolved under the standing mandate for `cBriefedPilot`; the pick and the reasoning are in §8. Header gains the ratified pointer.

## 10. Reuse audit

- **`dod_met` in `tools/unattended/unattended.sh`** — the seam. It is a `case` over the item name and
  already holds six arms; this is a seventh, and the reporting, the override budget and the
  agent-versus-machine labelling all come with it unchanged.
- **`DOD_CORE` and `CORE_FLOOR`** — the declaration and its shrink-only pin. The count is derived by
  the leg from the driver, and by the leg's own self-test through `CORE_FLOOR_DERIVED`, so growing the
  set needs no fixture edit.
- **`roster_ids`, `missing_units`, `unit_rows`, `nonterminal_units`** — unit 6's, consumed here. This
  unit adds the rule; unit 6 owns the reading.
- **`park()` and `verb_close`'s override path** — the record of an override, already written for
  every item. `build-complete` needs nothing new from it beyond unit 1's repeatability.

Probes run at authoring for the cluster. `python tools/codebase-map/reuse_lookup.py "unattended run
definition of done item checked at close"` names no seam for a completeness check; `dod_met` is not
in the symbol index, which is a miss recorded as an answer rather than retried with softer words.
Recall terms used: unattended close DoD override roster README region generated units plan spec
status terminal review base.
