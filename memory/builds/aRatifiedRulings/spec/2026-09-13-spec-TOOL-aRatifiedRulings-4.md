# TOOL-aRatifiedRulings-4 — a leg killed with no ceiling in play names the seconds it ran

**Status:** SPECCED · rev-1 · 2026-09-13 · node a · Tier-1 · base 16da4c6a · streams tooling · ratified 2026-09-13

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-review-TOOL-aRatifiedRulings-1-round1.md](../reviews/2026-09-13-review-TOOL-aRatifiedRulings-1-round1.md) | spec-audit | TOOL-aRatifiedRulings-1 TOOL-aRatifiedRulings-2 TOOL-aRatifiedRulings-3 |

<!-- /gen:spec-records -->

## 1. Goal

Build the branch `TOOL-aLeakedHandle-9` rules on: in `report_one` of `tools/run-gates/run-gates.sh`,
an rc=137 leg whose recorded bound is 0 prints `(killed after <secs>s)` — the elapsed value the
runner already wrote to `$WORK/<i>.sec` and the ledger already reads as field 2 — instead of the bare
`(exit 137)` it prints today. The ruling is the mandate and is not restated here; the park that
motivated it and the options the owner saw are `memory/builds/aLeakedHandle/RUN.md`, and the backlog
row that carried it is `TOOL-aLeakedHandle-5`.

## 2. Scope (IN)

- **S1** — One guarded assignment added to the failing branch of `report_one`, keyed on
  `rc = 137` AND the recorded bound NOT greater than 0, producing `(killed after ${secs:-?}s)` with
  no ceiling clause. `secs` is the value the sibling branch already reads from `$WORK/<i>.sec`; no
  new read, no new file. Observed by AC1, AC2 and AC3.
- **S2** — The source comment beside that branch, which today says both mapped codes "stay behind
  the PROF_TIMEOUT guard", is amended so that it is true of 124 alone. NOT OBSERVED — it is comment
  prose, and an arm asserting a comment grades the comment rather than the branch.
- **S3** — `tools/run-gates/run-gates.test.sh` gains one arm that drives the real runner over the
  existing `selfkill.sh` fixture under the existing `tbl-loose` profile with the `ceiling` key
  DROPPED from the manifest row, and asserts the tail's shape and its value against the ledger. It
  sits OUTSIDE the suite's `HAVE_TIMEOUT` guard, its assertions are counted beside it, and
  `FLOOR_ASSERTIONS` rises by the number of increments the arm adds. Observed by AC1, AC2, AC4 and
  AC5.
- **S4** — `tools/run-gates/README.md` gains one clause, in the paragraph that already documents
  the `(killed after Ns, ceiling Ms)` tail, naming the no-ceiling form. NOT OBSERVED — no gate
  reads that paragraph, for the reason S2 gives.

## 3. Non-goals (OUT)

- **rc=124 with no bound in play keeps `(exit 124)`.** `timeout` never ran on that path, so a 124
  there is the leg's own exit code and the runner has nothing truer to say about it. The 124 branch
  and its two pinning arms are untouched.
- **The tail does not distinguish a ceiling that was DECLARED BUT INERT from one never declared.**
  `runleg` writes 0 to `$WORK/<i>.bound` in both cases, because `CEILINGS_LIVE=0` sets `bound=0`
  before the write, and the profile line already prints `ceilings INERT` for the whole run. The tail
  states what bound was IN PLAY, which was none, and that is true in both cases. Re-reading the
  manifest's declaration inside `report_one` to tell them apart would be a second source for a fact
  `.bound` already records, and is refused in §4.
- **No verdict moves.** A killed leg is RED before and after. Nothing here turns a leg green,
  skipped, held or reused.
- **The ledger is not touched, and no ceiling is declared, removed or re-declared** in
  `tools/gate-legs.json`. In particular no real leg is stripped of its ceiling to observe this branch
  live; §4 says why the observation is fixture-only and what that costs.
- **No new leg, no new identifier.** The arm joins the existing `run-gates canary` suite, so no
  gate-legs inventory key, no `memory/map` claim, no subject-pins row and no budget row are owed.

### Edges

