# TOOL-dTotalRecall-98 — the restore lists every deleted record with rename detection off, so a record deleted beside a near-copy is put back

**Status:** DEFERRED · rev-1 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 40 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-build-TOOL-dTotalRecall-98-deviation-981.md](../build/2026-10-26-build-TOOL-dTotalRecall-98-deviation-981.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 89 to 92
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-89-spec-audit-round1.md`)
confirmed finding **id 15 at HIGH**, its item **H4**, alone in that item.

`TOOL-dTotalRecall-92` §4 "The restore" lists the records a pass of this build took out of the tree
with `git log --diff-filter=D --format='%H' --name-only 462d20f3..HEAD -- '<build>/*-deviation-*.md'`,
and the records each such commit modified with `git diff --name-only --diff-filter=M`. Both run with
git's default rename detection. A record deleted in the same commit that adds a similar file is shown
as a rename, not a deletion, and deviation records share most of their template. Reproduced
2026-10-26 in a fixture repository: after a `git mv` of one record and one appended line, the listing
printed nothing, and with `--no-renames` it printed the commit and the deleted path. The driver's own
listing passes `--no-renames` for this reason (`tools/workflows/unattended-build.js:602-606`). Unit
92's AC11, "every path it prints exists in the tree", then certifies a restore over a listing that
left the record out.

This unit spells both listings with `--no-renames`, observes the difference on a fixture repository,
and runs the corrected listing over the build after unit 92's pass, putting back any record unit 92's
listing missed. It repairs `TOOL-dTotalRecall-92`, at order 40, one above that unit's 39.

## 2. Scope (IN)

- **S1** — The listing, corrected. §4's `deleted_records` and `modified_records` are unit 92's two
  commands with `--no-renames`. Observed by AC1.
- **S2** — Seen red. In a fixture repository, one commit deletes a record and adds a near-copy under
  another name. `deleted_records` names the deleted path, and unit 92's spelling prints nothing.
  Observed by AC1.
  **Readers:** by name: no name retires, the item deleting only a record of a fixture repository made
  under the system temp directory, whose name no tracked file spells as a reader
  · by value: NO VALUE READERS, the fixture is removed with its repository and no tracked file counts
  or derives from it.
- **S3** — The restore, re-run. After unit 92's pass, every path `deleted_records` prints over
  `462d20f3..HEAD` that is absent from the working tree is put back from `C^` with
  `git checkout "$C^" -- <path>`, together with each record `modified_records` lists for `C`. A path
  is put back only where it is absent and no live record carries its `<n>`. Where either test fails,
  nothing is checked out and the ledger names the path, its commit and the record in the way.
  Observed by AC2.
- **S4** — Unit 92's AC11, recorded. Where S3 put back or named a record, a deviation record of
  `TOOL-dTotalRecall-92` names AC11 as certified over a rename-blind listing and lists each path, with
  the token `audit-89 id 15 s4`, by `TOOL-dTotalRecall-90` §4's recipe, only where
  `has_deviation memory/builds/dTotalRecall/build 92 'audit-89 id 15 s4'` prints 0. Observed by AC2.

## 3. Non-goals (OUT)

- Putting back a record whose path or `<n>` is taken (item M8, id 24): the batch
  `TOOL-dTotalRecall-100`, which reads S3's named conflicts.
- Making a restored duplicate pair one: unit 92's S11, which stands, with the correcting record of
  `TOOL-dTotalRecall-93`.
- The spec lint over probe fences the report suggests as the left-shift gate: the close's left-shift
  step (BUILD-METHOD M8).
- Editing spec 92, frozen once its unit builds.

### Edges

- **consumes-from** `TOOL-dTotalRecall-92` — its restore listing, its AC11 answer and the records its S11 put back, which this unit lists again with rename detection off
- **consumes-from** `TOOL-dTotalRecall-2` — `gov_record.py new deviation`, the door S4's record is written through
- **hands-off** `TOOL-dTotalRecall-100` — each restore S3 refused because the path or its `<n>` was taken, which that batch puts back under a free `<n>` for id 24

## 4. Design

### The listings

```bash
# run from the repository root
PS='memory/builds/dTotalRecall/build/*-deviation-*.md'
deleted_records() {  # range -> "<commit>" then each deviation record that commit deleted, rename detection off
  git log --no-renames --diff-filter=D --format='%H' --name-only "$1" -- "$PS"
}
modified_records() {  # commit -> each deviation record it modified, rename detection off
  git diff --no-renames --name-only --diff-filter=M "$1^" "$1" -- "$PS"
}
```

### The fixture repository

A clone or fixture repository needs a short path on Windows, so it is made under the system temp
directory, for example `%TEMP%/r98`, never inside the worktree and never at a drive root.

```bash
R="$TEMP/r98"; rm -rf "$R"; mkdir -p "$R/memory/builds/dTotalRecall/build"; cd "$R" && git init -q
B=memory/builds/dTotalRecall/build
for i in $(seq 1 12); do echo "- **Field $i:** shared template text, line $i" >> "$B/x-deviation-1.md"; done
git add -A && git -c user.email=f@x -c user.name=f commit -qm one
git mv "$B/x-deviation-1.md" "$B/x-deviation-2.md" && echo "- **Extra:** one" >> "$B/x-deviation-2.md"
git add -A && git -c user.email=f@x -c user.name=f commit -qm two
deleted_records HEAD~1..HEAD
git log --diff-filter=D --format='%H' --name-only HEAD~1..HEAD -- "$PS"
```

PINNED, measured 2026-10-26 with these exact commands and §4's listings under `%TEMP%/r98`:
`deleted_records` printed the second commit's sha and `memory/builds/dTotalRecall/build/x-deviation-1.md`,
and unit 92's spelling printed nothing. The report's skeptic measured the same in its own scratch.

### The restore

For each commit `C` and path `P` that `deleted_records 462d20f3..HEAD` prints, with `P` absent from
the working tree:

1. `ls memory/builds/dTotalRecall/build | grep -- "-deviation-<n>\.md$"`, where `<n>` is the number in
   `P`'s stem, prints nothing; else the ledger names `P`, `C` and the record printed, and `P` is left
   out.
2. `git checkout "$C^" -- "$P" $(modified_records "$C")` puts back `P` and the records `C` appended to.

The bytes are git's; nothing is retyped.

### Why order 40

Unit 92 restores at order 39, so the corrected listing reads the tree that unit left.

### Inventory

Minted: the functions `deleted_records` and `modified_records`, spec text only; restored records only
where unit 92's listing missed one; at most one deviation record of `TOOL-dTotalRecall-92`. Naming
cell: none, no product symbol minted.

### Files touched (estimate)

- `memory/builds/dTotalRecall/build/` (this unit's acceptance ledger, the restored records and the record of S4)

### Alternatives rejected

- **Raise the rename threshold with `-M100%`.** A record moved with no byte changed is still read as a
  rename, which is a deletion the restore must see; `--no-renames` is the form that lists every
  deletion.
- **Diff the build folder's file list at `462d20f3` against the tip.** It misses a record added and
  deleted inside the range, which the commit walk sees.

## 5. Production-readiness checklist

- security — no new write surface; S3 restores files the door wrote, from git's own objects.
- perf / scale — one `git log` over the build's range and one `git diff` per deleting commit.
- error / empty / loading states — an empty listing restores nothing; a taken path or `<n>` is named
  and left for the batch.
- observability — the ledger names each restored path with the commit that deleted it.
- risks — none beyond the restore's, which `TOOL-dTotalRecall-92` states.
- testing — AC1 and AC2 by the pass.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When §4's fixture repository is built, `deleted_records HEAD~1..HEAD` prints the second
  commit and the fixture's deleted record, x-deviation-1.md under the fixture's build folder, and unit
  92's spelling over the same range prints nothing.
  Red when: the corrected listing misses the deleted path, or the two spellings print the same.
  fixture: the repository is made under the system temp directory by the pass; the tree holds none.
- **AC2** — When `deleted_records 462d20f3..HEAD` runs after the pass, every path it prints exists in
  the working tree or is named in the ledger's AC2 line as a refused restore, and
  `has_deviation memory/builds/dTotalRecall/build 92 'audit-89 id 15 s4'` prints 1 where any path was
  restored or refused, else 0.
  Red when: a deleted record is neither in the tree nor named, or a restore overwrote a path that
  existed.

## 7. Gates

`memory hygiene` · `recall floor` · `recall floor arms`

No new arm: the observation is the two listings over a fixture repository and over the build's range.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-19`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 89 to 92, id 15
  (HIGH, item H4).

## 10. Reuse audit

The seams are `TOOL-dTotalRecall-92`'s restore, corrected here, and the driver's own commit listing,
which already passes `--no-renames` (`tools/workflows/unattended-build.js:602-606`).
`python tools/codebase-map/reuse_lookup.py "list the files a commit range deleted with rename detection off"`
ranked `build_commit` (`tools/unattended/lib-unattended.sh:1186`) first among its SEAM candidates,
which selects a unit's build commit in a range and lists no deleted path; none lists deleted paths
for a restore, and git's own flags are the mechanism. The recall query below found this audit's item H4 and unit 92's S11. No existing seam
fits beyond them.

Recall terms used: `python tools/memory-recall/query.py "how does a restore list every deleted record even when git pairs it as a rename" --terms "git log diff-filter deleted no-renames rename detection restore deviation record checkout listing"`
