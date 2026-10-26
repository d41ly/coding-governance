# TOOL-dFurnishedOrders-29 — the round-1 audit's 35 roles, hooks and runlog minors: one reader per value, bounded slot readers, the verifier hooks' failure paths and registries, and fixtures that read only what they plant

**Status:** OPEN · rev-2 · 2026-10-26 · node d · Tier-2 · base 5ff43572 · streams tooling · order 22 · advances TOOL-dFurnishedOrders-21

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dFurnishedOrders-22-round1-fix-return.md](../build/2026-10-26-build-TOOL-dFurnishedOrders-22-round1-fix-return.md) | research | TOOL-dFurnishedOrders-22 TOOL-dFurnishedOrders-30 |
| [2026-10-26-prompt-TOOL-dFurnishedOrders-22-round1-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dFurnishedOrders-22-round1-fix-brief.md) | research | TOOL-dFurnishedOrders-22 TOOL-dFurnishedOrders-30 |
| [2026-10-26-review-TOOL-dFurnishedOrders-22-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dFurnishedOrders-22-spec-audit-round1.md) | spec-audit | TOOL-dFurnishedOrders-25 TOOL-dFurnishedOrders-24 TOOL-dFurnishedOrders-22 TOOL-dFurnishedOrders-23 TOOL-dFurnishedOrders-26 TOOL-dFurnishedOrders-27 TOOL-dFurnishedOrders-28 TOOL-dFurnishedOrders-30 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the 20 unit specs
(`memory/builds/dFurnishedOrders/reviews/2026-10-26-review-TOOL-dFurnishedOrders-1-spec-audit-round1.md`)
confirmed 35 MEDIUM and 16 LOW findings. BUILD-METHOD M4 batches them into two units because they
split into disjoint write sets by M6 (§4 "Why two units"). This unit takes the 35 whose fixes write the
roles, hooks and runlog kits and the records those kits feed: 23 MEDIUM and 12 LOW. Each report id is
named once below and closed by its scope item; `TOOL-dFurnishedOrders-30` takes the other 16.

| Report item | Report id | Lands on | Scope item |
|---|---|---|---|
| M1 | 2 | unit 6 S1, S7, AC5 | S1 |
| M7 | 23 | unit 6 S7, AC5 | S2 |
| M8 | 24, 51 | unit 15 §5, F3 | S3 |
| M9 | 25 | unit 3 S1, S3 | S4 |
| M27 | 58 | unit 3 S1, §5 | S5 |
| L5, L9 | 14, 38, 27 | units 3 S4, 10 S2 and F3, 11 §4 | S6 |
| L6 | 15 | unit 15 AC7 | S7 |
| L8 | 26 | units 3 AC3, 11 AC4, 12 AC2, 17 AC1 | S8 |
| M10 | 29 | units 11 S7, 12 S6, 7 S4 | S9 |
| M11, L7 | 30, 16 | units 11 S3, 17 S2, 20 S5 and F5 | S10 |
| M12 | 31 | unit 12 S3 | S11 |
| M13 | 32 | unit 19 S2, S4, S5 | S12 |
| M14 | 33 | unit 2 S4 | S13 |
| M15 | 34 | unit 10 S5 | S14 |
| M16 | 35 | unit 8 S2, F1 | S15 |
| M17 | 36 | unit 2 S5 | S16 |
| M18 | 39 | unit 8 S5, §7 | S17 |
| M20 | 43 | unit 6 S8, S9, §7 | S18 |
| M21 | 44 | unit 6 S9 | S19 |
| M22 | 45 | units 6 S1, 14 S2 | S20 |
| L11 | 37 | unit 14 S1 | S21 |
| L13 | 47 | unit 8 S5, S10 | S22 |
| M25 | 56 | unit 1 S6 | S23 |
| M26 | 57 | units 17, 4, 9, 11, 12, 18, 2 | S24 |
| M28 | 59 | unit 12 S1, AC1 | S25 |
| L1 | 10 | unit 18 S2, F3 | S26 |
| L3 | 12 | unit 2 S2 | S27 |
| L15 | 61 | unit 7 S5 | S28 |
| L14 | 60 | unit 16 AC1 | S29 |
| M2 | 5 | unit 19 S1 | S30 |
| M4 | 7 | unit 14 AC5 | S31 |