- **consumes-from** external — the `$WORK/<i>.bound` and `$WORK/<i>.sec` writes in `runleg`, both
  made before the `$WORK/<i>.rc` completion signal, and the sibling branch `TOOL-aLeakedHandle-3`
  landed, which already reads both. If `.bound` stops being written as a number, the new predicate
  reads 0 through `${fired:-0}` and the tail says `killed after` for a leg that may have had a bound;
  if `.sec` stops being written, the tail degrades to `?` rather than to a wrong number.

## 4. Design

### The site

`tools/run-gates/run-gates.sh`, in `report_one`, at base `16da4c6a` (`run-gates.sh:1477` to
`run-gates.sh:1493`, comments elided):

```bash
local fired; fired=$(cat "$WORK/$i.bound" 2>/dev/null || printf 0)
local secs; secs=$(cat "$WORK/$i.sec" 2>/dev/null) || secs=""
ftail="(exit $rc)"
{ [ "$rc" = 124 ] && [ "${fired:-0}" -gt 0 ]; } && ftail="(timed out after ${fired}s)"
{ [ "$rc" = 137 ] && [ "${fired:-0}" -gt 0 ]; } && ftail="(killed after ${secs:-?}s, ceiling ${fired}s)"
```

`fired` is whatever `runleg` wrote to `$WORK/<i>.bound` at `run-gates.sh:1394`: the leg's declared
ceiling, else `PROF_TIMEOUT`, else 0 — and 0 unconditionally when `CEILINGS_LIVE` is not 1. An
rc=137 with `fired` at 0 therefore falls through both guarded lines and keeps `(exit $rc)`. That is
the whole defect: `secs` is already read on this path and already correct, and nothing prints it.

### The replacement

One line, added directly beneath the ceiling-present line:

```bash
{ [ "$rc" = 137 ] && ! [ "${fired:-0}" -gt 0 ]; } && ftail="(killed after ${secs:-?}s)"
```

The predicate is the sibling's guard NEGATED rather than a fresh `-eq 0`, so the two lines PARTITION
rc=137: every value of `fired` satisfies exactly one of them, and nothing can fall between. The
sibling line stays byte-identical, which keeps the arm that pins it unmoved. `${secs:-?}` is the same
degraded form the sibling uses, for the same reason: a `?` says the runner does not know, where any
numeric fallback is a second wrong answer. The seconds are printed VERBATIM from `.sec`, decimals
and all, because byte-equality with the ledger row is the property the parent unit restored and
this branch inherits it.

The source comment at `run-gates.sh:1471`, which says both codes "stay behind the PROF_TIMEOUT
guard, so a leg that chooses either for its own reasons is still reported as the code it chose", becomes false
for 137 and is amended in the same hunk. A leg that exits 137 by its own choice is indistinguishable
from one killed, because bash itself reports 128+9 for a SIGKILLed child, so there is no separate
"chose 137" case for a guard to protect.

Measured on 2026-09-13 at base `16da4c6a`, in a scratch repo under `TEMP` holding a copy of the
runner, the `selfkill.sh` fixture and a manifest row with no `ceiling` key, under a profile row
declaring `timeout=0`: the unpatched runner printed `GATE FAIL  selfkilled  (exit 137)` while
`gate-ledger.tsv` recorded `selfkilled` at `2.142`; with the one line above added, two sequential
runs printed `(killed after 2.889s)` and `(killed after 2.343s)` against ledger rows of `2.889` and
`2.343`, byte-equal both times. No `timeout` process was involved on either run: with `bound` at 0
`runleg` execs the leg directly, which is why the arm below can live outside the `HAVE_TIMEOUT`
guard.

### The gate arm, and the class it cannot escape

The arm lives in `tools/run-gates/run-gates.test.sh`, in the section-4 scratch repo `$P`, placed
AFTER the `fi` that closes the `HAVE_TIMEOUT` guard around arms 4h and 4h-kill and before the
manifest reset that follows it. It rewrites `$P/tools/gate-legs.json` to the 4h-kill row with its
`"ceiling": 600` REMOVED and nothing else changed, runs `runp GATE_PROFILES=fx/tbl-loose.txt`, and
asserts three things, each counted:

1. The run reports a line beginning `GATE FAIL  selfkilled  `, so the leg ran, was killed and was
   NAMED. This is the positive artifact: an arm whose fixture never executed has no such line and
   fails here, never passes on an empty capture.
