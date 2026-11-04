# PLAY-dOrderedCharter-42 — acceptance ledger

**Serves:** journal PLAY-dOrderedCharter-42

Each line is a probe this pass ran, at rev-5 of the spec, from the worktree root with the pass applied:
a scratch probe script that imports the kit (or a scratch copy of it) in a child python over scratch git
repositories under the host temp directory, the factory's own `--fixture --plant typed-kinds` run, and a
read of the rendered kind list. The legs the spec's section 7 names, the merge bar, and the New arm's
RED-first observation (the round trip red under the base tuple without the three tokens) are the main
loop's at the close.

**Evidences:** PLAY-dOrderedCharter-42
- AC1 — `read_bindings` from `tree_lib` over a scratch repository holding `…-exception-1.md`, `…-override-1.md` and `…-change-1.md` returned each `bound`, its kind its token
- AC2 — with the table as shipped, `set(build_records.KINDS) == set(tree_lib.TYPED_RECORD_KINDS)` printed `True`; importing `build_records` from a scratch copy whose table carries `widget` exited 1 with `ImportError: build_records: the kind table and tree_lib.TYPED_RECORD_KINDS differ on widget`
- AC3 — in the same repository a `<date>-build-<unit id>-change-1.md`-shaped file serving `journal` read `malformed`, `named as a change record, -change-<n>.md in a build/ folder, and its Serves kind is journal, not change`, and `notes.md` serving `exception` read `malformed`, `Serves kind exception, and the file is not named <date>-build-<unit id>-exception-<n>.md in a build's build/ folder`
- AC4 — `python build_records.py --fixture --plant typed-kinds` exited 0, printed one `bound` line per member of `TYPED_RECORD_KINDS` (deviation, exception through `new exception`, override, change) and `build-records: PASS typed-kinds — 4 typed kinds bound, --print-bindings printed no A row`, which it prints only when `--print-bindings` also printed each record's `S` row; `gen_build_index.py --print-bindings` over this worktree printed no `A` row either
- AC5 — a probe of the bullet of `tools/memory-tree/HYGIENE.template.md` opening with the closed `<kind>` list found each of `deviation`, `exception`, `override` and `change` as a backticked kind followed by its half-line, missing none; `adopt-memory-tree.sh --render` re-rendered `memory/HYGIENE.md` from it
- AC6 — `read_bindings` from a scratch copy of `tools/memory-tree/` whose `TYPED_RECORD_KINDS` adds `plan` returned `2026-10-20-build-PLAY-dClosedLoop-1-execution-return-plan-2.md` serving `research` as `bound` `research`, and `notes-deviation-1.md` serving `journal` as `bound`; `deviation_join.read_record` over it named `file name` `is not <date>-build-<unit id>-deviation-<n>.md in a build's build/ folder`