## 2. Scope (IN)

- **S1** — id 2. A broken role index is a recorded failure. In `tools/roles/answered-calls.js`, a
  `loadRoleIndex` answer of state `broken` (`tools/hooks/scratch-guard.js:952-988`) takes unit 6 S7's
  path, a `hook-failed` record carrying its `why`, and S7's catch covers S1 to S6. Observed by AC1.
- **S2** — id 23. `readSessionCli` folds dashes to dots as `skills/session-kickoff/manifest-check.sh:413`
  does, so the real `AI_AGENT` shape `claude-code_2-1-308_agent` reads `2.1.308`; the dotted shape reads
  the same. Observed by AC1 and AC2.
- **S3** — ids 24, 51. The tester's Write and Edit confined. `checkRouted` (`tools/hooks/scratch-guard.js:1113`)
  gains a step after step 3 (`:1093-1094`): a write tool whose payload `agent_type` names an index role
  with `writes` `none`, aimed inside the session repository, is denied naming the role; an absent index
  admits, a broken one denies, as step 6a does. A target outside the repository is admitted as today.
  Observed by AC3.
- **S4** — id 25. The labelled guard form. `tools/runlog/extract.py` passes each line of a Workflow
  result's logs that opens `[<stage>:<label>] [harness: ` to `derive_notices` with the label stripped,
  and the notice event's `src` names `<stage>:<label>`. Observed by AC4.
- **S5** — id 58. A cut pattern list. When the guard's list has no terminating `.` inside the lead
  `_read_result_text` returns (`extract.py:619-627`, 200 characters), `derive_notices` leaves out the partial
  last name and adds the label `truncated`. Observed by AC4.
- **S6** — ids 14, 38, 27. One by-file loader. `load_kit_module(kit, file, name)` in
  `tools/roles/roles_lib.py` resolves the file by `resolve_kit_dir` and loads it with
  `importlib.util.spec_from_file_location` under the private name `name`, cached in `sys.modules`. Unit
  3 S4 and unit 10 S2 load runlog's `extract.py` as `gov_runlog_extract`, and unit 11's ledger module is
  loaded the same way; no file under `tools/roles/` imports a sibling kit's module by its bare name.
  Observed by AC5.
- **S7** — id 15. `help/roles.md` and `tools/roles/README.md` each carry the string `outcome: probe`.
  Observed by AC6.
- **S8** — id 26. Each policy fixture of units 3, 11, 12 and 17 makes its scratch repository with
  `git init -b main` and commits `.governance/policy.toml` there, so `resolve` reads the landed revision
  (`tools/policy/policy.py:752-756`); unit 3's note says the value was read, not refused. Observed by AC6.
- **S9** — id 29. Units 11, 12 and 7 read `retrofit.slot-bytes`, `roles.orientation.house-index`,
  `memory.project-map`, `memory.map-unfold` and `roles.on-contradiction` through
  `read_policy_setting(key, root)` (TOOL-dBoundRoles-21 S1), a None reading the catalogue default; no
  `resolve_kit_dir("policy", "policy.py", ...)` import is left in `tools/roles/`. Observed by AC7.
- **S10** — ids 30, 16. One seed read. `read_item_seed(root, slug, unit, item, question)` lives in
  `tools/roles/handoff.py` once, runs `loop_lib.py seed` once per render, and the legacy, code and
  problems slots of units 11, 17 and 20 read its one answer. Observed by AC8.
- **S11** — id 31. Unit 12's `all` unfold reads the namespaces through `read_namespaces` of the playbook
  kit's `gov_tag.py` (PLAY-dOrderedCharter-19 S2), loaded by S6 as `gov_tag_reader`; no file under `tools/roles/` parses
  `namespaces.toml`. With no playbook kit the list stays `unarmed`. Observed by AC8.
- **S12** — id 32. One rule, one checker. `validate_return` evaluates with `check_return_schema` only
  the per-order properties the parent cannot see, `upstream` and S13's `tasks`; template fields stay
  TOOL-dBoundRoles-5 S1's, establishes rows unit 19 S2's. The whole schema is rendered for the order's
  block and the harness route only. Observed by AC9.
