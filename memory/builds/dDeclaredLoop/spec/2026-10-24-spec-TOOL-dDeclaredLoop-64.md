# TOOL-dDeclaredLoop-64 — a build's opening commit is found under the resolved `MEMORY_ROOT`, never a literal `memory/`

**Status:** DEFERRED · rev-3 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 35 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 |
| [2026-10-24-build-TOOL-dDeclaredLoop-57-promoted-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-57-promoted-fix-return.md) | research | TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 |
| [2026-10-24-build-TOOL-dDeclaredLoop-64-deviation-641.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-64-deviation-641.md) | deviation | — |
| [2026-10-24-build-TOOL-dDeclaredLoop-64-deviation-642.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-64-deviation-642.md) | deviation | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-57-promoted-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-57-promoted-fix-brief.md) | research | TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 |
| [2026-10-24-review-TOOL-dDeclaredLoop-57-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-57-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 |

<!-- /gen:spec-records -->

## 1. Goal

The round-2 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md`)
confirmed finding **id 57 at HIGH**, its item **H9**, alone in that item. `TOOL-dDeclaredLoop-53` §4's
rule spells `opened = commit adding memory/builds/<slug>/README.md`, and its §5 treats a build whose
README has no adding commit as opened after the placement, so held. In a tree whose `MEMORY_ROOT` is not
`memory` no such commit exists, and every pre-placement build is held at its plan gate on `--phase` and
`--close`, the in-flight wedge that unit exists to remove. The driver resolves its own paths through
`MEMORY_ROOT` (`tools/unattended/unattended.sh:560`, :739, :4298), and `TOOL-dDeclaredLoop-41` S1 treats a
non-`memory` root as a real adopter shape. This unit takes the report's fix. It repairs
`TOOL-dDeclaredLoop-53`.

## 2. Scope (IN)

- **S1** — The README path is `<MEMORY_ROOT>/builds/<slug>/README.md`, `MEMORY_ROOT` read from the tree
  root's `.memory-tree.conf` through the memory-tree kit's `parse_conf`, reached by
  `resolve_kit_dir("memory-tree", "tree_lib.py", here)`, the route `TOOL-dDeclaredLoop-41` S1 specifies;
  an absent conf or key reads `memory`, the driver's default. This supersedes the literal path in
  `TOOL-dDeclaredLoop-53` §4's rule. Observed by AC1, AC2.
- **S2** — A root that resolves but holds no `builds/<slug>/README.md` on `HEAD`'s history keeps
  `TOOL-dDeclaredLoop-53` §5's conservative reading, held, and now names the path it looked for:
  `breakpoint: owner gate · <position> · held — no commit adds <path>`, so a wrong root is visible on
  `--plan` instead of reading as an ordinary hold. Observed by AC3.
- **S3** — The fixture `MEMORY_ROOT=records` joins `TOOL-dDeclaredLoop-53` AC1's repository: the same
  pre-placement build, opened under `records/builds/`, is admitted. Observed by AC1.

## 3. Non-goals (OUT)

- Which adding commit is the oldest when the README was re-added: the audit's id 28, batched into
  `TOOL-dDeclaredLoop-67`.
- The literal root in `TOOL-dDeclaredLoop-48` and `-49`: the audit's ids 19 and 8, units
  `TOOL-dDeclaredLoop-60` and `TOOL-dDeclaredLoop-67`.
- A spec lint over literal `memory/builds/` paths, the finding's left-shift: the class is recorded at
  the close; S3 is this rule's non-default-root fixture.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-53` — the opening-commit rule in `tools/loop/breakpoints.py`, whose README path this unit resolves through the memory root
- **hands-off** `TOOL-dDeclaredLoop-67` — the resolved root of the opening-commit rule, beside which that unit fixes the oldest-add ordering and observes the literal root (ids 8 and 28)
- **hands-off** `TOOL-dDeclaredLoop-71` — the fixture plants of this unit's `New arm:`, which that unit's leg runs (the round-3 spec audit's id 28)
- **hands-off** `TOOL-dDeclaredLoop-72` — the records-root read, which that unit points at the driver's root (the round-3 spec audit's id 29)
- **hands-off** `TOOL-dDeclaredLoop-75` — the held line's root source and the docstring rationale (the round-3 spec audit's ids 17, 44)
- **hands-off** `TOOL-dDeclaredLoop-100` — S1's route clause, which that unit restates onto `read_tree_conf` (the round-12 spec audit's id 14)

