# TOOL-dPlacedRequest-99 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-99

The unit was built from its spec at rev-2 on base `57513c1df`. Built: S1, the kickoff suite's
card-store loop reading `card-store.fixture.sh --list`, its liveness row, its `TMP` normalised by
`cygpath -m` where `cygpath` exists, its floor raised and the stale count on the floor comment
corrected; S2, a resolver arm in each of the run-gates and kickoff suites; S3, `read_fence_line`'s
fourth return and `derive_push_failure` reading only an explicit refusal by the lease as `fenced`,
with two arms in the lander suite; S4, `read_card_stored` choosing the fresher stored card over the
stores `card.store` selects, through a new `derive_card_epoch` that converts a card's `published`
stamp to epoch seconds, and four plants in the card-store fixture; S5, `check_plant_tokens` in
`run-selftests.sh --check`, a `plants=<n>` token on every loop-kit budget row, the rows whose reading
covered fewer plants re-read, and two leg ceilings moved by the ceiling procedure; S6, ` · tail from
<store>` on every `stored`-mode success line; S7, the scratch-guard floor and its comment; S8, the
`--entry-claim` usage line, four pinning comments and an arm in the unattended kit's suite. The four
checklist records are written or extended and claimed. No gate, suite or bar ran in this pass.

THE PLANT RUNS: each card-store plant run alone as `bash skills/session-kickoff/card-store.fixture.sh
--plant <name>` with a forward-slashed `TMPDIR` under the run's scratch directory, on node d; each loop
row's plants run alone as `python <the module> --fixture --plant <name>` over the base, timed with
`date +%s%N`, the leg's `check` verb first where its argv carries one.

