# KICK-dKeptSession-64 — the round-4 minors batch's audit's 20 minor findings, closed after the batch they land on is built

**Status:** DEFERRED · rev-2 · 2026-10-26 · node a · Tier-2 · base 462d20f3 · streams kickoff · order 35 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-64-deviation-641.md](../build/2026-10-26-build-KICK-dKeptSession-64-deviation-641.md) | deviation | — |
| [2026-10-26-build-KICK-dKeptSession-64-promoted-fix-return.md](../build/2026-10-26-build-KICK-dKeptSession-64-promoted-fix-return.md) | research | — |
| [2026-10-26-prompt-KICK-dKeptSession-64-promoted-fix-brief.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-64-promoted-fix-brief.md) | research | — |
| [2026-10-26-review-KICK-dKeptSession-64-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-64-spec-audit.md) | spec-audit | — |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of `KICK-dKeptSession-63`
(`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-63-spec-audit.md`)
confirmed 13 findings at MEDIUM and 7 at LOW, with no blocker and no high. BUILD-METHOD M4 promotes
them into one batch, and this is it. Each finding is its own §2 item, named by report id beside its
report item:

- MEDIUM: ids 4, 15 and 19 (M1), 1 (M2), 12 (M3), 2 and 20 (M4), 3 (M5), 14 (M6), 5 (M7), 11
  (M8), 13 (M9), 21 (M10);
- LOW: ids 6 (L1), 7 and 17 (L2), 8 (L3), 9 (L4), 10 (L5), 18 (L6).

Ids sharing a report item describe one defect, so each takes its own item and one edit closes the
group. Every finding lands on unit 63, so this unit builds one step after it (order 35) and amends
what that unit built. Where an item supersedes a text of unit 63 or of a sibling, it does so by
name, and that unit's acceptance ledger answers the superseded text by this unit's id (AC2, AC4 and
AC17).

## 2. Scope (IN)

- **S1** — id 4, M1. The order and the predicate of `KICK-dKeptSession-63` S15's batched
  `--mail ack <slug> [<id> ...]`, per id after the dedupe: first `KICK-dKeptSession-5` S8's
  addressed-to check; then the "already acked" read, which is the id's `state` column in
  `read_mailbox <slug> cache` (63 S11) read as `acked` by unit 5 S7, a cached ack naming the id in
  `answers`; then, only
  for an id not read as acked, `derive_message_id` and `check_mail_duplicate`. A skipped id never
  reaches `check_mail_duplicate`, is named on stderr as `mail — already acked <id>` and is left out
  of the batch. Observed by AC1.
- **S2** — id 15, M1. The exit contract of `--mail ack`, superseded by name for that verb alone:
  unit 5 S5's "a duplicate post exits 1" and `KICK-dKeptSession-22`'s retry row (`check_mail_duplicate`
  rc 1, refused) never reach an id S1 reads as acked. An rc 1 on an id not read as acked, any rc 2,
  or a failed addressed-to check refuses the batch with exit 2. Exit 1 stays a lost write, so
  `KICK-dKeptSession-42` AC4's `ack not posted` refusal reads it unchanged. The `--mail ack` line of
  `tools/unattended/VERBS.template.md` and of its render states the skip and the three exits. The
  ledgers of units 5 and 22 answer the two superseded texts. Observed by AC2.
- **S3** — id 19, M1. A batch whose every id S1 skips exits 0 and writes nothing. A mixed batch
  lands only the ids not skipped, in one `write_mail_ref`, and exits as that write does. 63 AC15
  reads with the second call's exit asserted `0` and a mixed batch `<a> <c>`, `<a>` already acked,
  that lands only `<c>`'s ack. Observed by AC1 and AC3.
- **S4** — id 1, M2. Every sibling text 63 §2 supersedes or says "reads as", and that 63 AC27
  leaves out, is answered in its unit's acceptance ledger by this unit's pass. They are unit 59's §4
  literal-read sketch (63 S8 and S26); unit 61's AC3, its §4 Files touched with "`derive_mail_chain`
  and its caller", its §5 observability and user-docs lines and its §7 arm (63 S11 and S22, and S5
  here); and unit 62's S19 (63 S23), S31 (63 S24) and §5's "seven definitions" (63 S2). The unit 62
  text 63 names two ways is spelled "S15 and §4's ack-chain sketch" in every answer. Observed by AC4.
