**Serves:** journal TOOL-dTotalRecall-47
**Caused-by:** TOOL-dTotalRecall-47

# TOOL-dTotalRecall-47 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `d8db5522f` from [2026-11-22-prompt-TOOL-dTotalRecall-47-build-brief](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-47-build-brief.md), recorded whole; the pass tip is `a5f016658`.

## Why

TOOL-dTotalRecall-47 is built as its spec (rev-3) says, and its status header is set to CLOSED · 2026-11-23 in the same pass commit. Before any write I checked the spec's claims against the source and all of them held: `check_causes`, `read_bindings`/`_expand_ids`, `BIND_HEAD_LINES`=12, `read_header_edges`, `build_records.derive_record_name` and the `root` column. No divergence.

## Summary

TOOL-dTotalRecall-47 is committed as a5f016658 on base d8db5522f, with a `Pass: TOOL-dTotalRecall-47` trailer. Its AC1 and AC3 fixtures pass. AC2 was observed only through the verb itself and a `check_causes` probe; the `--check` run and the gates are owed to the close.

What was built, in tools/memory-tree/record_causes.py:
- **The verb:** `write_missing_causes(root)` behind `--backfill` (S1, S2). It picks the causes check's findings whose rule is `ABSENT_CAUSE`. That finding text is now a constant, so `check_causes` and the verb read the same rule. For each pick it writes `**Caused-by:** <first Serves id>` under the first Serves line, keeping the file's own line ending.
- **What it refuses:** it lists these under `not backfilled` and leaves them byte-identical: a non-Markdown record (`not markdown`), a typed-named record (`typed kind`), a record with no id (`no id`), and one whose Serves line is unfenced line 12 (`head window`).
- **The plants:** `backfill-selection` and `backfill-refusals` (`BACKFILL_PLANTS`) are new fixture plants. `check_backfill_plant` grades them and prints PASS or FAIL.
- **The test arm:** a new block in tools/memory-tree/check-memory-hygiene.test.sh covers AC1 and AC3.
- **The ledger:** memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-47-1-acceptance-ledger.md, which carries its own `Caused-by` line.
- **Regenerated and committed:** `symbols.json` (from `gen_map.py --write`) and the files `gen_build_index.py --write` rewrote (LIVE.md, backlog/TOOL.md, the build README, the spec's records region). RUN.md is in the commit too.
- **Build status:** after the regeneration the build README and LIVE.md show the build as DEFERRED, because no unit is INPROGRESS any more. Unit 51's pass committed the same kind of change.

Checks that ran (each a probe of this unit's own code, standing in for the `memory-hygiene self-test` arm and the `record causes` leg):
- **AC1:** `python record_causes.py --fixture --plant backfill-selection` exited 0 with PASS.
  - The first run wrote only `-new.md` and listed `-probe.sh` and `-unbound.md`.
  - The fixture's `git status` showed only `-new.md` changed.
  - `--check` named exactly those two records under causes, and the second run printed `0 backfilled`.
- **AC3:** `--plant backfill-refusals` exited 0 with PASS: `typed kind` and `head window` were listed and the fixture's status was clean.
- **The grade can fail:** in a `python -c` probe I moved the Serves line to unfenced line 11. The verb then wrote the record and the plant printed FAIL, so the window limit is exact.
- **Line endings:** a `python -c` probe over a CRLF record, and over one whose Serves line ends the file with no newline, kept each file's own line ending; a second run wrote nothing.
- **AC2 / S3:** `record_causes.py --backfill` on the real tree, run both before and after the ledger was staged, printed `0 backfilled · 0 not backfilled`. A `python -c` probe of `check_causes` over the tree found nothing. So S3 commits no backfilled records: nothing added after unit 19's seed is causeless at this tip.
- **Naming lexicon:** `lexicon.py --suggest` answered OK for `write_missing_causes`, `derive_backfill_refusal` and `check_backfill_plant`. Because all three start with a declared verb, I did not re-measure `VERB_OFFENDER_PIN`.
- **Pre-commit hook:** it passed during the commit, including `codebase-map coverage + freshness`.
- **Bug-class checklist:** `gotchas.py --for-diff HEAD~1..HEAD` listed 34 classes plus 6 universal ones. I went through the relevant ones and none needed a change:
  - a fixture passing by finding nothing: both plants require non-empty expected sets;
  - an append that repeats: the second run is observed;
  - inserting after a key that occurs twice: the first Serves line with ids is used, the same rule `read_bindings` follows;
  - a fact in two places: `ABSENT_CAUSE` is defined once;
  - inline fences and heredocs: none were used.

Owed to the close (none ran here, and no command hit its time limit):
- `python record_causes.py --check` at the tip printing `0 causeless`, i.e. the `record causes` leg (AC2).
- The `memory-hygiene self-test`, and the `New arm:` RED-first observation for tools/memory-tree/check-memory-hygiene.test.sh (AC1, AC3), staged by letting the verb write a legacy record and a typed record.
- `memory hygiene`, `recall floor`, `recall floor arms` and `lexicon naming predicates`.
