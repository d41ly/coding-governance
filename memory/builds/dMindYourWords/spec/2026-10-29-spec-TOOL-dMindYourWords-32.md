# TOOL-dMindYourWords-32 — a graft point's added set is its real diff, never its whole tree

**Status:** OPEN · rev-1 · 2026-10-29 · node d · Tier-2 · base ccd1292e · streams tooling · order 8

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md) | journal | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 TOOL-dMindYourWords-22 TOOL-dMindYourWords-23 TOOL-dMindYourWords-24 TOOL-dMindYourWords-25 TOOL-dMindYourWords-26 TOOL-dMindYourWords-27 TOOL-dMindYourWords-28 TOOL-dMindYourWords-29 TOOL-dMindYourWords-30 TOOL-dMindYourWords-31 TOOL-dMindYourWords-33 TOOL-dMindYourWords-34 TOOL-dMindYourWords-35 TOOL-dMindYourWords-36 TOOL-dMindYourWords-37 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 23 of `reviews/2026-10-29-review-TOOL-dMindYourWords-22-to-29-spec-audit-round1.md`,
HIGH, which shares item H1 with ids 1 (TOOL-dMindYourWords-30) and 11 (TOOL-dMindYourWords-31).
TOOL-dMindYourWords-28 S3 has `read_vocabulary_record(root, tags, rev=<commit>)` read "the records that
commit adds" with `git diff-tree --root`, so a commit grafted onto no parent reads as adding its whole
tree, and any row blamed to it is admitted by any record the tree holds. This unit makes the reader diff
each commit against its real parents, so a graft point adds only what it truly added.

## 2. Scope (IN)

- **S1** — The pin on the added-set read. The `rev=<commit>` mode of `read_vocabulary_record` in
  `tools/lexicon/lexicon_conf.py` (TOOL-dMindYourWords-11 S1, its root case TOOL-dMindYourWords-28 S3)
  runs its `git diff-tree` as `git --no-replace-objects diff-tree ...` with `GIT_GRAFT_FILE=/dev/null` in
  its environment, whatever other flags that command carries. A replace ref or a graft file then
  leaves every real parent in place, and only a commit with no parent in the object store reads as
  adding its whole tree. Observed by AC1 and AC2.
- **S2** — The root case kept. A true root commit still adds exactly its own tree under `--root`, so unit
  28 AC2's row written with its record in the repository's first commit is judged as before. Observed by
  AC3.
- **S3** — A missing real parent raises. When the pinned `diff-tree` exits non-zero, for instance
  because a parent object the replacement hid is absent from the store, the reader raises an error
  naming the commit and git's first stderr line, rather than returning no record or every record; the
  provenance join's existing refusal for a failed git read (unit 28 §5) prints it. Observed by AC4.

## 3. Non-goals (OUT)

- The provenance blame, which decides which commit a row is judged against: TOOL-dMindYourWords-30 (id
  1).
- Which paths a commit with a parent counts as added, `--diff-filter=A`: TOOL-dMindYourWords-33 (id 12).
- One spelling of the pin for the whole kit: TOOL-dMindYourWords-31 (id 11), which folds this call's pin
  and unit 30's into one helper.
- Kit version constants: minted at landing (`tools/push-main.sh:26-31`), so this unit moves none.

### Edges

- **consumes-from** `TOOL-dMindYourWords-28` — S3's `diff-tree --root` added set for a commit; without it there is no root-commit read to pin
- **hands-off** `TOOL-dMindYourWords-31` — the pinned added-set read, whose inline pin that unit replaces with the kit's one helper

## 4. Design

### Evidence

- Unit 28 S3 spells `git diff-tree --root -r --name-only --no-commit-id <commit>` and calls its output
  "the records that commit adds" (`spec/2026-10-29-spec-TOOL-dMindYourWords-28.md` S3).
- Measured on git 2.54.0 in a fixture under `%TEMP%` whose second commit adds `rec.md` over a first
  commit holding `reg.txt`: after `git replace --graft <c2>`, `git diff-tree --root -r --name-only
  --no-commit-id <c2>` printed `rec.md` and `reg.txt`, and the same with `--no-replace-objects` printed
  `rec.md` alone. With a `.git/info/grafts` line instead, `--no-replace-objects` still printed both, and
  `GIT_GRAFT_FILE=/dev/null` printed `rec.md` alone. PINNED 2026-10-29.
- The pin is the repository's policy for a history read (`tools/memory-tree/tree_lib.py:232-243`); the
  kit imports no sibling, so it is carried at the call.

