# TOOL-aWokenSentinel-19 — the adopter suite declares a shrink-only `FLOOR_ASSERTIONS`, and the close's kit-gate run is the named observer of every arm the committed `seed()` feeds

**Status:** CLOSED · rev-2 · 2026-09-21 · node a · Tier-2 · base 12513c25 · streams tooling · order 19

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-20-build-TOOL-aWokenSentinel-19-1-acceptance-ledger.md](../build/2026-09-20-build-TOOL-aWokenSentinel-19-1-acceptance-ledger.md) | journal | — |
| [2026-09-20-prompt-TOOL-aWokenSentinel-19-1-build-brief.md](../prompts/2026-09-20-prompt-TOOL-aWokenSentinel-19-1-build-brief.md) | journal | — |
| [2026-09-20-review-TOOL-aWokenSentinel-15-spec-audit-round1.md](../reviews/2026-09-20-review-TOOL-aWokenSentinel-15-spec-audit-round1.md) | spec-audit | TOOL-aWokenSentinel-15 TOOL-aWokenSentinel-16 TOOL-aWokenSentinel-17 TOOL-aWokenSentinel-18 TOOL-aWokenSentinel-20 |

<!-- /gen:spec-records -->

## 1. Goal

Close audit finding H5 (round 2, raw id 5): `TOOL-aWokenSentinel-14` S2 says the adopter suite's
arms keep their assertions and that AC2 observes it, and its §5 risks row says AC2 runs the suite's
arms over a seeded fixture; AC2 as written runs `adopt-unattended.sh --check` once per fixture and
a `grep -c 'git commit'`, and no arm of `tools/unattended/adopt-unattended.test.sh` — the suite
whose every arm runs over the seed unit 14 edits — is executed by any criterion, and the suite sits
on no `tools/gate-legs.json` leg. Two facts close it. The suite IS run at this build's close: the
README's build-level rule runs `run-unattended-gates.sh` once on a frozen clone, and that runner
delegates the `unattended adopter e2e` row of `tools/run-gates/selftest-budgets.txt:111`, so the
observer exists and spec 14 is folded to name it. And the suite's green must mean its arms RAN: it
prints `PASS (<n> assertions)` and pins nothing, so an arm lost to a seed change that skips a
fixture reads as a smaller green. This unit gives the suite the shrink-only executed-count floor
every sibling suite in the kit carries, authored from a static count and confirmed at the close's
first green, so the close's run reds on a lost arm and not only on a failed one.

## 2. Scope (IN)

- **S1** — `tools/unattended/adopt-unattended.test.sh` ends, before its `PASS` line, with the
  sibling suites' floor block: a `FLOOR_ASSERTIONS=<n>` pin with the authoring rule in its comment,
  and `[ "$n" -ge "$FLOOR_ASSERTIONS" ] || { echo "FAIL executed $n assertions against a floor of
  $FLOOR_ASSERTIONS — arms are UNREACHABLE rather than absent"; st=1; }`, the shape of
  `tools/unattended/gate-guard.test.sh:455`. Observed by AC1 and AC2.
- **S2** — The pin's value is DERIVED at the pass from a static count of the suite's assertion
  sites — `grep -cE '^\s*(same|hit|miss|absent|present) '` over the file, 72 at this unit's base —
  at ten percent headroom, rounded down, and the comment carries the authoring rule in the words
  `static count` and names the close's kit-gate run as what confirms it, exactly as
  `gate-guard.test.sh` authored its own. Observed by AC1 and AC4, which pins the comment's phrase.
- **S3** — Spec 14 is folded at its rev-4 so S2, §5 and AC5 name the close's
  `run-unattended-gates.sh` run as the observer of the arms the committed seed feeds, and name
  what that run actually surfaces: the runner delegates to `run-selftests.sh`, which writes each
  suite under a `mktemp -d` its EXIT trap removes and prints one `ok <name> <s>s` row per green
  suite or a non-zero exit naming the suite — no per-suite log persists and the suite's
  `PASS (<n> assertions)` line is never surfaced. The observation is therefore the
  `unattended adopter e2e` row being `ok`, which holds only if this floor held, and no criterion
  names a log or an executed count read from that run. Observed by AC3.
