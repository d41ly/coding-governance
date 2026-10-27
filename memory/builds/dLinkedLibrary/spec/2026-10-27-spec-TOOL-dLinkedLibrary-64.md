# TOOL-dLinkedLibrary-64 — the minors of the spec audit of units 37 to 53: 23 findings closed where the built code and records hold them

**Status:** OPEN · rev-4 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 29 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-88 TOOL-dLinkedLibrary-89 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91 TOOL-dLinkedLibrary-92 TOOL-dLinkedLibrary-93 TOOL-dLinkedLibrary-94 TOOL-dLinkedLibrary-95 TOOL-dLinkedLibrary-96 TOOL-dLinkedLibrary-97 TOOL-dLinkedLibrary-98 TOOL-dLinkedLibrary-99 TOOL-dLinkedLibrary-100 TOOL-dLinkedLibrary-101 TOOL-dLinkedLibrary-102 |
| [2026-10-27-build-TOOL-dLinkedLibrary-54-promoted-fix-return.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-54-promoted-fix-return.md) | research | TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-20 |
| [2026-10-27-build-TOOL-dLinkedLibrary-64-deviation-641.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-64-deviation-641.md) | deviation | — |
| [2026-10-27-prompt-TOOL-dLinkedLibrary-54-promoted-fix-brief.md](../prompts/2026-10-27-prompt-TOOL-dLinkedLibrary-54-promoted-fix-brief.md) | research | TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-20 |
| [2026-10-27-review-TOOL-dLinkedLibrary-54-spec-audit.md](../reviews/2026-10-27-review-TOOL-dLinkedLibrary-54-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 37 to 53
(`memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-37-spec-audit.md`) confirmed
14 MEDIUM and 9 LOW findings. BUILD-METHOD M4 promotes them into one batch unit, and this is it; each
finding is its own scope item below, by report id:

- MEDIUM: 5 (item M1), 6 and 20 (item M2), 7 (M3), 8 (M4), 18 (M5), 19 and 25 (M6), 28 (M7), 30 (M8),
  31 (M9), 32 (M10), 33 (M11), 34 (M12).
- LOW: 9 (L1), 10 (L2), 11 (L3), 13 (L4), 14 (L5), 15 (L6), 21 (L7), 22 (L8), 23 (L9).

The findings land on seventeen units, so this unit repairs none in particular and builds after every unit
of the build (order 29). Where an item corrects what a unit's criterion asserts, that unit's acceptance
ledger answers the criterion AMENDED, naming this unit and the item. One unit and not two: items S6 and
S17 both write `tools/memory-tree/gotchas.py`, items S10, S11 and S20 all write
`tools/memory-tree/kit.toml`, and S7, S8 and S14 all write `tools/codebase-map/dossier_move.py`, so no
split by M6's clauses leaves two disjoint write sets of useful size.

## 2. Scope (IN)

- **S1** — id 5, M1. `annotations.py` holds one fixture harness, `--fixture --plant <case>` under
  `TOOL-dLinkedLibrary-4` §4's contract, and `TOOL-dLinkedLibrary-48`'s `adopter-memory-tree-only` case
  and its variants are cases of it; where unit 48's pass hosted them in `--selftest`, the plant dispatches
  to the same case function, and no second parser of `--plant` exists. Observed by AC1.
- **S2** — id 6, M2. The unanchored-proposal warning lives on `accept`: `reuse_entries.py accept
  <proposal>`, when no tracked line carries the proposal's `gov:feature` anchor, prints `anchor not in the
  tree — accepting it reds the annotations leg until the line is written` and exits 2 unless
  `--anchor-absent-ok` is given. One helper, `derive_unanchored(proposal, root)`, answers it, and any
  listing `TOOL-dLinkedLibrary-39`'s pass built reads the same helper. Observed by AC2.
- **S3** — id 20, M2. `TOOL-dLinkedLibrary-39` AC4's observation runs through `reuse_entries.py`'s own
  `--fixture --plant accept-unanchored`, not through a `proposed` verb no unit builds; unit 39's ledger
  answers AC4 AMENDED, naming this unit. Observed by AC2.
- **S4** — id 7, M3. `TOOL-dLinkedLibrary-53`'s AC1, AC3 and AC8, which read files
  `TOOL-dLinkedLibrary-52` writes in the same step, are re-observed at this pass's tip, after both, and
  each re-observation is recorded in unit 53's acceptance ledger beside its pass answer. Observed by AC3.
- **S5** — id 8, M4. At this pass's tip the `marker` row of `tools/playbook/namespaces.toml` holds no
  `legacy` member and `tools/memory-tree/marker-words.toml` holds the `legacy` row; unit 23's ledger
  answers AC8's namespace half AMENDED, naming `TOOL-dLinkedLibrary-40` and this unit; and
  `memory/gotchas/amendment-leaves-its-other-half-standing.md` records this instance, a repair landed as a
  ledger answer while the repaired spec kept its other half. Observed by AC4.
- **S6** — id 18, M5. `gotchas.py --observe` resolves a leading `bash` through the memory-tree kit's
  `resolve_bash` (`tools/memory-tree/corpus_ids.py:390`) and a leading `python3` or `python` to
  `sys.executable`, as `tools/run-gates/regen.py:273-279` does, before it runs either observed argv.
  Observed by AC5.
- **S7** — id 19, M6. A re-filed proposal cannot share a path with the record it replaces: any re-file is
  made through `propose --unit TOOL-dLinkedLibrary-64`, a unit id no earlier proposal carries; and
  `dossier_move.py apply`'s re-run (`TOOL-dLinkedLibrary-52` S39) keys a seam on the part name read from
  the record body, never on the file name. Observed by AC6.
- **S8** — id 25, M6. The live count: at this pass's tip every part name a dossier's `seam:` lines give,
  `<feature>.<n>`, has exactly one proposal record with no `- **Disposition:**` line, or an accepted part;
  no rejected record shares a path with a live one; a seam with neither is re-filed by S7's rule.
  Observed by AC6.
- **S9** — id 28, M7. In the `ci-job` census (`TOOL-dLinkedLibrary-51` S5), a GitHub job with no
  `permissions:` key at workflow or job level reads `refused: no permissions block — default token grant
  unknown`; `secrets['<name>']` and `secrets: inherit` count as secret references; unit 51's plain
  test-job plant gains `permissions: contents: read`. Observed by AC7.
- **S10** — id 30, M8. The `adopt program selftest` declaration in `tools/memory-tree/kit.toml`
  (`TOOL-dLinkedLibrary-47` S1) guards `{kit}/`, `{prefix}/playbook/` and `{prefix}/policy/`, every kit
  directory its plants execute, and the rendered row in `tools/gate-legs.json` follows. Observed by AC8.
- **S11** — id 31, M9. The `code record selftest` declaration (`TOOL-dLinkedLibrary-46` S2) guards `{kit}/`
  and `{prefix}/policy/`, the kit `code_enrich.py` and the ctags pack read through `resolve`
  (`tools/policy/policy.py:752`). Observed by AC8.
- **S12** — id 32, M10. govkit's `find_block` (`TOOL-dLinkedLibrary-45` S1) returns `None` only when no
  line begins with either mark, the factory's MALFORMED prefix test of `TOOL-dLinkedLibrary-18` S1, so a
  text whose only marker lines are malformed reaches `find_pair` and raises `Refusal`. Observed by AC9.
- **S13** — id 33, M11. `splice_region` (`TOOL-dLinkedLibrary-52` S52) refuses any body line that begins
  with either mark, the same prefix test, raising `RegionError` naming the line, in the canonical
  `tools/lib/region.py` and every `region_py` copy. Observed by AC10.
- **S14** — id 34, M12. `dossier_move.py apply` (`TOOL-dLinkedLibrary-50` S1) checks `--build` against
  `SLUG_RE` (`tools/memory-tree/backlog.py:129`) and `--unit` against the id grammar of `GRANT_ID_RE`
  (:453) before any path join, exiting 2 naming the value and writing nothing. Observed by AC11.
- **S15** — id 9, L1. `TOOL-dLinkedLibrary-52` AC16's population is completed at this pass: for each leg
  of 52's S33 to S36, `tools/run-gates/ceiling-evidence.txt` and the claiming dossier carry its row, and
  unit 52's ledger answers AC16 AMENDED with the five-file reading. Observed by AC12.
- **S16** — id 10, L2. `region.py --census` names each of its arms by role in its output and source,
  `constant`, `marker test`, `regex opener` and `behavioural`, never by ordinal. Observed by AC13.
- **S17** — id 11, L3. `--observe` spells a clean run past its bound `unobservable: clean past <n>s` and a
  clean non-zero exit `unobservable: clean exit <n>`, one string per case of
  `TOOL-dLinkedLibrary-49`'s table, with a `--selftest` case `observe-clean-hang`. Observed by AC14.
- **S18** — id 13, L4. Unit 43's acceptance ledger records `region.py --census`'s raw output at this pass
  beside its AC1 answer, and names `tools/drift-audit/drift_report.py:1821`'s constant among the
  constants of table rows. Observed by AC15.
- **S19** — id 14, L5. The comment block above the deleted `[[files]]` rows of
  `tools/codebase-map/kit.toml` (:44-57), which names `rank_harness.py`, is deleted with them. Observed by
  AC16.
  **Readers:** by name: `tools/codebase-map/kit.toml`, the one tracked file outside this repository's build records
  that spells the block's text (a git grep of its sentences prints :51, :53 and :54 alone); the files it
  names keep the readers TOOL-dLinkedLibrary-3 S1 and TOOL-dLinkedLibrary-52 S41 answer for.
  by value: NO VALUE READERS because the block is a TOML comment, which the TOML reader discards, so no program reads it.
- **S20** — id 15, L6. Both declarations of S10 and S11 are spelled in descriptor tokens, `argv =
  ["python3", "{kit}/<module>", "--selftest"]` and guards led by `{kit}/`, as `tools/memory-tree/kit.toml:291`
  spells `gotchas selftest`; `{prefix}/memory-tree/` is never written in that descriptor. Observed by AC8.
- **S21** — id 21, L7. `help/annotations.md`'s markers section states the adopter envelope, a reader not
  installed is announced, a row owned outside the repository is not graded "appears nowhere", and an owned
  row's missing reader is red; `tools/memory-tree/README.md`'s registry paragraph says the same. Observed
  by AC17.
- **S22** — id 22, L8. `memory/map/generated/CARDS.md` is re-rendered with `MAP.md` and
  `inventories.json` by `gen_map.py` (:143-145), which renders all three. Observed by AC18.
- **S23** — id 23, L9. `HOUSE_INDEX_DIRS` and `HOUSE_INDEX_KINDS` leave `.codebase-map.conf` and
  `tools/codebase-map/.codebase-map.conf.example` where `TOOL-dLinkedLibrary-52` S44 moved them to
  catalogue keys; unit 52's ledger answers AC20 AMENDED. Observed by AC19.

## 3. Non-goals (OUT)

- The HIGH findings of the same audit: units 54 to 63, one per id.
- Re-opening any unit's design: each item corrects the built code or records where the finding lands.
- A gate per left-shift the report proposes: S5 records the one class the report names and every other
  item lands on an existing arm or plant.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-48` — `adopter-memory-tree-only` and its README sentence, which S1 and S21 re-host and complete (ids 5, 21)
- **consumes-from** `TOOL-dLinkedLibrary-4` — `--fixture --plant <case>` and `help/annotations.md`, the harness S1 keeps single and the page S21 completes (ids 5, 21)
- **consumes-from** `TOOL-dLinkedLibrary-39` — AC4 and any listing its pass built, which S2 and S3 re-point onto `accept` (ids 6, 20)
- **consumes-from** `TOOL-dLinkedLibrary-1` — `accept` in `reuse_entries.py`, which S2 guards (id 6)
- **consumes-from** `TOOL-dLinkedLibrary-53` — AC1, AC3 and AC8, which S4 re-observes after unit 52 (id 7)
- **consumes-from** `TOOL-dLinkedLibrary-52` — S39's re-run, S33 to S36's legs, S41's deletion, S44's key move and S52's `splice_region`, which S7, S13, S15, S19 and S23 complete (ids 7, 9, 14, 19, 23, 33)
- **consumes-from** `TOOL-dLinkedLibrary-23` — AC8's namespace half, which S5 answers AMENDED (id 8)
- **consumes-from** `TOOL-dLinkedLibrary-40` — the `legacy` row of `marker-words.toml`, which S5 observes (id 8)
- **consumes-from** `TOOL-dLinkedLibrary-49` — `--observe`'s runs and verdict spellings, which S6 and S17 complete (ids 18, 11)
- **consumes-from** `TOOL-dLinkedLibrary-38` — the re-filed proposals of its S4, whose names S7 and S8 keep apart and count (ids 19, 25)
- **consumes-from** `TOOL-dLinkedLibrary-51` — S5's grant and secret rules and the plain test-job plant, which S9 completes (id 28)
- **consumes-from** `TOOL-dLinkedLibrary-47` — the `adopt program selftest` declaration, whose guard S10 widens and S20 re-spells (ids 30, 15)
- **consumes-from** `TOOL-dLinkedLibrary-46` — the `code record selftest` declaration and its re-rendered map, which S11, S20 and S22 complete (ids 31, 15, 22)
- **consumes-from** `TOOL-dLinkedLibrary-45` — `find_block` and the census's behavioural arm, which S12 and S16 correct (ids 32, 10)
- **consumes-from** `TOOL-dLinkedLibrary-18` — `region_py` and the factory's MALFORMED prefix test, which S12 and S13 apply (ids 32, 33)
- **consumes-from** `TOOL-dLinkedLibrary-50` — `apply`'s `--build` and `--unit`, which S14 validates (id 34)
- **consumes-from** `TOOL-dLinkedLibrary-43` — `region.py --census` and the §4 table its ledger answers against, which S16 and S18 complete (ids 10, 13)
- **consumes-from** `TOOL-dLinkedLibrary-67` — `resolve_observed_argv`, which S6 and AC5 re-observe rather than land a second resolution (id 2 of the spec audit of units 54 to 64)
- **hands-off** `TOOL-dLinkedLibrary-74` — AC12, S13's `splice_region`, S14's validation and S19's deletion, which unit 74 completes (ids 5, 29, 44, 17 of the spec audit of units 54 to 64)
- **hands-off** `TOOL-dLinkedLibrary-80` — S6's `--observe` resolution, which unit 80 holds to unit 67's one resolver (id 3 of the spec audit of units 65 to 74)
- **hands-off** `TOOL-dLinkedLibrary-86` — S6's `--observe` resolution, which this pass re-observes through unit 67's `resolve_observed_argv` and lands no `resolve_bash` call of its own, writing an amendment line that unit 86's S19 reads (id 4 of the spec audit of units 75 to 80)

## 4. Design

### Evidence

- S1: `TOOL-dLinkedLibrary-48` (order 4) drives its criteria through `annotations.py --fixture --plant`;
  `TOOL-dLinkedLibrary-12` gives the module `check [--only]` and `--selftest`; `TOOL-dLinkedLibrary-4`
  (order 12) mints `--fixture` and `--plant` in its minted-names table.
- S2, S3: `TOOL-dLinkedLibrary-1`'s verbs are `propose`, `accept`, `reject`, `owed` and `check` (its
  inventory); `proposed` is a state.
