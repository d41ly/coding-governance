# TOOL-aBenchedProbe-2 — run-gates' held-count summary names its predicate

**Status:** CLOSED · rev-1 · 2026-10-09 · node a · Tier-1 · base 2b26f187 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-09-prompt-TOOL-aBenchedProbe-1-1-spec-brief.md](../prompts/2026-10-09-prompt-TOOL-aBenchedProbe-1-1-spec-brief.md) | journal | TOOL-aBenchedProbe-1 DEPL-aBenchedProbe-1 DEPL-aBenchedProbe-2 |
| [2026-10-09-prompt-TOOL-aBenchedProbe-1-2-build-brief.md](../prompts/2026-10-09-prompt-TOOL-aBenchedProbe-1-2-build-brief.md) | journal | TOOL-aBenchedProbe-1 DEPL-aBenchedProbe-1 DEPL-aBenchedProbe-2 |
| [2026-10-09-prompt-TOOL-aBenchedProbe-1.md](../prompts/2026-10-09-prompt-TOOL-aBenchedProbe-1.md) | research | TOOL-aBenchedProbe-1 DEPL-aBenchedProbe-1 DEPL-aBenchedProbe-2 |
| [2026-10-09-review-TOOL-aBenchedProbe-1-closing-diff-round1.md](../reviews/2026-10-09-review-TOOL-aBenchedProbe-1-closing-diff-round1.md) | diff-review | TOOL-aBenchedProbe-1 DEPL-aBenchedProbe-1 DEPL-aBenchedProbe-2 |

<!-- /gen:spec-records -->

## 1. Goal

The bar's closing summary says `(N held: every self-test, GATE_SELFTESTS=1 runs them)`. The runner
cannot know that: it holds a leg when `subject == kit` OR `chunk == selftests`, and an adopter's
manifest carries no chunk, so there a self-test declared `repo` runs while the summary claims every
self-test was held. This unit makes the line state the predicate the runner actually applied.

## 2. Scope (IN)

- **S1 — the one summary line.** In `tools/run-gates/run-gates.sh`, the line that appends the held
  count to `skipnote` (~3693 at BASE, verified 2026-10-09) prints
  `(${ondemands} held: subject kit or chunk selftests, GATE_SELFTESTS=1 runs them)`. No other line
  of the file changes. Observed by AC1, AC2.
- **S2 — its one reader moves in step.** The canary arm 3h3 in `tools/run-gates/run-gates.test.sh`
  (~1007 at BASE) greps the exact summary text; its expected string carries the new words. Observed
  by AC1.
- **S3 — no live copy of the old words survives.** Outside the memory tree, no tracked file spells
  the old parenthetical. Observed by AC3.

## 3. Non-goals (OUT)

- **The per-leg line.** `GATE held  <name>  (self-test, set GATE_SELFTESTS=1 to run)` (~2588) is a
  second, weaker form of the same claim. The owner's prompt says to edit only the summary line, so
  it stays; a follow-up may align it.
- **Every other region of `tools/run-gates/run-gates.sh`.** The concurrent run aThriftyLanding
  writes the stamp predicate, `GATE_REUSE` and the turnstile in this file. A one-line edit keeps the
  reconcile at landing to that line.
- **The hold predicate itself, and the verdict record.** The `held` row of the run record carries
  the count only; it does not change.
- **Review records quoting the old text.** They are history and stay as written.
- **The run-gates kit version bump and the kickoff manifest's `last-audit` re-stamp.** Both happen
  once at the build's close, because this file is staged.

### Edges

none

## 4. Design

### The words

The new parenthetical states the predicate in the vocabulary a reader of the manifest already has:
the two field names and their values, joined by `or`, which is the runner's `||` at ~2146. It keeps
the `N held:` head and the `GATE_SELFTESTS=1 runs them` tail, so a reader scanning for either still
finds it. It is true in gov, where 64 legs are held by that predicate, and in an adopter, where the
same predicate sees no chunk and holds by subject alone.

### Readers of the old text

