**Serves:** journal TOOL-dDeclaredLoop-79

# Builder return — TOOL-dDeclaredLoop-79, dispatch 1: the gained prune's D-to-E update cannot exit 0, because the step reader refuses the descriptor E takes out

## Why

DIVERGENCE: the §4 "The gained prune" table, and AC19, which owes the three updates "as §4 tables them", owe exit 0 for the D-to-E update. The landed update cannot exit 0 there. E takes extra's descriptor out while the registry still names it. Any read-only `update --to E` reaches `tools/govkit/upgrade_steps.py#read_steps` at to_commit, through `derive_pending_steps` in `tools/govkit/govkit.py#_cmd_update`, after the prune. read_steps refuses `<prefix>/extra/kit.toml: the registry names this descriptor for 'extra' and it is absent at <E>`, exit 2, whether or not extra is gained.

What I observed with S19 built as written, in a scratch gov under %TEMP%: the A-to-B update exits 0 and prints `default-gained extra NOT installed`, with no `update would leave`. The B-to-D update exits 0 and prints `would gain extra`. The D-to-E update prints `govkit update — default-gained extra NOT installed: its requires are unknown at d770963b: tools/extra/kit.toml does not resolve at d770963b`. It then refuses with the line above, rc 2.

The spec needs one of two changes:
- (a) The D-to-E row owes exit 2: the prune's NOT installed line printed, then the step reader's refusal naming extra's absent descriptor. The arm grades that line and that refusal, and never `update would leave` or `'extra' requires are unknown`.
- (b) E is staged some other way: one where read_requires_at answers unknown and read_steps at to_commit does not refuse. I found no such staging; an unparseable descriptor is likely refused by read_steps too.

Two smaller findings for the same revision:
1. In "The driver-conf subshell" sketch, ROOT=$2 is set before the unset loop. The prose says the names are unset before ROOT and CONF are set, so a request naming ROOT would unset the driver's ROOT. I built it by the prose, holding $2 in a private name and setting ROOT and CONF after the loop. The sketch should match the prose.
2. Two sweep figures are stale, which a deviation record could carry: the `loop guard fixtures` budget row reads 95 at HEAD, not 90. `memory/project/positional-refs.txt` holds 1 row of this spec at HEAD, not 16.

Every other item was built and observed holding (see summary). Nothing was committed. The product edits are saved as a patch at C:/Users/DAILY-~1/AppData/Local/Temp/claude/b120d4a7f8b5be2e/7c85732c-fa0c-43e9-83f2-238d293195e0/scratchpad/TOOL-dDeclaredLoop-79-divergence.patch, and every product path is restored.

One change is left staged in the index: the dispatch row that `--dispatch` wrote into memory/builds/dDeclaredLoop/RUN.md. That is the verb's own record of the declaration (two lines); I did not edit it by hand and left it in place.

## Summary

Nothing committed: this is a divergence report. Base is c7cb43a96. The brief was already recorded (`--brief` answered `already recorded, unchanged`). `--dispatch` declared the full write set and admitted it (2m20s run). Its row sits staged in memory/builds/dDeclaredLoop/RUN.md, the only change left in the tree.

Sweep re-run at HEAD:
- Design claims held: kit.toml `requires = ["memory-tree"]`; one `resolve_kit_dir("run-gates"` reach; no `--kits` selection names roles, loop or unattended except 57's arms; manifest ceilings 300 and 120; lexicon offender pin 1215; pass commits bbcbb2bab and 6a946400b; 14 manifest keys; no watched kickoff path is touched; SHARED_RECORDS is not written; no shell file is edited.
- Stale figures: the guard budget row reads 95, not 90, and this spec has 1 positional row, not 16.

Built, then saved to the patch and restored. Each item below was probed directly, with no gate, suite or bar:
- S1/S2: `python -c` over `read_driver_conf` with MEMORY_ROOT=elsewhere exported answers `{}` (AC1). The `${ROOT##*/}` / `${CONF##*/}` conf answers `ac2-records` and `.unattended.conf` (AC2).
- S3: the `tree leak` case and its environment set and restored. Run directly in a scratch tree with both names exported, `loop_table.py phase --from BOGUS` printed `refused — phase BOGUS: no row`, rc 1. `resolve_memory_root` printed `memory` (AC3's probe half).
- S4: the `requires` edge, the kit.toml comment, the help sentence and `_dl_claim` gaining run-gates. `derive_unsatisfied_requires(["loop"], ...)` lists `('loop','run-gates')`, the default selection stays `[]`, and the help grep counts 1 (AC4).
- S7: `loop_witness.py --fixture --plant sed-fails` PASS, raising `witness: normaliser unavailable — sed: exit 5`, with 1 worktree and rerun exit 1. `normaliser-missing` still PASS. Both docs name the plant (AC7).
- S13: one `Leg-row keys:` line; a key-diff probe printed `[]` (AC13).
- S19: A-to-B and B-to-D held; D-to-E diverges (see why).
- S20/S25: `trailing-slash-agree` and `no-confs` held (AC20, AC25). `no-own-conf-read` still held.
- S21: url-forms shows both https rows `equal` and the plant `held` (AC21).
- S22: the docstring probe found `merge-tree`, `per two-parent merge`, a time in ms (23 ms PINNED, the median of 10 merge-tree runs, measured 2026-11-17 on node d) and its date (AC22).
- S23: `push-merge-equal-to-every-parent` printed `merge-tree runs: 0`, all held, rc 0. `push-merge-revert-to-unchanged-side` was all held, rc 1 (AC23).
- Naming: the lexicon's `--suggest` answered OK for check_gained_prune_vintage.

Owed to the close, which runs once the unit is re-dispatched:
- AC10 and S10: the pass-commit legs at 8 PINNED commits, which are gate runs.
- AC3's `check --selftest`, and the 57 and 73 govkit arms under the new `_dl_claim`.
- Every section 7 leg.
- RED-first observation of the six `New arm:` lines.

Nothing was skipped or timed out. The gotchas check was not run, because there is no commit to run it over.
