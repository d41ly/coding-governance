# Build brief — TOOL-aBriskPreflight-7: preflight and the wiring check each declare a wall-clock ceiling and name a breach

**Serves:** research TOOL-aBriskPreflight-7

Build the unit its spec, `spec/2026-10-11-spec-TOOL-aBriskPreflight-7.md`, describes, and nothing
else. Units 1 to 6 and 10 are CLOSED; unit 4's `init_preflight_probes` is the start site your
`derive_wiring_bound` serves. This run sequences its passes one at a time, inline.

## The after-arm rows your S6 instrument reads

The whole-preflight A/B ran after every cost unit landed, two interleaved rounds on fixture clones
whose remote is a local bare mirror (rig: `build/2026-10-11-build-TOOL-aBriskPreflight-7-ab-prep.sh`
and `…-7-ab-run.sh`; rows: `build/2026-10-11-build-TOOL-aBriskPreflight-7-ab-rows.log`, one `host`
line before each run, one `label` line with rc and wall, one `proof` line with whether the output
carried `preflight OK`). Old code (BASE) was refused at check 109 both times — the claim push killed
at its 60 s bound, the symptom this build exists for — after 1820.0 s and 2112.3 s; new code passed
both times, 1041.7 s and 855.8 s. The host's five-spawn cost was 4.15 to 8.96 s (0.8 to 1.8 s a spawn)
and its kernel pool 19.5 GB paged, so these walls are a degraded host's. The whole-preflight counts at
a traced new-code run (`pf-fixture-new-traced`, before unit 4 and 10 landed): 762 forks, 653 execs,
against 1121 and 1032 at BASE. Derive the values from these rows by your spec's formula; state the
per-spawn allowance it assumes and the host it was measured on; never raise a value to make a run pass.

## How to work in this tree

- The run branch merged `origin/main` at `976a85a25`; line numbers in the spec are at BASE `b726385f`.
  Re-locate every site in the current tree; rev the spec first (its own `Pass: none` commit) where a
  claim no longer holds.
- **Declare before you write**, with `--dispatch`: the driver, the suite, `tools/unattended/README.md`,
  your build records, `memory/builds/aBriskPreflight/README.md`, `memory/LIVE.md`,
  `memory/ledger/2026-10.md`, `memory/map/generated/symbols.json`. Stage those AND `RUN.md`.
- Lexicon `--suggest` before naming; `gen_map.py --write` after; a records-only `.py` is lexicon-graded.
- `sh_hygiene.scan_file` over the driver before committing (a loop fed by a here-string over a
  substituted variable is refused, shrink-only registry).
- No suite, no bar: sliced arms of `unattended.test.sh` inside `tools/unattended/`, deleted before
  `gen_map.py --write`. A preflight-level check goes in a fixture clone from the rig above.
- Do not bump `KIT_UNATTENDED_VERSION` (1.97, main's). Never kill a process you did not start.
