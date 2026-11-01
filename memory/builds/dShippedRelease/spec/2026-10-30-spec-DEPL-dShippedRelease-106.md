# DEPL-dShippedRelease-106 — The round-2 spec audit's 79 minors, batched: the rules units 49 to 78 left unstated, their failure states, and the records that named the wrong seam

**Status:** OPEN · rev-3 · 2026-11-01 · node d · Tier-2 · base f4597719 · streams deployer · order 33 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-119 DEPL-dShippedRelease-120 DEPL-dShippedRelease-121 DEPL-dShippedRelease-122 DEPL-dShippedRelease-123 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125 DEPL-dShippedRelease-126 DEPL-dShippedRelease-127 DEPL-dShippedRelease-128 DEPL-dShippedRelease-129 DEPL-dShippedRelease-130 DEPL-dShippedRelease-131 DEPL-dShippedRelease-132 DEPL-dShippedRelease-133 DEPL-dShippedRelease-134 DEPL-dShippedRelease-135 DEPL-dShippedRelease-136 DEPL-dShippedRelease-137 DEPL-dShippedRelease-138 |
| [2026-11-01-build-DEPL-dShippedRelease-133-token-fix-return.md](../build/2026-11-01-build-DEPL-dShippedRelease-133-token-fix-return.md) | research | DEPL-dShippedRelease-133 DEPL-dShippedRelease-128 DEPL-dShippedRelease-126 DEPL-dShippedRelease-127 DEPL-dShippedRelease-138 |
| [2026-11-01-build-DEPL-dShippedRelease-79-round2-disposal-return.md](../build/2026-11-01-build-DEPL-dShippedRelease-79-round2-disposal-return.md) | research | DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 |
| [2026-11-01-review-DEPL-dShippedRelease-79-spec-audit-round1.md](../reviews/2026-11-01-review-DEPL-dShippedRelease-79-spec-audit-round1.md) | spec-audit | DEPL-dShippedRelease-100 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-93 DEPL-dShippedRelease-103 DEPL-dShippedRelease-92 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-90 DEPL-dShippedRelease-86 DEPL-dShippedRelease-91 DEPL-dShippedRelease-105 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-104 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 |

<!-- /gen:spec-records -->

## 1. Goal

The round-2 spec audit, `reviews/2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md`, confirmed 106 findings, and DEPL-dShippedRelease-79 to -105 take its
8 blockers and 19 highs. This unit is BUILD-METHOD M4's batch of its 60 MEDIUM and 19 LOW by raw id, one
scope item per id, in report order, M1 to M41 and then L1 to L16. They land on 38 units, so it repairs
no unit in particular and builds last, order 33, above every unit in this build.

Every id: M1 9, 71; M2 10, 31, 55, 90; M3 11; M4 12, 34, 101; M5 13, 68; M6 14, 102; M7 15; M8 16, 39, 56, 73; M9 17, 113; M10 18, 74; M11 19, 40; M12 20; M13 21, 38; M14 23, 92; M15 32; M16 99; M17 37, 76; M18 41; M19 50; M20 53; M21 54; M22 57; M23 59, 110; M24 75; M25 77; M26 78; M27 79; M28 80, 106; M29 82; M30 97; M31 98; M32 100; M33 103; M34 104; M35 105; M36 107; M37 108; M38 109; M39 111; M40 112; M41 114; L1 25; L2 26, 81, 85; L3 27; L4 42; L5 43; L6 44; L7 45; L8 46, 84; L9 51; L10 58; L11 60; L12 61; L13 62; L14 63; L15 64; L16 65.

## 2. Scope (IN)

