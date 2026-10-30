# DEPL-dShippedRelease-78 — the round-1 spec audit's 77 minors, batched: the Readers of what unit 10 retires, the legs and rows each unit owes, honest failure states, and the observations that read the wrong thing

**Status:** OPEN · rev-1 · 2026-10-30 · node d · Tier-2 · base f4597719 · streams deployer · order 32 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit, `reviews/2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md`,
confirmed 106 findings, and DEPL-dShippedRelease-49 to -77 take its 7 blockers and 22 highs. This
unit is BUILD-METHOD M4's batch of its 68 MEDIUM and 9 LOW by raw id, one scope item per id, in
report order, M1 to M58 and then L1 to L9. They land on 26 of the 31 units, so it repairs no unit in
particular and builds last, order 32, above every unit it repairs.

Every id: M1 5, 40; M2 8, 50; M3 9; M4 10, 38, 101; M5 11; M6 12, 66; M7 13; M8 14; M9 15, 81; M10
16; M11 17; M12 18, 98; M13 20; M14 21; M15 22; M16 24, 96; M17 26; M18 31, 60, 61; M19 33; M20 34;
M21 35; M22 36; M23 37; M24 39; M25 41; M26 42; M27 47; M28 48; M29 49; M30 51; M31 52; M32 53; M33
54; M34 55; M35 59; M36 62; M37 63; M38 67; M39 68; M40 69; M41 79; M42 80; M43 83; M44 87; M45 88;
M46 89; M47 90; M48 93; M49 95; M50 97; M51 99; M52 100; M53 102; M54 103; M55 105; M56 106; M57
107; M58 108; L1 19; L2 23; L3 25; L4 32; L5 43; L6 44; L7 56; L8 64; L9 109.

## 2. Scope (IN)

- **S1** — id 5, M1, landing on units 1, 2, 4, 13, 14 and 15. Each of those units'
  `kit version markers` reads as `kit version (one check)`, the successor column of
  `ended-legs.txt`. Observed by AC1.
- **S2** — id 40, M1, the same defect on the same lists. No §7 of this build is rewritten: the row's
  `ended-on` holds them, and `--list` names each. Observed by AC1.
- **S3** — id 8, M2, landing on unit 7. `remote_probe_py` reaches its copies by one `[[inline]]` row
  in `tools/lib/kit.toml`, never a literal `PARITY_ROWS` row. Observed by AC2.
- **S4** — id 50, M2. Unit 7's AC12 reads `python inline_blocks.py --rows` for the stem, and the
  block in `tools/govkit/kit_release.py` and `tools/run-gates/check_currency.py` is held by
  `--check`. Observed by AC2.
- **S5** — id 9, M3, landing on unit 21. Selfcheck arm 6c (`tools/govkit/govkit.py:2465`) passes a
  `[[generated]]` row with `write`, `check` and `stage` and no `path` on a not-installable entry, by
  a planted arm. Observed by AC3.
- **S6** — id 10, M4, landing on unit 31. AC6 of unit 31 reads each of S5's seven sites by its own
  text, six paths and seven sites. Observed by AC4.
- **S7** — id 38, M4. `WIRE-INTO-PROJECT.md`'s node-sense lines, and
  `tools/govkit/selftest.py:5510`, are kept, and the pinned list of kept lines is what the check
  compares. Observed by AC4.
- **S8** — id 101, M4. `tools/codebase-map/map_lib.py:62`, reading the whole fleet, is one of the
  seven and the pattern reads it. Observed by AC4.
- **S9** — id 11, M5, landing on units 3, 7, 10, 16 and 17. `kit-schema.toml` gains `[[field]]` rows
  `command`, `upgrade`, `layer` and `optional`, derived from the tree at the pass, and its README
  states that a new top-level key owes a row. Observed by AC5.
- **S10** — id 12, M6, landing on units 3, 7, 15 and 27. Each new `resolve_kit_dir` edge from a core
  kit carries its descriptor's `optional` row (part, point, fallback). Unit 15's AC3 runs the layer
  check, not an import grep. Observed by AC6.
- **S11** — id 66, M6, landing on units 5, 22, 24 and 26. Each such edge carries a `resolves` row,
  with the descriptor named. `kit conformance` is named in prose here and not on §7's line until it
  exists. Observed by AC6.
- **S12** — id 13, M7, landing on units 7, 11, 12, 16, 17, 19, 22 and 26. `deploy items` also runs
  `deploy_items.py --selftest`, and legs `offer selftest`, `kit walk selftest` and
  `tracker mirror selftest` join by `leg_factory.py new`; units 7, 19 and 26 put their fixture on
  their own leg's argv. Observed by AC7.
- **S13** — id 14, M8, landing on unit 27. `run_deploy_items` calls the `carries` write after
  `deploy.record`, so a real landing's `carries` is written. Observed by AC8.
- **S14** — id 15, M9, landing on units 1 and 12. Unit 1 S2 writes a record only for `landed-gated`,
  `landed-ungated` and `nothing-pushed`, an allow-list, and exits 1 naming any other class. Observed
  by AC9.
- **S15** — id 81, M9. `held` and `unlanded` are refused by that list, so S7's `already recorded`
  cannot pin a bad record. Observed by AC9.
- **S16** — id 16, M10, landing on units 7 and 16. Unit 7's AC13 is read at this unit's pass, after
  unit 16 lands `item.kits.offer`, and its ledger line says so. Observed by AC10.
