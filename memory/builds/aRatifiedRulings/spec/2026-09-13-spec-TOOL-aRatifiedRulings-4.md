# TOOL-aRatifiedRulings-4 — a leg killed with no ceiling in play names the seconds it ran

**Status:** SPECCED · rev-3 · 2026-09-13 · node a · Tier-1 · base 16da4c6a · streams tooling · ratified 2026-09-13

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-review-TOOL-aRatifiedRulings-1-round1.md](../reviews/2026-09-13-review-TOOL-aRatifiedRulings-1-round1.md) | spec-audit | TOOL-aRatifiedRulings-1 TOOL-aRatifiedRulings-2 TOOL-aRatifiedRulings-3 |
| [2026-09-13-review-TOOL-aRatifiedRulings-1-round2.md](../reviews/2026-09-13-review-TOOL-aRatifiedRulings-1-round2.md) | spec-audit | TOOL-aRatifiedRulings-1 TOOL-aRatifiedRulings-2 TOOL-aRatifiedRulings-3 |

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
  `FLOOR_ASSERTIONS` rises by the number of increments the arm adds. The `tbl-loose` profile write
  at `run-gates.test.sh:1150` is HOISTED above the guard's `if` at `:1131`, beside the three
  counters already hoisted there for the same reason, because today that file is written only
  inside the guard and on a timeout-less host the arm would run under the runner's silent built-in
  fallback (`run-gates.sh:270`) while claiming the profile. The arm, its increments and the hoist
  are observed by AC1, AC2, AC4 and AC5; the `FLOOR_ASSERTIONS` raise is observed by AC7.
- **S4** — `tools/run-gates/README.md` gains one clause, in the paragraph that already documents
  the `(killed after Ns, ceiling Ms)` tail, naming the no-ceiling form. NOT OBSERVED — no gate
  reads that paragraph, for the reason S2 gives.
- **S5** — The obligation the S1 edit incurs, in the same commit as that edit: the kickoff manifest
  `last-audit` re-stamp in `memory/guides/SESSION-KICKOFF.md`, with a delta line in the commit
  message, because `tools/run-gates/run-gates.sh` is on that manifest's `watch:` line and
  `skills/session-kickoff/manifest-check.sh` check 5 reds a watched change with no stamp at or after
  it, on every bar. Observed by AC6.
- **S6** — `KIT_RUN_GATES_VERSION` moves 1.6 to 1.7, in the same commit as the S1 edit, on both
  carriers `tools/check-kit-versions.sh:98-104` pairs: the constant and its same-line marker at
  `run-gates.sh:19`, and the `gov:kit run-gates@` marker at `tools/run-gates/README.md:3`. The
  record that binds it is `TOOL-dMuffledSentinel-3`, the ruling unit 1 §8 F2 already ranks as the
  later one; §3 says why the bump lands here and not at the closing pass. Observed by AC8.

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
- **The run-gates bump is NOT routed to this build's closing pass, and the closing pass declares
  no run-gates carrier.** It lands here, as S6, in the one commit that already edits
  `run-gates.sh` and re-stamps `last-audit`. No gate in this repo ties `KIT_RUN_GATES_VERSION` to
  the runner's bytes: `tools/check-kit-versions.sh:98-104` grades the constant at `run-gates.sh:19`
  against the two `gov:kit run-gates@` markers for AGREEMENT, and the verdict epoch leg is
  hardcoded to the memory-tree engine. So the bump is a ruling, not a gate, and the ruling this
  build reads is `TOOL-dMuffledSentinel-3` (2026-09-12): an adopter's `kit-versions` leg refused a
  pull whose bytes had moved under an unchanged version, and unit 1 §8 F2 ranks that record above
  the leave-it precedents because it is the later one. The parent's `922fd926` (2026-09-10) left
  1.6 in place over an edit to this same function, and it predates that ruling, so it is the weaker
  precedent and rev-2 cited it wrongly; its count was wrong too, verified 2026-09-13:
  `git log 6462556a..922fd926 -- tools/run-gates/run-gates.sh` lists `922fd926` alone, while five
  other commits in that range touched `tools/run-gates/` without touching the runner. `6462556a`
  (2026-09-08) is where 1.6 landed. The closing pass is the wrong carrier for two reasons unit 2
  §8 F1 does not share: the unattended bump goes there because TWO units edit that kit and per-unit
  bumps collide on every carrier, and this unit is the only one in the build that edits any
  run-gates byte; and `run-gates.sh` is on the kickoff manifest's `watch:` line, so a closing-pass
  bump would owe a second `last-audit` re-stamp and a second declaration for a one-line move this
  commit already pays the stamp for.