- **S1** — id 9, M1, landing on unit 66. `ended-legs.txt`'s row population (unit 66 S1) and its stale test (S4) read every non-terminal spec, DEFERRED included, and the hit arm stays on LIVE, so a carried spec naming an ended leg gets its row. Observed by AC1.
- **S2** — id 71, M1, landing on unit 66. A DEFERRED spec of `lexicon wiring`'s population, flipped to OPEN after its row exists, prints no `[leg]` hit: the reopening build owes no edit to clear a red the retirement caused. Observed by AC1.
- **S3** — id 10, M2, landing on units 65 and 10. Unit 10 stays first, since unit 65 consumes `derive_version_findings`. Unit 65 S1 is a spec-time disposition, closed against S4's frozen read, and it is no pass criterion. Observed by AC2.
- **S4** — id 31, M2, landing on unit 65. Unit 65 AC1 reads `git show f4597719:tools/check-kit-versions.sh`, the pinned base, so the count is taken on a blob that exists whatever order the file left the tree. Observed by AC2.
- **S5** — id 55, M2, landing on unit 65. The observed criterion is one plant per row of unit 65's table, the arm 5c rows included, each reding `govkit.py version`, plus plants for `KIT_MANIFEST_VERSION`'s same-line marker (`:191`) and a population of zero (`:214`, `:271`). Observed by AC3.
- **S6** — id 90, M2, landing on unit 65. Unit 65 S1's "stops the pass" and §5's mitigation read void, since the file is gone at the pass; the table is the disposition, and AC3's plants are what can fail. Observed by AC2.
- **S7** — id 11, M3, landing on units 66 and 10. Unit 66 follows unit 10 by design: S4 needs the legs gone, no gate runs in a pass, and `spec tokens` first runs at the close with both in. NOT OBSERVED: a statement of order, and the report judges it low.
- **S8** — id 12, M4, landing on unit 61. The census of DEPL-dShippedRelease-102 widens to the verbs `adopt` and `update` beside `apply`, the two unit 62 and DEPL-dShippedRelease-104 also refuse on, and a file outside `*.py` and `*.sh` is out by that stated rule. Observed by AC4.
- **S9** — id 34, M4, landing on unit 61. The census's output is pinned per file, §4 "The census at base", and the assertion is per file, so a cut assignment reds by name. Observed by AC4.
- **S10** — id 101, M4, landing on unit 61. A spawn through a helper counts: `run(`, `run_in_gov(`, `run_govkit(`, `gov(` and the rest of §4's list, while `.get(` and `run_git(` are `CENSUS_NOT_A_SPAWN`, so `tools/check-kit-placeholders.py`'s and `tools/branch-reconcile/selftest.py`'s false hits stay out. Observed by AC4.
- **S11** — id 13, M5, landing on units 72 and 12. `admission-error` is a class of unit 12's table, exit 1: admission's exit 2 and every unknown exit stop there, and `deploy.land`'s route holds and raises one `landing-admission` owner item, with no `transition` and no Test. Observed by AC5.
- **S12** — id 68, M5, landing on units 71 and 72. Unit 71 S2's exit row keys on a gate refusal alone, so an admission failure keeps the entry and its place. `held` is not reused, since it reads the failure as exit 5 `awaiting`, which unit 72 AC2 names as red. Observed by AC5.
- **S13** — id 14, M6, landing on units 52, 70 and 1. With no first-parent merge, `read_landing_outcome` keeps the class and prints `landing_prior_tip` as `-` with `prior-underived`, exit 0, and `read_landing_pin` refuses over that value. `derive_landing_prior_tip` exits 3 for no merge, and exit 2 stays the fetch's. Observed by AC6.
- **S14** — id 102, M6, landing on units 52 and 27. `derive_landing_carries` and `derive_outside_commits` read `-` as no range and write `carries` as `- · prior underived` with no git call, so `deploy.carries` never runs `-..<sha>`. Observed by AC6.
- **S15** — id 15, M7, landing on unit 78. `deploy items selftest` is a separate leg by `leg_factory.py new`, running `deploy_items.py --selftest`. Unit 78 AC7 reads that row's argv, and AC24 stands. Observed by AC7.
- **S16** — id 16, M8, landing on unit 78. Unit 78 AC18's grep is scoped to `tools skills .githooks WIRE-INTO-PROJECT.md help memory/guides memory/map/features memory/project .memory-tree.conf`. Observed by AC8.
- **S17** — id 39, M8, landing on unit 78. `memory/archive`, `memory/gotchas`, `memory/backlog` and `memory/map/generated` are excluded by name as history or renders. Observed by AC8.
- **S18** — id 56, M8, landing on units 78 and 10. The `memory/project/*` registers drain when the scripts go: `spawn-idiom-sites.txt`, `substitution-fed-loops.txt`, `testsuite-count-waivers.txt` and `unarmed-branches.txt` each lose their `check-verdict-epoch` rows. Observed by AC8.
- **S19** — id 73, M8, landing on unit 78. The pattern gains `epoch legs` and `kit version markers`, §4 "The residue AC8 keeps" lists what stays, and the grep is shown red at base. Observed by AC8.
- **S20** — id 17, M9, landing on unit 78. Unit 78 AC29 grades the spawn shape: no `["bash",` argv opener and no `subprocess` call whose first element is that literal, outside the marked block. Observed by AC9.
- **S21** — id 113, M9, landing on unit 78. AC29's `git grep -c '"bash"'` half reads void, because `tools/lib/resolve_bash.py:21-22` holds that literal inside the block AC29 requires. AC18's half is S16 to S19's. Observed by AC9.
- **S22** — id 18, M10, landing on unit 78. Unit 78 AC1 reads what holds at the close: `--list` prints no `[leg]` hit on any live spec, and each ended leg a live spec names holds a row. Observed by AC10.
- **S23** — id 74, M10, landing on unit 78. The held-by-name half reads on a live spec of another build, since units 1, 2, 4, 13, 14 and 15 are CLOSED by unit 78's pass and LIVE excludes CLOSED (`tools/check-spec-tokens.py:331`). Observed by AC10.
- **S24** — id 19, M11, landing on units 78 and 31. Unit 78 AC4 greps `\bfleet\b` over the six paths of unit 31 S5, so `tools/govkit/selftest.py:5510` and `tools/codebase-map/map_lib.py:62` are read and "the whole fleet" matches. Observed by AC11.
- **S25** — id 40, M11, landing on units 78 and 31. The kept lines are pinned here by their text, §4 "The kept fleet lines", and that list is AC4's comparand. Observed by AC11.
- **S26** — id 20, M12, landing on units 73 and 14. Unit 73 gains its S4: `pending` keeps `held · check_landing_review · pending`, `forged` replaces `unreadable field`, and unit 14 AC2's disposed plant is a planted report. Observed by AC12.
- **S27** — id 21, M13, landing on units 77 and 6. `read-current` reads per host kind: the override or env file wins when it exists, and `none` applies only when no such file exists. Systemd's read takes the `Environment` line whatever the `ActiveState`, superseding that clause of unit 6 S3, and S4 tests `ActiveState` apart. Observed by AC13.
- **S28** — id 38, M13, landing on units 77 and 6. Under `host-kind = compose`, after a failed `up -d`, `read-current` prints the digest in `<state-dir>/<E>.env`, and `--expect` compares that. Unit 77 §4's "a failed unit prints none" reads corrected. Observed by AC13.
- **S29** — id 23, M14, landing on units 59 and 68. The records test grades the tree: `git diff --no-renames --name-only <advertised tip> HEAD`, wholly under `memory/builds/<slug>/`, beside DEPL-dShippedRelease-92's commit test, so a rename reads at both ends. Observed by AC14.
- **S30** — id 92, M14, landing on units 59 and 68. A hand-made merge carrying content over `tools/` beside a clean records commit fails the same tree read, which `rev-list --no-merges` alone never saw. Observed by AC14.
- **S31** — id 32, M15, landing on unit 50. A CLOSED row does not end the exemption when the landing's `git diff --no-renames --name-only <advertised tip> HEAD` holds nothing outside `memory/`, `tools/gate-legs.json` and `tools/run-gates/ceiling-evidence.txt`, the ceiling raises dWellOiledMachine and dRankedPlan landed. Exit 3 stands for a CLOSED unit that wrote product. Observed by AC15.
- **S32** — id 99, M16, landing on unit 50. The one rule states its empty set: at least one row, every row DEFERRED, WONTDO or a CLOSED row by S31, and at least one DEFERRED. An empty region is no spec run. Observed by AC15.
- **S33** — id 37, M17, landing on units 77, 6 and 15. The value is `release.engine.compose-systemd.<environment>.service`, read by `read_engine_values`, and no `release.env.` row holds an engine-private value. Unit 6 AC7's count reads eight. Observed by AC16.
- **S34** — id 76, M17, landing on units 77, 6 and 15. §8 F3 gives the eighth row its grant, since unit 6 F3's covers seven and unit 15's three. Observed by AC16.
- **S35** — id 41, M18, landing on units 50 and 49. `**Build status:** WONTDO` reads `withdrawn`, the one tree fact the row names, and its other three words fall out, since `derive_status` outputs none of them. Observed by AC17.
- **S36** — id 50, M19, landing on units 50 and 69. `test_spec_run_landing` calls `unattended.sh --spec-run <slug>`, a verb over `check_spec_run` (`tools/unattended/unattended.sh:5152`), and keeps its region read as a guard on top. Unit 69's region read is carry-forward and stays apart, §4 says why, and an edge joins the two units. Observed by AC15.
- **S37** — id 53, M20, landing on unit 71. `check_landing_admitted` reads the head's disposed `landing-turn` item, and on `leave-queue` calls `write_queue_exit(slug, tree, "owner")`, the actor unit 71 S4 left unnamed, as unit 12 S3 reads `land-next`. Observed by AC18.
- **S38** — id 54, M21, landing on unit 58. Unit 58 AC3 reads S4's output: `check-wired` prints `<n> item(s) · <m> adapter row(s)`, `n` from `read_items(step="step.deploy")`, and `--check-adapters` asserts exit 0 alone. Observed by AC19.
- **S39** — id 57, M22, landing on unit 54. `run-gates adopter e2e` gains the guard `{prefix}/integrations/`, so an edit to `ci_emit.py` or `action-pins.toml` selects the leg that asserts over them. Observed by AC20.
- **S40** — id 59, M23, landing on units 75 and 27. `write_retrust_order` upserts on `id`, the id covering each path and its new sha256, so new bytes make a new open row, a re-run is a no-op, and an open row of the kind gives way to the new one, its old order file taken out. The offer path shares the rule. Observed by AC21.
- **S41** — id 110, M23, landing on units 75 and 17. `attend` runs nothing from the row, by S57's shape, and a row carrying an `argv` is refused printing it, so a tracked receipt cannot name a command for `attend`. Observed by AC21.
- **S42** — id 75, M24, landing on units 51, 14 and 78. `tools/workflows/kit.toml` gains a `resolves` row for `loop`, and `--landing` with no loop kit prints `landing pin — no loop kit`, exit 2. Unit 78 S11's sweep covers units 14 and 51. Observed by AC22.
- **S43** — id 77, M25, landing on unit 62. `adopt` runs the check by DEPL-dShippedRelease-104, and §8 F2 rules it no exemption: a passing `adopt` records the `install_from` that check read. Observed by AC23.
- **S44** — id 78, M26, landing on units 58 and 4. The landing instruction moves everywhere it is written: `tools/unattended/SKILL.template.md:164`, `tools/unattended/PROTOCOL.template.md:432` and `memory/guides/UNATTENDED-VERBS.md:924`'s sentence read `--deploy land <slug>`, the protocol line byte-neutral or shorter. Observed by AC24.
- **S45** — id 79, M27, landing on units 58 and 78. `check-wired` runs on the real tree inside `deploy items selftest`, its failing case an adapter row cut from a scratch copy, so a later `step.deploy` item with neither a verb nor an adapter reds the bar. Observed by AC7.
- **S46** — id 80, M28, landing on unit 68. `run_late_records_landing` opens with a forced `git worktree` removal and `git worktree prune` on its path, creates its branch with `-B`, and a trap clears both on every exit. Observed by AC25.
- **S47** — id 106, M28, landing on unit 68. The branch `records/<slug>` is taken away at the end, a re-run after exit 5 meets no leftover, and unit 68 §5's VERBS edit joins this unit's §4 with `recall floor` and `recall floor arms` on §7's line. Observed by AC25.
- **S48** — id 82, M29, landing on unit 78. This unit's §4 lists the paths unit 78's estimate omits: `tools/govkit/steps/receipt_schema_5.py`, `tools/playbook/core.py`, `tools/runtime/cadence.py`, `tools/runtime/cadence_dispatch.py`, `tools/playbook/README.md` and the dossiers of S46. NOT OBSERVED: an estimate, and the dispatch's `--writes` set reads it.
- **S49** — id 97, M30, landing on units 60 and 14. A `landing-review` `WAIT_KINDS` row takes `flow.wait-ceiling` as its deadline and raises one `landing-review-stalled` owner item, options `re-fire`, an explicit `--deploy review --refire`, and `dispose-with-reason`, which writes a report with `## Verdict: BLOCKED` and the reason as its one confirmed row, then runs `dispose-landing` over it. Observed by AC26.
- **S50** — id 98, M31, landing on units 53 and 1. `set_landing_field` exits 1 only for `absent`, printing that line, 2 for a dead fetch, and 3 for a compare-and-swap lost three times or a record `read_landing` refuses. Unit 53 S3 passes only on the `absent` line, and any other non-zero stops the walk with that exit. Observed by AC27.
- **S51** — id 100, M32, landing on units 49, 50 and 69. `read_build_rows(text)` in `tools/loop/deploy_items.py` is the one reader of `gen:build-units`, indexing Status from the row's right end, shared by units 49, 50 and 69. Observed by AC28.
- **S52** — id 103, M33, landing on unit 70. In `read_landing_outcome`'s no-record branch, after a good fetch, `--is-ancestor` exit 0 is contained and any other exit on a well-formed SHA reads `unlanded`. A value that is no full hex SHA, and a repository `git rev-parse --is-shallow-repository` calls shallow, exit 2 first. Observed by AC29.
- **S53** — id 104, M34, landing on unit 51. `--landing` refuses, exit 2 naming the class and firing no review, on a non-zero `outcome`, a `base` that resolves to no commit, or a `base` equal to `<sha>`. Observed by AC22.
- **S54** — id 105, M35, landing on units 56 and 13. `WALK_RECORD_ON_HOLD`'s pass exits the record item's non-zero exit when it fails, and 3 otherwise. A persistent exit 2 of `deploy.core`, as under `policy-file.on-missing-expansion = refuse`, also runs the record, with `core: pending`. Observed by AC30.
- **S55** — id 107, M36, landing on units 59 and 68. `RECORDS_RENDERS`, holding `memory/LIVE.md`, joins S29's tree read and DEPL-dShippedRelease-92's commit test, so a records commit that moves the build's `Last record` cell stays records-only under `.githooks/pre-commit:226-229`. Observed by AC14.
- **S56** — id 108, M37, landing on units 71, 59 and 12. The exit row is written from the lander's `refused` path through `queue-exit`, beside `write_landing_outcome`, so a refused direct `--land --slug` leaves the queue as `run_deploy_land` does. Observed by AC5.
- **S57** — id 109, M38, landing on units 75 and 27. At the pinned `codex-cli 0.139.0` no non-interactive re-trust verb exists, so the `codex-retrust` row is a recipe: it holds `recipe` and no `argv`, and `attend` prints it and stops `attended`, the shape unit 78 S19 gives a recipe step. Observed by AC21.
- **S58** — id 111, M39, landing on unit 77. `none` needs a positive empty answer from a responding daemon: `docker compose ps` with zero rows, or `systemctl show` with no `GOV_IMAGE`. Any other failure is exit 4, replicas with differing digests exit 2 naming the service, and S27's file read precedes the empty-`ps` test. Observed by AC13.
- **S59** — id 112, M40, landing on units 78 and 13. The `running` ceiling counts from a stamp keyed by SHA, `<common-dir>/gate-post-merge-<sha8>.started`, written once at the start beside the log, and an absent stamp raises the item, since `gate-post-merge.start` is one overwritten file and the log's mtime moves while the bar writes. Observed by AC31.
- **S60** — id 114, M41, landing on unit 78. Unit 78 S42's rule: `read_policy_value` in run-gates and integrations answers, with no policy kit, the adapter's own `POLICY_DEFAULTS` value, printing `policy — no policy kit · <key> default <value>` once per process, and a key outside that table raises naming it. S64's bound is the catalogue key `currency.max-age-days`, default 14. Observed by AC32.
- **S61** — id 25, L1, landing on unit 57. `baseline-red` is an inverted case: the arm passes when the inner check reports `baseline`, it runs in the default set, and its line is exempt from unit 57 AC3 by name. Observed by AC33.
- **S62** — id 26, L2, landing on units 75, 62 and 63. This unit's §4 holds `tools/govkit/kit_walk.py` and `help/offers.md` (unit 75), `help/upgrade-steps.md`, `tools/govkit/steps/receipt_schema_5.py` and `tools/govkit/selftest.py` (units 62, 63). NOT OBSERVED: an estimate.
- **S63** — id 81, L2, landing on units 69 and 68. This unit's §4 holds `tools/unattended/STOPS.template.md`, its render, and `tools/unattended/VERBS.template.md`, and its §7 owes `recall floor` and `recall floor arms`. NOT OBSERVED: an estimate.
- **S64** — id 85, L2, landing on unit 75. Unit 75 AC3 gains its `New arm:` line, §7 here, its failing case the recipe printed with no stop. Observed by AC21.
- **S65** — id 27, L3, landing on units 59, 68 and 69. `records-landing --slug` joins `deploy_items.py`'s verbs for the lander, beside DEPL-dShippedRelease-94's `late-records`, and `carry-forward --slug` for `run_unlease`. Unit 53's `derive_core_fields` is a Python call and needs none. Observed by AC34.
- **S66** — id 42, L4, landing on unit 62. Unit 62 AC2 is spelled `update --to <untagged> --write`, asserting exit 2 and `git status --porcelain` and the receipt's bytes unchanged. DEPL-dShippedRelease-104 AC2 states the preview. Observed by AC23.
- **S67** — id 43, L5, landing on units 49 and 50. Status is read by S51's reader on units 49 and 50 too, and the plant's title holds a `|`. Observed by AC28.
- **S68** — id 44, L6, landing on unit 66. Unit 66 AC1's cost reads 465.2s on node a, `tools/run-gates/ceiling-evidence.txt:133`, under a 940-second ceiling. NOT OBSERVED: a corrected figure, recorded in §4.
- **S69** — id 45, L7, landing on unit 78. Unit 78 AC58's second half points at `help/managed-guards.md`, the page S68 writes the probe's reading to. NOT OBSERVED: a pointer between two records.
- **S70** — id 46, L8, landing on unit 71. `help/loop.md` states the exit row and the held pass-over, and unit 71 §5's user-docs line reads so. Observed by AC35.
- **S71** — id 84, L8, landing on unit 71. `help/loop.md` states `leave-queue` and what an owner's answer does. Observed by AC35.
- **S72** — id 51, L9, landing on units 49 and 50. §8 F4 weighs `derive_landed_owners` (`tools/policy/check_policy.py:442`) against the generated line and keeps the line. `parent-wontdo` asserts where the two differ. Unit 49 §10's "no function reading a build's state" and unit 50's copy read corrected. Observed by AC17.
- **S73** — id 58, L10, landing on units 72, 68, 53, 58, 59 and 69. `push-main self-test` and `unattended kit gate` join this unit's §7 for the arms units 72, 68, 53, 58, 59 and 69 place in them. NOT OBSERVED: a record of what the bar already runs.
- **S74** — id 60, L11, landing on units 53, 59, 60, 68, 69 and 73. §4 "The corrected reuse audits" names the seam each of units 53, 59, 60, 68, 69 and 73 extends, with a phrase of its own. NOT OBSERVED: a correction of an audit record.
- **S75** — id 61, L12, landing on units 51 and 74. The same table: unit 51 names `read_landing_pin` and `read_landing_outcome`, and unit 74 names `classify_outcome` at `tools/govkit/govkit.py:6557`. NOT OBSERVED: a correction of an audit record.
- **S76** — id 62, L13, landing on units 66, 61 and 62. The same table: units 66, 61 and 62 each cite a phrase of their own behaviour, with what it ranked. NOT OBSERVED: a correction of an audit record.
- **S77** — id 63, L14, landing on units 63 and 64. Units 63's and 64's "no redactor in the tree" reads corrected: `derive_redacted` (`tools/run-gates/measure_legs.py:531`) and `redact` (`tools/run-gates/run-gates.sh:307`) mask `user:pass@` in leg logs, and a bare token passes them. They stay out of scope, because a receipt is a committed value and a leg log is node-local output. NOT OBSERVED: a correction of an audit record.
- **S78** — id 64, L15, landing on units 78 and 52. `derive_landing_merge(sha, root)` in `tools/loop/deploy_items.py` returns T. `derive_landing_prior_tip` returns its first parent, and unit 78 S30 calls it for T and compares T^1 with the advertised tip. Observed by AC36.
- **S79** — id 65, L16, landing on unit 78. Unit 78 §4's evidence reads four `read_policy_key()` copies, in `.githooks/pre-push`, `tools/push-main.sh`, `tools/run-gates/post-merge.sh` and `tools/unattended/unattended.sh`, and S36's verb stays: `run_deploy_core` is Python, and the lander's copy owns `GATE_POST_MERGE`. NOT OBSERVED: a corrected reason.

