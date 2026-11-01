# TOOL-dScopedBuild-35 — the round-1 spec audit's 38 minors, batched: 32 MEDIUM and 6 LOW findings, each its own scope item

**Status:** DEFERRED · rev-3 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 16 · advances TOOL-dScopedBuild-16

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dScopedBuild-1-agent-ledger.md) | journal | TOOL-dScopedBuild-1 TOOL-dScopedBuild-2 TOOL-dScopedBuild-3 TOOL-dScopedBuild-4 TOOL-dScopedBuild-5 TOOL-dScopedBuild-6 TOOL-dScopedBuild-7 TOOL-dScopedBuild-8 TOOL-dScopedBuild-9 TOOL-dScopedBuild-10 TOOL-dScopedBuild-11 TOOL-dScopedBuild-12 TOOL-dScopedBuild-13 TOOL-dScopedBuild-14 TOOL-dScopedBuild-15 TOOL-dScopedBuild-25 TOOL-dScopedBuild-26 TOOL-dScopedBuild-27 TOOL-dScopedBuild-28 TOOL-dScopedBuild-29 TOOL-dScopedBuild-30 TOOL-dScopedBuild-31 TOOL-dScopedBuild-32 TOOL-dScopedBuild-33 TOOL-dScopedBuild-34 TOOL-dScopedBuild-36 TOOL-dScopedBuild-37 TOOL-dScopedBuild-38 TOOL-dScopedBuild-39 TOOL-dScopedBuild-40 TOOL-dScopedBuild-41 TOOL-dScopedBuild-42 TOOL-dScopedBuild-43 |
| [2026-11-01-prompt-TOOL-dScopedBuild-25-promoted-fix-brief.md](../prompts/2026-11-01-prompt-TOOL-dScopedBuild-25-promoted-fix-brief.md) | research | TOOL-dScopedBuild-25 TOOL-dScopedBuild-28 TOOL-dScopedBuild-31 TOOL-dScopedBuild-32 TOOL-dScopedBuild-33 |
| [2026-11-01-review-TOOL-dScopedBuild-25-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dScopedBuild-25-spec-audit-round1.md) | spec-audit | TOOL-dScopedBuild-32 TOOL-dScopedBuild-33 TOOL-dScopedBuild-30 TOOL-dScopedBuild-28 TOOL-dScopedBuild-34 TOOL-dScopedBuild-27 TOOL-dScopedBuild-29 TOOL-dScopedBuild-31 TOOL-dScopedBuild-26 TOOL-dScopedBuild-25 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 1 to 15
(`memory/builds/dScopedBuild/reviews/2026-11-01-review-TOOL-dScopedBuild-1-spec-audit-round1.md`)
exited CONVERGED with 48 confirmed findings: ten at HIGH, which `TOOL-dScopedBuild-25` to
`TOOL-dScopedBuild-34` take, and 38 minors. BUILD-METHOD M4 batches every MEDIUM and LOW into one
unit, two only where they split into disjoint write sets by M6; §4 "Why one unit" says why these stay
one. Each finding is named by report id and is its own scope item, ids 12 and 13 included, which the
report merged into item M8. The minors land on all fifteen units, so this unit repairs no one unit
and builds after every unit of the build (order 16).

| Report item | Severity | Report id | Lands on | Scope item |
|---|---|---|---|---|
| M1 | MEDIUM | 4 | unit 7 S3, §4; unit 1 S4 | S1 |
| M2 | MEDIUM | 5 | units 4 S1, 13 S8; units 1, 7, 14 fixtures | S2 |
| M3 | MEDIUM | 6 | unit 5 S2, S4, §4, §5 | S3 |
| M4 | MEDIUM | 15 | unit 14 §5, §4 | S4 |
| M5 | MEDIUM | 16 | unit 9 S1, AC1 | S5 |
| M6 | MEDIUM | 18 | unit 10 §5, S1, S3 | S6 |
| M7 | MEDIUM | 21 | unit 3 S7, Files | S7 |
| M8 | MEDIUM | 12 | unit 14 AC9, S8 | S8 |
| M8 | MEDIUM | 13 | unit 2 AC6 | S9 |
| M9 | MEDIUM | 25 | unit 4 S3, §10 | S10 |
| M10 | MEDIUM | 26 | unit 7 S4 | S11 |
| M11 | MEDIUM | 27 | unit 1 S5, S7, Files, §7 | S12 |
| M12 | MEDIUM | 28 | unit 7 S3, S8, Files, §7 | S13 |
| M13 | MEDIUM | 29 | unit 11 S1, S8, Files | S14 |
| M14 | MEDIUM | 31 | unit 12 Files, §7 | S15 |
| M15 | MEDIUM | 32 | unit 13 S10, Files, §7 | S16 |
| M16 | MEDIUM | 33 | units 10, 7, 11 Files, §7 | S17 |
| M17 | MEDIUM | 34 | unit 3 S7, Files | S18 |
| M18 | MEDIUM | 37 | unit 14 S7, §4 | S19 |
| M19 | MEDIUM | 38 | unit 2 S1, §5 | S20 |
| M20 | MEDIUM | 39 | unit 1 S6 | S21 |
| M21 | MEDIUM | 40 | unit 1 S2 | S22 |
| M22 | MEDIUM | 41 | unit 10 S1, S4 | S23 |
| M23 | MEDIUM | 42 | unit 6 S1, §4 | S24 |
| M24 | MEDIUM | 43 | unit 5 S1, S4, §5 | S25 |
| M25 | MEDIUM | 44 | unit 3 S2, S8 | S26 |
| M26 | MEDIUM | 45 | unit 8 S3, §5 | S27 |
| M27 | MEDIUM | 46 | unit 9 S1, S3 | S28 |
| M28 | MEDIUM | 47 | unit 12 S9, S10 | S29 |
| M29 | MEDIUM | 48 | unit 4 S7, S8 | S30 |
| M30 | MEDIUM | 49 | unit 11 S6 | S31 |
| M31 | MEDIUM | 50 | unit 14 S6, §4; unit 3 S4 | S32 |
| L1 | LOW | 7 | unit 15 S7, AC10 | S33 |
| L2 | LOW | 8 | unit 11 S7; units 14 S6, 7 S4 | S34 |
| L3 | LOW | 9 | unit 5 AC8 | S35 |
| L4 | LOW | 10 | unit 4 §4 | S36 |
| L5 | LOW | 11 | unit 3 S3; unit 9 S2, S5 | S37 |
| L6 | LOW | 35 | unit 13 §7 | S38 |

