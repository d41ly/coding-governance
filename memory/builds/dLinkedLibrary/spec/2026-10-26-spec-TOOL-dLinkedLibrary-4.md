# TOOL-dLinkedLibrary-4 — the `gov:note` grammar, the generated annotation index, its resolve check and `gov:feature` anchors joined both ways with reuse entries

**Status:** DEFERRED · rev-3 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 12 · advances TOOL-dLinkedLibrary-26

**Carries:** cl-dClosedLoop-0241@0e5185f1 whole
**Carries:** node:policy-key.annotations.grammar
**Carries:** node:policy-key.annotations.resolve-scope
**Carries:** node:record-kind.annotation-index

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-88 TOOL-dLinkedLibrary-89 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91 TOOL-dLinkedLibrary-92 TOOL-dLinkedLibrary-93 TOOL-dLinkedLibrary-94 TOOL-dLinkedLibrary-95 TOOL-dLinkedLibrary-96 TOOL-dLinkedLibrary-97 TOOL-dLinkedLibrary-98 TOOL-dLinkedLibrary-99 TOOL-dLinkedLibrary-100 TOOL-dLinkedLibrary-101 TOOL-dLinkedLibrary-102 |
| [2026-10-26-build-TOOL-dLinkedLibrary-1-fix-return.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-fix-return.md) | research | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-23 |
| [2026-10-26-build-TOOL-dLinkedLibrary-1-reuse-scout-b.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-reuse-scout-b.md) | research | TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-1 |
| [2026-10-26-build-TOOL-dLinkedLibrary-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-spec-stage-returns.md) | research | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 |
| [2026-10-27-build-TOOL-dLinkedLibrary-4-deviation-41.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-4-deviation-41.md) | deviation | — |
| [2026-10-26-prompt-TOOL-dLinkedLibrary-1-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dLinkedLibrary-1-fix-brief.md) | research | TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-1 |
| [2026-10-26-prompt-TOOL-dLinkedLibrary-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dLinkedLibrary-1-spec-brief.md) | research | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 |
| [2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md](../reviews/2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 |

<!-- /gen:spec-records -->

## 1. Goal

Code annotations have no grammar, tags or index: 0 tag lines among 91,661 comment lines, cited ids
followed to their record within 3 calls 2.5% of the time, and nothing extracting the 6,540 id-bearing
comment lines (gap-mem-08); a comment can cite a record that never existed and no check sees it
(gap-mem-17). This unit lands the `gov:note` grammar and its one parser, a generated annotation index,
a resolve check over notes alone or every comment reference as `annotations.resolve-scope` says, and
`gov:feature` anchors joined both ways with the reuse entries, presence of a note governed by
`annotations.grammar`. Before any of it lands, drift-audit's shipped-evidence signal is re-checked so
a note's `refs=` never reads as "this unit shipped" (layer-memory `[annotations]`,
`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md:795-824`;
systems `[design-annotations]`, `2026-10-16-build-PLAY-dClosedLoop-1-systems.md:314-364`).

## 2. Scope (IN)

Preconditions this unit calls and does not build, each DEFERRED at base `5fede642` and landed before
this build run: the lexer block `tools/lib/extract_code.py` with `_LEX_PROFILES` moved into it and its
kit copies (TOOL-dTotalRecall-13 S1, S3, S6; the memory-tree copy TOOL-dTotalRecall-8 S2), the
memory-tree policy adapter `tools/memory-tree/policy_value.py` (TOOL-dTotalRecall-8 S10), the id
grammar `tools/memory-tree/id_grammar.py` (PLAY-dOrderedCharter-18 S1), the join factory
`tools/memory-tree/coverage_join.py` (PLAY-dOrderedCharter-19 S9), `TAG_RE` (PLAY-dOrderedCharter-19
S1), the edge-target form and the code-site adapter (PLAY-dOrderedCharter-24 S2, -28 S5), and the
record-kind factory `record_kinds.py new` (TOOL-dTotalRecall-1 S9). The reuse entries are
TOOL-dLinkedLibrary-1's, the `marker` namespace TOOL-dLinkedLibrary-12's.

- **S1** — The shipped-evidence signal re-checked first, in the unit's first commit. Signal 2,
  `signal_spec_status` (`tools/drift-audit/drift_report.py:713`, its record named
  `non_terminal_specs_cited_by_product_source`), reads a hit only on a line that does not carry a
  `gov:note` head line: its `git grep -l -w -F` (`:740`) becomes a `git grep -n -w -F` whose hits are
  kept per file when any hit line lacks `gov:note`, so a note's `refs=` is a pointer, never evidence
  that a unit shipped. The signal's `value` and `of` over the tree are read before and after the
  commit and must be equal, since no note exists at base. Observed by AC1 and AC2.
