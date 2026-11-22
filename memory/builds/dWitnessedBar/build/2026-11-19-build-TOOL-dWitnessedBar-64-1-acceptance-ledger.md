# TOOL-dWitnessedBar-64 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-64

No merge bar, no self-test suite and no gate leg ran in this pass, the naming lexicon excepted. The
criteria were observed through probes of the unit's own code on node d, 2026-11-21, with git
2.54.0.windows.1: the canonical `tools/lib/legacy_ledger.py seed --population p` run in five scratch
`git init`s at `%TEMP%/ll64v`, each holding a `[[ledger]]` registration `p`, its seed argv and home
directory staged and nothing committed, one left clean and four broken as spec S4's table states (the
symbolic loop with both files written, `refs/heads/other` pointing back); scratch copies of
`tools/lib/*.py` at `%TEMP%/ll64m` carrying each of AC3's three staged breaks, run over the same five
fixtures; and `read_head_sha` called from `python -c` under a `_run_git` stand-in. The three
`legacy_ledger_py` blocks were compared byte for byte after the edit and read identical. The `New arm:`
of spec section 7, section `2o`'s corrupt-HEAD block in `tools/lib/resolve-python.test.sh`, was written
and syntax-checked with `bash -n` only; it still owes its RED-first observation, which the main loop
makes at the close, and so does every leg that section names.

**Evidences:** TOOL-dWitnessedBar-64
- AC1 — `unarmed p no HEAD: ` — each corrupt fixture exited 1 with one stdout line, that lead and then
  `fatal: No such ref: HEAD` for the broken branch ref and the symbolic loop,
  `fatal: missing object 1111111111111111111111111111111111111111 for refs/heads/master` for the
  missing object, and `git symbolic-ref exited 1` for the detached-missing HEAD; stderr carried
  `legacy_ledger: p: no HEAD: <the same reason>; nothing written`; no home was written; and
  `grep -rl --exclude-dir=.git` for forty `0`s or forty `1`s printed nothing in any of the four.
- AC2 — `armed p 2` — the clean commitless fixture printed `armed p 2`, exit 0, with
  `seed: HEAD is unborn, rows carry the null SHA` once on stderr, and its home held the null SHA.
- AC3 — `armed p` — with S2's two probes removed every corrupt fixture printed `armed p 2` with the
  unborn line and wrote a home holding the null SHA; with only the `for-each-ref` probe removed the
  missing-object fixture printed `armed p 2` while the other three still read no HEAD; with
  `HEAD^{commit}` set back to `HEAD` the missing-object and detached fixtures printed `armed p 2` with
  no unborn line and a home holding the `1111…` SHA. In each break the clean fixture still printed
  `armed p 2`.
- AC4 — `(None, 'no HEAD: git rev-parse exited 128')` — `read_head_sha(".")` under a `_run_git`
  stand-in answering `(128, "", "")` printed exactly that, so an exit other than 1 from S1's probe
  never reaches S2's probes.
