# TOOL-dGroundRules-25 — the round-1 audit of units 13 to 21, its minors: thirty-nine findings closed in the code those units leave, one scope item each

**Status:** CLOSED · rev-10 · 2026-10-24 · node d · Tier-2 · base 3708a705 · streams tooling · order 8 · advances TOOL-dGroundRules-12

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-25-deviation-13.md](../build/2026-10-23-build-TOOL-dGroundRules-25-deviation-13.md) | deviation | — |
| [2026-10-23-build-TOOL-dGroundRules-25-deviation-59.md](../build/2026-10-23-build-TOOL-dGroundRules-25-deviation-59.md) | deviation | — |
| [2026-10-23-build-TOOL-dGroundRules-25-ledger.md](../build/2026-10-23-build-TOOL-dGroundRules-25-ledger.md) | journal | — |
| [2026-10-24-build-TOOL-dGroundRules-25-deviation-76.md](../build/2026-10-24-build-TOOL-dGroundRules-25-deviation-76.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dGroundRules-21-trim-task.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-21-trim-task.md) | research | TOOL-dGroundRules-21 TOOL-dGroundRules-34 TOOL-dGroundRules-64 |
| [2026-10-23-prompt-TOOL-dGroundRules-25-build-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-25-build-brief.md) | journal | — |
| [2026-10-24-prompt-TOOL-dGroundRules-25-1-spec-writer.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-25-1-spec-writer.md) | journal | — |
| [2026-10-24-prompt-TOOL-dGroundRules-25-2-spec-writer.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-25-2-spec-writer.md) | journal | — |
| [2026-10-24-prompt-TOOL-dGroundRules-25-3-spec-writer.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-25-3-spec-writer.md) | journal | — |
| [2026-10-24-prompt-TOOL-dGroundRules-25-divergence-brief.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-25-divergence-brief.md) | research | — |
| [2026-10-24-prompt-TOOL-dGroundRules-25-guards-brief.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-25-guards-brief.md) | research | — |
| [2026-10-24-prompt-TOOL-dGroundRules-25-size-trim-brief.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-25-size-trim-brief.md) | research | — |
| [2026-10-24-prompt-TOOL-dGroundRules-25-span-spec-writer.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-25-span-spec-writer.md) | journal | — |
| [2026-10-25-prompt-TOOL-dGroundRules-21-close-arms-brief.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-21-close-arms-brief.md) | research | TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-29 TOOL-dGroundRules-31 |
| [2026-10-25-prompt-TOOL-dGroundRules-25-arm-breaks-1-researcher.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-25-arm-breaks-1-researcher.md) | journal | — |
| [2026-10-25-prompt-TOOL-dGroundRules-25-arm-breaks-brief.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-25-arm-breaks-brief.md) | research | TOOL-dGroundRules-10 TOOL-dGroundRules-21 |
| [2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-65 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-51 TOOL-dGroundRules-52 |
| [2026-10-23-review-TOOL-dGroundRules-22-25-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-22-25-spec-audit-round1.md) | spec-audit | TOOL-dGroundRules-24 TOOL-dGroundRules-22 TOOL-dGroundRules-23 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 13 to 21
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-65-21-spec-audit-round1.md`)
exited CONVERGED with 42 findings. Its three HIGHs are `TOOL-dGroundRules-22` to
`TOOL-dGroundRules-24`; BUILD-METHOD M4 batches the other thirty-nine, twenty-eight MEDIUM and
eleven LOW, here. They land on units 13 to 22 and 24, mostly in the policy kit or
`tools/gate-legs.json`, so M6 yields no disjoint write sets (§4). A finding the review merged into
another's item keeps its own scope item.

| Finding id | Severity | Review item | Unit it lands on | Scope item | Criterion |
|---|---|---|---|---|---|
| 39 | MEDIUM | M19 | 13 | S1 | AC1 |
| 18 | MEDIUM | M9 | 14 | S2 | AC2 |
| 12 | MEDIUM | M8 | 14 | S3 | AC3 |
| 30 | MEDIUM | M8 | 14 | S4 | AC4 |
| 36 | MEDIUM | M18 | 16, 24 | S5 | AC5 |
| 15 | LOW | L4 | 16, 24 | S6 | AC6 |
| 23 | MEDIUM | M12 | 16, 24, 21 | S7 | AC7 |
| 9 | LOW | L2 | 16, 21 | S8 | AC8 |
| 3 | MEDIUM | M3 | 17 | S9 | AC9 |
| 11 | MEDIUM | M3 | 17 | S10 | AC10 |
| 37 | MEDIUM | M3 | 17, 22 | S11 | AC11 |
| 4 | MEDIUM | M4 | 17, 22 | S12 | AC12 |
| 33 | LOW | L9 | 17, 20 | S13 | AC13 |
| 27 | MEDIUM | M14 | 18 | S14 | AC14 |
| 8 | LOW | L1 | 18 | S15 | AC15 |
| 14 | LOW | L3 | 18 | S16 | AC16 |
| 35 | LOW | L11 | 18, 21 | S17 | AC17 |
| 44 | MEDIUM | M23 | 18 | S18 | AC18 |
| 7 | MEDIUM | M7 | 19 | S19 | AC19 |
| 25 | MEDIUM | M7 | 19, 21 | S20 | AC20 |
| 42 | MEDIUM | M7 | 19 | S21 | AC21 |
| 24 | MEDIUM | M13 | 19 | S22 | AC22 |
| 20 | MEDIUM | M10 | 20 | S23 | AC23 |
| 41 | MEDIUM | M21 | 20 | S24 | AC24 |
| 19 | LOW | L6 | 20 | S25 | AC25 |
| 5 | MEDIUM | M5 | 21 | S26 | AC26 |
| 6 | MEDIUM | M6 | 21 | S27 | AC27 |
| 21 | MEDIUM | M11 | 21 | S28 | AC28 |
| 32 | MEDIUM | M17 | 21 | S29 | AC29 |
| 43 | MEDIUM | M22 | 21 | S30 | AC30 |
| 16 | LOW | L5 | 21 | S31 | AC31 |
| 40 | MEDIUM | M20 | 21 | S32 | AC32 |
| 22 | LOW | L7 | 21 | S33 | AC33 |
| 28 | MEDIUM | M15 | 21 | S34 | AC34 |
| 29 | MEDIUM | M16 | 21 | S35 | AC35 |
| 34 | LOW | L10 | 15 | S36 | AC36 |
| 26 | LOW | L8 | 13 to 20 | S37 | AC37 |
| 1 | MEDIUM | M1 | 14, 19 | S38 | AC38 |
| 2 | MEDIUM | M2 | 15, 17, 18, 20 | S39 | AC39 |

Each fix is the one the review's skeptic judged sound, its corrected fix for ids 2, 22, 23, 26 and
35; where the review offered options, §8 records the pick.

## 2. Scope (IN)

- **S1** — Finding 39. `mirror-commit-rewrite` (`TOOL-dGroundRules-65` S5) runs its render, commit
  and `git commit-tree` rewrite once per reason kind: a policy file setting the key, a file present
  without it, the file absent, and an invalid file over a valid ancestor, the `last-valid` kind. Each
  asserts `mirror --check` exits 0 at the carrying commit and at its rewrite, and a failure names the
  kind. Observed by AC1.
- **S2** — Finding 18. An arm in `tools/push-main.test.sh` beside arms 28 to 32, built on
  `build_regen_fixture` (`tools/push-main.test.sh:934-946`): it commits a `.governance/policy.toml`
  change on `feat`, runs the real `--prepare`, then the clone's `regen.py --check` and
  `policy.py mirror --check` at the prepared HEAD, each expected to exit 0. It says `skip` with its
  reason where no policy kit sits beside the lander, as arms 28 to 32 do without `regen.py`
  (`:1046`). `mirror-landed-merge` stays as the policy leg's replay of the render. Observed by AC2.
- **S3** — Finding 12. The arm spells the lander as arm 28 does,
  `bash "$lander" --prepare --slug tPolicy`, on the non-default branch `feat` with a clean tree, its
  clones under the suite's own `$tmp`. Observed by AC3.
- **S4** — Finding 30. The arm asserts `--prepare` exited 0, printed `push-main: prepared` and left
  `git rev-parse HEAD^2` resolving, before it reads either check; a refused `--prepare` is a `bad`
  naming its exit status, never a regen verdict. Observed by AC4.
- **S5** — Finding 36. `adopter-fresh-target`, as `TOOL-dGroundRules-24` installs it, asserts that
  `legacy-homes.txt` is absent from the installed policy kit and that both `--check` runs print the
  `legacy-homes` announce line `not graded · the list is gov's own`. Observed by AC5.
- **S6** — Finding 15. The case's selection is `policy` and the closure of `requires` read as
  registry ids and passed to `--kits`, never resolved through `resolve_kit_dir` as homes.
  Observed by AC6.
- **S7** — Finding 23, the skeptic's corrected fix. `adopt-policy.sh --scaffold` runs
  `policy.py mirror --write` whenever HEAD resolves, as `TOOL-dGroundRules-21` S37 runs the settings
  render. `adopter-fresh-target` selects `run-gates` too. After the install's first commit it
  re-runs the installed `adopt-memory-tree.sh --scaffold`, found through its receipt row, whose
  `apply` run seeded the conf and stopped (`tools/memory-tree/kit.toml:145`), so its render check
  and `gen_build_index --check` are fresh; then it re-runs the policy adopter's `--scaffold`,
  commits the mirror, and runs the installed `regen.py --check`, expecting exit 0. On install day
  `mirror --write` refuses `uncommitted changes` (`tools/policy/policy.py:1305`), the scaffold
  having just written the policy file, until `TOOL-dGroundRules-31` lands its deferral:
  `adopter-fresh-target`, `limit-fresh-target-spawn` and `adopter-suite` (arm 4 of
  `adopt-policy.test.sh`) read red on this unit's commit and go green at `TOOL-dGroundRules-31`.
  Folding that deferral in here is refused: it is that unit's whole scope, its spec audited.
  Observed by AC7.
- **S8** — Finding 9. The join of `TOOL-dGroundRules-16` S3 also reads the leading token of the
  table's last column, `announce` or `finding`, and asserts it equals each `ARMS` entry's `empty`
  value (`TOOL-dGroundRules-21` S5). Observed by AC8.
- **S9** — Finding 3. The case `legacy-homes-withheld-install` builds a target as
  `TOOL-dGroundRules-24` S1 does, runs `govkit.py plan` and asserts that `legacy-homes.txt` is an
  `ORDER [project-owned]` row and neither a write nor a `SIDE` row, then runs `apply` and asserts no
  such file in the target. Observed by AC9.
- **S10** — Finding 11. The kit README's "Each arm in an adopter" row for `legacy-homes`, and the
  arm's announce line, say that the plan's `ORDER [project-owned]` row for the list is informational
  and that an adopter does not author the file. Observed by AC10.
- **S11** — Finding 37. The `legacy-homes` arm announces and grades nothing whenever
  `derive_census_tree` (`TOOL-dGroundRules-22` S2) answers `adopter`, a list at its kit directory
  included, so an adopter-authored list is never graded against gov's rows. Observed by AC11.
- **S12** — Finding 4. The case `census-default-adopter` installs `policy`, its requires closure and
  `kickoff-manifest` into a fresh target through `apply`, without `check-line-length`, its
  descriptor carrying the `[answers]` those entries ask for, `manifest_path` among them, and asserts
  that `arm_cap_census` announces `kit check-line-length not installed`, grades the manifest rows at
  the receipt's `manifest-check.sh` destination, and reports no finding. Observed by AC12.
- **S13** — Finding 33. `budgets-ships-join` and `fixtures-guard-census` locate the registry and
  `gate-legs.json` from the kit's own resolved tool root, never as a literal kit segment, and §7
  here carries `install-prefix (shipped surface)` and
  `foreign-prefix parity (every self-test at three prefixes)`. Observed by AC13.
- **S14** — Finding 27. "The predicate" in `tools/workflows/REVIEW-PROTOCOL.template.md` gains the
  writer receiver: an identifier assigned once on a line carrying `// gov:fixed-writers` whose
  split's K resolves to at most `runtime.agents-in-flight`, as `TOOL-dGroundRules-18` S1 admits it;
  the dogfood copy is rendered from it, and `review-protocol parity (kit vs dogfood)` is on §7.
  Observed by AC14.
- **S15** — Finding 8. `memory/guides/REVIEW-PROTOCOL.md` carries that receiver line inside "The
  predicate", before "Everything else is denied". Observed by AC15.
- **S16** — Finding 14. The rule-2 paragraph of `tools/hooks/README.md` keeps exactly one
  "cannot resolve to an integer ≤N" spelling, for the verifier bound, and states the writer bound in
  other words; `playbook parity` and `playbook parity selftest` are on §7. Observed by AC16.
- **S17** — Finding 35, the skeptic's corrected fix. The map card `memory/map/features/agent-cap.md`
  names the two bounds by their carriers, `MAX_VERIFIERS` and `runtime.agents-in-flight`, with no
  digit; the hooks README keeps the one digit the parity row extracts, in a shape
  `check-agent-cap-restatement.sh` does not match; `agent-cap restatement` is on §7.
  Observed by AC17.
- **S18** — Finding 44. The workflows render in `tools/workflows/check-protocol-parity.test.sh`
  reads the resolved agent-cap hook's `KIT_AGENT_CAP_VERSION` before it renders
  `unattended-build.js`. Below the version `TOOL-dGroundRules-18` ships, it renders the spec-writer
  split under `// gov:fixed-verifiers` with `Math.min(SPEC_WRITERS, 5)` and prints one stderr line
  naming `govkit update --kits agent-cap`, as its playbook-render floor does
  (`tools/workflows/check-protocol-parity.test.sh:337`). Observed by AC18.
- **S19** — Finding 7. The guard's mirror shape (`TOOL-dGroundRules-19` S1) reads its input set from
  the staged mirror's own record: the policy file, the kit's `catalogue.toml` and every key of
  `legacy_blobs`. A staged change to any of them refuses the mirror, the line naming that input.
  The case `guard-mirror-beside-conf` stages `.agent-cap.conf` with a mirror rendered at HEAD.
  Observed by AC19.
- **S20** — Finding 25. `policy.py mirror --write` and `--check` refuse a working-tree difference
  from HEAD over that same recorded set, so an uncommitted `.agent-cap.conf` edit is refused as an
  uncommitted policy-file edit is (`TOOL-dGroundRules-5` §4 "The verb"). Observed by AC20.
- **S21** — Finding 42. The case `guard-mirror-inputs-join` stages the render to record one more
  input than today and stages that input beside the mirror; the guard refuses naming it, so a
  recorded input the guard does not compare cannot exist. Observed by AC21.
- **S22** — Finding 24. `mirror --print` writes `render_mirror`'s bytes through `sys.stdout.buffer`,
  and the guard reads the subprocess's stdout as bytes and compares it with the staged blob as
  bytes. Observed by AC22.
- **S23** — Finding 20. The `policy fixtures` guard in `tools/gate-legs.json` gains
  `{prefix}/gate-legs.json`, the file `fixtures-guard-census` reads. Observed by AC23.
- **S24** — Finding 41. The same guard gains each in-kit module a Python census enforcer imports and
  each in-kit file a shell enforcer sources, derived from the census at build, and
  `fixtures-guard-census` walks the same imports and sourced files and reds one the guard does not
  cover. Its guards hit on another build's live spec is held by a waiver row and a deviation
  record (§4 "The guard's reach into another build's live spec", §8 F7). Observed by AC24.
- **S25** — Finding 19. `fixtures-guard-census` pipes every path it holds to
  `python <source tool root>/check-spec-tokens.py --legs-for -` and reds a path whose output does
  not name `policy fixtures`; it spells no guard-match rule of its own. An unreachable checker is a
  `WRONG`, never a pass. Observed by AC25.
- **S26** — Finding 5. Every `ARMS` entry declares `empty` with its reason. `arm_limits_readers`
  and `arm_mirror_landed` declare `announce` for a population that needs a HEAD or an `L` that does
  not resolve, and every arm reading HEAD or `L` announces when that revision does not resolve. The
  case `arms-empty-declared` reds an `ARMS` entry staged with no `empty`. Observed by AC26.
- **S27** — Finding 6. The case `arms-empty-target` runs `--check` over a target with no policy file
  and no tracked code, where `arm_schema`, the reader-coverage arm and `arm_mirror_readers` announce;
  over the scaffolded fresh target it asserts `arm_schema` grades its four keys with no finding.
  Observed by AC27.
- **S28** — Finding 21. `resolve_bash` becomes a canonical block, `# >>> resolve_bash_py`, in a new
  `tools/lib/resolve_bash.py` holding `tools/run-gates/profile_bar.py:282`'s rule, inlined between
  its markers in `tools/policy/check_policy.py` and held by a `PARITY_ROWS` row of
  `tools/lib/resolve-python.test.sh`. The other copies stay the deferred ask `TOOL-dSettledRoster-6`'s.
  Observed by AC28.
- **S29** — Finding 32. `adopter-suite` (`TOOL-dGroundRules-21` S4) prints `WRONG` unless the suite
  exits 0 and its output names its arm count; a bash `resolve_bash` cannot find is `WRONG`, never a
  skip. Observed by AC29.
- **S30** — Finding 43. The reader strips one leading U+FEFF from a revision's policy text before it
  parses it, as unit 10's conf reader tolerates one. The case `on-invalid-bom` writes a valid file
  with a BOM. Observed by AC30.
- **S31** — Finding 16. `on-invalid-shallow` (`TOOL-dGroundRules-21` S13) clones with
  `git clone --depth 1 file:///<abs path>` and asserts `git rev-parse --is-shallow-repository`
  prints `true` before it reads the key. Observed by AC31.
- **S32** — Finding 40. The settings `[[generated]]` row in `tools/policy/kit.toml` passes
  `.claude/settings.json` in its argv; `GOV_SETTINGS_JSON` steers the render only when no file
  argument is given; a declared `GOV_SETTINGS_JSON` that is not a file refuses with exit 2, as
  `tools/check-wiring.sh:102-108` does; the kit README names the environment-steered write. The case
  `limit-settings-env-stale` runs `regen.py --check` with the variable set to a scratch file and the
  tracked settings stale. Observed by AC32.
- **S33** — Finding 22, the skeptic's corrected fix. `limit-settings-elsewhere` observes the atomic
  write by its effect: a hard link to the target settings file keeps the old bytes after
  `settings --write`, the target is a new inode, and no temporary file is left beside it.
  Observed by AC33.
- **S34** — Finding 28. The valid fixture of `tools/check-playbook-parity.test.sh:159-161` writes the
  hooks README line `TOOL-dGroundRules-21` S35 re-points the `resolved-K ceiling` row to and no
  `boundedParallel(thunks, 5)` line; the comment at `tools/check-playbook-parity.sh:257` and the
  test's "three of the bounds" comment name the bounds that remain. Observed by AC34.
- **S35** — Finding 29. `TOOL-dGroundRules-21` S31 added no hygiene branch: with no Python launcher
  `tools/memory-tree/check-memory-hygiene.sh` stops at its `resolve_python` line (`:492`) with exit
  2, no `fail` call or exit-1 site, so `check-arms.py --report` lists no branch for it. Its suite,
  `tools/memory-tree/check-memory-hygiene.test.sh`, gains an arm that runs it under a `PATH` holding
  no Python launcher and asserts exit 2 and the line `HYGIENE — no usable python` by its text.
  `tools/check-template-size.test.sh` gains an arm under such a `PATH` over an over-cap subject that
  asserts the `fail 5` refusal, a branch already armed: it adds an assertion and moves no
  `ARMS_FLOORS` row. Observed by AC35 and by the hygiene arm.
- **S36** — Finding 34. The codebase map is regenerated at this unit's commit with
  `python tools/codebase-map/gen_map.py --write`, so `derive_lowered_limit`
  (`TOOL-dGroundRules-15`) and `derive_census_tree` (`TOOL-dGroundRules-22`) sit in
  `memory/map/generated/symbols.json`. Observed by AC36.
- **S37** — Finding 26, the skeptic's corrected fix. `read_spec_writes(text)` in
  `tools/memory-tree/design_lib.py` returns every word inside backticks under a spec's
  `### Files touched` sub-head, or `None` when it has none; `extract_files_touched`
  (`tools/check-spec-tokens.py:536`) reads its tokens through it and keeps its own shape filter.
  `render_order` in `tools/memory-tree/gen_build_index.py` marks a step's Parallel column `no` when
  two of its units declare intersecting write sets, a path of two or more segments equal to, or
  under a directory token of, the other's. Observed by AC37.
- **S38** — Finding 1. `read_spec_consumes(text)` in `tools/memory-tree/design_lib.py` returns the
  targets of a spec's §3 `**consumes-from**` bullets under check 12's bullet grammar
  (`tools/memory-tree/check-memory-hygiene.sh:2553`), and `render_order` marks a step `no` when one
  of its units consumes from another of the same step. The two rules meet in
  `derive_parallel_step(units)`. Observed by AC38.
- **S39** — Finding 2, the skeptic's corrected fix. Every build README's build-order region is
  re-rendered with `gen_build_index.py --write` in this unit's commit, so this build's steps 4, 6 and
  7 read `no`. Observed by AC39.

## 3. Non-goals (OUT)

- Every HIGH: `TOOL-dGroundRules-22` to `TOOL-dGroundRules-24`.
- Rewriting any reviewed spec: each defect closes here in code and criteria (BUILD-METHOD M4).
- Renumbering any unit's `order`; the render says which steps are not parallel.
- The other `resolve_bash` copies: `TOOL-dSettledRoster-6` stays their ask.
- A hygiene arm that reds a `consumes-from` edge inside one step: twenty-one sit in landed and live
  specs across nine builds (2026-10-23), so the render reports the step instead.
- An adopter verb for the workflows kit, which ships no adopter (`tools/workflows/kit.toml:93-96`);
  S18's floor lives in its render.

### Edges

- **consumes-from** `TOOL-dGroundRules-65` — `mirror-commit-rewrite` and `rev_phrase` (S1)
- **consumes-from** `TOOL-dGroundRules-14` — `mirror-landed-merge` (S2 to S4)
- **consumes-from** `TOOL-dGroundRules-15` — `derive_lowered_limit` (S36)
- **consumes-from** `TOOL-dGroundRules-16` — `adopter-fresh-target`, its README table and join (S5 to S8)
- **consumes-from** `TOOL-dGroundRules-17` — the withheld legacy-home list, `budgets-ships-join` and the census arm (S9 to S13)
- **consumes-from** `TOOL-dGroundRules-18` — `WRITER_MARK`, the writer bound and the hooks README's rule 2 (S14 to S18)
- **consumes-from** `TOOL-dGroundRules-19` — the guard's mirror shape, `mirror --print` and the `guard-mirror-` cases (S19 to S22)
- **consumes-from** `TOOL-dGroundRules-20` — the `policy fixtures` guard and `fixtures-guard-census` (S23 to S25)
- **consumes-from** `TOOL-dGroundRules-21` — `ARMS`, `adopter-suite`, the settings render and `--scaffold`, which S7, S8 and S26 to S35 amend
- **consumes-from** `TOOL-dGroundRules-22` — `derive_census_tree` and the census's adopter grading (S11, S12, S36)
- **consumes-from** `TOOL-dGroundRules-24` — the deployer-installed fresh target (S5 to S7, S9, S12)
- **hands-off** `TOOL-dGroundRules-27` — `legacy-homes-withheld-install` and `census-default-adopter`, moved onto `run_govkit` (finding 7)
- **hands-off** `TOOL-dGroundRules-30` — S18's writer-marker floor and AC18, which its AC1 and AC2 observe (finding 18)
- **hands-off** `TOOL-dGroundRules-31` — S7's `mirror --write` refusal, which it defers, and AC7's second clause (finding 24)
- **hands-off** `TOOL-dGroundRules-32` — the build-order rule, census and plan cases, BOM strip, map regeneration, card criterion, edge read and widened refusal (findings 3, 9, 10, 19, 14, 25, 27, 28, 6, 11, 12, 15, 22)
- **hands-off** `TOOL-dGroundRules-33` — S25's pipe to `--legs-for -`, which its guard trace reuses (id 26 of the round-1 audit of units 26 to 32)
- **hands-off** `TOOL-dGroundRules-34` — AC18's version-staging arm, which it removes, and `census-default-adopter` (ids 1, 25 and 33 of the round-1 audit of units 26 to 32)

## 4. Design

### Evidence

Every line below was read at base `3708a705` on 2026-10-23, the two cited `:80` and `:536` at
`4298cfcc7`.

- `tools/push-main.test.sh:927-946` is `build_regen_fixture`; arm 28 runs
  `bash "$lander" --prepare --slug tRegen`; `:1046` skips where no `regen.py` sits beside the lander.
- `tools/push-main.sh:99-107` refuses `--prepare` without a letter-led `--slug`, `:845-852` a
  detached HEAD or the default branch; `:947` prints `push-main: prepared`.
- `tools/govkit/govkit.py:3803-3811` maps `project-owned` to `ORDER`, printed
  `ORDER [project-owned] <dest>`.
- `render_order` (`tools/memory-tree/gen_build_index.py:1716-1739`) marks any step of two or more
  units `yes`; no tool reads the Parallel column (`git grep` over `tools/`).
- `tools/memory-tree/check-memory-hygiene.sh:2717-2720` reds a `consumes-from` target ordered after
  its consumer and is silent within a step.
- `extract_files_touched` (`tools/check-spec-tokens.py:536`) reads its own tokens;
  `{prefix}/check-spec-tokens.py` is a registry `[[exempt]]` path, so the shipped
  `gen_build_index.py` cannot import it; `--legs-for -` reads stdin.
- `tools/memory-tree/gen_build_index.py:307` imports `backlog` and `:186` `tree_lib`.
- `tools/workflows/check-protocol-parity.test.sh:95` renders `unattended-build.js`; `:337` reads
  `KIT_PLAYBOOK_RENDER_VERSION` as a floor first.
- "The predicate" (`tools/workflows/REVIEW-PROTOCOL.template.md:80`, its dogfood copy's `:80`)
  admits only `gov:fixed-verifiers` receivers.
- `tools/check-playbook-parity.sh:257` and `:270-272` hold the comment and the three README rows;
  `tools/check-playbook-parity.test.sh:159-161` writes the valid fixture.
- `tools/check-agent-cap-restatement.sh:90-91` declare `BOUND` and `NOUN`.
- `tools/lib/resolve-python.test.sh:170-172`: `PARITY_ROWS` is `stem|canonical|exclude`;
  `tools/run-gates/profile_bar.py:282` is the `resolve_bash` that runs each candidate;
  `memory/backlog/TOOL.md:494` lists `TOOL-dSettledRoster-6` DEFERRED.

### The build order after S37 and S38

```python
def derive_parallel_step(units):          # units: one step's spec records
    if len(units) < 2:
        return "no"
    for a, b in pairs(units):
        if b["id"] in a["consumes"] or a["id"] in b["consumes"]:
            return "no"                   # M6 clause 2: one reads the other's output
        if intersects(a["writes"], b["writes"]):
            return "no"                   # M6 clause 1: the write sets meet
    return "yes"
```

A spec with no Files touched sub-head contributes no writes. A `yes` means only that the estimates
are disjoint; `--dispatch` still decides.

### The guard's reach into another build's live spec

S23 and S24 in a scratch clone at `8149b14ec` make one `[guards]` hit,
`policy fixtures <- tools/roles/roles_lib.py` (census enforcers `check_roles.py` and `handoff.py`
import it), on TOOL-aScoutedSeam-1 (SPECCED), whose files touched list it and whose §7 lacks the
leg (the guards brief). By §8 F7, the commit that widens the guard writes:

- `memory/project/spec-token-waivers.txt` gains one row keyed
  `policy fixtures <- tools/roles/roles_lib.py`, its reason naming `[guards]`, TOOL-aScoutedSeam-1,
  this unit's widening, ask TOOL-dGroundRules-110 and the count;
- `memory/builds/dGroundRules/build/2026-10-24-build-TOOL-dGroundRules-25-deviation-76.md`,
  deviation-74 its template, carries `**Bound:** spec-token-waivers shrink-only count`,
  `**Tier:** middle`, `**Reason:**` naming F7's refused options and
  `**Surface:** memory/project/spec-token-waivers.txt`; its follow-through is ask
  TOOL-dGroundRules-110, which already asks that §7 for the leg;
- the builder re-measures the `[guards]` set with S24's derivation and waives any further hit so;
- `memory/guides/SESSION-KICKOFF.md`'s `last-audit:` is re-stamped, its `watch:` naming
  `tools/gate-legs.json`.

The commit's `Decided:` trailer cites F7 under rung 5 (ER:388) and carries
`widens: memory/project/spec-token-waivers.txt` and `relaxes: spec-token-waivers shrink-only count`.

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `read_spec_writes`, `read_spec_consumes` | py.function | `tools/memory-tree/design_lib.py` |
| `derive_parallel_step` | py.function | `tools/memory-tree/gen_build_index.py` |
| `resolve_bash_py` | canonical block | `tools/lib/resolve_bash.py` |
| `legacy-homes-withheld-install`, `census-default-adopter`, `guard-mirror-beside-conf`, `guard-mirror-inputs-join`, `arms-empty-declared`, `arms-empty-target`, `on-invalid-bom`, `limit-settings-env-stale` | `CASES` entries | `tools/policy/check_policy.py` |

`lexicon.py --suggest` answered OK for the three minted functions under `py.function` on 2026-10-23.

### Files touched (estimate)

- `tools/policy/policy.py`
- `tools/policy/check_policy.py`
- `tools/policy/guard.py`
- `tools/policy/kit.toml`
- `tools/policy/adopt-policy.sh`
- `tools/policy/README.md`
- `tools/gate-legs.json`
- `tools/lib/resolve_bash.py`
- `tools/lib/resolve-python.test.sh`
- `tools/push-main.test.sh`
- `tools/check-playbook-parity.sh`
- `tools/check-playbook-parity.test.sh`
- `tools/check-template-size.test.sh`
- `tools/memory-tree/check-memory-hygiene.test.sh`
- `tools/workflows/REVIEW-PROTOCOL.template.md`
- `memory/guides/REVIEW-PROTOCOL.md`
- `tools/workflows/check-protocol-parity.test.sh`
- `tools/hooks/README.md`
- `memory/map/features/agent-cap.md`
- `tools/memory-tree/design_lib.py`
- `tools/memory-tree/gen_build_index.py`
- `tools/check-spec-tokens.py`
- `memory/builds/dGroundRules/README.md`
- `memory/map/generated/symbols.json`
- `memory/map/generated/inventories.json`
- `memory/map/generated/MAP.md`
- `memory/project/spec-token-waivers.txt`
- `memory/builds/dGroundRules/build/2026-10-24-build-TOOL-dGroundRules-25-deviation-76.md`
- `memory/guides/SESSION-KICKOFF.md`

S39 also re-renders each other build README's order region the rule moves.

### Alternatives rejected

- **Two batch units split by kit.** Both write `tools/gate-legs.json`: M6's first clause fails.
- **Give the units that share a step distinct orders.** §3 and §8 F1.

## 5. Production-readiness checklist

- security — S19 to S21 refuse a staged render input; S32 bounds an environment-steered write;
  only F7's waiver row widens a surface.
- perf / scale — S9 and S12 add two `apply` runs; S37 reads two sub-sections per spec.
- error / empty / loading states — S4, S25, S26, S29 and S30.
- observability — each new refusal, announce and `WRONG` names its subject.
- risks — S39 moves other builds' order regions; S7 leaves three cases red until
  `TOOL-dGroundRules-31`.
- testing — §4's inventory cases, §7's arm lines, AC1 to AC39.
- migration — the map and build-order regions regenerated.
- user docs — the review protocol and template (S14, S15), the hooks README and map card (S16,
  S17), the policy kit README (S10, S32).

## 6. Acceptance criteria

Every command runs from the repository root. The criteria spell the policy kit's files by bare name,
`policy.py`, `check_policy.py`, `guard.py`, `adopt-policy.sh`, `kit.toml` and `README.md` under the
kit, and `policy.toml` and `policy.json` under `.governance/`, as `TOOL-dGroundRules-5` §6 does,
because the spec-token checker grades a path-shaped token in a criterion against the tracked set and
this build creates them. Each `--fixture <case>` runs `python check_policy.py --fixture <case>` and
passes when it prints no `WRONG`. Each fixture repository sits under the system temp directory,
short-named.

- **AC1** — When `--fixture mirror-commit-rewrite` runs, it reports each of the four reason kinds
  fresh at the carrying commit and at its rewrite; with the `last-valid` builder alone staged to
  format the rendered sha8, it prints `WRONG` naming `last-valid`.
  Red when: one reason builder still names the rendered commit and no kind exercises it.
- **AC2** — When the lander suite's new arm runs over a clone of the built tree, it prints `ok`
  with `regen.py --check` and `mirror --check` both exiting 0 at the prepared HEAD.
  Red when: a prepared merge carries a mirror its own checks call stale.
  cost: one clone and one `--prepare`, as arm 28 costs.
- **AC3** — When the same arm runs, the lander's output it captured holds `push-main: prepared`,
  which the lander prints only once `--prepare` has accepted its `--slug` and merged.
  Red when: the arm calls `--prepare` in a shape the lander refuses.
- **AC4** — When the arm's lander is staged to a stub that exits 2 and the arm runs, it prints `bad`
  naming the exit status and reads neither check.
  Red when: a refused `--prepare` is graded by checks over the unmerged branch.
- **AC5** — When `--fixture adopter-fresh-target` runs at the close, after `TOOL-dGroundRules-31`, it prints no `WRONG`,
  the target holds no `legacy-homes.txt`, and both `--check` runs print
  `not graded · the list is gov's own`.
  Red when: the installed target carries the withheld list, or the arm grades gov's rows there.
- **AC6** — When `requires` in a scratch copy of the policy kit's `kit.toml` is staged to name
  `agent-cap`, whose home is `hooks`, the same case, at the close, after `TOOL-dGroundRules-31`, installs the hooks kit, and its target holds
  the receipt's `agent-cap.js` destination.
  Red when: a required id is resolved as a home and the wrong kit, or none, is installed.
- **AC7** — When the same case runs at the close, after `TOOL-dGroundRules-31`, the installed `regen.py --check` exits 0 after the mirror's
  commit; and `bash adopt-policy.sh --scaffold --target <t>` over a committed target writes
  `policy.json` under its `.governance/`.
  Red when: an adopter's bar is refused at the preflight on install day.
- **AC8** — When an `ARMS` entry's `empty` is staged to differ from its README row's last column,
  `--fixture adopter-fresh-target`, at the close, after `TOOL-dGroundRules-31`, prints `WRONG` naming that arm.
  Red when: the documented empty-population choice can drift from the code.
- **AC9** — When `--fixture legacy-homes-withheld-install` runs, the plan it captured holds an
  `ORDER [project-owned]` row ending `legacy-homes.txt` and no write or `SIDE` row for it, and the
  applied target holds no such file.
  Red when: the criterion reads an imagined plan, or the list installs.
- **AC10** — When `grep -n "ORDER" README.md` runs under the kit, it prints the `legacy-homes` row
  saying the row is informational and the list is not the adopter's to author.
  Red when: the plan's row invites an adopter to write the file unanswered.
- **AC11** — When a case target holds a receipt and an adopter-written `legacy-homes.txt` at the
  installed kit directory, `python check_policy.py --repo <t>` prints the `legacy-homes` announce
  line and no finding.
  Red when: an adopter-authored list is graded against gov's rows.
- **AC12** — When `--fixture census-default-adopter` runs, `arm_cap_census` prints
  `kit check-line-length not installed`, grades the `manifest-bytes` row, and reports no finding.
  Red when: a real install without the conditional entry reds, or the manifest rows go ungraded.
  cost: one `apply` of four entries, a few seconds.
- **AC13** — When `--fixture budgets-ships-join` and `--fixture fixtures-guard-census` run from a
  scratch copy of this repository whose tool root carries another name, both pass.
  Red when: a case reads gov's manifest or registry through a literal prefix.
  cost: one copy of the repository, as the foreign-prefix leg makes.
- **AC14** — When `grep -c "gov:fixed-writers" tools/workflows/REVIEW-PROTOCOL.template.md` runs, it
  prints at least `1`, and the rendered `memory/guides/REVIEW-PROTOCOL.md` holds the same line.
  Red when: the kit's protocol states a predicate the hook no longer enforces.
- **AC15** — When `grep -n "gov:fixed-writers" memory/guides/REVIEW-PROTOCOL.md` runs, it prints a
  line between the heading `### The predicate` and the line opening `Everything else is denied`.
  Red when: the dogfood protocol denies a split the hook admits.
- **AC16** — When `grep -c "cannot resolve to an integer ≤" tools/hooks/README.md` runs, it prints
  `1`.
  Red when: a second spelling makes the parity row's extraction ambiguous.
- **AC17** — When `grep -nE "(verifiers?|agents?|writers?),? ?(≤|<=|at most) ?[0-9]" memory/map/features/agent-cap.md`
  runs, it prints nothing, and the card names `MAX_VERIFIERS` and `runtime.agents-in-flight`.
  Red when: a bound's digit is restated where the restatement leg reds it.
- **AC18** — When the workflows render runs in a scratch copy whose hook's `KIT_AGENT_CAP_VERSION`
  is staged below the version `TOOL-dGroundRules-18` ships, the rendered `unattended-build.js`
  carries `gov:fixed-verifiers` and `Math.min(` on the spec-writer split and stderr names
  `govkit update --kits agent-cap`; at the real version it carries `gov:fixed-writers`.
  Red when: a skewed adopter's hook denies every `unattended-build` call.
- **AC19** — When `--fixture guard-mirror-beside-conf` runs, `guard.py --staged` exits 1 naming
  `.agent-cap.conf`.
  Red when: a render input staged beside the mirror is admitted.
- **AC20** — When `.agent-cap.conf` carries an uncommitted edit in a scratch copy and
  `python policy.py mirror --write` runs there, it exits 2 naming `.agent-cap.conf` and
  `uncommitted changes`.
  Red when: a conf edit renders a mirror the commit will not carry.
- **AC21** — When `--fixture guard-mirror-inputs-join` runs, the guard refuses the staged extra
  input by name.
  Red when: the mirror can record an input the guard never compares.
- **AC22** — When `python policy.py mirror --print | od -c` runs on this node, no `\r` appears.
  Red when: a text-mode write makes every correct mirror differ on Windows.
- **AC23** — When `python tools/check-spec-tokens.py --legs-for tools/gate-legs.json` runs, it names
  `policy fixtures`.
  Red when: a manifest edit alone skips the leg whose case reads the manifest.
- **AC24** — When `tools/memory-tree/backlog.py` is staged out of the `policy fixtures` guard in a
  scratch copy of the manifest and `--fixture fixtures-guard-census` runs there, it prints `WRONG`
  naming `backlog.py`.
  Red when: an imported sibling can change with the leg skipped.
- **AC25** — When `check-spec-tokens.py` is absent from a scratch copy of the source and
  `--fixture fixtures-guard-census` runs there, it prints `WRONG` naming the checker.
  Red when: the join reads a missing checker as covering every path.
- **AC26** — When `--fixture adopter-fresh-target` runs at the close, after `TOOL-dGroundRules-31`, its first `--check` prints, for every
  `ARMS` entry, a graded line with no finding or an announce line; and with one entry's `empty`
  staged off, `--fixture arms-empty-declared` prints `WRONG` naming it.
  Red when: an arm with no declaration falls back to a finding on install day.
- **AC27** — When `--fixture arms-empty-target` runs, the three arms print `not graded` over the
  empty target, and over the scaffolded target `arm_schema` grades `4` keys with no finding.
  Red when: an announce stands in for a policy file that is really there.
  figure: the key count is DERIVED from the scaffold at observation.
- **AC28** — When the `resolve_bash_py` block is cut from `check_policy.py` and from its canonical
  `resolve_bash.py` under `tools/lib/` with the parity arm's awk range, the cuts are identical; with
  one byte changed in the policy copy, the cut differs.
  Red when: the policy kit's bash resolver has no canonical to drift from.
- **AC29** — When the adopter's sibling suite is staged to exit 1, and then staged absent,
  `--fixture adopter-suite`, at the close, after `TOOL-dGroundRules-31`, prints `WRONG` each time.
  Red when: a failed or never-started suite reads as clean.
- **AC30** — When `--fixture on-invalid-bom` runs, `policy.py get budgets.enforce --explain` prints
  the file's own value with source `file`.
  Red when: a BOM sends a valid owner file down the invalid branch.
- **AC31** — When `--fixture on-invalid-shallow` runs, it prints `is-shallow-repository true` before
  its verdict, and `history is shallow`.
  Red when: the case's clone is not shallow and the branch goes unexercised.
- **AC32** — When `--fixture limit-settings-env-stale` runs, `regen.py --check` exits non-zero naming
  `.claude/settings.json`; and with `GOV_SETTINGS_JSON` naming a directory,
  `python policy.py settings --write` exits 2.
  Red when: an exported variable steers the tracked render away from the file in force.
- **AC33** — When `--fixture limit-settings-elsewhere` runs, the hard link keeps the old bytes, the
  target's inode differs, and the directory holds no temporary file.
  Red when: the settings file is rewritten in place.
- **AC34** — When `grep -c "boundedParallel" tools/check-playbook-parity.test.sh` runs it prints `0`,
  and the suite's valid-fixture control holds the re-pointed sentence.
  Red when: the control loses a pair's stated side and the selftest leg reds.
- **AC35** — When `python tools/memory-tree/check-arms.py --report` runs, it prints the `fail 5`
  branch of `tools/check-template-size.sh`, the refusal a launcher-less run reaches, `ARMED`.
  Red when: the template-size refusal with no Python launcher has no arm.
- **AC36** — When `grep -c "derive_lowered_limit" memory/map/generated/symbols.json` runs it prints
  at least `1`, and `python tools/codebase-map/gen_map.py --check` exits 0.
  Red when: the map omits a function a unit of this build added.
- **AC37** — When the `build-index selftest` fixture renders a step of two units whose Files touched
  both name one path, its Parallel column reads `no`; with the paths disjoint it reads `yes`.
  Red when: a step whose write sets meet is told it may run concurrently.
- **AC38** — When the same fixture renders a step whose second unit consumes from its first, the
  column reads `no`.
  Red when: a unit is told it may run beside the unit whose output it needs.
- **AC39** — When `grep -nE "^\| (4|6|7) \|" memory/builds/dGroundRules/README.md` runs, each printed
  row ends `| no |`.
  Red when: this build's own table still tells the dispatcher to run intersecting units together.

## 7. Gates

`push-main self-test` · `python resolver (behaviour + inline parity + idiom ban)` · `build-index selftest` · `memory-hygiene self-test` · `spec-tokens self-test` · `template size gate selftest` · `harness arms (fail branches armed or pinned)` · `review-protocol parity (kit vs dogfood)` · `kit/dogfood doc parity` · `playbook parity` · `playbook parity selftest` · `agent-cap restatement` · `agent-cap self-test` · `scratch-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `tier2-review self-test` · `unattended-build self-test` · `install-prefix (shipped surface)` · `foreign-prefix parity (every self-test at three prefixes)` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `transition-audit arms` · `straggler-guard arms` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `memory hygiene` · `recall floor` · `recall floor arms` · `policy fixtures` · `spec tokens (a spec's own names resolve)`

The policy legs `TOOL-dGroundRules-1` declares run the cases.

New arm: tools/policy/check_policy.py --fixture · covers AC1 AC5 AC6 AC7 AC8 AC9 AC11 AC12 AC19 AC21 AC24 AC25 AC26 AC27 AC29 AC30 AC31 AC32 AC33 · each case named in §4's inventory and each case S1 to S33 extends, planting its input in its temporary repository and asserting its stated outcome · none
New arm: tools/push-main.test.sh · covers AC2 AC3 AC4 · a policy-file change on `feat` landed through the real `--prepare`, then the lander staged to a stub exiting 2 · that suite's assertion count, raised by the arm
New arm: tools/lib/resolve-python.test.sh · covers AC28 · the `resolve_bash_py` row, staged by one byte changed in the policy copy · that suite's assertion count, raised by the row
New arm: tools/memory-tree/gen_build_index.py (`--selftest`) · covers AC37 AC38 · a fixture step whose units' write sets meet, then one whose second unit consumes from its first · none
New arm: tools/check-template-size.test.sh · covers AC35 · a `PATH` holding no Python launcher over an over-cap subject, the `fail 5` line asserted · none
New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers none · a `PATH` holding no Python launcher, exit 2 and the line `HYGIENE — no usable python` asserted by its text · none
New arm: tools/workflows/check-protocol-parity.test.sh · covers AC18 · the hook's version constant staged below the writer marker's version in a scratch copy · none

## 8. Open questions

- **F1 — How are steps whose units share a write set or an edge closed (findings 1, 2, 26)?**
  (a) The render marks such a step `no`: distinct orders rewrite reviewed headers (M4, veto 1), and
  a hygiene arm reds twenty-one landed edges (§3). Rung 3. RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none
- **F2 — What happens to the replay case once the real lander has an arm (finding 18)?** (a) It
  stays as the policy leg's fast check. Rung 3. RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none
- **F3 — Where is the agent-cap floor of the writer marker enforced (finding 44)?** (a) In the
  workflows render (S18); the kit ships no adopter to carry a `--check` (veto 2, §3). Rung 3. RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none
- **F4 — Is an adopter-authored legacy-home list graded (finding 37)?** (a) Never: it cannot
  hold gov's rows, so grading it reds every adopter, failing `TOOL-dGroundRules-16` AC1 (veto 1). Rung 3. RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none
- **F5 — How does the guard join learn which legs a path trips (finding 19)?** (a) Through
  `--legs-for -`, gov's one trip rule; the case runs only in the gov-only `policy fixtures` leg. Rung 3. RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none
- **F6 — What does the reader do with a UTF-8 BOM (finding 43)?** (a) Strip one leading BOM
  and parse, as unit 10's conf reader does (AC30). Rung 3. RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none
- **F7 — How does S24's guard widening meet its hit on another build's live spec (§4)?** (a) Keep
  every import: waive the hit under ask TOOL-dGroundRules-110 with deviation-76, relaxing the
  registry's count. (b) Leave the module out: the gap finding 41 names. (c) Revise
  TOOL-aScoutedSeam-1's §7: an outside write this build's README refuses
  (`memory/builds/dGroundRules/README.md:48-49`). Recommendation (a). Rung 5:
  RESOLVED (agent, 2026-10-24, delegated): (a), citing ER:388 (`PLAY-dClosedLoop-6`) and
  TOOL-dGroundRules-20 §8 F1.
  widens: memory/project/spec-token-waivers.txt · relaxes: spec-token-waivers shrink-only count

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft.
- rev-2 · 2026-10-23 · §3 · hands-off edges to units 27, 30, 31 and 32.
- rev-3 · 2026-10-23 · §3 · hands-off edges to units 33 and 34.
- rev-4 · 2026-10-23 · §1 §3 §4 §5 §8 §10 · prose shortened.
- rev-5 · 2026-10-23 · §1 §2 §3 · unit 13 renamed TOOL-dGroundRules-65 (owner).
- rev-6 · 2026-10-24 · §6 · a code span rejoined onto one line.
- rev-7 · 2026-10-24 · §7 §9 · the policy fixtures leg added, owed by its guard.
- rev-8 · 2026-10-24 · §1 §4 §8 §9 · prose shortened.
- rev-9 · 2026-10-24 · §2 S24 · §4 · §5 · §7 · §8 F7 · one `[guards]` hit on TOOL-aScoutedSeam-1 measured before the build; ruled (a) under ER:388 (F7); §7 adds `spec tokens`.
- rev-10 · 2026-10-24 · §2 S7 S35 S37 S38 · §3 to §10 · the builder's divergence: S31 added no hygiene branch, and `mirror --write` refuses on install day. Ruled: the hygiene arm asserts its exit-2 line, AC35 keeps what `--report` prints; S7's three cases stay red until `TOOL-dGroundRules-31`, its deferral not folded in; the fixture re-runs the memory-tree adopter; three citations re-cited.

## 10. Reuse audit

Each item extends the seam it names: arm 28 of `tools/push-main.test.sh` (S2 to S4), `TOOL-dGroundRules-24`'s installed target (S5 to S7, S9, S12), `derive_census_tree`
(S11, S12), the parity rows of `tools/lib/resolve-python.test.sh` (S28), `--legs-for` (S25),
`check-protocol-parity.test.sh`'s version floor (S18), `tools/check-wiring.sh:102-108`'s
`GOV_SETTINGS_JSON` rule (S32), the two suites' arms (S35), `gen_map.py --write` (S36), and
`extract_files_touched`, whose token read moves into `design_lib.py` (S37).
`tools/codebase-map/reuse_lookup.py` over "locate an installed kit file in an adopter from its
install receipt" and "install a kit into a scratch target with the deployer and read its receipt"
ranked `resolve_kit_dir` and `kit_rel`; the rest came from the files the review cites. Recall
returned `TOOL-dGroundRules-21`, whose table this unit follows.

Recall terms used: `python tools/memory-recall/query.py "how are review minors batched into one
repair unit" --terms "minors batch promoted medium low disposed severity spec-audit repair unit write
set"`
