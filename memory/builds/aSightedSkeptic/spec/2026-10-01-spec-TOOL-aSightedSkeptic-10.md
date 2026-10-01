# TOOL-aSightedSkeptic-10 — discharge the two Observed-by claims no arm reads, and record the class

**Status:** CLOSED · rev-1 · 2026-10-01 · node a · Tier-2 · base ef1dcdb6 · streams tooling · order 10 · ratified 2026-10-01

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-01-build-TOOL-aSightedSkeptic-1-runlog-54774e91.md](../build/2026-10-01-build-TOOL-aSightedSkeptic-1-runlog-54774e91.md) | journal | TOOL-aSightedSkeptic-1 TOOL-aSightedSkeptic-2 TOOL-aSightedSkeptic-3 TOOL-aSightedSkeptic-4 TOOL-aSightedSkeptic-5 TOOL-aSightedSkeptic-6 TOOL-aSightedSkeptic-7 TOOL-aSightedSkeptic-8 TOOL-aSightedSkeptic-9 |
| [2026-10-01-build-TOOL-aSightedSkeptic-10-1-acceptance-ledger.md](../build/2026-10-01-build-TOOL-aSightedSkeptic-10-1-acceptance-ledger.md) | journal | — |
| [2026-10-01-prompt-TOOL-aSightedSkeptic-10-1-spec-brief.md](../prompts/2026-10-01-prompt-TOOL-aSightedSkeptic-10-1-spec-brief.md) | journal | — |
| [2026-10-01-prompt-TOOL-aSightedSkeptic-10-2-build-brief.md](../prompts/2026-10-01-prompt-TOOL-aSightedSkeptic-10-2-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The closing review's round 1 confirmed two HIGH findings of one class: a spec scope item says a
behaviour is "Observed by ACn", the arm that criterion names never reads the surface the behaviour
renders on, and a staged break of the behaviour leaves the suite green. This unit adds the arms that
read those surfaces, each observed red against the break the review names, and files the class in
the bug-class catalogue so the next spec citing a criterion for a separately rendered surface is
handed it.

## 2. Scope (IN)

- **S1** — Closing review finding H1, synthesis-death half. In `tools/workflows/tier2-review.test.sh`,
  one stub run with the synthesis dead and every skeptic batch confirming at severity `blocker` with
  `fixVerdict` `unsound` and a non-empty `fixNote` carrying a unique marker. Two assertions over its
  log lines that open `  CONFIRMED [`: exactly five lines, each opening `  CONFIRMED [blocker] `
  (spec 6 S9); and the same five lines each carrying `REJECTED` and the note marker and none carrying
  `NOT JUDGED` (spec 2 S6). Observed by AC1 and AC2.
- **S2** — Closing review finding H1, deferred half. One stub run with skeptic batch `verify:ids-2-2`
  dead and every other batch confirming at `blocker`. One assertion: exactly four log lines open
  `  CONFIRMED [`, and each opens `  CONFIRMED [blocker] ` (spec 6 S9). Observed by AC3.
- **S3** — Closing review finding H2, mixed half. One stub run where batch `verify:ids-3-3` answers
  `uncertain` and the rest confirm. One assertion that the return's `note` starts
  `PARTIAL: 1 finding(s) are unverified — 1 answered uncertain by a skeptic, 0 with no usable verdict`,
  the synthesis prompt's RUN INTEGRITY block carries
  `1 answered UNCERTAIN by a skeptic, 0 with NO usable verdict`, a log line opens
  `WARNING: 1 finding(s) answered UNCERTAIN`, and no log line carries `with NO usable verdict` (spec 6
  S8). Observed by AC4.
- **S4** — Closing review finding H2, all-uncertain half. One stub run where every batch answers
  `uncertain`. One assertion that `uncertain` and `unverified` are both 5, and `note` carries
  `none confirmed or refuted` and `5 answered uncertain by a skeptic, 0 with no usable verdict` and
  does not carry `none judged` (spec 6 S8). Observed by AC5.
- **S5** — `FLOOR_ASSERTIONS` in the same file rises by five, the assertions S1 to S4 add, over the
  value the file holds when this unit's build pass begins, with a `RAISED` comment line in the shape
  the earlier units wrote. Observed by AC6.
- **S6** — A new class record under `memory/gotchas/`, observed-by-claim-no-arm-discharges.md, in
  the catalogue's front-matter shape (`name`, `description`, `kind: class`, `universal: false`), whose
  derived anchors are exactly three, and the catalogue index re-rendered. Observed by AC7 and AC8.
- **S7** — No harness change: `tools/workflows/tier2-review.template.js` and its render are not edited.
  Observed by AC9.

## 3. Non-goals (OUT)

- Any edit to `tools/workflows/tier2-review.template.js` or `tools/workflows/tier2-review.js`. The
  behaviour both findings name is correct at the base of this unit, read at the line ranges §4 cites.
  If an arm is red at the pass's tip with no break staged, the template is wrong after all: the pass
  stops, records the arm, the failing line and the template line as a new §8 item with a rev bump,
  and does not change the template.
- The machine gate the review proposes for the class, a spec-ledger check that each "Observed by ACn"
  S-line names an arm whose assertions mention the S-line's output surface. Nothing in the tree joins
  an acceptance label to an arm's assertions, and building that join is a new checker. The class
  record says so (S6), which is the left-shift the review's "Short of that" clause names.
- Re-auditing the other "Observed by" claims of specs 1 to 9. The closing review CONVERGED over them,
  and M4 makes a converged subject terminal. See §8 F2.
- The closing review's MEDIUM and LOW findings, including L3 (findings 16 and 19, two correct guards
  with no arm) and M5 (the `sound` and `none` fix-verdict branches). The round-1 fold brief owns them.