### Edges

- **consumes-from** external — the `$WORK/<i>.bound` and `$WORK/<i>.sec` writes in `runleg`, both
  made before the `$WORK/<i>.rc` completion signal, and the sibling branch `TOOL-aLeakedHandle-3`
  landed, which already reads both. If `.bound` stops being written as a number, the new predicate
  reads 0 through `${fired:-0}` and the tail says `killed after` for a leg that may have had a bound;
  if `.sec` stops being written, the tail degrades to `?` rather than to a wrong number.
- **hands-off** external — a `runp` that REFUSES a `GATE_PROFILES` naming an absent path, so no arm
  in `tools/run-gates/run-gates.test.sh` can run under the runner's built-in fallback while
  believing it runs under a fixture. The round-1 audit proposed it as the left-shift for the S3
  defect; it changes a helper every section-4 arm routes through and is outside a ruling scoped to
  one branch plus one arm. The runner's own silent fallback at `run-gates.sh:270` stays either way,
  because it is the documented rollback.
- **hands-off** external — guarding the suite's four unguarded `timeout` calls at
  `run-gates.test.sh:517`, `:534`, `:1562` and `:1574` on `HAVE_TIMEOUT`, or rewriting them to an
  absolute path, which round 2 proposed as cluster C's left-shift. Those calls BOUND an arm's own
  runtime rather than grade `timeout`, so a guard would skip the clamp, expiry-verdict and wall
  arms on a timeout-less host to spare a stub, and an absolute path in the suite is the
  kit literal `run-gates.sh:358-361` refuses, one that resolves to nothing at another install
  prefix. AC5's stub is narrowed to the probes' argv instead, which leaves those calls real and the
  suite untouched.

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

**On a host with a runnable `timeout`, the failing case is observable only against a fixture that
strips the ceiling, and the spec says so rather than leaving the next session to discover it.**
Every leg in `tools/gate-legs.json` declares a `ceiling` today — the manifest owns that count and
this spec does not restate it; derive it with
`python -c "import json;l=json.load(open('tools/gate-legs.json'));print(len(l),sum('ceiling' in x for x in l))"` —
so on such a host no leg of the real bar runs with `bound` at 0 and the branch is reachable there
only by the fixture. The one real population the branch serves is the timeout-less host: there
`run-gates.sh:1393` runs `[ "$CEILINGS_LIVE" = 1 ] || bound=0` before the `.bound` write, every leg
of a real bar runs unbounded whatever the manifest declares, and an operator's or an OOM killer's
SIGKILL on any of them reaches this branch with a real leg. That host is why the arm sits outside
`HAVE_TIMEOUT`, and AC5 reproduces it on this box with a `PATH` stub. The class
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
running unbounded on a real bar. On a host with a runnable `timeout` that observation waits on a
leg shipping without a ceiling, and the row that carried this fork was written so it stays findable
if one ever does; on the timeout-less host it waits only on a kill nobody stages, which is the
host AC5's stub stands in for.

The arm sits OUTSIDE `HAVE_TIMEOUT` because the branch it grades is the one path that needs no
`timeout`. On a host with a runnable `timeout`, `bound` is 0 because no ceiling and no profile
timeout were declared; on a host without one, `CEILINGS_LIVE=0` at `run-gates.sh:1394` sets `bound`
to 0 anyway, and the profile's `timeout=0` is then redundant rather than load-bearing. Both reach
the same branch, so the arm executes on every host and its increments are counted beside it with no
skip. That is the opposite of 4h-kill, which reads a tail the runner only builds under a live bound
and skips with its sibling; the two arms are deliberately placed on opposite sides of the same `fi`.