- **S17** — id 17, M11, landing on units 17, 20 and 28. The two install rows of `KIT_HOOKS` are
  named `adopt-census` and `adopt-declarations`; file and receipt id key on that name. Observed by
  AC11.
- **S18** — id 18, M12, landing on unit 17. `attend` reads the step's witness first: a holding
  witness sets `applied`. Observed by AC12.
- **S19** — id 98, M12. A step whose `up` is a recipe prints it and stops the walk as `attended`,
  never `step-failed`, and rollback's `down` reads the same way. Observed by AC12.
- **S20** — id 20, M13, landing on units 10, 15 and 21. `core.py new kit` states `--purpose` as
  required, and each spelled command carries it. Observed by AC13.
- **S21** — id 21, M14, landing on unit 12. The `landing-turn` wait is one row, `on` the turn's ref,
  and its dead-holder case is planted. Observed by AC14.
- **S22** — id 22, M15, landing on units 4 and 5. `run_deploy_close` derives the outcome from
  `read_hold_answers` when `closes` is `after-release-verifies`; `--release-outcome` stays an
  override. Observed by AC15.
- **S23** — id 24, M16, landing on unit 6. `tools/integrations/release.py` joins its write set, and
  each value reads through a helper whose first argument is the key, `read_policy_value(f"...")`.
  Observed by AC16.
- **S24** — id 96, M16, landing on units 6 and 15. `check_environment_name` refuses a dotted name,
  naming the rule. Observed by AC16.
- **S25** — id 26, M17, landing on unit 27. The `commits.squash` read lives once, the literal in
  `tools/push-main.sh`, passed to `check_squash_landing` as a value, and a lander with no loop kit
  prints the `no loop kit` line. Observed by AC17.
- **S26** — id 31, M18, landing on unit 10. `memory/guides/SESSION-KICKOFF.md`'s source and
  `skills/session-kickoff/manifest-check.sh` name `govkit.py version`; no alias of the old verb
  ships. Observed by AC18.
- **S27** — id 60, M18. `tools/run-gates/selftest-budgets.txt` and
  `memory/map/features/row-grammar.md` hold no name unit 10 ended. Observed by AC18.
- **S28** — id 61, M18. `tools/push-main.sh`'s header, `WIRE-INTO-PROJECT.md`, `help/roles.md` and
  `tools/unattended/unattended.sh:3380` name the successors. Observed by AC18.
- **S29** — id 33, M19, landing on units 10 and 21. Govkit keeps its file row, and unit 10's rule
  exempts `installable = false` by name with a planted arm. Observed by AC19.
- **S30** — id 34, M20, landing on unit 4. `deploy.current` finds T as `check_prepared_merge` does,
  compares T^1 with the advertised tip and reads the verdict for T's tree. Observed by AC20.
- **S31** — id 35, M21, landing on unit 12. The second-node prior tip is `derive_landing_prior_tip`
  (DEPL-dShippedRelease-52), and unit 12's AC10 reads it on a stacked close. Observed by AC21.
- **S32** — id 36, M22, landing on units 7 and 16. The helper spelling is `!` then both paths
  through `shlex.quote(Path(p).as_posix())`. Observed by AC22.
- **S33** — id 37, M23, landing on unit 9. Parity compares CR-stripped, and the write keeps the
  file's existing line ending. Observed by AC23.
- **S34** — id 39, M24, landing on unit 1. AC9 reads the manifest by `json.load`, asserting the
  `deploy items` row's argv ends `deploy_fixture.py`, `--all`. Observed by AC24.
- **S35** — id 41, M25, landing on unit 13. The `running` ceiling counts from the mtime of the
  per-SHA log `tools/push-main.sh:454` writes, so a later landing cannot end the clock. Observed by
  AC25.
- **S36** — id 42, M26, landing on unit 13. `run_deploy_core` reads `GATE_POST_MERGE` through a
  shell-side verb of the lander, `push-main.sh --read-policy-key`, so no third parser exists.
  Observed by AC26.
- **S37** — id 47, M27, landing on unit 10. `kit_wiring.py` runs each row through
  `regen.run_command(argv, root, bound)` under `GATE_REGEN_BOUND`, and defines `read_check_rows`.
  Observed by AC27.
- **S38** — id 48, M28, landing on unit 26. `platform_matrix.py` carries `resolve_bash_py` inline
  and resolves a `bash` launch through it. Observed by AC28.
- **S39** — id 49, M29, landing on units 12 and 13. Every shell spawn of `deploy_items.py` resolves
  bash through the block the loop kit carries, the module holding the marker. Observed by AC29.
- **S40** — id 51, M30, landing on units 19 and 26. `read_job_conclusion` delegates to
  `read_remote_verdict`, step and pin checks off for an imported job, keeping only the walk over
  `JOB_WALK`. Observed by AC30.
- **S41** — id 52, M31, landing on unit 26. `read_remote_verdict` takes workflow, job, step and pin
  scope, in `tools/run-gates/remote_verdict.py`. Observed by AC31.
- **S42** — id 53, M32, landing on units 7, 8, 15, 22 and 26. One adapter per kit:
  `read_policy_value` in run-gates and in integrations, minted once in each, with one stated
  absent-kit rule. Observed by AC32.
- **S43** — id 54, M33, landing on units 10 and 26. `kit_factory.py --floor` prints the floor, and
  `ci_emit.py` reaches it through `resolve_kit_dir`. Observed by AC33.
