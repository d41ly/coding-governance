# TOOL-dBoundRoles-50 — the round-1 audit of units 37 to 44, its 24 roles-code minors: one fence walker per language, fence-aware marker readers, live leg names, waiver and registry rows kept true, and criteria that can fail

**Status:** OPEN · rev-4 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 30 · advances TOOL-dBoundRoles-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-51 TOOL-dBoundRoles-52 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-65 TOOL-dBoundRoles-66 TOOL-dBoundRoles-67 TOOL-dBoundRoles-68 TOOL-dBoundRoles-69 |
| [2026-10-26-build-TOOL-dBoundRoles-45-round2-fix-return.md](../build/2026-10-26-build-TOOL-dBoundRoles-45-round2-fix-return.md) | research | TOOL-dBoundRoles-43 TOOL-dBoundRoles-45 TOOL-dBoundRoles-49 TOOL-dBoundRoles-51 |
| [2026-10-26-prompt-TOOL-dBoundRoles-45-round2-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dBoundRoles-45-round2-fix-brief.md) | research | TOOL-dBoundRoles-45 TOOL-dBoundRoles-43 TOOL-dBoundRoles-49 TOOL-dBoundRoles-51 |
| [2026-10-26-review-TOOL-dBoundRoles-45-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dBoundRoles-45-spec-audit-round1.md) | spec-audit | TOOL-dBoundRoles-49 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-48 TOOL-dBoundRoles-47 TOOL-dBoundRoles-51 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the eight promoted specs 37 to 44
(`memory/builds/dBoundRoles/reviews/2026-10-26-review-TOOL-dBoundRoles-37-spec-audit-round1.md`) confirmed
five HIGH findings, `TOOL-dBoundRoles-45` to `-49`, and 21 MEDIUM and 11 LOW. BUILD-METHOD M4 batches
the minors, split in two by M6 (§4 "Why two units"). This unit takes the 17 MEDIUM and 7 LOW whose items
write or read the roles code, the hooks, govkit's self-test, the dead-path waivers and the spawn-idiom
registry: report ids 4, 5, 6, 10, 11, 12, 15, 18, 19, 21, 22, 25, 26, 27, 28, 29, 30, 33, 35, 36, 37, 38,
39 and 40. `TOOL-dBoundRoles-51` takes the other 8. Each id is its own item, even where the report merged
two: ids 4 and 29 share item M3, 11 and 26 item M6, 27 and 33 item M11, and ids 30 and 6 are one overlap
at two grades, items M13 and L1.

| Report item | Report id | Lands on | Scope item |
|---|---|---|---|
| M3 | 4, 29 | unit 43 §7 | S1, S2 |
| M4 | 5 | unit 43 S41, §7 | S3 |
| L1 | 6 | unit 44 §4, unit 43 §4 | S4 |
| M13 | 30 | unit 43 S2, Files touched | S5 |
| M5 | 10 | unit 38 AC4 | S6 |
| M6 | 11, 26 | unit 41 AC3 | S7, S8 |
| M8 | 18 | unit 38 S3, §10 | S9 |
| M9 | 19 | unit 37 S1 | S10 |
| M10 | 25 | unit 38 S4 | S11 |
| M11 | 27, 33 | unit 42 S1, S4, AC1, AC4 | S12, S13 |
| M12 | 28 | unit 42 AC4 | S14 |
| M17 | 37 | unit 42 S5 | S15 |
| M15 | 35 | unit 38 AC1, AC3, §7 | S16 |
| M16 | 36 | unit 38 S3, S4 | S17 |
| M18 | 38 | unit 40 S3, §5 | S18 |
| L4 | 12 | unit 39 S1 to S3 | S19 |
| L6 | 15 | unit 37 §8 F2 | S20 |
| L7 | 21 | unit 39 S1, §10 | S21 |
| L8 | 22 | unit 43 S34 | S22 |
| L9 | 39 | unit 38 AC5 | S23 |
| L10 | 40 | unit 39 AC4 | S24 |

## 2. Scope (IN)

