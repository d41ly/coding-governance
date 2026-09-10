# TOOL-aLeakedHandle-3 — a killed leg reports the seconds it ran, not the ceiling it did not reach

**Status:** CLOSED · rev-2 · 2026-09-10 · node a · Tier-1 · base 013b1af9 · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-10-build-TOOL-aLeakedHandle-1-1-root-cause-trace.md](../build/2026-09-10-build-TOOL-aLeakedHandle-1-1-root-cause-trace.md) | research | TOOL-aLeakedHandle-1 TOOL-aLeakedHandle-2 |
| [2026-09-10-build-TOOL-aLeakedHandle-3-1-acceptance-ledger.md](../build/2026-09-10-build-TOOL-aLeakedHandle-3-1-acceptance-ledger.md) | journal | — |
| [2026-09-10-prompt-TOOL-aLeakedHandle-3-1-build-brief.md](../prompts/2026-09-10-prompt-TOOL-aLeakedHandle-3-1-build-brief.md) | journal | — |
| [2026-09-10-review-TOOL-aLeakedHandle-1-spec-audit.md](../reviews/2026-09-10-review-TOOL-aLeakedHandle-1-spec-audit.md) | spec-audit | TOOL-aLeakedHandle-1 TOOL-aLeakedHandle-2 |

<!-- /gen:spec-records -->

## 1. Goal

`report_one` in `tools/run-gates/run-gates.sh` renders an rc=137 leg as `(timed out after ${fired}s,
killed)`, where `fired` is the leg's DECLARED CEILING rather than the time it ran. On the bar of
2026-09-10 a leg killed at 4168.392 s was reported as `(timed out after 16040s, killed)`, while
`<git-dir>/gate-ledger.tsv` recorded 4168.392 for the same leg on the same run. The summary and the
ledger disagreed by a factor of four, and a wrong number entering diagnosis is how
`TOOL-dRetiredFork-40` was misread in both directions. This unit makes the failure line print the
elapsed value the runner has already computed, and adds the arm that keeps it honest.

## 2. Scope (IN)

- **S1** — The rc=137 branch of `report_one` prints the elapsed seconds the worker measured, read
  from the `$WORK/<i>.sec` file `runleg` already writes, and names the declared ceiling as a
  separate, labelled field rather than passing it off as the elapsed time. The verb `timed out`
  leaves that branch, because rc=137 is SIGKILL and an operator, an OOM killer or a CI cancel
  produces it as readily as `timeout -k` does. Observed by AC1 and AC2.
- **S2** — The rc=124 branch is left exactly as it is, and the reason is written into the source
  beside it so the asymmetry reads as a decision rather than an oversight. Observed by AC3.
- **S3** — `tools/run-gates/run-gates.test.sh` gains one arm that drives the real runner over a
  fixture leg killed by SIGKILL under a large declared ceiling, and asserts that the seconds in the
  `GATE FAIL` tail equal that leg's `gate-ledger.tsv` field 2. Its three assertions are counted on
  both branches of the suite's `HAVE_TIMEOUT` guard and `FLOOR_ASSERTIONS` rises by three.
  Observed by AC1, AC4 and AC5.
- **S4** — `tools/run-gates/README.md` gains one clause naming the killed tail beside the sentence
  that already documents the timed-out one. NOT OBSERVED — no gate reads that file's prose about
  the tail, and an arm asserting a documentation sentence would grade the sentence rather than the
  behaviour it describes.

## 3. Non-goals (OUT)

- **The summary format is not redesigned.** One branch's tail string changes. The verb column, the
  two-space tail contract, the indented leg output and the durable `FAILED_LEGS` summary are all
  untouched, and every consumer that splits a verdict line on the double space keeps working.
- **No verdict moves.** A killed leg was RED before this unit and is RED after it. Nothing here can
  turn a leg green, skipped, held or reused.
- **The ledger is not touched.** `<git-dir>/gate-ledger.tsv` already holds the correct figure. The
  defect is that the summary disagrees with it, so the summary is what changes.
- **No ceiling is re-declared.** The 16040 s ceiling that produced the misprint stays exactly where
  it is; that question is `TOOL-aLeakedHandle-2`'s and the owner's.