**The fixture is not on both sides of that `fi` today, and the arm moves it.** `fx/tbl-loose.txt`
is written at `run-gates.test.sh:1150`, INSIDE the guard that opens at `:1131` and closes at
`:1211`; only `selfkill.sh` at `:977` is outside it. On a timeout-less host the file therefore does
not exist when the arm runs, and `run-gates.sh:270` (`if [ -f "$PROFILES" ]`) falls back to the
built-in formula without a word, as the runner's header at `:9-10` documents. The arm would still
pass there, because `CEILINGS_LIVE=0` forces the same branch, but it would pass under a profile it
did not name, and an arm whose fixture claim the run never checks is not driving the fixture it
says it drives. The one-line `printf` at `:1150` is therefore HOISTED to sit beside the three
`n=$((n+1))` counters above the `if` at `:1131`, which were moved there for the same
host-independence reason and say so in their own comment; 4h keeps reading the file from inside the
guard, byte-identical.
That is a move, not a new fixture. The alternative, the arm writing its own copy of the row, is a
second literal of one profile line and is refused for that.

**The stub refuses one argv and passes everything else to the real binary**, because the suite
calls `timeout` outside its `HAVE_TIMEOUT` guards and a stub that fails every call reds those arms.
Rev-2 said "a `timeout` stub that exits 1", and under that stub the suite's own PASS line is
unobservable: the clamp arms at `run-gates.test.sh:534` and `:517` capture an empty `out` with
`trc=1` and print `did not clamp to a working width` for all five widths, `:560` gets
`the clamp let it spin` where it expects `BOTH expired`, `:581-589` then compares two equal strings
and reds, and the wall arms at `:1562` and `:1574` write empty captures that fail `:1580` and
`:1583`. None of those sit inside a guard; the guards are `:158-249`, `:1082-1090` and
`:1131-1211` only. The seam is that both host probes run one byte-identical argument vector,
`timeout -k 1s 10 true` at `run-gates.test.sh:145` and `run-gates.sh:371`, and no other
non-comment `timeout` call in either file does — verified 2026-09-13 with
`grep -n -- '-k 1s 10 true'` over both files, which prints those two lines and two comments. So the
stub is:

```bash
REAL=$(command -v timeout)     # resolved BEFORE the stub dir is on PATH, or the stub finds itself
printf '#!/usr/bin/env bash\n[ "$*" = "-k 1s 10 true" ] && exit 1\nexec %s "$@"\n' "$REAL" > "$D/timeout"
chmod +x "$D/timeout"
PATH="$D:$PATH" bash tools/run-gates/run-gates.test.sh > <file> 2>&1
```

It is the shape the suite's own 4m arm already uses at `run-gates.test.sh:1295-1300`, a shim
prepended to `PATH` for the runner's probe, narrowed to the probe's bytes. The calls it must pass
through unchanged are the four direct ones at `:517`, `:534`, `:1562` and `:1574`, the first
reached through `clamp_expired_verdict` from `:536`, `:560`, `:569`, `:581` and `:582`; a stub
that refused the `-k` form instead would still red `:1562` and `:1574`, which spell `-k 5s 300`.
With the probe refused, `HAVE_TIMEOUT=0` in the suite and `CEILINGS_LIVE=0` in every runner the
suite spawns; the runner's reaper at `run-gates.sh:1009` is gated on that value, the wall at
`:1581-1621` is `EPOCHSECONDS`-driven and calls no `timeout`, the clamp fixtures are instant legs
whose verdict does not depend on a bound, and the wall arm's `"ceiling": 600` is inert either way
against a 120 s leg and an 8 s wall. The 4m arm prepends its own exit-127 shim ahead of this one
for its single invocation and is unaffected.

