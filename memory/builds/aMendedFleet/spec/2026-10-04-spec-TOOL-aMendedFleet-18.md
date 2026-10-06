# TOOL-aMendedFleet-18 — `tier2-review.js` prints one machine shape line with severity counts and output tokens

**Status:** CLOSED · rev-3 · 2026-10-04 · node a · Tier-1 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 18

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-06-review-TOOL-aMendedFleet-1-closing-diff-round1.md](../reviews/2026-10-06-review-TOOL-aMendedFleet-1-closing-diff-round1.md) | diff-review | KICK-aMendedFleet-1 KICK-aMendedFleet-2 KICK-aMendedFleet-3 KICK-aMendedFleet-4 PLAY-aMendedFleet-1 PLAY-aMendedFleet-2 PLAY-aMendedFleet-3 PLAY-aMendedFleet-4 TOOL-aMendedFleet-1 TOOL-aMendedFleet-2 TOOL-aMendedFleet-3 TOOL-aMendedFleet-4 TOOL-aMendedFleet-5 TOOL-aMendedFleet-6 TOOL-aMendedFleet-7 TOOL-aMendedFleet-8 TOOL-aMendedFleet-9 TOOL-aMendedFleet-10 TOOL-aMendedFleet-11 TOOL-aMendedFleet-12 TOOL-aMendedFleet-13 TOOL-aMendedFleet-14 TOOL-aMendedFleet-15 TOOL-aMendedFleet-16 TOOL-aMendedFleet-17 TOOL-aMendedFleet-19 TOOL-aMendedFleet-20 TOOL-aMendedFleet-21 TOOL-aMendedFleet-22 TOOL-aMendedFleet-23 TOOL-aMendedFleet-24 TOOL-aMendedFleet-25 TOOL-aMendedFleet-26 TOOL-aMendedFleet-27 TOOL-aMendedFleet-28 TOOL-aMendedFleet-29 TOOL-aMendedFleet-30 TOOL-aMendedFleet-31 TOOL-aMendedFleet-32 TOOL-aMendedFleet-33 TOOL-aMendedFleet-34 TOOL-aMendedFleet-35 TOOL-aMendedFleet-36 TOOL-aMendedFleet-37 TOOL-aMendedFleet-38 TOOL-aMendedFleet-39 TOOL-aMendedFleet-40 TOOL-aMendedFleet-41 TOOL-aMendedFleet-42 TOOL-aMendedFleet-43 TOOL-aMendedFleet-44 TOOL-aMendedFleet-45 TOOL-aMendedFleet-46 TOOL-aMendedFleet-47 TOOL-aMendedFleet-48 TOOL-aMendedFleet-49 TOOL-aMendedFleet-50 TOOL-aMendedFleet-51 TOOL-aMendedFleet-52 TOOL-aMendedFleet-53 TOOL-aMendedFleet-54 TOOL-aMendedFleet-55 TOOL-aMendedFleet-56 TOOL-aMendedFleet-57 TOOL-aMendedFleet-58 TOOL-aMendedFleet-59 TOOL-aMendedFleet-60 TOOL-aMendedFleet-61 TOOL-aMendedFleet-62 TOOL-aMendedFleet-63 TOOL-aMendedFleet-64 TOOL-aMendedFleet-65 TOOL-aMendedFleet-66 TOOL-aMendedFleet-67 TOOL-aMendedFleet-68 TOOL-aMendedFleet-69 TOOL-aMendedFleet-70 TOOL-aMendedFleet-71 TOOL-aMendedFleet-72 TOOL-aMendedFleet-73 TOOL-aMendedFleet-74 TOOL-aMendedFleet-75 TOOL-aMendedFleet-81 TOOL-aMendedFleet-82 TOOL-aMendedFleet-83 TOOL-aMendedFleet-84 TOOL-aMendedFleet-85 TOOL-aMendedFleet-86 TOOL-aMendedFleet-87 TOOL-aMendedFleet-88 TOOL-aMendedFleet-89 TOOL-aMendedFleet-90 TOOL-aMendedFleet-91 TOOL-aMendedFleet-92 TOOL-aMendedFleet-93 TOOL-aMendedFleet-94 TOOL-aMendedFleet-97 TOOL-aMendedFleet-98 TOOL-aMendedFleet-99 TOOL-aMendedFleet-100 TOOL-aMendedFleet-101 TOOL-aMendedFleet-102 TOOL-aMendedFleet-103 TOOL-aMendedFleet-104 TOOL-aMendedFleet-105 |

