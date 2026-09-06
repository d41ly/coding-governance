# TOOL-aQuenchedHarness-6 — the dominant suites rebuilt onto the harness, arm inventory preserved

**Status:** OPEN · rev-1 · 2026-09-06 · node a · Tier-2 · base faaea5f5 · streams tooling · order 6

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Rebuild the self-test suites that hold the cost onto `tools/lib/lib-selftest.sh`, so the on-demand
sweep runs in minutes rather than hours. The population is DERIVED from `<git-dir>/gate-ledger.tsv`
at build time and is not typed here; what is fixed is the RULE for choosing it and the rule for
proving nothing was lost.

## 2. Scope (IN)

- **S1** — select the suites to port by recorded cost: take held legs in descending recorded seconds
  until the selected set holds a DECLARED majority share of the held population's leg-sum. The share
  is declared in `tools/run-gates/selftest-budgets.txt`'s header with its reading; the SET is
  computed, so it moves when the ledger moves and no name is typed into this spec.
- **S2** — for each selected suite, extract its ARM INVENTORY before touching it: the staged break,
  the subject invoked, and the expected verdict, one row per arm, written to
  `memory/builds/aQuenchedHarness/build/` as a tracked artifact.
- **S3** — port the suite onto the harness, preserving every row of that inventory. The port changes
  how an arm is EXECUTED and never what it asserts.
- **S4** — re-extract the inventory after the port and DIFF it against the pre-port artifact. A
  non-empty diff is a defect in the port, not a judgement call. This is the mechanism that makes
  "preserved" checkable rather than claimed.
- **S5** — record, per ported suite, the before and after: seconds, spawn count, and arm count. Three
  numbers, all measured in the same conditions, so a later reader can tell a real improvement from a
  quieter box.
- **S6** — lower each ported suite's row in `tools/run-gates/selftest-budgets.txt` to its new
  reading, in the same commit as the port. A speed-up that leaves the old ceiling standing has bought
  headroom, not a verdict.
- **S7** — every suite NOT ported is NAMED in the build's wrap-up with its recorded cost, so the
  remainder is a stated fact rather than an omission.

## 3. Non-goals (OUT)

- Not porting every suite. The rule in S1 is a majority-share rule, and S7 names the remainder. A
  full port of all held suites is a follow-up a later build may take with this build's measurements
  in hand.
- Not changing any checker under test. Only the suites move.
- Not adding arms. A port that also improves coverage cannot be diffed against its own inventory, and
  the diff in S4 is the whole safety property. New arms are a separate unit.
- Not removing arms, even ones that look redundant. Same reason.

## 4. Design

### The inventory extractor

A small reader that walks a suite and emits one row per arm: the arm's label, the subject argv, and
the expected verdict. It reads the suite's own `arm`-shaped call sites, so it works on the pre-port
suite and the post-port suite alike — which is what makes the diff meaningful. Where a suite's arms
are not extractable by that reader, the suite is reported as UNEXTRACTABLE and is not ported in this
unit: porting a suite whose inventory cannot be compared would be exactly the unfalsifiable claim
this design exists to prevent.

### Ordering

One suite per pass, committed per pass, with the inventory diff in the commit message. A batch port
would make a failed diff ambiguous across suites.

### Inventory

- `tools/lib/selftest-arms.sh` — the inventory extractor, beside the harness it reads.
- `memory/builds/aQuenchedHarness/build/<date>-build-TOOL-aQuenchedHarness-6-arm-inventory-<suite>.md`
  — one tracked artifact per ported suite, holding the before and after inventories and the diff.

### Files touched (estimate)

`tools/lib/selftest-arms.sh` (new) · the selected `*.test.sh` files · `tools/run-gates/
selftest-budgets.txt` · one build record per suite.

### Alternatives rejected

