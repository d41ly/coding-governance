# TOOL-dFairHearing-40 — the round-5 spec audit's 35 minors: one build-wide version reading on one base, an attempt checker that refuses what it cannot place, and criteria a correct build can pass

**Status:** CLOSED · rev-6 · 2026-11-04 · node d · Tier-2 · base 3708a705 · streams tooling · order 28 · closes TOOL-dFairHearing-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dFairHearing-40-deviation-401.md](../build/2026-10-23-build-TOOL-dFairHearing-40-deviation-401.md) | deviation | — |
| [2026-11-03-build-TOOL-dFairHearing-1-agent-ledger.md](../build/2026-11-03-build-TOOL-dFairHearing-1-agent-ledger.md) | journal | TOOL-dFairHearing-1 TOOL-dFairHearing-2 TOOL-dFairHearing-3 TOOL-dFairHearing-4 TOOL-dFairHearing-5 TOOL-dFairHearing-6 TOOL-dFairHearing-7 TOOL-dFairHearing-8 TOOL-dFairHearing-9 TOOL-dFairHearing-10 TOOL-dFairHearing-11 TOOL-dFairHearing-12 TOOL-dFairHearing-13 TOOL-dFairHearing-14 TOOL-dFairHearing-15 TOOL-dFairHearing-16 TOOL-dFairHearing-17 TOOL-dFairHearing-18 TOOL-dFairHearing-20 TOOL-dFairHearing-21 TOOL-dFairHearing-22 TOOL-dFairHearing-23 TOOL-dFairHearing-25 TOOL-dFairHearing-26 TOOL-dFairHearing-27 TOOL-dFairHearing-28 TOOL-dFairHearing-29 TOOL-dFairHearing-30 TOOL-dFairHearing-31 TOOL-dFairHearing-32 TOOL-dFairHearing-33 TOOL-dFairHearing-34 TOOL-dFairHearing-35 TOOL-dFairHearing-36 TOOL-dFairHearing-37 TOOL-dFairHearing-38 TOOL-dFairHearing-39 |
| [2026-11-04-build-TOOL-dFairHearing-40-1-acceptance-ledger.md](../build/2026-11-04-build-TOOL-dFairHearing-40-1-acceptance-ledger.md) | journal | — |
| [2026-11-04-build-TOOL-dFairHearing-40-1-builder-return.md](../build/2026-11-04-build-TOOL-dFairHearing-40-1-builder-return.md) | journal | — |
| [2026-11-04-build-TOOL-dFairHearing-40-2-builder-return.md](../build/2026-11-04-build-TOOL-dFairHearing-40-2-builder-return.md) | journal | — |
| [2026-10-23-prompt-TOOL-dFairHearing-38-promoted-fix-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-38-promoted-fix-brief.md) | research | TOOL-dFairHearing-38 TOOL-dFairHearing-39 |
| [2026-10-23-prompt-TOOL-dFairHearing-40-1-spec-writer.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-40-1-spec-writer.md) | journal | — |
| [2026-11-02-prompt-TOOL-dFairHearing-40-build-brief.md](../prompts/2026-11-02-prompt-TOOL-dFairHearing-40-build-brief.md) | research | — |
| [2026-11-03-prompt-TOOL-dFairHearing-25-fold-fix-brief.md](../prompts/2026-11-03-prompt-TOOL-dFairHearing-25-fold-fix-brief.md) | research | TOOL-dFairHearing-25 TOOL-dFairHearing-30 TOOL-dFairHearing-35 TOOL-dFairHearing-32 TOOL-dFairHearing-37 |
| [2026-11-03-prompt-TOOL-dFairHearing-27-sweep-fix-brief.md](../prompts/2026-11-03-prompt-TOOL-dFairHearing-27-sweep-fix-brief.md) | research | TOOL-dFairHearing-27 TOOL-dFairHearing-28 TOOL-dFairHearing-29 TOOL-dFairHearing-30 TOOL-dFairHearing-31 TOOL-dFairHearing-35 TOOL-dFairHearing-32 TOOL-dFairHearing-33 TOOL-dFairHearing-34 TOOL-dFairHearing-36 TOOL-dFairHearing-37 TOOL-dFairHearing-38 TOOL-dFairHearing-39 |
| [2026-11-04-prompt-TOOL-dFairHearing-40-1-spec-writer.md](../prompts/2026-11-04-prompt-TOOL-dFairHearing-40-1-spec-writer.md) | journal | — |
| [2026-11-04-prompt-TOOL-dFairHearing-40-2-spec-writer.md](../prompts/2026-11-04-prompt-TOOL-dFairHearing-40-2-spec-writer.md) | journal | — |
| [2026-11-04-prompt-TOOL-dFairHearing-40-closes-fix-brief.md](../prompts/2026-11-04-prompt-TOOL-dFairHearing-40-closes-fix-brief.md) | research | — |
| [2026-11-04-prompt-TOOL-dFairHearing-40-fix-brief.md](../prompts/2026-11-04-prompt-TOOL-dFairHearing-40-fix-brief.md) | research | — |
| [2026-11-04-review-TOOL-dFairHearing-1-40-diff-review.md](../reviews/2026-11-04-review-TOOL-dFairHearing-1-40-diff-review.md) | diff-review | TOOL-dFairHearing-1 TOOL-dFairHearing-2 TOOL-dFairHearing-3 TOOL-dFairHearing-4 TOOL-dFairHearing-5 TOOL-dFairHearing-6 TOOL-dFairHearing-7 TOOL-dFairHearing-8 TOOL-dFairHearing-9 TOOL-dFairHearing-10 TOOL-dFairHearing-11 TOOL-dFairHearing-12 TOOL-dFairHearing-13 TOOL-dFairHearing-14 TOOL-dFairHearing-15 TOOL-dFairHearing-16 TOOL-dFairHearing-17 TOOL-dFairHearing-18 TOOL-dFairHearing-20 TOOL-dFairHearing-21 TOOL-dFairHearing-22 TOOL-dFairHearing-23 TOOL-dFairHearing-25 TOOL-dFairHearing-26 TOOL-dFairHearing-27 TOOL-dFairHearing-28 TOOL-dFairHearing-29 TOOL-dFairHearing-30 TOOL-dFairHearing-31 TOOL-dFairHearing-32 TOOL-dFairHearing-33 TOOL-dFairHearing-34 TOOL-dFairHearing-35 TOOL-dFairHearing-36 TOOL-dFairHearing-37 TOOL-dFairHearing-38 TOOL-dFairHearing-39 |

<!-- /gen:spec-records -->

## 1. Goal

