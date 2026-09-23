# TOOL-aRepatriatedFork-9 — row_grammar and check-arms take NicoCares' additions, and stop importing sibling engines

**Status:** SPECCED · rev-1 · 2026-09-23 · node a · Tier-2 · base a7c78ad2 · streams tooling · order 1

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

NicoCares' `scripts/row_grammar.py` is gov's file plus 757 lines of backlog-row grammar, two
declared pins, a derived row-age mode and one gov defect fix, and two nc legs crash on import
against gov's bytes. nc's `scripts/check-arms.py` adds a non-vacuity refusal gov lacks. Separately,
gov's `check-arms.py` and `row_grammar.py` import helpers from `corpus_ids.py` and
`gen_build_index.py`, so at inCMS, whose copies of those two files are its own programs, both die
with an `ImportError`. This unit takes the additions upstream, corrects the three defects the
upstreaming measured, and moves the shared helpers into one kit module both engines can import.

## 2. Scope (IN)

- **S1** — The tracked-but-absent guard in `scan()`. Gov reads each row document unguarded at
  `tools/memory-tree/row_grammar.py:235`; nc wraps the read at `scripts/row_grammar.py:240-252` and
  raises the module's own `Problem`. Taken verbatim. Observed by AC1.
- **S2** — The exported backlog-row grammar, as specified in §4 `### Data model`: `ParsedRow`,
  `parse_row`, `backlog_shards`, `census` and `census_problems`, from nc `scripts/row_grammar.py:386-583`,
  with two corrections nc's own corpus could not surface. The row id accepts a frozen legacy id such
  as `ABL-015` or `DPL-a012`, and a `CLOSED by` clause may carry a parenthetical before its separator.
  Observed by AC2 and AC3.
- **S3** — The two shard pins, `SEVERITY_UNLABELLED_PIN` and `LIVE_ROW_PIN`, read by `cmd_check` as
  shrink-only ratchets that are UNARMED when undeclared and say so in green output. Observed by AC4.
- **S4** — `--emit-pin` prints all three pins. nc prints `ROW_DUPLICATE_PIN` and
  `SEVERITY_UNLABELLED_PIN` only (`scripts/row_grammar.py:851-867`) while its own announcement at
  `:679` tells the operator `--emit-pin` prints the `LIVE_ROW_PIN` token. Observed by AC4.
- **S5** — The `--ages` mode and `row_first_seen`, from nc `scripts/row_grammar.py:903-998`, with
  `encoding="utf-8"` on its `git log` call. Observed by AC5.
- **S6** — Hygiene check 20 prints `row_grammar.py --check`'s output on a GREEN run as well as a red
  one, so the NOT MEASURED lines reach the operator of the bar. Today
  `tools/memory-tree/check-memory-hygiene.sh:2162-2165` prints the capture only on failure. Observed by AC4.
- **S7** — `check-arms.py` refuses an empty or undeclared `ARMS_FLOORS` while any gate is discovered,
  and gains `--emit-floors`, both from nc `scripts/check-arms.py:307-317` and `:385-411`. The
  refusal's remedy names the module by its derived kit path, not nc's literal `scripts/`. Observed by
  AC6.
- **S8** — A new kit module `tools/memory-tree/tree_lib.py` holds the helpers two or more engines
  share, and every engine in the kit imports them from it. The inventory is in §4. Observed by AC7
  and AC8.
- **S9** — `ARMS_FLOORS`, `LIVE_ROW_PIN` and `SEVERITY_UNLABELLED_PIN` join
  `tools/memory-tree/.memory-tree.conf.example` with their blank semantics stated, and join
  `optional_keys` in `tools/memory-tree/kit.toml`. Observed by AC9.
- **S10** — `KIT_MEMORY_TREE_VERSION` moves off 2.85 and every paired marker moves with it. Observed
  by AC9.

## 3. Non-goals (OUT)

- Fixing `drift_report.py`'s live-row count (`tools/drift-audit/drift_report.py:1327-1352`), whose
  three miscounts nc documents in the grammar's own comment. The grammar makes that fix possible; the
  drift-audit kit takes it separately.
- Validating `severity` against a vocabulary. nc's ruling stands: the raw field is returned
  unvalidated and `rank` is populated only from the closed four-token set.
