# TOOL-dPlacedRequest-52 — the round-3 promotions' minors: a placed race inside its lock bound, an oracle that answers by status, one walk, and criteria that read what they name

**Status:** DEFERRED · rev-6 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 27 · advances TOOL-dPlacedRequest-22

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-50-promoted-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-50-promoted-fix-return.md) | research | TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 |
| [2026-10-25-build-TOOL-dPlacedRequest-52-deviation-521.md](../build/2026-10-25-build-TOOL-dPlacedRequest-52-deviation-521.md) | deviation | — |
| [2026-10-25-build-TOOL-dPlacedRequest-52-deviation-522.md](../build/2026-10-25-build-TOOL-dPlacedRequest-52-deviation-522.md) | deviation | — |
| [2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md) | journal | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-50-promoted-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-50-promoted-fix-brief.md) | research | TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 |
| [2026-10-25-review-TOOL-dPlacedRequest-50-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-50-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-3 promotions
(`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-44-spec-audit.md`)
exited CONVERGED with 30 confirmed findings. Its two highs are units 50 and 51. This unit is the
batch BUILD-METHOD M4 makes of the rest: 20 MEDIUM and 8 LOW findings by raw id, one scope item per
id, each naming its finding and, in brackets, the review item holding it (M1 to M14, L1 to L6). Six
items hold more than one id (M1: 4, 12, 23 and 31; M2: 5 and 24; M3: 6 and 18; L2: 8 and 26; L3: 9
and 35), and three low items restate a medium's defect at another grade (L1 is M5's, L5 is M4's,
L3's second half is M14's). Each id still gets its own item and its own observation. The minors land
on twelve units, so this unit repairs none in particular and sits above every unit of the build, at
order 27, after units 49 and 51 at 26. Criterion ACn observes item Sn.

| Item | Finding | Severity | Lands on |
|---|---|---|---|
| S1 to S4 | 4, 12, 23, 31 (M1) | MEDIUM | units 37, 48, 49 |
| S5, S6 | 5, 24 (M2) | MEDIUM | units 43, 48 |
| S7, S8 | 6, 18 (M3) | MEDIUM | units 36, 38, 49 |
| S9, S10 | 7 (M4), 25 (L5) | MEDIUM, LOW | units 43, 49 |
| S11 to S13 | 11, 29 (M5), 2 (L1) | MEDIUM, LOW | units 34, 44, 49 |
| S14 | 3 (M6) | MEDIUM | units 44, 45 |
| S15 | 13 (M7) | MEDIUM | unit 48 |
| S16 | 14 (M8) | MEDIUM | unit 49 |
| S17 | 17 (M9) | MEDIUM | unit 44 |
| S18, S19 | 20 (M10), 21 (M11) | MEDIUM | units 43, 49 |
| S20 | 32 (M12) | MEDIUM | unit 49 |
| S21, S22 | 34 (M13), 36 (M14) | MEDIUM | units 46, 47 |
| S23, S24 | 8, 26 (L2) | LOW | units 33, 49 |
| S25, S26 | 9, 35 (L3) | LOW | unit 46 |
| S27 | 15 (L4) | LOW | unit 48 |
| S28 | 27 (L6) | LOW | unit 44 |

## 2. Scope (IN)

Every edit to another unit's spec is in place, one rev bump per spec with its §9 line naming this
unit and the items it carries.

- **S1** — finding 4 (M1). `TOOL-dPlacedRequest-48`'s placed race reaches its verdict only over
  `TOOL-dPlacedRequest-49` S25's bounded retry. 48 S2, §3 and its Edges name S25 as the bound B's lock
  wait relies on, and state that at order 25 that wait has no bound, so 48's own pass observes AC3 and
  the stub alone and the race is read at this unit's pass and at the close. Observed by AC1.
- **S2** — finding 12 (M1). 48 S2 states the margin: B's whole lock attempt, S25's 5 s retry, ends
  before A's `until`, which is the take plus `NODE_LOCK_BOUND`, 10 s with no override
  (`TOOL-dPlacedRequest-37` S1). 48's Edges gain a consumes-from `TOOL-dPlacedRequest-37`, mirrored in
  37. Observed by AC2.
- **S3** — finding 23 (M1). After B ends, the arm reads the common dir's health log: a
  `node-lock-broken` event naming `requests.lock` marks the attempt as a placement overrun, and the
  arm's output names that event, never "the lock does not serialise". Observed by AC3.
