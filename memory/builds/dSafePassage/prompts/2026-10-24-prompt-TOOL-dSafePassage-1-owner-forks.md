**Serves:** research TOOL-dSafePassage-1 TOOL-dSafePassage-6

# Brief: the owner resolves TOOL-dSafePassage-1's F12 and TOOL-dSafePassage-6's F7

## The prompt

> Spec 1, fork F12 go with the recommendation. Spec 6, F7 - not sure, if it's a non-breaking point - i'm for it.

— owner, 2026-10-24. F7's option (a) is non-breaking. Its one miss, a policy kit homed somewhere other
than the path written at render, makes the forwarder read `warn`, the key's catalogue default, and
still forward the call. The owner's condition holds, so F7 stands at (a) on the owner's word.

## The brief

### Goal

Mark both forks resolved by the owner, and make each spec read as its fork now decides.

### Items

1. **TOOL-dSafePassage-1, §8 F12.**
   - Append `RESOLVED (owner, 2026-10-24): (a).` to the fork, in the closed-paren form
     `memory/TEMPLATE-SPEC.md` gives.
   - Where S8, §4 or Files touched point at F12 instead of stating the outcome, state (a) directly. The
     seven `tools/policy/caps.toml` rows take the `policy` home form. `arm_limits_readers`' row and the
     cases planting the limits file go. `budgets-two-homes` is re-planted on a `conf:` home.
   - AC15 already passes only under (a), so it needs no change.
2. **TOOL-dSafePassage-6, §8 F7.** Replace `RESOLVED (agent, 2026-10-24, delegated): (a), ...` with
   `RESOLVED (owner, 2026-10-24): (a)`. Keep the option text and its tie-break reasoning. Add one short
   clause saying the miss reads `warn` and forwards, so the pick breaks no adopter's call.
3. **Both specs:** bump the **Status:** rev by one, dated 2026-10-24, still `DEFERRED`, and add one §9
   line naming the fork and this brief.
4. **Size, TOOL-dSafePassage-1 only.** The spec is 48847 bytes against a 49152 class cap, and the index
   render will add three records rows of about 165 bytes each. Bring `wc -c` to at most 48150 before
   the render by cutting authored prose anywhere outside the generated `gen:spec-records` region.
   Long §9 lines, Readers lines and §5 lines are the cheap places. Change no meaning, criterion or
   Carries line.

### Acceptance

- `grep -n 'RESOLVED (owner, 2026-10-24): (a)'` prints the F12 line in spec 1 and the F7 line in spec 6.
- Spec 1's `wc -c` is at most 48150, and spec 6's is under 49152.
- Each spec's **Status:** is one rev higher, and its §9 holds the new line.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your
  spec staged through `GIT_INDEX_FILE`, names it only for findings a `gen_build_index.py --write` render
  cures. Delete the copy after.

### Gates

Only the memory hygiene gate and the naming lexicon, as the role allows.

### Non-goals

- No other fork, criterion or spec. No Carries line.
- No commit, no stage into the real index, no deviation record: the main loop writes those.
