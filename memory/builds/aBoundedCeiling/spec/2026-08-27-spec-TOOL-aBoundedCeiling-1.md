# TOOL-aBoundedCeiling-1 — a leg declares how long it may take, and the runner holds it to it

**Status:** OPEN · rev-4 · 2026-08-27 · node a · Tier-2 · base 1d83cc94 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-27-build-TOOL-aBoundedCeiling-1-live-hang-observed.md](../build/2026-08-27-build-TOOL-aBoundedCeiling-1-live-hang-observed.md) | research | TOOL-aBoundedCeiling-5 TOOL-aBoundedCeiling-6 |
| [2026-08-27-prompt-TOOL-aBoundedCeiling-1.md](../prompts/2026-08-27-prompt-TOOL-aBoundedCeiling-1.md) | research | TOOL-aBoundedCeiling-5 TOOL-aBoundedCeiling-6 |
| [2026-08-27-review-TOOL-aBoundedCeiling-1-diff-review-round1.md](../reviews/2026-08-27-review-TOOL-aBoundedCeiling-1-diff-review-round1.md) | diff-review | TOOL-aBoundedCeiling-5 TOOL-aBoundedCeiling-6 |
| [2026-08-27-review-TOOL-aBoundedCeiling-1-round1.md](../reviews/2026-08-27-review-TOOL-aBoundedCeiling-1-round1.md) | spec-audit | TOOL-aBoundedCeiling-5 TOOL-aBoundedCeiling-6 |
| [2026-08-27-review-TOOL-aBoundedCeiling-1-round2.md](../reviews/2026-08-27-review-TOOL-aBoundedCeiling-1-round2.md) | spec-audit | TOOL-aBoundedCeiling-5 TOOL-aBoundedCeiling-6 |

<!-- /gen:spec-records -->

## 1. Goal

Give every leg in `tools/gate-legs.json` a declared wall-clock ceiling, and make
`tools/run-gates/run-gates.sh` enforce it: a leg that outlives its ceiling is killed and reported
RED naming itself and the number it broke. This closes the open half of `TOOL-aBoundedVerdict-10`
(a hung leg wedging the whole bar with no deadline) and `TOOL-aCollapsedScan-5` (no leg declares a
ceiling and the manifest has no field for one), and it implements charter §7's already-written rule
at the place legs actually run.

## 2. Scope (IN)

- **S1** — a `ceiling` key on every leg row in `tools/gate-legs.json`, a positive integer of
  seconds, one literal number per leg.
- **S2** — the manifest reader in `run-gates.sh` carries `ceiling` as a seventh field, appended
  after `subject` so every existing field keeps its position.
- **S3** — `runleg()` wraps each leg in `timeout -k 5s <that leg's ceiling>`, captured through a
  file exactly as the existing bound is, and only when the leg declares one.
- **S4** — `report_one()` attributes exit 124 and exit 137 to the leg's OWN ceiling, independently
  of `PROF_TIMEOUT`.
- **S5** — a liveness line when `timeout` will not run on this host: the ceilings are announced
  INERT on stderr, and every leg still runs unbounded rather than being skipped.
- **S6** — the runner REPORTS its unbounded legs and never reds on one. The profile line names how
  many of this run's legs carry no ceiling, so a manifest that is silently losing its bounds is
  visible on every run without any tree being refused for a field it cannot supply.
- **S9** — the DECLARATION requirement lives in `tools/run-gates/run-gates.gov.test.sh`, which
  asserts that every row of gov's own manifest carries a positive integer `ceiling`. A new leg
  arriving without one reds gov's bar, which is the forcing function charter §7 asks for. Numbered
  S9 and not S8 because rev-2 RETIRED an S8, and a retired label reused is two scope items answering
  to one name in the same document.
- **S7** — the shipped canary's pinned leg-key set gains `ceiling`, at BOTH of its two sites.

## 3. Non-goals (OUT)

