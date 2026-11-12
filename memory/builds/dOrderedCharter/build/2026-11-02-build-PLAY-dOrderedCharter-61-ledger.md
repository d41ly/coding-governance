# PLAY-dOrderedCharter-61 — acceptance ledger

**Serves:** journal PLAY-dOrderedCharter-61

Each line is a probe this pass ran in the worktree or under the run's scratch path, and what it
printed. The check's plain run is the layer leg, which a role agent may not run, so every reading of
the tree below is `check_layers.py --list`, whose summary and not-read line are the plain run's. The
leg itself, the plant table in `adopt-playbook.sh --selftest` and both `New arm:` lines' RED-first
observations are the main loop's at the close.

**Evidences:** PLAY-dOrderedCharter-61
- AC1 — `check_layers.py --list` — exit 1, `12 layer row(s), 30 kit descriptor(s); edges by kind: import 1 · dynamic 0 · probe 33 · copy 5 · shell 0 · requires-if 1; 0 allowed, 40 red; 0 contract red(s)`, and no `layers: edge` line names a site of section 4's table; no `read line by line` line, since no core shell file's quoting is unbalanced
- AC2 — `diff` — the `layers: edge` lines of `check_layers.py --list` saved before the first edit (60, at `ebb0ebfe`) against those after the pass (40): 21 removed, exactly section 4's table (`.githooks/pre-push.test.sh:2279`, `:2281`, `:2573`, `:2584`; `.githooks/pre_push_bar_selftest.py:180`; `skills/session-kickoff/manifest-check.test.sh:1918`; `tools/memory-tree/check-memory-hygiene.sh:1288`; `tools/playbook/check_layers.py:118`, `:129`; `tools/push-main.test.sh:1270`, `:1286`, `:1464`, `:1550`, `:1553`, `:1555`, `:1556`, `:1582`; `tools/unattended/unattended.sh:12194`; `tools/unattended/unattended.test.sh:1540`, `:1558`, `:16434`), one added, `tools/check-wiring.sh:1101`
- AC3 — `--fixture --plant quoted` — exit 1, `RED tools/corekit/run.sh:6 · probe · core kit corekit depends on non-core kit expkit` (the bare `expkit` in `"$(resolve_receipt_path expkit)"`) and `0 allowed, 1 red`; `run.sh:4`, the message opening a quote it closes on `:5`, is no edge; a scratch fixture whose `run.sh` ends inside a quote printed `layers: tools/corekit/run.sh read line by line: its quoting does not balance` and still read the line's bare `expkit` as an edge
- AC4 — `--fixture --plant unshipped` — exit 1, `RED tools/corekit/core.py:9 · probe · core kit corekit depends on non-core kit mapkit` ("mapkit/reader.py") and `0 allowed, 1 red`; `core.py:10`, `os.path.join(root, ".git", "mapkit", "journal.log")`, and `core.py:11`, the id "mapkit/planted-id", are no edge; the thirteen earlier plants each printed their table row's exit and line through the same build
- AC5 — `python -c "import json; ..."` — printed `[['{prefix}/playbook/', '{prefix}/memory-tree/import_walk.py', '{prefix}/memory-tree/check-arms.py', '{prefix}/memory-tree/tree_lib.py']]`; `memory/guides/SESSION-KICKOFF.md`, its `last-audit` re-stamped, is staged in this pass commit beside `tools/gate-legs.json`
- AC6 — `layers: not read:` — `--list` printed `layers: not read: a path computed at run time, JavaScript, a file no descriptor claims, a path that names no file the kit ships, and a bare kit name inside a string or a here-document`, the one `NOT_READ` constant the plain run prints too; `grep -n "names no file the kit ships" tools/playbook/README.md` printed line 183 of the layer section