- S5: `TOOL-dLinkedLibrary-23` S9 and AC8 still write and grep `marker.legacy` in
  `tools/playbook/namespaces.toml`; `TOOL-dLinkedLibrary-40` S2 restores that row at order 26.
- S6: `tools/memory-tree/corpus_ids.py:390-398`, the System32 WSL launcher and the WindowsApps alias.
- S10, S11: `tools/run-gates/leg_factory.py` (TOOL-dWitnessedBar-11 S2, built before this build run),
  whose `--check` exits 1 when `tools/gate-legs.json` differs from what `--write` renders from every
  declaration.
- S12, S13: `TOOL-dLinkedLibrary-18` S1, "a line that begins with the marker and is not one of those is
  MALFORMED and refused".
- S19: `grep -n "rank_harness\|replay-phrases" tools/codebase-map/kit.toml` prints :48, :53 and :57 at
  base; :53 is a comment.
- S20: `tools/memory-tree/kit.toml:291` reads `argv = ["python3", "{kit}/gotchas.py", "--selftest"]` with
  `guard = ["{kit}/"]`, and the descriptor spells no `{prefix}/memory-tree/`.
- S22: `tools/codebase-map/gen_map.py:143-145` renders `inventories.json`, `MAP.md` and `CARDS.md`.

