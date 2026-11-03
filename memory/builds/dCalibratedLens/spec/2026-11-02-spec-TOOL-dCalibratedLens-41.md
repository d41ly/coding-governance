# TOOL-dCalibratedLens-41 — the round-2 spec audit's 28 minors batched: each correction carried by the sibling it lands on, and the loop legs' guards widened to the files their plants read

**Status:** DEFERRED · rev-2 · 2026-11-03 · node a · Tier-2 · base 8bec4cef · streams tooling · order 19 · advances TOOL-dCalibratedLens-18

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-02-build-TOOL-dCalibratedLens-41-deviation-411.md](../build/2026-11-02-build-TOOL-dCalibratedLens-41-deviation-411.md) | deviation | — |
| [2026-11-02-prompt-TOOL-dCalibratedLens-31-promoted-fix-brief.md](../prompts/2026-11-02-prompt-TOOL-dCalibratedLens-31-promoted-fix-brief.md) | research | TOOL-dCalibratedLens-31 TOOL-dCalibratedLens-32 TOOL-dCalibratedLens-33 TOOL-dCalibratedLens-34 TOOL-dCalibratedLens-35 TOOL-dCalibratedLens-36 TOOL-dCalibratedLens-37 TOOL-dCalibratedLens-38 TOOL-dCalibratedLens-39 TOOL-dCalibratedLens-40 |
| [2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit.md](../reviews/2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit.md) | spec-audit | TOOL-dCalibratedLens-32 TOOL-dCalibratedLens-33 TOOL-dCalibratedLens-34 TOOL-dCalibratedLens-35 TOOL-dCalibratedLens-40 TOOL-dCalibratedLens-39 TOOL-dCalibratedLens-38 TOOL-dCalibratedLens-31 TOOL-dCalibratedLens-37 TOOL-dCalibratedLens-36 |

<!-- /gen:spec-records -->

## 1. Goal

The round-2 spec audit of units 19 to 30,
`reviews/2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit.md`, exited BOUNDED with 38 confirmed
findings; `TOOL-dCalibratedLens-31` to `-40` take its BLOCKER and its nine HIGH. This unit is
BUILD-METHOD M4's batch of its 22 MEDIUM and 6 LOW by raw id, one scope item per id, in report order.
They land on units 1, 2, 3, 6 and 19 to 30, unit 25 by its third criterion, which moved to
`TOOL-dCalibratedLens-37` (round-3 id 10), so the batch repairs no unit in particular and builds
last, order 19, above every unit of the build at its writing. They do not split into two disjoint write sets:
the corrections meet in `tools/loop/loop_review.py` and `tools/loop/measure.py`, which several
siblings write, so one unit carries them.

Every id: M1 3; M2 4; M3 5, 16, 23, 39; M4 7, 33; M5 10, 20, 38; M6 12; M7 13; M8 15; M9 17; M10 21;
M11 22; M12 32; M13 34; M14 35; M15 36; M16 40; L1 8; L2 9; L3 18, 29; L4 28; L5 41.

Each correction was made at the audit's disposal in the text of the unbuilt sibling it lands on: a
rev bump of that spec with a §9 line naming this unit and the review record by its stem, the S-item
or criterion rewritten in place for units 19 to 30 and, for units 1 to 17, a bullet `- **r2 id <n> ·
…**` in a §4 "Amendments (round-2 spec audit)" section with the criterion text itself rewritten where
a criterion is what the finding names. Each sibling then builds the corrected design and observes it
through its own criterion. The two corrections no sibling owned, ids 13 and 28, widen three guards;
the round-3 spec audit (`reviews/2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit.md`, id 22)
found them made in a manifest the leg factory will render, so `TOOL-dCalibratedLens-46` builds them
in each leg's declaration, and this unit builds no file of its own.

## 2. Scope (IN)

- **S1** — id 3, M1, landing on unit 30. AC1 greps `- **id 2 · ` for id 45 in specs 3, 4, 6 and 16,
  is stated a spec-text precondition read at writing, and S1 to S41 say each is observed by the
  amended criterion of the sibling it lands on. NOT OBSERVED here — a spec-text correction; no built
  code carries it.
