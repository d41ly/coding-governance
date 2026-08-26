# TOOL-dTieredTribunal-15 — the false-clean family enters the catalogue

**Status:** CLOSED · rev-2 · 2026-08-26 · node a · Tier-1 · base cd971285 · order 1 · streams tooling · ratified 2026-08-26

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-26-review-TOOL-dTieredTribunal-11-spec-audit-round1.md](../reviews/2026-08-26-review-TOOL-dTieredTribunal-11-spec-audit-round1.md) | spec-audit | TOOL-dTieredTribunal-11 TOOL-dTieredTribunal-12 TOOL-dTieredTribunal-13 TOOL-dTieredTribunal-14 |
| [2026-08-26-review-TOOL-dTieredTribunal-11-spec-audit-round2.md](../reviews/2026-08-26-review-TOOL-dTieredTribunal-11-spec-audit-round2.md) | spec-audit | TOOL-dTieredTribunal-11 TOOL-dTieredTribunal-12 TOOL-dTieredTribunal-13 TOOL-dTieredTribunal-14 |

<!-- /gen:spec-records -->

## 1. Goal

`memory/guides/BUILD-METHOD.md` M8 requires every confirmed finding to be left-shifted, into a
regression gate where one fits and into a `memory/gotchas/` class where none does, and it states that
a finding fixed and not left-shifted returns. This build's closing diff review confirmed two HIGH
findings, D1 and D2. Both were fixed in place and neither was left-shifted. The owner ruled at
`TOOL-dTieredTribunal-9` that what is owed is a RECORD and explicitly not a scanner. Write the record.

The record also has to fire on the diff class it exists for, which is a change to an agent-spawning
harness under `tools/workflows/`. A record whose anchors cannot select that surface ships inert, which
is itself a class this catalogue already carries. The anchor set is therefore measured before it is
written and not after.

## 2. Scope (IN)

- **S1** — a new record at `memory/gotchas/degradation-known-but-unreported.md`, carrying the front
  matter the existing records use. `kind` is `class` and `universal` is `false`.
- **S2** — the record's body carries a phrase `declares()` reads, so hygiene check 18 passes. The
  owner ruled this class a documented check rather than a gate, so the phrase is the no-machine-gate
  form and not the name of a leg that does not exist.
- **S3** — the record's anchors are the harness surface and nothing wider. The directory token
  `tools/workflows/` is the one that reaches the diff class, and the three harness citations are
  subsets of it. Anchors are DERIVED and not declared, so the record earns each one by citing it in
  its body, and its derived set is whatever the finished body contains. The measurement behind the
  width choice, and the spelling refused for it, are in section 4.
- **S4** — the record's evidence cites TRACKED files. The finding record is
  `memory/builds/dTieredTribunal/reviews/2026-08-26-review-TOOL-dTieredTribunal-1-closing-diff.md`,
  which states D1 and D2 in its own words, and the three harnesses carry the fixed and unfixed
  instances at the line numbers section 4 pins.
- **S5** — `python tools/memory-tree/gotchas.py --write` re-renders `memory/gotchas/INDEX.md` in the
  same commit as the record.
- **S6** — the new `gotcha-classes` inventory key is claimed by
  `memory/map/features/review-harnesses.md` in the same commit. That dossier already claims all three
  harnesses under `workflow-scripts`, its `[paths] globs` is `tools/workflows/*`, and its
  `gotcha-classes` list is empty at base.
- **S7** — `python tools/codebase-map/gen_map.py --write` re-renders `memory/map/generated/` in the
  same commit as the S6 claim edit. `tools/codebase-map/test_codebase_map.py` byte-compares the
  committed artifacts against a live re-render, so a claim landed without a render reds the very leg
  AC9 asserts is green.
- **S9** — a new backlog row `TOOL-dTieredTribunal-16` in `memory/backlog/TOOL.md` records the live
  REACH instance in `tools/workflows/tier2-review.js`, whose synthesis prompt hands the agent no
  liveness counter, so the record that harness writes cannot state that half its lenses died.
  Section 8's F1 resolves to writing it, on the ground that no unit of this build closes it.
- **S8** — the backlog row `TOOL-dTieredTribunal-5` in `memory/backlog/TOOL.md` flips from `OPEN` to
  `CLOSED`. That row says in as many words that writing the record closes it.

## 3. Non-goals (OUT)

- **A scanner.** The owner ruled it out at `TOOL-dTieredTribunal-9`, and the backlog row already
  prices both candidates: a ban on conditional ordering reds every legitimate chain, and a rule that
  every returned counter must appear in a prompt string is satisfiable by a comment.
- **A new gate leg.** The existing record checks over `memory/gotchas/` already grade the file and the
  index-freshness check already grades the render. Nothing new is wired.