- **S5** — id 12, M3. 63 S11's "never minted" reads as an explicit retirement: this unit's pass
  removes `read_mail_chain` and the `--mail chain` dispatch row from `tools/unattended/unattended.sh`,
  and the `--mail chain` line from `tools/unattended/VERBS.template.md` and its render, wherever unit
  61's or unit 63's pass left them. Unit 61's AC3 case in `tools/loop/selftest.py` reads
  `--mail read <parent> --cached --sent` instead. Observed by AC5 and AC4.
  **Readers:** by name: READER NOT IN TREE — the function and the verb are unit 61's, unbuilt at
  this base, and their readers are unit 61's own `--mail chain` line in the VERBS template, its
  loop-selftest AC3 case and its §5 lines, each re-pointed or answered here ·
  by value: NO VALUE READERS — the verb's rows are read only by unit 61's AC3 case, which this item
  re-points.
- **S6** — id 2, M4. 63 AC9 reads as S7's class. Each unit of the population 63 S9 derives, by
  `python tools/check-spec-tokens.py --legs-for` over every unit's `### Files touched (estimate)`,
  carries exactly one ledger line: the leg list, a `GAP —` line with the query's exit and output,
  or a `NOT RUN —` line with the reason. No line names a leg the manifest at that pass lacks. Units
  58, 59, 60 and 61 are members of that population, never lines fixed in advance, and 63's ledger
  lists the population it derived. Observed by AC6.
- **S7** — id 20, M4. 63 S17 reads as the class: a ledger line names a leg only when
  `tools/gate-legs.json` at that pass carries it, and otherwise opens
  `NOT RUN — <leg> not declared`, for `policy fixtures` and `loop selftest` alike and for any leg a
  later base declares.
  This unit's pass writes or corrects the lines of units 58 to 61 by that rule. Observed by AC7.
- **S8** — id 3, M5. 63 S13's sentence "This unit's pass re-checks the step on its own tree" is
  withdrawn, because on a tree whose manifest lacks the leg that check cannot fail. The step's
  liveness is this unit's probe over a scratch repository whose manifest declares the leg. The step
  at the real reconcile is owned by the reconcile pass, which records the join's output in this
  build's ledger. Observed by AC8.
- **S9** — id 14, M6. 63 S13 reads as the class. At each reconcile, every leg that the reconciled
  base's `tools/gate-legs.json` declares and HEAD's did not is added to the backtick leg line of
  every non-terminal spec of this build that the guards join names for it, each edit a rev bump with
  its §9 line. The new names are derived by comparing the `name` sets of the two manifests, so
  `policy fixtures` is one instance and `loop selftest` is the next, once dDeclaredLoop lands it.
  The step runs again at every reconcile. Observed by AC9.
- **S10** — id 5, M7. 63 S14's unset of `GOV_REMOTE` and `GOV_DEFAULT_BRANCH` sits in
  `tools/runlog/selftest.py` at import, as a module-level `del os.environ[...]` beside the `GIT_*`
  loop (`:355-356`), never in `build_arm_env` (`:1515-1520`), which copies `os.environ` for
  subprocess runs only. The in-process `rl_model.build_run_model` call (`:2585`) reaches
  `resolve_remote` (`tools/runlog/model.py:623`, reading `GOV_REMOTE` at `:652` and
  `GOV_DEFAULT_BRANCH` at `:673`) through `read_refs` (`:690`), and the scrub at import covers it.
  Observed by AC10.
- **S11** — id 11, M8. 63 S7's sentence reads as what is true. `tools/unattended/unattended.test.sh`
  is a withheld suite: `tools/unattended/kit.toml:47-50` records that its file ships and its leg
  does not, no leg of `tools/gate-legs.json` runs it, and it runs only through
  `tools/unattended/run-unattended-gates.sh` and the `unattended driver selftest shard <k>/8` rows
  of `tools/run-gates/selftest-budgets.txt:122-129`. The floor that moves is the effective
  `FLOOR_ASSERTIONS` pin (`:17940`), never the SHADOWED one at `:17665`, together with the
  `FLOOR_SHARD_<k>` line (`:18077-18141`) of the region holding the case, each by the case's counted
  assertions. The gap is recorded as `[gate]` requires: the main loop's close observes the case red
  and green by running the shard row that holds it. Observed by AC11 and AC17.