### Files touched (estimate)

- `tools/memory-tree/annotations.py`: S1
- `tools/memory-tree/reuse_entries.py`: S2, S3, S7's re-file
- `tools/memory-tree/gotchas.py`: S6, S17
- `tools/codebase-map/dossier_move.py`, `tools/codebase-map/selftest.py`: S7, S8, S14 and their plants
- `tools/memory-tree/adopt_program.py`: S9
- `tools/memory-tree/kit.toml`, `tools/gate-legs.json`: S10, S11, S20
- `tools/govkit/govkit.py`: S12
- `tools/lib/region.py`, `tools/memory-tree/marker-contract.test.sh`: S13, S16
- `tools/codebase-map/kit.toml`: S19
- `help/annotations.md`, `tools/memory-tree/README.md`: S21
- `memory/map/generated/MAP.md`, `memory/map/generated/inventories.json`, `memory/map/generated/CARDS.md`: S22
- `.codebase-map.conf`, `tools/codebase-map/.codebase-map.conf.example`: S23
- `memory/gotchas/amendment-leaves-its-other-half-standing.md`: S5
- the acceptance ledgers of units 23, 39, 43, 52 and 53 under `memory/builds/dLinkedLibrary/build/`: S3, S4,
  S5, S15, S18, S23
- the kit version constants of memory-tree, codebase-map and govkit, with their markers