- **Any edit to the three harnesses.** D1 is already fixed in all three at base and D2 in two of
  them. The record is the left-shift, not a second fix.
- **Fixing the live residual in `tools/workflows/tier2-review.js`.** Its synthesis prompt names no
  liveness counter at base, which is D2's shape in the reference harness. The record NAMES it as the
  live instance. Whether it also earns a backlog row is fork F1 in section 7 and is not decided here.
- **`universal: true`.** `.memory-tree.conf` declares `UNIVERSAL_BUDGET="4"`, and the universal row
  that `python tools/memory-tree/gotchas.py --report` prints shows the budget already spent in full
  at base. The flag would therefore need a same-commit budget raise, which is an owner call. It is
  also semantically wrong here, because this class binds harness diffs and not every diff.
- **Any edit to `memory/guides/BUILD-METHOD.md`.** That carrier is unit `TOOL-dTieredTribunal-12`'s
  subject, at order 5 of this build, and it is close enough to its own declared byte cap that the
  headroom is a budget somebody is already spending. This unit spends none of it, and does not name
  the class in that file.
- **Retrofitting the class onto past review records.**

## 4. Design

### The class, stated once

A pipeline computes how badly its own run degraded. It then fails to say so where it matters. Two
shapes, one family, and the family is that a degraded run produces a clean bill.

The first shape is ORDERING. A chained conditional tests the lesser degradation first, so the branch
naming the worst outcome is reachable only in the combination where nothing else went wrong, which is
the rarest one. At base, `tools/workflows/tier2-review.js:448`,
`tools/workflows/drift-audit-state.js:474` and `tools/workflows/drift-audit-code.js:454` all test the
synthesis death first, each under a comment naming the unit that reordered it. Before that reorder,
the string announcing that no report exists was emitted only when no lens and no skeptic had died and
no finding was unverified. The demote-on-conflict rule that landed in the same build made the last of
those non-zero more often, so the port narrowed the path to its own honest message while adding it.

The second shape is REACH. A counter is computed, returned to the caller, and never handed to the
agent that writes the durable artifact. At base the two drift-audit siblings interpolate a run-integrity
line into their synthesis prompts at `tools/workflows/drift-audit-state.js:431` and
`tools/workflows/drift-audit-code.js:414`. `tools/workflows/tier2-review.js` does not: its synthesis
prompt runs from line 328 to line 386, its shape line at 346 names the raw, confirmed, refuted and
unverified counts and the precision, and no line in that range interpolates a liveness counter. So the
record it writes cannot state that half the lenses died, in the harness the closing review called the
reference implementation.

Both shapes are invisible to a reader of the artifact, which is why the class is worth a name. The
tell to hand a reviewer is one question: does the thing that PERSISTS carry the degradation, or only
the thing that returns.

### The anchors, and the width that was refused

The anchor set selects a little over one percent of the tracked tree, and `tools/workflows/` alone
accounts for all but one of the paths in it. Measured by importing the shipped module and calling
`selectable()` over `git ls-files`, not estimated.

The spelling refused is the bare `tools/`, which selects about one tracked file in five. That is
near-universal selection bought under an anchor's name, and noise on a checklist is how reviewers
learn to skip the checklist.

NO ABSOLUTE COUNT IS WRITTEN IN THIS SECTION. Every one of these figures is derived from the tracked
path set, `git ls-files` is what the shipped module actually reads, and that set already disagrees
with the commit tree at base by one staged file. A number typed beside a source that owns it is wrong
on the next commit. The width claim is therefore a ratio, and it is OBSERVED by AC5 rather than
asserted.

Two anchor spellings are also deliberately absent. `memory/guides/BUILD-METHOD.md` would put this
class on the checklist of every diff editing the build method, including this build's own unit 12,
and a rule edit is not a harness diff. `tools/drift-audit/` would extend the class to a kit that
already ships its own dead-probe doctrine, on no measured instance. Neither is refused on principle;
both are refused because no observed instance of this class sits there.

### The fold trap this record has to survive

The record must NOT carry a bare backticked `tools/memory-tree/gotchas.py` or `gotchas.py` token,
because that token would become an anchor and would select AC5's negative. The catalogue's own
selection machinery is described in the record by naming the invocation as a whole command line,
which carries whitespace and which `ANCHOR_RE` therefore harvests to nothing. Verified by importing
the shipped module: the multi-word backticked command yields an empty anchor list while the same path
alone in backticks yields the anchor. This is a live constraint on any future fold of this record, not
a stylistic preference, and it is written here because that is where a folder will look.

A `file:line` citation still selects its file. `selectable()` matches both substring directions, so
the anchor `tools/workflows/drift-audit-state.js:474` selects `tools/workflows/drift-audit-state.js`
through the second of them. The record may therefore keep its line citations without losing reach.

