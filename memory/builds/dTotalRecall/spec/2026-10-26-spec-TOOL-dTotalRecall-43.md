# TOOL-dTotalRecall-43 — the round-1 spec audit's 59 minors, batched

**Status:** OPEN · rev-3 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 27 · advances TOOL-dTotalRecall-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-5 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-44 TOOL-dTotalRecall-45 TOOL-dTotalRecall-46 TOOL-dTotalRecall-47 TOOL-dTotalRecall-48 TOOL-dTotalRecall-49 TOOL-dTotalRecall-50 TOOL-dTotalRecall-51 TOOL-dTotalRecall-52 TOOL-dTotalRecall-53 TOOL-dTotalRecall-54 TOOL-dTotalRecall-55 TOOL-dTotalRecall-56 TOOL-dTotalRecall-57 TOOL-dTotalRecall-58 TOOL-dTotalRecall-59 TOOL-dTotalRecall-60 TOOL-dTotalRecall-61 TOOL-dTotalRecall-62 TOOL-dTotalRecall-63 TOOL-dTotalRecall-64 TOOL-dTotalRecall-65 TOOL-dTotalRecall-66 |
| [2026-10-26-build-TOOL-dTotalRecall-36-round1-fix-return.md](../build/2026-10-26-build-TOOL-dTotalRecall-36-round1-fix-return.md) | research | TOOL-dTotalRecall-36 TOOL-dTotalRecall-2 TOOL-dTotalRecall-8 TOOL-dTotalRecall-23 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 |
| [2026-10-26-prompt-TOOL-dTotalRecall-36-round1-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-36-round1-fix-brief.md) | research | TOOL-dTotalRecall-2 TOOL-dTotalRecall-8 TOOL-dTotalRecall-23 TOOL-dTotalRecall-36 TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-39 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 |
| [2026-10-26-review-TOOL-dTotalRecall-37-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dTotalRecall-37-spec-audit-round1.md) | spec-audit | TOOL-dTotalRecall-37 TOOL-dTotalRecall-38 TOOL-dTotalRecall-40 TOOL-dTotalRecall-41 TOOL-dTotalRecall-42 TOOL-dTotalRecall-36 TOOL-dTotalRecall-39 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dTotalRecall/reviews/2026-10-26-review-TOOL-dTotalRecall-1-spec-audit-round1.md`)
exited CONVERGED with 66 confirmed findings over units 1 to 26; its seven highs, ids 1, 16, 17, 23, 36,
49 and 51, are units 36 to 42. This unit is BUILD-METHOD M4's batch of every MEDIUM and LOW, each
keeping its report id, plus gap-mem-16 (id 2), the owned gap no spec carried. Landing on 24 units, it
builds after every unit (order 27, above `TOOL-dTotalRecall-12`'s 26).

Items follow the report's order, M1 to M44 then L1 to L13, but for M10's ids 11, 32 and 33 (S10 to
S12) and L12's id 67 (S17, beside its twin id 19); the review holds each item's text. Ids 9 and 36 are
one defect at two grades (unit 40 closes unit 4's half, S8 unit 2's); ids 19 and 67 are one match, ids
12 and 51 one home rule, each fixed once. Refuted ids 14 and 61 are outside the disposal.

## 2. Scope (IN)

Each item states its change to the unit it lands on, as built; a landed criterion the finding showed
unpassable is re-observed here, corrected.

- **S1** — id 2, gap-mem-16. `check_record_kinds` in `record_kinds.py` gains the arm
  `homeless records`: every tracked file under the memory root and outside `builds/` that carries a
  `**Serves:**` binding in its first `BIND_HEAD_LINES` lines is matched by some row's `home` or is red,
  named by path. Each period-, SHA- or adopter-keyed record kind the candidate run finds in the real
  tree gains a registry row with a glob `home`, in `TOOL-dTotalRecall-18`'s column grammar.
  Observed by AC1.
- **S2** — id 3. `TOOL-dTotalRecall-21` AC1's grep forbade the call its S4 and S8 require; corrected,
  recall spells the FTS builder's old name nowhere and keeps the one index writer. Observed by AC2.
- **S3** — id 4. The registry rows of units 11, 7, 3 and 4 take units 16 and 18's grammar:
  `layer = "layer.memory"`; `lifecycle` from the closed set (`append-only` for `shape-run` and `claim`,
  `current-state` for `ask` and `build-readme`); `readers` as read keys, or `[]` with
  `readers-none = "<reason>"`; `home` a glob (`memory/builds/*/BACKLOG.md`, `memory/builds/*/README.md`,
  `refs/gov/claims/*`, and unit 42's shape-run glob); and a `purpose` table. Observed by AC3.
- **S4** — id 5. `deviation` has one registry entry, the factory-kinds row, whose `source` is the
  factory's per-kind field table and whose `writer` reads `gov_record.py new <kind>`; the door's writer
  refusal (`TOOL-dTotalRecall-2` S2) admits `build_records.py new <kind>` as its alias. Observed by AC4.
  **Readers:** by name: READER NOT IN TREE — `record-kinds.toml`, minted by `TOOL-dTotalRecall-1`, is
  absent at base · by value: `check_record_kinds` and the door's kind lookup read the row's `writer`
  and `source` cells, the factory row after this item.
- **S5** — id 6. Unit 1's field check finds records by each row's `home`, which
  `TOOL-dTotalRecall-18` fills on every row. Its AC1 report, per-kind graded and legacy counts with
  `deviation`'s legacy count non-zero, holds at the tip. Observed by AC5.
- **S6** — id 7. The retag step of `TOOL-dTotalRecall-20` writes `## [section.<anchor>] <heading>`,
  the one authored-tag spelling `TOOL-dTotalRecall-9` S1 reads, and its conservation rule
  (`TOOL-dTotalRecall-20` S6) cuts `[section.<anchor>] `. Observed by AC6.
- **S7** — id 8. `TOOL-dTotalRecall-19` AC1 and AC2 named a `--serves` flag the door lacks; corrected,
  they use `--unit`, adding no alias. Observed by AC7.
- **S8** — id 9. Unit 2's half of the `journal` defect: the door's registry rewrite of `hand` rows
  (`TOOL-dTotalRecall-2` S9) names the row `log`, reading each row's kind through `canonical_kind`, so
  the `log` row's `writer` reads `gov_record.py new log`. Unit 40's alias census reds any raw comparison
  left in `gov_record.py`. Observed by AC8.
- **S9** — id 10. `stream-plan` joins the record-kind vocabulary: `RECORD_KIND_TOKENS` in
  `tree_lib.py` carries it, so a record opening `**Serves:** stream-plan <ids>`
  classifies under `read_bindings`, that line being the kind's binding, stated in the row's
  `purpose`. Observed by AC9.
- **S10** — id 11. The memory-tree kit declares its reach into the playbook kit's index once: a
  `requires_if` row for `playbook` in `tools/memory-tree/kit.toml` names `gov_map.py`, `code_record.py`
  and `record_extract.py`, which reach `tag_index.py` through `resolve_kit_dir`, each exiting 2 naming
  the playbook kit where it does not resolve. Observed by AC10.
- **S11** — id 32. `gen_atlas.py` (`TOOL-dTotalRecall-26` S5) reads policy through the memory-tree
  adapter `tools/memory-tree/policy_value.py` (`TOOL-dTotalRecall-8` S10), not the playbook kit's.
  Observed by AC11.
- **S12** — id 33. `gov_map.py` (`TOOL-dTotalRecall-14` S6) reads `memory.map-budget` and
  `memory.map-overflow` through S11's adapter. Observed by AC12.
- **S13** — id 12. The `record` extractor of `record_extract.py` takes a record's kind
  from `derive_record_kind` (unit 42 S5): the Serves kind decides and the home admits, so log, research,
  deviation, shape-run and stream-plan records under one `build/` folder each tag as their own kind.
  Observed by AC13.
- **S14** — id 13. A census hit kept on purpose carries the line marker `# slug-grammar: kept <reason>`,
  and `id_grammar.py --readers` prints no marked line, so `TOOL-dTotalRecall-5` AC7 reads "no line that
  is neither an entry point nor marked kept"; `tools/runlog/model.py:1571`'s `slug_re` carries the
  marker. Unit 38's split shapes read the same marker. Observed by AC14.
- **S15** — id 18. `BUILTIN_ARMED` in the `extract_code` block (`tools/lib/extract_code.py` and its
  copies) mirrors the lexicon's measured `KNOWN_EXTS` (`tools/lexicon/lexicon.py:117-119`): `js` maps
  to `js-regex` under `probe`, and no `mjs`, `cjs`, `jsx` or `bash` entry is armed. A parity arm in the
  block's suite holds them equal. Observed by AC15.
- **S16** — id 19. The memory-path match of `tools/runlog/memory_measure.py` (`TOOL-dTotalRecall-12` S3)
  folds `\` to `/`, case-folds a drive letter and maps `/c/` to `c:/`, then accepts an absolute word
  only when it starts with this clone's main worktree, or a `.claude/worktrees/*` worktree of it,
  followed by `/<root>/`; the harness's auto-memory directory never counts. Observed by AC16.
- **S17** — id 67. The same match accepts a relative word only when it starts with `<root>/` or equals
  `<root>`, so a bare `memory` word counts and a foreign repository's `memory/` does not. Observed by
  AC17.
- **S18** — id 24. One cycle walker: `backlog._scan_cycles` (`tools/memory-tree/backlog.py:1271`) is
  lifted into a fold-independent `scan_cycles(edges, live)` in the same module, the ask-hold check
  calling it with its fold's live set, and `check_relation_cycles` (`TOOL-dTotalRecall-6` S6) is a thin
  caller passing the `after` edges among resolved builds. Observed by AC18.
- **S19** — id 25. The `[[ledger]]` rows `record-kinds-legacy`
  (`TOOL-dTotalRecall-1` S8) and `legacy-records` (`TOOL-dTotalRecall-19` S7) fold into one,
  `record-kinds-legacy`, keyed by path and section with a field `check` holding `kind-schema` or
  `causes`, each slice keeping the seed point it had; `legacy_ledger.py` lists both slices together,
  and `check_causes` reads the `causes` slice. No row of either home is lost. Observed by AC19.
  **Readers:** by name: READER NOT IN TREE — both registrations, minted by `TOOL-dTotalRecall-1` and
  `TOOL-dTotalRecall-19`, are absent at base · by value: `check_causes` and `check_record_kinds` read
  the rows, each its own slice after this item.
- **S20** — id 26. The front-matter step (`TOOL-dTotalRecall-20` S4) calls the one grader
  `check_front_matter`, which `gen_build_index.py` exposes and its own `parse_front_matter` refusal
  (`TOOL-dTotalRecall-4` S4) calls, so the legacy exception holds in both. Observed by AC20.
- **S21** — id 27. The memory legs' readers `unfenced-head` and `id-harvest` (`TOOL-dTotalRecall-23` S2)
  register through PLAY-dOrderedCharter-44's extractor mechanism and write `blob_row` rows, the payload
  in `text`, so `blob_parsed` is the one freshness ledger. The 44 version rule gains an optional params
  digest these readers and S22's extraction share. The `leg_row` table and `LEG_READERS` give way
  to those rows. Observed by AC21.
  **Readers:** by name: READER NOT IN TREE — `leg_row` and `LEG_READERS`, minted by
  `TOOL-dTotalRecall-23`, are absent at base · by value: `read_rows_at` reads the payloads from
  `blob_row` after this item.
- **S22** — id 28. memory-recall's record and chunk extraction (`TOOL-dTotalRecall-21` S2) registers as
  an extractor of the namespace registry, so `blob_parsed` is its ledger, and its four inputs,
  `CACHE_VERSION`, `CHUNK_MAX`, the conf digest and the alias digest, form S21's params digest. The
  `fts_blob` table gives way to that ledger. Observed by AC22.
  **Readers:** by name: READER NOT IN TREE — `fts_blob`, minted by `TOOL-dTotalRecall-21`, is absent at
  base · by value: `build_index` and unit 23's recall copy read which blobs are current from
  `blob_parsed` after this item.
- **S23** — id 29. For a row whose `schema.source` names an owner literal, `check_record_kinds` calls
  that owner's reader, `deviation_join.read_record` or `build_records.read_record`, over the row's
  population, and generates its own field check only for kinds no owner grades. Observed by AC23.
- **S24** — id 30. `memory.map-purpose` drives PLAY-dOrderedCharter-22's `purpose` arm: under `refuse`
  that arm's awaiting exemption ends. `record_kinds.py --purpose-review` reads chain rows through
  `read_chain_registry` and namespace members through 22's member enumeration, and `record_kinds.py
  --check` grades only the registry's own rows' purpose. Observed by AC24.
- **S25** — id 31. The `sections` column of the spec row (`TOOL-dTotalRecall-9` S2) is held equal to
  `SPEC_TITLE_NUMBERS` (`tools/memory-tree/gen_build_index.py:8493`) by a parity arm, its `required`
  flags following hygiene check 12's tier rule, a Tier-1 spec's production-readiness and reuse
  sections optional (`tools/memory-tree/check-memory-hygiene.sh:1791`). Observed by AC25.
- **S26** — id 37. `WIRE-INTO-PROJECT.md` §0 (`:127`) and §3c's copy-install steps (`:582-586`) state
  that `<prefix>/playbook/` sits beside memory-recall, and `query.py` with no playbook kit beside it
  exits non-zero naming it. Observed by AC26.
- **S27** — id 38. `tools/memory-recall/verbatim.json` is re-stamped for `bench.py` and `union.py`, a
  reason each; `union.py`'s fork, `B.build_fts_rows` for `B.build_index`, is recorded in the selftest's
  verbatim docstring and the kit README's verbatim table. Observed by AC27.
- **S28** — id 39. Every fixture README under `tools/` that types `node`, `roster` or `streams` keeps only
  the keys `TOOL-dTotalRecall-4`'s schema admits as typed, except the plants staging that refusal; the
  files are those `git grep -lE '^(node|roster|streams): ' -- tools` lists at the pass.
  Observed by AC28.
- **S29** — id 40. Every leg units 1, 8, 11, 19, 22 and 26 added carries its meta-gate rows: a kit
  `[[gate_leg]]` or registry `[[exempt_leg]]` row, its `tools/govkit/subject-pins.tsv` row written by
  `govkit.py selfcheck --write`, its `tools/run-gates/ceiling-evidence.txt` line, and a
  `gate-legs` claim in a dossier with room under `DOSSIER_CAP_BYTES`. Observed by AC29.
- **S30** — id 41. `memory/map/generated/` is regenerated by `python tools/codebase-map/gen_map.py
  --write` at this pass, after every unit that minted or renamed a symbol. Observed by AC30.
- **S31** — id 42. Every name the units' Inventory lines mint is asked of the lexicon at this pass;
  each flagged name, `canonical_kind` and `ensure_index` among them, takes its suggestion, or, where
  the name is a contract across units, has its stem declared.
  Observed by AC31.
- **S32** — id 43. The legs running the readers unit 5 re-points, and the README slot contract for every
  unit editing `gen_build_index.py`, are named on this unit's §7 leg line. NOT OBSERVED: the leg line is
  the change, and the close runs it.
- **S33** — id 44. The resolver parity leg for unit 26's `help_pages` row, `drift-audit records` and the
  lexicon leg for unit 13's edits, and `runlog record schema` for unit 12's verb are named on this
  unit's §7 leg line. NOT OBSERVED: as S32.
- **S34** — id 45. `tools/codebase-map/scen-adversarial.json` ADV-05 and ADV-06 name
  `{prefix}/memory-tree/record_find.py` as `expected_file`, their `established_by` citing its lines, and
  the comment at `tools/memory-recall/selftest.py:1906` names `record_find.py`'s `rrf`. Observed by AC34.
- **S35** — id 46. `memory/guides/SESSION-KICKOFF.md:63` reads that a CLOSED Tier-2 unit owes an
  acceptance ledger "in a `log` record (`journal` read as its alias)", S54 re-stamping `last-audit`.
  Observed by AC35.
- **S36** — id 48. The worktree state of `read_defs_at` (`TOOL-dTotalRecall-13` S2) takes blob ids from
  one `git hash-object --stdin-paths` spawn, so filters apply; a path absent on disk yields no entry and
  is counted `missing`; a mode `120000` path is read as its link text. Observed by AC36.
- **S37** — id 50. The door refuses, exit 2 naming the argument, a `--field`, `--title`, `--caused-by` or
  `--edge` value holding a CR or an LF, through `check_line_break(label, value)` in
  `tools/memory-tree/backlog.py`, which unit 41's `check_row_value` calls for its line-break half.
  Observed by AC37.
- **S38** — id 52. Every index connection `query.py` opens sets a busy timeout; a busy or locked
  `sqlite3.OperationalError` prints `index busy` and exits 2, and only any other `DatabaseError` names
  `gov_tag.py --rebuild`. Observed by AC38.
- **S39** — id 53. `build_index`'s transaction bounds the FTS rows: it clears rows whose params digest
  no live worktree's conf derives, whatever their blob; at a live digest, rows whose blob no live
  worktree's HEAD tree and no `dirty_path` row holds; and `dirty_path` rows and their FTS rows for a
  worktree `git worktree list` does not name. The index line reports the freed rows. Observed by AC39.
- **S40** — id 56. `parse_front_matter` raises `StaleHeader` on a key given twice, naming the key and
  both line numbers. Observed by AC40.
- **S41** — id 57. `GIT_OWN` (`TOOL-dTotalRecall-18` §4 "The pockets") is a pattern set covering git's
  transient and optional common-dir entries: `*.lock`, `MERGE_MSG`, `MERGE_MODE`, `AUTO_MERGE`,
  `REBASE_HEAD`, `rebase-merge/`, `rebase-apply/`, `sequencer/`, `BISECT_*`, `rr-cache/`, `gc.pid` and
  `lfs/`. Observed by AC41.
- **S42** — id 58. The map cache `<git-common-dir>/gov/map/<tree>.map` is written to a temporary file
  beside it and moved into place with `os.replace`, its last line carrying the body's byte count,
  which the reader checks before serving. Observed by AC42.
- **S43** — id 60. The door's mint opens its file with `open(path, "x")`, counts the home's untracked
  files when computing the next free `<n>`, and on a collision takes the next `<n>`, leaving the
  existing file byte-identical. Observed by AC43.
- **S44** — id 62. Every caller of `derive_anchor` (`TOOL-dTotalRecall-10` S1) seeds `seen` with the
  record's authored tags before deriving any anchor, so an untagged heading never derives an address an
  authored tag holds; the contract in `tag_index.py` says so. Observed by AC44.
- **S45** — id 63. `edge_grammar.py --cardinality` with the memory-tree kit unresolved exits 2 naming
  that kit, and never prints a zero count. Observed by AC45.
- **S46** — id 64. `gen_atlas.py` emits each Mermaid node as `id["<label>"]`, `"` encoded `#quot;`,
  and escapes `|` as `\|` and each backtick in a table cell. Observed by AC46.
- **S47** — id 65. `record_kinds.py --purpose-review --write` refuses a write into a path a
  `[[generated]]` row or a kit `rendered` row owns, drafting an ask for that member; its `--writes` list
  names each member file it would write. Observed by AC47.
- **S48** — id 15. `TOOL-dTotalRecall-14` AC7 read a byte count the header does not carry; corrected,
  it reads the byte length of `gov_map.py`'s stdout. Observed by AC48.
- **S49** — id 20. The playbook kit's reach into `design_lib.py` is `TOOL-dTotalRecall-22`'s own, PLAY-
  dOrderedCharter-24 S7 being DEFERRED at base: `tools/playbook/kit.toml` declares it as a `requires_if`
  row for `memory-tree` naming `edge_grammar.py --cardinality`, beside S45's refusal. Observed by AC49.
- **S50** — id 21. The module docstring of `policy_value.py` states the adapter's
  reason: memory-tree's `requires` is empty, so a sibling import must be optional and declared in
  `requires_if`, and the adapter keeps the policy read degradable where no policy kit resolves.
  Observed by AC50.
- **S51** — id 22. No shipped prose carries the stale count `1,443`; where the kit README or a guide
  states the `journal` population, it reads 2,025 PINNED with its command and date. Observed by AC51.
- **S52** — id 34. The `class` extractor of `record_extract.py` calls `gotchas.build_record(rel, text)`
  (`tools/memory-tree/gotchas.py:271`) and selects `kind == "class"`, so a gotcha with no `kind:` key
  reads as `gotchas.py` reads it (`:253`). Observed by AC52.
- **S53** — id 35. One result-byte counter, `read_result_bytes(records)` in `tools/runlog/extract.py`,
  called by `measure_agent_memory` (`TOOL-dTotalRecall-12` S4) and `measure_bytes_before_act`
  (`TOOL-dTotalRecall-17`). Observed by AC53.
- **S54** — id 47. The kickoff guide's `last-audit` (S35) is re-stamped once at this pass,
  after the last unit editing a watched path, its delta line naming the watched paths this build edited.
  Observed by AC54.
- **S55** — id 54. A degraded code record is never written to the per-tree cache; a later run on the
  same tree re-derives, and `--check` on a degraded run prints `degraded`. Observed by AC55.
- **S56** — id 55. The code record's cache hit is keyed on PLAY-dOrderedCharter-44's `blob_parsed` row
  for the `code` extractor, written when a blob yields no row, so an empty or unparseable blob is parsed
  once. Observed by AC56.
- **S57** — id 59. `record_kinds.py new` refuses, exit 2 with nothing written, a name or a tag segment
  after `record.` that does not match `[a-z0-9][a-z0-9-]*` whole, a tag that is not `record.<name>`, and
  a `--field` key holding `*`, `:`, a quote, a backslash or a line break; the field-key group applies
  only to a factory kind. The row is written through a serializer that escapes each string as a TOML
  basic string. Observed by AC57.
- **S58** — id 66. `check_stream_plan` reds a stream name given twice, a unit id that
  `grammar_for(root).ID_RE` does not match whole or that the build's README `ids:` does not define, and
  a second `toml` fence. Observed by AC58.
- **S59** — id 68. The counter's replay detection (`TOOL-dTotalRecall-3` §4 "The counter") reads the
  family ref's whole first-parent history in one `git log --first-parent` spawn, so a replay older
  than 64 mints returns its earlier result. Observed by AC59.

## 3. Non-goals (OUT)

- The seven highs: units 36 to 42.
- Editing a landed spec, frozen at CLOSED (§2).
- The report's suggested spec lints (§6 flags, Files touched, §10 seams): grading specs, not code;
  the close's left-shift step records each confirmed class under `memory/gotchas/` (M8).

### Edges

- **consumes-from** `TOOL-dTotalRecall-1` — `record_kinds.py`, `check_record_kinds`, `new`, the legacy row
- **consumes-from** `TOOL-dTotalRecall-2` — `gov_record.py`, its writer refusal, hand-row rewrite and mint
- **consumes-from** `TOOL-dTotalRecall-3` — the counter's replay detection and the claim row
- **consumes-from** `TOOL-dTotalRecall-4` — `parse_front_matter`, the build-readme row, the fixtures it refuses
- **consumes-from** `TOOL-dTotalRecall-5` — `id_grammar.py --readers` and its kept hits
- **consumes-from** `TOOL-dTotalRecall-6` — `check_relation_cycles`
- **consumes-from** `TOOL-dTotalRecall-7` — the ask row
- **consumes-from** `TOOL-dTotalRecall-8` — `policy_value.py` and `code_record.py`
- **consumes-from** `TOOL-dTotalRecall-9` — `record_extract.py`, the `sections` column and `record_find.py`
- **consumes-from** `TOOL-dTotalRecall-10` — `derive_anchor` and its callers
- **consumes-from** `TOOL-dTotalRecall-11` — the shape-run row and its leg
- **consumes-from** `TOOL-dTotalRecall-12` — `memory_measure.py`'s path match and byte counter
- **consumes-from** `TOOL-dTotalRecall-13` — `BUILTIN_ARMED` and `read_defs_at`
- **consumes-from** `TOOL-dTotalRecall-14` — `gov_map.py` and its cache
- **consumes-from** `TOOL-dTotalRecall-16` — the purpose review and its write
- **consumes-from** `TOOL-dTotalRecall-17` — `measure_bytes_before_act`
- **consumes-from** `TOOL-dTotalRecall-18` — the column grammar, `canonical_kind`, `GIT_OWN`, the rename's prose
- **consumes-from** `TOOL-dTotalRecall-19` — `--caused-by`, `legacy-records` and the anchor reader
- **consumes-from** `TOOL-dTotalRecall-20` — the retag and front-matter steps
- **consumes-from** `TOOL-dTotalRecall-21` — `build_fts_rows`, `fts_blob`, `query.py`'s connections, the kit's
  `requires`
- **consumes-from** `TOOL-dTotalRecall-22` — `edge_grammar.py --cardinality` and its leg
- **consumes-from** `TOOL-dTotalRecall-23` — `leg_row` and `LEG_READERS`
- **consumes-from** `TOOL-dTotalRecall-25` — `check_stream_plan` and the stream-plan token
- **consumes-from** `TOOL-dTotalRecall-26` — `gen_atlas.py` and its leg
- **consumes-from** `TOOL-dTotalRecall-38` — the widened `--readers` split shapes
- **consumes-from** `TOOL-dTotalRecall-40` — the alias census
- **consumes-from** `TOOL-dTotalRecall-41` — `check_row_value`
- **consumes-from** `TOOL-dTotalRecall-42` — `derive_record_kind`
- **hands-off** `TOOL-dTotalRecall-52` — S19's merged `record-kinds-legacy` registration, which that unit keys by path, section and check (units 36 to 43's round-1 audit, id 37)
- **hands-off** `TOOL-dTotalRecall-53` — the kept marker, the homeless arm, the path match, `GIT_OWN` and the merged ledger, which that unit extends (units 36 to 43's round-1 audit, ids 9, 12, 26, 29, 49, 50, 51 and 52)
- **hands-off** `TOOL-dTotalRecall-60` — the `# slug-grammar: kept` lines S14 writes, which that unit re-marks in unit 53 S34's grammar (units 44 to 53's round-1 audit, id 27)

## 4. Design

### How the batch builds

One pass, after every unit is terminal. The items' write sets intersect on shared files (Files
touched), so BUILD-METHOD M6 keeps them one unit. Order: registry rows (S1, S3, S4, S9), code items
in unit order, then S29, S30, S31 and S54, each reading every earlier change.

### Inventory

Minted: the `homeless records` arm; `scan_cycles` (S18) and `check_line_break` (S37); the ledger
field `check`; `check_front_matter` (S20); the 44 params digest; `read_result_bytes` (S53); the marker
`# slug-grammar: kept`; S15's and S25's parity arms. Naming cells: S31 asks the lexicon.

### Files touched (estimate)

- `tools/memory-tree/record-kinds.toml`, `tools/memory-tree/record_kinds.py`
- `tools/memory-tree/tree_lib.py`, `tools/memory-tree/gov_record.py`, `tools/memory-tree/backlog.py`
- `tools/memory-tree/gen_build_index.py`, `tools/memory-tree/kit.toml`
- `tools/memory-tree/policy_value.py`, `tools/memory-tree/code_record.py`
- `tools/memory-tree/gov_map.py`, `tools/memory-tree/gen_atlas.py`
- `tools/memory-tree/record_extract.py`, `tools/memory-tree/record_find.py`
- `tools/memory-tree/record_causes.py`, `tools/memory-tree/id_grammar.py`
- `tools/memory-tree/gov-claim.sh`, `tools/memory-tree/check-memory-hygiene.test.sh`
- `tools/memory-tree/corpus_ids.py`, `tools/memory-tree/migrate_backlog.py`
- `tools/lib/extract_code.py`, `tools/lexicon/extract_code.py`, `tools/codebase-map/extract_code.py`
- `tools/memory-tree/extract_code.py`, `tools/runlog/memory_measure.py`, `tools/runlog/extract.py`
- `tools/runlog/model.py`, `tools/playbook/tag_index.py`, `tools/playbook/edge_grammar.py`
- `tools/playbook/kit.toml`, `tools/memory-recall/query.py`, `tools/memory-recall/bench.py`
- `tools/memory-recall/union.py`, `tools/memory-recall/verbatim.json`
- `tools/memory-recall/selftest.py`, `tools/memory-recall/README.md`
- `tools/govkit/steps/memory_retag.py`, `tools/govkit/steps/memory_front_matter.py`
- `tools/govkit/subject-pins.tsv`, `tools/govkit/registry.toml`
- `tools/run-gates/ceiling-evidence.txt`, `tools/codebase-map/scen-adversarial.json`
- `tools/unattended/unattended.test.sh`, `tools/workflows/unattended-build.test.sh`
- `WIRE-INTO-PROJECT.md`, `memory/guides/SESSION-KICKOFF.md`
- `memory/map/features/` (the dossiers S29 claims legs in)
- `memory/map/generated/` (regenerated by `python tools/codebase-map/gen_map.py --write`)

Each further fixture S28's grep lists is added here as a rev bump before its edit.

### Alternatives rejected

- **Fold each minor into its unit's spec.** M4 refuses folding at the exit.
- **For S27, a `build_index` alias in `bench.py` keeping `union.py` byte-identical.** S2's grep then
  finds `B.build_index(` in `union.py`, and the name ask `TOOL-dTotalRecall-33` retires stays live.

## 5. Production-readiness checklist

- security — S37 and S57 add write-boundary refusals; S47 narrows a write surface; none widens one.
- perf / scale — S39 bounds the index; S56 parses an empty blob once; S59 adds a spawn per mint.
- error / empty / loading states — S38 names a busy index; S45 refuses a missing kit; S42 re-renders.
- observability — S39's freed rows; S1's homeless paths; each refusal names its argument.
- risks — a row S19's merge of two shrink-only homes loses reds a legacy record; AC19 counts both.
- testing — AC1 to AC59 by the pass, S32 and S33 excepted; §7's arms at the close.
- migration — S19's ledger merge and S28's fixture edits, inside the tree.
- user docs — S26's runbook and S35's kickoff lines; no `help/` page covers these internals.

## 6. Acceptance criteria

Criteria are numbered by the item they observe; S32 and S33 carry none.

- **AC1** — When `python record_kinds.py --check` runs in a scratch copy holding a
  planted note file under the fixture's `memory/notes/` whose second line is `**Serves:** research X-a-1`, it exits 1
  naming that path under `homeless records`; at the tip it names none.
  Red when: a record outside `builds/` with no matching home passes.
- **AC2** — When `git grep -nE "(bench|B)\.build_index\(|def build_index" -- tools/memory-recall
  tools/memory-tree/row_grammar.py` runs at the tip, it prints nothing, and
  `git grep -n "def build_fts_rows" -- tools` prints one line.
  Red when: the FTS builder keeps its old name anywhere in recall.
- **AC3** — When `python record_kinds.py --check` runs at the tip, it names none of the
  rows `shape-run`, `ask`, `claim` and `build-readme`, and a `tomllib` probe reads `layer.memory` and a
  closed-set `lifecycle` on each.
  Red when: a row keeps `layer = "memory"`, a prose lifecycle or a directory home.
- **AC4** — When a `tomllib` probe counts the registry entries covering `deviation`, it counts one, and
  `python gov_record.py new deviation --build <slug> --unit <id> --caused-by <id>`
  in a scratch clone under `%TEMP%` exits 0.
  Red when: two rows cover the kind, or the door refuses its own factory kind.
- **AC5** — When `python record_kinds.py --check` runs at the tip, it prints each
  `fields` kind's graded and legacy counts, and the `deviation` legacy count is above zero.
  Red when: a `fields` row grades no record for want of a home.
- **AC6** — When the retag step's `up` runs over a fixture record repeating `## Notes`, the record
  carries `## [section.notes-2] Notes`, and `extract_section` from `record_extract.py` over it finds
  `section.notes-2`.
  Red when: the retag writes a bare `[notes-2]` the extractor does not read as authored.
- **AC7** — When `python gov_record.py new log --build <slug> --unit <id>` runs with
  no `--caused-by` in a scratch clone, it exits 2 naming `log` and `Caused-by`; with `--caused-by <id>`
  it exits 0.
  Red when: the command fails at argument parsing instead of at the cause refusal.
- **AC8** — When a `tomllib` probe reads the `log` row, its `writer` is `gov_record.py new log`, and
  `python record_kinds.py --check` names no line of `gov_record.py` under the alias
  census.
  Red when: the door's rewrite looks for a row named `journal` and leaves `log`'s writer `hand`.
- **AC9** — When a `python -c` probe runs `read_bindings` from `tools/memory-tree/tree_lib.py` over a
  planted record opening `**Serves:** stream-plan X-a-1`, it classifies the kind `stream-plan` and marks
  nothing malformed.
  Red when: the token is unregistered and the record reads as malformed.
- **AC10** — When `python gov_map.py` runs in a scratch copy with `tools/playbook`
  absent, it exits 2 naming the playbook kit; `grep -n "playbook" tools/memory-tree/kit.toml` prints the
  `requires_if` row naming the three modules.
  Red when: the module crashes on import or runs with no index.
- **AC11** — When `git grep -n "policy_value" -- '*gen_atlas.py'` runs at the tip, it
  names the memory-tree adapter and no `tools/playbook/` path.
  Red when: the atlas imports the playbook kit's reader.
- **AC12** — When `git grep -n "policy_value" -- '*gov_map.py'` runs at the tip, it names
  the memory-tree adapter and no `tools/playbook/` path.
  Red when: the map reads its two keys through the playbook kit.
- **AC13** — When `record_extract.py`'s `record` extractor runs over a fixture `build/` folder holding a
  log, a research, a deviation and a shape-run record, each row's tag is `record.<its Serves kind>`.
  Red when: two records under one folder take one kind from a shared home.
- **AC14** — When `python id_grammar.py --readers` runs at the tip, it prints no line
  carrying `# slug-grammar: kept`, and with one unmarked planted slug regex in a scratch copy it prints
  that line.
  Red when: a kept hit still prints, or the marker silences an unmarked one.
- **AC15** — When a `python -c` probe compares `BUILTIN_ARMED` from `extract_code.py` in the gov lib dir with
  `KNOWN_EXTS` from `tools/lexicon/lexicon.py`, they agree for every extension, `js` mapping to
  `("js-regex", "probe")`.
  Red when: JavaScript is armed under `ts-tokens` with no measured verdict.
- **AC16** — When `memory_measure.py`'s path match reads the fixture words
  `C:\Users\u\.claude\projects\p\memory\MEMORY.md` and the plant `msys-path`, a note under this
  clone's `memory/` spelled from its MSYS drive root, the first counts zero and the second
  counts.
  Red when: the harness's auto-memory directory counts as a memory read.
- **AC17** — When the same match reads `memory` alone and the plant `foreign-memory-path`, a note under
  another repository's `memory/`, the bare root counts and the foreign path counts zero.
  Red when: any absolute path holding `/memory/` counts.
- **AC18** — When an `ast` probe lists the functions under `tools/memory-tree/` that walk a graph for
  cycles, it lists one, `scan_cycles`, called by the ask-hold check and by `check_relation_cycles`.
  Red when: a second walker is found.
- **AC19** — When a `tomllib` probe reads the `[[ledger]]` rows of `tools/memory-tree/kit.toml` at the
  tip, one registration keyed by record path and section exists, `record-kinds-legacy`, and its home's
  rows counted per `check` value, `kind-schema` and `causes`, equal the two homes' row counts at the
  pass base.
  Red when: the merge loses a row, or two registrations remain.
- **AC20** — When a planted legacy README typing `node: d` is graded by
  `memory_front_matter.py` and by `python tools/memory-tree/gen_build_index.py
  --check` in a scratch copy, both exit 0; outside the legacy population both refuse it.
  Red when: the step prints `node derived` on a README hygiene accepts.
- **AC21** — When a `python -c` probe with `sqlite3` lists the index's tables after `build_index` at the
  tip, no `leg_row` table exists, and editing the `unfenced-head` reader's module in a scratch copy
  makes the next `build_index` re-run it through `blob_parsed`.
  Red when: the leg readers keep their own freshness table.
- **AC22** — When the same probe lists the tables, no `fts_blob` table exists, and changing
  `CHUNK_MAX` in a scratch copy re-extracts each corpus blob once through `blob_parsed`.
  Red when: recall keeps its own staleness rule beside the extractor ledger.
- **AC23** — When a fixture deviation record lacking `- **Caused-by:**` is graded by
  `python record_kinds.py --check` and by `deviation_join.read_record`, each reports
  the same missing field once.
  Red when: the gate grades the deviation fields with its own grammar.
- **AC24** — When `memory.map-purpose = "refuse"` is set in a scratch copy holding a chain row with no
  purpose, `gov_tag.py check`'s `purpose` arm reds it and `record_kinds.py --check` does not grade it.
  Red when: the two checks give opposite verdicts on one row.
- **AC25** — When the parity arm runs with one `SPEC_TITLE_NUMBERS` entry renamed in a scratch copy, it
  exits 1 naming the section; at the tip it passes, and the spec row reads `section.reuse-audit` not
  required for Tier-1.
  Red when: the column and the canon drift silently.
- **AC26** — When `grep -n "playbook" WIRE-INTO-PROJECT.md` runs at the tip, §0's recall line and §3c's
  copy steps name the playbook kit; and `python tools/memory-recall/query.py` in a scratch copy with no
  playbook kit exits non-zero naming it.
  Red when: the runbook pairs memory-recall with memory-tree alone.
- **AC27** — When a `python -c` probe hashes `bench.py` and `union.py` as
  `tools/memory-recall/selftest.py:1688-1708` does, both match `verbatim.json`, and the README's
  verbatim table names the `union.py` fork.
  Red when: the pins are stale, or the fork is unrecorded.
- **AC28** — When `git grep -lE '^(node|roster|streams): ' -- tools` runs at the tip, it lists only the
  plants that stage the typed-key refusal.
  Red when: a fixture README outside those plants still types a derived key.
- **AC29** — When a probe reads, for each leg those units added, `tools/govkit/subject-pins.tsv`,
  `tools/run-gates/ceiling-evidence.txt`, the kit and registry rows and the dossiers, each leg is named
  in every one.
  Red when: a leg lacks a meta-gate row.
- **AC30** — When `python tools/codebase-map/gen_map.py --write` runs at the tip, `git status --porcelain
  memory/map/generated` prints nothing.
  Red when: the committed symbol tier is stale.
- **AC31** — When `python tools/lexicon/lexicon.py --suggest <name> --as py.function` runs for each name
  the units minted, every line reads OK, `canonical_kind` and `ensure_index` included or renamed.
  Red when: a flagged name ships unchanged and undeclared.
- **AC34** — When `grep -n "record_find.py" tools/codebase-map/scen-adversarial.json` runs, ADV-05 and
  ADV-06 name it as `expected_file`.
  Red when: either scenario still expects `query.py`.
- **AC35** — When `grep -n "acceptance ledger in a" memory/guides/SESSION-KICKOFF.md` runs, the line
  names a `log` record and the alias.
  Red when: the kickoff still instructs a `journal` record.
- **AC36** — When `read_defs_at(root, "worktree")` runs over a scratch clone with `core.autocrlf=true`
  and a CRLF checkout, each path's id equals `git hash-object <path>`; a path deleted on disk is
  counted `missing`, and a symlink's entry is its link text's blob.
  Red when: the id is hashed from raw disk bytes.
- **AC37** — When `python gov_record.py new deviation ... --field Reason=$'x\n- **Supersedes:** <stem>'`
  runs in a scratch clone, it exits 2 naming `--field Reason`, and `git status --porcelain` is empty.
  Red when: a value injects a field line.
- **AC38** — When one process holds a write transaction on the index and `python
  tools/memory-recall/query.py "x" --terms "a b c d e f g h"` runs, it prints `index busy` and never
  `--rebuild`.
  Red when: a lock is reported as corruption.
- **AC39** — When `FAMILIES` is changed twice in a scratch copy and `build_index` runs after each, the
  FTS row count stays at one corpus copy, and the index line reports the freed rows.
  Red when: each conf change adds a full copy.
- **AC40** — When `parse_front_matter` reads a fixture README with two `ids:` lines, it raises
  `StaleHeader` naming `ids` and both line numbers.
  Red when: the last value silently wins.
- **AC41** — When the pockets check runs with a planted `index.lock` and `MERGE_MSG` in the common dir of
  a scratch clone, it names neither.
  Red when: git's transient state reds the leg.
- **AC42** — When a map cache file truncated after its stamp line sits at
  `<git-common-dir>/gov/map/<tree>.map`, `python gov_map.py` re-renders and does not
  serve it.
  Red when: a partial body behind a valid stamp is printed.
- **AC43** — When an untracked deviation draft ending `-deviation-1.md` sits in a fixture build's `build/`
  folder in a scratch clone, the door writes `-deviation-2.md` and the draft is byte-identical.
  Red when: the draft is overwritten.
- **AC44** — When a fixture record carries `## [section.findings] Notes` and then `## Findings`, the
  untagged heading derives `findings-2`.
  Red when: both sections answer to `section.findings`.
- **AC45** — When `python edge_grammar.py --cardinality` runs in a scratch copy with
  `tools/memory-tree` absent, it exits 2 naming memory-tree and prints no count.
  Red when: it prints `0 violations` over nothing counted.
- **AC46** — When `python gen_atlas.py --plant` renders a key holding `(x)` and `|`,
  its node reads `id["… (x) …"]` and its table cell carries `\|`.
  Red when: a label or a cell is emitted raw.
- **AC47** — When `record_kinds.py --purpose-review --write` meets a member whose purpose field sits in a
  rendered file in a scratch copy, it writes nothing there and drafts an ask naming the member.
  Red when: the review writes into a file its next render reverts.
- **AC48** — When `python gov_map.py | wc -c` runs at the tip, it prints at most
  `32768`.
  Red when: the map overruns its budget.
  figure: DERIVED at observation.
- **AC49** — When `grep -n "design_lib" tools/playbook/kit.toml` runs, it prints the `requires_if` row
  for memory-tree naming `--cardinality`.
  Red when: the reach is undeclared.
- **AC50** — When `python -c "import policy_value; print(policy_value.__doc__)"` runs from
  `tools/memory-tree/`, the docstring names `requires_if` and the empty `requires`, and not "imports no
  sibling kit".
  Red when: the docstring keeps the false reason.
- **AC51** — When `git grep -n "1,443" -- tools memory/HYGIENE.md memory/guides` runs at the tip, it
  prints nothing.
  Red when: the stale count ships in prose.
- **AC52** — When a planted gotcha with no `kind:` key is read by the `class` extractor and by
  `gotchas.py`, both count it as a class.
  Red when: the two parsers split on the missing key.
- **AC53** — When an `ast` probe lists the functions under `tools/runlog/` that sum tool-result bytes, it
  lists one, `read_result_bytes`, called by both measures.
  Red when: two counters remain.
- **AC54** — When `git log -1 --format=%H -- memory/guides/SESSION-KICKOFF.md` runs at the tip, that
  commit is later than the last commit touching any path on the manifest's `watch:` line, and the
  manifest's delta line names this build's watched paths.
  Red when: a watched path moved after the last re-stamp.
- **AC55** — When `python code_record.py` runs twice with `--ceiling 0.01` and then
  once with no ceiling on one tree, the third run re-derives fully, and `--check` after the first prints
  `degraded`.
  Red when: the degraded record is served from the cache.
- **AC56** — When the code record runs twice over a fixture holding an empty `__init__.py` and a `.py`
  with a syntax error, the second run parses neither blob.
  Red when: a blob that yields no row is parsed on every run.
- **AC57** — When `python record_kinds.py new widget --tag record.Widget` runs, and
  again with `--field 'a"b'`, each exits 2 and `record-kinds.toml` is byte-unchanged.
  Red when: an unvalidated name, tag or key reaches the registry.
- **AC58** — When the fixture plants `stream-name-twice`, `stream-foreign-unit` and `stream-two-fences`
  each in turn, `python record_kinds.py --check` exits 1 naming the case.
  Red when: a malformed plan reads green.
- **AC59** — When the counter fixture mints 65 times after a claimant's first mint and that claimant
  replays, `gov-claim.sh ask` returns the first result and pushes nothing.
  Red when: the replay is minted a second id.

## 7. Gates

`memory hygiene` · `build-index selftest` · `build README slot contract` · `format-guard self-test` · `pre-push run-log line` · `run-gates run-log line` · `verifier fan-out self-test` · `tier2-review self-test` · `review-join self-test` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `govkit refusal join` · `govkit acceptance matrix` · `row-grammar selftest` · `row-keyed merge driver replay` · `row-driver view refusal` · `check-arms selftest` · `harness arms (fail branches armed or pinned)` · `backlog migration selftest` · `routed commits name a specced unit` · `run-gates canary` · `corpus-ids selftest` · `unattended-build self-test` · `python resolver (behaviour + inline parity + idiom ban)` · `drift-audit records` · `runlog record schema` · `runlog selftest` · `lexicon naming predicates` · `lexicon selftest` · `codebase-map kit selftest` · `codebase-map coverage + freshness` · `memory-recall kit selftest` · `recall floor` · `recall floor arms` · `govkit selfcheck` · `govkit selftest` · `leg ceilings clear their evidenced maximum` · `kickoff-manifest ratchet` · `kit/dogfood doc parity` · `playbook render selftest`

New arm: tools/memory-tree/record_kinds.py · covers AC1 AC3 AC5 AC23 AC57 AC58 · the plants `homeless-record`, `row-grammar`, `owner-graded`, `bad-tag`, `bad-field-key` and the three stream plants, staged by cutting each arm in turn · none
New arm: tools/memory-tree/gov_record.py · covers AC4 AC7 AC37 AC43 · the plants `factory-alias`, `field-newline` and `untracked-draft`, staged by cutting `check_line_break` and the exclusive create · none
New arm: tools/lib/extract_code.py · covers AC15 AC36 · the `BUILTIN_ARMED` parity row and the CRLF worktree case, staged by arming `js` under `ts-tokens` · none
New arm: tools/runlog/memory_measure.py · covers AC16 AC17 AC53 · the path plants `harness-memory`, `msys-path`, `foreign-memory-path` and `bare-root`, staged by matching any `/memory/` · none
New arm: tools/memory-recall/selftest.py · covers AC38 AC39 · the held write transaction and the twice-changed conf, staged by mapping every `DatabaseError` to `--rebuild` · none

## 8. Open questions

- **F1 — Which binding line does a promoted unit carry?** Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`, the ruling that a chain spec run carries the units it adds; (b) a `part k/n`
  carry, redding the parts join, which veto 1 discards. RESOLVED (agent, 2026-10-26, delegated):
  (a), rung 3, `TOOL-dDeclaredLoop-36` §8 F1's precedent. widens: none · relaxes: none
- **F2 — How is the memory-tree kit's reach into the playbook kit's index declared (S10)?** Options:
  (a) a `requires_if` row naming the modules, each refusing by name where the kit does not resolve;
  (b) `requires = ["playbook"]`, breaking a memory-tree-only adopter; (c) a second module wrapping the
  index writer. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the kit's `requires_if` rows
  (§10) and S50's corrected reason. widens: none · relaxes: none
- **F3 — May this unit edit `WIRE-INTO-PROJECT.md` and `memory/guides/SESSION-KICKOFF.md` (S26, S35,
  S54)?** Options: (a) yes, under the build's grant, each edit stating a change cl-dClosedLoop-0232 or
  cl-dClosedLoop-0229 makes; (b) no, shipping a runbook and a kickoff the build left stale.
  RESOLVED (agent, 2026-10-26, delegated): (a), rung 5, the README's `may:` grant.
  grants: PLAY-dClosedLoop-3 WIRE-INTO-PROJECT.md §0 and §3c name the playbook kit beside
  memory-recall, and SESSION-KICKOFF.md names the `log` record · widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit's 59 minors: 46 MEDIUM
  (items M1 to M44) and 13 LOW (items L1 to L13).
- rev-2 · 2026-10-26 · §3 · the Edges block gains the hands-off mirror of TOOL-dTotalRecall-52, TOOL-dTotalRecall-53, each a consumes-from edge of a unit the round-1 spec audit of units 36 to 43 promoted; non-criterion prose cut to the size cap.
- rev-3 · 2026-10-26 · §3 · the Edges block gains the mirror of TOOL-dTotalRecall-60, each the other end of an edge a unit the round-1 spec audit of units 44 to 53 promoted wrote; non-criterion prose cut to the size cap.

## 10. Reuse audit

Each item extends the seam its finding names, cited at base `462d20f3` in its scope item where it
exists (S15, S18, S25, S52), plus `requires_if` (`tools/memory-tree/kit.toml:8`) for S10,
`parse_front_matter` (`tools/memory-tree/gen_build_index.py:402`) for S20 and S40,
PLAY-dOrderedCharter-44's `blob_parsed` for S21, S22 and S56, and each unit's module for the rest. The
reuse probes (`python tools/codebase-map/reuse_lookup.py "refuse a newline or separator in a backlog
row value before writing"` and five more, 2026-10-26) ranked name-stem neighbours only, and each name
§4 mints is a second caller's extraction of an existing rule.

Recall terms used: `python tools/memory-recall/query.py "how is a confirmed spec audit finding promoted to a repair unit ordered after the unit it repairs" --terms "promoted HIGH repairs order spec-audit disposal batched minors rescope add Derived PLAY-dClosedLoop-2 hands-off"`
