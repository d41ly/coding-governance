**Serves:** journal TOOL-dWitnessedBar-16

# TOOL-dWitnessedBar-16 — builder return 1 (run `wf_a23960d3-2d7`), a divergence, nothing committed

## Why

DIVERGENCE: I checked the spec against the code before writing anything (rev-9 at memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-16.md, against tools/lib/legacy_ledger.py and the readers it names). Two places in the spec cannot be built as written.

(1) §4 "The populations", the `memory/project/refusal-retirements.txt` row, conflicts with S4 and AC3. The row keys the population as `record · unit, path, check`, count 1. Its reader is `tools/memory-tree/check-arms.py#check_retirements` (lines 723-765, grammar in tools/memory-tree/README.md:621). Besides the decision id, that reader grades four more fields of every row:
- the R1 to R4 criteria (`lacks its R<k> field`)
- the survivor file (`lacks its survivor field`)
- a join that the survivor file still carries the recorded signature (`names the survivor X, which no longer carries its signature`)
- the replay line (`lacks its replay field`)

The ledger row is key fields, count, sha and disposition, so none of these survive the conversion. S5 only moves "reasons" to the conversion record. That makes S4's "keeping its messages and its exit codes" false for this reader. The survivor join, which is a real gate, quietly goes away, and so do the check-arms selftest cases that plant rows lacking a survivor or a replay (check-arms.py:1617-1633, on the §7 leg `check-arms selftest`). §5 risks does not mention any of this. The spec has to choose one of two things:
- (a) the survivor file, its signature and the replay become key fields, held verbatim, with R1-R4 moved to the record; or
- (b) the survivor join and its four messages are declared retired, with the check-arms arms removed and a §5 risk line saying so.

(2) §4's `memory/project/unarmed-branches.txt` row, with AC10, conflicts with the factory's `_check_table`. The row is `site · gate, check, signature`, and AC10 says one row per `gate, check, signature`. `tools/lib/legacy_ledger.py#_check_table` (lines 137-138) refuses a `site` table whose fields lack `path`, so a header rendered as written (`key site gate,check,signature`) cannot register. Also, the check field of shape-1 rows is a bare integer, which `LINE_NUMBER_RE` refuses unless the registration declares it `verbatim`. The spec has to say either that the gate field is named `path`, or that the key kind is `key`, and that `check` is verbatim. The same field naming should be stated for `corpus-path-unresolved.txt` (`citing path, cited path`) and `trace-waiver.txt` (`spec path, subject`), whose column text cannot be header field names as written. The same is true of fork-ceilings' integer `base` key field, which needs `verbatim`.

Nothing was written or committed. The tree is clean at base 9b69042ee.

## Summary

I stopped before writing any code: the spec for TOOL-dWitnessedBar-16 can't be built as written in two places, so nothing is committed and the unit needs a spec revision before it is dispatched again.

1. **The refusal-retirements row loses data its reader checks.** The spec keys `memory/project/refusal-retirements.txt` by unit, path and check only. Its reader, `check_retirements` in `tools/memory-tree/check-arms.py`, also checks each row's R1–R4 criteria, its survivor file, that the survivor still carries the recorded signature, and its replay line. None of that survives conversion. That contradicts the spec's promise (S4, AC3) that every reader keeps its messages and exit codes. It would also remove the `check-arms selftest` cases that plant rows missing a survivor or replay. The spec writer has two options:
   - (a) keep the survivor file, its signature and the replay as verbatim key fields, and move R1–R4 into the conversion record; or
   - (b) declare that check retired, drop those selftest cases, and add a risk line saying so.

2. **The unarmed-branches row can't register.** The spec names its fields `gate, check, signature` under the `site` key kind. `_check_table` in `tools/lib/legacy_ledger.py` refuses a `site` table with no `path` field. Its check numbers are bare integers, which the factory refuses as line numbers unless they are declared `verbatim`. The spec needs to rename the field to `path` (or use key kind `key`) and mark `check` verbatim. Three other rows need the same treatment:
   - `corpus-path-unresolved.txt` and `trace-waiver.txt`: the column text can't be used as header field names as written.
   - `fork-ceilings.txt`: its integer `base` field needs `verbatim`.

**Checks run:** the spec's claims probed against the source only. I read the ledger factory, `check_retirements` and its selftest cases, the step grammar in `upgrade_steps.py`, `ratchet.py`'s probe and plant functions, the 29 registry headers and their rows, and the list of kits that carry a copy of the factory. No gate, suite or bar ran, and no command timed out or was skipped. None of these reads stands in for a gate; every §7 leg and both `New arm:` RED-first observations are still owed at the close once the unit is rebuilt.

`bash tools/unattended/unattended.sh --brief` reported the brief as already recorded and unchanged at 25468d36ee60, so it wrote nothing. The tree is clean at base 9b69042ee. `gotchas.py --for-diff` was not run because there is no commit. No scratch file was made: `C:/Users/d41ly/AppData/Local/Temp/claude/06f17fbb3b45b392/0a586af7-47fb-45dc-b963-7ee82521f7da/scratchpad/readme-contract.converted.txt` was not written, since the conversion was never started.
