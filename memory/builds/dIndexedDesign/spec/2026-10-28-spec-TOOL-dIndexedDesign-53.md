# TOOL-dIndexedDesign-53 — the round-1 audit of units 39 to 46: its 20 minors batched, one home for each record number, one reader per opt-in, and every criterion made to observe

**Status:** OPEN · rev-1 · 2026-10-28 · node d · Tier-2 · base 57bc3b91 · streams tooling · order 21 · advances TOOL-dIndexedDesign-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md) | journal | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-31 TOOL-dIndexedDesign-32 TOOL-dIndexedDesign-33 TOOL-dIndexedDesign-34 TOOL-dIndexedDesign-35 TOOL-dIndexedDesign-36 TOOL-dIndexedDesign-37 TOOL-dIndexedDesign-38 TOOL-dIndexedDesign-39 TOOL-dIndexedDesign-40 TOOL-dIndexedDesign-41 TOOL-dIndexedDesign-42 TOOL-dIndexedDesign-43 TOOL-dIndexedDesign-44 TOOL-dIndexedDesign-45 TOOL-dIndexedDesign-46 TOOL-dIndexedDesign-47 TOOL-dIndexedDesign-48 TOOL-dIndexedDesign-49 TOOL-dIndexedDesign-50 TOOL-dIndexedDesign-51 TOOL-dIndexedDesign-52 |
| [2026-10-28-build-TOOL-dIndexedDesign-47-promoted-fix-return.md](../build/2026-10-28-build-TOOL-dIndexedDesign-47-promoted-fix-return.md) | research | TOOL-dIndexedDesign-47 TOOL-dIndexedDesign-49 TOOL-dIndexedDesign-52 |
| [2026-10-28-prompt-TOOL-dIndexedDesign-47-promoted-fix-brief.md](../prompts/2026-10-28-prompt-TOOL-dIndexedDesign-47-promoted-fix-brief.md) | research | TOOL-dIndexedDesign-47 TOOL-dIndexedDesign-49 TOOL-dIndexedDesign-52 |
| [2026-10-28-prompt-TOOL-dIndexedDesign-53-1-spec-writer.md](../prompts/2026-10-28-prompt-TOOL-dIndexedDesign-53-1-spec-writer.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 39 to 46
(`memory/builds/dIndexedDesign/reviews/2026-10-28-review-TOOL-dIndexedDesign-39-spec-audit-round1.md`)
exited CONVERGED with 26 confirmed findings. BUILD-METHOD M4 promotes every MEDIUM and LOW into one batch
unit, or two only where they split into disjoint write sets by M6. This is the one unit. Ids 21 and 22
alone touch the review harness and its commit list, but id 21's list must hold id 22's commit, so that
half depends on the other's output, and no other split holds:
`tools/memory-tree/design_lib.py` and `build_records.py` are written by ids 5, 15, 16, 28 and 29, across
the other candidate halves. Each finding is named by report id and is its own scope item, including where
the report merged ids into one item. The minors land on nine units, so this unit repairs no one unit
and takes order 21, above every unit of the build.

| Item | Sev | Id | Lands on | S |
|---|---|---|---|---|
| M1 | MED | 2 | unit 38 S5, AC5; unit 41 S4 | S1 |
| M2 | MED | 4 | unit 43 Rollout; unit 34's pass | S2 |
| M3 | MED | 5 | unit 46 S8 | S3 |
| M3 | MED | 15 | unit 42 S1, S3; unit 46 §10 | S4 |
| M3 | MED | 24 | unit 46 S4, AC2 | S5 |
| M4 | MED | 6 | unit 46 §8 F1, AC9 | S6 |
| M4 | MED | 11 | unit 46 S11, AC9 | S7 |
| M5 | MED | 7 | unit 46 AC16 | S8 |
| M6 | MED | 8 | unit 46 Files touched | S9 |
| M7 | MED | 16 | unit 46 S10 | S10 |
| M8 | MED | 18 | unit 41 S3 | S11 |
| M9 | MED | 21 | unit 44 §7; unit 39 AC1 | S12 |
| M10 | MED | 28 | unit 42 S3, AC3 | S13 |
| M11 | MED | 29 | unit 43 S1, AC1 | S14 |
| L1 | LOW | 9 | unit 42 AC1 to AC3 | S15 |
| L2 | LOW | 12 | unit 45 §10, §8 F1 | S16 |
| L3 | LOW | 13 | unit 41 AC2 | S17 |
| L4 | LOW | 22 | unit 44 S1 | S18 |
| L5 | LOW | 23 | unit 46 S13, AC11 | S19 |
| L6 | LOW | 25 | unit 46 S22, AC18 | S20 |

That is 14 MEDIUM and 6 LOW findings by raw id. Ids 5, 15 and 24 share item M3, and ids 6 and 11 share
M4. Id 2 is the AC5 half of id 20, whose S22 and census half `TOOL-dIndexedDesign-51` lands. Ids 6 and 11
are the medium reading of id 26, whose reader `TOOL-dIndexedDesign-52` restates.

## 2. Scope (IN)

Every item builds at this unit's pass, on the code its unit built, unless it names an earlier act. An
earlier act is named in that unit's Edges block, where its builder reads it. A "ledger note" is §4's rule.

- **S1** — id 2. At unit 38's pass: unit 38 S5's "exactly one `fail 49 "` call site" and AC5's third
  clause are superseded, with unit 38's hands-off line to unit 41, "so AC5 finds them true". AC5's clause
  reads "`check_design_exit`'s body holds no `fail <n> "`, and the `--dispatch` refusal goes through the
  THIN site". Ledger note under unit 38 AC5, beside unit 41 S4's. Observed by AC1.
- **S2** — id 4. An act ahead, in unit 34's pass commit: unit 43's S1 to S3 land there, so `inventory`
  becomes typed and admits its repeated `Of` and `Verdict` lines in one commit. Unit 43's own pass at
  order 11 reads its AC1 to AC3 at that commit. Ledger note under unit 43 AC1. Observed by AC2.
- **S3** — id 5. An act ahead, at unit 46's pass: unit 46 S8 splits in two.
  `derive_next_record_number(root, slug, kind)` in `build_records.py` returns one more than the highest
  `-<kind>-<n>.md` number over tracked and on-disk files, and creates nothing. `derive_next_record_path`
  calls it before its exclusive create. Observed by AC3.
- **S4** — id 15. One home for the fork number. At unit 42's pass, unit 42 S1's count reads tracked and
  on-disk files, as unit 46 S8 will. At unit 46's pass, `design_lib.py --decompose` takes its number from
  S3's `derive_next_record_number`, and `design_lib.py` keeps no count of its own. The one home is
  `build_records.py`. Ledger note under unit 42 AC3. Observed by AC3.
- **S5** — id 24. Unit 46 AC2's grep widens to every typed kind, its leading dash guarded. With an
  untracked `-fork-1.md` present, `--decompose` names `-fork-2.md` and writes no file. Ledger note under
  unit 46 AC2. Observed by AC3.
- **S6** — id 6. Unit 46 §8 F1's ground, "AC9 holds it to the driver's verdicts", reads "unit 52's table
  and this unit's S7 hold it to the driver's verdicts". Ledger note under unit 46 AC9, naming the bare
  `spec-audit:` case. Observed by AC4.
- **S7** — id 11. The parity arm. The spec-audit fixtures of `tools/unattended/unattended.test.sh` run
  `gen_build_index.py --design-exit` beside the driver's `--preflight`, over seven fixtures: a dated
  README key, `spec-audit: yes`, a bare `spec-audit:`, no key, a dated default, an undated default and a
  conf cut short. In each pair both refuse, both declare, or both read absent. Observed by AC4.
- **S8** — id 7. Unit 46 AC16's literal grep for `"preference"` and `"goal"` is superseded by a
  behavioural reading, since unit 8's forks rule still spells both. A scratch per-kind table gaining a
  `Class` value admits a fork record using it, and one losing `goal` refuses a `goal` record (§8 F1). At
  unit 46's pass: ledger note under unit 46 AC16. Observed by AC5.
- **S9** — id 8. At unit 46's pass: its `--dispatch --writes` row declares `tools/memory-tree/tree_lib.py`
  for its S15, and `tools/memory-tree/check-memory-hygiene.test.sh`, the suite unit 13 §7 names for the
  grader, carries the arm for its AC13. Ledger note under unit 46 AC13. Observed by AC6.
- **S10** — id 16. An act ahead, at unit 46's pass: `check_path_shaped` and `CITE_TAIL` move from
  `tools/check-spec-tokens.py` into `design_lib.py`, beside `check_dir_shaped`. `check-spec-tokens.py`
  keeps `CITE_TAIL = load_design_lib().CITE_TAIL`, as it aliases `NOT_A_TOKEN`, and `:1568` calls
  `load_design_lib().check_path_shaped`. Unit 46 S10's `check_meet_path(tok, files)` calls
  `check_path_shaped(tok, files) or check_dir_shaped(tok)`.
  **Readers:** by name: the call in `extract_files_touched` at `tools/check-spec-tokens.py:584` and the
  call at `:1568` of the same file, and unit 46 S10's `check_meet_path`, READER NOT IN TREE because unit
  46's pass creates it at order 19, after this spec's base · by value: `check_bare_shaped` (`:1130`) and
  `check_path_shaped` (`:1117`), each reading `CITE_TAIL`. Observed by AC7.
- **S11** — id 18. An act ahead, in unit 3's pass commit: unit 41 S3's site is the `fail 55` site of
  `check_authorization`, composed as
  `fail 55 "$_c55 at the default-branch side of the pinned BASE could not be evaluated to the end, so $_k55 is unknown and is not read as absent - $_t55"`.
  For the conf, `_c55` is `the project conf`, `_k55` is `whether it declares SPEC_AUDIT_DEFAULT` and
  `_t55` today's tail, so the printed text is unchanged. For unit 3's refusal, `_c55` is
  `the policy file .governance/policy.toml`, `_k55` is `its review.design value` and `_t55` the `check`
  line. Each cause is armed by its own `_k55` text. Observed by AC8.
- **S12** — id 21. At this unit's pass, the last of the build to change the harness, every commit
  `git log` lists for `tools/workflows/tier2-review.js` since BASE, and the working render, is fed to
  `check-verifier-fanout.sh`. That list supersedes unit 39 AC1's, read at order 5. Ledger note under
  unit 39 AC1. Observed by AC9.
- **S13** — id 28. An act ahead, at unit 42's pass: the findings of one `--decompose` run are numbered
  consecutively from the build's next free number, in print order, and no file is created. Ledger note
  under unit 42 AC3. Observed by AC10.
- **S14** — id 29. An act ahead, in unit 34's pass commit with S2: a field the kind declares repeatable is
  always a list, one element per line, so a single line gives a list of one. A field not declared
  repeatable is always a string. Ledger note under unit 43 AC1. Observed by AC2.
- **S15** — id 9. At unit 42's pass: its AC1 to AC3 run `python design_lib.py --decompose-fixture <dir> --plant <case>`,
  then `python design_lib.py --decompose tFix` in that repository, the form unit 8 S10 defines. Ledger
  note under unit 42 AC1. Observed by AC10.
- **S16** — id 12. Unit 45 §10's "which source confirms" is corrected: at base `--dispatch` also refuses
  out of declared order (`tools/unattended/unattended.sh:13728`), on a producer neither CLOSED nor WONTDO
  (`:13804`) and on a held ask (`:13841`). Unit 45 §8 F1's ground reads "the sentence is stale at base, and
  the build's own units add further refusals". Ledger note under unit 45 AC1. Observed by AC11.
- **S17** — id 13. Unit 41 AC2's census sentence names its fixture: a scratch clone with one literal
  `fail 49 "` site staged inside `check_design_exit`, and `check-arms.py --emit-floors` run with the
  clone as its cwd. Ledger note under unit 41 AC2. Observed by AC12.
- **S18** — id 22. When the coverage stage dispatched, every return of `tier2-review.template.js` counts
  its agent: in `lensesRun` when it returned, in `lensesDead` when it died, and in `agents` always. The
  readers are `unattended-build.template.js:1760` and `:1773`, which read `lensesDead` after the
  `deferred-platform` check. Observed by AC13.
- **S19** — id 23. `WIRE-INTO-PROJECT.md:716` and `tools/roles/kit.toml:14-15` drop the count of
  harnesses, saying "the harnesses the workflow table names", as unit 46 S13 words the roles README. The
  wrapped "and all / # three ship" reads "and all ship" (§8 F2). The readers are the carriers
  `git grep -n -i "three harnesses"` prints outside `memory/` for this set, read 2026-10-28.
  **Readers:** by name: `WIRE-INTO-PROJECT.md:716` and `tools/roles/kit.toml:14-15` here, and
  `tools/roles/README.md:283` and `tools/roles/kit.toml:19`, which unit 46 S13 rewords · by value: NO VALUE READERS, because the count
  is prose and a comment: no `*.py`, `*.sh` or `*.js` file reads it, and the reworded sentences point at
  `tools/workflows/workflows.toml`, the table that owns the set. Observed by AC14.
- **S20** — id 25. An act ahead, at unit 46's pass: the three readers of `PROBE_TIMEOUT_SECONDS` in
  `gen_build_index.py`, `run_probe`'s call (`:3793`), the kill message (`:3796`) and the selftest arm
  (`:7704`), read `design_lib.PROBE_TIMEOUT_SECONDS`. Ledger note under unit 46 AC18. Observed by AC15.

## 3. Non-goals (OUT)

- Any HIGH of the audit: `TOOL-dIndexedDesign-47` to `-52`.
- Raising `REFUSAL_CEILINGS` or `MAX_LENSES`: owner turns.
- Rewriting a repaired spec's text. Each is answered in its ledger or, for an earlier act, in its Edges
  block.
- `tools/workflows/README.md:34` and `:337`, which count the review harnesses that take `workerType`, a
  different set from the one `workflows.toml` names.
- The report's left-shift gates and checklist entries, beyond S7's parity arm. No clause of this build
  names them.

### Edges

- **consumes-from** `TOOL-dIndexedDesign-3` — its unreadable `review.design` refusal, which S11 composes into the `fail 55` site in that unit's pass commit (id 18)
- **consumes-from** `TOOL-dIndexedDesign-34` — its pass commit, which carries unit 43's S1 to S3 and S14's list shape (ids 4 and 29)
- **consumes-from** `TOOL-dIndexedDesign-38` — S5 and AC5's third clause, which S1 supersedes at that unit's pass, and its hands-off line to unit 41 (id 2)
- **consumes-from** `TOOL-dIndexedDesign-39` — AC1's commit list, which S12 re-derives at this unit's pass (id 21)
- **consumes-from** `TOOL-dIndexedDesign-41` — S3's site, which S11 names, AC2's census sentence, whose fixture S17 states, and S4's ledger note, beside which S1's sits (ids 2, 13 and 18)
- **consumes-from** `TOOL-dIndexedDesign-42` — S1's count, S3's findings and AC1 to AC3's command form, which S4, S13 and S15 change at that unit's pass (ids 9, 15 and 28)
- **consumes-from** `TOOL-dIndexedDesign-43` — S1 to S3, which S2 lands in unit 34's pass, and S1's list shape, which S14 states (ids 4 and 29)
- **consumes-from** `TOOL-dIndexedDesign-44` — S1's counts, whose returned values S18 states, and its pass commit, which S12's list covers (ids 21 and 22)
- **consumes-from** `TOOL-dIndexedDesign-45` — §10 and §8 F1's ground, which S16 corrects (id 12)
- **consumes-from** `TOOL-dIndexedDesign-46` — S4, S8, S10, S13, S15, S22, §8 F1 and its criteria, which S3 to S10, S19 and S20 restate, several at that unit's pass (ids 5, 6, 7, 8, 15, 16, 23, 24 and 25)
- **consumes-from** `TOOL-dIndexedDesign-52` — the restated opt-in reader, which S7's parity arm runs beside the driver (ids 6 and 11)

## 4. Design

### Evidence

- `tools/memory-tree/deviation_join.py:212-226`, `read_record`, stores `fields[key] = value` as a string
  and refuses a repeated key as "is given twice". `tools/gate-legs.json` guards `build-index selftest` on
  `{prefix}/lib/`, `{prefix}/memory-tree/` and `{prefix}/check-spec-tokens.py`.
- `tools/check-spec-tokens.py:317` holds `CITE_TAIL`, `:584` calls `check_path_shaped` with
  `check_dir_shaped`, `:878` aliases `NOT_A_TOKEN` from `design_lib`, `:1104` defines `check_path_shaped`,
  `:1130` reads `CITE_TAIL` in `check_bare_shaped`, and `:1568` calls `check_path_shaped`.
- `tools/unattended/unattended.sh:4028` is the `fail 55` site, `:3980` `fail 52` and `:4034` `fail 54`,
  each its own message. `grep -c` of the composed run
  `at the default-branch side of the pinned BASE could not be evaluated to the end, so` prints 1 over
  `unattended.sh` and 1 over `unattended.test.sh` (`:9715`), read 2026-10-28.
- `tools/memory-tree/gen_build_index.py:3679` holds `PROBE_TIMEOUT_SECONDS = 30`, read at `:3793`, `:3796`
  and `:7704`, and `:310` imports `design_lib`.
- `tools/workflows/tier2-review.template.js:1313`, `:1338`, `:1671`, `:1704` and `:2036` return
  `lensesRun`, and `:2039` returns `agents`. `unattended-build.template.js:1760` and `:1773` read
  `lensesDead`.
- `git grep -n -i "three harnesses"` outside `memory/` prints `WIRE-INTO-PROJECT.md:716`,
  `tools/roles/README.md:283`, `tools/roles/kit.toml:14` and `:19`, and `tools/workflows/README.md:34`
  and `:337`. `kit.toml:14-15` wraps "and all / # three ship". Read 2026-10-28.

### Ledger notes

Where an item supersedes a criterion or a sentence of another unit, that unit's acceptance ledger
carries, at the pass named, a continuation line under the named criterion's answer, two spaces in. It
holds the label `TOOL-dIndexedDesign-53 S<n>` and, on that one physical line, a backticked token of the
item. A note is never its own `- AC` line.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `derive_next_record_number` | Python function, `build_records.py` | `py.function`, answered OK by `lexicon.py --suggest` |
| `_c55`, `_k55`, `_t55` | shell locals in `unattended.sh` | none: locals are not graded |

### Migration

No record is rewritten. `check_path_shaped` and `CITE_TAIL` move module and keep their behaviour.

### Rollout

S11 lands in unit 3's pass (order 16). S2 and S14 land in unit 34's pass (order 10). S4's first half,
S13 and S15 land in unit 42's pass (order 10). S1 is unit 38's pass (order 17). S3, S4's second half,
S8, S9, S10 and S20 land in unit 46's pass (order 19). The rest, and every observation, are this unit's
own pass at order 21, the last of the build.

### Files touched (estimate)

- `tools/unattended/unattended.sh`: S11, in unit 3's pass
- `tools/unattended/unattended.test.sh`: S7, and S11's arms in unit 3's pass
- `tools/memory-tree/build_records.py`: S2 and S14 in unit 34's pass, S3 in unit 46's
- `tools/memory-tree/design_lib.py`: S4 and S13 in unit 42's pass, S4 and S10 in unit 46's
- `tools/check-spec-tokens.py`: S10, in unit 46's pass
- `tools/memory-tree/gen_build_index.py`: S20, in unit 46's pass
- `tools/workflows/tier2-review.template.js`, its render `tools/workflows/tier2-review.js` by
  `check-protocol-parity.test.sh --render`, and `tools/workflows/tier2-review.test.sh`: S18
- `WIRE-INTO-PROJECT.md`, `tools/roles/kit.toml`: S19
- `memory/builds/dIndexedDesign/build/`: the ledger notes and the recorded probes

### Alternatives rejected

- **Two batches.** Lost to M6: the only write-disjoint candidate, ids 21 and 22, is not independent,
  because id 21's list must hold id 22's commit.
- **Route `--decompose` through `derive_next_record_path` (S4, S13).** Lost to its exclusive create: a
  reporting check would write an empty fork record on every run, and the allocator does not exist at
  unit 42's order 10.
- **A new `fail` site for unit 3's refusal (S11).** Lost to the ceiling: the census reaches 324.

## 5. Production-readiness checklist

- security — S7 holds the standalone opt-in reader to the driver's refusals; S3 never overwrites a record.
- perf / scale — S7 adds one generator run per fixture; S12 one hook run per harness commit.
- error / empty / loading states — S13 and S5 name distinct files without writing any; S14 fixes one
  shape at count one.
- observability — S18's counts match the shape line; S11 keeps both refusal texts readable.
- risks — thirteen acts land in other units' passes, before this unit's order. AC1 to AC15 read the commits and ledgers that show
  they did.
- testing — AC1 to AC15 by probe, fixture or ledger grep; the arms §7 declares.
- migration — §4 Migration.
- user docs — none under `help/`; S19's carriers are the deployer's guide and a kit descriptor.

## 6. Acceptance criteria

- **AC1** — When `sed -n '/^check_design_exit()/,/^}/p' tools/unattended/unattended.sh | grep -c 'fail [0-9]* "'`
  runs at unit 38's pass commit it prints 0, and `grep -n "TOOL-dIndexedDesign-53 S1"` over unit 38's
  acceptance ledger prints the note under AC5's answer.
  Red when: the body holds a site, or the note is missing or its own `- AC` line.
- **AC2** — When `git log --reverse --format=%H -S "repeatable" <base>..HEAD -- '*/build_records.py'`
  runs, its first line is unit 34's pass commit. In a worktree there, unit 20 AC7's
  `python tools/memory-tree/gen_build_index.py --inventory tFix` over its `--plant inventory` fixture exits
  0, and a `python -c` read of a record with one `Of` and one `Verdict` reads `bound`, `fields['Verdict']`
  a list of length 1 and `fields['Input']` a string.
  Red when: the repeatable set lands after unit 34's pass, or a one-line field is a string.
- **AC3** — When `grep -nE -e '-(fork|diff|overlap)-(\{|%)' tools/memory-tree/design_lib.py` runs, it prints
  nothing. When `--decompose` runs over a scratch build holding an untracked `-fork-1.md` and one
  unrecorded F-item, it names `-fork-2.md`, and `git status --porcelain` shows no new file.
  Red when: `design_lib.py` derives a number itself, or the check writes a record.
  fixture: a scratch repository under `%TEMP%/<short-name>`.
- **AC4** — When the S7 arm runs its seven fixtures, the driver and `--design-exit` agree on each. With
  the reader staged to read `spec-audit: yes` as absent, the pair disagrees and the arm reds. A
  `grep -n "TOOL-dIndexedDesign-53 S6"` over unit 46's ledger prints the note under AC9's answer.
  Red when: a pair disagrees unstaged, or the staged reader passes.
- **AC5** — When a scratch copy of the per-kind table gains the `Class` value `planted`, the fork join
  admits a fork record using it, and when a copy drops `goal`, it refuses a `goal` record. A
  `grep -n "TOOL-dIndexedDesign-53 S8"` over unit 46's ledger prints the note under AC16's answer.
  Red when: the join keeps its own copy of the set.
- **AC6** — When `git show --stat <p> -- tools/memory-tree/tree_lib.py` runs for unit 46's pass commit
  `<p>`, it lists the file, and `grep -n "TOOL-dIndexedDesign-46" memory/builds/dIndexedDesign/RUN.md`
  prints a dispatch row naming `tools/memory-tree/tree_lib.py`.
  Red when: the pass wrote the file without declaring it.
- **AC7** — When `grep -c "def check_path_shaped"` runs over `tools/check-spec-tokens.py` it prints 0, and
  over `tools/memory-tree/design_lib.py` it prints 1. Unit 46 AC8's `python -c` verdicts are unchanged.
  Red when: the rule exists twice, or a verdict moves.
- **AC8** — When `python <repo>/tools/memory-tree/check-arms.py --emit-floors` runs in a worktree at unit
  3's pass commit, `tools/unattended/unattended.sh` reads at or under 323. There,
  `grep -v '^[[:space:]]*#' tools/unattended/unattended.test.sh | grep -c "whether it declares SPEC_AUDIT_DEFAULT is unknown"`
  and the same count for `its review.design value is unknown` each print at least 1.
  Red when: the census grows, or a cause has no arm.
  figure: 323 is PINNED by `REFUSAL_CEILINGS` at `.memory-tree.conf:653`.
- **AC9** — When each blob of the commits `git log --format=%H <base>..HEAD -- tools/workflows/tier2-review.js`
  lists, and the working render, is passed to `bash tools/workflows/check-verifier-fanout.sh <file>`, every
  run exits 0, and the list holds unit 16's pass commit.
  Red when: a harness is denied, or the list is empty.
  figure: the list is DERIVED at this unit's pass.
- **AC10** — When `python design_lib.py --decompose-fixture <dir> --plant fork-unrecorded` writes a build
  holding one fork record, with F1 and F2 of one unit and F1 of a second left unrecorded, and
  `python design_lib.py --decompose tFix` runs in it, the findings name `-fork-2.md`, `-fork-3.md` and
  `-fork-4.md`, and no file is written. A `grep -n "TOOL-dIndexedDesign-53 S1[35]"` over unit 42's
  ledger prints the notes under AC3 and AC1.
  Red when: two findings name one number, or a record is created.
- **AC11** — When `grep -n "TOOL-dIndexedDesign-53 S16"` runs over unit 45's acceptance ledger, it prints
  the note under AC1's answer naming `:13728`, `:13804` and `:13841`.
  Red when: the note is missing or names fewer refusals.
- **AC12** — When `python <repo>/tools/memory-tree/check-arms.py --emit-floors` runs with a scratch clone
  as its cwd, one literal `fail 49 "` site staged inside `check_design_exit`, it prints one more than over
  the same clone unstaged. A `grep -n "TOOL-dIndexedDesign-53 S17"` over unit 41's ledger prints the note.
  Red when: the census does not move on the planted site.
  fixture: a scratch clone under `%TEMP%/<short-name>`.
- **AC13** — When a `node -e` stub run of `tier2-review.js` with `coverage: 'only'` has a coverage agent
  return one finding, it returns `lensesRun` 1, `lensesDead` 0 and an `agents` count holding that agent.
  Under `with`, a coverage agent returning null counts in `lensesDead`.
  Red when: `lensesRun` is 0 under `only`, or `agents` leaves the agent out.
- **AC14** — When `tr '\n' ' ' < <file> | grep -ciE 'three harnesses|all #? *three ship'` runs over
  `WIRE-INTO-PROJECT.md`, `tools/roles/README.md` and `tools/roles/kit.toml`, it prints 0 for each.
  Red when: a count survives, wrapped or not.
- **AC15** — When `grep -n "PROBE_TIMEOUT_SECONDS" tools/memory-tree/gen_build_index.py` runs, every line
  it prints spells `design_lib.PROBE_TIMEOUT_SECONDS` or is a `from design_lib import` line, and none
  assigns `PROBE_TIMEOUT_SECONDS = `.
  Red when: a reader resolves the name another way.

## 7. Gates

`harness arms (fail branches armed or pinned)` · `unattended kit gate` · `build-index selftest` · `tier2-review self-test` · `unattended-build self-test` · `verifier fan-out self-test` · `verifier fan-out` · `review-join self-test` · `workflow script syntax` · `review-protocol parity (kit vs dogfood)` · `policy fixtures` · `memory-hygiene self-test` · `spec tokens (a spec's own names resolve)` · `roles catalogue` · `memory hygiene` · `recall floor` · `recall floor arms`

New arm: tools/unattended/unattended.test.sh · covers AC4 · the driver and `--design-exit` over seven opt-in fixtures, staged by the reader reading `spec-audit: yes` as absent · none
New arm: tools/unattended/unattended.test.sh · covers AC8 · each `fail 55` cause by its own text, staged by deleting the `review.design` arm · none
New arm: tools/memory-tree/build_records.py · covers AC2 · a one-`Of`, one-`Verdict` inventory record, staged by listing a field only on a repeat · none
New arm: tools/memory-tree/design_lib.py · covers AC3 AC10 · three unrecorded F-items beside an untracked record, staged by numbering each finding from the folder alone · none
New arm: tools/workflows/tier2-review.test.sh · covers AC13 · the returned counts under `only` and `with`, staged by counting `LENSES` alone · none

## 8. Open questions

- **F1 — Unit 46 AC16 (id 7): move the forks rule beside the per-kind table, or restate the criterion
  behaviourally?** Options: (a) the forks rule, `design.forks` value to admitted classes, lives in
  `build_records.py`'s per-kind table and the fork join reads it there; (b) AC16 observes the closed-set
  read by a planted `Class` value and drops the literal grep. Both satisfy the restated criterion and
  leave no follow-up. (a) opens a question (b) does not: a policy rule unit 8 §4 owns would sit in the
  record factory's shared table, which every typed kind reads. RESOLVED (agent, 2026-10-28, delegated):
  (b), rung 3, the tie broken by fewer open questions. widens: none · relaxes: none
- **F2 — `WIRE-INTO-PROJECT.md` is the deployer's guide, a governance carrier (S19, id 23).** Options:
  (a) edit line 716 under the README's `may: PLAY-dClosedLoop-3` grant, since the count goes stale through
  the build's own carried clause `cl-dClosedLoop-0397`, whose `plan` harness unit 15 adds and unit 38 S18
  wires; (b) leave it and file an ask. (b) leaves the finding open, which the severity rule forbids.
  RESOLVED (agent, 2026-10-28, delegated): (a), rung 3 with veto 2 lifted by the grant. grants:
  PLAY-dClosedLoop-3 the harness count at `WIRE-INTO-PROJECT.md:716`. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-28 · initial draft, the minors batch of the round-1 spec audit of units 39 to 46: 14
  MEDIUM and 6 LOW findings by raw id, each its own scope item.

## 10. Reuse audit

Each item extends the seam its finding names. S3 and S4 extend unit 46 S8's allocator in
`build_records.py` with a pure derivation beside it. S10 moves `check_path_shaped` to the module both
joins already load. S11 composes into the existing `fail 55` site. S7 extends the driver's own spec-audit
fixtures in `unattended.test.sh`. S12 reuses `check-verifier-fanout.sh` with file arguments. The probe
`python tools/codebase-map/reuse_lookup.py "evaluate a shell conf blob to its end and refuse when the read is cut short"`
ranked `read`, `read_text`, `load_conf` and `parse_conf`, none a reader that evaluates a conf. The probe
`python tools/codebase-map/reuse_lookup.py "compose several refusal messages into one existing fail site"`
ranked `fail`, `refusal`, `Refusal`, `DesignRefusal` and `read_id_list_refusals`, none a composer. No
item builds a seam that exists.

Recall terms used: `python tools/memory-recall/query.py "how were minor spec audit findings batched into one unit" --terms "minors batch MEDIUM LOW promoted one unit disjoint write sets ledger note spec audit round"`