- **S1** — id 4. Live leg names after the rename. Unit 25's pass, which renames `agent-cap self-test` to
  `spawn-guard self-test` in `tools/gate-legs.json`, makes the same rename on the §7 leg line of every
  non-terminal spec of this build that names the old leg, unit 43's and this one's, each a rev bump with
  its §9 line, as unit 25's hands-off edge to this unit says. This pass makes any bump still missing.
  Observed by AC1.
- **S2** — id 29. Unit 43's arm runs under the leg that exists. The `New arm:` line of unit 43 for
  AC50 names `tools/roles/spawn-guard.test.sh`, and on the built tree the one leg whose `argv` runs that
  suite is `spawn-guard self-test`; no leg is named `agent-cap self-test`. Observed by AC2.
- **S3** — id 5. Dead-path rows for unit 43's lines. The pass runs `bash tools/check-dead-paths.sh
  --list` for `agent-cap.js` and `agent-cap.test.sh` over `tools/govkit/steps/spawn_guard_pack.py` and
  `tools/govkit/selftest.py` as unit 43 leaves them, and writes or re-keys their rows in
  `tools/dead-path-waivers.txt` with `TOOL-dBoundRoles-42` S5's two reasons, so no needle line is
  unwaived and no row is stale. Observed by AC3.
- **S4** — id 6. The account of how 43 and 44 built. The pass records in its ledger the order of unit
  43's and unit 44's pass commits, serial at orders 28 and 29, and the one path both wrote, the build
  README's generated region. Observed by AC4.
- **S5** — id 30. The build index agrees after unit 43's rev bump of spec 25. `python
  tools/memory-tree/gen_build_index.py --check` exits 0 on the built tree. A red is returned to the main
  loop, whose commit regenerates the index; this unit writes no generated index (§4). Observed by AC5.
- **S6** — id 10. Unit 38 AC4's render half, observed where it can hold. From `TOOL-dBoundRoles-45` on a
  typed value is unfenced, so `--input question=` holding a four-backtick line nothing closes refuses as
  38 AC4 says; unit 38's ledger answers that half AMENDED, naming unit 45. The pass also renders a
  `--framed-by` work order whose `framing:job` field opens a fence it never closes, 38 S5's real target,
  and sees it refused. Observed by AC6.
- **S7** — id 11. Unit 41 AC3 inside one render. Over AC1's post-change render, the hashed `## Task`
  equals the join of the parts `render_handoff` appended, and the marker's task-sha equals
  `derive_section_sha` of the written `## Task`. Unit 41's ledger answers AC3 AMENDED, naming this unit.
  Observed by AC7.
- **S8** — id 26. Unit 41 AC3 across its own change. A handed spec with no grammar span plus a typed
  question renders at the parent of unit 41's pass commit and at that commit, each in a scratch worktree,
  and the two `## Task` sections and task-shas are equal. Observed by AC8.
- **S9** — id 18. One fence walker per language. `checkBuildable`'s H1 scan
  (`tools/hooks/scratch-guard.js:887-891`) reads lines through `readUnfencedLines`. `scanMessageLines`
  (`tools/hooks/format-guard.js:208-216`) derives each row's `fenced` flag from `readUnfencedLines`, which
  with `read_unfenced_lines` first gains its CommonMark rule: a backtick run whose line also holds a
  backtick after the run opens no fence (§8 F2). No `fenced = !fenced` toggle is left in the hooks kit.
  Observed by AC9.
- **S10** — id 19. Unit 37's agent predicate carries its default. `derive_roles_expected`'s `agents` is
  the slots whose `keys.get("agent", "true") == "true"`, the rule `tools/roles/render_agents.py:275`
  renders by, read through the installed kit's `load_roles`. Observed by AC10.
- **S11** — id 25. Every marker reader is fence-aware. `extract_unfenced_marker(text)` in `tools/roles/roles_lib.py`
  returns the first `MARKER_RE` line `read_unfenced_lines` yields, or None; `tools/roles/handoff.py:437`,
  `:834` and `tools/roles/roles_lib.py:553` call it in place of `MARKER_RE.search`. Observed by AC11.
- **S12** — id 27. The spawn-idiom registry matches the tree. `memory/project/spawn-idiom-sites.txt`
  carries no row keyed on `tools/hooks/agent-cap.test.sh`, the suite unit 25 deletes, and a row for each
  registry-class site the moved arms bring into `tools/roles/spawn-guard.test.sh` that the scan finds.
  Observed by AC12.
  **Readers:** by name: `tools/gate-lint/sh_hygiene.py`, whose `--spawn-idioms` registry check reds a
  row the scan no longer finds · by value: `tools/gate-lint/sh_hygiene.py`'s per-row count compare.