- **S2** — The grammar and its one parser, `parse_note_line(text)` in `tools/memory-tree/annotations.py`
  (I9), over the text of one comment line with its comment marker stripped:
  `gov:note <tag>[,<tag>…] — <definition> → <target> [refs=<ref>[,<ref>…]]`, `gov:feature <tag>` and
  `gov:end <tag>`. A tag fits `TAG_RE`, read through `resolve_kit_dir("playbook", "tag_index.py",
  here)`; an anchor's `<tag>` is one tag segment, the feature's `<name>`, and its node is `feature.<name>`, the spelling
  TOOL-dLinkedLibrary-1's entries and TOOL-dLinkedLibrary-19's nodes write
  (`anchors = ["gov:feature <tag>"]`); the definition is at most 80 characters; `<target>` is a unit tag, a repo path or a
  backticked command; each `<ref>` is an id or a repo path in PLAY-dOrderedCharter-24 S2's edge-target
  form, no space, comma or bracket inside it. It returns a `Note(word, tags, definition, target, refs)`
  or a `NoteRefused(rule)` naming the broken rule; no other module parses these lines. Observed by AC3.
- **S3** — The scan, `scan_annotations(root, rev=None)`: the candidate files are one `git grep -l -I
  -E "gov:(note|feature|end)\b"` over tracked paths outside the memory root, kept where the lexer has a
  profile for the file's extension or, for an extensionless file, for its shebang; each file's comment
  lines come from `extract_comment_spans(src, ext)`, which this unit adds to the lexer block (S4), and
  each comment line holding `gov:` is parsed by S2. A `gov:note` inside a string literal is not a row.
  Each row is `(path, line, word, tags, definition, target, refs, block_end)`, `block_end` the last
  line of the contiguous comment block the line opens. Observed by AC4.
- **S4** — The lexer's comment half, added to the canonical block in `tools/lib/extract_code.py` and
  its copies under their `extract_code` `PARITY_ROWS` row: `extract_comment_spans(src, ext)` yields
  `(line, text)` per comment line, strings excluded by the same single pass `_identifier_tokens` uses;
  a Python docstring's lines yield as comment text; and `resolve_lex_profile(path, src)` picks the
  profile by extension, else by a first-line shebang naming `sh`, `bash`, `python` or `node`. Observed
  by AC4.
