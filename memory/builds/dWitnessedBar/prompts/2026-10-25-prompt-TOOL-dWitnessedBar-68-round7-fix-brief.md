**Serves:** research TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73

# Round-7 fix brief — units 68 to 73's check hits, before the round-8 audit

The round-7 spec audit's disposal wrote TOOL-dWitnessedBar-68 to -73. Clear every finding below, changing nothing
else, so that `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` prints no dWitnessedBar finding and the
main loop's `python tools/check-spec-tokens.py` prints no dWitnessedBar hit.

- Units 68 to 73 are uncommitted at rev-1 and unaudited: edit them in place with no rev bump. Touch no other spec,
  no `order` verb and no deviation record. Do not commit, do not stage, and do not run the build-index generator.
  Your role admits the hygiene gate and the lexicon only.
- Report the byte count of TOOL-dWitnessedBar-51 (you do not edit it).

## 1. Check 25 — 68 S3 · 69 S1, S2 · 70 S1, S3 · 71 S3 · 72 S1, S3 · 73 S13, S15

Each is a §2 item whose words retire, replace, remove or rename a named thing. Where it truly retires a name, add a
`**Readers:**` clause in check 25's grammar: `by name:` then every reader that spells the name, by path, each found
by `git grep -n` at HEAD; then `by value:` and its value readers, or `NO VALUE READERS` and a reason; a reader not
yet in the tree is `READER NOT IN TREE` with the parent spec that creates it. Where it retires nothing (a staged
break a test plants, say), reword it so it no longer reads as a retirement, keeping its meaning, and say which.

## 2. Check-spec-tokens

- **[path]** A §6 criterion spells in backticks the full path of a file this build or a parent creates
  (`tools/run-gates/verdict_backends.py`, `tools/lib/legacy_ledger.py`), or a path inside a quoted Python literal
  (`json.load(open('tools/gate-legs.json'))`). Cite a created file by its basename in §6, keeping the full path in
  §2, §4 and Files touched; pass a read file as an argument read through `sys.argv`.
- **[bar]** A criterion of 71 and of 73 names the suite `tools/lib/resolve-python.test.sh` as its observation.
  Observe the code the unit changes on a staged break, a `--selftest` flag or a fixture, and name the suite on a
  `New arm:` line in §7.

## The spec-token hits, verbatim

- memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-68.md [path] `tools/run-gates/verdict_backends.py` — not tracked by git ls-files
- memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-69.md [path] `tools/run-gates/verdict_backends.py` — not tracked by git ls-files
- memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-69.md [path] `tools/run-gates/verdict_backends.py` — not tracked by git ls-files
- memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-71.md [bar] `tools/lib/resolve-python.test.sh` — a bar or suite is not an acceptance observation: observe the checker on a staged break, a --selftest flag or a fixture; name the suite under New arm:; the bar and the suites run once, after the build is complete
- memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-73.md [path] `tools/lib/legacy_ledger.py` — not tracked by git ls-files
- memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-73.md [path] `json.load(open('tools/gate-legs.json'))` — not tracked by git ls-files
- memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-73.md [bar] `tools/lib/resolve-python.test.sh` — a bar or suite is not an acceptance observation: observe the checker on a staged break, a --selftest flag or a fixture; name the suite under New arm:; the bar and the suites run once, after the build is complete