That is 32 MEDIUM and 6 LOW findings by raw id. Every item supersedes or completes a clause of the
unit it lands on by name; that unit's §3 names the item, and its acceptance ledger answers the
clause with a note naming this unit's scope item.

## 2. Scope (IN)

- **S1** — id 4. One red reading. `read_build_exit_red <slug> <R> <rc> <dir>` in
  `tools/unattended/unattended.sh` holds unit 1's exit table and unit 7's core arm, reads only, and
  returns 0 pass, 1 refuse, 2 unusable (`GR_STATE` `moved` or `none`, or an rc the table does not
  read). `check_build_exit` calls it, then runs its writing arms; `run_build_core` calls it alone,
  skipping `routed_commits.py --build --write`, the closing-review predicate, the ratification and
  the upstream term, and files only its core asks (S11) and its record. `--build-core` exits 1 on
  its return 2 alone. Observed by AC1.
- **S2** — id 5. The earlier exits' fixtures. The driver suite's exit fixture that unit 1 AC5 and AC7,
  unit 7 AC4 and AC5 and unit 14 AC7 build gains a tracked diff-review record naming a commit in its
  range and an upstream record, so those criteria still pass once unit 4's and unit 13's arms refuse
  on the absences. Observed by AC2.
- **S3** — id 6. One spelling. Unit 5's answer reads `"lease": "dispatched|attended|undeclared"`, an
  empty lease `undeclared`, and the hook calls `readUnitLease(top, build, unit, rel)` at every site;
  unit 5 S2's "S1's `derive_kit_dir`" is TOOL-dScopedBuild-3 S1's. Observed by AC3.
- **S4** — id 15. The staged population, bounded. `deviation_join.py --staged` builds its facts from
  the one `read_routed_commits(root, ["HEAD"])` pass and the first passes and pins of the staged
  specs' units alone, never the whole `read_population`; the verb's wall time over this tree with one
  staged spec is measured at the pass and pinned in unit 14's ledger. Observed by AC4.
- **S5** — id 16. `read_touched_hunks`' argv gains `--root`, so a root commit's hunks are read, as
  `read_routed_commits` reads them (`tools/memory-tree/routed_commits.py:232`). Observed by AC5.