- **S44** — id 55, M34, landing on units 15 and 22. Each shipped cadence row runs a dispatcher in
  `tools/runtime/` printing `not installed` and exiting 0 where its kit is absent. Observed by AC34.
- **S45** — id 59, M35, landing on units 9, 10, 15 and 21. `PROBLEM_PIN` reads the registry's count
  at the pass or each unanchored entry holds a `runbook_exempt` row, and unit 9 reads from that
  value to 0. Observed by AC35.
- **S46** — id 62, M36, landing on units 1, 6, 7, 8, 10, 15, 19 and 26. Each leg a unit mints or
  ends has its owning dossier's claim moved, `memory/map/baseline.toml` included. Observed by AC36.
- **S47** — id 63, M37, landing on units 1, 6, 7, 8, 15, 19 and 26. `tools/govkit/subject-pins.tsv`
  holds a row per new leg, by `govkit.py selfcheck --write`. Observed by AC37.
- **S48** — id 67, M38, landing on units 10 and 21. The dispatch of those units read the enumerated
  `kit.toml` paths, and this unit's ledger names them; each tripped narrow-guard leg ran at the
  close. Observed by AC38.
- **S49** — id 68, M39, landing on unit 3. Gov's `.claude/settings.json` gains a SessionStart entry
  for `tools/runtime/session-tick.sh`. Observed by AC39.
- **S50** — id 69, M40, landing on units 3, 7 and 31. `record_kinds.py --write` renders
  `tools/memory-tree/HYGIENE.template.md`, and `memory/HYGIENE.md` from it, for their kinds.
  Observed by AC40.
- **S51** — id 79, M41, landing on units 4 and 12. Closed by DEPL-dShippedRelease-59 S2; this item
  re-reads it for a direct `--land --slug`. Observed by AC41.
- **S52** — id 80, M42, landing on units 1 and 12. A write never replaces `landed-gated` or
  `landed-ungated` for one SHA, and `nothing-pushed` keeps the prior tip it finds. Observed by AC42.
- **S53** — id 83, M43, landing on unit 14. Closed by DEPL-dShippedRelease-60 S1; this item re-reads
  the `pending` arm on a re-walk. Observed by AC43.
- **S54** — id 87, M44, landing on unit 16. A symlink under a path the mode writes refuses as
  `undeliverable`, the clone walked first. Observed by AC44.
- **S55** — id 88, M45, landing on unit 16. A probe's refusal counts only from a remote that still
  answers; auth or transport failure and a probe ref left on the remote are `undeliverable`, the ref
  named on the order. Observed by AC45.
- **S56** — id 89, M46, landing on unit 16. The disposition gains exit 2, a signal and a timeout,
  each `undeliverable`; an existing `gov/update-<release>` compares trees and reports
  `already offered`; the `order` row resets what `update --write` staged. Observed by AC46.
- **S57** — id 90, M47, landing on unit 16. The census grades the call site: each `refuse` key's
  calls from `_cmd_update` sit under a guard reading the mode. Observed by AC47.
- **S58** — id 93, M48, landing on unit 25. An empty local tag list consults the remote when one
  resolves and `GOVKIT_NO_REMOTE_PROBE` is unset; tags there refuse naming the fetch, and a dead
  remote prints that the list was unverified. Observed by AC48.
- **S59** — id 95, M49, landing on unit 15. Exit 3 re-reads the lease epoch: still the holder
  re-picks under a new id or raises an item, and any engine exit outside the table is unreachable.
  Observed by AC49.
- **S60** — id 97, M50, landing on units 16 and 29. The offer computes the composition report in
  gov's process over the target's tree as data, and the order carries it. Observed by AC50.
- **S61** — id 99, M51, landing on unit 26. The row whose `uname` names this host is the running
  bar, whose exit writes that platform's record, and `launch` applies to other rows. Observed by
  AC51.
- **S62** — id 100, M52, landing on unit 31. `register` grades key, branch and remote, escapes the
  TOML row, and refuses a re-register changing `remote` with no flag. Observed by AC52.
- **S63** — id 102, M53, landing on unit 3. `kits.cut` refuses on a `refused` record, fetches the
  tip first, leaves no local tag after a failed push, and takes the witness from the remote.
  Observed by AC53.
- **S64** — id 103, M54, landing on units 7 and 16. A currency record older than a stated bound reds
  naming its age, and the fetch and the clone carry a timeout reading `unverified` or
  `undeliverable`. Observed by AC54.
- **S65** — id 105, M55, landing on unit 4. `deploy.current` adds exit 2, a dead probe with no
  `comparison` record, and names `HELD` and `NONE`. Observed by AC55.
- **S66** — id 106, M56, landing on units 1 and 12. The race fixtures hold the first process on a
  sentinel inside a stub push, and assert overlap from the writes. Observed by AC56.
- **S67** — id 107, M57, landing on unit 19. All rows for a job at a SHA must read `success` for
  GREEN, each other conclusion has a state, in-progress is `NONE`, and S3 reads each line and `&&`
  part of `run`. Observed by AC57.
- **S68** — id 108, M58, landing on unit 24. `help/managed-guards.md` states what a managed hook
  runs from a repository, with the probe's reading at the pinned harness version. Observed by AC58.
- **S69** — id 19, L1, landing on units 9 and 21. Both figures read as derived at the pass, no typed
  total. Observed by AC59.
- **S70** — id 23, L2, landing on unit 15. One line,
  `release — <E> · stale · compare-and-swap refused`, is the one AC5 reads, and S10's rollback
  prints the same. Observed by AC60.
