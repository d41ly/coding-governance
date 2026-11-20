# TOOL-dWitnessedBar-51 — the round-1 spec audit's 50 minors, batched: owed widen rows and record bindings, one reader each, honest failure states, and the observations that read the wrong verb

**Status:** INPROGRESS · rev-6 · 2026-11-20 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 31 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 |
| [2026-10-25-build-TOOL-dWitnessedBar-40-round1-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-40-round1-fix-return.md) | research | TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-44 |
| [2026-10-25-build-TOOL-dWitnessedBar-51-deviation-511.md](../build/2026-10-25-build-TOOL-dWitnessedBar-51-deviation-511.md) | deviation | — |
| [2026-10-25-build-TOOL-dWitnessedBar-51-deviation-512.md](../build/2026-10-25-build-TOOL-dWitnessedBar-51-deviation-512.md) | deviation | — |
| [2026-10-25-build-TOOL-dWitnessedBar-51-round10-size-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-51-round10-size-return.md) | research | — |
| [2026-10-25-build-TOOL-dWitnessedBar-52-round2-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-52-round2-fix-return.md) | research | TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 |
| [2026-10-26-build-TOOL-dWitnessedBar-51-deviation-513.md](../build/2026-10-26-build-TOOL-dWitnessedBar-51-deviation-513.md) | deviation | — |
| [2026-11-19-build-TOOL-dWitnessedBar-51-1-builder-return.md](../build/2026-11-19-build-TOOL-dWitnessedBar-51-1-builder-return.md) | journal | — |
| [2026-10-25-prompt-TOOL-dWitnessedBar-1-parents-crosscheck.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-1-parents-crosscheck.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-84 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-40-round1-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-40-round1-fix-brief.md) | research | TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-44 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-51-1-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-51-1-spec-writer.md) | journal | TOOL-dWitnessedBar-1 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-51-round10-size-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-51-round10-size-brief.md) | research | — |
| [2026-10-25-prompt-TOOL-dWitnessedBar-52-round2-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-52-round2-fix-brief.md) | research | TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 |
| [2026-10-26-prompt-TOOL-dWitnessedBar-1-parents-reground.md](../prompts/2026-10-26-prompt-TOOL-dWitnessedBar-1-parents-reground.md) | research | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-56 |
| [2026-11-19-prompt-TOOL-dWitnessedBar-51-1-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-51-1-spec-writer.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-51-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-51-build-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-51-fix1-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-51-fix1-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-51-fix1-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-51-fix1-spec-writer.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-51-reground-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-51-reground-brief.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-51-reground-spec-writer.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-51-reground-spec-writer.md) | journal | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-51-spec-tokens-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-51-spec-tokens-brief.md) | journal | TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-88 |
| [2026-10-25-review-TOOL-dWitnessedBar-40-spec-audit-round1.md](../reviews/2026-10-25-review-TOOL-dWitnessedBar-40-spec-audit-round1.md) | spec-audit | TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-43 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-1-spec-audit-round1.md`)
holds 61 findings, its 11 highs units 40 to 50 (PINNED 2026-10-25, the report's ledger). This unit is
M4's batch of its 37 MEDIUM and 13 LOW by raw id (PINNED 2026-10-25, the same ledger), one scope item
per id, plus S51, the install-prefix fix every earlier pass leg carried red. It builds alone, at order 31.

| Report item | Severity | Report ids | Scope items |
|---|---|---|---|
| M1 | MEDIUM | 1, 40 | S1, S2 |
| M2 | MEDIUM | 11, 20 | S3, S4 |
| M3 | MEDIUM | 22, 37 | S5, S6 |

Every other item, M4 to M34 and L1 to L13, is one id and one scope item in report order: M4 (id 2) is
S7, L13 (id 56) is S50. Ids 7 and 46 (S12, S26) wait with the deferred `TOOL-dWitnessedBar-28` and
leave this unit's scope. The items §4 "What HEAD already holds" lists landed with the units they name.

## 2. Scope (IN)

- **S1** — id 1. Every `shell-role` row the leg `portability (shell lines only shrink)` reds at the pass
  is settled in the pass commit. The owing set is derived, never typed: each tracked shell file whose
  code-line count, as `sh_hygiene.py --shell-role --measure` prints it, differs from its row in
  `memory/project/shell-role.txt`. A grown or new file is widened through
  `python tools/memory-tree/ratchet.py widen shell-role --key <path> --reason <text> --unit <id>`, one
  record per growing unit, its `Caused-by` that unit, found as the pass commits after unit 24's
  (`fe49c7d2a`) that touched the file, this unit's own growth under `TOOL-dWitnessedBar-51`; each
  widened row's count is then set to the measured count (§8 F5). A file that shrank has its row lowered
  to its count. Observed by AC1.
- **S2** — id 40. Units 4 and 25, which `TOOL-dWitnessedBar-24` §4 Rollout names as owing a widen row,
  are covered by S1's derivation like every other, and the `--shell-role` paragraph of
  `tools/gate-lint/README.md` states the derivation in place of a unit list. Observed by AC1.
- **S3** — id 11. Of the `New arm:` lines whose first field carries a flag, S4's rule resolves two to
  their legs: `shell-hygiene selftest` (unit 24) and `product-test contract (tests.product)` (unit 9),
  so `test.seen-red` owes each a seen-red record. Observed by AC2.
- **S4** — id 20. `tools/memory-tree/seen_red.py#derive_owed_gates` reads a `New arm:` line's suite path
  as the first whitespace-delimited word of its first ` · ` field, and each later word of that field as
  a further argv element the leg must also carry. The plant `unseen-arm-with-args` (a
  `New arm: tools/x.py --selftest` line on an existing leg, no seen-red line) exits 1. Observed by AC2.
- **S5** — id 22. The `.txt` names `TOOL-dWitnessedBar-16` S6 gave the two map files
  (`memory/map/baseline.txt`, `memory/map/affordance-exempt.txt`) reach every carrier AC3's grep finds:
  `.gitattributes` (its eol pins), `.governance/instructions.toml` and the `AGENTS.md` render,
  `WIRE-INTO-PROJECT.md`, `memory/gotchas/assertion-between-two-derived-values.md`,
  `memory/map/README.md`, `memory/map/FOUNDATION.md`, `memory/map/features/codebase-map.md`,
  `tools/check-spec-tokens.test.sh`, `tools/codebase-map/test_codebase_map.py` and its template, whose
  never-gains arm reads the old name today. The rows of `memory/project/dead-path-waivers.txt` whose
  disposition is `carried:TOOL-dWitnessedBar-51` drain with them. Observed by AC3.
- **S6** — id 37. The scoped grep holds and `dead-path carriers (deleted files still named)` stays
  green on the built tree. Observed by AC3.
- **S7** — id 2. Present at HEAD: `flake` and `gate-health` are members of
  `tools/memory-tree/tree_lib.py#TYPED_RECORD_KINDS` and of HYGIENE's closed kind list (units 8 and 1).
  Observed by AC4.
