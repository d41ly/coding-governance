**Serves:** research TOOL-dWitnessedBar-88

# Round-10 H1 pass — the spec writer's return

The returns of the agent dispatched from `memory/builds/dWitnessedBar/prompts/2026-10-25-prompt-TOOL-dWitnessedBar-88-2-spec-writer.md`, run direct/a83b8a35eb80a2e6c, one per stop, extracted from its transcript by script.

## Return 1

I shortened unit 88's H1 to 251 bytes, under the 255-byte limit. Only that one line changed in `memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-88.md`. There was no rev bump, and I committed nothing, staged nothing and did not run the index generator.

**TOOL-dWitnessedBar-88**, new H1:

### TOOL-dWitnessedBar-88 — the round-1 audit of units 79 to 84, 19 minors batched: quoted reasons answered, one return contract and pass-commit lookup, a derived owner on one line, a measure-keyed probe, arm spellings matched, hook directory guarded

- **Byte count:** 251 bytes including the line ending, measured with `head -n1 <spec> | wc -c`. The old line was 293.
- **Expected index row:** I removed 42 ASCII bytes and the em dash prefix is unchanged, so once you regenerate, the row should drop from 380 to about 338 characters, under the 350 cap.
- **Meaning kept:** each of the old title's points is still there in shorter form, covering scope items S1, S3, S5, S6/S18, S9, S10 and S11. I dropped "its" before "19 minors" and "the" before "hook directory".

I ran the memory hygiene gate afterwards and it still fails (exit 1):
- **Check 7** still flags `memory/builds/dWitnessedBar/README.md:177` at 380 characters against 350, and **check 9** reports that README as stale. That is expected: the index row is only rebuilt by `gen_build_index.py --write`, which the brief left to you.
- **Check 15 rule 1** flags four paths cited in `memory/builds/dWitnessedBar/BACKLOG.md` that point at nothing: lines 6, 9, 10 and 11. This was already failing before my edit and is outside this brief, so I didn't touch it.
