# TOOL-dSweptBranches-5 — the skill: a rendered `/branch-reconcile` that routes cleanup asks through the tool

**Status:** CLOSED · rev-1 · 2026-10-13 · node d · Tier-2 · base 2b852f5f · streams tooling · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-13-build-TOOL-dSweptBranches-5-1-acceptance-ledger.md](../build/2026-10-13-build-TOOL-dSweptBranches-5-1-acceptance-ledger.md) | journal | — |
| [2026-10-13-prompt-TOOL-dSweptBranches-1-brief.md](../prompts/2026-10-13-prompt-TOOL-dSweptBranches-1-brief.md) | research | TOOL-dSweptBranches-1 TOOL-dSweptBranches-2 TOOL-dSweptBranches-3 TOOL-dSweptBranches-4 |
| [2026-10-13-prompt-TOOL-dSweptBranches-5-1-build-brief.md](../prompts/2026-10-13-prompt-TOOL-dSweptBranches-5-1-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

A skill, `/branch-reconcile`, triggers on cleanup asks and routes them through
`branch_reconcile.py`, the way memory-recall routes through its CLI. Attended, it surfaces the live
and undecidable rows as decisions before any deletion. Unattended, it reports and deletes only the
safe rows.

## 2. Scope (IN)

- **S1** — `tools/branch-reconcile/SKILL.template.md`, rendered by
  `tools/branch-reconcile/adopt-branch-reconcile.sh --scaffold` to
  the skills directory as branch-reconcile/SKILL.md, with `KIT_DIR` substituted, and graded by `--check`,
  which re-renders and compares. Observed by AC1.
- **S2** — The skill's description triggers on "clean up branches", "reconcile worktrees", "stale
  branches" and "is any unmerged work left". Observed by AC2.
- **S3** — The attended route: fetch the remote, run the report, list the `UNMERGED-LIVE` and
  `UNKNOWN` rows first as the owner's decisions, and run `--write` only on the owner's yes, with
  `--remote` only on its own yes. Observed by AC2.
- **S4** — The offer for an `UNMERGED-LIVE` branch: merge the default branch into it in its own
  worktree; re-render generated artifacts instead of picking a side; union append-only logs; gate
  the result. Landing still needs the owner's explicit ask, through the repository's own lander.
  Observed by AC2.
- **S5** — The unattended route: the report and `--write`, never `--remote` without its own grant,
  and never a merge. Observed by AC2.
- **S6** — `kit.toml` gains the rendered row, its `[[regenerate]]`, `[check]` and `[adopt]` argv, an
  outcome probe, the `branch-reconcile skill wiring` gate leg and its `lf_pin`. Gov's own render is
  committed, and the leg joins `tools/gate-legs.json` with its subject pin. Observed by AC1 and AC3.

## 3. Non-goals (OUT)

- No merge performed by the tool. The skill instructs the agent.
- No landing. The skill names the repository's lander and stops.

### Edges

- **consumes-from** `TOOL-dSweptBranches-3` — the write flags the routes drive.

## 4. Design

The adopter is the runlog kit's adopter cut down to one placeholder: `--scaffold` renders,
`--check` re-renders into memory and compares bytes with CR stripped, and exits 1 on a difference
naming the file. The template carries `{{KIT_DIR}}`, resolved as the kit's directory relative to the
repository root.

### Files touched (estimate)

- `tools/branch-reconcile/SKILL.template.md`
- `tools/branch-reconcile/adopt-branch-reconcile.sh`
- `tools/branch-reconcile/kit.toml`
- `tools/branch-reconcile/README.md`
- `.claude/skills/branch-reconcile/SKILL.md`
- `.gitattributes`
- `tools/gate-legs.json`
- `tools/govkit/subject-pins.tsv`
- `memory/map/features/branch-reconcile.md`

### Alternatives rejected

- A static skill naming `tools/branch-reconcile/`. An adopter installs kits under its own prefix, so a
  literal path is wrong there and the install-prefix gate refuses it.

## 5. Production-readiness checklist

- security — the skill grants nothing: write mode stays behind the owner's yes when attended.
- perf / scale — N/A: a document and a renderer.
- error / empty / loading states — `--check` names a missing or stale render.
- observability — the wiring leg.
- risks — an agent following the unattended route deletes a remote branch. S5 forbids `--remote`
  without its own grant.
- testing — AC1 to AC3.
- migration — adopters receive the render through `govkit update`'s regenerate.
- user docs — the skill is the doc, and the kit README points at it.

## 6. Acceptance criteria

- **AC1** — When one byte is appended to the rendered `SKILL.md`,
  `adopt-branch-reconcile.sh --check` exits 1 naming it, and `--scaffold` restores the bytes.
  Red when: `--check` compares nothing.
- **AC2** — When `grep -c` runs over the rendered `SKILL.md` for the four trigger phrases, the
  attended and unattended headings, `UNMERGED-LIVE`, `--remote` and the merge offer, each is found.
  Red when: a route is dropped from the template.
- **AC3** — When `python tools/govkit/govkit.py selfcheck` runs, it exits 0 with the rendered row
  declared, and `bash tools/check-kit-versions.sh` exits 0.
  Red when: the row's placeholders differ from the template's.

## 7. Gates

`branch-reconcile selftest` · `govkit selfcheck` · `kit version markers` · `codebase-map coverage + freshness` · `memory hygiene` · `check-wiring self-test` · `recall floor` · `recall floor arms` · `govkit selftest` · `lexicon naming predicates` · `govkit refusal join` · `govkit acceptance matrix` · `install-prefix (shipped surface)` · `kit placeholders (a declared token its adopter substitutes)` · `run-gates canary` · `run-gates gov canary`

New arm: `tools/branch-reconcile/adopt-branch-reconcile.sh` · covers AC1 · one byte appended to the render, then restored · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-13 · initial draft.

## 10. Reuse audit

The seam is the runlog kit's adopter, `tools/runlog/adopt-runlog.sh`, with its `--scaffold` and
`--check` pair and its rendered row in `tools/runlog/kit.toml`. The skill's routing shape is
`.claude/skills/memory-recall/SKILL.md`'s. `reuse_lookup.py` ranked no other renderer.

Recall terms used: "is there a tool that reconciles stale branches and worktrees and deletes merged
ones" --terms "stragglers worktree branch merged prune cleanup reconcile relocation orphaned
superseded cherry ancestor lease"