### Alternatives rejected

- **One unit per finding.** M4 forbids it.
- **Folding each item into its unit's spec.** The owner's 2026-10-05 ruling promotes every minor and folds
  none.

## 5. Production-readiness checklist

- security — S9 denies a job whose token grant is unknown; S14 validates two CLI values before a path
  join; S12 and S13 refuse a write that would leave an unreadable pair.
- perf / scale — no item changes complexity.
- error / empty / loading states — S2, S14 and S12 each exit or raise naming the value or line.
- observability — each refusal names its file, line, row or value.
- risks — S8 re-files a lost seam under this unit's id; the owner's queue gains it once.
- testing — AC1 to AC19 by fixture, selftest case, plant and probe.
- migration — S8's re-files and S23's key removal, each in its own commit.
- user docs — `help/annotations.md`, S21.

## 6. Acceptance criteria

- **AC1** — When `python annotations.py --fixture --plant adopter-memory-tree-only` runs, it exits 0,
  and `grep -c 'add_argument("--plant"'` over the same `annotations.py` prints 1.
  Red when: the plant is unknown, or two harnesses parse `--plant`.
- **AC2** — When `python reuse_entries.py --fixture --plant accept-unanchored` runs
  `accept` over a proposal whose anchor no line carries, it exits 2 printing `anchor not in the tree`; with
  `--anchor-absent-ok` it accepts; and unit 39's ledger answers AC4 AMENDED naming this unit.
  Red when: an unanchored proposal is accepted with no warning.
