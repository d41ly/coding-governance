# TOOL-dWitnessedBar-52 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-52

No merge bar, no self-test suite and no gate leg of this repository ran in this pass, the naming lexicon
excepted, and `ratchet.py --fixture` did not run either. The criteria were observed through probes of the
unit's own code on node d, 2026-11-19: a scratch `git init` at `%TEMP%/r52a` for AC1, and for AC2 and AC3
a `python` probe that built each plant's fixture through `write_scalar_fixture` under `%TEMP%/r52c` and ran
the kit's CLI in it through `run_leg_cli`, the way the plants do, plus the spec's greps. The `New arm:` of
spec section 7, the plants `untracked-conf` and `ignored-conf`, owes its RED-first observation at the
close (dropping `--others` from `read_root_confs`), and so does every leg that section names. The third
builder pass re-observed AC1 at `%TEMP%/r52c` and AC2 and AC3 at `%TEMP%/r52p` over the same code, with the
same outputs; the red-at-base reading of AC1 is the second pass's.

**Evidences:** TOOL-dWitnessedBar-52
- AC1 — `FOO_PIN` — in the scratch target holding the kit copied to `tools/memory-tree/` and staged, the
  first `--scaffold` copied the example to `.memory-tree.conf` and stopped, exit 1; `git status` read the
  conf `??`. With `FOO_PIN="3"` appended, the second `--scaffold` exited 0 and the home held the row
  `.memory-tree.conf TAB FOO_PIN TAB 1` at the null SHA. The kit copy's `python tools/memory-tree/ratchet.py
  keys-not-scalar` printed `held · .memory-tree.conf TAB FOO_PIN TAB 1` and `pass`, exit 0; after `git add -A &&
  git commit` it printed the same, exit 0. Red at base: with HEAD's `ratchet.py` in the same probe the home
  held no row and, after the commit, the leg printed `undeclared site · .memory-tree.conf TAB FOO_PIN`, exit 1.
- AC2 — `untracked-conf` — the plant's fixture with an untracked root `.x.conf` assigning `FOO_PIN="3"`:
  `keys-not-scalar --measure` printed `.x.conf TAB FOO_PIN TAB 1` beside the tracked `.fix.conf TAB BAR_PIN TAB 1`, exit 0.
  Under the `ignored-conf` fixture, `.x.conf` named in `.git/info/exclude`, it printed `.fix.conf TAB BAR_PIN TAB 1`
  and no `.x.conf`, and the leg held `BAR_PIN` and passed, exit 0; a nested `sub/.y.conf` was not read
  either. `grep -n 'def read_root_confs' ratchet.py` named `:485`, whose docstring states the ignored-conf
  blind spot. Owed at the close: the two plants run by `ratchet selftest`.
- AC3 — `read_root_confs(` — `grep -n 'read_root_confs(\|read_tracked_paths(\|ROOT_CONF_RE' ratchet.py`
  named `read_tracked_paths(` at its definition `:123` and the widen check `:297`, `read_root_confs(` at its
  definition `:485` and in `read_root_conf_lines` `:504`, and no `ROOT_CONF_RE`. In the `untracked-conf`
  fixture, `.fix.conf`'s `BAR_PIN` held by the home's one row and `FOO_PIN` holding none, `keys-not-scalar`
  printed `conf-scalar-pins · undeclared site · .x.conf TAB FOO_PIN · measured 1, declared None`, exit 1. In
  gov's tree `read_root_confs` lists the five confs `git ls-files -- '.*.conf'` lists, so `measure_scalar_pins`
  and `measure_cutoffs` read the same set as before.