<!-- /gen:spec-records -->

## 1. Goal

Template §8 asks for a periodic re-audit of review cost against the severity-weighted value of what
the reviews confirmed, and no review record carries cost. The synthesis is told to state the review
shape near the top of its report, so each record words it differently, and no record says how many
output tokens the run spent. This unit renders ONE byte-stable `review-shape` line from the counts the
harness already holds plus the `budget.spent()` delta across the run, logs it, returns it on every
exit, and has the synthesis copy it verbatim into the record, so the cost-against-value audit becomes
a grep. Report `[B#23]`, brief unit 18.

## 2. Scope (IN)

- **S1** — A top-level pure function `renderShapeLine(fields)` in
  `tools/workflows/tier2-review.template.js` renders, in this fixed order and nothing else:

  ```
  review-shape kind=<diff-review|spec-audit> round=<n> intensity=<full|light> at=<find|verify|synth> raw=<n|-> confirmed=<n|-> refuted=<n|-> unverified=<n|-> blocker=<n|-> high=<n|-> medium=<n|-> low=<n|-> agents=<n> out-tokens=<n|unknown>
  ```

  A count the run has not produced at that stage is `-`, never `0`. The four severities count raw
  confirmed findings by their binding grade, `deriveBindingSeverity`; a grade outside the closed
  four is counted in none. `agents` follows the final return's own `agents` formula, finders plus
  batched skeptics plus the synthesis, through the stage reached: `lensesRunning` at `find`, plus the
  batch count at `verify`, plus 1 at `synth`. Only the final return carries an `agents` field, so the
  earlier stages take the formula, not a field. On the every-lens-dead exit `raw` is `-`: no lens
  returned, so the zero there was never produced. Observed by AC1.
- **S2** — A top-level function `readOutputTokens()` returns `budget.spent()` when the runtime's
  `budget` global exists and its `spent` is a function, and `null` otherwise. The script reads it once
  before its first agent call and again where it renders the line; `out-tokens` is the difference, or
  `unknown` when either read is `null`. Observed by AC2.
- **S3** — Every one of the script's five exit returns carries `shape`, the line rendered at that
  exit, and logs it as one line through `log`. The two returns before any skeptic render `at=find`,
  the two after the verify stage render `at=verify`, and the line handed to the synthesis renders
  `at=synth`, which the final return carries unchanged. Observed by AC3.
- **S4** — The synthesis prompt tells the agent to copy the `at=synth` line verbatim, alone on its
  own line, immediately above the appendix heading. Observed by AC4.
- **S5** — The kit README's return-field paragraph states the grammar, what `out-tokens` covers and
  what it cannot. Observed by AC5.
- **S6** — `memory/map/generated/symbols.json` is regenerated for the new
  definitions. NOT OBSERVED by a criterion here: `python tools/codebase-map/gen_map.py --check` at
  the close is its check, and §7 names the leg that reads it.

## 3. Non-goals (OUT)

- Replacing the prose "review shape" statement the synthesis already writes. A reader still wants it.
- The synthesis agent's own output tokens. The line is rendered before that agent runs, so the
  record's copy and the returned `shape` are byte-identical; including it would need a second line
  the agent could not copy.
- The adjudicated BLOCKER and HIGH counts the final return derives from the synthesis item list. Those
  stay in `blockers` and `highs`; the line counts raw confirmed findings by binding grade.
- A chat micro-format. The line is a record line, so it uses `key=value` fields and no head from
  template §16's closed set.
