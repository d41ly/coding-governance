**Serves:** research TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92

# Round-13 fix brief — units 91 and 92's check hits, before the round-14 audit

The round-13 spec audit's disposal wrote TOOL-dWitnessedBar-91 and -92. Clear the findings below, changing nothing
else, so that `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` prints no dWitnessedBar finding and
the main loop's `python tools/check-spec-tokens.py` prints no dWitnessedBar hit.

- Units 91 and 92 are uncommitted at rev-1 and unaudited: edit them in place with no rev bump. Touch no other spec,
  no `order` verb and no deviation record. Do not commit, do not stage, and do not run the build-index generator.
  Your role admits the hygiene gate and the lexicon only. Keep each H1 at 255 bytes or less, line included.

## 1. Check 25 — TOOL-dWitnessedBar-91 S1

S1 is a §2 item whose words retire, replace, remove or rename a named thing. Where it truly retires a name, add a
`**Readers:**` clause in check 25's grammar: `by name:` then every reader that spells the name, by path, each found
by `git grep -n` at HEAD; then `by value:` and its value readers, or `NO VALUE READERS` and a reason; a reader not
yet in the tree is `READER NOT IN TREE` with the parent spec that creates it. Where it retires nothing, reword it so
it no longer reads as a retirement, keeping its meaning, and say which you chose.

## 2. Check-spec-tokens

- **[bar]** A criterion of TOOL-dWitnessedBar-92 names the suite `run-gates.gov.test.sh` as its observation, as a
  bare backticked path. Observe the code the unit changes on a staged break, a `--selftest` flag or a fixture
  instead (an `awk` or `grep` probe over the suite's text is a probe, not a run), and name the suite on a `New arm:`
  line in §7.

## The spec-token hits, verbatim

- memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-92.md [bar] `tools/run-gates/run-gates.gov.test.sh` — a bar or suite is not an acceptance observation: observe the checker on a staged break, a --selftest flag or a fixture; name the suite under New arm:; the bar and the suites run once, after the build is complete
