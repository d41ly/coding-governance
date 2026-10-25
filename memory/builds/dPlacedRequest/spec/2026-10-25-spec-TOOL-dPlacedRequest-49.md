# TOOL-dPlacedRequest-49 — the round-2 promotions' minors: one bound per question, traps before takes, every carrier observed, and criteria that can fail

**Status:** DEFERRED · rev-3 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 26 · advances TOOL-dPlacedRequest-22

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-44-promoted-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-44-promoted-fix-return.md) | research | TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 |
| [2026-10-25-build-TOOL-dPlacedRequest-49-deviation-491.md](../build/2026-10-25-build-TOOL-dPlacedRequest-49-deviation-491.md) | deviation | — |
| [2026-10-25-prompt-TOOL-dPlacedRequest-44-promoted-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-44-promoted-fix-brief.md) | research | TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 |
| [2026-10-25-review-TOOL-dPlacedRequest-44-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-44-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-48 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-2 promotions
(`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-35-spec-audit.md`)
exited BOUNDED with 39 confirmed findings. Its blocker and four highs are units 44 to 48. This unit
is the batch BUILD-METHOD M4 makes of the rest: 22 MEDIUM and 12 LOW findings by raw id, one scope
item per id, each naming its finding and, in brackets, the review item holding it (M1 to M18, L1 to
L12). Five items hold more than one id (M1: 1 and 22; M3: 9, 14 and 34; M4: 11 and 35; M5 with L1:
15 and 39; M6 with L2: 36 and 7); each id still gets its own item and its own observation. The
minors land on twelve units, so this unit repairs none in particular and sits above every unit of the
build, at order 26, after units 44, 45 and 48 at 25. Criterion ACn observes item Sn.

| Item | Finding | Severity | Lands on |
|---|---|---|---|
| S1, S2 | 1, 22 (M1) | MEDIUM | units 33, 43 |
| S3 | 5 (M2) | MEDIUM | unit 34 |
| S4, S5, S6 | 9, 14, 34 (M3) | MEDIUM | units 24, 39 |
| S7, S8 | 11, 35 (M4) | MEDIUM | units 36, 38 |
| S9, S10 | 15 (M5), 39 (L1) | MEDIUM, LOW | units 36, 37, 38 |
| S11, S12 | 36 (M6), 7 (L2) | MEDIUM, LOW | units 41, 42, 43 |
| S13, S14 | 4 (M7), 19 (L3) | MEDIUM, LOW | unit 43 |
| S15, S16 | 20 (M8), 25 (L4) | MEDIUM, LOW | unit 43 |
| S17 to S23 | 2, 3, 8, 10, 23, 28, 24 (M9 to M15) | MEDIUM | units 2, 38, 43 |
| S24 | 27 (M16) | MEDIUM | units 36 to 39 |
| S25 | 37 (M17) | MEDIUM | units 37, 43 |
| S26 | 38 (M18) | MEDIUM | unit 41 |
| S27 to S34 | 6, 12, 13, 17, 18, 29, 30, 31 (L5 to L12) | LOW | units 36, 37, 38, 40, 43 |

## 2. Scope (IN)

- **S1** — finding 1 (M1). The card publish has its own bound: `CARD_PUBLISH_BOUND=${CARD_PUBLISH_BOUND:-140}`
  beside `CARD_CLAIMS_BOUND` (`skills/session-kickoff/manifest-check.sh:228`), read by the
  `--card-ref write` call alone. `TOOL-dPlacedRequest-33` S2 and its sketch name it, and
  `TOOL-dPlacedRequest-43` S16, AC16 and AC17 are re-pointed at it. Observed by AC1.
- **S2** — finding 22 (M1). The lookup keeps a reader's bound: `CARD_FETCH_BOUND=${CARD_FETCH_BOUND:-15}`,
  at most `CARD_CLAIMS_BOUND`, bounds `TOOL-dPlacedRequest-2` S6's fetch and `TOOL-dPlacedRequest-34`
  S11's `--card-ref lookup`, inside TOOL-aGraftedHelix-2's 15 s kill bound for a remote read
  (`memory/DECISIONS.md:218`). Neither read spells `CARD_PUBLISH_BOUND`. Observed by AC2.
- **S3** — finding 5 (M2). `TOOL-dPlacedRequest-34` AC59 is rewritten in place to run
  `TOOL-dPlacedRequest-44`'s §4 oracle, so the build carries one version-bump oracle and no
  `git diff` from the fixed base. Observed by AC3.
- **S4** — finding 9 (M3). `TOOL-dPlacedRequest-39` AC1 and its §4 agree: the `EXIT` trap is armed
  before `write_node_lock` runs (S6), so AC1's plant "directly after the lock take" sits under the
  trap, and §4's sketch shows that order. Observed by AC4.
- **S5** — finding 14 (M3), the skeptic's corrected fix. `write_node_lock` writes `owner` first and
  `until` second, on the first take and on the re-take after a break, so a taken lock always carries
  its token and `remove_node_lock` can match it. Observed by AC5.
- **S6** — finding 34 (M3). In `add_feed_event`'s subshell the `EXIT` trap is installed before
  `write_node_lock` and acts only when `_fl_mine` is set; `write_node_lock` sets `_fl_mine=1` in the
  same shell right after its own successful `mkdir`. The trap clears the lock directory when
  `_fl_mine` is set and `owner` is absent or reads this token. `TOOL-dPlacedRequest-39` S2 states the
  order, and its §3 "any such name, present or future" is narrowed to the windows the trap covers.
  Observed by AC6.
- **S7** — finding 11 (M4). `TOOL-dPlacedRequest-36` S2 reads "inline or sourced", and its AC3 is
  restated over the population: for every file `git grep -l '^# >>> gov_feed_sh' -- '*.sh'` lists,
  that file, or the one file it sources (`unattended.sh` sources `lib-unattended.sh` at `:101`),
  carries `^# >>> health_log_sh`; a miss names the file, and an empty population fails. Observed by
  AC7.
- **S8** — finding 35 (M4). `TOOL-dPlacedRequest-38`'s carrier arm sources each carrier's own
  `health_log_sh` cut, or its sourced library's for `unattended.sh`, never the canonical, and fails
  `<file>: no health_log_sh beside gov_feed_sh` when the carrier holds none, so
  `tools/push-main.sh`'s carriage (`TOOL-dPlacedRequest-15`) is graded by a standing arm. Observed by
  AC8.
- **S9** — finding 15 (M5). The `env -i` probes of `TOOL-dPlacedRequest-36` AC1 and AC2 and
  `TOOL-dPlacedRequest-37` AC1 pass `c="$c"`, and the commit `h="$h"` where read, through `env -i`, so
  the green case reaches the factory. Observed by AC9.
- **S10** — finding 39 (L1). The carrier arm of `TOOL-dPlacedRequest-38` in
  `tools/lib/resolve-python.test.sh` runs `env -i PATH="$PATH" HOME="$HOME" c="$c" h="$h" bash -c`.
  Observed by AC10.
- **S11** — finding 36 (M6). Every reader and writer of the queue line's tip field goes through
  `derive_queue_tip`: `add_gov_queue`'s newest-line lookup and base (`TOOL-dPlacedRequest-41` S1),
  `write_gov_queue`'s per-ref chain and compare-and-swap (41 S3, `TOOL-dPlacedRequest-24` S4 and
  S5) and the offline create's empty-tip line (`TOOL-dPlacedRequest-42` S2); `TOOL-dPlacedRequest-43`
  S8's Readers line names them. **Readers:** by name: READER NOT IN TREE, since every reader is
  minted in this build by units 1, 24, 41 and 42. by value: NO VALUE READERS, since each reaches the
  value only through `derive_queue_tip`. Observed by AC11.