- **S4** — finding 31 (M1), the skeptic's corrected fix. The arm stamps the time `$h/held` appears
  and the time B exits. An attempt whose B ends more than `NODE_LOCK_BOUND` after the hold, or whose
  health log carries S3's event, is discarded and the placement re-run, up to 3 attempts in all. The
  arm fails `request race placed past the lock bound` only when every attempt overruns. On every exit
  path, "never placed" included, it touches `$h/release` and waits for A under a bound. Observed by
  AC4.
- **S5** — finding 5 (M2). `TOOL-dPlacedRequest-43` S30 pins the copy: `--request` copies with one
  `cp -- <src> <git-common-dir>/requests/<key>.md` spawn, after the compare and under the lock. The
  built `--request` body holds that spawn; a body built with another copy form is changed to it.
  Observed by AC5.
- **S6** — finding 24 (M2). 48 S1, its §4 Files touched and its §5 risks line cite 43 S30 as the line
  that mandates the `cp` spawn its stub keys on. Observed by AC6.
- **S7** — finding 6 (M3). 49 S7 keeps no population of its own. `TOOL-dPlacedRequest-36` AC3 is
  restated to point at `TOOL-dPlacedRequest-38`'s carrier arm (49 S8), whose population takes the
  parity loop's pathspec and the `gov_feed_sh` row's exclude (`tools/lib/resolve-python.test.sh:218`),
  so the canonical `tools/lib/gov-feed.sh` never joins it. 49 AC7 gains that case. Observed by AC7.
- **S8** — finding 18 (M3). One carriage check: 38 §3's non-goal "No check that a carrier holds
  `health_log_sh` itself" is rewritten to name 38's own carrier arm as that check, 49 S8 names 38 §3
  among what it amends, and 49's Edges line to 38 names §3. Observed by AC8.
- **S9** — finding 7 (M4). 43 S22's figure is rewritten with AC22 to 48128, carrying 49 S13's
  derivation, and 49 S13 names S22 beside AC22. 43's §3 hand-off to this unit tells 43's order-24
  pass to read AC22 at 48128. Observed by AC9.
- **S10** — finding 25 (L5). 49 AC13 gains the count of the old figure in 43 outside its revision
  log, which must be 0. Observed by AC10.
- **S11** — finding 11 (M5). The oracle answers by its exit status. After its guards,
  `TOOL-dPlacedRequest-44` §4 ends `if git log … | grep -E '^[+-]KIT_(UNATTENDED|RUN_GATES)_VERSION='; then exit 1; fi; exit 0`:
  a found bump exits 1, a non-empty clean walk exits 0, and a refusal exits 2. 44 AC1 asserts exit 0
  on a clean build. `TOOL-dPlacedRequest-34` AC59 and 49 S3 read "the header line, exit 0, no `KIT_`
  line". Observed by AC11.
- **S12** — finding 29 (M5). No range is built from an unchecked command. The range comes only from
  a found prepared merge (S17); when none is found the oracle prints `version oracle: no prepared
  merge on HEAD` and exits 2, so a missing tracking ref never reads as an empty build. Observed by
  AC12.
- **S13** — finding 2 (L1). 44 AC3's empty walk exits 2, a status the clean walk never gives, and AC3
  is restated to expect it. Observed by AC13.
- **S14** — finding 3 (M6). One fixture, one count. 44 §6 defines its fixture once: a base, two
  branch commits (one bumping `KIT_UNATTENDED_VERSION` from 1.110 to 1.111), one default-branch commit
  and a `--no-ff` merge onto the default branch, its header ending `· 2 commits`. 44 §4 Evidence states that
  count, and 45 AC2 names its fixture by the same count, as `TOOL-dPlacedRequest-51` S2 writes it.
  Observed by AC14.
- **S15** — finding 13 (M7), the skeptic's corrected fix. 48 AC4 reads the AC30 paragraph itself:
  `awk '/^- \*\*AC30\*\*/{f=1} f&&/^- \*\*AC3[1-9]\*\*/{exit} f'` over 43, squeezed by
  `tr -s '[:space:]' ' '`, must contain `TOOL-dPlacedRequest-48` and must not contain
  `two background`. Observed by AC15.
- **S16** — finding 14 (M8), the skeptic's corrected fix. 49 AC24, AC30 and AC31 grep each file
  squeezed by `tr -s '[:space:]' ' '`, never line by line, so a phrase the house wrap splits is still
  read. Observed by AC16.
