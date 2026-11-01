# TOOL-dScopedBuild-37 — the bar scrub is the hook's `BAR_SCRUBBED_KNOBS` plus the driver's two, so `GATE_REGEN_CHECK` is scrubbed too

**Status:** OPEN · rev-2 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 3 · advances TOOL-dScopedBuild-16

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md) | journal | TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 TOOL-dScopedBuild-25 TOOL-dScopedBuild-26 TOOL-dScopedBuild-27 TOOL-dScopedBuild-28 TOOL-dScopedBuild-29 TOOL-dScopedBuild-30 TOOL-dScopedBuild-31 TOOL-dScopedBuild-32 TOOL-dScopedBuild-33 TOOL-dScopedBuild-34 TOOL-dScopedBuild-35 TOOL-dScopedBuild-36 TOOL-dScopedBuild-38 TOOL-dScopedBuild-39 TOOL-dScopedBuild-40 TOOL-dScopedBuild-41 |
| [2026-11-01-review-TOOL-dScopedBuild-36-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dScopedBuild-36-spec-audit-round1.md) | spec-audit | TOOL-dScopedBuild-38 TOOL-dScopedBuild-36 TOOL-dScopedBuild-39 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 25 to 35
(`memory/builds/dScopedBuild/reviews/2026-11-01-review-TOOL-dScopedBuild-25-spec-audit-round1.md`)
confirmed finding **id 22 at HIGH**, report item **H2**. `TOOL-dScopedBuild-32` S1 moves the
`gates-green` arm's seven-knob `_gknobs` line verbatim into `derive_bar_scrub` and calls it "the one
knob list", and its AC2 pins those seven names. The hook's `BAR_SCRUBBED_KNOBS`
(`.githooks/pre-push:1842`) also scrubs `GATE_REGEN_CHECK`, and its comment (`:1838-1841`) says the
push that lands may not choose it. The driver's own comment (`tools/unattended/unattended.sh:11160`)
calls its list the hook's plus the docs knob, so the omission is drift. Built as written,
`run_gate_bar` passes an inherited `GATE_REGEN_CHECK=0` to `build-exit` and `build-core`, and
`tools/run-gates/run-gates.sh:1442` then skips the generated-output preflight, so `build-exit: PASS`
can certify a stale generated output.

This unit states the list as the hook's names plus the driver's two and observes it against the
hook's own line. It repairs `TOOL-dScopedBuild-32` and builds one step after it (order 3).

## 2. Scope (IN)

- **S1** — The list. `derive_bar_scrub`'s knob line is the hook's `BAR_SCRUBBED_KNOBS` plus
  `GATE_REUSE_LINEAGE` and `GATE_DOCS_BASE`, eight names:
  `local _gk _gknobs="GATE_LEGS GATE_REUSE GATE_REUSE_LINEAGE GATE_DOCS_BASE GATE_SPAWN_CMD
  GATE_SPAWN_FLOOR GATE_VERDICT_FAULT GATE_REGEN_CHECK" _gset=""`, on one line, so the parity arm's
  cut (`tools/unattended/unattended.test.sh:4341`) reads it. The comment above it says
  `GATE_REGEN_CHECK` is the hook's and why. This supersedes unit 32 S1's "moved verbatim" seven-name
  line; the rest of S1 stands. Observed by AC1 and AC2.
- **S2** — The criterion that pins it. Unit 32 AC2's "prints the seven knob names" is superseded by
  AC2 here, which reads the hook's list off `.githooks/pre-push` and pins no count. Unit 32's
  acceptance ledger answers its AC2 with a note naming `TOOL-dScopedBuild-37 S2`. Observed by AC2.
- **S3** — The `gates-green` arm's change, stated. The arm reads the same list through
  `derive_bar_scrub`, so its bar now also runs with `GATE_REGEN_CHECK` unset and its not-honoured
  line names the knob when it was set. This answers unit 32 §5's risk line "the `gates-green` arm's
  behaviour must not move" for this one knob. Observed by AC1.
- **S4** — The parity arm green. The driver suite's parity arm for TOOL-aFrugalTurnstile-12 AC3
  (`unattended.test.sh:4334-4345`), red at base on `MISS GATE_REGEN_CHECK`, passes once S1 lands.
  NOT OBSERVED by a criterion here: it is a suite arm, and the close observes it red before this
  unit and green after, as §7 says.

## 3. Non-goals (OUT)

- Reading the hook's file at run time from the driver. A shipped driver does not depend on a hook
  path an adopter may not install, and AC2's read off the hook keeps the two lists equal.
- Moving the parity arm into a shard a bar leg runs, the report's second left-shift gate. No clause
  of this build names it.
- `run_gate_bar`'s signature, reap and bound, ids 15 and 31 of the same audit, which
  `TOOL-dScopedBuild-39` takes.

### Edges

- **consumes-from** `TOOL-dScopedBuild-32` — S1's `derive_bar_scrub` knob line and AC1's and AC2's knob sets, which S1 and S2 restate with `GATE_REGEN_CHECK` (id 22)
- **hands-off** `TOOL-dScopedBuild-41` — S1's comment and S3's `gates-green` line, which this unit's builder observes in the driver suite's TOOL-aFrugalTurnstile-12 AC1/AC2 arm with `GATE_REGEN_CHECK=0` exported, AC2's hook cut, which that unit's AC9 requires non-empty, and §3, which its S22 completes with `PM_SCRUB` (ids 6, 25, 22)

## 4. Design

### Evidence

- `.githooks/pre-push:1842`: `BAR_SCRUBBED_KNOBS="GATE_LEGS GATE_REUSE GATE_SPAWN_CMD GATE_SPAWN_FLOOR
  GATE_VERDICT_FAULT GATE_REGEN_CHECK"`.