- An authored `opened:` field. nc refuted its premise by measurement, and its slot stays parsed and
  unpopulated.
- The `encoding="utf-8"` sweep over the rest of these two files, and the posture gate on gov's bar.
  Unit 3 of this build owns both. The one new call S5 adds carries the encoding itself.
- The role under which inCMS's own `corpus_ids.py` and `gen_build_index.py` are declared. Unit 13 of
  this build owns that. S8 only removes the reason gov's other engines needed those files.
- Arming or pinning gov's branches at an adopter whose sibling test suites are withheld. Unit 18
  of this build owns that.

### Edges

- **hands-off** external — the drift-audit kit's live-row count moves onto `parse_row` in a later unit
- **hands-off** external — NicoCares deletes its two forks and keeps its two pin declarations, in its own tree

## 4. Design

### Data model

The row grammar, as it ships. Every name below is exported at module scope and is part of the
contract nc's `scripts/check_closed_build_rows.py:74` and `scripts/check_core_ask_closures.py:41`
already import against. `read` stays exported, because `check_closed_build_rows.py:217` calls it.

| Name | Kind | Contract |
|---|---|---|
| `UNRANKED_PIN_KEY` | constant | `"SEVERITY_UNLABELLED_PIN"` |
| `LIVE_ROW_PIN_KEY` | constant | `"LIVE_ROW_PIN"` |
| `LIVE_STATUSES` | tuple | `OPEN` `SPECCED` `INPROGRESS` `BLOCKED` |
| `TERMINAL_STATUSES` | tuple | `CLOSED` `WONTDO` `DEFERRED`, see F1 |
| `STATUS_VOCAB` | tuple | the two above joined; must equal `tree_lib.STATUS_TOKENS` as a set |
| `SEVERITY_VOCAB` | tuple | `BLOCKER` `HIGH` `MED` `LOW`, most severe first; closed |
| `ParsedRow` | class | slots `raw form id keyed status qualifiers closed_by live severity rank opened body pointer` |
| `parse_row(line)` | function | a `ParsedRow`, or `None` for prose |
| `backlog_shards(root, conf)` | function | every tracked `.md` under the memory root's `backlog/`, sorted |
| `census(root, conf)` | function | one dict per shard: `shard live terminal unkeyed rows dashes unranked note` |
| `census_problems(rows)` | function | the non-vacuity floor as messages |
| `unranked_pins(conf)`, `live_row_pins(conf)` | function | `{shard: ceiling}`, `{}` when undeclared |
| `row_first_seen(root, conf)` | function | `{row-id: ISO date}` from `git log --reverse -p -m` over the backlog pathspecs |

The two grammar corrections, both measured on 2026-09-23 on node a by parsing every tracked
`memory/backlog/*.md` with nc's module:

- **The row id.** nc's `_ROW_ID` at `scripts/row_grammar.py:395` accepts a bare family or a
  family-slug-seq id, and nothing between. inCMS carries frozen legacy-era ids in that gap
  (`ABL-015`, `DPL-a012`, `PBL-011`), and 58 of its 796 dash-led backlog rows fail to parse, 54 of
  them live. The ruling is `[A-Z][A-Za-z0-9]{1,9}(?:-[A-Za-z0-9]+)*`, with `keyed` meaning "carries
  at least one dash". PINNED, measured under that pattern: gov 629 of 629 rows, inCMS 796 of 796,
  nc 386 rows over 376 dash-led lines with its live count unchanged at 196.
- **The `by` clause.** Gov's `memory/backlog/TOOL.md` carries a row closed `CLOSED by deletion`
  followed by a parenthesised id, and nc's `by` group admits one token and then demands the middot.
  The clause admits an optional parenthetical after its token.

The CLI, with exits:

| Mode | Prints | Exit |
|---|---|---|
| `--check` | the clean line with the live population, then one NOT MEASURED line per shard per undeclared pin | 0 clean, 1 on a finding |
| `--report` | the per-shard census, the declared-rank census, the raw prefixes that are not a rank, any floor message | 0 |
| `--emit-pin` | `ROW_DUPLICATE_PIN`, `SEVERITY_UNLABELLED_PIN` and `LIVE_ROW_PIN` declarations, measured | 0, or 1 on an open fence |
| `--ages` | row age over the live keyed set, derived from git | 0, 1 on an undated live row, `Problem` on a vacuous walk |
| `--check-rotation`, `--selftest` | as today | as today |

