**Serves:** journal TOOL-dDeclaredLoop-25

# Builder return — TOOL-dDeclaredLoop-25, dispatch 1: the gov-rename plant is refused by check_program before any re-point runs

## Why

DIVERGENCE: rev-5's gov-rename case can't pass the way the spec builds it. Two places conflict: S3 with §4 "The frame rules" row 8, and §4 "The fixture cases" row `gov-rename` with AC6.

The conflict:
- S3 says `check_splices(stages, data, exclude, records, items)` reads gov's steps from the `data` it is given, and that "a plant may pass a definition holding a successor's tag".
- Frame rule 8 says an `item.adopter.<stage>.<name>` that no stage row declares is "refused by check_program", inside `check_splices`.
- `tools/loop/loop_lib.py#check_program` calls `check_loop(data, where)` first. That function only admits the tags in `tools/loop/loop_lib.py#STEP_TAGS`.
- So the `gov-rename` plant, which renames `step.test` to `step.verify` in the planted steps, is refused by rule 8 before any re-point runs. It exits 1, where AC6 needs exit 0.

Probe that shows it: `python -c` in tools/loop/, on the working definition with step.test retagged step.verify, calling `check_program(p, w, None)`. It raised `LoopError: loop.toml: step row 'step.verify' names no gov step; the gov steps are step.plan step.design step.build step.test step.deploy`.

A plant can't make this hold in memory. Renaming the step means changing STEP_TAGS, which is a code constant. `check_program` also ties every item tag's second segment to STEP_TAGS. A real rename would therefore have to rename every `item.test.*` row and the transition rows as well, which is not what the planted case says.

The spec would have to pick one of these:
- (a) Invert the `gov-rename` plant: keep the shipped definition, set the stage's `after` to an old tag (for example `step.verify`), and plant a change record with `Unit step.verify` and `Successor step.test`. AC6's wording (one line naming `step.adopter.security-review`, `step.test` and `step.verify`, with R1 leaving `testing`) holds as written. The `check_splices` signature and every rule stay the same. This is the smallest change.
- (b) Give `check_splices` a separate definition as `check_loop` holds it for rule 8's `check_program`, apart from the `data` that rules 3 to 5 and S4 read.
- (c) Let `check_program` skip `check_loop` for a caller that has already checked the steps. That is a wider change to a function that three other callers use.

No other check failed. Everything else I checked held: kinds.toml `kind.stage`, the core-pending row, `core.py#run_new` and `#check_kind_row`, overlay_rows `#read_kind_source`, `#read_kind_schema` and `#check_row_owners`, the absence of a `stage` namespace source, the build rows B4/B5/B7/B12 and Deploy's `closed` exit, loop_table `ROW_KEYS`, `loop_parents#read_policy_kit`, `build_records#read_changes`, `design_lib#derive_pin_hash`, `pins#read_change_successors`, step_gate's class-row arming in `govkit/selftest.py#check_step_gate_fixture`, and the lexicon suggest verb for every planned name. SHARED_RECORDS and REFUSAL_CEILINGS are not reached, since this unit touches no .sh file.

## Summary

I committed nothing and changed nothing in the worktree, so there was nothing to restore and no patch file. I did not run --dispatch or --brief: RUN.md already holds this unit's brief row at 2026-11-15T18:45:59Z, and a divergence leaves no write set to declare.

What ran:
- The spec's claims about current code, checked against the tree with greps and reads.
- A `python -c` probe of `loop_lib.check_program` on the working definition with step.test retagged step.verify. It raised LoopError, which is the divergence. No gate stands behind this probe; it shows that AC6's `gov-rename` case would exit 1 instead of 0.
- `tools/lexicon/lexicon.py --suggest` for every function name I planned. All returned OK, which stands in for the `lexicon naming predicates` leg on those names.

What did not run:
- `govkit.py epoch`, the kit epoch probe. The scratch-guard hook refused it as the `kit epoch` leg, so it is owed to the close.
- The playbook kit's shipped bytes have moved since the merge-base 0578adb7 and its version is still 1.38 (origin/main has 1.39). The brief puts the bump once, after the last move, so it is owed at the close.

Notes for the build after the spec is revised:
- Every section 7 leg, the `core kinds` and `core meta-check` exits behind AC11, the `step_gate.py --fixture --plant stage` run behind AC5, and both `New arm:` lines' RED-first observations go to the close.
- The new leg's budget row can only be a proxy figure, as for unit 6, because a pass can't run `--selftest`.
- I expect the commit to rewrite these companion files, so declare them up front: memory/builds/dDeclaredLoop/README.md, RUN.md, the spec, the acceptance ledger, memory/LIVE.md, memory/backlog/TOOL.md, the four memory/map/generated files, memory/guides/SESSION-KICKOFF.md for the manifest-audit stamp, and help/reference/kinds.md.

gotchas.py --for-diff was not run because there is no commit to run it over.

Paths:
- C:/projects/coding-governance/.claude/worktrees/unattended-declared-loop-d56bf0/memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-25.md
- C:/projects/coding-governance/.claude/worktrees/unattended-declared-loop-d56bf0/tools/loop/loop_lib.py
