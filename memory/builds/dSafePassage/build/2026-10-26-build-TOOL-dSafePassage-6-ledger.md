**Serves:** journal TOOL-dSafePassage-6

# TOOL-dSafePassage-6 — acceptance ledger

The unit as built, at spec rev-6. `tools/govkit/shims.toml` ships a header comment and no row.
`tools/govkit/shims.py` validates every `[[shim]]` row at `read_shim_rows`: a safe-segment path, one
language, `.py` for a module. It renders each open row's forwarder from one template per language
(two for `py`, command and module), each opening with its `gov:shim <id>` marker, its target and the
policy kit spelled relative to the forwarder's own directory. `--check` holds every forwarder equal
to its render and every closed row's file absent. The window is `check_shim_windows`:
`read_releases` is the stand-in returning `[]`, `resolve_shim_landing` runs one
`git log --first-parent --reverse -S` on the ladder's default branch, and `derive_shim_window` takes
the repository it asks and returns the count beside its verdict (deviation 173). `govkit.py` gains
`read_policy_value(key, root, rev=None)`, which runs `policy.py get <key> --json` from the policy kit
`resolve_kit_dir` finds and returns `(value, source, reason)`. It also gains selfcheck arm 11, which
stands down, saying so, in a govkit copied without `shims.py` (deviation 174). The `govkit selfcheck`
leg row gains a `reads` `history` entry. `help/shims.md` and its index line are new, and the two
catalogue rows gain `summary` and `usage`, drained by `lists --write`. The regenerated mirror lands
in its own second commit, as §4 Rollout states.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Each AC was observed on
node d (Windows, Python 3.15.2, node v22.22.3) by the generator's own fixture CLI or a `python`
probe of the changed code. The new selftest arm's block was run outside the suite by a probe that
execs it with a stub `check`: 28 cases, 0 failures, 54 s on four workers.

Red when, observed: `SH_TEMPLATE` patched in-process to forward `$*` instead of `"$@"` made
`run_fixture('sh', ...)` print `args: [a] [b] [c] · expects args: [a] [b c] · MISS` and return 1.
`PY_PRELUDE` patched to print under every mode made `--mode journal` print its stderr line, a MISS,
and return 1. `derive_shim_window` patched to ignore the release list let `--window 0 --releases 0`
print `allowed to close` and return 0. Selfcheck arm 11's own lines, exec'd over a scratch root
holding one `closed = true` row with no release cut, printed `shims: 1 row(s) graded · 0 open · 1
closed` and the problem `shims: fixture/moved is closed and held: landed at 1d4ccd1c, 0 release(s)
cut since of 0, window 2 (no release has been cut: dShippedRelease defines release tags)`. Over gov's
tree the same lines printed `shims: 0 row(s) graded · 0 open · 0 closed` and no problem.

Owed at the close: `govkit selftest` (the 28 `[dSafePassage-6]` rows, and the New arm's RED-first
observation, staged as above by a forwarder template that drops an argument), `govkit selfcheck`
(arm 11, its RED-first observation staged by a `shims.toml` holding one `closed = true` row),
`govkit refusal join`, `govkit acceptance matrix`, `recall floor arms`, `measure-legs selftest`,
`run-gates canary`, `run-gates gov canary`, `memory hygiene`, `policy fixtures`, `policy check`, and
`spec tokens (a spec's own names resolve)`.