- **N1** — no profile row's `timeout=` value moves. `PROF_TIMEOUT` stays `0` on every row, for the
  reason §4 gives, and no new profile knob is added.
- **N2** — no leg is made faster. Reducing a leg's spawn count is what a ceiling forces later, and
  is not this unit.
- **N3** — no unattended `*.test.sh` suite returns to `tools/gate-legs.json`. That removal is an
  owner ruling of 2026-08-23 and this build's standing constraint.
- **N4** — nothing here reaches an adopter's manifest. Carrying `ceiling` through the deployer is
  `TOOL-aBoundedCeiling-5` and cannot be done from inside the runner.
- **N5** — the ceiling is not graded against `<git-dir>/gate-ledger.tsv` at run time. That file is
  per-clone and per-machine, so a verdict read from it would be a fact about the node.
- **N6** — no `BUDGET_*` line in `tools/unattended/run-unattended-gates.sh` is deleted, and that file
  is not touched at all. rev-1 scoped exactly that deletion and the spec audit refuted it: `run_one`
  resolves `bkey="BUDGET_$(printf '%s' "$label" | tr ' -' '__')"` and then treats an EMPTY value as a
  failure — *"A MISSING BUDGET IS ITSELF A FAILURE"* — so deleting a line makes `--checks` print
  `OVER BUDGET  <label> declares no ceiling` and exit 1 forever. A leg may hold a ceiling in the
  manifest AND a `BUDGET_*` beside its suite; the two bound different things and neither is a copy of
  the other.

## 4. Design

### Data model

One new key per leg row, alongside the six the canary already pins:

```json
{ "name": "memory hygiene", "argv": ["bash", "tools/memory-tree/check-memory-hygiene.sh"],
  "chunk": "records", "subject": "repo", "ceiling": 1270 }
```

`ceiling` is a positive integer of seconds. It is a LITERAL, not a formula and not a lookup: a
number typed beside the leg it bounds is a number a reader can argue with, and a script that
re-derived it from the ledger would be a second answer to a question the manifest already answers.

**How the shipped numbers were picked, so a later reader can question them.** Each is
`max(60, 3 × the leg's own seconds in `<git-dir>/gate-ledger.tsv` on node `a`)`, rounded up. The
factor is not caution for its own sake: `memory/gotchas/process-creation-is-the-suite-cost.md`
measured the same workload at 10.7 s and at 26 s across one session on an antivirus-fronted node,
and states the consequence plainly — a ceiling that reds on ambient load is a ceiling that gets
ignored, which is worse than not having one. The 60 s floor is what gives the twenty-two legs that
finish in under five seconds a bound worth having; without it they would inherit a bound so wide
that nothing but a true hang could reach it.

Tightening the factor later is a one-line edit per leg with a reason beside it, which is the same
discipline `tools/unattended/run-unattended-gates.sh` already applies to its own eight ceilings.

**The formula applies to all 85 rows uniformly, and three of those legs ALSO carry a `BUDGET_*`
declaration in `run-unattended-gates.sh`. Those declarations are not touched, and they are not
duplicates of anything shipped here.** A `BUDGET_*` is a COST bound: it asks whether a suite still
costs roughly what somebody accepted. A manifest `ceiling` is a HANG bound: it asks whether a leg has
stopped returning at all. One is measured after the fact and deliberately does not kill; the other
kills. A leg carrying both carries two numbers because it is being asked two questions.

`unattended kit gate` is where the distinction earns its keep, and it is already on the record.
`TOOL-aCollapsedScan-3` is a RATIFIED decision noting that `BUDGET_kit_gate=120` was set against a
28 s reading and that `--checks` later read 305 s: *"The ceiling worked and nothing on the bar reads
it."* `TOOL-aCollapsedScan-4` is OPEN against that same breach. **This unit takes NEITHER of that
row's candidates** — it neither fixes the leg's cost nor re-declares the 120 s. It ships a 1600 s
HANG bound beside the untouched 120 s COST bound, and `-4` stays open on its own terms until someone
rules on the cost half. Saying that plainly is the point: a unit that claimed to close it would leave
a future session reading a closed row that is not.

