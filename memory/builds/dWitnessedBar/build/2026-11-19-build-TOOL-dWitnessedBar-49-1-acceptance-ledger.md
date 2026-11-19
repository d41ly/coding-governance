# TOOL-dWitnessedBar-49 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-49

No merge bar, no self-test suite and no gate leg ran in this pass, the naming lexicon excepted. The
criteria were observed through probes of the unit's own code on node d, 2026-11-19: `scan_bare_bash`
imported from `tools/run-gates` and called over fixture repos under `%TEMP%`, the two greps AC2
spells, and the new block with its adapter cut out of `tools/memory-recall/selftest.py` and run
alone. The `New arm:` of spec section 7 still owes its RED-first observation, which the main loop
makes at the close, and so does every suite the section names.

**Evidences:** TOOL-dWitnessedBar-49
- AC1 — `scan_bare_bash` — over a fixture repo tracking `const x = 1;` in a `.js` and a `.py` holding
  `bash = shutil.which("bash")`, it returned one hit naming `a.py`, line 2, shape 4; over the same `.js` beside the
  same line inside a `resolve_bash_py` block it returned `[]`. The scanner at `66f4e8d98`, run on the
  first fixture, returned `[]`, the criterion's red. Further probes: `shutil.which("bash.exe")`
  matched shape 4 and `shutil.which("git")` and `shutil.which(name)` did not; in a `.js`,
  `which('bash')`, `execSync("where bash")` and `execFileSync('which bash')` matched shape 4, while
  `which('git')` and a `which('bash')` inside a `resolve_bash_js` block did not. Over this worktree
  the widened scan returned `[]`.
- AC2 — `shutil.which("bash")` — `git grep -n` over `tools/memory-recall/selftest.py` printed nothing
  and exited 1, and `grep -c '^# >>> resolve_bash_py'` over it printed 1. The new block, cut between
  its two markers, compared equal to the canonical's in `tools/lib/resolve_bash.py`. The adapter
  `resolve_selftest_bash`, run live, returned Git's own bash and kept one scan across two calls; with
  `scan_bash` replaced by a refusal it raised `_Skip` carrying the refusal text.
