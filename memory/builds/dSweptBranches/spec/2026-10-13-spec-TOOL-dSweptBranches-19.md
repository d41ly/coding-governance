# TOOL-dSweptBranches-19 — the skill is `/cleanup`, renamed with every live reference

**Status:** CLOSED · rev-1 · 2026-10-13 · node d · Tier-2 · base 2b852f5f · streams tooling · order 17

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-13-build-TOOL-dSweptBranches-19-1-acceptance-ledger.md](../build/2026-10-13-build-TOOL-dSweptBranches-19-1-acceptance-ledger.md) | journal | — |
| [2026-10-13-prompt-TOOL-dSweptBranches-19-1-build-brief.md](../prompts/2026-10-13-prompt-TOOL-dSweptBranches-19-1-build-brief.md) | journal | — |
| [2026-10-13-prompt-TOOL-dSweptBranches-19-owner-follow-up.md](../prompts/2026-10-13-prompt-TOOL-dSweptBranches-19-owner-follow-up.md) | research | TOOL-dSweptBranches-20 TOOL-dSweptBranches-21 |
| [2026-10-13-review-TOOL-dSweptBranches-19-20-21-closing-diff-round1.md](../reviews/2026-10-13-review-TOOL-dSweptBranches-19-20-21-closing-diff-round1.md) | diff-review | TOOL-dSweptBranches-20 TOOL-dSweptBranches-21 |

<!-- /gen:spec-records -->

## 1. Goal

The owner renamed the kit's skill from `/branch-reconcile` to `/cleanup` (2026-10-13). Every live
reference moves with it, so no adopter renders, triggers or wires a skill by the old name.

## 2. Scope (IN)

- **S1** — `SKILL.template.md` declares `name: cleanup`, and its prose names `/cleanup`.
  **Readers:**
  by name: `tools/branch-reconcile/README.md` and `WIRE-INTO-PROJECT.md`, which name the skill.
  by value: NO VALUE READERS — the harness reads the name to list the skill, and nothing in this tree
  compares or counts it.
  Observed by AC1.
- **S2** — The adopter renders the skills directory's cleanup/SKILL.md, and its messages name the cleanup
  skill. The old render at `.claude/skills/branch-reconcile/SKILL.md` is moved, not copied.
  **Readers:**
  by name: `tools/branch-reconcile/kit.toml` (the rendered row, the outcome probe and the LF pin),
  `.gitattributes` and `memory/map/features/branch-reconcile.md`.
  by value: NO VALUE READERS — only the adopter's own `--check` byte-compares the render.
  Observed by AC1 and AC2.
- **S3** — The wiring leg `branch-reconcile skill wiring` becomes `cleanup skill wiring` in
  `tools/gate-legs.json`, the kit descriptor, `tools/govkit/subject-pins.tsv`, the dossier's claims and
  the README.
  **Readers:**
  by name: `tools/gate-legs.json`, `tools/branch-reconcile/kit.toml`, `tools/govkit/subject-pins.tsv`,
  `memory/map/features/branch-reconcile.md` and `tools/branch-reconcile/README.md`.
  by value: NO VALUE READERS — the runner and the meta-gates join on the name and count nothing by it.
  Observed by AC3.

## 3. Non-goals (OUT)

- The kit's directory, CLI, module, selftest leg and registry id keep `branch-reconcile`: they name
  the kit, not the skill.
- Closed specs, review and build records, and the run record keep the old name as history.

### Edges

- **consumes-from** `TOOL-dSweptBranches-5` — the skill, its adopter and its descriptor rows.

## 4. Design

A `git mv` of the rendered skill, then edits of each reader the Readers clauses name, then a
re-render through the adopter so the moved file is byte-identical to a fresh render. `govkit update`
moves an adopter's copy to the new destination its descriptor resolves, which is the documented
rename path, so no withdrawal is owed.

### Files touched (estimate)

- `tools/branch-reconcile/SKILL.template.md`
- `tools/branch-reconcile/adopt-branch-reconcile.sh`
- `tools/branch-reconcile/kit.toml`
- `tools/branch-reconcile/README.md`
- `.claude/skills/cleanup/SKILL.md`
- `.gitattributes`
- `tools/gate-legs.json`
- `tools/govkit/subject-pins.tsv`
- `memory/map/features/branch-reconcile.md`
- `WIRE-INTO-PROJECT.md`

### Alternatives rejected

- Renaming the whole kit to `cleanup`: the owner named the skill, and the kit's id, legs and paths
  are the adopters' install contract.

## 5. Production-readiness checklist

- security — N/A: a rename.
- perf / scale — N/A.
- error / empty / loading states — the adopter's `--check` names a missing render at the new path.
- observability — the wiring leg's line names the new path.
- risks — an adopter's old render is left behind; `govkit update` moves it.
- testing — AC1 to AC3.
- migration — adopters receive the move through `govkit update`.
- user docs — the kit README and the runbook.

## 6. Acceptance criteria

- **AC1** — When `adopt-branch-reconcile.sh --check` runs, it exits 0 naming
  the skills directory's cleanup/SKILL.md, whose front matter reads `name: cleanup`.
  Red when: the template or the adopter still names the old skill.
- **AC2** — When `git grep -n "/branch-reconcile\b\|skills/branch-reconcile"` runs over the tree
  outside this build's closed records and the run record, it finds nothing.
  Red when: a live reference keeps the old name.
- **AC3** — When `python tools/govkit/govkit.py selfcheck` runs, it exits 0 with the leg `cleanup skill
  wiring` declared, and the codebase-map check is green over the dossier claiming it.
  Red when: one of the leg's five readers keeps the old name.

## 7. Gates

`govkit selfcheck` · `codebase-map coverage + freshness` · `memory hygiene` · `check-wiring self-test` · `lexicon naming predicates` · `install-prefix (shipped surface)` · `recall floor` · `recall floor arms` · `run-gates canary` · `run-gates gov canary` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `branch-reconcile selftest`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-13 · initial draft, at the owner's instruction.

## 10. Reuse audit

`reuse_lookup.py` ranked only name-token neighbours; the seam is this build's own skill adopter,
`tools/branch-reconcile/adopt-branch-reconcile.sh`, and its descriptor rows. The rename path for a
rendered file is govkit's documented move, in `WIRE-INTO-PROJECT.md`'s maintenance section.

Recall terms used: "is there a tool that reconciles stale branches and worktrees and deletes merged
ones" --terms "stragglers worktree branch merged prune cleanup reconcile relocation orphaned
superseded cherry ancestor lease"
