# TOOL-dMindYourWords-31 — the kit's one history pin, carried by the shared blame reader into the drift blame

**Status:** DEFERRED · rev-2 · 2026-10-29 · node d · Tier-2 · base ccd1292e · streams tooling · order 20 · advances TOOL-dMindYourWords-18

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md) | journal | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 TOOL-dMindYourWords-22 TOOL-dMindYourWords-23 TOOL-dMindYourWords-24 TOOL-dMindYourWords-25 TOOL-dMindYourWords-26 TOOL-dMindYourWords-27 TOOL-dMindYourWords-28 TOOL-dMindYourWords-29 TOOL-dMindYourWords-30 TOOL-dMindYourWords-32 TOOL-dMindYourWords-33 TOOL-dMindYourWords-34 TOOL-dMindYourWords-35 TOOL-dMindYourWords-36 TOOL-dMindYourWords-37 TOOL-dMindYourWords-38 TOOL-dMindYourWords-39 TOOL-dMindYourWords-40 TOOL-dMindYourWords-41 TOOL-dMindYourWords-42 TOOL-dMindYourWords-43 TOOL-dMindYourWords-44 TOOL-dMindYourWords-45 TOOL-dMindYourWords-46 TOOL-dMindYourWords-47 TOOL-dMindYourWords-48 TOOL-dMindYourWords-49 TOOL-dMindYourWords-50 TOOL-dMindYourWords-51 TOOL-dMindYourWords-52 |
| [2026-10-29-build-TOOL-dMindYourWords-31-deviation-311.md](../build/2026-10-29-build-TOOL-dMindYourWords-31-deviation-311.md) | deviation | — |
| [2026-10-29-review-TOOL-dMindYourWords-30-to-37-spec-audit-round1.md](../reviews/2026-10-29-review-TOOL-dMindYourWords-30-to-37-spec-audit-round1.md) | spec-audit | TOOL-dMindYourWords-34 TOOL-dMindYourWords-30 TOOL-dMindYourWords-32 TOOL-dMindYourWords-33 TOOL-dMindYourWords-35 TOOL-dMindYourWords-36 TOOL-dMindYourWords-37 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 11 of `reviews/2026-10-29-review-TOOL-dMindYourWords-22-to-29-spec-audit-round1.md`,
HIGH, which shares item H1 with ids 1 (TOOL-dMindYourWords-30) and 23 (TOOL-dMindYourWords-32).
TOOL-dMindYourWords-29 S42 makes `read_blame_lines` the kit's one porcelain blame reader, "run with
`--root` as TOOL-dMindYourWords-28 S2 requires", so the drift blame of TOOL-dMindYourWords-10 inherits
the graft hole: under a replace ref or a graft file it attributes lines to the graft point and reads that
commit's time for each. This unit spells the repository's history pin once in the kit and has
`read_blame_lines` and every other history read in the kit run under it.

## 2. Scope (IN)

- **S1** — The one pin. `build_git_env()` in `tools/lexicon/lexicon_conf.py` returns a copy of the
  process environment with `GIT_GRAFT_FILE=/dev/null`, the repository's pin policy
  (`tools/memory-tree/tree_lib.py:232-243`), and its docstring states that callers put
  `--no-replace-objects` first in the argv. It is the only spelling of `GIT_GRAFT_FILE` under
  `tools/lexicon/`. Observed by AC3.
- **S2** — The shared reader pinned. `read_blame_lines` (TOOL-dMindYourWords-29 S42) runs `git
  --no-replace-objects blame --porcelain --root ...` with `build_git_env()`, so the provenance blame and
  the drift blame both read the real commit graph. Observed by AC1 and AC2.