## 3. Non-goals (OUT)

- A finding of a higher grade: units 79 to 105.
- Rewriting an audited spec's text: M4 forbids the fold, and §4 says where each correction lives.
- The audit's left-shift items: a gate is its own unit (BUILD-METHOD M2), and no clause of this build
  names one.

### Edges

- **consumes-from** `DEPL-dShippedRelease-102` — the census of `harness_census.py`, which this unit widens, and each later harness's declaration
- **consumes-from** `DEPL-dShippedRelease-1` — the text and code the batch repairs (review ids 14, 98)
- **consumes-from** `DEPL-dShippedRelease-4` — the text and code the batch repairs (review ids 78)
- **consumes-from** `DEPL-dShippedRelease-6` — the text and code the batch repairs (review ids 21, 37, 38, 76)
- **consumes-from** `DEPL-dShippedRelease-10` — the text and code the batch repairs (review ids 10, 11, 56)
- **consumes-from** `DEPL-dShippedRelease-12` — the text and code the batch repairs (review ids 13, 108)
- **consumes-from** `DEPL-dShippedRelease-13` — the text and code the batch repairs (review ids 105, 112)
- **consumes-from** `DEPL-dShippedRelease-14` — the text and code the batch repairs (review ids 20, 75, 97)
- **consumes-from** `DEPL-dShippedRelease-15` — the text and code the batch repairs (review ids 37, 76)
- **consumes-from** `DEPL-dShippedRelease-17` — the text and code the batch repairs (review ids 110)
- **consumes-from** `DEPL-dShippedRelease-27` — the text and code the batch repairs (review ids 59, 102, 109)
- **consumes-from** `DEPL-dShippedRelease-31` — the text and code the batch repairs (review ids 19, 40)
- **consumes-from** `DEPL-dShippedRelease-49` — the text and code the batch repairs (review ids 41, 43, 51, 100)
- **consumes-from** `DEPL-dShippedRelease-50` — the text and code the batch repairs (review ids 32, 41, 43, 50, 51, 99, 100)
- **consumes-from** `DEPL-dShippedRelease-51` — the text and code the batch repairs (review ids 61, 75, 104)
- **consumes-from** `DEPL-dShippedRelease-52` — the text and code the batch repairs (review ids 14, 64, 102)
- **consumes-from** `DEPL-dShippedRelease-53` — the text and code the batch repairs (review ids 58, 60, 98)
- **consumes-from** `DEPL-dShippedRelease-54` — the text and code the batch repairs (review ids 57)
- **consumes-from** `DEPL-dShippedRelease-56` — the text and code the batch repairs (review ids 105)
- **consumes-from** `DEPL-dShippedRelease-57` — the text and code the batch repairs (review ids 25)
- **consumes-from** `DEPL-dShippedRelease-58` — the text and code the batch repairs (review ids 54, 58, 78, 79)
- **consumes-from** `DEPL-dShippedRelease-59` — the text and code the batch repairs (review ids 23, 27, 58, 60, 92, 107, 108)
- **consumes-from** `DEPL-dShippedRelease-60` — the text and code the batch repairs (review ids 60, 97)
- **consumes-from** `DEPL-dShippedRelease-61` — the text and code the batch repairs (review ids 12, 34, 62, 101)
- **consumes-from** `DEPL-dShippedRelease-62` — the text and code the batch repairs (review ids 26, 42, 62, 77)
- **consumes-from** `DEPL-dShippedRelease-63` — the text and code the batch repairs (review ids 26, 63)
- **consumes-from** `DEPL-dShippedRelease-64` — the text and code the batch repairs (review ids 63)
- **consumes-from** `DEPL-dShippedRelease-65` — the text and code the batch repairs (review ids 10, 31, 55, 90)
- **consumes-from** `DEPL-dShippedRelease-66` — the text and code the batch repairs (review ids 9, 11, 44, 62, 71)
- **consumes-from** `DEPL-dShippedRelease-68` — the text and code the batch repairs (review ids 23, 27, 58, 60, 80, 81, 92, 106, 107)
- **consumes-from** `DEPL-dShippedRelease-69` — the text and code the batch repairs (review ids 27, 50, 58, 60, 81, 100)
- **consumes-from** `DEPL-dShippedRelease-70` — the text and code the batch repairs (review ids 14, 103)
- **consumes-from** `DEPL-dShippedRelease-71` — the text and code the batch repairs (review ids 46, 53, 68, 84, 108)
- **consumes-from** `DEPL-dShippedRelease-72` — the text and code the batch repairs (review ids 13, 58, 68)
- **consumes-from** `DEPL-dShippedRelease-73` — the text and code the batch repairs (review ids 20, 60)
- **consumes-from** `DEPL-dShippedRelease-74` — the text and code the batch repairs (review ids 61)
- **consumes-from** `DEPL-dShippedRelease-75` — the text and code the batch repairs (review ids 26, 59, 85, 109, 110)
- **consumes-from** `DEPL-dShippedRelease-77` — the text and code the batch repairs (review ids 21, 37, 38, 76, 111)
- **consumes-from** `DEPL-dShippedRelease-78` — the text and code the batch repairs (review ids 15, 16, 17, 18, 19, 39, 40, 45, 56, 64, 65, 73, 74, 75, 79, 82, 112, 113, 114)
- **consumes-from** `DEPL-dShippedRelease-79` — `unfired` and the value table, which id 20's line sits beside
- **consumes-from** `DEPL-dShippedRelease-80` — the arms of `run_deploy_review`, on which id 97's `--refire` sits
- **consumes-from** `DEPL-dShippedRelease-81` — `test_parents_admit`, which S31, S32 and S36's one rule feeds
- **consumes-from** `DEPL-dShippedRelease-84` — `read_report_verdict`, which id 97's report must pass
- **consumes-from** `DEPL-dShippedRelease-85` — `derive_report_count`, which id 97's one confirmed row satisfies
- **consumes-from** `DEPL-dShippedRelease-90` — the `landing` term, which id 97's report passes by stating its range, DEPL-dShippedRelease-110 having replaced the stamp
- **consumes-from** `DEPL-dShippedRelease-92` — `test_records_commit`, beside which ids 23, 92 and 107 grade the tree
- **consumes-from** `DEPL-dShippedRelease-93` — `queue-exit`, which id 108's refused row also calls
- **consumes-from** `DEPL-dShippedRelease-94` — `late-records`, beside which id 27 adds its two verbs
- **consumes-from** `DEPL-dShippedRelease-103` — the exit row's key, on which ids 13, 68 and 108 rest
- **consumes-from** `DEPL-dShippedRelease-104` — `_cmd_adopt`'s check, which id 77 rules on
- **consumes-from** `DEPL-dShippedRelease-110` — S2, which S49's `dispose-with-reason` report must pass, so the edge naming the stamp reads this unit (round-3 id 29)
- **consumes-from** `DEPL-dShippedRelease-114` — S49's route, which reads as S3 scopes it (round-3 id 22)
- **consumes-from** `DEPL-dShippedRelease-118` — S49's owner item, the way out of this refusal (round-3 id 50)
- **consumes-from** `DEPL-dShippedRelease-119` — `CENSUS_VERBS`, which S8 widens, and the predicate AC4 reads (round-3 id 5)
- **hands-off** `DEPL-dShippedRelease-125` — the text and code which the round-3 minors batch repairs (round-3 ids 7, 9, 10, 11, 20, 24, 26, 34, 41, 44, 46, 53, 58, 62, 65, 69, 70, 71, 73)
- **consumes-from** `DEPL-dShippedRelease-130` — `render_landing_record` and the `dispose-with-reason` verb, which S49's report and option read (round-4 id 4)
- **consumes-from** `DEPL-dShippedRelease-112` — S1's `diff-review` refusal, which reaches S49's report (round-4 id 52)
- **hands-off** `DEPL-dShippedRelease-138` — the text and code the batch repairs (round-4 ids 8, 19, 34, 41, 47, 52, 67); S44's Skill line reads "`--deploy land <slug>`, or the lander's `--land`. Never with a hook-bypass flag.", so check 44 of `tools/unattended/check-unattended.sh` keeps its literal at this unit's pass