- **S5** — The generated annotation index, record kind `annotation-index` (I3): `gen_map.py`'s
  `_artifacts` (`tools/codebase-map/gen_map.py:137`) gains `generated/annotations.json`, the rows of
  `scan_annotations` rendered by `render_annotation_index(rows)` in `annotations.py`, sorted by path and
  line, one JSON object per row, `[]` when the tree holds none; `gen_map.py --check` byte-compares it as
  it does `symbols.json`. The kind's row lands through `python record_kinds.py new annotation-index
  --tag record.annotation-index --writer generator:tools/codebase-map/gen_map.py --check
  "codebase-map coverage + freshness"`. Where the map is not installed there is no index file, and the
  checks of S6 to S8 read `scan_annotations` directly. Observed by AC5.
- **S6** — The grammar arm, `check_grammar(rows, value)`, under `annotations.grammar` read once per run
  by `read_policy_value("annotations.grammar", root)`: every row S2 refused is red with its path, line
  and rule; a note whose comment block holds a `MUST` or `NEVER` line carries `refs=`; a note's block
  holds no ISO calendar date (a four-digit year, a two-digit month and a two-digit day, dash-joined),
  since a date moves to the record `refs=` names. Under
  `voluntary`, the default, and `pushed-at-read`, only blocks that carry a note are graded; under
  `required`, every comment block a hunk touches since `resolve_compare_base(root)` must open with a
  `gov:note` head line, the touched blocks given by `derive_touched_blocks(root, base)`. Observed by
  AC3 and AC6.
- **S7** — The resolve arm, `check_resolve(rows, scope)`, under `annotations.resolve-scope` read by
  `read_policy_value("annotations.resolve-scope", root)`. The defined set is `derive_defined_ids(root)`,
  the definitions half of `build_source_cited_ids_with_no_record` (`drift_report.py:2214-2234`, ids on an
  anchor line under the memory root plus each spec's own H1, with the slug set) moved into
  `annotations.py` over `id_grammar.grammar_for(root)`; the drift builder imports it through
  `resolve_kit_dir("memory-tree", "annotations.py", here)`, its value and `of` unchanged. Under
  `notes`, every `refs=` id must be defined and every `refs=` path tracked. Under `every-comment-ref`,
  the default, so must every id the id grammar finds in any comment line of the scanned files whose
  slug some record anchors, and every `memory/` path such a line cites. Each unresolved citation is red
  with its path and line. Observed by AC7 and AC8.
- **S8** — The anchor arm, `check_feature_anchors(rows, entries)`, the entries read by
  `read_reuse_entries(root)` (`tools/memory-tree/reuse_entries.py`, TOOL-dLinkedLibrary-1 S1) with each
  one's state, joined both ways through `compute_coverage` from `tools/memory-tree/coverage_join.py`:
  every `gov:feature <tag>` line is named in the `anchors` of an entry, in any state, whose
  `reuse.tag` is `feature.<name>` with `<name>` that `<tag>` (LR-6: proposed, accepted, or rejected and kept); every `accepted` or
  `proposed` entry's `anchors` string is carried by a line in the tree; a second `gov:feature` line for
  one name is red; and an anchor in a file S3 cannot profile is red. It holds whatever
  `annotations.grammar` says (layer-memory:1087). Observed by AC9 and AC11.
- **S9** — The CLI. `tools/memory-tree/annotations.py` and its `check [--only <arm>]` verb, `ARMS` table
  and `--selftest` are TOOL-dLinkedLibrary-12's (its S5); this unit adds three `ARMS` entries,
  `grammar`, `resolve` and `feature`, each a named function (I10), and `--base <rev>`. Each finding
  prints `annotations: <arm>: <path>:<line> · <rule>`, the prefix TOOL-dLinkedLibrary-12 fixes, and
  each arm one summary line, `annotations: <arm>: <n> rows · <k> findings`, or `annotations: <arm>:
  unarmed: no gov:note or gov:feature line in the tree` while S3 finds no row; exit 1 on any finding,
  2 when a policy read refuses, naming the key. `--fixture --plant <case>` builds one plant's scratch
  repository, its `.governance/policy.toml` planted where a case names a value, and runs the arm;
  `--selftest` runs every plant. Observed by AC3 to AC9.
- **S10** — The code-site adapter of PLAY-dOrderedCharter-28 S5 in `tools/playbook/edge_grammar.py`
  reads a note's `refs=` segment by calling `parse_note_line` through `resolve_kit_dir("memory-tree",
  "annotations.py", here)`, its own parse of the segment deleted, its plants' verdicts unchanged.
  Observed by AC10.
  **Readers:** by name: the adapter's `refs=` parse is spelled only in `tools/playbook/edge_grammar.py`,
  which is READER NOT IN TREE at base, since PLAY-dOrderedCharter-28 lands it · by value:
  NO VALUE READERS — the adapter's edges are what its readers compare, and they are unchanged; at
  base a git grep for `refs=` over tools, skills and .githooks finds only shell variables of that
  name in the pre-push hook, its runlog suite and check-wiring, none reading a note.
- **S11** — The two keys. dGroundRules landed both catalogue rows (`tools/policy/catalogue.toml:345`
  `annotations.grammar`, `:1343` `annotations.resolve-scope`) with their allowed values, default and
  owner `dLinkedLibrary`; this unit adds no row: it fills each row's `summary` and a `usage` the row
  admits (`annotations.grammar = "required"`, `annotations.resolve-scope = "notes"`), drains both names
  from `tools/policy/unsummarised-keys.txt` with `python tools/policy/policy.py lists --write`, and
  regenerates `.governance/policy.json` with `policy.py mirror --write` in a second commit. Observed by
  AC12.
- **S12** — The guide. `tools/memory-tree/ANNOTATION-STYLE.template.md` and its render
  `memory/guides/ANNOTATION-STYLE.md`, moved together as `kit-dogfood-parity.test.sh:61` pairs them:
  A1's "no grammar … no marker … no gate" and A2's "a marker to filter on, a grammar … none of which
  exists" are amended to name the grammar of S2, the `annotations` leg, presence voluntary under the
  default value and required under `required`, and Signal 2's note filter of S1, which is what keeps
  A2's reason true. `help/annotations.md` is new, with a `help/README.md` row: how to write a note and
  an anchor, the two keys and their values, and what each check refuses. Observed by AC13.
- **S13** — The kit versions move with their shipped bytes: memory-tree's `KIT_MEMORY_TREE_VERSION`
  (`tools/memory-tree/check-memory-hygiene.sh:69`) and its `gov:kit` markers, `KIT_CODEBASE_MAP_VERSION`
  (`tools/codebase-map/map_lib.py:49`) and `KIT_DRIFT_AUDIT_VERSION` (`drift_report.py:95`).
  NOT OBSERVED by a criterion: the `kit epoch (shipped bytes move, the version moves)` and
  `kit version markers` legs grade it at the close.
- **S14** — Three `[[marker]]` rows in TOOL-dLinkedLibrary-12's registry `tools/memory-tree/marker-words.toml`:
  `note` and `feature` (`kind = "marker"`, `reader = "tools/memory-tree/annotations.py"`, `reads` naming
  `parse_note_line` and the arm that grades it) and `end` (`kind = "pair"`, the same reader, `reads`
  naming `parse_note_line` and TOOL-dLinkedLibrary-17's span arm), each `owner =
  "TOOL-dLinkedLibrary-4"`. Observed by AC14.

## 3. Non-goals (OUT)

- The `annotations` leg, the lookup and the read hook, `pushed-at-read`'s firing on shell reads among
  them: TOOL-dLinkedLibrary-7's. This unit reads `pushed-at-read` as `voluntary` for the grammar arm.
- The span rule, `gov:end <tag>`'s pairing and its refusals, and the typed edges a note emits:
  TOOL-dLinkedLibrary-17's. S2 parses `gov:end <tag>` as a line and pairs nothing.
- The legacy of the resolve arm, the touched-block budget and the untouched long blocks:
  TOOL-dLinkedLibrary-11's. Until that unit lands, the resolve arm's findings under
  `every-comment-ref` are printed by the CLI and no leg runs it.
- The marker namespace, its registry and the unregistered-word check: TOOL-dLinkedLibrary-12's; this
  unit adds the `note`, `feature` and `end` rows to its registry (S14), as that unit hands them here.
- The reuse entries, their states and their proposal path: TOOL-dLinkedLibrary-1's; S8 reads their
  `tag` and `anchors` fields only.
- A 30-block mutation probe and the load the head lines add: layer-memory lists them as tests owed by
  the build, and neither is in this clause; they are measured once notes exist, by the leg's unit.
- Rewriting the 6,540 id-bearing comment lines into notes. Presence stays voluntary under the default.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-12` — `marker`, the registry `marker-words.toml` this unit adds the `note`, `feature` and `end` rows to, and `annotations.py`'s `ARMS` table its three arms join; without them `check_marker_words` reds all three words
- **consumes-from** `TOOL-dLinkedLibrary-1` — `reuse.toml`, the entries whose `tag` and `anchors` fields S8 joins both ways with the `gov:feature` lines
- **consumes-from** `TOOL-dLinkedLibrary-19` — `feature.<name>`, the node a `gov:feature <tag>` anchor names, the dossier header's feature node
- **hands-off** `TOOL-dLinkedLibrary-17` — `parse_note_line`, with `scan_annotations` and each row's `block_end`, over which the span rule pairs `gov:note` and `gov:end <tag>`
- **hands-off** `TOOL-dLinkedLibrary-11` — `parse_note_line`, with `check_resolve`, `derive_defined_ids` and `derive_touched_blocks`, whose findings and touched blocks that unit's legacy populations and budget read, and whose `derive_defined_ids` is left with `check_resolve` its one caller when that unit deletes the drift builder S7 re-points at it
- **hands-off** `TOOL-dLinkedLibrary-15` — `parse_note_line`, the one parser of a `gov:note` line (S2), which that unit's enrichment reads under `in-code-notes`
- **hands-off** `TOOL-dLinkedLibrary-7` — `parse_note_line`, with `check_grammar`, `check_resolve` and `check_feature_anchors` behind `annotations.py check`, the CLI the leg runs, and `annotations.json` for the lookup's map arm; and `pushed-at-read`, whose hook is that unit's
- **consumes-from** external — dTotalRecall's lexer block and policy adapter (TOOL-dTotalRecall-13, -8), dOrderedCharter's id grammar, join factory, tag grammar and code-site adapter (PLAY-dOrderedCharter-18, -19, -24, -28), and the record-kind factory (TOOL-dTotalRecall-1 S9)
- **hands-off** external — the ask of §8 F3, that PLAY-dOrderedCharter-28 §3 names this build, not dTotalRecall, as owner of the `gov:note` grammar
- **hands-off** `TOOL-dLinkedLibrary-39` — `check_feature_anchors`, whose entry-to-anchor direction unit 39 narrows to accepted entries; this unit's ledger answers AC11 AMENDED (id 2)
- **hands-off** `TOOL-dLinkedLibrary-44` — `scan_comment_lines`, the default population unit 44 gives `check_resolve` under `every-comment-ref` (id 22)
- **hands-off** `TOOL-dLinkedLibrary-52` — `check_resolve`, whose defined set and citation cut unit 52 settles (ids 31, 68)
- **hands-off** `TOOL-dLinkedLibrary-64` — `--fixture --plant <case>` and `help/annotations.md`, the harness unit 64 keeps single and the page it completes (ids 5, 21 of the spec audit of units 37 to 53)

