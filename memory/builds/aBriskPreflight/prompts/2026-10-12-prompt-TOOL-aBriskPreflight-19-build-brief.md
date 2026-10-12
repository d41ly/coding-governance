# Build brief — TOOL-aBriskPreflight-19: the inherited reds that read as this build's own are drained

**Serves:** research TOOL-aBriskPreflight-19

Build the unit its spec, `spec/2026-10-12-spec-TOOL-aBriskPreflight-19.md`, describes: S1 to S3, each
leg made GREEN by its own checker run directly. The offenders and why each leg reads OWN or MIXED are
in the spec; the close that found them wrote its leg output to the session scratchpad as `close2.out`.

- **S2 is an equality**: `VERB_OFFENDER_PIN` is 1063 and must be met exactly. Rename exactly four
  offenders, re-run `lexicon.py --check`, and read `offenders=` before committing. A records-only or
  test `def` counts too.
- **S3**: a memory note records that `check-arms` wants the WHOLE refusal text, not a prefix; read
  `tools/memory-tree/check-arms.py` for what it grades before writing the assertion. A waiver row in
  `memory/project/unarmed-branches.txt` only if no arm can assert the whole text, with its reason.
- **Declare before you write**, with `--dispatch`: the two `.githooks` and `tools/unattended` suites,
  the run-gates evidence suite (or the waiver file), `memory/builds/aBriskPreflight/README.md`,
  `memory/LIVE.md`, `memory/ledger/2026-10.md`, `memory/map/generated/symbols.json`. Stage those AND
  `RUN.md`. A renamed function stales `symbols.json`: run `gen_map.py --write`.
- No suite, no bar: AC1 to AC3 are each one checker run directly. Do not bump any kit version.
  Never kill a process you did not start.
