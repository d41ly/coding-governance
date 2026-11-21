# TOOL-dWitnessedBar-61 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-61

No merge bar, no self-test suite and no gate leg ran in this pass, the naming lexicon excepted. The
criteria were observed through probes of the unit's own code on node d, 2026-11-19: the canonical
`tools/lib/legacy_ledger.py seed` run in a scratch `git init` at `%TEMP%/llu61` with its `[[ledger]]`
registration, seed argv and home directory staged and nothing committed, the memory-tree kit's copy
run the same way at `%TEMP%/llu61b`, and `read_head_sha`, `read_rows` and `read_home_state` called from
`python -c`. In that fixture `git rev-parse --verify -q HEAD` exited 1 printing nothing. The `New arm:`
of spec section 7, section `2o`'s unborn seed cases in `tools/lib/resolve-python.test.sh`, was written
and syntax-checked with `bash -n` only; it still owes its RED-first observation, which the main loop
makes at the close, and so does every leg that section names.

**Evidences:** TOOL-dWitnessedBar-61
- AC1 — `HEAD is unborn` — `seed --population p` printed `seed: HEAD is unborn, rows carry the null
  SHA` once and `armed p 2`, exit 0; the home's rows `a` and `b` each carried forty `0` characters in
  the fourth field; `read p` printed both rows and exited 0, and `read_rows` over the home returned two
  rows and no malformed line. With the home removed and the seed exiting 1, `seed` printed
  `unarmed p exit 1`, exit 1, the home held `# unarmed · exit 1 · ` and the null SHA, and
  `read_home_state` read it `unarmed`. The memory-tree copy printed the same line and stamped the same
  SHA. Outside the criterion: `--sha abcdef12` on the unborn HEAD stamped `abcdef12` with no unborn
  line; `read_head_sha` on a directory outside any repository returned no SHA and the reason
  `no HEAD: fatal: not a git repository ...`; and with that reason forced, `run_seed_cli` printed
  `unarmed p no HEAD: fatal: boom`, exit 1, and wrote no home.
- AC2 — `present p` — after the fixture's first commit the rerun printed `present p`, exit 0, and `cmp`
  found the home byte-identical to its copy taken before the commit; with a third key `c` and
  `--widen R1` it printed `widened p c`, the new row read `c`, `1`, the new HEAD's sha and
  `widened:R1`, and `a` and `b` kept the null SHA.
