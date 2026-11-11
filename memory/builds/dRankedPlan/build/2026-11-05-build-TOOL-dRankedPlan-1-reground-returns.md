**Serves:** research TOOL-dRankedPlan-1 TOOL-dRankedPlan-3

# dRankedPlan — the re-ground writers' returns, verbatim

The `gov-spec-writer` return for the re-ground brief [`2026-11-05-prompt-TOOL-dRankedPlan-1-parents-reground`](../prompts/2026-11-05-prompt-TOOL-dRankedPlan-1-parents-reground.md), extracted by script from each agent's transcript and not retyped. The cross-check record it folds is [`2026-11-05-build-TOOL-dRankedPlan-1-parents-crosscheck`](2026-11-05-build-TOOL-dRankedPlan-1-parents-crosscheck.md); each group's handoff sits beside the brief.

## Group A, led by spec 3

I revised TOOL-dRankedPlan-3 to rev-4. The one item, row 6, is folded as the brief decided. No row was refused.

**Row 6 still held at the branch tip.** I re-read both sides before editing:
- **Our spec:** TOOL-dRankedPlan-3 S5 still said `triage.py` writes "one record per pass per home build that the pass decided an ask in". The owner's 2026-11-05 fork picks did not touch this spec.
- **The parent:** TOOL-dTotalRecall-2 has not changed since `ab976b5b3`. Its §4 "Minting" still checks "the build's lease or claim" before a `<n>` mint, and "a lease or claim held by another refuses, naming the holder".

**What changed in the spec:**
- **Status line:** now `rev-4 · 2026-11-05`, with every other field kept.
- **S5:**
  - Each home's record now goes through the door before that home's rows are appended, so a refused home gets neither.
  - When the door refuses because another session leases or claims the home, it exits 2 with `refused triage: <why>` (TOOL-dTotalRecall-2 §4 "The command"). The pass then prints `triage — <home> held by <holder>`, taking the holder from the door's own refusal line.
  - It then appends nothing to that home, leaves its asks undecided for the next pass, moves on to the next home and exits 0. It reads no lease of its own.
  - Any other door refusal stops the pass with exit 2, naming the door's line.
  - "Observed by" now includes AC13.
- **S6:** its "the build whose folder holds the record" is unchanged.
- **§3, dTotalRecall edge:** now also cites the door's refusal of a mint into a held build (TOOL-dTotalRecall-2 S6, §4 "Minting").
- **§4 Inventory:** adds the plant `held-home`.
- **§5:** the error-states line notes the skipped home, and the observability line adds the `held by` line. Testing now counts nine plants.
- **§6, new AC13:**
  - **Setup:** `python triage.py --fixture --plant held-home` runs over two homes, `hA` and `hB`, with a lease on `hA` held by another session, planted as TOOL-dTotalRecall-2 AC5 plants it.
  - **Expected:** exit 0, `triage — hA held by <holder>`, and `git status --porcelain` over `hA`'s folder prints nothing. `hB` gets its row and its record, and after the lease is released a second pass labels `hA`'s ask.
  - **Red when:** a row or record lands in a home another session holds, or the pass exits non-zero.
- **§7:** the existing `triage.py` `New arm:` line now covers AC13, nine plants, and the failing case "a row written into a home another session holds". There is no new arm line.
- **§9:** one rev-4 line in the form the brief gives, naming row 6 and ending with the reground brief.

**Checks:**
- **Size:** `wc -c` is 41546, under 49152.
- **Memory hygiene:** I ran `check-memory-hygiene.sh --staged` over a copy of the index with only this spec staged, then deleted the copy. Its only failure was check 9, which wants a fresh build-index render. That is the main loop's job with `gen_build_index.py --write`. Check 9 names the spec only as the input that makes a render owed; the files it lists as stale are `memory/LIVE.md` and the README and spec files of dDeclaredLoop, dIndexedDesign, dRankedPlan and dTotalRecall.

**Things I left alone that you may want to act on:**
- **The refusal text is not fixed.** TOOL-dTotalRecall-2 says only that the refusal names the holder; it gives no fixed wording for that `<why>`. So S5 tells the held-home refusal from the door's other refusals by the authority cause of `check_mint_authority` (TOOL-dTotalRecall-2 §4 "Inventory"), taken from `build_records.py` in the same kit and never retyped. Whether the built door exposes that cause in a form the pass can import is unknown until TOOL-dTotalRecall-2 is built. If it doesn't, that is a gap in the parent spec, not something to fix here.
- **S6 has the same exposure.** S6's `ratify` writes rows and a second record of the same home through the same door. A home that another session takes between `pass` and `ratify` would be refused the same way. I left S6 unedited, as the brief requires; it is outside row 6.

The spec is `C:\projects\coding-governance\.claude\worktrees\vigilant-einstein-2d0f7d\memory\builds\dRankedPlan\spec\2026-10-26-spec-TOOL-dRankedPlan-3.md`.
