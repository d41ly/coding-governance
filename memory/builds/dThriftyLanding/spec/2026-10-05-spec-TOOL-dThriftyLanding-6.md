# TOOL-dThriftyLanding-6 — the carriers state how a doc-only push is scoped

**Status:** CLOSED · rev-2 · 2026-10-05 · node d · Tier-1 · base c3ef6742 · streams tooling · order 6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-05-build-TOOL-dThriftyLanding-6-1-acceptance-ledger.md](../build/2026-10-05-build-TOOL-dThriftyLanding-6-1-acceptance-ledger.md) | journal | — |
| [2026-10-05-prompt-TOOL-dThriftyLanding-6-1-build-brief.md](../prompts/2026-10-05-prompt-TOOL-dThriftyLanding-6-1-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

Units 1 to 5 add a manifest key, a runner mode, a hook decision, a deployer field and a shared stamp.
A reader learns each from four places: the run-gates kit README, the runbook an adopter follows, the
gate-env notes where the key is declared, and the charter's merge-bar section. This unit writes the
mechanism into each, once, pointing at the source that owns it rather than restating it.

## 2. Scope (IN)

- **S1** — `tools/run-gates/README.md` gains a section on `doc_reads` and `GATE_DOCS_BASE`: what a
  declaration means, that an absent one runs, and that a docs run never stamps a full green. Observed by AC1.
- **S2** — The key list in `.githooks/gate-env.sh` documents `GATE_DOC_PATHS`: its grammar, that it is
  read at R, and that empty means no doc class. Observed by AC2.
- **S3** — `WIRE-INTO-PROJECT.md` tells an adopter the mechanism is opt-in, and how to declare a doc
  class and their own legs' `doc_reads`. Observed by AC1 and AC3.
- **S4** — `AGENTS.md`'s merge-bar section says the push boundary scopes a doc-only push, and that a
  green earned in any worktree serves every push. Observed by AC1 and AC3.
- **S5** — Every kit whose shipped bytes this build moved advances its version once, in this unit,
  because it is the last to touch them: run-gates to 1.26, lexicon 1.18, memory-tree 2.125,
  process-monitor 0.14, review-harness 1.32 and unattended 1.68, each marker carrier with it.
  Observed by AC4.

## 3. Non-goals (OUT)

- The template, `coding-governance-agents.template.md`: it names no hook decision, and stays byte-for-byte.
- Any mechanism: units 1 to 5.

### Edges

- **consumes-from** `TOOL-dThriftyLanding-5` — the declarations the carriers point at.

## 4. Design

### Evidence

Read at base `c3ef6742`. The run-gates README has a section on reuse and the guard baseline; the
gate-env notes list `INHERITED_RED` and `GATE_SELFTESTS` with one line each; `AGENTS.md`'s merge-bar
section describes the hook's FULL-or-scoped decision in prose; the runbook's push-main paragraph
describes the lander and the hook.

### Files touched (estimate)

- `tools/run-gates/README.md`
- `.githooks/gate-env.sh`
- `WIRE-INTO-PROJECT.md`
- `AGENTS.md`

### Alternatives rejected

- **A new guide.** Four short additions beside the text that already describes each piece keep one
  fact in one place; a guide would restate all four.

## 5. Production-readiness checklist

- perf / scale — none.
- security — the gate-env note says the class is read at R, which is the property a reader must keep.
- error / empty / loading states — none.
- observability — none.
- testing — the doc legs: size, line length, runbook parity.
- migration — none.
- user docs — this unit.
- risks — none.

## 6. Acceptance criteria

- **AC1** — When `grep -n 'doc_reads' tools/run-gates/README.md WIRE-INTO-PROJECT.md AGENTS.md` runs,
  each file prints at least one line.
  Red when: a carrier omits the mechanism.
- **AC2** — When `grep -n 'GATE_DOC_PATHS' .githooks/gate-env.sh` runs, it prints the documenting line
  and the declaration.
  Red when: the key is declared without its grammar.
- **AC3** — When the `charter size`, `line length` and `govkit runbook parity` legs run, they are green.
  Red when: an addition breaks a size or parity bound.
- **AC4** — When `bash tools/check-kit-versions.sh` and `python tools/govkit/govkit.py epoch` run after
  this unit's commit, the first prints `clean` and the second reports no `FAILED` kit.
  Red when: a kit's shipped bytes moved and its version did not.

## 7. Gates

`charter size` · `line length` · `govkit runbook parity` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-05 · initial draft.
- rev-2 · 2026-10-05 · S5 and AC4: the version bumps the kit epoch owes ride the last unit to touch the
  kits; the charter's addition is paid for by a trimmed clause, the cap having 73 bytes left.

## 10. Reuse audit

No new seam: each addition sits beside the paragraph that already describes the piece it extends.
The recall query for the build returned no ruling about where push-boundary behaviour is documented
beyond these four carriers.

Recall terms used: pre-push GATE_FULL scoped gate full green stamp guard lag bound records-only landing push-main.sh leg manifest merge second parent
