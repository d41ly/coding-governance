# TOOL-dDeclaredLoop-72 — the loop kit reads the records root the driver reads, and refuses two confs that disagree

**Status:** CLOSED · rev-6 · 2026-11-16 · node d · Tier-2 · base ed497191 · streams tooling · order 36 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 TOOL-dDeclaredLoop-115 TOOL-dDeclaredLoop-116 TOOL-dDeclaredLoop-117 |
| [2026-10-24-build-TOOL-dDeclaredLoop-68-promoted-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-68-promoted-fix-return.md) | research | TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 |
| [2026-10-24-build-TOOL-dDeclaredLoop-72-deviation-721.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-72-deviation-721.md) | deviation | — |
| [2026-10-24-build-TOOL-dDeclaredLoop-72-deviation-722.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-72-deviation-722.md) | deviation | — |
| [2026-11-16-build-TOOL-dDeclaredLoop-72-1-acceptance-ledger.md](../build/2026-11-16-build-TOOL-dDeclaredLoop-72-1-acceptance-ledger.md) | journal | — |
| [2026-11-16-build-TOOL-dDeclaredLoop-72-deviation-723.md](../build/2026-11-16-build-TOOL-dDeclaredLoop-72-deviation-723.md) | deviation | — |
| [2026-11-17-build-TOOL-dDeclaredLoop-100-deviation-1172.md](../build/2026-11-17-build-TOOL-dDeclaredLoop-100-deviation-1172.md) | deviation | TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-117 |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-68-promoted-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-68-promoted-fix-brief.md) | research | TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-72-1-spec-writer.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-72-1-spec-writer.md) | journal | — |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-72-build-brief.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-72-build-brief.md) | journal | — |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-72-reground-brief.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-72-reground-brief.md) | research | — |
| [2026-10-24-review-TOOL-dDeclaredLoop-68-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-68-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 |
| [2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round1.md](../reviews/2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round1.md) | diff-review | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |
| [2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round2.md](../reviews/2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round2.md) | diff-review | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |

<!-- /gen:spec-records -->

## 1. Goal

The round-3 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-57-spec-audit.md`)
confirmed finding **id 29 at HIGH**, its item **H5**. The same defect is item M2 at medium (ids 4, 12, 42,
44) and its rationale half is item L2 at low (id 17), all three batched into `TOOL-dDeclaredLoop-75`.

The loop kit reads a build's records root in one function, `tools/loop/loop_transition.py#read_memory_root`,
which takes `MEMORY_ROOT` from `.memory-tree.conf` alone. Every read of a build's records goes through it:
`budget_state`'s population (the run-state file `tools/loop/adapt.py#read_run_file` names, the records
rotated beside it and the other builds' run-state files, `TOOL-dDeclaredLoop-60`'s), a patch build's
README, the spec headers, the transition records, and the README of `TOOL-dDeclaredLoop-53`'s
opening-commit rule, which `TOOL-dDeclaredLoop-64` observes under a records root. The unattended driver
writes under `.unattended.conf`'s `MEMORY_ROOT`, `memory` where that conf leaves it unset. Nothing
compares the two. Where they disagree, the budget counts no draw or refuses one on a build it cannot find,
and the opening-commit rule holds a build whose README it looked for under a root the driver did not use.

This unit makes the loop kit's one reader of the root answer the driver's root, and refuse by name where
the two confs name different roots. 64 builds at order 35 and 60 at order 30, so this unit follows the
later of the two and repairs both; its placement names `TOOL-dDeclaredLoop-64`.

## 2. Scope (IN)

- **S1** — `resolve_memory_root(tree)` in `tools/loop/loop_lib.py`, the loop kit's one reader of a build's
  records root. Where `<tree>/.unattended.conf` is a file, the root is its `MEMORY_ROOT`, read through
  `TOOL-dDeclaredLoop-70`'s `read_driver_conf`, or `memory` where that conf leaves the key unset, the
  driver's own default. Where it is not a file, the root is `.memory-tree.conf`'s `MEMORY_ROOT` through
  the memory-tree kit's `read_design_conf`, or `memory`. Each value is stripped of surrounding whitespace
  and slashes, as the loop readers strip it at the tip, and a blank value reads as unset. The driver-conf
  read is held for the process, keyed by the tree's resolved path and the bytes of its `.unattended.conf`,
  so one process sources that conf once and a fixture that rewrites it reads it again.
  Observed by AC1, AC2.
