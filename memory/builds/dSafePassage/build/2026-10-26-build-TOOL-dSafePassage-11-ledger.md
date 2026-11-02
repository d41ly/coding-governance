**Serves:** journal TOOL-dSafePassage-11

# TOOL-dSafePassage-11 — acceptance ledger

The unit as built, at spec rev-4, on node a at Python 3.15.2 (`py -0p` listing `pythoncore-3.15-64`
and `pythoncore-3.14-64`, no 3.11). `tools/lib/python-floor.txt` holds `3.15`. The canonical block
in `tools/lib/resolve-python.sh` gains `_rp_floor="3.15"`, probes each candidate once with
`-I -c` for its `major.minor` and its forward-slashed `sys.executable`, passes over and names a
candidate below the floor, echoes the probed executable where `[ -f ]` holds, and on refusal reads
`platforms.provision` with the newest candidate that ran: the canonical `resolve_kit_dir` carried
inline in a quoted heredoc finds the policy kit, and `"$_rp_best" "$_rp_kit/policy.py" get
platforms.provision` reads it at the landed revision. All 75 marked copies were re-synced
byte-identically, and the two unmarked ones, `tools/check-line-length.sh` and
`tools/playbook/adopt-playbook.sh`, gained the markers and the block. `tools/lib/python-floor.sh` carries `preflight` and `down`;
`tools/lib/python_floor.py` carries the six functions of §4, plus helpers the inventory does not
name: `run_git`, `derive_lib_rel` (the declaration's path from the module's own repository root),
`read_parity_population` (the parity rows' grep, shared by the check and the write),
`_scan_pep701`, `_scan_toml11` and `main`. `read_floor` reads with universal newlines, so a CRLF
checkout's `3.15\r\n` is the one optional newline (the file has no `eol=lf` pin). The step row
`lib/python-floor-3.15` follows `govkit/receipt-schema-4` in `tools/govkit/steps.toml`. The six
floor statements became pointers. The PEP 701 ban left `merge-rows.test.sh`, its compile arm kept.
`platforms.provision` gained its summary and usage, and `policy.py lists --write` drained it. The
page is `help/python-floor.md`, and its row is in `help/README.md`.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Fakes are two-line bash
scripts under the run's scratch directory; fixture repositories sit under `%TEMP%` (`fp11` for AC3,
`fd11` a `--shared` clone of this worktree carrying the raise for AC6, AC7, AC9, AC10 and AC11,
`ad11` the AC11 adopter). The four `New arm:` bodies in `tools/lib/resolve-python.test.sh`
(sections 1b to 1e) were run outside the suite by a scratch stand-in. It carried the suite's
prelude, `resolve_kit_dir` and the four sections verbatim, and printed `24 assertions, st=0`. The
suite's existing arms (a) to (e) ran the same way against the new block: `13 assertions, st=0`.

**Evidences:** TOOL-dSafePassage-11
- **AC1** — `PATH="<fakes>:$PATH" GOV_PYTHON=<fake> bash -c '. "$1"; resolve_python' _ tools/lib/resolve-python.sh`
  with all four fakes printing `3.14 $0` exited 1. Stderr named each of the four as `ran 3.14, below
  the floor 3.15`, then the GOV_PYTHON line and `install the floor with: uv python install 3.15`.
- **AC2** — a fake `python3` printing `3.15 C:/Users/daily-agent/AppData/Local/Python/pythoncore-3.15-64/python.exe`
  first on PATH yielded that path, not `python3`. A fake reporting a path that is no file yielded
  `python3`.
- **AC3** — in `fp11`, which has no remote, with pass-through fakes: `off` on `main` printed
  `platforms.provision is off, so this refusal names no install command.` and no command. `uv` on
  `main` printed `the install was not offered, because stderr is not a terminal` and both commands.
  With the key unset it printed both commands. With `off` on `main`, and `uv` on the checked-out
  `feature` commit and in an uncommitted edit, it printed no command. With `tools/policy` removed it
  printed `reads its catalogue default, name: no reader ran, because no policy kit holding policy.py
  in this install: looked in …` and both commands.
