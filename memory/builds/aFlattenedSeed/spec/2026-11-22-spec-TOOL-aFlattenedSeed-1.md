# TOOL-aFlattenedSeed-1 — three kit readers read an adopter's own layout

**Status:** CLOSED · rev-3 · 2026-11-22 · node a · Tier-1 · base b2eec4b6 · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-22-build-TOOL-aFlattenedSeed-1-widen-1.md](../build/2026-11-22-build-TOOL-aFlattenedSeed-1-widen-1.md) | widen | — |

<!-- /gen:spec-records -->

## 1. Goal

Three readers in the kits refuse or crash on layouts an adopter legitimately has. This unit fixes the
product-test contract reading a wrapped leg manifest, the eol-class scan meeting a submodule, and a
ledger seed whose kit is installed flat. After it, inCMS can seed its populations and run its bar.

## 2. Scope (IN)

- **S1** — `tools/run-gates/product_tests.py#read_manifest_rows` unwraps a top-level object's `legs`
  value before its list check, as `parse_leg_names` does since TOOL-aWrappedRoster-1. Observed by AC1.
- **S2** — `tools/gate-lint/eol_class.py#read_shebang_members` skips a mode-160000 index entry, a
  gitlink, because it is no file and its commit need not be in this object store. Observed by AC2.
- **S3** — The `legacy_ledger_py` block's `run_seed_argv` resolves each argument through a new
  `resolve_seed_arg`. An argument spelled `{prefix}/<home>/<file>` resolves through `resolve_kit_dir`,
  which reads the receipt, and any other argument goes through `resolve_prefix_token` as before. The
  block is re-inlined byte-identically into the memory-tree and gate-lint kit copies. Observed by AC3.

## 3. Non-goals (OUT)

- The other list-only manifest readers, `seen_red.py#read_manifest_legs` and
  `held_halves.py#load_manifest`: no adopter's bar reds on them today.
- Pinning an adopter's execution-sensitive files LF: once S2 lands, the scan grades them, and the
  adopter clears its own findings.
- A `{prefix}` argument nested deeper than `<home>/<file>`: no registered seed spells one.

### Edges

- **consumes-from** `TOOL-aWrappedRoster-1` — the wrapped manifest shape S1 reads
- **consumes-from** `TOOL-aRepatriatedFork-2` — `resolve_kit_dir`, the receipt-first kit locator S3 calls

## 4. Design

### Mechanism

- S1: `rows = rows.get("legs")` when the parsed top level is a dict. The existing check then refuses
  any object that has no row list under `legs`.
- S2: the `ls-files -s` mode column is read, and a gitlink never reaches `cat-file --batch`.
- S3: `resolve_kit_dir(<home>, <file>, <this copy's dir>)` finds the receipt row whose `source` ends
  in `<home>/<file>`, which locates the file wherever the install put it. Where no install holds that
  kit, the probes and the tool-root fallback keep today's answer.

### Files touched (estimate)

- `tools/run-gates/product_tests.py`, `tools/gate-lint/eol_class.py`
- `tools/lib/legacy_ledger.py`, `tools/memory-tree/legacy_ledger.py`, `tools/gate-lint/legacy_ledger.py`
- `tools/lib/resolve-python.test.sh`

## 5. Acceptance criteria

- **AC1** — When `product_tests.py check --fixture` runs every case, its `wrapped manifest` case reads
  the one row under `legs`. Red when: the reader refuses the object shape.
  Observed red against the base reader on 2026-11-22: "is no list of leg rows".
- **AC2** — When `eol_class.py --selftest` plants a gitlink whose commit the store lacks, the scan grades
  the same member count and does not raise. Red when: it raises IndexError.
  Observed red against the base reader on 2026-11-22: IndexError from `read_shebang_members`.
- **AC3** — When a seed argv names a kit file under a home directory the fixture lacks, and only a
  receipt row places that file, in a flat directory, `seed` arms the population. Red when: the token resolves only against the tool
  root and the seed exits non-zero.
  Observed red against the base block on 2026-11-22: `unarmed fx-flat exit 2`.

## 6. Gates

`product-test contract (tests.product)` · `portability (execution-sensitive files are LF by class)` · `python resolver (behaviour + inline parity + idiom ban)` · `shell-hygiene selftest` · `memory hygiene` · `line length` · `spec tokens (a spec's own names resolve)`

New arm: tools/run-gates/product_tests.py · covers AC1 · `--fixture` reads a planted wrapped manifest through `read_manifest_rows`; staged red against the base reader · none
New arm: tools/gate-lint/eol_class.py · covers AC2 · `--selftest` plants a gitlink with an absent commit; staged red against the base reader · none
New arm: tools/lib/resolve-python.test.sh · covers AC3 · part 2o seeds `fx-flat` through a receipt row on a flat layout · none

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-22 · initial draft.
- rev-2 · 2026-11-22 · AC3 · closed: the arm's red against the base block recorded.
- rev-3 · 2026-11-22 · AC3 · §6 · the bar's spec-tokens leg: AC3 names the fixture without paths gov does not track, and §6 names the leg `eol_class.py` guards.