## 4. Design

### Evidence

- `git grep -n -E "gov:(note|feature|end)\b" -- tools skills .githooks` returns no line at base.
- Signal 2 (`drift_report.py:713-768`) reads `git grep -l -w -F <own id>` over `EVIDENCE_GLOBS` as
  "this unit shipped"; aKeyedAnnotation measured one appended SPECCED id driving it from `ok` to
  `OVER PIN` (`memory/builds/aKeyedAnnotation/build/2026-09-05-build-TOOL-aKeyedAnnotation-1-design-pass.md:26-29`),
  and its §6 names "the spec-status oracle could filter marked lines and keep its meaning" (`:270`).
- `build_source_cited_ids_with_no_record` (`drift_report.py:2204-2282`) is report-only (`gateable:
  False`), its definitions loop at `:2214-2234`, its citation scan over whole tracked non-memory text
  at `:2236-2250`, the slug discriminator at `:2252-2259`; its pin is
  `"source_cited_ids_resolving_to_no_record": 2` (`tools/drift-audit/drift_signals.py:308`) with a
  RATCHETS row at `:456-457`. drift-audit already requires memory-tree (`tools/drift-audit/kit.toml:14`),
  so it may import from memory-tree and memory-tree may not import from it.
- The lexer `_LEX_PROFILES` is at `tools/codebase-map/map_lib.py:663` at base (scout B's `:714` is
  stale) and strips comments; `DEFINITION_CARRYING_EXTS` is derived from it. codebase-map requires
  memory-tree (`tools/codebase-map/kit.toml:7`), so `gen_map.py` may import `annotations.py`.