- **S13** — id 33. The batch join in the schema. `render_return_schema` takes the batch units
  `read_batch_units` reads and renders `tasks` as unit 19 renders `upstream`: each `unit` an `enum` of the
  batch, `maxItems` its count, one `contains` per unit, `job` and `nostop` required. `validate_return`
  names each fault `tasks · <class> · <unit>` in unit 19's class words, so the retry fires; `check_batch_tasks` keeps only
  the split's `--unit` membership. Observed by AC9.
- **S14** — id 34. `resolve_build_record(root, memory_root, build, tail)` in `handoff.py`, extracted from
  `write_agent_ledger` (`handoff.py:755-792`), returns `(path, ids)` or a note; `write_agent_ledger` and
  `write_role_metrics` both call it. Observed by AC10.
- **S15** — id 35. `resolve_slices` takes path, line, `end_line` and text from `gov_tag.py show <tag>
  --json` (PLAY-dOrderedCharter-19 S6) and cuts nothing itself; `parse_sections` stays only where
  `parse_charter` needs it. Where the index's extent is not fence-aware, the pass names that in its
  return for an ask on PLAY-dOrderedCharter-19. Observed by AC11.
- **S16** — id 36. Unit 2's `prompts.batch` reads `per-batch` on a None from any cause; the note
  `read_policy_setting` writes names a missing kit. Observed by AC12.
- **S17** — id 39. `memory/project/method-carriers.txt` keeps a `.claude/agents/` row only for an agent
  file that mentions `BUILD-METHOD.md` after unit 8, and words each kept row as carrying handed slices.
  Observed by AC13.
- **S18** — id 43. `memory/map/features/roles.md`'s `gate-legs` row gains the key
  `answered-calls self-test` and its `harness-hooks` row the key
  `PreToolUse tools/roles/answered-calls.js`; `answered-calls.test.sh` pins a non-zero
  `SELFTEST_FLOOR` and prints the agreed count line. Observed by AC14.
- **S19** — id 44. The `answered-calls self-test` row of `tools/gate-legs.json` carries the guard
  `{prefix}/roles/`, `{prefix}/hooks/scratch-guard.js`, `{prefix}/policy/policy-mirror.js`,
  `{prefix}/lib/`. Observed by AC14.
- **S20** — id 45. `answered-calls.js` finds `scratch-guard.js` as `agent-cap.js` finds its policy
  helper (`tools/hooks/agent-cap.js:465-467`), a sibling-kit path checked with `existsSync`; with none,
  it judges nothing, exits 0 and writes one stderr line naming the missing kit. `tools/roles/kit.toml`
  gains a `requires_if` edge to the hooks kit with its why. Observed by AC15.
- **S21** — id 37. An excerpt's heading anchor resolves through S15's `resolve_slices`; a symbol anchor
  is refused naming `not-installed: dTotalRecall's code record has not landed`. Observed by AC11.
- **S22** — id 47. `memory/map/features/roles.md:39` and `:136` say a role carries `## Facts` and the
  `### Method slices` it declares, never the Protocols section. Observed by AC14.
- **S23** — id 56. Unit 1 S6's verb is found by `resolve_kit_dir("codebase-map", "map_diff.py", KIT_DIR)`;
  when it is absent, fails or answers `unmeasured`, each claimed `record:` fact gets ` stale=unchecked`,
  which `FACT_RE` and its JavaScript copy in `tools/hooks/agent-cap.js` admit, and the render writes one
  note `roles: note — recall unchecked: <why>`. Observed by AC16.
- **S24** — id 57. Bounded slot readers. `run_slot_reader(argv, root, bound=30)` in `roles_lib.py` runs
  every slot subprocess of units 4, 9, 11, 12, 17, 18 and 2, unit 4's `gotchas.py --for-names` lookup
  among them; any outcome but its named success, a crash, an exit outside the reader's stated codes,
  garbled output or an expired bound, renders
  `not-installed: <cmd> exited <rc>` or `… timed out after 30s`, never `searched-empty` or `filled`.
  Unit 2's batch with no loop kit refuses, naming the kit and the per-task route. Observed by AC17.
- **S25** — id 59. `derive_role_set` leaves out a typed member no role file holds and writes one render note;
  `check_roles` reds on that member unless `instructions.exclude` (TOOL-dBoundRoles-20 S7) names it.
  Observed by AC18.