Porting by hand and asserting equivalence in prose was rejected: this repo's own record shows a
derived equivalence claim being wrong by 2.6x and going unnoticed because nobody could falsify it
(`tools/unattended/run-unattended-gates.sh`, the `TOOL-dNarrowedAnchor-1` note). A diffable artifact
is the cheapest thing that makes the claim falsifiable.

## 5. Production-readiness checklist

- security — N/A: no checker changes, no new execution path.
- perf / scale — the unit's whole subject; measured per suite by S5.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — UNEXTRACTABLE is a named state and is reported, never skipped.
- observability — the per-suite before/after artifact is the record.
- risks — the real hazard is a port that silently loses an arm, since a suite with fewer arms is
  faster AND greener. S4's diff is the guard, and it reads the suite rather than the port's own
  claim about itself.
- testing + left-shift gates — each ported suite IS its own test; the extractor gets arms of its own,
  including a suite whose arm it cannot read.
- migration / rollback — each port is one commit and reverts cleanly; the budgets move with it.
- user docs — none owed: the suites are developer surface, and the harness's header covers how to
  write a new one.

## 6. Acceptance criteria

- **AC1** — When a suite is ported, `bash tools/lib/selftest-arms.sh <suite>` produces an inventory
  identical to the one extracted before the port, and the diff is recorded in that suite's build
  artifact.
- **AC2** — When an arm is deliberately deleted from a ported suite, the diff from
  `bash tools/lib/selftest-arms.sh` is non-empty and the port is refused — the guard's own failing case, observed before landing.
- **AC3** — When the ported suites run under `bash tools/run-gates/run-selftests.sh`, each is inside
  its lowered row in `tools/run-gates/selftest-budgets.txt`.
- **AC4** — When the build closes, the selected set satisfies S1's declared majority share, computed
  from `<git-dir>/gate-ledger.tsv` and shown in the wrap-up rather than asserted.
- **AC5** — When a suite's arms cannot be extracted, `tools/lib/selftest-arms.sh` reports
  `UNEXTRACTABLE` naming it, and that suite appears in the unported remainder rather than being
  silently skipped.

## 7. Gates

`bash tools/run-gates/run-gates.sh` · `bash tools/run-gates/run-selftests.sh` for the ported suites ·
`GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` at the Definition of Done · `memory hygiene`,
which grades the per-suite build records this unit writes.

## 8. Open questions

- **F1 — what majority share does S1 declare?** RESOLVED (agent, 2026-09-06, delegated): the share is
  declared during the build from the ledger's own distribution, because the right cut is where the
  distribution has its shoulder and this repo's own measurement shows the shoulder is sharp — a
  handful of suites and a long tail of nothing. Declaring a number here before looking would be a pin
  chosen by preference over a measurement that already exists.
- **F2 — what happens to a suite whose arms are unextractable?** RESOLVED (agent, 2026-09-06,
  delegated): it is NOT ported in this unit and is named in the remainder. Porting it would mean
  hand-asserting equivalence, which §4's rejected alternative already refuses on this repo's own
  evidence.

## 9. Revision log

- rev-1 · 2026-09-06 · initial draft.

## 10. Reuse audit

The seam this unit extends is `tools/lib/lib-selftest.sh`, authored by `TOOL-aQuenchedHarness-5` in
this same build, plus each selected suite's existing arm set, which is preserved rather than
rewritten. `tools/codebase-map/reuse_lookup.py` returned `run` and `check` as the high-fan-in stems
over the thirteen existing `selftest.py` modules, confirming that the arm-running pattern is
duplicated per suite and has no shared owner today. The one prior instance of this exact work in this
tree — cutting a suite's spawn count from 469 to 220 per invocation — is recorded in
`tools/unattended/run-unattended-gates.sh`'s header and was read before writing; its lesson, that a
DERIVED equivalence claim went unfalsified and was wrong by 2.6x, is why S4 exists.

Recall terms used: `selftest gate leg ceiling guard GATE_SELFTESTS run-gates scratch repo mktemp
spawn wall-clock adopter kit.toml`
