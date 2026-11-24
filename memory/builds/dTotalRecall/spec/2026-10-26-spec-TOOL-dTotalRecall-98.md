# TOOL-dTotalRecall-98 — the restore lists every deleted record with rename detection off, so a record deleted beside a near-copy is put back

**Status:** CLOSED · rev-2 · 2026-11-24 · node d · Tier-2 · base 462d20f3 · streams tooling · order 40 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-43 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 TOOL-dTotalRecall-67 TOOL-dTotalRecall-68 TOOL-dTotalRecall-69 TOOL-dTotalRecall-70 TOOL-dTotalRecall-71 TOOL-dTotalRecall-72 TOOL-dTotalRecall-73 TOOL-dTotalRecall-74 TOOL-dTotalRecall-75 TOOL-dTotalRecall-76 TOOL-dTotalRecall-77 TOOL-dTotalRecall-78 TOOL-dTotalRecall-79 TOOL-dTotalRecall-80 TOOL-dTotalRecall-81 TOOL-dTotalRecall-82 TOOL-dTotalRecall-83 TOOL-dTotalRecall-84 TOOL-dTotalRecall-85 TOOL-dTotalRecall-86 TOOL-dTotalRecall-87 TOOL-dTotalRecall-88 TOOL-dTotalRecall-89 TOOL-dTotalRecall-90 TOOL-dTotalRecall-91 TOOL-dTotalRecall-92 TOOL-dTotalRecall-93 TOOL-dTotalRecall-94 TOOL-dTotalRecall-95 TOOL-dTotalRecall-96 TOOL-dTotalRecall-97 TOOL-dTotalRecall-99 TOOL-dTotalRecall-100 |
| [2026-10-26-build-TOOL-dTotalRecall-98-deviation-981.md](../build/2026-10-26-build-TOOL-dTotalRecall-98-deviation-981.md) | deviation | — |
| [2026-11-24-build-TOOL-dTotalRecall-98-1-acceptance-ledger.md](../build/2026-11-24-build-TOOL-dTotalRecall-98-1-acceptance-ledger.md) | log | — |
| [2026-11-24-prompt-TOOL-dTotalRecall-98-build-brief.md](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-98-build-brief.md) | journal | — |
| [2026-11-24-prompt-TOOL-dTotalRecall-98-reground-brief.md](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-98-reground-brief.md) | journal | — |
| [2026-11-24-prompt-TOOL-dTotalRecall-98-reground-spec-writer.md](../prompts/2026-11-24-prompt-TOOL-dTotalRecall-98-reground-spec-writer.md) | log | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 89 to 92
(`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-89-spec-audit-round1.md`)
confirmed finding **id 15 at HIGH**, its item **H4**, alone in that item.

`TOOL-dTotalRecall-92` §4 "The restore" lists the records a pass of this build took out of the tree
with `git log --diff-filter=D --format='%H' --name-only 462d20f3..HEAD -- '<build>/*-deviation-*.md'`,
and the records each such commit modified with `git diff --name-only --diff-filter=M`. Both run with
git's default rename detection. A record deleted in the same commit that adds a similar file is shown
as a rename, not a deletion, and deviation records share most of their template. Reproduced again
2026-11-24 in §4's fixture repository: after a `git mv` of one record and one appended line, the listing
printed nothing, and with `--no-renames` it printed the commit and the deleted path. The driver's own
changed-path listing passes `--no-renames` so a renamed path's source is listed too
(`tools/workflows/unattended-build.js#SPEC_COMMIT_CHECKLIST`). Unit 92's AC11, "every path it prints
exists in the tree", then certifies a restore over a listing that left the record out.

