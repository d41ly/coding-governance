# TOOL-dPlacedRequest-46 — the bounded age walk stops on a `renews: -` commit before any threshold test

**Status:** CLOSED · rev-6 · 2026-11-20 · node a · Tier-2 · base c63aabbb · streams tooling · order 24 · advances TOOL-dPlacedRequest-22

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-44-promoted-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-44-promoted-fix-return.md) | research | TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 |
| [2026-10-25-build-TOOL-dPlacedRequest-46-deviation-461.md](../build/2026-10-25-build-TOOL-dPlacedRequest-46-deviation-461.md) | deviation | — |
| [2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md) | journal | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-20-build-TOOL-dPlacedRequest-46-1-acceptance-ledger.md](../build/2026-11-20-build-TOOL-dPlacedRequest-46-1-acceptance-ledger.md) | journal | — |
| [2026-11-20-build-TOOL-dPlacedRequest-46-red-fix-31.md](../build/2026-11-20-build-TOOL-dPlacedRequest-46-red-fix-31.md) | red-fix | — |
| [2026-10-25-prompt-TOOL-dPlacedRequest-44-promoted-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-44-promoted-fix-brief.md) | research | TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 |
| [2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dPlacedRequest-11-build-brief.md) | research | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-20-prompt-TOOL-dPlacedRequest-46-1-spec-writer.md](../prompts/2026-11-20-prompt-TOOL-dPlacedRequest-46-1-spec-writer.md) | journal | — |
| [2026-11-20-prompt-TOOL-dPlacedRequest-46-2-spec-writer.md](../prompts/2026-11-20-prompt-TOOL-dPlacedRequest-46-2-spec-writer.md) | journal | — |
| [2026-11-20-prompt-TOOL-dPlacedRequest-46-divergence-brief.md](../prompts/2026-11-20-prompt-TOOL-dPlacedRequest-46-divergence-brief.md) | research | — |
| [2026-11-20-prompt-TOOL-dPlacedRequest-46-pass-red-fix-brief.md](../prompts/2026-11-20-prompt-TOOL-dPlacedRequest-46-pass-red-fix-brief.md) | research | — |
| [2026-11-21-prompt-TOOL-dPlacedRequest-46-mark-rewrap-brief.md](../prompts/2026-11-21-prompt-TOOL-dPlacedRequest-46-mark-rewrap-brief.md) | research | TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 |
| [2026-10-25-review-TOOL-dPlacedRequest-44-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-44-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 |
| [2026-11-19-review-TOOL-dPlacedRequest-11-spec-audit.md](../reviews/2026-11-19-review-TOOL-dPlacedRequest-11-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round1.md](../reviews/2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round1.md) | diff-review | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round2.md](../reviews/2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round2.md) | diff-review | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-2 promotions
(`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-35-spec-audit.md`)
confirmed **finding 32 at HIGH**, its item **H2**, which holds no other finding.
`TOOL-dPlacedRequest-35` S1 orders three stops: the epoch change, the renewing beat on `renews`
reading `yes` or absent, then `seen-utc < threshold -> stale`. A commit carrying `renews: -` matches
neither of the first two.

The builder's pass of run `wf_5cc8df6e-de1` found that the audit's case, every held lease going stale
under `leases.renewal none`, does not happen on the tree. A `-` commit the feed sighted before the
threshold stops the walk there, and the verdict pass reads a stopping commit's `-` as `live` before
any bound compare, so a chain written wholly under `none` reads `live`.

The defect this unit repairs is the mixed chain. A renewal-policy change to `none` mid-tenure writes a
`-` commit above older commits of the same tenure. When the `-` commit was sighted inside the bound
and an older `renews: no` commit before the threshold, the walk reads past the `-` commit, stops on
the older one, and the row reads `stale`. The holder's newest write declares a lease that never
expires (`TOOL-dPlacedRequest-17` S3), yet another node may take it over. This unit repairs
`TOOL-dPlacedRequest-35`, at order 23, so it sits at order 24: the walk names every class of `renews`
and the `-` class has its own stop ahead of the threshold.

## 2. Scope (IN)

- **S1** — The `-` stop. Inside the tenure, a commit whose `renews` reads `-` stops the walk and
  resolves the row by `TOOL-dPlacedRequest-17` S3's never-stale rule: `live`, or `unknown` with age
  `-` when the feed has not sighted that commit. It is tested after the epoch stop and before the
  threshold test, so the walk never reads past a `-` commit to an older one. Observed by AC1, AC2 and
  AC4.
