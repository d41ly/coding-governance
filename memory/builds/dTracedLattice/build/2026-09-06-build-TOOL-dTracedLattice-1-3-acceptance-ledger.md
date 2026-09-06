# TOOL-dTracedLattice-1 — acceptance ledger

**Serves:** journal TOOL-dTracedLattice-1

Nine scope items, and two of them did not ship: S3 and S2 were SPECCED conditional on their own
measurements and both failed them. The ledger records that as a result, not as a gap — the figures
are in `2026-09-06-build-TOOL-dTracedLattice-1-2-s2-s3-measured.md`.

**Evidences:** TOOL-dTracedLattice-1
- AC1 — `python tools/codebase-map/rank_harness.py --scenarios tools/codebase-map/scen-adversarial.json` — recall@5 is 17/28 with S1+S5 and 17/28 without, measured with the same instrument at the same sha by staging the pre-change spelling and restoring it. Comfortably above the `11/28` floor. recall@10 moves 22 to 21, a real one-scenario loss at depth, disclosed rather than averaged away
- AC2 — `python3 tools/codebase-map/selftest.py` — the arm `every co-defined symbol reaches every definer (AC2)` joins `symbols.json` against the loaded corpus and fails when any id with several definers yields fewer candidate files than it has definers. Observed RED against the pre-S1 last-write merge: `('ConfError', ['tools/lexicon/lexicon_conf.py', 'tools/memory-recall/recall_conf.py'], ['tools/memory-recall/recall_conf.py'])`. It REFUSES a corpus with no co-defined symbol rather than passing vacuously
- AC3 — `python tools/codebase-map/rank_harness.py --scenarios tools/codebase-map/scen-adversarial.json --control shuffle --trials 200` — the landed ranking scores 0.607 at k=5 against a shuffle p50 of 0.179 and p95 of 0.286. CLEARS. The control randomises position while holding each scenario's shortlist DEPTH and whether the answer was present at all, so it asks the question the criterion asks
- AC4 — `rank_harness` per-scenario ranks, run with and without S3 — used as the gate it is: S3's delta is ONE discordant pair at k=5 and zero at k=1, 10 and 20, which is below the criterion's floor of 6, so the delta was not reported as a finding and S3 did not land. The criterion's value here was refusing a change, which is the use it was written for
- AC5 — `python tools/codebase-map/replay-phrases.py` under two resolutions — the FILE-position reading says hit@5 falls 0.462 to 0.378 and the CANDIDATE-position reading says it holds at 0.385 with hit@10 up 0.420 to 0.441 and the hit rate up 0.587 to 0.615. A change winning one and losing the other has been framed, not measured — so both are recorded and the disagreement is DIAGNOSED rather than resolved by preference: S1 makes one candidate contribute every definer, so counting file positions charges a four-definer candidate four ranks while the shortlist a reader scans is one line per candidate. `measure_phrase` now ranks by candidate and its header carries both readings
- AC6 — amended rev-9 — its base_sha bias is an ABSOLUTE-recall bias: replaying at HEAD credits the tool with dossiers the graded unit itself wrote. A PAIRED before/after at one sha carries that bias identically on both sides, so it cancels out of the delta, and this unit makes only paired claims. The §9 line logs it
- AC7 — `grep -rn "specificity\|stem_spread" tools/codebase-map/*.py` returns nothing — no name-shape or frequency predicate is in the shipped code, because the one that was written (S3's stem spread) was measured and reverted. There is nothing for a harness to re-implement and nothing to byte-compare
- AC8 — the cost measurement that REJECTED S2's docstring probe — `ast.parse` over the 47 python files costs 1.1665 s against a whole `reuse_lookup` run of 1.162 s, and a regex over text the reference walk already reads costs 0.0508 s. The ceiling is 0.05 s. What DID land adds no scan at all: `fan_in` changes an argument type, and S6's coverage counters increment inside the existing walk
- AC9 — `python tools/codebase-map/rank_harness.py --scenarios tools/codebase-map/scen-adversarial.json --control constant` — the query-ignoring most-changed-files control scores 0.000 at k=5 and 0.107 at k=20 against 0.607 and 0.929. It clears, and the control is WEAK on this set: this repo's recent churn is dominated by `memory/` records while the scenarios target `tools/`, so churn barely intersects the answer set. Saying so is worth more than the ratio
- AC10 — `python tools/codebase-map/map_diff.py 6ec402bd..HEAD --converge` and `python tools/codebase-map/replay-phrases.py` — both disclosures, both readings taken at this commit rather than quoted. `dead_exports` moves 475 to 491. Citation churn over the 143 recorded phrases with section-10 ground truth: hit rate 0.587 to 0.615, hit@5 0.385 to 0.385, hit@10 0.420 to 0.441, upper-median rank of the first correct answer 2 in both
- AC11 — `memory/backlog/TOOL.md` — the `TOOL-aScouredKit-16` row carries the amendment: the dot-prefix half is REJECTED with the measurement rejecting it, and the three claims about the reinvention backlog being tracked, permanent and shipped to adopters are corrected in place. The row was edited by this unit alone, per S7
- AC12 — `python3 tools/codebase-map/selftest.py` — the arm `scan coverage line cannot go quiet (AC12)` asserts all three facts separately and was observed RED three times, once per fact removed from the emitting expression. It also pins that a scan which never ran says `not run` rather than printing zeros
- AC13 — `python3 tools/codebase-map/selftest.py` — the arm `gov-only files withheld on both paths (AC13)` derives the population from `kit.toml`'s own `project-owned` claims, excludes the seed destination by name, and asserts every member is also named in `WIRE-INTO-PROJECT.md`'s removal row. It states what it does not check: a gov-only file claimed in NEITHER carrier is invisible to it

## What this ledger does not evidence

The 132-scenario graded replay corpus AC5 and AC6 were written against was not rebuilt; the
citation replay above runs over 143 phrases harvested live from tracked specs by
`replay-phrases.py`, which is a different population reaching the same question. No unit's figures
were carried forward from the design dossier — every number above was produced by a command named
beside it, at this commit.

## One trap worth the line

`tools/install-prefix-waivers.txt` keys its rows by `<path>:<line>`. The 39 lines this unit added to
`map_lib.py` moved a waived literal out from under its waiver and reddened the leg for a change that
never touched the literal. Re-keyed rather than re-waived, so the count is unchanged — but a
line-keyed registry breaks under any insertion above its rows, and the next build to grow a waived
file will meet it again.