## 4. Design

### Why one unit and not two

M4 admits two batches only when the minors split into two disjoint write sets by M6. They do not. A loop half and a deployer half both write `tools/gate-legs.json` (S15, S39, S45), S19's grep reads every file of both halves as an acceptance input, which M6's clause 2 excludes, and `tools/policy/catalogue.toml` takes S33 and S60. The batch builds after every other unit, so a second unit buys no concurrency.

### The rule units 50, 69 and 81 share

Report ids 32, 50 and 99 each restate `test_spec_run_landing`, and the report asks one rule. It is true when `unattended.sh --spec-run <slug>` exits 0 and `read_build_rows` gives at least one row, every row DEFERRED, WONTDO or a CLOSED row S31 admits, and at least one DEFERRED. Exit 1 and exit 2 of the verb read false, with its reason printed. Unit 69's `test_carry_forward_landing` stays apart, because a build run with a deferred row is carry-forward and no spec run: it asks whether a lease hands back, and this rule asks whether a landing carries product.

### The census at base

PINNED at `d3b09a61` by DEPL-dShippedRelease-102's predicate over `apply`, `adopt` and `update`, with `CENSUS_NOT_A_SPAWN`: `tools/govkit/matrix.py`, `tools/govkit/selftest.py`, `tools/policy/check_policy.py`. `tools/govkit/kit_walk.py`, `tools/govkit/offer.py`, `tools/integrations/ci/ci_emit.py` and `tools/govkit/steps/receipt_schema_5.py` join by the close, and this unit assigns `GOVKIT_INSTALL_FROM` in each, the hand-off DEPL-dShippedRelease-102 S4 names. The helpers the walk sees are `run`, `gov_run`, `fork_gov`, `run_in_gov`, `run_govkit`, `run_gov`, `run_gov13`, `run_gov17`, `run_pv_govkit` and `run_ungraded_update`.