- **S17** — finding 17 (M9). The oracle finds the prepared merge by the lander's own derivation,
  `t=$(git rev-list --first-parent --min-parents=2 --max-count=1 HEAD)`, which is fact 1 of
  `check_prepared_merge` (`tools/push-main.sh:514-516`), and walks `$t^1..$t^2`. Its header reads
  `version oracle: <t8>^1..<t8>^2 · <n> commits`. 44 S1, §4 and AC1 are restated to it, with no
  subject match on HEAD and no `origin/main` form (F1). Observed by AC17.
- **S18** — finding 20 (M10). 43 S19 and its sketch "The bounded call (S19)" are rewritten to the
  helper 49 S21 and S22 build: `run_driver_bounded <bound> <verb args>`, output in `RDB_OUT` and
  `RDB_ERR`, the skip reason in `RDB_WHY`, and no line printed of its own. 49's spec-edit list names
  S21 and S22. Observed by AC18.
- **S19** — finding 21 (M11). A skip is signalled by `RDB_WHY` alone. `run_driver_bounded` empties it
  on entry and sets it on each of the four skips today's `derive_claims_line` prints: no conf
  (`skills/session-kickoff/manifest-check.sh:648`), no driver (`:650`), no `timeout -k` (`:651-652`)
  and no scratch directory (`:653-654`). Every caller branches on `RDB_WHY` being non-empty and never
  on rc 125, 126 or 127, so a driver's own 126 or 127, or `timeout`'s 125, reaches the caller's failure
  branch (`:689`). 49 S21 and its §4 sketch are restated to it. Observed by AC19.
- **S20** — finding 32 (M12). 49 S6's trap clears a lock with no `owner` only when this subshell's own
  `mkdir` succeeded (`_fl_mine` set) and no `<lock>.break` guard exists; it clears a lock whose `owner`
  reads this token; it leaves every other lock. A breaker holds that guard from before its `rm -rf`
  until after it writes `owner` (`tools/unattended/unattended.sh:2335-2350`, inherited by
  `write_node_lock`), so its window is never cleared. 49 §5's security line is restated to name the one
  window this leaves, as this unit's §5 states it. Observed by AC20.
- **S21** — finding 34 (M13). 47's sighted test is a shape test: `seen-utc` matches the ISO pattern
  `read_claims` applies to `beat-utc` (`tools/unattended/unattended.sh:2165`), spelled with repeated
  classes as there. A value that fails it takes 47 S2's unsighted outcomes. 47 S1 and §4 are restated
  and the built `awk` carries the test. Observed by AC21.
- **S22** — finding 36 (M14). One merged walk. 47 §4 states the stop list whole: tip unsighted, then
  epoch, then `renews -`, then `renews yes` or absent, then the sighted threshold, then read on. 46
  §4's walk becomes a pointer to it, and 46's and 47's Edges name each other. The built `awk` carries
  every stop in that order, and 46's and 47's arms re-run at this unit's pass. Observed by AC22.
- **S23** — finding 8 (L2). `TOOL-dPlacedRequest-33` §5's risks line names `CARD_PUBLISH_BOUND` as a
  publish's wait. Observed by AC23.
- **S24** — finding 26 (L2). 49 S1's re-point list names 33 §5's risks line beside 33 S2 and its
  sketch. Observed by AC24.
- **S25** — finding 9 (L3). 46 AC3 gains a row for a value outside the four: a `renews: maybe` tip
  sighted a minute ago over a `renews: no` commit of its tenure sighted 1,000 hours ago prints `stale`.
  46 S2 names it. Observed by AC25.
- **S26** — finding 35 (L3). An empty `renews` value, `renews:` or `renews: ` with nothing after it,
  is outside the four and reads on as `no` does, because only a missing key marks a legacy claim. The
  walk reads the key on a line beginning `renews:`, its value trimmed, so both spellings read alike. 46
  S2 states it and AC3 gains both rows in S25's shape. Observed by AC26.
- **S27** — finding 15 (L4). 48 AC2 is restated as a regression check of `TOOL-dPlacedRequest-30` S1's
  byte compare, its `Red when:` the scratch driver without that compare. The lock's observation stays
  on 48 AC1. Observed by AC27.
- **S28** — finding 27 (L6). 44 AC4 reads 43 before its revision log and greps `git log
  --first-parent`, never the bare token, so an honest §9 line naming the earlier walk does not red it.
  Observed by AC28.

