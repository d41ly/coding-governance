# TOOL-dCalibratedLens-48 — the round-3 spec audit's 25 minors batched: each correction carried by the sibling it lands on

**Status:** DEFERRED · rev-1 · 2026-11-03 · node a · Tier-2 · base 8bec4cef · streams tooling · order 21 · advances TOOL-dCalibratedLens-18

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-03-build-TOOL-dCalibratedLens-1-agent-ledger.md](../build/2026-11-03-build-TOOL-dCalibratedLens-1-agent-ledger.md) | journal | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-12 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 TOOL-dCalibratedLens-19 TOOL-dCalibratedLens-20 TOOL-dCalibratedLens-21 TOOL-dCalibratedLens-22 TOOL-dCalibratedLens-23 TOOL-dCalibratedLens-24 TOOL-dCalibratedLens-25 TOOL-dCalibratedLens-26 TOOL-dCalibratedLens-27 TOOL-dCalibratedLens-28 TOOL-dCalibratedLens-29 TOOL-dCalibratedLens-30 TOOL-dCalibratedLens-31 TOOL-dCalibratedLens-32 TOOL-dCalibratedLens-33 TOOL-dCalibratedLens-34 TOOL-dCalibratedLens-35 TOOL-dCalibratedLens-36 TOOL-dCalibratedLens-37 TOOL-dCalibratedLens-38 TOOL-dCalibratedLens-39 TOOL-dCalibratedLens-40 TOOL-dCalibratedLens-41 TOOL-dCalibratedLens-42 TOOL-dCalibratedLens-43 TOOL-dCalibratedLens-44 TOOL-dCalibratedLens-45 TOOL-dCalibratedLens-46 TOOL-dCalibratedLens-47 |
| [2026-11-03-build-TOOL-dCalibratedLens-48-deviation-481.md](../build/2026-11-03-build-TOOL-dCalibratedLens-48-deviation-481.md) | deviation | — |
| [2026-11-03-prompt-TOOL-dCalibratedLens-1-ancestors-crosscheck.md](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-1-ancestors-crosscheck.md) | research | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-19 TOOL-dCalibratedLens-20 TOOL-dCalibratedLens-28 TOOL-dCalibratedLens-32 TOOL-dCalibratedLens-33 TOOL-dCalibratedLens-34 TOOL-dCalibratedLens-35 TOOL-dCalibratedLens-42 |
| [2026-11-03-prompt-TOOL-dCalibratedLens-42-promoted-fix-brief.md](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-42-promoted-fix-brief.md) | research | TOOL-dCalibratedLens-42 TOOL-dCalibratedLens-43 TOOL-dCalibratedLens-44 TOOL-dCalibratedLens-45 TOOL-dCalibratedLens-46 TOOL-dCalibratedLens-47 |

<!-- /gen:spec-records -->

## 1. Goal

The round-3 spec audit of units 31 to 41,
`reviews/2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit.md`, exited CONVERGED with 31 confirmed
findings; `TOOL-dCalibratedLens-42` to `-47` take its six HIGH. This unit is BUILD-METHOD M4's batch
of its 16 MEDIUM and 9 LOW by raw id, one scope item per id, in report order. They land on units 3,
5, 6, 8, 10, 21, 23, 29, 31 to 41, 46 and 47, so the batch repairs no unit in particular and takes
the order above every unit of the build, 21. They do not split into two disjoint write sets: every
correction is text in the sibling it lands on, and the siblings that build them meet in
`tools/loop/loop_review.py`, `tools/hooks/format-guard.test.sh` and the guard declarations, so one
unit carries them.

Every id: M1 2; M2 3; M3 4, 29; M4 5; M5 6; M6 8; M7 13; M8 14; M9 19; M10 15; M11 20; M12 24; M13
28; M14 31; M15 32; L1 7, 16, 26; L2 9; L3 10; L4 17; L5 18; L6 21; L7 33.

Each correction was made at the audit's disposal in the text of the unbuilt sibling it lands on: a
rev bump of that spec with a §9 line naming this unit and the review record by its stem, the S-item
or criterion rewritten in place for units 19 to 41, a bullet `- **r3 id <n> · …**` in a §4
"Amendments (round-3 spec audit)" section for units 1 to 17, and the item written into the rev-1 text
of units 46 and 47, which build the guard rows. Each sibling then builds the corrected design and
observes it through its own criterion. This unit builds no file.

## 2. Scope (IN)

- **S1** — id 2, M1, landing on units 10 (r3 id 2), 23 and 36. At unit 10's order its AC6 reads the
  seed `owed`, naming the paths unit 5 moved, and red on `owed` holds only at the close after the main
  loop's replay. NOT OBSERVED here — unit 10's AC6 at its order and unit 23's AC2 at the close.
- **S2** — id 3, M2, landing on units 5, 8 and 10 (each r3 id 3), 23 and 36. The editors of the seed's
  loads are units 5 and 1; unit 8's guard-path edit owes the seed nothing; unit 5's §7 names
  `instruction-eval`; unit 23's S1 and AC1 name units 5 and 1. NOT OBSERVED here — unit 23's AC1, a
  precondition read at writing.
