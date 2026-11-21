# TOOL-dWitnessedBar-54 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-54

No merge bar, no self-test suite and no gate leg ran in this pass, the naming lexicon excepted. The
criteria were observed through probes of the unit's own code on node d, 2026-11-19. The `New arm:` of
spec section 7, `check_when_forms_agree` in `tools/govkit/selftest.py`, was driven outside the suite
over a scratch gov copy at `%TEMP%/w54h` with selfcheck stubbed, so its regen and shell-reader halves
were observed and its selfcheck half was not. Its RED-first observation, and every selfcheck half of
AC2 and AC3, are owed to the main loop at the close, with the legs section 7 names.

**Evidences:** TOOL-dWitnessedBar-54
- AC1 — `resolve_generated_indexes` — at the worktree root the call printed
  `tools/run-gates/../gate-legs.json:tools/run-gates/leg_factory.py`. In a scratch clone at
  `%TEMP%/w54b` carrying this pass's reader, the output with `tools/govkit/` deleted differed from the
  output with it only by that pair, and stderr was empty both times. With the reader at HEAD, before
  this pass, the same clone printed no `gate-legs` pair and no line saying why: the red.
- AC2 — `python tools/govkit/govkit.py selfcheck` — owed to the main loop. The `_gwbad` test was
  probed by executing its own source lines over gov's descriptors: `w54.conf:W54=on`,
  `exists:{prefix}/run-gates/regen.py`, `exists:{kit}/w54-absent.txt` and
  `exists:{prefix}/govkit/govkit.py` admitted; `exists:`, `exists:{nope}/regen.py` and
  `BACKLOG_MODE=builds` refused. The refusal text now reads `a when shaped <conf>:<KEY>=<value> or
  exists:<path>`, and the `[aWP r2]` case expects it.
- AC3 — `regen.build_items` — over the arm's six planted rows it kept `conf-true` and `present`,
  skipped `conf-false` and `absent`, and refused `unknown-token` and `empty-path`. The shell reader
  kept the same two and named the same two on stderr. The selfcheck half is owed to the main loop.
