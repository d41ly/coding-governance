**Serves:** journal TOOL-dWitnessedBar-8

# TOOL-dWitnessedBar-8 — builder return 1 (run `wf_0b92f31c-ee3`), a divergence, nothing committed

## Why

DIVERGENCE: before writing any code I checked the spec (memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-8.md, rev-6) against the tree. Three checks fail, and each needs a spec revision before this unit can be built as written.

(1) §4 "The ask" contradicts §6 AC4. §4 defines the line `flakes` prints as `hold  <leg>  <flakes>/<window>  <flake record ids>`: two spaces after the leg, two after the count, then the record ids. AC4 says the fixture prints `hold  A 2/10` (lines 349 and 351): one space after the leg and no ids. A grep for one form cannot match the other. The spec has to pick one form, and either AC4 or §4 has to change to match it.

(2) §4 "The window" and S5 have no source for the release time. S5 says to count "only rows after its last release", and §4 says "A release is the closing date of L's last held-flaky-leg ask". No closing date is recorded anywhere I can find:
- A backlog closing row reads `- CLOSED · <id> · by <id or sha> · <why>`, with no date (checked on the tracked BACKLOG.md rows, e.g. `- CLOSED · TOOL-aBatchedLintel-2 · by TOOL-aDrainedSluice-4 · ...`).
- Unit 30's S6 `write_ask_closing` writes `- CLOSED · <id> · by <sha> · <why>`, also with no date.
- The ask generator `ASKS_CMD` names (`gen_build_index.py --asks --json --all`) gives `filed`, `status`, `closing` and `decided_by`, but no closing date.
§4 needs to say how the release instant is derived. Options: the commit date of the commit that added the CLOSED row, the commit date of the closing row's `by <sha>` (with what happens when `by` names a unit id), or a dated field that unit 30's closing row writes. Each window comparison against a release depends on this.

(3) S3 and AC3 assume `build_records.py read` will accept a `flake` record once the kind is added to KINDS. It will not. `main`'s `read` verb has a branch for each of eight kinds, and any other kind goes to `read_exception`, which reads it as an exception record. I checked this on a planted `-leg-tail-1.md` record that has all five of its required fields: `read` exits 1 and reports the file name and Principle, Excuses, Reason and Caused-by as malformed. So "`python build_records.py read` over it reports no malformed field" fails unless `read` also gets a `flake` branch. §4 Files touched currently limits `tools/memory-tree/build_records.py` to "the `flake` entry of `KINDS` and its paragraph in the docstring", so it needs to add the `read` branch (or a generic typed-kind read), and S3 should say so.

Every other claim I checked holds at HEAD, including the blob-pinned lines 5506, 12013 and 1894. I changed no path and committed nothing.

## Summary

No commit: TOOL-dWitnessedBar-8 stopped before the first code edit because the spec has three divergences (listed in `why`). `base` is d4a97bfab6f05f349611ba001584cec75f722acf.

**What ran:**
- `unattended.sh --brief` answered "already recorded, unchanged".
- I read memory/guides/BUILD-METHOD.md, the brief and spec rev-6 whole, then probed the spec's claims against HEAD.

**Claims that held:**
- **Runner (`tools/run-gates/run-gates.sh`):**
  - `runleg` keeps the `.sample` attempt out of `gate-logs`.
  - `run_leg_retry` is called at line 5477, the sample block sits between it and `run_attribution` at 5527, and the `nondeterministic ·` line is at 5506.
- **`tools/run-gates/verdict_flow.py`:** `ROUTES`, `read_routing`, `derive_route`, `SELECT_SOURCES`, `derive_selection`, `read_held_runner`, `FIXTURES` and `main`'s `--run`/`--selection` rules are as cited.
- **Record factory:**
  - `tools/run-gates/keep_tails.py#load_factory` resolves and imports the memory-tree kit.
  - In `tools/memory-tree/build_records.py`, `write_record`, `read_records`, `KINDS`, `DOORS` and the typed-kinds plant are as cited.
  - `TYPED_RECORD_KINDS` in `tools/memory-tree/tree_lib.py` is as cited.
- **Unattended driver (`tools/unattended/unattended.sh`):** `write_held_asks`, `write_ask_rows`, `derive_ask_seq`, `write_leg_tails`, `run_verdict_route`, `derive_review_signals` and `_genv` at 12013 are as cited.
- **Hook suite:** `BAR_INERT_KNOBS` in `.githooks/pre-push.test.sh` is at 1894.
- **Policy keys:** the catalogue rows for `verdict.flakes` and `verdict.flakes.entry` exist with no summary, and both keys are listed in `tools/policy/unsummarised-keys.txt` and on `help/reference/policy.md`.
- **Other files:** the `watch:` line in `memory/guides/SESSION-KICKOFF.md` includes `run-gates.sh`, `add_scratch_worktree` is in `lib-attribute.sh`, and `ASKS_CMD` is in `.unattended.conf`.
- **Ask JSON:** `gen_build_index.py --asks --json --all` gives each ask's summary, status and filed date.

**Claims that failed:** I planted a leg-tail record and ran `build_records.py read` over it. It read the record as an exception and reported it malformed, which confirms check (3). Checks (1) and (2) come from reading the spec text and the tracked BACKLOG closing rows.

**Gates:** none. No gate, suite, bar or `--selftest` ran, and the naming lexicon was not needed because no name was minted. These probes do not stand in for any gate. All of §7 and the `New arm:` line (`tools/run-gates/run-gates.test.sh` covering AC1) still need their RED-first observation once the unit is built.

**Not run:** `gotchas.py --for-diff HEAD~1..HEAD`, because there is no commit.

**Working tree:** my only temporary file (under the scratchpad's `u8` folder) is deleted. The tree still shows only what was there before this pass: `RUN.md` staged by `--dispatch`, plus `help/reference/drive.md` and `help/reference/units.md`, which `git diff --stat` shows with no content changes, only CRLF warnings. I did not touch any of the three.