- **AC3** — When `grep -n "AC1\|AC3\|AC8" <unit 53's acceptance ledger>` runs, each criterion carries a
  re-observation dated at this pass.
  Red when: a criterion reading a file unit 52 writes is certified only on a tree without 52.
- **AC4** — When `grep -n 'marker.legacy\|"legacy"'` runs over the playbook kit's `namespaces.toml` (S5
  names both paths), it prints nothing; `grep -n 'word = "legacy"'` over the memory-tree kit's
  `marker-words.toml` prints the row; and the gotcha record names this instance.
  Red when: the member and the row coexist, or unit 23's ledger certifies the namespace member.
- **AC5** — When `python tools/memory-tree/gotchas.py --selftest` runs its `observe-bash-led` case, a stub
  leg with argv `["bash", "<stub>.sh"]` records `refused`, and the case prints `ok`.
  Red when: a bare `bash` reaches the Windows loader's launcher and the class reads `unobservable`.
- **AC6** — When `python dossier_move.py --fixture --plant refile` runs, a
  same-date `alpha-1` proposal under unit 19's id and a re-file of `alpha.1` both exist as two paths, the
  old carrying the rejected disposition; and at this pass's tip each seam's part name has exactly one live
  proposal or an accepted part.
  Red when: a rejected record shares a path with a live one, or a seam has no live proposal.
  figure: DERIVED at the pass from the dossiers' `seam:` lines.