- **S13** — id 33. Unit 25's readers derived from both basenames. The pass runs
  `git grep -l -E 'agent-cap\.(js|test\.sh)' -- ':!memory/builds' ':!memory/ledger'` on the built tree
  and records each file it prints with the unit whose disposition answers it, 25, 42, 44 or this one.
  Observed by AC13.
- **S14** — id 28. Unit 42 AC4's grep admits the registry it writes. The live-carrier grep runs with
  `':!tools/dead-path-waivers.txt'` beside `':!memory'` and `':!.governance/steps'`, and prints only the
  files 42 S4 admits. Unit 42's ledger answers AC4 AMENDED, naming this unit. Observed by AC14.
- **S15** — id 37. A waived line is a step's spelling, never a live reference.
  `tools/hooks/kit.toml` holds no `include`, `to` or `version_from` key naming `agent-cap.js` or
  `agent-cap.test.sh`, and `tools/govkit/selftest.py`'s `KIT_DIRS` anchors the hooks kit on a file that exists
  (`:115`). Where unit 25 left one, this pass rewrites it and re-keys S3's rows. The ledger records each
  waived row's step row or fixture label. Observed by AC15.
- **S16** — id 35. The JS walker's length rule is observed. A case in the scratch-guard suite feeds
  `readUnfencedLines` a four-backtick fence holding a three-backtick line and a separate five-backtick
  line; a case in the spawn-guard suite hands
  `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-13.md` through a render and pipes the
  payload to `tools/roles/spawn-guard.js`, which admits it. Observed by AC16.
- **S17** — id 36. The walker's open-fence yield has a meaning at each reader. `extract_prompt_marker`
  and S11's `extract_unfenced_marker` return None; the Python `FACT_RE` reader refuses, naming the line;
  `readWorkOrderAllowance` denies the write, naming the line. None raises. Observed by AC17.
- **S18** — id 38. Unit 40's replay has a bound and a shell. Each `SubagentStop` command runs through
  `govkit_module().resolve_bash()`, as `check_roles_install` runs check-wiring
  (`tools/govkit/selftest.py:2828`), with `CLAUDE_PROJECT_DIR` exported, under a 30-second timeout. A
  timeout is red, naming the command. Observed by AC18.
- **S19** — id 12. Unit 5's `agent_type` exit is reachable again. Two plants join
  `tools/roles/render_agents.py --selftest`: a marked direct-spawn transcript under
  `subagents/agent-<id>.jsonl` with `agent_type` absent, and the same with a type naming no agent-true
  role. Each prints nothing and writes no record. Observed by AC19.
- **S20** — id 15. Unit 37's derivation is present, not only the literal absent. The pass records
  `grep -n 'def derive_roles_expected' tools/govkit/selftest.py` and the empty output of 37 AC3's grep
  together in its ledger. Observed by AC20.
- **S21** — id 21. One spelling of the session layout in `handoff.py`. `resolve_subagent_dir(sdir,
  run_id)` returns `sdir / "subagents"`, or with a run id `sdir / "subagents" / "workflows" / run_id`;
  the `agents` verb (`tools/roles/handoff.py:847`, `:854`, `:885`) and `TOOL-dBoundRoles-39`'s route
  test read the layout through it. Observed by AC21.
- **S22** — id 22. Unit 43 S34's rate over one population. Over this build's specs and brief records
  holding a backticked `blob:`, `record:` or `cmd:` span, the ledger records the count of such files, the
  count rendered and the count refused, each with the command that printed it. Observed by AC22.
- **S23** — id 39. The fence docs carry a phrase only they write. `tools/roles/README.md` and the
  README holding the spawn guard's rule-6 paragraph after unit 25 each say `handed content is fenced`.
  Observed by AC23.
- **S24** — id 40. The return-check docs carry a phrase only they write. `tools/roles/README.md`'s
  `check-return` paragraph says it `grades a direct spawn` only. Observed by AC24.

