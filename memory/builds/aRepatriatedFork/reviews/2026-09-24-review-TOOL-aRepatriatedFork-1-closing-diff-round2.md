**Serves:** diff-review DEPL-aRepatriatedFork-13 TOOL-aRepatriatedFork-2 TOOL-aRepatriatedFork-5 TOOL-aRepatriatedFork-6 TOOL-aRepatriatedFork-7 TOOL-aRepatriatedFork-10 TOOL-aRepatriatedFork-22

# aRepatriatedFork: Tier-2 closing diff review, round 2

*Node `a`, 2026-09-24. This round reviews ONLY the fold of round 1's findings. The round-1 record,
[round 1](2026-09-24-review-TOOL-aRepatriatedFork-1-closing-diff-round1.md), states every item's
defect and intended fix. Fold A closed B1, H1 and M1 (`.githooks/pre-push`, `tools/push-main.sh` and
their suites). Fold B closed M2, M3, M4 and residual e (`tools/govkit/`). Fold C closed L1, L2 and M5
(`tools/unattended/unattended.sh`, `check-unattended.sh` and their suites). Fold D closed L3, L4 and
residual b. The finders were asked two things. First, does each fix close its item, tried against the
round-1 repro and its nearest variants? Second, did the fold introduce a new defect? Only new issues
and round-1 items the fold did not close are reported.*

**Range reviewed: `e69bf51418324bf716d4d8a51de65b8caaf4c6a3...f1da97d3ca434894839d411fc008e2d034049b9e`**
(branch `branch/arepatriated-fork-build-e42158`).

**Round: 2.**

## Verdict: CLEAN WITH FIXES

No blocker or high survived. Round 1's BLOCKER (B1) and HIGH (H1) drew no confirmed finding against
the fold's bytes, although the finders tried the interpreter, path, quoting and git-dir channel
variants. One round-1 item is only partly closed. L2 scoped the driver's `fact` and the leg's
`fact_of` to `## Run facts`, but gate-guard.js and three shell readers still read the whole file. The
driver and the hook now disagree on a record the fold's own fixture builds, and that disagreement is
the MEDIUM item. The two LOW items are defects the fold introduced: a writer left unscoped beside its
newly scoped reader, and a refusal message whose advice the fold's own M1 arm now refuses. The tally
is 1 MEDIUM and 2 LOW items, covering 2 and 4 raw confirmed findings.

## Review shape and run integrity

- **Raw findings:** 15. Confirmed 6, refuted 9, unverified 0. **Precision 0.40** (6/15).
- **Adjudicated by item:** 3 items. BLOCKER 0, HIGH 0, MEDIUM 1, LOW 2.
- **Adjudicated by raw confirmed finding:** 6. BLOCKER 0, HIGH 0, MEDIUM 2 (ids 5, 8), LOW 4
  (ids 6, 9, 7, 11).
- **Run integrity:** lenses 4/4 returned, 0 died. Skeptic batches 5/5 returned, 0 died. 0
  contradictory verdicts were demoted to unverified, 0 spurious verdicts were discarded, and there
  were 0 duplicates at the verdict stage. The run is complete for this shape.
- **Duplicates merged at synthesis:** {6, 9} and {7, 11} are the same defect found by two lenses.
  Id 8 is merged into id 5's item because one fix closes both: scope gate-guard.js's `readFact`.
- **Precision note:** 0.40 is below the ~0.5 line §8 names. A fold review sits on a surface that was
  already hardened once, so refuted noise is the expected shape. The next round should narrow its
  lenses rather than add agents.

## What the fold closed

Round-1 items B1, H1, M1, M2, M3, M4, M5, L1, L3, L4, residual b and residual e drew no confirmed
finding in this round. All four lenses and all five skeptic batches returned, so that silence counts
as evidence for this lens set. It is not a proof of absence. L2 is the one item reopened below.

## MEDIUM

### M1. L2 is half-closed: gate-guard.js and three shell readers still take the first whole-file match (ids 5, 8)

- **Where:** the driver's `fact` at `tools/unattended/unattended.sh:743` is now scoped to
  `## Run facts`. These readers of the same keys are not:
  - `tools/unattended/gate-guard.js:594-599` (`resolveRunPhase`'s `readFact`, which reads `phase`,
    `run-branch` and `branch-ref` with a `^key: (.*)$` regex and the `m` flag)
  - `check-brief-recorded.sh` `CLAIM_AWK` at `:242-245` (base, phase, witness)
  - `lib-unattended.sh` `baseline_units` at `:691`
  - the driver's own `dod_met` greps at `unattended.sh:4488` and `:4498`
- **Defect:** before the fold, all readers were first-match over the whole file, so they agreed with
  each other. The fold moved one side, so the same question now gets two answers. This is the class
  L2 set out to remove.