Pin format, shared by both new keys: space-separated `<shard-path>:<count>` tokens. A malformed
token is a named `Problem`. The census floor fires when a shard has dash-led lines and no parsed row;
when it fires, both ratchets are suppressed, so a broken grammar cannot print a "lower it to 0"
instruction.

`check-arms.py`: when `parse_floors(conf)` is empty and `discover(root)` found at least one gate,
`cmd_check` appends the refusal. `--emit-floors` prints one `ARMS_FLOORS="…"` line on stdout, one
`<gate>:<branches>:<armed>` token per discovered gate, sends anything unmeasured to stderr, and exits
1 when a gate errored, because an errored gate would be emitted at `0:0`.

### Inventory

`tools/memory-tree/tree_lib.py` is new. It takes these names, and the two modules that define them
today re-import them so every existing caller keeps working:

| Name | Today | Imported by, after |
|---|---|---|
| `parse_conf_line`, `parse_conf` | `corpus_ids.py:106-181` | `corpus_ids.py`, `gen_build_index.py`, `gotchas.py`, `check-arms.py`, `row_grammar.py` |
| `unfenced_lines` | `gen_build_index.py:294` | `gen_build_index.py`, `row_grammar.py` |
| `STATUS_TOKENS`, `TERMINAL` | `gen_build_index.py:150-151` | `gen_build_index.py`, `row_grammar.py` |
| `kit_rel` | `gen_build_index.py:135` | `gen_build_index.py`, `check-arms.py` |

The module name follows `tools/codebase-map/map_lib.py` and `tools/runlog/runlog_lib.py`. Each
function name keeps its current verb, so no lexicon cell moves. The new mode `--emit-floors` and
the new functions `cmd_emit_floors`, `cmd_ages`, `row_first_seen`, `census` and `census_problems`
are graded by the lexicon leg under the Python function cell; `census` is a noun-led name nc already
shipped and is a candidate for that leg's verb table, see F4.

### Migration

Additive for every adopter that declares nothing new: both pins are UNARMED when undeclared, and the
grammar is new API. The one behaviour that can red on the pull is S7: a tree with a discovered gate
and no `ARMS_FLOORS` refuses. Both measured adopters and gov declare the key today
(`.memory-tree.conf:24` at inCMS, `.memory-tree.conf:360` at nc, `.memory-tree.conf:523` in gov).

What each adopter then does:

- **NicoCares** takes gov's `row_grammar.py` and `check-arms.py` verbatim and keeps
  `.memory-tree.conf:380` and `:386`. Its `check_closed_build_rows.py` and `check_core_ask_closures.py`
  run unchanged against the gov module. No carve-out tag is spent on either fork, so nothing
  leaves the census.
- **inCMS** gets `tree_lib.py` as a new engine row on `govkit update`, after which gov's
  `check-arms.py` and `row_grammar.py` import. Its `scripts/check-arms.py` inline `load_conf`
  (`scripts/check-arms.py:93-102`) then has no reason to exist. The `KIT_MEMORY_TREE_ROW_GRAMMAR_DELTA`
  row in `.governance/kits.json` is encoding-only and leaves with unit 3. audit-B §7's other
  precondition, the pin file location, is inCMS data and not this unit's.

### Files touched (estimate)

- `tools/memory-tree/tree_lib.py` (new)
- `tools/memory-tree/row_grammar.py`
- `tools/memory-tree/check-arms.py`
- `tools/memory-tree/corpus_ids.py`
- `tools/memory-tree/gen_build_index.py`
- `tools/memory-tree/gotchas.py`
- `tools/memory-tree/check-memory-hygiene.sh`
- `tools/memory-tree/.memory-tree.conf.example`
- `tools/memory-tree/kit.toml`
- `tools/memory-tree/HYGIENE.template.md` and its render `memory/HYGIENE.md`, for the marker move
- `memory/map/features/row-grammar.md`

### Alternatives rejected

