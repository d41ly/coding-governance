# TOOL-dGroundRules-21 — the round-1 spec audit's minors: forty-one findings closed in the code units 1 to 10 leave, one scope item each

**Status:** DEFERRED · rev-6 · 2026-10-24 · node d · Tier-2 · base 3708a705 · streams tooling · order 7 · advances TOOL-dGroundRules-12

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-21-deviation-56.md](../build/2026-10-23-build-TOOL-dGroundRules-21-deviation-56.md) | deviation | — |
| [2026-10-23-build-TOOL-dGroundRules-21-deviation-9.md](../build/2026-10-23-build-TOOL-dGroundRules-21-deviation-9.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dGroundRules-21-1-spec-writer.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-21-1-spec-writer.md) | journal | — |
| [2026-10-23-prompt-TOOL-dGroundRules-21-build-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-21-build-brief.md) | journal | — |
| [2026-10-23-prompt-TOOL-dGroundRules-21-trim-task.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-21-trim-task.md) | research | TOOL-dGroundRules-25 TOOL-dGroundRules-34 TOOL-dGroundRules-64 |
| [2026-10-24-prompt-TOOL-dGroundRules-21-1-spec-writer.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-21-1-spec-writer.md) | journal | — |
| [2026-10-24-prompt-TOOL-dGroundRules-21-legline-fold-brief.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-21-legline-fold-brief.md) | research | — |
| [2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-65 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-51 TOOL-dGroundRules-52 |
| [2026-10-23-review-TOOL-dGroundRules-65-21-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-65-21-spec-audit-round1.md) | spec-audit | TOOL-dGroundRules-16 TOOL-dGroundRules-65 TOOL-dGroundRules-14 TOOL-dGroundRules-19 TOOL-dGroundRules-15 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-20 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-1-11-spec-audit-round1.md`)
exited BOUNDED with 49 confirmed findings. Its two BLOCKERs and six HIGHs are promoted one unit each,
`TOOL-dGroundRules-65` to `TOOL-dGroundRules-20`; BUILD-METHOD M4 batches the other forty-one,
thirty-three MEDIUM and eight LOW, into this unit. They land on units 1 to 10 and share
`tools/policy/policy.py`, `tools/policy/check_policy.py`, the codebase map and `tools/gate-legs.json`'s
neighbours, so M6's clauses yield no two disjoint write sets. It builds at order 7, after every unit
whose code it amends. A finding the review merged into another's item keeps its own scope item.

| Finding id | Severity | Review item | Unit it lands on | Scope item | Criterion |
|---|---|---|---|---|---|
| 19 | MEDIUM | M10 | 1 | S1 | AC1 |
| 27 | MEDIUM | M10 | 1, 7 | S2 | AC2 |
| 39 | MEDIUM | M16 | 1 | S3 | AC3 |
| 41 | MEDIUM | M18 | 1 | S4 | AC4 |
| 51 | MEDIUM | M25 | 1, 8 | S5 | AC5 |
| 20 | LOW | L3 | 1 | S6 | AC6 |
| 29 | LOW | L5 | 1 | S7 | AC7 |
| 14 | MEDIUM | M7 | 2 | S8 | AC8 |
| 24 | MEDIUM | M12 | 2 | S9 | AC9 |
| 53 | MEDIUM | M27 | 2, 4 | S10 | AC10 |
| 10 | LOW | L1 | 2, 9 | S11 | AC11 |
| 3 | MEDIUM | M1 | 3, 5 | S12 | AC12 |
| 52 | MEDIUM | M26 | 4 | S13 | AC13 |
| 17 | MEDIUM | M8 | 5 | S14 | AC14 |
| 47 | MEDIUM | M21 | 5, 4 | S15 | AC15 |
| 48 | MEDIUM | M22 | 5 | S16 | AC16 |
| 49 | MEDIUM | M23 | 5 | S17 | AC17 |
| 50 | MEDIUM | M24 | 5 | S18 | AC18 |
| 11 | LOW | L2 | 5 | S19 | AC19 |
| 26 | LOW | L4 | 5, 9 | S20 | AC20 |
| 25 | MEDIUM | M13 | 6 | S21 | AC21 |
| 56 | LOW | L8 | 6 | S22 | AC22 |
| 5 | MEDIUM | M2 | 7 | S23 | AC23 |
| 15 | MEDIUM | M2 | 7 | S24 | AC24 |
| 16 | MEDIUM | M3 | 7, 8 | S25 | AC25 |
| 6 | MEDIUM | M3 | 8 | S26 | AC26 |
| 7 | MEDIUM | M4 | 8, 4, 9 | S27 | AC27 |
| 8 | MEDIUM | M5 | 9 | S28 | AC28 |
| 18 | MEDIUM | M9 | 9 | S29 | AC29 |
| 36 | MEDIUM | M9 | 9 | S30 | AC30 |
| 44 | MEDIUM | M20 | 9 | S31 | AC31 |
| 9 | MEDIUM | M6 | 10 | S32 | AC32 |
| 34 | MEDIUM | M6 | 10 | S33 | AC33 |
| 21 | MEDIUM | M11 | 10 | S34 | AC34 |
| 33 | MEDIUM | M14 | 10 | S35 | AC35 |
| 38 | MEDIUM | M15 | 10 | S36 | AC36 |
| 42 | MEDIUM | M19 | 10, 1 | S37 | AC37 |
| 45 | MEDIUM | M28 | 10 | S38 | AC38 |
| 43 | LOW | L6 | 10 | S39 | AC39 |
| 54 | LOW | L7 | 10 | S40 | AC40 |
| 40 | MEDIUM | M17 | 2, 3, 4, 7, 8, 9, 10 | S41 | AC41 |

Each item's fix is the one the review's skeptic judged sound; for id 11 it is the skeptic's corrected
fix. Where the review offered options, §8 records the pick.

## 2. Scope (IN)

- **S1** — Finding 19. `policy.py scaffold` writes its bytes through `sys.stdout.buffer` with LF line
  ends, so its output is the same on every platform, and the policy file is compared as the blob git
  stores, not as a checkout. Observed by AC1.
- **S2** — Finding 27. `.gitattributes` pins `.governance/policy.toml`, `tools/policy/*.toml` and
  `tools/policy/*.txt` with `text eol=lf`, beside the `tools/template-size-limits.txt` pin
  (`.gitattributes:22`). Observed by AC2.
- **S3** — Finding 39. `tools/policy/kit.toml` declares
  `version_from = { file = "policy.py", pattern = "^KIT_POLICY_VERSION = " }`, and
  `tools/policy/README.md`'s first line is `<!-- gov:kit policy@<the constant's value> -->`, as
  `tools/roles/README.md:1` carries the roles kit's. Observed by AC3.
- **S4** — Finding 41. `tools/policy/adopt-policy.test.sh`, the sibling suite arming every refusal
  branch of `adopt-policy.sh` under `ARMS_REFUSALS="graded"` (`.memory-tree.conf:639`), its floor
  row in `.memory-tree.conf`'s `ARMS_FLOORS` from `check-arms.py --emit-floors`, and the case
  `adopter-suite` that runs it from `check_policy.py --fixture` so a leg executes it. Every kit path
  in `adopt-policy.sh` and in the fixture mode is derived from the kit's own location, never spelled
  as a literal kit segment. Observed by AC4.
- **S5** — Finding 51. Each `ARMS` entry declares what an empty population means, `finding` or
  `announce`, and `check_policy.py` applies that per arm in place of unit 1's blanket "a population
  of zero is a finding". `arm_schema` over an absent or empty policy file, the reader-coverage arm
  before any Owner build lands, and `arm_mirror_readers` over a tree with no code file announce;
  every other arm keeps the finding. Observed by AC5.
- **S6** — Finding 20. `tools/policy/README.md` states that `read_policy_key` keeps its `KEY=value`
  contract in four byte-identical copies and names each: `.githooks/pre-push:1306`,
  `tools/push-main.sh:404`, `tools/run-gates/post-merge.sh:171` and `tools/unattended/unattended.sh:9517`.
  Observed by AC6.
- **S7** — Finding 29. `resolve_compare_base` becomes a canonical block, `# >>> compare_base_py`, in
  a new `tools/lib/compare_base.py`, inlined between its markers in `tools/codebase-map/map_lib.py`
  and in `tools/policy/policy.py`, and held to its canonical by a row in the `PARITY_ROWS` of
  `tools/lib/resolve-python.test.sh`. Observed by AC7.
- **S8** — Finding 14. `policy.py` defines `resolve_remote` once, inside its
  `# >>> remote_ladder_py` block, and no line outside that block spells `"remote"`, `remote get-url`
  or `remote -v`: what `TOOL-dGroundRules-2`'s AC7 `git remote` count, which cannot pass on a correct
  build, meant. Observed by AC8.
- **S9** — Finding 24. The git location-variable list becomes a canonical block,
  `# >>> git_env_leaks_py`, in a new `tools/lib/git_env_leaks.py` holding the tuple
  `tools/memory-tree/tree_lib.py:262` holds, inlined in `tools/policy/policy.py` in place of the list
  that module spelled, and held by a `PARITY_ROWS` row. Observed by AC9.
- **S10** — Finding 53. The reader decodes a revision's policy text inside a handler for
  `UnicodeDecodeError` and hands the failure on as a `Problem` with `why` opening `not UTF-8:`, which
  unit 4's invalid branch treats as a TOML decode error. Observed by AC10.
- **S11** — Finding 10. `read_blob_at(repo, rev, path)` in `tools/policy/policy.py` returns a path's
  blob text at a revision or `None`; `read_policy_text` calls it, and `tools/policy/budgets.py` reads
  the limits home through it, the blob reader unit 2's edge handed unit 9. Observed by AC11.
- **S12** — Finding 3. `read_default_value` resolves a row whose `default` is
  `{ derived = "..." }` to a `Refusal` naming the row in the catalogue and the reason "a derived
  default no reader computes yet". The mirror omits such a key, so the helper reads it through the
  reader and refuses with that line. Observed by AC12.
- **S13** — Finding 52. `read_last_valid` asks `git rev-parse --is-shallow-repository`; when it is
  true and the first-parent walk ends at the shallow boundary with no valid revision, it refuses with
  `history is shallow at <sha8>; fetch more history`. Observed by AC13.
- **S14** — Finding 17. `check_policy.py` runs the shim through `resolve_bash(script)`, a copy of
  `tools/run-gates/profile_bar.py:282`'s rule: `GOV_BASH` first, then `bash` on PATH, then Git for
  Windows' two paths, each kept only when running it can stat the script. Observed by AC14.
- **S15** — Finding 47, the skeptic's corrected fix. `arm_mirror_parity` grades an absent mirror
  only when HEAD carries `.governance/policy.toml` or a mirror; otherwise, including when HEAD does not
  resolve, it prints one announce line and reports no finding. `arm_on_invalid` announces and reports
  no finding when HEAD does not resolve. Observed by AC15.
- **S16** — Finding 48. `readPolicy` maps every shim outcome other than exit 0 or the documented
  missing path to a `PolicyRefusal` carrying the status, the signal and the shim's stderr: exit 1,
  exit 127, a null status, a signal and a spawn error each refuse. It locates bash as S14 does,
  running each candidate once per process. Observed by AC16.
- **S17** — Finding 49. The mirror records `legacy_blobs`, a map from each legacy input the
  resolution reads, today `.agent-cap.conf`, to its blob id at the rendered revision or `null`; the
  helper compares every entry at `L` with the two blob ids, any difference reading the mirror as
  STALE. The kit README states the rule: a unit adding a resolution input adds its blob to this map.
  Observed by AC17.
- **S18** — Finding 50. `arm_mirror_readers` matches a read of the mirror, not a mention: a line
  that is not a comment and spells `readFileSync`, `open(`, `cat` or `git show` followed on the line
  by `policy.json`; `*.test.sh`, `*.test.js`, `selftest*.py` and `test_*.py` are not scanned, as unit
  8's scan excludes them. `mirror-direct-reader` stays red. Observed by AC18.
- **S19** — Finding 11, the skeptic's corrected fix. The `.gitattributes` line for the mirror names
  `.governance/policy.json` exactly, so `git check-attr eol` on that path prints `eol: lf`.
  Observed by AC19.
- **S20** — Finding 26. One scanner, `arm_single_reader(repo, path, reader_dir)` in
  `check_policy.py`, with its suffix set, its exclusions and S18's read shape stated once;
  `arm_mirror_readers` and `arm_limits_readers` become two rows of it, the second for
  `template-size-limits.txt` with `tools/policy/` as its reader directory. Observed by AC20.
- **S21** — Finding 25. The pre-commit guard block gains its `else`: when `guard.py` does not resolve
  and `git show HEAD:<GOV_KITROOT>/policy/guarded-paths.txt` lists a staged path, it calls
  `print_kit_miss "policy guard" policy guard.py` and sets `rc=1`. Observed by AC21.
- **S22** — Finding 56. The guard's fixture policy file carries a key with slashes and a leading dot,
  `".claude/skills/x/SKILL.md"`, raised in `guard-admits-raise` and lowered in `guard-lowered`, and
  the class key `"memory/builds/*/spec/"` in `guard-class-row`. Observed by AC22.
- **S23** — Finding 5. The legacy-home list's shrink-only half reads its base through the one
  comparison unit 1's `lists --check` calls, `resolve_compare_base`, spelled once in `cmd_lists` for
  both lists; no other base is read. Observed by AC23.
- **S24** — Finding 15. The case `legacy-homes-main-dropped`: the landed tip drops a conf key the
  branch's merge-base still holds, and the branch's derivation still carries it; `lists --check`
  reports no "new legacy home". Observed by AC24.
- **S25** — Finding 16. Unit 7 locates the roles house file through the inlined `resolve_kit_dir`
  with home `roles` and anchor `house/policy.toml`, never by joining a name to the tool root; a miss
  is an absent home, announced. The case `reader-coverage-relocated` proves it at a non-default
  prefix. Observed by AC25.
- **S26** — Finding 6. Unit 8 reaches `tree_lib` as `tools/memory-recall/extract.py:105-121` does:
  the inlined `resolve_kit_dir("memory-tree", "tree_lib.py", ...)`, `memory-tree` added to
  `requires` in `tools/policy/kit.toml`, and a miss raised as a refusal naming where the resolver
  looked. `tools/policy/README.md` states the kit's one rule: a sibling kit is reached through the
  inlined resolver and a declared `requires`, and a miss refuses. Observed by AC26.
- **S27** — Finding 7. Unit 8's pattern segment admits a quoted segment that holds `.` and an
  interpolated name inside the quotes, so `f'budgets."{cap}"'` and `'budgets."' + name + '"'` read
  `budgets.*`; unit 4's read of `policy-file.on-invalid` is spelled
  `parse_key("policy-file.on-invalid")`, a string literal the first call shape matches.
  Observed by AC27.
- **S28** — Finding 8. `check_budgets` refuses a `budgets.<cap>` that is not a non-negative
  integer; 0 keeps meaning unchecked, as the census's homes hold it today. Observed by AC28.
- **S29** — Finding 18. `arm_limits_readers` counts a line only when it reads the file, by S18's
  read shape or by naming the `SIZE_LIMITS_NAME` constant, so the docstrings at
  `tools/memory-recall/extract.py:346` and `tools/check-spec-tokens.py:159` are not readers.
  Observed by AC29.
- **S30** — Finding 36. The case `limits-reader-docstring` plants a docstring naming
  `template-size-limits.txt` and stays green, as the live arm does over this repository. Observed by AC30.
- **S31** — Finding 44. One rule for every switch enforcer, kept in `tools/policy/budgets.py`: a
  reader refusal inside `resolve_caps` gives the cap `mode = refuse` and prints the refusal once, so
  a subject over its cap refuses as today and is never read as `warn`. The four shell enforcers,
  `tools/check-template-size.sh`, `tools/check-line-length.sh`,
  `tools/memory-tree/check-memory-hygiene.sh` and `skills/session-kickoff/manifest-check.sh`, take
  the branch they take with no policy kit when no Python launcher resolves, and say so once.
  Observed by AC31.
- **S32** — Finding 9. Line 84 of `memory/map/features/agent-cap.md`, teaching as live the
  environment refusal unit 10 takes out of the hook, is rewritten to state rule 7, the limit's key
  and the writer and verifier bounds. Observed by AC32.
- **S33** — Finding 34. The D7 arm of `tools/workflows/check-review-join.test.sh:207` plants its
  environment refusal with a stub predicate that prints a refusal and exits 2 before any rule,
  placed where the gate's resolver finds it, as the arm below it plants its stub; it no longer sets
  `AGENT_CAP`. Observed by AC33.
- **S34** — Finding 21. The settings render and rule 7 resolve the settings file as
  `tools/check-wiring.sh:94-117` does: `GOV_SETTINGS_JSON` first, then `.claude/settings.json` under
  the checkout root. The render writes only the two `env` keys and keeps every other byte's
  meaning; ownership is settled in §8 F1 and stated in the kit README. Observed by AC34.
- **S35** — Finding 33. `tools/check-playbook-parity.sh` retires its `bounded-helper width` row
  (`:271`), whose README sentence described the raw-primitive ban unit 10 takes out, and re-points
  the `resolved-K ceiling` row (`:272`) to the hooks README's surviving rule-2 sentence stating the
  verifier bound against `MAX_VERIFIERS`. Observed by AC35.
  **Readers:**
  by name: `tools/check-playbook-parity.sh`, whose row at `:271` and comment at `:257` spell it.
  by value: NO VALUE READERS — the row's extracted number is compared only inside that script, and
  no other file reads its verdict by the row's name.
- **S36** — Finding 38. The markers `gov:kit agent-cap@1.40` at `tools/hooks/format-guard.js:7` and
  `tools/hooks/scratch-guard.js:144` move to the version `KIT_AGENT_CAP_VERSION` holds, marker text
  only. Observed by AC36.
- **S37** — Finding 42. `adopt-policy.sh --scaffold` runs `policy.py settings --write` whenever HEAD
  resolves, on a re-run over a kept file too, and prints one line naming the re-run when it does not;
  the kit's `[[regenerate]]` runs the same render on update. Observed by AC37.
- **S38** — Finding 45. Rule 7 runs inside a `try`/`catch` denying with exit 2 on any throw, naming
  the step; an unparseable settings file refuses naming it, and a `cwd` with no checkout refuses.
  Observed by AC38.
- **S39** — Finding 43. `tools/hooks/agent-cap.test.sh` carries no `git show <sha>:` read: the
  base-revision RED of the rules unit 10 takes out is the main loop's one-off observation at the
  close, in the acceptance ledger. Observed by AC39.
- **S40** — Finding 54. The settings render writes through a temporary file in the same directory
  and `os.replace`. The claim that a session keeps its harness settings until it restarts is marked
  UNVERIFIED in `help/agent-limit.md`, with the two-halves probe of
  `memory/gotchas/settings-edit-takes-effect-mid-session.md` that decides it, observed at the close.
  Observed by AC40.
- **S41** — Finding 40. The codebase map is regenerated over every unit of this build, by
  `python tools/codebase-map/gen_map.py --write`, into `memory/map/generated/`, and the
  `codebase-map coverage + freshness` leg is on §7. Observed by AC41.

## 3. Non-goals (OUT)

- Every BLOCKER and HIGH: `TOOL-dGroundRules-65` to `TOOL-dGroundRules-20`.
- Rewriting any reviewed spec's text: each defect is closed here in code and in the criteria it
  governs, and the repaired unit's §3 names this unit.
- The other copies of the git location-variable list: `TOOL-dRetiredFork-23` stays their ask.
- An `env` mode in `tools/settings-merge.py` (§8 F1).

### Edges

- **consumes-from** `TOOL-dGroundRules-1` — `scaffold`, `ARMS`, `CASES`, the fixture mode, `adopt-policy.sh`, `kit.toml`, the README and `resolve_compare_base`, which S1 to S7 amend
- **consumes-from** `TOOL-dGroundRules-2` — `read_policy_text`, the inlined ladder, the git environment and the decode path, which S8 to S11 amend
- **consumes-from** `TOOL-dGroundRules-3` — `read_default_value`, which S12 amends
- **consumes-from** `TOOL-dGroundRules-4` — `read_last_valid`, `arm_on_invalid` and the on-invalid read, which S13, S15 and S27 amend
- **consumes-from** `TOOL-dGroundRules-5` — the shim calls, `readPolicy`, the mirror's data model and its arms, which S14 to S20 amend
- **consumes-from** `TOOL-dGroundRules-6` — the pre-commit block and the `guard-` cases, which S21 and S22 amend
- **consumes-from** `TOOL-dGroundRules-7` — the legacy-home derivation and its shrink-only half, which S23 to S25 amend
- **consumes-from** `TOOL-dGroundRules-8` — the reader-coverage arm, its import and its scanner, which S25 to S27 amend
- **consumes-from** `TOOL-dGroundRules-9` — `budgets.py`, `check_budgets` and `arm_limits_readers`, which S11 and S28 to S31 amend
- **consumes-from** `TOOL-dGroundRules-10` — the settings render, rule 7, the retired readers and the version bump, which S32 to S40 amend
- **consumes-from** `TOOL-dGroundRules-15` — the lowering inside `resolve_read`, whose input S17 records in the mirror
- **consumes-from** `TOOL-dGroundRules-16` — `adopter-fresh-target`, which S5 and S15 turn green
- **hands-off** `TOOL-dGroundRules-25` — `empty` on `ARMS`, `adopter-suite`, the decode path, `on-invalid-shallow`, the settings render, the parity re-point, the no-launcher branch and `adopt-policy.sh --scaffold`, which that unit amends (findings 5, 6, 21, 32, 43, 16, 40, 22, 28, 29, 35, 23, 9)
- **hands-off** `TOOL-dGroundRules-61` — S34's rule-7 half, which that unit replaces with `readSettingsLayers`, bounding every settings layer rule 7 reads, the `GOV_SETTINGS_JSON` file included (id 1 of the spec run's closing diff review)
- **hands-off** `TOOL-dGroundRules-62` — S12's derived-default refusal, which that unit types as `DerivedDefault`, and S31's refused-reader rule, from which that unit exempts that type on a cap's value read (id 8 of the spec run's closing diff review)
- **hands-off** `TOOL-dGroundRules-64` — the policy file's full path in the opening paragraph of §6, respelled to its basename, which that unit restores

