# TOOL-dTrueNorth-1 — acceptance ledger

**Serves:** journal TOOL-dTrueNorth-1

No merge bar, no gate leg and no self-test suite ran in this pass. Every criterion was observed by a
probe of the new module: its own CLI over scratch fixtures written under the run's scratchpad, a
`python -c` or scratch-script import of the module over the real tree, a fixture repository and a
scratch clone of this worktree under the user temp directory, short-named, with the uncommitted
module and conf copied in. No suite arm lands with this unit (spec section 7): the parser's first
gated caller is `TOOL-dTrueNorth-2`'s join. The gates spec section 7 names are owed to the close.

**Evidences:** TOOL-dTrueNorth-1
- AC1 — `**Carries:**` — `design_lib.py --parse` over a scratch spec whose only line 1 is the clause
  carried at `83b6b11` exited 1 and printed `a1-bad.md:1:`, the line, and the `**Carries:**` grammar
  it fails. With the digit restored it exited 0 and printed `kind=carries line=1
  clause=cl-dClosedLoop-0001 hash=83b6b117 part=whole`.
- AC2 — `part 3/2` — one `--parse` run over a scratch spec holding a `part 3/2` carry, a `**Moved:**`
  line with no `to <build>`, a `**Retired:**` line naming `dGroundRules` and a `**Derived:**` line
  naming `none` exited 1 and named `a2.md:3`, `a2.md:4`, `a2.md:5` and `a2.md:6`, each with its line
  and the grammar or tightening it fails.
- AC3 — `node:record-kind.deviation` — `--parse` over a scratch spec carrying a whole carry, a
  `part 1/2` carry, `node:record-kind.deviation`, `**Derived:** PLAY-dClosedLoop-2` and one each of
  moved, retired and deferred exited 0 and printed seven bindings, each naming `kind`, `line`,
  `clause`, `hash`, `part`, `node`, `decision` and `to`. A scratch probe calling
  `parse_binding_lines` with `strict=False` on that text with AC1's malformed line appended returned
  the same seven bindings, equal as dicts, and raised nothing; the strict call on it raised naming
  line 12.
- AC4 — `--parse` — a scratch spec whose malformed `**Carries:**` line sits inside a closed fence
  exited 0 and printed `0 binding(s)`. The same line under a fence left open exited 1 and printed
  `a4-open.md:3: a fence opens here and never closes`, the fence's line.
- AC5 — `derive_clause_hash` — `design_lib.py --design` over the tree exited 0 and printed `509
  clause(s) across 22 build(s) · 0 withdrawn · 524 owned node(s)` in 0.6 s. A scratch probe loading
  `carries.py` and calling its `design()` found the same 509 ids in the same 22 builds and 0 rows
  whose `derive_clause_hash` differs from the instrument's hash, and 0 whose `extract_clause_tokens`
  differs from its tokens. Liveness: a hash taken with the id still on differs on 509 of 509 rows,
  and a planted double space moves an unfolded hash and not the folded one.
- AC6 — `--design --build dTrueNorth` — exited 0 and printed `cl-dClosedLoop-0001 83b6b117 baseline`
  through `cl-dClosedLoop-0006 06ceb3cc baseline`, the six hashes the packet's Items list gives, and
  `node record-kind.deviation`. A scratch copy of the view with row 10's id respelled
  `cl-dClosedLoop-0001`, given to `read_design_view`, raised `DesignRefusal` naming
  `cl-dClosedLoop-0001 repeats the row at line 9`. A `--build dNoSuch` exited 1 naming no chain build.
- AC7 — `read_retired_ids` — a fixture repository whose record lists `cl-dProbe-0002` after
  `Retired:` in its `[clause-ids]` section at the baseline commit, and `Retired: none.` in a later
  commit and the working tree, returned `['cl-dProbe-0002']` at the baseline and `[]` at HEAD; an id
  in the section after `[clause-ids]` was not read. Over the real tree it returned `set()`. A
  baseline of forty zeros raised `DesignRefusal` naming `DESIGN_BASELINE ... names no commit`, and a
  record absent at the baseline raised naming `DESIGN_RECORD`.
- AC8 — `read_owned_nodes` — `--design --build dTrueNorth` printed `node record-kind.deviation`, and
  the AC5 probe found `read_owned_nodes`'s set equal to `carries.py`'s `design()` nodes for all 22
  chain builds, 524 against 524. With `DESIGN_NODES` naming an untracked scratch `.py` file,
  `read_design` raised `DESIGN_NODES names ... which is not a tracked file`; naming a missing path and
  a `.md` file each raised naming the key. In the scratch clone, tracked derivers that raise in
  `derive()`, call `sys.exit` on load, or declare no `OWNED` each exited 1 naming `DESIGN_NODES`, and
  the deriver load wrote no `__pycache__` beside it.
- AC9 — `design_lib.py --chain-specs 2026-10-21` — in a scratch clone it printed `chain specs 20 in 1
  build(s) · passed over: other-build 1364, pre-cutoff 0, undated 0`. With a planted spec under the
  non-chain `dProbeOther`, one under chain build `dGroundRules` dated 2026-10-20, an undated file and
  a nested dated spec under dTrueNorth's `spec/`, all tracked, it listed dTrueNorth's specs only, the
  nested one included, and printed `other-build 1365, pre-cutoff 1, undated 1`. A cutoff of
  `2026-13-45` exited 1.
- AC10 — `read_cutoff_key` — the AC's grep over `.memory-tree.conf` printed the five keys at lines
  984 to 988 with the values S1 names. A probe loading `tools/check-spec-tokens.py` and calling
  `read_cutoff_key` on `SPEC_CARRIES_CUTOFF` returned `2026-10-21`. `grep -c DESIGN_` over
  `tools/memory-tree/.memory-tree.conf.example` printed 0.
- AC11 — `DESIGN_VIEW` — in the scratch clone with `DESIGN_VIEW` blanked, `--design` and
  `--chain-specs` each exited 2 printing `DESIGN_VIEW is blank, so nothing was read`. With all four
  keys blank, and again with all four absent, `--design` exited 2 printing `every DESIGN_* key is
  blank ... so nothing was read`. Restored, it exited 0.