### Files touched (estimate)

| Path | Change |
|---|---|
| `memory/gotchas/degradation-known-but-unreported.md` | new record |
| `memory/gotchas/INDEX.md` | regenerated by `gotchas.py --write` |
| `memory/map/features/review-harnesses.md` | one claim added to `gotcha-classes` |
| `memory/map/generated/` | regenerated by `gen_map.py --write` |
| `memory/backlog/TOOL.md` | one row status flip |

### Alternatives rejected

The awk leg the closing review proposed for D1, asserting that the synthesis-death test precedes the
first liveness test in every `note:` chain, and the grep leg it proposed for D2, asserting that every
synthesis prompt interpolates a dead-lens counter. Both were refused by the owner's ruling, and the
backlog row states the reason each fails on its merits rather than on authority. The grep form is the
weaker of the two: a comment containing the counter's name satisfies it, and this repo already carries
a class about a ban that greps whole file text.

## 5. Acceptance criteria

- **AC1** — When `ls memory/gotchas/ | grep degradation` runs, it returns the new record. Today it
  exits non-zero with no output, which is how this criterion fails.
- **AC2** — When `python tools/memory-tree/gotchas.py --check` runs, it exits zero. That covers the
  record's own shape checks and `INDEX.md` freshness together, because index freshness is check 17
  inside the same command and is not a leg with a name of its own.
- **AC3** — When `python tools/memory-tree/gotchas.py --for-paths tools/workflows/tier2-review.js`
  runs, the string `degradation-known-but-unreported` appears in its stdout and the summary line
  counts it among the anchor-selected classes. Today that name appears nowhere in that output. The
  criterion is phrased on the NAME and not on the selected-class count, because the count moves every
  time the catalogue grows and a criterion resting on it would go stale without anybody editing this
  unit. The argument is a FILE, because a file is what `--for-diff` derives from git and therefore
  what the checklist really receives.
- **AC4** — The positive arm, widened. When
  `python tools/memory-tree/gotchas.py --for-paths tools/workflows/drift-audit-code.js` runs, the same
  name appears. One file could be selected by an accident of the basename arm; a second file under the
  same directory anchor is the anchor working.
- **AC5** — The negative, and it is what makes section 4's width argument observable. When
  `python tools/memory-tree/gotchas.py --for-paths tools/memory-tree/gotchas.py` runs, the class name
  does NOT appear. That path is the discriminating case: the REFUSED anchor `tools/` selects it and
  the TAKEN set does not, and it is a plausible member of the family because it is a checker that
  emits counts and a summary line. Re-derived with the shipped `selectable()` before this criterion
  was written. The negative refused alongside it is `memory/DECISIONS.md`, which NEITHER the taken nor
  the refused anchor selects, so it could not fail under either arm and would discriminate nothing —
  the exact defect this build's round-3 audit found in the sibling unit's own acceptance set.
- **AC6** — When `python3 tools/codebase-map/test_codebase_map.py` runs, it exits zero. That is the
  `codebase-map coverage + freshness` leg, and it fails on any inventory key that is neither claimed
  by a dossier nor present in the baseline.
- **AC7** — Two greps, because one command does not make both observations. When
  `grep -n degradation-known-but-unreported memory/map/features/review-harnesses.md` runs it returns
  the claim, and when the same grep runs over `memory/map/baseline.toml` it returns nothing. The
  baseline half is an ABSENCE and not a removal: a key this unit creates was never in that file, and
  its header reserves additions for the initial backfill in as many words.
- **AC8** — When `grep -n closing-diff memory/gotchas/degradation-known-but-unreported.md` runs, it
  returns the S4 evidence citation, and `git ls-files --error-unmatch` resolves the path that citation
  names. S4's whole point is that the evidence is tracked, and no other criterion here reads the
  record's body.
- **AC9** — When the full bar runs with the record staged, the `memory hygiene` leg and the
  `codebase-map coverage + freshness` leg are both green.
- **AC10** — When `grep -n 'TOOL-dTieredTribunal-5 · CLOSED' memory/backlog/TOOL.md` runs, it returns
  the row. Today that row reads `OPEN`, which is how this criterion fails.
- **AC11** — When `grep -n 'TOOL-dTieredTribunal-16' memory/backlog/TOOL.md` runs, it returns the S9
  row, and that row names `tools/workflows/tier2-review.js` as the file carrying the instance.
  Today the grep returns nothing, which is how this criterion fails.

## 6. Gates

Two legs adjudicate this unit. Both are unguarded in `tools/gate-legs.json`, so both arm on every bar.

- `memory hygiene`, which runs `bash tools/memory-tree/check-memory-hygiene.sh`. The gate delegates
  the whole catalogue to `gotchas.py --check`, so checks 17 through 19 reach the record through this
  one leg, and index freshness is check 17 among them rather than a leg of its own.