- **S4** — The floor's failing case is observed at the pass without running the suite: the floor
  block is extracted with `sed -n` and evaluated by `bash -c` with `n` one below the pin, printing
  the `FAIL executed` sentence, and with `n` equal to the pin, printing nothing. Observed by AC2.
- **S5** — The structural arm `TOOL-dUnstalledConvoy-19` asks for, beside the floor and above the
  same `exit "$st"`: a self-read of `$0` asserting that no executable line follows the suite's
  terminal exit — `sed -n '/^exit "\$st"$/,$p' "$0" | grep -cvE '^\s*(#|$)'` prints exactly 1 —
  printing `FAIL a line follows the terminal exit and can never run` and setting `st=1` otherwise.
  The floor catches an arm made unreachable by a seed change, which is a count that can go slack;
  this arm catches an arm appended after the exit, which is one grep and cannot. Observed by AC5.

## 3. Non-goals (OUT)

- **No `tools/gate-legs.json` row.** The 2026-08-23 owner ruling took every kit self-test off the
  merge bar; the suite's home is the on-demand runner and the budgets file, which this build's close
  already runs.
- **No suite run inside the pass.** The build-level rule forbids it; the pin is authored from the
  static count and confirmed by the close, as the gate-guard suite's own floor was.
- **No change to any arm.** The floor counts what the arms execute; it does not edit them, and unit
  14's `--check` observation stays unit 14's.
- **No shard floors.** The suite runs whole in 38 seconds by the budgets row; sharding is the
  driver suite's answer to a 43-minute run and has no work here.
- **No kit-wide after-exit arm.** `TOOL-dUnstalledConvoy-19` names the class for every suite that
  ends `exit "$st"`; this unit builds the arm for the suite it floors and hands the loop over every
  `*.test.sh` in both kits off as a backlog row the close mints, citing -19.

### Edges

- **consumes-from** `TOOL-aWokenSentinel-14` — the committed `seed()` every arm of the suite runs
  over; the floor is what makes that suite's green at the close a count and not a colour.
- **consumes-from** external — `tools/unattended/gate-guard.test.sh:432` to `:455`, the floor block
  and its authoring rule; `tools/run-gates/selftest-budgets.txt:111`, the row the close's runner
  delegates; and the suite's own `n` counter and `PASS` line at `adopt-unattended.test.sh:426`.
- **hands-off** `TOOL-aWokenSentinel-21` — the floor, the leg, the budget row and the registry
  exemption for `tools/workflows/unattended-build.test.sh`, the other unfloored suite this build
  touches, which that unit puts in the declared self-test population.
- **hands-off** external — the kit-wide form of S5's structural arm, one loop over every
  `*.test.sh` in both kits that ends with a terminal `exit`, as `TOOL-dUnstalledConvoy-19` asks;
  a backlog row the close mints citing that row.

## 4. Design

### The floor block

Inserted before the `PASS` line at `tools/unattended/adopt-unattended.test.sh:426`:

```
# FLOOR_ASSERTIONS — a shrink-only pin on the EXECUTED count, not on the written one. Authored from a
# static count of the `same`/`hit`/`miss`/`absent`/`present` sites in this file at ~10 % headroom,
# because the pass that wrote this line may not run the suite; the close's first green under
# run-unattended-gates.sh is what confirms it held — that runner surfaces no count, only the row. Lower it
# in a reviewed diff or not at all.
FLOOR_ASSERTIONS=<n>
[ "$n" -ge "$FLOOR_ASSERTIONS" ] || { echo "FAIL executed $n assertions against a floor of $FLOOR_ASSERTIONS — arms are UNREACHABLE rather than absent"; st=1; }
```