## 4. Design

### Evidence

Every line below was read at base `3708a705` on 2026-10-23.

- `.gitattributes:22` pins `tools/template-size-limits.txt` and `:100` pins `.governance/deploy.toml`;
  `git check-attr eol` printed `unspecified` for the new policy paths, under a system
  `core.autocrlf=true`.
- `tools/roles/README.md:1` carries `<!-- gov:kit roles@1.8 -->`; govkit selfcheck 5 and 5c fail an
  entry with no `version_from` or no marker (`tools/govkit/govkit.py:2119-2124`, `:2250-2291`).
- `.memory-tree.conf:639` holds `ARMS_REFUSALS="graded"`, and `check-arms.py` reads arms from a gate's
  sibling `<stem>.test.sh` and requires a per-gate floor in `ARMS_FLOORS` (`:39-55`).
- `read_policy_key()` is defined at the four lines S6 names; v2's `## [presets]` heading is at line
  1409, not 1408, as `TOOL-dGroundRules-1` §4 cites it.
- `def resolve_compare_base` exists once, `tools/codebase-map/map_lib.py:1502`, outside any marked
  block; `tools/lib/resolve-python.test.sh:170-185` declares `PARITY_ROWS` as `stem|canonical|exclude`
  and grades every copy `git grep` finds by its opening marker.