- **S71** — id 25, L3, landing on unit 26. `tools/run-gates/remote_verdict.py` is in this unit's
  write set for S41. Observed by AC31.
- **S72** — id 32, L4, landing on unit 10. `tools/push-main.sh:805` and `:810` both name the version
  check. Observed by AC18.
- **S73** — id 43, L5, landing on unit 17. The printed recipe holds `--record-as <unit-id>`.
  Observed by AC61.
- **S74** — id 44, L6, landing on unit 12. The outcome directory is never pruned, and unit 12's
  Migration sentence is read so: it grows by one small file per attempt. NOT OBSERVED: a stated
  non-behaviour, and `help/loop.md` says it.
- **S75** — id 56, L7, landing on unit 10. AC11's ledger line reads `prints nothing`. Observed by
  AC18.
- **S76** — id 64, L8, landing on unit 31. `PROTOCOL.template.md`:504 is rewritten byte-neutral or
  shorter. Observed by AC62.
- **S77** — id 109, L9, landing on unit 28. A ruling records a value hash, a changed hash proposes
  the key again, `DIRECTIVES_EXTRA_TABLE` is an input, and the count reads seven. Observed by AC63.

## 3. Non-goals (OUT)

- A finding of a higher grade: units 49 to 77.
- Rewriting a spec's text: M4 forbids the fold, and §4 says where a correction lives.
- The audit's left-shift items: a gate is its own unit (BUILD-METHOD M2), and no clause of this
  build names one.

### Edges

- **consumes-from** `DEPL-dShippedRelease-1` — the record writer, AC5 and AC9 (review ids 5, 15, 39, 40, 62, 63, 80, 81, 106)
- **consumes-from** `DEPL-dShippedRelease-2` — its §7 list (review ids 5, 40)
- **consumes-from** `DEPL-dShippedRelease-3` — S2, S4, S5, S7 and its descriptor (review ids 12, 66, 68, 69, 102)
- **consumes-from** `DEPL-dShippedRelease-4` — `deploy.current` and `run_deploy_close` (review ids 5, 22, 34, 40, 79, 105)
- **consumes-from** `DEPL-dShippedRelease-5` — the close's outcome and its descriptor row (review ids 22, 66)
- **consumes-from** `DEPL-dShippedRelease-6` — S5, S7 and its write set (review ids 24, 62, 63, 96)
- **consumes-from** `DEPL-dShippedRelease-7` — the inline block, the helper's spelling, currency's bound and its rows (review ids 8, 12, 16, 36, 50, 53, 62, 63, 69, 103)
- **consumes-from** `DEPL-dShippedRelease-8` — its policy adapter and leg rows (review ids 53, 62, 63)
- **consumes-from** `DEPL-dShippedRelease-9` — parity's line ending and its figure (review ids 19, 37, 59)
- **consumes-from** `DEPL-dShippedRelease-10` — the Readers, the wiring runner and the schema (review ids 5, 11, 20, 31, 32, 33, 40, 47, 54, 56, 59, 60, 61, 62, 67)
- **consumes-from** `DEPL-dShippedRelease-12` — the turn, the classes and the race fixtures (review ids 21, 35, 44, 49, 79, 80, 106)
- **consumes-from** `DEPL-dShippedRelease-13` — the ceiling's clock, the key's read and shell spawns (review ids 41, 42, 49)
- **consumes-from** `DEPL-dShippedRelease-14` — the re-walk (review ids 83)
- **consumes-from** `DEPL-dShippedRelease-15` — S1, S4, S8, AC5 and its row (review ids 12, 20, 23, 53, 55, 59, 62, 63, 95, 96)
- **consumes-from** `DEPL-dShippedRelease-16` — the offer's helper, disposition, probe and census (review ids 11, 22, 36, 87, 88, 89, 90, 97, 103)
- **consumes-from** `DEPL-dShippedRelease-17` — `attend`, the recipe and its hooks (review ids 11, 17, 18, 43, 98)
- **consumes-from** `DEPL-dShippedRelease-19` — the job reader and its leg (review ids 13, 51, 62, 63, 107)
- **consumes-from** `DEPL-dShippedRelease-21` — arm 6c, the factory flag and the figures (review ids 9, 19, 20, 33, 59, 67)
- **consumes-from** `DEPL-dShippedRelease-22` — the cadence row and its adapter (review ids 13, 53, 55, 66)
- **consumes-from** `DEPL-dShippedRelease-24` — the managed target's pricing and its descriptor (review ids 66, 108)
- **consumes-from** `DEPL-dShippedRelease-25` — the empty tag list (review ids 93)
- **consumes-from** `DEPL-dShippedRelease-26` — the reader's parameter set, its shell and `bar` (review ids 13, 25, 48, 51, 52, 53, 54, 62, 63, 66, 99)
- **consumes-from** `DEPL-dShippedRelease-27` — `carries`' caller and the squash read (review ids 12, 14, 26, 66)
- **consumes-from** `DEPL-dShippedRelease-28` — the input count and the ruling's key (review ids 17, 109)
- **consumes-from** `DEPL-dShippedRelease-29` — the offered report (review ids 97)
- **consumes-from** `DEPL-dShippedRelease-31` — AC6, `register`, the kinds and the protocol line (review ids 10, 38, 64, 69, 100, 101)
- **consumes-from** `DEPL-dShippedRelease-52` — `derive_landing_prior_tip`, read for review id 35 (review ids 35)
- **consumes-from** `DEPL-dShippedRelease-59` — the admission rule, read for review id 79 (review ids 79)
- **consumes-from** `DEPL-dShippedRelease-60` — the re-walk rule, read for review id 83 (review ids 83)
- **consumes-from** `DEPL-dShippedRelease-66` — `ended-legs.txt`, read for review ids 5 and 40 (review ids 5, 40)
- **consumes-from** `DEPL-dShippedRelease-70` — `unlanded`, read for review ids 15, 35 and 81 (review ids 15, 35, 81)