- **S2** — Where `.unattended.conf` is a file and `.memory-tree.conf` declares a `MEMORY_ROOT` other than
  the root S1 took from the driver's conf, `resolve_memory_root` raises `ValueError` with the text
  `records root: .unattended.conf says <a>, .memory-tree.conf says <b> — the driver writes under <a>`.
  A verb that reaches the read prints that text on its refusal line and exits 2: `budget.py` as
  `loop: budget · refused · <text>`, `breakpoints.py` as `breakpoints: refused · <text>`.
  Observed by AC3.
- **S3** — Every caller of `loop_transition.py`'s `read_memory_root` calls S1 in its place, the opening
  read `TOOL-dDeclaredLoop-53` lands in `tools/loop/breakpoints.py` among them, and `read_memory_root` is
  retired from `tools/loop/loop_transition.py`, so no loop module keeps a second reading of the root
  beside S1. Observed by AC1, AC2, AC4.
  **Readers:**
  by name: tools/loop/adapt.py (its import, read_run_file and read_fenced_row), tools/loop/budget.py (its import and derive_patch_origin), tools/loop/loop_transition.py (the definition, read_build_headers, read_transition_records and read_transition_moves), memory/map/generated/symbols.json (its row for that module)
  by value: the run-state file, change record, patch README, spec header, transition record and opening-commit README paths each caller builds from the root, which S1 answers alike wherever `.unattended.conf` is absent or the two confs agree
- **S4** — The plants `unattended-root` and `confs-disagree` join `PLANTS` in `tools/loop/budget.py` and
  in `tools/loop/breakpoints.py`, as §4 "The plants" stages them. Each module's `--selftest` runs its
  `PLANTS`, under the built legs `loop budget fixtures` and `loop breakpoint fixtures`.
  Observed by AC1, AC2 and AC3, and by the `New arm:` lines in §7, RED first at the close.
- **S5** — The carriers. The section of `help/loop.md` headed "What stops a read" gains one paragraph:
  where a loop command finds a build's records, by S1's rule, and S2's refusal with what resolves it.
  The table of `loop_lib.py` functions in `tools/loop/README.md` gains a row for `resolve_memory_root`,
  and the paragraph after that table names its import of the memory-tree kit's conf reader among the
  module's reaches outside the standard library. The comment in `tools/loop/kit.toml` that lists the
  same reaches names it too. Observed by AC5.

## 3. Non-goals (OUT)

- Where the driver writes: `tools/unattended/unattended.sh`, unchanged.
- The four other loop functions that read `MEMORY_ROOT` from `.memory-tree.conf` through
  `read_design_conf` themselves: `tools/loop/position.py#derive_position_into`,
  `tools/loop/loop_parents.py#read_withdrawn_parents`, `tools/loop/upstream.py#write_upstream_record` and
  `tools/loop/loop_lib.py#read_builds_dir`. They answer what S1 answers except where `.memory-tree.conf`
  sets no `MEMORY_ROOT` and `.unattended.conf` sets one other than `memory`, and each then fails on a
  folder it does not find rather than reading another build's (§8 F4). The class is recorded at the close.
- The per-reader plants, wording and `--explain` line the medium and low grades of this defect ask for:
  ids 4, 12, 42, 44 and 17, scope items of `TOOL-dDeclaredLoop-75`.
- A check that reds two confs naming different roots across the whole tree, the finding's gate
  left-shift: S2 refuses at every loop read of a build's records; a tree-wide leg is recorded at the close.
- A leg of this unit's own: both modules' `PLANTS` already run under the legs unit 19 and unit 30 built.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-60` — `budget_state`'s run-state population, which reads its root through `read_memory_root` and which this unit points at the driver's root
- **consumes-from** `TOOL-dDeclaredLoop-64` — the records-root plant and held line over `TOOL-dDeclaredLoop-53`'s opening-commit README read, which this unit points at the driver's root
- **consumes-from** `TOOL-dDeclaredLoop-70` — `read_driver_conf`, the loop kit's one reader of the driver's conf
- **hands-off** `TOOL-dDeclaredLoop-75` — the resolved root, beside which that unit adds the per-reader plants, the docstrings and the `--explain` line (ids 4, 12, 17, 42, 44)
- **hands-off** `TOOL-dDeclaredLoop-76` — `resolve_memory_root` and AC4's no-own-conf-read property, which that unit gives a source value and grades on the syntax tree, its plant observing what AC4's grep states (the round-4 spec audit's id 1)
- **hands-off** `TOOL-dDeclaredLoop-79` — `resolve_memory_root`'s refusal and its `.memory-tree.conf` read, which that unit restates to the pseudo-code's population over normalised paths and to `parse_conf`'s real signature (ids 15, 35)
- **hands-off** `TOOL-dDeclaredLoop-82` — AC4, which that unit amends in place to observe through the `no-own-conf-read` plant (the round-5 spec audit's id 2)
- **hands-off** `TOOL-dDeclaredLoop-95` — `resolve_memory_root` and AC3's `confs-disagree` plant, which that unit re-runs over the moved read (the round-11 spec audit's id 1)
- **hands-off** `TOOL-dDeclaredLoop-100` — AC3's `confs-disagree` plant in `breakpoints.py`, which that unit re-runs over the read it changes (the round-12 spec audit's id 6)

## 4. Design

### Evidence

Read at branch `unattended-declared-loop-d56bf0`, tip `bd31adbcc`, through `git show`, unless named
otherwise. Units 53 and 64 are not built at that tip and are read on their committed specs, rev-3 and
rev-4. `read_driver_conf` is `TOOL-dDeclaredLoop-70`'s, read on its committed rev-2.

- `tools/loop/loop_transition.py#read_memory_root` answers `read_design_conf(root)`'s `MEMORY_ROOT`,
  stripped of whitespace and slashes, `memory` where unset. `tools/memory-tree/design_lib.py#read_design_conf`
  answers `{}` for an absent `.memory-tree.conf` and `parse_conf(text, {})` otherwise.
