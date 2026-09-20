# TOOL-aWokenSentinel-19 — the adopter suite declares a shrink-only `FLOOR_ASSERTIONS`, and the close's kit-gate run is the named observer of every arm the committed `seed()` feeds

**Status:** SPECCED · rev-1 · 2026-09-20 · node a · Tier-2 · base 12513c25 · streams tooling · order 19

<!-- gen:spec-records -->

*No record names this unit.*

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
  at ten percent headroom, rounded down, and the comment says so and names the executed count the
  close's first green reports as the observation that confirms it, exactly as `gate-guard.test.sh`
  authored its own. Observed by AC1.
- **S3** — Spec 14 is folded at its rev-3 so S2 and §5 name the close's `run-unattended-gates.sh`
  adopter row, read from that run's per-suite log and never through `tail`, as the observer of the
  arms the committed seed feeds, and AC2 keeps only what the pass can observe directly. Observed by
  AC3.
- **S4** — The floor's failing case is observed at the pass without running the suite: the floor
  block is extracted with `sed -n` and evaluated by `bash -c` with `n` one below the pin, printing
  the `FAIL executed` sentence, and with `n` equal to the pin, printing nothing. Observed by AC2.

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

### Edges

- **consumes-from** `TOOL-aWokenSentinel-14` — the committed `seed()` every arm of the suite runs
  over; the floor is what makes that suite's green at the close a count and not a colour.
- **consumes-from** external — `tools/unattended/gate-guard.test.sh:432` to `:455`, the floor block
  and its authoring rule; `tools/run-gates/selftest-budgets.txt:111`, the row the close's runner
  delegates; and the suite's own `n` counter and `PASS` line at `adopt-unattended.test.sh:426`.
- **hands-off** external — a floor for `tools/workflows/unattended-build.test.sh`, the other
  unfloored suite this build touches; a backlog row the close mints.

## 4. Design

### The floor block

Inserted before the `PASS` line at `tools/unattended/adopt-unattended.test.sh:426`:

```
# FLOOR_ASSERTIONS — a shrink-only pin on the EXECUTED count, not on the written one. Authored from a
# static count of the `same`/`hit`/`miss`/`absent`/`present` sites in this file at ~10 % headroom,
# because the pass that wrote this line may not run the suite; the close's first green under
# run-unattended-gates.sh confirms the executed count against it. Lower it in a reviewed diff or not at all.
FLOOR_ASSERTIONS=<n>
[ "$n" -ge "$FLOOR_ASSERTIONS" ] || { echo "FAIL executed $n assertions against a floor of $FLOOR_ASSERTIONS — arms are UNREACHABLE rather than absent"; st=1; }
```

`<n>` is the static count times 0.9 rounded down — 64 from the 72 sites at base, re-derived by the
pass from the file it edits, because units 3 and 5 add arms to this suite before this unit's order
and the count at the pass is what binds. The block sits above the `PASS` line so a breach prints a
`FAIL` and flips `st`, which is the suite's own refusal shape; the runner then reads the non-zero
exit and the budgets row names the suite.

### Why a static count and what confirms it

Every `same`, `hit`, `miss`, `absent` and `present` call increments `n`; a site inside a loop
executes more than once, so the static count is a LOWER bound on the executed count and a floor at
ninety percent of it is satisfiable by construction. The close's first green prints
`PASS (<n> assertions)` with the executed count, which is the observation the comment defers to; if
that count ever falls under the pin the runner reds naming the suite, and the reason — an arm made
unreachable — is the thing the floor exists to see.

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
  remedy is a reviewed lowering with the executed count in the comment, and the discount makes it
  unlikely. The gate-guard suite authored its floor the same way and its first green confirmed it.
- testing — §6; the block evaluated by `bash -c` on both sides of the pin.
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
  expected to have moved with units 3 and 5.
- **AC2** — When the floor block — the `FLOOR_ASSERTIONS=` line and the compare below it — is
  extracted with `sed -n` and run by `bash -c` with `n` set one below the pin and `st=0`, it prints
  `FAIL executed` and leaves `st` at 1; with `n` equal to the pin it prints nothing and `st` stays 0.
  Red when: the compare passes under the pin, which is a floor that cannot fail; or it reds at the
  pin, which is an off-by-one that reds every honest run.
- **AC3** — When `grep -c 'run-unattended-gates' memory/builds/aWokenSentinel/spec/2026-09-20-spec-TOOL-aWokenSentinel-14.md`
  runs it prints at least 1, and `grep -c 'reads no change'` over the same file prints 0.
  Red when: spec 14 still names AC2 as the observer of arms AC2 never runs, which is H5 re-entering
  by prose.
- **AC4** — When `grep -c 'FLOOR_ASSERTIONS' tools/unattended/adopt-unattended.test.sh` runs at
  the tip it prints at least 2 — the pin and the compare — and 0 at this unit's base.
  Red when: the pin exists and nothing reads it.
  figure: both counts are DERIVED by the grep at observation over the tip and over the file at
  `12513c25`.

## 7. Gates

`unattended kit gate` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `install-prefix (shipped surface)` · `lexicon naming predicates`

These run once at `--close`. The pass runs none of them: it verifies with the greps of AC1, AC3
and AC4 and the extracted block of AC2. The suite itself runs at the close under the build-level
rule's `run-unattended-gates.sh`, whose `unattended adopter e2e` row is where the pin is first
confirmed against an executed count.

New arm: `tools/unattended/adopt-unattended.test.sh` · the floor compare, whose failing case is `n` under the pin, staged by evaluating the extracted block · `FLOOR_ASSERTIONS` is this unit's own pin, authored at ten percent under the static count

## 8. Open questions

none

## 9. Revision log

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
returned `TOOL-dUnstalledConvoy-19`, `TOOL-aUnmannedHelm-6` (a core-set floor is a shrink-only
COUNT, and a membership form was measured vacuous — the reason this pin is a number) and the
aRatifiedRulings spec that raised the kit-gate floor by exactly its arm; none names a floor for the
adopter suite.

Recall terms used: `FLOOR_ASSERTIONS shrink-only executed count unreachable arms suite green first PASS floor headroom`
