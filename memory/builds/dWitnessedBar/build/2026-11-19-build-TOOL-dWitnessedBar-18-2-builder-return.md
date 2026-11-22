**Serves:** journal TOOL-dWitnessedBar-18

# TOOL-dWitnessedBar-18 — builder return 2 (run `wf_de850758-ca9`), a divergence, nothing committed

## Why

DIVERGENCE: §4 Migration and §5 contradict each other about how an empty list converts, and the code agrees with §5. §4 Migration says "An empty list, which `write_empty_lists` wrote at every target, converts to the header alone." The step it names is the adopter `[[upgrade]]` row on `tools/govkit/steps/registry_to_ledger.py` with a new `LEGACY` row. That row reaches `tools/memory-tree/convert_registry.py#derive_after` and then `#derive_converted_text`. For a home with no row, that function writes the header plus the factory's `# unarmed · dead probe · <sha>` line. It is never the header alone. `tools/memory-tree/legacy_ledger.py#read_home_state` reads that file as `unarmed`. It would read a header-only file as `armed`. §5 "error / empty / loading states" says "an empty list after conversion reads `unarmed` until its check is seen red". That matches the code and contradicts §4. Making §4 true would mean changing `derive_converted_text` for every unit-16 population. Files touched limits `convert_registry.py` to "its `LEGACY` table", and §10 reuses that program unchanged. So the build cannot satisfy the sentence as written. What the spec has to say: §4 Migration should say an empty legacy list converts to its header plus the `# unarmed · dead probe · <sha>` line that `derive_converted_text` writes, so it reads unarmed as §5 says. Then S5's `write_empty_lists` should be settled on the same state. As written it writes "the header where it wrote empty bytes", which reads armed and empty. A converted target's empty list would then read unarmed and a fresh target's would read armed. One sentence choosing which state a target's empty `positional-refs.txt` holds closes this. Secondary, a gap rather than a contradiction, for the same rev: S5 says a list holding rows with no registration naming it is refused with exit 2, but it does not say what a WRITER does with no registration. Examples: `positional.py producers --seed` or `writing_practice.py check pinned-facts --seed` at a tree with no govkit registry, where `write_rows` has no table to render a header from. One clause would stop the next builder guessing, for instance "a writer with no registration refuses with exit 2 naming the population, writing nothing". Every other claim probed holds; see summary.

## Summary

I stopped before writing any code. TOOL-dWitnessedBar-18's rev-7 spec says two things about an empty converted list that cannot both be true, so nothing is committed. The working tree is clean at the base, d912b77b25a887577fa4bd4d3269a14c0d252a01, and the full divergence is in `why`.

**The divergence:** §4 Migration says an empty list converts to the header alone. The step program it reuses, through `convert_registry.py#derive_converted_text`, writes the header plus a `# unarmed · dead probe · <sha>` line, which reads as unarmed. §5 says the same thing as the code. Making §4 true would change unit 16's landed converter, which is outside this unit's write set. The spec writer should also say how S5's `write_empty_lists` output for a new target should read, armed or unarmed, and what a list writer does when no registration names the list.

**Everything else I probed holds at the base:**
- Every path, symbol and flag S1–S7, §4, §8 and §10 cite exists as described. That includes the pinned lines `check-method-carriers.sh@91073d780040:65` (`"$M"/*) continue ;;`) and `check-memory-hygiene.sh@2ef59a33f96d:1044` (`F:positional-refs.txt) ;;`).
- `upgrade_steps.py` declares 24 step rows and 1 retired row naming a step id, so 25 distinct ids, matching §4's pin at 4fa55b94e.
- The four lists hold 38334, 15, 15216 and 33 rows, matching the pins, with no whitespace-padded field. (DERIVED from the builder's probe)
- Each list, given count 1, the run's base SHA 9e21ac760dc0a43d6ed007396922722ccee98d57 and `seeded`, parses through `legacy_ledger._parse_rows` with no refusal. `verbatim` covers the `ref` field of `positional-refs` only.
- The `[dOC-71 S3]` arms can be re-pointed to `core-pending.txt`, because govkit reads `include = []` as naming no source.

**Checks that ran, all read-only:**
- `git rev-parse HEAD`.
- `unattended.sh --brief`, which reported the brief already recorded and unchanged.
- A source read of each cited symbol.
- `git cat-file -p` on the two pinned blobs.
- A `python -c` probe of `read_steps` and `read_retired` over the working tree, standing in for `ratchet (both ways)`'s `landed-steps` seed.
- A `python -c` probe that parses each list as converted ledger rows, standing in for AC1 and AC3's `legacy_ledger.py read`.

No gate, suite or bar ran. `gotchas.py --for-diff` did not run because there is no commit to check.

**Owed at the close once the spec is revised and the unit rebuilt:**
- AC1–AC7.
- The `New arm:` `append-removed` plant in `ratchet selftest`, observed red and then green.

**Notes for the next builder:**
- New records under `memory/` are graded by `writing practice`'s pinned-facts arm and by the positional arm, so every count in them needs a pin and no unpinned file:line citation.
- The `gov_tag` fixture's ledger tables must be tracked in the scratch tree, because `read_registrations` reads `git ls-files`.
