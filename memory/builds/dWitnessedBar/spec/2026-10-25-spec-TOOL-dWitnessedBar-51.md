# TOOL-dWitnessedBar-51 — the round-1 spec audit's 50 minors, batched: owed widen rows and record bindings, one reader each, honest failure states, and the observations that read the wrong verb

**Status:** OPEN · rev-3 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 31 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 |
| [2026-10-25-build-TOOL-dWitnessedBar-40-round1-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-40-round1-fix-return.md) | research | TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-44 |
| [2026-10-25-build-TOOL-dWitnessedBar-52-round2-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-52-round2-fix-return.md) | research | TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-40-round1-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-40-round1-fix-brief.md) | research | TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-44 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-52-round2-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-52-round2-fix-brief.md) | research | TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 |
| [2026-10-25-review-TOOL-dWitnessedBar-40-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-40-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-43 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-1-spec-audit-round1.md`)
exited CONVERGED with 61 findings over the build's 30 units; its 11 highs are units 40 to 50. This unit is
M4's batch of every MEDIUM and LOW, one scope item per report id. They land on 28 units, so it builds
after every unit (order 31), before the close's bar; an item changing an earlier pass's output reaches
it through that unit's hands-off bullet to this one.

| Report item | Severity | Report ids | Scope items |
|---|---|---|---|
| M1 | MEDIUM | 1, 40 | S1, S2 |
| M2 | MEDIUM | 11, 20 | S3, S4 |
| M3 | MEDIUM | 22, 37 | S5, S6 |

Every other item, M4 to M34 and L1 to L13, is one id and one scope item in report order: M4 (id 2) is
S7, L13 (id 56) is S50.

That is 37 MEDIUM and 13 LOW findings by raw id.

## 2. Scope (IN)

- **S1** — id 1. Every shell file whose code-line count rose after `TOOL-dWitnessedBar-24`'s pass commit
  gets its `shell-role` widen row through `python tools/memory-tree/ratchet.py widen shell-role --key <path>
  --reason <text> --unit <id>`, one record per growing unit, its `Caused-by` that unit. The owing set is
  derived, never typed: the class members `git diff --numstat <unit 24 pass commit>..HEAD` shows grown,
  the commit found by its subject naming `TOOL-dWitnessedBar-24`. Observed by AC1.
- **S2** — id 40. Units 4 and 25, which `TOOL-dWitnessedBar-24` §4 Rollout names as owing a widen row,
  are covered by S1's derivation like every other, and `tools/memory-tree/README.md`'s shell-role
  paragraph states the derivation in place of a unit list. Observed by AC1.
- **S3** — id 11. The six `New arm:` lines whose first field carries a flag (units 24, 9 and 25) resolve to
  their legs through S4's rule, so `test.seen-red` owes each a seen-red record. Observed by AC2.
- **S4** — id 20. `tools/memory-tree/seen_red.py` reads a `New arm:` line's suite path as the first
  whitespace-delimited word of its first ` · ` field, and each later word of that field as a further argv
  element the leg must also carry. The plant `unseen-arm-with-args` (a `New arm: tools/x.py --selftest`
  line on an existing leg, no seen-red line) exits 1. Observed by AC2.
- **S5** — id 22. The rename of `memory/map/baseline.toml` and `affordance-exempt.toml` to `.txt`
  (`TOOL-dWitnessedBar-16` S6) reaches every carrier the git grep finds: `.gitattributes` (its eol pins),
  `AGENTS.md`, `.governance/deploy.toml`, `WIRE-INTO-PROJECT.md`, `memory/HYGIENE.md` and its template,
  `tools/codebase-map/selftest.py`, `tools/codebase-map/test_codebase_map.py` and its template,
  `tools/check-spec-tokens.test.sh`, `tools/codebase-map/README.md`, `memory/map/README.md`,
  `memory/map/FOUNDATION.md` and `memory/map/features/codebase-map.md`. Observed by AC3.
- **S6** — id 37. The rename's scoped grep holds and `dead-path carriers (deleted files still named)`
  stays green on the built tree. Observed by AC3.
- **S7** — id 2. The flake record (`TOOL-dWitnessedBar-8` S3) and the gate-health record
  (`TOOL-dWitnessedBar-1` S4) bind as `**Serves:** journal <unit id>`, the kind kept in the file name and
  the factory's kind row, since `journal` is a member of `RECORD_KIND_TOKENS`
  (`tools/memory-tree/tree_lib.py:406`) and `flake` and `gate-health` are not. Observed by AC4.
- **S8** — id 3. `leg_factory.py --conform`'s gate table gains the arm `purpose presence`: an absent
  `purpose` on a declaration whose name is no row of `leg-purpose-pending`, and a pending row for a leg
  that carries one or has left the manifest. The population's registration names `leg = "gate-leg
  conformance"` in place of `govkit selfcheck`. Observed by AC5.
- **S9** — id 4. `date-cutoffs`' registration names no `leg`, so `ratchet (both ways)` grades it, and
  `compare_counts` gains the `ceiling` rule "a measured value above the row's count" as `count rose`,
  `compare_to_base` keeping "a row raised above the base's" as `raised`. Observed by AC6.
- **S10** — id 5. The removal of a landed `[[upgrade]]` step row is observed through
  `ratchet.py both-ways`, which prints `unmeasured row` naming the step id, and the removal of its ledger
  row through `never-gains`, which prints `removed`. Observed by AC7.
- **S11** — id 6. `gate-leg conformance` and `leg-factory selftest` are `[[gate_leg]]` rows of
  `tools/run-gates/kit.toml`, the first a fixed row of an adopter's composition
  (`TOOL-dWitnessedBar-28` S3); at `TOOL-dWitnessedBar-11`'s pass commit gov's manifest differs from its
  parent only by the `enforces` key on rows and those two legs, and an adopter's emitted manifest differs
  only by those two legs' rows. Observed by AC8.
- **S12** — id 7. A self-test leg, `chunk = "selftests"`, carries `enforces = ["practice.verify"]`; the
  legs `powershell hygiene selftest`, `shell-hygiene selftest` (unit 24), `ratchet selftest` (unit 14)
  and `leg-factory selftest` (unit 11) carry it, and the contract leg of unit 9 and `leg sources` of
  unit 28 carry the practice tags unit 11's enforces rule derives for them, or a `leg` row of
  `tools/playbook/core-pending.txt`. Observed by AC9.
- **S13** — id 8. Unit 24's five homes, `encoding-stdout-sites.txt`, `encoding-js-sites.txt`,
  `path-literal-sites.txt`, `quoting-sites.txt` and `shell-role.txt`, join check 3's named list in
  `tools/memory-tree/check-memory-hygiene.sh` and leave gov's `PROJECT_REGISTRY_EXTRA`
  (`.memory-tree.conf:917`), the rule unit 17 S7 follows. Observed by AC10.
- **S14** — id 9. `LEG_KEYS` holds `level` and `precommit`, observed on its own line, and `LEG_KEY_FLOORS`
  holds a `"level":` and a `"precommit":` row. Observed by AC11.
- **S15** — id 10. `verdict_flow.py flakes --record-only --run <run dir> --build <slug> --unit <id>` writes
  the flake record, one row per executed leg, and prints no re-entry; the driver's `gates-green` calls it
  after every Test-step bar, green or red, under `record` and `quarantine`. A deviation record names the
  departure from `flow-steps.md:361`'s input. Observed by AC12.
- **S16** — id 19. `inherited_red.py up` over a target where no file read declares `INHERITED_RED` writes
  nothing and prints `inherited-red: undeclared — the kit default land read MIXED and CONTENDED reds as
  blocking; own-only now passes them`, so the loosening v2's default makes is said where it happens.
  Observed by AC13.
- **S17** — id 21. Every tracked `unarmed-branches.txt` outside the memory root, today
  `tools/unattended/unarmed-branches.txt` (71 lines), is converted with the central file, gains its
  `[[ledger]]` table in `tools/unattended/kit.toml`, and is read by `check-arms.py` through the factory.
  Observed by AC14.
- **S18** — id 23. `scan_bare_bash` over the built tree does not list `tools/govkit/govkit.py`'s
  membership test in `resolve_shell_argv`, by `TOOL-dWitnessedBar-48` S3's rule. Observed by AC15.
- **S19** — id 28. `fix_keeps.py`'s acceptance reader finds the section by heading text,
  `^## [0-9]+[.] Acceptance criteria`, and its backticked tokens by the `TICK` walk, carried inline from
  `tools/check-spec-tokens.py` (`extract_acceptance`, `:515`; `AC_HEAD`, `:334`; `TICK`, `:286`) under a
  `PARITY_ROWS` row. Observed by AC16.
- **S20** — id 29. `seen_red.py`'s `New arm:` reader reads arm lines only inside the Gates section, joins
  indented continuation lines, and is `scan_arm_covers`' arm walk (`tools/check-spec-tokens.py:1334-1345`)
  carried inline under a `PARITY_ROWS` row. Observed by AC2.
- **S21** — id 31. `measure_gate_health` takes the bar's legs through `held_halves.test_held`
  (`tools/run-gates/held_halves.py:76`), carried inline under a `PARITY_ROWS` row since drift-audit
  cannot import run-gates; unit 5's predicate notes `test_held`, `run-selftests.sh:833` and
  `govkit.py:2611` as copies that now read `derive_hold_source`'s word or state why each stays.
  Observed by AC17.
- **S22** — id 36. The `memory/project/readme-contract.txt` conversion of `TOOL-dWitnessedBar-16` S7 is
  made by the main loop's own commit at this pass, outside any dispatched `--writes`, because
  `.unattended.conf:417` lists the file in `SHARED_RECORDS` and `--dispatch` refuses it with code 49
  (`tools/unattended/unattended.sh:13834-13839`). Observed by AC18.
- **S23** — id 38. `fix-of` joins `_RUN_PARK_KINDS` in `tools/drift-audit/drift_report.py` (`:2427`) and
  `PARK_KINDS` in `tools/runlog/model.py` (`:98`), the two copies compared with the driver's.
  Observed by AC19.
- **S24** — id 39. `memory/guides/UNATTENDED-PROTOCOL.md` and its template fit their 66860-byte row
  (`tools/template-size-limits.txt:143`): this pass trims the render by at least the bytes the build's
  units added. Observed by AC20.
- **S25** — id 42. `resolve_shell_argv`'s nine callers keep their contracts once it raises: the eight at
  `tools/govkit/govkit.py:1229`, `:5013`, `:5231`, `:5268`, `:5307`, `:6214`, `:6321`, `:6445` and the
  ninth at `:13574`; `run_probe_in_empty_dir` (`:5225`) catches `Refusal` and returns `None`, its
  "could not launch" contract; the docstring states the raise. Observed by AC21.
- **S26** — id 46. `product_tests.py check` reads `tests.product`'s `declared-with-runners` as
  `declared` at a target whose installed `leg_factory.py` holds no `compose_target_legs`, so a landing
  that carries unit 9 without unit 28 reds no adopter. Observed by AC22.
- **S27** — id 47. `AGENTS.md` is re-rendered with the `gov-tester` role, and its high-water row moves
  through `check-template-size.sh --bump`. Observed by AC23.
- **S28** — id 48. `<common-dir>/gate-verdict/` keeps every tree a retained run record of any worktree
  names, read as `TOOL-dWitnessedBar-42` S1 reads them, and each worktree's `HEAD^{tree}`, and prunes
  the rest older than 30 days. Observed by AC24.
- **S29** — id 51. `refuse-wrong-shell.sh --coverage` asserts per member, over
  `TOOL-dWitnessedBar-50`'s population, that the first `refuse_wrong_shell || exit 2` line outside the
  block precedes the first line calling `resolve_python`. Observed by AC25.
- **S30** — id 52. `compare_to_base` reads a home absent at the base as a first seed, every working row
  `seeded`, printing `first seed <population> <n> rows`; a home present at the base in a grammar the
  ledger cannot read through the registration's legacy reader, its key set and counts not growing; any
  other unreadable base refuses naming why. Observed by AC26.
- **S31** — id 54. `resolve_rows`' ledger rule gains: a row gone on one side and changed on the other
  is a conflict region; an add on both sides of one key takes the lower count; a `%O` with no header
  beside `%A` and `%B` carrying one header is still the ledger class. Observed by AC27.
- **S32** — id 55. A seed argv's head `python` or `python3` runs as `sys.executable`, a head `bash` as the
  `resolve_bash_py` block's `found` (refused as it refuses), `{prefix}` and `{kit}` resolve as
  `regen.resolve_argv` resolves them, and the cwd is the repository root. Observed by AC28.
- **S33** — id 58. A live ratchet leg with no base exits 1, printing `unresolved` with
  `compare_to_base`'s reason and the remedy, and no `GATE_` knob turns it into a pass. Observed by AC29.
- **S34** — id 61. The tail is cut at the last whole UTF-8 character within 8192 bytes, decoded with
  `errors='replace'`, hashed as stored, and fenced in the `leg-tail` record with a backtick run longer
  than any inside it. Observed by AC30.
- **S35** — id 64. `read_leg_files` keeps the tracked files under a `fixtures/` or `fixture/` directory
  inside the gate script's own kit directory beside the argv files; imported product modules are not
  kept. Observed by AC31.
- **S36** — id 65. A quarantined leg is released by a row change only when a key outside
  `DECLARATIVE_LEG_KEYS` changed, the tuple of `tag`, `purpose`, `tests`, `enforces`, `level`,
  `precommit` and `pack` in `tools/run-gates/held_halves.py`. Observed by AC32.
- **S37** — id 69. A cutoff value other than blank or a valid `%Y-%m-%d` date reads as `99991231`, naming the
  conf and key. Observed by AC6.
- **S38** — id 12. `fix_keeps.py` keeps no target of a leg's `tests` edge, so the product module a
  code-miss fix must edit stays writable, as unit 22 §8 F3 rules. Observed by AC31.
- **S39** — id 13. The per-tree record carries `run_id` once: unit 4 writes it and unit 25 adds it to the
  run record's verdict block only. Observed by AC33.
- **S40** — id 14. The `warn.<k>` value's third TAB field is the subject and its fourth the unit.
  Observed by AC34.
- **S41** — id 15. `LEG_KEYS`' readers through the keys units 9 and 10 add are on the interface graph as
  this unit's consumes-from edge to `TOOL-dWitnessedBar-12` and its mirror. Observed by AC11.
- **S42** — id 16. The legs of units 24 and 9 take tags by `TOOL-dWitnessedBar-12`'s rule,
  `leg.<owner>.<name>`, the owner `gov` for an `[[exempt_leg]]`; the canary's tag arm re-derives each tag
  from owner and name. Observed by AC35.
- **S43** — id 17. `TOOL-dWitnessedBar-7`'s edits to `memory/HYGIENE.md`'s Acceptance ledger grammar and
  BUILD-METHOD M8 are traced to their grant by §8 F3 of this spec. Observed by AC36.
- **S44** — id 24. `tools/run-gates/README.md` names what manifest order drives: the dispatch tie-break,
  the report order, the `fail.<n>` indices, check-spec-tokens' first tripping guard and the held halves.
  Observed by AC37.
- **S45** — id 25. `eol_class.py`'s "What it does not check" states that an existing worktree keeps its
  CRLF copies until those files are checked out again (`git checkout -- <paths>`), which
  `git add --renormalize .` does not do for LF blobs. Observed by AC37.
- **S46** — id 30. The hook's bypass record is written by `write_push_once`/`write_push_line` with the
  fields `bypass`, `sha`, `policy` and `tree_verdict`; `push-main.sh` carries `write_push_line` itself as
  a byte-identical pair under a `PARITY_ROWS` row, and `write_bypass_line` is a thin caller.
  Observed by AC38.
- **S47** — id 32. `precommit.py` reads the manifest through `held_halves.load_manifest`, as
  `measure_legs.py` does (`:100`). Observed by AC39.
- **S48** — id 41. The runner's row hash (`run-gates.sh:2852`) hashes each row less its
  `DECLARATIVE_LEG_KEYS`, so a declarative key added later neither releases a reuse quarantine nor
  re-earns a held record; the one-time release and re-earn this pass itself causes is stated in §4 Migration.
  Observed by AC32.
- **S49** — id 43. The PINNED figure for shape 2's matches is re-derived at this pass's base by a stated
  command and is eight before `TOOL-dWitnessedBar-26`'s rewrite. Observed by AC15.
- **S50** — id 56. `seed` meets a home that exists but does not read, or whose header disagrees, by doing
  nothing, printing `refused <population> <reason>` and exiting 2; such a home never counts as absent.
  Observed by AC40.

## 3. Non-goals (OUT)

- Any high: units 40 to 50, one per id.
- The left-shift lints and checklist entries the report names: no clause of this build names them; the
  classes are recorded at the close.
- Re-reviewing or re-wording a repaired unit's spec (M4): each item is built and observed at this pass.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-24` — the shell-role ledger, the portability legs and their tags, `eol_class.py` and the five homes (ids 1, 7, 8, 11, 16, 25, 40)
- **consumes-from** `TOOL-dWitnessedBar-9` — `product_tests.py`, its `New arm:` line, its leg's tag and `enforces`, and the `level` key (ids 7, 9, 11, 16, 46)
- **consumes-from** `TOOL-dWitnessedBar-25` — its `New arm:` line and the leg tail's cut and record (ids 11, 61)
- **consumes-from** `TOOL-dWitnessedBar-7` — `seen_red.py`'s owed set and its carrier edits (ids 11, 17, 20, 29)
- **consumes-from** `TOOL-dWitnessedBar-16` — the map files' rename and the `unarmed-branches.txt` and `readme-contract.txt` conversions (ids 21, 22, 36, 37)
- **consumes-from** `TOOL-dWitnessedBar-8` — `verdict_flow.py flakes` and the flake record (ids 2, 10)
- **consumes-from** `TOOL-dWitnessedBar-1` — `measure_gate_health` and the gate-health record (ids 2, 31)
- **consumes-from** `TOOL-dWitnessedBar-11` — `leg_factory.py --conform`, its two legs and its landing compare (ids 3, 6, 7, 24)
- **consumes-from** `TOOL-dWitnessedBar-19` — the `purpose` presence rule and `leg-purpose-pending` (id 3)
- **consumes-from** `TOOL-dWitnessedBar-17` — `date-cutoffs` and `measure-cutoffs` (ids 4, 69)
- **consumes-from** `TOOL-dWitnessedBar-13` — `compare_counts`, `compare_to_base` and `resolve_rows`' ledger rule (ids 4, 52, 54)
- **consumes-from** `TOOL-dWitnessedBar-14` — the ratchet legs' no-base state and `ratchet selftest` (ids 7, 58)
- **consumes-from** `TOOL-dWitnessedBar-18` — `landed-steps` and its observation (id 5)
- **consumes-from** `TOOL-dWitnessedBar-10` — `precommit.py` and the `precommit` key (ids 9, 15, 32)
- **consumes-from** `TOOL-dWitnessedBar-12` — `LEG_KEYS`, `LEG_KEY_FLOORS` and the tag rule, read through the `level` and `precommit` keys units 9 and 10 add (ids 15, 16, 41)
- **consumes-from** `TOOL-dWitnessedBar-22` — the `tests` and `enforces` keys and the row-hash effect of adding them (ids 12, 41)
- **consumes-from** `TOOL-dWitnessedBar-3` — `inherited_red.py` and the protocol text (ids 19, 39)
- **consumes-from** `TOOL-dWitnessedBar-21` — `fix_keeps.py` and `fix-of` (ids 12, 28, 38, 64)
- **consumes-from** `TOOL-dWitnessedBar-26` — `scan_bare_bash`'s pinned count and `resolve_shell_argv`'s raise (ids 23, 42, 43)
- **consumes-from** `TOOL-dWitnessedBar-5` — the hold predicate's copies (id 31)
- **consumes-from** `TOOL-dWitnessedBar-23` — the `gov-tester` role and its render (id 47)
- **consumes-from** `TOOL-dWitnessedBar-4` — the per-tree verdict files and their `run_id` (ids 13, 48)
- **consumes-from** `TOOL-dWitnessedBar-27` — the refuse-wrong-shell coverage arm (id 51)
- **consumes-from** `TOOL-dWitnessedBar-15` — the seed verb's argv run and its state table (ids 55, 56)
- **consumes-from** `TOOL-dWitnessedBar-30` — the quarantine release's row compare (id 65)
- **consumes-from** `TOOL-dWitnessedBar-29` — the `warn.<k>` grammar (id 14)
- **consumes-from** `TOOL-dWitnessedBar-2` — `write_bypass_line` (id 30)
- **consumes-from** `TOOL-dWitnessedBar-28` — `leg sources`, its `enforces` and the composition S26 detects (ids 7, 46)
- **consumes-from** `TOOL-dWitnessedBar-40` — the per-tree record's `reused_cache`, unit 4's AC5 plant (id 13)
- **consumes-from** `TOOL-dWitnessedBar-42` — the every-worktree reading of the run records (id 48)
- **consumes-from** `TOOL-dWitnessedBar-44` — the absent-key path of `inherited_red.py up` (id 19)
- **consumes-from** `TOOL-dWitnessedBar-48` — shape 2's membership rule (ids 23, 43)
- **consumes-from** `TOOL-dWitnessedBar-50` — the derived wrong-shell population and `refuse-wrong-shell.sh --coverage` (id 51)
- **hands-off** `TOOL-dWitnessedBar-56` — the AC24 arm, the tail cut of S34 and the verdict prune of S28, which the verdict-boundary minors batch ages, escapes and annotates (ids 23, 48, 49)
- **hands-off** `TOOL-dWitnessedBar-57` — S1, S13, S21, S23, AC8, AC15, AC35, AC36 and its two parity rows, which the resolver and ledger minors batch grades on the prepared merge, observes and gives canonical markers (ids 9, 10, 22, 26, 31, 34, 38, 39, 46)
- **hands-off** `TOOL-dWitnessedBar-62` — S1, AC8, AC17 and S21's `PARITY_ROWS` precedent, on which the minors batch anchors the pass commit in `build_commit`, passes `--selection` and carries drift-audit's selection reader (ids 5, 23, 24, 29)

## 4. Design

### Why one unit and not two

The write sets are one connected set, so M6's clause 1 fails for every split: `run-gates.sh` joins S28,
S34 and S48; `held_halves.py` joins S21, S36, S47 and S48; `verdict_flow.py` joins S15 and S36; the
manifest joins S11, S12 and S42; the ledger factory joins S1, S9, S17, S30, S32 and S50; the parity rows
join S19, S20, S21, S29 and S46. One unit, sequenced.

### Evidence

- HYGIENE closes the record kind set S7 reads (`memory/HYGIENE.md:626-629`).
- `check-arms.py` reads the central file and every tracked sidecar (`tools/memory-tree/check-arms.py:41-42`,
  `:575-590`); the driver's `PARK_KINDS` is `tools/unattended/unattended.sh:875`.
- The protocol render and template measure 66859 bytes (row `tools/template-size-limits.txt:143`,
  2026-10-25); `AGENTS.md` measures 16732 against a 20480 row and a 16732 high-water
  (`tools/template-size-highwater.txt:2`).
- S25's callers are PINNED by `grep -n 'resolve_shell_argv('` (2026-10-25); `run_probe_in_empty_dir`
  catches `(OSError, subprocess.TimeoutExpired)` only (`tools/govkit/govkit.py:5234`).
- `regen.run_command` maps `python`, `python3` and `bash` (`tools/run-gates/regen.py:270-279`); the
  precedent over no base prints `UNGRADED` (`tools/codebase-map/test_codebase_map.py:159-170`).
- The row hash is the SHA-1 of the whole row as sorted JSON (`tools/run-gates/run-gates.sh:2852`), read
  by the reuse quarantine (`:3600`) and the reuse key (`:3225`).
- The hook's `write_push_line` and `write_push_once` (`.githooks/pre-push:345`, `:421`).

### The shell-role derivation (S1, S2)

```
c24   = unit 24's pass commit, found by its subject
grown = class members (unit 24 §4 "Line endings" less py, js, json, toml) over their ledger count at HEAD
for each unit u whose pass in c24..HEAD touched a member of grown:
    ratchet.py widen shell-role --key <path> --reason "grown by u's pass" --unit u
```

### The declarative keys (S36, S48)

S36's tuple lives in `tools/run-gates/held_halves.py`: the keys that change neither what a leg runs nor
how it is judged. The row hash and unit 30's release compare both drop them; the runner's embedded program
imports the tuple from its sibling, as `measure_legs.py` imports `held_halves` (`:100`).

### Inventory

Minted: `--record-only` of `verdict_flow.py flakes`; the arm `purpose presence`; the plants
`unseen-arm-with-args`, `arm-outside-gates` and `writes-fixture`; `DECLARATIVE_LEG_KEYS`; the parity rows
`acceptance_reader`, `arm_walk`, `hold_predicate` and `write_push_line`; the reading `first seed`. Each
is asked of `python tools/lexicon/lexicon.py --suggest <name>` at the pass.

### Migration

S48 changes every row hash once: each earlier reuse quarantine is released once and each held record
re-earns once; the reuse key carries the row hash (`run-gates.sh:3225`), so no stale green is reused.

### Rollout

Live at landing, after every other unit. The pass runs
`python tools/run-gates/owed_rows.py --base HEAD` before its commit (PLAY-dOrderedCharter-50 S6).

### Files touched (estimate)

`tools/memory-tree/ratchet.py`, `tools/memory-tree/README.md`, `memory/project/shell-role.txt`,
`tools/memory-tree/seen_red.py`, `.gitattributes`, `AGENTS.md`, `.governance/deploy.toml`,
`WIRE-INTO-PROJECT.md`, `memory/HYGIENE.md`, `tools/memory-tree/HYGIENE.template.md`,
`tools/codebase-map/selftest.py`, `tools/codebase-map/test_codebase_map.py`,
`tools/codebase-map/test_codebase_map.template.py`, `tools/check-spec-tokens.test.sh`,
`tools/codebase-map/README.md`, `memory/map/README.md`, `memory/map/FOUNDATION.md`,
`memory/map/features/codebase-map.md`, `tools/memory-tree/build_records.py`,
`tools/drift-audit/drift_report.py`, `tools/run-gates/leg_factory.py`, `tools/run-gates/kit.toml`,
`tools/lib/legacy_ledger.py`, `tools/memory-tree/legacy_ledger.py`, `tools/gate-lint/legacy_ledger.py`,
`tools/gate-lint/kit.toml`, `tools/memory-tree/kit.toml`, `tools/playbook/core-pending.txt`,
`tools/gate-legs.json`, `tools/memory-tree/check-memory-hygiene.sh`, `.memory-tree.conf`,
`tools/run-gates/run-gates.test.sh`, `tools/run-gates/verdict_flow.py`, `tools/unattended/unattended.sh`,
`tools/govkit/steps/inherited_red.py`, `tools/unattended/kit.toml`, `tools/unattended/unarmed-branches.txt`,
`tools/memory-tree/check-arms.py`, `tools/run-gates/measure_legs.py`, `tools/unattended/fix_keeps.py`,
`tools/lib/resolve-python.test.sh`, `tools/lib/refuse-wrong-shell.sh`, `tools/run-gates/held_halves.py`,
`tools/run-gates/run-selftests.sh`, `tools/govkit/govkit.py`, `memory/project/readme-contract.txt`,
`tools/runlog/model.py`, `tools/unattended/PROTOCOL.template.md`, `memory/guides/UNATTENDED-PROTOCOL.md`,
`tools/run-gates/product_tests.py`, `tools/template-size-highwater.txt`, `tools/run-gates/run-gates.sh`,
`tools/run-gates/run-gates.evidence.test.sh`, `tools/run-gates/README.md`, `tools/gate-lint/eol_class.py`,
`.githooks/pre-push`, `tools/push-main.sh`, `tools/run-gates/precommit.py`, `tools/govkit/selftest.py`,
`memory/builds/dWitnessedBar/build/<date>-build-TOOL-dWitnessedBar-51-widen-<n>.md`,
`memory/builds/dWitnessedBar/build/<date>-build-TOOL-dWitnessedBar-51-deviation-<n>.md`.

### Alternatives rejected

- **One unit per minor, or folding the minors into the repaired specs.** M4 forbids both.
- **Moving unit 24's shell-role arm to the end (id 1's option b).** Later units still grow files the arm
  reds; S1's widen rows are the ledger's record.

## 5. Production-readiness checklist

- security — S25 keeps selfcheck alive with no bash; S35 and S38 fence a fix pass from its judging
  fixtures; S16 and S33 refuse a silent pass.
- perf / scale — S48 ends a release per key addition; S28 bounds a growing directory.
- error / empty / loading states — S30, S33, S37 and S50 name a bad input, never a silent green.
- observability — each refusal or skip names its subject.
- risks — S48's one-time release (§4 Migration); S22's commit outside a dispatched pass.
- testing — AC1 to AC40; the arms under §7 at the close.
- migration — §4.
- user docs — S44 and S45 in the kit READMEs and a docstring; no page under `help/`.

## 6. Acceptance criteria

- **AC1** — When `python ratchet.py never-gains` and `python sh_hygiene.py --shell-role <ledger> .` run on
  the built tree, neither names a `shell-role` key, and every `widened:` row of `shell-role.txt` names a
  tracked widen record whose `**Caused-by:**` is a unit whose pass commit after unit 24's touched that
  file; `tools/memory-tree/README.md` names the derivation and lists no unit.
  Red when: a shell file grown by a later unit has no widen row, so the leg reds at the close.
- **AC2** — When `python seen_red.py --fixture --plant unseen-arm-with-args` runs in `tools/memory-tree/`,
  it exits 1 naming the leg; `--plant arm-outside-gates`, a spec quoting a `New arm:` line in its §4, exits
  0 owing nothing for it; and `python seen_red.py --build dWitnessedBar` lists the legs of the six flagged
  lines of units 24, 9 and 25 among those owed.
  Red when: a flagged first field resolves to no leg, or a quoted line outside Gates is owed.
- **AC3** — When `git grep -n 'baseline\.toml\|affordance-exempt\.toml' -- ':!memory/builds' ':!memory/archive' ':!memory/DECISIONS.md' ':!memory/gotchas'`
  runs on the built tree, it prints nothing, and `git grep -n 'baseline\.txt' -- .gitattributes` names
  the eol pin.
  Red when: a carrier still names a retired basename.
- **AC4** — When `python gen_build_index.py --print-bindings` runs in `tools/memory-tree/` over a fixture
  build holding one flake record and one gate-health record, both bind as `journal` with no `malformed`
  line.
  Red when: either record binds with a kind outside `RECORD_KIND_TOKENS`.
- **AC5** — When `python leg_factory.py --conform` runs in a scratch clone holding a declaration with no
  `purpose` and no `leg-purpose-pending` row, it exits 1 naming the arm `purpose presence`; with a pending
  row for a leg that carries a `purpose`, it exits 1 naming that row.
  Red when: a hand-written declaration with no `purpose` passes.
- **AC6** — When a scratch clone moves `SPEC_TIER1_CUTOFF` a day later and runs `python ratchet.py
  both-ways`, it exits 1 printing `count rose` naming `date-cutoffs` and the key; blanked, and set to
  `none`, it does the same; moved a day earlier, it exits 0.
  Red when: a malformed or later cutoff passes, or the observation runs through `never-gains`.
- **AC7** — When a scratch clone removes one landed `[[upgrade]]` row and runs `python ratchet.py
  both-ways`, it exits 1 printing `unmeasured row` naming the step id; when it deletes that id's row from
  `landed-steps.txt`, `never-gains` exits 1 printing `removed`.
  Red when: the append-only guarantee is observed through a compare the plant does not touch.
- **AC8** — When unit 11's AC2 compare command runs with `<c11>^` as its start against the manifest at
  `<c11>`, `TOOL-dWitnessedBar-11`'s pass commit, with `enforces` dropped from each row, it prints only
  the two added legs
  `gate-leg conformance` and `leg-factory selftest`; and `govkit.py apply --target <scratch> --all` at the
  parent and at the commit emit manifests whose difference is those two rows.
  Red when: a `gov` value moved in the migration, so a row other than the two changed.
  fixture: `<c11>` found by `git log --format=%H` over subjects naming `TOOL-dWitnessedBar-11`.
- **AC9** — When `python -c "import json,sys; [print(r['name'], r.get('enforces')) for r in json.load(open(sys.argv[1], encoding='utf-8')) if r.get('chunk') == 'selftests' and r['name'] in sys.argv[2:]]" tools/gate-legs.json "powershell hygiene selftest" "shell-hygiene selftest" "ratchet selftest" "leg-factory selftest"`
  runs, each prints `['practice.verify']`, and `python leg_factory.py --conform` exits 0.
  Red when: a self-test leg carries an empty `enforces` the arm reds.
- **AC10** — When `bash check-memory-hygiene.sh --only 3` runs in a scratch adopter after a seed writes the
  five homes, it exits 0, and `grep -c 'shell-role.txt' .memory-tree.conf` prints 0.
  Red when: a kit-shipped home is admitted only through `PROJECT_REGISTRY_EXTRA`.
- **AC11** — When `grep -nE '^LEG_KEYS=.*\blevel\b' run-gates.test.sh` and
  `grep -nE '^LEG_KEYS=.*\bprecommit\b' run-gates.test.sh` run in `tools/run-gates/`, each names one line,
  and `grep -nE '"(level|precommit)":' govkit.py` in `tools/govkit/` names two `LEG_KEY_FLOORS` rows; and
  this spec's §3 names `TOOL-dWitnessedBar-12` as a consumes-from edge.
  Red when: a key is added to one canary arm only, or the observation matches an unrelated fixture line.
- **AC12** — When `python verdict_flow.py flakes --record-only --run <fixture green run> --build x --unit
  TOOL-x-1` runs in `tools/run-gates/`, it writes one flake record with one row per executed leg and prints
  no re-entry line, and `grep -n 'flakes --record-only' unattended.sh` in `tools/unattended/` names the
  `gates-green` call.
  Red when: a green bar writes no record, so unit 1 never arms and no quarantine is released.
- **AC13** — When `python inherited_red.py up <target>` runs over a fixture target whose files declare no
  `INHERITED_RED`, it writes no `blocks` value and prints the `undeclared` line naming MIXED and
  CONTENDED.
  Red when: the absent path loosens with no witness.
- **AC14** — When `python check-arms.py --check` runs in `tools/memory-tree/` on the built tree, it exits 0
  reading the converted `tools/unattended/unarmed-branches.txt` rows, and `grep -n 'unarmed-branches'
  tools/unattended/kit.toml` names its `[[ledger]]` table.
  Red when: the sidecar keeps the old grammar or is dropped from the read.
- **AC15** — When `python -c "import sys; sys.path.insert(0,'tools/run-gates'); import measure_legs; print([h for h in measure_legs.scan_bare_bash('.') if 'govkit.py' in h])"`
  runs at the root, it prints `[]`; and this spec's §4 names the command that re-derived shape 2's
  count at the base.
  Red when: the membership test in `resolve_shell_argv` is listed as a launch.
- **AC16** — When `python fix_keeps.py --fixture --plant light-profile` runs in `tools/unattended/`, over a
  Tier-1 spec whose acceptance section is not its sixth, it reads that section's tokens; and the
  `grep -c '^# >>> acceptance_reader' fix_keeps.py` prints 1.
  Red when: the reader grades a section by position.
- **AC17** — When `python drift_report.py --gate-health --fixture held` runs in `tools/drift-audit/` over a
  fixture manifest with one leg held by `quarantine` and one by `kit`, neither is a bar leg, and
  `grep -c '^# >>> hold_predicate' drift_report.py` prints 1.
  Red when: the measurement's population differs from what the runner holds.
- **AC18** — When `git log -1 --format=%B -- memory/project/readme-contract.txt` runs after this pass, the
  commit is the main loop's, carrying no `Pass:` dispatch of a unit, and `python gen_build_index.py
  --check` in `tools/memory-tree/` exits 0 over the converted file.
  Red when: a dispatched pass declares the shared record.
- **AC19** — When `grep -c '"fix-of"' tools/drift-audit/drift_report.py tools/runlog/model.py` runs, it
  prints 1 for each file, the members the two kits' park-kind comparisons with the driver read.
  Red when: a copy lacks `fix-of`, so its comparison with the driver reds.
- **AC20** — When `wc -c < memory/guides/UNATTENDED-PROTOCOL.md` and `wc -c < tools/unattended/PROTOCOL.template.md`
  run, each prints at most 66860.
  Red when: the build's protocol edits cross the row.
- **AC21** — When `GOV_BASH=/nonexistent PATH=<dir with no bash> python tools/govkit/govkit.py selfcheck`
  runs in a scratch environment, 6b reports its no-launch count and the run does not exit 2 on a
  `Refusal`.
  Red when: the raise escapes `run_probe_in_empty_dir`.
- **AC22** — When `python product_tests.py check --fixture no-composition` runs in `tools/run-gates/`, over
  a planted target whose `leg_factory.py` lacks `compose_target_legs` and whose pyproject declares a level
  marker, it reads `declared` and exits 0.
  Red when: a target unit 28 has not routed reds the contract leg.
- **AC23** — When `grep -c 'gov-tester' AGENTS.md` runs, it prints at least 1, and
  `grep AGENTS.md tools/template-size-highwater.txt` prints the size `wc -c < AGENTS.md` prints.
  Red when: the role region is stale, or the charter's growth prints a size warning.
- **AC24** — When a scratch clone with two worktrees holds, under `<common-dir>/gate-verdict/`, a
  per-tree verdict named only by worktree B's retained run and one 31 days old named by none, a run in
  worktree A keeps the first and removes the second.
  Red when: one worktree's sweep deletes another's live verdict, or the directory never shrinks.
- **AC25** — When `bash refuse-wrong-shell.sh --coverage` runs from `tools/lib/` in a scratch clone where one
  member's `refuse_wrong_shell || exit 2` is moved below its first `resolve_python` call, it exits 1
  naming that file.
  Red when: a member refuses only after it resolved python.
- **AC26** — When `python legacy_ledger.py --fixture base-states` runs in `tools/lib/`, a home absent at
  the base prints `first seed p 2 rows`, a legacy-grammar base reads through the legacy reader and reds a
  grown key, and an unreadable base refuses naming why.
  Red when: an absent base reads every row `gained`, or green over nothing.
- **AC27** — When `merge-rows.sh` merges three fixture ledger files, `%O`, `%A` and `%B`, in a scratch
  repository, removed-against-changed yields a conflict region, add/add takes the lower count, and a
  header-less `%O` stays in the ledger class.
  Red when: a drain resurrects or a widen is dropped at the builder's choice.
- **AC28** — When `python legacy_ledger.py seed --population p` runs in a fixture whose seed argv is
  `["python3", "{prefix}/x.py"]`, the seed runs under `sys.executable` with `{prefix}` resolved and the cwd
  at the root, and prints `armed p`.
  Red when: `python3` reaches the MS-Store stub or `{prefix}` stays literal.
- **AC29** — When `python ratchet.py never-gains` runs in a scratch clone with its remote ref deleted, it
  exits 1 printing `unresolved` and the remedy.
  Red when: a leg with no base exits 0.
- **AC30** — When `python keep_tails.py --selftest` runs in `tools/run-gates/` with a tail holding a
  line that opens with three backticks, a `**Hash:**` line and a multibyte character across byte 8192, the written record's
  fence is longer than any run inside it, its fields read once, and its hash equals the stored bytes'.
  Red when: a tail closes the fence early or forges a field.
- **AC31** — When `python fix_keeps.py --fixture --plant writes-fixture` runs, a pass writing
  `tools/run-gates/fixtures/measure-legs/<file>` under `--fix-of leg:measure-legs selftest` is refused;
  under `--plant tests-target`, a write to the module a leg's `tests` edge names is admitted.
  Red when: a fix pass rewrites the red leg's fixtures, or is fenced from the product code.
- **AC32** — When a fixture bar runs with a quarantine file planted at a leg's row hash and then a `purpose`
  key added to that leg, the leg stays quarantined and `select` does not release it; with its `argv`
  changed, it is released.
  Red when: a declarative key releases a quarantine.
- **AC33** — When a full run writes a per-tree record after unit 25, `grep -c '^run_id' <record>` prints 1,
  and `.githooks/pre-push` meets a planted record with `reused_cache 2` by running the bar.
  Red when: `run_id` is written twice, or unit 4's AC5 plant names a key the record lacks.
- **AC34** — When the verdict-write block's slice runs over AC3 of unit 29's planted breach,
  `awk -F'\t' '$1=="warn.1"{print $4, $5}' verdict` prints the subject and the unit.
  Red when: the fields are read one place off.
- **AC35** — When a one-line Python over `tools/gate-legs.json` re-derives every `tag` from its row's
  owner and folded name, by unit 12's rule, for the rows whose `pack` is `portability` or
  `product-tests`, it prints no mismatch.
  Red when: a leg's tag is spelled by mode word or runner name.
- **AC36** — When `grep -n 'grants: PLAY-dClosedLoop-3' 2026-10-25-spec-TOOL-dWitnessedBar-51.md` runs in
  this build's `spec/` folder, it names §8 F3 and the two carriers.
  Red when: unit 7's carrier edits land with no recorded grant.
- **AC37** — When `grep -n 'fail\.<n>' README.md` runs in `tools/run-gates/` and `grep -n 'renormalize'
  eol_class.py` in `tools/gate-lint/`, each names the sentence S44 and S45 add.
  Red when: either claim stays unstated.
- **AC38** — When the `write_push_line` blocks of `tools/push-main.sh` and `.githooks/pre-push`, each
  between its `# >>> write_push_line` and `# <<< write_push_line` markers, are compared with `diff`, it
  prints nothing, and a fixture bypass with `RUNLOG_SWITCH=0` writes no line.
  Red when: the bypass writer skips the off switch or drifts from the hook's.
- **AC39** — When `grep -n 'load_manifest' precommit.py` runs in `tools/run-gates/`, it names the import,
  and `grep -c 'json.load' precommit.py` prints 0.
  Red when: `precommit.py` opens the manifest itself.
- **AC40** — When `python legacy_ledger.py seed --population p` runs over a home holding a legacy-grammar
  file, it prints `refused p` and exits 2, and the home is byte-identical.
  Red when: an unreadable home reads `present` or is treated as absent.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `build-index selftest` · `run-gates canary` · `run-gates evidence` · `measure-legs selftest` · `pre-push self-test` · `push-main self-test` · `drift-audit selftest` · `runlog selftest` · `codebase-map kit selftest` · `codebase-map adopter e2e` · `dead-path carriers (deleted files still named)` · `check-arms selftest` · `harness arms (fail branches armed or pinned)` · `python resolver (behaviour + inline parity + idiom ban)` · `row-keyed merge driver replay` · `unattended protocol size` · `charter size` · `playbook render wiring` · `govkit selftest` · `govkit selfcheck` · `shell-hygiene selftest` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `kit/dogfood doc parity` · `codebase-map gate coverage` · `govkit acceptance matrix` · `playbook render selftest` · `run-gates gov canary` · `transition-audit arms` · `straggler-guard arms` · `govkit refusal join` · `run-selftests self-test` · `pre-push run-log line` · `run-gates run-log line`

The unattended kit's own suites are waived for this build's landing (README rule), so AC12 and AC18
observe S15's driver call and S22's commit.

New arm: tools/memory-tree/seen_red.py · covers AC2 · the plants `unseen-arm-with-args` and `arm-outside-gates`, staged red by restoring the whole-field suite path · none
New arm: tools/run-gates/leg_factory.py · covers AC5 AC9 · the `purpose presence` arm and the self-test `enforces` rule in `--selftest`, staged red by a declaration with no `purpose` · none
New arm: tools/lib/resolve-python.test.sh · covers AC16 AC17 AC25 AC38 · the four new parity rows and the order assertion, staged red by a drifted copy and a member whose refusal follows its resolver call · none
New arm: tools/lib/legacy_ledger.py · covers AC26 AC28 AC40 · the base-state, argv-run and unreadable-home fixtures, staged red by reading an absent base as empty · none
New arm: tools/memory-tree/merge-rows.test.sh · covers AC27 · the three-way ledger matrix, staged red by dropping the removed-against-changed row · none
New arm: tools/run-gates/run-gates.evidence.test.sh · covers AC24 AC32 AC33 · the two-worktree verdict retention, the declarative-key quarantine and the single `run_id`, staged red by hashing the whole row · none
New arm: tools/unattended/fix_keeps.py · covers AC16 AC31 · the plants `light-profile`, `writes-fixture` and `tests-target`, staged red by keeping argv files only · none
New arm: tools/run-gates/keep_tails.py · covers AC30 · a tail holding a fence, a field line and a split character, staged red by a fixed three-backtick fence · none

## 8. Open questions

- **F1 — Which binding line does a promoted unit carry?** Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of each repaired unit's clause, which reds the parts join;
  veto 1 discards it. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the precedent
  `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none
- **F2 — Does an undeclared `INHERITED_RED` keep v2's default `own-only` (id 19)?** Today it reads the kit
  default `land` (`.githooks/pre-push:1341-1342`, `tools/unattended/unattended.sh:9590-9591`), blocking
  MIXED and CONTENDED reds. Options: (a) keep v2's default and say the loosening where the step runs
  (S16); (b) write `own-mixed-contended`, overriding the owner's walk T1 ruling for every adopter that
  never chose. RESOLVED (agent, 2026-10-25, delegated): (a), rung 1, v2:1271 (walk T1, default
  `own-only`). widens: none · relaxes: an adopter with no `INHERITED_RED` declared lands MIXED and
  CONTENDED reds that blocked before; this pass's deviation record carries **Bound:** that undeclared
  path only, **Tier:** middle, a policy key's bound, and **Reason:** v2's walk T1 default, the owner's.
- **F3 — Is a change to HYGIENE's Acceptance ledger and BUILD-METHOD M8 within this build's authority
  (id 17)?** `TOOL-dWitnessedBar-7` S1 and S9 edit both and record no grant. RESOLVED (agent,
  2026-10-25, delegated): yes, rung 3, veto 2 lifted by the README's `may:` grant, as the carried clause
  cl-0345 names the ledger's seen-red line and M8's read-back.
  grants: PLAY-dClosedLoop-3 the seen-red line grammar in `memory/HYGIENE.md` and M8's read-back sentence
  in `memory/guides/BUILD-METHOD.md`. widens: none · relaxes: none
- **F4 — How long does an unnamed per-tree verdict live (id 48)?** Options: (a) 30 days past its last
  write, kept while any worktree's retained run or `HEAD^{tree}` names it; (b) a file count, unsafe under
  churn; (c) no bound, the finding. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the bound that
  never removes a named verdict. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit's 37 MEDIUM and 13 LOW
  findings, batched.
- rev-2 · 2026-10-25 · §3 · the Edges block gains the hands-off bullets mirroring the consumes-from
  edges of TOOL-dWitnessedBar-56, TOOL-dWitnessedBar-57, promoted by the round-1 spec audit of units
  40 to 51; the prose of §1, §3, §4, §5, §8 and §10 compressed under the size ceiling, no scope item,
  criterion, edge, fork outcome or touched path moved.
- rev-3 · 2026-10-25 · §3 · the Edges block gains the hands-off bullet mirroring TOOL-dWitnessedBar-62's
  consumes-from edge, promoted by the round-1 spec audit of units 52 to 57; nothing else moved.

## 10. Reuse audit

Each item extends the seam its finding names, the ledger factory's verbs, `check-spec-tokens.py`'s
readers, `held_halves.py`, the hook's `write_push_line`, `regen.run_command` and check 3's named list,
cited in its scope item. `python tools/codebase-map/reuse_lookup.py "batch of spec audit minor findings
across many units"` ranked generic stems, none a seam for the batch.

Recall terms used: `python tools/memory-recall/query.py "what did the dWitnessedBar spec audit find at medium and low" --terms "spec audit minors batch dWitnessedBar medium low widen shell-role seen-red flake journal binding"`