- **S8** — id 3. `tools/run-gates/leg_factory.py#check_declarations` gains the arm `purpose presence`: a
  manifest row with no `purpose` reds. Observed by AC5.
- **S9** — id 4. Present at HEAD: `date-cutoffs` names `ratchet (both ways)` as its leg
  (`tools/memory-tree/kit.toml`), and `tools/lib/legacy_ledger.py#compare_counts` reads a `ceiling` count
  above its row as `count rose`. Observed by AC6.
- **S10** — id 5. Present at HEAD: a landed `[[upgrade]]` step gone reads `unmeasured row` in
  `ratchet.py both-ways`, which `landed-steps` names as its leg (`tools/govkit/registry.toml`), and its
  ledger row gone is the append-only finding of `never-gains`. Observed by AC7.
- **S11** — id 6. Present at HEAD: `gate-leg conformance` and `leg-factory selftest` are
  `[[exempt_leg]]` rows of `tools/govkit/registry.toml`, so an adopter's emitted manifest carries
  neither; at unit 11's pass commit gov's manifest differs from its parent only by the `enforces` key and
  those two legs. Observed by AC8.
- **S12** — id 7. Leaves this unit's scope: `leg sources`' `enforces` waits with
  `TOOL-dWitnessedBar-28`. NOT OBSERVED: this pass builds nothing for it.
- **S13** — id 8. Unit 24's five homes, `encoding-stdout-sites.txt`, `encoding-js-sites.txt`,
  `path-literal-sites.txt`, `quoting-sites.txt` and `shell-role.txt`, join check 3's named list
  (`tools/memory-tree/check-memory-hygiene.sh@ceb4e244:1075`) and leave `.memory-tree.conf#PROJECT_REGISTRY_EXTRA`,
  the rule unit 17 S7 follows. Observed by AC10.
- **S14** — id 9. Present at HEAD: `LEG_KEYS` in `tools/run-gates/run-gates.test.sh` holds `level` and
  `precommit`, and `tools/govkit/govkit.py#LEG_KEY_FLOORS` a row for each. Observed by AC11.
- **S15** — id 10. `verdict_flow.py flakes --record-only --run <run dir> --build <slug> --unit <id>`
  writes the flake record, one row per executed leg, and prints no re-entry; the driver's `gates-green`
  calls it after a green Test-step bar under `record` and `quarantine`, a red bar keeping its landed
  call. A deviation record names the departure from the `test.flakes` row of
  `memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md`, whose input is the
  nondeterministic reds. The call adds no refusal site: a miss rides `run_leg_records`' own lines.
  Observed by AC12.
- **S16** — id 19. `tools/govkit/steps/inherited_red.py#cmd_up` over a target where no file read declares
  `INHERITED_RED` writes nothing and prints `inherited-red: undeclared — the kit default land read MIXED
  and CONTENDED reds as blocking; own-only now passes them`, so the loosening v2's default makes is said
  where it happens. Observed by AC13.
- **S17** — id 21. Present at HEAD (§8 F6): `tools/unattended/unarmed-branches.txt` keeps its legacy
  sidecar grammar, read by `tools/memory-tree/check-arms.py#parse_pin` beside the central ledger.
  Observed by AC14.
- **S18** — id 23. Present at HEAD: `scan_bare_bash` lists nothing in `tools/govkit/`, the membership test
  of `tools/govkit/upgrade_steps.py#resolve_shell_argv` reading `BASH_NAMES`. Observed by AC15.
- **S19** — id 28. `tools/unattended/fix_keeps.py#read_acceptance_files` finds the section by
  `tools/check-spec-tokens.py#extract_acceptance` and its `AC_HEAD`, and its tokens by `TICK`, carried
  inline under a `PARITY_ROWS` row in place of its own `ACCEPTANCE_HEADING` and `TICKED`.
  Observed by AC16.
- **S20** — id 29. `seen_red.py`'s `New arm:` reader is `tools/check-spec-tokens.py#read_arm_lines`'s
  walk, carried inline under a `PARITY_ROWS` row: arm lines inside the Gates section only, indented
  continuation lines joined. Observed by AC2.
- **S21** — id 31. `tools/drift-audit/drift_report.py#read_gate_health` takes the bar's legs through
  `tools/run-gates/held_halves.py#test_held`, carried inline under a `PARITY_ROWS` row since drift-audit
  cannot import run-gates. The copies at `tools/run-gates/run-selftests.sh@f6685fa0:985` and
  `tools/govkit/govkit.py@7999040a:2603` read `derive_hold_source`'s word or state why each stays.
  Observed by AC17.
- **S22** — id 36. Present at HEAD: `memory/project/readme-contract.txt` was converted by the main
  loop's commit `1f4ce2c30`, carrying `Pass: none`. Observed by AC18.
- **S23** — id 38. Present at HEAD: `fix-of` joined `_RUN_PARK_KINDS` in
  `tools/drift-audit/drift_report.py` and `PARK_KINDS` in `tools/runlog/model.py` (unit 21, `cd03e4e75`).
  Observed by AC19.
- **S24** — id 39. `memory/guides/UNATTENDED-PROTOCOL.md` and its template stay within their row in
  `tools/template-size-limits.txt`: any protocol byte this pass adds is trimmed in the same pass.
  Observed by AC20.
- **S25** — id 42. `resolve_shell_argv`'s callers keep their contracts once it raises: the 13 call sites
  `grep -n 'resolve_shell_argv(' tools/govkit/govkit.py tools/govkit/matrix.py tools/govkit/upgrade_steps.py`
  prints less the definition (PINNED 2026-11-20). `tools/govkit/govkit.py#run_probe_in_empty_dir` catches
  `Refusal` and returns `None`, its "could not launch" contract, and its docstring states the raise.
  Observed by AC21.
- **S26** — id 46. Leaves this unit's scope: the composition it detects is `TOOL-dWitnessedBar-28`'s.
  NOT OBSERVED: this pass builds nothing for it.
- **S27** — id 47. `AGENTS.md` carries the `gov-tester` role at HEAD (unit 23); its high-water row in
  `tools/template-size-highwater.txt` moves to its size through `check-template-size.sh --bump`.
  Observed by AC23.
- **S28** — id 48. `<common-dir>/gate-verdict/` keeps every tree a retained run record of any worktree
  names, read as the tail sweep reads them (`tools/run-gates/run-gates.sh@5c7136a7:6299`), and each
  worktree's `HEAD^{tree}`, and prunes the rest older than 30 days (§8 F4). Observed by AC24.
- **S29** — id 51. `refuse-wrong-shell.sh --coverage` asserts per member, over
  `TOOL-dWitnessedBar-50`'s population, that the first `refuse_wrong_shell || exit 2` line outside the
  block precedes the first line calling `resolve_python`, the "does not check" its header names.
  Observed by AC25.