- `codebase-map coverage + freshness`, which runs `python3 tools/codebase-map/test_codebase_map.py`.
  It carries the S6 claim and the byte-comparison of the committed `memory/map/generated/` artifacts.

The kit self-tests `gotchas selftest`, `memory-hygiene self-test` and `codebase-map kit selftest` are
guarded on kit directories this unit's diff does not touch, so none of them can arm for it. This unit
adds no leg.

## 7. Open questions

- **F1 — does the live residual in `tools/workflows/tier2-review.js` also earn a backlog row.** Found
  while verifying section 4 against source, not carried in from the research record. Its synthesis
  prompt interpolates no liveness counter at base, which is D2's shape in the harness the closing
  review called the reference implementation. D2 as written named only the two drift-audit siblings,
  so this instance was never in any unit's scope and is unfixed today.

  *Option A, the record alone.* The record names it under its evidence as the live instance, which is
  the left-shift M8 asks for and is what this unit already ships. A backlog row would restate a claim
  the record makes, and this corpus has a class about a fact stated in two places.

  *Option B, a row as well.* A gotcha record is a checklist entry and carries no obligation to fix
  anything, so a defect recorded only there is recorded and not tracked. A row is how the fix gets
  scheduled.

  *Recommendation: A.* The record is the mechanism the owner ruled for, it names the instance
  concretely enough that the next harness diff meets it on the checklist, and minting a backlog id is
  outside the id range this run was given. If the owner wants the fix scheduled rather than merely
  named, B costs one row and this unit's scope does not change either way.


  **RESOLVED (agent, 2026-08-26, delegated): the residual earns a row, and this unit writes it.**
  The fork turned on whether anything else in this build closes it. Nothing does, and that is now
  checkable rather than assumed: `TOOL-dTieredTribunal-11` section 5 states in as many words that the
  liveness counters reach the caller and not the record, that the synthesis prompt interpolates
  finding counts only, and that this unit's record IS that disclosure. So the residual survives the
  whole build. A gotcha record describes a CLASS and a backlog row tracks an INSTANCE; the instance
  outlives the build and nothing drains a paragraph. Under M3 the row is the more feature-rich
  survivor — it leaves fewer follow-ups open at the same cost — and it trips no veto, being an
  ordinary record rather than a dependency, a surface or a carrier.
## 8. Revision log

- rev-1 · 2026-08-26 · initial draft. Every claim about existing code re-derived against source at
  base; `tools/`, `memory/gotchas/` and `memory/map/` are byte-identical between `cd971285` and the
  tip this was written at, so the line citations hold at the declared base.
- rev-2 · 2026-08-26 · M3 fork sweep. F1 RESOLVED to write the backlog row rather than let the record
  carry the instance alone, because `TOOL-dTieredTribunal-11` section 5 declines the residual
  explicitly, so no unit of this build closes it. S9 and AC11 are that row and its observation. The
  header gained `ratified 2026-08-26`.


## 9. Reuse audit

The seam is the memory-tree kit's own bug-class catalogue, `memory/gotchas/`, read by
`tools/memory-tree/gotchas.py`. Nothing is built. A record is authored into an existing catalogue, an
existing generator re-renders its index, and an existing dossier claims the key. The dossier that
claims it is `memory/map/features/review-harnesses.md`, whose title names the trust accounting these
harnesses do or do not carry and whose reuse-affordance block already offers `tier2-review.js` as the
reference implementation of every trust counter.

Two neighbouring records were read before writing a new one, because a near-duplicate class is worse
than none. `memory/gotchas/fallback-fabricates-the-passing-value.md` is about a degraded-mode
substitute that happens to BE some assertion's passing value; neither shape here substitutes anything,
and both compute the honest value and then withhold it. `memory/gotchas/armed-but-unreachable-rule.md`
is about a declaration with no possible violator, a population problem in a declared rule; D1 is a live
branch shadowed by an earlier and less serious branch in the same chain, an ordering problem in
control flow. Neither absorbs this class, and this class does not absorb either.

`python tools/codebase-map/reuse_lookup.py "a degraded review run reports a clean bill because its
liveness counters never reach the written report"` returned `gotcha-classes` inventory keys among its
candidates, which is this catalogue, alongside the `review-harnesses` and `agent-cap` affordance
seams. It named no existing record for this class.

Recall terms used with `python tools/memory-recall/query.py`: `false-clean trust counters lensesDead
skepticsDead ternary ordering synthesis dead report degraded gotcha class harness`. The query returned
the closing review's D1 and D2, the backlog row, and the sibling spec that ported the counters. It
surfaced no existing catalogue record for the family, which is a MISS and is the answer this section
needed — it agrees with the direct probe over the catalogue directory.