- **S6** — id 18. The reproduction gate's cost, stated and bounded. Each `ASKS_CMD <id>` call costs
  about 8.1 s at `c891f007` (the report's measurement, PINNED), paid once per `closes` or `advances`
  id at every `--dispatch`; each call runs under `RB_BOUND=60`, PINNED, and a timeout is unit 10 S4's
  `fail 49`. Observed by AC6.
- **S7** — id 21. `scope` registered. `python tools/memory-tree/record_kinds.py new scope --tag
  record.scope --writer "routed_commits.py --build --write" --check "routed-commits selftest"`
  (TOOL-dTotalRecall-1 S9) writes its row to `tools/memory-tree/record-kinds.toml`. The kind joins
  `RECORD_KIND_TOKENS`' untyped half, as PLAY-dOrderedCharter-42 S1 splits the tuple, and not
  `TYPED_RECORD_KINDS`, because unit 3 names its record `-scope.md` and the tree holds
  `2026-10-11-build-TOOL-aBriskPreflight-3-wiring-scope.md`. Observed by AC7.
- **S8** — id 12. Unit 14 AC9 runs `check-memory-hygiene.sh --staged` alone in the hygiene suite's
  scratch tree and greps its `check 32` line, in place of `--staged --only 32`, which the parser
  refuses (`tools/memory-tree/check-memory-hygiene.sh:41-44`). Observed by AC8.
- **S9** — id 13. Unit 2 AC6 likewise runs `--staged` alone and greps the `check 32` and `frozen`
  lines. Observed by AC9.
- **S10** — id 25. A unit's commits by I8. `python routed_commits.py --unit-commits <unit> <range>`
  prints the non-merge shas `extract_unit_ids` (`:119`) attributes to the unit by subject and `Pass:`
  trailer, the union; unit 4 S3's `per-unit` reads its commits from it in place of
  `read_attribution_tokens`. Observed by AC10.
- **S11** — id 26. The core asks through the one filer. `read_build_exit_red`'s core arm prints one
  `ask · core · CORE LEG <leg> RED · accept <leg> green at the build's tip, attributed against the
  advertised tip` line per refused core leg, and `write_gate_asks` (unit 14 S6) files them; unit 7
  S4's own compose and dedupe are not built. Observed by AC11.
- **S12** — id 27. `--build-exit` in the unattended Skill. `tools/unattended/SKILL.template.md` and
  its render `.claude/skills/unattended/SKILL.md` carry one `unattended.sh --build-exit <slug>`
  invocation, which check 26 asks of every `VERBS_SLUG` verb, and the render stays at or under 10240
  bytes CR-stripped by §8 F2's trim. Observed by AC12.
- **S13** — id 28. `--build-core` wired. The verb joins `VERBS_SLUG`, the usage header and the
  dispatch case as unit 1 S5 wires `--build-exit`, and the Skill carries one `unattended.sh
  --build-core <slug>` invocation within the same budget. Observed by AC13.
- **S14** — id 29. `--record-piece --unit`. The Skill's `--record-piece` line
  (`tools/unattended/SKILL.template.md:90`) and the attended form in `tools/unattended/VERBS.template.md`
  (`:665`) pass `--unit <id>`, within the same budget. Observed by AC14.
- **S15** — id 31. `memory/map/features/codebase-map.md` claims `codebase-map reuse-check fixtures`
  in its `gate-legs` list, and `gen_map.py --write` regenerates `memory/map/generated/`. Observed by
  AC15.
- **S16** — id 32. `memory/map/features/review-harnesses.md` claims `review rows fixtures`, and the
  map is regenerated. Observed by AC16.
- **S17** — id 33. Every shell function units 7, 10 and 11 add to `unattended.sh` is in the
  regenerated `memory/map/generated/symbols.json`. Observed by AC17.
- **S18** — id 34. The `**Serves:**` `<kind>` list of `tools/memory-tree/HYGIENE.template.md` and
  `memory/HYGIENE.md` names `scope` and its meaning, through the registry's region where
  TOOL-dTotalRecall-1 S6 has made the list one. Observed by AC18.
- **S19** — id 37. The staged deviation arm reads unit 2 S2's population: every staged spec path with
  a `HEAD` pre-image, a modification, a deletion or a rename from it; the unit read from the `HEAD`
  blob's H1; a deletion and a rename with a change each a revision. Observed by AC19.
- **S20** — id 38. The freeze's freshness stated. Unit 2's frozen arm prints
  `frozen: landed read at <ref> <sha8> — as fresh as this clone's last fetch` once per run; no second
  read of `CLOSED` at another ref is added. Observed by AC20.
- **S21** — id 39. The overridden close's fallback. With neither `GG_BAR_RC` nor `GG_BAR_DIR` set,
  unit 1 S6's term reads the rc from the `gates-run` fact's run dir's `verdict` file, GREEN as 0 and
  RED as 1, refuses when that file is unreadable, and refuses when the fact's sha8 is not HEAD's.
  Observed by AC21.
- **S22** — id 40. The base by ancestry. Unit 1 S2's oldest first pass is the one no other first pass
  is an ancestor of, read over the log pass's parent map with `deviation_join.read_ancestors`
  (`tools/memory-tree/deviation_join.py:312`); committer date breaks a tie between unrelated passes
  only. Observed by AC22.
- **S23** — id 41. An unfiled ask is unreadable. Where `ASKS_CMD <id>` prints `is filed in no tracked
  BACKLOG.md`, or no header line for the id, unit 10's gate refuses the dispatch with `fail 49`
  naming the ask. Observed by AC23.
- **S24** — id 42. Unit 6's refusal matches the program and mode,
  `gotchas\.py["']?\s+["']?--for-(paths|diff)\b`; under `--for-diff` it refuses a range whose base is
  a HEAD-relative one-commit expression, `HEAD~1`, `HEAD~`, `HEAD^`, `@~1` or `@^`, quoted or not,
  and admits `<sha>..HEAD`. Observed by AC24.
- **S25** — id 43. `readUnitLease`'s `spawnSync` carries `timeout: 20000`, below the 60 s hook
  timeout (`tools/hooks/agent-cap.js:149`), as `policy-mirror.js:73` bounds its probe; expiry is a
  refusal naming `timeout`. Observed by AC25.
- **S26** — id 44. The dispatch-row spawn resolves bash by `corpus_ids.resolve_bash()`
  (`tools/memory-tree/corpus_ids.py:390`): `GOV_BASH`, then each `PATH` candidate run and skipped
  under `/system32/` or `/windowsapps/`. A failed or non-zero spawn is a `Refusal`, the leg's exit 2
  and unit 5's `error` answer. Observed by AC26.
- **S27** — id 45. `read_site_lines` sends the touched paths on stdin, one per line, as unit 9 S3
  does, and an `OSError` at the spawn is the population's `not-installed: <why>`. Observed by AC27.
- **S28** — id 46. The touched-path set in full. `read_touched_hunks`' one spawn adds `--raw`, whose
  lines give every touched path, binary, pure-rename and mode-only changes included, with
  `-c core.quotePath=false`; a path git still C-quotes is unquoted before it is keyed. Observed by
  AC28.
- **S29** — id 47. Reuse-check status per unit: `stale`, not clean, when one of the unit's own commits
  (I8) touching `ROUTED_PATHS` is not an ancestor of its newest record's `**Head:**`; `not-owed`,
  passing, for a unit with no such commit; the record's own commit makes nothing stale. Observed by
  AC29.
- **S30** — id 48. Unit 4's two reads, in the spelling `TOOL-dScopedBuild-25` S2 gives them, fail
  closed: a `get` exit 2 or a value outside the key's set refuses the exit naming the key and why; a
  kit that does not resolve stays the one `per-build` fallback, and `decisions.major` has none.
  Observed by AC30.
- **S31** — id 49. `--propose` reuses an open ask only when its text equals the composed text, item,
  step and reason; otherwise it files a new ask. Observed by AC31.
- **S32** — id 50. `write_gate_asks` reuses an open ask by a stable key, the deviation's
  `<unit>@rev-<N>` address or the scope finding's unit id, carried in the ask text; the sha and the
  stray path list stay in the text and out of the key. Observed by AC32.
- **S33** — id 7. `fix_keeps.py --keeps reuse-check` prints
  `not-installed: tools/codebase-map/reuse_check.py does not resolve` where `resolve_kit_dir` raises
  `LookupError`, and the module path where it resolves. Observed by AC33.
- **S34** — id 8. `write_gate_asks` passes `build-exit` as `write_ask_rows`' tenth argument (unit 11
  S7), so an exit-time ask, the core asks of S11 among them, logs `build-exit: filed ask`. Observed by
  AC34.
