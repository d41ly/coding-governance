# TOOL-dWitnessedBar-10 deviation 101 — the shell ledgers this unit's shell edits move, lowered and widened

**Serves:** deviation TOOL-dWitnessedBar-10

- **Departs from:** `TOOL-dWitnessedBar-10@rev-5 [S3 S4]`
- **Hand-off:** spec-to-code
- **Before:** the spec's Files touched names no `memory/project/` ledger. S3 adds the `--precommit` arm to `tools/run-gates/run-gates.sh`, S4 retires three hand-named blocks from `.githooks/pre-commit` and their arms from `.githooks/pre-commit.test.sh`, S1 adds an arm-1a control pair to `tools/run-gates/run-gates.test.sh`, and §7 declares a new arm in `tools/run-gates/run-gates.evidence.test.sh`.
- **After:** `memory/project/shell-role.txt` lowers `.githooks/pre-commit` 257 -> 213 and `.githooks/pre-commit.test.sh` 277 -> 243, and widens `tools/run-gates/run-gates.sh` 3397 -> 3398, `tools/run-gates/run-gates.test.sh` 3036 -> 3044 and `tools/run-gates/run-gates.evidence.test.sh` 2145 -> 2188, each widened row stamped with the pass base and `widened:` this record; `memory/project/quoting-sites.txt` lowers `.githooks/pre-commit.test.sh heredoc-source` 2 -> 1; `memory/project/spawn-idiom-sites.txt` lowers `.githooks/pre-commit var-pipe` 4 -> 3. Every count is `sh_hygiene.py`'s own measure of the working tree, and the spawn-idiom count its scan over an empty registry.
- **Cause:** builder discovery
- **Reason:** TOOL-dWitnessedBar-24 landed the shell-role and quoting ledgers after this spec's base, graded `shrink-only` with `drain hunk`: a file that shrank reds `count fell` until its row is lowered in the same commit, and a grown file reds unless its row is widened with a record. The growth is the spec's own: one dispatch arm the runner must carry for S3, an arm-1a control pair S1 owes, and the §7 evidence arm in the shell suite the spec names. None of it moves to Python without contradicting the spec's named paths. The new shell lines avoid every spawn idiom (`$(<f)` for a read, `[[ ]]` for a match), so no spawn-idiom row grows.
- **Evidence:** `python tools/gate-lint/sh_hygiene.py --shell-role --measure . <the five files>` and `--quoting --measure`, run at the pass; the README of `tools/gate-lint/` on the widen route; the widened rows of `memory/project/unbound-records.txt`, which a TOOL-dWitnessedBar-17 builder record carries.
- **Risk:** loosening
- **Approver:** author, the gov-builder pass of the unattended run, under the build README's `author-recorded` value
- **Follow-through:** none
- **Caused-by:** PLAY-dClosedLoop-2
