# KICK-dKeptSession-4 — acceptance ledger

**Serves:** journal KICK-dKeptSession-4

No merge bar, no self-test suite, no gate leg and no `check_policy.py --fixture` run ran in this
pass, and `adopt-policy.test.sh` and the docs leg's run arm were not run. The criteria were observed
on win32 at the pass's base `136de315` by probes of the unit's own code: `run_intake_preset` and
`run_fresh_target` called from a `python -c` script in `tools/policy/`, each installing from a
snapshot of the working tree as the cases do, with `GOV_REMOTE`, `GOV_DEFAULT_BRANCH` and the
`GIT_*` location variables unset; the adopter and `policy.py scaffold` run as CLIs over scratch
targets under `%TEMP%`; and `grep`. The two new names, `cmd_scaffold` and `run_intake_preset`, are
`cmd_` and `run_` verbs, and `lexicon.py --suggest` answered OK for each as `py.function`.

Owed to the close: every leg the spec's section 7 names, the `policy fixtures` runs of the
`intake-preset`, `adopter-fresh-target`, `adopter-suite` and `limit-fresh-target-spawn` cases among
them; AC8, the docs leg's run arm over the tutorial; and the RED-first observation of both
`New arm:` lines: the `intake-preset` case and `adopter-fresh-target`'s moved key count in
`tools/policy/check_policy.py`, and the new arms 4b and 4c of `tools/policy/adopt-policy.test.sh`,
each on its staged break and green once restored.

**Evidences:** KICK-dKeptSession-4
- AC1 — `run_intake_preset("intake-preset")` with every `read_deploy_answers` answer but `preset` caught `build_install_target`'s `RuntimeError`: `the deployer's intake --kits policy,memory-tree exited 2`, carrying `the selected kits need answer(s) preset` and `Refusing to invent one`.
  The selection was `derive_requires_closure(["policy"])`, `policy` and `memory-tree` (DERIVED,
  that probe); its snapshot took 85.7 seconds (DERIVED, that probe's printed line).
- AC2 — with `preset = "strict"` added, the target's `deploy.toml` read `answers.preset` `'strict'`, and its `[policy]` table held exactly `on_baseline_red` and `on_hook_block`.
  The second snapshot took 51.7 seconds (DERIVED, that probe's printed line).
- AC3 — `apply --kits policy,memory-tree` exited 0; once the install was committed, the line after the policy file's header was `preset = "strict"`.
  The installed `policy.py get hooks.bypass --rev HEAD --explain` exited 0 printing `refused` on
  stdout and `policy: hooks.bypass · preset · preset strict at <sha8>, --rev HEAD` on stderr. The
  case returned 5 assertions, 0 wrong, in 259.3 seconds (DERIVED, that probe).
- AC4 — over a committed scratch target with no policy file, `adopt-policy.sh --scaffold` exited 2 printing its line ending `pass --preset <name>, one of the policy catalogue's presets`, before any `mkdir`.
  No `.governance` directory existed after it. With `--preset lax` it exited 1 printing
  `policy: the scaffold could not be written to` and the file's path, leaving `.governance` empty;
  and `python policy.py scaffold --preset lax` exited 2 with nothing on stdout and the stderr line
  `policy: scaffold refused · preset · "lax" is not one of ["velocity", "standard", "strict", "guarded"]; …`.
  `--preset` beside `--check`, and `--preset` with no value, each printed the usage line, exit 2.
- AC5 — over a committed target whose policy file holds `preset = "standard"`, `--scaffold --preset strict` exited 0 printing `… keeps its preset "standard", not the answer "strict": …`, and the file's `cksum` was unchanged.
  `--preset standard` over the same file exited 0 with no such line; `--preset lax` over it exited
  2 with the scaffold's refusal before any render; and the `[[regenerate]]` form, no `--preset`,
  exited 0 comparing nothing.
- AC6 — `run_fresh_target("adopter-fresh-target")` installed with `DEPLOY_FULL`'s answers, `preset = "standard"` among them, and `apply --kits policy,run-gates,memory-tree` exited 0.
  Each `arm_schema` line matched the count of `render_scaffold(rows, preset="standard")`'s keys,
  5 against 4 with no preset (DERIVED, a `python -c` render of both); the case returned 168
  assertions, 0 wrong, in 141.3 seconds (DERIVED, that probe), and it found the deferral line under
  the Install section of `help/policy.md`.
- AC7 — `grep -n -- "--answer preset=" help/policy.md help/tutorial/adopt-gov.md help/tasks/change-a-gov-rule.md` printed one line per page.
  The Install section of `help/policy.md` names `velocity`, `standard`, `strict` and `guarded`,
  says `strict` and `guarded` refuse hook bypass from the first commit, states the kept-file line,
  and gives the upgrade line `preset = "<name>"` under `[answers]`. Its usage anchor carries
  `dfdfbe12`, the fingerprint `docs_leg.py --fingerprints` printed for the adopter's row once it
  gained `--preset=` (DERIVED, that probe).
- AC8, owed — the docs leg's run arm over `help/tutorial/adopt-gov.md` is a gate leg's arm, so this pass did not run it.
  The tutorial's intake line now ends `--answer preset=standard`, the answer AC1 observed intake to
  need.