- **S12** — finding 7 (L2). `TOOL-dPlacedRequest-43` AC8's dedupe half is recast to observe the
  encoding: a flush of a `-` line creates the ref, and a scratch copy whose compare-and-swap reads
  `-` literally fails to push. Observed by AC12.
- **S13** — finding 4 (M7). `TOOL-dPlacedRequest-43` AC22's ceiling is set from a measurement:
  unit 34 measures 49053 bytes at rev-5, PINNED 2026-10-25, the named cuts take about 1.8 KB and the
  named additions add about 0.5 KB, so the ceiling is 48128, 1 KiB under the 49152 spec ceiling,
  DERIVED. Observed by AC13.
- **S14** — finding 19 (L3). `TOOL-dPlacedRequest-43` §4's pinned 50111 names the commit it was
  measured at, `dfb9b0d3`, beside the rev-5 figure. Observed by AC14.
- **S15** — finding 20 (M8). `TOOL-dPlacedRequest-43` §4's scratch-guard evidence names `readCard`
  (`tools/hooks/scratch-guard.js:667`), which spawns nothing at the base, its bash spawn added by
  `TOOL-dPlacedRequest-34` S28, and states that `:710` is `checkAuthorizedReadme`'s `runGit`, which
  takes no bound. Observed by AC15.