- Its callers are `tools/loop/adapt.py#read_run_file`, `tools/loop/adapt.py#read_fenced_row`,
  `tools/loop/budget.py#derive_patch_origin`, and in its own module `read_build_headers`,
  `read_transition_records` and `read_transition_moves`. `adapt.py` and `budget.py` import it from
  `loop_transition.py`. `tools/loop/budget.py#read_budget_rows` reads the run-state file
  `read_run_file` names, the `RUN.*.md` records beside it, and each `*/RUN.md` and rotated record in the
  builds folder above it, so the whole population hangs off that one root. `TOOL-dDeclaredLoop-53` rev-3
  S1 reads the opening README under the same function.
- The driver sets `MEMORY_ROOT=memory` before it sources `$ROOT/.unattended.conf`, then binds `M` to it.
  `tools/unattended/unattended.sh#readme_of` spells `$M/builds/<slug>/README.md` and
  `tools/unattended/unattended.sh#scaffold_runmd` writes `<MEMORY_ROOT>/builds/<slug>/RUN.md`. The grep
  in §5 re-derives the three lines.
- gov's `.unattended.conf` sets `MEMORY_ROOT=memory` under a comment that it matches `.memory-tree.conf`,
  which sets the same. Sourced alone in a bash subshell over a `git show` copy, on this node, it exits 0
  and reads `memory`.
- At the tip, `budget.py` and `breakpoints.py` each spell `.unattended.conf` once, in a driver plant that
  appends to the conf it copied, and neither spells `read_design_conf`, `parse_conf` or
  `read_driver_conf`.
- `budget.py`'s `main` prints a `ValueError` as `loop: budget · refused · <why>` and `breakpoints.py`'s as
  `breakpoints: refused · <why>`, each exiting 2. `tools/loop/breakpoints.py#read_breakpoints` reaches
  `read_transitions` through `read_tag_policy` before any other read of the build's records.
- `tools/loop/adapt.py#write_flow_states` turns a `ValueError` from `read_fenced_row` into the class
  `none`, but calls `read_run_file` first, outside that handler, so S2 raises there before the handler
  is reached.

### The resolution

```
normalise(v) = v.strip().strip("/"), or None where that is empty
resolve_memory_root(tree):
    mt = normalise(read_design_conf(tree).get("MEMORY_ROOT") or "")
    if (tree / ".unattended.conf") is a file:
        ua = normalise(read_driver_conf(tree, ["MEMORY_ROOT"]).get("MEMORY_ROOT") or "") or "memory"
             # held per (resolved tree, the conf's bytes) for the process
        if mt and mt != ua:
            raise ValueError("records root: .unattended.conf says <ua>, .memory-tree.conf says <mt>"
                             " — the driver writes under <ua>")
        return ua
    return mt or "memory"
```

The memory-tree kit is found and imported inside the function, as `read_builds_dir` finds it, so a tree
without that kit raises the `LookupError` its callers print as `unarmed`, as the read does at the tip.
`read_driver_conf`'s own refusal, an unreadable conf, propagates unchanged.

### The callers

| Caller | Module | At the tip | After this unit |
|---|---|---|---|
| `read_run_file`, `read_fenced_row` | `tools/loop/adapt.py` | `read_memory_root`, imported from `loop_transition.py` | `resolve_memory_root`, imported from `loop_lib.py` |
| `derive_patch_origin` | `tools/loop/budget.py` | `read_memory_root`, imported from `loop_transition.py` | `resolve_memory_root`, which the module already imports from |
| `read_build_headers`, `read_transition_records`, `read_transition_moves` | `tools/loop/loop_transition.py` | its own `read_memory_root` | `resolve_memory_root`, imported from `loop_lib.py` |
| the opening read of `read_breakpoints` | `tools/loop/breakpoints.py` | `read_memory_root`, once `TOOL-dDeclaredLoop-53` lands | `resolve_memory_root` |