### The residue AC8 keeps

At the close the grep of S16 and S19 prints only: the rows of `memory/project/ended-legs.txt`, the retirement record itself; `tools/govkit/registry.toml`'s `[[retired]]` row; and `tools/run-gates/ceiling-evidence.txt`, a measurement of a past run. Every other line at base is rewritten or goes with its script.

### The kept fleet lines

`\bfleet\b` over unit 31 S5's six paths, PINNED at `d3b09a61`, keeps these, each meaning the node set. The report's list was taken with `the fleet\b`, and the wider pattern adds the first two.

| Line | Text |
|---|---|
| `WIRE-INTO-PROJECT.md:37` | `**Fleet** — every machine that works here must hold a tag` |
| `WIRE-INTO-PROJECT.md:38` | `` `<gov>/<prefix>/playbook/fleet.toml` `` |
| `WIRE-INTO-PROJECT.md:163` | `the node registry is generated from the fleet` |
| `WIRE-INTO-PROJECT.md:177` | `### Nodes — taking the fleet's tags in an existing adopter` |
| `WIRE-INTO-PROJECT.md:181` | `take the fleet's: make sure every node working here holds a fleet row` |
| `WIRE-INTO-PROJECT.md:182` | `which refreshes the fleet registry` |
| `WIRE-INTO-PROJECT.md:796` | `comes from the fleet registry` |
| `WIRE-INTO-PROJECT.md:2176` | `Take the fleet's node tags` |
| `tools/govkit/selftest.py:5510` | `committed non-default descriptor in the fleet` |

### The corrected reuse audits

Each probe re-ran at writing, and each ranked name-stem helpers, so the seam below is read from the spec's own §2 and §4 and not from the probe.