- **S30** — id 52. Present at HEAD (§8 F7): a home absent at the base reads `new at <sha12>` and a
  legacy-grammar base `regrammared at <sha12>`, each with its row count
  (`tools/memory-tree/ratchet.py#check_new_at_base`, `#check_regrammared_at_base`); any other unreadable
  base is `unresolved` naming why (`tools/lib/legacy_ledger.py#compare_to_base`). Observed by AC26.
- **S31** — id 54. `tools/memory-tree/merge-rows.py#resolve_rows`' ledger rule gains: an add on both sides
  of one key takes the lower count; a `%O` with no header beside `%A` and `%B` carrying one is still the
  ledger class. A row one side took out and the other changed is a conflict region at HEAD.
  Observed by AC27.
- **S32** — id 55. In `tools/lib/legacy_ledger.py#run_seed_argv`, a seed argv's head `python` or
  `python3` runs as `sys.executable` and a head `bash` as the `resolve_bash_py` block's `found`, refused
  as it refuses, as `tools/run-gates/regen.py#run_command` maps them; `{prefix}` and the root cwd hold at
  HEAD. Observed by AC28.
- **S33** — id 58. A live ratchet leg with no base exits 1 printing `unresolved` with
  `compare_to_base`'s reason at HEAD; this pass adds the remedy to that line, and no `GATE_` knob turns
  it into a pass. Observed by AC29.
- **S34** — id 61. The tail is cut at the last whole UTF-8 character within 8192 bytes
  (`tools/run-gates/run-gates.sh@5c7136a7:6039`), decoded with `errors='replace'`, hashed as stored, and
  fenced in the `leg-tail` record with a backtick run longer than any inside it, in place of
  `tools/run-gates/keep_tails.py@c9acc115:202`'s fixed fence. Observed by AC30.
- **S35** — id 64. `tools/unattended/fix_keeps.py#read_leg_files` keeps the tracked files under a
  `fixtures/` or `fixture/` directory inside the gate script's own kit directory beside the argv files;
  imported product modules are not kept. Observed by AC31.
- **S36** — id 65. A quarantined leg is released by a row change only when a key outside
  `DECLARATIVE_LEG_KEYS` changed, the tuple of `tag`, `purpose`, `tests`, `enforces`, `level`,
  `precommit` and `pack` in `tools/run-gates/held_halves.py`, read by
  `tools/run-gates/verdict_flow.py#check_row_changed`. Observed by AC32.
- **S37** — id 69. `tools/memory-tree/ratchet.py#measure_cutoffs` reads a cutoff value other than blank or
  a valid `%Y-%m-%d` date as `99991231`, printing one stderr line naming the conf and key, where it raises
  today. Observed by AC6.
- **S38** — id 12. Present at HEAD: `fix_keeps.py` keeps argv words and check-class acceptance files
  only, and prints a leg's `tests` targets as `feature.<f>` tags, so the product module stays writable.
  Observed by AC31.
- **S39** — id 13. Present at HEAD: the per-tree record carries `run_id` once
  (`tools/run-gates/run-gates.sh@5c7136a7:6237`). Observed by AC33.
- **S40** — id 14. Present at HEAD: a `warn.<k>` value's third TAB field is the subject and its fourth
  the unit (`tools/run-gates/run-gates.sh@5c7136a7:5671`). Observed by AC34.
- **S41** — id 15. Present: this spec's §3 carries the consumes-from edge to `TOOL-dWitnessedBar-12`.
  Observed by AC11.
- **S42** — id 16. Present at HEAD: the legs of units 24 and 9 carry the tag
  `tools/run-gates/leg_factory.py#derive_leg_tag` derives from owner and name. Observed by AC35.
- **S43** — id 17. Present: unit 7's edits to `memory/HYGIENE.md`'s Acceptance ledger grammar and
  BUILD-METHOD M8 are traced to their grant by §8 F3 of this spec. Observed by AC36.
- **S44** — id 24. `tools/run-gates/README.md` gains a paragraph opening "Manifest order drives", naming
  the dispatch tie-break, the report order, the `fail.<n>` indices, check-spec-tokens' first tripping
  guard and the held halves. Observed by AC37.
- **S45** — id 25. `eol_class.py`'s "What this does not check" states that an existing worktree keeps its
  CRLF copies until those files are checked out again (`git checkout -- <paths>`), which
  `git add --renormalize .` does not do for LF blobs. Observed by AC37.
- **S46** — id 30. Present at HEAD (§8 F8): `write_bypass_line` is a byte-identical pair in
  `.githooks/pre-push` and `tools/push-main.sh`, honouring `GOV_RUNLOG=0`. Observed by AC38.
- **S47** — id 32. `tools/run-gates/precommit.py` reads the manifest through `held_halves.load_manifest`,
  as `measure_legs.py` does (`tools/run-gates/measure_legs.py@d9b2a0c4:101`). Observed by AC39.
- **S48** — id 41. The runner's row hash (`tools/run-gates/run-gates.sh@5c7136a7:3066`) hashes each row
  less its `DECLARATIVE_LEG_KEYS`, so a declarative key added later neither releases a reuse quarantine
  nor re-earns a held record; the one-time release and re-earn this pass causes is §4 Migration's.
  Observed by AC32.
- **S49** — id 43. Present: shape 2's matches at the base, re-derived by the probe §4 states, are 8
  (PINNED 2026-11-20). Observed by AC15.
- **S50** — id 56. `seed` meets a home that exists but does not read, or whose header disagrees, by doing
  nothing, printing `refused <population> <reason>` and exiting 2; such a home never reads `present` or
  absent (`tools/lib/legacy_ledger.py#read_home_state`). Observed by AC40.
- **S51** — the brief's install-prefix fix. The `conf-scalar-pins` registration's seed argv in
  `tools/memory-tree/kit.toml` reads `seed = ["python", "{prefix}/memory-tree/ratchet.py", ...]`, which
  `run_seed_argv` resolves, in place of a kit path the install-prefix leg reds. Observed by AC41.

## 3. Non-goals (OUT)

- Any high: units 40 to 50, one per id.
- Ids 7 and 46 (S12, S26): they wait with `TOOL-dWitnessedBar-28`, which this run defers.
- The left-shift lints and checklist entries the report names: no clause of this build names them.
- A leg for the three flagged `New arm:` lines no leg runs, `encoding_posture.py --selftest`,
  `eol_class.py --selftest` (unit 24) and `keep_tails.py --selftest` (unit 25), and a canary arm grading a
  hand-written leg tag: no clause of this batch builds either; the classes are recorded at the close.
- Re-reviewing or re-wording a repaired unit's spec (M4): each item is built and observed at this pass.

### Edges