## 3. Non-goals (OUT)

- No second mechanism for a high: units 50 and 51 own findings 1 and 10. S14 reads 45 AC2 as unit 51
  leaves it.
- No renumbering of any order: a promotion's order is set when it is added, and at order 27 a moved
  number moves nothing already built. S1 and S9 carry the order gap in text instead.
- No new gate leg, no lint over spec criteria and no new bug-class record: each arm joins an existing
  suite, and each class the review names already has its record under `memory/gotchas/`.
- No change to `NODE_LOCK_BOUND`'s value or to how a lock is broken: `TOOL-dPlacedRequest-37`'s and
  `TOOL-dPlacedRequest-24`'s.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-33` — §5's risks line, which S23 re-points
- **consumes-from** `TOOL-dPlacedRequest-34` — AC59's observation, which S11 restates
- **consumes-from** `TOOL-dPlacedRequest-36` — AC3, which S7 points at unit 38's carrier arm
- **consumes-from** `TOOL-dPlacedRequest-37` — `NODE_LOCK_BOUND`, which S2 names as the race's margin and S4 reads as its discard bound
- **consumes-from** `TOOL-dPlacedRequest-38` — the carrier arm's population and §3, which S7 and S8 make the one carriage check
- **consumes-from** `TOOL-dPlacedRequest-43` — S19 and its sketch, S22, AC22 and S30, which S5, S9 and S18 amend
- **consumes-from** `TOOL-dPlacedRequest-44` — the oracle, its fixture and AC1, AC3 and AC4, which S11 to S14, S17 and S28 amend
- **consumes-from** `TOOL-dPlacedRequest-45` — AC2's fixture, which S14 states by count
- **consumes-from** `TOOL-dPlacedRequest-46` — the walk, S2 and AC3, which S22, S25 and S26 amend
- **consumes-from** `TOOL-dPlacedRequest-47` — the sighted test and the walk, which S21 and S22 amend
- **consumes-from** `TOOL-dPlacedRequest-48` — the placed-race arm and S1, S2, AC2 and AC4, which S1 to S4, S6, S15 and S27 amend
- **consumes-from** `TOOL-dPlacedRequest-49` — S1, S3, S6 to S8, S13, S21, AC7, AC13, AC24, AC30, AC31 and §5, which S7 to S11, S16, S18 to S20 and S24 amend, and S25's retry, which S1 reads as the placed race's bound
- **hands-off** `TOOL-dPlacedRequest-53` — AC1, AC6 and AC9, which that unit rewrites to count occurrences
- **hands-off** `TOOL-dPlacedRequest-54` — the oracle's S12, S17, §4 sketch, AC12, fixtures and F1, which that unit gives the own-merge test
- **hands-off** `TOOL-dPlacedRequest-55` — S11's verdict and §4's sketch, which that unit makes read the walk's status, and a new AC29
- **hands-off** `TOOL-dPlacedRequest-56` — §6's `flat` note, the race arm, AC14, AC15, AC19, AC21, AC26, S14, S26, Edges and F1, which that unit's minors amend
- **hands-off** `TOOL-dPlacedRequest-58` — S4 and §4's race sketch as unit 56 restates them, in which that unit keeps the handshake clear
- **hands-off** `TOOL-dPlacedRequest-59` — AC12, AC29, §4's oracle and the hands-off edge to 53, which that unit's items for findings 3, 6, 9 and 21 amend
- **hands-off** `TOOL-dPlacedRequest-63` — AC11 to AC14 and AC17, which that unit's item for finding 1 gives the fixture's base
- **hands-off** `TOOL-dPlacedRequest-64` — the `### The oracle (S11 to S13, S17)` heading, which that unit's item for finding 19 names as the prefix of 59 AC13's section read

## 4. Design

### The oracle (S11 to S13, S17)

```bash
t=$(git rev-list --first-parent --min-parents=2 --max-count=1 HEAD)
[ -n "$t" ] || { echo "version oracle: no prepared merge on HEAD"; exit 2; }
r="$t^1..$t^2"
n=$(git rev-list --no-merges --invert-grep --grep='^mint:' --count "$r")
echo "version oracle: ${t:0:8}^1..${t:0:8}^2 · $n commits"
[ "$n" -gt 0 ] || { echo "version oracle: walked no commit of the build"; exit 2; }
if git log --no-merges --invert-grep --grep='^mint:' -p "$r" \
     -- tools/unattended/unattended.sh tools/run-gates/run-gates.sh \
     | grep -E '^[+-]KIT_(UNATTENDED|RUN_GATES)_VERSION='; then exit 1; fi
exit 0
```