## 4. Design

### Why one unit and not two

M4 admits two batches only when the minors split into two disjoint write sets by M6. They do not: `tools/loop/deploy_items.py` is read as a contract by nearly every item, `tools/gate-legs.json` is written by S12, S36 and S37 with its generator, and `memory/HYGIENE.md` and the map move with both halves. The rule never requires the split, and the batch builds after every other unit, so a second unit buys no concurrency.

### Evidence

Each scope item restates its finding's corrected fix, and the report holds each finding's citation and the skeptic's probe. The lines this unit leans on, read at base:

- `tools/govkit/check_runbook_parity.py:60` pins `PROBLEM_PIN = 18`; `tools/run-gates/selftest-budgets.txt:147` holds the `verdict-epoch self-test` row.
- `memory/guides/SESSION-KICKOFF.md:102` and `skills/session-kickoff/manifest-check.sh:48` name the `epoch` verb; `tools/push-main.sh:31`, `:805` and `:810` name the epoch legs.
- `tools/run-gates/regen.py:270` is `run_command`, and `tools/push-main.sh:404` and `.githooks/pre-push:1306` are the two `read_policy_key` copies.
- `tools/push-main.sh:454` writes the per-SHA log, and `tools/policy/catalogue.toml:1102` admits a dot in an environment name.
- `tools/unattended/unattended.sh:13857` refuses a glob in `--writes`.

### Migration

None. Every path is either new in this build or rewritten by a unit of it.

### Rollout

Live at this unit's pass, the last of the build. Spec text that a finding corrected stays as written on its unit, under M4; this spec is the correction, and its unit's ledger line for a superseded criterion points here.

### Files touched (estimate)

- `tools/loop/deploy_items.py`, `tools/loop/deploy_fixture.py`, `tools/loop/kit.toml`, `tools/loop/loop.toml`
- `tools/push-main.sh`, `tools/push-main.test.sh`, `tools/unattended/unattended.sh`, `.claude/settings.json`
- `tools/runtime/waits.py`, `tools/runtime/points.toml`, `tools/runtime/kits_cut.py`, `tools/runtime/kit.toml`, `tools/playbook/kit-schema.toml`, `tools/playbook/kit_factory.py`, `tools/playbook/adopt_declarations.py`, `tools/playbook/render_playbook.py`
- `tools/lib/kit.toml`, `tools/govkit/govkit.py`, `tools/govkit/selftest.py`, `tools/govkit/kit_release.py`, `tools/govkit/offer.py`, `tools/govkit/kit_walk.py`, `tools/govkit/adopter_reading.py`
- `tools/govkit/check_runbook_parity.py`, `tools/govkit/subject-pins.tsv`, `tools/integrations/release.py`, `tools/integrations/release_fixture.py`, `tools/integrations/ci/ci_emit.py`, `tools/integrations/ci_import.py`
- `tools/integrations/kit.toml`, `tools/integrations/tracker_mirror.py`, `tools/integrations/engines/compose_systemd.py`, `tools/run-gates/kit_wiring.py`, `tools/run-gates/platform_matrix.py`, `tools/run-gates/remote_verdict.py`, `tools/run-gates/check_currency.py`, `tools/run-gates/selftest-budgets.txt`
- `tools/gate-legs.json`, rendered by `leg_factory.py --write`
- `tools/memory-tree/HYGIENE.template.md`, rendered to `memory/HYGIENE.md`
- `tools/memory-tree/record-kinds.toml`
- `memory/guides/SESSION-KICKOFF.md`, from its kit source, and `skills/session-kickoff/manifest-check.sh`
- `tools/unattended/PROTOCOL.template.md`, rendered to `memory/guides/UNATTENDED-PROTOCOL.md`
- `memory/map/features/row-grammar.md`, `memory/map/baseline.toml`
- `WIRE-INTO-PROJECT.md`, `help/roles.md`, `help/loop.md`, `help/managed-guards.md`

## 5. Production-readiness checklist

- security — S44, S45, S54 and S62 are the write boundaries of a hostile clone and an operator's
  verb, each with a plant; S68 prices a machine-wide hook.
- perf / scale — S54's timeouts bound a tick; nothing else adds a read a landing feels.
- error / empty / loading states — each item names its refused state, and its criterion plants it.
- observability — each state prints the line its item names.
- risks — a batch this wide meets moved code at its pass, since every unit it lands on is built
  first; each item is re-read against source at the pass.
- testing — the criteria of §6 and the arms of §7.
- migration — none, §4.
- user docs — S28, S68 and S74 name each page.

## 6. Acceptance criteria

- **AC1** — When `python tools/check-spec-tokens.py --list` runs at the close, it prints no `[leg]`
  hit on a dShippedRelease spec and names the six units under `ended-leg join`.
  Red when: a sibling's §7 reads as a dead leg with no successor.
