# TOOL-aDistilledCharter-9 — the closing review's round-3 findings, closed as one batch

**Status:** CLOSED · rev-1 · 2026-10-09 · node a · Tier-2 · base 6473ae38 · streams tooling+playbook · order 14

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-09-build-TOOL-aDistilledCharter-1-acceptance-ledger.md](../build/2026-10-09-build-TOOL-aDistilledCharter-1-acceptance-ledger.md) | journal | TOOL-aDistilledCharter-1 TOOL-aDistilledCharter-2 TOOL-aDistilledCharter-3 TOOL-aDistilledCharter-4 PLAY-aDistilledCharter-1 PLAY-aDistilledCharter-2 PLAY-aDistilledCharter-3 PLAY-aDistilledCharter-4 DEPL-aDistilledCharter-1 KICK-aDistilledCharter-1 TOOL-aDistilledCharter-5 TOOL-aDistilledCharter-6 TOOL-aDistilledCharter-7 PLAY-aDistilledCharter-5 TOOL-aDistilledCharter-8 |

<!-- /gen:spec-records -->

## 1. Goal

Round 3 converged with six MEDIUM and LOW findings
(`reviews/2026-10-09-review-TOOL-aDistilledCharter-8-closing-diff-round3.md`). BUILD-METHOD M4
promotes them as one batch: their write sets meet in `render_playbook.py` and the descriptor.

## 2. Scope (IN)

- **S1** — T1: `PLAY-aDistilledCharter-2`'s AC1 is amended in its rev-2 to name where the sections
  live now, and the ledger answers it in the AMENDED form. NOT OBSERVED by a criterion here: the
  hygiene gate grades the ledger's form.
- **S2** — T2: the runbook and the review protocol say the checklist reaches every adoption that
  keeps the memory tree, which the runbook already requires. The README parks the owner's choice of
  making that a `requires`. Observed by AC1.
- **S3** — T3: the runbook, the descriptor's legacy block and the render's note point the outbound
  rules at the spec template. Observed by AC1.
- **S4** — T4: the moved Tier-2 bullet names the review protocol for the pattern. Observed by AC1.
- **S5** — T5: `checkout_dir` is read from `[answers]` only, and the code comment and
  `TOOL-aDistilledCharter-8`'s S1 say so. Observed by AC2.
- **S6** — T6: the legacy blocks are derived from the descriptor's `[[block]]` rows carrying
  `legacy`, with their `why` as the note, and a template at the engine's major carrying a legacy
  fence is refused. Observed by AC3.

## 3. Non-goals (OUT)

- Adding `requires = ["memory-tree"]` to the `playbook` entry. It changes what an adoption may
  select, which is the owner's call.

### Edges

- **consumes-from** `TOOL-aDistilledCharter-8` — both edit `render_playbook.py`; this lands last.

## 4. Design

### Files touched (estimate)

`tools/playbook/render_playbook.py` · `tools/govkit/entries/playbook.kit.toml` · `tools/memory-tree/SPEC-TEMPLATE.template.md` · `memory/TEMPLATE-SPEC.md` · `tools/workflows/REVIEW-PROTOCOL.template.md` · `memory/guides/REVIEW-PROTOCOL.md` · `WIRE-INTO-PROJECT.md`

## 5. Production-readiness checklist

- security — N/A — no new surface.
- perf / scale — N/A — no measurable change.
- error / empty / loading states — a v4.0 template carrying a legacy fence is refused by name.
- observability — the legacy-block note now quotes the descriptor's own reason.
- risks — none beyond the items.
- testing — the render selftest and the two doc parity renders.
- migration — none.
- user docs — the runbook and the protocol.

## 6. Acceptance criteria

- **AC1** — When `grep -n 'review protocol carries' WIRE-INTO-PROJECT.md tools/playbook/render_playbook.py`
  runs it prints nothing, and `grep -n 'pattern below' memory/TEMPLATE-SPEC.md` prints nothing.
  Red when: a stale pointer survives.
- **AC2** — When `python tools/playbook/render_playbook.py --selftest` runs, the `checkout_dir` arm
  passes with the key under `[answers]`. Red when: the arm needs `[charter]`.
- **AC3** — When the selftest renders a v4.0 fixture carrying a `when:node-table` fence under the
  shipped descriptor, it refuses naming the legacy block; and a `drop_blocks` legacy member with no
  fence is noted with the descriptor's `why`. Red when: the fence renders or the note is a typed copy.

## 7. Gates

`playbook render selftest` · `playbook render wiring` · `kit/dogfood doc parity` · `review-protocol parity (kit vs dogfood)` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `memory hygiene` · `verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `recall floor`

New arm: tools/playbook/render_playbook.py · covers AC2 AC3 · the round-2 fold's renderer · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft, the batch promoted from the closing review round 3.

## 10. Reuse audit

`reuse_lookup.py "render the node registry table into a charter"` is the set's probe; every item
extends `tools/playbook/render_playbook.py`, its descriptor or a doc pair this build already moved.

Recall terms used: `charter template playbook render AGENTS.md section parity size ceiling one-liner rule node registry tag`