- `unattended.sh:11163`: the arm's seven names, with no `GATE_REGEN_CHECK`;
  `grep -n GATE_REGEN_CHECK tools/unattended/unattended.sh` prints nothing at base.
- `unattended.test.sh:4334-4345`: the parity arm cuts `^ *local _gk _gknobs="..."` and names every
  hook name missing from it; at base the loop prints `MISS GATE_REGEN_CHECK` (the report's id 22).
- `run-gates.sh:1442`: `GATE_REGEN_CHECK=0` prints `generated outputs NOT checked` and skips the
  preflight.

### The list, after this unit

| Knob | Source |
|---|---|
| `GATE_LEGS`, `GATE_REUSE`, `GATE_SPAWN_CMD`, `GATE_SPAWN_FLOOR`, `GATE_VERDICT_FAULT`, `GATE_REGEN_CHECK` | the hook's `BAR_SCRUBBED_KNOBS` |
| `GATE_REUSE_LINEAGE` | the driver's, TOOL-aSparedSpawn-33 S7 |
| `GATE_DOCS_BASE` | the driver's docs knob |

### Inventory

Minted: nothing. No lexicon cell applies.

### Migration

None: no stored data changes.

### Rollout

Built at order 3, one step after unit 32 (order 2), tied with units 2 and 30. Unit 30 regenerates
`memory/map/generated/symbols.json`, whose generator reads `tools/unattended/unattended.sh`, so
BUILD-METHOD M6 sequences this unit with it within the step; unit 2's write set is disjoint.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`: unit 32 AC1's arm gains the knob

### Alternatives rejected

- **Keep seven names and document the gap.** The hook's comment says the landing push may not choose
  the knob, and a bar the driver runs certifies the same tree.
- **Source `BAR_SCRUBBED_KNOBS` from the hook at run time.** §3's first bullet.

## 5. Production-readiness checklist

- security — deny by default: an inherited knob that skips a preflight is unset for every bar the
  driver runs.
- perf / scale — the generated-output preflight now runs where an inherited knob had skipped it.
- error / empty / loading states — unchanged; an unset knob reads as the runner's default.
- observability — the not-honoured line names `GATE_REGEN_CHECK` when it was set.
- risks — `gates-green` gains the knob (S3); AC1 observes the new line.
- testing — AC1 in the driver suite, AC2 by probe, the parity arm at the close.
- migration — none.
- user docs — none under `help/`; no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When `GATE_LEGS=<a one-row manifest> GATE_REUSE=1 GATE_REGEN_CHECK=0 bash unattended.sh
  --build-exit tExit` runs in the driver suite's fixture, its `GATE_CMD` a stub recording
  `${GATE_LEGS-unset}`, `${GATE_REUSE-unset}` and `${GATE_REGEN_CHECK-unset}`, the stub records
  `unset unset unset` and the output holds `build-exit — not honoured from the environment by this
  bar: GATE_LEGS GATE_REUSE GATE_REGEN_CHECK`.
  Red when: the exit's bar inherits `GATE_REGEN_CHECK`.
  fixture: unit 1 AC5's slug fixture and stub bar, as unit 32 AC1 uses it.
- **AC2** — When `hk=$(sed -n 's/^BAR_SCRUBBED_KNOBS="\([^"]*\)"$/\1/p' .githooks/pre-push)` and
  `drv=$(sed -n 's/^ *local _gk _gknobs="\([^"]*\)".*/\1/p' tools/unattended/unattended.sh )` run on
  the built tree, every word of `$hk` is a word of `$drv`, `$drv` also holds `GATE_REUSE_LINEAGE` and
  `GATE_DOCS_BASE`, and `grep -c '_gknobs="' tools/unattended/unattended.sh` prints 1.
  Red when: the hook names a knob the driver's list lacks, or a second copy of the list exists.
  figure: DERIVED at observation from the hook's line; at base `GATE_REGEN_CHECK` is the one miss.

## 7. Gates

`unattended kit gate` · `harness arms (fail branches armed or pinned)` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · covers AC1 · unit 32 AC1's exit arm with `GATE_REGEN_CHECK=0` exported and recorded at the stub, staged by dropping the knob from the list · none

The close also runs the existing parity arm of S4, red at base and green after S1, and records both
in this unit's acceptance ledger.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a)
  `**Derived:**` naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of unit 32's clause. RESOLVED
  (agent, 2026-11-01, delegated): (a), rung 3, the precedent `TOOL-dWitnessedBar-91` §8 F1 set.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from the round-1 spec audit of units 25 to 35, id 22
  (HIGH, item H2).
- rev-2 · 2026-11-01 · §3 · the Edges block gains the bullet mirroring the edges of TOOL-dScopedBuild-41,
  the promotions of the round-1 spec audit of units 36 to 39 (ids 6, 25, 22).

## 10. Reuse audit

The seam is unit 32 S1's `derive_bar_scrub` and the knob line it moves from
`tools/unattended/unattended.sh:11163`, held to the hook's `BAR_SCRUBBED_KNOBS` by the parity arm
that already exists (`tools/unattended/unattended.test.sh:4334-4345`). `python
tools/codebase-map/reuse_lookup.py "the list of bar knobs the pre-push hook scrubs"` ranked `pre`,
`read_id_list`, `declared_list` and `read_id_list_refusals`, none a knob list, so no other seam fits.

Recall terms used: `python tools/memory-recall/query.py "which knobs does the landing push scrub before the bar" --terms "BAR_SCRUBBED_KNOBS GATE_REGEN_CHECK _gknobs derive_bar_scrub gates-green parity arm pre-push scrub knob"`