This unit spells both listings with `--no-renames`, observes the difference and the restore on a fixture
repository, and runs the corrected listing over the build after unit 92's pass, putting back any record
unit 92's listing missed. At `67ffd1289` neither spelling lists a deletion in the build's range, so the
run over the build is an observation unless a later pass deletes a record. It repairs
`TOOL-dTotalRecall-92`, at order 40, one above that unit's 39.

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
- **S3** — The restore, re-run. After unit 92's pass, §4's `write_restores 462d20f3..HEAD` puts back
  every path `deleted_records` prints that is absent from the working tree, from `C^`, together with
  each record `modified_records` lists for `C` whose bytes are still the ones `C` left. A path is put
  back only where it is absent and no record of the folder carries its `<n>`. Where either test fails,
  nothing is checked out and the ledger names the path, its commit and the record in the way. Over the
  fixture repository it restores and refuses as §4 pins. Observed by AC1 and AC2.
- **S4** — Unit 92's AC11, recorded. Where S3 put back or named a record, a deviation record of
  `TOOL-dTotalRecall-92` names AC11 as certified over a rename-blind listing and lists each path, with
  the token `audit-89 id 15 s4` in place of that recipe's `audit-77` token, by `TOOL-dTotalRecall-90`
  §4's recipe, only where `has_deviation memory/builds/dTotalRecall/build 92 'audit-89 id 15 s4'`
  prints 0. The probe is `TOOL-dTotalRecall-93` §4's, taken through unit 92, which consumes it and the
  recipe. Observed by AC2.

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

### The listings and the restore

```bash
# $SCRATCH/listings98.sh, sourced from the repository root
PS='memory/builds/dTotalRecall/build/*-deviation-*.md'
deleted_records() {  # range -> "<commit>" then each deviation record that commit deleted, rename detection off
  git log --no-renames --diff-filter=D --format='%H' --name-only "$1" -- "$PS"
}
modified_records() {  # commit -> each deviation record it modified, rename detection off
  git diff --no-renames --name-only --diff-filter=M "$1^" "$1" -- "$PS"
}
write_restores() {  # range -> one verdict line per record put back or refused, newest commit first
  local c= p n held m
  deleted_records "$1" | while read -r p; do
    case "$p" in '') continue ;; */*) ;; *) c=$p; continue ;; esac
    [ -e "$p" ] && continue
    n=${p##*-deviation-}; n=${n%.md}
    held=$(ls memory/builds/dTotalRecall/build | grep -- "-deviation-$n\.md$")
    [ -z "$held" ] || { echo "refused $p $c held" $held; continue; }
    git checkout -q "$c^" -- "$p" || { echo "red $p $c checkout-failed"; continue; }
    echo "restored $p $c"
    modified_records "$c" | while read -r m; do
      git diff --quiet "$c" -- "$m" || { echo "refused $m $c moved-since"; continue; }
      git checkout -q "$c^" -- "$m" && echo "restored $m $c" || echo "red $m $c checkout-failed"
    done
  done
}
```

The bytes are git's; nothing is retyped. A record deleted twice is put back from its newest deletion,
and its older line then finds the path present. `ls` reads the folder, so an untracked or superseded
record holds its `<n>` too, as the door and `tools/memory-tree/build_records.py#read_records` count it.

### The fixture repository

A fixture repository needs a short path on Windows, so it is made under the system temp directory, for
example `%TEMP%/r98`, never inside the worktree and never at a drive root. Each fence of this section is
written to a file under `$SCRATCH` and run as `bash <file>`: an isolated worktree session refuses an
inline command that changes directory before git. A second file is one that sources the listings first.