- **S35** — id 9. Unit 5 AC8 greps one fragment per file, each with a hit at base:
  `reads a status the agent writes` over `tools/hooks/scratch-guard.js` and `flipped to INPROGRESS`
  over `tools/hooks/README.md`, both printing nothing after unit 5. Observed by AC35.
- **S36** — id 10. Unit 4 §4's sentence reads that the predicate runs under both DoD items, and that
  `build-complete`'s copy is waived by `--override closing-review-recorded` (unit 4 S1). Observed by
  AC36.
- **S37** — id 11. `check_build_scope(repo, conf, read, id_map, value, at_exit)`: `at_exit` true under
  `--build <slug> --write` and false at the push, passed by unit 9 S2 to `check_touch_join`.
  Observed by AC37.
- **S38** — id 35. Unit 13's pass owes `memory-hygiene self-test` and `spec-tokens self-test`, the
  suites of `tools/check-spec-tokens.py`, which it edits; its ledger names both. Observed by AC38.

## 3. Non-goals (OUT)

- The report's left-shift gates: spec-lint, spec-audit checklist and hook rules, one per item. No
  clause of this build names them.
- The ten HIGH findings and their shared fixes, which units 25 to 34 make.
- Rewording units 1 to 15. Each item supersedes a clause by name, answered in that unit's ledger.
- Raising the unattended Skill's byte budget, §8 F2.

### Edges

- **consumes-from** `TOOL-dScopedBuild-1` — S4's exit body, AC5's and AC7's fixture, S5's verb, S6's fallback and S2's base, which S1, S2, S12, S21 and S22 complete (ids 4, 5, 27, 39, 40)
- **consumes-from** `TOOL-dScopedBuild-2` — AC6's command and S1's landed read, which S9 and S20 restate (ids 13, 38)
- **consumes-from** `TOOL-dScopedBuild-3` — S2's bash spawn, S3's signature, S4's scope subject and S7's record kind, which S7, S18, S26, S32 and S37 complete (ids 21, 34, 44, 50, 11)
- **consumes-from** `TOOL-dScopedBuild-4` — S1's arm, S3's per-unit commits, S7 and S8's reads and §4's sentence, which S2, S10, S30 and S36 complete (ids 5, 25, 48, 10)
- **consumes-from** `TOOL-dScopedBuild-5` — S2 and §4's lease word, S4's call and its spawn, and AC8's grep, which S3, S25 and S35 restate (ids 6, 43, 9)
- **consumes-from** `TOOL-dScopedBuild-6` — S1's refusal pattern, which S24 widens to the class (id 42)
- **consumes-from** `TOOL-dScopedBuild-7` — S3's run, S4's asks, S8's verb wiring and the functions it adds, which S1, S11, S13, S17 and S34 complete (ids 4, 26, 28, 33, 8)
- **consumes-from** `TOOL-dScopedBuild-8` — S3's `read_site_lines` spawn, which S27 bounds (id 45)
- **consumes-from** `TOOL-dScopedBuild-9` — S1's `read_touched_hunks` argv and path set and S2's call, which S5, S28 and S37 complete (ids 16, 46, 11)
- **consumes-from** `TOOL-dScopedBuild-10` — S1, S3 and S4's ask reads and its two functions, which S6, S17 and S23 complete (ids 18, 33, 41)
- **consumes-from** `TOOL-dScopedBuild-11` — S1's `--unit`, S6's reuse, S7's prefix and its functions, which S14, S17, S31 and S34 complete (ids 29, 33, 49, 8)
- **consumes-from** `TOOL-dScopedBuild-12` — the new leg and S9's status, which S15 and S29 complete (ids 31, 47)
- **consumes-from** `TOOL-dScopedBuild-13` — S8's arm, S10's leg and §7's leg line, which S2, S16 and S38 complete (ids 5, 32, 35)
- **consumes-from** `TOOL-dScopedBuild-14` — S6's filer, S7's staged arm, §5's cost, AC7's fixture and AC9's command, which S2, S4, S8, S11, S19, S32 and S34 complete (ids 5, 12, 15, 26, 37, 50, 8)
- **consumes-from** `TOOL-dScopedBuild-15` — S7's `--keeps reuse-check`, which S33 makes safe before unit 12's module exists (id 7)
- **consumes-from** `TOOL-dScopedBuild-25` — S2's spelling of unit 4's two reads, whose refused and out-of-set outcomes S30 grades (id 48)
- **hands-off** `TOOL-dScopedBuild-39` — AC18, S10, S21 and S26, which that unit's S2 to S4, S9, S12, S13 and S19 complete, `--unit-commits` minted by unit 4's build (ids 2, 13, 29, 6, 14, 20, 28)
- **hands-off** `TOOL-dScopedBuild-42` — S32's stable key, by which `write_gate_asks` reuses an OPEN ask, which that unit's S2 join names and whose absence stages its red (id 14)

