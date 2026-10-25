**Serves:** research TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-62

# Round-3 fix brief — the promoted specs' check hits, before the round-4 audit

The round-3 spec audit's disposal wrote TOOL-dWitnessedBar-58 to -62 and folded hands-off edges into the specs
they name. Clear every finding below, changing nothing else, so that
`bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` prints no dWitnessedBar finding and the main
loop's `python tools/check-spec-tokens.py` prints no dWitnessedBar hit.

- Units 58 to 62 are uncommitted at rev-1 and unaudited: edit them in place with no rev bump. Touch no other spec
  and no deviation record. Do not commit, do not stage, and do not run the build-index generator. Your role admits
  the hygiene gate and the lexicon only; the specs are staged, so `--only 2,12,25` grades them in place.
- Report the byte count of TOOL-dWitnessedBar-51 (you do not edit it): it is at 48521 against the 49152 ceiling.

## 1. Check 25 — TOOL-dWitnessedBar-60 S3

A §2 item whose words retire, replace, remove or rename a named thing. Where it truly retires a name, add a
`**Readers:**` clause in check 25's grammar: `by name:` then every reader that spells the name, by path, each found
by `git grep -n` at HEAD; then `by value:` and its value readers, or `NO VALUE READERS` and a reason; a reader not
yet in the tree is `READER NOT IN TREE` with the parent spec that creates it. Where it retires nothing, reword it so
it no longer reads as a retirement, keeping its meaning, and say which you chose.

## 2. Check-spec-tokens

- **[bar]** TOOL-dWitnessedBar-58 names the runner `run-gates.sh` as a criterion's observation. Observe the code
  the unit changes on a staged break, a `--selftest` flag or a fixture, and name any suite on a `New arm:` line in §7.
- **[path]** TOOL-dWitnessedBar-62 spells two backticked tokens the path arm reads as paths no file at HEAD carries:
  `sub/.git` and a `memory/LIVE.md:tools/memory-tree/gen_build_index.py` pair. Keep a fixture path out of backticks
  or name it by a placeholder in prose, and write the pair as two backticked paths.

## The spec-token hits, verbatim

- memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-58.md [bar] `run-gates.sh` — a bar or suite is not an acceptance observation: observe the checker on a staged break, a --selftest flag or a fixture; name the suite under New arm:; the bar and the suites run once, after the build is complete
- memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-62.md [path] `sub/.git` — not tracked by git ls-files
- memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-62.md [path] `memory/LIVE.md:tools/memory-tree/gen_build_index.py` — not tracked by git ls-files
