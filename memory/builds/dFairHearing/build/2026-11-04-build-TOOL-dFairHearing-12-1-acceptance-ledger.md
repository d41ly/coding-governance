# Acceptance ledger — TOOL-dFairHearing-12

**Serves:** journal TOOL-dFairHearing-12

Built against spec rev-3 and committed as pass commit `af3831a6c`, at parent `d059e36fd`. The main loop drafted this ledger at the close from the builder return `2026-11-03-build-TOOL-dFairHearing-12-1-builder-return.md` and the pass commit's message; nothing below was observed again for it. AC7's line was observed at the close. No suite, gate or bar ran in the pass: the `review-replay selftest` leg, the `New arm:` line's RED-first observations and the spec's other legs are owed to the close.

The close observed this unit's `New arm:` lines on 2026-11-08 at `4896589bc`: each row, RED or UNSEEN with its log line, is in `2026-11-08-build-TOOL-dFairHearing-1-arm-observations.md`, and every suite holding them exits 0 at that tip.

**Evidences:** TOOL-dFairHearing-12
- AC1 — `m1b` — a scratch results copy whose `m1b` row has no `seams` exited 2 naming `m1b` and `incms-decor-texture`, and a compare of two arms with no case in common exited 2 naming the empty pairing
- AC2 — `--grade m1b` — grade, compare and judged over the `b0fe68f30` blobs matched the grader blob run in the same probe: `positives 15 solved 10`, `items 17/40`, `graded 19 of 30`; `common 19 (15 positive)`, solved 10/15 against 9/15, MUST 97 against 114; `judged common 30 (24 positive)`, `primary 17/24`, `items 39/59`
- AC3 — `--corpus memory/builds` — that run and the two named records' runs are byte-identical to `review_replay.py` at `3708a705`, and the factory's `review-replay` CLI prints the same bytes as the adapter
- AC4 — `replay_scorer.extract_tag_ref` — all four results were as the criterion states, and `measure_recall` at window 0 over the tag match raised nothing
- AC5 — `check_instances()` — it returned None, and named `scouted-seam` once that entry was deleted
- AC6 — `replay_scorer.scan_pairing_sites` — the live tool root yielded no site, the grader blob yielded `bench.py:384` and `bench.py:647`, and a scratch copy of `tools/` with a planted module named only that module. The factory's own source, copied under another name, was not named
- AC7 — `ARMS_DECLARED` — at the tip `948e4141b`, `python tools/workflows/replay_scorer.py --selftest` printed `replay_scorer selftest: 29/29 arms` and exited 0, its `deterministic` arm ok. The count is the current declared total, not this pass's. The byte-identical `--compare` half is the builder return's
- AC8 — `--results` — both bad sources exited 2 naming the object
