# PLAY-aDistilledCharter-2 — the review protocol carries the security checklist and the tier definitions the charter drops

**Status:** SPECCED · rev-1 · 2026-10-09 · node a · Tier-2 · base 6473ae38 · streams playbook+tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-09-build-TOOL-aDistilledCharter-1-acceptance-ledger.md](../build/2026-10-09-build-TOOL-aDistilledCharter-1-acceptance-ledger.md) | journal | TOOL-aDistilledCharter-1 TOOL-aDistilledCharter-2 TOOL-aDistilledCharter-3 TOOL-aDistilledCharter-4 PLAY-aDistilledCharter-1 PLAY-aDistilledCharter-3 PLAY-aDistilledCharter-4 DEPL-aDistilledCharter-1 KICK-aDistilledCharter-1 TOOL-aDistilledCharter-5 TOOL-aDistilledCharter-6 TOOL-aDistilledCharter-7 DEPL-aDistilledCharter-2 |
| [2026-10-09-review-PLAY-aDistilledCharter-1-closing-diff-round1.md](../reviews/2026-10-09-review-PLAY-aDistilledCharter-1-closing-diff-round1.md) | diff-review | TOOL-aDistilledCharter-1 TOOL-aDistilledCharter-2 TOOL-aDistilledCharter-3 TOOL-aDistilledCharter-4 PLAY-aDistilledCharter-1 PLAY-aDistilledCharter-3 PLAY-aDistilledCharter-4 DEPL-aDistilledCharter-1 KICK-aDistilledCharter-1 |

<!-- /gen:spec-records -->

## 1. Goal

v4.0 keeps one `[security]` practice and one `[risk]` practice in the charter. The specific
security boundaries a new write path must meet, and the line between a Tier-1 and a Tier-2 change,
are read when a change is scoped or reviewed, not at every session start. This unit moves them into
the review protocol the review-harness kit already ships, so every adopter still receives them.

## 2. Scope (IN)

- **S1** — `tools/workflows/REVIEW-PROTOCOL.template.md` gains `## Tiers — which review a change
  owes`, ahead of `## The Tier-2 pattern`: what makes a change Tier 1 and what makes it Tier 2,
  and that a Tier-2 review reads the cumulative diff once, at the integration boundary. Carried from
  v3.5 §8 lines 230-232. Observed by AC1.
- **S2** — It gains `## Security boundaries — the checklist for a new write path or surface`,
  after the tier section: one line per boundary carried from v3.5 §9 lines 264-276 and §6 line 167,
  the URL normalizer and the SSRF guard included unconditionally. Observed by AC1.
- **S3** — `memory/guides/REVIEW-PROTOCOL.md` is re-rendered from the template by the kit's own
  render, so the pair stays in parity. Observed by AC2.

## 3. Non-goals (OUT)

- Removing the rules from the charter. PLAY-aDistilledCharter-1 does it, after this lands.
- Rewording a rule's substance. The lines are compressed, never weakened.
- Making the checklist a gate. A security boundary is a review judgment in this corpus.

### Edges

- **hands-off** `PLAY-aDistilledCharter-1` — the charter's `[security]` and `[risk]` lines point
  here.

## 4. Design

### Evidence

Read at `6473ae38` on 2026-10-09.

- `tools/workflows/kit.toml` ships `REVIEW-PROTOCOL.template.md` to
  `{memory_root}/guides/REVIEW-PROTOCOL.md`; `check-protocol-parity.test.sh` asserts the render
  equals the template rendered for this install, and its `--render` mode rewrites it.
- The protocol's headings at BASE: the hard cap, enforcement, concurrency, the Tier-2 pattern, and
  schema discipline. Neither the tier definitions nor any security boundary appears in it.

### Files touched (estimate)

`tools/workflows/REVIEW-PROTOCOL.template.md` · `memory/guides/REVIEW-PROTOCOL.md`

### Alternatives rejected

- **A new shipped security guide.** One more file to load and to keep in parity, for content read at
  the same moment as the review protocol.
- **The build method.** It is capped at 30720 bytes for re-reading at every pass boundary, and a
  security checklist is not part of the pass loop.

## 5. Production-readiness checklist

- security — the content moves intact; the charter keeps the practice and points here.
- perf / scale — N/A — a document.
- error / empty / loading states — N/A — a document.
- observability — N/A — a document.
- risks — an adopter that did not select `review-harness` loses the checklist; the charter's
  `[security]` line still binds it.
- testing — `review-protocol parity (kit vs dogfood)`.
- migration — none.
- user docs — this is the user doc.

## 6. Acceptance criteria

- **AC1** — When `grep -n '^## Tiers\|^## Security boundaries' memory/guides/REVIEW-PROTOCOL.md`
  runs, both headings print, and each §9 line of v3.5 maps to one bullet under the second.
  Red when: a heading is absent or a boundary is missing.
- **AC2** — When the kit's parity render is re-run over the committed tree,
  `git diff --exit-code memory/guides/REVIEW-PROTOCOL.md` exits 0.
  Red when: the render drifts from the template.

## 7. Gates

`review-protocol parity (kit vs dogfood)` · `dead-path carriers (deleted files still named)` · `memory hygiene` · `verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `recall floor` · `recall floor arms`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft.

## 10. Reuse audit

`reuse_lookup.py "render the node registry table into a charter"` is the set's probe and names no
seam here; the extended seam is the review-harness kit's existing template and its parity render,
`tools/workflows/check-protocol-parity.test.sh --render`.

Recall terms used: `charter template playbook render AGENTS.md section parity size ceiling one-liner rule node registry tag`