Measured 2026-09-13 on this host, the suite at base `16da4c6a` under that stub, stdout and stderr
to one file, with one other canary suite live on the box: it printed the three SKIP lines for arms
1c/1d/1e, 4g's timeout half and 4h/4h-kill, the teardown arm's own `Killed` job notice that the
last unstubbed log in `<git-dir>/gate-logs/run-gates_canary.log` also carries, nothing else, and
closed `PASS (147 assertions)` with exit 0 in 1079 s. One counter, the `stubborn` arm's at
`run-gates.test.sh:1165`, sits inside the guard — the only `n=$((n+1))` inside any of the three
guard ranges, counted 2026-09-13 — so a stubbed run closes one below the ordinary one, and it did:
that unstubbed log closed at 148 against a floor of 146. The arm's three increments and AC7's
raise keep that one-count slack where it is. This unit neither spends the slack nor moves that
counter, which is the 4h comment's own class and not this ruling's.

### Inventory

This unit mints no identifier, no file, no leg, no conf key and no naming cell. The arm is one more
block in an existing suite under an existing leg name.

### Files touched (estimate)

| File | Change |
|---|---|
| `tools/run-gates/run-gates.sh` | one guarded assignment added in `report_one`; one comment clause amended; `KIT_RUN_GATES_VERSION` and its same-line marker at `:19` moved 1.6 to 1.7 |
| `tools/run-gates/run-gates.test.sh` | one arm of about fifteen lines outside the `HAVE_TIMEOUT` guard; three `n=$((n+1))` beside it; the `tbl-loose` `printf` at `:1150` moved above the guard's `if` at `:1131`; `FLOOR_ASSERTIONS` raised by three |
| `tools/run-gates/README.md` | one clause in the existing killed-tail paragraph; the `gov:kit run-gates@` marker at `:3` moved to 1.7 |
| `memory/guides/SESSION-KICKOFF.md` | `last-audit` re-stamped, in the commit that edits `run-gates.sh` |

`FLOOR_ASSERTIONS` is a literal at `run-gates.test.sh:48`; its value is read from the file at the
pass's base and is DERIVED here, not pinned. It rises by exactly the number of `n=$((n+1))` lines
the arm adds, three, from whatever that line holds at the base — AC7 reads it that way, so a
sibling landing its own increments and raise first moves the base value and not the arithmetic.
No unit of this build touches the suite except this one.

### Rollout

One commit carries the `run-gates.sh` edit, the version bump on both carriers and the `last-audit`
re-stamp together, and the message carries the delta line. The bundle is not a preference:
`manifest-check.sh`'s staged leg C5s at `:408-420` refuses a commit whose staged set touches a
watched file while the staged manifest's audit block still carries HEAD's stamp, and
`.githooks/pre-commit:53-55` runs that leg whenever a watched file is staged, so a re-stamp as a
follow-up commit never gets past the hook; and `kit version markers` runs unguarded on every bar,
so the README marker lands with the constant or the next bar reds naming
`tools/run-gates/README.md`. The parent's unit 3 paid for the stamp at dispatch: its 12:03:13Z row
in `memory/builds/aLeakedHandle/RUN.md` declares no manifest and its 12:39:06Z row re-dispatches
with `memory/guides/SESSION-KICKOFF.md` appended. This unit declares it at dispatch. The suite edit
and the README's tail clause may ride the same commit or their own; neither is watched.

Passes of this build are SEQUENTIAL, and the roster orders them. Product files are disjoint across
the four units, but every pass declares its spec, the build README, `memory/LIVE.md` and the ledger
shard, and this unit and unit 1 both declare `memory/guides/SESSION-KICKOFF.md`, which is not a
`SHARED_RECORDS` member; `--dispatch` check 49 condition 1 at `unattended.sh:4853` refuses a
declared path that overlaps a still-open sibling's, and `lib-unattended.sh:100-105` makes equality
an overlap. Whichever of units 1 and 4 lands second re-stamps `last-audit` over the first, per the
charter's kickoff-manifest merge exception. Round-2 cluster B, id 9.

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
- **Have the arm write its own `tbl-loose` row** instead of hoisting the write at
  `run-gates.test.sh:1150`. Same bytes on a timeout host, a second literal of one profile line in
  the file, and the two copies drift the first time someone tunes 4h's width. The hoist is one
  line moved and leaves one source.