- **S2** — id 4, M2, landing on units 19, 20, 21, 22, 23, 24, 26, 27 and 29. Each AC1 that greps
  sibling spec text, and unit 26's AC4, is stated a precondition, and each S1 names the criterion of
  this unit's plant or the sibling's that runs the amended code. NOT OBSERVED here — a spec-text
  correction; no built code carries it.
- **S3** — id 5, M3, landing on unit 25's third criterion, which moved with its guard to
  `TOOL-dCalibratedLens-37` (id 24): the command indexes the top-level list of `gate-legs.json`.
  NOT OBSERVED here — `TOOL-dCalibratedLens-37` AC2 runs the corrected command.
- **S4** — id 16, M3, the same criterion and correction as S3. NOT OBSERVED here —
  `TOOL-dCalibratedLens-37` AC2.
- **S5** — id 23, M3, the same criterion and correction as S3. NOT OBSERVED here —
  `TOOL-dCalibratedLens-37` AC2.
- **S6** — id 39, M3, the same criterion and correction as S3, its base state the six guard entries
  with no charter path. NOT OBSERVED here — `TOOL-dCalibratedLens-37` AC2.
- **S7** — id 7, M4, landing on units 3 and 27. An empty-`accept` proposal is refused by its own
  printed line, files nothing for itself, and is not the file item's refusal: the walk exits 0 and the
  period records. Unit 27 S3's claim holds on that path. NOT OBSERVED here — unit 27's third
  criterion runs the plant twice.
- **S8** — id 33, M4, landing on unit 22. Its plant runs `run` with a counting filer as well as
  `--dry-run`, and its second criterion states exit 0 and that a second run files no new intake.
  NOT OBSERVED here — unit 22's second criterion.
- **S9** — id 10, M5, landing on units 28 and 6. `read_measured_item_budget` reaches unit 3's
  `read_loop_records` and `read_metrics_lines` through `resolve_kit_dir`, so one ordering rule has one
  copy; an absent loop kit reads 96,000 with its stderr line. NOT OBSERVED here — unit 6's seventh
  criterion.
- **S10** — id 20, M5, landing on units 3 and 30. Unit 6 joins the caller list of unit 3's id-30
  bullet and of unit 30's S16. NOT OBSERVED here — a spec-text correction.
- **S11** — id 38, M5, landing on units 3 and 6. `read_loop_records` lists
  `git ls-tree -r --name-only HEAD -- memory/loop-review/`, the folder prefix, and keeps a name only
  when `fnmatch.fnmatchcase(name, "memory/loop-review/*-loop-review-*.md")` holds, since `git ls-tree`
  matches a path as a literal prefix and never as a glob (round-3 id 11, `TOOL-dCalibratedLens-43`);
  it reads the revision, never the index; unit 6's seventh criterion plants a staged, uncommitted
  newest record and asserts the committed one is listed. NOT OBSERVED here — unit 6's seventh
  criterion and `TOOL-dCalibratedLens-43`'s `records-listed` plant.
- **S12** — id 12, M6, landing on unit 20. S3 and the third criterion fail the plant itself, naming
  the cut record, when a cut-field run exits 0; the `home-kind mismatch` gloss is gone. NOT OBSERVED
  here — unit 20's third criterion.
- **S13** — id 13, M7. The `loop-review selftest` and `loop measure fixtures` guards gain the files
  the loop plants run and what those files import. Built by `TOOL-dCalibratedLens-46` S3 and S4, in
  each leg's declaration (round-3 ids 22 and 28). NOT OBSERVED here — `TOOL-dCalibratedLens-46` AC1.
- **S14** — id 15, M8, landing on units 1 and 24. Unit 1's third criterion's own text carries the
  `node -e` payload pipe, and unit 24's first criterion greps that criterion, not the amendment
  bullet. NOT OBSERVED here — unit 24's second criterion runs the payload.
- **S15** — id 17, M9, landing on units 2 and 26. Under `node-journal` an `always_run` leg that
  declares `doc_reads` is observed only when a windowed bar named it red, because a docs-mode bar
  skips it before its guard is read; unit 26 adds a `catch-docs-only` plant. NOT OBSERVED here —
  unit 26's second criterion.