- Rewording an existing arm. The AC3 arms of specs 2 and 6 and the AC5 arm of spec 6 keep their names
  and assertions; this unit's assertions are new `ck` calls, so the floor moves by what was added.

### Edges

- **consumes-from** `TOOL-aSightedSkeptic-2` — `renderFixLine` on the synthesis-death log path and the `REJECTED` wording an unsound fix with a note renders; S1's second assertion reads it.
- **consumes-from** `TOOL-aSightedSkeptic-6` — `deriveBindingSeverity` on both CONFIRMED log paths, the `uncertain` verdict, and the uncertain count kept apart from the no-verdict count in the note, RUN INTEGRITY and the log; S1 to S4 read them.

## 4. Design

### Evidence

Read at the run branch's tip on 2026-10-01, which carries units 1 to 9 over base `ef1dcdb6`. Line
numbers are PINNED to that reading and will move under the round-1 fold; the builder locates each by
the quoted text, not the number.

| Surface | Template line | What renders it |
|---|---|---|
| synthesis-death CONFIRMED log | 1353 | `[${deriveBindingSeverity(f)}]`, then `${renderFixLine(f)}` after a pipe |
| deferred-path CONFIRMED log | 1094 | `[${deriveBindingSeverity(f)}]`, no fix |
| uncertain WARNING log | 976 | `WARNING: ${uncertainFindings.length} finding(s) answered UNCERTAIN` |
| RUN INTEGRITY unverified clause | 1171 | `answered UNCERTAIN by a skeptic, ${noVerdict.length} with NO usable verdict` |
| success `note`, judged-zero arms | 1404–1407 | `judged === 0 && !uncertainFindings.length` selects "none judged" |
| success `note`, PARTIAL arm | 1409 | `answered uncertain by a skeptic, ${noVerdict.length} with no usable verdict` |

An all-uncertain round reaches the success `note`: the early return at `confirmed.length +
unverified.length === 0` does not take it, and the stub synthesis places no id, so no tally fault
pre-empts the judged-zero arms.

### Data model

The arms reuse the self-test's stubs: `buildStubs`, `buildGradedVerdicts`, `buildFixVerdicts`,
`buildFixLens` and `scanConfirmedEntries`, all defined inside `runWholeScriptArms`. S1 needs a skeptic
stub confirming at `blocker` with an unsound fix and a note. It is one const helper, named
`buildRejectedVerdicts` (lexicon cell `js.function`, checked with `--suggest`: leads with `build`),
composing `buildFixVerdicts('unsound', <marker>)` and setting `severity` on each verdict. S1 uses
`buildFixLens` so the finder's fix carries a marker distinct from the note.