`git grep -n "held: every self-test"` at BASE (2026-10-09) finds the runner line, the canary
expectation at `tools/run-gates/run-gates.test.sh` ~1007, and this build's own prompt records.
Searched for parsers of the summary in `.githooks/`, `tools/unattended/`, `tools/runlog/` and every
`*.py` and `*.js`: none reads its parenthetical. The `held` count travels to readers through the
verdict record's `held` row, which this unit leaves alone.

### The slice that observes the arm

The canary is the held `run-gates canary` leg, a suite of about 3200 lines whose leg ceiling is
13200 s, so a pass runs one arm instead (memory note "Slice a suite to debug one arm"). The slice is
lines 1 to the end of the `SCRATCH` fixture setup (through the `instant.sh` fixture, ~543), then
the 3h3 block (~973 to ~1039), then the file's last exit line. It must sit inside
`tools/run-gates/`, because the prologue resolves the runner from its own directory. It is named
`.slice-3h3.sh`, not `*.test.sh`, and is deleted before the commit and before any
`gen_map.py --write`, because the map extractor reads untracked shell files.

### Files touched (estimate)

- `tools/run-gates/run-gates.sh`
- `tools/run-gates/run-gates.test.sh`

### Alternatives rejected

- **Count held legs per cause** (`N held by subject, M by chunk`). Two figures need a second counter
  in the reporting pass, which is a second line of this file aThriftyLanding is editing around, and
  the owner asked for an accurate line, not a breakdown.
- **Drop the claim and print only `N held`.** Accurate but tells a reader nothing about why a leg did
  not run; the predicate is the useful half.

## 5. Production-readiness checklist

- security — N/A — output text only.
- perf / scale — N/A — no computation changes.
- error / empty / loading states — the line prints only when the held count is above 0, unchanged.
- observability — the point of the unit: the summary names the rule it applied.
- risks — a merge conflict with aThriftyLanding on this file; one line keeps it small.
- testing — the moved canary expectation, observed RED then GREEN through a slice (§6).
- migration — N/A.
- user docs — N/A — no `help/` page quotes the line.

## 6. Acceptance criteria

- **AC1** — When the 3h3 slice in §4, carrying the new expected text, runs with `bash` against the
  BASE runner line, its output carries
  `canary: the summary did not name the held population`; when it runs after S1, that line is
  absent and every other 3h3 assertion stays silent. Red when: the slice passes against the BASE
  line, which would mean the arm cannot fail, or still prints the line after S1.
  fixture: built from the suite at build time, deleted before commit; the tree holds none today.
  cost: seconds, against a 13200 s leg ceiling for the whole suite.
- **AC2** — When `git diff -U0 -- tools/run-gates/run-gates.sh` is read after the edit, it shows one
  removed and one added line, both the `skipnote` held-count line. Red when: any other line of the
  file differs from BASE.
- **AC3** — When `git grep -n "held: every self-test" -- ':!memory'` runs, it prints nothing.
  Red when: a runner, test or doc line outside the memory tree still spells the old words.

## 7. Gates

`run-gates canary` · `kit version markers` · `memory hygiene`

`python tools/check-spec-tokens.py --legs-for` owes no narrow leg for either path: `tools/run-gates/`
is a broad guard (run 2026-10-09). The bar at the close runs the held canary only under its owner's
on-demand switch.

New arm: tools/run-gates/run-gates.test.sh · covers AC1 · the BASE summary line, run through the 3h3 slice · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft, from the build's spec brief and the reader search in §4.

## 10. Reuse audit

No new code and no seam to extend: the unit rewrites one string and its one assertion.
`python tools/codebase-map/reuse_lookup.py "run-gates summary line naming the held leg count"`
returned only name-stem matches (`run`, `counts`, `legs`, `check_line`), none of which builds the
summary. Recall ranked `TOOL-aBoundedCeiling-10` (the earlier `kit self-tests` to `every self-test`
change at `325d5f55` left this canary pin stale, so the arm's expectation must move in the same
commit) and the `TOOL-dUnstalledConvoy-26` closing review, which first printed the held parenthetical.

Recall terms used: subject kit repo held selftests chunk GATE_SELFTESTS ondemand skipnote summary canary adopter descriptor
