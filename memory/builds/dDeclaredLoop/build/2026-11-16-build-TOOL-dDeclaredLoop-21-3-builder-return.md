**Serves:** journal TOOL-dDeclaredLoop-21

# Builder return — TOOL-dDeclaredLoop-21, dispatch 3: check 2 reds the historical round records, and the driver suite's fixture policy is never read

## Why

DIVERGENCE: rev-6 §2 S6, together with §4 "Rollout" and §7's `unattended kit gate`, cannot be built as written. A second interface disagreement sits between §2 S4 and §4 "How the shell reads it". Both were probed read-only at base c28d4e5f.

(1) S6 newly reds check 2 on the tracked historical corpus.
- S6 says check 2's awk arm (tools/unattended/check-unattended.sh#scan_round_writes's sibling block, the `n[it] > ceil` comparison) "compares each subject's rounds with that subject's bound".
- Check 2 reads every tracked `memory/builds/*/RUN*.md` (`GIT ls-files ":(glob)$M/builds/*/RUN*.md"`). It counts every `review · item` row per subject, and any subject over the limit feeds `rv_bad`, which ends in check 2's single `fail 2` ("review loops that ran past the ceiling ...").
- Those records are append-only, and today they are graded against the retired constant of 8.
- Measured with the awk's own subject split over every tracked RUN*.md, with gov's bounds after this unit (spec bound 1 under `one`, closing bound 3, `review.max-rounds` 3):
  - 69 subjects exceed their own subject's bound. Most are spec subjects with 2 to 4 rounds, for example aSurfacedLexicon's 13 unit subjects at 2 each and dDerivedDocket-specs-g1 at 3.
  - Even the gentlest reading, comparing only against `review.max-rounds` as the ceiling, reds 4: memory/builds/aBatchedArm/RUN.md TOOL-aBatchedArm-3 (4) and TOOL-aBatchedArm-5 (4), memory/builds/aStagedLane/RUN.md aStagedLane-spec-set (4), and memory/builds/aWeldedTribunal/RUN.md aWeldedTribunal, the slug subject (4).
- §4 "Rollout" ("a round past 3 now reads CEILING") and §4 "What this does not check" never say how records written under the 8-round backstop are graded. AC6 does not cover it.
- So the bar's `unattended kit gate` goes red at the close on records no verb can rewrite.
- The spec has to say how check 2 grades a record written before the policy keys. Options:
  - (a) Grandfather by the record's first-commit date, the `rv_fc` idiom check 2 already applies to DISPOSITION_CUTOFF and FOLD_CUTOFF. This needs a named cutoff and its home.
  - (b) Read the bound at each record's own BASE, as `read_fold_cutoff` does. A record before the keys then reads the retired 8.
  - (c) Keep the corpus comparison against a named historical backstop and compare per-subject bounds only on the in-flight record.
- Each option adds a value or reader the spec does not name today. None adds a `fail` site; check-unattended.sh is 266 against its ceiling of 266.

(2) S4's fixture re-pointing does not reach §4's reader.
- §4 runs `review_bounds.py show` with no `--rev`. That goes through tools/policy/policy.py#resolve to tools/policy/policy.py#derive_landed_revision, which reads `refs/remotes/<remote>/<branch>`.
- The driver suite's fixture pushes `main` to a bare ORIGIN once, then works on branch `unit`. `reset_tree` hard-resets to UNIT0 per arm, and many arms pin BASE to origin/main.
- So the per-arm "committed policy file" S4 asks for, which replaces mkconf's seventh positional (default 7, with arm values 9, 8, 0 and 1), is never read by `--review`. The arms would silently run at the catalogue defaults.
- The spec has to choose:
  - (a) Seed the default fixed-count-7 and max-rounds-7 policy on the fixture's main before the ORIGIN push, and say how a per-arm value lands without moving the anchor.
  - (b) Have the driver call `show --rev HEAD`, which is a change to §4.
- The unattended suites are waived for this landing (§3), but S4 asks for these edits to be made, and as written they cannot be made meaningful.