- **Keep an inline conf parser in `check-arms.py`**, as inCMS does. It re-opens
  `TOOL-aScouredKit-19`, whose measured failure was exactly a naive parser removing coverage while
  the gate stayed green.
- **Ship nc's grammar unchanged.** It under-counts inCMS's live set by 54 rows, which is the
  two-answers class the grammar was written to end, relocated to the next corpus.
- **Import the status tuples from `gen_build_index.py` as today.** That is the coupling S8 removes;
  the tuples move with the parser.

## 5. Production-readiness checklist

- security — no new write path. `--ages` runs one `git log` with a fixed argv and pathspecs built
  from `MEMORY_ROOT`; nothing from a row reaches a shell.
- perf / scale — the census re-reads the backlog shards, a few hundred KB. nc measured the `--ages`
  walk at 0.27 s over 247 live rows; it is not on `--check`.
- error / empty / loading states — an undeclared pin announces itself; an empty shard is 0 live and
  passes; a shard whose dash lines all fail to parse reds the floor; a tracked-but-absent document is
  a named failure, never a traceback.
- observability — S6 carries the NOT MEASURED lines to the hygiene leg's output on green runs.
- risks — S7 reds any adopter with a discovered gate and no floors on the pull. Mitigated by the
  refusal printing the `--emit-floors` remedy; F2 asks whether that is acceptable on day one.
- testing — nc's selftest arms travel with the code, plus one arm per correction in §4 and the
  import-graph arm in AC8.
- migration — additive keys, blank means unarmed; S7 is the only tightening, discussed above.
- user docs — `tools/memory-tree/README.md` gains the two pins and `--ages`, `--emit-floors`;
  `.memory-tree.conf.example` carries each key's blank semantics.

## 6. Acceptance criteria

- **AC1** — When a fixture tracks a row document and deletes it from the worktree,
  `python3 tools/memory-tree/row_grammar.py --check` exits 1 naming the path as tracked but not on
  disk, and prints no traceback.
  Red when: the read at `scan()` is unguarded and `FileNotFoundError` escapes.
- **AC2** — When `python3 tools/memory-tree/row_grammar.py --report` runs over a fixture shard holding
  `- ABL-015 · OPEN · body`, the census reports it live and keyed.
  Red when: the row id pattern is nc's and the line reads as prose.
  figure: DERIVED at observation; the 58-row inCMS count in §4 is PINNED 2026-09-23.
- **AC3** — When a fixture row reads `CLOSED by deletion` followed by a parenthesised id and a middot,
  `parse_row` returns status `CLOSED` and `live` False.
  Red when: the `by` group rejects the parenthetical and the row returns `None`.
- **AC4** — When `LIVE_ROW_PIN` is undeclared, `bash tools/memory-tree/check-memory-hygiene.sh`
  exits 0 and its output carries the `NOT MEASURED` line naming the shard; and `--emit-pin` prints a
  `LIVE_ROW_PIN=` line.
  Red when: check 20 swallows green output, or `cmd_emit_pin` omits the live-row pin.
- **AC5** — When `python3 tools/memory-tree/row_grammar.py --ages` runs over a fixture whose one row
  was edited in place after it was minted, it reports the mint date; and over a fixture whose
  families match nothing, it raises the vacuity `Problem`.
  Red when: `row_first_seen` drops `-m` or the walk reads blame dates.
- **AC6** — When `ARMS_FLOORS=""` over a tree with one discovered gate,
  `python3 tools/memory-tree/check-arms.py --check` exits 1 with the empty-floors refusal naming the
  derived module path, and `--emit-floors` prints one token for that gate.
  Red when: the empty mapping is iterated and the check passes.
- **AC7** — When gov's `tools/memory-tree/row_grammar.py` and `check-arms.py` are copied beside an
  inCMS-shaped `corpus_ids.py` that defines no `parse_conf`, both `--selftest` runs pass.
  Red when: either module still imports a name from `corpus_ids` or `gen_build_index`.
  fixture: a scratch copy of the inCMS worktree's own corpus_ids.py; that tree holds one today.
- **AC8** — When `python3 tools/memory-tree/row_grammar.py --selftest` runs, its import-graph arm
  asserts that no module in the kit directory imports a name from `corpus_ids` or `gen_build_index`
  other than those two modules' own mutual use, and it is observed RED on a staged re-import.
  Red when: a later edit adds a sibling import and the arm stays green.
