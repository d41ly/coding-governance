# TOOL-aMendedFleet-35 — the map's symbol tier reads shell definitions through the lexicon's tokenizer

**Status:** SPECCED · rev-1 · 2026-10-04 · node a · Tier-2 · base 7af5f564 · streams tooling · ratified 2026-10-04 · closes TOOL-aWeighedCompass-8 · order 35

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Shell carries this repo's gates, adopters and hooks, and the reuse probe cannot see one shell
function: every answer prints `unscanned layers: .sh`. The ask to fix it waited on a shell parser
that would not be the regex `map_extractors.py` refuses to ship; the lexicon kit landed one, the
tokenizer `parse_shell_defs`, a day later. This unit registers a shell layer in the map's
`SYMBOL_EXTRACTORS` that reads every product shell file through that tokenizer, re-renders the
symbol index, retires the `.sh` dark declaration, and rewrites the texts that still say shell is
dark. The review measured the effect at 102 unreachable phrases falling to 35.

## 2. Scope (IN)

- **S1** — `tools/codebase-map/map_extractors.py` gains `scan_shell_layer(layer, roots)` and a
  `kit-sh` row in `SYMBOL_EXTRACTORS` calling it over `SHELL_ROOTS`: the tool root, `.githooks/`
  and `skills/`. It walks each root as `python_symbols` walks one, with the map's skip set, reads
  every `*.sh` file through `parse_shell_defs`, and emits one `function` row per definition whose
  name does not start with `_`, the rule `python_symbols` applies to Python. Observed by AC1, AC2.
- **S2** — FAIL CLOSED. A file the tokenizer refuses raises `MapError` naming the file and the
  tokenizer's own message. A lexicon kit `resolve_kit_dir` cannot find raises `MapError`. A layer
  yielding zero rows raises, as `_live_py` does. None of the three ever yields a smaller index.
  Observed by AC3.
- **S3** — `memory/map/generated/symbols.json` is re-rendered by `gen_map.py --write` in the same
  pass, and the freshness leg's byte compare holds over it. Observed by AC1.
- **S4** — `RECALL_DARK_LAYERS` in `.codebase-map.conf` becomes the empty string, and its comment
  says that no layer is dark today and how a future uncovered layer is declared. Observed by AC4.
  **Readers:** by name: `tools/codebase-map/reuse_lookup.py` (`load_corpus`) and
  `tools/codebase-map/selftest.py` (`test_every_declared_layer_is_present_on_this_tree`).
  by value: `derive_layer_verdict` in `tools/codebase-map/reuse_lookup.py` compares the declared
  set against the derived one; with `.sh` covered and the declaration empty it reports nothing, and
  the selftest arm's loop over declared tokens runs zero times while its own non-empty assertion on
  the present set still binds.
- **S5** — The seven lines that say shell is dark are rewritten to the current fact, in six files:
  the comment above `SYMBOL_EXTRACTORS` in `tools/codebase-map/map_extractors.py`, the comment above
  `RECALL_DARK_LAYERS` in `.codebase-map.conf`, the "bash is recall-dark" bullet in
  `memory/map/features/codebase-map.md`, the `LANGS` comment in `.lexicon.conf`, the coverage-modes
  paragraph of the module docstring in `tools/lexicon/lexicon.py`, and the probe-taxonomy line in
  `tools/memory-tree/README.md`. Observed by AC5.
- **S6** — The reuse probe's coverage banner needs no code change: it is DERIVED, and once `.sh`
  carries symbols it prints that every present layer has an extractor. Observed by AC4.

## 3. Non-goals (OUT)

- Indexing private helpers. `TOOL-aWeighedCompass-13` owns whether `_`-prefixed names are indexed,
  for both languages at once; this unit keeps Python's rule.
- Shell files with no `.sh` suffix, such as the tracked `pre-push` hook. They are not a present
  layer by extension, so the banner claims nothing about them; covering them needs a shebang
  reader, which is another mechanism.
- Changing the reuse probe's ranking, its neighbour cap or its output size. The shortlist grows by
  about 1,060 distinct names; bounding what it prints is unit 36's.
- The codebase-map template, `map_extractors.template.py`. An adopter without the lexicon kit has
  no tokenizer to call, so the layer is this repo's project-owned row.
- Editing the node-local auto-memory note that says the probe cannot see shell. It lives outside
  the tree.

### Edges

- **hands-off** `TOOL-aMendedFleet-36` — the larger shortlist this layer produces; that unit's
  `--budget` default is measured after this one lands.
- **consumes-from** external — `parse_shell_defs` in the lexicon kit, already landed; without it
  there is no tokenizer and S2 raises.

## 4. Design

### Evidence

Read at base `7af5f564`, whose bytes for every file below equal HEAD's at `580dc980e`.

- `SYMBOL_EXTRACTORS` in `tools/codebase-map/map_extractors.py` holds `kit-py` and `kit-js`; its
  header comment says shell has no extractor and declares it dark. `_read_lexicon_verbs` in the same
  file already imports from the lexicon kit through `resolve_kit_dir`.