One batch unit closes every MEDIUM and LOW finding that the round-5 spec audit confirmed
(`memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-33-37-spec-audit.md`), 35
report ids over units 33 to 37. MEDIUM ids: 2 and 26 (item M1), 3, 20 and 27 (M2), 14, 21 and 35 (M3),
13 (M4), 4 (M5), 12 (M6), 15 and 38 (M7), 22 (M8), 18 (M9), 25 (M10), 28 (M11), 31 (M12) and 33 (M13).
LOW ids: 5 (L1), 6 (L2), 7 (L3), 8 (L4), 9 and 24 (L5), 10 (L6), 16 (L7), 17 (L8), 23 (L9), 29 (L10),
30 (L11), 34 (L12), 36 (L13), 37 (L14) and 39 (L15). Each id is its own §2 item. The minors land on
five units, so this unit repairs no one unit and sits above every order in the build, after units 38
and 39. That order is also what item M1 needs: this unit's commit is the build's last pass commit, the
one place a build-wide version reading sees every unit's edits. A criterion it supersedes is named by
the hands-off bullet in that unit's §3. Every unit it supersedes is CLOSED, and units 33, 34 and 36
closed with no acceptance ledger, each builder return owing it to the build's close. So this unit's
own acceptance ledger records each supersession, naming the unit and the criterion, outside its
`**Evidences:**` block (`TOOL-dFairHearing-23` §8 F7's form, written where it can be read now).

## 2. Scope (IN)

Each item names its report id, its report item, the unit it lands on and the criterion that observes
it. Where a report item merges ids, the later id points at the first one's mechanism.

- **S1** — id 2 (M1, units 33 and 34, AC1). The build-wide half of unit 27 S15's rule is read at this
  unit's commit, after the order-26 passes. Unit 37's commit `6d768c563` edits
  `tools/workflows/tier2-review.template.js`, review-harness's `version_from` carrier per
  `tools/workflows/kit.toml:8`, and unit 36's commit `e69ecfcf0` edits no kit file. `constants.py`
  and `markers.py`, as S18, S19, S26 and S34 correct them, run over `<base>..HEAD` with `<base>` from
  S3. Unit 33 AC1 and unit 34 AC1 keep their reading at their own commit; the "a constant moved on the
  branch" half of each Red when clause is answered here. A unit ordered after this one inherits the
  re-run. Observed by AC1.
- **S2** — id 26 (M1). S1's mechanism. Observed by AC1.
- **S3** — id 3 (M2, units 33, 34 and 36). One base seam for the build-wide reading: S1's `<base>` is
  the sha unit 36's `base.py` prints, which takes `GATE_BASE` unchanged and otherwise calls
  `resolve_compare_base` (`tools/codebase-map/map_lib.py:1507` at `53192a48d`). Units 33 and 34 at
  order 23 read unit 31's probe, and the two bases agree only with `GATE_BASE` unset and `HEAD` ahead
  of the remote tip. Each unit's builder return names `GATE_BASE` unset when its AC1 ran (the returns
  of `479c500ca` and `f94f3ecb9`); their acceptance ledgers are owed to the close. Observed by AC1 and
  AC2.
- **S4** — id 20 (M2). S3's mechanism: the consumes-from edge of units 33 and 34 on unit 31 stays for
  their order-23 reading, and the build-wide reading consumes `base.py` here. Observed by AC2.
- **S5** — id 27 (M2, unit 36 §4, unit 31 AC1). Unit 31's script and its AC1 are left as they are:
  `base <sha> from origin/main` is unit 31's label and `base <sha> from merge-base of HEAD and
  origin/main` is `base.py`'s, each read only by its own criterion. Unit 36 §4's sentence "It prints the
  line unit 31's probe prints, so units 33 and 34 read its sha the same way" is superseded by S3's
  statement. Observed by AC2.
- **S6** — id 14 (M3, unit 35 S1, S2 and §4). The checker's `failed` outcome, a completed void attempt
  that takes one of the two eligible slots, and its refusal of an attempt-opening row it cannot parse
  are carried by unit 35 S7, before unit 35 scores. This item keeps the read after: the checker,
  re-run over unit 30's record at this unit's commit, prints what unit 35's `## Scoring` quotes.
  Observed by AC3.
- **S7** — id 21 (M3). A `Completed` row refused naming its line, never dropped: carried by unit 35
  S7. NOT OBSERVED here: unit 35 AC2 observes it.
- **S8** — id 35 (M3). A call that died or timed out is `failed`, so its label is never the runner's
  choice between `refused` and `completed`: carried by unit 30 S9, which labels it, and unit 35 S7,
  which reads it. NOT OBSERVED here: unit 35 AC2 observes it.
- **S9** — id 13 (M4, unit 35 S2, AC1), read after unit 35 scores. The void column is re-derived, never
  trusted. For each attempt row, `void.py` (§4) derives its void cause from evidence the record names
  beside that clone: the report's parse, read by `parse_candidates` as `--experiment` counts a run
  parsed (§8 F5); the dead finders and skeptics its Workflow result file records (§8 F4); and for a
  cell citing an outside read, the transcript line it quotes. A cell that disagrees, a `refused` row
  whose clone holds a report, or a named report, result file or transcript not on disk is red. What
  had to hold before the runs is carried: unit 30 S9 writes each outside-read cell with its transcript
  line, and unit 30 S10 and unit 35 S9 keep the reports and transcripts on disk until this pass, as
  unit 35's `## Scoring` records (`test -e` over 8 reports and 24 transcript files). The result files
  sit in the session's `tasks/` folder the record names, which no keep rule covers; all nine are on
  disk at `53192a48d`. Observed by AC4.
- **S10** — id 4 (M5, unit 35 AC3, unit 37 AC11). Unit 35 AC3's half, which holds unless the checker
  exited 3, is carried by unit 35 S8. Unit 37 AC11's half: the clones unit 37's ledger grades are the
  scored ones, distinct, and a `void after cap` pair is listed with its reason. Unit 35's checker named
  no `void after cap` pair (its `## Scoring` section), so that branch has no population here, and this
  unit's ledger states it empty, never as coverage. Observed by AC5.
- **S11** — id 12 (M6, unit 36 AC3). Carried by unit 36 AC3 since its rev-3: its suite input is base's
  hook suite as `git show` prints it at `3708a705`, and the builder return of `e69ecfcf0` records 73
  and 5 under both `PYTHONUTF8` settings. NOT OBSERVED here: unit 36 AC3 observes it, and this unit's
  former AC6, the same reading, is dropped.
- **S12** — id 15 (M7, unit 37 S8 and §4). The per-arm step refuses, exit 2 naming the variable, when
  `SCRATCH` or `ORCH` is empty, and builds the clone's parent from `TEMP`, else `TMPDIR`, refusing when
  both are empty. Carried by unit 30 S7 before its runs, where unit 37 S8 moved. NOT OBSERVED here:
  unit 30 AC5 observes it.
- **S13** — id 38 (M7). The orchestrating commit read as its own call, `git -C "$ORCH" rev-parse
  --verify HEAD`, its status checked before the log line: carried by unit 30 S7. NOT OBSERVED here:
  unit 30 AC5 observes it.
- **S14** — id 22 (M8, unit 37 S8, AC8). The run log line observed over a clean fixture clone: carried
  by unit 30 S7 and its AC5, where unit 37 AC8 moved. NOT OBSERVED here.
- **S15** — id 18 (M9, unit 37 S9, AC9). Unit 37 closed with S9's two-pass reader, its ledger's AC9
  line reading `renderBlankedView` plus a scan of every `${…}`. This unit re-reads the absence through
  `renderLexedView` (`tools/hooks/agent-cap.js:448` at `53192a48d`), which blanks strings, cuts `//`
  comments, blanks template text and copies each `${…}` body with its brace depth saved in
  `interpDepths`, deciding the nested and comment cases that reader leaves open. Observed by AC8.
- **S16** — id 25 (M10, unit 35 S3, S6), completion work after unit 35's decision, correcting none of
  its criteria. Unit 35's record states `selected` (its `**The decision:` line, :374 of unit 30's
  record at `53192a48d`), 26/59 over `ungated`'s 25/59. The range's selection is then the decided
  checklist, and no prose carrier changes: `memory/guides/MERGE-BAR.md`,
  `memory/guides/SESSION-KICKOFF.md`, `memory/HYGIENE.md` and its template
  `tools/memory-tree/HYGIENE.template.md`, the four unit 23 S45 rewords, stay as they are. The
  `ungated` branch, where a carrier is reworded in unit 23 S45's form, has no population. Observed by
  AC9.
- **S17** — id 28 (M11, unit 37 S13, AC12). The cure of a disagreement between `resolveKitDir` in
  `tools/hooks/agent-cap.js` and `tools/lib/resolve_kit_dir.py` on rows 8 and 9 was this unit's, after
  units 36 and 37. Unit 37's ledger records the two agreeing on every row (its AC12 line). The port as
  unit 32 built it tests `.git` with `fs.existsSync` (`tools/hooks/agent-cap.js:997` at `53192a48d`)
  and treats a `JSON.parse` throw as no rows (:1003 to :1005), so there is nothing to cure and this
  unit writes no hook. Unit 37 §7's AC12 arm already stages both breaks, so this unit adds no arm.
  Observed by AC10.
