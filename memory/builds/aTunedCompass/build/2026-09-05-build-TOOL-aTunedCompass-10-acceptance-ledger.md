# aTunedCompass — the acceptance ledger for unit 10

**Serves:** journal TOOL-aTunedCompass-10

*Node `a`, 2026-09-05, written by the unattended run that built the unit.*

Every line below is `OBSERVED` with the command that made it, or `AMENDED` naming the revision that
changed the criterion. There is no third form.

## The finding AC4 exists to force into the open

**The narrowing LOWERS the overall hit rate, 0.600 → 0.586.** AC4 says in its own words that this is
a finding to report and not a result to bury, so it is the first thing in this record.

Measured precisely, over the same 140 phrases:

| | before (kind-only) | after (directory-scoped) |
|---|---|---|
| hit rate | 0.600 | **0.586** |
| hit@5 | 0.371 | 0.371 |
| hit@10 | 0.400 | 0.400 |
| upper-median rank of first correct | 2 | 2 |

Two phrases lose their hit and **none is gained**. Their ranks BEFORE were **31 and 27** — both far
below the twelve-slot neighbour cap, so neither answer was ever printed to a reader. Among phrases
hitting in both states, one rank improves and none worsens.

So the trade is: two answers that existed only in a list nobody sees, against a neighbour pool that
a cap can meaningfully bound. That is worth taking, and it is worth an owner knowing it was taken.
The alternative reading — that the predicate is too aggressive — is not supported by these numbers,
because the loss is entirely below the cap and the top of the list is unchanged.

## Evidences

**Evidences:** TOOL-aTunedCompass-10

- AC1 — `python tools/codebase-map/reuse_lookup.py` on this build's own probe phrase, checked in
  process rather than by reading printed reasons: the seed directories are `tools/codebase-map` and
  `tools/memory-recall`, and the count of same-kind neighbours from any OTHER directory is **0**.
- AC2 — `reuse_lookup.assemble_shortlist` driven in process, looping over every (directory, kind)
  group in the corpus holding more than one symbol: **18 groups, 18 probed, 0 whose narrowed arm
  came back empty.** So the empty-pool state F1 accepts is real in principle and unreached on this
  corpus today.
- AC3 — `python tools/codebase-map/selftest.py` — **28 executed, 0 skipped, PASS**, with the new
  two-direction arm. Observed RED against the un-narrowed predicate first, and the failure names
  what it admitted: `the same-kind arm admitted a candidate from another directory ... ['far_helper',
  'near_helper']`. The fixture gives `far_helper` the HIGHER fan-in of the two on purpose, so its
  absence is the predicate refusing it rather than the ranking burying it — otherwise the arm would
  pass for the wrong reason.
- AC4 — `python tools/codebase-map/replay-phrases.py`, before and after, `--json` for the per-row
  join. The table above is the result; the two lost phrases and their prior ranks are named there.
- AC5 — `python tools/codebase-map/gen_map.py --check` — exit 0 after `--write`, and
  `memory/map/features/codebase-map.md` carries the narrowed predicate, its measured reach
  reduction, and the cost above, refreshed in this same commit.
- AC6 — `bash tools/check-kit-versions.sh` — exit 0 with `KIT_CODEBASE_MAP_VERSION` at `1.6` and
  the `gov:kit codebase-map@` marker moved with it.

## A note on the instrument, because it nearly produced a false number

The staged break for AC4 was applied twice by a script that asserted on a multi-line string. The
file holds CRLF, so the match failed, the script raised before writing, and the "before" run
executed the UNCHANGED code — producing two identical columns that would have read as "the
narrowing changes nothing". The break was redone line-by-line and VERIFIED with a grep before the
measurement was taken. This is the third time in this build that a CRLF working copy has silently
defeated a multi-line edit, and the lesson is the one already recorded for unit 5: the instrument
that stages a break needs checking as carefully as the arm it arms.