- **S2** — Every class named. The walk's stops cover each value `renews` takes: `yes`, absent on a
  legacy claim, `-`, and `no`, which alone reads on; a value outside the four reads on as `no` does.
  A fixture row runs the walk once per class. Observed by AC3.
- **S3** — The guide names the stop. Section 7 of `tools/unattended/STOPS.template.md`, copied to
  `memory/guides/UNATTENDED-STOPS.md`, defines the renewing beat as the newest commit of the tenure
  whose `renews` reads `yes` or is absent; it gains the `-` commit as a stop of the same walk, so the
  guide predicts the mixed chain's `live`. Observed by AC5.

## 3. Non-goals (OUT)

- No change to which write sets `renews: -`: `TOOL-dPlacedRequest-25`'s.
- No change to the epoch stop, the renewing beat or the fallback: `TOOL-dPlacedRequest-35` S1 and S2.
- No change to the verdict pass: its never-stale read of the stopping commit's flag is
  `TOOL-dPlacedRequest-17` S3's and stays.
- No guard for an unsighted commit at the threshold test: finding 33's, `TOOL-dPlacedRequest-47`.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-35` — S1's stop order inside the age pass's `awk`, which this unit extends with the `-` stop; without it there is no ordered walk to extend
- **hands-off** `TOOL-dPlacedRequest-52` — the walk, S2 and AC3, which that unit's items for findings 9, 35 and 36 merge with `TOOL-dPlacedRequest-47`'s walk and extend with out-of-set rows

## 4. Design

### The walk, per tail

```
per tail, tip first, tip included:
  tip                         -> tenure epoch = its epoch (absent reads 0)
  epoch != tenure epoch       -> tenure ended: resolve by 35 S2
  renews -                    -> stop here: the verdict pass reads it live, unknown if unsighted   (S1)
  renews yes or absent        -> renewing beat: resolve, age from its sighting
  seen-utc < threshold        -> resolve stale
  else                        -> oldest-of-tenure = this commit, read on
```

The `-` stop sits beside the renewing beat because both resolve the row on the commit's own class.
It sits above the threshold test because a never-expiring lease has no threshold, and a commit older
than the `-` one must never decide the row.

### Evidence

- The walk is the `step` function of the walk `awk` in `tools/unattended/unattended.sh#read_claims`.
  A commit stops a row on the epoch change, on `renews` reading `yes` or absent
  (`tools/unattended/unattended.sh@87ec5c35d720:2594`), or on a feed sighting before the threshold
  (`tools/unattended/unattended.sh@87ec5c35d720:2595`); otherwise the walk reads on to its parent. A
  `-` commit reaches only the threshold test.
- The walk prints, per row, whether its stopping commit carries `renews: -`
  (`tools/unattended/unattended.sh@87ec5c35d720:2626`). The verdict pass reads that flag as `live`
  (`tools/unattended/unattended.sh@87ec5c35d720:2644`) before the bound compare
  (`tools/unattended/unattended.sh@87ec5c35d720:2646`).
- The builder's probe, PINNED by run `wf_5cc8df6e-de1` on 2026-11-20: a `-` tip sighted 60 s (PINNED) ago
  over a `renews: no` commit of the same epoch sighted 3600000 s (PINNED) ago reads `stale` on the
  unit-35-order copy and `live` with the stop.
- Read from `step`, not measured: a `renews: yes` commit sighted before the threshold beneath a
  younger `-` commit of the same tenure stops the row as its renewing beat and reads `stale` too. The
  `-` stop covers it, and no criterion plants it.
- `TOOL-dPlacedRequest-17` S3: a row whose renewing beat carries `renews: -` (`leases.renewal: none`)
  never reads `stale`.

### Files touched (estimate)

- `tools/unattended/unattended.sh`: the walk `awk` in `read_claims`, and the function's header
  comment that names the stops
- `tools/unattended/unattended.test.sh`: the class arms
- `tools/unattended/STOPS.template.md`: section 7's renewing-beat sentence
- `memory/guides/UNATTENDED-STOPS.md`: the dogfooded copy of the same sentence

`TOOL-dPlacedRequest-47` writes the same two driver files at the same order, so the two passes run in
sequence.
- `memory/map/generated/`: regenerated by the codebase-map kit's `gen_map.py --write` in this
  unit's own pass wherever its diff mints, renames or deletes a function the symbol extractor reads,
  so `gen_map.py --check` exits 0 after the pass; `TOOL-dPlacedRequest-34` S38 is the final re-check
  only

### Alternatives rejected