- **AC2** — When `python inline_blocks.py --rows` runs it prints `remote_probe_py`, and `--check`
  with a drifted `check_currency.py` copy exits 1 naming it.
  Red when: a second literal table holds the block.
- **AC3** — When `python tools/govkit/govkit.py selfcheck` runs on the tree it exits 0, and with arm
  6c's exemption cut from a scratch copy it fails naming lib's row.
  Red when: the row reds selfcheck, or any path-less row passes.
- **AC4** — When `git grep -n -i "the fleet\b" -- WIRE-INTO-PROJECT.md` runs, its lines equal the
  kept list of unit 31 §3 and S5's site `:545` is absent; a planted `the fleet` at that site turns
  it red.
  Red when: the check demands a kept node-sense line go, or misses a renamed site.
- **AC5** — When `python kit_factory.py --conform` runs at the close it exits 0 over the descriptors
  holding `[[command]]` and `[[upgrade]]`, and a planted unknown key exits 1 naming it.
  Red when: a declared key reds, or the unknown-key arm stops reading.
- **AC6** — When `python kit_factory.py --conform` and `python check_layers.py` run at the close
  each exits 0, and a planted `resolve_kit_dir` edge with no row exits 1 naming the file.
  Red when: a new edge sits undeclared, or a core kit's probe reaches a non-core home.
- **AC7** — When `python -c` loads `tools/gate-legs.json` by `json.load`, `deploy items` argv holds
  `--selftest` and the three new legs exist.
  Red when: a named arm runs in no leg, so a regression passes the bar.
- **AC8** — When `python deploy_fixture.py --case carries-walk` walks a landing, `read-landing`
  prints a `carries` value that is not `-`.
  Red when: `carries` stays `-` on a real landing.
- **AC9** — When `--deploy record` runs on a planted `held` outcome and on an `unlanded` one, each
  exits 1 naming the class and no ref exists.
  Red when: a non-landing is recorded and pinned by idempotence.
- **AC10** — When `python loop_lib.py --check` runs at this unit's pass it exits 0 with `offered`
  resolved.
  Red when: a route names no item at the close.
- **AC11** — When `python kit_walk.py --fixture --plant install-hooks` runs, both `adopt-census` and
  `adopt-declarations` orders exist and two receipt ids.
  Red when: one order overwrites the other.
- **AC12** — When `python kit_walk.py --fixture --plant attend-recipe-step` runs over the shards
  case, `attend` prints the recipe and ends `attended`; after a hand migration a re-run sets
  `applied`.
  Red when: `attend` reports a failure every run on a shards tree.
- **AC13** — When `python core.py new kit fixture-kit --layer layer.memory --purpose "x"` runs in a
  scratch copy it exits 0; with no `--purpose` it exits 2 naming it.
  Red when: a spelled command cannot exit 0.
- **AC14** — When `python waits.py sweep` runs on a planted dead holder past `leases.expiry-hours`,
  it raises one owner item, and a second sweep raises none.
  Red when: a dead holder stops every landing with no signal.
- **AC15** — When `python deploy_fixture.py --case close-unreleased` answers the hold and walks, the
  T10 transition holds the outcome, on a second node's `--deploy run` too.
  Red when: the transition carries nothing.
- **AC16** — When `python release_fixture.py --case environments` plants `["prod.eu"]`, it exits 2
  naming the dot rule; `check_policy.py` counts each engine value read.
  Red when: a dotted name passes and every read refuses as no key.
- **AC17** — When `bash tools/push-main.sh --land` runs with `commits.squash` set and no loop kit,
  it prints `no loop kit` and lands.
  Red when: the lander calls a missing module.
- **AC18** — When `git grep -n -E 'govkit.py epoch|check-verdict-epoch|the epoch legs'` runs outside
  `memory/builds/`, it prints nothing, and `bash tools/check-dead-paths.sh --list` names no retired
  file.
  Red when: a reader of a retired name stays live.
- **AC19** — When `python tools/govkit/govkit.py version` runs on the tree it exits 0 with
  `KIT_GOVKIT_VERSION` read, and a planted constant in a landable-less entry of another kit exits 1.
  Red when: the exemption reads wider than `installable = false`.
- **AC20** — When `python deploy_fixture.py --case engine-current-stacked` runs with one records
  commit above the merge, `--deploy current` exits 0.
  Red when: a current merge routes to Test.
- **AC21** — When `outcome <sha>` runs on `deploy_fixture.py --case review-range-second-node`, it
  prints T^1.
  Red when: a take-over node names a one-commit range.
- **AC22** — When `python adopter_reading.py --fixture --case helper-spawned` has git call the
  helper against a credentialed stub on this node, the read answers.
  Red when: a backslash path mangles under sh and reads as an access refusal.
- **AC23** — When `python tools/playbook/render_playbook.py --check-render --scope runbook` runs on
  a CRLF copy it exits 0, and `git diff --stat` over bytes outside the pair prints nothing.
  Red when: the render reds every CRLF checkout or flips the file.
- **AC24** — When `python -c` loads `tools/gate-legs.json` and reads the `deploy items` row, its
  argv ends `deploy_fixture.py`, `--all`; with the row cut from a scratch copy it reports none.
  Red when: the criterion cannot match a correct build.
- **AC25** — When `python deploy_fixture.py --case core-ceiling-later-landing` plants a later
  landing's start record, a killed bar still raises one `core-verdict` item.
  Red when: the first SHA loses its clock.
