---
slug: aDeclaredBound
node: a
opened: 2026-08-18
streams: tooling
roster: TOOL
ids: TOOL-aDeclaredBound-1 TOOL-aDeclaredBound-2 TOOL-aDeclaredBound-3 TOOL-aDeclaredBound-4 TOOL-aDeclaredBound-5 TOOL-aDeclaredBound-6
---

# aDeclaredBound — four hardcoded thresholds become declarations, and one of them gets a guard rail

Node `a` · opened 2026-08-18 · streams tooling.

`TOOL-aLoosenedCeiling` made the read-path budget adjustable and then surveyed what else is not.
The owner picked four from that survey. This build specs them.

| threshold | today | where |
|---|---|---|
| check 7's entry budget | `300`, and `350` for a build README | `check-memory-hygiene.sh` awk, and a third copy inside the failure message |
| `SPEC10_CUTOFF` | `2026-08-04`, settable through TWO channels | a shell default read AFTER the conf source, while its three siblings are assigned before it |
| `_RATCHET_LOOKBACK` | `14` | `drift_report.py` module constant |
| agent-cap's `CAP` / `MAX_VERIFIERS` / `MAX_LENSES` | `5` each | `agent-cap.js` file constants, deliberately not overridable |

## The fourth is not like the other three

The first three are ordinary: a number that should have been a declaration and is not. The fourth
is a number that is a constant **on purpose**, and its own source says why:

> A BARE LITERAL, never an environment read. An env-settable ceiling is the defeatable class this
> guard exists to remove, and it leaves no diff behind when someone raises it.

The owner's ask is that it become adjustable *by the owner*, with agents not touching it absent an
explicit request. Those two halves are not in tension with the recorded decision — the objection is
to the ENVIRONMENT as a channel, not to adjustability. An env read leaves no trace; a committed
declaration leaves a diff, a blame line and a reviewable justification. This build keeps the env
refusal exactly as it is and adds a declaration channel that cannot be used quietly.

**What no in-repo mechanism can do is PREVENT an agent from raising it.** An agent with shell access
can edit any file, including the gate that would catch it. `memory/guides/UNATTENDED-PROTOCOL.md` §9
already says this about checks running under a run's own uid, and this build says it again rather
than implying a guarantee it cannot deliver. What the design buys is: lowering is free, raising is
loud, and an unattributed raise reds the bar.

## Units

| id | mechanism | tier |
|---|---|---|
| `TOOL-aDeclaredBound-1` | check 7's two entry budgets become conf keys | 2 |
| `TOOL-aDeclaredBound-2` | `SPEC10_CUTOFF` joins its three sibling cutoffs in the conf | 2 |
| `TOOL-aDeclaredBound-3` | `_RATCHET_LOOKBACK` moves to drift-audit's PROJECT LAYER, not a conf | 2 |
| `TOOL-aDeclaredBound-4` | agent-cap reads a declaration; lowering is free, raising is attributed | 2 |
| `TOOL-aDeclaredBound-5` | the agent-cap number is single-sourced — prose points, never restates | 2 |

**Why five units for four thresholds.** Unit 5 is not extra scope; it is what makes unit 4 honest.
The number `5` is restated across the live document surface — the charter, the README, the BINDING
review protocol, the byte-gated playbook template, a map dossier and the shipped kickoff skill among
them. The moment the value is adjustable, every one of those becomes a second answer to a question
that now has a declared first answer. This repo already ruled on that shape for the kit version:
*"a version written in prose rots between bumps, and this one rotted twice in a day."* Unit 4 without
unit 5 ships a knob whose documentation is wrong for anyone who turns it.

## What round 2 changed, and the run that found it

Round 2 returned BLOCKED on 28 findings — the last round available under `TOOL-aBoundedVerdict-1`'s
two-per-subject cap. The first unattended run of this build ABORTED at that boundary rather than
building on specs no round had called clean; its record is retired beside this file and the owner
resolved both parked decisions before the second run folded them.