- **S3** — id 4, M3, landing on units 32 and 33. Every mutating case of the `three-homes` plant works
  on its own copy of the scratch registry, and writes the shipped bytes back and compares them
  before it returns. NOT OBSERVED here — unit 32's AC3, the cases run in reverse.
- **S4** — id 29, M3, the same correction as S3. NOT OBSERVED here — unit 32's AC3.
- **S5** — id 5, M4, landing on units 35 and 5 (r3 id 5). The `graded-by-a-row` pass line counts and
  names its records, AC1 reads 2 and AC3 reads 3 with the keep's path, and a plant that writes no
  record prints `FAIL · 0 records`. NOT OBSERVED here — unit 35's AC1 and AC4.
- **S6** — id 6, M5, landing on units 31 and 47. Unit 31's §4 rationale is corrected, since the roles
  adopter self-test is held on a default bar and a `format-guard.js` edit never selects it; its arm
  moves to `tools/hooks/format-guard.test.sh`, whose leg the hook selects; and unit 47 S3 adds
  `{prefix}/roles/handoff.py` and `{prefix}/roles/roles_lib.py` to that leg's guard, so a renderer edit
  selects it too. NOT OBSERVED here — unit 47's AC1.
- **S7** — id 8, M6, landing on unit 36. The `seed-loads` plant spells its commits one by one, the loads
  in commit 1 and the case naming commit 1's sha in commit 2. NOT OBSERVED here — unit 36's AC1.
- **S8** — id 13, M7, landing on units 10 (r3 id 13), 23 and 36. The seed's `**Loads:**` names the three
  audit agents in their rendered `.claude/agents/` form, and unit 10's guard admits `.claude/agents/`.
  NOT OBSERVED here — unit 36's AC1, whose plant commits the rendered loads.
- **S9** — id 14, M8, landing on unit 31. The arm's python side writes UTF-8 bytes through
  `sys.stdout.buffer.write` and node reads stdin as `utf8`. NOT OBSERVED here — unit 31's AC3, run
  once with `PYTHONUTF8=0`.
- **S10** — id 19, M9, landing on unit 33. The `disjoint-homes` case counts the rows whose home admits
  each planted path through the grader's own `derive_record_kind`, and its §4 is re-cited to
  TOOL-dTotalRecall-42 S5 and §5. NOT OBSERVED here — unit 33's AC1 and AC2.
- **S11** — id 15, M10, landing on units 38, 29 and 6 (r3 id 15). A re-added work order maps to its
  newest add, the add that wrote its bytes at `HEAD`, through a `newest` keyword on
  `tree_lib.read_adding_commits` whose default keeps today's callers on the first add. NOT OBSERVED
  here — unit 38's AC1 and AC4.
- **S12** — id 20, M11, landing on units 38 and 29. `tree_lib.read_git_output` and the two readers take
  a `timeout` keyword, and unit 29's step passes its 120 s bound through them. NOT OBSERVED here —
  unit 38's AC3.
- **S13** — id 24, M12, landing on unit 34. The pass holds the codebase map fresh, §7 names
  `codebase-map coverage + freshness`, and AC4 reads `gen_map.py --check`. NOT OBSERVED here — unit
  34's AC4.
- **S14** — id 28, M13, landing on unit 46, which builds it. The widened guards carry each entry
  file's import closure: the runlog kit as a directory, `roles_lib.py`, `tree_lib.py`,
  `catalogue.toml`, `budgets.py`, `policy-mirror.js` and `scratch-guard.js`. NOT OBSERVED here — unit
  46's AC1 and AC2.
- **S15** — id 31, M14, landing on units 10 (r3 id 31), 23, 36 and 41. The owed rule diffs the
  replayed sha against the working tree with the untracked loads, and the `seed-loads` plant holds an
  uncommitted edit owed. NOT OBSERVED here — unit 36's AC3.
- **S16** — id 32, M15, landing on units 40, 3 (r3 id 32) and 21. A list answer's refusal is per entry:
  the entry carrying a line break is `<name>: unread · refused value` in its place, the other entries
  as answered. NOT OBSERVED here — unit 40's AC3.
- **S17** — id 7, L1, landing on units 37 and 47. The criterion that observes check 7c's classing is
  `python tools/govkit/govkit.py selfcheck` after the pass, staged red by the bare template path in a
  scratch copy, and the leg line has no criterion of its own. NOT OBSERVED here — unit 47's AC2.
- **S18** — id 16, L1, the same correction as S17. NOT OBSERVED here — unit 47's AC2.
- **S19** — id 26, L1, the same correction as S17. NOT OBSERVED here — unit 47's AC2.
- **S20** — id 9, L2, landing on unit 31. AC3's staged red reads the lines that go red: `returned` and
  `merged` refused by the guard, `SPEC` caught only by the bracket assertion, and `returned`'s second
  form raising `RolesError` naming `units`. NOT OBSERVED here — unit 31's AC3 with unit 44's AC2 and
  unit 45's AC1.