- **AC26** — When `bash tools/push-main.sh --read-policy-key GATE_POST_MERGE` runs over each row of
  a comment, quote, CR and repeated-assignment table, it answers as `read_policy_key` does, and
  `run_deploy_core` calls it.
  Red when: a legal spelling takes the wrong arm.
- **AC27** — When `python kit_wiring.py` runs with a stub `bash` first on PATH, it prints the same
  kit lines, each row's bound named.
  Red when: a row reaches the WSL launcher.
- **AC28** — When `python platform_matrix.py bar` runs with a stub `bash` first on PATH, the launch
  uses the resolved shell.
  Red when: the leg reds for a shell reason.
- **AC29** — When `git grep -c '"bash"' -- '*deploy_items.py'` runs at the close it prints nothing,
  and `inline_blocks.py --check` holds the block there.
  Red when: a bare argv reaches the WSL launcher.
- **AC30** — When `python ci_import.py --fixture --case imported-job` reads a job through
  `read_job_conclusion`, its liveness rules are `read_remote_verdict`'s, seen on a planted row with
  no `head_sha`.
  Red when: an imported leg reads green where the reader refuses.
- **AC31** — When `python platform_matrix.py verify --ci-rows <saved>` reads a `bar-linux` job
  through the real reader on a planted `gov-bar.yml` row, it answers GREEN.
  Red when: the job reads `DEAD PROBE`, and `verify` exits 1 on every release.
- **AC32** — When `git grep -n 'def read_policy' -- tools/run-gates tools/integrations` runs, each
  kit prints one definition, and `python release_fixture.py --case policy-absent` prints its stated
  line.
  Red when: one kit answers a missing policy kit two ways.
- **AC33** — When `python kit_factory.py --floor` runs it prints the bytes of `python-floor.txt`,
  and `ci_emit.py render` writes that value.
  Red when: a second floor reader ships.
- **AC34** — When `python cadence.py --fixture --case no-integrations` runs the two rows on a tree
  with no integrations kit, each prints `not installed` and exits 0.
  Red when: a tick takes a lease and runs a missing file daily.
- **AC35** — When `python tools/govkit/check_runbook_parity.py` runs at the close it exits 0 with a
  value derived at the pass.
  Red when: the pin reds from the first unit to the last.
- **AC36** — When `python tools/codebase-map/test_codebase_map.py` runs on a planted scratch leg
  with no claim, it names it `UNCLAIMED`, and at the close it passes.
  Red when: a leg sits unclaimed or a stale claim stands.
- **AC37** — When `python tools/govkit/govkit.py selfcheck` runs at the close it exits 0, and a
  planted leg with no pin row fails.
  Red when: a new leg has no subject on record.
- **AC38** — When `grep -c 'tools/\*/kit.toml' <this unit's ledger>` runs it prints 0, and the
  ledger lists each path.
  Red when: a glob reaches `--dispatch --writes`.
- **AC39** — When `python -c` reads `.claude/settings.json`, its `SessionStart` hooks name
  `session-tick.sh`.
  Red when: gov's cadence reads `not ready` and no tag is cut.
- **AC40** — When `python record_kinds.py --check` runs at the close it exits 0, and the
  `gen:record-kinds` region of `memory/HYGIENE.md` holds each new kind.
  Red when: a kind's row sits outside the rendered region.
- **AC41** — When `python deploy_items.py admit --slug fy` runs for a direct `--land --slug` with no
  entry, it enqueues.
  Red when: an unqueued landing passes the queue.
- **AC42** — When a planted lander lands and `--land` re-runs in
  `deploy_fixture.py --case outcome-sticky`, `outcome <sha>` still prints `landed-gated` and the
  first prior tip.
  Red when: a retry destroys the gated evidence.
- **AC43** — When `python deploy_fixture.py --case review-rewalk-pending` runs `--deploy review`
  twice, the stub logs one `--trigger`.
  Red when: a re-walk re-fires the review.
- **AC44** — When `python offer.py --fixture --plant symlink-outbox` runs, nothing lands outside the
  scratch and the disposition reads `undeliverable`.
  Red when: the order's write leaves the clone.
- **AC45** — When `python offer.py --fixture --plant probe-dead-remote` and
  `--plant probe-failed-delete` run, each reads `undeliverable`, the second naming the ref.
  Red when: a dead remote reads as a scoped grant.
- **AC46** — When `python offer.py --fixture --plant offer-retry` re-runs after a killed run, it
  prints `already offered`, and `--plant update-exit-2` reads `undeliverable`.
  Red when: a retry reads non-fast-forward, or an exit has no row.
- **AC47** — When `python offer.py --fixture --plant census` runs on a build following §4 of unit
  16, it exits 0; a call site with no guard exits 1 naming it.
  Red when: a dead read passes the arm, or a correct build reds.
- **AC48** — When `python receipt_schema_5.py --fixture --case tagless-clone` plants tags on the
  remote and none in the clone, `apply` at an untagged commit exits 2 naming the fetch.
  Red when: a CI checkout defeats `install.from`.
- **AC49** — When `python release_fixture.py --case out-of-band-move` plants an operator's move, the
  next tick does not print `skip · held elsewhere` for a day; a planted exit 255 reads unreachable.
  Red when: E's lease sits held with no item.
- **AC50** — When `python offer.py --fixture --plant lost-orphaned` offers over a planted lost
  change, the order names it.
  Red when: a lost change is reported nowhere.
- **AC51** — When `python platform_matrix.py bar` runs on a stub `uname` and the default set under
  `platforms.verify = bar`, it exits 0 with this host's record written.
  Red when: the value can never pass on its default set.