- **S26** — id 10. `ORDER_SLOTS` holds `instructions` exactly once, unit 4 S1's entry. Observed by AC19.
- **S27** — id 12. Unit 2's render refuses a batch of more units than `read_agent_limit(root)`, naming
  `runtime.agents-in-flight`, and a batch with no `--item`, naming the flag. Observed by AC19.
- **S28** — id 61. `derive_repair_producer` refuses before any write a `blob:` or `record:` segment that
  fails `roles_lib.SLUG_RE` (`tools/roles/roles_lib.py:77`) or names no `<MEMORY_ROOT>/builds/<slug>/README.md`.
  Observed by AC20.
- **S29** — id 60. `derive_attended` takes `transcripts=None`, passed to `runlog.py turns
  --transcripts`, so a fixture plants its transcripts without reading the live session. Observed by AC20.
- **S30** — id 5. `[return.establishes]` is no arm: `derive_return_arms` reads only tables carrying
  `outcome`, and `render_role` appends `establishes:list` to the role's own template line, a field of
  every outcome. Observed by AC21.
- **S31** — id 7. The repair carry's two rows planted: an ask whose `handed=` is a `blob:` excerpt of
  the spec renders the `### repair:<ask id>` block; one whose `handed=` is the spec's `record:` key
  renders the repaired fact in place. Observed by AC21.

## 3. Non-goals (OUT)

- Rewording the spec text of units 1 to 20. Each item is closed by what this pass builds; where a
  landed criterion cannot hold as written (unit 6 AC5, unit 14 AC5, unit 15 AC7), that unit's ledger
  answers it AMENDED, naming this unit.
- The 16 minors of `TOOL-dFurnishedOrders-30`, and the BLOCKER and HIGH findings units 22 to 28 close.
- The report's left-shift gates: the spec-lint rules, the checklist entries and the import gate. No
  clause of this build names them.

### Edges

- **consumes-from** `TOOL-dFurnishedOrders-1` — the fact-line recall run, whose resolution and failure form S23 add (id 56)
- **consumes-from** `TOOL-dFurnishedOrders-2` — the batch render, whose join, key read, bounds and loop-kit branch S13, S16, S24 and S27 settle (ids 33, 36, 57, 12)
- **consumes-from** `TOOL-dFurnishedOrders-3` — `derive_notices` and the runlog load, which S4 to S6 and S8 extend (ids 25, 58, 14, 38, 26)
- **consumes-from** `TOOL-dFurnishedOrders-4` — `render_slot`, `ORDER_SLOTS` and the bug-class lookup, whose reader S24 bounds and whose slot list S26 holds (ids 57, 10)
- **consumes-from** `TOOL-dFurnishedOrders-6` — `answered-calls.js`, its suite and its leg, whose failure path, version read, registries and sibling reach S1, S2 and S18 to S20 settle (ids 2, 23, 43, 44, 45)
- **consumes-from** `TOOL-dFurnishedOrders-7` — the contradiction key and the producer, read and checked by S9 and S28 (ids 29, 61)
- **consumes-from** `TOOL-dFurnishedOrders-8` — `resolve_slices` and the Protocols carry, which S15, S17, S21 and S22 settle (ids 35, 39, 37, 47)
- **consumes-from** `TOOL-dFurnishedOrders-9` — the matrix verb, whose subprocess S24 bounds (id 57)
- **consumes-from** `TOOL-dFurnishedOrders-10` — `write_role_metrics` and the runlog load, which S6 and S14 re-point (ids 14, 27, 34)
- **consumes-from** `TOOL-dFurnishedOrders-11` — the legacy slot's seed, key reads and ledger load, which S6, S8, S9, S10 and S24 settle (ids 27, 26, 29, 30, 57)
- **consumes-from** `TOOL-dFurnishedOrders-12` — `derive_role_set`, the map slot's keys and unfolds, which S8, S9, S11, S24 and S25 settle (ids 26, 29, 31, 57, 59)
- **consumes-from** `TOOL-dFurnishedOrders-14` — `read_excerpt` and the repair carry, whose anchor and fixture S21 and S31 settle (ids 37, 7)
- **consumes-from** `TOOL-dFurnishedOrders-15` — the tester's Write and Edit and its docs, which S3 confines and S7 tightens (ids 24, 51, 15)
- **consumes-from** `TOOL-dFurnishedOrders-16` — `derive_attended`, which S29 gives a transcripts root (id 60)
- **consumes-from** `TOOL-dFurnishedOrders-17` — the code slot's seed, reader and fixture, which S8, S10 and S24 settle (ids 26, 30, 16, 57)
- **consumes-from** `TOOL-dFurnishedOrders-18` — the instructions slot and its readers, which S24 bounds and S26 holds once (ids 57, 10)
- **consumes-from** `TOOL-dFurnishedOrders-19` — `validate_return`, `render_return_schema` and the establishes arm, which S12, S13 and S30 settle (ids 32, 33, 5)
- **consumes-from** `TOOL-dFurnishedOrders-20` — the problems slot's seed, which S10 reads from one call (ids 30, 16)
- **consumes-from** `TOOL-dFurnishedOrders-24` — the outcome branches, which S12 keeps out of `validate_return`'s own evaluation (id 32)
- **consumes-from** `TOOL-dFurnishedOrders-31` — S30 whole, the outcome filter of `derive_return_arms` and `establishes:list` on the template line, landed by unit 31 at order 10, which this pass finds present and records as closed (id 1 of the second audit)
- **hands-off** `TOOL-dFurnishedOrders-37` — AC5's import grep, `run_slot_reader`'s bound and class, the answered-call guard, the broken-index branch and the `FACT_RE` widening, which unit 37 S2, S3, S12, S24 to S26 and S32 settle, and the kickoff manifest re-stamp S17 makes after this unit's `tools/gate-legs.json` edit (ids 5, 14, 20, 38, 39, 37, 15, 26 of the second audit)

