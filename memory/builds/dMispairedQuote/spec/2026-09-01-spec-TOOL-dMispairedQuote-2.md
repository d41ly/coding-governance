# TOOL-dMispairedQuote-2 — the carriers that describe `agent-cap.js`'s string views describe what they now do

**Status:** OPEN · rev-2 · 2026-09-01 · node d · Tier-1 · base d65da7ab · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-01-prompt-TOOL-dMispairedQuote-1.md](../prompts/2026-09-01-prompt-TOOL-dMispairedQuote-1.md) | research | TOOL-dMispairedQuote-1 |
| [2026-09-01-review-TOOL-dMispairedQuote-1-2-spec-audit-round1.md](../reviews/2026-09-01-review-TOOL-dMispairedQuote-1-2-spec-audit-round1.md) | spec-audit | TOOL-dMispairedQuote-1 |
| [2026-09-01-review-TOOL-dMispairedQuote-1-2-spec-audit-round2.md](../reviews/2026-09-01-review-TOOL-dMispairedQuote-1-2-spec-audit-round2.md) | spec-audit | TOOL-dMispairedQuote-1 |

<!-- /gen:spec-records -->

## 1. Goal

Carriers state preconditions about `agent-cap.js`'s string handling that `TOOL-dMispairedQuote-1`
makes false. A reader who believes them concludes the class is closed, which is what the last two
review rounds concluded. This unit rewrites them to what is then true.

**The carrier list is DERIVED from unit 1's files-touched, not authored.** Round 1's finding was that
authoring it from the reported defect's carriers under-reached unit 1's actual edit by three
carriers, one of which review had already caught once and never fixed.

## 2. Scope (IN)

- **S1** — `tools/hooks/agent-cap.js` header, the `ponytail:` ceiling paragraph at `:44-48`. It says
  line comments AND quoted-string literals are stripped before the scan. State what is now true: a
  quote the file cannot resolve as a literal opener is left as text and its line is still blanked, so
  no view ever hands a consumer a raw line.
- **S2** — the `TOOL-aLexedStripper-5` note at `:276-286`. Its sentence *"This file models no regex
  literal"* stays TRUE and stops being the explanation: the reported defect was not a regex-literal
  defect, and the note should say so, naming the apostrophe as the mechanism and pointing at
  `checkLiteralOpen`.
- **S3** — the SECOND `TOOL-aLexedStripper-5` note, inside `fanoutFindings` at `:352-354`. It reads
  that an unterminated scan falls back to the per-line view, which "returns the verdict this hook
  reached before rule 2 moved". Unit 1's S2 re-bases that view, so the sentence is false in the same
  commit that makes it false. Two notes cite one record and rev-1 reached only the first.
- **S4** — the `addc6169` comment inside `renderCodeView`'s quote branch. It says `stripStrings`
  needs a matching PAIR before it blanks anything, *"and so does this now"* — which is what let the
  wrong pair through. Rewrite it to state the pair must be the RIGHT one.
- **S5** — `blankLiterals`' own header at `:596-600`, the function unit 1's S5 edits. It claims
  string AND template contents gone, comments gone, and records the prior author's refusal to
  re-baseline the strip. Unit 1 does both. This carrier was already caught once, as `aLexedStripper`
  spec-audit round 1 finding 11, and still stands unedited at HEAD.
- **S6** — `memory/map/features/agent-cap.md`, the dossier. Three edits, not one: the gap bullet
  *"Block comments naming a primitive still trip rule 1 … Benign and fail-closed"* — which the
  measured `/* don't */` shape refutes, since it failed OPEN; the `-5` gap bullet at `:163-169`,
  whose "residual is precision, not safety" is refuted by the same measurement; and a RESIDUAL naming
  what survives, which is a balanced set of loose prose quotes straddling a fan-out.
- **S7** — a `memory/gotchas/` class for the finding, per §7's left-shift rule for a class the gate
  covers but the next reader will meet again in another scanner. **`gotcha-classes` is a
  machine-enumerated inventory key set**, so the new filename is CLAIMED in the dossier's
  `gotcha-classes` array and `memory/map/generated/` is regenerated in the same commit.