- **S12** — id 13, M9. Files touched names `memory/guides/UNATTENDED-VERBS.md`, the render of
  `tools/unattended/VERBS.template.md`, regenerated by `bash tools/unattended/adopt-unattended.sh`,
  which `check-unattended.sh` check 10 compares to the template (`:3152-3153`, `_c10_cmp` at
  `:3166`). This unit's pass leaves the two equal. Observed by AC12.
- **S13** — id 21, M10. The ask row 63 §8 F1 files in `memory/builds/dPlacedRequest/BACKLOG.md`
  reads with all three input shapes of `write_gov_ref`. A deletion, an empty `<src>`
  (TOOL-dPlacedRequest-11 S1), keeps TOOL-dPlacedRequest-13 S3's single deletion event, which
  `KICK-dKeptSession-23` relies on for the mailbox prune. A create, an empty expected sha, appends
  the new chain oldest first. An update appends the chain the feed does not hold, oldest first. The
  row's accept clause requires a deletion through `write_gov_ref` to append exactly one event, and
  the row names the writer's callers outside this build: `write_claim`, `write_red_ref` and
  `remove_red_ref` (TOOL-dPlacedRequest-11 S3), and the card-ref writes of TOOL-dPlacedRequest-2 and
  -33. This unit's pass rewrites the row 63 filed, keeping its id, or files it where 63 did not.
  Observed by AC13.
- **S14** — id 6, L1. 63 S25's `MARKER_LEAD` in `tools/lib/resolve-python.test.sh` is spelled as an
  ERE, `(# |// )`, and every site reads it as one: the awk extractor `blk` (`:213`) natively, the
  population read (`:218`) as `git grep -lE` and the count `nblk` (`:224`) as `grep -cE`. Observed by
  AC14.
- **S15** — id 7, L2. The two order-gate comments in `tools/unattended/unattended.sh`, already in
  63's write set, say that units sharing an `order` value are candidates for one parallel group, and
  that the edge refusal can still sequence them: `:13649` and the edge-refusal comment at `:13692`.
  Observed by AC15.
- **S16** — id 17, L2. 63 S24's population is derived, not listed: every hit of
  `git grep -n -i 'parallel group' -- tools memory/map` says "candidates for one parallel group"
  on one line. At
  this base that adds `tools/unattended/unattended.test.sh:6398`,
  `tools/workflows/unattended-build.test.sh:1353`, `tools/memory-tree/gen_build_index.py:1717` and
  the prompt string at `tools/workflows/unattended-build.js:2078` and its template twin at
  `tools/workflows/unattended-build.template.js:2078`, edited to the same bytes. The one exclusion
  is `tools/memory-tree/SPEC-TEMPLATE.template.md:84`, which unit 62 §8 F1 hands to the owner with
  `memory/TEMPLATE-SPEC.md:84`. Observed by AC16.
- **S17** — id 8, L3. 63 §4 Evidence's `_check_inside` sentence reads as: `_check_inside` (defined
  at `tools/runlog/extract.py:176`) guards `scan_preflights` (`:1004`) among others (`:252`, `:258`,
  `:278`, `:961`), while `measure_tree` (`:1135`) and `measure_ready_tree` (`:1209`) glob without
  it. 63's ledger answers the sentence. Observed by AC17.
- **S18** — id 9, L4. The walk of S13's row is TOOL-dPlacedRequest-13 S4's `add_feed_sightings`,
  never a second walk: after S3 sets the cache ref `refs/gov/remote/<tail>`, `write_gov_ref`'s
  success exit calls that walk over the one ref, either by the existing function or by S4's walk
  factored per ref and called from both sites. The walk stops at the newest commit the feed holds
  for the ref, which for an update is the tip read, and at the first commit not authored
  `gov-claim`; every mail commit is authored `gov-claim` (TOOL-dPlacedRequest-11 S2), so a chain is
  never cut short. §8 F1 records the choice. Observed by AC18.
