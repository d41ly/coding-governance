# Acceptance ledger — TOOL-aCarriedStop-10

**Serves:** journal TOOL-aCarriedStop-10

Built against spec rev-1 in one pass commit, on node a. AC3 to AC5 are the criteria's own commands over the worktree with S1 and S2 in place, before the commit. No suite, gate leg or bar ran in the pass: the brief's `bash tools/check-install-prefix.sh` was tried once and the role gate refused it to the builder as the `install-prefix (shipped surface)` leg. Owed to the main loop at the close: AC1 green at the pass commit, AC2 red at its parent, and the legs of the spec's Gates section.

**Evidences:** TOOL-aCarriedStop-10
- AC1 — `bash tools/check-install-prefix.sh` — not run in the pass: the role gate refused this argv to the builder as the `install-prefix (shipped surface)` leg. The exit 0 at the pass commit, with no line of `tools/chain-packet.py` or `tools/chain-packet.test.sh` listed, is owed to the main loop at the close.
- AC2 — `bash tools/check-install-prefix.sh` — not run in the pass, as AC1. The exit 1 in a scratch clone detached at the pass commit's parent, listing `tools/chain-packet.py@dc026a49:239`, `tools/chain-packet.py@dc026a49:245` and `tools/chain-packet.test.sh@d3447869:405`, is owed to the main loop at the close.
- AC3 — `grep -c '"memory-tree"' tools/chain-packet.test.sh` — it printed `0`; `grep -n '"memory-tree"' tools/chain-packet.py` printed the one line `120:    KIT_DIR = resolve_kit_dir("memory-tree", "tree_lib.py", HERE)`; and the `diff` of the two `resolve_kit_dir` blocks printed nothing and exited 0.
- AC4 — `python -c` — the criterion's probe loading `tools/chain-packet.py` as a module printed `tools/memory-tree` for `KIT_DIR.relative_to(HERE.parent)`.
- AC5 — `chain-packet.py --check x` — the door copied alone into a `mktemp -d` folder, run from a sibling repo over the stub instrument, printed on stderr the one line `chain-packet: shortcuts off, running the instrument as it stands — packet: blob 6bcb6f4b0b1e, read against cab3bff165a1; carries: no file; schedule: no file; tree_lib.py is not beside this script`, on stdout `stub ran ['--check', 'x']`, and exited 1.