The pass runs `git grep -n -w read_memory_root -- tools/loop` at its own base and moves every hit, so a
caller an earlier order added is moved too.

### The plants

Each plant prints `held` or `MISSED <why>`, as the module's other plants do.

- `budget.py`, `unattended-root`. `write_transition_plant(top, "default")` stages the tree, then
  `git mv memory records` moves the build, `.memory-tree.conf` is rewritten to `FAMILIES="tool:TOOL"`
  alone, `.unattended.conf` is written as `MEMORY_ROOT=records`, and `records/builds/tFix/RUN.md` is
  written as the module's `PLANT_RUN`, all committed. Two `draw --build tFix --cause fix-pass --item
  TOOL-tFix-1` verbs run in the scratch, and `budget_state("tFix", top)` is read.
- `budget.py`, `confs-disagree`. `write_transition_plant(top, "default")` stages the tree with
  `memory/builds/tFix/RUN.md` as `PLANT_RUN`, and `.unattended.conf` is written as `MEMORY_ROOT=records`
  beside `.memory-tree.conf`'s `MEMORY_ROOT=memory`. One `draw` on `tFix` runs, and the run-state file's
  bytes are compared before and after.
- `breakpoints.py`, `unattended-root`. The pre-placement staging of `TOOL-dDeclaredLoop-53`'s plants,
  which `TOOL-dDeclaredLoop-64` makes take the memory root and the builds' README paths as arguments, is
  called with the root `records` and build `tRec` opened under `records/builds/` on the line the placement
  does not reach. Its conf commit writes `.unattended.conf` as `MEMORY_ROOT=records` and
  `.memory-tree.conf` with no `MEMORY_ROOT` line, beside the policy file carrying
  `autonomy = "three-gates"`. The scratch's own copy of the module runs `list --build tRec` in the scratch.
- `breakpoints.py`, `confs-disagree`. `write_transition_plant(top, "default")` stages the tree and
  `.unattended.conf` is written as `MEMORY_ROOT=records` beside `.memory-tree.conf`'s
  `MEMORY_ROOT=memory`. `list --build tFix` runs in the scratch through the module's `main`.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `resolve_memory_root` | Python function in `tools/loop/loop_lib.py` | `py.function`, verb-first |
| `unattended-root`, `confs-disagree` | `PLANTS` names, in each of the two modules | none |
| `records root:` | refusal text | none |

`python tools/lexicon/lexicon.py --suggest resolve_memory_root --as py.function` answered OK on the
worktree at `179486e8f`, whose `.lexicon.conf` verb declarations equal the branch's; the two files differ
only in `VERB_OFFENDER_PIN`, its comment and the tag rule. The retired `read_memory_root` of
`loop_transition.py` leads with `read`, a declared verb, so it was no offender.

### Files touched (estimate)

- `tools/loop/loop_lib.py`
- `tools/loop/loop_transition.py`
- `tools/loop/adapt.py`
- `tools/loop/budget.py`
- `tools/loop/breakpoints.py`
- `tools/loop/README.md`
- `tools/loop/kit.toml`
- `help/loop.md`
- `tools/run-gates/selftest-budgets.txt`
- `memory/map/generated/symbols.json`, `memory/map/generated/MAP.md`, `memory/map/generated/CARDS.md`,
  `memory/map/generated/inventories.json`

### Alternatives rejected

- **The driver passing `--memory-root "$M"`.** It is exact for driver calls but leaves a hand run and a
  fixture with no source; S1 reads the same conf the driver sources, so both agree by construction.
- **Reading `.memory-tree.conf` and warning on disagreement.** A warning beside a zero count is the
  silent refill the finding names.
- **`read_memory_root` kept as a one-line delegate of S1** (§8 F3). Two names for one root, and a later
  caller may take either.
- **The rule written into `read_memory_root` itself, no new name** (§8 F3). Seven later specs build on
  the name `resolve_memory_root`, three of them placing it in `loop_lib.py`, and the driver-conf read
  would sit apart from `read_driver_conf`.
- **The runlog kit's `resolve_memory_root`** (`tools/runlog/runlog_lib.py#resolve_memory_root`). It reads
  `.memory-tree.conf` alone, and the loop kit takes no edge to that kit.

## 5. Production-readiness checklist

- security — a read; S2 fails closed on a misconfigured tree. Sourcing the driver's conf is
  `read_driver_conf`'s, project shell the driver already runs on every verb.