- **AC9** — `bash tools/check-kit-versions.sh` exits 0 after the bump, and
  `tools/memory-tree/.memory-tree.conf.example` carries `ARMS_FLOORS`, `LIVE_ROW_PIN` and
  `SEVERITY_UNLABELLED_PIN` with their blank meaning stated.
  Red when: a paired marker is left on 2.85, or a key is read by the engine and absent from the example.

## 7. Gates

`row-grammar selftest` · `check-arms selftest` · `harness arms (fail branches armed or pinned)` · `memory hygiene` · `recall floor` · `recall floor arms` · `memory-hygiene self-test` · `corpus-ids selftest` · `build-index selftest` · `gotchas selftest` · `kit/dogfood doc parity` · `kit version markers` · `verdict epoch (kit version dates the engine)` · `codebase-map coverage + freshness` · `lexicon naming predicates`

New arm: `tools/memory-tree/row_grammar.py --selftest` · a legacy-id row, a parenthesised `CLOSED by` row, an undeclared-pin green run, and a staged sibling import · none
New arm: `tools/memory-tree/check-arms.py --selftest` · an empty `ARMS_FLOORS` over a tree with one discovered gate · none
New arm: `tools/memory-tree/check-memory-hygiene.test.sh` · a green check 20 run whose capture carries a NOT MEASURED line · the hygiene gate's `ARMS_FLOORS` token, if S6 adds a branch

## 8. Open questions

- **F1 — is `DEFERRED` a live backlog row?** nc rules it terminal for the census, while
  `gen_build_index.TERMINAL` is `CLOSED` and `WONTDO` only, and check 24's `cut` mode keeps a
  `DEFERRED` row in the live index. Both answers ship in one module under this unit. Options: (a)
  nc's ruling, named as a second tuple beside `TERMINAL` in `tree_lib.py` with the reason; (b) one
  terminal set, making a `DEFERRED` row live. Recommendation: (a). A census counting parked work as
  outstanding is the defensible report-only reading, not a gate's, and naming both tuples in one
  place is what keeps it one decision.
- **F2 — does S7 red a fresh adopter on day one?** It does: installing this kit installs
  `check-memory-hygiene.sh`, which defines the helper `discover()` looks for, so nc's claim that a
  fresh adopter has no gate is false for this kit. Options: (a) refuse, and have
  `adopt-memory-tree.sh --scaffold` print the `--emit-floors` command in its next steps; (b) announce
  an undeclared key as NOT MEASURED and refuse only an explicitly empty one. Recommendation: (a),
  matching how `UNDECLARED_WRITE_CEILING` is handled, because (b) cannot catch the key being dropped.
- **F3 — should gov declare the two shard pins for its own tree?** Undeclared, gov's own bar
  prints four NOT MEASURED lines on every run. Recommendation: measure with `--emit-pin` in the build
  commit and declare both, so the ratchets are exercised on the one tree that ships them.
- **F4 — `census` and `census_problems` as function names.** The lexicon leg may refuse a
  noun-led name. Recommendation: ask `--suggest` at build time and rename in gov before nc's two
  importers are told to follow, since they are the only callers.

## 9. Revision log

- rev-1 · 2026-09-23 · initial draft, from audit-D §1 and §5, audit-B §7 and audit-A's side finding,
  with the two grammar corrections measured over all three corpora on node a.

## 10. Reuse audit

The seam is the kit's existing conf-parser seam: `reuse_lookup.py` ranks `parse_conf` in
`tools/memory-tree/corpus_ids.py` as a SEAM at fan-in 5, and this unit moves it rather than adding
a second parser beside it. `census` in `tools/memory-tree/merge-rows.py` also ranks, and it answers
a different question, a line-level duplicate count, so no existing seam parses a backlog row's
fields. `TOOL-aWeldedTribunal-5` is the record that created the coupling S8 removes.

Recall terms used: `row_grammar parse_row census LIVE_ROW_PIN SEVERITY_UNLABELLED_PIN ARMS_FLOORS
emit-floors check-arms non-vacuity carve-out adopter parse_conf`.