- **Make the arm announce a skip on a timeout-less host** instead of running there. The branch is
  reachable on that host, so a skip would report a capability gap the box does not have; a skip
  that announces itself is the right shape only for an arm whose subject the host cannot exercise.

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
  RED against the unpatched runner, on a fixture the spec names as the only observation available;
  the timeout-less host class observed once on this box through the `PATH` stub AC5 names, which
  refuses the two probes' argv and nothing else, so the suite's own unguarded `timeout` calls run
  real and its PASS line is observable under it; the floor raise observed by AC7.
- migration — N/A for stored files, manifest keys and record formats. The kit version moves 1.6 to
  1.7 (S6), which is what an adopter's `kit-versions` leg reads to tell this vintage from the last;
  `govkit.py:3438` reads it from `run-gates.sh`, so no adopter-side file changes shape.
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
- **AC5** — When `bash tools/run-gates/run-gates.test.sh` runs with the §4 stub first on `PATH`
  — a `timeout` that exits 1 for the argv `-k 1s 10 true` and `exec`s the real binary by absolute
  path for every other call, stdout and stderr redirected `> <file> 2>&1` — the suite's probe at
  `run-gates.test.sh:145` reads `HAVE_TIMEOUT=0`, the run prints the SKIP lines for arms 1c/1d/1e,
  4g's timeout half and 4h/4h-kill, prints NO skip naming the new arm, reports the `selfkilled` leg
  under `gate profile: loose` rather than a built-in row, and closes `PASS (<n> assertions)` with
  `<n>` at or above the raised `FLOOR_ASSERTIONS`; the ordinary run on the same host closes exactly
  one higher, the `stubborn` increment at `run-gates.test.sh:1165` being the one counter the guard
  still holds.
  Red when: the arm, its increments or the `tbl-loose` write sit inside the `HAVE_TIMEOUT` guard,
  so the stubbed run skips an arm whose branch it can reach, executes three fewer assertions than
  a correctly placed arm gives it and lands below the raised floor, or reports the leg under the
  runner's silent built-in profile because the `tbl-loose` row was never written. Staged break for
  the placement: move the arm's three `n=$((n+1))` inside the `if` at `:1131` and run under the
  stub — `<n>` closes at the base suite's stubbed count, two below the raised floor on today's
  figures, and `:1675` reds it naming both numbers.
  cost: a second full canary run. The one `run-gates canary` row in `<git-dir>/gate-ledger.tsv`
  read 1340 s on 2026-09-13 at the round-2 fold, where rev-2's earlier read of the same file the
  same day saw two rows at 22 to 27 minutes; the stubbed run at base took 1079 s beside another
  live canary suite. DERIVED from that ledger, which is per-host and rotates.
  fixture: the stub is the three-line script §4 quotes, in a scratch dir, with the real binary's
  path resolved before that dir is prepended. It refuses only the argv both probes share and so
  reaches `run-gates.sh:371` and `run-gates.test.sh:145` and nothing else; the suite's four
  unguarded calls at `:517`, `:534`, `:1562` and `:1574` run the real binary through it, and so do
  the expiry-verdict arms at `:560`, `:569`, `:581` and `:582` that route through the first. A stub
  that exits 1 for every call is NOT this fixture: under it those arms red and
  the PASS line never prints, which is what rev-2 specified and round 2 caught. The suite at base
  was run under this stub on 2026-09-13 and closed `PASS (147 assertions)` with exit 0, so the
  observation is available on this tree before the arm lands; with the arm's three increments the
  stubbed close should read 150 against AC7's raised floor of 149, both DERIVED from those reads.
- **AC6** — When `bash skills/session-kickoff/manifest-check.sh` runs at the landed tip, its check 5
  reports no watched file changed since `last-audit`, because the commit that edits
  `tools/run-gates/run-gates.sh` re-stamps the `last-audit` line in
  `memory/guides/SESSION-KICKOFF.md` with a delta line in its message.
  Red when: the runner edit lands without the re-stamp and check 5 names
  `tools/run-gates/run-gates.sh` as a watched file changed after the stamp, which is what one
  appended comment line to that file printed in the round-1 audit's scratch clone; or the stamp
  lands as a later commit and the staged leg C5s refuses the first.