The uniform formula happens to produce 1600 s for that leg (533 × 3) and 490 s for
`playbook validity gate` (161.8 × 3), so no row here is a hand-placed exception. There are no
exceptions.

### Why `PROF_TIMEOUT` must stay zero

The obvious move — set `timeout=` on a profile row — is refused, and the reason is not taste.
`run-gates.sh:407` derives the turnstile's holder TTL from it: `TS_TTL=$(( PROF_TIMEOUT * 3 ))`
when it is non-zero, and `${GATE_TURNSTILE_TTL:-1800}` otherwise. `TS_MAXWAIT` is `TS_TTL * 4`.
`tools/run-gates/run-gates.turnstile.test.sh` copies the SHIPPED profile table into every fixture
and sets no `GATE_PROFILES`, so a non-zero row silently outranks the `GATE_TURNSTILE_TTL` values
its arms drive the mechanism with. Arm 7c must then burn `12 × PROF_TIMEOUT` seconds against a
refresher that never lets go. There is no safe non-zero value: large hangs that suite, and small
reds the fixture legs, which sleep between one and twelve seconds.

So the per-leg ceiling is a SECOND, independent bound, and the two must never wrap one leg at once —
nested deadlines produce exit 124 with no way to tell which fired. `runleg()` uses the leg's ceiling
when it has one and `PROF_TIMEOUT` otherwise, never both.

### Why it is runner-side and never argv

`input_key()` at `run-gates.sh:790` keys the reuse cache on the leg's argv. A ceiling passed as an
argv element would change every leg's key and invalidate the whole reuse cache on the commit that
lands it. The value is read from the manifest into a shell array beside `guards` and `subjects` and
never reaches the child's command line.

### Rollout

The declaration check is scoped to a manifest that ALREADY carries at least one ceiling. That is
not a soft-launch; it is the rule the run-gates canary's own header states for exactly this case:

> until a deployer unit teaches govkit to carry it, gov-only: an adopting tree's emitted manifest
> cannot contain one. An arm that reds on its ABSENCE is an arm that reds in every adopting tree on
> arrival, which is the same defect one level up from the one it guards.

`tools/gate-legs.json` is not shipped. An adopter's manifest is machine-emitted by `govkit apply`
from the selected kits' `[[gate_leg]]` rows, and that emitter writes no `ceiling` today. A check
that redded on absence would therefore red every adopter on upgrade day over a field they have no
way to supply. Presence-scoping is what makes the check meaningful in gov — where all eighty-five
rows gain a ceiling in one commit, so a later row arriving without one reds — and inert everywhere
it would only be cruel.

**Why the RUNNER does not enforce the declaration at all, which is a change from two earlier
revisions of this spec and is the simpler answer they were both circling.** An adopter's manifest is
a MERGE, not a rewrite: `govkit apply` reads the target's existing rows, replaces or appends only the
rows a kit owns, and writes the whole list back — a protection that exists precisely so a leg the
target wrote survives. So the first apply after `TOOL-aBoundedCeiling-5` produces a MIXED manifest,
kit rows carrying a ceiling and project rows not.

rev-3 answered that by scoping the runner's check to rows a kit receipt claims. That is wrong for a
reason worth stating: **the runner cannot know.** A receipt is `govkit`'s artifact, and teaching the
merge-bar runner to read the deployer's bookkeeping to decide whether to refuse a leg couples two
kits that are deliberately independent, in the direction that makes the bar depend on the deployer.