- **AC7** — When `python adopt_program.py --fixture --plant ci-census` runs, a job with
  no `permissions:` key running `gh pr merge` reads `refused: no permissions block`, a job reading
  `secrets['NPM_TOKEN']` reads `refused`, and the plain test job, now `contents: read`, reads `importable`.
  Red when: an absent grant or a bracketed secret reads `importable`.
- **AC8** — When `grep -n "adopt program selftest\|code record selftest" -A 4 tools/memory-tree/kit.toml`
  runs, each declaration's argv opens `"python3", "{kit}/` and its guard names `{prefix}/policy/`, the
  first also `{prefix}/playbook/`; and `python leg_factory.py --check` run in `tools/run-gates` exits 0.
  Red when: a guard omits a kit the selftest executes, or a declaration is spelled in rendered tokens.
- **AC9** — When `python -c` imports govkit and calls `find_block` over a text whose only open and close
  carry a trailing tab, it raises `Refusal` naming the factory's rule, and `write_block` writes nothing.
  Red when: a malformed-only text returns `None` and a second pair is appended.
- **AC10** — When `splice_region` is called with a body line `<open>\t` or `<open>x`, it raises
  `RegionError` naming the line, in the lib canonical `region.py` and each copy the parity discovery finds.
  Red when: a body line the factory reads as MALFORMED is spliced in.
- **AC11** — When `python dossier_move.py --fixture --plant bad-values` runs `apply
  --build .. --unit TOOL-x-1` and `apply --build dLinkedLibrary --unit TOOL-x-1/../y` in its scratch map,
  each exits 2 naming the value and writes nothing.
  Red when: a value holding `..` or a separator reaches a path join.
- **AC12** — When `grep -c "<leg>" tools/run-gates/ceiling-evidence.txt memory/map/features/memory-tree-hygiene.md`
  runs for each leg of unit 52's S33 to S36, it prints 1 or more per file, and 52's ledger answers AC16
  AMENDED.
  Red when: a meta row of S33 is observed by no criterion.
- **AC13** — When `python region.py --census` runs, each output line names its arm by role, and
  `grep -c "third arm"` over the same `region.py` prints 0.
  Red when: an arm is named by an ordinal.
- **AC14** — When `python tools/memory-tree/gotchas.py --selftest` runs its `observe-clean-hang` case, a
  clean run past a 2-second ceiling records `unobservable: clean past 2s`.
  Red when: the clean-run timeout reads `clean exit`.
- **AC15** — When `grep -n "drift_report.py:1821" <unit 43's acceptance ledger>` runs, it prints the
  census reconciliation line.
  Red when: the ledger's population cannot be reconciled with the census output line for line.
- **AC16** — When `grep -c "rank_harness\|replay-phrases" tools/codebase-map/kit.toml` runs at this pass's
  tip, it prints 0.
  Red when: a comment naming a deleted file survives.
- **AC17** — When `grep -n "not installed"` runs over the help page `annotations.md` and
  `tools/memory-tree/README.md`, each file prints the envelope's sentences.
  Red when: the help page states only gov's own tree.
