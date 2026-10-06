# TOOL-aMendedFleet-29 — acceptance ledger, and the spec-probe recall journal

**Serves:** journal TOOL-aMendedFleet-29

**Evidences:** TOOL-aMendedFleet-29
- AC1 — `python tools/memory-recall/check-recall.py --spec-probes` on the tree after the pass — exit 0, 88 rows and the summary line quoted below; one served-cache build, about 19 s
- AC2 — the same run — the row for `memory/builds/dMispairedQuote/spec/2026-09-01-spec-TOOL-dMispairedQuote-1.md` lists `TOOL-aLexedStripper-5 TOOL-aLexedStripper-4` and not `TOOL-aLexedStripper-3`; RED first in a `git clone --local` under `%TEMP%/r29` with the section-10 exclusion deleted from `derive_probe_labels`: the row listed `TOOL-aLexedStripper-3` first, and hit@10 rose to 0.5983 over 117, which is the contamination the exclusion removes
- AC3 — `python tools/memory-recall/check-recall.py --spec-probes` in that clone with every spec line naming `query.py` deleted — exit 1, printing `DEAD PROBE -- the harvest stage found no query.py probe`, and no figure
- AC4 — the AC1 run — the row for `memory/builds/dTieredTribunal/spec/2026-08-26-spec-dTieredTribunal-13.md` carries "why does agent-cap refuse a caller-settable bound wearing a constant's clothes" whole; RED first in the clone with the closing quote a character class: that row vanished, its question cut at the apostrophe and its `--terms` lost, and `no-terms` rose from 8 to 27
- AC5 — `git grep -n "hit@10" -- memory/builds/aMendedFleet` — hits this file's summary line, its reproducing command and the 20 verdicts below
- AC6 — `python tools/memory-recall/check-recall.py --help` — the `--spec-probes` line says it is a report that sets no floor and names the three blind spots: a probe return never written into section 10, today's corpus including later records, and ids outside the declared families

## The result

Reproduce with `python tools/memory-recall/check-recall.py --spec-probes` at this pass's commit:

```
check-recall: spec-probes -- probes 203 · set aside: no-terms 8 · no-label 107 · unresolved ids 0 · n 88 · hit@10 0.2955 (h 26, n 88) -- a report, no floor
```

The harvest also matches single and curly quotes, so it finds 203 probes where the spec's
double-quote probe found 123.

## The spot-check: 20 questions, by an agent

The sample is the first 20 graded rows in path order. A verdict is KEEP when at least one label is
a record that answers the question. It is REJECT when every label is a record the spec relied on
for something else.

1. `TOOL-aBatchedArm-1`, per-arm re-runs and a pooled harness — REJECT: both labels are unrelated red-suite asks.
2. `TOOL-aBatchedArm-2`, a parser for a gate's fail branches — REJECT: the one label is about the gate's spawn cost.
3. `TOOL-aBatchedArm-3`, sharding a self-test suite — KEEP: `TOOL-aShardedFloor-3` splits a gate's self-test by contract.
4. `TOOL-aBatchedArm-4`, serial runs by default and pooling under sweep — KEEP: `TOOL-aScannedThrottle-6` measures legs dilating inside the pool.
5. `TOOL-aBatchedArm-5`, the same question — KEEP: `TOOL-aPooledSweep-1` is the decision that the sweep pools and issues no cost verdict.
6. `TOOL-aDeclaredBound-4`, why the fan-out cap is a file constant — REJECT: both labels make the same argument about other constants.
7. `TOOL-aDeclaredCeiling-1`, a conf declaration instead of a hardcoded value — REJECT: both labels are about the size ceiling's value and its observed failing case.
8. `TOOL-aDeferredBar-1`, where a pass is told to run the bar — REJECT: the five labels are version-marker, budget and harness records.
9. `TOOL-aDeferredBar-2`, date-gated spec-token joins — REJECT: the label restructures the revision log.
10. `TOOL-aHonedRuleset-2`, the charter restating the micro-format grammar — REJECT: the label is a missing size ceiling.
11. `TOOL-aHonedRuleset-3`, the kickoff engine's exit-count floor — REJECT: none of the four labels is about that floor.
12. `TOOL-aHonedRuleset-5`, where the last-audit sha rule lives — REJECT: both labels are about other mechanisms.
13. `TOOL-aHonedRuleset-8`, why the micro-format gate is a conditional govkit entry — REJECT: ten govkit-adjacent labels, and none of them decides that entry. It scored a hit anyway.
14. `TOOL-aJoinedCanon-7`, a shape that makes section-7 gate names resolve — KEEP: `TOOL-dTieredTribunal-17` is the driver mapping spec sections by number.
15. `TOOL-aLeakedHandle-1`, a heredoc instead of a pipe in a while-read loop — REJECT: neither label is about that shell class.
16. `PLAY-aMendedFleet-1`, what the merge-bar section holds — REJECT: the label is the pre-push rule that section cites.
17. `TOOL-aMendedFleet-13`, a landed but unclosed spec — REJECT: both labels are about other checks.
18. `TOOL-aMendedFleet-14`, earlier bulk triage of stale asks — REJECT: the seven labels are the asks being triaged, not a prior triage.
19. `TOOL-aMendedFleet-15`, the severity pin blanked at the backlog switch-over — KEEP: `TOOL-dDerivedDocket-34` is the switch-over's decision record.
20. `TOOL-aMendedFleet-25`, an earlier byte ceiling on spec files — REJECT: the label is the harness-rendering ruling.

**5 KEEP, 15 REJECT.** So a label taken from citations outside section 10 is usually something the
author relied on, not the answer to the question. That makes the 0.2955 a noisy figure, and the
noise runs in both directions: row 13 scored a hit on labels that do not answer it. The owner's full
hand-check of the labels is parked in the run-state file, per the spec's resolved F2.

## The new arms

- `tools/memory-recall/test_recall_floor.py` gains `test_spec_probes_dead_harvest`, which runs a
  fixture repo with no section-10 probe and expects exit 1 and DEAD PROBE at the harvest, and
  `test_spec_probes_matched_delimiter`, which checks that an apostrophe question across a wrap parses
  whole and that a section-10 id is excluded. Both ran as a two-arm slice, outside the suite: green
  on the tree, then RED against the clone's staged breaks. The first went red when the
  empty-harvest branch was disabled, and the second when the closing quote was a character class.
  The suite as a whole did not run.

## Owed at the close

- `recall floor arms` and `memory-recall kit selftest` are held self-test legs, and neither ran in
  this pass.
- `codebase-map coverage + freshness` over the new definitions. `gen_map.py --write` regenerated
  `memory/map/generated/symbols.json`. `lexicon.py --offenders` lists none of the new names.
- The memory-recall kit version bump owed by the README edit, per the brief.
