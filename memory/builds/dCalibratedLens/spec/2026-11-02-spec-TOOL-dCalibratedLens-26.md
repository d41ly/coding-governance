# TOOL-dCalibratedLens-26 — a catch source that observed no run of a leg reads `-`, never 0, so no unobserved leg is proposed for retirement

**Status:** OPEN · rev-1 · 2026-11-02 · node a · Tier-2 · base 8bec4cef · streams tooling · order 2 · advances TOOL-dCalibratedLens-18

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-02-build-TOOL-dCalibratedLens-26-deviation-261.md](../build/2026-11-02-build-TOOL-dCalibratedLens-26-deviation-261.md) | deviation | — |
| [2026-11-02-prompt-TOOL-dCalibratedLens-19-promoted-fix-brief.md](../prompts/2026-11-02-prompt-TOOL-dCalibratedLens-19-promoted-fix-brief.md) | research | TOOL-dCalibratedLens-19 TOOL-dCalibratedLens-20 TOOL-dCalibratedLens-21 TOOL-dCalibratedLens-22 TOOL-dCalibratedLens-23 TOOL-dCalibratedLens-24 TOOL-dCalibratedLens-25 TOOL-dCalibratedLens-27 TOOL-dCalibratedLens-28 TOOL-dCalibratedLens-29 TOOL-dCalibratedLens-30 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 48, HIGH, item H8 of the round-1 spec audit
(`reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md`). Unit 2's §5 says "no
flake record: every leg's `catches` reads 0", an absent journal gives zero events, and S4 says nothing
of `runlog.py journal` exiting 2 or timing out; unit 5's `derive_retire_proposals` proposes `retire`
for every `idle` row whose `catches` is a number. This tree holds no flake record (`git ls-files
'memory/builds/*/build/*-flake-*.md'` prints nothing at base) and `verdict.flakes = retry-only` writes
none, so at the first review every leg not `new` would be proposed for retirement. Unit 2's own rule
that "`-` is an absence, never `0`" is broken by its leg kind. This unit makes a leg's catch columns a
count only when the source observed that leg run in the window, and proves both sides with plants. It
repairs `TOOL-dCalibratedLens-2`.

## 2. Scope (IN)

- **S1** — The design change, made at the audit's disposal in unit 2's text (rev-2, its §4
  "Amendments (round-1 spec audit)", id 48): `read_catch_events` answers, beside the events, the set of
  legs the source OBSERVED running in the window, and `derive_ledger_rows` writes `-` in a leg's three
  catch columns when the leg is outside that set. Under `verdict-records` a leg is observed when a
  tracked flake record whose `Ended` lies in the window carries a row for it (TOOL-dWitnessedBar-8 S3:
  one row per leg the run executed, green ones included). Under `node-journal` a leg is observed when the
  journal read succeeded, at least one GREEN or RED bar lies in the window, and the leg is one
  `build_leg_yield` marks `always_run` (`tools/runlog/runlog.py:90-140`: no guard, subject not `kit`,
  chunk not `selftests`) or one a windowed bar named red; an absent journal, an unreadable one (exit 2),
  a timeout or a missing runlog kit observes none. `price` prints one line, `NOTE: catch source <value>
  observed no run of <n> leg(s) · <why>`, when any leg reads `-`. Unit 2 §5's "every leg's `catches`
  reads 0" now reads `-`. Observed by AC1.
- **S2** — The proof, three `--fixture` plants in `tools/loop/loop_review.py`: `catch-none` (no flake
  record, `verdict-records`): every leg's `catches`, `false-reds` and `last-catch` read `-` and the
  `NOTE:` line names `0 flake record(s) in the window`; `catch-green` (one flake record in the window
  whose rows give `alpha` rc 0 and `beta` rc 1 then 1): `alpha` reads `catches` 0 and state `idle`,
  `beta` 1, and a leg with no row reads `-`; `catch-journal-dead` (`node-journal`, a `gates.log` the
  runlog reader refuses): every leg reads `-` and the `NOTE:` line names the refusal. Observed by AC2
  and AC3.
- **S3** — The consequence downstream, stated for unit 5 at the disposal (spec-5 rev-2, id 48): AC5
  also runs over `catch-none`, where `propose --dry-run` prints no `retire` proposal. Observed by AC4.

## 3. Non-goals (OUT)

- The retire rule itself: unit 5 S6 already proposes only for a numeric `catches`, which is correct
  once an unobserved leg reads `-`.
- A per-leg run count column. The ledger's row grammar keeps its nine columns; observation decides
  only between a count and `-`.
- Windowing the journal's per-leg counter: id 27 (`TOOL-dCalibratedLens-30`) moves S4's red count onto
  `build_leg_yield`, which this unit's `always_run` set already reads.