- **S3** — The inline pins folded. The pin TOOL-dMindYourWords-30 S1 carries at the provenance blame and
  the one TOOL-dMindYourWords-32 S1 carries at `read_vocabulary_record`'s `rev` read are replaced by S1's
  helper, and the other history reads the kit makes over commits it did not just create, the contract
  walk of TOOL-dMindYourWords-29 S31 and the ancestor reads at `tools/lexicon/lexicon.py:4129-4145`,
  take it too. Observed by AC3.
  **Readers:** by name: READER NOT IN TREE — the inline pins are minted by TOOL-dMindYourWords-30 and
  -32 at order 8, and no tracked file under `tools/lexicon/` spells `GIT_GRAFT_FILE` at base ccd1292e ·
  by value: NO VALUE READERS — the pin is an environment value and an argv flag git reads, and no code
  in the tree compares or derives from it.

## 3. Non-goals (OUT)

- The shallow-history refusal inside `read_blame_lines`: review id 20, the minors batch
  TOOL-dMindYourWords-37.
- What a merge commit means to the contract walk: TOOL-dMindYourWords-36.
- The left-shift gate the report names under H1: a gate is its own unit (BUILD-METHOD M2).
- Kit version constants: minted at landing (`tools/push-main.sh:26-31`), so this unit moves none.

### Edges

- **consumes-from** `TOOL-dMindYourWords-29` — S42's `read_blame_lines` and S31's contract walk; without them there is no shared reader to pin
- **consumes-from** `TOOL-dMindYourWords-30` — the pinned provenance blame, whose inline pin S3 folds into the helper
- **consumes-from** `TOOL-dMindYourWords-32` — the pinned `rev` read, whose inline pin S3 folds into the helper
- **hands-off** `TOOL-dMindYourWords-37` — `read_blame_lines` under the one pin, inside which the batch moves the shallow probe (id 20)
- **consumes-from** `TOOL-dMindYourWords-41` — `build_graft_fixture`, through which the drift-blame graft arms stage their graft with its control in force
- **consumes-from** `TOOL-dMindYourWords-42` — `--ignore-revs-file=` on the kit's blame, which S2's pinned argv for `read_blame_lines` keeps
- **hands-off** `TOOL-dMindYourWords-47` — `build_git_env()` and the call sites S2 and S3 pin by hand, which that unit moves onto the kit's one runner `run_git` (review id 3)
- **hands-off** `TOOL-dMindYourWords-52` — `build_git_env()`, which the minors batch strips of `GIT_ENV_LEAKS` (review id 17)

## 4. Design

### Evidence

- Unit 29 S42: `read_blame_lines(root, rel, lines=None, rev=None, contents=None, ignore_ws=False)`, "run
  with `--root` as TOOL-dMindYourWords-28 S2 requires", called by unit 5's provenance and unit 10's drift
  blame (`spec/2026-10-29-spec-TOOL-dMindYourWords-29.md` S42).
- Measured on git 2.54.0 in a fixture under `%TEMP%`: under `git replace --graft <c2>` an unpinned
  `blame --porcelain --root` attributed the first commit's line to `c2`; `--no-replace-objects` with
  `GIT_GRAFT_FILE=/dev/null` attributed it to `c1`, for a replace ref and for an `info/grafts` line
  alike. PINNED 2026-10-29.
- `tools/lexicon/lexicon.py:4129` and `:4145` read a tree and its blobs at a commit sha
  (`git ls-tree`, `git cat-file --batch`), the ancestor reads the kit already makes.
- `build_git_env` is the name the repository's pin already carries (`tools/memory-tree/tree_lib.py:232`);
  `lexicon.py --suggest build_git_env --as py.function` answered `OK` at writing.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `build_git_env` | function, `tools/lexicon/lexicon_conf.py` | `py.function`, asked: OK |

### Rollout

Live at landing, one order after TOOL-dMindYourWords-29, which mints `read_blame_lines`.

### Files touched (estimate)

- `tools/lexicon/lexicon_conf.py`: S1, S3
- `tools/lexicon/lexicon.py`: S2, S3
- `tools/lexicon/selftest.py`: the arm of §7

### Alternatives rejected

- **Setting the two variables in `os.environ` at `main`**: it pins only runs that enter through `main`,
  and a caller importing `lexicon_conf` reads unpinned; the helper pins every call that passes it.