- **S18** — id 31 (M12, unit 33 §4, S3, AC3). `constants.py` catches `RuntimeError`, the base of
  `govkit.Refusal` (bound at `tools/govkit/govkit.py:142` to the class at
  `tools/govkit/upgrade_steps.py:305`, both at `53192a48d`), beside its other exceptions, so a registry
  that does not load exits 2 naming it. Observed by AC11.
- **S19** — id 33 (M13, unit 33 S2, §5). A `new` outcome is a refusal, exit 2, unless the entry's
  descriptor is absent at the base. The registry is read at both ends, and an entry present at the base
  and absent at the head is a refusal naming it. Unit 33 §5's line "a kit removed by the build refuses
  rather than passes" is then true. Observed by AC11 and AC12.
- **S20** — id 5 (L1, unit 37 AC17, AC5). The trap count, `trap '` only on lines of the replay
  section's fenced bash blocks with comments excluded, is carried by unit 25 S9 and its AC8, where unit
  37 AC17 moved. Unit 37 AC5 took the finding's other fix at its rev-6: it counts the argv form
  `"--literal-pathspecs", "ls-files"`, the order git reads. This unit keeps the complement, an
  absence: no `ls-files` then `--literal-pathspecs` spelling, string or argv form, remains in
  `replay_scorer.py`. Unit 37 AC5's valid-path control is its own, armed in its §7. Observed by AC13.
- **S21** — id 6 (L2, unit 35 §4). The checker exits 1 naming the line when a row's last cell is empty:
  carried by unit 35 S7. NOT OBSERVED here: unit 35 AC2 observes it.
- **S22** — id 7 (L3, unit 36 AC6). Unit 36's AC6 is precondition evidence: both of its reads hold at
  unit 36's parent. Unit 36 closed with no acceptance ledger (the builder return of `e69ecfcf0` owes
  it to the close), so this unit's ledger carries the label, on its AC14 line (§8 F6). Observed by
  AC14.
- **S23** — id 8 (L4, unit 37 AC15). Unit 37 AC15 first requires its grep to print the
  `function deriveAddressKey` line, and where the comment above it cites the instrument by line it holds
  `:1665-1666`. Unit 37's ledger records a comment citing no instrument line, so the second half has
  no population at `53192a48d`. Observed by AC15.
- **S24** — id 9 (L5, unit 35 S5). Unit 35 S5's change to unit 30's record's `**Serves:**` line is
  observed. Observed by AC16.
- **S25** — id 24 (L5). S24's mechanism. Observed by AC16.
- **S26** — id 10 (L6, unit 33 S3, AC3). The two refusals unit 33 AC3 never stages are staged: a
  constant resolving at the base and not at the head, and zero constants compared. Observed by AC11.
- **S27** — id 16 (L7, unit 36 §4). S5's mechanism: the sentence is superseded by S3's statement of
  when the two bases agree. Observed by AC2.
- **S28** — id 17 (L8, unit 33 §4). Unit 33 §4's sentence naming `(none declared)` as a value the `(`
  test reads is corrected: the guard above it skips undeclared entries on the predicate
  `resolve_entry_version_at` (`tools/govkit/govkit.py:773-775` at `53192a48d`) uses, so only
  `(unresolvable)` reaches the test. NOT OBSERVED by a criterion: it corrects a sentence and changes no
  behaviour; this unit's ledger records it superseded (§1).
- **S29** — id 23 (L9, unit 33 S2). The `absent` and `new` outcomes are asserted: the `7d98741e3` pair
  prints `absent branch-reconcile` and `absent roles`, and the pair that adds the branch-reconcile kit
  prints `new branch-reconcile 1.0`. Observed by AC12.
