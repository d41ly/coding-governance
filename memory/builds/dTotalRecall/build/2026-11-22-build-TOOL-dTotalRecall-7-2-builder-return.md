**Serves:** journal TOOL-dTotalRecall-7

# TOOL-dTotalRecall-7 build pass 2 — the builder's return

The gov-builder return for the pass dispatched at `822bb3213` from [2026-11-22-prompt-TOOL-dTotalRecall-7-build-brief-2](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-7-build-brief-2.md), recorded whole; the pass tip is `5688d011a`.

## Why

Before writing anything I checked rev-6 against the code and it could be built as written. Every surface it cites exists: `write_new_record`'s counter half, `read_kind_row`, `KIND_HANDLERS`, `tree_lib.read_policy_value`, `run_sourced`/`derive_ask_seq`, the `gov-claim.sh ask` "local … · no remote" answer, `record_kinds.check_row` and the catalogue row. With no remote, `derive_ask_seq` answered 1 in a seed that had no `.unattended.conf`, so the brief's mention of planting one was not needed. A seed with a committed `asks.acceptance = "bogus"` printed AC7's exact `policy: refused` line. So there was no divergence, and the unit is built and CLOSED in pass commit 5688d011a. The policy mirror is in a second commit, f33615fac (`Pass: none`), because `policy.py mirror --write` refuses an uncommitted catalogue.

## Summary

TOOL-dTotalRecall-7 is built in pass commit 5688d011a (base 822bb3213), and the policy mirror is in the follow-up commit f33615fac. No gate, suite or bar ran.

**What was built**
- `tools/memory-tree/backlog.py`: the new `check_ask_acceptable` predicate. V14 and R5 now both call it instead of their own copies.
- `tools/memory-tree/build_records.py`:
  - `write_seq_mint`: the counter half of `write_new_record`, moved out unchanged, and `write_new_record` now calls it.
  - The `ask-door` fixture plant: `seed_ask_repo`, `run_ask_door` and `check_ask_plant`.
- `tools/memory-tree/gov_record.py`: the `ask` entry in `KIND_HANDLERS` (`write_new_ask`), plus `derive_ask_key` and `render_backlog_text`, which writes `BACKLOG.md` in the same layout as the shell filer's `write_backlog_rows`. The steps run in the spec's order: arguments and `--family` check, policy read, grade, content key, listing (`exists` on a replay), mint, write and stage, read-back with rollback.
- `tools/memory-tree/record-kinds.toml`: the `ask` row, added by hand. Its table is re-rendered into `tools/memory-tree/HYGIENE.template.md` and `memory/HYGIENE.md`.
- `tools/policy/catalogue.toml`: `asks.acceptance` now has its summary and usage. It is drained from `unsummarised-keys.txt` and `memory/project/docs-undocumented.txt`, and its section is rendered in `help/reference/policy.md`.
- `tools/memory-tree/README.md`: the V14 line now names the predicate and the filing command.
- `tools/memory-tree/gen_build_index.py`: one new selftest arm for the predicate.
- `tools/memory-tree/check-memory-hygiene.test.sh`: one arm that runs the `ask-door` plant and skips aloud if a kit it needs is missing. The assertion floor goes from 828 to 830.
- Also in the pass commit: the acceptance ledger `memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-7-2-acceptance-ledger.md`, `symbols.json`, `RUN.md`, and the spec status set to CLOSED.

**Checks that ran**
- **AC1, AC3 and the new arm's expression:** `python -c` probes, which stand in for the build-index selftest's V14 arms. AC1 printed `[True, True, False, False]`; AC3 printed `[12, 14]`, and `[12]` with an accept clause.
- **AC2 and AC13:** the grep counts came out 1/3 and 1/1/1/0 as the spec expects. These only show that the code is present.
- **The `ask-door` plant**, run directly (`build_records.py --fixture --plant ask-door`, about 46 s, DERIVED from the builder's run): PASS on all 9 cases, covering AC4–AC7 and AC10–AC12. It stands in for the new `check-memory-hygiene.test.sh` arm. I also broke the code twice on purpose to check the plant fails. With the family check cut it printed `FAIL undeclared family`; with the listing cut it printed `FAIL replay`. Both were restored and checked byte-identical afterwards.
- **AC8:** a direct `record_kinds.check_row` call (standing in for the `record-kinds` leg) returned no reds on the `ask` row, and the "writer is empty" red when the writer was blank.
- **AC9:** `policy.py get asks.acceptance --explain` printed `refuse`, and the three grep counts read 0/1/0 (standing in for the `policy fixtures`, `policy check` and `docs` legs).
- **Naming lexicon:** every new function name passed `lexicon.py --suggest`.

**Owed at the close**
- Both `New arm:` RED-first observations:
  - The `gen_build_index.py` V14 arms plus the new `check_ask_acceptable` arm, broken by cutting the predicate's run test.
  - The `check-memory-hygiene.test.sh` `ask-door` arm, broken in turn by moving the grade after the write, cutting the family check, minting before the grade and cutting the listing.
- AC8's `record_kinds.py --check` line over the whole tree.
- TOOL-dTotalRecall-2's counter arms, which now run through `write_seq_mint`.
- Every leg in section 7.

**Other changes in the pass commit**
- Running `gen_build_index.py --write` re-rendered more than this unit's rows. The build README's status changed from INPROGRESS to DEFERRED, `memory/backlog/TOOL.md`'s TOOL-dTotalRecall-27 row and the `memory/LIVE.md` row moved, and the records region of this spec gained the ledger row. I declared these extra paths with `--dispatch` before staging them.
- Another session has unstaged edits to the specs of units 41 and 9. I staged the README with those two rows left at HEAD; their working-copy edits are still unstaged.
- The door also refuses a non-slug `--build`, a missing build folder and empty or multi-line values. The read-back also checks the filed ask's content key. Both are recorded as `Decided:` trailers, with no separate deviation record.

**Bug-class checklist**
I ran `gotchas.py --for-diff` over HEAD~1..HEAD and over 822bb3213..HEAD. Nothing needed fixing. The heredoc edits carried no backslash-sensitive text, and the generated regions show no CRLF churn. The one point left open: the BACKLOG layout is now written in two places, the shell filer and `render_backlog_text`, as the spec directs.

All temporary fixture directories were removed, and no command timed out or was skipped.
