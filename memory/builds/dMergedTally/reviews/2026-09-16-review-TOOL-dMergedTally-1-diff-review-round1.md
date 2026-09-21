**Serves:** diff-review TOOL-dMergedTally-1

# dMergedTally — closing diff review, round 1

*Node `d`, 2026-09-16, on `branch/eager-gagarin-7a8cc8`. Tier-2, run as direct agents rather than
through `tier2-review.js`, because the session held no opt-in for the `Workflow` tool: three primed
finder lenses in one wave, one batched skeptic prompted to refute, and this synthesis, written by the
orchestrating session. Four agents in all.*

**Reviewed range:** `4cf0944dbdce94714870f26760936bc5edabc64e...ff8f1a4c` — ROUND 1.

## Verdict: CLEAN WITH FIXES

Two findings were confirmed, both in the regression arms and neither in the fix. The test double for
the synthesis returned `items` whatever schema the callee declared, so reverting the schema and the
prompt left every arm green. And the path where nothing is confirmed and everything is unverified,
whose counts are now derived rather than typed, had no arm. Both are folded as spec rev-2. Fourteen
findings were refuted, one of them reported twice.

## Review shape

- Lenses: correctness, integration seams and contract, test validity.
- Raw findings **16**, confirmed **2**, refuted **14**, unverified **0**, precision **0.13**.
- Precision is far below the 0.5 floor `AGENTS.md` section 8 sets. Two causes are visible. The lenses
  were told what was known and still re-derived consequences the brief had accepted: the raw-count
  design was one of the two the owner offered. And the test-validity lens reported mutations that no
  plausible edit produces. A narrower brief naming the accepted design as by-design is the retune.
- Adjudicated: **0 BLOCKER, 0 HIGH, 1 MEDIUM, 1 LOW**. No finding merges another, so the tally by item
  and by raw finding agree.

## Run integrity

- Lenses: **3 of 3** returned, **0 died**.
- Skeptic batches: **1 of 1** returned, **0 died**.
- Verdicts: **16** for 16 findings, **0** contradictory, **0** spurious. Duplicates judged by the
  skeptic: C1 and S1 are one finding; C4 and T4 are two sides of one note-ordering choice.

## Confirmed

### M1 · MEDIUM · lens T1 — the synthesis double ignores the schema

`tools/workflows/unattended-build.test.sh`, the synthesis double in `build_merged_returns`. The
agent stub returned the doubled value whatever `opts.schema` required, and no arm read the synthesis
prompt. Reverting `required` to `blockers`/`highs` and the prompt to the old return passed all 16
arms, while a real synthesis following that schema returns no `items` and every audit round with a
confirmed finding would throw as degraded. The skeptic lowered it from high: that failure is loud on
the first real run and cannot produce a wrong merge.

**Fold:** `run_wf` gained `RUN_WF_SCHEMA=strict`, under which a doubled value missing a required key
comes back null and an undeclared top-level key is dropped. The MT arms run the callee through
`run_merged_review`, which sets it. Two arms joined: the `prompt:synth:` line carries
`Return JSON {path, items, summary}`, and a double with no `items` key reads as a dead synthesis with
both counts null. The revert mutation now reds 11 arms.

**Left-shift:** the strict switch is the gate. A later arm running a real callee should use it.

### L1 · LOW · lens T3 — zero confirmed with unverified findings is unarmed

`tools/workflows/tier2-review.js`, the derivation block. With nothing confirmed the counts used to be
whatever the agent typed and are now derived from an empty set. Adding `!severityById.size` to the
fault predicate passed all 16 arms, and it turns a disposable round of 48 unverified findings into a
throw.

**Fold:** one fixture with no verdicts and an empty item list. The callee returns 0 and 0 beside 48
unverified, and the harness logs `disposal: done — promoted 0 · folded 48`. The mutation now reds 2
arms.

## Refuted, with the skeptic's reason

- **C1 and S1, medium — the convergence count is now raw.** The mechanics reproduce, but the diff did
  not change the documented unit: `blockers` was always defined over confirmed findings. This harness
  audits spec-set subjects bounded at one round, and the diff-review skeptics refute duplicates. The
  residual is named in spec section 3.
- **C2, low — an id under an unknown severity and a valid one counts once.** It needs the runtime to
  pass a severity outside the schema enum and a synthesis contradicting its own prompt.
- **C3, low — a repeat at the same severity nulls a knowable split.** Failing closed is the file's
  stated policy; the note's wording for a repeat inside one item is cosmetic.
- **C4 and T4, low — the tally-fault note outranks PARTIAL.** One worst-first note is the documented
  order, and lens deaths travel in their own fields.
- **C5, low — the synthesis is not told to write raw ids into the report.** Behavioural, and a
  miscount fails closed at the reconciliation refusal.
- **S2, low — the degraded throw does not name the report path.** The report lands in the caller's
  own `reviewDir`; a stale comment list is a nit.
- **S3, low — no review-harness version bump.** No written rule requires one, and the gap is the open
  row `TOOL-aHoistedPass-31`.
- **T2, low — two arms could go vacuous if their `sed` stops matching.** Both catch their mutants
  today; going vacuous needs a fixture reformat and a regression in one change.
- **T5, low — non-confirmed ids are armed only for unverified ones.** One predicate covers every
  non-confirmed id, and the synthesis never sees refuted ids.
- **T6, low — the disposal prompt's new sentence has no arm.** It is guidance; the floors it
  describes are enforced and armed.
- **T7, low — the per-item tally and two log lines are unarmed.** Nothing reads them.
- **T8, low — the verify double answers every id in every batch.** Batching and the verdict join are
  old code outside this diff, and the tally does not change.

## Bug classes run

`fixture-passes-by-finding-nothing` produced M1 and L1. `staged-break-substitutes-a-synthetic-value`
was checked: the fixture is the measured shape, 48 raw and 13 confirmed with the record's own merges.
`degradation-known-but-unreported` was checked: the tally fault is carried in `note` and logged.