- **S19** — id 10, L5. The re-check of S9 is the existing guards join in `tools/check-spec-tokens.py`
  (`:1543-1576`), which the `spec tokens (a spec's own names resolve)` leg runs. At the reconciled
  tip that join prints no `guards` hit `<leg> <- <path>` for any spec of this build. 63 AC13's
  `--legs-for` population is withdrawn, since `print_legs_for` (`:637-674`) prints broad-only trips
  that the join excludes (`:1580`). 63 S9's ledger population keeps `--legs-for`, a query and not a
  gate. Observed by AC8 and AC19.
- **S20** — id 18, L6. Files touched names `memory/map/generated/symbols.json`, regenerated by
  `python tools/codebase-map/gen_map.py --write`, since 63 adds the top-level `derive_kit_imports`
  to `tools/runlog/selftest.py` and the unguarded `codebase-map coverage + freshness` leg compares
  that render. This unit's pass leaves it fresh. Observed by AC20.

## 3. Non-goals (OUT)

- Rewording sibling specs: each superseded text is named here and answered in its unit's ledger.
- The report's left-shift gates: the ledger lint, the spec-tokens checks and the reconcile step in
  the lander are each a separate gate, so a separate unit by M2, and no clause of this build names
  the bug-class checklist.
- A gate leg that runs `tools/unattended/unattended.test.sh`: the leg is withheld by the ruling
  `tools/unattended/kit.toml:47-50` records, and a new leg is its own unit.
- The two template texts at `:84`, which unit 62 §8 F1 hands to the owner.
- Renumbering any order.

### Edges

