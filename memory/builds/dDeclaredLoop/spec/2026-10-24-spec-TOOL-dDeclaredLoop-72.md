# TOOL-dDeclaredLoop-72 — the loop kit reads the records root the driver reads, and refuses two confs that disagree

**Status:** OPEN · rev-4 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 36 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-68-promoted-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-68-promoted-fix-return.md) | research | TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 |
| [2026-10-24-build-TOOL-dDeclaredLoop-72-deviation-721.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-72-deviation-721.md) | deviation | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-68-promoted-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-68-promoted-fix-brief.md) | research | TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 |
| [2026-10-24-review-TOOL-dDeclaredLoop-68-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-68-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 |

<!-- /gen:spec-records -->

## 1. Goal

The round-3 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-57-spec-audit.md`)
confirmed finding **id 29 at HIGH**, its item **H5**. The same defect is item M2 at medium (ids 4, 12, 42,
44) and its rationale half is item L2 at low (id 17), all three batched into `TOOL-dDeclaredLoop-75`.
`TOOL-dDeclaredLoop-60` S2 and `TOOL-dDeclaredLoop-64` S1 read `MEMORY_ROOT` from `.memory-tree.conf`.
The driver reads it from `.unattended.conf`: it defaults `MEMORY_ROOT=memory`
(`tools/unattended/unattended.sh:560`), sources that conf (:617), binds `M` (:739), writes run records
under `$M/builds/` (:3313) and reads each README at `$M/builds/<slug>/README.md` (:1348). Nothing checks
that the two confs agree. Where they disagree, `budget_state` counts zero draws and the budget refills,
and the opening-commit rule looks for a README under a root the driver did not use.

This unit gives both readers the driver's root through one function, and refuses by name where the two
confs name different roots. 64 builds at order 35 and 60 at order 30, so this unit follows the later of
the two and repairs both; its placement names `TOOL-dDeclaredLoop-64`.

## 2. Scope (IN)

- **S1** — `resolve_memory_root(tree)` in `tools/loop/loop_lib.py`. Where `.unattended.conf` exists the
  root is its `MEMORY_ROOT`, read through `TOOL-dDeclaredLoop-70`'s `read_driver_conf`, or `memory` when
  the conf leaves it unset, the driver's default. Where it does not exist, the root is
  `.memory-tree.conf`'s `MEMORY_ROOT` through the memory-tree kit's `parse_conf`, or `memory`.
  Observed by AC1, AC2.
- **S2** — Where both confs declare `MEMORY_ROOT` and the values differ, `resolve_memory_root` refuses
  by name: `records root: .unattended.conf says <a>, .memory-tree.conf says <b> — the driver writes under
  <a>`. Observed by AC3.
- **S3** — `budget_state`'s population (60 S1, S2) and the opening-commit rule's README path (64 S1)
  take their root from S1 alone; neither file reads either conf itself. Observed by AC1, AC2, AC4.
- **S4** — The fixture cases `confs-disagree` and `unattended-root` join `budget.py --fixture` and
  `breakpoints.py --fixture`: the two confs naming `records` and `memory`, and `.unattended.conf` alone
  naming `records`. Observed by AC1, AC3.

## 3. Non-goals (OUT)

- Where the driver writes: `tools/unattended/unattended.sh`, unchanged.
- The per-reader plants, wording and `--explain` line the medium and low grades of this defect ask for:
  ids 4, 12, 42, 44 and 17, scope items of `TOOL-dDeclaredLoop-75`.
- A check that reds two confs naming different roots across the whole tree, the finding's gate
  left-shift: S2 refuses at the two readers that act on the root; a tree-wide leg is recorded at the
  close.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-60` — `budget_state`'s run-state population and its root read, which this unit points at the driver's root
- **consumes-from** `TOOL-dDeclaredLoop-64` — the opening-commit rule's README path and its root read, which this unit points at the driver's root
- **consumes-from** `TOOL-dDeclaredLoop-70` — `read_driver_conf`, the loop kit's one reader of the driver's conf
- **hands-off** `TOOL-dDeclaredLoop-75` — the resolved root, beside which that unit adds the per-reader plants, the docstrings and the `--explain` line (ids 4, 12, 17, 42, 44)
- **hands-off** `TOOL-dDeclaredLoop-76` — `resolve_memory_root` and AC4's no-own-conf-read property, which that unit gives a source value and grades on the syntax tree, its plant observing what AC4's substring grep stated (the round-4 spec audit's id 1)
- **hands-off** `TOOL-dDeclaredLoop-79` — `resolve_memory_root`'s refusal and its `.memory-tree.conf` read, which that unit restates to the pseudo-code's population over normalised paths and to `parse_conf`'s real signature (ids 15, 35)
- **hands-off** `TOOL-dDeclaredLoop-82` — AC4, which that unit amends in place to observe through the `no-own-conf-read` plant (the round-5 spec audit's id 2)
- **hands-off** `TOOL-dDeclaredLoop-95` — `resolve_memory_root` and AC3's `confs-disagree` plant, which that unit re-runs over the moved read (the round-11 spec audit's id 1)

## 4. Design

### Evidence

- `MEMORY_ROOT=memory` is set before `. "$CONF"` (`tools/unattended/unattended.sh:560`, :617), so an
  unset key reads `memory`; `CONF="$ROOT/.unattended.conf"` (:547).
- The driver reads `.memory-tree.conf` only for other keys (:4576, :5687-5688, :9873); `readme_of`
  spells `$M/builds/$1/README.md` (:1348).
- gov's `.unattended.conf:9` comments that its value matches `.memory-tree.conf`, and
  `tools/unattended/kit.toml:174` lists `MEMORY_ROOT` as an optional key; no check compares the two.

### The resolution

```
resolve_memory_root(tree):
    mt = parse_conf(tree/.memory-tree.conf).get("MEMORY_ROOT")       # None when the file or key is absent
    if (tree/.unattended.conf) exists:
        ua = read_driver_conf(tree, ["MEMORY_ROOT"]).get("MEMORY_ROOT") or "memory"
        if mt and mt != ua: refuse "records root: .unattended.conf says ua, .memory-tree.conf says mt ..."
        return ua
    return mt or "memory"
```

### Files touched (estimate)

- `tools/loop/loop_lib.py`
- `tools/loop/budget.py`
- `tools/loop/breakpoints.py`

### Alternatives rejected

- **The driver passing `--memory-root "$M"`.** It is exact for driver calls but leaves a hand run and a
  fixture with no source; S1 reads the same conf the driver sources, so both agree by construction.
- **Reading `.memory-tree.conf` and warning on disagreement.** A warning beside a zero count is the
  silent refill the finding names.

## 5. Production-readiness checklist

- security — a read; S2 fails closed on a misconfigured tree.
- perf / scale — one conf source per process, memoised by `read_driver_conf`.
- error / empty / loading states — an unset key reads the driver's default; S2 names a disagreement.
- observability — S2's refusal names both files, both values and the root the driver writes under.
- risks — an adopter whose two confs disagree today is refused at the budget and placement reads until
  it aligns them; its driver and memory tree already disagree on where records live.
- testing — AC1 to AC4 as plants; the arms under §7, observed at the close.
- migration — none: the readers are unbuilt at base.
- user docs — none.

## 6. Acceptance criteria

- **AC1** — When `python budget.py --fixture --plant unattended-root` draws in a tree whose
  `.unattended.conf` sets `MEMORY_ROOT=records` and that has no `.memory-tree.conf`, `budget_state`
  answers the drawn count.
  Red when: the reader takes `.memory-tree.conf` alone and counts nothing under `records/builds/`.
- **AC2** — When `python breakpoints.py --fixture --plant unattended-root` opens a build under
  `records/builds/` in the same tree shape and then places the gate, the gate is listed
  `passed before placement`.
  Red when: the rule looks under `memory/` and holds the build.
- **AC3** — When `--plant confs-disagree` runs in each of `budget.py` and `breakpoints.py` with
  `.unattended.conf` at `records` and `.memory-tree.conf` at `memory`, each exits non-zero printing
  `records root:` and both values.
  Red when: either reader picks one conf silently.
- **AC4** — When `grep -c ".memory-tree.conf\|.unattended.conf" budget.py breakpoints.py` runs in `tools/loop/`,
  each prints 0.
  Red when: a reader keeps its own conf read beside S1.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)`

This pass keeps the sibling-minted `loop budget fixtures` leg (`TOOL-dDeclaredLoop-30`) and the
`loop breakpoints fixtures` leg (`TOOL-dDeclaredLoop-71`) green; both sit outside the base manifest.

New arm: tools/loop/budget.py · covers AC1 AC3 · the unattended-root and confs-disagree plants, staged against TOOL-dDeclaredLoop-60's .memory-tree.conf read · none
New arm: tools/loop/breakpoints.py · covers AC2 AC3 · the same two plants, staged against TOOL-dDeclaredLoop-64's .memory-tree.conf read · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — Read the driver's conf, or refuse a disagreement?** The fix offers either. (a) read
  `.unattended.conf`; (b) refuse when the confs disagree; (c) both. (c) satisfies every criterion either
  satisfies and leaves no silent pick. RESOLVED (agent, 2026-10-24, delegated): (c).
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-3 spec audit's id 29 (HIGH, item H5).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the bullets mirroring the edges of
  TOOL-dDeclaredLoop-76 and TOOL-dDeclaredLoop-79, written by the round-4 spec audit's disposal; nothing else moved.
- rev-3 · 2026-10-24 · §3 · the Edges block gains the bullets mirroring the edges of
  TOOL-dDeclaredLoop-82, written by the round-5 spec audit's disposal; nothing else moved.
- rev-4 · 2026-10-24 · §3 · the Edges block gains the bullet mirroring the edge of
  TOOL-dDeclaredLoop-95, written by the round-11 spec audit's disposal; nothing else moved.

## 10. Reuse audit

The seams are `read_driver_conf` (`TOOL-dDeclaredLoop-70`), which sources the conf the driver sources, and
the memory-tree kit's `parse_conf` (`tools/memory-tree/tree_lib.py:135`) for a tree without the
unattended kit. `python tools/codebase-map/reuse_lookup.py "resolve the memory root the driver uses"`
ranked `resolve` (`tools/memory-recall/recall_conf.py`), `repo_root`, `resolve_kit_dir` and `map_root`;
none reads the driver's `MEMORY_ROOT`, so S1 is the loop kit's one resolver over the two seams.

Recall terms used: MEMORY_ROOT unattended.conf memory-tree.conf driver root records root budget_state opening commit README two-readers