2. The seconds extracted from that tail equal field 2 of the `selfkilled` row in
   `$P/.git/gate-ledger.tsv`, both non-empty, compared as strings so a rounded tail reds. An empty
   extraction or an absent row fails with a message saying the arm could not measure — the liveness
   half sits inside the same assertion, exactly as 4h-kill's does. This asserts the VALUE, not the
   presence of a row.
3. The whole line matches `^GATE FAIL  selfkilled  [(]killed after [0-9][0-9.]*s[)]$` — no
   `ceiling` clause, no `exit 137`, no `timed out`. Assertion 2 alone would pass a tail that printed
   the right seconds and then claimed a ceiling of 0.

It restores the manifest it found, so the arms after it read the row set they expect.

**The failing case is observable only against a fixture that strips the ceiling, and the spec says
so rather than leaving the next session to discover it.** Every leg in `tools/gate-legs.json`
declares a `ceiling` today — the manifest owns that count and this spec does not restate it; derive
it with `python -c "import json;l=json.load(open('tools/gate-legs.json'));print(len(l),sum('ceiling' in x for x in l))"` —
so the population this branch serves is EMPTY and no run of the real bar can reach it. The class
that describes an arm proving a mechanism against a simpler stand-in for the shipped value is
`memory/gotchas/staged-break-substitutes-a-synthetic-value.md`, and the ruling accepted the arm with
that class named. Three things keep the arm inside that gotcha's own remedy rather than its
symptom. First, there is no shipped value to substitute: the branch's whole input is "no bound in
play", and the only way to produce that input is a row without the key. Second, the fixture alters
ONE field of the real record the sibling arm already drives — the same `selfkill.sh`, the same
`tbl-loose` profile, the same runner, the same ledger read — and the property removed is the
ceiling, which is the branch's predicate and not a stand-in for it. Third, the staged RED is a
mutation of the SUBJECT: the arm is run against the runner at base before the line lands and after
the line is reverted, and the break it observes is the code's, not the constant's. What the arm
still cannot show is the branch firing on a leg an operator or an OOM killer actually killed while
running unbounded on a real bar; that observation waits on a leg shipping without a ceiling, and
the row that carried this fork was written so it stays findable if one ever does.

The arm sits OUTSIDE `HAVE_TIMEOUT` because the branch it grades is the one path that needs no
`timeout`. On a host with a runnable `timeout`, `bound` is 0 because no ceiling and no profile
timeout were declared; on a host without one, `CEILINGS_LIVE=0` sets `bound` to 0 anyway. Both
reach the same branch with the same fixture, so the arm executes on every host and its increments
are counted beside it with no skip. That is the opposite of 4h-kill, which reads a tail the runner
only builds under a live bound and skips with its sibling; the two arms are deliberately placed on
opposite sides of the same `fi`.

### Inventory

This unit mints no identifier, no file, no leg, no conf key and no naming cell. The arm is one more
block in an existing suite under an existing leg name.

### Files touched (estimate)

| File | Change |
|---|---|
| `tools/run-gates/run-gates.sh` | one guarded assignment added in `report_one`; one comment clause amended |
| `tools/run-gates/run-gates.test.sh` | one arm of about fifteen lines outside the `HAVE_TIMEOUT` guard; three `n=$((n+1))` beside it; `FLOOR_ASSERTIONS` raised by three |
| `tools/run-gates/README.md` | one clause in the existing killed-tail paragraph |

`FLOOR_ASSERTIONS` is a literal at `run-gates.test.sh:48`; its value is read from the file at build
time and is DERIVED here, not pinned. It rises by exactly the number of `n=$((n+1))` lines the arm
adds, unless a sibling unit lands increments into the same file first, in which case the suite's own
closing `PASS (<n> assertions)` line is the figure to set it from.

### Alternatives rejected

- **Restructure the two 137 lines into one `if/else`.** Equivalent, and it rewrites the sibling
  line the 4h-kill arm and the kill-after arm both pin. One added line keeps that line byte-identical
  and the diff smaller.
- **Print `(killed after Ns, ceiling none)` or `(killed after Ns, unbounded)`.** The absence of the
  clause IS the information, the README would then document three tail shapes instead of two, and
  `unbounded` is the word the runner's own stderr count already uses for a different population — the
  legs that DECLARED nothing — which the inert case is not in.