- **Repro (the fold's own fixture):** `unattended.test.sh:2601` runs `sed -i '1a phase: LANDED'` on
  RUN.md and asserts that the driver reads RUNNING. On that record, gate-guard.js reads LANDED.
  LANDED is in `PHASES_ALLOW` (`gate-guard.js:98`), so `checkCommand` filters the record out and
  admits the commands the hook exists to deny. The driver keeps driving the run, and check 34 grades
  only the section, so it reports clean. Before the fold, the forged phase also made the driver
  refuse verbs on a "terminal" record, so the forgery at least cost the run something. Now it
  silently disables the hook and nothing else.
- **Second vector (id 8), the CR channel:** `--park`, `--propose`, `--rescope` and `--brief` refuse
  only LF (`wc -l`, at `unattended.sh:4965`, `5023`, `5404` and `5086`). `park()` appends the reason
  verbatim. JS treats CR as a line terminator under the `m` flag, so
  `--park --reason $'x\rrun-branch: refs/heads/other'` writes a line that gate-guard's
  `readFact('run-branch')` matches under `## Parked`. `readFact('run-branch') || readFact('branch-ref')`
  lets that forged value beat a genuine `branch-ref`, which is all most older records carry. The
  guard is then bound to another branch. The comment at `check-unattended.sh:2854`, which says no
  verb writes a key-shaped line outside the section any more, is false for CR.
- **DoD split:** on the aPacedTurnstile/aPromptedMandate shape, where `parked-surfaced:` sits under
  `## Attestations`, the whole-file grep at `:4498` passes. `fact` at `:4499` then returns empty, and
  the function returns 0 without running the surfaced-count comparison.
- **Fix:** scope every remaining reader the way `fact` is scoped. For `readFact` in gate-guard.js,
  copy run-lease.js's `FACTS_HEADING` slice (`run-lease.js:145`). For `CLAIM_AWK` and
  `baseline_units`, use an awk guard of the form `/^## Run facts/{s=1;next} /^## /{s=0} s&&...`. Make
  `dod_met` call `fact` instead of grep. Move the LF+CR refusal into `park()` itself, since every
  reason-carrying verb goes through it, instead of patching callers one at a time. The fold added CR
  to `--abort` and `--close` only.
- **Left-shift:** add a gate-guard arm to the L2 fixture. On the `1a phase: LANDED` record, assert
  that gate-guard.js still DENIES, and add a `\r run-branch:` park row asserting the binding does not
  move. Then gate the class. Add a structural leg in `check-unattended.sh` that enumerates every
  `^<key>:`-shaped read of a run-state file across `tools/unattended/` (sh, awk and js), and reds any
  read that does not route through `fact`, `fact_of` or a `FACTS_HEADING` slice. Stage an unscoped
  read to observe it go RED before landing it (§7).

## LOW

### L1. `set_fact` still writes whole-file while `fact` now reads only the section (ids 6, 9)

- **Where:** `tools/unattended/unattended.sh:3150-3156` (`set_fact`). The comment at `:738-742` says
  `## Run facts` is "the one section `set_fact` writes".
- **Defect:** `set_fact` tests `grep -q "^$k: "` over the whole file, and its awk rewrites every
  `k: ` line wherever it sits. It inserts under `## Run facts` only when no such line exists
  anywhere. The fold scoped the reader and not the writer, and the new comment claims a scope the
  code does not have.
- **Impact:** if a key exists only outside the section, `set_fact` rewrites that line and reports
  success, and the next `fact` read returns empty. Two concrete paths:
  - `verb_preflight`'s `[ -n "$(fact "$rel" base)" ] || set_fact "$rel" base "$base"`, followed by
    the re-read at `:3015`, leaves `base` empty.
  - `--attest parked-decisions-surfaced` (`verb_attest`, `:4736`) on a record shaped like
    aPacedTurnstile/aPromptedMandate rewrites the `## Attestations` line, which feeds the DoD split in
    M1.
  It needs a hand-edited or legacy-shaped record, hence LOW.
- **Fix:** give `set_fact` the same section bounds as `fact`. It should match and replace only
  between `## Run facts` and the next `## ` heading. When the section lacks the key, it should insert
  under the heading, even if a same-named line exists elsewhere.
- **Left-shift:** add a suite arm that puts `base:` only above the heading, runs `--preflight`, and
  asserts that `fact base` is non-empty afterwards. A pairing check belongs in the M1 structural leg
  too: any writer of run-state keys must share the reader's section bounds.

### L2. The refusal's "Sanctioned use" names a script that does not exist and that M1's arm refuses (ids 7, 11)

- **Where:** `.githooks/pre-push:577`, `:588` and `:598`. All three print
  `$knob='bash $GOV_KITROOT/unattended-bar.sh'`. The executed-word refusal at `:588` is new in this
  fold.
- **Defect:** `git ls-files` finds no `unattended-bar.sh`. The name came in from the NicoCares spec
  and exists here only as a fixture in `pre_push_bar_selftest.py`. Even if someone created and
  tracked it, the declared arm at `:606-612` accepts only `bash $GATE_RUNNER` or the GATE_CMD in the
  committed `.unattended.conf` (`_bar_decl`, set at `:536-538`). In gov that is
  `bash tools/run-gates/run-gates.sh`. The advice was harmless before M1, and the fold made it false.
- **Impact:** an operator who follows the printed remedy gets a second refusal. It is a message
  defect only.
- **Fix:** print the value that would actually pass: `$_bar_decl` when one is declared, otherwise
  `bash $GATE_RUNNER`. Change all three sites.
- **Left-shift:** add a selftest row in `.githooks/pre_push_bar_selftest.py` that extracts the
  "Sanctioned use" value from each refusal's stderr, feeds it back through `check_bar_command`, and
  asserts that it PASSES. Such a row cannot go stale against the arm, because it asks the arm.
