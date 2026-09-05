# TOOL-aWeldedTribunal-1 — acceptance ledger

**Serves:** journal TOOL-aWeldedTribunal-1

## What changed

`tools/hooks/agent-cap.js` gained one keyword source and lost six regex literals. `LOOP_KEYWORDS`
is the string `for(?:\s+await)?|while`; `LOOP_HEADER`, `LOOP_HEADER_G` and `LOOP_KEYWORD_TAIL` are
built from it. The six sites now read:

| Site | Takes |
|---|---|
| `checkSeqMarker` C5 | `LOOP_HEADER` |
| `checkSeqMarker` C6 (counts openers) | `LOOP_HEADER_G` |
| `checkSeqMarker` nesting walk | `LOOP_HEADER` |
| opener walk | `LOOP_KEYWORD_TAIL` |
| call-site braceless arm | `LOOP_HEADER` |
| call-site brace walk | `LOOP_HEADER` |

`tools/hooks/agent-cap.test.sh` gained six arms, four denying and two admitting.

## Each criterion, answered

- **AC1** — a `for await (…)` thunk-array fan piped to `node tools/hooks/agent-cap.js` exits **2**.
  It exited **0** against the shipped hook before this unit, measured and recorded in
  `2026-09-04-build-TOOL-aWeldedTribunal-2-1-predicate-measurement.md`.
- **AC2** — the same fan inside `do { … } while (…)` exits **2**. It exited **0** before.
- **AC3** — `bash tools/hooks/agent-cap.test.sh` ran GREEN before the arms were added:
  **169 passed, 0 failed, exit 0**. Every pre-existing arm survives the change.
- **AC4** — every tracked harness still exits 0: `check-workflow-syntax.js`, `drift-audit-code.js`,
  `drift-audit-state.js`, `tier2-review.js`, `unattended-build.js`. This matches the baseline
  recorded before the change, so it is a comparison rather than a recollection.
- **AC5** — a `for await` fan reached through the OPENER walk (`for await (const f of allFindings) await agent(f.claim)`)
  exits **2**. This is the `:910` path, and it needed the end-of-text form: a pattern ending in `\(`
  can never match text tested BEFORE an opener.
- **AC6** — `grep -n 'for|while' tools/hooks/agent-cap.js` returns the constant definition and its
  explaining comment. All six inline literals are gone.

## The suite, after the arms

**175 passed, 0 failed, exit 0** — 169 pre-existing plus this unit's 6.

## The staged failing case, observed

The charter says a gate is not landed until its failing case has been observed. Here the direction is
inverted and stronger than a staged break: the two evasion shapes were run against the SHIPPED hook
and exited 0 before a line was written, then against the built hook and exited 2. The failing case
was the tree's actual behaviour, not a synthetic break — which is the one shape
`staged-break-substitutes-a-synthetic-value` cannot apply to.

## What this unit does NOT close, stated

A BRACELESS `do` — `do out.push(await agent(f)); while (…)` — has no brace for the `do\s*\{` arm and
no keyword before the opener for the tail arm. Named as a residual in §3 of the spec and unchanged
here. The `do` spelling is deliberately absent from `LOOP_KEYWORD_TAIL`, because a `do` block opens
with a brace and never appears as an enclosing paren opener; putting it there would match nothing and
imply coverage that does not exist.

## Evidence

**Evidences:** TOOL-aWeldedTribunal-1
- AC1 — `node tools/hooks/agent-cap.js` — a `for await` thunk-array fan exits 2; it exited 0 against the shipped hook before this unit
- AC2 — `node tools/hooks/agent-cap.js` — the same fan inside a `do`/`while` block exits 2; it exited 0 before
- AC3 — `bash tools/hooks/agent-cap.test.sh` — 169 passed, 0 failed BEFORE this unit's arms were added, so no pre-existing arm changed verdict
- AC4 — `node tools/hooks/agent-cap.js` — all five tracked harnesses still exit 0, compared against the baseline in the pre-wiring measurement record
- AC5 — `node tools/hooks/agent-cap.js` — a `for await` fan reached through the OPENER walk exits 2, which needed the end-of-text sibling form
- AC6 — `tools/hooks/agent-cap.js` — one keyword source plus two derived siblings; the six inline literals are gone