### Inventory

Minted: none.

### Rollout

Live at landing, one order after TOOL-dMindYourWords-28 and beside TOOL-dMindYourWords-30 and -33, each
a separate change to its own read; none consumes another.

### Files touched (estimate)

- `tools/lexicon/lexicon_conf.py`: S1, S2, S3
- `tools/lexicon/selftest.py`: the arm of §7

### Alternatives rejected

- **Refuse any parentless commit that is not in `git --no-replace-objects rev-list --max-parents=0
  HEAD`**: it needs a second spawn per judged commit and still reads a graft-file root wrongly unless
  the graft file is pinned too, which makes the spawn redundant.
- **Read the added set through `git log -1 --diff-filter=A`**: `log` honours the same replace refs and
  graft file, so it changes the spelling and not the answer.

## 5. Production-readiness checklist

- security — deny by default: a graft can no longer make a commit "add" a record it never added.
- perf / scale — unchanged: one `diff-tree` per judged commit; the pin is a flag and a variable.
- error / empty / loading states — S3: a failed pinned read raises, so the join reds and never reads
  absence as either answer.
- observability — the join's refusal names the commit and git's first stderr line.
- risks — none beyond S3's refusal on a store that lacks a hidden parent.
- testing — AC1 to AC4 and the arm of §7.
- migration — none.
- user docs — N/A — TOOL-dMindYourWords-30 S3 states the pin in the kit README for both reads.

## 6. Acceptance criteria

- **AC1** — When `python -c` imports `lexicon_conf` from `tools/lexicon/` and calls
  `read_vocabulary_record(root, ("unit.lexicon.suppressions",), rev="<c2>")` in a fixture whose first
  commit adds a suppressions record and whose second commit adds only a registry row and is grafted onto
  no parent with `git replace --graft <c2>`, it prints a falsy result.
  Red when: the graft point reads as adding the first commit's record.
  fixture: the repository under `%TEMP%/<short>`.
- **AC2** — When the same fixture carries the graft as a `.git/info/grafts` line instead, the same call
  prints a falsy result.
  Red when: only `--no-replace-objects` was added and the graft file still empties the parent list.
- **AC3** — When AC1's `read_vocabulary_record` call names the first commit of a fixture whose root
  commit adds both the row and its record, it prints a truthy result.
  Red when: the pin breaks the true root's whole-tree added set.
- **AC4** — When AC1's call runs in a copy of the fixture whose first commit's loose object was removed
  after the replace, wrapped in `try`/`except Exception as e: print("raised", e)`, it prints `raised`
  and the second commit's sha.
  Red when: the failed read returns a falsy or truthy result instead of raising.
  fixture: the loose object removed with `rm` under `.git/objects/`, the repository under
  `%TEMP%/<short>`.

## 7. Gates

`lexicon naming predicates` · `lexicon selftest` · `codebase-map kit selftest`

New arm: tools/lexicon/selftest.py · covers AC1 AC2 AC3 · the replace-ref, graft-file and root-commit fixtures, its failing case the pin cut out of the `rev` read, under which AC1's call returns the first commit's record · none

## 8. Open questions

- **F1 — What does a graft point add?** Options: (a) its real diff, read under the repository's pin;
  (b) its whole tree, refused unless it is a true root by a second `rev-list` spawn; (c) its whole tree,
  as unit 28 S3 reads it now. (c) is the defect, and (b) costs a spawn per commit to reach (a)'s answer
  only once the graft file is pinned as well. RESOLVED (agent, 2026-10-29, delegated): (a), rung 3, the
  pin `tools/memory-tree/tree_lib.py:232` already states. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-29 · initial draft, promoted from review id 23 (HIGH, item H1, shared with ids 1 and
  11) of the round-1 audit of units 22 to 29.

## 10. Reuse audit

The seam is the repository's history pin, `build_git_env` (`tools/memory-tree/tree_lib.py:232-243`),
carried at the call because the lexicon kit imports no sibling, on the reader TOOL-dMindYourWords-11
adds to `tools/lexicon/lexicon_conf.py`. `python tools/codebase-map/reuse_lookup.py "ignore git replace
objects and grafts before trusting a history read"` ranked generic git readers and `build_git_env`, and
no added-set reader that already pins; no existing seam fits the read itself beyond the one it changes.

Recall terms used: `python tools/memory-recall/query.py "how does a git history reader stay honest when replace refs graft a commit onto no parent" --terms "graft replace no-replace-objects blame porcelain root boundary provenance diff-tree added shallow history"`