- **S30** — id 29 (L10, unit 37 S15). `check_ungated`'s sentence end changed after unit 30's runs used
  it. Unit 30's `ungated` instrument,
  `memory/builds/dFairHearing/build/2026-11-04-build-TOOL-dFairHearing-30-ungated.py`, imports the
  orchestrating repository's `gotchas.py`, and at the orchestrating commit `3cf918a65`
  `GATED_SCOPE_RE` read a sentence end as `\.(?=\S)`. Unit 32's commit `fb755fa80`, which `3cf918a65`
  does not contain, made it `` \.(?![*_)`]*(?:\s|\Z)) `` (`tools/memory-tree/gotchas.py:419` at
  `53192a48d`); unit 37 S15 changes no code and adds a selftest arm. The class set unit 35's
  `## Scoring` records, per `ungated` clone its appended count and its checklist's sha256, is re-derived
  by that instrument with today's function over each kept clone and its range spelled in full shas, as
  the recorded checklist's first line spells it (§8 F7), and compared; this unit's ledger states
  `unchanged` or names each class that moved. Observed by AC17.
- **S31** — id 30 (L11, units 36 and 37 §4). The `--dispatch --writes` set of each order-26 pass names
  every path its pass commit writes: its acceptance ledger record where it commits one, and the
  renders the build-index hook forces into every pass commit (`memory/LIVE.md`,
  `memory/backlog/TOOL.md` and the build README). As built, unit 37's commit `6d768c563` adds its
  ledger and its row names it; unit 36's commit `e69ecfcf0` adds none and writes no supersession into
  the ledgers of units 28, 29 and 31, none of which exists. Observed by AC18.
- **S32** — id 34 (L12, unit 34 §3, §4). Unit 34 §3's attribution is corrected: a marker in an added or
  renamed file, and a marker present only at the head in a modified file, are graded by
  `govkit selfcheck`'s check 5c (`tools/govkit/govkit.py:1975` at `53192a48d`) within its basis of
  claimed paths and `marker_carriers`, never by `kit version markers`, whose script reads a fixed list
  of pairs. A file outside that basis is not graded by either, and the residual says so. NOT OBSERVED by
  a criterion: it corrects an attribution and changes no behaviour; this unit's ledger records it
  superseded (§1).
- **S33** — id 36 (L13, unit 37 S6). Every `git -C ${repo}` interpolation in
  `tools/workflows/tier2-review.template.js`, the prompts and `diffCmd` (:1671 at `53192a48d`) included,
  is quoted as `git -C "${repo}"`, and after unit 37 S6's fold, the `const repo` read at :253, a `repo`
  holding a double quote, a `$` or a backtick is refused naming the character. A path holding a space
  then stays one argument. Observed by AC19.
- **S34** — id 37 (L14, unit 37 S9). S15's mechanism: `renderLexedView` takes an interpolation only
  inside template text and balances its braces, so the nested and comment copies unit 37 S9 left
  undefined are decided. Its residual: it does not blank block comments, so a `/* MAX_LENSES */` copy
  fails the probe closed. Observed by AC8.
- **S35** — id 39 (L15, unit 36 S12). `base.py`'s refusal of a tip answer names both causes that reach
  it: "HEAD is not ahead of <tip>, or shares no merge-base with it (shallow or unrelated history)".
  Observed by AC2.

## 3. Non-goals (OUT)

- No re-review, and no fold into the specs of units 33, 34, 36 and 37. The items unit 35's scoring and
  unit 30's runs needed before they ran are folded into those specs under M4's repair rule (unit 25 §8
  F2). Each item left here makes the corrected statement true and reopens no severity.
- No re-run of a replay and no re-decision. When the checker re-run or the void re-derivation reads
  unit 30's record differently from unit 35's recorded output, AC3 or AC4 goes red and the main loop
  parks the decision; this unit never re-scores.
- No HIGH finding: ids 1 and 11 are `TOOL-dFairHearing-38` and `-39`.
- No new gate leg and no committed checker: `constants.py`, `markers.py`, `base.py`, `attempts.py` and
  `void.py` stay scratch probes, as units 33 to 36 resolved.
- No change to `gotchas.py`, its catalogue or its rendered index header: the header hands a reader the
  classes, and the harness's own acquisition is the workflows README's.
- No help page: `help/` covers neither the review harness, the scorer factory, the hooks nor a
  build-time check.

### Edges

- **consumes-from** `TOOL-dFairHearing-30` — the verdict record, each attempt's clone, report path and Workflow result file, the reports and transcripts its S10 keeps, and its committed `ungated` instrument, which S9, S24 and S30 read
- **consumes-from** `TOOL-dFairHearing-32` — `resolveKitDir`, the port S17 reads, and `GATED_SCOPE_RE`'s sentence end, under which S30 re-derives the recorded class set
- **consumes-from** `TOOL-dFairHearing-33` — `constants.py`, S2, S3, §4, AC1 and AC3, which S1, S3, S4, S18, S19, S26, S28 and S29 correct
- **consumes-from** `TOOL-dFairHearing-34` — `markers.py`, §3 and AC1, which S1, S3, S4 and S32 correct
- **consumes-from** `TOOL-dFairHearing-35` — the checker its S7 carries, the `## Scoring` section and the decision, which S6, S9, S16, S24 and S30 read after it scores
- **consumes-from** `TOOL-dFairHearing-36` — `base.py`, AC3 and AC6, its §4 and its pass's dispatch row, which S3, S5, S11, S22, S27, S31 and S35 read or correct
- **consumes-from** `TOOL-dFairHearing-37` — S6's fold, S9's reader, AC5, AC9, AC11, AC12 and AC15 as its rev-6 reads them, its ledger and its pass's dispatch row, which S10, S15, S17, S20, S23, S31, S33 and S34 read or correct

## 4. Design

### Why one batch unit

M6 admits two halves only when neither writes a file the other reads as an acceptance input. S1 reads
every kit's version carrier, and S33 writes one of them, `tools/workflows/tier2-review.template.js`.
Any split that keeps S1 apart from S33 fails that clause, and S1 must run last. So the 35 minors are
one unit at the build's last order.

### The version probes, corrected (S1, S18, S19, S26, S29, S35)

`constants.py` is unit 33 §4's script with three changes. The `except` tuple gains `RuntimeError`. The
`new` branch refuses unless the descriptor is absent at the base. And before the loop, the registry is
read at both ends:

```python
# inside the try, after read_descriptors
reg = pathlib.Path(govkit.derive_registry_path(root)).resolve().relative_to(root).as_posix()
def ids(ref):
    blob = govkit.blob_at(root, ref, reg)
    return {e.get("id") for e in tomllib.loads(blob.decode("utf-8")).get("entry", [])} if blob else set()
gone = sorted(ids(base) - ids(head))
# after the problems check
if gone:
    refuse(f"registry entries at {base} and not at {head}: {' '.join(gone)}")
# the new branch
elif old.startswith("("):
    if subprocess.run(["git", "-C", str(root), "cat-file", "-e", f"{base}:{dpath}"],
                      capture_output=True).returncode == 0:
        refuse(f"{eid}: its descriptor is at {base} and its constant does not resolve there: {old}")
    print(f"new {eid} {new}")
```

`import tomllib` joins the import line, and the loop names the descriptor path `dpath` where unit 33
wrote `_dpath`. A base holding no registry blob holds no entry, so every entry it lacks is new.
`markers.py` is unit 34 §4's script unchanged. `base.py` is unit 36 §4's script with S35's one change,
its tip refusal:

```python
    if how.endswith(" tip"):
        refuse(f"HEAD is not ahead of {how[:-4]}, or shares no merge-base with it (shallow or unrelated history)")
```

Measured on 2026-10-23: the branch-reconcile kit's descriptor and version file are both added by
`0baf2e47a`, and its parent holds neither. Measured again on 2026-11-04 at `53192a48d` with the
corrected `constants.py`: over `8bec4cefd..HEAD` it printed `constants 20` and exited 0; AC11's three
clone commits and the root pair each exited 2 naming their cause; AC12's two pairs printed their
pinned lines beside `absent policy`, a kit added after 2026-10-23. `govkit.py` binds `Refusal` from its
sibling `upgrade_steps` (:142), so AC11's scratch root holds the govkit kit's modules, not `govkit.py`
alone. With them and no registry the probe exits 2 naming `registry.toml`; with `RuntimeError` taken
out of the tuple it prints `upgrade_steps.Refusal` as a traceback.

### The attempt checker (S6 to S8, S21)

Carried by unit 35 §4 (its S7), before unit 35 scores. S6's re-read runs that checker over unit 30's
record at this unit's commit.

### The void re-derivation (S9)

`void.py <record>` reads the attempts table with unit 35 §4's grammar and, for each row, three things
unit 30's record names in that clone's `## Each clone` bullet: the report path, the Workflow run whose
folder under the record's transcript root holds the cited transcripts, and the Workflow result file
under the record's `tasks/` folder. A report parses when `parse_candidates` in
`tools/workflows/replay_scorer.py`, called as `measure_replay_experiment` calls it
(`tools/workflows/replay_scorer.py:1091-1092` at `53192a48d`), returns rows and no error. A run's dead
agents are its result file's `lensesDead` and `skepticsDead`.

| Row | Must hold | Red when |
|---|---|---|
| `refused` | the clone holds no review report | a report is on disk |
| `completed`, void `-` | the report is on disk and parses, and its result file records 0 dead lenses and 0 dead skeptics | any of the three fails |
| `completed` or `failed`, void naming a cause | the cause re-derives: `not parsed:` from the parse error, the cell's quoted text equal to it; a dead agent from a non-zero result count; an outside read from a cell quoting `<transcript file>:<line>` and the absolute path, where that line holds that path, outside the clone and the scratchpad | the cause does not re-derive, or the quoted line is absent |

It prints `agrees <record> <arm> <attempt>` for each row that holds, and exits 1 naming the first row
that does not. A report, result file or transcript the record names and that is no longer on disk is
red, as not re-derivable. The residual: an outside read on an attempt whose cell reads `-`, which the
pass did not record, is not re-derived; spec 1 §4's probe at order 23 is its only observation. Measured
on 2026-11-04: `parse_candidates` returns 12 rows for f1s1's report, 3 for f2s2's, and for f2s1's the
error its void cell quotes, `liveness: 3 confirmed appendix row(s) against a stated confirmed count of 0`;
all nine result files read `lensesDead` 0 and `skepticsDead` 0.

### The per-arm step (S12 to S14)

Carried by unit 30 §4 (its S7), written into the README's replay section before unit 30's runs.

### The absence probe's view (S15, S34)

The probe slices `const LITERAL_OPENERS` (`tools/hooks/agent-cap.js:120-122` at `53192a48d`),
`checkLiteralOpen`, `resolveLiteralEnd` and `renderLexedView` out of `tools/hooks/agent-cap.js`, each
from its opening line to the next column-0 line opening `function `, `const `, `let ` or `module.`,
and evaluates them together in a `vm` context. `checkLiteralOpen` reads the constant, so a slice
without it fails on a quote after an identifier. `renderLexedView` is not among the hook's exports
(`module.exports`, `tools/hooks/agent-cap.js:906-909` at `53192a48d`), so the probe slices it rather
than requiring the file. A `ReferenceError` names a further name to slice and exits 2, never a pass.
The probe joins the view's `code` lines and searches `\bMAX_LENSES\b`. The same view is applied to
`check-verifier-fanout.js`. Measured on 2026-11-04 with that slice: both files read absent, the three
interpolation copies of AC8 hold the name, and the two comment copies do not.

### The port (S17)

No cure: unit 37's ledger records rows 8 and 9 agreeing, and the port already tests `.git` by
existence, as `tools/lib/resolve_kit_dir.py:29` does with `(d / ".git").exists()`, and treats a
receipt whose `JSON.parse` throws as absent, as :33 catches `ValueError`. AC10 re-reads both rows.

### The recorded class set, re-derived (S30)

The instrument takes `<orch repo> <clone> <base>..<head>`, prints the checklist on stdout and
`f30-ungated: <n> selected + <m> ungated, legs <k>` on stderr. Run with this unit's checkout as the
orchestrating repository, over `$TEMP/f1u1` to `$TEMP/f4u1` and each record's range as
`git rev-parse` spells its two ends in full, its `<m>` and the sha256 of its stdout bytes are compared
with unit 35's `## Scoring` table. Measured on 2026-11-04 at `53192a48d`: 38, 20, 53 and 75 appended,
and `668cc4180bb4`, `bffdbeb67415`, `6f166104d7ff` and `0f260b686f44`, each equal to the record's. With
the ranges spelled short, the four counts and the appended names still agree and every sha differs,
because the checklist's first line carries the range as given. Where a row differs, the run is
repeated with a scratch extraction of `tools/memory-tree/` at `3cf918a65` as the orchestrating
repository, and each `(ungated)` item one run holds and the other does not is a class that moved.

### Files touched (estimate)

- `tools/workflows/tier2-review.template.js`
- `tools/workflows/tier2-review.js`
- `tools/workflows/tier2-review.test.sh`
- `memory/builds/dFairHearing/build/`

`tools/workflows/tier2-review.js` is the template's render, and carries the same 13 bare
interpolations. Three arms of `tools/workflows/tier2-review.test.sh` assert the unquoted text, at
`53192a48d`: :725 (unit 37's `FH37` arm, `git -C C:/x/y`), :1164 and :2172 (`git -C /tmp/r`). Their
expected strings take the quoted form, the same assertions. Under the build folder, only this unit's
acceptance ledger is written. `tools/hooks/agent-cap.js` and the four prose carriers are not written:
S17 has nothing to cure, and S16's decision is `selected`.

### Alternatives rejected

- **Two batch units.** §4 "Why one batch unit".
- **Refuse a `repo` holding a space (S33).** Every caller whose checkout path holds one would fail;
  quoting keeps the path one argument.
- **State as a non-goal that a caller's checklist keeps the selection (S16).** It leaves the decision
  applying only to callers that pass none, where the carriers can say so for the cost of a grep.
- **Re-run units 33 and 34 at order 27.** Unit 33 and 34's own readings stay at their commits; one
  build-wide reading at the last order is the one that sees every unit.
- **Arm rows 8 and 9 again (S17).** Unit 37 §7's AC12 arm stages the `isDirectory()` and `JSON.parse`
  breaks over those rows; a second arm would copy it.

## 5. Production-readiness checklist

- security — S33 quotes a path pasted into shell commands and refuses the three characters a
  double-quoted bash string cannot hold literally; no new write path.
- perf / scale — two `git show` reads per declared constant and per modified file; one parse per
  attempt report; one `--for-diff` per `ungated` clone for S30.
- error / empty / loading states — every probe refuses by name: a registry entry dropped, a moved
  carrier, a void cell the evidence does not support, a report, result file or transcript gone.
- observability — each probe prints its population before its verdict.
- risks — a difference between the checker re-run and unit 35's recorded output stops the build
  rather than re-deciding; a deleted report reds S9 as not re-derivable, and so does a Workflow result
  file, which sits in the session's `tasks/` folder that no keep rule names (§8 F4).
- testing — scratch probes and fixtures per criterion; the §7 arm observed RED then GREEN at the close.
- migration — none for adopters beyond the harness's quoted `repo` and its refusal of three characters.
- user docs — none: the replay section is units 25 and 30's; there is no `help/` page (§3).

## 6. Acceptance criteria

`constants.py`, `markers.py`, `base.py` and `void.py` are the scripts of §4 and of units 33, 34 and 36
as §4 corrects them, and `attempts.py` is unit 35 §4's, each written under the pass's scratch
directory. A clone or fixture repository goes under `$TEMP/<short name>`. Unit 30's record is
`memory/builds/dFairHearing/build/2026-11-04-build-TOOL-dFairHearing-30-replay-verdict.md`, and its
kept clones are `$TEMP/f1s1` to `$TEMP/f4u1` and `$TEMP/f2s2`.

- **AC1** — When `python base.py .` runs at this unit's commit with `GATE_BASE` unset and prints `base
  <sha>`, `python constants.py . <sha>` prints `constants <n>` and no `->` line and exits 0, and
  `python markers.py . <sha>` prints `files <m>` and no `->` line and exits 0.
  Red when: a version value moved in any commit of the build, units 36 and 37 included.
  figure: `<n>` and `<m>` are DERIVED, as unit 33 AC1 and unit 34 AC1 derive them.
- **AC2** — When `python base.py .` runs at this unit's commit with `GATE_BASE` unset, its sha equals
  `git merge-base HEAD origin/main`. In a fixture made by `git clone --depth 1 file://<source>` of a
  two-commit repository, it exits 2 printing `shares no merge-base`. `git grep -n GATE_BASE` over
  `memory/builds/dFairHearing/build/2026-11-04-build-TOOL-dFairHearing-33-2-builder-return.md` and over
  `memory/builds/dFairHearing/build/2026-11-04-build-TOOL-dFairHearing-34-1-builder-return.md` prints at
  least one line each, naming `unset` or the value.
  Red when: the build-wide reading takes a base other than `base.py`'s, a shallow clone's refusal names
  only the not-ahead cause, or a builder return leaves the order-23 base unstated.
  fixture: a two-commit repository under `$TEMP/fsa` cloned to `$TEMP/fsb`, made by the probe and
  removed after it.
- **AC3** — When `python attempts.py <unit 30's record>` runs at this unit's commit, its `scored` and
  `void after cap` lines equal those unit 35's `## Scoring` section quotes. The staged tables are unit
  35 AC2's.
  Red when: unit 30's record, edited after unit 35's commit, no longer yields the attempts unit 35
  scored.
- **AC4** — When `python void.py <unit 30's record>` runs at this unit's commit, it prints one `agrees`
  line per attempt row, nine, and exits 0. Over a scratch copy whose record 1 `selected` attempt 1 void
  cell is changed to cite an outside read that line 1 of `agent-a24141d7921658b99.jsonl` in that run's
  folder does not hold, it exits 1 naming that row. Over one whose f1s1 row is relabelled `refused`, it
  exits 1 naming the report on disk. Over one whose f2s1 cell quotes a stated count other than 0, it
  exits 1 naming that row.
  Red when: a void cell the evidence does not support decides which attempt is scored.
  fixture: the record copies under the pass's scratch directory; the reports, Workflow result files
  and transcripts unit 30's record names, on disk.
- **AC5** — When `python attempts.py <unit 30's record>` runs, the clones unit 37's ledger grades on
  its AC11 line are exactly the eight its `scored` lines name, f2s1 not among them. It prints no
  `void after cap` line, and this unit's ledger states that branch empty, not counted as coverage.
  Unit 35 AC3's exit-3 case is unit 35's own since the fold.
  Red when: unit 37's ledger grades a clone the checker did not score, or omits one it did.
- **AC8** — When the S15 probe reads `tools/hooks/agent-cap.js` and `check-verifier-fanout.js`, neither
  holds a `MAX_LENSES` identifier. Scratch copies holding `` `x ${f({k: MAX_LENSES})}` ``,
  `` `${ {a:1}.a + MAX_LENSES }` `` and `` `${ `${MAX_LENSES}` }` `` each fail the probe, and copies
  holding `// see ${MAX_LENSES}` and `// MAX_LENSES was 6` each pass it.
  Red when: a nested interpolation passes as absent, or a line comment reds a correct build.
- **AC9** — When `grep -n "^\*\*The decision:" <unit 30's record>` prints one line naming `selected`,
  `git diff <this unit's parent> HEAD -- memory/guides/MERGE-BAR.md memory/guides/SESSION-KICKOFF.md memory/HYGIENE.md tools/memory-tree/HYGIENE.template.md`
  prints nothing.
  Red when: a carrier changes after a `selected` decision, or the record holds no decision line.
- **AC10** — When a scratch probe runs `tools/lib/resolve_kit_dir.py` and `resolveKitDir`, sliced from
  `tools/hooks/agent-cap.js` at this unit's commit, over unit 37's rows 8 and 9, the two print the same
  directory on each row, and `git diff <this unit's parent> HEAD -- tools/hooks/agent-cap.js` prints
  nothing.
  Red when: the port walks past a worktree's `.git` file or denies on a malformed receipt.
- **AC11** — When `constants.py` runs with `HEAD HEAD` as its two ends over a one-commit scratch
  repository under `$TEMP/fce` holding the govkit kit's Python modules, `tools/govkit/govkit.py` and its
  siblings, and no registry, it exits 2 naming `registry.toml`; over one under `$TEMP/fcf` holding no
  govkit kit, it exits 2 naming the import. In a clone under `$TEMP/fcd` that deletes
  `tools/roles/roles_lib.py` in one commit, `python constants.py <clone> HEAD~1 HEAD` exits 2 naming
  `roles`; with the clone's `tools/branch-reconcile/branch_reconcile.py` moved by `git mv` and its
  version line raised in one commit, it exits 2 naming `branch-reconcile`; and with that kit's registry
  entry removed in one commit, it exits 2 naming it. `python constants.py . <root> <root>`, where
  `<root>` is the commit `git rev-list --max-parents=0 HEAD` prints, exits 2 printing `no declared
  constant resolved at both ends`.
  Red when: any of the six exits 0 or 1, or prints a traceback.
  fixture: the clone under `$TEMP/fcd`, and the scratch repositories under `$TEMP/fce` and `$TEMP/fcf`,
  made by the probe and removed after it.
- **AC12** — When `python constants.py . 7d98741e3~1 7d98741e3` runs, it prints `absent branch-reconcile`
  and `absent roles` beside unit 33 AC2's two lines. `python constants.py . 0baf2e47a~1 0baf2e47a`
  prints `new branch-reconcile 1.0`. Each also prints `absent policy`, a kit added after the pin.
  Red when: an `absent` or `new` outcome is refused, dropped or misprinted.
  figure: the lines are PINNED, measured on 2026-10-23 at `7d98741e3` and `0baf2e47a`, and again on
  2026-11-04 at `53192a48d`.
- **AC13** — When `grep -cE "ls-files.{0,8}--literal-pathspecs" replay_scorer.py` runs in the
  workflows kit, it prints 0. Unit 37 AC5 counts the argv form that stands, and its arm holds the
  valid-path control.
  Red when: the spelling after the verb, which git refuses with exit 129, returns in string or argv
  form.
- **AC14** — When `<c36>` is the commit `git log --format=%H -1 --grep='^Pass: TOOL-dFairHearing-36$'`
  prints, `git ls-tree -r --name-only <c36>~1 | grep extract-arms.sh` prints `tools/lib/extract-arms.sh`
  alone and `git show <c36>~1:tools/lib/extract-arms.sh | grep -c "PASS (N assertions)"` prints a
  number above 0, so unit 36's AC6 held before unit 36 was built. The AC14 line of this unit's
  acceptance ledger then labels unit 36's AC6 `precondition` evidence, naming `TOOL-dFairHearing-36`.
  Red when: a criterion green at base is recorded as observing S8 and S9.
- **AC15** — When `grep -n -B12 "function deriveAddressKey" tools/workflows/tier2-review.template.js`
  runs, it prints the `function deriveAddressKey` line, and the comment it prints holds no `:1664` and,
  where it cites the instrument by line, holds `:1665-1666`.
  Red when: the grep prints nothing, which passed unit 37 AC15 vacuously.
- **AC16** — When `grep -c "^\*\*Serves:\*\*.*TOOL-dFairHearing-35"` runs over unit 30's record, it
  prints 1.
  Red when: the record does not bind to unit 35.
- **AC17** — When `memory/builds/dFairHearing/build/2026-11-04-build-TOOL-dFairHearing-30-ungated.py`
  runs with this unit's checkout as its orchestrating repository over each of `$TEMP/f1u1` to
  `$TEMP/f4u1`, with its record's range spelled `<base>..<head>` as `git rev-parse` prints the two ends
  of the record's `## The four records` row in full, its stderr's `<m> ungated` equals that record's
  `appended ungated` cell in unit 35's `## Scoring` table, and the first 12 hex digits of the sha256 of
  its stdout bytes equal that row's checksum; this unit's ledger then states `unchanged`. Where a row
  differs, the ledger names each `(ungated)` item that differs from the same run with a scratch
  extraction of `tools/memory-tree/` at `3cf918a65` as the orchestrating repository. Over a scratch
  copy of this unit's `tools/memory-tree/` whose `check_ungated` returns False, every row prints
  `0 ungated` and the comparison names it.
  Red when: the shipped function and the recorded set disagree with nothing recorded.
  figure: 38, 20, 53 and 75, and `668cc4180bb4`, `bffdbeb67415`, `6f166104d7ff` and `0f260b686f44`,
  are PINNED in unit 35's `## Scoring` section; on 2026-11-04 at `53192a48d` all four re-derived equal.
- **AC18** — When `git show --name-only --format= <c>` runs for each of unit 36's and unit 37's pass
  commits, `<c>` being the commit `git log --format=%H -1 --grep='^Pass: <unit>$'` prints, every path
  it lists is named on that unit's row that `grep -E "dispatch · item [0-9a-f]+ <unit> · reason "`
  prints over `memory/builds/dFairHearing/RUN.md`. Unit 37's row names its acceptance ledger record.
  Red when: a pass's recorded write set omits a record or a render its commit writes.
- **AC19** — When a scratch stub-agent run of `tools/workflows/tier2-review.js` is given `repo` as
  `C:/x y/z`, every captured prompt's `git -C` command names `"C:/x y/z"` in double quotes, and given a
  `repo` holding `$`, the call throws naming `$`. `grep -c 'git -C \${repo}'
  tools/workflows/tier2-review.template.js` prints 0.
  Red when: a path holding a space splits into two arguments, or an unquoted interpolation remains.

## 7. Gates

`agent-cap self-test` · `scratch-guard self-test` · `hook destinations self-test` · `verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `kit/dogfood doc parity` · `kickoff-manifest ratchet` · `recall floor` · `recall floor arms` · `workflow script syntax` · `kit version markers` · `govkit selfcheck` · `review-replay selftest` · `python resolver (behaviour + inline parity + idiom ban)` · `harness arms (fail branches armed or pinned)` · `testsuite counts (every bar self-test prints one)` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `policy fixtures`

New arm: tools/workflows/tier2-review.test.sh · covers AC19 · a stub run whose `repo` holds a space, and one holding `$`, staged against the harness at `TOOL-dFairHearing-37`'s commit `6d768c563`, today's, where all 13 `git -C ${repo}` interpolations are bare and no character of `repo` is refused · FLOOR_ASSERTIONS in that suite, 627 at `53192a48d`, raised by the arms added

AC10 takes no arm here: unit 37 §7's AC12 arm, rows 8 and 9 in the python resolver's behaviour suite,
already stages the `isDirectory()` and `JSON.parse` breaks it names.

## 8. Open questions

- **F1 — One batch unit or two (BUILD-METHOD M4, M6)?** Options: (a) one; (b) two, split by the units
  the minors land on. §4 shows S1 reads a file S33 writes, so no split clears M6 clause 2 while S1 runs
  last. RESOLVED (agent, 2026-10-23, delegated): (a), rung 3. widens: none · relaxes: none
- **F2 — Quote or refuse a `repo` holding a space (S33)?** Options: (a) quote every interpolation and
  refuse only `"`, `$` and a backtick; (b) refuse any whitespace or shell metacharacter. (b) fails every
  caller whose checkout path holds a space. RESOLVED (agent, 2026-10-23, delegated): (a), rung 3; it
  satisfies AC19 as (b) does and breaks no caller. widens: none · relaxes: none
- **F3 — Edit the prose carriers or state a non-goal (S16)?** Options: (a) on an `ungated` record, each
  carrier says the harness acquires its own checklist, reworded in unit 23 S45's form where it does
  not; (b) a non-goal stating that a caller's checklist keeps the selection. (a) satisfies the finding's
  consequence and reuses unit 23 S45's wording. RESOLVED (agent, 2026-10-23, delegated): (a), rung 3;
  the only governance carrier it can touch, `memory/HYGIENE.md`, is one unit 23 S45 already rewords
  in the same form. widens: none · relaxes: none
- **F4 — Where does `void.py` read an attempt's dead agents (S9)?** Options: (a) the Workflow result
  file unit 30's record names beside each clone, its `lensesDead` and `skepticsDead`; (b) the report's
  `Run integrity` prose. (b) is discarded because the nine reports spell that prose at least four ways
  (`5/5 lenses returned and 0 died`, `All 5 lenses returned and none died`, `Lenses: 5/5 returned, 0
  died`, `lenses 5/5 returned, 0 DIED`), so one grammar either reds a correct build on a spelling it
  does not read or reads loosely enough to pass a count it misreads. (a) is the harness's own
  structured return, and the record cites it for this part of the void rule. RESOLVED (agent,
  2026-11-04, delegated): (a), rung 3; its residual, that no keep rule names the result files, is
  stated in S9 and §5. widens: none · relaxes: none
- **F5 — Which reader decides that a report parses (S9)?** Options: (a) `parse_candidates`, imported
  from `tools/workflows/replay_scorer.py` and called as `measure_replay_experiment` calls it, parsed
  meaning rows and no error; (b) `replay_scorer.py --experiment` over a one-candidate scratch manifest,
  as rev-4 wrote. (b) is discarded because `check_experiment` applies its manifest, one-variable,
  known-record and case-evidence rules before it reads a report, so a one-candidate manifest can
  refuse for a cause that is not the report's parse, and a correct build reds or pads the manifest.
  (a) is the same call with nothing in front of it. RESOLVED (agent, 2026-11-04, delegated): (a),
  rung 3. widens: none · relaxes: none
- **F6 — Where is unit 36's AC6 labelled precondition evidence (S22)?** Options: (a) this unit's
  ledger, on its AC14 line, after AC14 re-reads unit 36's AC6 at unit 36's parent; (b) unit 36's
  acceptance ledger, observed here where it exists and recorded empty where it does not; (c) this unit
  writes unit 36's acceptance ledger. (b) is discarded by the charter's [gate] rule: unit 36 closed with
  no ledger, so its observation here is an empty population, never coverage. (c) is discarded by §4's
  write set, which writes only this unit's ledger under the build folder, and by [one-fact]: unit 36's
  ledger has one writer, the close its builder return names. RESOLVED (agent, 2026-11-04, delegated):
  (a), rung 3. widens: none · relaxes: none
- **F7 — What does AC17 compare (S30)?** Options: (a) the instrument's `<m> ungated` count and its
  stdout's sha256 prefix against the `## Scoring` row, the range spelled in full shas; (b) the
  `(ungated)` item names against the `checklist` of unit 30's `f<r>u1-args.json` files; (c) (a) with
  the range spelled short, as the record's table spells it. (b) is discarded because the args files sit
  in the session scratchpad, untracked, so the comparison would rest on a file no record pins. (c) is
  discarded because the checklist's first line carries the range as given: measured on 2026-11-04,
  every sha differs while the counts and the names agree, so it reds a correct build. RESOLVED (agent,
  2026-11-04, delegated): (a), rung 3; the record pins both values. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting the 19 MEDIUM and 16 LOW findings of the round-5 spec
  audit of specs 33 to 37 as one batch.
- rev-2 · 2026-11-03 · §7 · the leg line adds `policy fixtures`, whose guard §4's
  `tools/hooks/agent-cap.js` trips (fix brief 2026-11-03-prompt-TOOL-dFairHearing-27-sweep-fix-brief, item 1). §4 keeps the hook: unit 32's
  `resolveKitDir`, which S17 cures, lands there after unit 16.
- rev-2 · 2026-11-03 · S3 · S15 · S18 · S28 · S32 · S33 · §4 · §10 · re-cited at `9c1a2857a`:
  `resolve_compare_base` (:1502 to :1507), `renderLexedView` (:720 to :452), `govkit.Refusal` (:115 to
  its binding at :142 and its class in `upgrade_steps.py`), `resolve_entry_version_at`'s guard
  (:703-705 to :773-775), check 5c (:2222 to :1975), `diffCmd` (:1081 to :1318) and the two
  `git -C /tmp/r` arms (:766 and :1659 to :967 and :1912) (fix brief 2026-11-03-prompt-TOOL-dFairHearing-27-sweep-fix-brief, item 2).
- rev-2 · 2026-11-03 · §4 · the absence probe's reason for slicing re-grounded: since unit 16 the hook
  runs `main()` only as the entry point, and the probe slices because `renderLexedView` is not
  exported; the slice and its `ReferenceError` refusal are unchanged (fix brief 2026-11-03-prompt-TOOL-dFairHearing-27-sweep-fix-brief, item 2).
- rev-3 · 2026-11-03 · header · S1 · S17 · S31 · §4 · the header's order 26 to 28, above units 38
  and 39, now at 27; S1, S17, S31, §4 and the rejected alternative re-word the positions of units 30, 36 and 37
  to match (fix brief 2026-11-03-prompt-TOOL-dFairHearing-25-reorder-fix-brief, items 2 and 3).
- rev-4 · 2026-11-03 · S6 · S7 · S8 · S9 · S10 · S12 · S13 · S14 · S16 · S20 · §3 · §4 · §5 · AC3 ·
  AC5 · AC7 · AC13 · the items unit 35's scoring and unit 30's runs needed before they ran moved to
  those units (fix brief 2026-11-03-prompt-TOOL-dFairHearing-25-fold-fix-brief, items 2, 3 and 5; unit
  25 §8 F2). S6, S7, S8 and S21's checker grammar (ids 14, 21, 35 and 6) is carried by unit 35 S7 and
  §4, S6 keeping the re-run of AC3 and AC3 its staged tables moving to unit 35 AC2; S8's `failed`
  label by unit 30 S9 too; S9's reports and transcripts kept on disk (id 13) by unit 30 S10 and unit 35
  S9, S9 keeping the re-derivation; S10's unit-35 half (id 4) by unit 35 S8, AC5 keeping unit 37
  AC11's half; S12, S13 and S14's per-arm corrections (ids 15, 38 and 22) by unit 30 S7 and AC5, AC7
  leaving this spec and the README leaving §4's write set; S20's trap count (id 5) by unit 25 S9 and
  AC8, AC13 keeping the absence half. S16 is completion work after the decision. §3's edges on units
  30, 35 and 37 read rather than correct what moved.
- rev-5 · 2026-11-04 · S30 · §4 · AC17 · restated on `check_ungated` as it stands: unit 37 S15 changes
  no code, and unit 32's `fb755fa80` changed the sentence end after the orchestrating commit
  `3cf918a65` that computed the recorded set; the set is re-derived by unit 30's committed instrument
  with today's function and compared by count and checksum, with a staged `check_ungated` that admits
  nothing to show the comparison reds (fix brief 2026-11-04-prompt-TOOL-dFairHearing-40-fix-brief, item 1).
- rev-5 · 2026-11-04 · §8 · F7 · AC17's comparison recorded as a fork: the range in full shas, since a
  short range changes every checksum (fix brief 2026-11-04-prompt-TOOL-dFairHearing-40-fix-brief,
  items 1 and 5).
- rev-5 · 2026-11-04 · S15 · S34 · §4 · unit 37 closed with S9's two-pass reader, so S15 re-reads the
  absence rather than replacing that reader; the probe also slices `LITERAL_OPENERS`, which
  `checkLiteralOpen` reads, and `renderLexedView` and `module.exports` are re-cited (:452 to :448 and
  :910-913 to :906-909 at `53192a48d`) (fix brief 2026-11-04-prompt-TOOL-dFairHearing-40-fix-brief,
  items 2 and 4).
- rev-5 · 2026-11-04 · S17 · §4 · §7 · AC10 · unit 37's ledger records rows 8 and 9 agreeing, so the
  port's cure is dropped: `tools/hooks/agent-cap.js` leaves Files touched, AC10 asserts its empty diff,
  and the AC10 `New arm:` line is dropped as a copy of unit 37's AC12 arm, whose break no longer reds
  anything this unit changes (fix brief 2026-11-04-prompt-TOOL-dFairHearing-40-fix-brief, items 2 and 4).
- rev-5 · 2026-11-04 · S20 · AC13 · unit 37 AC5 counts the argv form at its rev-6, so S20 no longer
  says it observes an absence; AC13 keeps the absence and leaves the valid-path control to unit 37's
  arm (fix brief 2026-11-04-prompt-TOOL-dFairHearing-40-fix-brief, item 2).
- rev-5 · 2026-11-04 · S10 · AC5 · unit 35's checker named no `void after cap` pair, so that branch is
  stated empty in the ledger, and AC5 reds on a graded clone the checker did not score (fix brief
  2026-11-04-prompt-TOOL-dFairHearing-40-fix-brief, items 2 and 3).
- rev-5 · 2026-11-04 · S23 · unit 37's ledger records a comment citing no instrument line, so AC15's
  `:1665-1666` half has no population today; AC15 is unchanged (fix brief
  2026-11-04-prompt-TOOL-dFairHearing-40-fix-brief, item 2).
- rev-5 · 2026-11-04 · S31 · AC18 · restated over each order-26 pass commit's paths against its
  dispatch row: unit 36 committed no ledger and wrote into none, and both rows name the renders the
  build-index hook forces, which rev-4 called written by neither (fix brief
  2026-11-04-prompt-TOOL-dFairHearing-40-fix-brief, items 2 and 3).
- rev-5 · 2026-11-04 · S33 · §4 · §7 · `diffCmd` re-cited (:1318 to :1671) and the fold named at :253;
  the arms asserting the bare text are :725, :1164 and :2172 at `53192a48d`, unit 37's `FH37` arm among
  them, in place of :967 and :1912; the AC19 arm's staged break is named as `6d768c563`, today's
  harness (fix brief 2026-11-04-prompt-TOOL-dFairHearing-40-fix-brief, items 2 and 4).
- rev-5 · 2026-11-04 · S9 · §4 · §5 · AC4 · `void.py` reads the dead agents from each Workflow result
  file and the parse through `parse_candidates`; AC4's three staged copies are named against the
  record's own rows (fix brief 2026-11-04-prompt-TOOL-dFairHearing-40-fix-brief, item 3).
- rev-5 · 2026-11-04 · §8 · F4 · F5 · the two readers of S9 recorded as forks (fix brief
  2026-11-04-prompt-TOOL-dFairHearing-40-fix-brief, items 3 and 5).
- rev-5 · 2026-11-04 · S16 · §4 · AC9 · unit 35 decided `selected`, so the four prose carriers leave
  Files touched and AC9 reads the `selected` branch over all four (fix brief
  2026-11-04-prompt-TOOL-dFairHearing-40-fix-brief, item 3).
- rev-5 · 2026-11-04 · S11 · AC6 · dropped: unit 36 AC3 reads its suite by `git show 3708a705:` since
  its rev-3, and its builder return records 73 and 5 (fix brief
  2026-11-04-prompt-TOOL-dFairHearing-40-fix-brief, item 3).
- rev-5 · 2026-11-04 · S22 · AC14 · §8 · F6 · unit 36 closed with no acceptance ledger, so AC14
  re-reads unit 36's AC6 at unit 36's parent and this unit's ledger carries the label (fix brief
  2026-11-04-prompt-TOOL-dFairHearing-40-fix-brief, items 3 and 5).
- rev-5 · 2026-11-04 · §1 · S28 · S32 · units 33, 34 and 36 closed with no acceptance ledger, so this
  unit's ledger records each supersession (fix brief 2026-11-04-prompt-TOOL-dFairHearing-40-fix-brief,
  item 3).