The block is headed `// ==== TOOL-aSightedSkeptic-10` and sits inside `runWholeScriptArms`, after the
unit 7 block and before `await runLedgerArms()`, where every helper above is in scope. Each `ck`
message opens `observed-by: ` so the five are countable by one grep.

| Arm (`ck` message) | Stubs | Staged break that must turn it red |
|---|---|---|
| `observed-by: a dead synthesis logs every CONFIRMED finding at its binding grade` | `synth: null`, `find:` `buildFixLens`, `verify:` `buildRejectedVerdicts` | line 1353's `deriveBindingSeverity(f)` replaced by `f.severity` |
| `observed-by: a dead synthesis logs every CONFIRMED finding's fix through renderFixLine` | the same run | line 1353's `renderFixLine(f)` replaced by `f.fix` |
| `observed-by: a dead skeptic batch logs every CONFIRMED finding at its binding grade` | `verify:` confirming at `blocker`, `verify:ids-2-2: null` | line 1094's `deriveBindingSeverity(f)` replaced by `f.severity` |
| `observed-by: one uncertain answer is counted apart from no verdict in the note, RUN INTEGRITY and the log` | `verify:ids-3-3` answering `uncertain` | line 1171's and line 1409's `noVerdict.length` replaced by `unverified.length` |
| `observed-by: an all-uncertain round never reads as none judged` | every `verify:` answering `uncertain` | `&& !uncertainFindings.length` deleted from line 1404 |

Each arm asserts an exact count of the lines or values it reads before asserting their content, so a
run that rendered none of them is red rather than vacuously green (the zero-guard class,
`memory/gotchas/fixture-passes-by-finding-nothing.md`).

The class record follows the catalogue's shape: front matter, then `## Symptom`, `## Where it bit`
(this build's closing review, findings 13 and 14, cited by path in plain text so it derives no
anchor), `## The fix` (stage the break of the S-line's own surface and watch the cited arm, never read
the arm and agree), `## Related` (`criterion-asserts-what-its-own-command-cannot-show` is the
criterion-level sibling; `fixture-passes-by-finding-nothing` is the test-level one), and `## Its gate`
opening "No machine gate" with the reason §3 gives. Its body backticks exactly three path-like tokens,
and no other, because each one is an anchor `gotchas.py` derives:

| Anchor | What it selects, and why |
|---|---|
| `/spec/` | every spec file, the surface where an "Observed by" claim is written; the fold-text record uses the same token for the same reason |
| `tools/workflows/tier2-review.test.sh` | the self-test where this instance bit, and where most arms citing spec criteria in this repo's review harness live |
| `memory/TEMPLATE-SPEC.md` | the scope-join rule itself, whose grader reads SHAPE only and is where the gap is stated |

### Inventory

One identifier is minted: `buildRejectedVerdicts`, a const-bound arrow in the self-test, cell
`js.function`. One record name: `observed-by-claim-no-arm-discharges`.

### Rollout

The build pass writes the five assertions and the floor, then observes each arm red: a scratchpad
script slicing the suite's runner to the new block, run against a copy of the template with the
table's break applied and the render regenerated by `bash tools/workflows/check-protocol-parity.test.sh --render`,
then `git checkout -- tools/workflows/tier2-review.template.js tools/workflows/tier2-review.js` and a
clean `git status` before the next break. The same slice at the tip with no break staged passes. It
then writes the class record, runs `python tools/memory-tree/gotchas.py --write`, and commits once.
The suite itself runs once, at VERIFYING, in the main loop.

### Files touched (estimate)

`tools/workflows/tier2-review.test.sh` · `memory/gotchas/` · `memory/gotchas/INDEX.md` · this spec (status)

### Alternatives rejected