- **Tell a declared-but-inert ceiling from an undeclared one** by reading `${ceilings[$i]}` in
  `report_one`. A second source for a fact `.bound` already records, and the profile line already
  says `ceilings INERT` once per run where it belongs.
- **Strip one real leg's ceiling to observe the branch on the bar.** That removes a declaration
  from the merge bar to test a message, which is the `fixture-removes-the-path-under-test` shape
  aimed at the manifest instead of a fixture, and `derive-ceilings.py --check` reds any leg that
  has an evidence row and no ceiling, naming it as "no ceiling declared" — verified against
  `derive-ceilings.py:438` on 2026-09-13.
- **Place the arm inside the `HAVE_TIMEOUT` guard beside 4h-kill**, for symmetry. It would skip
  on exactly the host where the branch is MOST reachable, since an absent `timeout` makes every leg
  run unbounded.

## 5. Production-readiness checklist

- security — N/A. The tail carries a leg name and a duration the runner computed. No leg output
  reaches it and the `redact` path is untouched.
- perf / scale — one `[` test on the FAILING path only, reading a variable already in hand. The
  green path and the pool are untouched.
- error / empty / loading states — the only degraded state is an unreadable `.sec`, which renders
  `?` as the sibling branch does. Reachable only if `runleg` failed to write it.
- observability — the point of the unit. A leg killed with no bound in play names how long it ran
  in the summary, so the operator does not open the ledger to learn it.
- risks — the tail's bytes change for one branch that today prints `(exit 137)`. Nothing outside
  the suite parses the tail's contents; consumers split a verdict line on the double space and read
  the verb and the leg name.
- testing — one new arm in `tools/run-gates/run-gates.test.sh`, its failing case staged and observed
  RED against the unpatched runner, on a fixture the spec names as the only observation available.
- migration — N/A. No stored file, manifest key or record format changes.
- user docs — one clause in `tools/run-gates/README.md`; the existing sentences stay true.

## 6. Acceptance criteria

- **AC1** — When `bash tools/run-gates/run-gates.test.sh` runs, the new arm drives the `selfkilled`
  fixture leg with NO `ceiling` key under the suite's `tbl-loose` profile, and the run's
  `GATE FAIL  selfkilled` line matches `^GATE FAIL  selfkilled  [(]killed after [0-9][0-9.]*s[)]$`
  exactly — no ceiling clause, no `exit 137`, no `timed out`.
  Red when: the tail reads `(exit 137)`, which is what the runner at base `16da4c6a` prints for this
  fixture, measured on 2026-09-13 outside the suite.
  cost: the whole `run-gates canary` suite, not seconds. That leg sits in chunk `selftests`, is held
  on every boundary bar, and no boundary sets `GATE_SELFTESTS=1`; observe it by running the file
  directly, or through `bash tools/run-gates/run-selftests.sh --kit tools/run-gates` for the
  budgeted verdict.
  fixture: the suite's own scratch repo and its existing `selfkill.sh` fixture, with the `ceiling`
  key dropped from the manifest row. That drop is the only observation available and is the class
  `memory/gotchas/staged-break-substitutes-a-synthetic-value.md` names; §4 states why the arm stays
  inside that gotcha's remedy.
- **AC2** — When the same run reports that leg, the seconds in its tail equal field 2 of the
  `selfkilled` row in the scratch repo's `gate-ledger.tsv`, byte for byte, both non-empty; an empty
  extraction or an absent row fails the arm with a could-not-measure message rather than passing on
  two empty strings.
  Red when: the branch prints a rounded, truncated or re-derived number, or the arm's extraction
  matches nothing and the comparison is skipped.
  figure: the seconds are DERIVED at observation time from the ledger row; no literal is pinned.
- **AC3** — When the same suite reaches the arms already on either side of the guard, the
  `stubborn` kill-after arm still accepts `ceiling 3s` when KILL wins, the 4h-kill arm still
  observes `ceiling 600s` for `selfkilled` under its declared ceiling, and the two rc=124 arms still
  observe `timed out after` with their ceilings.
  Red when: the new predicate overlaps the ceiling-present one — keyed on `rc` alone, say — so a
  kill under a live bound loses its ceiling clause, or the change widened into the 124 branch.
  permission: the `stubborn` and 4h-kill halves execute only on a host with a runnable `timeout`;
  this host has one, measured by the suite's own `HAVE_TIMEOUT` probe.