## 3. Non-goals (OUT)

- Rewording the specs of units 1 to 49. Each item is closed by what this pass builds or observes; a
  criterion that cannot hold as written is answered AMENDED in that unit's ledger, as each repaired
  spec's hands-off edge to this unit says.
- The 8 minors of `TOOL-dBoundRoles-51` and the HIGH findings `TOOL-dBoundRoles-45` to `-49`.
- The report's left-shift gates: the spec-coherence checklist, the same-order disjointness check, the
  spec-tokens rename mode, the run-each-criterion-at-base check and the fence-toggle lint. S9's single
  walker is the regression for id 18; no clause of this build names the others.

### Edges

- **consumes-from** `TOOL-dBoundRoles-25` — the leg rename, carried into the live §7 lines by its pass, and the deleted suite whose registry rows S12 answers (ids 4, 27, 29 and 33)
- **consumes-from** `TOOL-dBoundRoles-37` — `derive_roles_expected`, whose predicate S10 restates and whose presence S20 records (ids 15 and 19)
- **consumes-from** `TOOL-dBoundRoles-38` — the walkers, the marker readers and AC4, which S6, S9, S11, S16, S17 and S23 complete (ids 10, 18, 25, 35, 36 and 39)
- **consumes-from** `TOOL-dBoundRoles-39` — the route test and its docs, which S19, S21 and S24 complete (ids 12, 21 and 40)
- **consumes-from** `TOOL-dBoundRoles-40` — the `SubagentStop` replay, which S18 bounds (id 38)
- **consumes-from** `TOOL-dBoundRoles-41` — the graded text and AC3, which S7 and S8 observe (ids 11 and 26)
- **consumes-from** `TOOL-dBoundRoles-42` — the class table, AC4 and S5's waiver rows, which S12 to S15 complete (ids 27, 28, 33 and 37)
- **consumes-from** `TOOL-dBoundRoles-43` — its §7, S41's lines, S2's rev bump and S34's counts, which S1 to S5 and S22 complete (ids 4, 5, 6, 22, 29 and 30)
- **consumes-from** `TOOL-dBoundRoles-45` — the typed value written unfenced, through which S6 observes unit 38 AC4's render half (id 10)
- **hands-off** `TOOL-dBoundRoles-56` — S9's `checkBuildable` read through `readUnfencedLines`, whose twins `parse_spec_h1` and KICK R4 unit 56 moves onto the same rule (id 20 of the round-1 audit of units 45 to 51)
- **hands-off** `TOOL-dBoundRoles-58` — S8, S21, AC3, AC4, AC7, AC12, AC20, AC22 and §3, which unit 58 restates, folding `resolve_subagent_dir` into `resolve_agent_transcript` (ids 3, 17, 24, 25, 31, 47 and 48 of the round-1 audit of units 45 to 51)
- **hands-off** `TOOL-dBoundRoles-64` — the spawn-guard arm of §7, whose floored assertions unit 64 carries in a term naming this unit (ids 1, 13 and 19 of the round-1 audit of units 61 to 63)
- **hands-off** `TOOL-dBoundRoles-66` — the spawn-guard arm of §7, whose assertions unit 66 counts against the term naming this unit, under a `# ---- ` header naming it (ids 3 and 20 of the round-1 audit of unit 64)

## 4. Design

### Why two units

The minors split into two write sets that meet none of M6's three clauses. This unit writes
`tools/roles/`, `tools/hooks/`, `tools/govkit/selftest.py`, `tools/dead-path-waivers.txt` and
`memory/project/spawn-idiom-sites.txt`. `TOOL-dBoundRoles-51` writes the memory-recall Skill's template
and render and, where a build commit wrote it, `.governance/policy.json`. Every item whose criterion reads
a file this unit writes is here: S3 and S14 read lines of `selftest.py` that S15 may rewrite, S13 and S12
read the suites this unit edits, and S22 renders through `handoff.py`. Unit 51's criteria read
`memory/` records, two ledgers, the commit log and its own files. Neither unit edits a generator, writes a
generated index, `memory/DECISIONS.md`, a backlog shard or the run-state file, which is why S5 reads the
index and returns a red rather than regenerating it.

### How an item closes