- rev-5 · 2026-11-04 · S1 · S3 · AC2 · unit 36's commit edits no kit file; units 33 and 34 name
  `GATE_BASE` in their builder returns, which AC2 greps in place of ledgers that do not exist; the
  shallow fixture is cloned through `file://`, which a local `--depth` needs (fix brief
  2026-11-04-prompt-TOOL-dFairHearing-40-fix-brief, item 4).
- rev-5 · 2026-11-04 · S35 · §4 · `base.py`'s corrected tip refusal written out (fix brief
  2026-11-04-prompt-TOOL-dFairHearing-40-fix-brief, item 4).
- rev-5 · 2026-11-04 · AC11 · AC12 · §4 · the scratch root holds the govkit kit's modules and runs
  with `HEAD HEAD`, since `govkit.py` alone fails its import on `upgrade_steps`; AC12 names the
  `absent policy` line a later kit adds; both measured at `53192a48d` (fix brief
  2026-11-04-prompt-TOOL-dFairHearing-40-fix-brief, item 4).
- rev-5 · 2026-11-04 · S3 · S18 · S28 · S32 · §4 · §10 · re-cited at `53192a48d`, every line
  unchanged from `9c1a2857a`: `resolve_compare_base` :1507, `govkit.Refusal` :142 and :305, the guard
  :773-775, check 5c :1975 (fix brief 2026-11-04-prompt-TOOL-dFairHearing-40-fix-brief, item 4).