- `compute_coverage` is at `map_lib.py:1404`, moving to `coverage_join` with PLAY-dOrderedCharter-19 S9.
- The catalogue rows are at `tools/policy/catalogue.toml:345-349` and `:1343-1347`, both on
  `tools/policy/unsummarised-keys.txt` (lines 7 and 9).
- The guide and its template are byte-paired by `tools/memory-tree/kit-dogfood-parity.test.sh:61`.

### The line

```
# gov:note feature.roles — renders each role file into an agent definition → tools/roles/README.md refs=TOOL-aOrientedCast-3,memory/DECISIONS.md
// gov:feature roles
# gov:end feature.roles
```

The em dash and the arrow are the grammar's two separators as systems.md:318 spells them; no ASCII
alternative is admitted, so one line has one spelling.

### The policy values

| Key | Value | What the arm does |
|---|---|---|
| `annotations.grammar` | `voluntary` (default) | grades each block that carries a note |
| | `required` | also: each comment block a hunk touches since the base opens with a note |
| | `pushed-at-read` | as `voluntary` here; TOOL-dLinkedLibrary-7's hook pushes on reads |
| `annotations.resolve-scope` | `notes` | `refs=` ids and paths of notes |
| | `every-comment-ref` (default) | also every id and `memory/` path in any scanned comment line |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `parse_note_line`, `scan_annotations`, `render_annotation_index`, `derive_touched_blocks`, `derive_defined_ids`, `check_grammar`, `check_resolve`, `check_feature_anchors` | functions, `annotations.py` | `py.function`, asked at the pass |
| `Note`, `NoteRefused` | classes, `annotations.py` | `py.class`, asked at the pass |
| `extract_comment_spans`, `resolve_lex_profile` | functions, the `extract_code` block | `py.function`, asked at the pass |
| `--base`, `--fixture`, `--plant`; the `grammar`, `resolve` and `feature` arms | flags and `ARMS` entries of `annotations.py` | none |
| `note`, `feature`, `end` | rows of `marker-words.toml` | none |
| `memory/map/generated/annotations.json` | generated file, `gen_map.py` | none |
| `annotation-index` | record kind row, `tools/memory-tree/record-kinds.toml` | none |
| the plants of §6 | fixture cases | none |

### Migration

None. No existing comment is rewritten: the 6,540 id-bearing lines stay prose, read by
the resolve arm under `every-comment-ref` and held, where they do not resolve, by
TOOL-dLinkedLibrary-11's legacy population.

### Rollout

Live at landing as a CLI; no leg runs it until TOOL-dLinkedLibrary-7 adds the `annotations` leg in the
same build run. Under the defaults a repository with no note sees the grammar and anchor arms print
`unarmed` and the resolve arm grade its existing comment citations.

### Files touched (estimate)

- `tools/memory-tree/annotations.py` (TOOL-dLinkedLibrary-12 creates it): S2, S3, S5's renderer, S6 to S9
- `tools/memory-tree/marker-words.toml`: S14's three rows
- `tools/lib/extract_code.py`, `tools/memory-tree/extract_code.py`, `tools/codebase-map/extract_code.py`,
  `tools/lexicon/extract_code.py`: S4, the block and its copies
