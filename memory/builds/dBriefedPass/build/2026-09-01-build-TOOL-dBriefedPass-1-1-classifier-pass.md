# TOOL-dBriefedPass-1 — the classifier pass, and the corpus measurement that graded it

**Serves:** journal TOOL-dBriefedPass-1

*Node `d`, 2026-09-01, unattended prompt-mode run under a standing mandate. Every token below names
the command that produced the observation.*

## What was measured, before and after

The unit's real witness is not a fixture. It is a controlled before/after over the whole tracked
spec corpus, driving BOTH readers — the shipped one from the worktree and the pre-fix one from
`git show HEAD:tools/unattended/unattended.sh` — sliced out of real bytes rather than retyped, with
a liveness assertion that refuses if either slice grades nothing.

```
specs graded: 401 (tier-1-shaped 4, tier-2-shaped 397)
regraded:       4 (tier-1 4, tier-2 0)
REGRADE tier-1 FORKED -> READY  memory/builds/aWrittenMethod/spec/2026-08-11-spec-aWrittenMethod-3.md
REGRADE tier-1 FORKED -> READY  memory/builds/aWrittenMethod/spec/2026-08-11-spec-aWrittenMethod-5.md
REGRADE tier-1 FORKED -> READY  memory/builds/dTieredTribunal/spec/2026-08-26-spec-dTieredTribunal-15.md
REGRADE tier-1 FORKED -> READY  memory/builds/dTieredTribunal/spec/2026-08-26-spec-dTieredTribunal-2.md
```

Every regrade is a Tier-1 spec and every one is the removal of a false `FORKED`. No Tier-2 spec
moved, which is the claim AC4 makes and the one a title-keyed rewrite could most easily have broken.

**The section titles were enumerated before the predicate was written**, because a title match over a
corpus with variant spellings would have silently under-selected:
`git grep -h "^## [0-9]*\. <title>"` returns 393 `## 2. Scope (IN)`, 389 + 4 `Acceptance criteria`,
387 + 4 `Gates`, 392 + 4 `Open questions`, with no variant spelling in any of the four.

## The half that was quiet, and why it mattered more

The backlog row that reported this defect named the loud half: every Tier-1 spec graded `FORKED`,
because the ordinal reader took `## 8. Revision log` as the open-questions section and a revision log
has bullets and no conforming mark. The quiet half was not in that row and is worse. The acceptance
slot was filled by the `Gates` section, so **a Tier-1 spec stating no acceptance criterion at all
graded `READY`** — a THIN predicate that could not fail on an entire spec shape, in the classifier
whose THIN branch is what `build-complete` reads to decide a landing.

## Evidence

**Evidences:** TOOL-dBriefedPass-1
- AC1 — `bash tools/unattended/unattended.sh --plan dTieredTribunal` — `TOOL-dTieredTribunal-15` and
  `TOOL-dTieredTribunal-2` printed `DONE (FORKED)` before the change and print `DONE` after it. Both
  rows are in the regrade table above.
- AC2 — `scratchpad/arms.sh` — a Tier-1 fixture with an empty `## 5. Acceptance criteria` grades
  `THIN`. Observed RED first against the pre-fix bytes via `scratchpad/arms-old.sh`, which graded the
  same fixture `FORKED` — that is, it never reached the acceptance question at all.
- AC3 — `scratchpad/arms.sh` — a Tier-1 fixture whose `## 8. Revision log` carries bullets and whose
  `## 7. Open questions` reads `none` grades `READY`. RED against the pre-fix bytes: `FORKED`.
- AC4 — `scratchpad/regrade.sh` — 397 Tier-2-shaped specs, 0 regraded, table above.
- AC5 — `scratchpad/arms.sh` — two arms over a spec carrying two `Acceptance criteria` headings:
  filled-first grades `READY`, empty-first grades `THIN`. Both arms, so a reader that always took the
  last would fail one. **This pair does NOT discriminate against the pre-fix reader** and the test
  file says so in a comment: the ordinal reader could not match a second `## 9. Acceptance criteria`
  at all, so these arms pin a rule that title keying makes newly expressible rather than a behaviour
  that changed.
- AC6 — `wc -c` — `memory/guides/BUILD-METHOD.md` 24560 → 24553 and
  `tools/memory-tree/BUILD-METHOD.template.md` 24571 → 24564, both under the 24576 cap and both
  smaller than before. The M2 edit was priced at +20 bytes in its first wording, which broke both
  files, and was re-worded to −7; the surviving line is 103 characters, identical to the length of
  the line it replaced, so the line-length leg cannot newly fire on it.
- AC7 — `bash tools/memory-tree/kit-dogfood-parity.test.sh` — `kit-parity: shipped and installed docs
  agree (3 pairs, rendered for 'tools/memory-tree')`.
- AC8 — `grep -n "^2\. \*\*THIN\*\*\|^3\. \*\*FORKED\*\*"` over both halves — the THIN line names
  `Scope`, `Acceptance criteria` and `Gates`, the FORKED line names `Open questions`, and neither
  carries a `§`-prefixed ordinal. RED before the edit: both lines read `§2 Scope, §6 Acceptance or §7
  Gates` and `§8 Open questions`.

## What this pass did NOT verify, stated rather than left to be discovered

The arms in `tools/unattended/unattended.test.sh` were WRITTEN and their logic was proven by driving
the same fixtures through the sliced predicate standalone. **The suite itself was not run.** A
standing owner instruction on this node forbids running the unattended kit self-tests, and the
2026-08-23 ruling took those seven suites off the merge bar, so no leg would have run them either.
The arms are therefore covered by an equivalent standalone execution and not by their own harness,
and that distinction is recorded here because a green suite is not what happened.

`bash tools/unattended/check-unattended.sh` exits 0. It emits a check-23 warning naming
`TOOL-aClosedDocket-3` and `tools/unattended/unattended.test.sh` — a concurrent run's open dispatch
declaring a file this pass also wrote. Reproduced in a clean clone at `HEAD` before this pass's
changes existed, so it is that run's row and not this diff's.