- `tools/memory-tree/tree_lib.py:262` holds `GIT_ENV_LEAKS`; `memory/builds/dRetiredFork/BACKLOG.md:9`
  files `TOOL-dRetiredFork-23`, the ask that the copies agree.
- `tools/run-gates/profile_bar.py:282` is a `resolve_bash` that runs each candidate;
  `memory/gotchas/subprocess-resolves-a-different-shell.md` records the class it closes.
- `tools/workflows/check-review-join.test.sh:207` plants `env AGENT_CAP=7`;
  `memory/map/features/agent-cap.md:84` teaches the `AGENT_CAP` refusal as live.
- `tools/check-playbook-parity.sh:271-272` extract `boundedParallel(thunks, N)` and "cannot resolve to
  an integer ≤N" from the hooks README and compare each with `MAX_VERIFIERS`.
- S36's two carriers hold `gov:kit agent-cap@1.40`; `tools/check-kit-versions.sh` fails a carrier
  that differs from the constant.
- `tools/check-wiring.sh:94-117` resolves `GOV_SETTINGS_JSON` first; `tools/hooks/kit.toml:52-56`
  records settings-merge as the hook wiring's owner.
- `tools/memory-recall/extract.py:346` and `tools/check-spec-tokens.py:159` name
  `template-size-limits.txt` in docstrings.
