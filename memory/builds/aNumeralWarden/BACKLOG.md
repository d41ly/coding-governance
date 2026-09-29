# aNumeralWarden — asks

## Asks

- TOOL-aNumeralWarden-1 · filed 2026-08-10 · agent-cap.js never reads the fan-out bound it enforces, so `a.maxVerifiers || 5` lets a caller raise the verifier count past the BINDING cap with every gate green; at rev-3 it also owns the Agent-matcher refusal folded in from TOOL-aUnmannedHelm-1
- TOOL-aNumeralWarden-2 · filed 2026-08-10 · agent-cap's enclosing-opener walk is defeated by two nested wrappers or 59 lines of distance between the `.map` and the `agent(` call; it needs a statement-level walk, not an opener count, and the 58/59 boundary is unfixtured
- TOOL-aNumeralWarden-3 · filed 2026-08-10 · a drift-audit pin RAISE is indistinguishable from a population drain to every gate leg; `--check` compares only `value > pin`, so `ORPHAN_ID_PIN` 4 -> 5 and `handkept` 1 -> 7 both landed unchallenged
- TOOL-aNumeralWarden-4 · filed 2026-08-10 · `map_lib.scan_js_definitions` joins the export scan in the `kit-js` layer, so the 30 definitions under `tools/` are indexed alongside the 3 `meta` exports and `boundedK` is findable — closed by TOOL-dClosedLexicon-12

## Dispositions

- CLOSED · TOOL-aNumeralWarden-1 · by TOOL-aUnmannedHelm-1 · agent-cap.js never reads the fan-out bound it enforces, so `a.maxVerifiers || 5` lets a caller raise the verifier count past the BINDING cap with every gate green; at rev-3 it also owns the Agent-matcher refusal folded in from TOOL-aUnmannedHelm-1
- CLOSED · TOOL-aNumeralWarden-4 · by TOOL-dClosedLexicon-12 · `map_lib.scan_js_definitions` joins the export scan in the `kit-js` layer, so the 30 definitions under `tools/` are indexed alongside the 3 `meta` exports and `boundedK` is findable — closed by TOOL-dClosedLexicon-12
