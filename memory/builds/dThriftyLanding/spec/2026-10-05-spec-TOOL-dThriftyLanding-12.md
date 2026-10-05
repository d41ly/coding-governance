# TOOL-dThriftyLanding-12 — the closing review's batched minors, round 1

**Status:** CLOSED · rev-2 · 2026-10-05 · node d · Tier-2 · base f765eb8e · streams tooling · order 12

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-05-build-TOOL-dThriftyLanding-1-runlog-58509c21.md](../build/2026-10-05-build-TOOL-dThriftyLanding-1-runlog-58509c21.md) | journal | TOOL-dThriftyLanding-1 TOOL-dThriftyLanding-2 TOOL-dThriftyLanding-3 TOOL-dThriftyLanding-4 TOOL-dThriftyLanding-5 TOOL-dThriftyLanding-6 TOOL-dThriftyLanding-8 TOOL-dThriftyLanding-9 TOOL-dThriftyLanding-10 TOOL-dThriftyLanding-11 |
| [2026-10-05-build-TOOL-dThriftyLanding-12-1-acceptance-ledger.md](../build/2026-10-05-build-TOOL-dThriftyLanding-12-1-acceptance-ledger.md) | journal | — |
| [2026-10-05-prompt-TOOL-dThriftyLanding-12-1-build-brief.md](../prompts/2026-10-05-prompt-TOOL-dThriftyLanding-12-1-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The closing review's eighteen confirmed mediums and lows, promoted as one unit by the owner's ruling
`TOOL-aBatchedMinors-5`. Each item below names the finding ids it closes; the review record carries
their evidence. M1's findings 6, 7 and 23 are the high defect at medium grade, closed by units 8 and 9
and listed here so every id has a home.

## 2. Scope (IN)

- **S1** — M1, findings 6, 7 and 23: closed by the full-history reads of units 8 and 9; nothing further.
  Observed by AC1.
- **S2** — M2, findings 2 and 8: the hook treats a push as doc-only only when the inherited-red policy
  at R reads `land`, and says why when it does not, so a doc push under `park` cannot skip a leg red at
  an unproven R. Observed by AC2.
- **S3** — M3, findings 9 and 13: govkit's hand-edit drift predicate compares `doc_reads` as it compares
  `argv` and `guard`. Observed by AC3.
- **S4** — M4, findings 11, 16 and 24: canary 1b grades guard and `doc_reads` elements at a path
  component boundary, as the runner's pathspecs and the deployer do. Observed by AC4.
- **S5** — M5, finding 12: an element `.` or one starting `./` voids the doc class. Observed by AC5.
- **S6** — M6, finding 17: an install-level selftest arm applies a kit whose leg declares `doc_reads` to
  a fixture target and reads the emitted row; the below-floor half stays the unit-level D1 arm,
  because a target holding a run-gates install needs a receipt claiming it, which a fixture cannot
  plant without tripping the converge refusal. Observed by AC6.
- **S7** — L1, finding 14: the runner comment and the run-gates README state that the shared stamp is
  one slot per clone, last writer wins. Observed by AC7.
- **S8** — L2, finding 15: the hook drops the dead re-read of the own record on the FULL path. Observed
  by AC7.
- **S9** — L3, findings 19, 20 and 21: arms for the inherited-green docs decision, for a linked
  worktree adopting the primary's stamp, for the runner withholding `GATE_DOCS_BASE` from a leg, and a
  positive control for the 3i2 stamp absence. Observed by AC8.
- **S10** — L4, finding 25: the charter and the gate-env note say a doc push skips a DECLARED leg whose
  reads did not move and that any worktree's green serves every push; `memory/DECISIONS.md` records
  the dropped developer-choice sentence. Observed by AC9.
  **Readers:** by name: none — no tracked file spells the dropped sentence. by value: NO VALUE READERS —
  it was prose in the charter, read by people only.

## 3. Non-goals (OUT)

- The high findings: units 8 to 11.
- Keying the shared stamp by sha: L1 is fixed by documenting the slot, the fix the review names as the
  minimum.

### Edges

- **consumes-from** `TOOL-dThriftyLanding-8` — the runner read S1 relies on.
- **consumes-from** `TOOL-dThriftyLanding-9` — the hook read S1 relies on.

## 4. Design

### Evidence

Read at `f765eb8e`, against the review record `memory/builds/dThriftyLanding/reviews/2026-10-05-review-TOOL-dThriftyLanding-1-closing-diff-round1.md`, which states each finding's
location, reproduction and judged-sound fix.

### Files touched (estimate)

- `.githooks/pre-push`
- `.githooks/pre-push.test.sh`
- `.githooks/gate-env.sh`
- `tools/run-gates/run-gates.sh`
- `tools/run-gates/run-gates.test.sh`
- `tools/run-gates/README.md`
- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`
- `AGENTS.md`
- `memory/DECISIONS.md`

### Alternatives rejected

- **Split the batch in two.** Its write sets intersect on the hook and the runner, so by M6's clauses
  the two halves would not be disjoint; one unit, built in sequence.

## 5. Production-readiness checklist

- perf / scale — no new process on the common path.
- security — narrows nothing the push boundary decides; each change makes a skip rarer or a check wider.
- error / empty / loading states — unchanged.
- observability — each refusal or decision names its reason.
- testing — each arm observed RED against `f765eb8e` first.
- migration — none.
- user docs — the carriers unit 6 wrote, where this unit's change touches them.
- risks — none beyond the finding's own.

## 6. Acceptance criteria

- **AC1** — When units 8 and 9's arms run, the runner prints `GATE ok` for the merged side branch's
  doc path and the hook prints no `docs-only` for its code.
  Red when: either arm fails.
- **AC2** — When a DOCS fixture declares `INHERITED_RED=park` at R and pushes a doc edit, the decision
  carries no `docs-only` and the hook names the policy.
  Red when: the hook at `f765eb8e` prints `docs-only` under `park`.
- **AC3** — When a fixture target's owned row has its `doc_reads` hand-edited, the next apply reports
  drift rather than overwriting it.
  Red when: govkit at `f765eb8e` overwrites the row silently.
- **AC4** — When canary 1b's predicate reads a manifest whose `doc_reads` names a string prefix of a
  tracked file, it fails; naming the directory, it passes.
  Red when: the prefix passes, as at `f765eb8e`.
- **AC5** — When R declares `GATE_DOC_PATHS="."`, the hook prints `not a plain repo path` and no
  `docs-only`.
  Red when: the hook at `f765eb8e` classifies the push doc-only.
- **AC6** — When the install-level arm applies `check-kit-versions` to a fresh fixture target, the
  emitted `kit version markers` row carries `"doc_reads": []`, and D1 still refuses the key at 1.24.
  Red when: the emitted row drops the descriptor's declaration.
- **AC7** — When `grep -n 'last writer wins' tools/run-gates/README.md tools/run-gates/run-gates.sh` runs,
  each file prints a line, and the hook no longer re-reads the own record after a FULL decision.
  Red when: either statement is absent.
- **AC8** — When the new L3 arms run, the inherited-green docs line names `docs-only`, the linked
  worktree adopts the common dir's own stamp, a leg reads `GATE_DOCS_BASE` as unset, and the 3i2 full
  run writes `gate-full-green`.
  Red when: any arm fails.
- **AC9** — When `grep -n 'DECLARED leg' AGENTS.md` runs, it prints the reworded sentence, and
  `memory/DECISIONS.md` holds the row naming the dropped sentence; `charter size` stays green.
  Red when: the charter still says only legs whose reads moved run.

## 7. Gates

`pre-push self-test` · `run-gates canary` · `run-gates evidence` · `govkit selftest` · `govkit selfcheck` · `charter size` · `govkit acceptance matrix` · `govkit refusal join` · `recall floor arms` · `recall floor` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

New arm: .githooks/pre-push.test.sh · a doc push under INHERITED_RED=park and one under GATE_DOC_PATHS=. at R, against the f765eb8e hook · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-05 · promoted from the closing diff review, round 1.
- rev-2 · 2026-10-05 · S6 and AC6: the below-floor half stays at the unit level, measured — a fixture
  holding run-gates without a claiming receipt is refused by the deployer before it writes anything.
  The two kits this unit and units 8 to 11 moved, run-gates and govkit, advance to 1.27 and 1.14.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "scope the push-boundary bar to the legs a doc-only diff can affect"` was run for the build and cannot see `.sh`; no existing seam fits beyond the one named here. Each fix extends the seam its finding names: `classify_docs`, `write_gate_legs`'s drift predicate,
canary 1b, the stamp comment, and the existing DOCS and IR fixtures of the hook suite.

Recall terms used: pre-push GATE_FULL scoped gate full green stamp guard lag bound records-only landing push-main.sh leg manifest merge second parent