- **An rc=137 leg that declared NO ceiling keeps its `(exit 137)` tail.** That leg states no number
  at all, so it is outside the class this unit closes, which is a tail whose number disagrees with
  the ledger row for the same leg. Widening it would add a message where none existed rather than
  correct one that lies. Carried as the open fork in section 8.

### Edges

- **hands-off** `TOOL-aLeakedHandle-2` — every ceiling VALUE, including the 16040 s one this unit
  stops misprinting. This unit corrects what the report says and re-declares no number, so unit 2's
  evidence rule lands on an unchanged `.leg` row shape and an unchanged `derive-ceilings.py`.
- **consumes-from** external — the per-leg elapsed value `runleg` writes to `$WORK/<i>.sec` before
  it writes `$WORK/<i>.rc`. If a future change stops writing it, or writes it after the completion
  signal, the tail degrades to a `?` rather than to a wrong number.

## 4. Design

### The site

`tools/run-gates/run-gates.sh`, in `report_one`, at base `013b1af9`:

```bash
local fired; fired=$(cat "$WORK/$i.bound" 2>/dev/null || printf 0)
ftail="(exit $rc)"
{ [ "$rc" = 124 ] && [ "${fired:-0}" -gt 0 ]; } && ftail="(timed out after ${fired}s)"
{ [ "$rc" = 137 ] && [ "${fired:-0}" -gt 0 ]; } && ftail="(timed out after ${fired}s, killed)"
```

`fired` is read from `$WORK/<i>.bound`, which `runleg` writes as the bound it passed to `timeout`.
It is the ceiling, and on the 124 path it is also, within scheduling overhead, the elapsed time. On
the 137 path it is neither.

### The value to print, and why no new plumbing is needed

`runleg` already computes each leg's own duration from two `date +%s%N` readings and writes it to
`$WORK/<i>.sec`, at `run-gates.sh:1409`. The ledger block at `run-gates.sh:1682` reads that same
file as field 2 of every row. So the number the ledger carries and the number the summary should
carry are one value in one file, and this unit adds a third reader rather than a second source.

The write order is what makes the read safe. `runleg` writes `.sec` before it writes `.rc`, and
`report_one` reaches the failing branch only for a leg whose `.rc` holds a numeric code, which only
`runleg` writes. A leg decided by a guard, a reuse or an on-demand hold never enters `runleg` and
never reaches this branch.

The whole-run wall guard is safe for a DIFFERENT reason, and rev-1 of this paragraph stated the
mechanism backwards. `runleg` writes its own `$BASHPID` to `$WORK/<i>.pid` at `run-gates.sh:1367`,
the watcher hands that pid to `run_leg_reap`, and `scan_descendants` seeds its result set with the
root pid itself at `run-gates.sh:429` — so `remove_descendants` SIGKILLs the `runleg` subshell along
with its children. A wall-killed leg writes neither `.sec` nor `.rc`, and `report_one` returns at its
`[ ! -f "$WORK/$i.rc" ]` guard at `run-gates.sh:1449` with `(no result)`, before any tail is built.
The read this unit adds is safe on that path because the rc=137 branch is UNREACHABLE there, not
because the file is present. `TOOL-aLeakedHandle-1` AC2's third `Red when:` states the same
mechanism from the ledger side, where the absent `.sec` makes the ledger loop skip the leg and carry
its previous row forward; the pair agrees once that spec keeps its clause as written. Verified
against source on 2026-09-10 at base `013b1af9`.

### The replacement

```bash
local secs; secs=$(cat "$WORK/$i.sec" 2>/dev/null) || secs=""
{ [ "$rc" = 124 ] && [ "${fired:-0}" -gt 0 ]; } && ftail="(timed out after ${fired}s)"
{ [ "$rc" = 137 ] && [ "${fired:-0}" -gt 0 ]; } && ftail="(killed after ${secs:-?}s, ceiling ${fired}s)"
```

Three properties, each deliberate. The seconds are printed VERBATIM from `.sec`, decimal places and
all, because byte-equality with the ledger row is the property this unit exists to restore and
rounding reopens the disagreement at one decimal place instead of four digits. The ceiling stays on
the line, labelled, because a reader diagnosing a kill wants to know whether the leg was anywhere
near its bound. And `${secs:-?}` is the degraded form for the case where `.sec` is unreadable: a `?`
says the runner does not know, where any numeric fallback would be a second wrong number.