As unit 43 §4 states for its batch: the batch builds after the units it repairs, each item states the
built tree's end state, and the pass does what is missing or records that a landed unit already left it.

### Inventory

Minted: `extract_unfenced_marker` and `resolve_subagent_dir` (`py.function`), the two plants of S19, the waiver rows
of S3 and S15, and the registry rows of S12. Each function name is asked of
`python tools/lexicon/lexicon.py --suggest <name> --as py.function` at the pass.

### Migration

None: no stored data changes. S9's CommonMark rule reads a line such as three backticks followed by
text holding a backtick as text, which no rendered handoff writes.

### Rollout

Live at landing, at order 30, after every unit it repairs and beside `TOOL-dBoundRoles-51`.

### Files touched (estimate)

- `tools/roles/roles_lib.py`
- `tools/roles/handoff.py`
- `tools/roles/render_agents.py`
- `tools/roles/adopt-roles.test.sh`
- `tools/roles/spawn-guard.test.sh`
- `tools/roles/README.md`
- `tools/hooks/scratch-guard.js`
- `tools/hooks/scratch-guard.test.sh`
- `tools/hooks/format-guard.js`
- `tools/hooks/format-guard.test.sh`
- `tools/hooks/kit.toml`
- `tools/hooks/README.md`
- `tools/govkit/selftest.py`
- `tools/dead-path-waivers.txt`
- `memory/project/spawn-idiom-sites.txt`

### Alternatives rejected

- **One batch unit.** The two halves meet no M6 clause, and M4 has disjoint minors build concurrently.
- **Waive a live reference under a step's reason (S15).** The dead-path leg would then be silenced where
  unit 25 partly failed.
- **Keep `scanMessageLines` as a second walker (S9).** The two rules disagree on a long fence holding a
  short run, the class unit 38 closes; §8 F2.

## 5. Production-readiness checklist

- security — S11 and S17 close the quoted-marker reading on three readers and the crash on an open
  fence; S15 keeps a waiver from hiding a live reference. No new write path.
- perf / scale — greps, probes, a few renders, one dead-path listing and one replay bound.
- error / empty / loading states — S17 gives every reader of the open-fence yield a stated result.
- observability — the ledger records S4, S13, S15, S20 and S22.
- risks — S1 depends on unit 25's pass reading its edge; this pass makes any bump still missing.
- testing — AC1 to AC24 by probe, render, payload, grep and checker listing; the arms of §7 at the close.
- migration — none.
- user docs — none under `help/`; the READMEs by S23 and S24.

## 6. Acceptance criteria

- **AC1** — When a `python -c` probe reads the leg line of every non-terminal spec under
  `memory/builds/dBoundRoles/spec/` and the names in `tools/gate-legs.json`, every backticked leg name is
  in the manifest. Red when: a live spec names a leg unit 25 renamed.
- **AC2** — When `python -c` lists the `tools/gate-legs.json` rows whose `argv` names the spawn-guard
  suite S2 names, it prints `spawn-guard self-test` alone, and no row is named `agent-cap self-test`.
  Red when: unit 43's arm sits in no leg.
- **AC3** — When `bash tools/check-dead-paths.sh --list` runs on the built tree, it prints no unwaived
  hit and no stale row in `spawn_guard_pack.py` or govkit's self-test module. Red when: a line unit 43
  added is unwaived, or a re-keyed line leaves a stale row.
- **AC4** — When `grep -n 'TOOL-dBoundRoles-43' <this unit's acceptance ledger>` runs, it names the two
  commits' order and the shared path. Red when: the ledger repeats the claim that the two built together.
- **AC5** — When `python tools/memory-tree/gen_build_index.py --check` runs on the built tree, it exits
  0. Red when: the build README's units region is stale after unit 43's rev bump.
- **AC6** — When the roles adopter fixture renders `--input question=` holding an unclosed four-backtick
  line, and separately a `--framed-by` work order whose `framing:job` opens a fence it never closes, each
  exits non-zero naming the block and writes no file. Red when: an open fence in authored text renders.
  fixture: a scratch repository with the roles kit installed, under `%TEMP%`, short-pathed.
- **AC7** — When a `python -c` probe re-joins unit 41 AC1's appended parts and hashes the written
  `## Task` with `handoff.derive_section_sha`, the join equals the section and the hash equals the
  marker's task-sha. Red when: building the graded text changed the hashed section.
