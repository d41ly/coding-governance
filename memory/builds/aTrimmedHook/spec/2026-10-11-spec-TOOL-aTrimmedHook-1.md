# TOOL-aTrimmedHook-1 — check 9 under `--staged` renders the build index only when the staged set can move it

**Status:** CLOSED · rev-1 · 2026-10-11 · node a · Tier-2 · base b726385f · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-build-TOOL-aTrimmedHook-1-1-acceptance-ledger.md](../build/2026-10-11-build-TOOL-aTrimmedHook-1-1-acceptance-ledger.md) | journal | — |
| [2026-10-11-prompt-TOOL-aTrimmedHook-1-2-build-brief.md](../prompts/2026-10-11-prompt-TOOL-aTrimmedHook-1-2-build-brief.md) | journal | — |
| [2026-10-11-prompt-TOOL-aTrimmedHook-1-brief.md](../prompts/2026-10-11-prompt-TOOL-aTrimmedHook-1-brief.md) | research | TOOL-aTrimmedHook-2 TOOL-aTrimmedHook-3 KICK-aTrimmedHook-1 |
| [2026-10-11-review-TOOL-aTrimmedHook-1-closing-diff-round1.md](../reviews/2026-10-11-review-TOOL-aTrimmedHook-1-closing-diff-round1.md) | diff-review | TOOL-aTrimmedHook-2 KICK-aTrimmedHook-1 TOOL-aTrimmedHook-3 |

<!-- /gen:spec-records -->

## 1. Goal

Hygiene check 9 runs `gen_build_index.py --check`, a full render of every build-index artifact, on
every commit that touches `memory/`: about 51 s of the staged leg's ~300 s on node a, measured
2026-10-11 at 64-82 host bash processes. This unit makes the staged leg render only when a staged
path can move the index, decided by the exact classifier the owner chose, and announce the skip
otherwise. The full run is unchanged.

## 2. Scope (IN)

- **S1 — one id scan, two callers.** `tools/memory-tree/gen_build_index.py` gains
  `build_roster_id_re(families)`, the compiled id pattern `rosters()` builds today (raising the same
  `Problem` on an empty family set), and `extract_roster_ids(text, id_re)`, which applies
  `scan_missing_citations` and returns the id tokens a text contributes to a roster. `rosters()` calls
  both and its output is byte-identical. Observed by AC5.
- **S2 — the structural predicate.** `check_index_input(rel, m, kit)` answers True for every path
  whose presence, name or content the renderer reads other than through prose ids, or writes: a build
  `README.md` or `BACKLOG.md`; anything under a build's `spec/`, `build/`, `prompts/` or `reviews/`;
  `<m>/LIVE.md`; anything under `<m>/ledger/`, `<m>/backlog/` or `<m>/project/`; `.memory-tree.conf`;
  anything under the kit's own directory. Observed by AC4 and AC6.
- **S3 — the classifier.** `check_staged_render(root, conf)` returns `(render, reason)` from two git
  spawns: `git diff --cached --name-status --no-renames -z` over the memory root, the conf and the
  kit directory, and ONE `git cat-file --batch` for each modified non-structural path's `HEAD:<p>`
  and `:<p>` blobs. It renders when any staged path is new to the index or absent from it, when any is
  structural by S2, or when a modified path's `extract_roster_ids` set differs between the two blobs, or either blob
  does not decode. Otherwise it skips. Observed by AC1, AC2, AC3 and AC4.
- **S4 — the mode.** `main` accepts `--check --staged`: a skip prints
  `build-index: render SKIPPED under --staged — <reason>; the push boundary renders in full` and exits
  0; a render owed runs `cmd_check` exactly as `--check`. The usage line names the modifier. Observed
  by AC1 and AC2.
- **S5 — the hygiene call.** In `tools/memory-tree/check-memory-hygiene.sh` check 9, `STAGED=1`
  passes `--staged` and prints the skip line the generator returns; the guard
  `printf '%s\n' "$STAGED_MD" | grep -q .` becomes the fork-free `[ -n "$STAGED_MD" ]`. `STAGED=0`
  runs the same command as at BASE. Observed by AC7.
- **S6 — the arms.** `test_staged_render(arm)`, called from `cmd_selftest`, holds fixture arms for
  AC1 to AC6, built with `_fixture`.
  Observed by AC1 to AC6.