- **AC4** — `bash "tools/lib/python-floor.sh" preflight` under AC1's fakes exited 1, and `cmp` found its
  stderr identical to AC1's. With no fakes it exited 0 printing `python-floor:
  C:/Users/daily-agent/AppData/Local/Python/pythoncore-3.15-64/python.exe runs Python 3.15.2, at the
  floor tools/lib/python-floor.txt declares`.
- **AC5** — the spec's `tomllib` one-liner printed `['govkit/receipt-schema-4', 'lib/python-floor-3.15']`.
  `upgrade_steps.py list` read the row, as position 2 of 3.
- **AC6** — in `fd11`, `bash tools/lib/python-floor.sh down 3.11 <clone>` over a committed
  `planted.py` holding `v = f"{"X" if c else "y"}"` printed `mode static, because no interpreter at
  3.11 resolves here` and `planted.py:2: a string in a replacement field reuses the enclosing
  f-string's quote`. It exited 1 and left the declaration reading `3.15`. With the plant removed
  it exited 0 with `the floor 3.11 restored in 77 file(s)`: the declaration and all 76 copies'
  literals read `3.11`. A probe confirmed that `ast.parse(plant, feature_version=(3, 11))` accepts
  the plant.
  **Finding: gov's own tree fails this down today.** Over a clean clone with no plant, the down
  exited 1 on two lines that do not compile under 3.11: `tools/govkit/upgrade_steps.py:2864`
  (`b'v2\n'` inside an f-string's replacement field) and `tools/memory-recall/check-recall.py:394`
  (`'#'` inside one). Both landed under the 3.11 floor and fall outside this unit's write set. The
  green half above was observed with those two files removed from the fixture clone. Until they are
  rewritten, the step's down refuses on gov's own tree, which TOOL-dSafePassage-8's lander and
  TOOL-dSafePassage-5's rollback both walk.
- **AC7** — over a committed `planted.toml` holding a multi-line inline table, the down exited 1
  naming `planted.toml:2: a line break inside an inline table`. Probes of `_scan_toml11` flagged a
  trailing comma in an inline table, `\e`, `\x41`, `07:32` and `1979-05-27T07:32Z`. They did not
  flag an offset `-07:00`, a multi-line array inside an inline table, a literal string's `\e`, a
  quoted `"07:32"`, a table header or an array's trailing comma. Interpreter mode,
  `check_down_floor(<clone>, "3.14")` through `py -3.14`, named `planted.toml:2: Invalid initial
  character for a key part`.
- **AC8** — `python tools/lib/python_floor.py check --rev 3708a705` printed six statements, among
  them `tools/settings-merge.py:3`'s, and exited 1. `python tools/lib/python_floor.py check` on the tree printed
  nothing and exited 0.
- **AC9** — in `fd11`, with `python-floor.txt` reading `3.16`, `check` exited 1 naming all 76
  copies' `_rp_floor="3.15"`. With `This kit needs Python 3.12 or newer.` planted in `help/README.md`,
  it exited 1 naming `help/README.md:11`.
- **AC10** — `git grep -c '_rp_floor="3.15"' -- '*.sh' '.githooks/*'` printed `1` for all 76 files,
  `tools/check-line-length.sh` and `tools/playbook/adopt-playbook.sh` among them. With either
  file's opening marker deleted, `check` named `tools/check-line-length.sh:64` or
  `tools/playbook/adopt-playbook.sh:18` as `an unmarked multi-line definition of resolve_python`.
- **AC11** — `fd11` committed the raise as `14ad72bc4`. In `ad11`, `intake` and `apply --kits
  lexicon` came from that clone, and the receipt was forced to schema 3 with `steps` taken out.
  `govkit.py update --target ad11 --to 14ad72bc4 --write` then ran under AC1's fakes, with govkit
  itself under the real interpreter. It exited 1 with `step govkit/receipt-schema-4 · applied`,
  `step lib/python-floor-3.15 · failed · exit 1: resolve_python: or, on Windows: py install 3.15`
  and `stopped at lib/python-floor-3.15`. The receipt read schema 4, and its `steps` held
  `govkit/receipt-schema-4 applied`, then `lib/python-floor-3.15 failed`. The failure carries the
  refusal's last stderr line, the one the walk records.
- **AC12** — `git grep -n 'FSTR=' -- tools/memory-tree/merge-rows.test.sh` printed nothing (exit 1).
  The `py_compile` grep still printed the compile arm.
- **AC13** — `git grep -n 'platforms.provision' -- help` named `help/python-floor.md`. `python
  tools/policy/policy.py lists --check` printed `green · 0 finding(s)`. The list no longer names the
  key, and the catalogue holds one row of that name with `name`, `uv`, `off`, default `name`, a
  summary and a usage. The `policy\.py"? get platforms\.provision` grep printed
  `tools/lib/resolve-python.sh:134`.

NOT OBSERVED IN THIS PASS. The `uv` offer on a terminal and its `y` answer: no captured run has a
terminal. The `New arm:` lines' RED-first observations are the close's.

SIDE EFFECT ON THE RECALL MAP. `gen_map.py --write` dropped four public functions of
`tools/check-wiring.sh` from `symbols.json`: `resolve_kit_dir`, `resolve_kit_file`,
`resolve_kit_files` and `check_hook_blobs`. The lexicon kit's `parse_shell_defs` already loses quote
parity on `wired()`'s `"${3:+{CLAUDE_PROJECT_DIR\}/$3\\\"}"`, two blocks above. The old resolver
block happened to resync it, and the new one resyncs it only at `check_hook_modes`. Measured over
every changed shell file, check-wiring is the only file that lost a definition. The symbol tier
feeds recall only, never the ratchet.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Observed by a researcher in scratch clones of `83817478f` (batch a, `2026-10-28-prompt-TOOL-dSafePassage-5-close-arms-a-researcher.md`), each break staged alone and restored: Four `New arm:` lines, all in `tools/lib/resolve-python.test.sh`, each break staged alone in a slice: **AC1 AC2 AC4 (arm 1b).** Break: `resolve-python.sh:46`'s floor comparison set to `-ge 0`. Result: `FAIL fakes reporting 3.14 were accepted below the floor 3.15 (got '…/below/gp')` and `FAIL the refusal does not name the install command uv python install 3.15`. Restored: `SLICE PASS (10 assertions)`. **AC3 (arm 1c).** Break: `:140`'s provision value ignored (`_rp_prov=name`). Result: `FAIL platforms.provision off on main still named an install command: …`, 3 of 5 checks red. Restored: PASS (5). **AC8 AC9 AC10 (arm 1d).** Break: `check_floor_copies` stops reporting a copy literal that drifts. Result: `FAIL a copy's literal differing from the declaration was not named: …`, 1 of 3 checks red; the planted-statement and unmarked-definition checks are untouched by this break. Restored: PASS (5). **AC6 AC7 (arm 1e).** Break: static mode forced and both scanners emptied. Result: `FAIL the down over a planted PEP 701 f-string did not exit 1 naming planted.py:2: rc=0 …` and `FAIL the down over a planted TOML 1.1 inline table did not exit 1 naming planted.toml: …`, 6 FAIL lines in all. Restored: PASS (9).
