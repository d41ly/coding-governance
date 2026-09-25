# TOOL-aRepatriatedFork-38 — every conf reader drops a trailing comment the way bash does

**Status:** CLOSED · rev-2 · 2026-09-25 · node a · Tier-1 · base ea2988c1 · streams tooling · order 19

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-25-build-TOOL-aRepatriatedFork-38-1-acceptance-ledger.md](../build/2026-09-25-build-TOOL-aRepatriatedFork-38-1-acceptance-ledger.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

inCMS declares `ratified="2026-09-10 node a"   # …` and gov's conf readers disagree with bash about
it: one kept the comment, one read `"2026-09-10`. A reader that disagrees with the shell sourcing the
same file grades a different declaration from the one the adopter wrote. Owner ruling, 2026-09-25.

## 2. Scope (IN)

- **S1** — Every conf reader in gov takes bash's rule: a QUOTED value ends at its matching quote,
  whatever follows, and an UNQUOTED value ends at a `#` that begins a word. Seven readers change:
  `lexicon_conf.load_conf` and `adopt-lexicon.sh` `read_conf_scalar`, `map_lib.load_conf`,
  `recall_conf.load_conf`, `check-spec-tokens.py` `read_conf_key`, `render_playbook.read_conf`
  and `process-monitor/scope.py` `read_roots`. Observed by AC1.
- **S2** — Each reader's own suite gains an arm pinning both spellings, red first on the old bytes.
  Observed by AC2.
- **S3** — codebase-map, lexicon, memory-recall, playbook-render and process-monitor take their
  version bump in every carrier. `check-spec-tokens.py` ships nowhere. Observed by AC3.

## 3. Non-goals (OUT)

- The readers that already agree with bash: `tree_lib.parse_conf_line`, which the five memory-tree
  loaders share, `drift_report.load_conf` and `runlog_lib._read_conf_key`. They are the controls.
- Shell grammar beyond these two spellings, as `parse_conf_line`'s own docstring rules out.

### Edges

- **hands-off** `DEPL-aRepatriatedFork-20` — inCMS's `ratified` line and any other commented
  declaration, which gov's readers now read as its shell does.

## 4. Design

### Evidence

`git grep -n "def load_conf\|def read_conf\|def parse_conf\|def _read_conf"` over `tools` found
thirteen readers; `scope.read_roots` and `adopt-lexicon.sh` `read_conf_scalar` were found by
grepping for a hand-rolled quote strip. A probe fed each one `A="2026-09-10 node a"   # note` and
`B=plain   # note` beside bash sourcing the same file:

| Reader | A before | B before |
|---|---|---|
| `lexicon_conf.load_conf` | the whole tail, quotes and comment | `plain   # another note` |
| `map_lib.load_conf`, `recall_conf.load_conf` | `"2026-09-10` | `plain` |
| `check-spec-tokens.py` `read_conf_key` | blank, which turns a cutoff off | `plain   # another note` |
| `render_playbook.read_conf` | `2026-09-10 node a"   # a trailing note` | `plain   # another note` |
| `scope.read_roots` | five tokens, `#` among them | not probed |
| `adopt-lexicon.sh` `read_conf_scalar` | `2026-09-10 node a"   # a trailing note` | `plain   # another note` |

`map_lib` and `recall_conf` tested whether a value's first and last characters were quotes, the
defect `drift_report.load_conf` fixed under `TOOL-dLoggedFlight-13`. Their fix is that one.

### Inventory

No new function. Each reader keeps its own copy of the rule, because kits are copied into adopters
independently and cannot import one another.

### Files touched (estimate)

The seven readers, their six suites, `tools/install-prefix-waivers.txt` (re-keyed for `map_lib.py`),
the map, and the version carriers.

### Alternatives rejected

- One shared reader. A kit cannot import another kit's module at an adopter.

## 6. Acceptance criteria

- **AC1** — A scratch probe feeding every reader `A="2026-09-10 node a"   # note` and
  `B=plain   # note` prints `BAD` for the seven on the old bytes and `ok` for every reader after,
  with bash sourcing the file as the reference row.
  Red when: any reader still disagrees with bash.
- **AC2** — Each new arm passes on the built tree and fails with the old reader swapped in:
  `test_parser_vs_bash` in `tools/memory-recall/selftest.py`, `test_conf_grammar` in
  `tools/codebase-map/selftest.py`, `test_read_roots_drops_a_trailing_comment` in
  `tools/process-monitor/selftest.py`, the two cutoff arms in `tools/check-spec-tokens.test.sh`, the
  `read_conf` arm of `render_playbook.py --selftest`, and the two arms in `tools/lexicon/selftest.py`.
  Red when: an arm passes on the old bytes.
- **AC3** — `bash tools/check-kit-versions.sh` exits 0 and `python tools/govkit/govkit.py epoch`
  reports no FAILED entry. Red when: a moved kit kept its old value in any carrier.

## 7. Gates

`kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `lexicon wiring` · `memory-recall skill wiring` · `install-prefix (shipped surface)` · `codebase-map coverage + freshness` · `harness arms (fail branches armed or pinned)`

New arm: `tools/process-monitor/selftest.py` · `test_read_roots_drops_a_trailing_comment` · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-25 · initial draft, from the owner's ruling.
- rev-2 · 2026-09-25 · §2 S1 · §4 Evidence · the class measured at seven readers, not one. Built:
  every reader agrees with bash, every new arm red on the old bytes.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "parse a KEY=VALUE conf line the way bash sources it"`
ranked `key`, `parse` and `load_conf`, the last listing ten of the readers this unit graded. The
rule reused is `tree_lib.parse_conf_line`'s, whose docstring states it and which already agreed
with bash; each fixed copy follows it rather than inventing a third reading.

Recall terms used: `conf load_conf parse_conf_line quoted value trailing comment bash sourcing
ratified cutoff read_conf_scalar`.