### Why rc=124 keeps printing the ceiling

Both figures are defensible for 124 and the ceiling is the better one. rc=124 means `timeout` fired
its own TERM, so the ceiling is the CAUSE of the verdict and is true by construction; the elapsed
value on that path is the ceiling plus kill-path and scheduling overhead, measured by the suite's
own comment at 12 s against a 2 s bound under heavy load. Printing 12 where the operator declared 2
would make the reader hunt for a bound that does not exist. Two live arms also pin the ceiling
there, at `run-gates.test.sh:225` and `run-gates.test.sh:1133`, and both stay green — which is what
makes them this unit's control rather than a cost. A leg whose own command chooses 124 while a
ceiling is declared is misreported by this branch, and that is a separate defect nobody has
observed; it is not opened here.

### The gate arm

The class is a failure tail whose number disagrees with the ledger row for the same leg. The arm
grades that class rather than the rc=137 instance: it extracts whatever seconds the tail states and
compares them with field 2 of the ledger, so any future branch that invents a number reds it too.

It lives beside arm 4h in `tools/run-gates/run-gates.test.sh`, inside the existing `HAVE_TIMEOUT`
guard and in the existing scratch repo `$P`. A new fixture `$P/fx/selfkill.sh` sleeps and then runs
`kill -9 $$`; the manifest row declares `"ceiling": 600` against it. `timeout` returns 128+9 for a
command killed by a signal, so the runner sees rc=137 from a kill it did not order — the operator
case, staged without an operator, deterministically, in about two seconds. Against the source at
base `013b1af9` the tail says `600` and the ledger says `2.0xx`.

Three assertions, each counted:

1. The run reports a `GATE FAIL  selfkilled` line, so the leg was killed and NAMED.
2. The seconds in that tail equal field 2 of the `selfkilled` row in `$P/.git/gate-ledger.tsv`,
   both non-empty. The liveness half is inside the same assertion: an absent ledger row or a tail
   the extraction did not match fails with a message saying the arm could not measure, never with a
   quiet pass.
3. The tail does not contain `timed out`, because the ceiling did not fire.

The comparison is exact and inlines its own `awk` over the ledger rather than calling the file's
existing `leg_secs` helper, which truncates to an integer by design for the two magnitude arms that
use it. A truncated compare would pass on a tail that rounded, which is half the defect.

The three `n=$((n+1))` increments sit OUTSIDE the `HAVE_TIMEOUT` branch, and the skip announces
itself in the `else` arm, exactly as arm 4h does. The suite's floor is a count of EXECUTED
assertions, so counting inside the guard would drop the executed total by three on a host with no
runnable `timeout` and red a correct suite there.

The existing arm at `run-gates.test.sh:1156` accepts `(timed out after 3s, killed)` for the
kill-after escalation and MOVES with this change. That path is a genuine ceiling-fired 137, and the
new tail is more honest about it too: the leg ran the bound plus the five-second kill-after, so the
old line's `3s` was already wrong by 5 s. The moved assertion accepts either signal winning, as it
does today — `(timed out after 3s)` when TERM wins, `(killed after <n>s, ceiling 3s)` when KILL
does — because which one wins is the host's business.

### Files touched (estimate)

| File | Change |
|---|---|
| `tools/run-gates/run-gates.sh` | one line rewritten, one local read added, a short comment naming the 124 asymmetry |
| `tools/run-gates/run-gates.test.sh` | one fixture, one arm of about twenty lines, the `run-gates.test.sh:1156` assertion moved, `FLOOR_ASSERTIONS` raised by three |
| `tools/run-gates/README.md` | one clause on the existing ceiling sentence |

`FLOOR_ASSERTIONS` reads 143 at base `013b1af9`, PINNED by reading `run-gates.test.sh:48` on
2026-09-10. It becomes 146 unless a sibling unit lands assertions into the same file first, in which
case it is DERIVED from the suite's own executed count.

### Alternatives rejected

- **Keep the verb and swap only the number**, giving `(timed out after 4168.392s, killed)`. It costs
  the same bytes and still asserts a timeout that did not happen. The root-cause trace is explicit
  that rc=137 does not mean the ceiling fired.
- **Round the elapsed seconds to whole numbers** for a tidier line. It breaks byte-equality with the
  ledger, which is the only property the new arm can assert cheaply and exactly.
