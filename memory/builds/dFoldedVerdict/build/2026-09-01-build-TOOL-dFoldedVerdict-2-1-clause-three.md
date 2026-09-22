# TOOL-dFoldedVerdict-2 — clause 3 reads the disposition instead of guessing from ids

**Serves:** journal TOOL-dFoldedVerdict-2

*Node `d`, 2026-09-01, owner-present build under `memory/guides/BUILD-METHOD.md`.*

## What binds now

Check 2's third clause no longer infers what a review exit did from the unit ids a build gained. For
a record graded by `DISPOSITION_CUTOFF` it READS the disposition off each exited subject's own
terminal row: a subject recording `promote` demands the id delta the clause always demanded, and a
subject recording `fold` **demands nothing at all**. That asymmetry is the entire point — the old
predicate could only ever observe promotion, so a run that folded every blocker correctly was graded
as though it had promoted.

Three outcomes are refusals rather than passes, and the second and third exist because the obvious
rewrite replaces one vacuity with another:

- a graded record whose exited subject records NO disposition. Without this, `nneed` falls to zero on
  every unlabelled record and the clause becomes green-by-absence.
- a disposition OUTSIDE `fold|promote`. The driver validates the flag at write time, so an illegal
  value can only reach a record by hand — and `TOOL-dFoldedVerdict-3` creates exactly that class, so
  this is not a hypothetical branch. Reading it as "absent" would name the wrong cause.
- a declared `DISPOSITION_CUTOFF` that is not an ISO date.

Blank or absent grandfathers every record onto the id-delta proxy and the leg **announces that on
stdout, unconditionally, once per run**. Not through `report()`, which is gated on
`GOV_UNATTENDED_REPORT` and would make the disabled term invisible on a default bar run — a silently
disabled clause reads exactly like a clause finding nothing wrong.

## One criterion was wrong and the code follows the criterion

AC3 asks that a malformed cutoff "grades no record under either predicate, rather than silently
choosing one". The first cut refused AND then graded every record on the pre-cutoff proxy, because
`rv_graded` fell to 0 for all of them. Observed, not reasoned about: the run printed the refusal and
then named `dMispairedQuote` under the old message.

That is the fault the refusal exists to prevent, one level down. A malformed cutoff now SKIPS the
record loop entirely and says so, the same shape the `RUNAWAY_CEILING` arm beside it already uses.

## The renumber, which is an obligation and not a discovery

The new `fail 2` sits above the record loop, so it becomes check 2's FIRST branch and every later
ordinal moves by one. `memory/project/unarmed-branches.txt` pins three of this leg's check-2 branches
by ordinal; left alone that reds `harness arms` FOUR times — one row pinning a branch that is now
armed, two stale signatures, and one unarmed branch no longer pinned. All three rows were renumbered
9, 10, 11 → 10, 11, 12 in this commit, signatures and count untouched.

Scoped to check 2, deliberately. `check-arms.py` numbers branches per CHECK NUMBER and not per file,
so the five `check 16` rows this same file pins do NOT move, and editing them would be the over-fix.
Verified against `--report`: they are unchanged at 13 through 17.

## Evidence

**Evidences:** TOOL-dFoldedVerdict-2

- **AC1** — `bash tools/unattended/check-unattended.sh` over this tree names
  `memory/builds/dBriefedPass/RUN.md` for subjects `dBriefedPass-spec-set` and `dBriefedPass`, and
  `memory/builds/dMispairedQuote/RUN.md` for `TOOL-dMispairedQuote-1` and `TOOL-dMispairedQuote-3`,
  each for recording no disposition. FOUR exited subjects across two records, which is exactly the
  four rows the owner ruling gave `TOOL-dFoldedVerdict-3`. None of the eleven records whose first
  commit precedes the cutoff is named.
- **AC2** — with `DISPOSITION_CUTOFF=""` in the working tree, the verdict returns to today's:
  `dMispairedQuote` alone, named by the pre-cutoff shortfall message with its `LOWER BOUND` sentence
  intact, and the announcement line printed above it. The conf edit was made in the working tree and
  reverted; `git diff --stat` over it is empty.
- **AC3** — with `DISPOSITION_CUTOFF="not-a-date"`, the leg emits the S6 refusal naming the value and
  grades NO record under either predicate, printing `check 2 clause 3 graded NO record` in its place.
  Observed in both shapes: the first implementation refused and then graded anyway, which is recorded
  above rather than quietly corrected.
- **AC4** — `memory/builds/dBriefedPass/RUN.md` going UNNAMED at `nneed 0` is the substitute
  observation this criterion names, and it is **NOT YET AVAILABLE**: it requires
  `TOOL-dFoldedVerdict-3` at order 4 to label that record's two exits. What IS observed today is the
  half that precedes it — the record is named, by the absent-disposition refusal, which is the state
  the label is supposed to clear. The fold arm in the suite covers the same ground and may not be
  run. Marked as owed to unit 3 rather than claimed here.
- **AC5** — likewise `memory/builds/dMispairedQuote/RUN.md` at `nneed 1` against `newids 1` is owed
  to `TOOL-dFoldedVerdict-3`. The two promote arms in the suite may not be run. What is observed is
  that the record is named today for the absent disposition rather than for a count.
- **AC6** — the fixed string `non-WONTDO unit id(s) this run BASE lacked` now matches BOTH
  `tools/unattended/check-unattended.test.sh` (3 hits) and `tools/unattended/check-unattended.sh`
  (2 hits). Before this unit the first search returned nothing while the second matched, which is
  S9's live defect: that arm has been RED since `ccb5492c`.