## 4. Design

### Why two units

This unit's write set is its Files touched below; `TOOL-dFurnishedOrders-30`'s is the workflows,
unattended, kickoff and memory-tree files, none of them here. Each kit's version line moves with its
own bytes, so the split follows the kits: a shared version file would make the halves intersect. No
criterion here reads a file unit 30 writes: the roles render reads no workflows script, the hooks read
no kickoff file, and S17's criterion reads only the `.claude/agents/` files. The two build concurrently.

### How an item closes

Each item states the built tree's end state, and the pass does what is missing or records that a
landed unit already left it so.

### Inventory

Minted: `load_kit_module`, `read_item_seed` (moved, its name unit 20's), `resolve_build_record` and
`run_slot_reader`, each answered OK by `python tools/lexicon/lexicon.py --suggest <name> --as
py.function`; the attribute value `stale=unchecked`; the label `truncated`; the private module names
`gov_runlog_extract` and `gov_tag_reader`.

### Migration

None: no stored data changes shape. S23's attribute is additive to the fact line's grammar.

### Rollout

Live at landing, at order 22, after every unit it lands on. `KIT_ROLES_VERSION`, the hooks kit's and the
runlog kit's versions move for the kit epoch leg.

### Files touched (estimate)

- `tools/roles/answered-calls.js`
- `tools/roles/answered-calls.test.sh`
- `tools/roles/roles_lib.py`
- `tools/roles/handoff.py`
- `tools/roles/check_roles.py`
- `tools/roles/render_agents.py`
- `tools/roles/kit.toml`
- `tools/roles/adopt-roles.test.sh`
- `tools/roles/README.md`
- `tools/hooks/scratch-guard.js`
- `tools/hooks/scratch-guard.test.sh`
- `tools/hooks/agent-cap.js`
- `tools/runlog/extract.py`
- `tools/runlog/selftest.py`
- `tools/gate-legs.json`
- `memory/map/features/roles.md`
- `memory/project/method-carriers.txt`
- `help/roles.md`
- `.claude/agents/` and `.claude/roles.json` (renders, by `render_agents.py --write`)

### Alternatives rejected

- **One batch.** The kits' version lines would put both halves in one write set, and M4 has disjoint
  minors build concurrently.
- **Correct unit 15's security row instead of confining the tester (S3).** It records a widening with
  no owner grant, which veto 3 refuses.
- **A scout-reported failure form for a slot reader (S24).** Each reader would invent its own; one
  bounded runner gives one spelling.

## 5. Production-readiness checklist

- security — S3 denies a `writes: none` role's in-repository write; S28 validates an agent-written
  path segment before any write; S20 never fails closed on a missing sibling kit.
- perf / scale — S10 removes two seed subprocesses per render; S24 caps each slot reader at 30 seconds.
- error / empty / loading states — S1, S23 and S24 each turn a failure into a named state.
- observability — S1's record, S23's note and S24's state line name the cause.
- risks — S12 narrows the Python evaluator; AC9 shows each defect still reported once.
- testing — AC1 to AC21 by probes and fixtures a pass builds; the arms of §7 at the close.
- migration — none.
- user docs — `help/roles.md` by S7.

## 6. Acceptance criteria

- **AC1** — When the AC5 payload of unit 6 is piped to `node answered-calls.js` with `.claude/roles.json`
  invalid and `AI_AGENT` `claude-code_2-1-292_agent`, it exits 0 recording `hook-failed` with the
  index's `why`; with `claude-code_2-1-308_agent`, it exits 1.
  Red when: a broken index runs silently, or a dashed version reads unreadable.
- **AC2** — When `node -e` calls `readSessionCli` with `claude-code_2-1-308_agent` and with
  `claude-code_2.1.308_x`, each returns `2.1.308`; with `claude-code_x` it returns null.
  Red when: the dash fold is missing.
- **AC3** — When `node scratch-guard.js` reads a `Write` payload with `agent_type` `gov-tester` aimed at
  a new file under `memory/`, it exits 2 naming the role; aimed outside the repository, it exits 0; with
  `agent_type` `gov-builder` aimed at the same file under `memory/`, it exits 0 as today.
  Red when: a `writes: none` role edits a record.
- **AC4** — When `python tools/runlog/runlog.py extract` reads a fixture whose Workflow result logs hold
  `[verify:ids-1] [harness: subagent output matched instruction-shaped pattern(s): a, b.`, the session
  holds one `notice` of class `security`, labels `a,b`, `src` `verify:ids-1`; a list past the 200-character
  lead yields whole names and `truncated`.
  Red when: a harness-route notice is dropped, or a cut name is recorded as a label.
- **AC5** — When `python -c` imports memory-recall's `extract.py` first and then calls
  `roles_lib.load_kit_module("runlog", "extract.py", "gov_runlog_extract")` twice, both return one module
  holding `derive_notices`; and `git grep -n -E "^\s*import extract|sys.path.insert" -- tools/roles/`
  prints only `read_cap_answer`'s lines.
  Red when: a by-name import picks the wrong `extract`.
- **AC6** — When `grep -n "outcome: probe"` runs over `help/roles.md` and `tools/roles/README.md` each
  prints a line; when a scratch repository made by S8's recipe, `git init -b main` and a commit of
  `.governance/policy.toml` holding `bypass = "never"` under `[core]`, is read by `python -c` calling
  `policy.resolve("core.bypass", <scratch>)`, it answers `never` with source `file`, and the same file
  written into a repository with no commit raises `Refusal`; and
  `grep -n "init -b main" tools/runlog/selftest.py tools/roles/adopt-roles.test.sh` prints a line per
  policy fixture S8 names.
  Red when: a docs grep passes at base, or a fixture's read passes by refusal.
- **AC7** — When `git grep -n -E "import policy|[^.]\bresolve\(" -- tools/roles/` runs, every code line
  it prints sits inside `read_policy_setting`; at base it prints only a comment of `roles_lib.py:110`.
  figure: the base line is PINNED 2026-10-26.
  Red when: a second policy reader is left.
- **AC8** — When `python handoff.py render --role gov-builder --item <tag>` runs in a fixture whose stub
  `loop_lib.py` appends one line per call to a counter file, the counter gains one line per render; and
  with `memory.map-unfold = all` and a stub `gov_tag.py` listing two namespaces, the map slot's unfolds
  name both.
  Red when: one render cuts slots from different seeds, or the registry is parsed twice.
- **AC9** — When `validate_return` reads a return with one wrong-typed template field and one malformed
  `establishes` row, it reports exactly two defects, neither a schema keyword; and a batch return
  dropping one unit names `tasks · dropped · <unit>`.
  Red when: one fault is reported in two vocabularies, or a dropped task passes.
- **AC10** — When `write_agent_ledger` and `write_role_metrics` write in a fixture build, both files are
  named `<today>-build-<first id><tail>`, and two `-role-metrics.tsv` files raise `RolesError` naming both;
  the locating glob and id regex of `handoff.py:755-792` appear once in `tools/roles/handoff.py`, inside
  `resolve_build_record`.
  Red when: the two writers keep two location rules.
- **AC11** — When `python -c` calls `roles_lib.resolve_slices` on a `doc` tag whose section holds a
  fenced `## ` line, its lines and text equal `gov_tag.py show <tag> --json`'s; and an excerpt cut by a
  symbol anchor is refused naming `not-installed`.
  Red when: two cutters disagree on one section's extent.
- **AC12** — When unit 2's batch render, `handoff.py render --role <dest> --unit <a> --unit <b>`, runs
  with the policy kit removed, it renders per batch and its notes carry the reader's missing-kit note.
  Red when: the caller probes the kit privately.
- **AC13** — When `grep -c "BUILD-METHOD.md"` runs over each `.claude/agents/` file
  `memory/project/method-carriers.txt` names, each prints at least 1, and every agent file that prints at
  least 1 has a row.
  Red when: the registry declares a carrier that no longer points at the method.
- **AC14** — When `python -c` reads `tools/gate-legs.json`, the `answered-calls self-test` row's guard
  is S19's four paths; `grep -n "answered-calls self-test" memory/map/features/roles.md` prints the
  claims line; `grep -c "Protocols and Facts" memory/map/features/roles.md` prints 0; and the suite holds a
  `SELFTEST_FLOOR=` above 0.
  Red when: the new leg reds the map and testsuite-count legs, or skips on a sibling change.
- **AC15** — When `node answered-calls.js` runs in a fixture holding the roles kit and no hooks kit, it
  exits 0 with one stderr line naming the hooks kit; and `tools/roles/kit.toml` holds a `requires_if`
  row naming `hooks`.
  Red when: a missing sibling fails every role read.
- **AC16** — When `handoff.py render` runs with the codebase-map kit removed, every claimed `record:`
  fact line carries ` stale=unchecked`, both `FACT_RE` copies parse it, and one `recall unchecked` note
  is printed.
  Red when: an unchecked fact reads as fresh.
- **AC17** — When each slot reader of S24 is replaced by a stub that exits 1 printing nothing, its slot
  renders `not-installed:` naming the command and 1; a stub sleeping past the bound renders
  `timed out`; unit 2's batch with no loop kit exits 1 naming the kit.
  Red when: a reader that never ran renders `searched-empty`.
- **AC18** — When `memory.project-map` is `structural-roles` and `instructions.exclude` names
  `gov-planner`, `handoff.py render` for `gov-builder` and `gov-architect` succeeds with one note naming
  `gov-planner`; with no exclusion, `check_roles.py` names it.
  Red when: one missing structural role refuses every render.
- **AC19** — When `python -c` counts `instructions` in `roles_lib.ORDER_SLOTS` it prints 1; and unit 2's
  render with five units over a limit of four, or with no `--item`, exits 1 naming
  `runtime.agents-in-flight` or `--item`.
  Red when: a slot is declared twice, or a bound is unreadable.
- **AC20** — When `roles_lib.derive_repair_producer` reads a `record:` key whose segment under
  `memory/builds/` is `..`, it raises before any write; and `derive_attended(root, session="s1", transcripts=<scratch>)` reads only the scratch root
  while `CLAUDE_CONFIG_DIR` names another.
  Red when: an agent-written segment reaches a path, or a fixture reads the live session.
- **AC21** — When `render_agents.py --write` runs, `.claude/agents/gov-builder.md`'s template line holds
  `establishes:list` and no `- or outcome:` line names `establishes`; and unit 14's render over a
  `blob:` repair ask holds a `### repair:` block, over a `record:` one the fact in place.
  Red when: a field renders as an outcome, or the carry's block row is never planted.

## 7. Gates

`roles catalogue` · `roles render wiring` · `roles render selftest` · `roles adopter self-test` · `scratch-guard self-test` · `agent-cap self-test` · `format-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `runlog selftest` · `pre-push run-log line` · `run-gates canary` · `run-gates gov canary` · `run-gates run-log line` · `method carriers (every pointer declared)` · `method-carriers self-test` · `codebase-map coverage + freshness` · `testsuite counts (every bar self-test prints one)` · `measure-legs selftest` · `recall floor` · `recall floor arms` · `check-wiring self-test` · `policy fixtures` · `kit epoch (shipped bytes move, the version moves)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/roles/adopt-roles.test.sh · covers AC5 AC6 AC7 AC8 AC9 AC10 AC11 AC12 AC16 AC17 AC18 AC19 AC20 AC21 · stub readers, a batch, a fenced section, a planted repair ask and the policy fixtures of units 11, 12 and 17, staged by restoring the second seed call and a fixture's uncommitted policy file · none
New arm: tools/hooks/scratch-guard.test.sh · covers AC3 · a `gov-tester` write inside and outside the repository, staged by dropping the new step · none
New arm: tools/runlog/selftest.py · covers AC4 AC6 · a labelled log line, a list past the lead and unit 3's policy fixture, staged by reading notification results only and by leaving that fixture's policy file uncommitted · none

## 8. Open questions

- **F1 — How long may a slot reader run?** Options: (a) 30 seconds per reader; (b) unbounded; (c) the
  key's own budget. (b) is the defect; (c) prices bytes, not time. RESOLVED (agent, 2026-10-26,
  delegated): (a), rung 3, PINNED 2026-10-26 by this choice. widens: none · relaxes: none
