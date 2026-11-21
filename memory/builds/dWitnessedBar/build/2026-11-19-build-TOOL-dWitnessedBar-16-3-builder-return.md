**Serves:** journal TOOL-dWitnessedBar-16

# TOOL-dWitnessedBar-16 — builder return 3 (run `wf_8d4ba11d-d24`), a divergence, nothing committed

## Why

DIVERGENCE: before writing anything I checked spec rev-11 (memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-16.md) against the tree at f294dafda. It cannot be built as written. Items (1) to (3) block the build; (4) to (6) are smaller gaps reported now so this unit does not diverge again over them.

(1) Three shipped readers have no way to reach the factory. This hits S4, the §4 "The populations" rows for lexicon-suffix-waivers, lexicon-verb-waivers, testsuite-count-waivers and agent-cap-restatement-waivers, §4 Files touched and §10. S4 requires every reader in §4's table to read rows through the factory's `read_rows` and grade them through `compare_counts`/`compare_to_base`. A factory copy exists only in tools/lib/ (gov-internal, ships nothing), tools/memory-tree/ and tools/gate-lint/, and the `legacy_ledger_py` row of tools/lib/resolve-python.test.sh's parity table holds the copies identical. Three readers ship to adopters from kits that neither carry a copy nor require a kit that does:
- `tools/lexicon/lexicon.py#load_waivers`: tools/lexicon/kit.toml declares no `requires`. `lexicon.py#check_self_containment` refuses any import that is neither stdlib nor a sibling `.py` ("this kit must install without its neighbours"), and that rule runs on the `lexicon selftest` / `lexicon naming predicates` legs §7 names.
- `tools/check-testsuite-counts.sh`: the entry tools/govkit/entries/check-testsuite-counts.kit.toml has `requires = []`.
- `tools/check-agent-cap-restatement.sh`: its entry has `requires = ["agent-cap"]`. The entry's own note says the gate is green with the waiver file absent or empty in an adopter.

Getting around that rule with a dynamic import or a subprocess call into memory-tree would be working around a gate's refusal. The spec has to choose one of:
- a new inline copy of the `legacy_ledger_py` block, plus the `coverage_join` and `compare_base` blocks and `resolve_kit_dir` it calls, in each such kit, with rows in tools/lib/resolve-python.test.sh (none of these paths is in Files touched);
- a `requires` edge on memory-tree, which is a dependency change;
- a stated exception to S4 for these readers.

(2) S2 and §4 disagree on corpus-path-unresolved.txt's count. S2 says "the count is its count column, else `1`". The file has a count column, `<citing-file> TAB <cited-path> TAB <occurrences> TAB <absent|moved:DEST>`, but §4's table gives Count `1`. Its reader grades that column: tools/memory-tree/corpus_ids.py check 15 rule 1 prints "occurs N time(s), row says {count}", and S4 keeps that message. The same reader also grades the `absent|moved:DEST` column, which §4 "Field names" sends to the conversion record: rule 4's "destination ... is not a tracked file" / "is a directory, not a file", and "state '...' is neither 'absent' nor 'moved:<dest>'". S4's list of retiring messages names none of them. This is F12's class, a graded field that is neither key nor count. The spec has to say what the count is and what happens to those refusals.

(3) transition-audit.txt rows are `<sha> accounted`, and §4 keys them `record · sha`. tools/memory-tree/transition_audit.py#print_registry refuses a pinned row whose second field is not `accounted` ("the only verdict a pinned row may carry is `accounted`"). That field leaves the row, and S4 neither keeps nor retires the message.

(4) S2 says every row is `seeded` "at the build run's base SHA" (RUN.md's base is 9e21ac76). S10 says `convert --home` converts "at the repository's HEAD", and gov's own conversion runs `convert`, so its rows would carry HEAD's sha. The spec should name a `--sha` for `convert` or say which sha holds.

(5) tools/run-gates/owed_rows.py#derive_owed_rows also reads spawn-idiom-sites.txt, testsuite-count-waivers.txt and unarmed-branches.txt by their first column, for the path-deleted population. Its FIXTURE plants a legacy unarmed-branches row at line 282. §4's table does not name owed_rows as a reader of those three, and S6 cites it only for baseline.toml, so S4's "every reader" leaves it out.

(6) memory/map/affordance-exempt.toml holds `exempt = []` at HEAD and at c52a74c4d. That makes it an eighth home with no row. S2's general rule writes it unarmed, but F14 and AC13 pin seven homes. F10's adopter seed, via `seed --home` with `--out` writing the ledger grammar, writes a header-only armed home wherever an adopter's list is empty, and `ratchet (populated)` reds that home.

Nothing was written or committed. The tree is clean at f294dafda. The `--brief` verb reported the brief already recorded and unchanged at ce2fc79546f0, and wrote nothing.

## Summary

I didn't build TOOL-dWitnessedBar-16: spec rev-11 can't be built as written, so I stopped before writing any code. Nothing is committed, and the tree is clean at base f294dafda60b8ad68560416402724d09f7686339.

**The blocker:** S4 requires every reader in §4's table to read through the ledger factory. Three of those readers ship to adopters from kits that neither carry a copy of the factory nor require a kit that does:
- `tools/lexicon/lexicon.py`: the lexicon kit declares no dependency, and its own gate refuses any import from outside the kit.
- `tools/check-testsuite-counts.sh`: its entry has `requires = []`.
- `tools/check-agent-cap-restatement.sh`: its entry requires only agent-cap.

The spec has to pick a route: a new copy of the factory in each kit, with its parity rows; a dependency on memory-tree; or a stated exception for these readers. The `why` field has the detail.

**Two more conflicts:**
- **corpus-path-unresolved.txt:** S2 says the count is the count column, but §4's table says 1. Its reader in `corpus_ids.py` grades that count, and it also grades the column §4 sends to the conversion record. S4 neither keeps nor retires those messages.
- **transition-audit.txt:** the reader refuses a row whose second field isn't `accounted`, and that field leaves the row.

**Smaller gaps, reported now so this unit doesn't stop over them next time:**
- S2 wants rows stamped at the run's base sha (9e21ac76), while S10's `convert` stamps the repository's HEAD.
- `owed_rows.py` reads three of the converted lists that §4 doesn't name it as reading.
- `memory/map/affordance-exempt.toml` is empty, which makes it an eighth home with no rows; F14 and AC13 pin seven.

**What I checked (reading the code only):**
- Every symbol the spec cites in the readers, the factory, `ratchet.py`, `upgrade_steps.py` and the drift settings: all present, except as listed above.
- The header and rows of each of the 29 lists, and the field counts of the multi-field ones.
- A search across `tools/` for every reader of each list.
- Where the factory copies live, and each kit's and entry's `requires`.

These reads stand in for no gate. No gate, suite or bar ran, and nothing timed out or was skipped.

**Not done:**
- `gotchas.py --for-diff` didn't run, because there is no commit.
- I didn't write the converted `readme-contract.txt` to `C:/Users/d41ly/AppData/Local/Temp/claude/06f17fbb3b45b392/0a586af7-47fb-45dc-b963-7ee82521f7da/scratchpad/readme-contract.converted.txt`, because the conversion never started.
- The spec's status stays INPROGRESS.
- Every §7 leg and both `New arm:` red-first checks are still owed at the close once the unit is built: `tools/drift-audit/selftest.py` for AC7 and AC8, and `tools/memory-tree/ratchet.py`'s `regrammared` case for AC12.