- **S16** — finding 25 (L4). `readCard`'s bound is a named constant, `CARD_READ_BOUND_MS = 5000`,
  with a `SCRATCH_GUARD_CARD_READ_BOUND_MS` override for the arm, shaped as `runLiveness`
  (`tools/unattended/stop-guard.js:106-114`): `timeout: bound, killSignal: 'SIGKILL'`. Observed by
  AC16.
- **S17** — finding 2 (M9). `TOOL-dPlacedRequest-43` AC6's static half reads the surface that holds
  the cause list, `help/loop.md`, and its §5 user docs name that page. Observed by AC17.
- **S18** — finding 3 (M10). `skills/session-kickoff/card-store.fixture.sh --plant publish-late` runs a
  stub driver that writes the ref and sleeps past `CARD_PUBLISH_BOUND=2`; `TOOL-dPlacedRequest-43`
  §4 Files touched and §7 name the file and its arm. Observed by AC18.
- **S19** — finding 8 (M11). `TOOL-dPlacedRequest-43` AC15 plants the run-state `prior-session` fact
  naming the record's session and the matching `keepalive` fact before it expects `same`, the
  take-over row at `tools/unattended/unattended.sh:2263`. Observed by AC19.
- **S20** — finding 10 (M12). `TOOL-dPlacedRequest-38`'s arm commits once in its scratch repository,
  passes that sha to `add_feed_event`, and asserts `gov-feed.log` gained one line. Observed by AC20.
- **S21** — finding 23 (M13). `run_driver_bounded` prints nothing of its own: a skip returns a code
  per reason with the reason in `RDB_WHY`, and each caller prints its own unchanged line,
  `overlaps — skipped:`, `claims — skipped:`, `card — remote-ref not written:`, or the lookup's
  quiet fall-through to the next store. Observed by AC21.
- **S22** — finding 28 (M14). `run_driver_bounded` captures stderr to `$RDB_ERR` beside `$RDB_OUT`,
  and `derive_claims_line`'s failure branch reads both, as it reads `$sd/out` and `$sd/err` today
  (`manifest-check.sh:655`, `:690-695`). Observed by AC22.
- **S23** — finding 24 (M15). `TOOL-dPlacedRequest-43` AC20's probe runs under
  `env -u GOV_NODE -u USER USERNAME=<row user>`, since `resolve_node_tag` answers `GOV_NODE` first
  (`tools/run-gates/run-selftests.sh:294`), with a second case where `GOV_NODE` names a registered
  tag and all three resolvers print it. Observed by AC23.
- **S24** — finding 27 (M16). `TOOL-dPlacedRequest-36`, `-37`, `-38` and `-39` each state in §4 that
  their write sets meet in `tools/lib/gov-feed.sh` and its carriers, and that their passes run in
  sequence despite the shared order 5, as `--dispatch` enforces. Observed by AC24.