- **AC7** — `python tools/memory-tree/check-arms.py --check` exits 0 with `.memory-tree.conf`
  UNCHANGED by this unit. No floor was raised, and the spec's reasoning holds: the floors are
  one-sided minimums far below the measured values, so a raise cannot fail. What binds is the
  unarmed-and-unpinned refusal, which has a real failing case.
- **AC7a** — `--report` shows the three check-2 rows at ordinals 10, 11 and 12 with signatures
  unchanged, the five check-16 rows unchanged at 13 through 17, and no row reported stale, newly
  armed, or pinning a branch that no longer exists.
- **AC7b** — `tools/unattended/check-unattended.sh` measures **173 branches / 165 armed**, risen by
  exactly ONE from the 172 / 164 this unit inherited. **The criterion's stated pre-image is stale and
  the reorder is why:** it names BASE's 169 / 161 on the reasoning that `TOOL-dFoldedVerdict-1` keeps
  out of this file — true, but `TOOL-dFoldedVerdict-5` now lands at order 1 and added three branches
  to it. The substance of the criterion is the RISE OF EXACTLY ONE, and that is what was measured.
- **AC8** — `grep -n '^DISPOSITION_CUTOFF=' .unattended.conf` returns the declared date at `:230`,
  and check 22 reports no key disagreement. Two separate observations, because check 22 grades the
  PROJECT conf in one direction only: a green check 22 cannot witness the project declaration, and
  inferring it from one would pass a commit that adds the key to the example and the table, forgets
  `.unattended.conf`, and lands the blank-cutoff grandfather over the whole corpus with a green bar.
- **AC9** — `bash tools/memory-tree/check-memory-hygiene.sh` names no failing check, and
  `wc -c` reports **54621** for both halves of the protocol pair, byte-identical and far under 61440.
  The spec wrote this criterion against a document at exactly its cap adding TWO things; S14 was
  withdrawn and `TOOL-dFoldedVerdict-5` freed 7209 bytes at order 1, so the constraint that made this
  the unit's hardest criterion no longer binds.
- **AC10** — `grep -cF` for the WONTDO filter returns 1, the same count as today, and the line it
  matches is the HEAD-side id read at `:294`. The BASE-side read carries no such filter and S8 leaves
  both unchanged.
- **AC11** — `memory/gotchas/arm-literal-strands-on-message-edit.md` now states the exclusion this
  clause proves, a SECOND limit distinct from the one measured under S13. A message COMPOSED INSIDE an awk sub-program and appended
  to a `fail` argument is outside the population `check-arms` signs at all: what gets signed is the
  outer head, and `--report` duly lists `check 2 branch 3` ARMED on
  `review loops that ran past the ceiling …` alone. Named by SIGNATURE and not by ordinal, because S6
  moved that branch from 2 to 3. Three per-record messages were rewritten and two added under it, and
  `--check` stayed green throughout.
- **AC12** — one terminal row of `memory/builds/dMispairedQuote/RUN.md` hand-edited to
  ` · disposition promoted` produces S3's illegal-value refusal naming the file, the subject
  `TOOL-dMispairedQuote-1=promoted` and the value, and it does NOT reuse S2's wording. Taken at this
  unit's own image exactly as the criterion describes: the OTHER subject is still unlabelled, so both
  messages appear side by side in one output and a build folding the illegal value into the absent
  message fails visibly. The record was STAGED before the edit and reverted after, because a
  `git checkout --` restores the whole file.
- **AC13** — the `promoted to a unit rather than parked` sentence is gone from both halves of the
  PROTOCOL pair, but NOT by this unit's doing, and the criterion is stale. It asks that that sentence
  be gone from both halves of the PROTOCOL pair and
  the amended `--review` bullet present there. `grep -c` returns 0 in both protocol halves — but
  because `TOOL-dFoldedVerdict-5` MOVED section 7 out at order 1, not because this unit amended
  anything. The bullet lives in the VERBS pair, where `TOOL-dFoldedVerdict-1` corrected it at order 2
  and its AC17 graded it; `grep -c disposition` returns 3 in each half. S14 is WITHDRAWN, so this
  unit touches no verb bullet at all, and claiming this criterion here would be claiming a sibling's
  work.
- **S12a, verified with the LEG'S OWN extractor rather than a plausible one.** Check 22 reads the
  section-8 keys as `awk -F'|' 'NF>2 {print $2}' | grep -oE '`[A-Z_]+`'`. Under it, BASE
  `adc0543c` yields 29 keys and this tree yields 30. A first attempt used a stricter first-cell
  pattern and measured 28 → 29 — the right DELTA off the wrong base, which would have handed
  `TOOL-dFoldedVerdict-6` a number that is wrong by one.

## What this pass did NOT do

The nine new suite arms have not been executed — the standing owner instruction again. Every arm
pins its cutoff to `2000-01-01` or `2099-01-01` rather than to a date near today, so none of them
depends on the day the suite runs; a cutoff of "today" would have made them pass or fail by calendar.

`TOOL-dMispairedQuote-7` was NOT repointed here, although S13 names it. `TOOL-dFoldedVerdict-3` S8
claims that row explicitly and says it is owned there and not by this unit — two specs authored in
parallel took the same row, and the explicit claim wins. Only `TOOL-dBriefedPass-9` was closed here.

The id-delta computation is untouched, including its one-sided `| WONTDO |` filter.