- **F2 — What does a slot with no loop kit do in a batch?** Options: (a) refuse the batch naming the
  per-task route; (b) admit with a note. (b) frames tasks of a role at an item nobody checked it acts in.
  RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, deny by default. widens: none · relaxes: none
- **F3 — How is a `writes: none` role's write held?** Options: (a) S3's step; (b) correct unit 15's §5
  and record a widening. (b) needs an owner grant (veto 3). RESOLVED (agent, 2026-10-26, delegated):
  (a), rung 3, the survivor. widens: none · relaxes: none
- **F4 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-26,
  delegated): `**Derived:**` naming `PLAY-dClosedLoop-2`, rung 3, the precedent `TOOL-dBoundRoles-39`
  §8 F1 records. widens: none · relaxes: none
- **F5 — The units this one lands on are unbuilt.** Units 1 to 20 and 24 are specced and unbuilt at
  `5ff43572`. RESOLVED (agent, 2026-10-26, delegated): the build run re-grounds on each at the pass and
  records any item a landed unit already closed, rung 1, the brief's rule. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, the round-1 spec audit's roles, hooks and runlog minors batched.
- rev-2 · 2026-10-26 · §3 · a consumes-from edge to unit 31, which lands S30 at order 10, and a
  hands-off edge to unit 37 (ids 1, 5, 14, 20, 38, 39, 37, 15 and 26 of the second audit).