Everything else I probed holds at c28d4e5f:
- census 326/326 and 266/266; families 1/1, 11/11, 36/37
- REFUSAL_CEILINGS token and positional row at 326
- the decision row TOOL-dDeclaredLoop-21 is in memory/DECISIONS.md
- BUILD-METHOD.md is 30709 PINNED bytes, and the two M4 substitutions land at 30714
- the four catalogue keys and their defaults
- review_state, verb_review and RUNAWAY_CEILING as cited
- tools/unattended/unattended.sh#resolve_position_engine already takes a loop-kit script name, so it is the seam for `load_review_bounds`
- the parity arm in tier2-review.test.sh
- the ceiling-of-8 arms in unattended.test.sh
- core-pending.txt row 30 `principle principle.p38 dGroundRules`
- fanout_cap.py and its [[upgrade]] row in tools/hooks/kit.toml

## Summary

Nothing is committed and the tree is unchanged: TOOL-dDeclaredLoop-21 rev-6 can't be built as written. HEAD is still c28d4e5f1ae527105861e1fb6ef4b747fae1d480 and the tree is clean. I edited no product file, so there is no patch file.

**Blocker 1 — check 2 would go red on old run records.** S6 asks check 2 in tools/unattended/check-unattended.sh to compare each review subject's round count with that subject's new bound, where it compares against 8 today. Check 2 reads every tracked `RUN*.md` under memory/builds, and those records can't be rewritten.
- Against the new per-subject bounds (1 for a spec audit, 3 for the closing review), 69 recorded subjects are over.
- Even comparing only against `review.max-rounds` (3), 4 are over:
  - memory/builds/aBatchedArm/RUN.md, TOOL-aBatchedArm-3 and TOOL-aBatchedArm-5, 4 rounds each
  - memory/builds/aStagedLane/RUN.md, aStagedLane-spec-set, 4 rounds
  - memory/builds/aWeldedTribunal/RUN.md, the build's own closing review, 4 rounds
- So the `unattended kit gate` leg in §7 would fail at the close. The spec doesn't say how records written under the 8-round limit are graded. `why` gives three ways the spec writer could fix that.

**Blocker 2 — the fixture policy file would never be read.** §4 has the driver run `review_bounds.py show` with no `--rev`, which reads the policy file on the remote's main. S4 moves the driver suite's per-test round bound into a committed policy file. In that suite the remote's main is pushed once at setup, and every test works on a separate branch. A policy file committed there is never read, so those tests would silently run at the default bounds. The spec has to say either how the fixture's main gets the policy without moving the base other tests rely on, or that the driver reads `--rev HEAD`.

Every other rev-6 claim I checked still holds. That covers the refusal counts and the 326 ceiling entry, the decision row, the M4 byte arithmetic (30714 after the change), the catalogue defaults and the code `why` lists.

**What ran:** I read the build method, spec and brief in full and probed the spec's claims with read-only greps and reads. I re-ran the second builder's census script at C:/Users/DAILY-~1/AppData/Local/Temp/claude/b120d4a7f8b5be2e/7c85732c-fa0c-43e9-83f2-238d293195e0/scratchpad/census21.py. It reported 326 refusal sites in the driver against a ceiling of 326, 266 in check-unattended.sh against 266, and families at 1/1, 11/11 and 36/37. That run stands in for the census half of the `harness arms (fail branches armed or pinned)` leg. A shell loop splitting each record's review rows by subject, the way check 2's awk does, stands in for check 2's round comparison in the `unattended kit gate`. No gate, suite or bar ran.

**Not done:**
- `--dispatch`: RUN.md has no dispatch row for this unit, even though the task said the main loop had made one, and a divergence declares nothing.
- `--brief`: RUN.md already has a brief row for this brief (03:05:42Z today), and a new one would leave an uncommitted change.
- `gotchas.py --for-diff`: there's no commit to run it over.

**Owed at the close once the spec is revised and the unit rebuilt:** the RED-first runs of the three `New arm:` lines. They are:
- the `loop review bounds fixtures` plants, for AC1 to AC3
- the govkit self-test arms, for AC7 and AC8
- the unattended and check-unattended suite arms, for AC4 and AC6, which are waived for this landing

The harness arms leg also owes a census read after the build, at 327 against the raised ceiling.