- **S25** — finding 37 (M17). `--request` retries `requests.lock` every 50 ms for up to 5 s, as
  `TOOL-dPlacedRequest-24` S2's two callers do; a lock it cannot take prints `request not written —
  requests.lock busy`, exits 2 and writes nothing. `TOOL-dPlacedRequest-37` S1 names the request
  section among those `NODE_LOCK_BOUND` covers. Observed by AC25.
- **S26** — finding 38 (M18), the skeptic's corrected fix. `TOOL-dPlacedRequest-41`'s offline write
  refuses when the newest queued line's commit is absent under `git cat-file -e` or the line fails the
  four-field shape: one `queue: NOTE - <ref>: queued commit unreadable; nothing queued` line, exit 2,
  nothing appended. Queued commits stay out of every ref. Observed by AC26.
- **S27** — finding 6 (L5). `TOOL-dPlacedRequest-43` AC21 observes S21's content: the `RUN_CLAIMS` row
  of `tools/unattended/PROTOCOL.template.md` names no `refs/gov/` path and cites `UNATTENDED-STOPS.md`
  §7, with the size clause kept as its second half. Observed by AC27.
- **S28** — finding 12 (L6). The exempt `status` act of `TOOL-dPlacedRequest-40` S2 has its own
  criterion there: an id-less `--lease status` exits 0. Observed by AC28.
- **S29** — finding 13 (L7). `TOOL-dPlacedRequest-43` AC25 runs one `grep -c` per event and requires
  each at least 1. Observed by AC29.
- **S30** — finding 17 (L8). `TOOL-dPlacedRequest-36`'s Goal states the stale-break outcome as the
  code gives it: `post-merge.sh` runs `set -u` (`:26`) with no errexit, so the event is lost and two
  error lines reach stderr while the carrier carries on; the abort is `TOOL-dPlacedRequest-37`'s
  `REMOTE_BOUND` arithmetic. Observed by AC30.
- **S31** — finding 18 (L9). `TOOL-dPlacedRequest-38` §5 perf states the arm's time measured once on
  a Windows node when built, with the node and the date, in place of "well under a second". Observed
  by AC31.
- **S32** — finding 29 (L10). `TOOL-dPlacedRequest-38`'s arm lists its population with the parity
  loop's pathspec and exclude (`tools/lib/resolve-python.test.sh:218`), so a Markdown record quoting
  the marker never joins it. Observed by AC32.
- **S33** — finding 30 (L11). `TOOL-dPlacedRequest-37` S1 lists every section `NODE_LOCK_BOUND`
  covers, the feed append (39), the offline write (41), the offline create (42) and the request copy
  (43 S30), and justifies 10 s against the longest, measured once on node a. Observed by AC33.
- **S34** — finding 31 (L12). `TOOL-dPlacedRequest-43` S26 and AC26 read every event token passed to
  `add_health_event` in the driver and the `gov_feed_sh` block, and `tools/unattended/README.md`'s
  event sentence (`:246-252`) names `lease-yielded`. Observed by AC34.

## 3. Non-goals (OUT)

- No second mechanism for the blocker or a high: units 44 to 48 own those; S3 points unit 34 at
  unit 44's oracle and S25 gives unit 48's lock its busy outcome, each its own finding.
- No new gate leg and no lint over spec criteria: each arm joins an existing suite.
- No renumbering of order 5: `--dispatch` already refuses a group whose declared paths meet
  (`tools/unattended/unattended.sh:13936`), so S24 records the sequence rather than moving it.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-2` — the card-store fixture, which S18 gives the `publish-late` plant
- **consumes-from** `TOOL-dPlacedRequest-24` — `write_node_lock`, whose write order S5 sets
- **consumes-from** `TOOL-dPlacedRequest-33` — `--card-ref write`'s bound, which S1 names
- **consumes-from** `TOOL-dPlacedRequest-34` — AC59, which S3 rewrites
- **consumes-from** `TOOL-dPlacedRequest-36` — the Goal, S2, AC1 to AC3 and §4, which S7, S9, S24 and S30 amend
- **consumes-from** `TOOL-dPlacedRequest-37` — S1, AC1 and §4, which S9, S24, S25 and S33 amend
- **consumes-from** `TOOL-dPlacedRequest-38` — the carrier arm and §5, which S8, S10, S20, S24, S31 and S32 amend
- **consumes-from** `TOOL-dPlacedRequest-39` — the trap order, AC1 and §4, which S4, S6 and S24 amend
- **consumes-from** `TOOL-dPlacedRequest-40` — the exempt `status` act, which S28 observes
- **consumes-from** `TOOL-dPlacedRequest-41` — the offline write's queued base, which S11 and S26 amend
- **consumes-from** `TOOL-dPlacedRequest-42` — the offline create's queue line, which S11 routes through `derive_queue_tip`
- **consumes-from** `TOOL-dPlacedRequest-43` — S6, S8, S15 to S22, S25, S26, S30 and their criteria, which S1, S2 and S11 to S34 amend
- **consumes-from** `TOOL-dPlacedRequest-44` — the version-bump oracle, which S3 makes unit 34's AC59 run
- **hands-off** `TOOL-dPlacedRequest-52` — S1, S3, S6 to S8, S13, S21, S25, AC7, AC13, AC24, AC30, AC31 and §5, which that unit's items for findings 4, 6, 7, 11, 14, 18, 20, 21, 25, 26 and 32 amend or, for S25's retry, read as the placed race's bound

## 4. Design

### The contained append, in order (S4 to S6)

```
add_feed_event ref commit           (caller's shell: dir, tree, as TOOL-dPlacedRequest-39)
  ( _fl_mine=
    trap '[ -n "$_fl_mine" ] && owner absent or == tok && rm -rf "$dir/gov-feed.lock"' EXIT
    write_node_lock "$dir/gov-feed.lock" "$tok" || exit 3
        mkdir ok -> _fl_mine=1; owner <- tok; until <- EPOCHSECONDS + NODE_LOCK_BOUND
    key check, counter, append )
```

