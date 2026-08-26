# TOOL-aCollapsedScan-4 — `BUDGET_kit_gate` re-declared against a measurement, and the scoping refused

**Status:** INPROGRESS · rev-1 · 2026-08-26 · node a · Tier-1 · base 3c37a1fb · streams tooling · order 3

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Make `BUDGET_kit_gate` a ceiling the leg can actually meet, by re-declaring it against a measurement
with the reason beside it, and record in writing why the alternative — scoping check 30's population
— was refused. The file's own header names both outcomes as progress; what it forbids is raising a
ceiling silently.

## 2. Scope (IN)

- **S1** — `BUDGET_kit_gate` in `tools/unattended/run-unattended-gates.sh` re-declared, with the
  node-`a` measurement and the reason in the comment that sits beside it, in the same idiom the
  seven sibling ceilings use.
- **S2** — The NODE-RELATIVITY stated where the ceilings are declared: every figure in that block
  is a node-`d` reading, the same leg costs 2.5× more on node `a`, and a single global integer
  cannot be right for both. Stated as a known limit of the mechanism, not fixed here.
- **S3** — The refusal of the scoping alternative recorded in `memory/DECISIONS.md`, with the
  measurement that decided it.

## 3. Non-goals (OUT)

- Scoping check 30 to changed builds. §8 F1 resolves this and §4 records the reasoning; the whole
  point of this unit is that the refusal is written down rather than left as an untaken option.
- Making the ceilings node-relative. That is the real defect S2 names and it is a mechanism change
  across eight declarations and their reader; this unit measures and states it, and leaves a
  backlog row.
- Adding a `ceiling` field to `tools/gate-legs.json`. That is `TOOL-aCollapsedScan-5` and it is a
  merge-bar contract change with 85 legs in scope.
- Any further optimization of `check-unattended.sh` or `--plan`. `TOOL-aCollapsedScan-1` took the
  spawn cost out; what remains is `plan_state`, driver startup and per-build git work, and its §3
  already rules the first of those out.

## 4. Design

### The measurement this ceiling is set against

Node `a`, 2026-08-26, `bash tools/unattended/run-unattended-gates.sh --checks`:

| When | kit gate | Declared ceiling |
|---|---|---|
| at `da9e4cd2`, before the spawn fix | 305 s | 120 s |
| at `3c37a1fb`, after it | 187 s | 120 s |

The 120 s figure was declared 2026-08-23 against a 28 s reading on node `d`. The same leg with check
30 removed costs about 70 s on node `a`, so the two nodes differ by roughly 2.5× on this leg's own
work, and 28 × 2.5 is 70. The ceiling was never wrong about node `d`; it was never a statement about
node `a` at all.

The new value is **240 s** — the 187 s measurement plus headroom for the ambient-load factor this
same file already documents at 2.4× for a different suite. It reds well before the 305 s the leg
cost when nobody was watching, which is the property a ceiling has to keep.

### Why the scoping alternative was refused

Change-scoping check 30 to builds whose `README.md` or `spec/*.md` moved would save roughly 100 s of
a 650 s bar, about 15%. Against that: check 30's own header states it is a corpus check
deliberately, because the blocker it gates was live on FIVE tracked builds while every fixture arm
in the kit was green. A scoped walk grades the records that changed and is blind to a driver change
that breaks the property everywhere at once — and the driver is exactly what
`TOOL-aCollapsedScan-1` just rewrote. Buying 15% of a bar by narrowing the only check that saw
those five builds is the wrong side of that trade, and the previous unit already refused a
different narrowing of the same check on measurement.

### Files touched (estimate)

`tools/unattended/run-unattended-gates.sh`, `memory/DECISIONS.md`, `memory/backlog/TOOL.md`.

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — the subject. No code runs differently; a declaration changes.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — N/A.
- observability — improved: the ceiling stops firing on every run, so a future breach is a signal
  rather than noise a reader learns to skip.
- risks — a ceiling raised is a ceiling that catches less. Bounded by the fact that the old one
  caught nothing, because nothing on the bar runs the checker that reads it.
- testing + left-shift gates — the check IS the runner; `--checks` exits 1 on a breach, verified.
- migration / rollback — a one-integer revert.
- user docs — none owed.

## 6. Acceptance criteria

- **AC1** — When `bash tools/unattended/run-unattended-gates.sh --checks` runs on node `a`, it
  reports no `OVER BUDGET` line and exits 0.
- **AC2** — When the new `BUDGET_kit_gate` value is read, the comment beside it names the node, the
  date and the measurement, matching the idiom of the seven sibling `BUDGET_*` declarations.
- **AC3** — When the ceiling is deliberately breached by lowering it in a scratch copy,
  `--checks` prints `OVER BUDGET` and exits 1, so the mechanism is observed still armed rather than
  assumed.
- **AC4** — When `bash tools/run-gates/run-gates.sh` runs, the bar is green.

## 7. Gates

`unattended kit gate` · `playbook validity gate` · `unattended skill wiring` · the full bar. No new
gate: the ceiling is itself the check, and it already exists.

## 8. Open questions

- **F1 — re-declare, or scope check 30's population?** Both are sanctioned by
  `run-unattended-gates.sh`'s own header. RESOLVED (agent, 2026-08-26, delegated): re-declare.
  §4 carries the measurement and the reasoning; the deciding factor is that scoping trades the only
  check that ever saw the five defective builds for 15% of a bar.
- **F2 — is a global integer the right shape for a node-variable cost?** RESOLVED (agent,
  2026-08-26, delegated): no, and that is recorded rather than fixed. S2 states it beside the
  declarations and a backlog row carries it; changing the shape touches eight declarations and their
  reader, which is a unit of its own and not a rider on this one.

## 9. Revision log

- rev-1 · 2026-08-26 · initial draft.

## 10. Reuse audit

The seam is the `BUDGET_*` block in `tools/unattended/run-unattended-gates.sh` and its `run_one`
reader, which already treats a missing ceiling as a failure and prints the breach with both numbers.
This unit changes one declared value inside that mechanism and adds nothing beside it. Recall terms
used: `duplicate id backlog shard decision log hygiene check merge driver row-keyed conflict ceiling
budget gate leg check-30 population liveness`.