**Evidences:** TOOL-dSafePassage-6
- AC1 — `python "tools/govkit/shims.py" --check` exit 0 printing `shims: 0 row(s) graded · 0 finding(s)`; `python "tools/govkit/shims.py" --fixture --plant parity-edit` exit 0, its observations `--check exit on the render: 0` and `--check exit on a forwarder edited by hand: 1`, the finding `shims: fixture/moved's forwarder tools/demo/old.sh differs from its render`.
- AC2 — `python "tools/govkit/shims.py" --fixture --plant sh` exit 0, printing `first line: #!/usr/bin/env bash`, `marker: gov:shim fixture/moved-sh` and `target: ../moved/new.sh`, with `target spelled relative to the forwarder: True` (no `{prefix}`, no scratch path in the render).
- AC3 — `--fixture --plant <lang>` for each of `sh`, `js`, `py` and `module` exit 0, each printing `exit: 3`, `args: [a] [b c]` and `stdin: [in]`; `module` also printed `names: newmod newmod.py`, the planted `import oldmod` resolving to the target's names.
- AC4 — `--mode warn`, `--mode unset` and `--mode bogus` for each language exit 0 with one stderr line `gov: tools/demo/old.<ext> has moved to tools/moved/new.<ext>; this forwarder is held only until its deprecation window closes` and `journal: 1 line(s)`; under `bogus` the line adds `(the policy could not be read, so this reads warn)`.
- AC5 — `--mode journal` for each language exit 0 with `stderr: none` and `journal: 1 line(s)`, the line `from=… mode=journal shim=fixture/moved-<lang> to=…`, its keys `utc,shim,from,to,mode`, and `journal carries no argument: True`.
- AC6 — `--plant window --window <w> --releases <n>` exited 1 at `0 0`, `1 0`, `2 0`, `2 1`, `4 0`, `4 3` (each `the closed row is held`) and 0 at `0 1`, `1 1`, `2 2`, `4 4` (`allowed to close`); `--window 0 --releases 3 --unlanded` exited 1, `landed at no default-branch commit`.
- AC7 — `python -c "import sys; sys.path.insert(0, 'tools/govkit'); import shims; print(shims.read_releases('.'))"` printed `[]`; `--plant window --window 0 --releases 0` exited 1: `0 release(s) cut since of 0, window 0`.
- AC8 — `git grep -n -e "check_shim_parity(" -e "check_shim_windows(" -e "shims: " -- tools/govkit/govkit.py` found both calls and the `shims: {_sh_n} row(s) graded` line in `selfcheck`'s arm 11; `print(shims.check_shim_windows('.'))` printed `[]`.
- AC9 — the `tomllib` probe printed `[('install.deprecation-window', 'dSafePassage', True, True), ('install.on-shim-call', 'dSafePassage', True, True)]`; `python "tools/policy/policy.py" lists --check` exit 0, `green · 0 finding(s)`; the `grep -c` on `tools/policy/unsummarised-keys.txt` printed `0`; the `git grep` found `readPolicy("install.on-shim-call"` at `shims.py:131` and `read_policy_value("install.deprecation-window"` at `shims.py:333`, and `check_policy.scan_reader_keys('.')` spells both keys.
- AC10 — `git grep -n -e "on-shim-call" -- help/` found `help/shims.md` and its line in `help/README.md`.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Observed by a researcher in scratch clones of `83817478f` (batch a, `2026-10-28-prompt-TOOL-dSafePassage-5-close-arms-a-researcher.md`), each break staged alone and restored: One `New arm:` line, for `tools/govkit/govkit.py` (selfcheck arm 11). I ran arm 11's three calls (`read_shim_rows`, `check_shim_parity`, `check_shim_windows`, as `govkit.py:3540-3544` makes them) over a `shims.build_scratch` fixture, not the whole selfcheck. The break was a declaration whose one row was landed on `main`, then committed `closed = true`, under `deprecation-window = 2`. It exited 1 with `FAIL shims: fixture/moved is closed and held: landed at 722f295d, 0 release(s) cut since of 0, window 2 (no release has been cut: dShippedRelease defines release tags)`. Restored to the row open with its forwarder rendered, it exited 0 with `shims: 1 row(s) graded · 1 open · 0 closed`.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Observed by a researcher in scratch clones of `83817478f` (batch b, `2026-10-28-prompt-TOOL-dSafePassage-1-close-arms-b-researcher.md`), each break staged alone and restored: the `TOOL-dSafePassage-6 AC1 to AC7` block in `main()`, run unchanged (50 cases). Break: `shims.py` `derive_shim_window` reads `since >= window - 1`. RED: `FAIL [dSafePassage-6] AC6 window 2 with 1 release(s) held a closed row, --expect held matching — exit 1, expected 0: … the closed row: allowed · expects held · MISS`, and the same for window 4 with 3 releases. GREEN restored: both ok, 31 ok. Inconclusive at HEAD: the 10 `--expect <other> … missing` arms fail on both sides. The arm requires `"MISS" not in stdout`, but an exit-1 case is a MISS by design, so these arms can never pass.