Measured 2026-10-25 on node a in a fixture repository under `%TEMP%` built as S14 states: the
derivation found the merge from the merge itself and from a single-parent `records: close` commit
stacked on it, `$t^1..$t^2` listed `b2` and `bump`, the bump walk's `grep` exited 0 and an empty
`$t^1..$t^1` walk's `grep` exited 1, which is the inversion S11 ends.

### The walk, per tail, merged (S21, S22)

```
per tail, tip first, tip included:                           sighted = seen-utc matches the ISO shape
  tip not sighted                       -> resolve unknown, age -                         (47 S2)
  tip                                   -> tenure epoch = its epoch (absent reads 0)
  epoch != tenure epoch                 -> tenure ended: resolve by 35 S2
  renews -                              -> never-stale: live from its sighting, unknown if not sighted   (46 S1)
  renews yes, or no renews key          -> renewing beat: not sighted ? unknown : age from its sighting
  sighted and seen-utc < threshold      -> resolve stale                                  (47 S1)
  else (no, empty, any other value)     -> oldest-of-tenure = this commit, read on        (46 S2)
chain or tenure ended                   -> 35 S2's fallback; an oldest not sighted reads unknown
```

### The out-of-set rows (S25, S26)

A one-commit tenure sighted 1,000 hours ago reads `stale` whether its value is read as `no` or as a
renewing beat, so such a row cannot fail. The rows here put the value on a fresh tip over an old
`renews: no` commit: read as `no`, the tail ages from the old commit and prints `stale`; read as a
renewing beat or as `-`, it prints `live`.

### The placed race, bounded (S1 to S4)

```
attempt 1..3:
  A in background; wait for $h/held (30 s bound) -> stamp th, or record "never placed"
  B to its end -> stamp tb; read the health log for node-lock-broken on requests.lock
  touch $h/release; wait for A (bound); clear $h/once $h/held $h/release
  tb - th <= NODE_LOCK_BOUND and no break event -> judge AC1's asserts, stop
  else -> discard this attempt
every attempt overran -> fail "request race placed past the lock bound"
```

### Files touched (estimate)

- `tools/unattended/unattended.sh`: S5's copy, S21 and S22's walk
- `tools/lib/gov-feed.sh`: S20's trap, with its carried copies in `tools/unattended/unattended.sh`,
  `tools/run-gates/post-merge.sh` and `tools/push-main.sh`
- `tools/unattended/unattended.test.sh`: the arms of §7
- `tools/lib/resolve-python.test.sh`: S7's population
- `skills/session-kickoff/manifest-check.sh` and `skills/session-kickoff/manifest-check.test.sh`: S19
- `memory/builds/dPlacedRequest/spec/`: the specs of units 33, 34, 36, 37, 38, 43 to 49, each edit a
  rev bump with its §9 line

### Alternatives rejected

- **Two batches.** S5, S21 and S22 write `tools/unattended/unattended.sh`, S20 writes a block carried
  into it, and S1 to S4, S20 to S22 and S25 to S27 write `tools/unattended/unattended.test.sh`, so no
  split gives M6 two disjoint write sets.
- **The review's literal out-of-set rows (S25, S26).** A lone commit sighted 1,000 hours ago reads
  `stale` both ways, so the row passes on the defect it exists to catch.
