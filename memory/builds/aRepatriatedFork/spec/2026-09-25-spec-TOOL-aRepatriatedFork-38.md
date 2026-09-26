# TOOL-aRepatriatedFork-38 — every conf reader drops a trailing comment the way bash does

**Status:** CLOSED · rev-3 · 2026-09-26 · node a · Tier-1 · base 6373c6ee · streams tooling · order 19

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-25-build-TOOL-aRepatriatedFork-38-1-acceptance-ledger.md](../build/2026-09-25-build-TOOL-aRepatriatedFork-38-1-acceptance-ledger.md) | journal | — |
| [2026-09-26-review-TOOL-aRepatriatedFork-36-closing-diff-round1.md](../reviews/2026-09-26-review-TOOL-aRepatriatedFork-36-closing-diff-round1.md) | diff-review | TOOL-aRepatriatedFork-31 TOOL-aRepatriatedFork-32 TOOL-aRepatriatedFork-35 TOOL-aRepatriatedFork-36 TOOL-aRepatriatedFork-37 |

<!-- /gen:spec-records -->

## 1. Goal

inCMS declares `ratified="2026-09-10 node a"   # …` and gov's conf readers disagree with bash about
it: one kept the comment, one read `"2026-09-10`. A reader that disagrees with the shell sourcing the
same file grades a different declaration from the one the adopter wrote. Owner ruling, 2026-09-25.

## 2. Scope (IN)

- **S1** — Every conf reader in gov takes bash's rule: a QUOTED value, single or double, ends at its
  matching quote, whatever follows; an UNQUOTED value ends at a `#` that FOLLOWS whitespace, so a `#`
  opening the word is data (`K=#x` is `#x`); and whitespace right after `=` ends the assignment
  (`K=   # note` is empty). One rule, carried in each reader because kits cannot import one another.
  Seven readers changed at rev-2: `lexicon_conf.load_conf` and `adopt-lexicon.sh`
  `read_conf_scalar`, `map_lib.load_conf`, `recall_conf.load_conf`, `check-spec-tokens.py`
  `read_conf_key`, `render_playbook.read_conf` and `process-monitor/scope.py` `read_roots`. Rev-3
  brings the three rev-2 controls to the same rule — `tree_lib.parse_conf_line`,
  `drift_report.load_conf` and `runlog_lib._read_conf_key` — since each split from bash on one of
  the two word-start spellings. Observed by AC1.
- **S2** — Each reader's own suite gains an arm pinning the spellings, red first on the old bytes.
  The lexicon arm asserts its fixture edit landed before it grades. Observed by AC2.
- **S3** — codebase-map, drift-audit, lexicon, memory-recall, memory-tree, playbook-render,
  process-monitor and runlog take their version bump in every carrier. `check-spec-tokens.py` ships
  nowhere. Observed by AC3.

## 3. Non-goals (OUT)

- Shell grammar beyond these spellings, as `parse_conf_line`'s own docstring rules out: an escaped
  quote inside a quoted value and adjacent concatenation stay wrong in every reader.

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

The round-1 closing-diff review (C3, C4, C5) measured what rev-2 left. `read_conf_scalar` peeled no
single quote, so `canon_unfrozen='…'` read with its quotes and `--check` refused a stamp `lexicon.py`
reads fine. Seven readers split on a `#` at the value's first character, so `K=#x` read empty where
bash reads `#x`, and the three first-word readers read `K=   # note` as the word `#`. The lexicon
arm never checked that its fixture edit happened.

### Inventory

No new function. Each reader keeps its own copy of the rule, because kits are copied into adopters
independently and cannot import one another.

### Files touched (estimate)

The ten Python readers and the shell one, their suites, `tools/install-prefix-waivers.txt`
(re-keyed where a line moved), the map, and the version carriers.

### Alternatives rejected

- One shared reader. A kit cannot import another kit's module at an adopter.

## 6. Acceptance criteria

- **AC1** — A scratch probe feeding every reader `K=#x`, `K= #x`, single- and double-quoted values
  with and without a trailing comment, and `K=plain   # note`, prints no `BAD` line for any of the
  eleven readers, with bash sourcing the file as the reference row; on the rev-2 bytes it prints 13.
  Red when: any reader still disagrees with bash.
- **AC2** — Each new arm passes on the built tree and fails with the old reader swapped in:
  `test_parser_vs_bash` in `tools/memory-recall/selftest.py`, `test_conf_grammar` in
  `tools/codebase-map/selftest.py`, `test_read_roots_drops_a_trailing_comment` in
  `tools/process-monitor/selftest.py`, the cutoff arms in `tools/check-spec-tokens.test.sh`, the
  `read_conf` arm of `render_playbook.py --selftest`, the conf-parse arms of
  `tools/memory-tree/corpus_ids.py --selftest`, `test_conf_parser_matches_bash` in
  `tools/drift-audit/selftest.py`, `test_ac10_conf_readers` in `tools/runlog/selftest.py`, and the
  arms in `tools/lexicon/selftest.py`, whose fixture arm reds when the scaffold spells the key
  differently. Red when: an arm passes on the old bytes.
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
- rev-3 · 2026-09-26 · S1 · S2 · S3 · §3 · §4 · AC1 · AC2 · folds the round-1 closing-diff review's
  C3, C4 and C5: the shell reader peels single quotes, every reader decides the word start on the
  text right after `=` — the three rev-2 controls included, since each split from bash there — and
  the lexicon arm asserts its fixture. The base moves to the rewritten parent.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "parse a KEY=VALUE conf line the way bash sources it"`
ranked `key`, `parse` and `load_conf`, the last listing ten of the readers this unit graded. The
rule reused is `tree_lib.parse_conf_line`'s, whose docstring states it; each fixed copy follows it
rather than inventing a third reading, and rev-3 corrects that original where it split from bash.

Recall terms used: `conf load_conf parse_conf_line quoted value trailing comment bash sourcing
ratified cutoff read_conf_scalar`.
