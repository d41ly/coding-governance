# TOOL-aRepatriatedFork-9 — acceptance ledger

**Serves:** journal TOOL-aRepatriatedFork-9

One unit pass under the mandate. It ran no merge bar and no self-test suite. Every criterion below
was observed by a direct run: a module's own `--selftest` flag, one engine run over a fixture tree,
a module function called on the live tree, or the version gate. Each red case was observed against
the bytes this build started from, or against a copy carrying one staged break.

## The fixtures

- **Young tree**: a hand-built memory tree under `%TEMP%/rg9/young`, the same shape as the young-tree
  arm in `check-memory-hygiene.test.sh`: one empty `ARCH` shard and no backlog-row pin declared. The
  kit was copied beside it, once as built and once with check 20's block reverted to print on failure
  only.
- **Base bytes**: `row_grammar.py` and `check-arms.py` as HEAD e6573b75 held them, which is identical
  to BASE for both. NicoCares' `scripts/row_grammar.py` at 14b9fb7a is the red case for the two
  grammar corrections.
- **Adopter clones**: `git clone --shared` of NicoCares at 14b9fb7a and `git clone --local --shared`
  of inCMS at bc7e95589, both under `%TEMP%`, with gov's three files copied over their `scripts/`
  and restored after. Neither real tree was written.

**Evidences:** TOOL-aRepatriatedFork-9
- AC1 — `python3 tools/memory-tree/row_grammar.py --check` — with the young tree's tracked shard deleted from disk it exited 1 naming `memory/backlog/ARCH.md` as tracked but not on disk; the base bytes raised `FileNotFoundError`
- AC2 — `python3 tools/memory-tree/row_grammar.py --report` — a shard holding `- ABL-015 · OPEN · body` reported `live=1 terminal=0 unkeyed=0 rows=1`; NicoCares' module reported `rows=0` and its floor fired
- AC3 — `parse_row` — `- ARCH-tOne-1 · CLOSED by deletion (ARCH-tTwo-1) · a body` returned status `CLOSED`, `live` False and `closed_by` `deletion`; NicoCares' module returned `None`
- AC4 — `bash tools/memory-tree/check-memory-hygiene.sh` — over the young tree it exited 0 and printed `NOT MEASURED` naming `memory/backlog/ARCH.md` for `LIVE_ROW_PIN`; with check 20's block reverted the same run printed no such line. `--emit-pin` printed one `LIVE_ROW_PIN=` line on gov's tree and NicoCares' printed none
- AC5 — `python3 tools/memory-tree/row_grammar.py --selftest` — the edited-in-place row reported its mint date `2026-01-01`, a families list matching nothing raised the vacuity `Problem`, and a copy with `-m` dropped from the walk failed the merge arm
- AC6 — `python3 tools/memory-tree/check-arms.py --check` — with `ARMS_FLOORS=""` over gov's tree it exited 1 with the empty-floors refusal naming the derived module path; the base bytes exited 0. `--emit-floors` printed one token per discovered gate, and the selftest's one-gate fixture printed exactly `ARMS_FLOORS="tools/gate-b.sh:1:1"`
- AC7 — `--selftest` — `row_grammar.py` and `check-arms.py` copied beside inCMS's own `corpus_ids.py`, which defines no `parse_conf`, both passed. The base bytes beside it died on import. The selftest's shell cross-reader arm could not run there, because no hygiene script sat beside the copy
- AC8 — `python3 tools/memory-tree/row_grammar.py --selftest` — the import-graph arm read `hits=[]` over the kit's 7 modules and named the staged re-import. In a kit copy with `from corpus_ids import parse_conf` appended to `gotchas.py`, the arm failed and the scan named `('gotchas.py', 659, 'corpus_ids')`
- AC9 — `bash tools/check-kit-versions.sh` — it exited 0 at 2.88. With the `SPEC-TEMPLATE.template.md` marker put back to 2.87 it reported one problem naming that file. `tools/memory-tree/.memory-tree.conf.example` carries `ARMS_FLOORS`, `LIVE_ROW_PIN` and `SEVERITY_UNLABELLED_PIN`, each with its blank meaning

## At the adopters

NicoCares ran gov's three files verbatim. `row_grammar.py --check`, `--report` and `--ages` gave the
same output as its own fork, and so did `check-arms.py --check`. Its `check_closed_build_rows.py`
and `check_core_ask_closures.py` also ran unchanged against the gov module and printed the same.

inCMS ran gov's `row_grammar.py` beside its own `corpus_ids.py` and `gen_build_index.py`, which its
own fork of `row_grammar.py` cannot do: that fork dies on import. The census parsed 797 of 797
dash-led rows and 719 were live. `--ages` dated all 719 live keyed rows. Two reds there belong to
inCMS's data and not to this unit. Check 20 names 3 dash-led lines whose id the row grammar cannot
key. `check-arms.py --check` names 46 unarmed branches, because inCMS's sibling suites are withheld,
and unit 18 of this build owns that.