- **Importing `tools/memory-tree/tree_lib.py`'s `build_git_env`**: the lexicon kit imports no sibling
  (`check_self_containment`, `tools/lexicon/lexicon.py:2359`).

## 5. Production-readiness checklist

- security — every history read in the kit answers for the real commit graph; no replace ref or graft
  file can re-parent a commit under any reader.
- perf / scale — none: an argv flag and one variable per spawn.
- error / empty / loading states — a pinned read that fails on a missing real object raises, as unit 32
  S3 states for the `rev` read; the drift blame then prints `drift not measured — <why>`, the form of
  the line unit 29 S27 prints for a shallow history, and grades no `drift` key.
- observability — the drift row names the real commit's time.
- risks — none beyond the refusal on a store missing an object a replacement hid.
- testing — AC1 to AC3 and the arm of §7.
- migration — none.
- user docs — N/A — TOOL-dMindYourWords-30 S3's README sentence covers every reader.

## 6. Acceptance criteria

- **AC1** — When `python <kit>/lexicon.py --offenders` runs in unit 10's drift fixture after its second
  commit is grafted onto no parent with `git replace --graft <c2>`, the `drift` keys it prints are those
  the ungrafted fixture prints.
  Red when: the drift blame dates lines by the graft point and a different key prints.
  fixture: the drift fixture under `%TEMP%/<short>`.
- **AC2** — When the graft is a `.git/info/grafts` line instead, the run prints the same keys.
  Red when: only `--no-replace-objects` was added and the graft file still re-parents the commit.
- **AC3** — When `git grep -h -c 'GIT_GRAFT_FILE' -- tools/lexicon/lexicon.py tools/lexicon/lexicon_conf.py`
  runs after the pass, it prints `1`, and `git grep -h -c -- '--no-replace-objects' --
  tools/lexicon/lexicon.py tools/lexicon/lexicon_conf.py` prints a nonzero count for each file it lists.
  Red when: an inline pin survives beside the helper, or a reader lost its argv flag.

## 7. Gates

`lexicon naming predicates` · `lexicon selftest` · `codebase-map kit selftest`

New arm: tools/lexicon/selftest.py · covers AC1 AC2 · the drift fixture grafted by a replace ref and by a graft file, its failing case the pin cut out of `read_blame_lines`, under which AC1 prints a different `drift` key · none

## 8. Open questions

- **F1 — Where does the kit spell its history pin?** Options: (a) one helper in `lexicon_conf.py`, which
  `lexicon.py` imports, passed by every history read; (b) the two variables set in `os.environ` at
  `main`; (c) each call keeps its own inline pin. (b) leaves importers unpinned and (c) is the
  duplication this unit removes. RESOLVED (agent, 2026-10-29, delegated): (a), rung 3, the shape of
  `tools/memory-tree/tree_lib.py:232`. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-29 · initial draft, promoted from review id 11 (HIGH, item H1, shared with ids 1 and
  23) of the round-1 audit of units 22 to 29.
- rev-2 · 2026-10-29 · §3 · the Edges gain the mirror of each edge the promoted units of the round-1 audit of units 30 to 37
  declare toward this unit (TOOL-dMindYourWords-41, TOOL-dMindYourWords-42, TOOL-dMindYourWords-47, TOOL-dMindYourWords-52); no scope, design or criterion moved.

## 10. Reuse audit

The seam is the repository's history pin `build_git_env` (`tools/memory-tree/tree_lib.py:232-243`),
mirrored by name inside the kit because the kit imports no sibling, and the shared reader
`read_blame_lines` TOOL-dMindYourWords-29 S42 mints. `python tools/codebase-map/reuse_lookup.py "ignore
git replace objects and grafts before trusting a history read"` ranked `build_git_env` among the generic
git readers; no pin exists under `tools/lexicon/` at base (`git grep -n GIT_GRAFT_FILE -- tools/lexicon`
prints nothing).

Recall terms used: `python tools/memory-recall/query.py "how does a git history reader stay honest when replace refs graft a commit onto no parent" --terms "graft replace no-replace-objects blame porcelain root boundary provenance diff-tree added shallow history"`