- **consumes-from** `KICK-dKeptSession-63` — the batched `--mail ack`, the `cache` and `sent` read, S9's population, S13's and S17's rules, S14's scrub, S24's reword, S25's marker lead and §8 F1's ask row, which every item here amends (all 20 ids)
- **consumes-from** `KICK-dKeptSession-5` — S5's exit contract, S7's `acked` state and S8's `--mail ack` and its addressed-to check, which S1 to S3 order and narrow for a skip (ids 4, 15, 19)
- **consumes-from** `KICK-dKeptSession-22` — the retry row of its red-case table and `check_mail_duplicate`'s rc 1, which S2 supersedes for `--mail ack` (id 15)
- **consumes-from** `KICK-dKeptSession-59` — §4's literal-read sketch, whose ledger answer S4 reads (id 1)
- **consumes-from** `KICK-dKeptSession-61` — AC3, §4 Files touched, §5, §7's arm and the loop-selftest case, which S4 reads and S5 re-points to `--mail read <parent> --cached --sent` (ids 1, 12)
- **consumes-from** `KICK-dKeptSession-62` — S19, S31, §5's "seven definitions" and S15 and §4's ack-chain sketch, whose ledger answers S4 reads (id 1)
- **consumes-from** external — TOOL-dPlacedRequest-13 S3's success exit and S4's `add_feed_sightings`, and TOOL-dPlacedRequest-11 S1's input shapes, which the amended ask row names (S13, S18)
- **hands-off** external — the amended ask row in `memory/builds/dPlacedRequest/BACKLOG.md`, for dPlacedRequest to build (S13, S18)
- **hands-off** `KICK-dKeptSession-65` — the batched `--mail ack`'s skip and order, S5's retirement, S7's and S9's reconcile rules, S10's scrub, S13's and S18's ask row, S14's marker lead, S16's reword, S17's citations, §3's left-shift bullet, §4's Evidence and sketch and AC5, AC8 to AC11, AC17 and AC18, which the batch amends (all 26 ids of the round-5 minors batch's audit)

## 4. Design

### Evidence

Each item's evidence is the audit's appendix row for its id, re-read for this spec on 2026-10-26.
Re-verified at this base: `tools/runlog/selftest.py` deletes every `GIT_*` variable at module level
(`:355-356`), `build_arm_env` (`:1515-1520`) returns a copy of `os.environ` with `DECOY_VARS`
aimed at scratch, and `rl_model.build_run_model` runs in-process at `:2585`;
`tools/runlog/model.py`'s `resolve_remote` (`:623`) reads `GOV_REMOTE` at `:652` and
`GOV_DEFAULT_BRANCH` at `:673`, and `read_refs` (`:677`) calls it at `:690`. No leg of
`tools/gate-legs.json`, `tools/run-gates/run-gates.sh` or `.github/workflows/remote-ci.yml` names
`unattended.test.sh` or `run-unattended-gates`; `unattended.test.sh` holds `FLOOR_ASSERTIONS=675`
marked SHADOWED at `:17665`, the effective `FLOOR_ASSERTIONS=2776` at `:17940` and the eight
`FLOOR_SHARD_<k>` lines at `:18077-18141`. `diff` of the CR-stripped `VERBS.template.md` and
`memory/guides/UNATTENDED-VERBS.md` prints nothing. `resolve-python.test.sh` spells `^# >>> ` at
`:213`, `:218` and `:224`. `git grep -n -i 'parallel group' -- tools memory/map` prints ten lines:
the seven S15 and S16 name, the two 63 S24 names and the excluded template line.
`extract.py` calls `_check_inside` at `:252`, `:258`, `:278`, `:961` and `:1004`, and
`scan_preflights` opens at `:991`. `symbols.json` lists 253 symbols of `tools/runlog/selftest.py`.
`tools/check-spec-tokens.py` runs the guards join at `:1543-1576`, and `derive_legs_path` (`:271`)
finds a fixture tree's one `gate-legs.json`, which the probe of AC8 relies on. `origin/main`'s
manifest declares `policy fixtures` with guard `{prefix}/policy/` and no `loop selftest`; this
branch's declares neither. No `write_gov_ref` or `add_feed_sightings` exists in the tree: both are
TOOL-dPlacedRequest-11 and -13 specs, and the F1 ask row is not filed yet.

### The ack batch, in order

```
--mail ack <slug> <id> [<id> ...]                 ids deduped, the first of each kept
  per id: addressed-to check (unit 5 S8)          -> fails: exit 2, nothing built
          state from read_mailbox <slug> cache    -> acked: skip, `mail — already acked <id>`
          derive_message_id, check_mail_duplicate -> rc 1 or 2: exit 2, nothing built
  no id left                                      -> exit 0, nothing written
  write_mail_ref <ref> <tip read> <ack> ...       -> 0 landed · 1 lost write · 2 not completed
```

### Inventory

None minted. Each name an item uses is minted by unit 5, 22, 61, 63 or TOOL-dPlacedRequest-13.

### Migration

None: no stored record changes shape. The skip writes nothing, and the ask row changes only which
feed lines a later unit appends.

### Files touched (estimate)

- `tools/unattended/unattended.sh`: S1 to S3, S5, S15
- `tools/unattended/unattended.test.sh`: S1, S3, S5 and S11's floors, S16
- `tools/unattended/VERBS.template.md`, `memory/guides/UNATTENDED-VERBS.md`: S2, S5, S12
- `tools/loop/selftest.py`: S5
- `tools/runlog/selftest.py`: S10
- `tools/lib/resolve-python.test.sh`: S14
- `tools/memory-tree/gen_build_index.py`: S16
- `tools/workflows/unattended-build.js`, `tools/workflows/unattended-build.template.js`,
  `tools/workflows/unattended-build.test.sh`: S16
- `memory/map/generated/symbols.json`: S20
- `memory/builds/dKeptSession/build/`: the ledger lines of S2, S4, S6, S7 and S17
- `memory/builds/dKeptSession/spec/`: S9's leg lines, at reconcile
- `memory/builds/dPlacedRequest/BACKLOG.md`: S13's and S18's ask row

### Alternatives rejected

- **Two batches.** The mail half and the rest both write `tools/unattended/unattended.sh` (S1 and
  S15) and the ledgers under `memory/builds/dKeptSession/build/` (S2 and S6), so the two write sets
  are not disjoint by M6's clauses.
- **An rc 1 from `check_mail_duplicate` read as the skip, for S1.** That reads any equal-fields
  collision as acked; the `acked` state of unit 5 S7 is the one predicate that says an ack exists.
- **A new leg, or the case moved into `check-unattended.sh`, for S11.** The leg is withheld by
  ruling, and a behaviour case does not belong in the kit's gate; the shard runner already runs the
  suite.
- **A second first-parent walk inside `write_gov_ref`, for S18.** It is 63 F1's option (a); see §8.

## 5. Production-readiness checklist

- security — S1 checks every id before any commit, as 63 S15 does; a skip writes nothing.
- perf / scale — S1 reads the cache once per batch; S18 reuses S4's walk, which stops at the tip read.
- error / empty / loading states — a fully skipped batch exits 0 and writes nothing (S3); a
  non-success query writes a `GAP —` or `NOT RUN —` line (S6, S7).
- observability — each skipped id is named on stderr (S1); each ledger line carries the query's exit
  and output (S6).
- risks — S13's ask changes the success exit every governance-ref writer shares: `write_claim`,
  `write_red_ref`, `remove_red_ref`, the card-ref writes and this build's `write_mail_ref`; a
  single-commit update still appends one event, since the walk stops at the tip read.
- testing — the criteria of §6 and the arms of §7.
- migration — §4.
- user docs — the `--mail` section of `tools/unattended/VERBS.template.md` and its render state the
  skip and the exits of `--mail ack` (S2) and name no `--mail chain` (S5).

## 6. Acceptance criteria

Fixtures are each repaired unit's own, named by that unit's spec, under `%TEMP%`.

- **AC1** — When `--mail ack <slug> <a>` runs twice in `KICK-dKeptSession-5`'s fixture repository
  through a scratch copy of `unattended.sh` whose `check_mail_duplicate` prints `DUPCHECK <id>` on
  stderr, the second call prints `mail — already acked <a>`, prints no `DUPCHECK <a>`, exits `0`,
  and leaves the session ref's tip, read by `git rev-parse`, where the first call put it.
  Red when: the duplicate check runs first and the second call exits 2 with `mail — duplicate`.
- **AC2** — When `grep -n "KICK-dKeptSession-64"` runs over the acceptance ledgers of units 5 and
  22, it prints the answers to unit 5's S5 duplicate exit and unit 22's retry row, and
  `grep -n "already acked" tools/unattended/VERBS.template.md` prints the `--mail ack` line stating
  exit 0 for a skip, 1 for a lost write and 2 for a refusal.
  Red when: either superseded text has no answer, or the line names the skip without its exit.
- **AC3** — When `--mail ack <slug> <a> <c>` runs with `<a>` already acked, it exits `0`,
  `--mail read` shows one ack of each, and `git rev-list --count <tip before>..<tip after>` prints
  `1`; and
  `--mail ack <slug> <a> <a>` exits `0` with the tip unchanged.
  Red when: the mixed batch exits 2, lands nothing, or lands a second ack of `<a>`.
- **AC4** — When `grep -n "KICK-dKeptSession-64"` runs over the acceptance ledgers of units 59, 61
  and 62, it prints an answer to each text S4 names, and every answer to the unit 62 sketch spells
  "S15 and §4's ack-chain sketch".
  Red when: one listed text has no answer, so unit 61's AC3 stays in force.
- **AC5** — When `grep -c -e read_mail_chain -e "--mail chain"` runs over
  `tools/unattended/unattended.sh`, `tools/unattended/VERBS.template.md` and
  `memory/guides/UNATTENDED-VERBS.md`, each prints `0`, and
  `grep -n -- "--cached --sent" selftest.py`, run in the loop kit's directory, prints unit 61's AC3 case.
  Red when: the verb still prints rows, or unit 61's case still calls it.
- **AC6** — When a probe re-derives 63 S9's population with `check-spec-tokens.py --legs-for` over
  every unit's Files touched and reads the ledger, each unit in it carries exactly one line opening
  with a leg list, `GAP —` or `NOT RUN —`, and 63's ledger lists the population.
  Red when: a unit of the population has no line, or has two.
  figure: DERIVED, the population re-derived by the query at the pass.
- **AC7** — When a probe reads every leg named on a leg-list line S7 wrote and compares it with the
  `name` values `python -c` reads from that pass's `tools/gate-legs.json`, every one is declared;
  where the manifest declares neither leg, the lines owing them open
  `NOT RUN — policy fixtures not declared` and `NOT RUN — loop selftest not declared`.
  Red when: a line names `policy fixtures` while the manifest lacks it.
- **AC8** — When `python <repo>/tools/check-spec-tokens.py` runs in a scratch repository under
  `%TEMP%`, built as the spec-tokens self-test builds its fixtures (its lines 203 and 317), whose
  `tools/gate-legs.json` declares `policy fixtures` with guard `{prefix}/policy/`, with tracked
  stubs at the policy paths and copies of units 58, 59, 60, 62 and 63, it prints a `guards` hit
  `policy fixtures <- tools/policy/...` for unit 58's copy with the name left off its leg line, and
  no such hit once the name is on it.
  Red when: the left-off name prints no hit, so the step is never exercised.
  fixture: built by the probe; the tree holds none today.
- **AC9** — When `python -c` compares the `name` sets of AC8's base manifest, declaring neither
  leg, and a reconciled one that also declares `loop selftest` with guard `{prefix}/loop/`, it
  prints both names; with `loop selftest` left off unit 61's copy the join prints
  `loop selftest <- tools/loop/...`, and after the step it prints no `guards` hit for either.
  Red when: the step adds only `policy fixtures` and the loop hit stands.
- **AC10** — When a `python -c` probe parses the runlog kit's selftest module with `ast`, a
  module-level statement
  outside every function deletes `GOV_REMOTE` and `GOV_DEFAULT_BRANCH` from `os.environ` at or
  above the `GIT_*` loop's line, and the body of `build_arm_env` names neither variable.
  Red when: the unset sits only in `build_arm_env`, so `rl_model.build_run_model` reads an ambient
  `GOV_REMOTE`.
- **AC11** — When
  `git diff <parent of 63's pass>..HEAD -- tools/unattended/unattended.test.sh` is read at this
  unit's pass, the line marked `SHADOWED` is unchanged, and the effective
  `FLOOR_ASSERTIONS=` line and one `FLOOR_SHARD_<k>=` line each rise by the counted cases of 63's
  chain read and of this unit's S1, S3 and S5.
  Red when: the shadowed pin moved and the effective one did not.
  figure: PINNED, `675` and `2776` read at base on 2026-10-26; the rise DERIVED off the diff.
- **AC12** — When the CR-stripped template and render are compared at this unit's pass,
  `diff` over the process substitutions (`sed 's/\r$//' tools/unattended/VERBS.template.md`) and
  (`sed 's/\r$//' memory/guides/UNATTENDED-VERBS.md`) prints nothing.
  Red when: the template is edited alone and check 10 reds the drift.
- **AC13** — When `grep -n` reads the ask row in `memory/builds/dPlacedRequest/BACKLOG.md`, it
  names a deletion, a create and an update, the callers `write_claim`, `write_red_ref` and
  `remove_red_ref` and the card-ref writes, and an accept clause in which a deletion through
  `write_gov_ref` appends exactly one event.
  Red when: the row has no deletion case, so the mailbox prune's event is lost.
- **AC14** — When `grep -n 'MARKER_LEAD' tools/lib/resolve-python.test.sh` runs, the population
  read's line carries `git grep -lE` and the count's line `grep -cE`; and a probe running the
  count's command with `MARKER_LEAD='(# |// )'` over a scratch file holding one `# >>> s` and one
  `// >>> s` block prints `2`.
  Red when: a site reads the ERE value as BRE and counts `0`, so no copy is compared.
- **AC15** — When `git grep -n -i 'parallel group' -- tools/unattended/unattended.sh` runs, every
  line it prints says "candidates for one parallel group".
  Red when: `:13649` still says units sharing an order are the parallel group.
- **AC16** — When
  `git grep -n -i 'parallel group' -- tools memory/map ':!tools/memory-tree/SPEC-TEMPLATE.template.md' | grep -v -i 'candidates for one parallel group'`
  runs, it prints nothing, and `grep -c 'candidates for one parallel group'` prints `1` over each of
  `tools/workflows/unattended-build.js` and `tools/workflows/unattended-build.template.js`.
  Red when: the shipped workflow prompt still says a shared order is one parallel group.
- **AC17** — When `grep -n "KICK-dKeptSession-64"` runs over 63's acceptance ledger, it prints the
  answers to each 63 text superseded here: S7, S11, S13, S14, S15, S17, S24, S25, AC9, AC13, AC15,
  AC24, §4 Evidence's `_check_inside` sentence, §4 Files touched, §7's first arm line and §8 F1.
  Red when: a superseded text has no answer.
- **AC18** — When `grep -n` reads the same ask row, it names `add_feed_sightings` and
  TOOL-dPlacedRequest-13 S4 as the walk S3 calls, and `grep -c "first-parent commit between"` over
  the row prints `0`.
  Red when: the row asks for a second walk in `write_gov_ref`.
- **AC19** — When 63's ledger answer to its AC13 is read, it names the
  `spec tokens (a spec's own names resolve)` leg's `guards` hits as the criterion and carries no `--legs-for` population, and
  AC8's probe reads the join's output, never `print_legs_for`'s.
  Red when: the reconcile's re-check still takes its population from `--legs-for`.
- **AC20** — When `python tools/codebase-map/gen_map.py --check` runs at this unit's pass it exits
  `0`, and `grep -c '"derive_kit_imports"' memory/map/generated/symbols.json` prints `1`.
  Red when: the render is left stale and `--check` exits 1.

## 7. Gates

`build-index selftest` · `tier2-review self-test` · `unattended-build self-test` · `verifier fan-out self-test` · `review-join self-test` · `pre-push run-log line` · `run-gates run-log line` · `runlog selftest` · `recall floor` · `recall floor arms` · `python resolver (behaviour + inline parity + idiom ban)` · `unattended kit gate` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The loop kit's `loop selftest` leg runs its cases once dDeclaredLoop has landed it; S9 adds the name
to the line above at that reconcile.

New arm: tools/unattended/unattended.test.sh · covers AC1 AC3 AC5 · a twice-acked id, a mixed batch and an absent `--mail chain`, staged red by a scratch `unattended.sh` running `check_mail_duplicate` before the state read · the effective `FLOOR_ASSERTIONS` pin and its region's `FLOOR_SHARD_<k>` rise by the counted cases; a withheld suite run by the shard runner, not by a leg
New arm: tools/runlog/selftest.py · covers AC10 · an in-process `resolve_remote` over a remote-less scratch repository in a process started under `GOV_REMOTE=planted`, staged red by a copy whose unset sits in `build_arm_env` · none
New arm: tools/loop/selftest.py · covers AC5 · unit 61's AC3 case through `--mail read <parent> --cached --sent`, staged red by a copy still calling `--mail chain` · none
New arm: tools/lib/resolve-python.test.sh · covers AC14 · a `// >>>` block counted by the ERE sites, staged red by a BRE `grep -c` · none

## 8. Open questions

- **F1 — Which walk appends a chained landing's feed lines, ids 9 and 21?** Options: (a) 63 F1's
  pick, a new walk in `write_gov_ref`'s success exit over the first-parent commits between the tip
  read and the landed tip; (d) that exit calls TOOL-dPlacedRequest-13 S4's `add_feed_sightings` over
  the one ref after S3 sets its cache ref, or S4's walk factored per ref and called from both. (a)
  encodes the chain-order rule `check_feed` grades in a second appender, and its "between" has no
  meaning for a deletion or a create. (d) reuses the one walk, keeps S3's deletion branch, and
  meets AC13, AC18 and 63's AC16 through the same ask row. RESOLVED (agent, 2026-10-26, delegated):
  (d), rung 3. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, the round-4 minors batch's audit's minors batch.
- rev-2 · 2026-10-26 · §3 · the Edges bullet to `KICK-dKeptSession-65` mirrored, the other ends of
  the edges the round-5 minors batch's audit's disposal declared

## 10. Reuse audit

Every item extends the seam its repaired unit names: `read_mailbox`'s `state` column (unit 5 S6 and
S7) for S1 to S3; the guards join (`tools/check-spec-tokens.py:1543-1576`) for S8, S9 and S19; the
`GIT_*` scrub loop (`tools/runlog/selftest.py:355-356`) for S10; the shard rows of
`tools/run-gates/selftest-budgets.txt` and their runner for S11; the adopter's render
(`tools/unattended/adopt-unattended.sh:649`) for S12; `gen_map.py --write` for S20; and
TOOL-dPlacedRequest-13 S4's `add_feed_sightings` for S13 and S18.
`python tools/codebase-map/reuse_lookup.py "skip an id already acknowledged before the duplicate refusal"`
ranked `before`, `refusal`, `skip` and `read_id_list` by name stem only; no mail code exists at this
base, so no existing seam in the tree fits the ack order beyond the sibling specs' reader and
writer, which are the seams extended.

Recall terms used:
`python tools/memory-recall/query.py "how does a minors batch amend a batch unit that is not yet built" --terms "promoted batch minors ledger superseded skip refusal reconcile declared leg scrub carriers walk"`