- **S16** — id 21, M10, landing on unit 21. The `metrics-multi` plant parses the written record
  through `read_metrics_lines` and compares its triples to the planted pairs, staged red by a splitter
  that cuts at the first ` · `; §10 names `read_metrics_lines` and `render_loop_record`. NOT OBSERVED
  here — unit 21's second criterion.
- **S17** — id 22, M11, landing on units 3 and 27. The gather item's outcome line counts its unread
  readings, `loop — <key> · item.loop.gather · measured · <n> unread: <names>`. NOT OBSERVED here —
  unit 27's second criterion.
- **S18** — id 32, M12, landing on unit 27. `record-refuses` runs `run` without `--dry-run`, the key
  in `GOV_CADENCE_KEY=2026-W45` as the executor supplies it, and the filer is the counting stub; its
  staged break reads a count above 0. NOT OBSERVED here — unit 27's third criterion.
- **S19** — id 34, M13, landing on unit 29. A tracked work order the adding-commit reader leaves
  unanswered is counted into one stderr line and never raises, and the `item-budget-tree` plant
  asserts that count equals what a per-path `git log --diff-filter=A -1` leaves unanswered.
  NOT OBSERVED here — unit 29's second criterion.
- **S20** — id 35, M14, landing on unit 29. Every adding commit with no `.governance/policy.toml`
  joins one absent group, read once at one of its commits as the catalogue default, and the measure
  fixture plants a pre-policy commit. NOT OBSERVED here — unit 29's second criterion.
- **S21** — id 36, M15, landing on unit 23. S1 is a rule: the replay is recorded after the last commit
  touching a path the seed loads, judged right before the close bar by `git diff --name-only <replayed
  sha>` over those loads against the working tree, with the untracked loads, as unit 10 S3 reads it
  (round-3 id 31); `check_evals.py` is re-read after every later fix pass, unit 24's red path and the
  closing review's fixes named as triggers. NOT OBSERVED here — unit 23's second criterion, the main
  loop's.
- **S22** — id 40, M16, landing on unit 21. A list reading that answers no pair writes one line
  `<name>: searched-none · <source>`, and the `metrics-multi` plant carries an empty-list case.
  NOT OBSERVED here — unit 21's second criterion.
- **S23** — id 8, L1, landing on unit 20. Its first criterion also probes `TYPED_RECORD_KINDS` in
  `tree_lib.py` and counts both kinds in `HYGIENE.template.md` and `memory/HYGIENE.md`.
  NOT OBSERVED here — unit 20's first criterion.
- **S24** — id 9, L2, landing on unit 28. Its first criterion matches an amended S-item opening with
  `\(amended, ids? [0-9, ]*\b50\b`. NOT OBSERVED here — a spec-text correction.
- **S25** — id 18, L3, landing on units 19 to 29. Each spec's §3 states that its first criterion
  observes only the disposal text and is green at writing, as unit 30's does. NOT OBSERVED here — a
  spec-text correction, made with S2's.
- **S26** — id 29, L3, the same correction as S25. NOT OBSERVED here — a spec-text correction.
- **S27** — id 28, L4. The `tier2-review self-test` guard gains `{prefix}/hooks/agent-cap.js`, the
  hook unit 24's arm runs, and what it loads. Built by `TOOL-dCalibratedLens-46` S5, in the leg's
  declaration (round-3 ids 22 and 28). NOT OBSERVED here — `TOOL-dCalibratedLens-46` AC2.
- **S28** — id 41, L5, landing on unit 29. The argv staged break is a step that refuses when the argv
  it would pass exceeds 32,767 bytes, so the red does not depend on the host's limit. NOT OBSERVED
  here — unit 29's second criterion under its staged break.

## 3. Non-goals (OUT)

- A class gate per left-shift line. Each item's correction is the sibling's to build and observe;
  the two guard edits no sibling owned are `TOOL-dCalibratedLens-46`'s (round-3 id 22).
