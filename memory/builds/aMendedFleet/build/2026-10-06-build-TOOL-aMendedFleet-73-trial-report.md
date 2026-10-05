# TOOL-aMendedFleet-73 — the vague-brief trial: stopped at the pilot, no headroom

**Serves:** journal TOOL-aMendedFleet-73

## Result

The trial ran once, from the main loop, as one Workflow call over the committed script
`2026-10-06-build-TOOL-aMendedFleet-73-trial.js`, on 2026-10-06 on node a. It stopped at stage 2, the
headroom guard, before either arm ran:

- **Verifier.** It renamed no test: all ten `test_intent_*` tests reach the tool only through what the
  vague brief pins, and all fifteen `test_contract_*` tests assert something only the full brief
  pins. `cells` made eleven cells, `freeze` wrote both hashes to the committed `-73-freeze.tsv`, and
  `stub` printed `stub: 25 tests, 0 passed the exit-0 stub`.
- **Pilot.** One agent built `declared.py` from the three-sentence brief with no plan and no spec.
  `hidden` graded it `intent 10/10 = 1.000` and `contract 5/15 = 0.333`; the rows are in the
  committed `-73-results.tsv`.
- **Stop.** 10 of 10 is above the 0.8 guard the spec fixed before the run, so the workflow returned
  `stopped: headroom` and spawned nothing further. Three agents ran, of the 27 the full trial costs.

## What it means

The question was whether, on a vague brief, a full Tier-2 spec builds a better tool than a 40-line
plan. This instrument cannot answer it: a build with NO design document already passes every intent
test, so neither arm could score above it. The aBlindedTrial build met the same ceiling on explicit
briefs, where every tool passed its hidden suite; this run shows the ceiling holds on a three-sentence
brief too, and that the guard caught it for three agents instead of twenty-seven. The charter's §1
design-pass rule is unchanged, as the spec required: the trial reports and changes no rule.

The contract rate, 5 of 15, has room, but it measures guessed spellings the vague brief never states,
so it ranks luck, not design. The instrument with room is the decision list: eighteen behaviours the
full brief pins and the vague one leaves open, which stages 4 and 5 grade through blind probes. A
rerun that makes the decision-met rate the primary measure, with its own pilot headroom check, is
filed as TOOL-aMendedFleet-109.

## The instruments, after the run

- The `tokens` verb matched its tag only at the start of an agent's first prompt, and the Workflow
  harness puts a preamble there, so it read every agent as untagged. It now searches for the tag:
  the trial's three agents read `verifier` 2269, `pilot` 6676 and `runner-pilot` 386 output tokens.
  It still reads the whole session tree, so in this shared session the other 138 workflow agents
  count as untagged; a rerun belongs in a session of its own.
- `aggregate` over the committed rows exits as a DEAD PROBE, because there is no score row to read.
- The cells are under `%TEMP%` and are not part of the record; the pilot's grading rows are.
