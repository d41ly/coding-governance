# TOOL-dThriftyLanding-6 — the carriers state how a doc-only push is scoped

**Status:** OPEN · rev-1 · 2026-10-05 · node d · Tier-1 · base c3ef6742 · streams tooling · order 6

<!-- gen:spec-records -->

*No record names this unit.*

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

## 7. Gates

`charter size` · `line length` · `govkit runbook parity` · `spec tokens (a spec's own names resolve)`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-05 · initial draft.

## 10. Reuse audit

No new seam: each addition sits beside the paragraph that already describes the piece it extends.
The recall query for the build returned no ruling about where push-boundary behaviour is documented
beyond these four carriers.

Recall terms used: pre-push GATE_FULL scoped gate full green stamp guard lag bound records-only landing push-main.sh leg manifest merge second parent
