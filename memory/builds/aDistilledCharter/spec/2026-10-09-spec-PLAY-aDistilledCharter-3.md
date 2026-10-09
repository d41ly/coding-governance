# PLAY-aDistilledCharter-3 — the hygiene guide carries the id-minting protocol the charter drops

**Status:** SPECCED · rev-1 · 2026-10-09 · node a · Tier-2 · base 6473ae38 · streams playbook+tooling · order 3

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

v4.0 keeps one `[ids]` practice. The minting protocol behind it — the slug, the per-family
sequence, the collision grep, the tie-break and the frozen legacy eras — is read when an id is
minted, and the memory-tree kit already grades ids. This unit moves the protocol into that kit's
hygiene guide, so every adopter still receives it.

## 2. Scope (IN)

- **S1** — `tools/memory-tree/HYGIENE.template.md` gains `## Ids — how a session mints them`,
  before `## The check catalog`: one line per rule carried from v3.5 §2 lines 94-103. Observed by
  AC1.
- **S2** — `memory/HYGIENE.md` is re-rendered from the template through the kit's dogfood render,
  so the pair stays in parity. Observed by AC2.

## 3. Non-goals (OUT)

- Removing the rules from the charter. PLAY-aDistilledCharter-1 does it, after this lands.
- Gating the collision grep. Check 13 already catches a collision after the fact.
- The node tag the slug starts with. TOOL-aDistilledCharter-2 owns where a tag comes from.

### Edges

- **hands-off** `PLAY-aDistilledCharter-1` — the charter's `[ids]` line points here.

## 4. Design

### Evidence

Read at `6473ae38` on 2026-10-09.

- `memory/HYGIENE.md` names ids in checks 5, 13 and 14 and the build-folder grammar, and states no
  minting procedure; `skills/session-kickoff/MANIFEST-TEMPLATE.md` defers to "governance §1–§2"
  for it.
- `tools/memory-tree/kit-dogfood-parity.test.sh` pairs the template with `memory/HYGIENE.md`.

### Files touched (estimate)

`tools/memory-tree/HYGIENE.template.md` · `memory/HYGIENE.md`

### Alternatives rejected

- **The kickoff manifest template.** It is copied once per adopter and then owned there, so a later
  correction would never reach an installed manifest.
- **Keeping the protocol in the charter.** Ten lines every session reads for an act one session per
  day performs.

## 5. Production-readiness checklist

- security — N/A — a document.
- perf / scale — N/A — a document.
- error / empty / loading states — N/A — a document.
- observability — N/A — a document.
- risks — an adopter without `memory-tree` loses the detail; the charter's `[ids]` line keeps the
  shape and the no-counter rule.
- testing — the memory-tree dogfood parity leg.
- migration — none.
- user docs — this is the user doc.

## 6. Acceptance criteria

- **AC1** — When `grep -n '^## Ids' memory/HYGIENE.md` runs, the heading prints, and each of v3.5
  §2 lines 94-103 maps to one bullet under it. Red when: the heading or a rule is absent.
- **AC2** — When the kit's dogfood render is re-run over the committed tree,
  `git diff --exit-code memory/HYGIENE.md` exits 0.
  Red when: the render drifts from the template.

## 7. Gates

`memory hygiene` · `dead-path carriers (deleted files still named)` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft.

## 10. Reuse audit

`reuse_lookup.py "render the node registry table into a charter"` is the set's probe and names no
seam here; the extended seam is the memory-tree kit's template and its dogfood parity pair,
`tools/memory-tree/kit-dogfood-parity.test.sh`.

Recall terms used: `charter template playbook render AGENTS.md section parity size ceiling one-liner rule node registry tag`