- **S8** — `TOOL-aLexedStripper-3` and `-4` backlog rows: annotate each with what unit 1 did and did
  NOT touch, so neither reads as closed. Add a row for the balanced-loose-quote residual.

## 3. Non-goals (OUT)

- Any change to `agent-cap.js` behaviour. This unit is prose and records only.
- Closing `TOOL-aLexedStripper-3` or `-4`. S8 annotates; it does not resolve.
- Restating the marker grammar, which `tools/hooks/README.md` owns.
- The `memory/DECISIONS.md` supersession row for `TOOL-aLexedStripper-5`'s cannot-regress clause.
  That is unit 1's S8, because the claim it supersedes is a property of unit 1's change.

## 4. Design

Each carrier gets the smallest edit that makes it true. The header ceiling and the dossier residual
are the two a reader reaches first, so both name the surviving hole explicitly rather than implying
it is gone. Every S-item has its own acceptance clause in §6, because an AC pinning one edit of eight
certifies coverage this unit does not have.

### Files touched (estimate)

`tools/hooks/agent-cap.js` · `.claude/hooks/agent-cap.js` (verbatim mirror) ·
`memory/map/features/agent-cap.md` · `memory/map/generated/` (regenerated) · `memory/gotchas/` (one
new file) · `memory/backlog/TOOL.md`.

## 5. Production-readiness checklist

N/A — a Tier-1 records unit changing no executable behaviour. The one risk it carries is a prose
claim that outruns unit 1's measurement, which §6 answers by pinning each claim to the reproduction
that supports it rather than to a summary of it.

## 6. Acceptance criteria

- **AC1** — When `agent-cap.js`'s `ponytail:` paragraph is read, it names the no-raw-line property
  and no sentence claims a quoted literal is always stripped.
- **AC2** — When `grep -n 'aLexedStripper-5' tools/hooks/agent-cap.js` runs, BOTH hits — the note
  near `:276` and the one inside `fanoutFindings` — sit in this commit's touched set.
- **AC3** — When the `addc6169` comment in `renderCodeView` is read, it states that a pair must be
  the right one, and the phrase `and so does this now` is absent.
- **AC4** — When `blankLiterals`' header is read, the re-baselining refusal is recorded as
  discharged and the string-and-template-contents-gone claim is stated conditionally.
- **AC5** — When `memory/map/features/agent-cap.md` is read, the block-comment gap bullet no longer
  calls that shape fail-closed, the `-5` bullet no longer calls its residual precision-only, and a
  residual names the balanced-loose-quote shape citing `TOOL-dMispairedQuote-1`.
- **AC6** — When `python tools/codebase-map/gen_map.py --check` and the `codebase-map coverage +
  freshness` leg run, both are green: the new `memory/gotchas/` file is claimed by the dossier's
  `gotcha-classes` array and `memory/map/generated/` matches a fresh render.
- **AC7** — When `grep -n 'aLexedStripper-3\|aLexedStripper-4' memory/backlog/TOOL.md` runs, both
  rows carry the annotation and neither is marked CLOSED, and a third row records the residual.
- **AC8** — When `bash tools/run-gates/run-gates.sh` runs, the `memory-tree hygiene` leg and the
  `agent-cap self-test` two-copy parity arm are green over the mirrored header.

## 7. Gates

`bash tools/run-gates/run-gates.sh` — the `memory-tree hygiene` leg, the `codebase-map coverage +
freshness` leg, and the `agent-cap self-test` two-copy parity arm for the mirrored header.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-01 · initial draft.
- rev-2 · 2026-09-01 · folded spec-audit round 1, findings 31, 33 and 34. Derived the carrier list
  from unit 1's files-touched instead of authoring it, which added S3 (`fanoutFindings:352`), S5
  (`blankLiterals`' header) and the two extra dossier bullets in S6. Claimed the new
  `gotcha-classes` key and the generated-map regen in S7. Split the acceptance criteria so each
  S-item has one. Dropped §1's authored carrier count.