- **Fold `-` into the renewing beat's test.** It reads the same verdicts and the same `beat-sha`,
  because the verdict pass reads the flag from whichever commit stops the row. It is rejected because
  `read_claims`' header comment and `TOOL-dPlacedRequest-35` S1 define the renewing beat as `yes` or
  absent, and S2 keeps one stop per class.
- **Skip the threshold test for the whole chain under `none`.** The walk reads the record, not the
  conf, and a chain written partly under another policy carries both classes.
- **Drop the verdict pass's never-stale read so a `-` row is judged by its walk alone.** It would
  remove `TOOL-dPlacedRequest-17` S3's rule only to give the old criteria a red (F2).

## 5. Production-readiness checklist

- security — closes a take-over of a held lease whose tenure carries a `-` commit above an older
  commit sighted before the threshold.
- perf / scale — none: one more string compare per commit, and the walk now stops at the tip under
  `none`.
- error / empty / loading states — an unsighted `-` commit reads `unknown`, age `-`.
- observability — `--claims`' verdict field, unchanged in shape.
- risks — none beyond `TOOL-dPlacedRequest-26` §5's.
- testing — the probes of §6 and the arm in §7.
- migration — none: the walk is new in this build.
- user docs — S3: section 7 of `memory/guides/UNATTENDED-STOPS.md` names the `-` stop beside the
  renewing beat.

## 6. Acceptance criteria

The fixture is the observer clock's fixture in `tools/unattended/unattended.test.sh`, which
`TOOL-dPlacedRequest-26` and `TOOL-dPlacedRequest-35` extend: a scratch clone with a bare origin,
`RUN_CLAIMS=on`, planted lease commits and feed lines, and `leases.expiry-hours` at the fixture's
default of 24. The unit-35-order copy is a scratch copy of the driver whose walk `awk` lacks the `-`
stop, so it holds `TOOL-dPlacedRequest-35` S1's order.

- **AC1** — When a tenure's tip carries `renews: -`, sighted 60 s (PINNED) ago, over a `renews: no` commit of
  the same epoch sighted 3600000 s (PINNED) ago, `--claims` prints the row `live`.
  Red when: the walk reads past a `-` tip to an older sighting; the unit-35-order copy prints the row
  `stale`.
  figure: 60 s and 3600000 s are PINNED, the builder's probe of run `wf_5cc8df6e-de1`; the
  24-hour bound is DERIVED by `read_lease_bound expiry` at observation time.
- **AC2** — When the tip carries `renews: no`, sighted 60 s (PINNED) ago, over a `renews: -` commit sighted
  120 s (PINNED) ago, over a `renews: no` commit sighted 3600000 s (PINNED) ago, all of one epoch, `--claims` prints
  the row `live`.
  Red when: the walk reads past a `-` commit below the tip; the unit-35-order copy prints `stale`.
  figure: 60 s, 120 s and 3600000 s are PINNED literals of this rev.
- **AC3** — When four two-commit tenures, planted in turn, carry tips reading `renews: yes`, no
  `renews` key, `renews: -` and `renews: no`, each tip sighted 60 s (PINNED) ago over a `renews: no` commit of
  its epoch sighted 3600000 s (PINNED) ago, `--claims` prints them `live`, `live`, `live` and `stale`.
  Red when: a class of `renews` reaches a stop the walk does not name; the unit-35-order copy prints
  the `-` row `stale` and the other three as the pass does.
  figure: 60 s and 3600000 s are PINNED literals of this rev.
- **AC4** — When the tip carries `renews: no`, sighted 60 s (PINNED) ago, over an unsighted `renews: -`
  commit, over a `renews: no` commit sighted 3600000 s (PINNED) ago, all of one epoch, `--claims` prints the
  row `unknown` with age `-`.
  Red when: the walk reads past an unsighted `-` commit to an older sighting; the unit-35-order copy
  prints `stale`.
  figure: 60 s and 3600000 s are PINNED literals of this rev.
- **AC5** — When `grep -n 'renews' memory/guides/UNATTENDED-STOPS.md` runs, section 7's
  renewing-beat sentence names a `renews: -` commit as a stop of the walk, and
  `cmp tools/unattended/STOPS.template.md memory/guides/UNATTENDED-STOPS.md` exits 0.
  Red when: the guide still defines the walk's stops as `yes` or absent alone.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `unattended kit gate` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `scratch-guard self-test` · `tier2-review self-test` · `codebase-map coverage + freshness`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 AC4 · mixed chains, a `renews: -` commit above an older `renews: no` commit of its tenure, each read by the driver and by the unit-35-order copy, a scratch copy whose walk `awk` lacks the `-` stop and reads the `-` rows `stale` · waived for this build's landing by README rule 8, so its clean reading is owed with PLAY-dClosedLoop-14