- **S21** — id 10, L3, landing on unit 41. Its §1 landing list names units 19 and 25. NOT OBSERVED
  here — a prose correction.
- **S22** — id 17, L4, landing on unit 31. Its §4 and §10 name `build_shape_regex` in
  `tools/runlog/prose.py`, and its Alternatives rejected says why the renderer keeps its own split.
  NOT OBSERVED here — a record of a seam; unit 31's AC3 holds the copy to the guard.
- **S23** — id 18, L5, landing on unit 34. Its S2 extends `memory/gotchas/spec-names-code-its-base-lacks.md`
  rather than minting a second record. NOT OBSERVED here — unit 34's AC1 and AC2.
- **S24** — id 21, L6, landing on units 32, 33, 34, 35, 36, 37, 39, 40 and 41. Each §10 records a
  `reuse_lookup.py` phrase for that unit's own behaviour and its top candidates. Observed by AC2.
- **S25** — id 33, L7, landing on units 39 and 3 (r3 id 33). `read_metrics_lines` skips a blank line
  and ends the section at the next `## ` heading or the end of the text, and the `metrics-repeat`
  plant reads a record carrying both. NOT OBSERVED here — unit 39's AC3.

## 3. Non-goals (OUT)

- A class gate per left-shift line. Each item's correction is the sibling's to build and observe.
- The HIGH corrections: `TOOL-dCalibratedLens-42` to `-47`.
- Re-reviewing any sibling. The next audit reads every spec this disposal moved.
- AC1 observes only the disposal's text and is green at writing; it is a precondition, not an
  observation of a build.

### Edges

none

## 4. Design

### Evidence

- The report's appendix: 16 MEDIUM and 9 LOW confirmed by raw id, and the merges its review shape
  names (ids 4 and 29 into M3; ids 7, 16 and 26 into L1).
- `memory/guides/BUILD-METHOD.md` M4: the minors batch into one unit, two only across disjoint write
  sets; M6's clauses decide disjointness.
- The siblings' write sets: units 32, 33, 35, 39, 40, 42 and 43 write `tools/loop/loop_review.py`;
  units 31, 44 and 45 write `tools/hooks/format-guard.test.sh`; units 46 and 47 write
  `tools/gate-legs.json`. No half of the minors lands outside those shared files.

### Inventory

No identifier is minted.

### Files touched (estimate)

None. Every correction is sibling text, built by the sibling it lands on.

### Alternatives rejected

- **Two batch units.** There is no second write set to build concurrently: the batch builds no file.
- **Fold the minors into the HIGH units.** Each HIGH unit is one mechanism; a minor rides with the
  sibling whose text it corrects, and units 46 and 47 carry ids 28, 6 and the L1 ids because they are
  the units that write those rows.

## 5. Production-readiness checklist

- security — N/A: sibling text only.
- perf / scale — N/A.
- error / empty / loading states — N/A.
- observability — each sibling's §9 line names this unit and the record.
- risks — a sibling's correction read as this unit's coverage: each S-item names the sibling's
  criterion that observes it.
- testing — AC1 and AC2 at writing; each sibling's amended criterion at its own pass.
- migration — N/A.
- user docs — N/A.

## 6. Acceptance criteria

- **AC1** — When `grep -l "TOOL-dCalibratedLens-48"` runs over the build's `spec/` folder, it lists
  the specs of units 3, 5, 6, 8, 10, 21, 23, 29, 31 to 41, 46 and 47.
  Red when: a sibling the batch lands on carries no line naming this unit, so its correction has no
  record of the finding it closes.
- **AC2** — When a `python -c` probe reads the first `reuse_lookup.py "<phrase>"` of each §10 in the
  specs of units 31 to 48, no phrase appears twice.
  Red when: two units of one disposal cite one probe phrase, so one of them asked nothing about its own
  behaviour.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-03 · initial draft, the batch of the round-3 spec audit
  `2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit`'s 16 MEDIUM and 9 LOW; units 3, 5, 6, 8, 10,
  21, 23, 29 and 31 to 41 amended at the disposal, and units 46 and 47 written with ids 28, 6, 7, 16
  and 26.

## 10. Reuse audit

Every correction extends the sibling it lands on; no seam is minted. `python
tools/codebase-map/reuse_lookup.py "batch a spec audit's minor findings into one unit"` ranked name
stems only (`units` in `tools/unattended/unattended.test.sh`, `audit`, `read_spec_revisions`,
`parse_spec_h1`); none batches findings, which is the disposal's authored act.

Recall terms used: `python tools/memory-recall/query.py "how is a staged break that an ancestor
clause cannot make red repaired, and how is a spec audit finding promoted to a repair unit" --terms
"staged break ancestor clause superseded red twin spec audit promoted repair unit order shape line
renderer"`