- **Extend `criterion-asserts-what-its-own-command-cannot-show` instead of a new record (§8 F1).** That
  record's three forms are about a criterion that cannot fail. Here every cited criterion CAN fail, for
  its own surface; the defect is the scope item's join to it. Its anchors, `tools/check-spec-tokens.py`
  and `tools/check-testsuite-counts.sh`, do not select the self-test or a spec file, so the class would
  not reach the checklist that needs it without re-anchoring a record whose other forms do not belong
  there.
- **Fold the new assertions into the existing AC3 and AC5 arms.** It reaches the same surfaces, but
  the floor cannot move by what was added, the arm names stop describing what they read, and a red
  arm no longer says which surface broke.

## 5. Production-readiness checklist

- security — N/A: test arms over stub agents and one markdown record; no input crosses a boundary.
- perf / scale — four more stub runs of the harness inside one node process, each well under a second
  on the existing runner; the suite's declared ceiling is not approached.
- error / empty / loading states — every arm asserts an exact count of what it reads, so a run that
  rendered nothing is red, not green.
- observability — each `ck` message names its surface; a red arm says which line broke.
- risks — the round-1 fold rewrites `renderFixLine`'s unsound wording (fold M3). S1's second assertion
  reads `REJECTED`, which the fold keeps because spec 2's own AC3 and AC4 arms assert it; if the fold
  drops it, those arms and this one move together.
- testing — the five assertions of S1 to S4, each observed red against its staged break.
- migration — N/A: no data, no shipped behaviour changes.
- user docs — N/A: no `args` field or user-facing behaviour changes.

## 6. Acceptance criteria

- **AC1** — Arm `observed-by: a dead synthesis logs every CONFIRMED finding at its binding grade`
  passes, and is red when the synthesis-death log line prints `f.severity` instead of
  `deriveBindingSeverity(f)`.
  Red when: any of the five synthesis-death CONFIRMED lines opens with `[high]`, or fewer than five
  are logged.
  permission: the suite is not run in a pass; the pass observes red and green by the scratchpad slice
  §4 Rollout names, and the main loop reads the pass at VERIFYING.
- **AC2** — Arm `observed-by: a dead synthesis logs every CONFIRMED finding's fix through renderFixLine`
  passes, and is red when that log line prints `f.fix` instead of `renderFixLine(f)`.
  Red when: a synthesis-death CONFIRMED line lacks `REJECTED` or the note marker, or carries
  `NOT JUDGED`.
  permission: as AC1.
- **AC3** — Arm `observed-by: a dead skeptic batch logs every CONFIRMED finding at its binding grade`
  passes, and is red when the deferred-path log line prints `f.severity` instead of
  `deriveBindingSeverity(f)`.
  Red when: any of the four deferred CONFIRMED lines opens with `[high]`, or a count other than four
  is logged.
  permission: as AC1.
- **AC4** — Arm `observed-by: one uncertain answer is counted apart from no verdict in the note, RUN INTEGRITY and the log`
  passes, and is red when the RUN INTEGRITY clause and the PARTIAL note interpolate
  `unverified.length` where they read `noVerdict.length`.
  Red when: the note or RUN INTEGRITY reads `1 with no usable verdict`, the uncertain `WARNING:` line
  is absent, or a no-verdict `WARNING:` line appears.
  permission: as AC1.
- **AC5** — Arm `observed-by: an all-uncertain round never reads as none judged` passes, and is red
  when `&& !uncertainFindings.length` is deleted from the judged-zero arm of the success `note`.
  Red when: the note reads `none judged`, or `uncertain` is not 5.
  permission: as AC1.
- **AC6** — When `grep -c "'observed-by: " tools/workflows/tier2-review.test.sh` and
  `grep -n "^FLOOR_ASSERTIONS=" tools/workflows/tier2-review.test.sh` run at the pass's commit, the
  first prints 5 and the second prints a value five above the same grep at the pass's parent commit.
  Red when: an assertion is missing, or the floor did not move by five.
  figure: both numbers are DERIVED at observation time; the parent's floor is read, not pinned here,
  because the round-1 fold may raise it first.