## 8. Open questions

- **F1 — Where does a `renews: -` commit stop the walk?** (a) Its own stop after the epoch stop and
  before the threshold, resolving never-stale; (b) folded into the renewing beat; (c) no stop, as
  `TOOL-dPlacedRequest-35` reads. (c) is the defect. (b) reads the same verdicts on the tree, since
  the flag follows whichever commit stops the row (rev-6), and blurs the renewing beat's definition.
  RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the review's fix judged sound. widens: none ·
  relaxes: none
- **F2 — What does the `renews: -` stop repair, when the verdict pass already reads a `-` beat
  live?** (a) The mixed chain: a `-` commit above an older sighted `renews: no` commit of the same
  tenure, which reads stale today; (b) keep the old criteria and name a red copy that also drops the
  verdict pass's never-stale read; (c) retire the unit as WONTDO. RESOLVED (agent, 2026-11-20,
  delegated): (a), rung 3; it is the one input the stop changes, a renewal-policy change mid-tenure
  makes it real, and its red fires on the unit-35-order copy. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the spec audit of the round-2 promotions, finding
  32 (HIGH, item H2).
- rev-2 · 2026-10-25 · header above §1 · the round-3 promotions' fix brief: the `**Derived:** PLAY-dClosedLoop-2` line, binding this audit-promoted unit, which carries no clause, to the decision that derives it.
- rev-3 · 2026-10-25 · §3 · the disposal of the spec audit of the round-3 promotions: the hands-off edge to `TOOL-dPlacedRequest-52`, mirroring its consumes-from.
- rev-4 · 2026-11-19 · §7 · names `scratch-guard self-test` and `tier2-review self-test`, the legs the spec-token guard join names for `tools/unattended/unattended.sh` under this spec's Files touched; the round-1 fold of `2026-11-19-review-TOOL-dPlacedRequest-11-spec-audit` gave its siblings this repair and missed this spec.
- rev-5 · 2026-11-19 · §4 Files touched · §7 · folds
  `2026-11-19-review-TOOL-dPlacedRequest-1-spec-audit`: finding 17 (M8), this unit's own pass
  regenerates `memory/map/generated/`, named in Files touched, and §7 names its leg.
- rev-6 · 2026-11-20 · §1 · S1 · S3 · §3 · §4 · §5 · AC1 AC2 AC3 AC4 AC5 · §7 · §8 · §10 · folds
  `2026-11-20-prompt-TOOL-dPlacedRequest-46-divergence-brief` over the builder's divergence of run
  `wf_5cc8df6e-de1`: the defect is the mixed chain, a `-` commit above an older sighted `renews: no`
  commit of its tenure, since the verdict pass already reads a `-` stopping commit `live`; §1 and §4
  Evidence carry the builder's probe; AC1 to AC3 plant mixed chains red on the unit-35-order copy,
  AC4 the unsighted `-` commit; F2 records the ruling and F1's (b) rationale is corrected; S3 and AC5
  bring section 7 of the stops guide current with the stop, under the charter's `[docs]` rule; code
  is cited as `path#symbol` or blob pin.
- editorial · 2026-11-20 · §4 Evidence · AC1 AC2 AC3 AC4 · no rev bump, the status stays CLOSED:
  each line carrying the probe's ages of 60, 120 and 3600000 seconds marks every figure PINNED on
  that line, an inline red fix of the pinned-facts leg, per
  `2026-11-20-prompt-TOOL-dPlacedRequest-46-pass-red-fix-brief`.

## 10. Reuse audit

The seam extended is `TOOL-dPlacedRequest-35`'s stop order inside the walk `awk` of
`tools/unattended/unattended.sh#read_claims`; one stop is added and the one `awk` kept. `python
tools/codebase-map/reuse_lookup.py "a lease walk stop for a renewal policy that never expires"`
ranked `walk`, `load_policy`, `resolveLease` and `build_walk`, name stems only; `resolveLease`
resolves the run lease of the stop hook, not an age. `python tools/memory-recall/query.py "how does
the age walk treat a renews dash commit under renewal none"` returned scout A's row on
`TOOL-dPlacedRequest-17`, this audit's H2, `TOOL-dPlacedRequest-35` §4 and `TOOL-dPlacedRequest-26`;
none disagrees with source.

Recall terms used: renews dash leases.renewal none never stale age walk tenure renewing beat threshold expiry-hours