## 10. Reuse audit

The seams extended: `resolve_kit_dir` (`tools/roles/roles_lib.py:97`) under S6's loader;
`read_policy_setting` (TOOL-dBoundRoles-21 S1) for S9 and S16; `write_agent_ledger`'s locator
(`tools/roles/handoff.py:755-792`), extracted at its second caller by S14; `loadRoleIndex` and the
write gate's step order (`tools/hooks/scratch-guard.js:952`, `:1090-1112`) for S1 and S3; the sibling
path of `tools/hooks/agent-cap.js:465-467` for S20. `python tools/codebase-map/reuse_lookup.py "locate
or create a build folder record file by its name tail"` ranked `build`, `records` and `build_commit`,
none a record locator, so S14 extracts one; `"a hook that records its own failure when the role index
cannot be read"` ranked `read`, `read_text` and `read_conf_key`, none a hook failure path. The recall
probe returned KICK-dKeptSession-64 and -65, two earlier minors batches, and units 6 and 14's file
lists, none disagreeing with source.

Recall terms used: `python tools/memory-recall/query.py "which minor findings of the dFurnishedOrders
spec audit land on the roles kit" --terms "minors batch roles handoff read_policy_setting read_item_seed
resolve_build_record slot subprocess not-installed answered-calls scratch-guard"`