- **AC18** — When `python tools/codebase-map/gen_map.py` runs at this pass's tip, `git status --porcelain
  memory/map/generated/` prints nothing.
  Red when: a rendered artifact of the map is stale, `CARDS.md` included.
- **AC19** — When `grep -c "HOUSE_INDEX_" .codebase-map.conf tools/codebase-map/.codebase-map.conf.example`
  runs, it prints 0 for each, and 52's ledger answers AC20 AMENDED.
  Red when: a moved key keeps its old home.

## 7. Gates

`policy fixtures` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `every held leg is budgeted, every budget row resolves` · `foreign-prefix parity (every self-test at three prefixes)` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor` · `recall floor arms` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `codebase-map coverage + freshness` · `gotchas selftest` · `marker contracts` · `python resolver (behaviour + inline parity + idiom ban)` · `kit version markers` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/reuse_entries.py · covers AC2 · the `accept-unanchored` plant, the failing case staged by an `accept` that skips `derive_unanchored` · none
New arm: tools/memory-tree/gotchas.py · covers AC5 AC14 · the `observe-bash-led` and `observe-clean-hang` cases, the failing case staged by a bare `bash` and by the single clean-run spelling · none
New arm: tools/codebase-map/selftest.py · covers AC6 AC11 · the `refile` and `bad-values` plants of `dossier_move.py --fixture`, the failing case staged by a file-name key and an unvalidated join · none
New arm: tools/memory-tree/adopt_program.py · covers AC7 · the no-permissions and bracketed-secret jobs of the `ci-census` plant, the failing case staged by unit 51's rev-1 grant rule · none
New arm: tools/memory-tree/marker-contract.test.sh · covers AC10 · the `<open>\t` and `<open>x` body cases, the failing case staged by an exact-match body test · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of a repaired unit's clause. (b) splits clauses the
  repaired units carry whole; veto 1 discards it. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3,
  the precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none
- **F2 — Where does the unanchored-proposal warning live?** Options: (a) on `accept`, which refuses
  without `--anchor-absent-ok`; (b) a new `proposed` listing verb; (c) `propose`'s own output. (b) mints a
  verb no criterion of unit 1 names, beside an owner turn that already passes through `accept`; (c) is
  read once, before the anchor could be written. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3,
  the most feature-rich survivor. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 37 to 53, 14 MEDIUM and 9 LOW
  findings batched in one unit.
- rev-2 · 2026-10-27 · §3 · the Edges block gains the bullets mirroring TOOL-dLinkedLibrary-67, TOOL-dLinkedLibrary-74, promoted from the spec audit of units 54 to 64; nothing else moved.
- rev-3 · 2026-10-27 · §3 · the Edges block gains the bullets mirroring TOOL-dLinkedLibrary-80, promoted from the spec
  audit of units 65 to 74; nothing else moved.
- rev-4 · 2026-10-27 · §3 · the Edges block gains the bullets mirroring TOOL-dLinkedLibrary-86, promoted from the spec
  audit of units 75 to 80; nothing else moved.

## 10. Reuse audit

Every item extends the seam its finding names: unit 4's fixture harness, unit 1's `accept`,
`resolve_bash` (`tools/memory-tree/corpus_ids.py:390`), unit 51's census, the leg factory's declarations,
the factory's MALFORMED prefix test, `SLUG_RE` and `GRANT_ID_RE` (`tools/memory-tree/backlog.py:129`,
:453), `gen_map.py`'s render set and the existing gotcha record; no item mints a second implementation of
any. `python tools/codebase-map/reuse_lookup.py "resolve a marker word reader through the install
receipt"` ranked `read`, `read_text`, `resolve` and `resolve_kit_dir`, none an owner test or a proposal
guard, so no existing seam fits beyond those the items name.

Recall terms used: `python tools/memory-recall/query.py "how does a promoted high finding repair a spec-audited unit at the next order step" --terms "spec-audit promoted high finding repairs order inline parity block tree-kill witness before-image"`