| Unit | Seam it extends | Behaviour phrase | Ranked |
|---|---|---|---|
| 53 | `--deploy record`, `set_landing_field` | copy a landing verdict onto a record at its write | `write`, `write_text`, `records` |
| 59 | `check_landing_admitted` | admit a records only landing ahead of the queue | `records`, `queue`, `extract_records` |
| 60 | `run_deploy_review` | read a report path from a field before firing a review | `read`, `read_text`, `before` |
| 68 | the lander's build-lease fence, `run_late_records_landing` | land a commit from a detached worktree after the tombstone | `build_commit`, `add_scratch_worktree` |
| 69 | `run_unlease`, `check_unleased` | hand a build lease back on a carry-forward landing | `build`, `build_commit`, `build_fixture` |
| 73 | `check_landing_review` | grade a close term against sources the field does not control | `note`, `field`, `terms` |
| 51 | `read_landing_pin`, `read_landing_outcome` | read the first parent tip a landing was prepared on | `read`, `read_text`, `read_conf` |
| 74 | `classify_outcome`, the `[[outcome]]` grammar | decide an install outcome from an exit code and a probe | `probe`, `classify_outcome`, `outcome_accepted` |
| 66 | the leg arm of `tools/check-spec-tokens.py` | retire a gate leg and keep older specs resolvable | `resolve`, `legs`, `leg` |
| 61 | `read_install_from`, an environment seam | declare an environment override for a test harness | `declares`, `declared_list`, `declared_scalar` |
| 62 | `_cmd_apply`'s pre-write pass | refuse an install before the first write | `write`, `before`, `write_text` |

### Supersedes

Each scope item names the unit it lands on and the sentence it restates, and unit 78's and each audited unit's text stays as written. This spec is the correction, and a unit's ledger line for a superseded criterion points here.

### Evidence

- `tools/check-spec-tokens.py:331` excludes DEFERRED and CLOSED from LIVE.
- `tools/lib/resolve_bash.py:21-22` hold `"bash"` inside the block, and `tools/push-main.sh:454` writes the per-SHA log.
- `.githooks/pre-commit:226-229` runs hygiene `--staged`, and `memory/guides/UNATTENDED-PROTOCOL.md` measured 66859 bytes at `d3b09a61`, one under its limit.
- `tools/run-gates/ceiling-evidence.txt:133` holds the 465.2s reading.
- `codex --help` at `codex-cli 0.139.0` lists no hook or trust command, only `--dangerously-bypass-hook-trust`, per invocation; `codex hooks --help` falls back to the top-level help. Measured 2026-11-01 on this node, PINNED.
- `memory/map/features/` holds the claims of the legs S46 moves: `memory-tree-hygiene.md`, `govkit.md`, `lexicon.md`, `run-gates.md`.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `read_build_rows`, `derive_landing_merge` | functions, `tools/loop/deploy_items.py` | `py.function`, each OK by `--suggest` at writing |
| `RECORDS_RENDERS`, `POLICY_DEFAULTS` | module constants | none |
| `admission-error`, `prior-underived` | a landing class, an outcome word | none |
| `landing-admission`, `landing-review-stalled`, `landing-review` | owner-item kinds, a wait kind | none |
| `deploy items selftest` | gate leg | none |
| `--spec-run`, `--refire`, `records-landing`, `carry-forward` | verbs and a flag | none |
| `release.engine.compose-systemd.<environment>.service`, `currency.max-age-days` | catalogue rows | none |
| `recipe` | a `codex-retrust` row key | none |

### Files touched (estimate)

- `tools/loop/deploy_items.py`, `tools/loop/deploy_fixture.py`, `tools/loop/kit.toml`
- `tools/push-main.sh`, `tools/push-main.test.sh`, `tools/unattended/unattended.sh`
- `tools/unattended/SKILL.template.md`, `tools/unattended/PROTOCOL.template.md`, `tools/unattended/VERBS.template.md`, `tools/unattended/STOPS.template.md`
- `memory/guides/UNATTENDED-PROTOCOL.md`, `memory/guides/UNATTENDED-VERBS.md`, `memory/guides/UNATTENDED-STOPS.md`, the renders
- `tools/runtime/waits.py`, `tools/runtime/owner_items.py`, `tools/runtime/cadence.py`, `tools/runtime/cadence_dispatch.py` (new)
- `tools/check-spec-tokens.py`, `tools/check-spec-tokens.test.sh`, `memory/project/ended-legs.txt`
- `memory/project/spawn-idiom-sites.txt`, `memory/project/substitution-fed-loops.txt`, `memory/project/testsuite-count-waivers.txt`, `memory/project/unarmed-branches.txt`
- `tools/govkit/govkit.py`, `tools/govkit/selftest.py`, `tools/govkit/matrix.py`, `tools/govkit/harness_census.py`, `tools/govkit/kit_walk.py`, `tools/govkit/offer.py`, `tools/govkit/codex_targets.py`, `tools/govkit/steps/receipt_schema_5.py`
- `tools/integrations/release.py`, `tools/integrations/release_fixture.py`, `tools/integrations/ci/ci_emit.py`, `tools/integrations/engines/compose_systemd.py`, `tools/integrations/engines/compose-systemd-host.sh`
- `tools/workflows/review_pin.py`, `tools/workflows/kit.toml`, `tools/workflows/README.md`
- `tools/policy/catalogue.toml`, `tools/policy/unsummarised-keys.txt`, `tools/policy/check_policy.py`
- `tools/playbook/core.py`, `tools/playbook/README.md`
- `tools/run-gates/receipt_fields.py`, `tools/run-gates/check_currency.py`, `tools/run-gates/kit.toml`
- `tools/gate-legs.json`, `tools/govkit/subject-pins.tsv`
- `memory/map/features/memory-tree-hygiene.md`, `memory/map/features/govkit.md`, `memory/map/features/lexicon.md`, `memory/map/features/run-gates.md`, `memory/map/features/row-grammar.md`, `memory/map/features/spec-tokens.md`
- `help/loop.md`, `help/deploy.md`, `help/release.md`, `help/offers.md`, `help/upgrade-steps.md`, `help/managed-guards.md`

## 5. Production-readiness checklist

- security — S41 keeps a tracked receipt from naming a command, S29 and S30 grade the tree a records landing carries, and S33 keeps an engine value in its namespace; the rest add no surface.
- perf / scale — nothing here adds a read a landing feels; S52's `rev-parse` is one spawn.
- error / empty / loading states — each item names its refused state, and its criterion plants it.
- observability — each state prints the line its item names.
- risks — a batch this wide meets moved code at its pass, since every unit it lands on is built first; each item is re-read against source at the pass.
- testing — the criteria of §6 and the arms of §7.
- migration — none. Every path is either new in this build or rewritten by a unit of it, and `currency.max-age-days` is a new key with a default.
- user docs — S70, S71 and S69 name each page; `help/upgrade-steps.md` and `help/offers.md` take S62's rows.

## 6. Acceptance criteria

- **AC1** — When `python tools/check-spec-tokens.py --list` runs on a fixture tree holding a DEFERRED
  spec that names a retired leg with a row, it prints no `ENDED` finding; flipped to OPEN, it prints no
  `[leg]` hit.
  Red when: a carried spec's row reds as stale, or its reopening reds the bar.
- **AC2** — When `git show` reads the script at `f4597719` and `grep -c 'kit-versions:'` counts that
  blob, it prints the row count unit 65's table lists.
  Red when: the disposition is graded on a file that is gone at the pass.
  figure: 33 is PINNED at `f4597719` by the same read.
- **AC3** — When `python tools/govkit/govkit.py version` runs on a scratch copy per row of unit 65's
  table, each exits 1 naming its finding, `:191`'s marker, `:214`'s and `:271`'s zero population
  included.
  Red when: a row has no plant, so a check vanishes with the script.