## 4. Design

### Why one unit

M6's clauses decide a split. Seventeen items write `tools/unattended/unattended.sh` and nine write
`tools/memory-tree/routed_commits.py`, and the Python and shell halves both regenerate
`memory/map/generated/symbols.json`, a generated index with its generator, which clause 3 forbids two
concurrent passes to share. No partition leaves two disjoint write sets, so the minors are one unit.

### Evidence

- `check-memory-hygiene.sh:41-44` refuses `--only` beside any other argument (S8, S9).
- `routed_commits.py:232` reads its log with `--root` (S5); `deviation_join.py:312` is
  `read_ancestors(parents, sha, cache)` (S22); `corpus_ids.py:390-433` is `resolve_bash` (S26).
- `gen_build_index.py --asks TOOL --json` returned 622 rows at `c891f007`, none with a `seen` field,
  PINNED on 2026-11-01, so no projection call carries what S6's gate reads (§8 F3).
- `gen_build_index.py:3313` refuses a second id to `--asks` (S6); `--asks TOOL-nosuch-99` prints `is
  filed in no tracked BACKLOG.md` and exits 0 (the report's id 41) (S23).
- `.claude/skills/unattended/SKILL.md` is 10237 bytes against the 10240-byte row of
  `tools/template-size-limits.txt:154` at `c891f007`, PINNED; that row's comment says growth past it
  "means prose is coming back that belongs in" the verbs carrier's `The paths, in order` section
  (S12 to S14, §8 F2).
- `tools/hooks/agent-cap.js:149` states the 60 s hook timeout and that a timed-out PreToolUse hook is
  non-blocking; `tools/policy/policy-mirror.js:73` bounds its probe at 20000 ms (S25).
- `tools/hooks/scratch-guard.js:89` holds `reads a status the agent writes` and
  `tools/hooks/README.md:364` holds `flipped to INPROGRESS` at base (S35).
- `unattended.sh:12958-12960` names the silent drop an inexact proposal compare causes (S31).
- `tools/unattended/lib-unattended.sh:1144-1155`: `read_attribution_tokens` lets a `Pass:` trailer
  stand in for the subject, which I8's union does not (S10).

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `read_build_exit_red` | shell function, `unattended.sh` | `sh.function`, OK |
| `--unit-commits` | mode of `routed_commits.py` | none |
| `scope`, `record.scope` | record kind and tag, registry row | none |
| `stale`, `not-owed` | reuse-check status words | none |
| `staged-rename`, `staged-delete` | `deviation_join.py` fixture plants | none |

### Rollout

Built at order 16, after every unit, as the disposal rule places a batch landing on several units.
Where an item corrects an interface an earlier unit calls, S37's `at_exit` and S10's mode, that unit's
builder spells the call as the item does, which its §3 hands-off line names, and this unit's pass
observes it.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/lib-unattended.sh`
- `tools/unattended/SKILL.template.md`, rendered to `.claude/skills/unattended/SKILL.md`
- `.claude/skills/unattended/SKILL.md`
- `tools/unattended/VERBS.template.md`, copied to `memory/guides/UNATTENDED-VERBS.md`
- `memory/guides/UNATTENDED-VERBS.md`
- `tools/unattended/fix_keeps.py`
- `tools/memory-tree/routed_commits.py`
- `tools/memory-tree/deviation_join.py`
- `tools/memory-tree/tree_lib.py`
- `tools/memory-tree/record-kinds.toml`
- `tools/memory-tree/HYGIENE.template.md`, rendered to `memory/HYGIENE.md`
- `memory/HYGIENE.md`
- `tools/memory-tree/check-memory-hygiene.test.sh`
- `tools/hooks/scratch-guard.js`
- `tools/hooks/scratch-guard.test.sh`
- `tools/workflows/unattended-unit.js`
- `tools/workflows/unattended-build.test.sh`
- `tools/codebase-map/reuse_check.py`
- `memory/map/features/codebase-map.md`
- `memory/map/features/review-harnesses.md`
- `memory/map/generated/inventories.json`, `memory/map/generated/MAP.md` and
  `memory/map/generated/symbols.json`, regenerated by `gen_map.py --write`

### Alternatives rejected

- **Two units, shell and Python.** Rejected by §4 "Why one unit": `symbols.json` is written by both.
- **One unit per minor.** M4 forbids it.

## 5. Production-readiness checklist

- security — S21, S23, S26, S30 and S25 each turn an unread value into a refusal; nothing widens a
  write path.
- perf / scale — S4 bounds the commit-time read; S6 states and bounds the dispatch's.
- error / empty / loading states — S27, S28, S29 and S33 give the empty and failed cases a named line.
- observability — S20's freshness line, S34's prefix and S1's distinct unusable exit.
- risks — S12 to S14 must fit 10240 bytes; §8 F2 says how.
- testing — the arms of §7, each a fixture or a slice; AC2, AC15 to AC17 and AC38 at the close.
- migration — none; no stored record moves.
- user docs — `memory/guides/UNATTENDED-VERBS.md` and `memory/HYGIENE.md` through their templates.

## 6. Acceptance criteria

- **AC1** — When `--build-core tRun` runs over unit 7's fixture, no `-scope.md` record and no
  `BACKLOG.md` row other than core asks is written; over a planted `moved` record it exits 1, and
  over an own core red it exits 0 writing an `own-red` result.
  Red when: the core run writes the exit's records, or an own red exits 1.
- **AC2** — When `check_build_exit` is sliced over the shared exit fixture after units 4 and 13 are
  built, it returns 0; with the fixture's `diff-review` record taken out it refuses naming the review.
  Red when: an earlier unit's passing exit fixture refuses on a record it never planted.
  permission: observed at the close.
- **AC3** — When `python routed_commits.py --unit-lease tRun TOOL-tRun-9 a.py` runs for a unit with no
  write set, it prints `"lease": "undeclared"`, and `grep -o "readUnitLease([^)]*)"
  tools/hooks/scratch-guard.js` prints one arity at every site.
  Red when: the answer says `none`, or two arities exist.
- **AC4** — When `deviation_join.py --staged` runs at this tree's root with one spec staged, it
  finishes within 15 s, and the pinned figure is written to unit 14's ledger.
  Red when: the verb reads the whole population, which ran past 115 s.
  figure: PINNED at the pass; 15 s is the bound.
- **AC5** — When unit 9 AC1's fixture runs, `read_touched_hunks` returns `(1, 3)` for the root commit's
  hunk beside `(2, 1)`.
  Red when: the root commit yields no pair.
- **AC6** — When `--dispatch` runs with an `ASKS_CMD` stub that sleeps past 60 s, it refuses with
  `fail 49` naming the ask within the bound.
  Red when: the call waits for `GATE_BOUND`.
- **AC7** — When `python -c` loads `record-kinds.toml` with `tomllib`, a `scope` row exists with tag
  `record.scope`, and `tree_lib.RECORD_KIND_TOKENS` holds `scope` while `TYPED_RECORD_KINDS` does not.
  Red when: the kind has no row, or is typed.
- **AC8** — When the hygiene suite's scratch tree stages a memory file and no spec and runs
  `check-memory-hygiene.sh --staged`, the output holds check 32's held line and the exit is 0.
  Red when: check 32 prints nothing under `--staged`.
- **AC9** — When the same scratch tree stages unit 2 AC2's edit, `check-memory-hygiene.sh --staged`
  fails naming `check 32` and `frozen`; staging AC4's status-only edit, it passes.
  Red when: the frozen edit passes the gate.
- **AC10** — When `routed_commits.py --unit-commits TOOL-tRun-1 <range>` runs over a commit whose
  subject names `TOOL-tRun-1` and whose trailer names `TOOL-tRun-2`, it lists it, as the same call for
  `TOOL-tRun-2` does, and unit 4's `per-unit` reads it under both subjects.
  Red when: the trailer hides the subject's unit.
- **AC11** — When `check_build_exit` refuses an own core leg `x`, `write_gate_asks` stages one ask
  whose text names `CORE LEG x RED`; a second exit at the same tip stages none.
  Red when: a second filer composes the ask, or the rerun files twice.
- **AC12** — When `grep -c "unattended.sh --build-exit " tools/unattended/SKILL.template.md
  .claude/skills/unattended/SKILL.md` runs it prints at least 1 for each, and `tr -d '\r' <
  .claude/skills/unattended/SKILL.md | wc -c` prints at most 10240.
  Red when: check 26's Skill join misses the verb, or the render breaches its row.
- **AC13** — When `grep -n -- "--build-core" tools/unattended/unattended.sh` runs it prints the
  `VERBS_SLUG` line, a usage-header line and a dispatch case, and the Skill files carry
  `unattended.sh --build-core `.
  Red when: the verb is unwired in any of the four places.
- **AC14** — When `grep -n -- "--record-piece" tools/unattended/SKILL.template.md
  tools/unattended/VERBS.template.md` runs, every invocation line carries `--unit`.
  Red when: a shipped instruction makes a call the driver refuses.
- **AC15** — When `grep -c "codebase-map reuse-check fixtures" memory/map/features/codebase-map.md
  memory/map/generated/inventories.json` runs after unit 12 lands, each file prints at least 1.
  Red when: the leg is an unclaimed inventory key.
- **AC16** — When `grep -c "review rows fixtures" memory/map/features/review-harnesses.md` runs after
  unit 13 lands, it prints at least 1.
  Red when: the leg is unclaimed.
- **AC17** — When `grep -c "check_reproduction_owed\|read_ask_seen" memory/map/generated/symbols.json`
  runs after unit 10 lands, it prints at least 2, and each function units 7 and 11 add is named too.
  Red when: `symbols.json` is stale for a mapped shell function.
- **AC18** — When `grep -n "scope" tools/memory-tree/HYGIENE.template.md memory/HYGIENE.md` runs, each
  file's `<kind>` list names `scope`.
  Red when: the grammar's closed list contradicts the code.
- **AC19** — When `python deviation_join.py --fixture --plant staged-rename --staged` and `--plant
  staged-delete --staged` run under `refuse`, each exits 1.
  Red when: a renamed or deleted passed spec gets past the commit-time gate.
- **AC20** — When the frozen arm runs over a fixture whose remote holds A `CLOSED` and whose local
  tracking ref predates it, it prints `as fresh as this clone's last fetch` with the ref's sha8 and
  does not refuse A.
  Red when: no freshness line is printed.
- **AC21** — When `--close tRun --override gates-green` runs over a `gates-run` fact whose record
  reads RED with an `x OWN` row, `build-complete` is UNMET naming `x`; with the fact's sha8 not HEAD's,
  it is UNMET naming the sha.
  Red when: an overridden close passes an unread or foreign record.
- **AC22** — When unit 1 AC2's fixture gives the second unit's first pass, a child of the first, an
  earlier committer date, `--build-base tFix` still prints the spec commit's sha.
  Red when: clock skew moves the base.
- **AC23** — When `--dispatch` runs for a unit whose header closes `TOOL-tRun-99`, an ask no
  `BACKLOG.md` holds, it refuses with `fail 49` naming `TOOL-tRun-99`.
  Red when: the unfiled ask reads as "not a bug".
- **AC24** — When unit 6's check runs over grounds spelling `HEAD^..HEAD`, `HEAD~..HEAD`, `@~1..@`,
  `"--for-paths" a` and `--for-diff "HEAD~1..HEAD"`, it refuses each; `--for-diff 1a2b3c4d..HEAD`
  passes.
  Red when: an equivalent spelling of the withdrawn lookup spawns a builder.
- **AC25** — When the hook's lease shim is a stub that sleeps 30 s, the write is refused within 20 s
  naming `timeout`.
  Red when: the hook waits for the harness's 60 s, a non-blocking outcome.
- **AC26** — When `GOV_BASH` names a stub bash that exits 1, `check_routed_commits` exits 2 rather than
  reading the unit `attended`.
  Red when: a failed spawn falls back to the spec's Files touched.
- **AC27** — When `read_site_lines` runs over 2000 touched paths of 200 characters each, it prints a
  result or one `not-installed` line and no traceback.
  Red when: an argv limit crashes the leg.
- **AC28** — When unit 9 AC1's fixture adds a binary change, a pure rename and a non-ASCII path, each
  is a key of `read_touched_hunks`' result, and `GIT_SPAWNS` still rises by one.
  Red when: a touched path that prints no hunk is missing.
- **AC29** — When a product commit of `TOOL-tRun-1` lands after its clean record, `reuse_check.py
  status tRun` exits 1 naming `stale`; a `WONTDO` unit with no commit reads `not-owed` and does not
  block `verb_review`; the record's own commit stales nothing.
  Red when: an old head certifies new code, or an unbuilt unit blocks every round.
- **AC30** — When the fixture's policy sets `review.build.when = "bogus"`, `--build-exit` refuses
  naming `review.build.when`; with the kit uninstalled it grades `per-build`.
  Red when: a refused read grades `per-build`.
- **AC31** — When `--propose` runs twice for one item and step with two reasons, both reasons are
  recorded in open asks.
  Red when: the second proposal is reported filed and written nowhere.
- **AC32** — When two exits run over rebased shas of one unrecorded revision, `write_gate_asks`
  stages one ask.
  Red when: a rebase files a duplicate.
- **AC33** — When `python fix_keeps.py --keeps reuse-check` runs in a tree without the map kit's
  `reuse_check.py`, it prints `not-installed` and exits 0.
  Red when: it raises `LookupError`.
- **AC34** — When `write_gate_asks` files an ask in the driver suite, its log line opens `build-exit:
  filed ask`.
  Red when: an exit-time ask logs as `gates-green:`.
- **AC35** — When `grep -n "reads a status the agent writes" tools/hooks/scratch-guard.js` and `grep
  -n "flipped to INPROGRESS" tools/hooks/README.md` run after unit 5, each prints nothing; each
  printed a line at base.
  Red when: either stale sentence survives.
- **AC36** — When `--close tRun` runs with no diff-review record, both `build-complete` and
  `closing-review-recorded` are UNMET; with `--override closing-review-recorded`, neither names the
  review.
  Red when: the override waives one item and not the other.
- **AC37** — When `python -c` prints `inspect.signature(routed_commits.check_build_scope)`, it lists
  `at_exit`, and unit 9 AC4's exit run writes the grace shrink while its push run does not.
  Red when: the host cannot pass the exit state.
- **AC38** — When `grep -n "memory-hygiene self-test" memory/builds/dScopedBuild/build/*TOOL-dScopedBuild-13*acceptance-ledger*`
  runs at the close, it prints a line, and the same line names `spec-tokens self-test`.
  Red when: unit 13's ledger names neither suite.
  permission: the ledger is written at the close.

## 7. Gates

`unattended kit gate` · `unattended skill size` · `harness arms (fail branches armed or pinned)` · `routed-commits selftest` · `routed commits name a specced unit` · `policy fixtures` · `policy check` · `memory hygiene` · `memory-hygiene self-test` · `spec-tokens self-test` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `check-wiring self-test` · `lexicon naming predicates` · `agent-cap self-test` · `scratch-guard self-test` · `format-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `tier2-review self-test` · `unattended-build self-test` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `codebase-map coverage + freshness` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC6 AC10 AC11 AC13 AC21 AC23 AC29 AC30 AC31 AC32 AC34 AC36 · the driver fixtures for each item, staged by restoring each superseded clause · none

New arm: tools/memory-tree/routed_commits.py · covers AC3 AC5 AC22 AC26 AC27 AC28 AC37 · the selftest's fixtures for each item, staged by the base argv and the date-only base · none

New arm: tools/memory-tree/deviation_join.py · covers AC4 AC19 AC20 · the two staged plants and the stale-ref fixture, staged by the HEAD-blob population · none

New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC8 AC9 · the scratch tree under `--staged`, staged by passing `--only 32` · none

New arm: tools/workflows/unattended-build.test.sh · covers AC24 · the five equivalent spellings, staged by the literal pattern · none

New arm: tools/hooks/scratch-guard.test.sh · covers AC25 · a sleeping shim, staged by spawning without `timeout` · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a)
  `**Derived:**` naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of a repaired unit's clause.
  Fifteen units' clauses would split for one batch. RESOLVED (agent, 2026-11-01, delegated): (a),
  rung 3, the precedent `TOOL-dWitnessedBar-97` §8 F1 set. widens: none · relaxes: none
- **F2 — How does the unattended Skill stay within 10240 bytes (ids 27, 28, 29)?** Options: (a) trim
  Skill prose into the verbs carrier's `The paths, in order` section, bytes out matching bytes in;
  (b) raise `tools/template-size-limits.txt`'s row under the file's run-raise terms. The row's comment
  says growth past it means prose belongs in that section, which (b) contradicts, and (b) needs a
  `memory/DECISIONS.md` row, a shared record. RESOLVED (agent, 2026-11-01, delegated): (a), rung 3,
  the survivor the row's own comment states. widens: none · relaxes: none
- **F3 — How is the reproduction gate's cost bounded (id 18)?** Options: (a) one `--asks <FAMILY>
  --json` read filtered in the driver; (b) a multi-id `--asks`; (c) the per-id cost pinned and each
  call bounded. (a) reads no `seen` field (§4 Evidence), (b) widens the generator's surface for a
  case one id serves, as unit headers here name one ask. RESOLVED (agent, 2026-11-01, delegated): (c),
  rung 3, the survivor. widens: none · relaxes: none
- **F4 — Where does `--keeps reuse-check` live before unit 12's module exists (id 7)?** Options: (a)
  a kit-relative path printed unresolved; (b) `not-installed` where it does not resolve; (c) the
  keeps entry moved into unit 12. (a) prints a path no file backs, and (c) moves a value out of the
  unit that owns `--fix-of`. RESOLVED (agent, 2026-11-01, delegated): (b), rung 3, the most
  feature-rich survivor. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from the round-1 spec audit of units 1 to 15: 32
  MEDIUM and 6 LOW findings, batched.
- rev-2 · 2026-11-01 · §3 · the Edges block gains the bullets mirroring the edges of TOOL-dScopedBuild-39,
  the promotions of the round-1 spec audit of units 25 to 35 (ids 2, 6, 13, 14, 20, 28, 29).
- rev-3 · 2026-11-01 · §3 · the Edges block gains the bullet mirroring the edges of TOOL-dScopedBuild-42, the promotion of the round-1 spec audit of units 40 and 41 (id 14).

## 10. Reuse audit

Each item extends the seam its finding names and spells no second rule: `read_ancestors`
(`tools/memory-tree/deviation_join.py:312`) for S22, `resolve_bash` (`tools/memory-tree/corpus_ids.py:390`)
for S26, `extract_unit_ids` (`tools/memory-tree/routed_commits.py:119`) for S10, `write_gate_asks`
(unit 14 S6) for S11, S32 and S34, the record-kind factory (TOOL-dTotalRecall-1 S9) for S7 and S18,
and unit 2 S2's staged population for S19. `python tools/codebase-map/reuse_lookup.py "file an ask
row from a gate's ask lines at the build exit"` ranked `rows`, `row`, `build`, `build_commit` and
`build_fixture`, none a filer, so the build's own `write_gate_asks` is the seam S11 routes through.
The recall probe returned TOOL-dDerivedDocket-41, which records that check 26 joins verb names and
never flags, the gap S14 closes for `--record-piece`.

Recall terms used: `python tools/memory-recall/query.py "unattended skill byte budget verbs invocation check 26" --terms "SKILL.template.md 10240 check 26 VERBS_SLUG invocation unattended skill size budget trim"`
