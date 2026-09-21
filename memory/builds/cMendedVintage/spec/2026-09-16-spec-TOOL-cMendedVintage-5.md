# TOOL-cMendedVintage-5 — the carried predicate sees a `${VAR:-tools/…}` default

**Status:** CLOSED · rev-3 · 2026-09-17 · node c · Tier-2 · base 859daa67 · streams tooling · order 16

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-17-build-TOOL-cMendedVintage-5-acceptance-ledger.md](../build/2026-09-17-build-TOOL-cMendedVintage-5-acceptance-ledger.md) | journal | — |
| [2026-09-16-prompt-DEPL-cMendedVintage-1-1-spec-briefs.md](../prompts/2026-09-16-prompt-DEPL-cMendedVintage-1-1-spec-briefs.md) | journal | DEPL-cMendedVintage-1 DEPL-cMendedVintage-2 DEPL-cMendedVintage-3 DEPL-cMendedVintage-4 DEPL-cMendedVintage-5 DEPL-cMendedVintage-6 DEPL-cMendedVintage-7 DEPL-cMendedVintage-8 DEPL-cMendedVintage-9 DEPL-cMendedVintage-10 DEPL-cMendedVintage-11 DEPL-cMendedVintage-12 DEPL-cMendedVintage-13 DEPL-cMendedVintage-14 TOOL-cMendedVintage-1 TOOL-cMendedVintage-2 TOOL-cMendedVintage-3 TOOL-cMendedVintage-4 TOOL-cMendedVintage-6 TOOL-cMendedVintage-7 TOOL-cMendedVintage-8 TOOL-cMendedVintage-9 |
| [2026-09-16-prompt-TOOL-cMendedVintage-5-2-build-brief.md](../prompts/2026-09-16-prompt-TOOL-cMendedVintage-5-2-build-brief.md) | journal | — |
| [2026-09-16-review-DEPL-cMendedVintage-1-spec-audit-round1.md](../reviews/2026-09-16-review-DEPL-cMendedVintage-1-spec-audit-round1.md) | spec-audit | TOOL-cMendedVintage-1 TOOL-cMendedVintage-2 TOOL-cMendedVintage-3 TOOL-cMendedVintage-4 TOOL-cMendedVintage-6 TOOL-cMendedVintage-7 TOOL-cMendedVintage-8 TOOL-cMendedVintage-9 DEPL-cMendedVintage-1 DEPL-cMendedVintage-2 DEPL-cMendedVintage-3 DEPL-cMendedVintage-4 DEPL-cMendedVintage-5 DEPL-cMendedVintage-6 DEPL-cMendedVintage-7 DEPL-cMendedVintage-8 DEPL-cMendedVintage-9 DEPL-cMendedVintage-10 DEPL-cMendedVintage-11 DEPL-cMendedVintage-12 DEPL-cMendedVintage-13 DEPL-cMendedVintage-14 |
| [2026-09-17-review-DEPL-cMendedVintage-1-diff-review-round1.md](../reviews/2026-09-17-review-DEPL-cMendedVintage-1-diff-review-round1.md) | diff-review | DEPL-cMendedVintage-1 DEPL-cMendedVintage-2 DEPL-cMendedVintage-3 DEPL-cMendedVintage-4 DEPL-cMendedVintage-5 DEPL-cMendedVintage-6 DEPL-cMendedVintage-7 DEPL-cMendedVintage-8 DEPL-cMendedVintage-9 DEPL-cMendedVintage-10 DEPL-cMendedVintage-11 DEPL-cMendedVintage-12 DEPL-cMendedVintage-13 DEPL-cMendedVintage-14 DEPL-cMendedVintage-15 DEPL-cMendedVintage-16 DEPL-cMendedVintage-17 DEPL-cMendedVintage-18 DEPL-cMendedVintage-19 DEPL-cMendedVintage-20 DEPL-cMendedVintage-21 TOOL-cMendedVintage-1 TOOL-cMendedVintage-2 TOOL-cMendedVintage-3 TOOL-cMendedVintage-4 TOOL-cMendedVintage-6 TOOL-cMendedVintage-7 TOOL-cMendedVintage-8 TOOL-cMendedVintage-9 TOOL-cMendedVintage-10 |
| [2026-09-21-review-DEPL-cMendedVintage-1-diff-review-round2.md](../reviews/2026-09-21-review-DEPL-cMendedVintage-1-diff-review-round2.md) | diff-review | DEPL-cMendedVintage-1 DEPL-cMendedVintage-2 DEPL-cMendedVintage-3 DEPL-cMendedVintage-4 DEPL-cMendedVintage-5 DEPL-cMendedVintage-6 DEPL-cMendedVintage-7 DEPL-cMendedVintage-8 DEPL-cMendedVintage-9 DEPL-cMendedVintage-10 DEPL-cMendedVintage-11 DEPL-cMendedVintage-12 DEPL-cMendedVintage-13 DEPL-cMendedVintage-14 DEPL-cMendedVintage-15 DEPL-cMendedVintage-16 DEPL-cMendedVintage-17 DEPL-cMendedVintage-18 DEPL-cMendedVintage-19 DEPL-cMendedVintage-20 DEPL-cMendedVintage-21 DEPL-cMendedVintage-22 DEPL-cMendedVintage-23 DEPL-cMendedVintage-24 DEPL-cMendedVintage-25 DEPL-cMendedVintage-26 DEPL-cMendedVintage-27 DEPL-cMendedVintage-28 TOOL-cMendedVintage-1 TOOL-cMendedVintage-2 TOOL-cMendedVintage-3 TOOL-cMendedVintage-4 TOOL-cMendedVintage-6 TOOL-cMendedVintage-7 TOOL-cMendedVintage-8 TOOL-cMendedVintage-9 TOOL-cMendedVintage-10 TOOL-cMendedVintage-11 TOOL-cMendedVintage-12 |