- **Report elapsed on the 124 branch too**, for symmetry. Argued above and refused: the ceiling is
  the true cause there, and two live arms pin it.
- **Recompute elapsed in `report_one`** from the `.leg` row's start and end stamps. A second
  derivation of a value that already sits in a file is the two-stores-of-one-fact shape the ledger
  block's own header rejects.

## 5. Production-readiness checklist

- security — N/A. The tail carries a leg name, an integer the manifest declared and a duration the
  runner computed. No leg output reaches it, so the `redact` path is untouched.
- perf / scale — one `cat` of a file already on disk, on the FAILING path only. The green path and
  the pool are untouched.
- error / empty / loading states — the only degraded state is an unreadable `.sec`, which renders
  `?` rather than a fallback number. Named in section 4 and reachable only if `runleg` failed to
  write it.
- observability — the point of the unit. After it, the summary and the ledger read one value from
  one file, so a killed leg cannot be diagnosed against two different numbers.
- risks — the tail's bytes change for one branch. Nothing outside this suite parses the tail:
  `tools/govkit/` and the deployer read the verb and the leg name by splitting on the double space,
  and the only readers of the tail's contents are the two arms named in section 4.
- testing — one new arm plus the one moved assertion, both in `tools/run-gates/run-gates.test.sh`,
  with the failing case staged and observed RED before landing.
- migration — N/A. No stored file, manifest key or record format changes.
- user docs — one clause in `tools/run-gates/README.md`. Its existing sentence documents the 124
  tail and stays true.

## 6. Acceptance criteria

- **AC1** — When `bash tools/run-gates/run-gates.test.sh` runs on a host with a working `timeout`,
  the new arm drives a fixture leg that SIGKILLs itself under a declared ceiling of 600, and the
  seconds in its `GATE FAIL  selfkilled` tail equal field 2 of that leg's row in
  `$P/.git/gate-ledger.tsv`, byte for byte.
  Red when: the tail states the ceiling (`600`) where the elapsed value belongs, which is what the
  source at base `013b1af9` does.
  cost: the whole suite, not seconds. Run the file directly — `run-gates canary` sits in chunk
  `selftests`, so no push boundary or default bar runs it.
  fixture: the suite builds its own scratch repo and manifest; the tree needs no new fixture tree,
  and the arm sits inside the existing `HAVE_TIMEOUT` guard.
  figure: `600` is PINNED as the fixture's declared ceiling. The seconds are DERIVED at observation
  time from the ledger row, so the fixture's sleep length can change without touching the assertion.
- **AC2** — When the same run reports that leg, the tail reads `killed after <n>s, ceiling 600s` and
  contains no `timed out`.
  Red when: the rc=137 branch keeps the `timed out` verb, so a report of an operator kill, an OOM
  kill or a CI cancel still claims a ceiling fired.
- **AC3** — When the same run reaches the two rc=124 arms, `run-gates.test.sh:225` still observes
  `GATE FAIL  slow bounded` with `timed out after 2s` and `run-gates.test.sh:1133` still observes
  `GATE FAIL  sleeper  (timed out after 3s)`. Both name the CEILING, which is the boundary this unit
  draws in section 2's S2.
  Red when: the change widened into the 124 branch and printed elapsed there, where the ceiling is
  the true cause and both arms pin it.
- **AC4** — When the one-line hunk in `tools/run-gates/run-gates.sh` is reverted and
  `bash tools/run-gates/run-gates.test.sh` is run again, the new arm FAILS, naming both numbers —
  the ceiling the tail printed and the seconds the ledger recorded. Restoring the hunk makes the
  same suite pass.
  Red when: the arm passes against the unfixed source, which would mean it asserts something the
  defect already satisfies — the fixture-passes-by-finding-nothing class this suite's own arm 1c
  header names.
- **AC5** — When the suite finishes on this host, its closing `PASS (<n> assertions)` line reports
  an `<n>` at or above the raised `FLOOR_ASSERTIONS` in `tools/run-gates/run-gates.test.sh`.
  Red when: the arm's three increments sit inside the `HAVE_TIMEOUT` branch, so a host with no
  runnable `timeout` executes three fewer than the raised floor and reds a correct suite.
  permission: the timeout-less half of that Red-when cannot be observed by this run, because no
  such host is reachable from here. The placement is verified by reading the source beside arm 4h,
  which counts on both branches for exactly this reason and says so in its skip message.