`<n>` is the static count times 0.9 rounded down — 64 from the 72 sites at base, re-derived by the
pass from the file it edits, because units 3 and 4 add arms to this suite before this unit's order
(spec 3 §7's adopter-suite arm line and spec 4 §7's; spec 5 never touches this file) and the count
at the pass is what binds. The block sits above the `PASS` line so a breach prints a `FAIL` and
flips `st`, which is the suite's own refusal shape; the runner then reads the non-zero exit and the
budgets row names the suite.

### The structural arm, beside the floor

```
# NOTHING EXECUTABLE MAY FOLLOW THE TERMINAL EXIT (TOOL-dUnstalledConvoy-19): an arm appended after it
# is dead while every static signal says it is fine, and a numeric floor with headroom hides exactly
# that many. One grep, and it cannot go slack.
[ "$(sed -n '/^exit "\$st"$/,$p' "$0" | grep -cvE '^\s*(#|$)')" = 1 ] || { echo "FAIL a line follows the terminal exit and can never run"; st=1; }
```

The range starts at the exit line itself, so a suite with nothing after it reads exactly 1; a
comment or a blank line after the exit is not counted; any other line is. It sits above the exit it
reads, which is the only place a self-read of `$0` can run, and it is the arm -19 records as the
fix for the class the floor's slack cannot see — the floor is kept because it catches a different
loss, an arm made unreachable by a seed change that skips a fixture.

### Why a static count and what confirms it

Every `same`, `hit`, `miss`, `absent` and `present` call increments `n`; a site inside a loop
executes more than once, so the static count is a LOWER bound on the executed count and a floor at
ninety percent of it is satisfiable by construction. What confirms it is the close's kit-gate run
reading `ok` on the `unattended adopter e2e` row: `run-selftests.sh` keeps no per-suite log
(`:492` to `:493`, a `mktemp -d` removed by its EXIT trap) and prints no assertion count, so the
suite's `PASS (<n> assertions)` line is seen by nobody at the close and the comment defers to the
row, not to a number. If the executed count ever falls under the pin the suite exits non-zero, the
runner reds naming it, and the reason — an arm made unreachable — is the thing the floor exists to
see. `TOOL-dUnstalledConvoy-19` records that a floor's headroom is exactly the number of stranded
arms it hides, which is true of this one's eight; that is why S5's structural arm sits beside it
rather than the floor standing alone, and why §5's risks row does not call the discount a
protection.

### Inventory

| identifier | kind | cell |
|---|---|---|
| `FLOOR_ASSERTIONS` | a shell variable in the adopter suite, the sibling suites' name | no cell; not a function |

No function, key, verb or file is minted.

### Files touched (estimate)

| file | change |
|---|---|
| `tools/unattended/adopt-unattended.test.sh` | the floor block above the `PASS` line |
| `memory/builds/aWokenSentinel/spec/2026-09-20-spec-TOOL-aWokenSentinel-14.md` | rev-3: S2, §5 and AC2 name the close's run as the observer |

### Alternatives rejected

- **An AC in spec 14 that runs the suite at the tip and compares its pass count to base.** The
  audit's own fix. It puts a suite run inside a pass, which the build-level rule forbids, and it
  compares two counts with no pin, so a suite that lost an arm at base and tip alike reads equal.
- **A `gate-legs.json` row for the suite.** Reverses an owner ruling; veto 2.
- **Pin the count at exactly the executed value.** Reds on the first arm anybody legitimately
  removes; the sibling suites' discount exists for that reason and is copied.

## 5. Production-readiness checklist

- security — N/A; a count at the end of a test suite.
- perf / scale — one integer compare.
- error / empty / loading states — a suite that executes zero assertions reds against any positive
  floor, which is the green-by-absence class the charter names and the reason the floor is not
  zero.