- **consumes-from** `TOOL-dWitnessedBar-24` — the shell-role ledger, the portability legs and their tags, `eol_class.py` and the five homes (ids 1, 8, 11, 16, 25, 40)
- **consumes-from** `TOOL-dWitnessedBar-9` — its `New arm:` line, its leg's tag and the `level` key (ids 9, 11, 16)
- **consumes-from** `TOOL-dWitnessedBar-25` — its `New arm:` line and the leg tail's cut and record (ids 11, 61)
- **consumes-from** `TOOL-dWitnessedBar-7` — `seen_red.py`'s owed set and its carrier edits (ids 11, 17, 20, 29)
- **consumes-from** `TOOL-dWitnessedBar-16` — the map files' new names, the sidecar and the `readme-contract.txt` conversion (ids 21, 22, 36, 37)
- **consumes-from** `TOOL-dWitnessedBar-8` — `verdict_flow.py flakes` and the flake record (ids 2, 10)
- **consumes-from** `TOOL-dWitnessedBar-1` — `read_gate_health` and the gate-health record (ids 2, 31)
- **consumes-from** `TOOL-dWitnessedBar-11` — `leg_factory.py --conform`, its two legs and its landing compare (ids 3, 6, 24)
- **consumes-from** `TOOL-dWitnessedBar-19` — the `purpose` key every leg carries (id 3)
- **consumes-from** `TOOL-dWitnessedBar-17` — `date-cutoffs` and `measure-cutoffs` (ids 4, 69)
- **consumes-from** `TOOL-dWitnessedBar-13` — `compare_counts`, `compare_to_base` and `resolve_rows`' ledger rule (ids 4, 52, 54)
- **consumes-from** `TOOL-dWitnessedBar-14` — the ratchet legs' no-base state and their `new at` reading (ids 52, 58)
- **consumes-from** `TOOL-dWitnessedBar-18` — `landed-steps` and its observation (id 5)
- **consumes-from** `TOOL-dWitnessedBar-10` — `precommit.py` and the `precommit` key (ids 9, 15, 32)
- **consumes-from** `TOOL-dWitnessedBar-12` — `LEG_KEYS`, `LEG_KEY_FLOORS` and the tag rule, read through the `level` and `precommit` keys units 9 and 10 add (ids 15, 16, 41)
- **consumes-from** `TOOL-dWitnessedBar-22` — the `tests` and `enforces` keys and the row-hash effect of adding them (ids 12, 41)
- **consumes-from** `TOOL-dWitnessedBar-3` — `inherited_red.py`, the protocol text and `lib-verdict.sh` (ids 1, 19, 39)
- **consumes-from** `TOOL-dWitnessedBar-21` — `fix_keeps.py` (ids 12, 28, 64)
- **consumes-from** `TOOL-dWitnessedBar-26` — `scan_bare_bash`'s pinned count and `resolve_shell_argv`'s raise (ids 23, 42, 43)
- **consumes-from** `TOOL-dWitnessedBar-5` — the hold predicate's copies (id 31)
- **consumes-from** `TOOL-dWitnessedBar-23` — the `gov-tester` role and its render (id 47)
- **consumes-from** `TOOL-dWitnessedBar-4` — the per-tree verdict files and their `run_id` (ids 13, 48)
- **consumes-from** `TOOL-dWitnessedBar-27` — the refuse-wrong-shell coverage arm (id 51)
- **consumes-from** `TOOL-dWitnessedBar-15` — the seed verb's argv run and its state table (ids 55, 56)
- **consumes-from** `TOOL-dWitnessedBar-30` — the quarantine release's row compare (id 65)
- **consumes-from** `TOOL-dWitnessedBar-29` — the `warn.<k>` grammar (id 14)
- **consumes-from** `TOOL-dWitnessedBar-2` — `write_bypass_line` (id 30)
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

The write sets connect, so M6's clause 1 fails for every split: `run-gates.sh` joins S28, S34 and S48,
`held_halves.py` S21, S36 and S48, `verdict_flow.py` S15 and S36, the ledger factory's three copies S32
and S50, `fix_keeps.py` S19 and S35, and `tools/lib/resolve-python.test.sh`'s parity rows S19, S20 and
S21.

### What HEAD already holds

S7, S9, S10, S11, S14, S17, S18, S22, S23, S30, S38 to S43, S46 and S49 hold at HEAD `762c6d8c6`: the
units their scope item names landed them, or this spec's text carries them. This pass builds nothing for
them and observes each through its criterion.

### Evidence

- The shell-role leg grades each row exactly (`tools/gate-lint/sh_hygiene.py#run_shell_role_scan`), and
  `tools/memory-tree/ratchet.py#run_widen` raises a widened row by one. At HEAD 24 rows differ from the
  measure, 20 grown, 3 shrunk and 1 new file, `tools/run-gates/lib-verdict.sh` (PINNED 2026-11-20, a
  probe of `sh_hygiene.measure_code_lines` over `read_shell_sources` against the rows); unit 10's three
  `widened:` rows name a deviation record.
- `seen_red.py` resolves a whole first field (`tools/memory-tree/seen_red.py#derive_owed_gates`); of this
  build's flagged `New arm:` lines, 5 at HEAD (PINNED 2026-11-20), two resolve under S4's rule.
- The map files carry `.txt` names; the dead-path waiver holds 20 `carried:TOOL-dWitnessedBar-51` rows
  (PINNED 2026-11-20, `grep -c`), and `memory/project/positional-refs.txt` keys frozen records under
  `memory/builds/` that quote the old names, outside S5's population.
- AC3's four exclusions are records or keys of records: `memory/builds`, `memory/archive`,
  `memory/DECISIONS.md` and `memory/project/positional-refs.txt`.
- Unit 19's review left no leg underived, so no `leg-purpose-pending` population exists: every one of
  219 manifest rows carries `purpose` (PINNED 2026-11-20, `tools/gate-legs.json`).