- **AC8** — When `handoff.py render` runs the same no-span inputs in scratch worktrees at unit 41's pass
  commit and at its parent, the two `## Task` sections and task-shas are equal. Red when: unit 41 changed
  the bytes it hashes. fixture: two worktrees under `%TEMP%`, short-pathed, removed after.
- **AC9** — When `grep -n 'fenced = !fenced' tools/hooks/*.js` runs it prints nothing, a
  `checkBuildable` case whose spec holds an H1 line inside a four-backtick fence holding a three-backtick
  line names the real H1, and a format-guard row inside such a fence reads fenced. Red when: a second
  walker remains, or a short run closes a long fence.
- **AC10** — When a `python -c` probe calls `selftest.derive_roles_expected` over a scratch copy of the
  roles kit carrying one more role file whose front matter omits `agent:`, the agent set gains that slot.
  Red when: the predicate needs an explicit `agent: true`.
- **AC11** — When `grep -n 'MARKER_RE.search' tools/roles/*.py` runs it prints only `extract_unfenced_marker`'s
  line, and R15 over a stand-in-tailed prompt whose only marker sits inside a fence reports the marker
  missing. Red when: a reader takes a quoted marker for the file's own.
- **AC12** — When `grep -c 'agent-cap.test' memory/project/spawn-idiom-sites.txt` runs it prints 0, and
  `python tools/gate-lint/sh_hygiene.py --spawn-idioms memory/project/spawn-idiom-sites.txt` exits 0.
  Red when: a row names the deleted suite, or a moved site has no row.
- **AC13** — When S13's `git grep` runs on the built tree, every file it prints has a line in this unit's
  ledger naming its disposition. Red when: a reader of either basename is unanswered.
- **AC14** — When `git grep -l -F 'agent-cap.js' -- ':!memory' ':!.governance/steps' ':!tools/dead-path-waivers.txt'`
  runs, it prints only the files 42 S4 admits. Red when: an unadmitted live carrier names the hook.
- **AC15** — When `grep -nE '^(include|to|version_from)\b.*agent-cap\.(js|test\.sh)' tools/hooks/kit.toml`
  and `grep -nF '("hooks", "agent-cap.js")' tools/govkit/selftest.py` run, both print nothing. Red when:
  a live include or anchor names the deleted file.
- **AC16** — When `node -e` feeds `readUnfencedLines` S16's long fence, it yields nothing from inside
  it; and an `Agent` payload carrying a render that hands spec 13, piped through `node` to the roles
  pack's `spawn-guard.js` (S16), exits 0. Red when: a `readUnfencedLines` that closes a long fence on a
  run of three passes.
- **AC17** — When `python -c` feeds `extract_prompt_marker`, `extract_unfenced_marker` and the `FACT_RE` reader a text
  ending inside a fence, and `node -e` feeds `readWorkOrderAllowance` the same, each returns its stated
  result with no exception. Red when: a reader raises or guesses on the open-fence yield.
- **AC18** — When unit 40's replay runs with a staged `SubagentStop` hook that sleeps 40 seconds, it is
  red naming that command. Red when: a hung hook is recorded as named but not red.
- **AC19** — When `python tools/roles/render_agents.py --selftest` runs, the two plants of S19 print
  nothing and write no record, and with unit 5 S2's `agent_type` exit removed they block. Red when: the
  exit has no plant that reaches it.
- **AC20** — When `grep -n 'derive_roles_expected' <this unit's acceptance ledger>` runs, it names the
  definition's line. Red when: the ledger records only the literal's absence.
- **AC21** — When `grep -n '"subagents" / "workflows"' tools/roles/handoff.py` runs, it prints only
  `resolve_subagent_dir`'s line. Red when: the layout is spelled twice in the file.
- **AC22** — When `grep -n 'refused' <this unit's acceptance ledger>` runs, it names the three counts of
  S22, each with its command. Red when: a rate's two counts come from two populations.
- **AC23** — When `grep -n 'handed content is fenced' tools/roles/README.md` and the rule-6 README run,
  each prints one line. Red when: the phrase is absent, which the base text cannot satisfy.