### Edges

- **consumes-from** `TOOL-dCalibratedLens-2` — `read_catch_events`, `derive_ledger_rows`, `price` and the `--fixture` frame; without them there are no catch columns to observe

## 4. Design

### Evidence

- spec-2 §5 "error / empty / loading states": "no flake record: every leg's `catches` reads 0"; §4 "The
  row": "`-` is an absence, never `0`".
- spec-5 S6: `derive_retire_proposals` takes "every ledger row whose state is `idle` and whose `catches`
  is a number".
- TOOL-dWitnessedBar-8 S3 and its §4 "The flake record": one TAB row per executed leg, so a green leg is
  named; S4: `retry-only` writes nothing.
- `tools/runlog/README.md` (the `--by-leg` paragraph) at base: the journal names failures, never the
  legs a bar ran, so `bars` is an upper bound for a guarded or held leg; `cmd_journal` returns 2 for an
  unreadable file and prints `absent` for a missing one.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `catch-none`, `catch-green`, `catch-journal-dead` | `--fixture` plant names | none |

### Files touched (estimate)

- `tools/loop/loop_review.py` — S2, the plants

### Alternatives rejected

- **`-` only when the source holds no record at all.** The skeptic's test: under `verdict-records` a
  leg that ran green all window is named in the flake records; reading every unnamed leg `-` is right,
  reading every leg `-` because one record exists elsewhere is not. Observation is per leg.
- **Counting a guarded leg's catches as 0 under `node-journal`.** The journal cannot say it ran, so a 0
  would be the defect this unit closes.

## 5. Production-readiness checklist

- security — no new surface; the reads are the ones S4 already makes.
- perf / scale — one set per price run, at most the manifest's legs.
- error / empty / loading states — every dead or empty source yields `-` and one `NOTE:` line.
- observability — the `NOTE:` line names the source and why.
- risks — a repository on `retry-only` never proposes a leg retirement; that is the honest reading of
  a source that records nothing.
- testing — the three plants.
- migration — N/A: no snapshot exists at base.
- user docs — `help/loop-review.md`'s value-ledger section (unit 2 S12) states the `-` rule.

## 6. Acceptance criteria

- **AC1** — When `grep -n 'observed no run' memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-2.md`
  runs, it prints the amendment, and `grep -c "every leg's .catches. reads 0"` over the same file
  prints 0.
  Red when: an unobserved leg still reads 0 in the design.
- **AC2** — When `python loop_review.py --fixture --plant catch-none` runs `price --dry-run`, every leg
  row's `catches` is `-` and one `NOTE:` line prints; `catch-green` prints `alpha` with `catches` 0 and
  `idle`, `beta` with 1, and an unnamed leg with `-`.
  Red when: an unobserved leg prints 0, or an observed green leg prints `-`.
- **AC3** — When the plant `catch-journal-dead` runs, every leg reads `-` and the `NOTE:` line names
  the runlog refusal.
  Red when: a dead journal prices as zero catches.
- **AC4** — When `grep -n 'catch-none' memory/builds/dCalibratedLens/spec/2026-11-02-spec-TOOL-dCalibratedLens-5.md`
  runs, it prints unit 5's amended AC5 line.
  Red when: unit 5's retire criterion never meets an unobserved leg.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

The loop kit's leg `loop-review selftest` (TOOL-dCalibratedLens-2 S11) is not in the manifest at base
and is named here in prose; it runs the plants once that unit lands.

New arm: tools/loop/loop_review.py · covers AC2 AC3 · the plants `catch-none`, `catch-green` and `catch-journal-dead`, staged red by a pricer that reads an unobserved leg as 0 · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-02 · initial draft, promoted from id 48 (HIGH, item H8) of the round-1 spec audit;
  units 2 and 5 amended at the disposal (their rev-2).

## 10. Reuse audit

The seam extended is `build_leg_yield`'s `always_run` rule (`tools/runlog/runlog.py:90-140`, read at
base), which already says which legs every bar ran, and TOOL-dWitnessedBar-8's flake record, whose rows
name every executed leg. `python tools/codebase-map/reuse_lookup.py "isolate each reader so one failure
becomes an unread line, never the walk's exit"`, run once for the set, ranked `read_journal`
(`tools/runlog/runlog_lib.py`) among its name stems, the reader `cmd_journal` wraps; no seam computes
per-leg observation, so the set is new over those two. The recall probe returned
TOOL-cMendedVintage-19, the placement ruling this unit's order follows.

Recall terms used: `python tools/memory-recall/query.py "how is a spec audit finding promoted to a
repair unit placed after the unit it repairs" --terms "spec audit promoted repair unit order hands-off
consumes-from minors batch loop review record kind"`
