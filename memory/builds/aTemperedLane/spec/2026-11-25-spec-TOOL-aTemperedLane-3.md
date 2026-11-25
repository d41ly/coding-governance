# TOOL-aTemperedLane-3 — the closing review's three mediums and two lows: one false claim corrected and pinned, four coverage gaps given arms

**Status:** CLOSED · rev-1 · 2026-11-25 · node a · Tier-1 · base 3d6c1702 · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-25-build-TOOL-aTemperedLane-3-1-acceptance-ledger.md](../build/2026-11-25-build-TOOL-aTemperedLane-3-1-acceptance-ledger.md) | journal | — |
| [2026-11-25-prompt-TOOL-aTemperedLane-3-brief.md](../prompts/2026-11-25-prompt-TOOL-aTemperedLane-3-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 closing review confirmed five items over units 1 and 2. M1 is a false claim about a
deleted guarded list. M2, M3, L1 and L2 are rules with no check that fails. This unit makes the claim
true in words, pins it, and adds an arm for each gap. No verdict of `routed_commits.py` changes.

## 2. Scope (IN)

- **S1** — M1, the statements. Three places state the bound: the L2 NOT-checked sentence of the
  module docstring of `tools/memory-tree/routed_commits.py`, the L2 bullet under "What it does not
  check" of `help/red-fix-lane.md`, and the `routed_commits.py` row of `tools/memory-tree/README.md`.
  The bound is the sentence §4, "The statements", gives. Observed by AC1.
- **S2** — M1, the claims. The help page's "still guards" sentence and the third bullet under
  "Expected improvements" of `memory/builds/aTemperedLane/README.md` claim no more than §4, "The
  statements", gives them. Observed by AC2.
- **S3** — M1, the pin. A self-test arm over commit h7 of §4, whose parent holds the list and whose own
  tree does not. With no disk copy the verb names no L2 for the path the parent's list names. The
  arm's control is the same commit with the disk copy there. Observed by AC3.
- **S4** — M2. `build_fixture` accepts bytes for a file's body. Two arms beside the AC5 arm of unit 2:
  a first parent whose list is not UTF-8, and one whose list path is a directory, each graded by the
  working list. Observed by AC4 and AC5.
- **S5** — M3. An arm over a trailered merge in a fixture of its own, graded by the first parent's
  list. Observed by AC6.
- **S6** — L1. An arm over `read_blob_batch` with `run_git` stubbed by three streams: one cut before a
  header, one cut inside a body, and one with a tree answer before a blob. Observed by AC7.
- **S7** — L2. `tools/memory-tree/marker-contract.test.sh` checks that `check_marker_line` of
  `gen_build_index`, of `routed_commits` and of `tree_lib` are one object. Observed by AC8.

## 3. Non-goals (OUT)

- Any change to a verdict, a predicate, a git-call figure or a finding's wording. AC9 observes it.
- Reading the parent's list where the working tree holds none. The owner chose the rule with its
  fallback, and the base behaved the same way.
- The review's refuted finding 2.
- The closed specs of units 1 and 2, and their ledgers. They are frozen.
- A change to the `parentlist` and `parentroot` fixtures, whose commits the AC7 arm of unit 2 counts.
- `.governance/instructions.toml` and the kit version, as in the first brief.

## 4. Design

### Evidence

- `tools/memory-tree/routed_commits.py#resolve_guarded_path` answers the empty string where
  `resolve_kit_dir` finds no `guarded-paths.txt` on disk. `read_parent_lists` then answers no list and
  `read_guarded_paths` answers None, so `check_red_fix_limits` refuses the `.governance/` prefix alone.
- `tools/memory-tree/routed_commits.py@f9517a1c:516` takes the first parent, and
  `tools/memory-tree/routed_commits.py@f9517a1c:524` is the branch a list that is not UTF-8 takes. No
  arm reaches either choice.
- `read_blob_batch` raises its two refusals at `tools/memory-tree/routed_commits.py@f9517a1c:282` and
  `tools/memory-tree/routed_commits.py@f9517a1c:289`. It looks `run_git` up in the module's globals,
  as it looks up every function the self-test already swaps.
- `tools/memory-tree/routed_commits.py#build_fixture` encodes every body as UTF-8, on one line.
- `help/red-fix-lane.md@1dd6ceb8:86` opens the "still guards" sentence, and
  `memory/builds/aTemperedLane/README.md@12930682:23` is the third bullet.
- Probed 2026-11-25 by a scratch script over the fixtures below. Each expected answer of AC3 to AC7
  held. The staged breaks of AC4, AC5 and AC6 each turned their own case, and those of AC4 and AC5
  turned no other. The identity of S7 is true today.

### The statements

Each of the three places of S1 says: a guarded list absent from the working tree, deleted by the fix
commit or by any later one, leaves only the `.governance/` prefix, whatever the first parent's list
holds. Each carries the phrase `absent from the working tree` on one line. The help page's sentence reads: "So a line the commit itself removes, the list still being present, still
guards." The README bullet reads: "A line a fix commit itself removes from the guarded list, the list
still being present, still guards, which it does not today." Each keeps `the list still being present`
on one line. The limits table of the help page and the docstring's rule sentences stand, since they
already say what an unresolved list refuses.

### The fixtures

Two scratch repositories from `build_fixture`, beside `parentlist` in `run_selftest` and under the
same `KIT` stub and its `finally`. Each has the disk copy `kits/policy/guarded-paths.txt` naming
`src/a.txt` alone and the unit's spec in its first commit, dated before the cutoff. Every fix commit
names `TOOL-tFix-1` and carries `Red-fix: leg one`.

| Fixture | Commit | Holds | L2 |
|---|---|---|---|
| `parentodd` | h1, plain | `src/a.txt`, `src/b.txt`, the spec | not graded |
| `parentodd` | h2, plain | adds the list, bytes naming `src/b.txt` with one byte that is not UTF-8 | not graded |
| `parentodd` | h3, fix | edits `src/a.txt` | finding, by the working list |
| `parentodd` | h4, plain | removes the list and adds a file under its path, so the path is a directory | not graded |
| `parentodd` | h5, fix | edits `src/a.txt` | finding, by the working list |
| `parentodd` | h6, plain | removes that file and adds the list, naming `src/b.txt` | not graded |
| `parentodd` | h7, fix | deletes the list and edits `src/b.txt` | finding with the disk copy there, none once it is removed |
| `parentmerge` | m1, plain | `src/a.txt`, `src/b.txt`, the spec | not graded |
| `parentmerge` | m2, plain, the side lineage | adds the list, naming `src/a.txt` | not graded |
| `parentmerge` | m3, plain, from m1 | adds the list, naming `src/b.txt` | not graded |
| `parentmerge` | m4, fix, from m3, merges m2 | edits `src/b.txt` | finding, by m3's list |

The disk copy is written by hand, so which commit deleted the list does not enter the reading. The
removed copy under h7 therefore stands for a deletion by a later commit too.

### The stub arm

A lambda in the place of `run_git` answers one stream per call over the two names `n1` and `n2`, and
the real function is put back in a `finally`. The lambda takes any keyword, since the caller passes
`stdin`.

| Stream | Answer |
|---|---|
| a whole blob, then nothing | a `Refusal` naming `n2`, "ended before it answered" |
| a whole blob, then a header of size 3 and two bytes | a `Refusal` naming `n2`, "ended inside" |
| a tree header with its body, the body holding an LF, then a whole blob | `n1` None and `n2` the blob's bytes |

### The marker check

A `"$PY" -c` line beside the one-CR source grep, `tools/memory-tree/marker-contract.test.sh@21ac8011:228`,
puts `$KIT_MT` on the path, imports the three modules and exits 1 unless the three names are one
object. A non-zero exit, an import failure included, prints a `FAIL` line and sets `st=1`. It is a
case of its own, so `ncase` rises by one. It sits after the leg's skip, so an install with no
unattended kit does not run it.

### Inventory

No function, key, file or flag is minted. The fixture names `parentodd` and `parentmerge` are string
arguments, which no naming cell grades.

### Files touched (estimate)

- `tools/memory-tree/routed_commits.py`
- `tools/memory-tree/marker-contract.test.sh`
- `tools/memory-tree/README.md`
- `help/red-fix-lane.md`
- `memory/builds/aTemperedLane/README.md`

### Alternatives rejected

- **Resolving the list's path with no file on disk.** It changes a verdict, and the brief keeps the code.
- **h1 to h7 and the merge in `parentlist`.** The AC7 arm of unit 2 requires eight fix commits there,
  and a leg reading equal to the limits pass's, which a merge breaks.

## 5. Acceptance criteria

Every probe below is a scratch script that imports `routed_commits`, builds the fixture under the
temp folder by `build_fixture` and calls `main` with `--red-fix-limits` and the sha. A break replaces
a function in the probe's process and never edits the tree.

- **AC1** — When `grep -c "absent from the working tree"` runs over
  `tools/memory-tree/routed_commits.py`, `help/red-fix-lane.md` and `tools/memory-tree/README.md`,
  each prints 1 or more, and reading each hit shows both halves: deleted by the fix commit or a later
  one, and only the `.governance/` prefix left.
  Red when: one of the three statements is missing or wraps inside that phrase.
- **AC2** — When `grep -c "the list still being present"` runs over `help/red-fix-lane.md` and
  `memory/builds/aTemperedLane/README.md`, each prints 1; and `grep -c "shortens the guarded list"`
  over the second prints 0.
  Red when: either page still claims that a deleted list's lines guard.
- **AC3** — When `--red-fix-limits` runs for h7 it exits 1 naming `L2` and src/b.txt, and after the
  disk copy is removed it exits 0 and names no `L2`.
  Red when: the first run passes, so the second proves nothing; or `resolve_guarded_path` answers the
  list's path with no file on disk, so the second run names that path and the statement is stale.
- **AC4** — When `--red-fix-limits` runs for h3, it exits 1 naming `L2` and src/a.txt.
  Red when: the `UnicodeDecodeError` branch of `read_parent_lists` sets `got[sha] = []`.
- **AC5** — When `--red-fix-limits` runs for h5, it exits 1 naming `L2` and src/a.txt.
  Red when: the None branch of `read_parent_lists` sets `got[sha] = []` before its `continue`. The
  break of AC4 does not reach this case.
- **AC6** — When `--red-fix-limits` runs for m4, it exits 1 naming `L2` and src/b.txt.
  Red when: `read_parent_lists` reads `parents[-1]`.
- **AC7** — When `read_blob_batch` runs over the three streams of §4, the first two raise `Refusal` in
  the words §4 gives, and the third answers None for `n1` and the blob's bytes for `n2`.
  Red when: either refusal is dropped for a short answer, or a body that is not a blob is not skipped.
- **AC8** — When the check's own python line runs by itself from the repository root with
  `tools/memory-tree` on the path, it exits 0; and with `gen_build_index.check_marker_line`, then
  `routed_commits.check_marker_line`, replaced in that process by a function that strips every
  trailing CR, it exits 1.
  Red when: the line compares fewer than the three names.
- **AC9** — When `python tools/memory-tree/routed_commits.py --red-fix-limits <sha>` runs for each of
  `dbc7bb6a`, `3fa017d5`, `918ffb5b`, `69a05280`, `b9a6d520`, `0b026d5c`, `e6196f84`, `f40a0e58` and
  `be10c468`, it exits 0; and `git diff 7654f9db2 -- tools/memory-tree/routed_commits.py` shows
  changes in the module docstring, `build_fixture` and `run_selftest` alone.
  Red when: a predicate or a verdict moved.
  fixture: the run branch's objects, which this clone holds; the verb only reads them.

## 6. Gates

`routed commits name a specced unit` · `routed-commits selftest` · `marker contracts` · `policy fixtures` · `lexicon naming predicates` · `docs` · `memory hygiene` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

The close runs these once. Each arm is observed red and then green at the close, and the pass uses
the probes of the acceptance criteria.

New arm: tools/memory-tree/routed_commits.py · covers AC3 · h7 with the disk copy there and removed, staged red by `resolve_guarded_path` answering the list's path with no file on disk · none
New arm: tools/memory-tree/routed_commits.py · covers AC4 · h3, staged red by `got[sha] = []` in the except · none
New arm: tools/memory-tree/routed_commits.py · covers AC5 · h5, staged red by `got[sha] = []` in the None branch · none
New arm: tools/memory-tree/routed_commits.py · covers AC6 · m4, staged red by `parents[-1]` · none
New arm: tools/memory-tree/routed_commits.py · covers AC7 · the three stubbed streams, staged red by dropping each refusal in turn, then by skipping the body of a blob alone · none
New arm: tools/memory-tree/marker-contract.test.sh · covers AC8 · the identity check, staged red by a local `check_marker_line` using `rstrip` in `gen_build_index.py`, then in `routed_commits.py` · none

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-25 · initial draft.

## 9. Reuse audit

`python tools/codebase-map/reuse_lookup.py "self-test arm grades a Red-fix commit against the parent's
guarded list"` ranked `read_routed_commits` and no arm builder of this module. The seams are
`build_fixture`, `run_limits_verb`, the `parentlist` fixture with its `KIT` stub in `run_selftest`,
and the one-CR check of `tools/memory-tree/marker-contract.test.sh`. The fixes are the review's own
corrected ones, in `2026-11-25-review-TOOL-aTemperedLane-1-closing-diff-review-round1.md`.

Recall terms used: `python tools/memory-recall/query.py "which arms and statements does the red-fix
lane's L2 parent list and the marker predicate still owe" --terms "red-fix lane limits guarded-paths
routed_commits L2 first parent merge cat-file torn stream marker-contract check_marker_line selftest
arm"`