- The driver's flake call sits in the red branch of `gates-green` only
  (`tools/unattended/unattended.sh@05c22cae:12307`). The driver holds 343 refusal sites, 339 armed
  (DERIVED by `check-arms.py --emit-floors`, unit 21's builder return); S15 adds none.
- `run_probe_in_empty_dir` catches `(OSError, subprocess.TimeoutExpired)` only, and `Refusal` is
  `upgrade_steps.Refusal`, aliased in govkit (`tools/govkit/govkit.py#Refusal`).
- `run_seed_argv` resolves `{prefix}` and runs at the root, the head spelled as written; no registered
  seed argv spells `{kit}` (DERIVED, `git grep -n 'seed = \['` over the kit descriptors and the registry).
- The row hash is the SHA-1 of the whole row as sorted JSON (`tools/run-gates/run-gates.sh@5c7136a7:3066`),
  read by the reuse quarantine (`:3908`) and written by its release (`:5561`).
- The protocol render and template measure 68283 bytes against a 68288 row (PINNED 2026-11-20,
  `wc -c` and `tools/template-size-limits.txt`); `AGENTS.md` measures 23575 against a high-water row of
  16732 (PINNED 2026-11-20, `wc -c` and `tools/template-size-highwater.txt`).

### Shape 2 at the base (S49)

Re-derived 2026-11-20: 8 matches, every tuple or list literal holding both `bash` and `bash.exe` in a
Python file at `cdfbd1cf`, `tools/govkit/govkit.py`'s two among them.

```
python -c "import ast,subprocess as s;r='cdfbd1cf';n=0
for f in s.run(['git','ls-tree','-r','--name-only',r],capture_output=True,text=True).stdout.split():
  if not f.endswith('.py'): continue
  try: t=ast.parse(s.run(['git','show',r+':'+f],capture_output=True).stdout)
  except SyntaxError: continue
  n+=sum({'bash','bash.exe'}<={e.value for e in x.elts if isinstance(e,ast.Constant)} for x in ast.walk(t) if isinstance(x,(ast.Tuple,ast.List)))
print(n)"
```

### The shell-role settlement (S1, S2)

```
c24   = fe49c7d2a, unit 24's pass commit
owed  = each shell file whose `--measure` count differs from its row, or has no row
for each owed file grown or new, for each unit u whose pass commit in c24..HEAD touched it:
    ratchet.py widen shell-role --key <path> --reason "grown by u's pass" --unit u
then:   each owed row's count := its `--measure` count (§8 F5)
```

### The declarative keys (S36, S48)

S36's tuple holds the keys that change neither what a leg runs nor how it is judged; the runner's
embedded program imports it from its sibling, as `measure_legs.py` imports `held_halves`.

### Inventory

Minted: `--record-only` of `verdict_flow.py flakes`; the arm `purpose presence`; the plants
`unseen-arm-with-args`, `arm-outside-gates`, `writes-fixture`, `light-profile`, `cutoff-none` and
`no-base-remedy`; the drift fixture `held`; `DECLARATIVE_LEG_KEYS`; the parity rows `acceptance_reader`,
`arm_walk` and `hold_predicate`. Each is asked of `python tools/lexicon/lexicon.py --suggest <name>` at
the pass.

### Migration

S48 changes every row hash once: each earlier reuse quarantine releases and each held record re-earns
once; the reuse key carries the row hash, so no stale green is reused.

### Rollout

Live at landing. The pass runs `python tools/run-gates/owed_rows.py --base HEAD` before its commit
(PLAY-dOrderedCharter-50 S6).

### Files touched (estimate)

`tools/memory-tree/ratchet.py`, `memory/project/shell-role.txt`, `tools/gate-lint/README.md`,
`tools/memory-tree/seen_red.py`, `tools/memory-tree/check-memory-hygiene.test.sh`, `.gitattributes`,
`.governance/instructions.toml`, `AGENTS.md`, `WIRE-INTO-PROJECT.md`,
`memory/gotchas/assertion-between-two-derived-values.md`, `memory/map/README.md`,
`memory/map/FOUNDATION.md`, `memory/map/features/codebase-map.md`, `tools/check-spec-tokens.test.sh`,
`tools/codebase-map/test_codebase_map.py`, `tools/codebase-map/test_codebase_map.template.py`,
`memory/project/dead-path-waivers.txt`, `tools/run-gates/leg_factory.py`,
`tools/memory-tree/check-memory-hygiene.sh`, `.memory-tree.conf`, `tools/run-gates/verdict_flow.py`,
`tools/unattended/unattended.sh`, `tools/govkit/steps/inherited_red.py`, `tools/check-spec-tokens.py`,
`tools/unattended/fix_keeps.py`, `tools/unattended/unattended.test.sh`, `tools/drift-audit/drift_report.py`,
`tools/run-gates/held_halves.py`, `tools/run-gates/run-selftests.sh`, `tools/govkit/govkit.py`,
`tools/lib/resolve-python.test.sh`, `tools/template-size-highwater.txt`, `tools/run-gates/run-gates.sh`,
`tools/run-gates/run-gates.evidence.test.sh`, `tools/run-gates/keep_tails.py`, `tools/lib/refuse-wrong-shell.sh`,
`tools/memory-tree/merge-rows.py`, `tools/memory-tree/merge-rows.test.sh`, `tools/lib/legacy_ledger.py`,
`tools/memory-tree/legacy_ledger.py`, `tools/gate-lint/legacy_ledger.py`, `tools/run-gates/README.md`,
`tools/gate-lint/eol_class.py`, `tools/run-gates/precommit.py`, `tools/memory-tree/kit.toml`,
`memory/builds/dWitnessedBar/build/<date>-build-TOOL-dWitnessedBar-51-widen-<n>.md`,
`memory/builds/dWitnessedBar/build/<date>-build-TOOL-dWitnessedBar-51-deviation-<n>.md`.

### Alternatives rejected

- **Unit 24's shell-role arm moved last (id 1's option b):** later units still grow files it reds.

## 5. Production-readiness checklist

- security — S25 keeps selfcheck alive with no bash; S35 fences a fix pass from its judging fixtures;
  S16 and S33 refuse a silent pass; S51 keeps a kit path out of a shipped argv.
- perf / scale — S48 ends a release per key addition; S28 bounds a growing directory.
- error / empty / loading states — S33, S37 and S50 name a bad input, never a silent green.
- observability — each refusal or skip names its subject.
- risks — S48's one-time release (§4 Migration); S1's rows set by hand from a measure (§8 F5).
- testing — the criteria of §6; the arms under §7 at the close.
- migration — §4.
- user docs — S2, S44 and S45 in the kit READMEs and a docstring; no page under `help/`.

## 6. Acceptance criteria

- **AC1** — When `python ratchet.py never-gains` and `python sh_hygiene.py --shell-role <ledger> .` run on
  the built tree, neither names a `shell-role` key, and every `widened:` row of `shell-role.txt` names a
  tracked widen record whose `**Caused-by:**` is a unit whose pass commit after `fe49c7d2a` touched that
  file; `tools/gate-lint/README.md` names the derivation and lists no unit.
  Red when: a shell file grown by a later unit has no widen row, so the leg reds at the close.
- **AC2** — When `python seen_red.py --fixture --plant unseen-arm-with-args` runs in `tools/memory-tree/`,
  it exits 1 naming the leg; `--plant arm-outside-gates`, a spec quoting a `New arm:` line in its §4, exits
  0 owing nothing for it; and `python seen_red.py --build dWitnessedBar` lists `shell-hygiene selftest`
  and `product-test contract (tests.product)` among those owed.
  Red when: a flagged first field resolves to no leg, or a quoted line outside Gates is owed.
- **AC3** — When `git grep -n 'baseline\.toml\|affordance-exempt\.toml' -- ':!memory/builds' ':!memory/archive' ':!memory/DECISIONS.md' ':!memory/project/positional-refs.txt'`
  runs on the built tree, it prints nothing, and `git grep -n 'baseline\.txt' -- .gitattributes` names
  the eol pin.
  Red when: a carrier, or its waiver row, still names an old basename.
