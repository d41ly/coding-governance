# DEPL-aDistilledCharter-2 — the review protocol ships with every default adoption

**Status:** WONTDO · rev-2 · 2026-10-09 · node a · Tier-2 · base 6473ae38 · streams deployer · order 10 · superseded by PLAY-aDistilledCharter-5, closing review round 2 B1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-09-review-TOOL-aDistilledCharter-7-closing-diff-round2.md](../reviews/2026-10-09-review-TOOL-aDistilledCharter-7-closing-diff-round2.md) | diff-review | TOOL-aDistilledCharter-2 TOOL-aDistilledCharter-5 TOOL-aDistilledCharter-6 TOOL-aDistilledCharter-7 |

<!-- /gen:spec-records -->

## 1. Goal

v4.0 moved the security boundaries and the tier definitions into the review protocol, which ships
with the `review-harness` kit, and govkit's default selection does not include that kit, so a
default adoption loses both. This unit adds `review-harness` to the default selection, because the
charter's `[security]` and `[risk]` practices assume the protocol and its harness.

## 2. Scope (IN)

- **S1** — `tools/govkit/registry.toml` `[selection] default` gains `review-harness`. Observed by
  AC1.
- **S2** — `WIRE-INTO-PROJECT.md` §2 says the review protocol carries the security checklist and
  ships by default, and that a selection without the kit goes without it. Observed by AC2.

## 3. Non-goals (OUT)

- Existing adopters' selections. They chose their kits; the runbook line tells them what dropping
  `review-harness` costs.
- Moving the checklist again.

### Edges

- **consumes-from** `PLAY-aDistilledCharter-2` — the protocol sections that now ship by default.

## 4. Design

One entry id in the declared default list. govkit's selfcheck 7b already asserts every default
member is a real entry, so a misspelling reds there.

### Files touched (estimate)

`tools/govkit/registry.toml` · `WIRE-INTO-PROJECT.md`

### Alternatives rejected

- **Moving both sections into a memory-tree guide.** A third move of the same text in one build, and
  the review protocol is where a reviewer looks.

## 5. Production-readiness checklist

- security — restores the security checklist to every default adoption.
- perf / scale — one more kit installed by default.
- error / empty / loading states — N/A — a declaration.
- observability — `govkit intake` lists the default kits it selected.
- risks — a default adoption now installs the review harness scripts too.
- testing — `govkit selfcheck`.
- migration — none for existing adopters.
- user docs — the runbook line.

## 6. Acceptance criteria

- **AC1** — When `python tools/govkit/govkit.py selfcheck` runs, it is clean, and
  `tools/govkit/registry.toml`'s default list names `review-harness`. Red when: the id is missing or
  selfcheck refuses it.
- **AC2** — When `grep -n 'review-harness' WIRE-INTO-PROJECT.md` runs, the §2 line about the
  security checklist prints. Red when: the runbook is silent about it.

## 7. Gates

`govkit selfcheck` · `govkit runbook parity` · `govkit acceptance matrix` · `recall floor arms` · `govkit selftest` · `govkit refusal join`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft, promoted from the closing review round 1, C1 (HIGH).
- rev-2 · 2026-10-09 · §2 · retired: `review-harness` requires `agent-cap` and `settings-merge`, so
  the default selection refused every adoption (round 2, B1). The change is reverted.

## 10. Reuse audit

`reuse_lookup.py "render the node registry table into a charter"` is the set's probe and names no
seam here; the seam extended is the `[selection] default` declaration of `tools/govkit/registry.toml`.

Recall terms used: `charter template playbook render AGENTS.md section parity size ceiling one-liner rule node registry tag`
