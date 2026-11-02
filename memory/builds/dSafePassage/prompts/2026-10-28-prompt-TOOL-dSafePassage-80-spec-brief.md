**Serves:** research TOOL-dSafePassage-80

# Brief: the ceilings of the three legs this build added clear their evidence

## The prompt

> At the close, `python tools/run-gates/derive-ceilings.py --check` reports CEILING-EVIDENCE FAILED for the three gate legs dSafePassage added: `step-gate` (ceiling 60 s, evidence 4.4 s), `docs` (ceiling 60 s, evidence 2.7 s) and `upgrade-walk` (ceiling 7200 s, evidence 7177 s, the whole leg timed at the close on node a under load). The rule is a ceiling clearing its evidenced maximum by max(120 s, 1.0x). BUILD-METHOD M10 adopts that discovery as a unit at once.

## The brief

### Goal
Author the spec of TOOL-dSafePassage-80, which sets each of the three legs' `ceiling` in `tools/gate-legs.json` to clear its evidenced maximum in `tools/run-gates/ceiling-evidence.txt` by the margin `tools/run-gates/ceiling-margin.txt` declares, so `derive-ceilings.py --check` names none of them. The spec is Tier-2, status `DEFERRED`, `advances TOOL-dSafePassage-14`, `order 16` (TOOL-dSafePassage-61 holds order 16 and stays non-terminal), carries `**Derived:** TOOL-dSafePassage-5`, declares no `consumes-from` edge onto a CLOSED unit, and has one mechanism, §6 criteria each with a Red-when, §7 gates with a `New arm:` line or the reason the check's own failing case is its arm, and §10 reuse. Add its row to the README `roster:units` table. Read how the margin is computed in `derive-ceilings.py` before choosing a value, and state the value and the evidence row it clears for each leg; never edit `ceiling-evidence.txt` by hand.

### Items
- `step-gate`: ceiling 60 s against evidence 4.4 s.
- `docs`: ceiling 60 s against evidence 2.7 s.
- `upgrade-walk`: ceiling 7200 s against evidence 7177 s; say in §3 what a whole-leg cost of about two hours means for the bar under the charter's cost rule, as a finding for the owner, not a change.

### Non-goals
No product code; no edit to a CLOSED spec; no commit, no stage into the real index, no RUN.md row; no other leg's ceiling.

### Acceptance
The spec names each leg's new ceiling with the arithmetic that clears its row, and is conforming. `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your files staged through `GIT_INDEX_FILE`, names no finding in it other than check 9's stale build index.

### Gates
Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.