- `.githooks/pre-commit:174` defines `print_kit_miss`, which each kit leg's `else` calls.

### Per-unit changes, by file

| File | Items |
|---|---|
| `tools/policy/policy.py` | S1, S7, S8, S9, S10, S11, S12, S13, S17, S23, S25, S26, S27, S34, S40 |
| `tools/policy/check_policy.py` | S4, S5, S14, S15, S18, S20, S22, S24, S25, S29, S30 |
| `tools/policy/policy-mirror.js` | S16, S17 |
| `tools/policy/budgets.py` | S11, S28, S31 |
| `tools/policy/kit.toml` | S3, S26, S37 |
| `tools/policy/adopt-policy.sh`, `tools/policy/adopt-policy.test.sh` | S4, S37 |
| `tools/policy/README.md` | S3, S6, S17, S26, S34 |
| `tools/hooks/agent-cap.js`, `tools/hooks/agent-cap.test.sh` | S34, S38, S39 |
| the rest | as each item names |

### The empty-population declaration (S5)

```python
ARMS = [
    Arm(name="arm_schema", run=arm_schema, empty="announce"),   # no policy file is legal
    Arm(name="arm_shape", run=arm_shape, empty="finding"),
    ...
]
```

An `announce` arm with population 0 prints `policy-check: <arm> · not graded · <why>` and no
finding; a `finding` arm with population 0 prints its line and one finding. `TOOL-dGroundRules-16`'s
README table names the same choice per arm in its last column.

