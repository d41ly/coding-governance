# DEPL-aRepatriatedFork-1 — acceptance ledger

**Serves:** journal DEPL-aRepatriatedFork-1

One unit pass under the mandate. It ran no merge bar and no self-test suite. Each criterion was
observed by the direct check named on its line. The two govkit selftest arm groups this unit adds
were run on their own, by importing `tools/govkit/selftest.py` and calling
`check_playbook_hole_modes` over a scratch directory, and by staging the `when_selected` typo in the
real tree and running `govkit selfcheck`. The whole `selftest.py` suite was not run; the close owes
it.

The adopters were read-only. Both observations used `git clone --local --shared` clones under
`%TEMP%`:

- **inCMS:** `%TEMP%/ic1`, cloned from `C:/projects/incms/main` at
  `10c15529c582c20cc7c1f40572182f2439947492`.
- **nc:** `%TEMP%/nc1`, cloned from `C:/projects/incms/main/.git/modules/vendor/nicocares-package`
  at `b10628e47c20395bab3fcf2337cf7b0e68b12b52`. `C:/projects/nicocares/main` is a submodule
  checkout whose gitfile is relative, so a clone of that path fails. The module's git dir is the
  same repository at the same HEAD.

## AC2 — the AC1 arm, observed RED before S1 landed

The arm was added to `run_selftest` with `render()` still at a7c78ad2's bytes. `git diff a7c78ad2`
over `tools/playbook/render_playbook.py` was empty at that point. The arm is
`an answer outranks a derived probe that answers too`, and it failed with:

```
  arm FAIL an answer outranks a derived probe that answers too — body 'root memory\n' notes ['derived   MEMORY_ROOT = memory']
render_playbook.selftest FAILED — 1 of 9 arm(s)
```

The body carried the probe value, which is the red AC1 names.

Every other new arm was also observed red, by mutating the one guard it covers in place and running
`--selftest`. Seven arms went red together, and the tree was restored from a byte copy before the
build went on. For the template arm the red was the defect itself: the file became its own
template plus an appended `gov:playbook` region. The two govkit `check` arms went red the same way,
with `resolve_stand_down` returning nothing and with the `[charter]` join disabled.

**Evidences:** DEPL-aRepatriatedFork-1
- AC1 — `python tools/playbook/render_playbook.py --selftest` — 18 arms OK. The `answered` note reads `(probe would derive memory)` and the body carries `records`
- AC2 — `render_playbook.py` — the arm's name and failure line are recorded above, observed at a7c78ad2's engine bytes
- AC3 — `adopt-playbook.sh --target . --check` — exit 0 in `%TEMP%/ic1` with gov's `playbook.kit.toml`, under both the installed 1.0 engine and gov's 1.1 engine
- AC4 — `MEMORY_DISCIPLINES` — in `%TEMP%/nc1` with gov's descriptor and engine, `--check` reports DRIFT and a write moves exactly one line, `package brand` to `package, brand`. The PROJECT_NAME row is answered `NicoCares` and does not move
- AC5 — `--selftest` — the arm drives `main` with `playbook_path = "AGENTS.md"`: exit 1, message `are one file`, AGENTS.md unchanged
- AC6 — `playbook-render` — `python tools/govkit/govkit.py check --target` against `%TEMP%/ic1`: `hole 'playbook-placeholders' stood down — playbook-render observes this`, and no playbook UNDISCHARGED line
- AC7 — `selfcheck` — a staged `when_selected = ["playbook-rendr"]` redded with `non-entries named: playbook-rendr`. The copy-mode `check_playbook_hole_modes` arm reports `UNDISCHARGED`
- AC8 — `bash tools/playbook/adopt-playbook.sh --target . --check` — exit 0 in gov, and `git diff --quiet a7c78ad2 -- AGENTS.md` is clean
- AC9 — `[charter]` — the render selftest arm carries the trailer byte-exact inside a code span, and the govkit arm sees `answers.commit_trailer` refused by `check`
- AC10 — `[charter]` — five `--selftest` refusal arms: `{{`, a region marker, an ESC byte, a key an argv needs, and a key naming no placeholder. Each names the key
- AC11 — amended rev-2 — observed by `govkit selfcheck` at exit 0, and red on a staged `playbook-render@1.0` marker beside the 1.1 constant. `grep -c '\[charter\]'` over the README returns 4. The section 9 rev-2 line logs the change
