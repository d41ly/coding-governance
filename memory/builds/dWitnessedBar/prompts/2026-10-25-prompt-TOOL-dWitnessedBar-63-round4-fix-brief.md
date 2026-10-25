**Serves:** research TOOL-dWitnessedBar-63

# Round-4 fix brief — unit 63's check hits, before the round-5 audit

The round-4 spec audit's disposal wrote TOOL-dWitnessedBar-63, the batch of its 34 minors. Clear every finding below,
changing nothing else, so that `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` prints no
dWitnessedBar finding and the main loop's `python tools/check-spec-tokens.py` prints no dWitnessedBar hit.

- Unit 63 is uncommitted at rev-1 and unaudited: edit it in place with no rev bump. Touch no other spec and no
  deviation record. Do not commit, do not stage, and do not run the build-index generator. Your role admits the
  hygiene gate and the lexicon only; the spec is staged, so `--only 2,12,25` grades it in place.
- Report the byte count of TOOL-dWitnessedBar-51 (you do not edit it).

## 1. Check 25 — TOOL-dWitnessedBar-63 S13, S31, S34

Each is a §2 item whose words retire, replace, remove or rename a named thing. Where it truly retires a name, add a
`**Readers:**` clause in check 25's grammar: `by name:` then every reader that spells the name, by path, each found
by `git grep -n` at HEAD; then `by value:` and its value readers, or `NO VALUE READERS` and a reason; a reader not
yet in the tree is `READER NOT IN TREE` with the parent spec that creates it. Where it retires nothing, reword it so
it no longer reads as a retirement, keeping its meaning, and say which you chose.

## 2. Check-spec-tokens

- **[bar]** A criterion of TOOL-dWitnessedBar-63 names the suite `run-gates.gov.test.sh` as its observation. Observe
  the code the unit changes on a staged break, a `--selftest` flag or a fixture instead, and name the suite on a
  `New arm:` line in §7.

## The spec-token hits, verbatim

- memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-63.md [bar] `run-gates.gov.test.sh` — a bar or suite is not an acceptance observation: observe the checker on a staged break, a --selftest flag or a fixture; name the suite under New arm:; the bar and the suites run once, after the build is complete