```bash
. "$SCRATCH/listings98.sh"
R="$TEMP/r98"; rm -rf "$R"; mkdir -p "$R/memory/builds/dTotalRecall/build"; cd "$R" && git init -q || exit 2
B=memory/builds/dTotalRecall/build
write_commit() { git add -A && git -c user.email=f@x -c user.name=f commit -qm "$1"; }
for i in $(seq 1 12); do echo "- **Field $i:** shared template text, line $i" >> "$B/x-deviation-1.md"; done
echo one > "$B/x-deviation-7.md"; echo one > "$B/x-deviation-8.md"; write_commit one
git mv "$B/x-deviation-1.md" "$B/x-deviation-2.md" && echo "- **Extra:** one" >> "$B/x-deviation-2.md"
echo two >> "$B/x-deviation-7.md"; echo two >> "$B/x-deviation-8.md"; write_commit two
echo three >> "$B/x-deviation-8.md"; write_commit three
echo "== corrected"; deleted_records HEAD~2..HEAD
echo "== unit 92"; git log --diff-filter=D --format='%H' --name-only HEAD~2..HEAD -- "$PS"
echo "== held"; touch "$B/y-deviation-1.md"; write_restores HEAD~2..HEAD; rm "$B/y-deviation-1.md"; git status --short
echo "== restored"; write_restores HEAD~2..HEAD; git status --short
echo "== again"; write_restores HEAD~2..HEAD
```

PINNED, measured 2026-11-24 on node a, git 2.56.1.windows.1, with these exact commands under a scratch
path. Every commit named is the second, every path under the fixture's build folder:

| Block | Printed (PINNED 2026-11-24) |
|---|---|
| `corrected` | the second commit's sha, then x-deviation-1.md |
| `unit 92` | nothing |
| `held` | one `refused` line for x-deviation-1.md ending `held y-deviation-1.md`, and an empty status |
| `restored` | `restored` for x-deviation-1.md and for x-deviation-7.md, `refused` for x-deviation-8.md ending `moved-since`; the status adds the first and modifies the second, staged |
| `again` | nothing |

### The run over the build

```bash
# run from the repository root, with the listings sourced
deleted_records 462d20f3..HEAD
git log --no-renames --diff-filter=A --format= --name-only 462d20f3..HEAD -- "$PS" | grep -c .
write_restores 462d20f3..HEAD
```

The second line is the liveness: from a subdirectory the pathspec matches nothing, and `deleted_records`
then prints nothing and exits 0. Measured at `67ffd1289`, the listing printed nothing in 0.4 s (PINNED 2026-11-24),
the liveness 150 from the repository root and 0 from `tools/` (PINNED 2026-11-24), and `write_restores` nothing.
Unit 92's spelling printed nothing either. `TOOL-dTotalRecall-88` rev-4 S19 merges and deletes no
record, so no pass before unit 92 is designed to take one out.

### Why order 40

Unit 92 restores at order 39, so the corrected listing reads the tree that unit left. The §3 edge holds
the order: `--dispatch` refuses this unit while unit 92 is neither CLOSED nor WONTDO
(`tools/unattended/unattended.sh#verb_dispatch`).

### Inventory

Minted: the functions `deleted_records`, `modified_records` and `write_restores`, spec text only;
restored records only where unit 92's listing missed one; at most one deviation record of
`TOOL-dTotalRecall-92`. Naming cell: none, no product symbol minted.

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
- error / empty / loading states — an empty listing restores nothing and is read only beside its
  liveness; a taken path or `<n>` is named and left for the batch; a failed checkout is a `red` line.
- observability — the ledger names each restored path with the commit that deleted it.
- risks — none beyond the restore's, which `TOOL-dTotalRecall-92` states. The walk does not read a
  deletion only a merge made, nor one on a side branch git's default history simplification prunes. With
  `--full-history --diff-merges=separate` the same range lists none (DERIVED 2026-11-24, that command at
  `67ffd1289`).
- testing — AC1 and AC2 by the pass.
- migration — none.
- user docs — none under `help/`.

## 6. Acceptance criteria

- **AC1** — When §4's fixture repository is built and run, its five blocks print what §4 pins. In them,
  `deleted_records HEAD~2..HEAD` prints the second commit and the fixture's deleted record,
  x-deviation-1.md under the fixture's build folder, and unit 92's spelling over the same range prints
  nothing.
  Red when: the corrected listing misses the deleted path, the two spellings print the same, a held
  `<n>` is restored over, or a record moved since the deleting commit is overwritten.
  figure: the five blocks are PINNED in §4, measured 2026-11-24.
  fixture: the repository is made under the system temp directory by the pass; the tree holds none.