- **AC52** — When `python tools/govkit/govkit.py register` runs with `--key a..b`, a `-x` branch, a
  `-x` remote, a newline name, and a changed remote, each exits 2 naming the value.
  Red when: a value breaks a ref, an argv or the row.
- **AC53** — When `python kits_cut.py --fixture --case span-refused` and
  `--case tag-refused-no-residue` run, the first refuses and the second leaves no local tag.
  Red when: a corrupt landing leaves the notes, or an unpushed tag reads as a witness.
- **AC54** — When `python check_currency.py --fixture --case stale-record` and `--case hung-remote`
  run, the first reds naming the age and the second reads `unverified` inside its timeout.
  Red when: an old `within` stays green, or a hung remote holds the tick.
- **AC55** — When `python deploy_fixture.py --case engine-current-verdicts` plants `DEAD PROBE`,
  `HELD` and `NONE`, each exits 2 and writes no `comparison` record.
  Red when: a network fault costs a re-test.
- **AC56** — When `python deploy_items.py --fixture --plant two-nodes-one-turn` runs, the first
  process sits on the sentinel inside the stub push before the second starts, and the overlap reads
  from the writes.
  Red when: the criterion passes with no race.
- **AC57** — When `python ci_import.py --fixture --case conclusions` plants a matrix with one
  failure, `skipped`, `cancelled`, `neutral`, `timed_out` and in-progress, none reads GREEN, and
  `cd app && pytest` passes the test-job read.
  Red when: a failing matrix reads green.
- **AC58** — When `grep -n CLAUDE_PROJECT_DIR managed-guards.md` runs it prints the operator's rule,
  and §5 of this unit states the probe's reading.
  Red when: a machine policy runs a repository's own file unpriced.
- **AC59** — When `python kit_factory.py --conform` runs at the close it prints the entry count, and
  units 9's and 21's ledger lines cite that printed count.
  Red when: a typed total stands beside the derived one.
- **AC60** — When `python release_fixture.py --case stale-rollback` runs, it prints
  `stale · compare-and-swap refused` for promote and rollback alike.
  Red when: two spellings of one line.
- **AC61** — When `python kit_walk.py --fixture --plant recipe-prints` runs the printed recipe, it
  exits 0.
  Red when: the owner's first command fails.
- **AC62** — When `bash tools/check-template-size.sh memory/guides/UNATTENDED-PROTOCOL.md` runs
  after the render it exits 0.
  Red when: the guide crosses its limit by one byte.
- **AC63** — When `python adopt_declarations.py --fixture --case value-changed` changes a ruled
  value it proposes the key once, and `--case same-value` proposes none.
  Red when: a changed house default stays silent for ever.

## 7. Gates

`codebase-map coverage + freshness` · `govkit selfcheck` · `kit/dogfood doc parity` · `govkit runbook parity` · `every held leg is budgeted, every budget row resolves` · `dead-path carriers (deleted files still named)` · `unattended protocol size` · `unattended kit gate` · `check-wiring self-test` · `push-main self-test` · `policy fixtures` · `policy check` · `govkit selftest` · `manifest-check self-test` · `scratch-guard self-test` · `recall floor` · `recall floor arms` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `lexicon naming predicates` · `govkit refusal join` · `govkit acceptance matrix` · `playbook render selftest` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/loop/deploy_fixture.py · covers AC8 AC9 AC15 AC20 AC21 AC25 AC41 AC42 AC43 AC55 · one planted case per criterion, its failing case each item's change cut out in turn · none

New arm: tools/push-main.test.sh · covers AC17 AC26 AC56 · a stubbed loop kit and the truth table of S36, its failing case a differing reader · none

New arm: tools/govkit/offer.py · covers AC44 AC45 AC46 AC47 AC50 · one plant per criterion, its failing case `symlink-outbox` writing outside the scratch · none

New arm: tools/integrations/release_fixture.py · covers AC16 AC49 AC60 · the planted cases, their failing case a dotted name passing · none

## 8. Open questions

- **F1 — One batch or two (§4)?** Options: (a) one unit; (b) two, by M6. (b) has no disjoint split,
  since both halves read `tools/loop/deploy_items.py` as a contract. RESOLVED (agent, 2026-10-30,
  delegated): (a), rung 3. widens: none · relaxes: none
- **F2 — What keeps govkit's version check, S29?** Options: (a) govkit declares `none` and leaves
  the population; (b) unit 10's rule exempts `installable = false` by name. (a) drops
  DEPL-dGaugedVintage-1's check unannounced. RESOLVED (agent, 2026-10-30, delegated): (b), rung 3.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-30 · initial draft, promoted from review the 77 minors, one scope item per raw id of the round-1 spec audit.

## 10. Reuse audit

The seams extended are named per item by the report's corrected fixes, each a seam of the unit it
lands on.
`python tools/codebase-map/reuse_lookup.py "walk ordered items stopping on the first non-zero exit and resuming by re-running"`
and the ten other probes of units 49 to 77 ranked name-stem helpers and no second home for any item,
so no item mints a seam of its own, and S42 and S43 remove a duplicate rather than add one. The
recall probe surfaced the report's items, which this spec follows.

Recall terms used:
`python tools/memory-recall/query.py "how does the deploy walk resume after a held item and which items hold the lease" --terms "deploy walk idempotent held exit run_deploy_items landing record tombstone lease unlease close"`
