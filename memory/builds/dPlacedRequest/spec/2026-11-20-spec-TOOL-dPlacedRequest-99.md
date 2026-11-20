# TOOL-dPlacedRequest-99 — the closing review's minors: every plant on a gate, a resolver arm, honest re-fence and card outcomes, a re-priced row and three loose ends

**Status:** DEFERRED · rev-1 · 2026-11-20 · node d · Tier-2 · base 95c3103a · streams tooling · order 37

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-20-prompt-TOOL-dPlacedRequest-99-closing-review-spec-brief.md](../prompts/2026-11-20-prompt-TOOL-dPlacedRequest-99-closing-review-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review of this build confirmed two MEDIUM items in round 1
(`memory/builds/dPlacedRequest/reviews/2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round1.md`)
and three MEDIUM and three LOW items in round 2
(`memory/builds/dPlacedRequest/reviews/2026-11-20-review-TOOL-dPlacedRequest-1-64-closing-diff-round2.md`).
Round 2's exit batched all eight into this one unit, as BUILD-METHOD M4's severity rule orders. None
ships a wrong result today except round 2's M1 and M2, an aborted run and a stale build card; the rest
are checks that cannot fail, a budget row priced for half its suite, dead plumbing and a usage line
that omits two exits. Each scope item below takes the record's fix, the skeptic's class-level fix where
the record gives one, and the record's left-shift where it fits this unit's write set, else a
bug-class checklist entry.

## 2. Scope (IN)

- **S1** — Round 1 M1, finding id 4, fix judged SOUND. The plant loop of
  `skills/session-kickoff/manifest-check.test.sh` reads its names from `card-store.fixture.sh --list`
  instead of a hand-typed list of 8, and a liveness row asserts the number of plants run equals the
  number `--list` prints. `FLOOR_ASSERTIONS` rises by the rows the loop gains, the floor comment's
  stale count is corrected, and the `manifest-check self-test` row of
  `tools/run-gates/selftest-budgets.txt` is re-priced from a reading over every plant. A plant that
  misses once gated is fixed in this unit where its cause lies in the fixture or the kickoff engine;
  none missed when this spec was written.
  Observed by AC1.
- **S2** — Round 1 M2, finding id 5, the skeptic's class-level fix. An arm per resolver that
  `TOOL-dPlacedRequest-43` S20 changed: in `tools/run-gates/run-selftests.test.sh` a registry row whose
  user token is a strict substring of the user, its tag `s`, above the exact row `t`, asserting pooled
  evidence keyed on `t`; in `skills/session-kickoff/manifest-check.test.sh` a `--card` run with
  `USERNAME` set to the registry row's user in upper case, asserting the row's tag and not `UNKNOWN`.
  The kickoff suite's floor rises by its row. Observed by AC2.
- **S3** — Round 2 M1, finding id 2, the skeptic's class-level fix. `read_fence_line` in
  `tools/push-main.sh` returns 1 only for an explicit `lease refused — <cause>` line other than
  `offline`, 3 for `offline`, and a new 4 for every non-answer: an unparsed, multi-line or empty read,
  every exit-2 `lease not written` line, the no-python branch, and a `check_fence_beat` failure on a
  fence line the driver did answer. `derive_push_failure` reads 1 as `fenced` and every other return
  but a fence as `unreachable`. Two arms in `tools/push-main.test.sh` assert `claim-lost` is never
  printed for an exit-2 `lease not written — x` answer and for a bad-beat fence line on the `--after`
  call. Observed by AC3.
- **S4** — Round 2 M2, finding id 3, the skeptic's class-level fix. `read_card_stored` in
  `skills/session-kickoff/manifest-check.sh` picks the stored tail by freshness over the stores
  `card.store` selects, by the rule of §4, and two plants in
  `skills/session-kickoff/card-store.fixture.sh` observe it: a publish offline after an earlier
  lookup, then a follow, and the same with the remote answering again at the follow. Observed by AC4.
- **S5** — Round 2 M3, finding id 1, fix judged SOUND. The `loop placement fixtures` row of
  `tools/run-gates/selftest-budgets.txt` is re-priced from a reading over its 29 plants, its note naming
  the count and the base, and the leg's ceiling in `tools/gate-legs.json` is checked against the new
  figure. The left-shift the record names lands in `tools/run-gates/run-selftests.sh --check`: every
  budget row whose held leg runs a loop-kit module declaring a top-level `PLANTS` dict carries a
  `plants=<n>` token equal to that dict's size. Every such row is given its token in this unit, and a
  row whose reading covered fewer plants is re-priced first. The checklist record
  `memory/gotchas/budget-row-not-remeasured-after-added-arms.md` names the check. An arm in
  `tools/run-gates/run-selftests.test.sh` reds a mismatched token. Observed by AC5.
- **S6** — Round 2 L1, finding id 4, fix judged SOUND. `CARD_STORED_FROM` gains its reader: each
  `card —` success line `write_build_card` prints in `stored` mode carries ` · tail from
  <ref|cache|record>`. The class, a global assigned in a kit script and read nowhere, has no gate in
  this write set, so it lands as the checklist record `memory/gotchas/global-set-and-never-read.md`.
  Observed by AC6.
- **S7** — Round 2 L2, finding id 6, fix judged SOUND. `FLOOR_ASSERTIONS` in
  `tools/hooks/scratch-guard.test.sh` rises by the one `TOOL-dPlacedRequest-34` AC28 row that runs on
  every host, and a comment line names both AC28 rows, the Windows-only one left out of the count by
  its skip elsewhere. The class lands as a section of
  `memory/gotchas/floor-left-below-the-arms-it-guards.md`. Observed by AC7.
- **S8** — Round 2 L3, finding id 8, fix judged SOUND. The `--entry-claim` usage line of
  `tools/unattended/unattended.sh` lists `0 claimed, 1 refused, 2 not written, 3 budget spent, 4
  waiting, 5 a fresh slug owed`, as `run_entry_claim`'s header does. The class lands as the checklist
  record `memory/gotchas/usage-exit-list-lags-its-function.md`, and the instance gains an arm in the
  unattended kit's suite: the usage line names every code `run_entry_claim`'s body returns. Observed by
  AC8.

## 3. Non-goals (OUT)

- No change to what any card-store plant asserts beyond the two S4 adds; a plant fixed under S1 is
  fixed to hold its own stated observation.
- No shared selection function between `read_card_stored` and `resolve_build_card`: the class rule the
  record states admits a fixture asserting the two agree instead, and the S4 plants are that fixture.
- No re-pricing of a budget row that is not a loop-kit row S5 names.
- No new gate for the classes of S6, S7 and S8: each would live in another write set, the shell-hygiene
  checker, the testsuite counts leg and the unattended kit gate, and each lands as a checklist entry.
- No change to the lander's arms 42 to 54 beyond the two S3 adds, and no change to the fixture under
  them, which `TOOL-dPlacedRequest-98` owns.

### Edges

- **consumes-from** external — the card store, the node resolvers, the fenced landing, the placement
  suite and the entry claim this build's units built and CLOSED; each scope item corrects landed code,
  and those specs stay frozen

## 4. Design

### S1 — the plant loop

```
cs_list=$(bash "$cs_fx" --list)         # the fixture's own PLANTS, one per line
for cs_plant in $cs_list; do ...as at the base, one ok or FAIL row per plant...; done
check_eq "the suite ran every plant --list names" "$(wc -l <<<"$cs_list")" "$cs_ran"
```

Cited at the base: the hand list is `skills/session-kickoff/manifest-check.test.sh@f227fdc7:2383`, its
floor `skills/session-kickoff/manifest-check.test.sh@f227fdc7:2457`; the fixture's `--list` prints its
`PLANTS` at `skills/session-kickoff/card-store.fixture.sh@9d4246db:37`.

The plant inventory, measured by this spec's writer, one plant at a time by direct CLI with a
forward-slash `TMPDIR` on node d, 2026-11-20 (PINNED):

- `--list` prints 30 plants (DERIVED by `--list` piped to `wc -l`), and the suite runs 8 of them.
- Every one of the 30 held, each exiting 0 with no `MISSED` line, so gating them reds nothing today.
- The 30 runs took 781 seconds in all (PINNED, node d, 2026-11-20, one reading each).
- The 8 the suite already runs took 207 seconds of them (PINNED, the same readings).
- So the 22 added plants cost 574 seconds (DERIVED, the difference), read partly under a concurrent probe.

A `TMPDIR` spelled with backslashes reds every plant, an awk escape warning on each read; the suite
hands the plants its own `mktemp` directory, which is forward-slashed, so this is a probe's trap and
not the gate's. The budget row is re-priced from a reading over all 30, worst of two, at the file's
stated margin.

### S2 — the resolver arms

`tools/run-gates/run-selftests.sh#resolve_node_tag` compares the lower-cased user with each registry
token for equality, and `skills/session-kickoff/manifest-check.sh#derive_node_tag` folds both sides
with `tolower`. The `run-selftests.test.sh` fixture writes one row whose token is exactly the user
(`tools/run-gates/run-selftests.test.sh@382f88e6:395`), which the substring rule matches too; the new
row is the user's first character at tag `s`, written above it. That suite pins no
`FLOOR_ASSERTIONS`, so its arm moves no floor; the record's "raise each suite's floor" holds for the
kickoff suite only.

### S3 — the re-fence outcome

```
read_fence_line -> 0 a fence, or none · 1 an explicit refusal by the lease · 3 offline · 4 no answer
derive_push_failure, the lease tip moved:
  0 with FENCE_REF  -> refenced          1 -> fenced, the claim-lost remedy
  anything else     -> unreachable, retry, no abort remedy
```

The two callers that read the first fence, at `tools/push-main.sh@7a142cb6:1733` and
`tools/push-main.sh@7a142cb6:1928`, test `if ! read_fence_line`, so 4 refuses the landing there as 1
does today. The function's header comment lists the four returns. Cited at the base:
`tools/push-main.sh#derive_push_failure`, its `fenced` fall-through at `tools/push-main.sh@7a142cb6:334`;
`tools/push-main.sh#read_fence_line`; `tools/push-main.sh#check_fence_beat`; the driver's exit-2 lines in
`tools/unattended/unattended.sh#write_fence_beat`.

### S4 — the freshness rule

```
stores = read_card_policy card.store
cache  = local-clone selected and the cache file exists;  cref = its `# card-ref` line
refc   = remote-ref selected and refs/gov/remote/builds/<slug>/card resolves -> its commit
1. cache and (cref = local or cref != refc)      -> the cache        CARD_STORED_FROM=cache
2. refc  and (no cache or cref = refc)           -> the ref          CARD_STORED_FROM=ref
3. cache                                         -> the cache        CARD_STORED_FROM=cache
4. build-folder selected and a card record       -> the record       CARD_STORED_FROM=record
5. none                                          -> return 1
```

Rule 1 holds whether or not this follow's `read_card_ref` answered, which is the case the record's
instance fix left standing. Cited at the base: `skills/session-kickoff/manifest-check.sh#read_card_stored`,
its fixed ref-first order at `skills/session-kickoff/manifest-check.sh@b25206f8:1921`;
`skills/session-kickoff/manifest-check.sh#write_card_cache` writes `local` or the ref's commit;
`skills/session-kickoff/manifest-check.sh#resolve_build_card` filters by `card.store` and trusts the cache
only when its card-ref is the fetched tip.

The two plants, `follow-offline-publish` and `follow-offline-publish-online`, join the gate through S1's
`--list` read with no further edit to the suite.

### S5 — the plant-count token

Each loop-kit budget row's note gains one token, `plants=<n>`, beside its prose: the number of plants
its reading covered. `run-selftests.sh --check` joins each row to its held leg by name, reads the leg's
argv, and for a `{prefix}/loop/<module>.py` declaring a module-level `PLANTS` dict counts its keys by
`ast`; a missing token or one that differs is a finding naming the row, the token and the count. A row
whose leg runs no such module is not graded, and the check's clean line says how many rows it graded.
The inventory at the base, read by an `ast` probe joining each row to its leg (DERIVED, re-derived by the
same probe):

| rows graded | rows whose prose count already equals `PLANTS` | rows to re-price |
|---|---|---|
| 22 | 9 | at most 13, placement's among them |

A row whose note names the commit its reading was taken at takes its token from `PLANTS` at that
commit, read by `ast` over `git show`, and is re-priced only where that count differs from today's.
Each row to re-price is read the way its peers were, its plants one at a time by direct CLI, worst
reading x1.5 floored at 60, its note naming the reading's base and node. Where a new budget exceeds the
leg's `ceiling`, the ceiling moves by `derive-ceilings.py --write`, as the checklist record's fix
states. Cited at the base: `tools/run-gates/selftest-budgets.txt@25b27c00:84`;
`tools/loop/placement.py@a7f26e84`'s `PLANTS`, 29 keys (DERIVED by `ast`).

### S6 to S8

- **S6.** The suffix rides each success line, `remote-ref`, `local-clone` and the snapshot's, only in
  `stored` mode, where a tail was read; `session` and `none` modes read no store. Cited at the base:
  `skills/session-kickoff/manifest-check.sh@b25206f8:1815` declares it, and
  `skills/session-kickoff/manifest-check.sh#write_build_card` prints the lines.
- **S7.** The value is one above whatever the file holds when this unit builds, since
  `TOOL-dPlacedRequest-95` raises the same pin for its own rows. Cited at the base:
  `tools/hooks/scratch-guard.test.sh@ff709691:1842`.
- **S8.** The arm collects the `return <n>` codes inside `run_entry_claim`'s body by `awk` and asserts
  each appears in the usage line's exit list. The class rule across every mode belongs to the unattended
  kit gate, another write set, so it is the checklist record's. The unattended kit's own suites are
  waived for this build's landing (README rule 8), so the arm's clean reading is owed with
  PLAY-dClosedLoop-14 and AC8 observes by `grep`. Cited at the base:
  `tools/unattended/unattended.sh@0e8038fd:55`, the record's line 56 being one off;
  `tools/unattended/unattended.sh#run_entry_claim`.

### Inventory

| identifier | kind | cell that grades it |
|---|---|---|
| `check_plant_tokens` | the S5 check, a function of the self-test runner | `sh.function`, graded OK by `lexicon.py --suggest` |
| `plants=<n>` | S5's token in a budget row's note | none; the check reads it |
| `follow-offline-publish`, `follow-offline-publish-online` | S4's plant names in the fixture's `PLANTS` | none; plant names are data |
| `tail from` | S6's line suffix | none |
| 4 | S3's return of `read_fence_line` | none |

### Rollout

This unit shares files with its order-37 siblings: `tools/hooks/scratch-guard.test.sh` with
`TOOL-dPlacedRequest-95`, `tools/push-main.test.sh` with `TOOL-dPlacedRequest-98`,
`tools/unattended/unattended.sh` with `TOOL-dPlacedRequest-96` and `TOOL-dPlacedRequest-97`, and
`memory/gotchas/INDEX.md` with `TOOL-dPlacedRequest-95`. The dispatch sequences them by their recorded
write sets. Each floor rises over the value the file holds when the unit builds, and S3's two arms raise
the lander suite's floor whenever `TOOL-dPlacedRequest-98` has pinned one.

### Files touched (estimate)

- `skills/session-kickoff/manifest-check.test.sh`: S1's loop, liveness row and floor; S2's arm
- `skills/session-kickoff/card-store.fixture.sh`: S4's two plants, and S1's fixes to a plant that misses
- `skills/session-kickoff/manifest-check.sh`: S4's rule, S6's suffix, and S1's fixes in the engine
- `tools/run-gates/run-selftests.test.sh`: S2's arm, S5's arm
- `tools/run-gates/run-selftests.sh`: S5's check
- `tools/run-gates/selftest-budgets.txt`: S1's and S5's rows
- `tools/gate-legs.json`: a ceiling, only where a new budget exceeds it
- `tools/push-main.sh`: S3's returns and classifier
- `tools/push-main.test.sh`: S3's arms
- `tools/hooks/scratch-guard.test.sh`: S7's floor and comment
- `tools/unattended/unattended.sh`: S8's usage line
- `tools/unattended/unattended.test.sh`: S8's arm
- `memory/gotchas/budget-row-not-remeasured-after-added-arms.md`: S5's check named
- `memory/gotchas/global-set-and-never-read.md`: S6's class, new
- `memory/gotchas/floor-left-below-the-arms-it-guards.md`: S7's section
- `memory/gotchas/usage-exit-list-lags-its-function.md`: S8's class, new
- `memory/gotchas/INDEX.md`: rendered by `gotchas.py --write`
- each touched kit's version carrier, moved once by the kit-epoch rule

### Alternatives rejected

- **S3 by the finder's instance fix**, a separate code for the unparsed, `lease not written` and
  no-python reads only. It leaves a `check_fence_beat` failure classed `fenced`, which the skeptic named.
- **S4 by the finder's instance fix**, the cache preferred only when this follow's ref read did not
  answer. It leaves the stale ref winning whenever the remote answers again at the follow.
- **S6 by removal.** The record offers it; with S4's rule the store a tail came from is the one fact a
  reader of a re-rendered card needs, so the variable gains its reader instead.

## 5. Production-readiness checklist

- security — none of the eight widens a surface; S3 narrows when a holder is told to abort.
- perf / scale — S1 adds 22 plants to the kickoff leg, about ten minutes by §4's readings, so its budget
  row is re-priced; S5's check is one `ast` parse per loop-kit module.
- error / empty / loading states — S3's non-answer is `unreachable`, a retry; S4 with no store holding a
  card still returns 1.
- observability — S6 prints the store a follow's tail came from.
- risks — a plant gated by S1 that misses for a cause outside this write set holds the unit open; it is
  parked with its cause, never waived. S5's re-pricing costs about half an hour of direct-CLI plant runs.
- testing — the probes of §6 and the arms in §7.
- migration — none; no data moves.
- user docs — none: no page under `help/` names the card store's lines, the lander's re-fence outcome or
  the budget rows; `help/loop.md` names `--entry-claim` without its exit codes.

## 6. Acceptance criteria

- **AC1** — When `bash skills/session-kickoff/card-store.fixture.sh --plant <name>` runs once for each
  name `--list` prints, every run exits 0 with no `MISSED` line; and
  `grep -c 'for cs_plant in publish publish-off' skills/session-kickoff/manifest-check.test.sh` prints 0
  while the suite's loop reads `--list`.
  Red when: the loop names a hand list; at 95c3103ad the loop names 8 of the 30 plants `--list` prints,
  its RED-first reading.
  cost: about thirteen minutes on node d for the thirty runs, by §4's readings.
- **AC2** — When a probe evaluates `resolve_node_tag`, cut by `awk` from the run-gates kit's self-test
  runner, over a scratch root whose `AGENTS.md` registry holds the user's first character at tag `s`
  above the user at tag `t`, it prints `t`; and when a probe evaluates `derive_node_tag`, cut from
  `skills/session-kickoff/manifest-check.sh`, over a scratch registry naming the user, with `USERNAME`
  upper-cased, it prints that row's tag and not `UNKNOWN`.
  Red when: a resolver matches by substring or case-sensitively; staged in scratch copies by the
  pre-S20 `case` line and the case-sensitive compare, the probes print `s` and `UNKNOWN`, and at
  95c3103ad neither suite feeds either input, so both staged rules pass there, its RED-first reading.
- **AC3** — When a probe evaluates `read_fence_line` and `check_fence_beat`, cut from `tools/push-main.sh`
  by `awk`, against a stub driver answering `--lease fence build fx --after <tip>`, it returns 4 for an
  exit-2 `lease not written — x` line, 4 for a fence line whose beat is not parented on the tip, and 1
  for a `lease refused — live-holder` line.
  Red when: a non-answer returns 1; at 95c3103ad both non-answers return 1, which
  `derive_push_failure` reads as `fenced` with the `claim-lost` remedy, its RED-first reading.
- **AC4** — When `bash skills/session-kickoff/card-store.fixture.sh --plant follow-offline-publish` and
  `--plant follow-offline-publish-online` run, each exits 0 and its follow's card carries the offline
  publish's tail.
  Red when: the stored tail is read ref-first; staged by the fixture beside a copy of the engine at
  95c3103ad, each plant prints `MISSED` with the older tail, its RED-first reading.
- **AC5** — When a probe evaluates `check_plant_tokens`, cut by `awk` from the run-gates kit's self-test
  runner, over
  the tip's `tools/run-gates/selftest-budgets.txt` it reports no finding; and over a scratch copy whose
  placement row reads `plants=15` it reports that row with 29.
  Red when: a row's count differs from its module's `PLANTS`; at 95c3103ad the placement row prices
  fifteen plants against 29 and no check reads it, its RED-first reading.
  figure: 29 is DERIVED by `ast` over `PLANTS` at the probe; 15 is the staged break.
- **AC6** — When AC4's `follow-offline-publish` plant runs, its follow's `card —` line carries
  `tail from cache`; and `python tools/memory-tree/gotchas.py --for-paths skills/session-kickoff/manifest-check.sh`
  prints `global-set-and-never-read`.
  Red when: `CARD_STORED_FROM` is assigned and read nowhere; at 95c3103ad
  `grep -rn CARD_STORED_FROM skills tools` prints only lines that assign it or name it in a comment,
  its RED-first reading.
- **AC7** — When `grep -n '^FLOOR_ASSERTIONS=' tools/hooks/scratch-guard.test.sh` runs, it prints a value
  one above the pin the file held before this unit, and `grep -c '^# [0-9]* = [0-9]* + .*AC28'
  tools/hooks/scratch-guard.test.sh` prints 1.
  Red when: the floor leaves AC28's rows out; at 95c3103ad the pin reads 396 and the second grep prints 0,
  its RED-first reading.
- **AC8** — When `grep -c '0 claimed, 1 refused, 2 not written, 3 budget spent, 4 waiting, 5 a fresh
  slug owed' tools/unattended/unattended.sh` runs, it prints 1; and
  `python tools/memory-tree/gotchas.py --for-paths tools/unattended/unattended.sh` prints
  `usage-exit-list-lags-its-function`.
  Red when: the usage line omits a return; at 95c3103ad the same grep prints 0, its RED-first reading.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `manifest-check self-test` · `run-selftests self-test` · `every held leg is budgeted, every budget row resolves` · `push-main self-test` · `scratch-guard self-test` · `agent-cap self-test` · `hook destinations self-test` · `verifier fan-out self-test` · `review-join self-test` · `unattended kit gate` · `tier2-review self-test` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `recall floor` · `recall floor arms` · `testsuite counts (every bar self-test prints one)` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `lexicon naming predicates`

New arm: skills/session-kickoff/manifest-check.test.sh · covers AC1 AC2 AC4 AC6 · the hand list of 8 restored, the case-sensitive node compare restored, and the engine of 95c3103ad under the two S4 plants · FLOOR_ASSERTIONS raised by the rows added
New arm: tools/run-gates/run-selftests.test.sh · covers AC2 AC5 · the substring case restored, and a budget copy whose placement token reads 15 · none, the suite pins no floor
New arm: tools/hooks/scratch-guard.test.sh · covers AC7 · the every-host AC28 row deleted, which the floor of 95c3103ad absorbs as slack and the raised floor reds · FLOOR_ASSERTIONS raised by one
New arm: tools/unattended/unattended.test.sh · covers AC8 · the usage line of 95c3103ad, which omits the returns 2 and 3 · waived for this build's landing by README rule 8, so its clean reading is owed with PLAY-dClosedLoop-14
New arm: tools/push-main.test.sh · covers AC3 · the exit-2 answer and the bad-beat fence line on the after call, staged against the classifier of 95c3103ad that reads both as fenced · the floor TOOL-dPlacedRequest-98 pins, raised by the two rows

## 8. Open questions

- **F1 — What does S5's check compare a row against?** (a) A `plants=<n>` token every loop-kit row
  whose leg runs a module with `PLANTS` must carry, equal to that dict's size, each row re-priced where
  its reading covered fewer. (b) The same token, compared only where a row carries it, placement's row
  the first. (c) The prose count, read as an English number word. (c) reads a word list of mixed nouns,
  plants, cases and sums, and a false match is silent. (b) leaves the 12 other mismatched rows
  unchecked, the follow-up the record's "each loop row" asks to close. (a) is the record's fix as stated
  and trips no veto of BUILD-METHOD M3; its cost is the re-pricing, stated under §5. RESOLVED (agent,
  2026-11-20, delegated): (a), the feature-rich survivor. widens: none · relaxes: none
- **F2 — `CARD_STORED_FROM`: print it or remove it?** (a) Print it on the stored-mode success lines;
  (b) remove the variable, its assignments and its mention. Both are judged SOUND by the skeptic. (a)
  satisfies the record and gives S4's plants a line to read; (b) is smaller. RESOLVED (agent,
  2026-11-20, delegated): (a), the feature-rich option, no veto tripped. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-20 · initial draft, the minors batch of the closing diff review: round 1 M1 and M2
  (finding ids 4 and 5), round 2 M1, M2, M3, L1, L2 and L3 (finding ids 2, 3, 1, 4, 6 and 8), promoted by
  round 2's exit as one unit.

## 10. Reuse audit

Every item extends a seam already in the tree: the fixture's own `--list` verb for S1, each suite's
existing registry fixture for S2, `tools/push-main.sh#read_fence_line`'s return codes for S3,
`skills/session-kickoff/manifest-check.sh#read_card_stored` for S4 with the fixture's plant table,
`tools/run-gates/run-selftests.sh --check`'s declaration walk for S5, and the gotchas catalogue's record
shape for S6 to S8. `python tools/codebase-map/reuse_lookup.py "the build card's stored tail chosen by
freshness over the selected stores"` and `python tools/codebase-map/reuse_lookup.py "a budget row's
plant count compared with the suite's plants"` ranked name stems only, `read`, `check` and
`resolve`, no seam beyond those named. The recall query below returned both round records and
`TOOL-dPlacedRequest-2`'s scout; where the records' line numbers disagree with the source, this spec
cites the source: the usage line is line 55, not 56, and the round-1 record's eight-plant count is the
source's, its finder's 33 is not.

Recall terms used: card-store.fixture.sh plants --list read_card_stored card.store read_fence_line derive_push_failure resolve_node_tag selftest-budgets FLOOR_ASSERTIONS entry-claim usage