So the runner REPORTS and never refuses, and the requirement moves to the one place that may hold a
claim about gov's corpus: `tools/run-gates/run-gates.gov.test.sh`. That file exists for exactly this,
is already the `run-gates gov canary` leg, and is withheld from the kit payload as `project-owned`.
Its own header states the rule this unit is obeying — *"the shipped canary may assert only what is
true in ANY tree"* — and names `memory/gotchas/pin-copied-from-another-corpus.md` as the class that
follows from breaking it.

The result is stronger in gov and harmless everywhere else. In gov all 85 rows carry a ceiling, and
the 86th arriving without one reds the bar. In an adopter nothing is refused, a mixed manifest is
legal, and the unbounded count is printed on every run so the state is visible rather than silent.

### Inventory

| site | change |
|---|---|
| `tools/gate-legs.json` | a `ceiling` on each of the 85 rows |
| `run-gates.sh` manifest reader (~:712) | emit a seventh `\x1e`-separated field |
| `run-gates.sh` row loader (~:721) | a `ceilings` array parallel to `names` |
| `run-gates.sh` `runleg()` (~:890) | wrap in the leg's own bound when it declares one |
| `run-gates.sh` `report_one()` (~:966) | attribute 124 and 137 to the leg's own ceiling |
| `run-gates.sh` liveness (~:349) | say so when `timeout` will not run |
| `run-gates.test.sh` (:96 and :125) | `ceiling` joins the pinned `KNOWN` set, both copies |
| `run-gates.gov.test.sh` | S9's arm: every row of GOV's manifest declares a ceiling |

### Alternatives rejected

**A profile-wide `timeout=`.** One number must cover a one-second leg and a 1320-second one. To
let the longest live it must sit near 4000 s, which converts an unbounded hang into a
sixty-six-minute one and catches nothing else. It also breaks the turnstile suite, as above.

**Grading elapsed time against the ledger after the fact**, which is `TOOL-aCollapsedScan-5`'s own
suggested route and is how `run-unattended-gates.sh` works. Rejected here because it cannot bound a
HANG: a leg that never returns is never measured, and the bar wedges exactly as it does today. The
two mechanisms are genuinely different and must not be unified — one kills at the bound, the other
deliberately does not, because a killed suite prints no verdict and the kill then reads as silence.

## 5. Production-readiness checklist

- **security** — no new input is trusted. The ceiling is read from a tracked manifest the bar
  already parses, and reaches `timeout` as a validated integer, never the child's command line.
- **perf/scale** — one integer per leg, read in the existing parse. No measurable cost.
- **observability** — a breach names the leg and its ceiling on stdout, in the durable summary, and
  in the per-leg log the runner already persists.
- **risks** — a ceiling set too tight reds a healthy leg on a slow node. Priced by the 3× factor and
  the 60 s floor, both argued in §4. The rollback is one integer.
- **testing + left-shift gates** — AC1 to AC4 and AC6 live in `run-gates.test.sh`, which IS the
  `run-gates canary` leg and therefore may name no leg of this corpus. AC8 lives in
  `run-gates.gov.test.sh`, which is the suite that MAY name one. AC5 is a whole-bar run and belongs
  to no suite. Every failing case is observed before landing, per charter §7.
- **migration / rollback** — deleting every `ceiling` key restores today's behaviour exactly; the
  reader `.get`-defaults the field and the wrapper is skipped when it is absent.
- **user docs** — `tools/run-gates/README.md` gains the field and the derivation rule. The TTL
  sentence at its lines 96-99 is re-read against §4 and corrected if it now misleads.

## 6. Acceptance criteria

- **AC1** — When a leg declares `"ceiling": 2` and sleeps 30, the bar reports it `GATE FAIL` naming
  the leg and `2`, and the RUN takes seconds rather than 30 — measured as ELAPSED time in
  `run-gates.test.sh`, never as a message, because the message was always the correct half of
  `memory/gotchas/bounded-through-a-pipe-is-unbounded.md`.
- **AC2** — When that same leg breaches, the verdict is `FAIL` and never `skip`, `held` or `reuse`,
  keeping the governing invariant in `tools/run-gates/gate-profiles.txt` that no knob may turn a leg
  into a pass or a skip.