- perf / scale — one bash per process for each tree and conf bytes, only where `.unattended.conf`
  exists; `.memory-tree.conf` is parsed on each call, as at the tip.
- error / empty / loading states — an unset key reads the driver's default, an absent driver conf reads
  the memory tree's, and `read_driver_conf`'s refusal of an unreadable conf propagates by name.
- observability — S2's refusal names both files, both values and the root the driver writes under.
- risks — the refusal reaches every loop command that reads a build's records through the callers above:
  the budget, the breakpoints, the transition record, the flow changes, the composition reads and the
  position read. `tools/loop/position.py#derive_position` answers `invalid-input` with the text as its
  reason. An adopter whose two confs disagree today is refused there until it aligns them; its
  driver and memory tree already disagree on where records live. What no criterion here checks: the four
  readers §3 names, and a conf whose value changes between two reads within one process without its bytes
  changing.
- testing — AC1 to AC3 as plants, AC4 and AC5 as greps; the arms under §7, observed at the close.
- migration — none: no record or conf moves, and no `[[upgrade]]` row is owed; S2's text names the fix.
- user docs — `help/loop.md`, S5.

### The sweep

Read at the tip `bd31adbcc`; counts PINNED there unless named DERIVED.

| Changed | Population | What keeps it green |
|---|---|---|
| `read_memory_root` leaves `loop_transition.py` | its callers: `tools/loop/adapt.py` three lines, `tools/loop/budget.py` two, `tools/loop/loop_transition.py` four, and the opening read `TOOL-dDeclaredLoop-53` lands in `tools/loop/breakpoints.py` | each call and import moves to S1, re-derived by the pass's grep at its base (§4 "The callers") |
| the same | the same-named functions of other kits: `skills/session-kickoff/manifest-check.sh`, `tools/branch-reconcile/branch_reconcile.py`, `tools/playbook/positional.py` and `tools/policy/check_policy.py` | other modules, none importing the loop kit's; untouched |
| the same, and S1 minted | `memory/map/generated/symbols.json`, its row for `loop_transition.py` and a new row for `loop_lib.py`, under `codebase-map coverage + freshness` | `python tools/codebase-map/gen_map.py --write` regenerates it and its three siblings |
| S1's answer | the plants that copy gov's two confs, both `memory`: `budget.py`'s `driver-draws`, `spent-spec-round` and `driver-exhausted`; `breakpoints.py`'s `driver-close`, `driver-optin` and `driver-plan`; `position.py`'s driver plants; and `loop_witness.py`'s `hold-inherited`, which writes `MEMORY_ROOT=memory` | the confs agree, so S1 answers `memory` and S2 is silent; each Python process the driver starts there sources the conf once |
| the same | every other loop plant, whose scratch has `.memory-tree.conf` and no `.unattended.conf`, `TOOL-dDeclaredLoop-64`'s `pre-placement-records-root` at `MEMORY_ROOT=records` among them | the no-driver-conf branch is the tip's reading |
| the same | the driver's own suites, whose scratch confs each set `MEMORY_ROOT=memory` | any loop read they reach answers `memory` |
| S2 | gov's tree | both confs set `memory` |
| S2's `ValueError` | the handlers between it and a verb: each module's `main`, `derive_position`, and `write_flow_states`' handler | the first two print it by name; the third is never reached before `read_run_file` raises (§4 "Evidence") |
| four plants added | the legs `loop budget fixtures` and `loop breakpoint fixtures`, which run `--selftest`, and their rows in `tools/run-gates/selftest-budgets.txt`, priced 476 seconds PINNED and 179 seconds PINNED at the tip, both proxies | each row re-priced from a timed run of its leg's plants with these, PINNED with date and node by that file's rule; neither manifest ceiling of 300 seconds PINNED is raised, and a priced reading past it is a divergence the pass reports, as the budget row's already is |
| the same | the two legs' `[[exempt_leg]]` rows in `tools/govkit/registry.toml` and the two scripts' usage rows in `tools/govkit/usage.toml` | the rows name no plant; no verb or flag is added |
| `help/loop.md` | `docs`, `help page commands`, `help reference pages` | one prose paragraph under an existing heading, no command, no usage row or anchor |
| `tools/loop/README.md`, `tools/loop/kit.toml` | the kit's version marker and the descriptor read by `tools/govkit/` | a table row and a comment; the loop kit's version is owed at the lander |
| shipped bytes | `install-prefix (shipped surface)` | the new lines name conf files and a root read from them, never a kit path |
| sibling specs | 75, 76, 79, 82, 95, 97, 99 and 100 name `resolve_memory_root` in `loop_lib.py`, its two branches, its refusal and the two plants, all kept; 76 and 82 quote rev-5's AC4 grep; 53 and 64 cite `read_memory_root` as the root read; 71 rev-2 names a leg `loop breakpoints fixtures` | the names, branches and plants hold; AC4 is restated (§9) and 76 and 82 re-ground on it; 53 and 64 build first and this unit moves their read; the arms run under unit 19's built leg |
| another build | `TOOL-dFurnishedOrders-37` S9 cites §4's rule for its own reader | the rule is unchanged |
| `memory/project/positional-refs.txt` | its three rows for this spec, naming rev-5's line citations into the memory-tree kit, the unattended kit's descriptor and the driver, under `positional (the citation check alone)` | this revision cites symbols only, so the commit landing it runs `python tools/playbook/positional.py shrink`, which takes the three rows out |