### The mirror after S17

```json
{"catalogue_blob": "...", "keys": {...}, "legacy_blobs": {".agent-cap.conf": "<id or null>"}, "policy_blob": "..."}
```

`TOOL-dGroundRules-65`'s invariant gains the legacy blobs: two commits with equal policy, catalogue
and legacy blobs and the same first-parent history render byte-identical mirrors.

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `read_blob_at` | py.function | `tools/policy/policy.py` |
| `resolve_bash` | py.function, copied | `tools/policy/check_policy.py` |
| `arm_single_reader` | arm function | `tools/policy/check_policy.py` |
| `compare_base_py`, `git_env_leaks_py` | canonical blocks | `tools/lib/compare_base.py`, `tools/lib/git_env_leaks.py` |
| `legacy_blobs` | mirror field | `.governance/policy.json` |
| `adopter-suite`, `legacy-homes-main-dropped`, `reader-coverage-relocated`, `limits-reader-docstring` | `CASES` entries | `tools/policy/check_policy.py` |
| `resolution-derived-default`, `on-invalid-shallow`, `on-invalid-utf16`, `mirror-stale-legacy`, `mirror-shim-exit-one`, `mirror-absent-adopter`, `reader-quoted-pattern`, `budgets-zero-cap`, `budgets-reader-refused`, `limit-settings-elsewhere`, `limit-hook-settings-malformed`, `limit-hook-reader-throws`, `limit-fresh-target-spawn` | `CASES` entries | `tools/policy/check_policy.py` |

Each name takes its house prefix, `read`, `resolve` or the `arm_` every arm in `ARMS` carries; the
builder confirms each with `python tools/lexicon/lexicon.py --suggest <name> --as py.function`.

### Files touched (estimate)

- `tools/policy/policy.py`
- `tools/policy/check_policy.py`
- `tools/policy/policy-mirror.js`
- `tools/policy/budgets.py`
- `tools/policy/kit.toml`
- `tools/policy/adopt-policy.sh`
- `tools/policy/adopt-policy.test.sh`
- `tools/policy/README.md`
- `.governance/policy.json`
- `.gitattributes`
- `.memory-tree.conf`
- `.githooks/pre-commit`
- `.githooks/pre-commit.test.sh`
- `tools/lib/compare_base.py`
- `tools/lib/git_env_leaks.py`
- `tools/lib/resolve-python.test.sh`
- `tools/codebase-map/map_lib.py`
- `tools/hooks/agent-cap.js`
- `tools/hooks/agent-cap.test.sh`
- `tools/hooks/format-guard.js`
- `tools/hooks/scratch-guard.js`
- `tools/hooks/README.md`
- `tools/workflows/check-review-join.test.sh`
- `tools/check-playbook-parity.sh`
- `tools/check-template-size.sh`
- `tools/check-line-length.sh`
- `tools/memory-tree/check-memory-hygiene.sh`
- `skills/session-kickoff/manifest-check.sh`
- `help/agent-limit.md`
- `memory/map/features/agent-cap.md`
- `memory/map/generated/symbols.json`
- `memory/map/generated/inventories.json`
- `memory/map/generated/MAP.md`

### Alternatives rejected

- **Two batch units split by kit.** Every half writes `tools/policy/policy.py` or
  `tools/policy/check_policy.py`, and both move functions the codebase map regenerates from, so M6's
  first and third clauses fail.
- **A fix per spec text.** Nothing is folded at this exit (BUILD-METHOD M4; §3).

## 5. Production-readiness checklist

- security — S16 and S38 close two fail-open paths in rule 7, S21 a swallowed guard miss, and S31
  a refused reader read as `warn`. No item widens a write surface.
- perf / scale — S16 adds at most one bash probe per hook process; S20 makes two scans one.
- error / empty / loading states — S5, S10, S13, S15, S16 and S38 each give a state an outcome.
- observability — each new refusal and announce line names its file, step or arm.
- risks — S7 and S9 move canonical blocks other kits inline; the parity rows hold them, and their
  population arm reds a row whose copies vanish.
- testing — the cases in §4's inventory under `--fixture`, the suites on §7's arm lines, and AC1 to
  AC41.
- migration — `.governance/policy.json` re-rendered with `legacy_blobs`; the codebase map
  regenerated; the memory-tree, codebase-map, hooks and kickoff kits' version markers move with their
  shipped bytes.
- user docs — `help/agent-limit.md` (S40); the policy kit README (S3, S6, S17, S26, S34).

## 6. Acceptance criteria

Every command runs from the repository root. The criteria spell the policy kit's files by bare name,
`policy.py`, `check_policy.py`, `policy-mirror.js`, `budgets.py`, `adopt-policy.sh`,
`adopt-policy.test.sh`, `kit.toml`, `README.md` and `caps.toml` under the kit, and `policy.toml` and
`policy.json` under `.governance/`, as `TOOL-dGroundRules-5` §6 does, because the spec-token checker
grades a path-shaped token in a criterion against the tracked set and this build creates them. Each
`--fixture <case>` runs `python check_policy.py --fixture <case>` and passes when it prints no
`WRONG`. Each fixture repository sits under `%TEMP%`, short-named.