- **AC4** — When `python gen_build_index.py --print-bindings` runs in `tools/memory-tree/` over a fixture
  build holding one flake record and one gate-health record, it prints an `S` row for each, of kind
  `flake` and `gate-health`, and no `A` row.
  Red when: either serves as `journal`, which PLAY-dOrderedCharter-42 S3 reads as malformed.
- **AC5** — When `python leg_factory.py --conform` runs in a scratch clone whose manifest holds a row with
  no `purpose`, it exits 1 naming the arm `purpose presence` and the leg.
  Red when: a hand-written declaration with no `purpose` passes.
- **AC6** — When a scratch clone moves `SPEC_TIER1_CUTOFF` a day later and runs `python ratchet.py
  both-ways`, it exits 1 printing `count rose` naming `date-cutoffs` and the key; blanked, and set to
  `none`, it does the same; moved a day earlier, it exits 0.
  Red when: a malformed or later cutoff passes, or the observation runs through `never-gains`.
- **AC7** — When a scratch clone removes one landed `[[upgrade]]` row and runs `python ratchet.py
  both-ways`, it exits 1 printing `unmeasured row` naming the step id; when it deletes that id's row from
  `memory/project/landed-steps.txt`, `never-gains` exits 1 printing `removed`.
  Red when: the append-only guarantee is observed through a compare the plant does not touch.
- **AC8** — When unit 11's AC2 compare runs with `<c11>^` as its start against the manifest at `<c11>`,
  `TOOL-dWitnessedBar-11`'s pass commit, with `enforces` dropped from each row, it prints only the two
  added legs `gate-leg conformance` and `leg-factory selftest`; and after `govkit.py apply --target
  <scratch> --all` at HEAD, `grep -c 'leg-factory selftest' <scratch>/tools/gate-legs.json` prints 0.
  Red when: a `gov` value moved in the migration, or an exempt leg reaches an adopter.
  fixture: `<c11>` is `b80649e60`, found by `git log --format=%H` over subjects naming
  `TOOL-dWitnessedBar-11`.
- **AC10** — When `bash check-memory-hygiene.sh --only 3` runs in a scratch adopter after a seed writes the
  five homes, it exits 0, and `grep -c 'shell-role.txt' .memory-tree.conf` prints 0.
  Red when: a kit-shipped home is admitted only through `PROJECT_REGISTRY_EXTRA`.
- **AC11** — When `grep -nE '^LEG_KEYS=.*\blevel\b' run-gates.test.sh` and
  `grep -nE '^LEG_KEYS=.*\bprecommit\b' run-gates.test.sh` run in `tools/run-gates/`, each names one line;
  `grep -nE '"(level|precommit)":' govkit.py` in `tools/govkit/` names the one `LEG_KEY_FLOORS` line
  holding both; and this spec's §3 names `TOOL-dWitnessedBar-12` as a consumes-from edge.
  Red when: a key is added to one canary arm only, or the observation matches an unrelated fixture line.
- **AC12** — When `python verdict_flow.py flakes --record-only --run <fixture green run> --build x --unit
  TOOL-x-1` runs in `tools/run-gates/`, it writes one flake record with one row per executed leg and prints
  no re-entry line, and `grep -n 'flakes --record-only' unattended.sh` in `tools/unattended/` names the
  `gates-green` call on its green branch.
  Red when: a green bar writes no record, so gate health never arms and no quarantine is released.
- **AC13** — When `python inherited_red.py up <target>` runs over a fixture target whose files declare no
  `INHERITED_RED`, it writes nothing and prints the `undeclared` line naming MIXED and CONTENDED.
  Red when: the absent path loosens with no witness.
- **AC14** — When `python check-arms.py --check` runs in `tools/memory-tree/` on the built tree, it exits 0
  with the sidecar's rows read, and `git grep -n '^home = "tools/' -- 'tools/*/kit.toml'` prints nothing.
  Red when: the sidecar is dropped from the read, or a ledger home sits under a kit directory.
- **AC15** — When `python -c "import sys; sys.path.insert(0,'tools/run-gates'); import measure_legs; print([h for h in measure_legs.scan_bare_bash('.') if 'govkit' in str(h)])"`
  runs at the root, it prints `[]`; and this spec's §4 names the probe that re-derived shape 2's count at
  the base.
  Red when: the membership test in `resolve_shell_argv` is listed as a launch.
- **AC16** — When `python fix_keeps.py --fixture --plant light-profile` runs in `tools/unattended/`, over a
  Tier-1 spec whose acceptance section is not its sixth, it reads that section's tokens; and
  `grep -c '^# >>> acceptance_reader' fix_keeps.py` prints 1.
  Red when: the reader grades a section by position, or drifts from the spec-token checker's.
- **AC17** — When `python drift_report.py --gate-health --fixture held` runs in `tools/drift-audit/` over a
  fixture manifest with one leg held by `quarantine` and one by `kit`, neither is a bar leg, and
  `grep -c '^# >>> hold_predicate' drift_report.py` prints 1.
  Red when: the measurement's population differs from what the runner holds.
- **AC18** — When `git log -1 --format=%B -- memory/project/readme-contract.txt` runs, it prints the main
  loop's commit carrying `Pass: none`, and `python gen_build_index.py --check` in `tools/memory-tree/`
  exits 0 over the converted file.
  Red when: a dispatched pass declares the shared record.
- **AC19** — When `grep -c '"fix-of"' tools/drift-audit/drift_report.py tools/runlog/model.py` runs, it
  prints 1 for each file, the members the two kits' park-kind comparisons with the driver read.
  Red when: a copy lacks `fix-of`, so its comparison with the driver reds.
- **AC20** — When `wc -c < memory/guides/UNATTENDED-PROTOCOL.md` and `wc -c < tools/unattended/PROTOCOL.template.md`
  run on the built tree, each prints at most the protocol's row in `tools/template-size-limits.txt`.
  Red when: this pass's protocol edits cross the row.
  figure: the row is DERIVED from the file at observation time.
- **AC21** — When `GOV_BASH=/nonexistent PATH=<dir with no bash> python tools/govkit/govkit.py selfcheck`
  runs in a scratch environment, 6b reports its no-launch count and the run does not exit 2 on a
  `Refusal`.
  Red when: the raise escapes `run_probe_in_empty_dir`.
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
- **AC26** — When `python ratchet.py --fixture --plant new-population` and `--plant regrammared` run in
  `tools/memory-tree/`, each exits 0, printing `new at` and `regrammared at` with the row count.
  Red when: an absent or legacy base reads every row `gained`, or green over nothing.
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
  Red when: a leg with no base exits 0, or names no remedy.
- **AC30** — When `python keep_tails.py --selftest` runs in `tools/run-gates/` with a tail holding a
  line that opens with three backticks, a `**Hash:**` line and a multibyte character across byte 8192,
  the written record's fence is longer than any run inside it, its fields read once, and its hash equals
  the stored bytes'.
  Red when: a tail closes the fence early or forges a field.