The two blockers were structural, not editorial. Unit 5's ratified predicate could not be satisfied
at its own landing commit, because half of it needs a conf key and a hook read that unit 4 mints
later — resolved by splitting the predicate across the two units. And the gate measurement that had
been reported as "zero false positives at 18 hits" did not contain the pattern that produced it: a
nine-item noun list was load-bearing and undocumented, without which the same pattern matches 54
lines rather than 19, including the very line the spec names as the gate's green control. That
record now carries an appended correction rather than a quiet rewrite.

## What the round-1 spec audit changed

Verdict BLOCKED, 33 findings, two of them blockers, and the record is under `reviews/`. The two
that changed the DESIGN rather than the wording:

- **Unit 5 cannot strip the digit from the review protocol.** `check-protocol-parity.test.sh`
  greps for that exact literal as a deliberate anti-vacuity arm. It is now unit 5's S2 and the
  first thing the build decides, with a recommendation and a stated alternative.
- **Unit 4's ratchet could not fire.** `drift_report.py` skips a file absent at the base ref,
  and the first draft deliberately left `.agent-cap.conf` uncommitted — so the first raise, the
  one the ratchet exists for, would never have been compared. The file is now committed at the
  shipped values.

Three more worth naming: unit 4 was specifying a resolver `agent-cap.js` already contains; its
attribution grammar named no key while all three bounds default to the same number; and unit 5's
carrier inventory was wrong in BOTH directions — one listed file has no cap site at all and four
live carriers were missing. The invented total is gone; the build measures.

## Order

Derived from the specs' own Files-touched lists rather than asserted. The rev-1 claim that units
1, 2 and 3 were independent "three different files, three different kits" was false four ways and
was contradicted two sentences later by the README itself.

| pair | why they are NOT independent |
|---|---|
| 1 and 2 | the same hygiene engine, the same self-test, the same kit-version carriers |
| 3 and 4 | both write `tools/drift-audit/drift_signals.py`, and both need arms in `tools/drift-audit/selftest.py` |
| 3 and 5 | both write `tools/drift-audit/README.md` |
| 1, 2, 3 | two kits, not three |

**The order, named rather than implied.** Unit 1, then unit 2 — unit 2's commit carries the single
`KIT_MEMORY_TREE_VERSION` bump, and unit 1's own commit reds the verdict-epoch leg in the window
between them, which both specs now say in their §7. Then unit 3, whose `drift_signals.py` edit
lands before unit 4's. Then unit 5, then unit 4.

**Unit 5 still lands BEFORE unit 4**, and the audit's blocker against that is resolved by SPLITTING
the predicate rather than by reordering: unit 5 asserts the pointer SHAPE, unit 4 adds the
reads-it half in the commit that makes the hook read the declaration. Reordering would reopen the
window unit 5 exists to close — the declaration holding a value the documents contradict, including
a BINDING protocol an agent is instructed to obey.

<!-- gen:build-index -->
**Build status:** OPEN · 5 unit(s) · node a · opened 2026-08-18 · streams tooling
ids TOOL-aDeclaredBound-1 TOOL-aDeclaredBound-2 TOOL-aDeclaredBound-3 TOOL-aDeclaredBound-4 TOOL-aDeclaredBound-5 TOOL-aDeclaredBound-6