- **AC1** — When `python policy.py scaffold` is piped to `od -c` on this node, no `\r` appears, and
  its bytes equal the policy file's blob as `git show` prints it at HEAD.
  Red when: the scaffold writes CRLF through a text-mode stdout.
- **AC2** — When `git check-attr eol` runs over the policy file, `catalogue.toml`, `caps.toml`,
  `legacy-homes.txt` and `unsummarised-keys.txt` under the kit, each prints `eol: lf`.
  Red when: a parsed policy file checks out CRLF under `core.autocrlf=true`.
- **AC3** — When `grep -c "gov:kit policy@" README.md` runs under the kit it prints `1`, and
  `grep -n "version_from" kit.toml` prints the line naming `KIT_POLICY_VERSION`.
  Red when: the registry entry has no version source or no marker, which govkit selfcheck 5c reds.
- **AC4** — When `python tools/memory-tree/check-arms.py --report` runs, it names
  `adopt-policy.sh`'s sibling suite as arming each of its refusal branches and pins none; and
  `bash adopt-policy.sh --check --target <t>` over a scratch target whose policy file sets
  `runtime.agents-in-flight = 0` exits 1, the branch the suite arms.
  Red when: an `exit 1` site of the adopter has no arm and no pin.
- **AC5** — When `--fixture adopter-fresh-target` runs, `arm_schema`, the reader-coverage arm and
  `arm_mirror_readers` each print `not graded` and no finding over the fresh target; and a `finding`
  arm planted with population 0 prints one finding.
  Red when: a legal empty population reds, or an empty `finding` arm passes.
- **AC6** — When `grep -c "unattended/unattended.sh:9517" README.md` runs under the kit it prints `1`,
  and the same section names the other three copies.
  Red when: the kit's own account of the legacy reader names three copies.
- **AC7** — When the `compare_base_py` block is cut from `map_lib.py` under `tools/codebase-map/`,
  from `policy.py` and from its canonical `compare_base.py` under `tools/lib/` with the parity
  arm's awk range, the three cuts are identical; with one byte changed in the policy copy,
  `git grep -n "# >>> compare_base_py"` still lists it and the cut differs.
  Red when: the copied compare base has no canonical to drift from.
- **AC8** — When `grep -c '^def resolve_remote' policy.py` runs it prints `1`, and an `awk` that skips
  the `# >>> remote_ladder_py` range, piped to `grep -nE '"remote"|remote get-url|remote -v'`, prints
  nothing.
  Red when: the reader reads a remote outside the canonical ladder.
- **AC9** — When the `git_env_leaks_py` block is cut from `policy.py` and from
  its canonical `git_env_leaks.py` under `tools/lib/`, the cuts are identical, and the tuple
  equals the one `tools/memory-tree/tree_lib.py` holds.
  Red when: the reader's list of stripped variables can drift unseen.
- **AC10** — When `--fixture on-invalid-utf16` runs, with V valid and C written as UTF-16LE,
  `policy.py get budgets.enforce --explain` prints V's value with source `last-valid` and a reason
  holding `not UTF-8`.
  Red when: the reader dies with a traceback on a file a PowerShell redirect wrote.
- **AC11** — When `grep -n "read_blob_at(" policy.py budgets.py` runs, it prints the definition, the
  call in `read_policy_text` and the limits read in `budgets.py`.
  Red when: unit 9 reads a blob through a reader unit 2 never defined.
- **AC12** — When `--fixture resolution-derived-default` plants a row whose default is
  `{ derived = "x" }`, `policy.py get` on it exits 2 naming the row and `a derived default`, and the
  mirror rendered there holds no such key.
  Red when: a derived default resolves to, or is mirrored as, an inline table.
- **AC13** — When `--fixture on-invalid-shallow` clones a repository whose V precedes C at
  `--depth 1` and reads a key at C, it exits 2 printing `history is shallow`.
  Red when: a shallow clone refuses with the false reason that no valid revision precedes.
- **AC14** — When `--fixture mirror-landed-parity` runs with a stub `bash` that exits 127 placed first
  on `PATH`, the case still passes and names the bash it used.
  Red when: the shim runs under a launcher that cannot see the kit's path.
- **AC15** — When `--fixture mirror-absent-adopter` runs over a target whose HEAD carries neither the
  policy file nor a mirror, and over one with no commit, `arm_mirror_parity` and `arm_on_invalid`
  each print an announce line and no finding.
  Red when: an adopter reds on a mirror nothing there writes.
- **AC16** — When `--fixture mirror-shim-exit-one` points the helper at a shim exiting 1, then at one
  killed by a signal, `node policy-mirror.js get budgets.enforce` exits 2 each time with a
  `PolicyRefusal` naming the status.
  Red when: a non-2 shim exit returns an undefined value or throws a non-refusal.
- **AC17** — When `--fixture mirror-stale-legacy` lands a change to `.agent-cap.conf` alone and keeps
  the old mirror, the helper reads the mirror STALE, its reason opening `mirror stale at`.
  Red when: a conf-only landing leaves the mirror fresh with the old limit.
- **AC18** — When `--fixture mirror-direct-reader` runs it is RED as planted; and a tracked `.js` whose
  only mention of `policy.json` is a `//` comment leaves `arm_mirror_readers` green.
  Red when: a comment or a test's data reds the class arm.
- **AC19** — When `git check-attr eol` runs on the mirror `policy.json` by its full path under
  `.governance/`, it prints `eol: lf`.
  Red when: the mirror's pin names another spelling of the path.
- **AC20** — When `grep -c "def arm_single_reader" check_policy.py` runs it prints `1`, and
  `grep -nE "def arm_(mirror|limits)_readers" check_policy.py` prints nothing, both arms being rows.
  Red when: two scanners of one predicate remain.
- **AC21** — When a scratch repository whose `core.hooksPath` holds a copy of `.githooks/pre-commit`,
  whose kit lacks `guard.py` while `guarded-paths.txt` stays at HEAD, runs `git commit` staging the
  policy file from this run's shell, the commit exits non-zero printing `policy guard`.
  Red when: a missing guard reads as a clean commit.