- **AC24** — When `grep -n 'grades a direct spawn' tools/roles/README.md` runs, it prints one line on the
  `check-return` paragraph. Red when: the docs item is unwritten.

## 7. Gates

`roles adopter self-test` · `roles catalogue` · `roles render selftest` · `agent-cap self-test` · `scratch-guard self-test` · `format-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor` · `recall floor arms` · `dead-path carriers (deleted files still named)` · `shell hygiene (a fork spent on builtin work)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

`agent-cap self-test` is named because `tools/hooks/` trips its guard at base; S1 renames it on this line
when unit 25 renames the leg.

New arm: tools/hooks/scratch-guard.test.sh · covers AC9 AC16 AC17 · the long-fence walker, `checkBuildable`'s fenced H1 and the allowance reader on an open fence, staged by a walker that closes on a run of three · none
New arm: tools/roles/adopt-roles.test.sh · covers AC6 AC11 · the open fence in a typed value and a framing field, and the fenced-only marker, staged by a render that skips 38 S5's walk and a reader calling `MARKER_RE.search` · none
New arm: tools/roles/render_agents.py · covers AC19 · the two `agent_type` plants, staged by removing unit 5 S2's exit · none
New arm: tools/govkit/selftest.py · covers AC10 AC18 · a role omitting `agent:` and a sleeping `SubagentStop` hook, staged by an explicit-true predicate and an unbounded replay · none
New arm: tools/roles/spawn-guard.test.sh · covers AC16 · spec 13's handoff piped to the guard, staged by a `readUnfencedLines` that closes on a run of three · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a carry of a clause. The batch carries no clause; veto 1 discards
  (b). RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1
  set. widens: none · relaxes: none
- **F2 — Route `scanMessageLines` through the walker, or record why it stays (id 18)?** Options: (a)
  give both walkers CommonMark's info-string rule and route it; (b) keep it with a recorded reason. (b)
  leaves two rules in one kit, one of which closes a long fence on a short run; (a) satisfies the report's
  grep over every walker. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the more feature-rich.
  widens: none · relaxes: none
- **F3 — Who renames the leg in the live §7 lines (ids 4, 29)?** Options: (a) unit 25's pass, which makes
  the rename, carried by its edge; (b) this pass at order 30. Under (b), `--dispatch` runs the spec-token
  checker over the live tree before each pass from order 27 on and reds on the stale name. RESOLVED
  (agent, 2026-10-26, delegated): (a), rung 3, the one survivor; S1 makes any bump (a) missed.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, the roles-code half of the round-1 minors of units 37 to 44:
  17 MEDIUM and 7 LOW, each id its own item.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the bullets mirroring TOOL-dBoundRoles-56 and -58, promotions of the round-1 audit of units 45 to 51; nothing else moved.
- rev-3 · 2026-10-26 · §3 · the Edges block gains the bullet mirroring TOOL-dBoundRoles-64, the minors batch of the round-1 audit of units 61 to 63; nothing else moved.
- rev-4 · 2026-10-26 · §3 · the Edges block gains the bullet mirroring TOOL-dBoundRoles-66, the minors batch of the round-1 audit of unit 64; nothing else moved.

## 10. Reuse audit

The seams are `TOOL-dBoundRoles-38`'s two walkers, which S9, S11 and S17 extend rather than copy; the
dead-path waiver registry (`tools/dead-path-waivers.txt`, whose `<path>\t<ordinal>\t<line-text>\t<reason>`
grammar S3 and S15 write); the spawn-idiom registry check (`tools/gate-lint/sh_hygiene.py`); govkit's
`resolve_bash` (`tools/govkit/selftest.py:2828`); and `handoff.py`'s own session layout (`:847`, `:854`,
`:885`), which S21 lifts before citing any other kit.
`python tools/codebase-map/reuse_lookup.py "skip lines inside a fenced code block when reading a document line by line"`
ranked `read`, `read_text`, `skip` and `read_conf`, none a fence walker, so no seam fits beyond 38's
walkers.

Recall terms used: `python tools/memory-recall/query.py "how is handed content kept from forging machine-read lines in a work order" --terms "fence walker marker reader dead-path waiver spawn-idiom registry leg rename session layout sentinel"`