## 7. Gates

`run-gates canary` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: `tools/run-gates/run-gates.test.sh` · a fixture leg running `kill -9 $$` under a declared
ceiling of 600, so the runner sees rc=137 from a kill it did not order and the unfixed source prints
600 against a ledger row of about 2 · `FLOOR_ASSERTIONS` rises by three, from the 143 it reads at
this spec's base sha.

Moved arm: `tools/run-gates/run-gates.test.sh` · the kill-after assertion at line 1156 accepts the
new killed tail alongside the unchanged 124 tail · no floor change.

## 8. Open questions

- **F1 — should an rc=137 leg that declared NO ceiling also report its seconds?** Today it reports
  `(exit 137)` and states no number, so it is outside the class this unit closes and section 3 cuts
  it. The case is real: a leg killed by an operator or an OOM killer while running unbounded names a
  bare exit code, and the operator then reads the ledger to learn how long it ran. The whole-run wall
  guard is NOT one of those cases, for the reason section 4 now gives: it kills the `runleg` subshell,
  so the leg has no `.rc` and reports `(no result)` with no tail built at all.
  Closing it costs one more branch, `(killed after ${secs}s)` with no ceiling clause, and one more
  assertion. Against it: this unit's mandate is the wrong number, not the missing one, and every
  line added to `report_one` is a line the tail contract has to keep true. Recommendation: leave it
  out of this unit and carry it as a `TOOL` backlog row, so the decision is recorded rather than
  silently folded into a one-line fix.

RESOLVED (agent, 2026-09-10, delegated) F1: out of this unit, carried as a TOOL backlog row.
Measured while resolving: all 104 legs in tools/gate-legs.json declare a ceiling, so the
population this branch would serve is EMPTY today and the code would ship dead. That is
corroboration and not the deciding reason -- M3's counter-rule refuses a fork decided by a signal
reading zero -- the deciding reason is section 3, which cuts the missing number from a unit whose
mandate is the wrong one. The row keeps it findable if a leg ever ships unbounded.

## 9. Revision log

- rev-1 · 2026-09-10 · initial draft.
- rev-2 · 2026-09-10 · §4 · §8 F1 · folded the round-2 spec audit's D6, the one defect that round
  assigns to this unit. §4's claim that `run_leg_reap` kills only the leg's own process and lets the
  `runleg` subshell finish is FALSE and is replaced by the mechanism the source shows: the `.pid`
  file holds the subshell's own `$BASHPID` (`run-gates.sh:1367`), `scan_descendants` seeds its result
  with that root pid (`run-gates.sh:429`), so the subshell is SIGKILLed, no `.sec` and no `.rc` are
  written, and `report_one` returns `(no result)` at `run-gates.sh:1449` before any tail is built.
  The conclusion is unchanged — the new `.sec` read is safe on the wall path — but the reason is now
  that the rc=137 branch is unreachable there rather than that the file exists. F1's description
  carried the same false premise in one clause and is corrected with it; the fork's RESOLVED mark and
  its decision are untouched.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "failed leg elapsed seconds reported in the run-gates
failure tail"`, run on 2026-09-10 at base `013b1af9`, reported
`scan coverage: 69 files scanned | 0 parse skips | unscanned layers: .sh`. Every file this unit
touches is `.sh`, so the map probe is BLIND to this subject and NO claim in this spec rests on it —
its twenty ranked candidates are Python symbols from other kits and none of them is this seam. Said
plainly because the same probe returns a confident ranked list either way, and a "no seam fits"
resting on it would be unfounded.

The seam was found by reading the source instead, and it exists rather than being absent: `runleg`
writes each leg's measured duration to `$WORK/<i>.sec` at `run-gates.sh:1409`, and the ledger block
at `run-gates.sh:1682` already reads that file as field 2 of every row. This unit adds a third
reader in `report_one` and mints no new identifier, no new file and no new helper. On the test side
the seam is the suite's existing scratch-repo harness, `runp` and the ledger at
`$P/.git/gate-ledger.tsv`, both of which the timing arms already drive.

Recall terms used, from the build's committed root-cause trace, re-run for this unit:
`run-gates leg rc timeout killed ceiling ledger summary verdict report elapsed fired sigkill`.