- observability — the breach sentence names both numbers.
- risks — a static count that overshoots the executed one reds the close's first green; the
  remedy is a reviewed lowering with the executed count in the comment. The discount that makes
  an overshoot unlikely is the same slack `TOOL-dUnstalledConvoy-19` records as hiding stranded
  arms, which the floor cannot see and S5's structural arm can; the two are kept together for
  that reason. The gate-guard suite authored its floor the same way and its first green confirmed
  it.
- testing — §6; the floor block evaluated by `bash -c` on both sides of the pin, and the
  structural arm evaluated over a copy of the suite with a line appended after its exit.
- migration — N/A.
- user docs — none; the block's comment.

## 6. Acceptance criteria

- **AC1** — When `grep -cE '^\s*(same|hit|miss|absent|present) ' tools/unattended/adopt-unattended.test.sh`
  runs at the tip it prints a count `c`, and `sed -n 's/^FLOOR_ASSERTIONS=//p'` over the same file
  prints an integer at or below `c * 9 / 10` and above `0`; at this unit's base the `sed` prints
  nothing.
  Red when: the pin is above the static count, which reds the close's first green on honest arms;
  or the pin is zero, which cannot fail; or no pin exists.
  figure: `c` is DERIVED by the grep at observation — 72 at base, PINNED as read on 2026-09-20 and
  expected to have moved with units 3 and 4, the two units whose §7 arm lines name this suite.
- **AC2** — When the floor block — the `FLOOR_ASSERTIONS=` line and the compare below it — is
  extracted with `sed -n` and run by `bash -c` with `n` set one below the pin and `st=0`, it prints
  `FAIL executed` and leaves `st` at 1; with `n` equal to the pin it prints nothing and `st` stays 0.
  Red when: the compare passes under the pin, which is a floor that cannot fail; or it reds at the
  pin, which is an off-by-one that reds every honest run.
- **AC3** — When `grep -c 'run-unattended-gates' memory/builds/aWokenSentinel/spec/2026-09-20-spec-TOOL-aWokenSentinel-14.md`
  runs it prints at least 1, `grep -c 'reads no change'` over the same file prints 0, and
  `grep -c 'per-suite log'` over the same file prints 0.
  Red when: spec 14 still names AC2 as the observer of arms AC2 never runs, which is H5 re-entering
  by prose; or it names a per-suite log the close's runner never writes, which is an observer that
  does not exist.
  figure: all three counts are DERIVED by the greps at observation, run at authoring time over
  spec 14 rev-4.
- **AC4** — When `grep -c 'FLOOR_ASSERTIONS' tools/unattended/adopt-unattended.test.sh` runs at
  the tip it prints at least 2 — the pin and the compare — and 0 at this unit's base; and
  `grep -c 'static count' tools/unattended/adopt-unattended.test.sh` prints at least 1 at the tip
  and 0 at base, which only the pin's comment can carry.
  Red when: the pin exists and nothing reads it; or the pin carries no authoring rule, which
  leaves the next session lowering it with no stated procedure.
  figure: every count is DERIVED by the greps at observation over the tip and over the file at
  `12513c25`.
- **AC5** — When the structural arm's line is extracted with `sed -n` and run by `bash -c` with
  `$0` set to the adopter suite's own path at the tip and `st=0`, it prints nothing and `st` stays
  0; with `$0` set to a scratch copy of the suite that has `echo stranded` appended
  after its `exit "$st"`, it prints `FAIL a line follows the terminal exit` and leaves `st` at 1;
  and `sed -n '/^exit "\$st"$/,$p' tools/unattended/adopt-unattended.test.sh | grep -cvE '^\s*(#|$)'`
  prints exactly 1 at the tip.
  Red when: an appended arm is not seen, which is the -19 class with a grep that cannot fail; or
  the arm reds on the honest suite, which is a range anchored on a line the file does not carry.
  fixture: `bash -c '<line>' <path>` binds `$0` to the path, so the same line grades the tip and
  the scratch copy.

