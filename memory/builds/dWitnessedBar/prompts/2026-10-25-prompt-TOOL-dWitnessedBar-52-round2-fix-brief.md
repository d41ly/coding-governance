**Serves:** research TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57

# Round-2 fix brief — the promoted specs' check hits and unit 51's size, before the round-3 audit

The round-2 spec audit's disposal wrote TOOL-dWitnessedBar-52 to -57 and folded hands-off edges into the specs
they name. Clear every finding below, changing nothing else, so that
`bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` prints no dWitnessedBar finding and the main
loop's `python tools/check-spec-tokens.py` prints no dWitnessedBar hit.

- Units 52 to 57 are uncommitted at rev-1 and unaudited: edit them in place with no rev bump. A spec the disposal
  folded an edge into carries an uncommitted rev entry for that fold; an edit to it joins that entry, so extend that
  §9 line to say what moved, and bump nothing.
- Touch no deviation record. Do not commit, do not stage, and do not run the build-index generator. Your role
  admits the hygiene gate and the lexicon only; the specs are staged, so `--only 2,12,25` grades them in place.

## 1. Check 25 — retirements owe a Readers clause

- TOOL-dWitnessedBar-53 S1 · TOOL-dWitnessedBar-55 S1 · TOOL-dWitnessedBar-56 S2, S13, S15 ·
  TOOL-dWitnessedBar-57 S4, S13, S15.

Each is a §2 item whose words retire, replace, remove or rename a named thing. Where it truly retires a name, add a
`**Readers:**` clause in check 25's grammar: `by name:` then every reader that spells the name, by path, each found
by `git grep -n` at HEAD; then `by value:` and its value readers, or `NO VALUE READERS` and a reason. A reader not
yet in the tree is written `READER NOT IN TREE` with the parent spec that creates it. Where the item retires
nothing, reword it so it no longer reads as a retirement, keeping its meaning, and say which you chose.

## 2. Check-spec-tokens

- **[path]** A backticked path no file at HEAD carries, or a path spelled inside a quoted Python literal. Cite a
  file this build or a parent creates by its basename in §6 (keeping its full path in §2, §4 and Files touched), and
  pass a read file as an argument (`... tools/gate-legs.json` read through `sys.argv`), never inside the literal.
- **[bar]** A criterion names a suite (`run-gates.gov.test.sh`) as its observation. Observe the checker on a staged
  break, a `--selftest` flag or a fixture instead, and name the suite on a `New arm:` line in §7.

## 3. TOOL-dWitnessedBar-51 is over the size ceiling again

The round-2 disposal's folded edges took unit 51 to 50817 bytes against the 49152 ceiling. The ceiling is a class
row the owner moves, and M4 admits two minors units only over disjoint write sets, which unit 51 does not have (the
round-1 fix return's analysis stands). So trim unit 51's text that is not a criterion, a scope item or an edge, to at
most 47500 bytes, leaving room for one more round's folded edges: compress §4's design prose, merge §3 bullets that
hand the same token to several units into one bullet naming each unit, and shorten §10 to the seam, the terms and
the probe result. Every path in Files touched stays named. Report the final byte count.

## The spec-token hits, verbatim

- size join · 84 live spec(s) · ceiling 49152 from tools/template-size-limits.txt · largest unheld 50817 B memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-51.md · 6 held at a recorded high-water
- memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-56.md [path] `json.load(open('tools/gate-legs.json',` — not tracked by git ls-files
- memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-56.md [path] `tools/loop/guard.py` — not tracked by git ls-files
- memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-56.md [path] `tools/loop/guard.py` — not tracked by git ls-files
- memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-56.md [bar] `run-gates.gov.test.sh` — a bar or suite is not an acceptance observation: observe the checker on a staged break, a --selftest flag or a fixture; name the suite under New arm:; the bar and the suites run once, after the build is complete
- memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-57.md [path] `memory/project/shell-role.txt` — not tracked by git ls-files
- memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-51.md [size] `size <- memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-51.md` — 50817 bytes, 1665 over the spec ceiling 49152; split the spec or move history out of it
