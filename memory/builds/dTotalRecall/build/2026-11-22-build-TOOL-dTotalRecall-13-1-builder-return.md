**Serves:** research TOOL-dTotalRecall-13

# TOOL-dTotalRecall-13 build pass 1 — the builder's return

The gov-builder return of `unattended-unit.js` run `wf_5898832a-aa0`, at base `a3d6d07ed`, pass commit `3dc09b861`, saved in substance.

## why

The spec was buildable as written. Every symbol, range, reader and path it cites was checked against the tree at base a3d6d07ed and all of them held. I built all of S1 to S9 and committed them as one pass commit with the trailers `Pass: TOOL-dTotalRecall-13` and `Co-Authored-By: Claude Opus 5`. The same commit sets the spec's status to CLOSED, dated 2026-11-22.

## summary

Built TOOL-dTotalRecall-13 and committed it as 3dc09b861 on base a3d6d07ed. I ran no gate leg, suite or bar. Every criterion was checked with a probe of this unit's own code, comparing the base's kit files (from `git archive a3d6d07ed tools`) against the tip's.

**What the commit does:**
- **New block.** The `extract_code` block is in tools/lib/extract_code.py and is copied byte-identical into tools/lexicon/extract_code.py and tools/codebase-map/extract_code.py. It holds the lexicon range from `ext_of` through `extract_text` except `resolve_pattern_sets`, plus `PATTERN_SETS`, and the map lexer range from `_IDENT_TOKEN_RE` through `_identifier_tokens`. A script moved both ranges, so no code byte changed. Comments the move made false were corrected.
- **New reader.** The block adds `BUILTIN_ARMED` and `read_defs_at(root, state, paths=None, cache=None, *, armed=None, sets=None)`. Its helpers are `read_state_listing` and `read_blob_batch`, both named from the lexicon's declared verbs and answered OK by `--suggest`.
- **Lexicon.** lexicon.py imports every moved name by an explicit list. `read_defs_at_sha` is now the thin adapter the spec gives.
- **Map.** map_lib.py imports the lexer from its kit's copy. `scan_shell_layer` imports `parse_shell_defs` from its own kit and no longer looks up the lexicon kit.
- **Drift-audit.** drift_report.py's `_read_defs_at_sha` is deleted and both callers use `lex.read_defs_at_sha`.
- **Wiring.** New `PARITY_ROWS` row `extract_code`. The `drift-audit selftest` guard gains `{prefix}/lexicon/extract_code.py`, rendered into gate-legs.json by leg_factory.
- **Verb pin.** `VERB_OFFENDER_PIN` is re-measured from 1421 to 1444, as `--measure` printed it. Its dated comment names 29 arrived and 6 left:
  - the 11 inherited offenders, all in dWitnessedBar's replay.py build record;
  - 18 arrivals: six names times three copies, the six being `ext_of`, `_python_defs`, `_probe_defs`, the nested `hits`, `_identifier_tokens` and the nested `_string`.
- **Regenerated and recorded.** gen_map and gen_build_index were re-run, the kickoff manifest was re-stamped (gate-legs.json is on its watch list), and the acceptance ledger was written.

**Results:**
- **AC1:** the parity arm's `blk` cut gives three equal 2138-line blocks, and a one-byte change in the codebase-map copy makes its cut differ.
- **AC2:** `read_defs_at_sha` returns 10920 pairs from both base and tip, and the sets are equal. (DERIVED, the builder's own run)
- **AC3 and AC7:** a fixture repo under %TEMP% read `f`, `g` and `h` from HEAD, the index and the worktree, each under its own blob id. The worktree id equals `git hash-object`. A missing revision returns `None`, and a file with a syntax error maps to the empty triple.
- **AC4:** the shell layer returns 2636 rows at base and tip, equal over untouched files. A scratch tree with no lexicon kit returns 2628 rows, which is the tip's rows less 8 under tools/lexicon/. (DERIVED, the builder's own run)
- **AC5:** the drift signal gives byte-equal JSON from base and tip, and `git grep _read_defs_at_sha -- tools/drift-audit` exits 1.
- **AC6:** token sets are equal over 30 mapped extensions, one unmapped extension and 29 corpus files. The ast probe finds no `_LEX_PROFILES` assignment left in map_lib.py.
- **AC8:** `py_reads.py --guards "drift-audit selftest"` lists the copy and exits 0; with that guard entry removed, the gap appears. No other leg's guard gaps changed.

**Owed to the close (these probes stand in for those runs):**
- Legs: `python resolver (behaviour + inline parity + idiom ban)` (AC1 over the committed files), `lexicon selftest` (AC3, AC7), `codebase-map kit selftest` (AC4), `python reads (a name never bound, an import outside its guard)` (AC8), `lexicon naming predicates` (S8's two-sided pin), and the rest of section 7.
- RED-first observations for the three `New arm:` lines:
  - the `extract_code` `PARITY_ROWS` row, staged by one byte changed in tools/codebase-map/extract_code.py;
  - the new `read_defs_at` arm in tools/lexicon/selftest.py, staged by reading the index through the worktree branch;
  - the new `shell layer: builds with no lexicon kit reachable` arm in tools/codebase-map/selftest.py, staged by restoring the `from lexicon import` line.
- Both new arms passed when I ran just their own code.

**Other things to know:**
- Two existing lexicon selftest patches targeted text that moved. I pointed them at extract_code.py; the commit's `Decided:` trailer records this.
- Risk for `recall floor`: all three copies are named extract_code.py, so the map's install-site scan treats each one as the canonical and counts none as an install site. Fan-in for the moved functions may therefore shift. The spec fixes the marker text, so I left it as written.
- Another session is editing specs 8, 16 and 18 and has untracked files in this same worktree. I left all of that out of the commit. I staged README.md with only my own rows, so its TOOL-16 row stays out.
- The pre-commit hook's build-index check failed the first attempt because of that session's unstaged edits. Re-running `gen_build_index.py --write` cleared it, and the commit then went through.
- gotchas.py `--for-diff HEAD~1..HEAD` printed 52 classes, and I acted on the relevant ones: (DERIVED, the builder's own run)
  - guard coverage: I compared every guarded leg's gaps, base against tip;
  - line-keyed registries: nothing keyed to the edited files by line;
  - encoding posture: new subprocess calls carry `encoding`;
  - naming: helpers use declared verbs.
- No probe or cleanup timed out. The only miss: removing the read-only git objects of one fixture under %TEMP% failed. That probe was only re-running the AC3/AC7 fixture for the two byte-identical kit copies, so nothing was lost.

Files: C:/projects/coding-governance/.claude/worktrees/unattended-dtotalrecall-ae256e/tools/lib/extract_code.py, C:/projects/coding-governance/.claude/worktrees/unattended-dtotalrecall-ae256e/memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-13-1-acceptance-ledger.md