- **AC7** — When `python tools/memory-tree/gotchas.py --for-paths tools/workflows/tier2-review.test.sh`
  and `python tools/memory-tree/gotchas.py --for-paths memory/builds/aSightedSkeptic/spec/2026-10-01-spec-TOOL-aSightedSkeptic-6.md`
  run, each lists `observed-by-claim-no-arm-discharges`, and
  `python tools/memory-tree/gotchas.py --report` lists it with `3 anchor(s)`.
  Red when: either path does not select the record, or it derives more or fewer than three anchors.
- **AC8** — When `python tools/memory-tree/gotchas.py --check` runs it exits 0, and
  `python tools/memory-tree/gotchas.py --declares` over the new record prints `declares: yes`.
  Red when: the index was not re-rendered, or the record neither names a gate nor says it has none.
- **AC9** — When `git diff --stat HEAD~1 HEAD -- tools/workflows/tier2-review.template.js tools/workflows/tier2-review.js`
  runs at the pass's commit, it prints nothing.
  Red when: the pass edited the harness or its render.

## 7. Gates

`tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `review-replay selftest` · `verifier fan-out self-test` · `memory hygiene` · `recall floor` · `recall floor arms`

New arm: tools/workflows/tier2-review.test.sh · stub runs with the synthesis dead, one skeptic batch dead, one batch uncertain and every batch uncertain, each against the template line §4's table names · FLOOR_ASSERTIONS rises by 5

The class record has no arm of its own: `gotchas.py --check` grades its shape, and the `memory hygiene`
leg runs that check at the close.

## 8. Open questions

- **F1 — Is the left-shift a new class record, or an extension of an existing one?** (a) A new record,
  anchored on the spec directory, the self-test and the spec template. (b) A fourth form in
  `criterion-asserts-what-its-own-command-cannot-show`, re-anchored. §4 Alternatives rejected records
  why (b) loses: its three forms are a criterion that cannot fail, its anchors do not reach the paths
  this class bites on, and re-anchoring it puts unrelated forms on those checklists. Recommendation (a).
  RESOLVED (agent, 2026-10-01, delegated): (a), which is also the shape the spec brief names.
- **F2 — Does this unit discharge only H1 and H2, or every "Observed by" claim specs 1 to 9 make?** The
  build README's roster row for this unit reads as the second. (a) H1 and H2, the claims the review
  confirmed false, by staged breaks of the surfaces it names. (b) A staged break per "Observed by"
  S-line across all nine specs. (b) re-opens the closing review's subject, which CONVERGED, and M4 makes
  a converged subject terminal, so it is not an option the delegation offers; the spec brief also
  scopes the unit to H1 and H2. Recommendation (a).
  RESOLVED (agent, 2026-10-01, delegated): (a); the roster row's wording is the caller's to align.

## 9. Revision log

- rev-1 · 2026-10-01 · initial draft, from the closing review round 1 (H1 and H2), the unit's spec
  brief, the shared spec brief's invariants, and the harness template and self-test read at the run
  branch's tip over base `ef1dcdb6`.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "a test arm that stages a break of a rendered log line and asserts the line"`
and the same with "review harness self-test stub agents" ranked name-stem neighbours only (`armed`,
`log_path`, `build_self_chain`, `derive_review_exit`) and the run-gates and backlog seams, none of
which drives the review harness; the probe also prints `unscanned layers: .sh`, so it cannot see the
self-test's embedded runner. No existing seam fits outside the self-test itself, which is the seam this
unit extends: `runReview`, `buildStubs`, `buildGradedVerdicts`, `buildFixVerdicts`, `buildFixLens` and
`scanConfirmedEntries` in `tools/workflows/tier2-review.test.sh`, read directly. The recall probe
returned the closing review itself, this unit's brief, and the neighbouring class records
`fixture-passes-by-finding-nothing` and `vacuous-selector-empty-population`; a grep of
`memory/gotchas/` for "Observed by" found no record of this class, and the nearest sibling is weighed in
§8 F1.

Recall terms used: Observed-by scope-join acceptance arm staged break could-not-fail fixture vacuous self-test FLOOR_ASSERTIONS left-shift gotcha verification

The question passed with them: "is there a record for a spec claim that an acceptance arm observes a
behaviour the arm never exercises".
