# TOOL-dMindYourWords-49 — the merge walk and the branch's first-parent walk read the real graph

**Status:** OPEN · rev-1 · 2026-10-29 · node d · Tier-2 · base ccd1292e · streams tooling · order 21

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md) | journal | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 TOOL-dMindYourWords-22 TOOL-dMindYourWords-23 TOOL-dMindYourWords-24 TOOL-dMindYourWords-25 TOOL-dMindYourWords-26 TOOL-dMindYourWords-27 TOOL-dMindYourWords-28 TOOL-dMindYourWords-29 TOOL-dMindYourWords-30 TOOL-dMindYourWords-31 TOOL-dMindYourWords-32 TOOL-dMindYourWords-33 TOOL-dMindYourWords-34 TOOL-dMindYourWords-35 TOOL-dMindYourWords-36 TOOL-dMindYourWords-37 TOOL-dMindYourWords-38 TOOL-dMindYourWords-39 TOOL-dMindYourWords-40 TOOL-dMindYourWords-41 TOOL-dMindYourWords-42 TOOL-dMindYourWords-43 TOOL-dMindYourWords-44 TOOL-dMindYourWords-45 TOOL-dMindYourWords-46 TOOL-dMindYourWords-47 TOOL-dMindYourWords-48 TOOL-dMindYourWords-50 TOOL-dMindYourWords-51 TOOL-dMindYourWords-52 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 22 of `reviews/2026-10-29-review-TOOL-dMindYourWords-30-to-37-spec-audit-round1.md`,
HIGH, which shares item H2 with ids 3 (TOOL-dMindYourWords-47) and 21 (TOOL-dMindYourWords-48).
TOOL-dMindYourWords-36 widens the contract walk to `git log --full-history --format='%H %P'` and reads
each parent's rows, and hands the pin on those reads to unit 31, which builds before it at the same
order and never names them. TOOL-dMindYourWords-37 S17 rewrites the branch's added set as `git log
--first-parent --no-merges … <base>..HEAD` and names no pin either. Under a graft, `%P` and the
first-parent chain are the substituted parents: the merge walk can make a resolution-made row look
composed, and the branch walk can count a default-branch record as the branch's own. This unit moves
both walks onto `run_git` and observes each under a graft.

## 2. Scope (IN)

- **S1** — The merge walk. Every git spawn of `check_contract_record` (TOOL-dMindYourWords-29 S31 as
  TOOL-dMindYourWords-36 S1 widens it), the `log --full-history --format='%H %P'` listing and each
  read of a commit's or a parent's `.lexicon.conf` among them, calls `run_git`. Observed by AC1 and
  AC3.
- **S2** — The branch walk. Every git spawn of `read_branch_added_paths` (TOOL-dMindYourWords-26 S1, in
  the first-parent form TOOL-dMindYourWords-37 S17 gives it) calls `run_git`. Observed by AC2 and AC3.

## 3. Non-goals (OUT)

- The per-parent `diff-tree` of `read_vocabulary_record` for a merge: it is a spawn of that reader,
  which TOOL-dMindYourWords-47 S2 moves.
- The merge-loss guard, the signals, the rename map and the index read: TOOL-dMindYourWords-48.
- A branch-walk rule for merges the branch makes: review id 37, the minors batch
  TOOL-dMindYourWords-52.
- Kit version constants: minted at landing (`tools/push-main.sh:26-31`), so this unit moves none.

### Edges

- **consumes-from** `TOOL-dMindYourWords-47` — `run_git`, the runner both walks move onto
- **consumes-from** `TOOL-dMindYourWords-41` — `build_graft_fixture`, through which AC1 and AC2 stage their grafts with the control in force
- **consumes-from** `TOOL-dMindYourWords-36` — S1's merge-visiting walk and its parent reads, whose pin that unit handed to unit 31
- **consumes-from** `TOOL-dMindYourWords-37` — S17's first-parent form of `read_branch_added_paths`, built before this unit at the same order
- **hands-off** `TOOL-dMindYourWords-50` — the moved walks, which that unit's inventory finds inside `run_git` calls and nowhere else

## 4. Design

### Evidence

- Unit 36 S1 spells `git log --full-history --format='%H %P' -- .lexicon.conf` and its §3 hands "the
  history pin on the walk's reads" to TOOL-dMindYourWords-31
  (`spec/2026-10-29-spec-TOOL-dMindYourWords-36.md` S1, §3); unit 31 S3 names the walk of unit 29 S31
  only (`spec/2026-10-29-spec-TOOL-dMindYourWords-31.md` S3), and unit 31 builds first, both at order
  20.
- Unit 37 S17 spells `git log --first-parent --no-merges -M --diff-filter=A --name-status -z --format=
  <base>..HEAD` (`spec/2026-10-29-spec-TOOL-dMindYourWords-37.md` S17) and names no pin.
- The order-21 group builds in id order (`tools/workflows/unattended-build.js:608-613`), so unit 37's
  rewrite of `read_branch_added_paths` is in the tree when this unit moves its spawn.

### Inventory

Minted: none.

### Rollout

Live at landing, after TOOL-dMindYourWords-37 and -47 at the same order, which sort first.

### Files touched (estimate)

- `tools/lexicon/lexicon.py`: S1, S2
- `tools/lexicon/selftest.py`: the arm of §7

### Alternatives rejected

- **Reordering unit 36 before unit 31**, the report's first route: it re-sequences landed specs, and it
  would still leave unit 37's rewrite outside any pin.
- **A pin per walk, spelled at each spawn**: the per-call-site shape unit 47 retires.

## 5. Production-readiness checklist

- security — closes the graft half of the contract-record bypass and of the widened-row admission: no
  substituted parent can make a resolution's row look composed or another branch's record look added.
- perf / scale — none: the same spawns.
- error / empty / loading states — each walk keeps its own handling.
- observability — unchanged; each refusal still names the commit.
- risks — none beyond unit 47's.
- testing — AC1 to AC3 and the arm of §7.
- migration — none.
- user docs — N/A — internal.

## 6. Acceptance criteria

- **AC1** — When `python <kit>/lexicon.py` runs in unit 36 AC1's fixture, an evil merge whose resolution
  writes a `CONTRACTS:` row with no record, with an older `unit.lexicon.contracts` record in one parent's
  history, after `build_graft_fixture` grafts the merge onto no parent, it exits 1 naming `CONTRACTS
  changed with no change record` and the merge's sha8, as the ungrafted fixture does; once for a
  replace ref and once for a graft file.
  Red when: the walk reads the grafted merge as a root commit adding the whole tree, and the old
  record admits the row.
  fixture: a scratch repository under `%TEMP%/<short>`, no `core.hooksPath`.
- **AC2** — When unit 37 AC17's fixture, a branch citing in a `widened:<record>` row a record a
  default-branch commit `D` added, has its first branch commit grafted onto `D` with
  `build_graft_fixture`, `python <kit>/lexicon.py` exits 1 naming `record not added by this branch`, as
  the ungrafted fixture does.
  Red when: the first-parent walk follows the graft into `D` and counts its record as the branch's.
  fixture: the bare origin and clone of unit 37's `build_compare_base_fixture` under `%TEMP%/<short>`.
- **AC3** — When `python -c` parses `tools/lexicon/lexicon.py` with `ast` and lists, inside
  `check_contract_record` and `read_branch_added_paths`, each call whose function is `subprocess.run`
  with a first argument beginning `"git"`, it prints none, and both call `run_git`.
  Red when: either walk still spawns git on its own.

## 7. Gates

`lexicon naming predicates` · `lexicon selftest` · `codebase-map kit selftest`

New arm: tools/lexicon/selftest.py · covers AC1 AC2 · an evil merge grafted onto no parent and a branch commit grafted onto a default-branch commit, its failing case each walk's spawn restored to a bare `subprocess.run`, under which AC1 exits 0 · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-29 · initial draft, promoted from review id 22 (HIGH, item H2, shared with ids 3 and
  21) of the round-1 audit of units 30 to 37.

## 10. Reuse audit

The seam is `run_git`, TOOL-dMindYourWords-47's runner; the walks are unit 36's and unit 37's as
written, moved onto it, and the graft fixtures are TOOL-dMindYourWords-41's helper. `python
tools/codebase-map/reuse_lookup.py "route every git history read through one pinned spawn helper"`
ranked `run_git`, `read_git_output` and `build_git_env`, so no new seam is minted.

Recall terms used: `python tools/memory-recall/query.py "how does a kit hold every git history read to the replace and graft pin as a class rather than a list" --terms "graft replace no-replace-objects pinned reader run_git merge walk first-parent parents spawn"`
