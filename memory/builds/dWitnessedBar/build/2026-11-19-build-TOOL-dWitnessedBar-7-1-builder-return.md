**Serves:** journal TOOL-dWitnessedBar-7

# TOOL-dWitnessedBar-7 — builder return 1 (run `wf_83129641-dea`), committed 28edeaa0b

## Why

TOOL-dWitnessedBar-7 is built as rev-6 of its spec states it and is committed as one pass commit. It carries the `Pass: TOOL-dWitnessedBar-7` trailer, and the spec header moved INPROGRESS to CLOSED in that same commit. Before writing, I checked the spec against the tree and found no divergence. Every cited symbol exists. Check 23's ledger awk has the same text as the pinned blob 2c5ed1a3a960; only its line numbers moved, by 2. BUILD-METHOD.md measured 30717 bytes against a 30720 limit. loop.toml still held `command:test.seen-red`, and no kit.toml held a `[[command]]` row. The kickoff manifest re-stamp is the one path outside the spec's Files touched. The brief said to expect it, and I declared it with `--dispatch --writes memory/guides/SESSION-KICKOFF.md`, which was admitted.

## Summary

I built TOOL-dWitnessedBar-7 and committed it as 28edeaa0b on base 0b01f7ccd. No gate, suite or bar ran in this pass. The suite arms and their RED-first observations are owed at the close.

**What changed**
- `tools/memory-tree/tree_lib.py` gains `read_evidence_lines`, the `**Evidences:**` block walk taken out of `deviation_join.read_population`. `deviation_join.py` now calls it.
- `tools/memory-tree/seen_red.py` is new:
  - `read_seen_red_records` reads the seen-red lines of every tracked journal record.
  - `derive_owed_gates` finds the gates a build adds or changes.
  - `--build <slug> [--base <sha>]` joins the two. The base defaults to the `base:` fact in the build's RUN.md.
  - `--fixture --plant seen|unseen-gate|unseen-arm|bad-line|empty` runs the join over a scratch repository.
- Check 23's ledger awk in `check-memory-hygiene.sh` now closes an open answer at a `- seen-red` line, so that line's tokens join no criterion.
- `ratchet.py`: `ratchet (populated)` now admits an empty armed population when a seen-red line names its leg, and exits 2 on a malformed line. `EMPTY_TEXT` is reworded, the new plant is `populated-seen-red`, and both docstrings plus the kit README row say the same.
- The command factory wrote the `seen-red` row into the memory-tree `kit.toml`. In `loop.toml` the `item.test.seen-red` actor now names `command:memory-tree.seen-red`.
- The seen-red line's grammar is stated once, in the "Acceptance ledger" section of `HYGIENE.template.md` and its render `memory/HYGIENE.md`.
- M8's sentence in `BUILD-METHOD.template.md` and its render now records both observations as a seen-red line and names `seen_red.py --build <slug>` as the read-back. The file stays at 30717 bytes against its 30720 limit.
- `check-memory-hygiene.test.sh` gains fixture 149 for check 23 and an arm running the five seen_red plants.
- The commit also carries the re-rendered `symbols.json`, the `gen_build_index --write` outputs, `RUN.md`, the acceptance ledger and the kickoff manifest re-stamp.

**Checks that ran** (each stands in for the gate or suite named)
- AC1–AC4 and AC6: all five `seen_red.py --fixture --plant` cases gave the exits and lines the spec states: 0, 1, 1, 2 and 0. Stands in for the `memory-hygiene self-test` arm.
- AC5: `deviation_join.py --fixture --plant amended` printed identical bytes before and after the extraction (compared with `cmp`). Separately, check 23's awk, run on its own over a scratch ledger, kept the seen-red line's tokens out of the AC1 answer; the same line read as a continuation does join them. Stands in for `policy fixtures` and the check 23 fixture in the memory-hygiene self-test.
- AC8: the `populated-seen-red` plant, called in process, passed all three cases (exit 0 admitted, exit 1 empty, exit 2 naming the record), and `populated-empty-armed` still exits 1. Stands in for `ratchet selftest`.
- The new self-test block, run on its own with `hit` and the counters stubbed, gave 11 checks with 0 failed. Stands in for `memory-hygiene self-test`.
- AC7: the specified greps and `wc -c` (30717 against 30720). Stands in for `build-method size` and `kit/dogfood doc parity`.
- The factory's own `loop command conformance` came back green. `seen_red.py --build dWitnessedBar` over this repository exits 1 and names gates with no record.
- The naming lexicon passed every new name. I renamed one helper (`commit_fixture` to `write_fixture_commit`) because `commit` is not a declared verb.

**Owed at the close**
- New arm: `tools/memory-tree/check-memory-hygiene.test.sh` covering AC1–AC6, staged red by deleting the owed-set half (a) and by dropping the seen-red flush from check 23's awk.
- New arm: `tools/memory-tree/ratchet.py --fixture` plant `populated-seen-red` covering AC8, staged red by `run_populated` skipping its seen-red read.
- The legs of §7, especially `memory-hygiene self-test`. Fixture 149 adds a CLOSED Tier-2 spec to the shared fixture tree, and I did not see whether any other assertion counts that population.

**Bug-class checklist:** `gotchas.py --for-diff HEAD~1..HEAD` selected 42 anchored and 6 universal classes. I went through them and none needs a further change:
- The grammar is spelled only in HYGIENE; the reader's docstring and refusal message point there.
- No ledger token is wrapped across a line.
- The new README row has no pipe.
- A blank conf falls back to the defaults.
- An empty set of owed gates is announced rather than silent.
- Errors exit 2 instead of being swallowed.

**Other notes**
- The Edit tool left CRLF in four working copies; the index was already LF, and I normalised the files before committing.
- `help/reference/drive.md` and `help/reference/units.md` were already modified when I started. I left them unstaged and untouched.
- No command hit its timeout.