- rev-5 · 2026-11-04 · §6 · fixtures and clones spelled under `$TEMP`, and unit 30's record and its
  kept clones named once (fix brief 2026-11-04-prompt-TOOL-dFairHearing-40-fix-brief, item 4).
- rev-5 · 2026-11-04 · §3 · the consumes-from rows on units 30, 32, 36 and 37 name what this unit now
  reads (fix brief 2026-11-04-prompt-TOOL-dFairHearing-40-fix-brief, items 1 to 3).
- rev-6 · 2026-11-04 · header · §9 · `advances TOOL-dFairHearing-19` becomes `closes TOOL-dFairHearing-19`:
  this unit is the build's last in order, which the build's BACKLOG.md DEFERRED row, the README's rule 1
  and the ask's accept clause name as the header that closes the ask; with `advances`, the CLOSED flip
  drops the ask to OPEN (fix brief
  2026-11-04-prompt-TOOL-dFairHearing-40-closes-fix-brief, items 1 to 3).

## 10. Reuse audit

Every item extends a seam an earlier unit mints or the base tree carries: units 33, 34 and 36's scratch
probes corrected in place, govkit's readers (`read_descriptors`, `resolve_version_value_at`,
`derive_registry_path` and `blob_at` in `tools/govkit/govkit.py`), `resolve_compare_base`
(`tools/codebase-map/map_lib.py:1507`), unit 35's attempt checker, `renderLexedView`
(`tools/hooks/agent-cap.js:448`), both at `53192a48d`, `parse_candidates` in
`tools/workflows/replay_scorer.py`, unit 30's committed `ungated` instrument, and unit 23 S45's carrier
wording. `python tools/codebase-map/reuse_lookup.py "refuse a table row a parser recognises but cannot parse"`
ranked the generic `rows`, `row` and `parse` stems and no row-refusing reader, so no existing seam fits
the attempt-table refusal; it stays in the scratch checker. The recall query returned the audit's M3 and
M13 items, unit 35's checker, unit 36's `base.py`, and `DEPL-aHoistedPass-10` and
`TOOL-aBoundedVerdict-29`, two marker sites outside a gate's population, which S32's residual names.

Recall terms used: `python tools/memory-recall/query.py "a build-wide version check run once before later units edit kit files, and an attempt checker that drops rows" --terms "constants markers base.py resolve_compare_base attempts void after cap renderLexedView per-arm TEMP SCRATCH quoting repo"`