An abort anywhere after the `mkdir` finds the flag set and either no `owner` or this token, so the
lock never outlives the subshell; an abort before the `mkdir` finds the flag empty and touches
nothing another writer holds.

### The bounded call (S21, S22)

```
run_driver_bounded <bound> <verb args>    -> 0..n verb rc, out in $RDB_OUT, err in $RDB_ERR
  no .unattended.conf | no driver | no timeout -k  -> rc 125, 126 or 127, RDB_WHY=<reason>, prints nothing
  GOV_RUNLOG=0 timeout -k 2 <bound> bash <driver> <verb args> </dev/null >"$RDB_OUT" 2>"$RDB_ERR"
caller: overlaps | claims | card publish | card lookup each prints its own line from rc and RDB_WHY
```

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `CARD_PUBLISH_BOUND` | constant in `manifest-check.sh` | none: `sh.constant` is undeclared |
| `RDB_ERR`, `RDB_WHY` | outputs of `run_driver_bounded`, beside unit 43's `RDB_OUT` | none: `sh.constant` is undeclared |
| `_fl_mine` | flag inside `add_feed_event`'s subshell | none declared |
| `CARD_READ_BOUND_MS`, `SCRATCH_GUARD_CARD_READ_BOUND_MS` | constant and its override in `scratch-guard.js` | none: `js.constant` is undeclared |

### Evidence

- Bounds today: `CARD_OVERLAP_BOUND` 10, `CARD_CLI_BOUND` 5, `CARD_CLAIMS_BOUND` 15
  (`manifest-check.sh:220`, `:224`, `:228`); `CARD_FETCH_BOUND` has no value at the base, and
  `TOOL-dPlacedRequest-2`:79, `TOOL-dPlacedRequest-33`:47 and :100, and `TOOL-dPlacedRequest-34`:65
  spell it.
- The claim-push body the factory inherits writes `until` then `owner` (`unattended.sh:2347-2348`), and
  `check_claim_push_lock_stale` falls back to `-mmin +2` with no `until` (`:2329`).
- The take-over identity rows: `unattended.sh:2260-2263`; the `same` row needs a `prior-session` fact.
- The parity loop's population: `resolve-python.test.sh:218`; its non-empty arm: `:221`.
- `stop-guard.js:97` declares `LIVENESS_BOUND_MS`; `:106-114` is `runLiveness`.
- `--dispatch` refuses two passes claiming one path (`unattended.sh:13936`, fail 49).

### Files touched (estimate)

- `tools/lib/gov-feed.sh`: S5, S6, with its carried copies in `tools/unattended/unattended.sh`,
  `tools/run-gates/post-merge.sh` and `tools/push-main.sh`
- `tools/unattended/unattended.sh`: S11, S25, S26
- `tools/unattended/unattended.test.sh`: the arms of §7
- `tools/lib/resolve-python.test.sh`: S8, S10, S20, S32
- `skills/session-kickoff/manifest-check.sh` and `skills/session-kickoff/manifest-check.test.sh`: S1,
  S2, S21, S22
- `skills/session-kickoff/card-store.fixture.sh`: S18
- `tools/hooks/scratch-guard.js` and `tools/hooks/scratch-guard.test.sh`: S16
- `tools/unattended/README.md`: S34
- `memory/builds/dPlacedRequest/spec/`: the specs of units 33, 34, 36 to 41 and 43, each edit a rev
  bump with its §9 line: S1, S3, S4, S6, S7, S9, S11 to S15, S17, S19, S23, S24, S25, S27 to S31, S33,
  S34

### Alternatives rejected

- **Two batches.** S5, S6, S11, S25 and S26 all write `tools/unattended/unattended.sh` or a file
  carried into it, and the spec edits share unit 43's file, so no split gives M6 two disjoint write
  sets.
