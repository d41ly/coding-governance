# TOOL-aScannedThrottle-1 — measure the lander, find what actually binds its wall clock

**Status:** OPEN · rev-1 · 2026-08-20 · node a · Tier-1 · base 4773902f · streams tooling

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
  zero, plus the reconciliation of every open backlog row about bar performance.

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

none — this unit had no fork to resolve. Two things it could not establish (the cold/warm factor at
the current leg count, and the real distribution of turnstile queue wait) are not forks in its
design; they are recorded as limits in the report's closing section and carried forward by
`TOOL-aScannedThrottle-2`.

## 9. Revision log

- rev-1 · 2026-08-20 · initial. The measurement is complete and every §6 criterion is met, but the
  status stays OPEN deliberately: this unit's deliverable is a set of recommendations and NONE of
  them is landed. A terminal status would assert that something shipped, and `drift-audit`'s
  `closed_specs_with_no_product_commit` signal is right to say otherwise — it reds exactly this
  shape, a closed plan with no product commit. Close it when the rows it minted are dispositioned.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "reconstruct a gate bar schedule from its run record and
grade pool utilization"` returns no seam that reads per-leg records. The nearest existing thing is
`tools/run-gates/profile_bar.py`, which brackets a wall clock around the runner and records a run
envelope — it does not open the `.leg` rows and cannot report occupancy, packing or dispatch rank.
Nothing was built to ship, so no seam was wired: the readers are throwaway scratchpad scripts, and
the finding is that `profile_bar.py` is the right home if any of them is ever worth keeping.