- **AC4** — When the one added line in `tools/run-gates/run-gates.sh` is reverted and
  `bash tools/run-gates/run-gates.test.sh` is run again, the new arm FAILS, quoting the `(exit 137)`
  tail it got; restoring the line makes the same suite pass.
  Red when: the arm passes against the unfixed source, which would mean it asserts something the
  defect already satisfies — the `fixture-passes-by-finding-nothing` class the suite's arm 1c header
  names.
- **AC5** — When the suite finishes on this host, its closing `PASS (<n> assertions)` line reports
  an `<n>` at or above the raised `FLOOR_ASSERTIONS` in `tools/run-gates/run-gates.test.sh`, and the
  arm's three increments sit outside the `HAVE_TIMEOUT` guard beside the arm itself.
  Red when: the arm or its increments are placed inside the guard, so a host with no runnable
  `timeout` skips an arm whose branch it can reach, or executes three fewer than the raised floor
  and reds a correct suite.
  permission: the timeout-less half of that Red-when cannot be observed by this run, because no such
  host is reachable from here. The placement is verified by reading the source on both sides of the
  guard's closing `fi`.

## 7. Gates

`run-gates canary` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

Each leg's chunk and guard, read from `tools/gate-legs.json` on 2026-09-13: `run-gates canary` is
chunk `selftests` with guard `tools/`, `tools/gate-legs.json` and `tools/lib/`, so it is HELD on
every boundary bar and no boundary sets `GATE_SELFTESTS=1` — AC1 through AC5 all ride it and are
observed by the direct invocation AC1 names. `memory hygiene` is chunk `records` with no guard, and
grades this file. `spec tokens (a spec's own names resolve)` is chunk `declarations` with no guard,
and joins this section's leg line and §6's paths against the tree.

New arm: `tools/run-gates/run-gates.test.sh` · the 4h-kill manifest row with its `ceiling` key
removed under the `tbl-loose` profile, so `runleg` execs `selfkill.sh` directly with `bound` at 0
and the unpatched runner prints `(exit 137)` against a ledger row of about 2 s · `FLOOR_ASSERTIONS`
rises by the arm's three increments, from whatever `run-gates.test.sh:48` reads at build time.

## 8. Open questions

- **F1 of the parent unit — should an rc=137 leg that declared NO ceiling also report its
  seconds?** Argued in `memory/builds/aLeakedHandle/spec/2026-09-10-spec-TOOL-aLeakedHandle-3.md`
  §8, cut from that unit by its §3, carried as `TOOL-aLeakedHandle-5`, and not re-argued here.
  RESOLVED (owner, 2026-09-13): build it — `TOOL-aLeakedHandle-9`, with the fixture-only red case
  accepted as stated. This spec is the work that ruling mandates and opens no further fork.

## 9. Revision log

- rev-1 · 2026-09-13 · initial draft.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "killed leg with no declared ceiling reports elapsed
seconds in the run-gates failure tail"`, run on 2026-09-13 at base `16da4c6a`, reported
`scan coverage: 70 files scanned | 0 parse skips | unscanned layers: .sh`. Every file this unit
touches is `.sh`, so the map probe is BLIND to this subject and no claim in this spec rests on it;
its ranked candidates are Python `run` and `report` symbols from other kits and none is this seam.

The seam was found by reading the source, and it exists: `report_one` already reads `$WORK/<i>.bound`
into `fired` and `$WORK/<i>.sec` into `secs` on the failing path, both landed by
`TOOL-aLeakedHandle-3`, and this unit adds one guarded assignment over those two values and mints
nothing. On the test side the seam is the suite's existing `selfkill.sh` fixture, its `tbl-loose`
profile row, the `runp` helper and the inline `awk` over `$P/.git/gate-ledger.tsv` that the 4h-kill
arm already drives; the new arm reuses all four and adds no fixture.

Recall terms used: `python tools/memory-recall/query.py "why does a killed leg with no declared
ceiling print a bare exit 137 in the run-gates failure tail" --terms run-gates report_one rc 137
killed ceiling unbounded ledger elapsed secs tail sigkill`, run 2026-09-13; its first hit is
`TOOL-aLeakedHandle-5` and its fourth is the parent unit's spec, which is the record set this unit
builds from.