- **AC31** — When `python fix_keeps.py --fixture --plant writes-fixture` runs, a pass writing a file under
  the red leg's kit `fixtures/` directory is refused; under `--plant writes-product`, the product file is
  admitted.
  Red when: a fix pass rewrites the red leg's fixtures, or is fenced from the product code.
- **AC32** — When a fixture bar runs with a quarantine file planted at a leg's row hash and then a `purpose`
  key changed on that leg, the leg stays quarantined and `select` does not release it; with its `argv`
  changed, it is released.
  Red when: a declarative key releases a quarantine.
- **AC33** — When a full run writes a per-tree record, `grep -c '^run_id' <record>` prints 1, and
  `.githooks/pre-push` meets a planted record with `reused_cache 2` by running the bar.
  Red when: `run_id` is written twice, or unit 4's AC5 plant names a key the record lacks.
- **AC34** — When the verdict-write block's slice runs over AC3 of unit 29's planted breach,
  `awk -F'\t' '$1=="warn.1"{print $4, $5}' verdict` prints the subject and the unit.
  Red when: the fields are read one place off.
- **AC35** — When a one-line Python over `tools/gate-legs.json` re-derives through
  `leg_factory.derive_leg_tag` every `tag` of the rows whose `pack` is `portability`, and of
  `product-test contract (tests.product)`, from its owner and name, it prints no mismatch.
  Red when: a leg's tag is spelled by mode word or runner name.
- **AC36** — When `grep -n 'grants: PLAY-dClosedLoop-3' 2026-10-25-spec-TOOL-dWitnessedBar-51.md` runs in
  this build's `spec/` folder, it names §8 F3 and the two carriers.
  Red when: unit 7's carrier edits land with no recorded grant.
- **AC37** — When `grep -n 'Manifest order drives' README.md` runs in `tools/run-gates/` and
  `grep -n 'git checkout --' eol_class.py` in `tools/gate-lint/`, each names the sentence S44 and S45 add.
  Red when: either claim stays unstated.
- **AC38** — When the `write_bypass_line` bodies of `tools/push-main.sh` and `.githooks/pre-push`, each
  printed by `sed -n '/^write_bypass_line()/,/^}/p'`, are compared with `diff`, it prints nothing, and a
  fixture bypass under `GOV_RUNLOG=0` writes no journal line.
  Red when: the bypass writer skips the off switch or drifts from its pair.
- **AC39** — When `grep -n 'load_manifest' precommit.py` runs in `tools/run-gates/`, it names the import,
  and `grep -c 'json.load' precommit.py` prints 0.
  Red when: `precommit.py` opens the manifest itself.
- **AC40** — When `python legacy_ledger.py seed --population p` runs over a home holding a legacy-grammar
  file, it prints `refused p` and exits 2, and the home is byte-identical.
  Red when: an unreadable home reads `present` or is treated as absent.
- **AC41** — When `grep -n 'population = "conf-scalar-pins"' -A3 tools/memory-tree/kit.toml` runs, its
  seed line reads `"{prefix}/memory-tree/ratchet.py", "keys-not-scalar"`; and in a scratch clone with
  `memory/project/conf-scalar-pins.txt` deleted, `python tools/memory-tree/legacy_ledger.py seed
  --population conf-scalar-pins` prints `armed conf-scalar-pins`.
  Red when: the argv names a kit path, or the `{prefix}` spelling resolves to nothing.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `build-index selftest` · `run-gates canary` · `run-gates evidence` · `measure-legs selftest` · `pre-push self-test` · `push-main self-test` · `drift-audit selftest` · `runlog selftest` · `codebase-map kit selftest` · `codebase-map adopter e2e` · `dead-path carriers (deleted files still named)` · `check-arms selftest` · `harness arms (fail branches armed or pinned)` · `python resolver (behaviour + inline parity + idiom ban)` · `row-keyed merge driver replay` · `unattended protocol size` · `charter size` · `playbook render wiring` · `govkit selftest` · `govkit selfcheck` · `shell-hygiene selftest` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `kit/dogfood doc parity` · `codebase-map gate coverage` · `govkit acceptance matrix` · `playbook render selftest` · `run-gates gov canary` · `transition-audit arms` · `straggler-guard arms` · `govkit refusal join` · `run-selftests self-test` · `pre-push run-log line` · `run-gates run-log line` · `branch-guard self-test` · `policy fixtures` · `scratch-guard self-test` · `tier2-review self-test` · `portability (shell lines only shrink)` · `install-prefix (shipped surface)` · `ratchet selftest` · `leg-factory selftest`

The unattended kit's own suites are waived for this build's landing (README rule), so AC12 and AC16
observe S15's driver call and S19's reader directly.

New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC2 · the plants `unseen-arm-with-args` and `arm-outside-gates` run through `seen_red.py --fixture`, staged red by restoring the whole-field suite path · none
New arm: tools/run-gates/leg_factory.py · covers AC5 · the `purpose presence` arm in `--selftest`, staged red by a declaration with no `purpose` · none
New arm: tools/memory-tree/ratchet.py · covers AC6 AC29 · the plants `cutoff-none` and `no-base-remedy`, staged red by `measure_cutoffs` raising on `none` and an unresolved line with no remedy · none
New arm: tools/lib/resolve-python.test.sh · covers AC16 AC17 AC25 AC28 AC40 · the three new parity rows, the order assertion, and the seed's argv-run and unreadable-home cases, staged red by a drifted copy, a member whose refusal follows its resolver call, and a home read as absent · none
New arm: tools/memory-tree/merge-rows.test.sh · covers AC27 · the add/add and header-less `%O` rows, staged red by dropping the lower-count rule for an add on both sides · none
New arm: tools/run-gates/run-gates.evidence.test.sh · covers AC24 AC30 AC32 · the two-worktree verdict retention, the declarative-key quarantine, and `keep_tails.py --selftest`'s fence and character cut (§8 F9), staged red by hashing the whole row and by a fixed three-backtick fence · none
New arm: tools/unattended/unattended.test.sh · covers AC16 AC31 · the plants `light-profile` and `writes-fixture` run through `fix_keeps.py --fixture`, staged red by keeping argv files only · none

## 8. Open questions

- **F1 — Which binding line does a promoted unit carry?** RESOLVED (agent, 2026-10-25, delegated):
  `**Derived:**` naming `PLAY-dClosedLoop-2`, rung 3, the precedent of `TOOL-dDeclaredLoop-36` §8 F1.
  widens: none · relaxes: none
