**Serves:** research TOOL-dSafePassage-28 TOOL-dSafePassage-42

# Brief: TOOL-dSafePassage-42's per-row expectation folds into TOOL-dSafePassage-28, so 28 builds green on the shipped lander

## The prompt

No owner prompt: the build run's builder handed TOOL-dSafePassage-28 back as a DIVERGENCE before code (`wf_3de5e6ef-32e`), and the run revises the specs under M2.

## The brief

### Goal

TOOL-dSafePassage-28's arm asserts, per refusal row, the branch position that row's refusal can actually leave — the old sha for every row but compare-and-swap, the sha the plant moved it to for compare-and-swap — so the unit commits a green arm on the shipped lander, and TOOL-dSafePassage-42 no longer carries what moved.

**The defect.** 28's §2 S3 and §6 AC2 say every planted refusal "exits 1 with the branch unmoved". S2 plants the compare-and-swap refusal by having the planted `regen.py` move the branch with a second commit before the swap; at `tools/push-main.sh:1098` the guarded `git update-ref "refs/heads/$branch" "$t" "$oldb"` refuses only when the branch is no longer at `$oldb`, and the refusal path at `:1099` checks the branch out where the plant left it. So that row can never read "at its old sha". TOOL-dSafePassage-42's S1, S2 and S3 already give the fix — an `expect` column, `old` or `moved`, per row, "so ... the arm reads green on the shipped lander" — but 42 is order 10 and 28 order 5, so 28 cannot consume it.

**The direction.** Fold 42's S1 and S2 (the per-row `expect` value and the compare-and-swap row's postcondition) into 28: 28's S3 and AC2 read per row; the compare-and-swap row asserts the branch at the sha the plant moved it to, still checked out, `git status --porcelain` empty and no `.governance/steps` or `.governance/outbox` path left; every other row keeps "at its old sha"; §4's row table gains the `expect` column naming each row's value. In 42, leave S1 and S2 as pointer stubs naming TOOL-dSafePassage-28 (keep their labels, as the 61 split did), move their criteria with them, and re-check what of S3 still stands in 42.

### Items

1. **Revise TOOL-dSafePassage-28** as a rev bump dated 2026-10-27, still `DEFERRED`: S3, AC2 and the §4 table as above; its `New arm:` covers list still names the criteria that observe the rows; one §9 line names this brief.
2. **Revise TOOL-dSafePassage-42** as a rev bump dated 2026-10-27, still `DEFERRED`: S1 and S2 become pointer stubs to 28, their criteria move with them, §3 Edges and §4 Files touched match; one §9 line names this brief.
3. **Cross-read** TOOL-dSafePassage-25, -27 (CLOSED, read-only) and -35 on M2's axes; fix a disagreement only in a DEFERRED spec.
4. **Commit nothing.** Return the files you wrote.

### Acceptance

- 28's AC2 names the per-row expectation and the compare-and-swap row's four postconditions.
- 42 no longer states S1 or S2's mechanism, and names TOOL-dSafePassage-28 where they were.
- With both specs flipped to `INPROGRESS` in a scratch working tree, `python tools/check-spec-tokens.py` prints no line naming either; restore the status before returning. If the scratch guard refuses the checker for your role, say so.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your files staged through `GIT_INDEX_FILE`, names no finding in them other than check 9's stale build index.

### Gates

Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.

### Non-goals

- No product code; no edit of a CLOSED spec.
- No commit, no stage into the real index, no deviation record.