| Unit | Status | Rev | Last change |
|---|---|---|---|
| [TOOL-aDeclaredBound-1 — check 7's entry budget becomes a declaration](spec/2026-08-18-spec-TOOL-aDeclaredBound-1.md) | CLOSED | rev-3 | 2026-08-18 |
| [TOOL-aDeclaredBound-2 — SPEC10_CUTOFF joins its three sibling cutoffs in the conf](spec/2026-08-18-spec-TOOL-aDeclaredBound-2.md) | CLOSED | rev-3 | 2026-08-18 |
| [TOOL-aDeclaredBound-3 — the ratchet lookback becomes a project-layer declaration](spec/2026-08-18-spec-TOOL-aDeclaredBound-3.md) | CLOSED | rev-3 | 2026-08-18 |
| [TOOL-aDeclaredBound-4 — agent-cap reads a declaration: lowering is free, raising is attributed](spec/2026-08-18-spec-TOOL-aDeclaredBound-4.md) | OPEN | rev-4 | 2026-08-18 |
| [TOOL-aDeclaredBound-5 — the agent-cap number is single-sourced before it becomes adjustable](spec/2026-08-18-spec-TOOL-aDeclaredBound-5.md) | CLOSED | rev-5 | 2026-08-18 |

Records live under `spec/`, `build/` and `reviews/`.

| Record | Kind | Serves |
|---|---|---|
| [2026-08-18-build-TOOL-aDeclaredBound-5-gate-measurement.md](build/2026-08-18-build-TOOL-aDeclaredBound-5-gate-measurement.md) | research | TOOL-aDeclaredBound-5 |
| [2026-08-18-review-TOOL-aDeclaredBound-1-2.md](reviews/2026-08-18-review-TOOL-aDeclaredBound-1-2.md) | spec-audit | TOOL-aDeclaredBound-1 TOOL-aDeclaredBound-2 TOOL-aDeclaredBound-3 TOOL-aDeclaredBound-4 TOOL-aDeclaredBound-5 |
| [2026-08-18-review-TOOL-aDeclaredBound-1-5-cumulative-round2.md](reviews/2026-08-18-review-TOOL-aDeclaredBound-1-5-cumulative-round2.md) | diff-review | TOOL-aDeclaredBound-1 TOOL-aDeclaredBound-2 TOOL-aDeclaredBound-3 TOOL-aDeclaredBound-4 TOOL-aDeclaredBound-5 |
| [2026-08-18-review-TOOL-aDeclaredBound-1-5-cumulative.md](reviews/2026-08-18-review-TOOL-aDeclaredBound-1-5-cumulative.md) | diff-review | TOOL-aDeclaredBound-1 TOOL-aDeclaredBound-2 TOOL-aDeclaredBound-3 TOOL-aDeclaredBound-4 TOOL-aDeclaredBound-5 |
| [2026-08-18-review-TOOL-aDeclaredBound-1.md](reviews/2026-08-18-review-TOOL-aDeclaredBound-1.md) | spec-audit | TOOL-aDeclaredBound-1 TOOL-aDeclaredBound-2 TOOL-aDeclaredBound-3 TOOL-aDeclaredBound-4 TOOL-aDeclaredBound-5 |
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

<!-- gen:build-docs -->

- **`spec/`**
  - [2026-08-18-spec-TOOL-aDeclaredBound-1.md](spec/2026-08-18-spec-TOOL-aDeclaredBound-1.md)
  - [2026-08-18-spec-TOOL-aDeclaredBound-2.md](spec/2026-08-18-spec-TOOL-aDeclaredBound-2.md)
  - [2026-08-18-spec-TOOL-aDeclaredBound-3.md](spec/2026-08-18-spec-TOOL-aDeclaredBound-3.md)
  - [2026-08-18-spec-TOOL-aDeclaredBound-4.md](spec/2026-08-18-spec-TOOL-aDeclaredBound-4.md)
  - [2026-08-18-spec-TOOL-aDeclaredBound-5.md](spec/2026-08-18-spec-TOOL-aDeclaredBound-5.md)
- **`build/`**
  - [2026-08-18-build-TOOL-aDeclaredBound-5-gate-measurement.md](build/2026-08-18-build-TOOL-aDeclaredBound-5-gate-measurement.md)
- **`reviews/`**
  - [2026-08-18-review-TOOL-aDeclaredBound-1-2.md](reviews/2026-08-18-review-TOOL-aDeclaredBound-1-2.md)
  - [2026-08-18-review-TOOL-aDeclaredBound-1-5-cumulative-round2.md](reviews/2026-08-18-review-TOOL-aDeclaredBound-1-5-cumulative-round2.md)
  - [2026-08-18-review-TOOL-aDeclaredBound-1-5-cumulative.md](reviews/2026-08-18-review-TOOL-aDeclaredBound-1-5-cumulative.md)
  - [2026-08-18-review-TOOL-aDeclaredBound-1.md](reviews/2026-08-18-review-TOOL-aDeclaredBound-1.md)
<!-- /gen:build-docs -->
