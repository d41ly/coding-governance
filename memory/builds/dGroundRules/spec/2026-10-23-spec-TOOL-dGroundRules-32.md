# TOOL-dGroundRules-32 — the round-1 audit of units 22 to 25, its minors: twenty findings closed in the code those units leave, one scope item each

**Status:** DEFERRED · rev-7 · 2026-10-24 · node d · Tier-2 · base 3708a705 · streams tooling · order 10 · advances TOOL-dGroundRules-12

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-32-deviation-20.md](../build/2026-10-23-build-TOOL-dGroundRules-32-deviation-20.md) | deviation | — |
| [2026-10-23-build-TOOL-dGroundRules-32-deviation-61.md](../build/2026-10-23-build-TOOL-dGroundRules-32-deviation-61.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dGroundRules-32-build-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-32-build-brief.md) | journal | — |
| [2026-10-24-prompt-TOOL-dGroundRules-32-1-spec-writer.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-32-1-spec-writer.md) | journal | — |
| [2026-10-24-prompt-TOOL-dGroundRules-32-2-spec-writer.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-32-2-spec-writer.md) | journal | — |
| [2026-10-24-prompt-TOOL-dGroundRules-32-divergence-2-brief.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-32-divergence-2-brief.md) | research | — |
| [2026-10-24-prompt-TOOL-dGroundRules-32-divergence-brief.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-32-divergence-brief.md) | research | — |
| [2026-10-24-prompt-TOOL-dGroundRules-32-span-spec-writer.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-32-span-spec-writer.md) | journal | — |
| [2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-65 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-51 TOOL-dGroundRules-52 |
| [2026-10-23-review-TOOL-dGroundRules-26-32-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-26-32-spec-audit-round1.md) | spec-audit | TOOL-dGroundRules-26 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-27 TOOL-dGroundRules-30 TOOL-dGroundRules-31 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 22 to 25
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-22-25-spec-audit-round1.md`)
exited CONVERGED with 26 confirmed findings. Its six HIGHs are promoted one unit each,
`TOOL-dGroundRules-26` to `TOOL-dGroundRules-31`. BUILD-METHOD M4 promotes the other twenty,
thirteen MEDIUM and seven LOW, batched into one unit, and this is that unit. They land on units 22,
23, 24 and 25, and nearly every one of them writes `tools/policy/check_policy.py`; the build-order
half and the policy half both regenerate `memory/map/generated/symbols.json`, so they do not split
into two disjoint write sets by M6's clauses, and one unit carries them all. It repairs no unit in
particular, so it builds at order 10, above every unit of this build. Ids 10 and 19 share review
item M6, and each still takes its own scope item here. Ids 12, 15 and 22 are taken at LOW, the grade
the review gives them after its skeptic re-graded each from MEDIUM.

| Finding id | Severity | Review item | Unit it lands on | Scope item | Criterion |
|---|---|---|---|---|---|
| 3 | MEDIUM | M1 | 24, 25 | S1 | AC1 |
| 4 | MEDIUM | M2 | 23 | S2 | AC2 |
| 5 | MEDIUM | M3 | 23 | S3 | AC3 |
| 8 | MEDIUM | M4 | 25 | S4 | AC4 |
| 9 | MEDIUM | M5 | 25 | S5 | AC5 |
| 10 | MEDIUM | M6 | 25 | S6 | AC6 |
| 19 | MEDIUM | M6 | 25 | S7 | AC7 |
| 13 | MEDIUM | M7 | 23 | S8 | AC8 |
| 14 | MEDIUM | M8 | 25 | S9 | AC9 |
| 21 | MEDIUM | M9 | 24 | S10 | AC10 |
| 25 | MEDIUM | M10 | 22, 25 | S11 | AC11 |
| 27 | MEDIUM | M11 | 25 | S12 | AC12 |
| 28 | MEDIUM | M12 | 25 | S13 | AC13 |
| 6 | LOW | L1 | 25 | S14 | AC14 |
| 11 | LOW | L2 | 25 | S15 | AC15 |
| 12 | LOW | L3 | 24, 25 | S16 | AC16 |
| 15 | LOW | L4 | 25 | S17 | AC17 |
| 16 | LOW | L5 | 24 | S18 | AC18 |
| 22 | LOW | L6 | 25 | S19 | AC19 |
| 29 | LOW | L7 | 24 | S20 | AC20 |

Each item's fix is the one the review's skeptic judged sound; for id 12 it is the skeptic's
corrected fix. Where the review offered options, §8 records the pick.

## 2. Scope (IN)

- **S1** — Finding 3. Step 3 of this build's build-order region (`TOOL-dGroundRules-24`, `-5` and
  `-6`, each declaring `tools/policy/check_policy.py`) renders `no`, under `TOOL-dGroundRules-25`
  S37's rule as S9 here builds it, and this unit's commit re-renders the region. Observed by AC1.
- **S2** — Finding 4. Step 7 (`TOOL-dGroundRules-21`, `-22` and `-23`, which meet on
  `tools/policy/check_policy.py` and `tools/policy/budgets.py`) renders `no` by the same rule.
  Observed by AC2.
- **S3** — Finding 5. The `policy fixtures` guard already carries the descriptor line of every
  census kit, `{prefix}/memory-tree/kit.toml` among them (`tools/gate-legs.json:1798-1806`), written
  by `TOOL-dGroundRules-23`; S3 adds no guard line. What remains is the run-time derivation:
  `fixtures-guard-census` derives the descriptor path of every entry a census row's `kit` names from
  that entry's `descriptor` field in `tools/govkit/registry.toml`, and prints `WRONG` for one the
  guard does not cover, so no descriptor list is typed beside the registry. Observed by AC3.
- **S4** — Finding 8. Every descriptor `build_install_target` writes carries the `[answers]` table
  of S16, `manifest_path` and `user_skills` among them, so the fresh-target case installs a closure
  that reaches `kickoff-manifest`. That case already reports a non-zero `apply` as its `WRONG`
  before it reads the receipt (`run_fresh_target`, `tools/policy/check_policy.py:1149-1154`).
  Observed by AC4.
- **S5** — Finding 9, already holding at HEAD: no code changes. `legacy-homes-withheld-install`
  matches each `plan` line with `PLAN_LINE` (`tools/policy/check_policy.py:1257`), keeps the rows
  whose destination ends `/legacy-homes.txt`, and passes only when their (mark, role) pairs are
  exactly one `ORDER` `project-owned` pair (`:1273-1276`), so a `write` or `SIDE` row for the list
  fails it. Observed by AC5, which this unit makes as the confirming observation.
- **S6** — Finding 10. The observation of `TOOL-dGroundRules-25` AC39 reads only the build-order
  region: the rows `awk '/<!-- gen:build-order -->/,/<!-- \/gen:build-order -->/'` prints from
  `memory/builds/dGroundRules/README.md` that open with a step number. Observed by AC6.
- **S7** — Finding 19. The outcome of `TOOL-dGroundRules-25` S39 is limited to the steps that hold
  two units declaring `tools/policy/check_policy.py`, steps 1 to 9 and 12 to 14, each of which reads
  `no`; a one-unit step, 10, 11, 15, 16 or 20, reads `no` by `derive_parallel_step`'s first branch.
  Steps 17 and 18 each hold one unit declaring it and read `yes`: no two of their units' write sets
  meet, and no unit of either step consumes from another unit of the same step. Observed by AC7.
- **S8** — Finding 13. `budgets-ships-join` already prints a `WRONG` when the deployer's `Report`
  holds a problem (`tools/policy/check_policy.py:3564-3565`). What remains is the refactor:
  `read_shipped_descriptors(root)` in `tools/govkit/govkit.py`, factored out of `cmd_shipped`,
  returns the registry's descriptors or raises `Refusal` naming every problem the `Report` holds;
  `cmd_shipped` calls it and prints exactly what it prints today; and `budgets-ships-join` reads the
  descriptors through it in place of its own `read_descriptors` call and `Report` check
  (`:3556-3565`), the refusal being the case's `WRONG` naming the problems, so the join and
  `govkit.py shipped` read the registry through one function. Observed by AC8.
- **S9** — Finding 14. `derive_dir_segments`, `check_dir_shaped` and `check_guard_trips` move from
  `tools/check-spec-tokens.py` into `tools/memory-tree/design_lib.py`, and `check-spec-tokens.py`
  calls them through the `design_lib` it already loads. `check_writes_intersect(a, b)` in
  `design_lib.py` is true when `check_guard_trips` holds in either direction for some pair of the two
  write sets, and `derive_parallel_step` calls it in place of its nested `meets`. Its nested
  `pathlike` filter, a word of two or more non-empty segments, survives the switch: each write set
  reaches `check_writes_intersect` as its `pathlike` words only, so a step whose units all declare
  a write set renders as it does at HEAD and no build README outside the eight S13 names changes.
  An arm in `tools/check-spec-tokens.test.sh` holds its verdict equal to `overlaps` of
  `tools/unattended/lib-unattended.sh` on a directory and file pair and on a disjoint pair.
  Observed by AC9, whose audited text stands; its probe is run with the two pairs spelled whole as
  `TOOL-dGroundRules-34` S15 restates them.
- **S10** — Finding 21. The `policy fixtures` guard carries, for each kit of the policy kit's
  `requires` closure, its `kit.toml` and its `[adopt]` script, and `{prefix}/run-gates/kit.toml` and
  `{prefix}/run-gates/regen.py`, which `TOOL-dGroundRules-25` S7's case runs; `fixtures-guard-census`
  derives that closure at run time and prints `WRONG` for a path the guard does not cover.
  Observed by AC10.
- **S11** — Finding 25. A receipt `derive_census_tree` reads must be a JSON object whose `kits` is a
  list of strings and whose `prefix` is a relative string with no `..` segment. Any other shape
  answers `invalid` with the field it failed, `arm_cap_census` prints one finding naming the receipt
  and that field, and the `legacy-homes` arm (`TOOL-dGroundRules-25` S11) announces under `invalid`
  as it does under `adopter`. Observed by AC11.
- **S12** — Finding 27. One helper in `tools/policy/policy.py`, `derive_bomless_text(text)`,
  answers `text` less one leading U+FEFF. The strip `TOOL-dGroundRules-25` S30 put in
  `read_policy_text` (`tools/policy/policy.py:488`) moves into it, and `parse_policy`, `validate` and
  `arm_schema`'s nested parse (`tools/policy/check_policy.py:232`) each call it on their text before
  `tomllib` parses, so the three readers agree. `tools/policy/guard.py` imports no policy reader, so
  `TOOL-dGroundRules-6` AC10 stays true: `check_raise_shape` strips one leading U+FEFF from each
  decoded side inline before its own `tomllib` parse, under one comment naming
  `derive_bomless_text` as the helper it mirrors. `on-invalid-bom` also builds `build_guard_repo`'s
  fixture with its committed policy file BOM-led, stages the `guard-admits-raise` change over it with
  the BOM kept, and runs `guard.py --staged`, the one mode the guard accepts, which admits it.
  Observed by AC12.
- **S13** — Finding 28. A unit whose spec has no `### Files touched` sub-head contributes an unknown
  write set: the unit record keeps the `None` `read_spec_writes` answers, `derive_parallel_step`
  answers `unknown` for a step of two or more units holding one, and `render_order` prints it. The
  re-render in this unit's commit moves a step to `unknown` in eight build READMEs:
  `memory/builds/aBlindedTrial/README.md`, `memory/builds/aBoundedCeiling/README.md`,
  `memory/builds/aBriskPreflight/README.md`, `memory/builds/aTunedCompass/README.md`,
  `memory/builds/dDerivedDocket/README.md`, `memory/builds/dGaugedVintage/README.md`,
  `memory/builds/dRetiredFork/README.md` and `memory/builds/dTieredTribunal/README.md`.
  Observed by AC13.
- **S14** — Finding 6. `TOOL-dGroundRules-25` S36's observation is a staged probe: a scratch copy
  whose `memory/map/generated/symbols.json` lacks the `derive_census_tree` entry makes
  `gen_map.py --check` there exit non-zero naming it. Observed by AC14.
- **S15** — Finding 11. `TOOL-dGroundRules-25` AC17's observation calls the restatement gate,
  `tools/check-agent-cap-restatement.sh`, in place of a grep restating part of its pattern.
  Observed by AC15.
- **S16** — Finding 12, the skeptic's corrected fix, on the builder that exists. `build_install_target`
  in `tools/policy/check_policy.py` stays the one builder `adopter-fresh-target`,
  `legacy-homes-withheld-install` and `census-default-adopter` call, extended in place to
  `build_install_target(name, ids)`, which answers `(target, snapshot)`. The descriptor it writes
  ends with the `[answers]` table of `DEPLOY_FULL` in `tools/govkit/selftest.py`, read as text from
  the snapshot's copy of that file under the tool root `run_govkit` resolves; a copy holding no such
  table raises the `RuntimeError` naming that file. The `answers` parameter and the `KICKOFF_ANSWERS`
  constant leave the file with this change. Neither `apply` nor `check` moves into it:
  `legacy-homes-withheld-install` runs `plan` over the built target before its `apply`, and `check`
  is the fresh-target case's own (S18). An answer the closure asks for that `DEPLOY_FULL` lacks makes
  `apply` exit non-zero naming it, and each of the three cases carries `apply`'s output in its
  `WRONG` when it does. Before building, the builder probes `DEPLOY_FULL`'s answers against `apply`
  in a fresh target of the three cases' closures; if `apply` refuses, the builder hands back a
  divergence naming the failing answer and builds none of S16. Observed by AC16.
- **S17** — Finding 15. `read_spec_edges(text, verb)` in `tools/memory-tree/design_lib.py` returns
  the target and the text of each `**<verb>**` bullet of a spec's `### Edges` under check 12's target
  rule. `TOOL-dGroundRules-25` S38's consumes read is `read_spec_edges(text, "consumes-from")`, and
  `scan_handoffs` takes its bullets through `read_spec_edges(text, "hands-off")`, keeping its
  continuation-line read and its silent count. Observed by AC17.
- **S18** — Finding 16. After its `apply` exits 0, `run_fresh_target` runs
  `govkit.py check --target <t>` through `run_govkit`, and each `is in the receipt and not on disk` line it prints is
  the case's `WRONG`. Its own engine-or-seed absence loop (`tools/policy/check_policy.py:1160-1163`)
  gives way to those lines, so `check_policy.py` keeps only the stray-file direction of
  `TOOL-dGroundRules-24` S2 and the legacy-list line. Observed by AC18.
- **S19** — Finding 22. The refusal sentence stays the one `check_mirror_render` in
  `tools/policy/guard.py` prints at HEAD, quoted in the help page as it is today:
  "the mirror renders HEAD and its input <path> is staged changed: commit <path> first, then
  regenerate". `help/policy.md`'s section "Who may change the policy file" already names the policy
  file, the catalogue and `.agent-cap.conf`; its list of the mirror's inputs gains only the keys of
  the mirror's `legacy_blobs` record, so it names each input the guard compares. No code changes.
  Observed by AC19.
- **S20** — Finding 29, already met at HEAD: every git call `build_install_target` and the cases
  make in the target goes through `run_fixture_git`, which passes `-c user.name` and `-c user.email`
  (`tools/policy/check_policy.py:3915-3917`), so the target's commit needs no identity the runner
  holds. The builder confirms the deployer makes no commit in the target with the probe AC20 names;
  only if it does, `build_install_target` writes a repository-local `user.email` and `user.name`
  through `run_fixture_git`. Observed by AC20.

## 3. Non-goals (OUT)

- Every HIGH: `TOOL-dGroundRules-26` to `TOOL-dGroundRules-31`.
- Rewriting any reviewed spec's text. Each defect a spec stated is closed here in the code and the
  observation it governs, and the repaired unit's §3 names this unit; nothing is folded
  (BUILD-METHOD M4).
- Renumbering any unit's `order`, or a Rollout added to `TOOL-dGroundRules-23` or `-24`. The render
  says which steps are not parallel, and `--dispatch` condition 1 refuses a concurrent pair whose
  declared write sets meet.
- Moving the fresh-target case into `tools/govkit/matrix.py` (§4 "Alternatives rejected").
- A new `govkit.py` flag. S8 adds a function, not a verb or an option.

### Edges

- **consumes-from** `TOOL-dGroundRules-22` — `derive_census_tree` and its receipt read, which S11 gives a required shape
- **consumes-from** `TOOL-dGroundRules-23` — `budgets-ships-join` and its guard lines, which S3 and S8 extend
- **consumes-from** `TOOL-dGroundRules-24` — `adopter-fresh-target`, its receipt compare and its guard lines, which S4, S10, S16 and S18 extend
- **consumes-from** `TOOL-dGroundRules-25` — the build-order rule, the census and plan cases, the BOM strip, the map regeneration, the card criterion, the edge read and the widened refusal, which S1, S2, S5 to S7, S9, S11 to S15, S17 and S19 amend
- **consumes-from** `TOOL-dGroundRules-26` — `build_source_snapshot`, which `build_install_target` calls
- **consumes-from** `TOOL-dGroundRules-27` — `run_govkit`, which S18 calls and through which each case S16 serves runs `apply`
- **consumes-from** `TOOL-dGroundRules-29` — the three answers of `derive_census_tree`, beside which S11 adds `invalid`
- **hands-off** external — widening `SCRATCH_KITS` in `tools/govkit/matrix.py` to `policy`, which stays with the open ask `TOOL-aScouredKit-24`
- **hands-off** `TOOL-dGroundRules-33` — `build_install_target`'s answer values from `DEPLOY_FULL` (S16) and the guard lines of S3 and S10, which that unit extends to `{prefix}/govkit/selftest.py` and a trace of every in-process source read (id 26 of the round-1 spec audit of units 26 to 32)
- **hands-off** `TOOL-dGroundRules-34` — `build_install_target`, the receipt prefix rule, AC9's overlap pairs and their arm, AC6, the evidence citations and the kit README's census rows, which that unit amends, and the other build READMEs S13 re-renders, which that unit names as this unit's writes (ids 6, 15, 29, 37, 35, 18, 19, 9, 16, 27 and 36 of the round-1 spec audit of units 26 to 32)
- **hands-off** `TOOL-dGroundRules-52` — `derive_parallel_step`, whose rendering of steps 12 to 14 of this build that unit observes (id 6 of the round-1 spec audit of units 35 to 43)

## 4. Design

### Evidence

Every line below was read at base `3708a705` on 2026-10-23 and re-read by symbol at `93e4b4d31` on
2026-10-24, and the S3, S8 and S12 lines again at `3e16f3efe`; a line that moved is cited where it
now sits.

- `tools/policy/guard.py` imports `tomllib` (`:30`) and no policy module, its docstring saying it
  imports no policy reader (`:15-16`); `check_raise_shape` decodes both sides and parses them at
  `:145-146`; `main` accepts `--staged` alone (`:194-196`). `TOOL-dGroundRules-6` AC10 holds that
  import grep to printing nothing.
- `parse_policy` parses at `tools/policy/policy.py:493` and `validate` at `:560`; `arm_schema`
  parses again for `scan_keys` at `tools/policy/check_policy.py:232`. `build_guard_repo` sits at
  `:2175-2189` and the `guard-admits-raise` plant at `:2145`.
- The `policy fixtures` guard lists `{prefix}/govkit/entries/` and each census kit's descriptor
  outside it (`tools/gate-legs.json:1798-1806`), and lists neither `{prefix}/run-gates/kit.toml`
  nor `{prefix}/memory-tree/adopt-memory-tree.sh`.
- `budgets-ships-join` calls `govkit.read_descriptors` at `tools/policy/check_policy.py:3557` and
  reports a `Report` problem as a `WRONG` at `:3564-3565`.
- The `watch:` line of `memory/guides/SESSION-KICKOFF.md:6` names `tools/gate-legs.json`, so a
  commit writing it re-stamps the manifest's audit under check C5 of
  `skills/session-kickoff/manifest-check.sh`.
- `DEPLOY_FULL`'s `[answers]` (`tools/govkit/selftest.py:707-712`) set `manifest_path` to a
  `docs/` path and `user_skills` to a home path; `check_policy.py` names `DEPLOY_FULL` nowhere yet,
so no policy case has run `apply` with them.

- `memory/builds/dGroundRules/README.md:244-267` is the build-order region; every step renders `no`
  but 17 and 18, which render `yes`. `grep -nE "^\| (4|6|7) \|"` over the README also prints the
  roster rows `:62`, `:64` and `:65`, which end in clause text.
- Each spec's Files touched read through `read_spec_writes` (`tools/memory-tree/design_lib.py:525`):
  steps 1 to 9 and 12 to 14 each hold two or more units declaring `tools/policy/check_policy.py`;
  steps 10, 11, 15, 16 and 20 hold one unit; in steps 17 and 18 only `TOOL-dGroundRules-61` and
  `TOOL-dGroundRules-62` declare it. The builder's step probe rendered both `yes` under the rule S9
  and S13 build, the `pathlike` filter kept, and the eight READMEs of S13 as the only change outside
  this build; without the filter it also flipped aEvidencedLens step 8, aHoistedPass step 2 and
  aRepatriatedFork step 17 to `no`.
- `derive_parallel_step` sits at `tools/memory-tree/gen_build_index.py:1722-1743`, its nested
  `pathlike` at `:1728-1730` and `meets` at `:1732-1734`; the unit record reads `writes` as
  `read_spec_writes(text) or []` at `:546`, so a spec with no sub-head reads as declaring nothing.
- `tools/govkit/registry.toml:71` names `{prefix}/memory-tree/kit.toml` as a descriptor outside
  `entries/`; `tools/memory-tree/kit.toml:139-147` holds the `[[outcome]]` whose `ok = true` decides
  whether `apply` exits 0.
- `tools/hooks/kit.toml:9` requires `kickoff-manifest`, whose descriptor writes
  `to = "{manifest_path}"` (`tools/govkit/entries/kickoff-manifest.kit.toml:30`) and links
  `{user_skills}/session-kickoff` as a machine-scoped row `apply` only orders (`:44-49`);
  `DEPLOY_FULL` (`tools/govkit/selftest.py:703-713`) carries `manifest_path` and `user_skills` in its
  `[answers]` table. A missing answer fails `apply` with `entry '<id>' needs answer '<k>'`
  (`tools/govkit/govkit.py:4036`).
- `build_install_target(name, ids, answers="")` sits at `tools/policy/check_policy.py:1045-1077` and
  runs neither `apply` nor `check`; its callers are `run_fresh_target` (`:1148`, `apply` at `:1149`
  and its exit graded at `:1150-1154`), `run_legacy_withheld_install` (`:1270`, `plan` at `:1272`
  before `apply` at `:1277`) and `run_census_default_adopter` (`:1309`, the one passing
  `KICKOFF_ANSWERS`, `:1294-1295`). `run_govkit` sits at `:1080-1097`; the fresh-target case's
  engine-or-seed absence loop at `:1160-1163`; `PLAN_LINE` at `:1257` and its compare at `:1273-1276`.
- `run_fixture_git` (`tools/policy/check_policy.py:3915-3917`) passes `-c user.name` and
  `-c user.email` on every call, and `.github/workflows/remote-ci.yml` sets no git identity.
- `KIND_MARKS` maps `order` to `"ORDER "` (`tools/govkit/govkit.py:3834`), and `cmd_plan` prints
  `f"  {mark} [{row['role']:<13}] {row['dest']}   <- {row['kit']}"` (`:5054`).
- `cmd_shipped` (`tools/govkit/govkit.py:13283-13306`) exits 1 with no row when the `Report` holds a
  problem; `read_descriptors` (`:13238-13253`) only records a missing descriptor and continues.
- `derive_dir_segments`, `check_dir_shaped` and `check_guard_trips` sit at
  `tools/check-spec-tokens.py:560-590`; `scan_handoffs` at `:781-850`; `load_design_lib` at `:888`;
  the hands-off join's report line at `:1747`. `covers` and `overlaps` sit at
  `tools/unattended/lib-unattended.sh:745-750`; check 12's Edges block at
  `tools/memory-tree/check-memory-hygiene.sh:2514-2580`; `read_spec_consumes`, the consumes read of
  `TOOL-dGroundRules-25` S38, at `tools/memory-tree/design_lib.py:540`.
- Every receipt reader in `govkit.py` spells `.get("kits") or []` (`:967`, `:1001`, `:4317`, `:5425`).
- `python -c "import tomllib; tomllib.loads('﻿a = 1')"` raises `Invalid statement (at line 1,
  column 1)` (run 2026-10-23); `read_policy_text` strips one U+FEFF
  (`tools/policy/policy.py:478-488`), and `parse_policy` (`:490-501`) does not.
- `extract_files_touched`'s docstring keeps `None` for a spec with no sub-head apart from a sub-head
  declaring nothing (`tools/check-spec-tokens.py:535-557`).
- `cmd_check` fails a receipt row missing from disk with `'<path>' is in the receipt and not on
  disk` (`tools/govkit/govkit.py:5471-5477`).
- `check_mirror_render` (`tools/policy/guard.py:99-127`) compares the policy file, the catalogue and
  each key of the staged mirror's `legacy_blobs`, and refuses at `:120` with the sentence S19
  quotes; `help/policy.md:172-175` quotes it and names the first three inputs. `legacy_blobs` holds
  `LEGACY_INPUTS` (`tools/policy/policy.py:783`), today `.agent-cap.conf` alone.
- `tools/check-agent-cap-restatement.sh:90-102` declares `BOUND`, `NOUN` and the three shapes.
- `tools/govkit/matrix.py:71` declares `SCRATCH_KITS` and `:829` runs its `apply`.

### The fresh-target builder after S16, S18 and S20

```text
build_install_target(name, ids) -> (t, s):
    s = build_source_snapshot(the tree under test)
    answers = the [answers] table of DEPLOY_FULL in s/<tool root>/govkit/selftest.py,
              else RuntimeError naming that file
    t = git init; core.autocrlf=false; README.md; .governance/deploy.toml with
        gov_source = s, prefix, kits = ids, then answers
    commit once, through run_fixture_git and its -c identity
    return t, s

run_fresh_target, after its apply exits 0:
    rc, out = run_govkit(s, source_top, "check", "--target", t)
    WRONG for each "is in the receipt and not on disk" line of out
```

### The build order after S9 and S13

```python
def derive_parallel_step(units):
    if len(units) < 2:
        return "no"
    if any(u["writes"] is None for u in units):
        return "unknown"
    for a, b in pairs(units):
        if b["id"] in a["consumes"] or a["id"] in b["consumes"]:
            return "no"
        if check_writes_intersect([w for w in a["writes"] if pathlike(w)],
                                  [w for w in b["writes"] if pathlike(w)]):
            return "no"
    return "yes"
```

`pairs` is `itertools.combinations(units, 2)`, so no helper is minted for it; `pathlike` stays the
nested function it is at HEAD.

### Per-item changes, by file

| File | Items |
|---|---|
| `tools/policy/check_policy.py` | S3, S4, S10, S11, S12, S16, S18, and S20 only if its probe finds a deployer commit |
| `tools/policy/policy.py`, `tools/policy/guard.py` | S12 |
| `tools/gate-legs.json` | S10 |
| `memory/guides/SESSION-KICKOFF.md` | S10, its audit re-stamped |
| `tools/govkit/govkit.py` | S8 |
| `tools/memory-tree/design_lib.py`, `tools/memory-tree/gen_build_index.py`, `tools/check-spec-tokens.py` | S9, S13, S17 |
| `tools/check-spec-tokens.test.sh` | S9 |
| `help/policy.md` | S19 |
| `memory/builds/dGroundRules/README.md` | S1, S2, S6, S7, by re-render |
| the eight build READMEs S13 names | S13, by re-render |
| the codebase map | S9, S12, S16, S17, by regeneration |

S1, S2, S5, S6, S7, S14, S15 and S19 change no code of their own (S19 writes the help page only); each is the observation this unit owes
for a defect in a criterion or a stated outcome, made against the code S9 and `TOOL-dGroundRules-25`
build.

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `read_shipped_descriptors` | py.function | `tools/govkit/govkit.py` |
| `derive_bomless_text` | py.function | `tools/policy/policy.py` |
| `check_writes_intersect`, `read_spec_edges` | py.function | `tools/memory-tree/design_lib.py` |
| `invalid` | an answer of `derive_census_tree` | `tools/policy/check_policy.py` |
| `unknown` | a Parallel value of `render_order` | `tools/memory-tree/gen_build_index.py` |

`lexicon.py --suggest` answered OK for `read_shipped_descriptors`, `check_writes_intersect` and
`read_spec_edges` under `py.function` on 2026-10-23, and for `derive_bomless_text` on 2026-10-24
(`strip_bom` was refused for `extract`, which names a shape taken, not one left). `derive_dir_segments`, `check_dir_shaped` and
`check_guard_trips` move and are not minted; `build_install_target` is extended, not minted.

### Files touched (estimate)

- `tools/policy/check_policy.py`
- `tools/policy/policy.py`
- `tools/policy/guard.py`
- `tools/gate-legs.json`
- `tools/govkit/govkit.py`
- `tools/memory-tree/design_lib.py`
- `tools/memory-tree/gen_build_index.py`
- `tools/check-spec-tokens.py`
- `tools/check-spec-tokens.test.sh`
- `help/policy.md`
- `memory/guides/SESSION-KICKOFF.md`
- `memory/builds/dGroundRules/README.md`
- `memory/builds/aBlindedTrial/README.md`
- `memory/builds/aBoundedCeiling/README.md`
- `memory/builds/aBriskPreflight/README.md`
- `memory/builds/aTunedCompass/README.md`
- `memory/builds/dDerivedDocket/README.md`
- `memory/builds/dGaugedVintage/README.md`
- `memory/builds/dRetiredFork/README.md`
- `memory/builds/dTieredTribunal/README.md`
- `memory/map/generated/symbols.json`
- `memory/map/generated/inventories.json`
- `memory/map/generated/MAP.md`

The eight build READMEs after this build's own are those S13's re-render moves to `unknown`, each
in its generated build-order region, written by `gen_build_index.py --write` in this commit; S9's
kept `pathlike` filter changes no other README. `memory/guides/SESSION-KICKOFF.md` changes only in
its audit block, re-stamped because S10 writes `tools/gate-legs.json`, a path its `watch:` line names.

### Alternatives rejected

- **Two batch units, the build-order half and the policy half.** Both regenerate
  `memory/map/generated/symbols.json`, so M6's first clause fails.
- **The fresh-target case moved into `tools/govkit/matrix.py`.** Its per-arm adopter reading is
  `TOOL-dGroundRules-16`'s and is observed by `check_policy.py --fixture` criteria a move would
  orphan, and `matrix.py` applies from its own checkout's HEAD, the defect `TOOL-dGroundRules-26`
  closes. `build_install_target`, the one builder in `check_policy.py`, takes its place.
- **A second builder, `build_fresh_target`, beside `build_install_target`.** The three cases
  already share `build_install_target`; a second would be the copy the reuse rule refuses.
- **`apply`, or `apply` and `check`, inside `build_install_target`.** `legacy-homes-withheld-install`
  runs `plan` over the built target before its `apply`, so the builder would need a switch to stop
  short, and `check` serves only the fresh-target case's receipt compare.
- **A `--writes` flag on `govkit.py shipped`.** A public option on a product verb; S8's function
  answers the join in process.

## 5. Production-readiness checklist

- security — S11 refuses a receipt `prefix` that climbs out of the target; no item widens a write
  surface beyond what `TOOL-dGroundRules-22` to `TOOL-dGroundRules-25` priced.
- perf / scale — S18 adds one `govkit.py check` to the fresh-target case; S3 and S10 read the registry
  and three descriptors per run of `fixtures-guard-census`.
- error / empty / loading states — S8, S11 and S13 each give a state that read as a pass, a silence
  or a false `yes` its own outcome.
- observability — each new `WRONG`, finding and `unknown` names its path, field, entry or unit.
- risks — S9 moves three functions a shipped kit now owns; `check-spec-tokens.py` loads them by path
  as it loads the rest of `design_lib`.
- testing — the cases under `--fixture`, the arm in `tools/check-spec-tokens.test.sh`, and AC1 to
  AC20.
- migration — the codebase map and the build-order regions regenerated in this unit's commit.
- user docs — `help/policy.md` (S19).

## 6. Acceptance criteria

Every command runs from the repository root. The criteria spell the policy kit's files by bare name,
`policy.py`, `check_policy.py`, `guard.py`, `kit.toml` and `README.md` under the kit, as
`TOOL-dGroundRules-5` §6 does. Each `--fixture <case>` runs `python check_policy.py --fixture <case>`
and passes when it prints no `WRONG`. Let `ORDER_ROWS` stand for
`awk '/<!-- gen:build-order -->/,/<!-- \/gen:build-order -->/' memory/builds/dGroundRules/README.md | grep -E '^\| [0-9]+ \|'`.

- **AC1** — When `ORDER_ROWS` runs on the built tree, the row for step 3 ends `| no |`.
  Red when: a step whose units share a write is told it may run concurrently.
- **AC2** — When `ORDER_ROWS` runs, the row for step 7 ends `| no |`.
  Red when: units 21, 22 and 23 read as one parallel group.
- **AC3** — The descriptor lines are already in the guard (`TOOL-dGroundRules-23`); this criterion
  observes the derivation. When `--fixture fixtures-guard-census` runs on the built tree, it prints a
  line naming `tools/memory-tree/kit.toml` and no `WRONG`; with the guard line for
  `tools/memory-tree/kit.toml`, spelled under `{prefix}`, staged out of the `policy fixtures` guard
  in a scratch copy of the manifest, it prints `WRONG` naming that descriptor.
  Red when: a census kit's descriptor can leave the guard unseen, or is graded from a list typed
  beside the registry.
- **AC4** — When `requires` in a scratch copy of the policy kit's `kit.toml` is staged to name
  `agent-cap` and `--fixture adopter-fresh-target` runs there, it reports `apply` exiting 0 and the
  receipt's `agent-cap.js` row.
  Red when: the install is refused for an answer the closure needs.
- **AC5** — When `--fixture legacy-homes-withheld-install` runs, it passes; with the list's rule
  staged to `engine` in a scratch copy of the policy kit's `kit.toml`, it prints `WRONG`.
  Red when: the plan matcher matches nothing and both halves pass.
- **AC6** — When `ORDER_ROWS` runs, it prints exactly one row per step and no row of the roster
  table.
  Red when: the observation reads roster rows that can never end `| no |`.
- **AC7** — When `ORDER_ROWS` runs, the rows for steps 1 to 16 and 20 each end `| no |`, and the
  rows for steps 17 and 18 each end `| yes |`.
  Red when: the stated outcome claims a step the rule leaves parallel, or the rule serializes a step
  with no meeting write sets and no consumes-from edge inside it.
  figure: PINNED — the step membership and each unit's `check_policy.py` declaration read on
  2026-10-24; in steps 17 and 18 no two units' write sets meet and no unit consumes from another.
- **AC8** — When one registry entry's descriptor is staged missing in a scratch copy and
  `--fixture budgets-ships-join` runs there, it prints `WRONG` naming that entry; and
  `python tools/govkit/govkit.py shipped` there exits 1 printing no row; and on the built tree
  `grep -cw read_descriptors check_policy.py` prints `0` and `grep -c read_shipped_descriptors check_policy.py`
  prints 1 or more.
  Red when: the join grades a narrowed registry as the whole one, or reads the registry through a
  copy of `cmd_shipped`'s read.
- **AC9** — When a `python -c` probe calls `check_writes_intersect` on `["tools/policy/"]` against
  `x.py"]` and on `a.py"]` against `ab.py"]`, it answers `True` then
  `False`, the answers `overlaps` gives for the same pairs; and
  `grep -c "def check_guard_trips" tools/check-spec-tokens.py` prints `0`.
  Red when: the render and the dispatcher hold two overlap rules.
- **AC10** — When `python tools/check-spec-tokens.py --legs-for tools/memory-tree/kit.toml tools/memory-tree/adopt-memory-tree.sh`
  runs, it names `policy fixtures` for each path; with `adopt-memory-tree.sh` staged out of the guard
  in a scratch copy, `--fixture fixtures-guard-census` prints `WRONG` naming it.
  Red when: an edit to a closure kit's descriptor or adopter skips the leg its install runs in.
- **AC11** — When a case target's receipt holds `{"prefix":"tools"}` and
  `python check_policy.py --repo <t>` runs, `arm_cap_census` prints one finding naming the receipt
  and `kits`; with `{"kits":["policy"],"prefix":"../x"}`, the finding names `prefix`.
  Red when: a receipt of the wrong shape reads as an adopter that installed nothing.
- **AC12** — When `--fixture on-invalid-bom` runs, `guard.py --staged` admits the staged raise over
  the BOM-led file, `arm_schema` reports no parse failure for it, and
  `policy.py get budgets.enforce --explain` prints the file's own value. On the built tree,
  `grep -n derive_bomless_text policy.py check_policy.py` prints its `def` line and one call each
  inside `parse_policy`, `validate` and `arm_schema`; `grep -c derive_bomless_text guard.py` prints
  `1`, the comment above the guard's inline strip in `check_raise_shape`; and
  `grep -nE "^\s*(import|from)\s+policy\b" guard.py` still prints nothing.
  Red when: a reader of the policy file or the guard still rejects a leading BOM, the readers strip
  it in more than one place, or the guard reads the file through a policy reader.
- **AC13** — When a `python -c` probe calls `derive_parallel_step` on two unit records, one of them
  with `writes` set to `None`, it answers `unknown`.
  Red when: an unknown write set renders as a disjoint one.
- **AC14** — When `derive_census_tree`'s entry is removed from a scratch copy's
  `memory/map/generated/symbols.json` and `python tools/codebase-map/gen_map.py --check` runs in that
  copy, it exits non-zero naming `derive_census_tree`.
  Red when: the map can lose a function this build added unseen.
  cost: one copy of the repository.
- **AC15** — When `bash tools/check-agent-cap-restatement.sh` runs on the built tree, it names no
  line of `memory/map/features/agent-cap.md`; in a scratch clone whose card carries
  `at most 5 agents`, it exits non-zero naming the card.
  Red when: the card restates a bound in a shape the criterion's own command cannot see.
- **AC16** — When `build_install_target` is staged in a scratch copy to raise at its first line,
  `--fixture adopter-fresh-target`, `--fixture legacy-homes-withheld-install` and
  `--fixture census-default-adopter` each print `WRONG`; with `manifest_path` staged out of
  `DEPLOY_FULL` in a scratch copy, `--fixture census-default-adopter` prints `WRONG` naming
  `manifest_path`; and `grep -c KICKOFF_ANSWERS check_policy.py` prints `0`.
  Red when: a case keeps its own install-into-a-target code, or its answers are typed beside the
  deployer's own fixture.
- **AC17** — When the backticked-target branch of `read_spec_edges` is staged out in a scratch copy
  and `python tools/check-spec-tokens.py --list` runs there, its `hands-off join` line reports more
  silent bullets than on the unchanged tree.
  Red when: the hands-off join reads edges through a copy of the grammar of its own.
- **AC18** — When the fresh-target case's target has one engine row's file deleted after `apply` in
  a scratch copy, the case prints `WRONG` carrying `is in the receipt and not on disk` and no line
  carrying `absent from the target (missing)`.
  Red when: a receipt row missing from disk passes the case, or two checks grade that direction.
- **AC19** — When
  `awk '/^## Who may change the policy file/,/^## The keys the file holds today/' help/policy.md | grep -c legacy_blobs`
  runs, it prints 1 or more; and `grep -c "is staged changed: commit <path> first" help/policy.md`
  prints `1`.
  Red when: the help page names fewer inputs than the guard compares, or quotes a refusal the guard
  does not print.
- **AC20** — When a print of `git -C <t> rev-list --count HEAD` is staged right after the case's
  `apply` in a scratch copy and `--fixture adopter-fresh-target` runs there, it prints `1`; and when
  `--fixture adopter-fresh-target` runs with `GIT_CONFIG_GLOBAL` naming an empty file and
  `GIT_CONFIG_NOSYSTEM=1`, it prints no `WRONG`.
  Red when: the target's commit relies on an identity the runner may not have, or the deployer
  commits in the target unseen.

## 7. Gates

`run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `govkit acceptance matrix` · `govkit refusal join` · `govkit selftest` · `govkit selfcheck` · `build-index selftest` · `memory-hygiene self-test` · `spec-tokens self-test` · `tier2-review self-test` · `agent-cap restatement` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `memory hygiene` · `recall floor` · `recall floor arms` · `policy fixtures`

The policy legs `TOOL-dGroundRules-1` declares, `policy check` and `policy fixtures`, run the cases;
they are named by the arm lines, because neither exists at this spec's base.

New arm: tools/policy/check_policy.py --fixture · covers AC3 AC4 AC5 AC8 AC10 AC11 AC12 AC16 AC18 AC20 · each case named in S3 to S5, S8, S10 to S12, S16, S18 and S20, its stated input staged in its temporary repository or scratch copy · none
New arm: tools/check-spec-tokens.test.sh · covers AC9 · `check_writes_intersect` staged to test one direction only, against `overlaps` on the directory and file pair · that suite's assertion count, raised by the arm
New arm: tools/memory-tree/gen_build_index.py (`--selftest`) · covers AC13 · a fixture step holding a unit with no Files touched sub-head · none

## 8. Open questions

- **F1 — What does the render print for a step holding a unit whose write set is unknown (finding
  28)?** (a) `unknown`. (b) `no`. Both meet AC13's red condition; (a) also tells a reader why the
  step is not known to be parallel, where (b) reads like a measured intersection, and no tool reads
  the column, so the extra value breaks no reader. Recommendation (a). Rung 3.
  RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none
- **F2 — How does the guard's refusal name an input other than the policy file or the catalogue
  (finding 22)?** (a) `TOOL-dGroundRules-19` S3's sentence kept, the input appended as
  ` · staged input <path>`. (b) The sentence re-worded to `commit <input> first`. (b) changes
  `TOOL-dGroundRules-19` AC2's observed text, a fold BUILD-METHOD M4 refuses (veto 1). (a) meets every
  criterion and changes no other unit's case. Recommendation (a). Rung 3.
  RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none
  Overtaken at rev-6: the sentence `check_mirror_render` prints at HEAD already names the input, so
  S19 keeps it as printed and appends nothing (§9).
- **F3 — How does the census-ships join keep `cmd_shipped`'s refusal (finding 13)?** (a) A function
  factored out of `cmd_shipped` that raises on a non-empty `Report`, called in process. (b) A
  `--writes` flag on `govkit.py shipped` printing the destination, run as a subprocess. (b) adds a
  public option to a product verb (veto 2). Recommendation (a). Rung 3.
  RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting the thirteen MEDIUM and seven LOW findings of the
  round-1 spec audit of units 22 to 25 in one batch, from the review's sound fixes and the skeptic's
  corrected fix for id 12, with each cited line read at base `3708a705`.
- rev-2 · 2026-10-23 · §3 · the **hands-off** edges to TOOL-dGroundRules-33, TOOL-dGroundRules-34 added, each the reciprocal of that unit's **consumes-from** line: the promotions of the round-1 spec audit of units 26 to 32 that build on this unit. No scope, design or acceptance moved here; the repair is the promoted unit's.
- rev-3 · 2026-10-23 · §3 · the hands-off edge to `TOOL-dGroundRules-52`, the reciprocal ends the disposal of
  the round-1 spec audit of units 35 to 43 wrote; no scope or criterion moved.
- rev-4 · 2026-10-24 · §6 · AC11: a criterion code span rejoined onto one line so hygiene check 23 reads the criterion's tokens; no meaning change.
- rev-5 · 2026-10-24 · §7 · the policy fixtures leg added to the leg line, owed by its guard, which a §4 path trips; no design change.
- rev-6 · 2026-10-24 · §2 §3 §4 §6 §8 §10 · the builder's divergence at `93e4b4d31`, ruled by the run. Disagreements: S7/AC7 claimed every step serial, and steps 17 and 18 render `yes`; S16 minted `build_fresh_target` beside `build_install_target`, the builder three cases share, with `KICKOFF_ANSWERS` typed in it; S20 asked for an identity `run_fixture_git` already passes; S19 kept a refusal sentence the guard no longer prints; S9 left the `pathlike` filter unsaid; S13 named no README; S5 already held. Rulings: S7/AC7 limited to the steps holding a `check_policy.py` pair, 17 and 18 pinned `yes`; S16 extends `build_install_target(name, ids)` with `DEPLOY_FULL`'s answers, neither `apply` nor `check` moving in, and S4 and S18 restated on it; S20 met unless AC20's probe finds a deployer commit; S19 keeps the HEAD sentence and appends the `legacy_blobs` keys to the help page; S9 keeps `pathlike`; S13 and §4 name the eight READMEs; S5 restated as holding; every moved citation re-read by symbol.
- rev-7 · 2026-10-24 · §2 §4 §6 §9 §10 · the builder's second divergence at `3e16f3efe`, ruled by the run. Disagreements: S12/AC12 routed the guard's parse through `parse_policy`, which the reader-free guard cannot import under `TOOL-dGroundRules-6` AC10, ran a `--check` the guard does not accept, and left `validate` and `arm_schema`'s nested parse unstripped; S3 had the guard gain descriptor lines unit 23 already wrote; S8 asked for a `WRONG` that already fires; AC9's spans are the pair fragments `TOOL-dGroundRules-34` S15 restates whole; §4 lacked `memory/guides/SESSION-KICKOFF.md`; S16's `DEPLOY_FULL` answers were not probed against `apply`. Rulings: one helper, `derive_bomless_text`, called by `parse_policy`, `validate` and `arm_schema`, the guard stripping inline under a comment naming it, `on-invalid-bom` running `guard.py --staged` only; S3/AC3 keep only the run-time derivation and its `WRONG`; S8 keeps only the `read_shipped_descriptors` refactor, AC8 observing it; AC9 kept, S9 naming the whole spellings; §4 adds the manifest; S16 probes the answers first and hands back a divergence on refusal.

## 10. Reuse audit

Each item extends a seam already named in its row: `fixtures-guard-census` and the `policy fixtures`
guard (S3, S10), `DEPLOY_FULL` in `tools/govkit/selftest.py` (S4, S16), `run_fixture_git`'s
identity (S20), `PLAN_LINE`, already matching the plan printer's own format (S5), `cmd_shipped`, the one derivation of what gov ships (S8), the trip rule
`check_guard_trips` that `--legs-for` already uses (S9), `scan_handoffs` and check 12's Edges grammar
(S17), `govkit.py check`'s receipt-integrity arm (S18), and `build_install_target`, the one builder
`TOOL-dGroundRules-25` left, with `TOOL-dGroundRules-26` and `TOOL-dGroundRules-27`'s snapshot and
helper (S16). S12's `derive_bomless_text` sits beside `parse_policy`, the policy kit's one reader;
the other U+FEFF handling a grep for `ufeff` finds under `tools/` lives in other copy-installed kits,
which carry their primitives inline, so no shared seam fits, and the guard mirrors the helper inline
because it imports no reader. `python tools/codebase-map/reuse_lookup.py "install a kit into a scratch target with the deployer and read its receipt"`
ranked `read`, `read_text`, `scratch`, `kit_rel` and `resolve_kit_dir` among name-stem hits; the
others were found by reading the files the review cites, each verified at base. `tools/govkit/matrix.py`
was weighed for S16 and rejected (§4). The recall probe returned the prior minors batch
`TOOL-dGroundRules-25`, whose one-item-per-finding table this unit follows, and this audit's own items.

Recall terms used: `python tools/memory-recall/query.py "how are review minors batched into one
repair unit" --terms "minors batch promoted medium low disposed severity spec-audit repair unit write
set"`
