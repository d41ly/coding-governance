# TOOL-dTotalRecall-69 — the kickoff manifest's `last-audit` is re-stamped over unit 65's `.memory-tree.conf` edit, so the manifest ratchet is green from step 32

**Status:** OPEN · rev-2 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 32 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 |
| [2026-10-26-review-TOOL-dTotalRecall-67-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-67-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-70 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 61 to 66
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-61-spec-audit-round1.md`)
confirmed finding **id 21 at HIGH**, its item **H3**, alone in that item. The `watch:` list of
`memory/guides/SESSION-KICKOFF.md` (`:6`) includes `.memory-tree.conf`. `TOOL-dTotalRecall-60`
(order 31) S22 re-stamps `last-audit` over unit 52's edit of that file, under its §8 F2 grant.
`TOOL-dTotalRecall-65` builds after unit 60 in the same step and adds `census-kept-paths.txt` to
`PROJECT_REGISTRY_EXTRA` in that file. It names no re-stamp, no manifest leg and no grant.
manifest-check's C5 (`skills/session-kickoff/manifest-check.sh:1462-1473`) then calls `fail 5`,
because a watched file changed with no re-stamp at or after the change. The `kickoff-manifest
ratchet` row of `tools/gate-legs.json` carries no guard, so the bar is red on every run from unit
65's pass to the close.

This unit re-stamps `last-audit` after unit 65's edit, under the README's `may:` grant, as unit 60
F2 did. It repairs `TOOL-dTotalRecall-65`, at step 32, one above that unit's order.

## 2. Scope (IN)

- **S1** — The re-check. Before stamping, the pass re-reads the manifest's front-loaded claims
  derived from `.memory-tree.conf` (the families and the arming conf lines, `SESSION-KICKOFF.md:125`
  and `:131`) against the conf at the pass base. It corrects any that unit 65's edit made stale, as
  C5's own remedy text asks. Observed by AC3.
- **S2** — The re-stamp. The `last-audit` value in the `manifest-audit` block reads
  `<ISO datetime> @ <sha>`, where `<sha>` is HEAD at the stamp (the check's `STAMP_SHA_RULE`,
  `manifest-check.sh:1346`). It is committed as its own change of that value, after unit 65's pass
  commit. Observed by AC1 and AC2.
- **S3** — Nothing else in step 32 moves a watched path. `TOOL-dTotalRecall-66` and
  `TOOL-dTotalRecall-68` name no path of the `watch:` list in their Files touched, so the stamp holds
  until step 33. There the batch `TOOL-dTotalRecall-70` bundles its own re-stamp with its edit of
  `check-memory-hygiene.sh` (id 24). Observed by AC1.

## 3. Non-goals (OUT)

- Any edit of `.memory-tree.conf`, or of another watched file.
- The spec-lint rule the report suggests, which reds a spec that edits a watched path and names no
  re-stamp: the close's left-shift step (BUILD-METHOD M8).
- The batch's own re-stamp at step 33: `TOOL-dTotalRecall-70`'s.

### Edges

- **consumes-from** `TOOL-dTotalRecall-65` — its `.memory-tree.conf` edit at step 31, the watched change this stamp follows; without that pass there is nothing to re-audit
- **hands-off** `TOOL-dTotalRecall-75` — the ratchet leg after this re-stamp, whose C9 stall that unit clears by advancing `last-body-change` at step 33 (the round-1 audit of units 67 to 70, id 17)
- **hands-off** `TOOL-dTotalRecall-76` — its AC1 pair and the steps its argument left unnamed, which that batch answers by running the checker at each pass commit (the round-1 audit of units 67 to 70, ids 16, 31)

## 4. Design

### Why a unit after unit 65, and not a move of unit 60's stamp

Unit 65 consumes unit 60 by a §3 edge, for the reasons unit 60's S26 grades. So unit 60 builds first
in step 31, and its re-stamp cannot follow unit 65's edit. Moving it would make unit 60 consume
unit 65, a cycle. The first step after unit 65 is 32.

### The observation

C5 compares two commits. W is the newest commit touching a watched path. S is the newest commit
that changed the `last-audit` value. W must be an ancestor of S, or equal to it. AC1 reads the same
pair without running the leg. AC2 runs the checker directly, as `TOOL-dTotalRecall-60` AC22 does.

### Inventory

Minted: nothing.

### Files touched (estimate)

- `memory/guides/SESSION-KICKOFF.md`

### Alternatives rejected

- **Amend unit 65's spec to carry the re-stamp.** Unit 65 builds at order 31, before this unit.
- **Re-stamp once at the close.** The bar would stay red across steps 31 to the close. A unit pass
  between those steps that needed the leg's verdict would read red for a reason that is not its own.

## 5. Production-readiness checklist

- security — no surface. The stamp is a value in a governance carrier, changed under the README's
  grant (§8 F1).
- perf / scale — none.
- error / empty / loading states — a stamp naming a commit before unit 65's pass is AC3's red.
- observability — the commit's `Decided:` trailer names the grant and the watched change it follows.
- risks — a later watched edit makes the stamp stale again. S3 names the one such edit, at step 33,
  and its owner.
- testing — AC1 to AC3 by the pass.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When `git merge-base --is-ancestor <W> <S>` runs at this pass's tip, it exits 0. W is
  `git rev-list -1 HEAD -- <each path of the watch: line>` and S is
  `git log -1 --format=%H -G'^last-audit:' -- memory/guides/SESSION-KICKOFF.md`.
  Red when: a watched path moved after the newest change of the stamp.
- **AC2** — When `bash skills/session-kickoff/manifest-check.sh` runs at this pass's tip, it exits
  0.
  Red when: C5 names `.memory-tree.conf`.
- **AC3** — When `git merge-base --is-ancestor <unit 65's pass commit> <the sha after @ in last-audit>`
  runs at this pass's tip, it exits 0. The pass commit is
  `git log --reverse --format=%H --grep='^Pass: TOOL-dTotalRecall-65$' 462d20f3..HEAD`'s first line.
  Red when: the stamp names a commit before unit 65's edit.

## 7. Gates

`kickoff-manifest ratchet` · `memory hygiene` · `recall floor` · `recall floor arms`

No new arm: the ratchet leg exists, and this unit moves a value it reads.

## 8. Open questions

- **F1 — May this unit re-stamp `memory/guides/SESSION-KICKOFF.md`, a governance carrier?** Options:
  (a) yes, under the build's grant, the stamp following unit 65's edit of a watched file; (b) no,
  leaving the `kickoff-manifest ratchet` leg red from unit 65's pass to the close. (b) fails AC2.
  RESOLVED (agent, 2026-10-26, delegated): (a), rung 5, the README's `may:` grant, as
  `TOOL-dTotalRecall-60` §8 F2 used it. grants: PLAY-dClosedLoop-3 SESSION-KICKOFF.md's last-audit
  stamp follows unit 65's `.memory-tree.conf` edit · widens: none · relaxes: none
- **F2 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-19`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 61 to 66, id 21
  (HIGH, item H3).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-75, TOOL-dTotalRecall-76, each the other end of an edge a unit the round-1 spec audit of units 67 to 70 promoted wrote; nothing else moved.

## 10. Reuse audit

The seam is the manifest's own ratchet. `manifest-check.sh` C5 (`:1462-1473`) states the condition,
and `TOOL-dTotalRecall-60` S22 and §8 F2 set the in-build precedent this unit repeats one step
later. `python tools/codebase-map/reuse_lookup.py "re-stamp the kickoff manifest last-audit after a watched file changes"`
ranked name-stem neighbours (`manifest`, `stamp`, `audit`) and no re-stamp helper. The stamp is
written by hand, as every re-stamp in `git log -- memory/guides/SESSION-KICKOFF.md` was (`6d2ed123a`,
`e634ce986`). No existing seam fits beyond the check and the precedent.

Recall terms used: `python tools/memory-recall/query.py "how is the kickoff manifest re-stamped after a unit edits a watched file" --terms "kickoff manifest last-audit re-stamp watched C5 ratchet SESSION-KICKOFF memory-tree.conf grant may"`