- `tools/lib/resolve-python.test.sh`: the `extract_code` parity row's behaviour section gains the
  comment-span cases
- `tools/drift-audit/drift_report.py`: S1, S7's import; `KIT_DRIFT_AUDIT_VERSION`
- `tools/drift-audit/selftest.py`: S1's plant
- `tools/codebase-map/gen_map.py`: S5; `tools/codebase-map/map_lib.py`: `KIT_CODEBASE_MAP_VERSION`
- `memory/map/generated/annotations.json`: rendered by `gen_map.py --write`, never edited
- `tools/memory-tree/record-kinds.toml`: S5's row, written by `record_kinds.py new`
- `tools/playbook/edge_grammar.py`: S10
- `tools/policy/catalogue.toml`, `tools/policy/unsummarised-keys.txt`, `.governance/policy.json`: S11
- `tools/memory-tree/ANNOTATION-STYLE.template.md`, `memory/guides/ANNOTATION-STYLE.md` (its render):
  S12
- `help/annotations.md` (new), `help/README.md`: S12
- `tools/memory-tree/check-memory-hygiene.sh`: `KIT_MEMORY_TREE_VERSION`

### Alternatives rejected

- **The resolve arm in drift-audit.** drift-audit requires memory-tree and an optional kit cannot host
  a core gate; the definitions half moves the other way, so one function answers "is this id defined".
- **A `git grep` scan with no lexer.** A `gov:note` inside a fixture string reads as a note; the
  lexer's single pass already separates strings from comments.
- **The index as the only producer.** The index lives in the optional map (AN-1); the checks read
  the scan its rows are rendered from, so both hold one answer.
- **ASCII separators beside `—` and `→`.** Two spellings of one grammar are two parsers' worth of
  drift for no reader that needs them.

## 5. Production-readiness checklist

- security — no new write path into the tree beyond the generated index; the scan reads tracked blobs
  through `git grep` and the lexer with no shell, and a path is never interpolated into a command line.
- perf / scale — one `git grep -l` narrows the files, so the lexer runs only on files holding `gov:`;
  `derive_defined_ids` reads the memory root once per run, as the drift builder does today.
- error / empty / loading states — an empty population prints `unarmed`, never green; a refused policy
  read exits 2 naming the key.
- observability — every finding prints its arm, path, line and rule; each arm prints its row count.
- risks — `every-comment-ref` reds existing dangling comment citations until TOOL-dLinkedLibrary-11's
  legacy lands; no leg runs the arm before then.
- testing — the plants of §6 red and green; Signal 2's plant in drift-audit's selftest.
- migration — none.
- user docs — `help/annotations.md` and the guide, S12.

## 6. Acceptance criteria

- **AC1** — When `python tools/drift-audit/drift_report.py --json` runs over the tree before and after
  S1's commit, `non_terminal_specs_cited_by_product_source` reads the same `value` and `of` both times.
  Red when: the note filter changes the signal's population on a tree holding no note.
  figure: DERIVED at the pass; no note exists at base.
- **AC2** — When `python drift_report.py --json` runs in a scratch repository holding one OPEN spec and
  a product file citing its id only on a `# gov:note … refs=<id>` line, Signal 2's
  `non_terminal_specs_cited_by_product_source` reads 0, and with the same id on a plain comment line it
  reads 1.
  Red when: a note's `refs=` reads as shipped evidence, or the filter hides a plain citation.
- **AC3** — When `python annotations.py --fixture --plant note-grammar` runs `check --only grammar`, it
  exits 1 naming exactly the planted bad tag, the missing arrow, the 81-character definition, the
  `MUST` block with no `refs=` and the dated block, each with its line, and none of the valid lines.
  Red when: a malformed note passes, or a well-formed one is named.
- **AC4** — When `python annotations.py --fixture --plant scan-sources` runs, `scan_annotations`
  returns the note in a `.py` comment, the note in a Python docstring and the note in an extensionless
  file whose first line is a bash shebang, and no row for the `gov:note` inside a string literal.
  Red when: a string literal yields a row, or a shebang file is skipped.
- **AC5** — When `python tools/codebase-map/gen_map.py --check` runs after the pass, it exits 0 with
  `annotations.json` among the generated files; after one planted note is added and the file is not
  re-rendered, it exits 1 naming `annotations.json`.
  Red when: a stale index passes the byte compare.
- **AC6** — When `python annotations.py --fixture --plant grammar-values` plants a comment block a
  commit touches with no head line, `check --only grammar` exits 0 under a planted
  `annotations.grammar = "voluntary"` and `"pushed-at-read"`, and exits 1 naming the block under
  `"required"`.
  Red when: `required` admits an unheaded touched block, or `voluntary` demands one.