- **AC2** — When §4's run over the build is made after the pass, its liveness prints at least 1. Every
  path `deleted_records 462d20f3..HEAD` prints exists in the working tree or is named as a refused
  restore on the AC2 line of the ledger that
  `git grep --untracked -n "Evidences:\*\* TOOL-dTotalRecall-98" -- memory/builds/dTotalRecall/build`
  names. That line also states an empty listing as empty, beside the liveness, and
  `has_deviation memory/builds/dTotalRecall/build 92 'audit-89 id 15 s4'` prints 1 where any path was
  restored or refused, else 0.
  Red when: a deleted record is neither in the tree nor named, a restore overwrote a deleted path that
  had come back or an appended record changed since, or an empty listing is read with no liveness.
  figure: at `67ffd1289` the listing is empty, the liveness 150 and the probe 0, PINNED 2026-11-24; the
  pass's own are DERIVED.

## 7. Gates

`memory hygiene` · `recall floor` · `recall floor arms`

No new arm: the observation is the two listings and the restore over a fixture repository and over the
build's range.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry of `TOOL-dTotalRecall-19`'s clause, which would split a clause that unit carries whole. (b)
  reds the parts join; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none
- **F2 — What becomes of a record the deleting commit appended to, changed again since?** Rev-1 checked
  out every `modified_records` path, which exists, against AC2's own red on an overwritten path. Options:
  (a) overwrite it, as rev-1 spelled; (b) put it back only where its bytes are the ones that commit left,
  else name it. (a) loses the later edit and reds AC2; veto 1 discards it.
  RESOLVED (agent, 2026-11-24, delegated): (b). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 89 to 92, id 15
  (HIGH, item H4).
- rev-2 · 2026-11-24 · §1 · S3 · S4 · §4 · §5 · AC1 · AC2 · §8 F2 · §10 · re-grounded at `67ffd1289` per
  `2026-11-24-prompt-TOOL-dTotalRecall-98-reground-brief`, over unit 93 rev-2 and unit 88 rev-4: the restore
  is spelled as `write_restores` and exercised on the fixture, since the build's range lists no deletion;
  a record changed since its deleting commit is refused; the empty listing carries a liveness; the fences
  run as files; S4 names whose probe and recipe it takes; citations are by symbol. No item is cut.

## 10. Reuse audit

The seams, re-read at `67ffd1289`, are `TOOL-dTotalRecall-92`'s restore, corrected here, and the driver's
own changed-path listing, which already passes `--no-renames`
(`tools/workflows/unattended-build.js#SPEC_COMMIT_CHECKLIST`). The class is
`memory/gotchas/porcelain-diff-names-a-rename-by-its-destination.md`, whose quieter arm, a read that
failed looking like a range that touched nothing, is what AC2's liveness answers.
`python tools/codebase-map/reuse_lookup.py "list the files a commit range deleted with rename detection off"`,
re-run 2026-11-24, ranked `build_commit` and `read_commits` among its SEAM candidates. The first selects
a unit's build commit in a range, and `tools/lib/commit_trailers.py#read_commits` lists every path a
commit touched with rename detection off, not the ones it deleted. None lists deleted paths for a
restore, and git's own flags are the mechanism. The recall query below, re-run 2026-11-24, found this
audit's item H4, unit 92's §4 "The restore", unit 100's listing and `DEPL-dCarriedReceipt-11`, whose rename
detection serves an adopter's withdrawn files and restores nothing. `tools/memory-tree/id_grammar.py#read_kept_reason` and the build-folder walks of
`tools/memory-tree/record_causes.py#check_cause_writers` and
`tools/memory-tree/record_kinds.py#check_alias_compares` are no seam here: this unit reads no marker and
no registry. No existing seam fits beyond them.

Recall terms used: `python tools/memory-recall/query.py "how does a restore list every deleted record even when git pairs it as a rename" --terms "git log diff-filter deleted no-renames rename detection restore deviation record checkout listing"`