- Aggregating the lines across records, and the monthly escape ratio: unit 50.
- The bug-class column: `TOOL-aMendedFleet-17`, which edits the same template and builds first.

### Edges

none

## 4. Design

### Evidence

Read at base `7af5f564`, re-verified 2026-10-04 against the report's claim at `ac65de998`.

- No `budget.` read exists in `tools/workflows/tier2-review.template.js`. The runtime's `budget.spent()`
  returns the output tokens spent this turn across the main loop and every workflow, a shared pool, so
  only a delta isolates one run. `tools/workflows/orient-counterfactual.js` already measures exactly
  that delta around a spawn, and the kit README documents it.
- The synthesis prompt interpolates intensity, raw, confirmed, refuted, unverified and precision into a
  prose request to "state the review shape near the top"; records such as the dSpentCeiling review
  carry it as a hand-shaped table.
- The script has five exit returns, each with an `exit` field: two before any skeptic, two after the
  verify stage (every finding refuted, and a partial fan), and the final one after the synthesis.
- `tools/workflows/tier2-review.test.sh` evaluates the whole script with stub agents and defines no
  `budget`, which is why S2 reads it through a `typeof` guard rather than calling it.

### Why the line is rendered before the synthesis

The synthesis agent writes the record and the script cannot. A line rendered after the synthesis
cannot reach the record, and two lines, one per side, would disagree on `out-tokens` in every record.

### Inventory

- `renderShapeLine` and `readOutputTokens`, top-level so a `node` slice can evaluate each alone;
  `render` and `read` are the declared verbs. A name the lexicon leg refuses is replaced with its
  `--suggest` answer at build time, and this list is amended with a rev bump.
- `renderStageShape(at, counts, agents)`, the one caller of both: it fills the run's kind, round,
  intensity and token delta around a stage's counts, so the five exits do not each restate them.
  Not pure, so no criterion slices it; AC3 and the suite arm observe it through the exits.

### Files touched (estimate)

- `tools/workflows/tier2-review.template.js`
- `tools/workflows/tier2-review.js`
- `tools/workflows/README.md`
- `tools/workflows/tier2-review.test.sh` — the §7 arm, written in the pass and run at the close
- `memory/map/generated/symbols.json`

### Rollout

Additive. `REVIEW_SHAPE` does not move: it keys the reuse of lens files, and no lens or skeptic prompt
changes. Builds after `TOOL-aMendedFleet-17`, which writes the same template. The review-harness kit
version bump is owed once, at this build's close.

### Alternatives rejected

- **Count `blockers` and `highs` from the synthesis items on the line.** They exist only after the
  agent that writes the record has returned, so the record could not carry them.
- **Render with ` · ` separators and an em-dash head.** That is the chat micro-format grammar of
  template §16, whose head set is closed; a record line borrowing it reads as a new head.

## 5. Production-readiness checklist

- security — the line carries counts, enums and an integer; no agent text reaches it.
- perf / scale — two reads of a runtime counter and one string per exit.
- error / empty / loading states — an absent `budget` prints `out-tokens=unknown`; an unreached count
  prints `-`.
- observability — the line is the observation, logged, returned and recorded.
- risks — the pool is shared, so spend elsewhere in the same turn during the run inflates the delta.
  The README says so.
- testing — `node` slices of both functions, a count of exits against `shape` fields, and a new arm in
  the harness's own suite at the close.
- migration — none.
- user docs — the kit README's return-field paragraph, S5.

## 6. Acceptance criteria

- **AC1** — When `node -e` slices `renderShapeLine` out of `tools/workflows/tier2-review.js` and
  evaluates it over a fixture of a round-2 light diff review at `at=synth` with raw 9, confirmed 5,
  refuted 3, unverified 1, binding grades 1/2/1/1, 9 agents and 1234 tokens, it returns exactly the
  S1 grammar filled with those values; and over an `at=find` fixture it prints `-` for every count
  the find stage has not produced.
  Red when: a field is missing, reordered, renamed, or an unproduced count prints `0`.