```
B=branch/unattended-declared-loop-d56bf0
git grep -c -w read_memory_root "$B" -- tools/loop                       # adapt 3, budget 2, loop_transition 4
git grep -c "unattended\.conf" "$B" -- 'tools/loop/*.py'                  # budget, breakpoints, loop_witness, position: 1 each
git grep -c -e read_design_conf -e parse_conf -e read_driver_conf "$B" -- tools/loop/budget.py tools/loop/breakpoints.py   # no match
git grep -n "MEMORY_ROOT" "$B" -- 'tools/unattended/*.test.sh'            # every scratch conf sets memory
git show "$B:tools/unattended/unattended.sh" | grep -n -e '^MEMORY_ROOT=memory' -e '^\. "\$CONF"' -e '^M="\$MEMORY_ROOT"'
git show "$B:tools/run-gates/selftest-budgets.txt" | grep -e '^loop budget fixtures' -e '^loop breakpoint fixtures'
git show "$B:.memory-tree.conf" | grep '^REFUSAL_CEILINGS'                 # the driver's token, ceiling 342
git show "$B:.lexicon.conf" | grep '^VERB_OFFENDER_PIN'                    # "1215"
git show "$B:.unattended.conf" | grep -e '^MEMORY_ROOT' -e '^SHARED_RECORDS'
git show "$B:memory/guides/SESSION-KICKOFF.md" | grep '^watch:'
git show "$B:memory/project/positional-refs.txt" | grep -c 'spec-TOOL-dDeclaredLoop-72.md'   # 3
```

### Budgets and records

- The lexicon offender pin: `VERB_OFFENDER_PIN` in `.lexicon.conf` stays 1215 PINNED. The one function
  minted leads with `resolve` and the retired one with `read`, both declared verbs (§4 "Inventory").
- The shared records: `SHARED_RECORDS` in `.unattended.conf` names `memory/DECISIONS.md` and
  `memory/project/readme-contract.txt`. The pass writes neither, and no decision row is owed ahead.
- The refusal ceilings and families: no `*.sh` is edited, so `tools/memory-tree/check-arms.py#branches`
  and `tools/memory-tree/check-arms.py#scan_refusal_sites`, which read tracked `*.sh` files alone, read
  the same sites. The driver's ceiling is 342 at the tip and 343 once `TOOL-dDeclaredLoop-52` lands under
  its decision row, both PINNED; `tools/unattended/unattended.families.txt` does not move.
- Help anchors: no verb or flag is added, so no usage row and no anchor.
- Subject pins, epoch delegates, upgrade rows and the kickoff watch list: no leg is added, no delegate in
  `tools/memory-tree/check-verdict-epoch.sh` names a loop module, no `[[upgrade]]` row is owed, and no file
  the `watch:` line of `memory/guides/SESSION-KICKOFF.md` names is edited.

### Dependency