- `parse_shell_defs` in `tools/lexicon/lexicon.py` returns `(name, line)` pairs from a tokenizer,
  recognises the four definition forms, skips heredoc bodies, and raises `SyntaxError` on a file it
  cannot tokenize. Importing the module costs 0.08 s, PINNED on node a.
- A probe running `parse_shell_defs` over every tracked `*.sh`, PINNED 2026-10-04: 123 files, none
  refused. Under `SHELL_ROOTS` it read 117 files and 1,428 public definitions, 1,060 distinct names,
  886 of them in `*.test.sh` files. The six other files are repro scripts under `memory/builds/`.
- `memory/map/generated/symbols.json` held 2,130 rows in 252,238 bytes, about 118 bytes a row, so
  the layer adds about 170 KB. PINNED estimate, 2026-10-04.
- `python tools/codebase-map/replay-phrases.py` at base, PINNED 2026-10-04: 360 graded phrases,
  hit rate 0.689, hit@5 0.408, hit@10 0.464, 104 that cannot hit, 14.4 s against a 60 s ceiling.
- `build_reference_index` in `tools/codebase-map/map_lib.py` derives its roots and extensions from
  the symbol file list, and `_LEX_PROFILES` already strips shell comments and strings for `.sh`, so
  fan-in over shell references needs no change there.

### Mechanism

```python
SHELL_ROOTS = (TOOLS, ROOT / ".githooks", ROOT / "skills")

def scan_shell_layer(layer, roots):
    # resolve the lexicon kit as _read_lexicon_verbs does, but RAISE MapError when it is absent
    # walk each root with the map's skip set; for each *.sh, parse_shell_defs(text)
    # SyntaxError -> MapError("<layer>: shell parse error in <rel>: <message>")
    # keep names not starting with "_"; rows {"id", "kind": "function", "file": <posix rel>}
    # zero rows over all roots -> MapError, the _live_py liveness rule
```

### Inventory

- `scan_shell_layer` — cell `py.function`; `python tools/lexicon/lexicon.py --suggest scan_shell_layer --as py.function` answered OK.
- `SHELL_ROOTS` — a module constant of `map_extractors.py`.
- `kit-sh` — the new layer key in `SYMBOL_EXTRACTORS`.

### Rollout

The lexicon and memory-tree kit versions each move once, at the build's close, for the shipped
bytes S5 edits. Unit 36 sequences after this one and measures its default over the grown corpus.
Unit 16 also writes `tools/memory-tree/README.md`, at a different row.

### Files touched (estimate)

- `tools/codebase-map/map_extractors.py`
- `tools/codebase-map/selftest.py`
- `.codebase-map.conf`
- `memory/map/generated/symbols.json`
- `memory/map/features/codebase-map.md`
- `.lexicon.conf`
- `tools/lexicon/lexicon.py`
- `tools/memory-tree/README.md`

### Alternatives rejected

- **A same-line regex for `name()` and `function name`.** It is the extractor the header comment
  bans, and it reports the JavaScript function inside `agent-cap.test.sh`'s heredoc as shell.
- **Fail open to an empty layer when the lexicon is absent**, as the verbs inventory does. Here an
  empty layer re-darkens `.sh`, and with the declaration emptied the probe then refuses repo-wide;
  raising names the cause at the renderer instead.
- **Index only the tool root.** `.githooks/gate-env.sh` and the session-kickoff checker are product
  shell, and leaving them out while the banner claims `.sh` is covered would be a false claim.

## 5. Production-readiness checklist

- security — N/A: reads tracked shell sources through a tokenizer that never evaluates or expands.
- perf / scale — one tokenizer pass over 117 files at render time; the probe's reference scan reads
  about 117 more files per query, which AC6 bounds through the replay harness's own ceiling.
- error / empty / loading states — S2's three refusals; no state yields a smaller index silently.
- observability — the coverage banner reports no unscanned layer, derived from the corpus walk.
- risks — symbols.json grows by about 170 KB and every new public shell function now owes a
  `gen_map.py --write` in its commit, which the freshness leg reds without; the test helpers add
  common names such as `fail` to the shortlist, and the review measured the median rank of the first
  correct answer moving from 3 to 5.
- testing — a fixture arm in the kit selftest, declared in §7, and AC1 to AC6 run directly.
- migration — N/A: a regenerated artifact and one conf value.
- user docs — the dossier bullet and the memory-tree README line in S5.

## 6. Acceptance criteria

- **AC1** — When `python tools/codebase-map/test_codebase_map.py` runs after the pass, it passes,
  and `grep -c '"file": "skills/session-kickoff/manifest-check.sh"' memory/map/generated/symbols.json`
  prints a count of at least 1.
  Red when: the layer is registered but symbols.json was not re-rendered, which the byte compare
  reds, or the file carries no shell row.