- **AC7** — When `grep -E '^FLOOR_ASSERTIONS=' tools/run-gates/run-gates.test.sh` runs at the
  landed tip, it reads the value the same line held at the pass's base plus three, one per
  `n=$((n+1))` the arm adds; and the stubbed run AC5 names closes `PASS (<n> assertions)` with
  `<n>` at or above that raised value.
  Red when: the grep reads the base value, which is what a pass that lands the arm and forgets the
  raise leaves behind and what no other criterion here can see, since the suite's only read of the
  constant is `[ "$n" -ge "$FLOOR_ASSERTIONS" ]` at `run-gates.test.sh:1675` and any `<n>` above
  the unraised floor satisfies it; or the stubbed `<n>` is below the raised value, which is the
  arm's increments sitting inside a guard. Staged break: leave the constant at its base value with
  the arm landed and run the grep — it prints the base value, RED; `check-testsuite-counts.sh`
  does not catch it, its header says it runs nothing.
  figure: the base value is DERIVED from `run-gates.test.sh:48` at the pass's own base — 146 at
  `16da4c6a`, read 2026-09-13, so 149 if nothing lands increments there first — and is never pinned
  here.
- **AC8** — When `bash tools/check-kit-versions.sh` runs at the landed tip it exits 0, and
  `grep -E '^KIT_RUN_GATES_VERSION=' tools/run-gates/run-gates.sh` reads `1.7`, with
  `git log --format=%h -S'KIT_RUN_GATES_VERSION=1.7' -- tools/run-gates/run-gates.sh` and
  `git log --format=%h -S'ftail="(killed after ${secs:-?}s)"' -- tools/run-gates/run-gates.sh`
  each printing one sha and the two shas equal.
  Red when: the grep reads `1.6`, the bump forgotten; or the constant moved and the README marker
  did not, in which case the checker prints
  `kit-versions: tools/run-gates/README.md gov:kit marker != KIT_RUN_GATES_VERSION (1.7)` and
  exits 1 — observed 2026-09-13 in a scratch clone with `run-gates.sh:19` at 1.7 and
  `README.md:3` at 1.6, and observed exit 0 once both carried 1.7; or the bump landed in a commit
  other than the runner edit's, which is the same-version-two-vintages shape
  `TOOL-dMuffledSentinel-3` records, one commit narrower.
  fixture: the two carriers `check-kit-versions.sh:98-104` pairs, both in this unit's Files
  touched; `kit version markers` is unguarded and runs on every bar, so the half-bump red needs no
  hand invocation to be seen.

## 7. Gates

`run-gates canary` · `kickoff-manifest ratchet` · `kit version markers` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

Each leg's chunk and guard, read from `tools/gate-legs.json` on 2026-09-13: `run-gates canary` is
chunk `selftests` with guard `tools/`, `tools/gate-legs.json` and `tools/lib/`, so it is HELD on
every boundary bar and no boundary sets `GATE_SELFTESTS=1` — AC1 through AC5 all ride it and are
observed by the direct invocations AC1 and AC5 name, and AC7's grep reads the floor those runs
close against. `kickoff-manifest ratchet` is chunk `records` with no guard, so every bar runs it;
AC6 rides it, and it is the leg the round-1 audit showed RED on one unstamped comment line to
`run-gates.sh`. `kit version markers` is chunk `declarations` with no guard; it grades that
`KIT_RUN_GATES_VERSION` at `run-gates.sh:19` and the two `gov:kit run-gates@` markers still agree
after S6 moves all three to 1.7, and AC8 rides it — its half-bump red was observed in a scratch
clone on 2026-09-13. `memory hygiene` is chunk `records` with no guard, and grades this file.
`spec tokens (a spec's own names resolve)` is chunk `declarations` with no guard, and joins this
section's leg line and §6's paths against the tree.