- **Release A once B makes its first lock attempt (finding 23's second fix).** The PATH stub sees only
  `cp`, not B's lock attempt, so the arm would need a hook in the driver.

## 5. Production-readiness checklist

- security — S20 narrows the trap to locks this writer took; the one window left is a third writer's
  own `mkdir`-to-`owner` window after a peer broke this writer's lock and released it, reachable only
  by an append that outlives `NODE_LOCK_BOUND` and a full peer cycle, and 49 §5 names it. S21 closes a
  take-over a torn stamp would permit.
- perf / scale — S4 runs at most three placements; the oracle is two `git` walks at the close.
- error / empty / loading states — S12 and S13 give every refusal exit 2 with a named line; S19 gives
  every skip a reason.
- observability — S3's output names the break event; the oracle's header names the merge it read.
- risks — S5 binds the copy's form; a `--request` built otherwise is changed, which 48's stub needs.
- testing — the probes of §6 and the arms of §7.
- migration — none: every surface is new in this build.
- user docs — none beyond the specs: no user-facing behaviour changes.

## 6. Acceptance criteria

`flat <file>` below is `sed '/^## 9\./,$d' <file> | tr -s '[:space:]' ' '`: the file before its
revision log, whitespace squeezed, so a wrapped phrase and an honest revision line read alike. The
fixtures are the named units': unit 26's chains for the walk, unit 19's clones for requests, unit 38's
scratch carriers for the block, unit 2's card store for the engine, and S14's repository under
`%TEMP%` for the oracle, each `RUN_CLAIMS=on` unless stated.

- **AC1** — When the placed-race arm runs over a scratch driver whose `requests.lock` wait has no
  bound, it fails with `request race placed past the lock bound`; over the built driver it passes, and
  `flat 2026-10-25-spec-TOOL-dPlacedRequest-48.md | grep -c 'S25'` prints at least 2. Red when: an
  unbounded wait reads as an unserialised lock.
- **AC2** — When `flat 2026-10-25-spec-TOOL-dPlacedRequest-48.md | grep -o 'NODE_LOCK_BOUND[^.]*'`
  runs, it names 10 s and the 5 s retry, and 48's and 37's Edges carry the paired edge. Red when: the
  arm's timing rests on a deadline 48 does not name.
- **AC3** — When a stub delays B by 11 s after `held` on a locked build, the arm's output names
  `node-lock-broken`. Red when: a stale break is reported as a lock that does not serialise.
- **AC4** — When that delay applies to the first attempt only, the arm discards it and passes; when it
  applies to every attempt, the arm fails `request race placed past the lock bound`; after either, no
  `--request` process of the arm remains. Red when: an overrun reads as a lock defect or leaves A
  waiting.
- **AC5** — When the `--request` body of `tools/unattended/unattended.sh` is extracted and grepped for
  `cp -- `, one line names `requests/`, and `flat 2026-10-25-spec-TOOL-dPlacedRequest-43.md` names the
  spawn in S30. Red when: the copy is a redirect, a `mv` or a Python write that 48's stub never sees.
- **AC6** — When `flat 2026-10-25-spec-TOOL-dPlacedRequest-48.md | grep -c '43 S30'` runs, it prints
  at least 2, S1 and §5 risks. Red when: the stub keys on a spawn no writer spec mandates.
- **AC7** — When 38's carrier arm lists its population over the real tree, `gov-feed.sh`, the file
  `TOOL-dPlacedRequest-13` creates, is not in it and the arm passes, and 36 AC3 names 38's arm. Red when: the canonical joins the population
  and a correct tree reds.
- **AC8** — When `flat 2026-10-25-spec-TOOL-dPlacedRequest-38.md | grep -c 'No check that a carrier holds'`
  runs, it prints 0, and 49 S8 names `§3`. Red when: 38's non-goal contradicts its own arm.
- **AC9** — When `gen_build_index.py --write` has rendered and `wc -c` reads unit 34's spec, it prints
  at most 48128, and `flat 2026-10-25-spec-TOOL-dPlacedRequest-43.md | grep -c 48128` prints at least
  2. Red when: S22 and AC22 state different ceilings.
  figure: 48128 DERIVED as 49152 less 1024, 49 S13's derivation.
- **AC10** — When `flat 2026-10-25-spec-TOOL-dPlacedRequest-43.md | grep -c 47104` runs, it prints 0,
  and 49 AC13 names that count. Red when: the old figure stands in 43 outside its revision log.
- **AC11** — When the oracle runs on S14's fixture, it prints both `KIT_UNATTENDED_VERSION` lines and
  exits 1; on the same shape with no bump commit, it prints the header alone and exits 0. Red when: a
  clean build exits non-zero or a bump exits 0.
- **AC12** — When the oracle runs in a fixture repository with no merge on HEAD's first-parent line
  and no remote, it prints `no prepared merge on HEAD` and exits 2. Red when: an unreadable range
  prints `walked no commit of the build`.
- **AC13** — When the oracle runs on a merge built by `git commit-tree -p <tip> -p <base>`, whose
  second parent is an ancestor of its first, it prints `walked no commit of the build` and exits 2.
  Red when: the empty walk and the clean walk share a status.
- **AC14** — When S14's fixture is built and the oracle runs, its header ends `· 2 commits`, and
  `flat` of 44 and of 45 each names `two branch commits`. Red when: two specs describe the shared
  fixture with different counts.
- **AC15** — When S15's extraction runs over 43, the output contains `TOOL-dPlacedRequest-48` and not
  `two background`; over 43 at rev-3, read by `git show`, it contains `two background`. Red when: the
  check reads the hands-off edge at 43's `:168` instead of AC30.
- **AC16** — When 49 AC24's squeezed grep runs over the specs of units 36 to 39, each prints at least
  1, and AC31's squeezed form finds `well under a second` in a scratch copy of 38 that wraps it across
  two lines. Red when: a wrapped phrase escapes the grep.
- **AC17** — When a single-parent `records: close` commit is stacked on S14's merge and the oracle
  runs, the header names `<t8>^1..<t8>^2` with `· 2 commits` and the bump lines print. Red when: the
  oracle keys on HEAD's subject and falls to another range.
- **AC18** — When `flat 2026-10-25-spec-TOOL-dPlacedRequest-43.md | grep -c 'run_driver_bounded <cell>'`
  runs, it prints 0, and 49's spec-edit list names S21 and S22. Red when: 43 states the old signature.
- **AC19** — When `derive_claims_line` runs in a scratch tree whose resolved `unattended.sh` is a stub
  printing `FAILED: boom` and exiting 127, the cell prints `claims — skipped: FAILED: boom`; with
  `CARD_DIR` unwritable, it prints the `no scratch directory` line. Red when: rc 127 reads as "no
  driver", or the scratch skip prints nothing.
- **AC20** — When a plant sets `_fl_mine`, stages a peer's break (`mkdir <lock>.break`, `rm -rf
  <lock>`, `mkdir <lock>`, no `owner`) and the subshell exits, the lock directory survives; with no
  `.break` and no `owner`, it is cleared. Red when: the trap clears a lock a breaker holds.
- **AC21** — When the renewing beat's feed line carries `2026-10-2`, `--claims` prints `unknown` with
  age `-`; when a `renews: no` middle commit carries it under a tip and a start sighted a minute ago,
  it prints `live`. Red when: a torn stamp sorts below the threshold and reads `stale`.
- **AC22** — When 46's and 47's arms run over the built driver, all their rows pass; a scratch copy
  without the `renews -` stop reds 46 AC1, and one without the unsighted-tip stop reds 47 AC2.
  Red when: the second pass's walk lost the first pass's stop.
- **AC23** — When `flat 2026-10-25-spec-TOOL-dPlacedRequest-33.md | grep -c CARD_FETCH_BOUND` runs, it
  prints 0, and §5 names `CARD_PUBLISH_BOUND`. Red when: 33 names two bounds for one publish.
- **AC24** — When 49's S1 paragraph is extracted by `awk '/^- \*\*S1\*\*/{f=1} f&&/^- \*\*S2\*\*/{exit} f'`
  and squeezed, it names `§5`. Red when: an amendment's re-point list skips a line naming the old
  bound.
- **AC25** — When the `renews: maybe` row runs, `--claims` prints `stale`; a scratch copy reading an
  unknown value as a renewing beat prints `live`. Red when: a value outside the four hides an expiry.
- **AC26** — When the `renews:` and `renews: ` rows run, both print `stale`. Red when: an empty value
  reads as a legacy renewing beat and prints `live`.
- **AC27** — When 48's third call runs over a scratch driver without unit 30's byte compare, it exits 0
  and the stored copy is `b.md`; over the built driver it exits 2 printing `collision`. Red when: AC2
  names a break it cannot stage.
- **AC28** — When `flat 2026-10-25-spec-TOOL-dPlacedRequest-43.md | grep -c 'git log --first-parent'`
  runs, it prints 0, and over a scratch copy whose §9 names the earlier `--first-parent` walk it still
  prints 0. Red when: an honest revision line reds the criterion.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `python resolver (behaviour + inline parity + idiom ban)` · `unattended kit gate` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `govkit selfcheck` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `manifest-check self-test` · `scratch-guard self-test` · `push-main self-test`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC3 AC4 AC20 AC21 AC22 AC25 AC26 AC27 · each item's plant, staged against the unit it amends as written · waived for this build's landing by README rule 8, so its clean reading is owed with PLAY-dClosedLoop-14
New arm: tools/lib/resolve-python.test.sh · covers AC7 · the real tree's population, staged against a pathspec without the canonical's exclude · none
New arm: skills/session-kickoff/manifest-check.test.sh · covers AC19 · a stub driver exiting 127 and an unwritable `CARD_DIR`, staged against callers that branch on rc 125 to 127 · none

## 8. Open questions

- **F1 — How does the oracle find its range (S12, S17)?** (a) The lander's fact-1 derivation alone,
  refusing with exit 2 when no merge is found; (b) (a) gated on `push-main.sh --prepared`; (c) (a)
  with a merge-base fallback whose remote comes from `tools/lib/resolve-remote.sh`. (b) reads the
  remote's advertised tip, which a fixture lacks and a read of local history does not need; (c)
  sources a canonical whose header says its test alone sources it (`tools/lib/resolve-remote.sh:3-7`),
  for a fallback no caller runs, since 44 §5 and the README's close rule run the oracle once, on the
  prepared merge. All three meet every criterion written. RESOLVED (agent, 2026-10-25, delegated):
  (a), rung 3, the fewest open questions, and the seam `check_prepared_merge` found. widens: none ·
  relaxes: none
- **F2 — Which ownerless lock may S6's trap clear (S20)?** (a) One this subshell's `mkdir` made, with
  no `.break` guard present; (b) one whose directory identity, read by `stat`, matches the one made;
  (c) none. (b) rests on inode numbers under Git Bash on NTFS, unmeasured here; (c) leaves 49 AC6's
  abort holding the lock for two minutes. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the
  review's fix judged sound, with its residual stated in §5. widens: none · relaxes: none
- **F3 — How does the placed race stay inside the lock bound (S1 to S4)?** (a) Stamp, discard and
  re-place up to three times; (b) release A once B makes its first lock attempt; (c) order 48 after
  49. (b) needs a driver hook; (c) renumbers a built unit and moves nothing at order 27. RESOLVED
  (agent, 2026-10-25, delegated): (a), rung 3, the skeptic's corrected fix for finding 31, with
  finding 23's health-log read as its cause line. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, the batch of the spec audit of the round-3 promotions' 20
  MEDIUM and 8 LOW findings.
- rev-2 · 2026-10-25 · the promoted fix brief's gate hits: AC7 cites `gov-feed.sh` by basename, the
  file `TOOL-dPlacedRequest-13` creates; AC22's red case on one `Red when:` line.
- rev-3 · 2026-10-25 · §3 · the disposal of the spec audit of the round-4 promotions: the hands-off edges to `TOOL-dPlacedRequest-53`, `TOOL-dPlacedRequest-54`, `TOOL-dPlacedRequest-55`, `TOOL-dPlacedRequest-56`, mirroring their consumes-from.
- rev-4 · 2026-10-25 · §3 · the disposal of the spec audit of the round-5 promotions: the hands-off edges to `TOOL-dPlacedRequest-58` and `TOOL-dPlacedRequest-59`, mirroring their consumes-from.
- rev-5 · 2026-10-25 · §3 · the disposal of the spec audit of the round-7 promotions: the hands-off edge to `TOOL-dPlacedRequest-63`, mirroring its consumes-from.
- rev-6 · 2026-10-25 · §3 · the disposal of the spec audit of the round-8 promotions: the hands-off edge to `TOOL-dPlacedRequest-64`, mirroring its consumes-from.

## 10. Reuse audit

Each item extends the unit its finding names, and the new code reuses four seams: the lander's
prepared-merge derivation (`check_prepared_merge`, `tools/push-main.sh:514-516`) for S17, the strict
ISO pattern of `read_claims` (`tools/unattended/unattended.sh:2165`) for S21, the parity loop's
pathspec and exclude (`tools/lib/resolve-python.test.sh:218`) for S7, and the claim-push factory's
`.break` guard (`tools/unattended/unattended.sh:2335-2350`) for S20.
`python tools/codebase-map/reuse_lookup.py "a fixture that reaches a guard past every earlier stop in
the age walk"` ranked `walk`, `fixture` and `build_fixture`, name stems only, `fixture` being the
suite these arms join. `python tools/memory-recall/query.py "how is a spec audit's minor findings
batch promoted into one unit that amends several specs"` returned TOOL-aDistilledCharter-7,
`TOOL-dPlacedRequest-49`, TOOL-aGraftedHelix-32 and the dFairHearing round-3 batch's departure record,
batches of the same kind; none disagrees with source.

Recall terms used: minors batch promote medium low spec audit round finding item amend in place edge mirror
