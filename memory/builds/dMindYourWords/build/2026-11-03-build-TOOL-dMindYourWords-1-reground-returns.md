**Serves:** research TOOL-dMindYourWords-1 TOOL-dMindYourWords-11

# dMindYourWords — the re-ground writer's return, verbatim

The `gov-spec-writer` return for the re-ground brief [`2026-11-03-prompt-TOOL-dMindYourWords-1-parents-reground`](../prompts/2026-11-03-prompt-TOOL-dMindYourWords-1-parents-reground.md), extracted by script from the agent's transcript and not retyped. The cross-check record it folds is [`2026-11-03-build-TOOL-dMindYourWords-1-parents-crosscheck`](2026-11-03-build-TOOL-dMindYourWords-1-parents-crosscheck.md).

## Spec 11

I've revised the TOOL-dMindYourWords-11 spec (row 2 folded), and the memory hygiene gate names nothing of my spec except one index-render finding, which belongs to the main loop.

**Spec:** `C:\projects\coding-governance\.claude\worktrees\modest-gates-539d2a\memory\builds\dMindYourWords\spec\2026-10-29-spec-TOOL-dMindYourWords-11.md`

**Row 2 (MISMATCH): folded.** I checked the parent against `66c5b8dbf`, and TOOL-dTotalRecall-2 says what the brief says:
- **tr2:80-84:** S9 gives `writer = "gov_record.py new <kind>"` only to `hand` rows whose form is `fields`. "a `hand` row of another form keeps `hand`".
- **tr2:57-58:** a row not of form `fields` is written only by a kind verb of S7.
- **tr2:175-176:** the unit adds only the `build-readme` and `spec` handlers.

In S10 I removed "until TOOL-dTotalRecall-2 registers a door". It now says the row keeps `writer = hand` because it is a `rows` kind tr2 S9 leaves at `hand` (tr2:80-84), with no door planned. Nothing else in the spec changed. I invented no door and no ask, and no fork was opened or resolved.

**Row 3 (UNKNOWN UNTIL BUILT): not edited**, as the brief directs.

**Status and log:** the **Status:** line now reads `rev-3 · 2026-11-03`, with every other field unchanged. §9 gains this line:
`- rev-3 · 2026-11-03 · §2 S10 · the `lexicon-declaration` row's writer stays `hand` as a `rows` kind TOOL-dTotalRecall-2 S9 leaves at `hand` (tr2:80-84) with no door planned, no longer awaiting a tr2 door; no scope, design or criterion moved, by the brief prompts/2026-11-03-prompt-TOOL-dMindYourWords-1-parents-reground.md`

The log line avoids quoting the removed phrase so that the acceptance grep stays empty.

**Acceptance:**
- `wc -c` gives 35750, under 49152.
- `grep -n "until TOOL-dTotalRecall-2 registers"` prints nothing.
- The memory hygiene gate (`--staged`) ran over a copy of the index with only this spec staged, and I deleted the copy afterwards. Check 9 fails only because the build index is stale, which only a `gen_build_index.py --write` render fixes. It names `memory/LIVE.md` and the dMindYourWords, dScopedBuild and dShippedRelease build READMEs; that render is the main loop's. No other check names this spec.

**A parent line to note (not edited):** cross-check row 1 (line 15 of the returns record) quotes tr1:194, "`hand` is legal until TOOL-dTotalRecall-2 registers a door". That is TOOL-dTotalRecall-1's wording, not ours. Read alongside tr2 S9, it suggests every `hand` row is temporary, which tr2 contradicts for `rows`-form kinds. I didn't verify tr1:194 myself and touched no dTotalRecall file; whoever owns dTotalRecall may want to reconcile it.

I made no commit and staged nothing into the real index.