- **AC2** — When `python tools/codebase-map/reuse_lookup.py "write the orientation card for a session"`
  runs, its candidates name `write_card` with `skills/session-kickoff/manifest-check.sh` among its
  files, and no candidate's name starts with `_` from a `.sh` file.
  Red when: the layer is absent, or a private shell helper is indexed.
- **AC3** — When a `python -c` call importing `map_extractors` from the kit directory calls
  `scan_shell_layer` on a scratch root holding one `.sh` file with an unterminated quote, it raises
  `MapError` naming that file; on a scratch root holding no `.sh` file it raises naming the layer.
  Red when: either call returns a list.
  fixture: two scratch directories under the run's scratchpad; the tree holds neither.
- **AC4** — When `python tools/codebase-map/reuse_lookup.py "anything"` runs, its banner line reads
  `unscanned layers: none` and stderr carries no `RECALL_DARK_LAYERS` note, and
  `grep -n '^RECALL_DARK_LAYERS=""' .codebase-map.conf` prints one line.
  Red when: the banner still names `.sh`, or the declaration still carries it.
- **AC5** — When `git grep -n -i -F -e "nothing for shell" -e "DECLARED RECALL-DARK" -e "bash is recall-dark" -e "DARK on purpose" -e "declares that language recall-dark" -e "In this repo **bash"`
  runs over the six files S5 names, it prints nothing.
  Red when: any of the seven lines it printed at base survives.
- **AC6** — When `python tools/codebase-map/replay-phrases.py` runs at the pass's commit and again
  in a throwaway clone checked out at its parent, the pass's run reports fewer phrases that cannot
  hit and a higher hit rate than the parent's, and exits 0 inside its own ceiling.
  Red when: the unreachable count is unchanged, which means the corpus never consumed the layer.
  fixture: a `git clone --local` under a short `%TEMP%` root.
  figure: DERIVED from the two runs; at base the harness read 104 unreachable and 0.689.

## 7. Gates

`codebase-map coverage + freshness` · `codebase-map kit selftest` · `codebase-map adopter e2e` · `codebase-map gate coverage` · `lexicon naming predicates` · `lexicon selftest` · `straggler-guard arms` · `govkit acceptance matrix` · `recall floor` · `recall floor arms` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

New arm: tools/codebase-map/selftest.py · a fixture root holding a public definition, a private one and a heredoc-embedded function, plus one untokenizable file, staged red by removing the underscore filter · none

## 8. Open questions

- **F1 — Which shell files does the layer read?**
  Options: the tool root only, matching the Python and JavaScript layers; the tool root plus
  `.githooks/` and `skills/`; every tracked `*.sh`. The second adds eight product files, so the
  banner's coverage claim holds for the product; the third adds six repro scripts from build
  records, which are evidence and not seams.
  RESOLVED (agent, 2026-10-04, delegated): the three product roots, `SHELL_ROOTS`.
- **F2 — Are `*.test.sh` definitions indexed?**
  Options: index them, as the Python layer indexes test modules; skip them, cutting 886 of 1,428
  rows and the regeneration they cost. Indexing keeps fixture builders reachable, and the review's
  measured gain was taken over the whole shell population.
  RESOLVED (agent, 2026-10-04, delegated): index them, by the same rule as Python.
- **F3 — What happens when the lexicon kit cannot be resolved?**
  Options: an empty layer, as the verbs inventory does; a `MapError`. See §4 Alternatives.
  RESOLVED (agent, 2026-10-04, delegated): `MapError`, S2.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the synthesis's item [#38], `map_extractors.py` and a
  tokenizer probe over every tracked shell file at base.

## 10. Reuse audit

The seams extended are `SYMBOL_EXTRACTORS` in `tools/codebase-map/map_extractors.py`, with its
`_live_py` liveness rule and `_read_lexicon_verbs`'s `resolve_kit_dir` import, and
`parse_shell_defs` in `tools/lexicon/lexicon.py`, called unchanged; `build_reference_index` and the
`.sh` lexical profile in `tools/codebase-map/map_lib.py` already serve fan-in. `python
tools/codebase-map/reuse_lookup.py "extract shell function definitions into the symbol recall
index"` ranked `python_symbols`, `scan_js_definitions` and `all_symbols` among its candidates, the
sibling layers this one copies; it printed `unscanned layers: .sh`, so the lexicon tokenizer was
found in source, not by the probe. Recall returned `TOOL-aWeighedCompass-8`, the ask this closes,
`TOOL-aProbedToolkit-7`, which found an emptied symbol tier invisible and motivates S2's zero-row
raise, and `TOOL-aWeighedCompass-13` on private helpers.

Where the report and the tree disagree: the report spoke of three stale "shell is dark" texts; the
tree holds seven lines in six files. Its 102 unreachable phrases over 335 now read 104 over 360,
because the phrase set grew.

Recall terms used: `python tools/memory-recall/query.py "why is shell dark to the codebase map
symbol index and what would cover it" --terms "shell recall-dark RECALL_DARK_LAYERS
SYMBOL_EXTRACTORS parse_shell_defs symbols.json tokenizer lexicon map_extractors fail-closed"`