**Evidences:** TOOL-dPlacedRequest-99
- AC1 — `card-store.fixture.sh` — `--list | grep -c .` printed 34, and each of the 34 names run alone over this pass's engine exited 0 with every observation line `held` and no `MISSED` line: the 30 earlier plants in 613 s and S4's four in 119 s, node d. (DERIVED)
- AC1 — `FLOOR_ASSERTIONS` — over the tip, `grep -c 'for cs_plant in publish publish-off'` printed 0, `grep -c 'cs_fx" --list'` printed 1, `grep -c 'the suite ran every plant --list names'` printed 1 and `grep '^FLOOR_ASSERTIONS='` printed `FLOOR_ASSERTIONS=408`, each over the kickoff suite. (DERIVED)
- AC1 — `selftest-budgets.txt` — the `manifest-check self-test` row reads 4860, no longer 3820, and its note names the 34 plants `card-store.fixture.sh --list | grep -c .` prints. (DERIVED)
- AC1 — `manifest-check self-test` — the RED reading over the base `57513c1df`, whose kickoff suite still holds the hand list as at `95c3103ad`: the loop grep printed 1, the floor read 379 and the row read 3820. (DERIVED)
- AC2 — `TOOL-dPlacedRequest-99 S2` — over the tip, the grep printed 2 for `tools/run-gates/run-selftests.test.sh`, the arm's label and its comment, its row writing tag `s` above tag `t`, and 3 for the kickoff suite, the comment and the two rows of the upper-cased `USERNAME` run; the kickoff floor reads 408. (DERIVED)
- AC2 — `resolve_node_tag` — under `env -u GOV_NODE`, the function cut by `awk` with `_rs_reg_rx` from the run-gates kit's self-test runner, over a scratch root whose `AGENTS.md` holds the node's user's first character at tag `s` above the user at tag `t`, printed `t`; over a scratch copy staged with the substring compare it printed `s`. (DERIVED)
- AC2 — `derive_node_tag` — under `env -u GOV_NODE`, the function cut from `skills/session-kickoff/manifest-check.sh` over a scratch registry naming the user at tag `q`, with `USERNAME` upper-cased, printed `node — q · <the user>`; over a copy staged with the case-sensitive compare it printed `UNKNOWN`. (DERIVED)
- AC3 — `read_fence_line` — cut by `awk` from `tools/push-main.sh` with `check_fence_beat`, against a stub driver answering `--lease fence build fx --after <tip>` over a scratch remote: an exit-2 `lease not written — x` line returned 4, a fence line whose beat is not parented on the tip returned 4, and `lease refused — live-holder` returned 1. Over the base's lander the same three returned 1, 1 and 1. (DERIVED)
- AC3 — `derive_push_failure` — cut with the functions it calls, the lease moved on the scratch remote: the `lease not written` answer and the bad-beat line each printed `unreachable` with no `claim-lost` on stderr, the live-holder answer printed `fenced` with it. Over the base's lander all three printed `fenced` with the `claim-lost` remedy, its RED-first reading. (DERIVED)
- AC4 — `follow-offline-publish` — run alone it exited 0, every line held, the follow's card at step designing ending in the offline publish's READY line; `follow-offline-publish-online` the same, read from the remote ref. (DERIVED)
- AC4 — `resolve_build_card` — `follow-foreign-after-cached` and `follow-foreign-after-offline` each exited 0, every line held: the follow's card carries the foreign publish's READY line, and the lookup run after it re-keys a session card whose `## route` section onward equals the follow card's. (DERIVED)
- AC5 — `check_plant_tokens` — cut by `awk` from the runner with `read_population`, over the tip's budgets it printed `plant tokens graded 22 row(s), 0 finding(s)` and returned 0; over a copy whose placement row reads `plants=15` it reported that row with 29 and returned 1; over a scratch module declaring two plants and adding one by `PLANTS.update`, under a row reading `plants=2`, it reported that row with 3. (DERIVED)
- AC5 — `observed` — `grep -c observed memory/gotchas/budget-row-not-remeasured-after-added-arms.md` printed 1; at the base it printed 0, and the base runner holds no `check_plant_tokens`, its grep printing 0. (DERIVED)
- AC6 — `tail from cache` — the `follow-offline-publish` plant's line `S6 the follow's local-clone line says tail from cache` held. (DERIVED)
- AC6 — `global-set-and-never-read` — `gotchas.py --for-paths skills/session-kickoff/manifest-check.sh` printed it, and `grep -c 'global-set-and-never-read.md' memory/map/features/session-kickoff.md` printed 1. At the base the engine held no `tail from`, and every `CARD_STORED_FROM` line assigned it. (DERIVED)
- AC7 — `AC28` — `grep -n '^FLOOR_ASSERTIONS=' tools/hooks/scratch-guard.test.sh` printed 401, one above the base's 400, and the comment grep printed 1; at the base it printed 0. (DERIVED)
- AC8 — `usage-exit-list-lags-its-function` — the exit-list grep over `tools/unattended/unattended.sh` printed 2 at the tip and 1 at the base; `gotchas.py --for-paths tools/unattended/unattended.sh` printed the record, and the dossier grep printed 1. The arm, cut from the suite and sourced with a stub `same`, passed its three rows over the tip's driver and failed all three over the base's. (DERIVED)

## Readings beside the criteria

- S4's four plants, read once each by direct CLI, took in all: (PINNED)
  119 s (PINNED)
- so the kickoff row's proxy, the row's 2547 s plus the 22 plants' 574 s the spec derived plus those, is: (DERIVED)
  3240 s (DERIVED)
- and its budget at x1.5: (DERIVED)
  4860 (DERIVED)
- The leg's ceiling under `ceiling-margin.txt`'s rule, the reading plus the larger of its 120 s floor and the reading itself, needs at least: (DERIVED)
  6480 (DERIVED)
- so the `manifest-check self-test` ceiling in `tools/gate-legs.json` moved from 4370 to 6480, and the proxy was recorded with `GOV_NODE=d derive-ceilings.py --write --observed`, its `--how` saying it is a proxy and no run. (DERIVED)
- The placement leg's 29 plants by direct CLI took: (PINNED)
  79.2 s (PINNED)
- which by the same rule needs a ceiling of at least 199.2, so its ceiling moved from 120 to 200 and the reading was recorded the same way; `pass_legs.py --apply` then changed no `pass_leg` field. (DERIVED)
- Eight of placement's plants MISSED at the base on a `TypeError` in the format string of its lease-status read, `tools/loop/placement.py@57513c1df:595`, two `%s` fed one value. The loop kit is outside this write set, so the cause is reported, not fixed, and the `loop placement fixtures` leg reds at the close until it is. (DERIVED)
- The loop rows' runtime `PLANTS` and the readings, by direct CLI over the base: witness 11 in 20.7 s, splice 14 with `check` in 9.3 s, parent routes 8 in 5.8 s, transition 13 with `check` in 33.4 s, placement 29 in 79.2 s, review bounds 14 in 10.0 s, termination 16 with `check` in 18.1 s, definition 55 in 21.3 s, breakpoints 14 in 88.3 s, guard 45 in 69.1 s, budget 41 in 177.7 s, position 31 in 68.3 s, factories 15 in 481.8 s. (PINNED)
- The other nine loop rows already priced every plant their module holds, and took the token alone. (DERIVED)
- The computed-witness row names its commit, `202e287fb`, where `PLANTS` held 4 against today's 11, so it was re-read; the splice row's `e9dbe0bb8` resolves to no object in this clone, so it was re-read as a row naming none. (DERIVED)
- Where a re-read row's reading at x1.5 floored at 60 fell under its standing budget, the row kept the higher figure and its note records the reading beside it; only placement and definition rose. (DERIVED)
- The run-gates suite pins `SELFTEST_FLOOR`, not `FLOOR_ASSERTIONS`, so by S2's wording its new arms move no floor; the pin is a minimum and the arms do not lower the count. (DERIVED)
- The kit-epoch rule binds at the push boundary, where the lander mints each moved kit's version, so no version carrier moved in this pass. (DERIVED)

- The bug-class checklist over the pass commit `f1b6cd352` selected `portability-sweep`: the kickoff arm upper-cased the user with a bash-4 case expansion the suite used nowhere else, now `tr '[:lower:]' '[:upper:]'`, probed to print the user upper-cased. (DERIVED)
- It selected `refusal-branch-with-no-arm`: `check_plant_tokens`'s import-failure finding had no arm, so the run-gates suite gains one, a scratch module raising at import; the same function, cut and run over that module, printed `which did not import` and returned 1. (DERIVED)
- It selected `fixture-passes-by-finding-nothing`: the S8 arm's first row compares named placeholders rather than two captures that could both be empty, a fix made before the pass commit from the same checklist read over the paths, and over an empty stand-in driver it fails. The S1 liveness row and the S5 control's graded count hold their populations. (DERIVED)
- It selected `a-spelling-change-strands-its-readers`: no file under `skills/`, `tools/` or `help/` quotes a `card —` success line or the lander's re-fence `unreachable` wording; arm 54 matches the line's unchanged prefix. (DERIVED)
- It selected `an-attested-count-must-count-what-the-grader-counts`: the kickoff floor counts `pass`, the lander floor `n` from `ok`, and the scratch-guard floor `n` as `pass` plus `fail`; each raise counts the rows its own counter takes. (DERIVED)

## Items diverged

None.

## Owed at the close

- `New arm:` `skills/session-kickoff/manifest-check.test.sh` — the hand list of 8 restored, the case-sensitive node compare restored, and the base engine under the four S4 plants: RED-first, then GREEN, and the count against `FLOOR_ASSERTIONS`.
- `New arm:` `tools/run-gates/run-selftests.test.sh` — the substring compare restored, a budget copy whose placement token reads 15, and the scratch module growing `PLANTS` under a token of 2.
- `New arm:` `tools/hooks/scratch-guard.test.sh` — the every-host AC28 row deleted with `sg_win` forced empty.
- `New arm:` `tools/unattended/unattended.test.sh` — the base usage line and a variable return with no pinning comment; its clean reading is owed with PLAY-dClosedLoop-14.
- `New arm:` `tools/push-main.test.sh` — arms 55 and 56 against the base classifier, and the count against the raised `FLOOR_ASSERTIONS`.
- The `install-prefix` and `shell hygiene` pass legs, which the role's hook refused in the pass, and the legs the spec's Gates section names, run once by the main loop.
