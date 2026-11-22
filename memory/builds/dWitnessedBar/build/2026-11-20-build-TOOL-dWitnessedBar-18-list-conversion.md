**Serves:** journal TOOL-dWitnessedBar-18

# TOOL-dWitnessedBar-18 — the list conversion record

What each converted list held that the ledger row has no field for, and how many rows it held before and after (§2 S2, §8 F5). Each list was rewritten in place through the factory's `write_rows`, every key kept, each row its key fields, the count `1`, the build run's base sha `9e21ac760dc0` and `seeded`; `instructions-legacy.txt` was first moved by `git mv` from the playbook kit's directory to `memory/project/` (§8 F7). A row's key is its fields TAB-joined, as the factory prints it, and is written below as its fields joined by ` · `.

## Where a count moved

- No count moved: each list kept one row per legacy row, each read back through `read_ledger` with no malformed line at `9e21ac760dc0`.
- `positional-refs`: 38334 rows before and after (PINNED 2026-11-20, at `9e21ac760dc0`).
- `positional-producers`: 15 rows before and after (PINNED 2026-11-20, at `9e21ac760dc0`).
- `unpinned-facts`: 15216 rows before and after (PINNED 2026-11-20, at `9e21ac760dc0`).
- `instructions-legacy`: 33 rows before and after (PINNED 2026-11-20, at `9e21ac760dc0`).
- `landed-steps`: written new, one row per step id `upgrade_steps.py list --ids` prints in this pass's tree, 26 rows (DERIVED, the spec's 25 and this unit's own step), each `seeded` at `9e21ac760dc0`.

## The lines that left the files

- `instructions-legacy.txt`: its five-line `#` preamble, which named the list's grammar and its policy key; the page `tools/playbook/README.md` and the registration's header now say both.
- `positional-producers.txt`: its two-line `#` preamble and its four `# ` reason lines, each reason written below keyed by the rows it stood above. A later kept hit's reason is written by `ratchet.py widen positional-producers` into a widen record.

## The producer reasons, keyed by their rows

- Reason: narration of the old form: the line describes a `file:line` join, key or reader, and directs no citation
  - tools/memory-tree/HYGIENE.template.md · `check-method-carriers.sh`. Keyed on PATH alone, never `<path>:<line>`. It is per-repo and the kit
  - tools/workflows/README.md · candidate side prints how many of its confirmed rows carry no readable `file:line`, and is refused
  - tools/workflows/README.md · first backticked `file:line`). Recall from the two record eras is therefore in different units.
  - tools/workflows/check-review-join.sh · #   * COLLISION — two findings at one file:line (normal when two lenses read one function) collapse
  - tools/workflows/check-review-join.sh · # that join on a `file:line` STRING the skeptic has to reproduce byte-for-byte has two failure modes,
  - tools/workflows/check-review-join.test.sh · // The retired join was `verdicts[v.ref] = v`, which collided on a shared file:line.
  - tools/workflows/replay_scorer.py · Each item is `{id, path, line}`, path and line None when the item is UNSCORABLE; in `spec-audit`
  - tools/workflows/tier2-review.template.js · // (b) COLLISION — two findings at one file:line are entirely normal when two lenses read the same
  - tools/workflows/tier2-review.template.js · // integer id, never by `ref` (two findings at one file:line would collapse into one row).
- Reason: a read directive: the writer re-reads the line a finding already cites, and writes no citation
  - tools/roles/agents/gov-skeptic.agent.md · - Re-run the finding's evidence yourself: the command it names, or the path and line it cites.
  - tools/workflows/tier2-review.template.js · `Then re-run the finding's evidence under the PROBE POLICY above: run the command it names, or re-read the path and line it names, and say in \`reason\` what you observed.\n` +
- Reason: a citation of a document line: a record's line, whose suffix CODE_EXTENSIONS does not hold
  - tools/runlog/SKILL.template.md · `<path>:<line>`, a run-state line by its time and verb, a commit by its sha, or a journal line by
- Reason: main's merged narration of the file:line form, carried by the reconcile with origin/main at 47ed57fab (PLAY-dOrderedCharter-83)
  - tools/workflows/check-review-join.js · `its skeptic verdict on a \`file:line\` STRING loses findings to echo drift and COLLAPSES two ` +
  - tools/workflows/check-verifier-fanout.sh · # MSYS converts an absolute path only as a whole argument, so `<path>:<line>` reached node unconverted
  - tools/workflows/replay_scorer.py · """`<path>:<line>` of each pairing comprehension in the tracked `*.py` at and below `root`, this file excepted.