- The HIGH and BLOCKER corrections: `TOOL-dCalibratedLens-31` to `-40`.
- Re-reviewing any sibling. The next audit reads every spec this disposal moved.

### Edges

- **hands-off** `TOOL-dCalibratedLens-46` — the guard widenings of S13 and S27, which that unit makes in each leg's declaration (round-3 id 22)

## 4. Design

### Evidence

- `tools/gate-legs.json` at base: the `tier2-review self-test` guard is `{prefix}/workflows/` and
  `{prefix}/memory-tree/gen_build_index.py`.
- Unit 2 S11 and unit 4 S9: the loop legs are guarded on `{prefix}/loop/` and
  `{prefix}/loop/measure.py`.
- `python tools/check-spec-tokens.py --legs-for` over `tools/roles/handoff.py` and
  `tools/memory-tree/tree_lib.py` at base names `policy fixtures` as their one narrow leg; neither
  selects a loop leg.
- `memory/gotchas/held-suite-guard-misses-a-sibling-kit.md`, the class ids 13 and 28 instance.

### Inventory

No identifier is minted.

### Files touched (estimate)

None. The guard files of S13 and S27 are `TOOL-dCalibratedLens-46`'s.

### Alternatives rejected

- **Guards in units 2 and 4's own rows at their passes.** The files are read by plants landed at
  orders 3 to 14; a guard naming a file before its reader exists is speculative, and one owner at the
  end edits each row once, `TOOL-dCalibratedLens-46`.
- **Two batch units.** Every correction but S13 and S27 is sibling text, so there is no second write
  set to build concurrently.

## 5. Production-readiness checklist

- security — N/A: sibling text only.
- perf / scale — N/A.
- error / empty / loading states — N/A.
- observability — each sibling's §9 line names this unit and the record.
- risks — a sibling's correction read as this unit's coverage: each S-item names the criterion that
  observes it in the sibling, and AC1 is a precondition, not an observation of a build.
- testing — AC1 at writing; each sibling's amended criterion at its own pass.
- migration — N/A.
- user docs — N/A.

## 6. Acceptance criteria

- **AC1** — When `grep -n "TOOL-dCalibratedLens-46"` runs over the specs of units 2 and 4 and this
  one, units 2 and 4 each hand their row's guard to unit 46 and this spec's S13 and S27 name it as
  their builder; green at writing, a precondition of unit 46's criteria.
  Red when: a guard widening is claimed by two units, or by none.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-02 · initial draft, the batch of the round-2 spec audit
  `2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit`'s 22 MEDIUM and 6 LOW; units 1, 2, 3, 6, 20
  to 24 and 26 to 30 amended at the disposal.
- rev-2 · 2026-11-03 · §1 §3 §4 §5 §6 §7 §10 S11 S13 S21 S27 AC1 AC2 · amended at the disposal of the
  round-3 spec audit `2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit`: S11 lists by folder prefix
  (id 11, `TOOL-dCalibratedLens-43`); S13 and S27 and their criteria move to
  `TOOL-dCalibratedLens-46` (id 22), carrying the module closure of id 28; from
  `TOOL-dCalibratedLens-48`, §1's landing list names units 19 and 25 (id 10), S21's rule reads the
  working tree (id 31) and §10 records this unit's own probe phrase (id 21); §3 hands the guards to
  unit 46.

## 10. Reuse audit

Every correction extends the sibling it lands on, rewritten in place with a rev bump and a §9 line;
the guard rows are `TOOL-dCalibratedLens-46`'s. `python tools/codebase-map/reuse_lookup.py "rewrite a
sibling spec's text with a revision bump at a disposal"` ranked name stems only (`read_text`,
`write_text`, `read_spec_revisions`, `load_text`); no seam fits beyond the sibling specs, since a
disposal is authored text. The recall probe returned TOOL-cMendedVintage-19, the placement ruling;
a batch that repairs no unit in particular takes the order above every unit.

Recall terms used: `python tools/memory-recall/query.py "how is a staged break that an ancestor
clause cannot make red repaired, and how is a spec audit finding promoted to a repair unit" --terms
"staged break ancestor clause superseded red twin spec audit promoted repair unit order shape line
renderer"`
