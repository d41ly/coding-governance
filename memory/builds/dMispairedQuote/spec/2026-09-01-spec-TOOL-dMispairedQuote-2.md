# TOOL-dMispairedQuote-2 — the file's stated ceiling and the dossier's residual describe what the view now does

**Status:** OPEN · rev-1 · 2026-09-01 · node d · Tier-1 · base d65da7ab · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-01-prompt-TOOL-dMispairedQuote-1.md](../prompts/2026-09-01-prompt-TOOL-dMispairedQuote-1.md) | research | TOOL-dMispairedQuote-1 |

<!-- /gen:spec-records -->

## 1. Goal

Three carriers state a precondition about `agent-cap.js`'s string handling that
`TOOL-dMispairedQuote-1` makes false. A reader who believes them concludes the class is closed, which
is what the last two review rounds concluded. This unit rewrites them to what is then true.

## 2. Scope (IN)

- **S1** — `tools/hooks/agent-cap.js` header, the `ponytail:` ceiling paragraph. It says line
  comments AND quoted-string literals are stripped before the scan. State the fail-closed halves
  unit 1 adds: a quote that cannot be paired leaves its line unblanked, in all three views.
- **S2** — `tools/hooks/agent-cap.js` around line 277, the `TOOL-aLexedStripper-5` note. Its
  sentence *"This file models no regex literal"* stays TRUE and stops being the explanation: the
  reported defect was not a regex-literal defect, and the note should say so, naming the apostrophe
  as the mechanism and pointing at `opensLiteral`.
- **S3** — the `addc6169` comment inside `renderCodeView`'s quote branch. It says `stripStrings`
  needs a matching PAIR before it blanks anything, *"and so does this now"* — which is what let the
  wrong pair through. Rewrite it to state the pair must be the RIGHT one.
- **S4** — `memory/map/features/agent-cap.md`, the dossier. Refresh the prose covering these views
  and restate the RESIDUAL: what survives is a balanced set of prose quotes straddling a fan-out,
  which needs an even count of loose quotes on both sides of it.
- **S5** — a `memory/gotchas/` class for the finding, per §7's left-shift rule for a class the gate
  covers but the next reader will meet again in another scanner.
- **S6** — `TOOL-aLexedStripper-3` and `-4` backlog rows: annotate each with what unit 1 did and did
  NOT touch, so neither reads as closed.

## 3. Non-goals (OUT)

- Any change to `agent-cap.js` behaviour. This unit is prose and records only.
- Closing `TOOL-aLexedStripper-3` or `-4`. S6 annotates; it does not resolve.
- Restating the marker grammar, which `tools/hooks/README.md` owns.

## 4. Design

Each carrier gets the smallest edit that makes it true. The header ceiling and the dossier residual
are the two a reader reaches first, so both name the surviving hole explicitly rather than implying
it is gone.

### Files touched (estimate)

`tools/hooks/agent-cap.js` · `.claude/hooks/agent-cap.js` (mirror) · `memory/map/features/agent-cap.md` ·
`memory/gotchas/` (one new file) · `memory/backlog/TOOL.md`.

## 5. Production-readiness checklist

N/A — a Tier-1 records unit changing no executable behaviour. The one risk it carries is a prose
claim that outruns unit 1's measurement, which §6 answers by citing the spec rather than the code.

## 6. Acceptance criteria

- **AC1** — When `agent-cap.js`'s header is read, the `ponytail:` paragraph names the fail-closed
  per-line halves and no sentence claims a quoted literal is always stripped.
- **AC2** — When `memory/map/features/agent-cap.md` is read, its residual names the balanced-loose-quote
  shape and cites `TOOL-dMispairedQuote-1`.
- **AC3** — When `bash tools/run-gates/run-gates.sh` runs, the `codebase-map` coverage and freshness
  legs and the `memory-tree hygiene` leg are green over the edited dossier and the new gotcha file.
- **AC4** — When `grep -n 'aLexedStripper-3\|aLexedStripper-4' memory/backlog/TOOL.md` runs, both
  rows carry the annotation and neither is marked CLOSED.

## 7. Gates

`bash tools/run-gates/run-gates.sh` — the memory-tree hygiene leg, the codebase-map legs, and the
`agent-cap self-test` two-copy parity arm for the mirrored header.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-01 · initial draft.