- **AC4** — When `python harness_census.py` runs at the close, its file lines equal §4's list, and with the assignment cut from `tools/govkit/matrix.py` it exits 1 naming that file.
  Red when: a helper spawn is unseen, a doc is demanded a declaration, or a `get` reads as a spawn.
- **AC5** — When `bash tools/push-main.sh --land --slug fx` runs with `admit` stubbed to exit 2, it
  exits 1 and the outcome reads `admission-error`, no transition is recorded and the queue ref gains no
  `exit` commit; a direct `--land --slug` refused by a gate writes one with `why` `refused`, and the
  queue's second build then exits 0 from `admit`.
  Red when: a crash costs a re-test and a queue place, or a refused direct landing holds every build.
- **AC6** — When `python deploy_fixture.py --case linear-history` walks a landing on a line with no
  first-parent merge, `outcome <sha>` prints `landed-ungated` and `prior-underived`,
  `python review_pin.py --landing <sha>` refuses, and the walk passes `deploy.carries`.
  Red when: a healthy remote reads as dead, or `deploy.carries` runs `-..<sha>`.
- **AC7** — When `python -c` loads `tools/gate-legs.json` by `json.load`, the row `deploy items selftest`
  holds `--selftest`, `deploy items` ends `deploy_fixture.py`, `--all`, and with an adapter row cut from
  a scratch copy `python deploy_items.py --selftest` exits 1 naming the item.
  Red when: unit 78 AC7 and AC24 grade one argv for two commands, or `check-wired` runs in no leg.
- **AC8** — When `git grep -n -E 'govkit.py epoch|check-verdict-epoch|epoch legs|kit version markers' -- tools skills .githooks WIRE-INTO-PROJECT.md help memory/guides memory/map/features memory/project .memory-tree.conf`
  runs at the close, its files equal §4's residue; at `f4597719` it prints the four `memory/project/`
  registers.
  Red when: a live reader stays stale, or the criterion demands a rewrite of frozen history.
- **AC9** — When `git grep -n -F '["bash",' -- '*deploy_items.py'` runs at the close, it prints nothing,
  and `python inline_blocks.py --check` holds the block there.
  Red when: a bare argv reaches the WSL launcher, or the criterion forbids the block it requires.
- **AC10** — When `python tools/check-spec-tokens.py --list` runs at the close, it prints no `[leg]` hit
  on a live spec, and a live spec of another build naming a retired leg is held by name.
  Red when: the criterion needs units CLOSED by the close to stay open.
- **AC11** — When `git grep -n -i -E '\bfleet\b'` runs over unit 31 S5's six paths at the close, its
  lines equal §4's table, and a planted `the whole fleet` at `tools/codebase-map/map_lib.py:62` adds a
  line.
  Red when: the compare has no comparand, or a renamed site goes unread.
- **AC12** — When `python deploy_fixture.py --case review-pending-line` runs `--deploy close` on `pending`,
  it prints `held · check_landing_review · pending`, and on `lgtm` it prints `forged`.
  Red when: an honest `pending` reads as tampering.
- **AC13** — When `python compose_systemd.py --fixture --case restart-fails` runs under each `host-kind`,
  `read-current` prints the configured digest, and `rollback <E> <sha> --expect <that digest>` exits 0;
  `--case daemon-down` exits 4, and `--case two-replicas` exits 2 naming the service.
  Red when: E has no id when a rollback is needed, or a dead daemon reads `none`.
- **AC14** — When `python deploy_fixture.py --case engine-records-tree` plants a tracked `tools/` file
  moved into the build folder, and a merge whose tree adds `tools/x`, `test_records_landing` is false
  and the remote's tip does not move; a records commit moving `memory/LIVE.md` reads true.
  Red when: a product change passes as records, or a dated record strands the lander.
- **AC15** — When `python deploy_items.py --fixture --plant spec-run-rule` runs a dWellOiledMachine-shaped
  build, a WONTDO row and a build run with every unit deferred, the first two exit 0 from `parents`, and
  `--plant spec-run-empty-region` and the third exit 3.
  Red when: the rule reads one word two ways, or passes on an empty region.
- **AC16** — When `python -c` reads `tools/policy/catalogue.toml`, no `release.env.` row holds `service`,
  and `read_engine_values` returns eight values for a fixture environment.
  Red when: an engine-private value lands in the neutral namespace.
- **AC17** — When `python deploy_items.py --fixture --plant parent-wontdo` reads a parent whose README
  reads `**Build status:** WONTDO`, it answers `withdrawn`, and the plant prints `derive_landed_owners`'
  differing answer.
  Red when: a wholly retired parent reads `held` with no route.
- **AC18** — When `python deploy_fixture.py --case owner-leave` answers `leave-queue` through the real
  `owner_items.py answer` verb, the queue ref holds an exit row naming `owner`.
  Red when: the owner answers and a live head still blocks every landing.
- **AC19** — When `python deploy_items.py check-wired` runs, it prints `<n> item(s) · <m> adapter row(s)`,
  and `n` equals the `read_items(step="step.deploy")` count.
  Red when: a criterion compares a count its verb cannot print.
- **AC20** — When `python -c` reads the `run-gates adopter e2e` row, its guard holds
  `{prefix}/integrations/`, and a staged edit to `ci_emit.py` selects the leg.
  Red when: the edit that would break the check skips it.
- **AC21** — When `python kit_walk.py --fixture --plant retrust-second-move` moves one hook twice and
  re-runs once, the receipt holds one open row; `--plant retrust-tampered-argv` refuses printing the
  `argv`; and `--plant attend-retrust` prints the recipe and ends `attended` with no spawn.
  Red when: a row duplicates, a tracked receipt runs a command, or `attend` hangs.
- **AC22** — When `python review_pin.py --landing <sha>` runs with `outcome` exiting 1, with a `base` that
  resolves to nothing, with a `base` equal to `<sha>` and with no loop kit, each exits 2 naming the case
  and fires no review.
  Red when: a review pins over an unusable base, or a missing kit tracebacks.
- **AC23** — When `python receipt_schema_5.py --fixture --case update-untagged` runs
  `update --to <untagged> --write`, it exits 2, and `git status --porcelain` and the receipt's bytes are
  unchanged; a passing `adopt` records `install_from`.
  Red when: the bytes half reads green by construction.
- **AC24** — When `git grep -n -F -- '--land --slug <slug>' -- tools/unattended/SKILL.template.md tools/unattended/PROTOCOL.template.md`
  runs at the close, it prints nothing, and
  `bash tools/check-template-size.sh memory/guides/UNATTENDED-PROTOCOL.md` exits 0.
  Red when: a run following its binding instructions bypasses `run_deploy_land`.
- **AC25** — When `python deploy_fixture.py --case engine-late-close-stale` leaves a directory and branch
  from a killed run, the late landing lands, and a re-run after exit 5 meets no leftover;
  `git worktree list` holds no `close-wake` path after either.
  Red when: a safety-path close never finishes against its own leftovers.
- **AC26** — When `python deploy_fixture.py --case review-stalled` plants `pending` past
  `flow.wait-ceiling`, one `landing-review-stalled` item is raised and a second walk raises none;
  answering `dispose-with-reason` closes the term.
  Red when: a dead review holds the close with no alert, or its disposal reads `forged`.