<!-- /gen:spec-records -->

## 1. Goal

`re_ship` at `tools/check-install-prefix.sh:399` excludes `-` from the character class that may
precede a carried `tools/…` literal, so the whole `${VAR:-tools/path}` family is invisible to the
ban. That is the commonest way a dead literal is spelled in this tree: a variable that resolves at
one prefix, with a hardcoded fallback that resolves at gov's. Drop `-` from the lead-exclusion class,
bump the predicate epoch, rebaseline once, and confirm the widened predicate reds on a staged break.

## 2. Scope (IN)

- **S1** `tools/check-install-prefix.sh:399` drops `-` from `re_ship`'s lead-exclusion class:
  `[^/{}[:alnum:]._-]` becomes `[^/{}[:alnum:]._]`. One character, and it is the whole predicate
  change. Observed by AC1.
- **S2** `PREDICATE_EPOCH` at `:347` goes 3 to 4, and the epoch history comment block below it gains
  an `epoch 4` line saying what the widening admits. The file already documents epochs 1, 2 and 3
  that way and the block is the only record of what each ratchet baseline means. Observed by AC2.
- **S3** `bash tools/check-install-prefix.sh --rebaseline` runs once and
  `tools/install-prefix-carried.txt` is committed with the new rows and the `# predicate-epoch: 4`
  header. The mode refuses unless the recorded and declared epochs differ, so S2 must be in the tree
  before it runs. Observed by AC2.
- **S4** Every row the widening RAISES carries a fourth-column reason naming what the new occurrence
  is and whether draining it is a follow-up. A rebaseline blesses whatever is in the tree, so a row
  that arrives with no reason is a defect recorded as a baseline. Observed by AC3.
- **S5** The widened predicate is confirmed RED on a staged break before the unit closes: a
  `${VAR:-tools/<name>.sh}` default added to a file in the shipped population, `--check` observed to
  name it, the break unstaged. Observed by AC4.

## 3. Non-goals (OUT)

- No change to the root predicate's copy of the same class at `tools/check-install-prefix.sh:202`.
  Its subject is a BARE `<kit>/file.ext` spelling rather than a `tools/`-prefixed one, so the
  populations differ and the widening's size there is unmeasured. It is a real follow-up and the
  first thing that follow-up owes is that measurement; guessing it here would put an unmeasured
  number beside a predicate.
- `/` stays in the exclusion class. MEASURED at BASE: dropping it takes the occurrence count from
  1307 to 1511. RE-MEASURED at the build commit, per rev-3: 1148 to 1351. The reading moved and the
  verdict did not, because the addition is dominated in both readings by CORRECT `<gov>/tools/…`
  spellings that name gov's own checkout in runbook and adopter prose. The ban would then red on the
  one spelling that is right.
- No draining of the rows the widening raises. This unit changes the PREDICATE; fixing the sites it
  newly sees is separate work, and S4 is how each one is recorded rather than absorbed.
- No `--write-ratchet` run. That mode may lower a count and may not raise one, which is the ban this
  repo deliberately built; `--rebaseline` is the one-shot escape a predicate change earns and S3 uses
  exactly one of them.
- No new waiver row in `tools/install-prefix-waivers.txt`. That registry is shrink-only and a
  widening is not a reason to spend it.

### Edges

- **consumes-from** `TOOL-cMendedVintage-4` — eight of the ten occurrences the widening newly sees
  at BASE are the `${smerge:-tools/settings-merge.py}` tails that unit deletes. The rebaseline is
  ONE-SHOT and blesses whatever is in the tree, so landing this unit first records those eight as
  carried and makes the class invisible again with no second rebaseline available.