`TOOL-dDeclaredLoop-70` (order 36, committed rev-2) is read for `read_driver_conf(tree, names)` in
`tools/loop/loop_lib.py`, its sourced read and its refusal; it builds before this unit within order 36.
`TOOL-dDeclaredLoop-53` (order 34, committed rev-3) is read for the opening read under
`read_memory_root` and the pre-placement staging, and `TOOL-dDeclaredLoop-64` (order 35, committed rev-4)
for that staging's root and README arguments and its `pre-placement-records-root` plant; this unit builds
over both units' landed code. `TOOL-dDeclaredLoop-19` and `TOOL-dDeclaredLoop-30` are CLOSED and built
the two legs and their rows. At order 34, `TOOL-dDeclaredLoop-33` (committed rev-6) edits `adapt.py`,
`loop_transition.py`, `README.md`, `help/loop.md` and `selftest-budgets.txt`, and
`TOOL-dDeclaredLoop-52` (committed rev-3) edits `breakpoints.py`, `README.md` and `help/loop.md`, each at
other functions, sections and rows. At order 35, `TOOL-dDeclaredLoop-54` (rev-3) edits `README.md` and
`help/loop.md`, `TOOL-dDeclaredLoop-63` (rev-3) edits `breakpoints.py` and `help/loop.md`, and
`TOOL-dDeclaredLoop-55` (rev-3) writes nothing. At order 36, `TOOL-dDeclaredLoop-56` (rev-5) edits
`loop_lib.py` and `loop_transition.py` at other functions, the three modules of §3's readers, and
`kit.toml` and `selftest-budgets.txt` at other lines, and `TOOL-dDeclaredLoop-71` (rev-2) edits
`breakpoints.py`, `kit.toml` and the leg manifest. `TOOL-dDeclaredLoop-34` is
deferred against ask TOOL-dDeclaredLoop-113 and `TOOL-dDeclaredLoop-33`'s numeric direction against ask
TOOL-dDeclaredLoop-114; neither moves a read this unit makes. The reuse probe, the recall query and the
lexicon verb ran on the worktree at `179486e8f`, which holds no loop kit; every other claim was read on
the branch.

## 6. Acceptance criteria

Each `python budget.py` and `python breakpoints.py` command below runs in the loop kit's folder.

- **AC1** — When `python budget.py --fixture --plant unattended-root` runs, it prints `held`: in a
  scratch whose `.unattended.conf` sets `MEMORY_ROOT=records` and whose `.memory-tree.conf` sets no
  `MEMORY_ROOT`, both draws on `tFix` exit 0, the build's run-state file under the records root holds the
  freeze row and both draw rows, and `budget_state` answers `open 2/6`.
  Red when: the read takes `.memory-tree.conf` alone, finds no run-state file or record under
  `memory/builds/tFix/`, and refuses the draw.
  figure: `6` DERIVED, the default `4+2` at the one unit.
- **AC2** — When `python breakpoints.py --fixture --plant unattended-root` runs, it prints `held`: in a
  scratch of the same two confs, the scratch's module prints, for `list --build tRec`,
  `breakpoint: owner gate · at item.design.exit · owner · autonomy · passed before placement`, the same
  release at `item.plan.exit` and before `item.deploy.mandate`, and no `breakpoints: held` line.
  Red when: the opening read looks under `memory/builds/`, finds no commit adding the README, and holds
  `tRec`.
- **AC3** — When `--plant confs-disagree` runs in each of `budget.py` and `breakpoints.py`, each prints
  `held`: with `.unattended.conf` at `records` and `.memory-tree.conf` at `memory`, the `draw` exits 2
  printing `loop: budget · refused · records root: .unattended.conf says records, .memory-tree.conf says
  memory — the driver writes under records` and leaves the run-state file's bytes as they were, and
  `list --build tFix` exits 2 printing `breakpoints: refused · ` followed by the same text.
  Red when: either reader picks one conf silently.
- **AC4** — When `git grep -n -w read_memory_root -- tools/loop` runs at the pass commit, it prints
  nothing; and when `grep -c "read_design_conf\|read_driver_conf\|parse_conf" budget.py breakpoints.py`
  runs in `tools/loop/`, each file prints 0.
  Red when: a module keeps its own reading of the root beside S1.
- **AC5** — When `grep -c "records root"` runs over the loop kit's help page, help/loop.md, and
  `grep -c "resolve_memory_root"` over the kit's README, tools/loop/README.md, each prints at least 1.
  Red when: the refusal ships and neither page names it.

## 7. Gates

`docs` · `help page commands` · `help reference pages` · `install-prefix (shipped surface)` · `positional (the citation check alone)` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The plants run under the built legs `loop budget fixtures` and `loop breakpoint fixtures`, which sit
outside the base manifest the leg line is joined against.

New arm: tools/loop/budget.py · covers AC1 AC3 · the unattended-root and confs-disagree plants, staged against the tip's `read_memory_root`, which reads `.memory-tree.conf` alone · none
New arm: tools/loop/breakpoints.py · covers AC2 AC3 · the same two plants, staged against the same read under the opening-commit rule · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — Read the driver's conf, or refuse a disagreement?** The fix offers either. (a) read
  `.unattended.conf`; (b) refuse when the confs disagree; (c) both. (c) satisfies every criterion either
  satisfies and leaves no silent pick. RESOLVED (agent, 2026-10-24, delegated): (c).
  widens: none · relaxes: none