## 7. Gates

`unattended kit gate` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `install-prefix (shipped surface)` · `lexicon naming predicates`

These run once at `--close`. The pass runs none of them: it verifies with the greps of AC1, AC3
and AC4, the extracted block of AC2 and the extracted line of AC5. The suite itself runs at the
close under the build-level rule's `run-unattended-gates.sh`, whose `unattended adopter e2e` row
reads `ok` only if the pin held and the structural arm found nothing after the exit; that row is
the observation, because the runner persists no per-suite log and surfaces no count.

New arm: `tools/unattended/adopt-unattended.test.sh` · the floor compare, whose failing case is `n` under the pin, staged by evaluating the extracted block; the after-exit structural arm, whose failing case is a line appended after the terminal exit in a scratch copy · `FLOOR_ASSERTIONS` is this unit's own pin, authored at ten percent under the static count

## 8. Open questions

none

## 9. Revision log

- rev-2 · 2026-09-20 · S2 · S3 · S5 · §3 · §4 · §5 · AC1 · AC3 · AC4 · AC5 · §7 · §10 · folded
  spec-audit round 3: M11 (raw 42) — `TOOL-dUnstalledConvoy-19` rules that a floor with headroom
  hides exactly that many stranded arms and asks for a structural after-exit arm, and this spec
  cited it and installed eight assertions of slack without engaging it; S5 and AC5 add the one-grep
  arm beside the floor, §4, §5 and §10 say why the floor stays beside it, and the kit-wide loop is
  handed off with -19 cited; M12 (raw 31) — `run-selftests.sh` persists no per-suite log and
  surfaces no `PASS (<n> assertions)`, so S3, §4 and §7 name the runner's `ok` row as the
  observation and spec 14 AC5 is folded at its rev-4 to the same; L3 (raw 13) — AC4 pins the
  comment's `static count` phrase; L4 (raw 24) — the adopter suite's arm writers before this
  order are units 3 and 4, not 3 and 5, in §4 and AC1's figure note, and spec 4 §7 is folded at
  its rev-4 to cite this floor as spec 3 §7 does. The `hands-off` on the harness suite's floor
  names `TOOL-aWokenSentinel-21`, which now owns it.
- rev-1 · 2026-09-20 · initial draft, authored at the M4 disposal of spec-audit round 2 as the
  promotion of H5 (raw id 5).

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "declare a shrink-only assertion floor on a test suite's
executed count"` returned no seam and `unscanned layers: .sh`; no Python seam fits a shell suite.
The seam, read at source, is the floor block the kit's sibling suites already carry:
`tools/unattended/gate-guard.test.sh:432` to `:455`, authored from a static count because the pass
that wrote it could not run it, which is this unit's situation exactly; the driver suite's
`FLOOR_ASSERTIONS` at `tools/unattended/unattended.test.sh:5721` and the kit-gate suite's at
`tools/unattended/check-unattended.test.sh:3252` are the same shape with shards. The recall probe
returned `TOOL-dUnstalledConvoy-19` — OPEN, and a ruling on this exact shape: a floor's headroom
hides exactly that many stranded arms, raising it "fixes the instance and not the class", and the
class wants a structural after-exit arm that is one grep; S5 builds that arm for this suite and
the floor is kept for the loss the arm cannot see — `TOOL-aUnmannedHelm-6` (a core-set floor is a
shrink-only COUNT, and a membership form was measured vacuous — the reason this pin is a number)
and the aRatifiedRulings spec that raised the kit-gate floor by exactly its arm; none names a
floor for the adopter suite, and no `*.test.sh` in the kit carries the after-exit arm (grepped).

Recall terms used: `FLOOR_ASSERTIONS shrink-only executed count unreachable arms suite green first PASS floor headroom`
