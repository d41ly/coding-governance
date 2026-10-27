**Serves:** journal TOOL-dSafePassage-9

# TOOL-dSafePassage-9 — acceptance ledger

The unit as built, at spec rev-5. In `tools/govkit/govkit.py`: `VERDICT_GRID[("differs", "absent")]`
answers `retired-edited`; `UPDATE_ROLE` and `UNLANDED_REASON` gain the `retired-edited` row (its
disposition `order`); the seed override passes `SEED_KEPT_VERDICTS` through; selfcheck arm 7g's two
loops are `derive_dispatch_gaps`. The write loop's ordered arm, before its `how` guard, takes
`ORDERED_VERDICTS`: `read_retired_edits_mode` reads `install.retired-edits` once per run through
TOOL-dSafePassage-6's `read_policy_value`, `write_row_order` writes the order (the `withdrawn` arm's
writer, extracted), `render_retired_edited_line` prints the row's line, and a first-time row's role
becomes `retired-edited`. `check_render_edited` makes an edited render `render-edited` and holds its
kit. The withdrawn arm unwires a `.fragment.json` row through `remove_wired_fragments(...,
cause="withdrawn")` before any deletion, under the target-code switch read once above the write loop,
and a rollback of that kit re-wires it through `run_fragment_merges` after its files are restored.
The fixture is `tools/govkit/fixtures/retired_edits.py` (deviation 175); the selftest gains 16
`[dSafePassage-9]` rows; `help/update-edits.md` and its index line are new; the catalogue row gains
`summary` and `usage`, drained by `lists --write`; the mirror follows in its own commit.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each AC was observed on
node d (Windows, Python 3.15.2) by the fixture CLI or a `python` probe of the changed code.

- AC1 — `--plant fragment-withdrawn` exit 0, 5 of 5: entry `gone`, fragment `present`, one withdrawn order; `--write-withdrawals` exit 0, entry `gone`, file `gone` (the unwire read the fragment, so it ran first); `--rerender-off` exit 0, 6 of 6: entry `wired`, file `present`, one `left WIRED — GOVKIT_RERENDER=0` line.
- AC2 — `--plant fragment-rollback` exit 0, 6 of 6: `hooks: tools/demo/hook.fragment.json unwired, gov no longer ships it`, `ROLLED BACK`, the entry `wired` after. Red when, observed: the re-wire guard patched to `if False:` printed `settings entry after the rollback: 'gone' · expects 'wired' · MISS`, exit 1; restored byte-identical.
- AC3 — `--plant edited-gone` exit 0, 7 of 7: verdict `retired-edited`, one `update-retired-edited-` order, role `retired-edited`, bytes kept under `--write-withdrawals`. Red when, observed: the cell patched back to `patched` printed four MISS lines (`verdict ... 'patched'`, `retired-edited orders: '0'`), exit 1.
- AC4 — `--plant edited-row` exit 0, 9 of 9; `--stub forked` exit 1: `verdict ...: 'report'`, `retired-edited orders: '0' · expects '1' · MISS`, `the order line: 'False'`.
- AC5 — `--plant dispatch-gap` exit 0, 3 of 3: one message naming `'retired-edited'` over the copy, none over the module's tables. Red when, observed: the `UNLANDED_REASON` row renamed away printed `the message names the role: 'False'` and `messages over the module's own tables: '1'`, exit 1.
- AC6 — `--plant keep` exit 0, 9 of 9: `kept, no order (install.retired-edits = keep)`, no order; `--stub report-omits` exit 1, `the line naming keep: 'False' · expects 'True' · MISS`.
- AC7 — `git grep -n -e "update-withdrawn-" -- tools/govkit/govkit.py` finds no line: the one order writer is `write_row_order`, composing `update-<kind>-<slug>.md`. A probe wrote the withdrawn order through `write_row_order` and compared it with the `3708a705` f-string over the same row and vintage: equal bytes, both with and without `--write-withdrawals`.
- AC8 — `--plant render-edited` exit 0, 6 of 6: the recorded `oid` present, verdict `render-edited`, `HELD BACK demo:`, one `update-render-edited-` order, edit kept; `--stub today` exit 1: `re-rendered`, no HELD BACK, no order, `the edited bytes: 'overwritten'`.
- AC9 — `--plant render-clean` exit 0, 5 of 5: `re-rendered`, no order, the render `tpl v3`.
- AC10 — the `tomllib` probe printed `[(['order', 'keep'], 'order', 'dSafePassage', True, True)]`; `git grep -n -F 'read_policy_value("install.retired-edits"' -- tools/govkit/govkit.py` found one line. The `-x` grep refused on this host's git (`error: unknown switch 'x'`, exit 129); `git grep -c -F "install.retired-edits" -- tools/policy/unsummarised-keys.txt` found none (exit 1), and `lists --write` printed `drained 1: install.retired-edits`.
- AC11 — `git grep -n -e "retired-edited" -- help/` finds `help/update-edits.md` and its `help/README.md` line.
- AC12 — `--plant seed-retired-edited` exit 0, 5 of 5; `--plant seed-retired-clean` exit 0, 6 of 6 (`withdrawn`, the `reported only` line, no order, the copy kept); `--stub seed-override` exit 1: `patched`, `retired-edited orders: '0'`, role `seed`.

OWED AT THE CLOSE: the bar's legs §7 names, and the New arm's RED-first observation (the
`[dSafePassage-9]` rows of `tools/govkit/selftest.py`, red on a staged break, green restored).