## 3. Non-goals (OUT)

- **N1** — no partial render (`--builds <slugs>`), brief item 5, parked. A render owed is the full
  render.
- **N2** — the renderer still reads the WORKTREE, not the index, as at BASE; the classifier reads
  the index. An unstaged edit can move the verdict of a render either way, as it already can.
- **N3** — `LIVE_LANDED_UNCLOSED` reads tracked product source, and pre-commit reaches hygiene only
  when `memory/**` is staged; neither changes here, so a staged conf or kit file alone never reaches
  check 9 at commit time, as at BASE.
- **N4** — a HEAD already drifted by a `--no-verify` commit is not seen by a skip; the skip line says
  the push boundary renders in full, and it does.
- **N5** — no change to `--check`, `--write` or any other mode when `--staged` is absent.

### Edges

none

## 4. Design

### Why a classifier and not a path list

`rosters()` (~766 at BASE) builds each build README's `ids:` line from id tokens in the prose of
EVERY tracked file under the memory root except `LIVE.md`, `ledger/` and, under `builds`,
`backlog/`. A staged `RUN.md`, gotcha or decision row that adds an id therefore moves a README, so
the prompt's path list (README, spec header, BACKLOG, LIVE, ledger, backlog) would skip real drift.
The owner chose the exact classifier at the attended hand-back.

### What can move the render

The renderer's sources, from its module docstring and `collect()`: build front matter, spec status
headers, every tracked memory file's prose ids (roster), record FILENAMES (last-record date and the
bindings count), record `Serves:` lines, `BACKLOG.md` under `builds`, the stale-header waiver under
`project/`, the conf, and the kit's own grammar files. Its outputs: build READMEs, spec record
regions, `LIVE.md`, `ledger/`, and the family views under `backlog/`. Every source except prose ids
is covered by S2's structural set or by the Added/Deleted rule; prose ids are covered by the id-set
comparison. `--no-renames` makes a rename an add plus a delete, both of which render.

### The id-set comparison

`extract_roster_ids` is the exact scan `rosters()` runs per file. Comparing the SET per modified file
between `HEAD:<p>` and `:<p>` is sufficient because a roster is a union over files keyed by the id's
own slug: if no file's contribution changes, no union changes. The own-README exclusion in
`rosters()` never applies here, because a README is structural and always renders.

### One batch read

`git cat-file --batch` takes `HEAD:<p>` and `:<p>` lines on stdin and answers
`<sha> blob <size>` plus the bytes, or `<name> missing`. A `missing` HEAD blob is an added file,
already a render by the A rule; it is treated as a render rather than trusted, so a malformed answer
can only cost a render. The subprocess runs with `_build_git_env()`, the module's one git
environment, so a hook's inherited `GIT_DIR` cannot pin the wrong tree.

### The parity arm

AC6 asserts that every artifact path `plan()` returns on the fixture tree satisfies
`check_index_input`. A future output written outside the structural set reds this arm, rather than
silently landing a path whose staged edit would skip the render.

### Inventory

| identifier | where | cell |
|---|---|---|
| `build_roster_id_re` | `tools/memory-tree/gen_build_index.py` | `py.function`, verb `build` |
| `extract_roster_ids` | `tools/memory-tree/gen_build_index.py` | `py.function`, verb `extract` |
| `check_index_input` | `tools/memory-tree/gen_build_index.py` | `py.function`, verb `check` |
| `check_staged_render` | `tools/memory-tree/gen_build_index.py` | `py.function`, verb `check` |
| `test_staged_render` | `tools/memory-tree/gen_build_index.py` | `py.function`, verb `test`, the arms, module-level so a pass runs them alone |

All five confirmed by `python3 tools/lexicon/lexicon.py --suggest <name> --as py.function`.

### Files touched (estimate)

- `tools/memory-tree/gen_build_index.py`
- `tools/memory-tree/check-memory-hygiene.sh`
- `tools/memory-tree/README.md`

### Rollout

Order 1. TOOL-aTrimmedHook-2 writes `check-memory-hygiene.sh` after this unit. The pass runs
`python tools/codebase-map/gen_map.py --write` after adding the five functions, and claims the new
keys in the memory-tree dossier. The memory-tree version bump is the build's, after the last unit.