New arm: `tools/run-gates/run-gates.test.sh` · the 4h-kill manifest row with its `ceiling` key
removed under the `tbl-loose` profile, whose write moves above the `HAVE_TIMEOUT` guard so the file
exists on every host, so `runleg` execs `selfkill.sh` directly with `bound` at 0 and the unpatched
runner prints `(exit 137)` against a ledger row of about 2 s · `FLOOR_ASSERTIONS` rises by the
arm's three increments, from whatever `run-gates.test.sh:48` reads at build time.

## 8. Open questions

- **F1 of the parent unit — should an rc=137 leg that declared NO ceiling also report its
  seconds?** Argued in `memory/builds/aLeakedHandle/spec/2026-09-10-spec-TOOL-aLeakedHandle-3.md`
  §8, cut from that unit by its §3, carried as `TOOL-aLeakedHandle-5`, and not re-argued here.
  RESOLVED (owner, 2026-09-13): build it — `TOOL-aLeakedHandle-9`, with the fixture-only red case
  accepted as stated. This spec is the work that ruling mandates and opens no further fork.

## 9. Revision log

- rev-1 · 2026-09-13 · initial draft.
- rev-2 · 2026-09-13 · §2 S3 S5 · §3 · §4 · §5 · AC5 AC6 · §7 · §10 · folded round-1 spec audit
  clusters M (ids 10, 15, 29) and N (ids 16, 33). M: the `run-gates.sh` edit owes the kickoff
  manifest `last-audit` re-stamp, which the parent's unit 3 only discovered at re-dispatch; S5,
  the files row, the Rollout, AC6 and the `kickoff-manifest ratchet` leg now carry it, and §3
  states that `KIT_RUN_GATES_VERSION` stays at 1.6 with the `kit version markers` leg named. N:
  `fx/tbl-loose.txt` was written inside the `HAVE_TIMEOUT` guard, so the arm as specced ran under
  the runner's silent built-in fallback on a timeout-less host while claiming the profile; the
  write is hoisted above the guard, §4 says why and refuses the duplicate-row alternative, AC5 now
  observes the timeout-less class on this host through a `PATH` stub instead of conceding it, and
  §10's "adds no fixture" is qualified to a move.
- rev-3 · 2026-09-13 · S3 S6 · §3 · §4 · §5 · AC5 AC7 AC8 · §7 · folded round-2 spec-audit
  clusters C (id 16), E (id 4), H (id 25), L (id 28) and the unit-4 half of B (id 9). C: the AC5
  stub that exited 1 for every call red the suite's own unguarded clamp and wall arms, so its PASS
  line was unobservable; the stub now refuses only the argv both host probes share and execs the
  real binary otherwise, §4 quotes it, names the eight calls it passes through, and records the
  base suite closing green under it, and the guard-the-arms left-shift is declined as a hands-off
  edge. E: the `FLOOR_ASSERTIONS` raise had no observer; AC7 greps the constant against the base
  value plus three. H: `KIT_RUN_GATES_VERSION` stayed at 1.6 on a precedent that predates the
  ruling unit 1 F2 ranks above it, and the commit count was wrong; S6 moves it to 1.7 in this
  unit's own commit, §3 says why not the closing pass, AC8 observes it with its half-bump red seen
  in a scratch clone, and Files touched, Rollout, §5 and §7 carry it. L: the "EMPTY population"
  paragraph contradicted the timeout-less host the same section names; it now qualifies the claim
  to hosts with a runnable `timeout`. B, id 9: the Rollout states passes are sequential under
  check 49 condition 1 and that this unit and unit 1 both declare `SESSION-KICKOFF.md`.

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
arm already drives; the new arm reuses all four and adds no fixture. It MOVES one: the
`tbl-loose` write leaves the `HAVE_TIMEOUT` guard so the row exists on every host, which is a
relocation of a line 4h keeps reading, not a second copy of it. `selfkill.sh` is untouched.

Recall terms used: `python tools/memory-recall/query.py "why does a killed leg with no declared
ceiling print a bare exit 137 in the run-gates failure tail" --terms run-gates report_one rc 137
killed ceiling unbounded ledger elapsed secs tail sigkill`, run 2026-09-13; its first hit is
`TOOL-aLeakedHandle-5` and its fourth is the parent unit's spec, which is the record set this unit
builds from.