- **F2 — Does an undeclared `INHERITED_RED` keep v2's default `own-only` (id 19)?** At base it read the
  kit default `land` (`.githooks/pre-push@1ecf9aa6:1341`, `tools/unattended/unattended.sh@f499fbac:9590`).
  RESOLVED (agent, 2026-10-25, delegated): keep v2's default and say the loosening where the step runs
  (S16), rung 1, v2:1271 (walk T1). widens: none · relaxes: an adopter with no `INHERITED_RED` declared
  lands MIXED and CONTENDED reds that blocked before; this pass's deviation record carries **Bound:** that
  undeclared path only, **Tier:** middle, a policy key's bound, and **Reason:** v2's walk T1 default, the
  owner's.
- **F3 — Is a change to HYGIENE's Acceptance ledger and BUILD-METHOD M8 within this build's authority
  (id 17)?** RESOLVED (agent, 2026-10-25, delegated): yes, rung 3, veto 2 lifted by the README's `may:`
  grant, as cl-0345 names both.
  grants: PLAY-dClosedLoop-3 the seen-red line grammar in `memory/HYGIENE.md` and M8's read-back sentence
  in `memory/guides/BUILD-METHOD.md`. widens: none · relaxes: none
- **F4 — How long does an unnamed per-tree verdict live (id 48)?** RESOLVED (agent, 2026-10-25,
  delegated): 30 days past its last write, kept while any worktree's retained run or `HEAD^{tree}` names
  it, rung 3, the bound that never removes a named verdict. widens: none · relaxes: none
- **F5 — How does S1 bring a shell-role row to its measured count, when the widen door raises a row by
  one and the leg compares exactly?** (a) the widen door per growing unit for the record and the
  `widened:` stamp, then each owed row's count set to the population's own `--measure` count in the same
  commit; (b) a `--count <n>` option on the widen door; (c) unit 10's precedent, a deviation record and
  hand-written rows. RESOLVED (agent, 2026-11-20, delegated): (a), rung 3: no door option this batch alone
  would use, the count is derived by the population's seed, and the record is the `widen` kind AC1
  reads, where (c)'s is a deviation. widens: none · relaxes: none
- **F6 — Does the unattended kit's sidecar convert onto the ledger (id 21)?** (a) keep its legacy grammar,
  read by `parse_pin`'s sidecar loop as landed, so no pin is dropped; (b) fold its 8 rows (PINNED
  2026-11-20) into the central ledger, losing the prefix-relative keying a shipped pin needs; (c) a
  `[[ledger]]` home at the sidecar's path, which `install-prefix (shipped surface)` reds with no waiver.
  RESOLVED (agent, 2026-11-20, delegated): (a), rung 3: the landed reader closes the finding's defect,
  and (b) and (c) each break a shipped surface. widens: none · relaxes: none
- **F7 — Does `compare_to_base` mint a `first seed` reading (id 52) beside the ratchet's landed `new at`
  and `regrammared at`?** (a) no: the leg-layer readings settle the misread; (b) yes, as rev-5 specced.
  RESOLVED (agent, 2026-11-20, delegated): (a), rung 3, one reading per state. What it does not check:
  a regrammared base's legacy rows against the converted ones, which the conversion record holds.
  widens: none · relaxes: none
- **F8 — Does `write_bypass_line` route through the hook's `write_push_line` (id 30)?** (a) no: the landed
  pair is held byte-identical by the lander suite and honours `GOV_RUNLOG=0`, its values fixed tokens
  needing no escaping; (b) yes, carrying the hook's writer into the lander as a second copy.
  RESOLVED (agent, 2026-11-20, delegated): (a), rung 3: the residue the finding graded low is closed,
  and (b) grows shell lines S1 then widens. widens: none · relaxes: none
- **F9 — Where does S34's `keep_tails.py --selftest` arm live, when no leg runs that selftest?** (a) the
  evidence suite calls it, a suite a leg runs, so `test.seen-red` owes it; (b) a new leg. RESOLVED (agent,
  2026-11-20, delegated): (a), rung 3, no new leg for one arm. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft.
- rev-2 · 2026-10-25 · §3 · hands-off bullets for TOOL-dWitnessedBar-56 and TOOL-dWitnessedBar-57;
  prose compressed for the size ceiling.
- rev-3 · 2026-10-25 · §3 · the hands-off bullet for TOOL-dWitnessedBar-62.
  Prose of §1, §4, §8 and §9 trimmed for the size ceiling; nothing else moved.
- rev-4 · 2026-10-26 · S7 · AC4 · re-grounded by
  `build/2026-10-26-build-TOOL-dWitnessedBar-1-parents-crosscheck.md`, row 100: the two records serve
  as their own kinds, not `journal`.
- rev-5 · 2026-11-19 · §7 · the leg line gains `branch-guard self-test`, `policy fixtures`,
  `scratch-guard self-test` and `tier2-review self-test`, whose manifest guards hold the §4 paths
  `tools/memory-tree/check-memory-hygiene.sh`, `AGENTS.md` and `tools/unattended/unattended.sh`, per
  brief 2026-11-19-prompt-TOOL-dWitnessedBar-51-spec-tokens-brief; nothing else moved.
- rev-6 · 2026-11-20 · §1 · S1 to S51 · §3 · §4 · §5 · AC1 to AC41 · §7 · §8 F2, F5 to F9 · §10 ·
  re-grounded over HEAD `762c6d8c6` past order 29 by the brief
  `2026-11-19-prompt-TOOL-dWitnessedBar-51-reground-spec-writer`: code citations by symbol or
  blob-pinned; S12, S26, AC9 and AC22 leave scope with unit 28, whose edge goes, and id 38 leaves the
  unit 21 edge; S7, S9 to S11, S14, S17, S18, S22, S23, S30, S38 to S43, S46 and S49 read as present;
  S1 settles every drifted row (F5); S3 names the two flagged arms that resolve; S5's carriers and
  waiver rows re-derived; S8 loses the pending half no population backs; S15 calls on the green branch
  only; S17, S30 and S46 keep the landed shape (F6 to F8); S25's callers re-counted; S51 and AC41 carry
  the install-prefix fix; the arm homes are the suites a leg runs (F9); §7 gains the legs its new paths'
  guards name. Goal and Scope intent unchanged.

## 10. Reuse audit

Each item extends the seam its finding names, cited in its scope item: the ratchet pack's widen door
`tools/memory-tree/ratchet.py#run_widen`, the spec-token checker's readers
`tools/check-spec-tokens.py#extract_acceptance` and `#read_arm_lines`, `held_halves.py#test_held` and
`#load_manifest`, `tools/run-gates/regen.py#run_command`, the tail sweep of `run-gates.sh` and check 3's
named list. `python tools/codebase-map/reuse_lookup.py "batch of spec audit minor findings across many
units"` ranked generic stems, none a seam for the batch; re-run 2026-11-20, it ranks `units`, `audit` and
`parse_unit_rows`, still no seam for the batch.

Recall terms used: `python tools/memory-recall/query.py "what did the dWitnessedBar spec audit find at medium and low" --terms "spec audit minors batch dWitnessedBar medium low widen shell-role seen-red flake journal binding"`