- **Distinct orders for units 36, 37 and 39 (finding 27's first fix).** This unit builds at order 26,
  after those units; a renumbering then moves nothing, and `--dispatch` already sequences them.
- **One bound for the publish and the lookup (unit 43 F3 as written).** A read would wait out a
  writer's 140 s; two questions get two constants.

## 5. Production-readiness checklist

- security — S6 never clears a lock another writer took; S25 names the busy outcome of the request
  lock.
- perf / scale — S2 holds a hung lookup to 15 s; S16's override keeps the hook arm under a second.
- error / empty / loading states — S7 and S8 fail on an empty population; S25 and S26 each name an
  outcome.
- observability — S8's red names the carrier; S34 documents every emitted event.
- risks — S5 changes a write order every carrier holds, carried by the parity row.
- testing — the probes of §6 and the arms of §7.
- migration — none: every surface is new in this build.
- user docs — `help/loop.md` (S17), the kit README (S34) and the stops guide's existing rows.

## 6. Acceptance criteria

The fixtures are the named units': unit 1's AC7 clone and bare origin for the driver, unit 2's card
store fixture for the engine, unit 19's two clones for requests, unit 38's scratch carriers for the
block, each `RUN_CLAIMS=on` unless stated.

- **AC1** — When `grep -n 'CARD_PUBLISH_BOUND' skills/session-kickoff/manifest-check.sh` runs, it
  names the declaration and the `--card-ref write` call only, and `awk` reads its default above twice
  `REMOTE_BOUND` plus 5. Red when: the publish runs under the lookup's bound.
- **AC2** — When `awk` reads the defaults of `CARD_FETCH_BOUND` and `CARD_CLAIMS_BOUND`, the first is
  at most the second, and the lookup's `timeout` line spells no `CARD_PUBLISH_BOUND`. Red when: a
  writer's bound reaches a read.
- **AC3** — When `grep -c 'git diff c63aabbb' 2026-10-25-spec-TOOL-dPlacedRequest-34.md` runs, it
  prints 0, and AC59 there names `TOOL-dPlacedRequest-44`. Red when: two oracles answer one question.
- **AC4** — When unit 39's AC1 probe runs as written over the built block, it prints `after` and no
  `gov-feed.lock` remains. Red when: the plant precedes the trap.
- **AC5** — When `: "$GOVFEED_PLANT_UNSET"` is planted in a scratch cut of `write_node_lock` after its
  first write and the take runs under `set -u` in a subshell, the lock directory's `owner` reads the
  token. Red when: an abort leaves a lock with no owner.
- **AC6** — When that plant sits between the `mkdir` and the first write and
  `bash -c 'set -u; . cut.sh; add_feed_event refs/gov/bar-red "$h"; echo after'` runs, it prints
  `after`, no `gov-feed.lock` remains, and a second clean call appends one line. Red when: an abort
  inside the factory leaves the lock for two minutes.
- **AC7** — When unit 36's restated AC3 runs over a scratch tree whose one carrier holds
  `gov_feed_sh` alone, it fails naming that file; over an empty population it fails; over the real
  tree it passes. Red when: a carrier's missing appender is observed nowhere.
- **AC8** — When unit 38's arm runs over a scratch carrier holding `gov_feed_sh` without
  `health_log_sh`, it prints `no health_log_sh beside gov_feed_sh` and fails. Red when: the arm
  sources the canonical appender.
- **AC9** — When unit 37's corrected AC1 probe runs over the built block, it prints `rc=0`; the
  uncorrected `env -i` form prints `c: unbound variable`. Red when: green and red fail alike.
- **AC10** — When `grep -n 'env -i' tools/lib/resolve-python.test.sh` runs, the carrier arm's line
  passes `c="$c"`, and the arm passes over a self-contained scratch copy. Red when: the arm reds
  every copy.
- **AC11** — When an offline create of `tOff` with an empty tip is queued, then
  `--lease release build tOff --as withdrawn`, and the flush runs, the release's parent is the
  create's commit and the remote reads `withdrawn`. Red when: a reader compares the raw field.
- **AC12** — When a queued `-` line is flushed, the ref is created; a scratch copy whose
  compare-and-swap passes `-` literally fails to push. Red when: the encoding is never read.
- **AC13** — When `gen_build_index.py --write` has rendered and `wc -c` reads unit 34's spec, it
  prints at most 48128, and unit 43's AC22 names 48128. Red when: a ceiling no named cut reaches.
  figure: 49053 PINNED at rev-5, 2026-10-25; 48128 DERIVED as 49152 less 1024.
- **AC14** — When `grep -n '50111' 2026-10-25-spec-TOOL-dPlacedRequest-43.md` runs, the line names
  `dfb9b0d3`. Red when: a pin carries no commit.
- **AC15** — When `grep -n ':710' 2026-10-25-spec-TOOL-dPlacedRequest-43.md` runs, the line names
  `checkAuthorizedReadme`, and the `spawnSync('git'` line of `scratch-guard.js` carries no `timeout`.
  Red when: the bound lands on the README call.
- **AC16** — When `readCard`, required from `tools/hooks/scratch-guard.js`, runs under
  `SCRATCH_GUARD_CARD_READ_BOUND_MS=500` over a stub checker sleeping 30 s, it returns no card within
  2 s, and `grep -c 'CARD_READ_BOUND_MS' tools/hooks/scratch-guard.js` prints at least 2. Red when:
  the bound is a bare literal.
- **AC17** — When `grep -n 'follow-leases' loop.md` runs in `help/`, it names the value only on the
  `awaiting` row. Red when: the page lists `offline` under `refuse` for `follow-leases`.
- **AC18** — When `card-store.fixture.sh --plant publish-late` runs, the card prints
  `remote-ref unknown`. Red when: a landed write reads `not written`.
- **AC19** — When unit 43's AC15 runs with the `prior-session` and `keepalive` facts planted, the class
  is `same`; without them it is a `foreign-` class. Red when: a fact the row needs is not planted.
- **AC20** — When unit 38's arm runs over a scratch copy whose append reads `$ROOT` after the lock, it
  fails; over the real block `gov-feed.log` gains one line. Red when: the call returns before the lock.
- **AC21** — When the card publish runs in a tree with no `.unattended.conf`, it prints
  `card — remote-ref not written: no .unattended.conf`, and the overlaps cell keeps
  `overlaps — skipped: no .unattended.conf in this tree`. Red when: the helper prints a caller's line.
- **AC22** — When `derive_claims_line` runs in a scratch tree holding `.unattended.conf` whose
  resolved `unattended.sh` is a stub that writes `boom` to stderr only and exits 1, the claims cell
  prints `claims — skipped: boom`. Red when: the cell reads `printed nothing`.
- **AC23** — When the probe runs under `env -u GOV_NODE -u USER USERNAME=<row user>` per `fleet.toml`
  row, each resolver prints that row's tag; with `GOV_NODE=a`, all three print `a`. Red when: an
  ambient `GOV_NODE` answers.
- **AC24** — When `grep -l 'in sequence'` runs over the specs of units 36 to 39, it lists all four.
  Red when: an order group shows meeting write sets as parallel unremarked.
- **AC25** — When a fresh `requests.lock` is planted in the common dir and `--request a.md` runs, it
  prints `request not written — requests.lock busy` and exits 2, `requests/` unchanged. Red when: the
  busy path is unnamed.
- **AC26** — When the newest queued line for `tOff` names an absent sha and an offline write to
  `tOff` runs, it prints `queued commit unreadable`, exits 2, and `gov-queue.log` is unchanged.
  Red when: the write chains on garbage or falls back to the cached tip.
- **AC27** — When `grep -n 'RUN_CLAIMS' tools/unattended/PROTOCOL.template.md` runs, the row names no
  `refs/gov/` path and names `UNATTENDED-STOPS.md`. Red when: only the byte count is observed.
- **AC28** — When `env -u CLAUDE_CODE_SESSION_ID bash unattended.sh --lease status build tFix` runs, it
  exits 0 and prints the status line. Red when: a scratch copy that leaves `status` off the exempt
  list refuses it.
- **AC29** — When `grep -c 'node-lock-broken'` and `grep -c 'node-lock-guard-cleared'` run apart over
  `tools/unattended/README.md`, each prints at least 1. Red when: one combined count hides a miss.
- **AC30** — When `grep -c 'aborts the carrier' 2026-10-25-spec-TOOL-dPlacedRequest-36.md` runs, it
  prints 0, and the Goal names `set -u`. Red when: the mechanism is misdescribed.
- **AC31** — When `grep -n 'well under a second' 2026-10-25-spec-TOOL-dPlacedRequest-38.md` runs, it
  prints nothing, and §5 names a measured time with its node. Red when: a perf claim carries no
  measurement.
- **AC32** — When a scratch `notes.md` quoting `# >>> gov_feed_sh` at column 0 is staged beside the
  carriers, unit 38's arm leaves it out of the population. Red when: a record joins the population.
- **AC33** — When `grep -n 'NODE_LOCK_BOUND' 2026-10-25-spec-TOOL-dPlacedRequest-37.md` runs, S1
  names the four sections and a measured longest under 10 s. Red when: the bound is justified
  against sections it does not name.
- **AC34** — When a probe lists each token `add_health_event` is passed in `unattended.sh` and
  `gov-feed.sh` and greps `tools/unattended/README.md` for it, none is missing, `lease-yielded`
  included. Red when: an emitted event is undocumented.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `python resolver (behaviour + inline parity + idiom ban)` · `unattended kit gate` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `govkit selfcheck` · `lexicon naming predicates` · `spawn budget (forks per hot entrypoint)` · `recall floor` · `recall floor arms` · `manifest-check self-test` · `scratch-guard self-test` · `agent-cap self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `format-guard self-test` · `push-main self-test` · `run-selftests self-test`

New arm: tools/unattended/unattended.test.sh · covers AC5 AC6 AC11 AC12 AC25 AC26 AC28 · each item's plant, staged against the unit it amends · waived for this build's landing by README rule 8, so its clean reading is owed with PLAY-dClosedLoop-14
New arm: tools/lib/resolve-python.test.sh · covers AC8 AC10 AC20 AC32 · scratch carriers lacking the appender, reading `$ROOT` after the lock, and a quoting record, staged against unit 38's arm as written · none
New arm: skills/session-kickoff/card-store.fixture.sh · covers AC18 · a stub driver that writes the ref and sleeps past `CARD_PUBLISH_BOUND=2`, staged against the `not written` kill line · none
New arm: skills/session-kickoff/manifest-check.test.sh · covers AC21 AC22 · a missing conf and a stderr-only failing driver, staged against the helper printing its own line and capturing stdout alone · none
New arm: tools/hooks/scratch-guard.test.sh · covers AC16 · a stub checker that never answers under the 500 ms override, staged against the bare literal · none

## 8. Open questions

- **F1 — What bounds the card publish and the card lookup (S1, S2)?** (a) Two constants, the
  publish's 140 s and the lookup's 15 s; (b) one constant at 140 s, as unit 43 F3 reads; (c) the
  bound passed into the driver. (b) holds a read past the 15 s remote-read bound; (c) adds a flag
  for one caller. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, finding 1's fix judged sound
  and finding 22's skeptic-corrected fix. widens: none · relaxes: none
- **F2 — How is the feed lock cleared on an abort inside the factory (S5, S6)?** (a) Owner first, and
  a flag-guarded trap armed before the take; (b) the trap after the take, as unit 39 reads; (c) the
  trap clearing any lock it finds. (b) leaves a two-minute ownerless lock; (c) can clear another
  writer's lock. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the skeptic's corrected fix for
  finding 14 and finding 34's fix. widens: none · relaxes: none
- **F3 — What closes finding 27 at order 26 (S24)?** (a) Each spec records its sequence; (b) the
  orders renumbered; (c) a render that marks meeting write sets. (b) moves nothing after those units
  are built; (c) is a third parser of Files touched beside `check-spec-tokens.py:530` and
  `unattended.sh:3389`. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the finding's second
  fix. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, the batch of the spec audit of the round-2 promotions' 22 MEDIUM
  and 12 LOW findings.
- rev-2 · 2026-10-25 · header above §1, §6 · the round-3 promotions' fix brief: the `**Derived:** PLAY-dClosedLoop-2` line binding this unit; AC16 and AC22 observe `readCard` and `derive_claims_line` over their stubs rather than naming the suites, which stay on their `New arm:` lines; AC17 cites the page this build creates by its basename; AC26's `Red when:` is joined onto one line.
- rev-3 · 2026-10-25 · §3 · the disposal of the spec audit of the round-3 promotions: the hands-off edge to `TOOL-dPlacedRequest-52`, mirroring its consumes-from.

## 10. Reuse audit

Each item extends the unit its finding names, and the new code reuses four seams: the
`CARD_*_BOUND` default pattern (`manifest-check.sh:220-229`) for S1 and S2, `runLiveness`'s bounded
spawn (`tools/unattended/stop-guard.js:106-114`) for S16, the parity loop's pathspec and `blk`
extractor (`tools/lib/resolve-python.test.sh:213-221`) for S8, S10 and S32, and
`TOOL-dPlacedRequest-24`'s retry for S25. `python tools/codebase-map/reuse_lookup.py "bounded driver
call that returns a skip reason and captures stderr"` ranked `skip`, `boundedParallel`, `drive` and
`read_bound_key`, name stems only, none the engine's call. `python tools/memory-recall/query.py "how
are a spec audit's minor findings batched into one unit"` returned TOOL-dGroundRules-21, -32 and -43
and PLAY-dOrderedCharter-49, batches of the same kind; none disagrees with source.

Recall terms used: minors batch promote medium low spec audit round finding item scope criterion edge mirror
