# TOOL-aScannedThrottle-1 — measure the lander, find what actually binds its wall clock

**Status:** OPEN · rev-2 · 2026-08-21 · node a · Tier-1 · base 4773902f · streams tooling

## 1. Goal

The owner reports the lander is extremely slow and does not use the machine, and names the canary
gates as a congestion target. Measure the bar rather than theorise about it, decide whether the
named target is the real one, and return ranked recommendations each priced in seconds of span.

## 2. Scope (IN)

- **S1** — Reconstruct every full-bar schedule this node has a run record for: span, leg-seconds,
  floor, throughput, utilization, packing, and occupancy over time.
- **S2** — A list-schedule simulator over the measured leg durations, VALIDATED against the run it
  is built from before any what-if is believed, so a model that does not fit refuses itself.
- **S3** — Attribute the canary leg's wall clock to source lines on a quiet box, with the
  contention state of the run recorded alongside the numbers.
- **S4** — Re-measure the process-creation tax the backlog blames, on a quiet box, against the
  recorded baseline.
- **S5** — A written report with recommendations, each carrying the span it buys or an explicit
  zero, plus the reconciliation of every open backlog row about bar performance, **applied to the
  row and not only written in the report**. The population is DERIVED, not authored: every row in
  `memory/backlog/TOOL.md` whose status token is `OPEN` and whose text names the bar's wall clock,
  leg timings, pool width, dispatch order, spawn cost or scratch cost. A reconciliation is applied
  when the row itself carries a dated disposition line citing the report section that measured it.
  *(rev-2: the original said "every" and delivered a curated eight, which cannot distinguish an
  omission from a judgement call, and applied none of them to the backlog — spec audit F1, F4.)*

## 3. Non-goals (OUT)

No edit to `run-gates.sh`, `gate-legs.json`, `gate-profiles.txt` or any `*.test.sh`. No sharding of
the unattended selftests — that is `TOOL-aPacedTurnstile-8` and it stays a separate unit. No
Defender exclusion and no Memory Integrity change; both need admin and both are the owner's call.
Recommendations only. Follow-ups: the rows minted in §4 of the report.

## 4. Design

### Data model

The measurement reads artifacts the bar already writes and adds no instrumentation to it. Each
`<git-dir>/gate-run/<id>/<i>.leg` row is tab-separated `name · status · rc · seconds · start_ns ·
end_ns · input_key`, and the sibling `header` carries the resolved width and the dispatch order. A
schedule is therefore fully reconstructable after the fact, including occupancy, from records that
already exist.

### Inventory

Three throwaway readers, none installed, all in the session scratchpad: a schedule reconstructor, a
dispatch-order probe, and the simulator. The trace harness drives `bash -x` with a `PS4` carrying
`EPOCHREALTIME` and `LINENO`, and an attributor buckets inter-record gaps by source line.

### Alternatives rejected

Running fresh instrumented bars for the primary measurement — rejected because four real bars had
already written their records, and a synthetic run on a shared node measures the node's contention
rather than the bar. The synthetic runs were kept only for the canary trace, which needs xtrace.

## 5. Production-readiness checklist

- security — N/A: reads records, writes one report and one backlog block.
- perf / scale — the measurement itself must not perturb the subject; the canary trace waits on the
  turnstile beacon before starting.
- a11y — N/A: no user interface.
- i18n — N/A.
- error / empty / loading states — the simulator refuses when it cannot reproduce its own run; the
  attributor prints a dead-probe line when the trace holds no parseable records.
- observability — every number in the report names the run it came from.
- risks — a contended reading quoted as a quiet one. Mitigated by recording contention state beside
  each figure, and both contamination events are written into the report rather than dropped.
- testing + left-shift gates — this unit adds no product code, so it adds no gate. The findings it
  left-shifts are backlog rows, not gates.
- migration / rollback — N/A: records only.
- user docs — N/A: internal.

## 6. Acceptance criteria

- **AC1** — When the schedule reconstructor runs over this node's run records, it reports span,
  floor, throughput and utilization per run and names which bound binds, for every run holding
  `.leg` rows.
- **AC2** — When `sim.py` runs against a bar it does not fit it prints its own error and refuses
  rather than emitting what-ifs; against the well-scheduled run it reproduces the observed span
  within a stated tolerance.
- **AC3** — When `tools/run-gates/run-gates.test.sh` is traced under `bash -x`, at least 95 % of its
  wall clock is attributed to source lines and the unattributed remainder is reported as its own
  figure.
- **AC4** — When `memory/builds/aScannedThrottle/build/2026-08-20-build-TOOL-aScannedThrottle-1.md`
  is read, every recommendation carries a span figure in seconds or an explicit zero, and every dead
  end carries the measurement that killed it.
- **AC5** — The bar stays green on the records this unit adds: `bash tools/run-gates/run-gates.sh`
  scoped to the diff.

## 7. Gates

`memory hygiene`, `kickoff-manifest ratchet`, `build README slot contract`, `codebase-map coverage
+ freshness`, and the diff-scoped `bash tools/run-gates/run-gates.sh`. This unit adds no gate.