- **F3 — Where does the resolver live, and what becomes of `read_memory_root`?** At the tip the loop kit
  already reads the root in one function, `loop_transition.py`'s `read_memory_root`. Options: (a)
  `resolve_memory_root` in `loop_lib.py`, `read_memory_root` kept as a one-line delegate of it; (b)
  `resolve_memory_root` in `loop_lib.py`, every caller moved to it and `read_memory_root` retired; (c)
  the rule written into `read_memory_root`, no new name. (c) moves the name and file that units 75, 76,
  79, 82, 95, 97 and 99 build on, and keeps the driver-conf read apart from `read_driver_conf`; (a) keeps
  two names for one root, either of which a later caller may take. Recommendation: (b), one name and one
  function, the callers' diff a line each. RESOLVED (agent, 2026-11-16, delegated): (b).
  widens: none · relaxes: none
- **F4 — Do the four other loop readers of `MEMORY_ROOT` move to S1 too?** Options: (a) the callers of
  the shared reader only, the population the finding names; (b) those four as well, §3's list. They differ
  from S1 in one conf shape, `.memory-tree.conf` without the key beside a driver conf naming another
  root, and each then fails on a folder it does not find. (b) edits three modules
  `TOOL-dDeclaredLoop-56` edits at this order, and `read_builds_dir` keys its answer on `DESIGN_RECORD`,
  a second rule. Recommendation: (a), the class recorded at the close. RESOLVED (agent, 2026-11-16,
  delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-3 spec audit's id 29 (HIGH, item H5).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the bullets mirroring the edges of
  TOOL-dDeclaredLoop-76 and TOOL-dDeclaredLoop-79, written by the round-4 spec audit's disposal; nothing else moved.
- rev-3 · 2026-10-24 · §3 · the Edges block gains the bullets mirroring the edges of
  TOOL-dDeclaredLoop-82, written by the round-5 spec audit's disposal; nothing else moved.
- rev-4 · 2026-10-24 · §3 · the Edges block gains the bullet mirroring the edge of
  TOOL-dDeclaredLoop-95, written by the round-11 spec audit's disposal; nothing else moved.
- rev-5 · 2026-10-24 · §3 · the Edges block gains the bullet mirroring the edge of
  TOOL-dDeclaredLoop-100, written by the round-12 spec audit's disposal; nothing else moved.
- rev-6 · 2026-11-16 · §1 to §10 · S1 to S5 · AC1 to AC5 · §8 F3, F4 · re-grounded on branch
  `unattended-declared-loop-d56bf0` at `bd31adbcc` and on the committed specs of TOOL-dDeclaredLoop-53,
  TOOL-dDeclaredLoop-64 and TOOL-dDeclaredLoop-70, per the brief
  `2026-11-16-prompt-TOOL-dDeclaredLoop-72-1-spec-writer`: the loop kit's existing root reader,
  `read_memory_root`, is the read this unit points at the driver's root, its callers moved to
  `resolve_memory_root` and the name retired (F3); the memory-tree read is `read_design_conf`; S2's
  refusal is stated to the pseudo-code; the plants are staged on the built modules, the breakpoints one
  on the pre-placement staging; AC4's literal-name grep, already red at the tip from the driver plants, is
  restated to the retired name and the reader calls; S5 carries the rule to help, the kit README and the
  descriptor comment; the four other readers are out (F4); line citations made symbol citations; the
  sweep.

## 10. Reuse audit

The seam is the loop kit's existing root reader, `tools/loop/loop_transition.py#read_memory_root`, which
every caller already goes through: its rule moves into `resolve_memory_root` beside `read_driver_conf`
(`TOOL-dDeclaredLoop-70`) in `tools/loop/loop_lib.py`, and its callers follow it. The memory-tree side
is `tools/memory-tree/design_lib.py#read_design_conf`, which the tip's reader already calls.

`python tools/codebase-map/reuse_lookup.py "resolve the records root the unattended driver writes under from its conf and the memory tree conf"`,
on the worktree at `179486e8f`, ranked `tree`, `resolve`, `resolve_kit_dir`, `repo_root`, `load_conf`,
`parse_conf` and `read_design_conf`; none reads the driver's `MEMORY_ROOT`, and `read_design_conf` is the
memory-tree read S1 keeps. The runlog kit's `resolve_memory_root` reads `.memory-tree.conf` alone, in a
kit the loop kit takes no edge to.
`python tools/memory-recall/query.py "the loop kit reads the records root the unattended driver writes under" --terms "<the terms below>"`
returned this spec's rev-5, the round-3 audit's id 29, `TOOL-dDeclaredLoop-64` and
`TOOL-dDeclaredLoop-60`, and no other reader of the driver's root in the loop kit.

Recall terms used: MEMORY_ROOT unattended.conf memory-tree.conf records root driver root read_memory_root budget opening commit two confs disagree
