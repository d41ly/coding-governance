**Serves:** journal TOOL-dTotalRecall-55
**Caused-by:** TOOL-dTotalRecall-55

# TOOL-dTotalRecall-55 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `b9f735339` from [2026-11-23-prompt-TOOL-dTotalRecall-55-build-brief](../prompts/2026-11-23-prompt-TOOL-dTotalRecall-55-build-brief.md), recorded whole; the pass tip is `5b5895a49`.

## Why

TOOL-dTotalRecall-55 is built from spec rev-5 as written. Every claim the spec makes about the code held when probed against base b9f735339: the eight CAUSE_WRITER_KEPT rows, KEPT_PINNED and KEPT_OUTSIDE as their only readers, read_build_code_paths, the pinned seam, tree_lib.BIND_HEAD_LINES imported by both censuses, the census count line `9 census file(s) · 8 kept · 1 pinned · 0 red`, and the plant suite check-memory-hygiene.test.sh. No divergence. The pass is committed with the spec header set to CLOSED.

## Summary

Built TOOL-dTotalRecall-55 and committed it as 5b5895a49, starting from base b9f735339.

**What changed:**
- **`tools/memory-tree/tree_lib.py`**: adds `CENSUS_KEPT_PATHS`, the eight `check_cause_writers` rows. `asbuilt.py` and `packet.py` carry the reason `pinned instrument` and the other six carry `outside the write set`. It also adds `read_kept_rows(census, table=CENSUS_KEPT_PATHS)`, the table's one reader, and `read_kept_path`, which answers through it (§8 F2 a).
- **`tools/memory-tree/record_causes.py`**:
  - `check_cause_writers` and `run_check` now take `kept` beside `pinned`. The local counter is renamed to `n_kept`, as the brief asked.
  - The build-folder loop keeps a file through `read_kept_path`, and the remedy line now names `CENSUS_KEPT_PATHS`.
  - The new S4 drain: after the loop, a row whose file the walk reads but which spells no Serves literal past its binding window prints `cause-writer · kept row · <path> · red · drained` and adds one red naming `CENSUS_KEPT_PATHS` and the path.
  - `CAUSE_WRITER_KEPT`, `KEPT_PINNED` and `KEPT_OUTSIDE` are removed, along with the docstring and remedy text that named them.
  - New fixture pieces: `KEPT_SCRIPT`, `FIXTURE_KEPT`, and the plant `kept-row-drained`, added to `PLANTS`. Only that plant passes `FIXTURE_KEPT` to `run_check`; every other plant reads the default table.
- **`tools/memory-tree/check-memory-hygiene.test.sh`**: the new arm. It expects exit 1, the drained line, the named red, and exactly one `RED ` line.
- **Records and regenerated files in the same commit**: the acceptance ledger `memory/builds/dTotalRecall/build/2026-11-23-build-TOOL-dTotalRecall-55-1-acceptance-ledger.md`; `memory/map/generated/symbols.json` (gen_map); `memory/LIVE.md`, `memory/backlog/TOOL.md`, `memory/builds/dTotalRecall/README.md` and the spec's records table (gen_build_index); `RUN.md`; and the spec header INPROGRESS→CLOSED. No path outside the declared write set was touched.
- **Index side effect:** the index regeneration now shows the dTotalRecall build status and ask TOOL-dTotalRecall-27 as DEFERRED, because no unit is INPROGRESS any more.

**Commit trailers:**
- Two `Decided:` lines. One names the eight rows. The other records a choice the spec left open: a drained row prints before the build-folder count line and is not counted in it, so the count line keeps its shape.
- `Pass: TOOL-dTotalRecall-55` and `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`. I used this co-author line, the one the charter and brief give, not the harness reminder's Opus 5.5 line.

**Checks run (probes of this unit's own CLI only; they stand in for the `memory hygiene` leg and the record-causes plants of the hygiene suite):**
- **AC1:** `python record_causes.py --cause-writers` from `tools/memory-tree/` exited 0. It lists the eight files as `kept` with their reasons and `deviations.py` as `pinned CAUSE_WRITER_PINNED`, still reading `9 census file(s) · 8 kept · 1 pinned · 0 red`; its build-folder lines match the base output exactly. `python record_causes.py --check` exited 0 (green). `git grep -n "CAUSE_WRITER_KEPT\|KEPT_PINNED\|KEPT_OUTSIDE" -- tools` printed nothing.
- **AC2:** `python record_causes.py --fixture --plant kept-row-drained` exited 1 with exactly one red, `cause-writer CENSUS_KEPT_PATHS memory/builds/fRoot/build/2026-01-01-build-TOOL-fRoot-1-kept.py: ...`. All three of the arm's grep strings match the output.
- **Staged break, previewed:** with `tree_lib.read_kept_rows` replaced by an empty reader in a `python -c` probe, the plant exits 0 with no red. That is the break the `New arm:` line names.
- **Neighbouring plants:** `legacy`, `writer-without-cause`, `pinned-writer-drained`, `departures-pinned` and `unmarked-writer` still give their expected exits or PASS.
- **Naming:** `lexicon.py --suggest` printed OK for `read_kept_rows` and `read_kept_path`.
- **Bug-class checklist:** `gotchas.py --for-diff HEAD~1..HEAD` selected 35 anchored classes plus 6 universal. I acted on these:
  - Retired names read by value: a repo-wide grep outside `memory/builds` finds no remaining reader of the retired constants or the old remedy text.
  - Fixture that finds nothing: the plant does fire, and the staged break flips it to exit 0.
  - Grep as a presence probe: AC1's grep is backed by the census output.
  - Ledger token wrapped across a line: each ledger line keeps its backticked token on one line.

**Owed to the close (not run here):**
- The new arm's RED-first observation, in `tools/memory-tree/check-memory-hygiene.test.sh`. Stage the break by skipping S4's drain test, see the plant exit 0 and the arm go red, then restore and see it green.
- Every §7 leg: `memory hygiene`, `lexicon naming predicates`, `recall floor`, `recall floor arms`, `codebase-map coverage + freshness`, `codebase-map kit selftest`, `codebase-map gate coverage` and `codebase-map adopter e2e`. The pre-commit hook already reported `codebase-map coverage + freshness ok` on this commit.

No command hit its time bound and nothing was skipped. The `--brief` verb reported the brief already recorded and unchanged at 64d3b9748a2d.