## 8. Open questions

none — this unit had no fork to resolve. Two things it could not establish are not forks in its
design; they are recorded as limits in the report's closing section and carried forward by a row
each. The real distribution of turnstile queue wait is `TOOL-aScannedThrottle-2`. The cold/warm
factor at the current leg count is `TOOL-aTimedTurnstile-4`, which the report's §6 already names.
*(rev-2: both limits used to cite the first row, which holds only one of them — spec audit F13.)*

## 9. Revision log

- rev-1 · 2026-08-20 · initial. The measurement is complete, but the status stays OPEN
  deliberately: this unit's deliverable is a set of recommendations and NONE of them is landed. A
  terminal status would assert that something shipped, and `drift-audit`'s
  `closed_specs_with_no_product_commit` signal is right to say otherwise — it reds exactly this
  shape, a closed plan with no product commit. Close it when the rows it minted are dispositioned.
- rev-2 · 2026-08-21 · the M4 spec audit that rev-1 never had, folded. Record:
  [`reviews/2026-08-21-review-TOOL-aScannedThrottle-1.md`](../reviews/2026-08-21-review-TOOL-aScannedThrottle-1.md),
  verdict CLEAN WITH FIXES, 38 confirmed of 46. What moved, and why:

  **The closing condition is REPLACED (F2, F3).** rev-1's "close it when the rows it minted are
  dispositioned" names a state no run bound to this build's scope can reach: four of the seven
  rows need edits §3 forbids, two need admin the owner holds, and "dispositioned" is a corpus
  hapax — it appears in this file and nowhere else, so it has no evaluable predicate at all. The
  cost was mechanical, not academic: an OPEN unit fails the unattended kit's machine-checked
  `build-complete` item, so every run carrying this build owed an override.

  **The replacement, each clause checkable against a named file.** CLOSE this unit when all three
  hold. (1) Every id in the report's §5 and §5.1 carries a dated disposition line in
  `memory/backlog/TOOL.md` citing the report section that measured it. (2) The rows this build
  minted — `TOOL-aScannedThrottle-2` … `-8` — are each present in that file. (3) A `spec-audit`
  and a `diff-review` record naming this id exist under `reviews/`. **Landing a recommendation is
  explicitly NOT a clause**: the build README puts that in separate units, and the seven minted
  rows are forward pointers, never the close gate.

  **What the flip to CLOSED still costs, recorded rather than taken (F5).** rev-1's drift premise
  is TRUE and was re-measured: `TRACE_GLOBS` in `tools/drift-audit/drift_signals.py` does not
  cover `memory/`, so a bare close takes `closed_specs_with_no_product_commit` to 2 against a pin
  of 1 and reds the `drift-audit records` leg. What rev-1 never mentions is that the signal
  documents its own escape for exactly this shape — `drift_report.py` names "a unit whose
  deliverable is records-only", which this unit is verbatim (§5, §10) — and the registry
  `memory/project/trace-waiver.txt` exists. **The trap:** the signal restricts its population to
  TERMINAL specs and turns a leftover waiver row into a suspect of its own, so **the waiver row
  and the status flip must land in ONE commit or neither.** All six existing rows are the OTHER
  shape (product landed before the id-in-subject convention), so this would be the first
  records-only waiver in the repo — a gate exemption of a new kind, which is an owner turn under
  the fork rule, not an agent's. It is PARKED on this run's record, not taken.

  **rev-1's §6 self-grade was wrong and is withdrawn (F7, F8).** It asserted "every §6 criterion
  is met". AC1 was not: the report's §2 table carries no throughput column and left the fourth
  run's row blank. AC4 was not: R4 read "UNQUANTIFIED", which is neither a figure nor an explicit
  zero. Both are corrected in the report at §2 and §4 R4, dated and marked.

  **Also folded:** the report's mint line undercounted its own rows and now reads `-2` … `-8`
  (F10); the backlog row that duplicated this unit's own id is re-minted as
  `TOOL-aScannedThrottle-8`, with R1's citation corrected (F6); the span range in the build
  README is reconciled to 925–1058 s (F12).

  **Not folded, and named so the omission is an answer.** Editing `AGENTS.md` — which still
  states 873 s against a measured 1001.3 s mean, and still names the dead `gate-timings.tsv` as
  the live dispatch input — is a change to a governance carrier and an owner turn. It is re-cited
  in `TOOL-aMeteredTurnstile-4` instead, whose own line number had gone stale.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "reconstruct a gate bar schedule from its run record and
grade pool utilization"` returns no seam that reads per-leg records. The nearest existing thing is
`tools/run-gates/profile_bar.py`, which brackets a wall clock around the runner and records a run
envelope — it does not open the `.leg` rows and cannot report occupancy, packing or dispatch rank.
Nothing was built to ship, so no seam was wired: the readers are throwaway scratchpad scripts, and
the finding is that `profile_bar.py` is the right home if any of them is ever worth keeping.