- **hands-off** external — the two occurrences that survive the settings-merge retirement named in
  the bullet above are argv defaults in gov's own checkers and are recorded by S4 rather than fixed.
  Draining them is a follow-up nobody in this build carries.

## 4. Design

### Data model

MEASURED on 2026-09-16 against BASE `859daa67`, by running the gate's own population derivation and
then both regexes over it. The population is 229 shipped source paths.

| predicate | occurrences | delta |
|---|---|---|
| `re_ship` as shipped | 1307 | — |
| `-` dropped from the lead class | 1317 | +10, on 10 lines in 3 files |
| `/` dropped from the lead class | 1511 | +204 |

The ten new occurrences at BASE, every one of them the defect shape:

| file | lines | spelling |
|---|---|---|
| `tools/check-wiring.sh` | `414`, `423`, `425`, `473`, `475`, `521`, `579`, `581` | `${smerge:-tools/settings-merge.py}` and its uppercase twin |
| `tools/check-agent-cap-restatement.sh` | `54` | `WAIVERS=${1:-tools/agent-cap-restatement-waivers.txt}` |
| `tools/check-line-length.sh` | `49` | `DECL=${DECL:-tools/line-length-limits.txt}` |

The brief this unit was written from states 11. The reading above says 10, and the figure is DERIVED
rather than PINNED for that reason: it is a count over a tree that moves, and the number that matters
is the one the rebaseline records at the commit, not the one a spec typed a day earlier.

After `TOOL-cMendedVintage-4` lands, eight of the ten are gone and the widening's live delta is the
two argv defaults. Both are gov-side checkers whose registry path is dead at any other prefix, so
both are real and both are S4 rows rather than repairs.

### Rollout

Order within the unit is load-bearing and is three steps, not one: edit `re_ship`, bump
`PREDICATE_EPOCH`, then `--rebaseline`. Reversed, the mode refuses — it compares the recorded epoch
to the declared one and exits when they agree. It also refuses over a dead probe, requiring
`carried_live()` above zero, which is this gate's liveness assertion and is untouched.

### Inventory

Minted by this unit: nothing. One character leaves a character class, one integer constant moves, and
one generated artifact is rewritten by a mode that already exists.

### Alternatives rejected

Anchoring on the `:-` operator specifically rather than widening the lead class: it catches this
family and misses `${VAR:+tools/…}`, `${VAR:=tools/…}` and every other expansion whose operator is
not `-`. The lead class is the general form and the measurement says its false-positive count at BASE
is zero.

Adding the sites to `tools/install-prefix-waivers.txt` and leaving the predicate alone: that records
ten known-dead literals as permitted, which is the exemption-instead-of-coverage shape.

### Files touched (estimate)

| Path | Change |
|---|---|
| `tools/check-install-prefix.sh` | one character in `re_ship`, `PREDICATE_EPOCH`, one epoch comment line |
| `tools/install-prefix-carried.txt` | rewritten by `--rebaseline`, plus the S4 reason columns |
| `tools/check-install-prefix.test.sh` | one arm over a fixture carrying a `${VAR:-tools/…}` default |

## 5. Production-readiness checklist

- security — none. The gate reads tracked text and writes one declaration file.
- perf / scale — unchanged. One character in a regex over the same 229 files.
- error / empty / loading states — `--rebaseline`'s two refusals are both liveness guards and both
  stay: it refuses when the epochs agree, and it refuses over an empty population.
- observability — `--check` prints ROSE, SLACK and the per-path counts, so the widening's effect is
  visible as named rows rather than as a verdict.
- risks — the rebaseline is one-shot, so a wrong ordering against `TOOL-cMendedVintage-4` is
  unrecoverable without declaring a fifth epoch for no predicate change. `TOOL-dTieredTribunal-27`
  also records that the ratchet file is itself in the graded population, so a write can move its own
  row; the pass runs `--check` after the rebaseline rather than assuming one pass converged.
- testing — AC1 and AC4 run the gate directly over a staged break. The permanent arm is declared in
  section 7.
- migration — none for an adopter. This gate is gov-side and is not shipped as a target's leg.
- user docs — the epoch comment block in `tools/check-install-prefix.sh` is the documentation for
  what each baseline means, and S2 extends it. No other page states the predicate.

## 6. Acceptance criteria

- **AC1** — When a file in the shipped population is given a `${GOV_X:-tools/agent-cap.js}` default
  and `bash tools/check-install-prefix.sh --check` runs, that file is named with a count one higher
  than its row; with the break unstaged, the same command exits 0.
  Red when: `-` is left in the lead-exclusion class, so the staged default is invisible and the run
  reports the pre-break count — which is the state this unit exists to leave.
  figure: DERIVED — the count is the gate's own per-path figure at observation time.