## 4. Design

### Evidence

- `MEMORY_ROOT=memory` is the driver's default (`tools/unattended/unattended.sh:560`), `M="$MEMORY_ROOT"`
  its one binding (:739), and the scaffold writes `<MEMORY_ROOT>/builds/<slug>/RUN.md` (:4298): read at
  base `ed497191`.
- `tools/memory-tree/.memory-tree.conf.example` ships `MEMORY_ROOT` as a setting, and `parse_conf`
  (`tools/memory-tree/tree_lib.py:135`) is the kit's one reader of that file.

### The rule, restated

```
root      = parse_conf(<tree>/.memory-tree.conf).get("MEMORY_ROOT") or "memory"
placement = oldest commit adding <loop kit>/breakpoints.py on HEAD's history
opened    = commit adding <root>/builds/<slug>/README.md
held      = owner gate placed  and  (opened is none  or  merge-base --is-ancestor placement opened)
```

### Files touched (estimate)

- `tools/loop/breakpoints.py`

### Alternatives rejected

- **Asking the driver for the root.** No driver verb prints it, and the memory-tree conf is the file the
  driver itself defaults from.
- **Treating a missing README commit as pre-placement.** It would exempt every build of a tree whose
  root is misread, the silent exemption `TOOL-dDeclaredLoop-53` §5 refuses.

## 5. Production-readiness checklist

- security — the hold stays conservative where the README is not found; S2 only names why.
- perf / scale — one conf read per process.
- error / empty / loading states — an unreadable conf reads the default root and says so once.
- observability — S2's line names the path looked for.
- risks — an adopter that moved its root after opening builds holds those builds until the README's
  new path has an adding commit, which a move commit provides.
- testing — AC1 to AC3 as fixture probes; the arm under §7, observed at the close.
- migration — none.
- user docs — none beyond `TOOL-dDeclaredLoop-19` S10's protocol text.

## 6. Acceptance criteria

- **AC1** — When `python breakpoints.py --fixture --plant pre-placement-records-root` opens a build
  under `records/builds/` in a repository whose `.memory-tree.conf` sets `MEMORY_ROOT=records`, then adds
  the loop kit's `breakpoints.py`, the owner gate is listed `passed before placement`.
  Red when: the rule looks under a literal `memory/` and holds the build.
- **AC2** — When the same plant runs with no `.memory-tree.conf`, a build opened under `memory/builds/`
  is listed `passed before placement`.
  Red when: an absent conf leaves the root unresolved.
- **AC3** — When `--plant wrong-root` sets `MEMORY_ROOT=records` over a build opened under
  `memory/builds/`, the gate is held and the line names `records/builds/` and the slug.
  Red when: the hold prints no path, so a misread root looks like an ordinary hold.

## 7. Gates

`unattended kit gate` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/breakpoints.py · covers AC1 AC2 AC3 · the records-root, no-conf and wrong-root plants, staged against the literal-root rule `TOOL-dDeclaredLoop-53` §4 specified · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-2 spec audit's id 57 (HIGH, item H9).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the bullets mirroring the edges of
  TOOL-dDeclaredLoop-71 and TOOL-dDeclaredLoop-72 and TOOL-dDeclaredLoop-75, written by the round-3 spec audit's disposal; nothing else moved.
- rev-3 · 2026-10-24 · §3 · the Edges block gains the bullet mirroring the edge of
  TOOL-dDeclaredLoop-100, written by the round-12 spec audit's disposal; nothing else moved.

## 10. Reuse audit

The seam is the memory-tree kit's `parse_conf` reached by `resolve_kit_dir`, the root route
`TOOL-dDeclaredLoop-41` S1 already specifies for a sibling reader in this build. `python
tools/codebase-map/reuse_lookup.py "resolve the memory root from the memory-tree conf"` ranked `tree`,
`resolve` (`tools/memory-recall/recall_conf.py`), `load_conf`, `repo_root`, `parse_conf`
(`tools/memory-tree/tree_lib.py`) and `resolve_kit_dir`; `parse_conf` and `resolve_kit_dir` are the two
this unit calls, and the recall kit's `resolve` reads that kit's own conf.

Recall terms used: MEMORY_ROOT memory-tree conf parse_conf resolve_kit_dir breakpoints placement opened README pre-placement hold