- **AC7** — When `python annotations.py --fixture --plant refs-dangling-id` and `--plant
  refs-dangling-path` run `check --only resolve`, each exits 1 naming the note's line and the
  dangling `refs=` target; with the target defined, each exits 0.
  Red when: a dangling `refs=` id or path passes.
- **AC8** — When `python annotations.py --fixture --plant scope-values` plants a plain comment citing
  an undefined id of a slug some record anchors, `check --only resolve` exits 0 under a planted
  `annotations.resolve-scope = "notes"` and exits 1 naming it with no policy file, the default
  `every-comment-ref`; a fixture-slug id no record anchors is named under neither.
  Red when: either value grades the other's population, or a fixture slug is named.
- **AC9** — When `python annotations.py --fixture --plant feature-no-entry` runs `check --only feature`,
  it exits 1 naming the anchor's tag; the plants `entry-no-anchor`, `feature-twice` and
  `feature-no-pack` each exit 1 naming the entry, the second line, and the unprofiled file; the plant
  `feature-joined` exits 0.
  Red when: an anchor with no entry, an entry with no anchor, a duplicate anchor or an anchor in an
  unreadable file passes.
- **AC10** — When `python edge_grammar.py --fixture` runs PLAY-dOrderedCharter-28 S7's malformed
  `gov:note` refs plant after S10, it exits 1 as before, and `git grep -n "refs=" -- '*edge_grammar.py'`
  shows no parse of the segment outside the call to `parse_note_line`.
  Red when: the adapter keeps a second parse of `refs=`, or its verdict moves.
- **AC11** — When `python annotations.py check --only feature` runs over the tree after the pass, it
  exits 0 and prints `unarmed` if neither an anchor line nor an entry exists, else the joined count.
  Red when: an accepted or proposed entry's anchor is carried by no line, or the arm prints a count
  over an empty population.
  figure: DERIVED at the pass from the entries `read_reuse_entries` returns.
- **AC12** — When `python tools/policy/policy.py get annotations.grammar` and `get
  annotations.resolve-scope` run in a repository whose policy file sets neither, they print
  `voluntary` and `every-comment-ref`, and after `policy.py lists --write` the summary list names
  neither key.
  Red when: a row is unsummarised, or a default differs from v2:1195 or v2:1356.
- **AC13** — When `grep -n "gov:note" tools/memory-tree/ANNOTATION-STYLE.template.md memory/guides/ANNOTATION-STYLE.md annotations.md`
  runs over the guide template, its render and the help page, each names the grammar of S2 and the
  `annotations` leg, and the template's A1 and A2 no longer read "no grammar defines it" or "none of
  which exists".
  Red when: the guide still says no grammar or gate exists, or its render differs from the template.
- **AC14** — When `python annotations.py check --only markers` runs over a scratch clone holding one
  planted `gov:note`, one `gov:feature` and one `gov:end` line, it names no unregistered word; with the
  `end` row deleted from `marker-words.toml`, it exits 1 naming `end`.
  Red when: a grammar word is missing from the registry.

## 7. Gates