- **AC2** — When `bash tools/check-install-prefix.sh --rebaseline` runs after S1 and S2 are in the
  tree, it prints `REBASELINED for predicate epoch 3 -> 4`, and a second invocation prints
  `REFUSING to rebaseline` and exits non-zero.
  Red when: the epoch constant is not bumped, in which case the first invocation is the one that
  refuses and the widened predicate never gets a baseline.
- **AC3** — When `tools/install-prefix-carried.txt` is read after the rebaseline, every row whose
  count is higher than at BASE `859daa67` carries a fourth-column reason.
  Red when: the rebaseline is committed as written, so a newly seen dead literal is recorded as a
  blessed baseline with nothing saying what it is.
- **AC4** — When `bash tools/check-install-prefix.sh --check` runs against the unmodified tree after
  the rebaseline, it exits 0 and its report names a non-zero graded population.
  Red when: the rebaseline ran over a collapsed population, so the baseline records zeros and the
  gate passes by grading nothing.
  figure: DERIVED — `carried_live()` is the gate's own population figure and is printed by the run.

## 7. Gates

`install-prefix (shipped surface)` · `install-prefix self-test` · `check-wiring self-test` · `line length` · `dead-path carriers (deleted files still named)`

New arm: `tools/check-install-prefix.test.sh` · a fixture file carrying a `${VAR:-tools/<name>.sh}`
default, asserted to be counted under epoch 4 and not under epoch 3 · no assertion floor to move.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-16 · initial draft.
- rev-3 · 2026-09-17 · §3, §4 and §7 · TWO CORRECTIONS, no criterion and no design changed. §3's
  `/` non-goal is the OTHER HALF of correction (a) and moved with it: it stated the BASE reading in
  the present tense, so amending §4 alone would have left one measurement answering in two figures.
  Its verdict is unchanged under both readings, which is the point of recording both.
  (a) The Data model table's ABSOLUTE figures no longer describe the tree. Re-measured at the build
  commit by re-running the gate's own population derivation and all three regexes over it, the
  population is still 229 shipped source paths and the occurrence counts are 1148 as shipped, 1150
  with `-` dropped and 1351 with `/` dropped. So the live deltas are +2 and +203, against the +10
  and +204 the table recorded at BASE. The table's absolute numbers are a reading of a tree fifteen
  units old and are wrong for this one; its PREDICTION was right to the occurrence, and the two
  survivors are the two it named. Both are the argv defaults: line `54` of
  `tools/check-agent-cap-restatement.sh`
  and line `49` of
  `tools/check-line-length.sh`,
  which is the whole live delta and the whole of what S4 records. The brief this unit was written
  from claimed 11 and claimed that dropping `/` adds roughly 240; the first is a BASE figure and the
  second is an estimate, and neither reproduced.
  (b) §7 declares ONE new arm. Two were written, because this suite's own header requires a green
  control over the same mechanism for every red arm, and an arm asserting only that the widened
  predicate reds cannot tell "the gate caught the default" from "the gate rejects everything". The
  control is the `/`-preceded spelling the `/` non-goal deliberately keeps excluded, so it is also
  the arm that reds if a later pass widens the class again. No assertion floor moved.
- rev-2 · 2026-09-16 · §3 · the `hands-off` external edge named a sibling unit id in backticks, which
  hygiene check 12 reads as a joinable edge written as an unjoinable one. The sibling is already
  joined by the `consumes-from` bullet above it, so the reference is now spelled without the id. Not
  a review finding — found by running the gate over the spec set while disposing round 1.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "resolve the install prefix for a remedy string printed by
a wiring checker"` returned no seam that counts a path literal — the ranking is `resolve_*` symbols
in govkit, codebase-map and memory-recall, none of which grades text — and reported `.sh` as an
unscanned layer, so this gate is invisible to the map by construction. No existing seam fits, and the
evidence is the record that already established it: `DEPL-dGaugedVintage-7`'s own section 10 says the
same lookup returned `repo_root`, `map_root`, `require_adopted_root` and `tracked_files`, "none of
which counts anything", and that the counting lives inline in `tools/check-install-prefix.sh`. This
unit changes it in the same place, and reuses the epoch mechanism `TOOL-dRetiredFork-17` built for
exactly this act rather than adding a second way to widen. The recall probe returned the prior
widening to model on: `TOOL-cWidenedNet-1`, which took the predicate 2 to 3, and
`TOOL-dTieredTribunal-27`, the open row recording that the ratchet file sits in its own population.

Recall terms used: `--terms "check-install-prefix carried predicate KIT_REL boundary walk repo root
empty prefix settings-merge remedy adopter install prefix ratchet rebaseline PREDICATE_EPOCH
check-wiring"`, with the question "why do shipped kit files carry a literal tools/ prefix and what
predicate catches a carried prefix at a scripts install".
