# TOOL-aRepatriatedFork-12 — acceptance ledger

**Serves:** journal TOOL-aRepatriatedFork-12

Written by the unit pass. The six new arms of `tools/memory-recall/selftest.py` were run as a SLICE:
the suite's prologue, `build_synthetic_log` and the unit's own block, exec'd from a scratchpad
script against the kit. All six passed over the new kit. The same slice run over a scratch kit holding
the HEAD-before-this-unit `recall_conf.py`, `extract.py`, `query.py`, `bench.py` and `union.py`
failed all six. The whole suite did not run, and neither did `test_recall_floor.py`. The close owes
both. The inCMS observation used a `git clone --local --shared` of `C:/projects/incms/main` at
`bc7e95589` under `%TEMP%`, removed afterwards. Nothing was written to inCMS itself.

**Evidences:** TOOL-aRepatriatedFork-12
- AC1 — `extract.DURABLE` — imported at gov's root, it matches memory/archive/architecture/DECISIONS.2026-07-27.md where a7c78ad2's pattern does not, and over `git ls-files memory` it selects 9 files, the same 9 set a7c78ad2's pattern selects
- AC2 — `NODE_TAG_CLASS=a-f` — the slice arm's scratch repo prints it under the key and `NODE_TAG_CLASS=a-z` without it, and `extract.ID_RE` refuses `TOOL-xFoo-3` under `a-f`; `a-f]` and `f-a` exit 2 naming `RECALL_NODE_TAG_CLASS`. The pre-unit kit printed `a-z` and still matched
- AC3 — `RECALL_CITED_FAMILIES="PKG"` — `extract.ID_RE` and `grammar_for(root)` both match `PKG-dCandidLodestar-5`, `extract.DURABLE` does not match memory/backlog/PKG.md and still matches memory/backlog/ARCH.md, and `RECALL_CITED_FAMILIES="ARCH"` exits 2. The pre-unit kit did not match the PKG id
- AC4 — `query.build_cutoff("a")` — returns `163` under `RECALL_BUILD_QID_CUTOFF="a:163"`, `build_cutoff("b")` returns `0`, and `"a163"` exits 2 naming the key. The pre-unit kit returned `0 0`
- AC5 — `RECALL_EXPORT_DIR="memory/archive/project"` — `query.py --export --tag a` writes recall-traffic-a.md under that directory with a header saying it is inside the worktree. `"../out"` exits 2 and writes neither there nor under the git dir, and absent writes under the common git dir. The pre-unit kit ignored the key
- AC6 — `CONF_DIGEST` — `recall_conf.py` prints a different digest when `RECALL_NODE_TAG_CLASS` or `RECALL_CITED_FAMILIES` is added, and the base digest when `RECALL_BUILD_QID_CUTOFF` or `RECALL_EXPORT_DIR` is added. The pre-unit kit printed one digest for all five confs
- AC7 — `bash tools/check-kit-versions.sh` — exits 0 with `KIT_MEMORY_RECALL_VERSION = "1.12"` (spec rev-3), and the README grep for the old denial prints nothing
- AC8 — `corpus_ids.py --check ids` — in the inCMS clone holding gov's three recall files, gov's `check-wiring.sh` and the five S8 conf lines, `recall_conf.py` prints `NODE_TAG_CLASS=a-f`. The check exits 0, its output is byte-identical to inCMS's own files' run, and it has no `PKG-*` row and no `ARCH-xFoo-3` row. The sieve classes `PERF-aSwiftHourglass-2` as `grammar` (§8 F3). With a7c78ad2's three files it exits 1 with 28 `PKG-` lines, the `ARCH-xFoo-3` orphan and the `glossed` mismatch