- **AC22** — When `--fixture guard-admits-raise`, `guard-lowered` and `guard-class-row` run, the
  first admits the dotted, slashed key's raise, the second refuses its lowering, and the third refuses
  the spec-folder class row of the limits file.
  Red when: the guard's key handling is proved only on one-segment names.
- **AC23** — When `grep -c "resolve_compare_base(" policy.py` runs it prints the definition and one
  call, in `cmd_lists`.
  Red when: the legacy list reads a second base.
- **AC24** — When `--fixture legacy-homes-main-dropped` runs, `lists --check` reports no
  `new legacy home`.
  Red when: a branch opened before main dropped a key reds as adding one.
- **AC25** — When `--fixture reader-coverage-relocated` runs with the kits at a non-default prefix, the
  reader-coverage arm grades the landed owners or refuses, and never prints a population of 0.
  Red when: a relocated install grades nothing and passes.
- **AC26** — When `grep -n "requires" kit.toml` runs under the kit it names `memory-tree`, and with the
  memory-tree kit removed from a scratch copy the reader-coverage arm exits 1 naming where the
  resolver looked.
  Red when: an `ImportError` reads as "no build landed".
- **AC27** — When `--fixture reader-quoted-pattern` plants `resolve(f'budgets."{cap}"')`, the arm reads
  `budgets.*` as having a reader; and `grep -c 'parse_key("policy-file.on-invalid")' policy.py`
  prints at least `1`.
  Red when: a correct build of units 4 and 9 leaves reader coverage red.
- **AC28** — When `--fixture budgets-zero-cap` sets a cap to 0, `policy.py check` exits 0 and the
  enforcer reads the cap as unchecked.
  Red when: a cap whose home holds 0 today cannot be carried.
- **AC29** — When `arm_limits_readers` runs over this repository, it names neither
  `tools/memory-recall/extract.py` nor `tools/check-spec-tokens.py:159`.
  Red when: a docstring counts as a reader.
- **AC30** — When `--fixture limits-reader-docstring` runs it stays green, and `python check_policy.py`
  over this repository reports no `arm_limits_readers` finding at this unit's commit.
  Red when: the arm's own population holds a file outside its write set.
- **AC31** — When `--fixture budgets-reader-refused` plants two remotes and no `GOV_REMOTE` with a
  subject over its cap, the enforcer refuses and prints the ladder's refusal once; and
  `check-template-size.sh` with no launcher refuses an over-cap subject and says why.
  Red when: a refused reader reads as `warn`, or a missing launcher passes.
- **AC32** — When `grep -n "AGENT_CAP" memory/map/features/agent-cap.md` runs, no line it prints says a
  set `AGENT_CAP` is refused.
  Red when: the map card teaches a retired rule as live.
- **AC33** — When `grep -c "AGENT_CAP=7" tools/workflows/check-review-join.test.sh` runs it prints `0`,
  and the D7 arm still prints `is its own refusal and not a join`.
  Red when: D7 depends on a refusal the hook no longer makes.
- **AC34** — When `--fixture limit-settings-elsewhere` sets `GOV_SETTINGS_JSON` to another path,
  `policy.py settings --write` writes that file and rule 7 grades it.
  Red when: the render and rule 7 grade a file that is not in force.
- **AC35** — When `grep -nE "boundedParallel\(thunks, [0-9]+\)|integer ≤[0-9]+" tools/hooks/README.md`
  runs, no line it prints describes the raw-primitive ban or the clamp as denied, and
  `grep -c "bounded-helper width" tools/check-playbook-parity.sh` prints `0`.
  Red when: a parity row extracts nothing and prints `PAIRFAIL`.
- **AC36** — When `git grep -l "gov:kit agent-cap@1.40" -- '*.js'` runs it prints nothing.
  Red when: a carrier keeps the old marker and the kit-version leg reds.
- **AC37** — When `--fixture limit-fresh-target-spawn` installs the hooks and policy kits into a
  committed fresh target and runs `adopt-policy.sh --scaffold`, the first `Agent` payload through
  `node tools/hooks/agent-cap.js` exits 0.
  Red when: an adopter cannot spawn until it runs the render by hand.
- **AC38** — When `--fixture limit-hook-settings-malformed` and `limit-hook-reader-throws` run, each
  payload exits 2 through `node tools/hooks/agent-cap.js`, naming the file or the step.
  Red when: a throw in rule 7 exits 1, which a PreToolUse hook does not block on.
- **AC39** — When `grep -cE "git show [0-9a-f]{7,40}:" tools/hooks/agent-cap.test.sh` runs it prints
  `0`.
  Red when: the suite reads its oracle from a historical sha.
- **AC40** — When `grep -n "os.replace" policy.py` runs it names the settings write, and
  `grep -n "UNVERIFIED" agent-limit.md` names the restart claim.
  Red when: the settings file is rewritten in place, or the claim stands as fact.
  permission: the two-halves probe needs live harness sessions; the main loop observes it at the
  close and records the answer.
- **AC41** — When `python tools/codebase-map/gen_map.py --check` runs at this unit's commit it exits 0.
  Red when: the map still describes functions units 2 to 10 added or retired.

## 7. Gates

