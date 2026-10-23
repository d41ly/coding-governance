# PLAY-dOrderedCharter-53 — a file:line citation is grandfathered by the commit that wrote its line, never by the age of its file

**Status:** OPEN · rev-1 · 2026-10-24 · node d · Tier-2 · base ce13efbe · streams playbook · order 11 · advances PLAY-dOrderedCharter-38

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-PLAY-dOrderedCharter-53-deviation-531.md](../build/2026-10-24-build-PLAY-dOrderedCharter-53-deviation-531.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-2 spec audit (`memory/builds/dOrderedCharter/reviews/2026-10-24-review-PLAY-dOrderedCharter-39-spec-audit.md`)
confirmed **finding 36 at HIGH**, its item **H4**. `PLAY-dOrderedCharter-47` S2 and S3 grandfather a
record under `memory/builds/**` by the adding commit of the FILE: every unlisted file:line reference
in a file added before `L`, the commit that brought the positional check in, is print-only. That
population includes files edited for as long as their build lives: each build's `README.md`,
`BACKLOG.md` and `RUN.md`, and every spec a rev bump touches. A citation a later run writes into any
of them is never graded, and the check certifies the file clean while grading nothing in it. This
unit grades per line: a reference is print-only only when the line holding it was written by a commit
that does not descend from `L`. It repairs unit 47 and is built right after it.

## 2. Scope (IN)

- **S1** — The provenance. For a record under `memory/builds/` holding at least one unlisted
  file:line reference that unit 26 S3 would red, `positional.py` reads `git blame --porcelain -M
  HEAD -- <path>` once and maps each line to the commit that wrote it. Blame follows the file across
  its renames, and `-M` keeps a line moved within the file attributed to its first writer. Observed
  by AC1 to AC3.
- **S2** — The verdict. A reference is grandfathered when the commit blame names for its line is
  outside unit 47 S2's descendant set of `L`, and graded under unit 26 S3 when it is inside it. A line
  blame attributes to no commit, an uncommitted edit, is graded. This supersedes unit 47 S2's "whose
  adding commit, read through `tree_lib.read_adding_commits` over `memory/builds/**`, is outside
  that set" and S3's "In such a record, every unlisted file:line reference" as the grandfathering
  key; unit 47 S1's derivation of `L` and S2's descendant set stand. Observed by AC1 and AC2.
- **S3** — The printed line names the line's commit: `positional — grandfathered: <path>:<line> <ref>
  (written in <sha8>, before the check)`. Observed by AC1.
- **S4** — The plants, through unit 19's fixture, `python tools/playbook/gov_tag.py --fixture --plant
  <case>`: `positional-edited-after` (a record added on a branch forked before `L`, merged after it,
  then appended by a post-merge commit citing `x.py:3`), `positional-renamed-after` (that record
  renamed after the merge, its old lines unchanged) and `positional-uncommitted` (the post-merge
  citation left uncommitted). Observed by AC1 to AC3.

## 3. Non-goals (OUT)

- `L`, the descendant set and the plant `positional-forked-before`: unit 47's.
- The list, its seed and the `pin` and `shrink` verbs: unit 26's.
- Grading text outside `memory/builds/`: unit 47 S3's limit stands.

### Edges

- **consumes-from** `PLAY-dOrderedCharter-47` — `L`, its descendant set and the grandfathered print, which S1 to S3 re-key per line; without them there is no check-landing commit to compare against
- **hands-off** `PLAY-dOrderedCharter-55` — the spec-record and rename faces of the same rule (ids 15, 37), each observed over this unit's per-line verdict

## 4. Design

### Evidence

Read at `ce13efbe`; the seam is unit 47's design over `tree_lib.read_adding_commits`
(`tools/memory-tree/tree_lib.py:302`), which returns the oldest add of each path from one
`git log --reverse --no-renames --diff-filter=A`. `git log --oneline -- memory/builds/dOrderedCharter/RUN.md`
printed four commits against one add and `README.md` eight, PINNED 2026-10-24 by the audit's probe;
`memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-1.md` was added in `8aa81a42e` and modified in `41c08120b`.

### Why blame, and its cost

Blame answers the property itself, which commit wrote this line, where a file's adding commit answers
a property of the file. It attributes a line to the commit on whichever branch first wrote it, so a
line written on a branch forked before `L` and merged after it keeps its pre-`L` commit, and a line
written after that branch merged `L` carries a descendant of `L`. Blame is the expensive read, so it
runs only over records that hold a reference unit 26 S3 would red, a population the check already
derives, and never over a clean record.

### Inventory

Minted: the plants `positional-edited-after`, `positional-renamed-after` and `positional-uncommitted`,
and the printed line's `written in` field. Naming cells: `lexicon naming predicates` grades the
Python names.

### Files touched (estimate)

- `tools/playbook/positional.py`
- `tools/playbook/gov_tag.py` (the plants)

### Rollout

Live at landing, order 11, after unit 47 at order 10. Unit 7 shares order 11 and writes neither file.

### Alternatives rejected

- **Grandfathering only write-once folders** (`build/`, `reviews/`, `prompts/`), the review's second
  fix: a spec there is rev-bumped for the build's whole life, so the hole moves rather than closes.
- **A post-`L` content diff of each record**: a three-dot diff per record reads the same history blame
  reads, and loses a line moved within the file.

## 5. Production-readiness checklist

- security: no new surface; the rule reads history and narrows only references nobody wrote under the
  check.
- perf / scale: one `git blame` per record holding a red reference; DERIVED at the pass by timing the
  leg against its ceiling.
- error / empty / loading states: a failed blame raises naming the path and exits 2, never a silent
  grandfather.
- observability: each grandfathered reference prints its line and the commit that wrote it.
- risks: a whitespace-only rewrite of a pre-`L` line re-attributes it to the rewriting commit, which
  grades it; that errs toward grading.
- testing: AC1 to AC3 by plant under unit 19's selftest arm.
- migration: none.
- user docs: unit 47's sentence in `tools/playbook/README.md` names the per-line rule.

## 6. Acceptance criteria

- **AC1** — When `python gov_tag.py --fixture --plant positional-edited-after` runs, the
  pre-fork line's `x.py:1` prints `positional — grandfathered:` with its line, and the appended
  `x.py:3` reds.
  Red when: a citation appended after the merge to a pre-fork record is print-only.
- **AC2** — When `--plant positional-renamed-after` runs, the renamed record's pre-fork `x.py:1` is
  still printed as grandfathered and the leg's arm exits 0.
  Red when: a rename after the merge strips grandfathering from lines nobody rewrote.
- **AC3** — When `--plant positional-uncommitted` runs, the uncommitted `x.py:3` reds.
  Red when: an uncommitted line is read as written before the check.

## 7. Gates

`playbook render selftest` · `govkit acceptance matrix` · `lexicon naming predicates` · `encoding posture (text IO names its encoding)` · `spec tokens (a spec's own names resolve)`

Unit 19's `tags (the resolver's checks)` leg runs the positional arm over the tree, this unit's
verdict included, and unit 26's `tags positional selftest` runs the positional plants; neither leg is
in `tools/gate-legs.json` at base, so both stay off the line above.

New arm: tools/playbook/adopt-playbook.sh · covers AC1 AC2 AC3 · the playbook-render selftest runs the three plants, each failing case staged by unit 47's per-file adding-commit rule · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`, as the tree's promoted specs do; (b) none; (c) a part of unit 26's
  clause. (b) reds unbound and (c) splits a clause this unit does not carry. RESOLVED (agent,
  2026-10-24, delegated): (a), rung 3. widens: none · relaxes: none
- **F2 — What grandfathers a reference.** Options: (a) the commit blame names for its line; (b) the
  file's adding commit, as unit 47 wrote; (c) write-once folders only. (b) is the finding and (c)
  leaves specs ungraded. RESOLVED (agent, 2026-10-24, delegated): (a), rung 3. widens: none ·
  relaxes: unit 26 S3's red, for a reference whose line a commit outside `L`'s descendants wrote

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-2 spec audit's finding 36 (HIGH, item H4).

## 10. Reuse audit

The seam extended is unit 47's grandfather verdict in `tools/playbook/positional.py`, with `L` and its
descendant set reused as unit 47 derives them; `tree_lib.read_adding_commits`
(`tools/memory-tree/tree_lib.py:302`) stays the reader of `L` itself. `python
tools/codebase-map/reuse_lookup.py "which commit wrote a given line of a file"` ranked `build_commit`,
`check_line`, `render_line` and `parse_conf_line` by name stem, none a line-provenance reader, so no
existing seam fits and the blame read is new. The recall query returned unit 47, TOOL-dTrueNorth-1
and the gotcha `a-merged-in-check-can-refuse-a-pinned-record`, the class this rule narrows.

Recall terms used: `python tools/memory-recall/query.py "how is an old record exempted from a check that landed after it was written" --terms "grandfather adding commit blame line provenance merged-in check pinned record exempt"`