- **AC27** — When `python deploy_fixture.py --case field-cas-lost` fails the setter's compare-and-swap
  three times, `unattended.sh --deploy field <sha> core green` exits 3, and `run_deploy_core` stops with
  that exit.
  Red when: a failed write reads as `record pending` and the verdict is lost.
- **AC28** — When `python deploy_items.py --fixture --plant status-right-index` reads a row whose title
  holds `- run: |`, `read_build_rows` returns its real Status, and a grep of `gen:build-units` over
  `tools/loop/` finds no second parser.
  Red when: a pipe in a title decides a parent's state.
- **AC29** — When `python deploy_items.py --fixture --plant outcome-shallow` runs, and
  `--plant outcome-malformed-sha`, each exits 2; `--plant outcome-unknown-object` prints `unlanded`.
  Red when: a fault reads as a class, or a killed node's unpushed merge reads as a dead probe.
- **AC30** — When `python deploy_fixture.py --case engine-core-running-record-fails` fails the record, the
  walk exits that exit, and `--case engine-core-refuse` runs the record with `core: pending`.
  Red when: a failed record reads as a bar wait, or a refused core leaves no landing record.
- **AC31** — When `python deploy_fixture.py --case core-ceiling-no-log` runs with the log absent, and
  `--case core-ceiling-growing-log` with a live writer, each raises one `core-verdict` item at the
  ceiling.
  Red when: a bar still writing defers the ceiling, or an absent log gives no clock.
- **AC32** — When `python release_fixture.py --case policy-absent` runs with no policy kit, it prints
  `policy — no policy kit · ` and the key's default, and
  `python check_currency.py --fixture --case stale-record` reds naming the record's age against
  `currency.max-age-days`.
  Red when: two adapters answer a missing kit two ways, or the builder invents the bound.
- **AC33** — When `python ci_emit.py --fixture` runs on the tree, every case line but `baseline-red`
  prints `baseline 0`, and `baseline-red` passes by reading `baseline`.
  Red when: a correct build fails its own default set.
- **AC34** — When `python deploy_items.py carry-forward --slug fx` and `records-landing --slug fx` run on
  the fixtures, each exits 0 on true and 1 on false.
  Red when: a shell caller invents its own spelling of a Python test.
- **AC35** — When `grep -c leave-queue loop.md` runs at the close, it prints at least 1, and the page
  states the exit row.
  Red when: an owner meets the option with no page explaining it.
- **AC36** — When `git grep -c 'first-parent --min-parents=2' -- '*deploy_items.py'` runs at the close, it
  prints 1, in `derive_landing_merge`.
  Red when: two copies of one graph walk sit in one module.

## 7. Gates

`codebase-map coverage + freshness` · `govkit selfcheck` · `kit/dogfood doc parity` · `govkit runbook parity` · `dead-path carriers (deleted files still named)` · `unattended protocol size` · `unattended kit gate` · `push-main self-test` · `build-index selftest` · `memory-hygiene self-test` · `transition-audit arms` · `straggler-guard arms` · `measure-legs selftest` · `run-gates canary` · `run-gates gov canary` · `recall floor` · `recall floor arms` · `policy fixtures` · `policy check` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `lexicon naming predicates` · `playbook render selftest` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/loop/deploy_fixture.py · covers AC6 AC12 AC14 AC18 AC25 AC26 AC27 AC30 AC31 · one planted case per criterion, its failing case each item's change cut out in turn · none

New arm: tools/loop/deploy_items.py · covers AC15 AC17 AC28 AC29 AC34 · the planted rows and refs, their failing case `read_build_rows` indexing from the left · none

New arm: tools/push-main.test.sh · covers AC5 · a stubbed `deploy_items.py` beside the lander, its failing case `admit` exit 2 routed to `refused` · none

New arm: tools/govkit/kit_walk.py · covers AC21 · `attend-retrust`, its failing case the recipe printed with no stop · none

New arm: tools/integrations/engines/compose_systemd.py · covers AC13 · both host kinds, their failing case `none` on a failed read · none

New arm: tools/check-spec-tokens.test.sh · covers AC1 · a DEFERRED spec flipped to OPEN, its failing case the row population read from LIVE · none

## 8. Open questions

- **F1 — One batch or two (§4)?** Options: (a) one unit; (b) two, by M6. (b) has no disjoint split, since
  both halves write `tools/gate-legs.json` and S19 reads both as an acceptance input. RESOLVED (agent,
  2026-11-01, delegated): (a), rung 3. widens: none · relaxes: none
- **F2 — Does `adopt` refuse or stand exempt, S43?** Options: (a) the same check before its first write;
  (b) an exemption, since `adopt` installs nothing. (b) records `any-commit` under `release-tag`, the
  state unit 62 AC2 calls a defect. RESOLVED (agent, 2026-11-01, delegated): (a), rung 1, id 94's fix
  decides it. widens: none · relaxes: none
- **F3 — A home and a grant for the two catalogue rows, S33 and S60?** Options: (a) `service` under
  `release.engine.compose-systemd.<environment>`, and `currency.max-age-days` beside
  `currency.max-behind`; (b) `release.env.<environment>.service`, and an age read from
  `currency.max-behind`. (b) puts an engine value in the neutral family, and `max-behind` counts tags.
  RESOLVED (agent, 2026-11-01, delegated): (a), rung 3, default 14 being two of unit 3's weekly cuts.
  widens: none · relaxes: none · grants: PLAY-dClosedLoop-3 the rows
  `release.engine.compose-systemd.<environment>.service` and `currency.max-age-days`.
- **F4 — Which reader says a parent landed, S72?** Options: (a) the generated `**Build status:**` line
  with a `CLOSED` row, unit 49's; (b) `derive_landed_owners`' spec-header read through `tree_lib`. (b)
  needs the memory-tree kit at each `read_parent_state`, and reads a WONTDO-only build as landed, the
  unsafe direction for a hold. RESOLVED (agent, 2026-11-01, delegated): (a), rung 3, the difference
  asserted by `parent-wontdo`. widens: none · relaxes: none
- **F5 — What does a `dispose-with-reason` report's verdict read, S49?** Options: (a) `BLOCKED` with the
  reason as its one confirmed row; (b) `CLEAN WITH FIXES` with none. (b) says a review ran that did not.
  RESOLVED (agent, 2026-11-01, delegated): (a), rung 3, the one closed-set member that is true, its
  filed row the owner's trail. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from the 79 minors, one scope item per raw id of the round-2 spec audit.
- rev-2 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the round-3 spec audit's promoted units declare toward this unit (units 110, 114, 118, 119, 125); no scope, design or criterion moved. The edge naming the stamp reads DEPL-dShippedRelease-110, as report item H1 asks.
- rev-3 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the round-4 spec audit's promoted units declare toward this unit (units 130, 112, 138); no scope, design or criterion moved.

## 10. Reuse audit

The seams extended are named per item by the report's corrected fixes, each a seam of the unit it lands
on, and §4 "The corrected reuse audits" re-runs the probes of the audited units it corrects. Probed for
the batch: `python tools/codebase-map/reuse_lookup.py "keep two copies of a credential predicate agreeing"`
and the eleven phrases of §4's table ranked name-stem helpers and no second home for any item, apart
from `classify_outcome`, which is unit 74's. No item mints a seam of its own except `read_build_rows`
and `derive_landing_merge`, each replacing a respelling. The recall probe surfaced the report's items,
which this spec follows.

Recall terms used:
`python tools/memory-recall/query.py "which spec audit minors repair the landing queue records landing and the release engine" --terms "landing queue records test_records_landing exit row read_build_rows spec run check_spec_run census retrust ceiling"`