`agent-cap self-test` · `scratch-guard self-test` · `format-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `tier2-review self-test` · `unattended-build self-test` · `playbook parity` · `playbook parity selftest` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `codebase-map coverage + freshness` · `line-length gate selftest` · `govkit acceptance matrix` · `govkit selfcheck` · `manifest-check self-test` · `lexicon naming predicates` · `kit/dogfood doc parity` · `transition-audit arms` · `straggler-guard arms` · `harness arms (fail branches armed or pinned)` · `install-prefix (shipped surface)` · `python resolver (behaviour + inline parity + idiom ban)` · `branch-guard self-test` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `memory hygiene` · `recall floor` · `recall floor arms` · `policy fixtures`

The policy legs `TOOL-dGroundRules-1` declares run the cases; they are named by the arm lines, because
neither exists at this spec's base.

New arm: tools/policy/check_policy.py --fixture · covers AC10 AC12 AC13 AC14 AC15 AC16 AC17 AC18 AC22 AC24 AC25 AC27 AC28 AC30 AC31 AC34 AC37 AC38 · each case named in §4's inventory, planting its input in its temporary repository and asserting its stated outcome · none
New arm: tools/policy/adopt-policy.test.sh · covers AC4 · each refusal branch of `adopt-policy.sh` planted in a scratch target · `ARMS_FLOORS`, its new row for `adopt-policy.sh`
New arm: tools/lib/resolve-python.test.sh · covers AC7 AC9 · the `compare_base_py` and `git_env_leaks_py` rows, staged by one byte changed in the policy copy · that suite's assertion count, raised by the two rows
New arm: .githooks/pre-commit.test.sh · covers AC21 · `guard.py` removed with its list at HEAD and a listed path staged · that suite's assertion count, raised by the arm
New arm: tools/workflows/check-review-join.test.sh · covers AC33 · the D7 arm re-planted with a stub predicate exiting 2 before any rule · none

## 8. Open questions

- **F1 — Who writes the harness's `env` keys in `.claude/settings.json` (finding 21)?** (a) The policy
  kit's render, as S34 states it: settings-merge owns hook entries, the policy kit owns
  `env.CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` and `env.CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS`. Not an `env` mode in `tools/settings-merge.py`,
  which changes a separately versioned copy-installed kit's fragment contract, a public surface the
  grant's words for `cl-dClosedLoop-0016` do not name (veto 2). Rung 3. RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none
- **F2 — How is the reader's git location-variable list held (finding 24)?** (a) A canonical block in
  `tools/lib/` inlined in `policy.py` and graded by a parity row, over a set-equality check: it reuses
  the inline-block seam and gives `TOOL-dRetiredFork-23` its canonical. Rung 3. RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none
- **F3 — How is the copied compare base held (finding 29)?** (a) A canonical `compare_base_py` block
  inlined in both copies; a deviation record would still owe the check this is. Rung 3. RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none
- **F4 — Is a derived-default key in the mirror (finding 3)?** (a) Omitted, so the helper reads it
  through the reader and refuses; a refusal record would add a value shape every JS consumer must
  test for. Rung 3. RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none
- **F5 — What does `budgets.<cap> = 0` mean (finding 8)?** (a) Unchecked, as each enforcer reads 0
  today, so `check_budgets` admits non-negative integers; refusing it cannot carry
  `INDEX_CAP_LINES="0"` or `DOSSIER_CAP_LINES="0"`, which the census holds, and fails AC28 (veto 1).
  Rung 1: unit 9's data model says 0 "keeps meaning unchecked". RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none
- **F6 — How does the policy kit reach `tree_lib` (finding 6)?** (a) The inlined `resolve_kit_dir` and
  a declared `requires`, a miss refusing, as `tools/memory-recall/extract.py:105-121` does, the seam M5
  found; inlining the four names would copy `TERMINAL` and `HDR_RE` ungated. Rung 3. RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none
- **F7 — How is `adopt-policy.sh`'s refusal armed (finding 41)?** (a) A sibling suite run by the
  fixture mode, with its floor row; a pin in `memory/project/unarmed-branches.txt` observes nothing.
  Rung 3. RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none
- **F8 — How does reader coverage see units 4 and 9's reads (finding 7)?** (a) Unit 8's pattern
  segment admits a quoted segment and unit 4 spells its read as a literal; reading `budgets.*` from
  the census join would special-case one key family. Rung 3. RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none
- **F9 — Where does the refused-reader rule live (finding 44)?** (a) Once, in `budgets.py`, with the
  four shell enforcers' no-launcher branch, not ten spellings of one rule (`[core]`). Rung 3. RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none
- **F10 — How do the stale agent-cap markers move (finding 38)?** (a) By hand, marker text only, in
  this unit; `govkit.py mint` at the landing leaves the `kit version markers` leg red on every bar
  before it. Rung 3. RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none
- **F11 — Who owns the blob reader unit 9 consumes (finding 10)?** (a) `read_blob_at` in `policy.py`,
  which `read_policy_text` calls, not a second git blob read in one kit. Rung 3. RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none
- **F12 — What happens to the playbook-parity rows (finding 33)?** (a) Retire the bounded-helper row
  and re-point the resolved-K row to rule 2's sentence; keeping both sentences teaches retired rules
  as live, which AC35 forbids. Rung 3. RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft from the round-1 spec audit's forty-one MEDIUM and LOW findings.
- rev-2 · 2026-10-23 · §3 · hands-off edge to TOOL-dGroundRules-25 added.
- rev-3 · 2026-10-23 · §3 · hands-off edges to TOOL-dGroundRules-61, TOOL-dGroundRules-62 and TOOL-dGroundRules-64 added.
- rev-4 · 2026-10-23 · §1 §2 §4 §5 §8 §10 · prose shortened under the spec ceiling; no meaning moved.
- rev-5 · 2026-10-23 · §1 §3 §4 · TOOL-dGroundRules-13 renamed TOOL-dGroundRules-65 by the owner's ruling.
- rev-6 · 2026-10-24 · §7 §9 · the policy fixtures leg added to the leg line, owed by its guard, which a §4 path trips; older revision lines condensed under the spec ceiling; no design change.

## 10. Reuse audit

Each item extends the seam its row names: the parity rows of
`tools/lib/resolve-python.test.sh` (S7, S9), `resolve_bash` of `tools/run-gates/profile_bar.py:282`
(S14, S16), `resolve_kit_dir` as `tools/memory-recall/extract.py:105-121` uses it (S25, S26),
`print_kit_miss` in `.githooks/pre-commit` (S21), the `GOV_SETTINGS_JSON` rule of
`tools/check-wiring.sh:94-117` (S34), `check-arms.py`'s sibling-suite rule (S4) and
`gen_map.py --write` (S41). `python tools/codebase-map/reuse_lookup.py "guard paths of a held selftest
leg covering sibling kit files"` and `python tools/codebase-map/reuse_lookup.py "install a kit into a
fresh target and run its check"` ranked `resolve_kit_dir` (`tools/lib/resolve_kit_dir.py`) among
name-stem hits; the other seams came from the files the review cites, each verified at base, and no
hit disagreed with source. The recall probe returned `TOOL-aProbedUnit-9` and
`TOOL-aEvidencedLens-20`, a prior minors batch whose per-finding table this unit follows, and
`TOOL-cMendedVintage-19`, all agreeing with BUILD-METHOD M4.

Recall terms used: `python tools/memory-recall/query.py "how are review minors batched into one
repair unit" --terms "minors batch promoted medium low disposed severity spec-audit repair unit write
set"`