`drift-audit selftest` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map coverage + freshness` · `codebase-map adopter e2e` · `lexicon selftest` · `python resolver (behaviour + inline parity + idiom ban)` · `playbook render selftest` · `govkit acceptance matrix` · `policy fixtures` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `memory hygiene` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

dGroundRules' `policy check` reads the two rows' summaries and the mirror's parity; the `annotations`
leg that runs S9's CLI is TOOL-dLinkedLibrary-7's, so neither is graded here as this unit's own.

New arm: tools/memory-tree/annotations.py · covers AC3 AC4 AC6 AC7 AC8 AC9 AC14 · its `--fixture` plants, each failing case staged by deleting the rule's predicate from its arm · none
New arm: tools/drift-audit/selftest.py · covers AC2 · the `note-refs-not-evidence` plant, staged by reverting Signal 2's grep to `-l` · none
New arm: tools/lib/resolve-python.test.sh · covers AC4 · the `extract_code` behaviour section's comment-span cases, staged by a string literal yielding a comment line · none
New arm: tools/codebase-map/selftest.py · covers AC5 · a stale `annotations.json` reds `--check` · none

## 8. Open questions

- **F1 — Where does the generated annotation index live, and who writes it?** Options: (a)
  `memory/map/generated/annotations.json`, written by `gen_map.py` from `scan_annotations` and checked by
  the map's byte compare, the checks reading the scan where the map is absent; (b) rows in the one
  index under the git common dir, written by an extractor beside TOOL-dTotalRecall-9's; (c) a committed
  file in the core memory tree. (b) is never committed, so "checked against a re-render" has nothing
  to compare, and (c) puts the map's index in the core, against AN-1's "part of codebase map tool
  index". RESOLVED (agent, 2026-10-26, delegated): (a), rung 1: the owner's AN-1 answer and the
  research's home "under `memory/map/`, queried … never loaded whole"
  (`2026-10-16-build-PLAY-dClosedLoop-1-research-annotations-a.md:153`), with one producer for both
  readers. widens: none · relaxes: none
- **F2 — Where does the resolve arm's id resolution live?** Options: (a) the definitions half of
  `build_source_cited_ids_with_no_record` moves into `annotations.py` and the drift builder imports it;
  (b) the arm calls the drift builder; (c) a second copy in `annotations.py`. (b) makes a core check
  require an optional kit that already requires memory-tree, a cycle; (c) is a second answer to "is
  this id defined". RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the most feature-rich
  survivor, and the tie-break's reuse of the seam M5 found: the drift signal's value is unchanged and
  layer-memory's "built on its function" holds. widens: none · relaxes: none
- **F3 — PLAY-dOrderedCharter-28 §3 gives the `gov:note` grammar to dTotalRecall.** v2's
  `cl-dClosedLoop-0241` and the packet's owned nodes give it to this build, and TOOL-dTotalRecall-9 §3
  agrees ("The annotations system … dLinkedLibrary's"). Options: (a) build it here and ask
  dOrderedCharter to correct its non-goal; (b) wait for dTotalRecall. RESOLVED (agent, 2026-10-26,
  delegated): (a), rung 1, v2 answers; the ask for the main loop to file: target build dOrderedCharter,
  accept PLAY-dOrderedCharter-28 §3 names dLinkedLibrary's TOOL-dLinkedLibrary-4 as owner of the
  `gov:note` grammar and its checks beyond `refs=`, and S5's code-site adapter reads `refs=` through
  `parse_note_line`. widens: none · relaxes: none
- **F4 — What does `required` require?** Options: (a) a head line on each comment block a hunk touches
  since the compare base, as the retrofit round settled
  (`2026-10-17-build-PLAY-dClosedLoop-1-retrofit.md:155`); (b) a head line on every comment block in
  the tree. (b) reds every existing block on the day an adopter switches the value. RESOLVED (agent,
  2026-10-26, delegated): (a), rung 1, the retrofit round's M25 revision. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 4, layer-memory `[annotations]`, systems
  `[design-annotations]` and `[answers]`, the research-memory-annotations candidate B tests, the
  aKeyedAnnotation design pass, v2:1195 and :1356, and scout B's row for this unit.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the bullets mirroring TOOL-dLinkedLibrary-39, TOOL-dLinkedLibrary-44, TOOL-dLinkedLibrary-52, promoted from the round-1 spec audit of the 25 unit specs; nothing else moved.
- rev-3 · 2026-10-27 · §3 · the Edges block gains the bullets mirroring TOOL-dLinkedLibrary-64, promoted from the spec audit of units 37 to 53; nothing else moved.

## 10. Reuse audit

The seams extended are `build_source_cited_ids_with_no_record` (`tools/drift-audit/drift_report.py:2204`),
whose definitions half moves into `annotations.py`; `signal_spec_status` (`:713`), narrowed by S1;
the lexer block's `_LEX_PROFILES` and single-pass scanner (`tools/codebase-map/map_lib.py:663`, moving
to `tools/lib/extract_code.py` with TOOL-dTotalRecall-13 S6), gaining its comment half;
`compute_coverage` (`map_lib.py:1404`, moving to `coverage_join` with PLAY-dOrderedCharter-19 S9);
`gen_map.py`'s `_artifacts` (`:137`); and the record-kind factory (TOOL-dTotalRecall-1 S9).
`python tools/codebase-map/reuse_lookup.py "parse a structured comment annotation line and resolve its
references"` ranked name stems (`parse` in `query.py`, `resolve`, `parse_args`, `resolve_kit_dir`,
`build_reference_index`); none parses a comment grammar, so no existing seam fits the parser and S2
adds it, while the resolution reuses the drift builder above. Scout B's row agreed on the drift seam and
the lexer; its `:714` for `_LEX_PROFILES` is stale (`:663` at base), and its count of a 35-id exemption
class (layer-memory:819-820) disagrees with the code, which drops fixture slugs with no waiver list
(`drift_signals.py:305-307`), the discriminator S7 keeps. The recall query returned scout B's row,
layer-memory `[annotations]` and the brief's row.

Recall terms used: `python tools/memory-recall/query.py "what grammar does a gov:note annotation line follow and how are its references resolved" --terms "gov:note gov:feature annotation grammar refs resolve check source-cited ids shipped-evidence signal reuse entry anchor"`
