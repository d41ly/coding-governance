# PLAY-dOrderedCharter-82 — the acceptance matrix's guard covers the modules its closure now imports

**Status:** DEFERRED · rev-1 · 2026-11-11 · node a · Tier-1 · base 8ecef2cf1 · streams playbook · order 44 · advances PLAY-dOrderedCharter-38

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md](../build/2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md) | journal | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-53 PLAY-dOrderedCharter-54 PLAY-dOrderedCharter-55 PLAY-dOrderedCharter-61 PLAY-dOrderedCharter-62 PLAY-dOrderedCharter-63 PLAY-dOrderedCharter-64 PLAY-dOrderedCharter-65 PLAY-dOrderedCharter-67 PLAY-dOrderedCharter-68 PLAY-dOrderedCharter-69 PLAY-dOrderedCharter-70 PLAY-dOrderedCharter-71 PLAY-dOrderedCharter-72 PLAY-dOrderedCharter-73 PLAY-dOrderedCharter-74 PLAY-dOrderedCharter-75 PLAY-dOrderedCharter-76 PLAY-dOrderedCharter-77 PLAY-dOrderedCharter-78 PLAY-dOrderedCharter-80 PLAY-dOrderedCharter-81 |
| [2026-11-11-prompt-PLAY-dOrderedCharter-82-1-spec-writer.md](../prompts/2026-11-11-prompt-PLAY-dOrderedCharter-82-1-spec-writer.md) | journal | — |
| [2026-11-11-prompt-PLAY-dOrderedCharter-82-build-brief.md](../prompts/2026-11-11-prompt-PLAY-dOrderedCharter-82-build-brief.md) | journal | — |
| [2026-11-11-prompt-PLAY-dOrderedCharter-82-spec-brief.md](../prompts/2026-11-11-prompt-PLAY-dOrderedCharter-82-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The python-reads leg reds at `8ecef2cf1` on fourteen modules the `govkit acceptance matrix` leg
imports and its guard does not cover. This unit adds exactly those fourteen paths to that leg's
guard, so the reads leg reads green over the tree, and changes nothing else.

## 2. Scope (IN)

- **S1** — The `guard` list of the `govkit acceptance matrix` row in `tools/gate-legs.json`,
  `tools/gate-legs.json@094abe94:1732`, gains fourteen exact file entries, each spelled
  `{prefix}/<kit>/<module>.py`: the eleven memory-tree modules, the policy kit's `budgets.py` and
  `policy.py`, and the roles kit's `roles_lib.py`, as section 4 lists them. The five entries the row
  holds today stay, in their order. Observed by AC1, AC2 and AC3.

## 3. Non-goals (OUT)

- The row's `ceiling`, argv, chunk and subject. A guard decides when a scoped bar runs the leg, not
  how long a run takes (`tools/run-gates/run-gates.sh@4ab05900:539`), so the ceiling of 7030 does not
  move.
- Any edit to `tools/govkit/matrix.py`, the renderer or the reads checker. The import that grew the
  closure is PLAY-dOrderedCharter-81 S2's, and its reading of the renderer's constants stays.
- A directory guard over the three kits (section 4, Alternatives rejected).
- Any other leg's guard: the matrix row is the only one with a gap (section 4, Evidence).

## 4. Design

### Evidence

Read at `8ecef2cf1`. The reads leg itself is refused to this writer's role, so each figure is from a
probe calling the checker's own `derive_guard_gaps` and `read_legs`,
`tools/run-gates/py_reads.py@cf8f2730:179`, over the tree.

- The gaps: fourteen, all on the `govkit acceptance matrix` row, and no other row of the 26 the arm
  walks has one (PINNED, that probe at `8ecef2cf1`). Eleven are under `tools/memory-tree/`, two under
  `tools/policy/` and one under `tools/roles/`. The brief counted fourteen memory-tree modules; the
  policy and roles kits supply three of them.
- The cause: the matrix closure is two files at `84a28f634~1` and 33 at `84a28f634`, the build of
  PLAY-dOrderedCharter-81, with 0 and 14 gaps (PINNED, the same probe over a `git archive` of each
  commit's `tools/`). The brief named PLAY-dOrderedCharter-78. The new reach is
  `govkit.resolve_kit_dir("playbook", "render_playbook.py", HERE)` and the import after it,
  `tools/govkit/matrix.py@0d6bbdf0:111` to `tools/govkit/matrix.py@0d6bbdf0:113`: the walk adds a
  literally resolved kit's directory, `tools/run-gates/py_reads.py@cf8f2730:169`, and follows the
  renderer's imports from there. The seventeen playbook modules it reaches are under
  `{prefix}/playbook/`, which the guard holds.
- The name arm is clean at the base: no hit over 151 tracked files, no star import (PINNED, a probe
  of `scan_tracked_names` at `8ecef2cf1`). So the fourteen guard lines are the leg's whole red, and
  the leg exits 0 once they are covered, `tools/run-gates/py_reads.py@cf8f2730:266`.
- A guard entry covers a module by its exact path, or by a prefix when the entry ends in `/`,
  `tools/run-gates/py_reads.py@cf8f2730:194`. All fourteen paths are tracked (PINNED, `git ls-files`
  at `8ecef2cf1` lists 14).
- No second copy of this guard exists. The leg's name appears in `tools/govkit/registry.toml`
  as an `exempt_leg` row with a reason only, `tools/govkit/registry.toml@7b1f4bec:533`, in
  `tools/govkit/subject-pins.tsv` with its subject and chunk, and in
  `tools/run-gates/ceiling-evidence.txt` with its measured time; none carries a guard, so no
  parity row moves.

### The row after the pass (S1)

```json
    "guard": [
      "{prefix}/govkit/",
      "{prefix}/playbook/",
      "{prefix}/check-microformats.sh",
      "{prefix}/check-line-length.sh",
      "{prefix}/memory-tree/asbuilt_view.py",
      "{prefix}/memory-tree/backlog.py",
      "{prefix}/memory-tree/build_records.py",
      "{prefix}/memory-tree/coverage_join.py",
      "{prefix}/memory-tree/design_lib.py",
      "{prefix}/memory-tree/deviation_join.py",
      "{prefix}/memory-tree/id_grammar.py",
      "{prefix}/memory-tree/import_walk.py",
      "{prefix}/memory-tree/routed_commits.py",
      "{prefix}/memory-tree/row_grammar.py",
      "{prefix}/memory-tree/tree_lib.py",
      "{prefix}/policy/budgets.py",
      "{prefix}/policy/policy.py",
      "{prefix}/roles/roles_lib.py",
      ".lexicon.conf"
    ],
```

The new entries sit after the row's `{prefix}` files and before its root file, in the walk's sorted
order. This is the exact-file form other legs already use for the same modules: `playbook render
selftest`, `recall floor arms` and `policy fixtures` each list memory-tree, policy or roles files
one by one.

What the guard still does not check: it lists the closure as the walk reads it today. A module that
joins the closure later is outside the guard until someone adds it, and the reads leg reds on that
the same way it reds now. A module reached through a subprocess or a computed kit name is outside
the walk, `tools/run-gates/py_reads.py@cf8f2730:18`, and so outside this guard as well.

### Alternatives rejected

- Three directory entries, `{prefix}/memory-tree/`, `{prefix}/policy/` and `{prefix}/roles/`.
  Shorter, but a scoped bar would then run the matrix after an edit to any file in those kits,
  for example `tools/memory-tree/gen_build_index.py`, which the matrix never imports. Its evidenced
  run is 218.8 s on node a (PINNED, `tools/run-gates/ceiling-evidence.txt@0d5d8d62:57`). The brief
  asks for the narrowest addition, and that is the fourteen exact paths.
- Reading the renderer's four constants without importing it. That changes PLAY-dOrderedCharter-81
  S2's design, which the brief puts out of scope.

### Files touched (estimate)

- `tools/gate-legs.json` (S1)

## 5. Acceptance criteria

| Leg | Criteria |
|---|---|
| `python reads (a name never bound, an import outside its guard)` | AC1, with AC2 |

- **AC1** — When `python tools/run-gates/py_reads.py` runs over the tree after the pass, it exits
  0, prints no line opening `py-reads: RED`, and prints
  `py-reads: guards · 26 suites walked, 45 guarded legs of another head not read`. At the base it
  exits 1 and prints fourteen lines opening `py-reads: RED guard · govkit acceptance matrix ·`.
  Red when: a module in the matrix closure is still outside the row's guard.
  figure: PINNED, 26 rows walked out of 71 guarded rows, by a probe of `derive_guard_gaps` at `8ecef2cf1`.
  permission: the main loop runs it; a role agent's scratch guard refuses this leg.
- **AC2** — When `python tools/run-gates/py_reads.py --guards "govkit acceptance matrix"` runs after
  the pass, it exits 0, prints 33 lines opening `py-reads: closure · govkit acceptance matrix ·`,
  and prints no line opening `py-reads: RED`.
  Red when: an added entry is misspelled, so the module it was meant to cover is still a gap.
  figure: PINNED, a 33-file closure by the same probe at `8ecef2cf1`.
  permission: the main loop runs it, as for AC1.
- **AC3** — When `python -c "import json, sys; r = [l for l in json.load(sys.stdin.buffer) if l['name'] == 'govkit acceptance matrix'][0]; print(len(r['guard']), r['ceiling'], r['guard'][0], r['guard'][-1])" < tools/gate-legs.json`
  runs after the pass, it prints `19 7030 {prefix}/govkit/ .lexicon.conf`, where the base prints
  `5 7030 {prefix}/govkit/ .lexicon.conf`.
  Red when: the pass adds an entry the closure does not need, drops one the row held, or moves the
  ceiling.

## 6. Gates

`python reads (a name never bound, an import outside its guard)` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `policy fixtures` · `spec tokens (a spec's own names resolve)`

The guarded legs on the line are the four whose guard names `{prefix}/gate-legs.json` itself. The
legs guarded by `{prefix}/` are broad by the spec-token check's floor of five,
`tools/check-spec-tokens.py@bf9a3e50:390`, so the join leaves them out. The matrix leg is not on the
line: `tools/gate-legs.json` does not trip its guard, and its verdict does not depend on its guard.

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-11 · initial draft, from `2026-11-11-prompt-PLAY-dOrderedCharter-82-spec-brief.md`.
  The gaps were re-read at `8ecef2cf1` by a probe of the checker's own `derive_guard_gaps`, and
  attributed to PLAY-dOrderedCharter-81's build by the same probe over each commit's archived
  `tools/`. The brief named PLAY-dOrderedCharter-78 as the cause and counted fourteen memory-tree
  modules; three of the fourteen belong to the policy and roles kits.
- rev-1 · 2026-11-11 · AC3 · its command reads the manifest on stdin, `< tools/gate-legs.json`, in
  place of a quoted path inside `open(...)`, which the spec-token check graded as an untracked
  path. The observation and its printed figures are unchanged, re-probed at `8ecef2cf1`; the rev
  stays.

## 9. Reuse audit

This unit extends an existing seam, the matrix row's own `guard` list in `tools/gate-legs.json`, in
the exact-file form `playbook render selftest`, `recall floor arms` and `policy fixtures` already use
for memory-tree, policy and roles modules. The gaps are measured by the reads checker's own reader.
No new mechanism is added.

Recall terms used: `py_reads guard gap closure resolve_kit_dir govkit acceptance matrix gate-legs guard exact-file memory-tree policy roles_lib scoped bar`