- **AC2** — When `node -e` slices `readOutputTokens` and evaluates it once with no `budget` global and
  once beside a stub whose `spent()` returns 100, the first returns `null` and the second 100.
  Red when: the absent case throws or returns a number.
- **AC3** — When `grep -c -E "^\s+exit: "` and `grep -c -E "^\s+shape: "` run over
  `tools/workflows/tier2-review.js`, both print the same count, and that count is 5.
  Red when: an exit return carries no `shape`.
  figure: 5 is PINNED from the exits at base, 2026-10-04; a sixth exit raises both counts together.
- **AC4** — When `grep -n review-shape tools/workflows/tier2-review.js` runs, a line of the synthesis
  prompt tells the agent to copy the shape line verbatim, alone, immediately above the appendix
  heading.
  Red when: the prompt carries no such instruction.
- **AC5** — When `grep -n -E "review-shape|out-tokens" tools/workflows/README.md` runs, the
  return-field paragraph states the grammar, that `out-tokens` is a delta over a shared pool, and that
  it excludes the synthesis agent.
  Red when: either caveat is missing.

## 7. Gates

`workflow script syntax` · `review-protocol parity (kit vs dogfood)` · `tier2-review self-test` · `verifier fan-out self-test` · `unattended-build self-test` · `review-join self-test` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness`

New arm: tools/workflows/tier2-review.test.sh · each stubbed exit path asserts its return carries a `shape` matching the S1 grammar with the stage its path reaches, and `out-tokens=unknown` under the stub runtime · the suite's assertion floor rises by the arms added

## 8. Open questions

- **F1 — Which severity counts does the line carry?**
  Options: the synthesis's adjudicated item counts; raw confirmed findings by binding grade. Only the
  second exists before the agent that writes the record runs.
  RESOLVED (agent, 2026-10-04, delegated): raw confirmed findings by binding grade.
- **F2 — How does the line reach a committed record?**
  Options: the caller appends the returned `shape`; the synthesis copies it, as it already copies the
  appendix. No caller writes the record today, and the copy rides an instruction that already works.
  RESOLVED (agent, 2026-10-04, delegated): the synthesis copies it, and every exit also returns it.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the five exit returns and the synthesis prompt at base.
- rev-2 · 2026-10-04 · §2 S6 · §4 · §7 · M2 cross-read: the definitions this unit adds
  move `memory/map/generated/symbols.json`, which `TOOL-aMendedFleet-82` and the build's other
  code units regenerate and declare; this spec omitted the write, its Files touched row and the leg.
- rev-3 · 2026-10-05 · §2 S1 · §4 Inventory · build-time: S1 said `agents` is the value the return's
  own field carries at each stage, and four of the five exits carry no `agents` field, so S1 now
  names the formula per stage; it also fixes `raw=-` on the every-lens-dead exit and leaves an
  off-vocabulary grade uncounted. The inventory adds the `renderStageShape` helper the five exits
  share; the lexicon's `--suggest` answered OK for all three names. Files touched gains the suite,
  which §7's new arm writes and the estimate omitted.

## 10. Reuse audit

The seams extended are the five exit returns and the synthesis prompt in
`tools/workflows/tier2-review.template.js`, with `deriveBindingSeverity` for the grades, and the
`budget.spent()` delta that `tools/workflows/orient-counterfactual.js` already takes around a spawn.
`python tools/codebase-map/reuse_lookup.py "print one machine-readable summary line of a review's
severity counts and token cost"` returned only generic readers such as `read_text` and `read_journal`,
so no existing seam renders a review summary line. Recall returned the batching decision
`TOOL-aBatchedTribunal-1j`, whose token figures were measured by hand, and the dSpentCeiling review's
hand-shaped table, which is the variance this line removes. The report said no record carries cost;
the tree agrees at base.

Recall terms used: tier2-review shape line severity counts output tokens budget.spent cost review record precision agents micro-format
