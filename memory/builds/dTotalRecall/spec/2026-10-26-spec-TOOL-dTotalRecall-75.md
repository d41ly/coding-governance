# TOOL-dTotalRecall-75 — the kickoff manifest's `last-body-change` is advanced after §B is re-read, so manifest-check's C9 stall count is under ten from step 33

**Status:** OPEN · rev-1 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 33 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-76 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 67 to 70
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-67-spec-audit-round1.md`)
confirmed finding **id 17 at HIGH**, its item **H4**, alone in that item.

`TOOL-dTotalRecall-69` (order 32) re-stamps `last-audit` in `memory/guides/SESSION-KICKOFF.md` so
that manifest-check's C5 passes, and its AC2 requires `manifest-check.sh` to exit 0. The same leg
runs C9 (`skills/session-kickoff/manifest-check.sh:1563-1581`), which calls `fail 9` once
`git rev-list --count --no-merges <last-body-change>..HEAD -- <watch paths>` reaches 10. The
manifest's `last-body-change` is `f221e113556ac8406fcbd834cce37f746c23bd73` (`SESSION-KICKOFF.md:9`).
Fourteen units at order 31 or below edit watched paths, and no unit in the build advances that
value. So unit 69's AC2 cannot pass as designed, and the `kickoff-manifest ratchet` leg stays red.

This unit re-reads §B against the tree, corrects what is stale, and advances `last-body-change` to
a current full sha, which is C9's own remedy. It repairs `TOOL-dTotalRecall-69`, at step 33, one
above that unit's order.

## 2. Scope (IN)

- **S1** — The re-read. The pass re-reads the manifest's front-loaded claims (§B) against the tree
  at the pass base: each watched path's claim, the gate command, the families and the arming conf
  lines. It corrects any that the build's watched edits made stale, in the same commit as S2.
  Observed by AC3.
- **S2** — The advance. `last-body-change` in the `manifest-audit` block reads the full 40-hex sha of
  HEAD at the pass base. Where S1 corrected the body, `last-audit` is re-stamped in the same commit,
  `<ISO datetime> @ <sha>` under the check's `STAMP_SHA_RULE` (`manifest-check.sh:1346`). Observed
  by AC1 and AC2.
- **S3** — The verdict. The checker runs at the tip and prints neither C5's nor C9's failure. Observed
  by AC2.

## 3. Non-goals (OUT)

- The red span of the ratchet leg before step 33, which unit 69 neither names nor covers (id 31):
  the batch `TOOL-dTotalRecall-76`.
- The `last-audit` re-stamp unit 69 makes at step 32, and unit 70's at step 33.
- Any edit of a watched path. `memory/guides/SESSION-KICKOFF.md` is not on the `watch:` line.
- Editing unit 69's spec, frozen once its unit builds at order 32.
- The checklist item the report suggests as the left-shift gate: the close's left-shift step
  (BUILD-METHOD M8).

### Edges

- **consumes-from** `TOOL-dTotalRecall-69` — its `last-audit` re-stamp at step 32, after which C9 is the remaining failure of the ratchet leg this unit clears

## 4. Design

### The two checks the leg runs

C5 compares W, the newest watched commit since `last-audit`'s sha, with S, the newest commit that
changed the `last-audit` value, and requires W to be an ancestor of S or equal to it
(`manifest-check.sh:1453-1478`). C9 counts non-merge watched commits since `last-body-change` and
fails at 10, or at 90 days (`:1574-1581`). Unit 69 answers C5. This unit answers C9.

PINNED, measured 2026-10-26 at `addc4073e`: the C9 count since `f221e113` is 2. Units 1, 5, 8, 9,
11, 15, 18, 19, 21, 22, 26, 52, 53 and 65 each edit a watched path by their Files touched, the
audit's join, so the count passes 10 before step 32.

### The advance

`last-body-change` names the commit where the manifest body was last revised (the `RETROFIT` text,
`manifest-check.sh:1347`). C9's remedy reads "re-read §B and advance last-body-change to a current
sha". The value is HEAD at the pass base, because the pass's own commit sha is not known before it
is made. SESSION-KICKOFF.md is not watched, so the advance moves neither C5's W nor C9's count.

### Order inside step 33

`TOOL-dTotalRecall-70` shares step 33 and also writes `memory/guides/SESSION-KICKOFF.md`, for its
S12 re-stamp. The two passes are not disjoint, and BUILD-METHOD M6 sequences them in either order.
Unit 70's edit of `check-memory-hygiene.sh` adds at most its own pass commits to the count, so the
count stays under 10 at step 33's tip whichever runs first. `TOOL-dTotalRecall-73` shares the step
and writes no manifest.

### Inventory

Minted: nothing.

### Files touched (estimate)

- `memory/guides/SESSION-KICKOFF.md`

### Alternatives rejected

- **Advance `last-body-change` once at the close.** The leg stays red from step 33 to the close, and
  a pass that needs its verdict reads a red that is not its own.
- **Advance it without re-reading §B.** C9 exists to make the body be re-read. A blind advance clears
  the count and leaves the claims unverified, the failure the check names.
- **Raise C9's threshold.** That is a change to a governance carrier's checker, which no clause of
  this build names.

## 5. Production-readiness checklist

- security — no surface. The value lives in a governance carrier, changed under the README's grant
  (§8 F1).
- perf / scale — none.
- error / empty / loading states — a value that is not a full 40-hex sha, or not an ancestor of
  HEAD, is C9's own `fail 9`, which AC2 reads.
- observability — the commit's `Decided:` trailer names the grant and the count it cleared.
- risks — later watched edits raise the count again. Units after step 33 edit few watched paths, and
  the batch's own edits re-read §B under its item for id 18.
- testing — AC1 to AC3 by the pass.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When `git rev-list --count --no-merges <last-body-change>..HEAD -- <each path of the watch: line>`
  runs at this pass's tip, it prints a value under 10, and
  `git merge-base --is-ancestor <unit 69's pass commit> <last-body-change>` exits 0. The pass commit
  is `git log --reverse --format=%H --grep='^Pass: TOOL-dTotalRecall-69$' 462d20f3..HEAD`'s first
  line.
  Red when: the value still names a commit before unit 69's pass.
  figure: the count is DERIVED at the tip; the base value 2 is PINNED in §4, measured 2026-10-26.
