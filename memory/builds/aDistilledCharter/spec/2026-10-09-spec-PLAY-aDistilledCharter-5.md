# PLAY-aDistilledCharter-5 — the security checklist and the tier definitions ship with the memory tree

**Status:** SPECCED · rev-1 · 2026-10-09 · node a · Tier-2 · base 6473ae38 · streams playbook+tooling · order 12

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-09-build-TOOL-aDistilledCharter-1-acceptance-ledger.md](../build/2026-10-09-build-TOOL-aDistilledCharter-1-acceptance-ledger.md) | journal | TOOL-aDistilledCharter-1 TOOL-aDistilledCharter-2 TOOL-aDistilledCharter-3 TOOL-aDistilledCharter-4 PLAY-aDistilledCharter-1 PLAY-aDistilledCharter-2 PLAY-aDistilledCharter-3 PLAY-aDistilledCharter-4 DEPL-aDistilledCharter-1 KICK-aDistilledCharter-1 TOOL-aDistilledCharter-5 TOOL-aDistilledCharter-6 TOOL-aDistilledCharter-7 TOOL-aDistilledCharter-8 |

<!-- /gen:spec-records -->

## 1. Goal

`PLAY-aDistilledCharter-2` put the security boundaries and the tier definitions in the review
protocol, which only the `review-harness` kit ships, and making that kit a default needs two more
kits in every default adoption (closing review round 2, B1). This unit moves both sections into the
spec template the memory-tree kit renders, which every adoption has because the memory tree is
required, and where a design pass for a new write path already looks.

## 2. Scope (IN)

- **S1** — `tools/memory-tree/SPEC-TEMPLATE.template.md` gains `## Tiers — which review a change
  owes` and `## Security boundaries — the checklist for a new write path or surface`, ahead of the
  skeleton, carrying the text the review protocol held. `memory/TEMPLATE-SPEC.md` follows through
  the kit's dogfood render. Observed by AC1.
- **S2** — `tools/workflows/REVIEW-PROTOCOL.template.md` keeps one line where the sections were,
  pointing at the spec template, and `memory/guides/REVIEW-PROTOCOL.md` follows. Observed by AC2.
- **S3** — `tools/govkit/registry.toml` `[selection] default` returns to its BASE members, and the
  runbook's §2 line says where the checklist lives. Observed by AC3.
- **S4** — The charter's memory-tree protocol line names the spec template for a new write path or
  surface; the review-harness line names the review protocol for reviews and fan-outs. The ledger of
  `PLAY-aDistilledCharter-1` follows. Observed by AC4.

## 3. Non-goals (OUT)

- The default selection beyond restoring BASE's. Adding the review harness, the cap hook and the
  settings merger to every default adoption is the owner's call, and is filed rather than made.
- Rewording any boundary.

### Edges

- **consumes-from** `PLAY-aDistilledCharter-2` — the two sections it wrote.
- **hands-off** `TOOL-aDistilledCharter-8` — the round's other findings.

## 4. Design

### Files touched (estimate)

`tools/memory-tree/SPEC-TEMPLATE.template.md` · `memory/TEMPLATE-SPEC.md` · `tools/workflows/REVIEW-PROTOCOL.template.md` · `memory/guides/REVIEW-PROTOCOL.md` · `tools/govkit/registry.toml` · `WIRE-INTO-PROJECT.md` · `coding-governance-agents.template.md` · `AGENTS.md`

### Alternatives rejected

- **Three kits added to the default selection.** It changes what every default adoption installs,
  a hook into its settings among them; the owner decides that.

## 5. Production-readiness checklist

- security — the checklist reaches every adoption again.
- perf / scale — N/A — documents.
- error / empty / loading states — N/A — documents.
- observability — N/A — documents.
- risks — the review protocol's readers follow one pointer to the spec template.
- testing — the memory-tree and review-harness parity renders; the charter render.
- migration — none.
- user docs — these are the user docs.

## 6. Acceptance criteria

- **AC1** — When `grep -n '^## Tiers\|^## Security boundaries' memory/TEMPLATE-SPEC.md` runs, both
  headings print, and the dogfood render leaves `git diff --exit-code memory/TEMPLATE-SPEC.md`
  clean. Red when: a heading is missing or the pair drifts.
- **AC2** — When `grep -c '^## Security boundaries' memory/guides/REVIEW-PROTOCOL.md` runs it
  counts 0 and the protocol names the spec template. Red when: the section stands in both.
- **AC3** — When `git diff 6473ae38 -- tools/govkit/registry.toml` runs it prints nothing.
  Red when: the default selection still differs from BASE.
- **AC4** — When `render_playbook.py --target . --check` runs it is green, and the ledger resolver
  over `PLAY-aDistilledCharter-1`'s rows finds 0 unresolved. Red when: a moved row points at the old
  home.

## 7. Gates

`kit/dogfood doc parity` · `review-protocol parity (kit vs dogfood)` · `playbook render wiring` · `govkit selfcheck` · `govkit selftest` · `memory hygiene` · `verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `recall floor` · `recall floor arms` · `govkit refusal join` · `govkit acceptance matrix`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft, the fix for the closing review round 2, B1.

## 10. Reuse audit

`reuse_lookup.py "render the node registry table into a charter"` is the set's probe and names no
seam here; the seams extended are the memory-tree kit's spec template and its dogfood render.

Recall terms used: `charter template playbook render AGENTS.md section parity size ceiling one-liner rule node registry tag`
