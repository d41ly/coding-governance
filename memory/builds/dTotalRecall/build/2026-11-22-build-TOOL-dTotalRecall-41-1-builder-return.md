**Serves:** journal TOOL-dTotalRecall-41

# TOOL-dTotalRecall-41 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `4ddb0f115` from [2026-11-22-prompt-TOOL-dTotalRecall-41-build-brief](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-41-build-brief.md), recorded whole; the pass tip is `c2814ccc0`.

## Why

TOOL-dTotalRecall-41 is built as its rev-4 spec says. Every claim the spec makes about current code held when checked against the tree: `write_new_ask`, `render_ask_row`, `parse_file`, `derive_clauses`, `build_corpus`, `check_ask_acceptable`, the `ask-door` plant, `read_open_asks`, and the unattended.sh symbols it cites. So nothing diverged. One phrase in §2 is stale: it calls unit 7's handler "unbuilt at HEAD", but unit 7 has since been built and CLOSED. The units still fit together, so I treated that as stale wording, not a divergence.

## Summary

Pass commit c2814ccc0 on base 4ddb0f115. Its trailers are `Pass: TOOL-dTotalRecall-41`, `Co-Authored-By: Claude Opus 5` (the charter's spelling) and three `Decided:` lines. In the same commit the spec header moved INPROGRESS to CLOSED, with the date already 2026-11-22.

What was built:
- **tools/memory-tree/backlog.py** — new `check_row_value(label, value)`. It raises ValueError naming the label and the character when a value holds a CR, an LF, SEP or ARROW.
- **tools/memory-tree/gov_record.py** — `write_new_ask` now runs in §4's order:
  1. calls `check_row_value` on `--text`, each `--clause` value, `--pointer` and the `--sev` reason (unit 7's empty-value refusal stays beside it);
  2. reads `asks.acceptance`;
  3. parses BACKLOG.md once (the before-parse);
  4. renders both rows under the provisional id `<FAMILY>-<slug>-0` into the would-be file, parses it, and requires exactly one added ask and one SEV row, using the new `check_rows_added`;
  5. grades `derive_clauses(build_corpus([would]))` for the provisional id;
  6. runs the listing over the before-parse;
  7. mints and writes;
  8. counts the written file again, keeping unit 7's key check and restore.
  The renderer is called through the module, so a rebound `backlog.render_ask_row` is the one used.
- **tools/memory-tree/build_records.py** — `RENDER_PLANTS` (`drop-clauses`, `second-ask`) and `run_planted_door`, a child Python that rebinds `backlog.render_ask_row` and then calls `gov_record.main`. `check_ask_plant` gains the six cases §7 names: `text-newline`, `text-separator`, `pointer-cr`, `sev-newline`, `graded-args-not-row`, `two-rows-added`.
- **tools/memory-tree/check-memory-hygiene.test.sh** — only the `ask-door` hit's comment changed; the assertion count is unchanged.
- **Regenerated files:** memory/map/generated/symbols.json from `gen_map.py --write`, and from `gen_build_index.py --write` the build README, memory/LIVE.md, memory/backlog/TOOL.md and this spec's generated records table.
  - In the README I staged only this unit's rows. The TOOL-dTotalRecall-67 row change belongs to another writer and is left unstaged.
  - The commit also carries the RUN.md rows that `--dispatch` and `--brief` staged; `--brief` reported "already recorded, unchanged".
- **Acceptance ledger:** memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-41-1-acceptance-ledger.md.

The first commit attempt was refused by hygiene check 23: the AC4 ledger line led with `two added asks`, which the criterion does not spell in backticks. I re-led it with `backlog.render_ask_row` and the commit passed the pre-commit hook.

Checks that ran, all probes of the unit's own code, no gate:
- `python tools/memory-tree/build_records.py --fixture --plant ask-door` printed `build-records: PASS ask-door — 15 cases`, each of the six new cases exiting 2 with its needles. This stands in for the `memory-hygiene self-test` leg's `ask-door` hit.
- A python -c probe in a scratch seed under %TEMP% printed every refusal message, including `--clause accept holds the pointer arrow`.
- A second probe used a renderer that varies with the id. It passed the provisional count, then exited 2 at the post-write read-back with the file restored and an empty status. That probe is not one of the plant's cases.
- `lexicon.py --suggest` printed OK for `check_row_value`, `check_rows_added`, `run_planted_door` and `render_rows`. `lexicon.py --measure` kept `VERB_OFFENDER_PIN` at 1448.

Owed to the close (main loop), from §7:
- The `New arm:` RED-first observation for AC1 to AC4: the `ask-door` hit in check-memory-hygiene.test.sh, staged three ways in turn — cutting the `check_row_value` calls, grading the argument mapping, and cutting the count — each seen red, then green restored.
- The legs `memory hygiene`, `memory-hygiene self-test`, `build-index selftest`, `backlog migration selftest`, `recall floor`, `recall floor arms`, `drift-audit selftest`, `memory-recall kit selftest`, `policy fixtures`, `lexicon naming predicates`, and the four codebase-map legs.

`gotchas.py --for-diff HEAD~1..HEAD` selected 41 classes; I read the first 14 it printed and acted on them:
- **fixture-passes-by-finding-nothing:** each case asserts exit 2, specific needles and a clean status, and the later `file` case minting EXMP-tDoor-1 shows no refusal minted.
- **staged-break-substitutes-a-synthetic-value:** the plants wrap the shipped renderer rather than replace it.
- **guard-above-a-fold:** `check_row_value` now catches injected rows before the post-write count can see them, so that count is exercised only by my probe, not by the plant.
- **heredoc-escape:** no heredoc was used.

No command timed out or was skipped.