- **AC2** — When `bash skills/session-kickoff/manifest-check.sh` runs at this pass's tip, it exits 0
  and prints no line holding `fail 9` or `watched files changed since last-audit`.
  Red when: C9 counts ten or more watched commits, or C5 names a watched file.
- **AC3** — When `git show <this unit's pass commit> -- memory/guides/SESSION-KICKOFF.md` runs, its
  diff changes the `last-body-change:` line. The commit's `Decided:` trailer names each §B claim it
  re-read, and each it corrected or `none corrected`.
  Red when: the stamp moved and no re-read is recorded.

## 7. Gates

`kickoff-manifest ratchet` · `memory hygiene` · `recall floor` · `recall floor arms`

No new arm: the ratchet leg exists, and this unit moves a value it reads.

## 8. Open questions

- **F1 — May this unit advance `last-body-change` in `memory/guides/SESSION-KICKOFF.md`, a
  governance carrier?** Options: (a) yes, under the build's grant, the advance following the build's
  watched edits after §B is re-read; (b) no, leaving the `kickoff-manifest ratchet` leg red on C9
  from the tenth watched commit to the close. (b) fails AC2. RESOLVED (agent, 2026-10-26, delegated):
  (a), rung 5, the README's `may:` grant, as `TOOL-dTotalRecall-69` §8 F1 and `TOOL-dTotalRecall-60`
  §8 F2 used it. grants: PLAY-dClosedLoop-3 SESSION-KICKOFF.md's last-body-change follows the build's
  watched edits · widens: none · relaxes: none
- **F2 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-19`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 67 to 70, id 17
  (HIGH, item H4).

## 10. Reuse audit

The seam is the manifest's own ratchet: C9 (`skills/session-kickoff/manifest-check.sh:1563-1581`)
states the condition and its remedy, and `TOOL-dTotalRecall-69` with `TOOL-dTotalRecall-60` S22 set
the in-build precedent for moving a stamp under the grant.
`python tools/codebase-map/reuse_lookup.py "re-stamp the kickoff manifest last-audit after a watched file changes"`
ranked name-stem neighbours (`manifest`, `stamp`, `audit`) and no stamp helper. The value is written
by hand, as every stamp in `git log -- memory/guides/SESSION-KICKOFF.md` was. No existing seam fits
beyond the check and the precedent.

Recall terms used: `python tools/memory-recall/query.py "how is the kickoff manifest last-body-change advanced after watched files change" --terms "kickoff manifest last-body-change C9 stall watched re-read ratchet SESSION-KICKOFF grant may"`