- **AC3** — When a manifest carries rows with and without a `ceiling`, `bash
  tools/run-gates/run-gates.sh` runs every leg and its profile line NAMES the unbounded count. No
  tree is refused for a missing ceiling, asserted in `run-gates.test.sh` over a mixed fixture,
  because that shipped suite runs in an adopter's tree where a mixed manifest is the normal state.
- **AC8** — When a row is removed from `tools/gate-legs.json`'s ceiling set, `bash
  tools/run-gates/run-gates.gov.test.sh` FAILS naming that leg — the staged break observed RED
  before this unit lands, per charter §7.
- **AC4** — When `timeout` cannot run on the host, `run-gates.sh` prints that the ceilings are INERT
  and every leg still executes, with the run's verdict unchanged against a control.
- **AC5** — When `ceiling` is added to `tools/gate-legs.json`, `bash tools/run-gates/run-gates.sh`
  under `GATE_SELFTESTS=1` is GREEN, including the `run-gates canary` leg whose pinned `KNOWN` set
  the field would otherwise break.
- **AC6** — When a leg's argv is unchanged, `input_key` returns the same value whether or not the
  leg declares a `ceiling` — asserted in `run-gates.test.sh` with the TREE HELD CONSTANT. The claim
  is only that the ceiling never enters the key, NOT that the reuse cache survives a manifest edit:
  it does not, because an unguarded leg's key is `FPRINT_START`, which digests the tree and moves on
  any edit to `tools/gate-legs.json`. 48 of the 85 legs lose their key on the commit that lands this
  unit, once, by design.

## 7. Gates

`bash tools/run-gates/run-gates.sh` with `GATE_SELFTESTS=1`, which is the only run that exercises
`run-gates canary`, `run-gates gov canary`, `run-gates turnstile` and `run-gates evidence` — all four
are held on a default bar and all four read what this unit changes. No new gate LEG is added: the
ceilings are enforced by the runner every leg already goes through, and S8's assertion joins a suite
that is already a leg.

## 8. Open questions

- **F1 — the headroom factor.** 3× measured with a 60 s floor, against a tighter 1.5× that would
  make an ordinary regression fail rather than only a hang. RESOLVED (agent, 2026-08-27, delegated):
  3× and 60 s. `memory/gotchas/process-creation-is-the-suite-cost.md` measured a 2.4× spread on one
  node in one session and states that a ceiling redding on ambient load gets ignored; 1.5× is inside
  that spread. Tightening later is a per-leg edit with a reason, which is the shape this repo already
  uses for every other pin it owns.
- **F2 — where the no-ceiling refusal fires.** In the manifest parser, which kills the whole run on
  one bad row, against after the parse, which reds one leg. RESOLVED (agent, 2026-08-27, delegated):
  after the parse. A missing ceiling is a declaration defect, not an unparseable manifest, and the
  parser's existing hard-subscript behaviour already produces `cannot parse` and zero legs — reusing
  that path would make a one-row omission indistinguishable from a corrupt file.
- **F3 — what happens to the three `BUDGET_*` lines whose suites are also manifest legs.** RESOLVED
  (agent, 2026-08-27, delegated): NOTHING happens to them, and rev-1's answer here was wrong in the
  dangerous direction. It resolved to delete them, which `run_one`'s empty-value refusal turns into a
  permanent RED on `--checks`. They stay. See N6.

## 9. Revision log
- rev-1 · 2026-08-27 · initial draft, grounded on five read-only probes of `run-gates.sh`, the
  turnstile suite, the canary's pinned key set and `govkit`'s leg emitter.
- rev-2 · 2026-08-27 · folded the round-1 spec audit. Dropped S8 and AC7, which were INVERTED — the
  deletion they scoped causes the failure AC7 asserted it prevents; added N6 saying so. Excluded the
  three already-declared ceilings from the 3x formula and took `TOOL-aCollapsedScan-4`'s candidate
  (2) explicitly. Cited `TOOL-aCollapsedScan-3` and `-4` in §10. Re-routed §5's acceptance homes,
  which contradicted §7. Narrowed AC6, whose reuse-cache clause was false for 48 of 85 legs. Dropped
  a misplaced Inventory condition.
- rev-3 · 2026-08-27 · folded the round-2 spec audit. Scoped S6 to the rows a receipt claims, after
  R2-1 showed specs 1 and 5 together would red an adopter's mixed manifest. Replaced the exclusion
  list in §4 with the uniform formula, which already produces the two argued numbers, and corrected
  the claim that this unit takes `TOOL-aCollapsedScan-4`'s candidate (2) — it takes neither.
- rev-4 · 2026-08-27 · DESIGN CHANGE made before the code, per M2. The runner no longer enforces the
  ceiling declaration at all: it reports its unbounded count and refuses nothing, and the requirement
  moves to `run-gates.gov.test.sh`, the gov-only suite that already exists for corpus-specific claims
  and is withheld from the kit payload. rev-2 required a ceiling on every row, which round 2's R2-1
  showed would red an adopter's mixed manifest; rev-3 scoped that to rows a kit receipt claims, which
  is worse — it would make the merge-bar runner read the deployer's bookkeeping to decide a refusal.
  Reporting plus a gov-only arm is simpler than either and strictly stronger in gov. S6 restated, S9
  and AC8 added, AC3 rewritten, `run-gates gov canary` added to §7.

## 10. Reuse audit

**The seam exists and this unit wires through it rather than building one.** `run-gates.sh:890`
already implements a per-leg wall-clock bound — `timeout -k 5s "$PROF_TIMEOUT"`, captured through a
file rather than a pipe, with exits 124 and 137 attributed at `:966-970` and an inertness probe at
`:349-351`. What is missing is a per-leg VALUE to give it. This unit supplies that and changes no
part of the enforcement's shape.

The second seam is the manifest reader at `run-gates.sh:712`, whose sixth field `subject` was
appended after `chunk` for the stated reason that a field inserted earlier would be misparsed by any
reader that had not moved in the same commit. `ceiling` is appended by the same rule.

`python tools/codebase-map/reuse_lookup.py "a wall-clock ceiling per gate leg, enforced by the
runner, that turns a hang into a red verdict"` returned `KITDIR`/`ROOTN`/`KITREL`/`LEGS_FILE`
[run-gates] as an affordance seam and the `gate-legs` inventory keys, which is the manifest this
unit extends.

Recall terms used, because M7 re-runs the query: `leg ceiling timeout deadline hang wedge selftest
guard bar budget verdict spawn profile runner`. It returned `TOOL-aCollapsedScan-5`, which proposes
this exact field and whose closure this unit is, and `TOOL-aBoundedVerdict-10`, whose per-leg
deadline half it closes.

**Two governing records the first draft missed, and the audit found.** `TOOL-aCollapsedScan-3` is a
RATIFIED decision in `memory/DECISIONS.md` about the very ceiling this unit nearly overwrote, and
`TOOL-aCollapsedScan-4` is an OPEN backlog row against the same breach. §4 above takes `-4`'s
candidate (2) by name. The recall query returned neither, because it was phrased about deadlines and
hangs while both records are phrased about a BUDGET and a leg cost — a reminder that a probe answers
the question asked and the miss is the querier's, not the corpus's.

**Where a hit was STALE.** `TOOL-aCollapsedScan-5` suggests grading the ceiling against
`<git-dir>/gate-ledger.tsv` because "the measurement half already exists". Verified against source
and rejected in §4: that route cannot bound a hang, and the ledger is per-clone and per-machine.
The ledger is used to DERIVE the shipped numbers once, at authoring time, and is not read at run time.