### Alternatives rejected

- **The prompt's path list.** Refuted by the roster read above; a RUN.md adding an id would skip.
- **Render whenever any staged diff line carries an id-shaped token.** Most `RUN.md` edits carry
  ids, so the commit the owner measured would still pay the render. The owner chose the classifier.
- **The classifier in shell.** The id grammar and the missing-citation form are Python's; a shell
  copy is a second reader of one rule.

## 5. Production-readiness checklist

- security — N/A — reads git objects of the local repository through the module's existing git
  environment; no new input surface.
- perf / scale — one python start (already paid by check 9) and two git spawns, against a ~51 s
  render; a render owed costs the same as at BASE plus those two spawns.
- error / empty / loading states — nothing staged under the scanned paths is a skip with that
  reason; a git failure is a render, never a skip.
- observability — every skip prints one line naming why and that the push boundary renders.
- risks — a renderer source the predicate misses would skip a real drift at commit time only; the
  push boundary still catches it, and AC6 pins the output half by derivation.
- testing — AC1 to AC6 are `--selftest` arms; AC7 is a staged run of the hygiene leg.
- migration — none; removing the modifier restores BASE behavior.
- user docs — `tools/memory-tree/README.md` gains one sentence on `--check --staged`.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/gen_build_index.py --selftest` runs, the arm that stages a
  one-line edit adding no id to a tracked non-structural memory file sees `check_staged_render`
  return no render, and `--check --staged` print the SKIPPED line and exit 0.
  Red when: the arm sees a render owed, or the skip prints nothing.
  cost: one fixture repo; seconds.
- **AC2** — When `gen_build_index.py --selftest` runs, the arm that stages a line adding a new `ARCH-tOne-7` id to
  that file sees a render owed, and `--check --staged` run the full check.
  Red when: it skips. Observed RED first by running the arm against a classifier that ignores ids.
- **AC3** — When `gen_build_index.py --selftest` runs, an arm staging an Added memory file and an arm staging a
  Deleted one each see a render owed.
  Red when: either skips.
- **AC4** — When `gen_build_index.py --selftest` runs, arms staging a build README edit, a spec status edit, a conf
  edit and a kit-directory file each see a render owed.
  Red when: any skips.
- **AC5** — When `gen_build_index.py --selftest` runs, the roster arms already present still pass and a new arm
  asserts `rosters()` over the fixture equals the per-file union of `extract_roster_ids`.
  Red when: any roster arm moves.
- **AC6** — When `gen_build_index.py --selftest` runs, the parity arm finds every key of `plan()`'s artifact map on
  the fixture satisfying `check_index_input`.
  Red when: any artifact path is not structural. Observed RED first by removing `ledger/` from S2.
- **AC7** — When `bash tools/memory-tree/check-memory-hygiene.sh --staged` runs with only a one-line
  no-id edit to a tracked `RUN.md` staged, its output carries the SKIPPED line; with a line adding a
  new id to that file staged instead, it carries no SKIPPED line.
  Red when: the first prints no SKIPPED line or the second prints one.
  cost: two staged-leg runs; minutes each on a contended host.

## 7. Gates

`build-index selftest` · `memory hygiene` · `memory-hygiene self-test` · `harness arms (fail branches armed or pinned)` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `kit version markers`

New arm: tools/memory-tree/gen_build_index.py test_staged_render · covers AC1 AC2 AC3 AC4 AC5 AC6 · a classifier ignoring ids, and `ledger/` removed from the structural set · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft, from the brief and the attended orientation's roster finding.

## 10. Reuse audit

The seam is `rosters()` in `tools/memory-tree/gen_build_index.py` with `scan_missing_citations` from
`tools/memory-tree/tree_lib.py`: S1 factors the per-file scan out so the classifier and the renderer
call one function. `python tools/codebase-map/reuse_lookup.py "decide whether a staged change can move
the generated build index"` returned only name-stem matches (`build`, `changed`, `build_commit`),
none of which classifies a staged set. Recall returned `TOOL-aGroundedOrientation-3` and
`TOOL-aThawedCorpus-5`, which named check 9's near-vacuous staged disjunct and deferred it; neither
proposed a mechanism.

Recall terms used: staged pre-commit hygiene check 9 gen_build_index fork spawn cost manifest-check C6 commit-msg check-commit
