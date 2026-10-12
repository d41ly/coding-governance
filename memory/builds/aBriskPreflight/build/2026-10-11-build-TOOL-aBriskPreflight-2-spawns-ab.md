# TOOL-aBriskPreflight-2 — the A/B: check-wiring's readers, before and after

**Serves:** research TOOL-aBriskPreflight-2

Node `a`, 2026-10-11, the build pass. Spec rev-1. The built checker is blob `fda1854b97cb`, the
`tools/check-wiring.sh` the pass commit carries. "Old" is blob `de28993fd950`, the checker at the
pass-start commit `20a9e88e7`, which carries TOOL-aBriskPreflight-1 and main's merge.

## The fixture

A throwaway clone, `git clone --local` of this worktree under `%TEMP%/bp2`, checked out at
`20a9e88e7`. No `--fix` ran in it, so both checkers print the same two `UNWIRED  hooks` lines and the
`merge` lines there; every `--check` below exits 1 on those, old and new alike. Each run copied one
checker over the clone's `tools/check-wiring.sh`. Probes and logs went under the run's scratchpad.

## The spawn counts (AC10)

Traced with `2026-10-11-build-TOOL-aBriskPreflight-1-run-traced.sh` and read by
`2026-10-11-build-TOOL-aBriskPreflight-1-trace-spawns.py`, each with its own checker as the span
source, new first and then old, on one host state:

| Run | At (UTC) | spawn5 | Pool Paged | CPU | Wall traced | Forks | Execs | `sed` | `head` | `tr` | `grep` | `python3` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `cw2-new-traced` | 09:30:55 | 4.44 s | 18111 MB | 27% | 151.3 s | 180 | 121 | 13 | 3 | 13 | 22 | 3 |
| `cw2-old-traced` | 09:33:59 | 2.77 s | 18124 MB | 32% | 253.5 s | 320 | 231 | 58 | 21 | 19 | 43 | 17 |

The two runs' combined stdout and stderr are byte-identical. The brief's "before", 333 forks and
246 execs, was unit 1's trace of this file in unit 1's clone; the old row above re-traced it here so
both rows read one tree. The host was loaded by this pass's own concurrent probes, and spawn5 moved
from 4.44 s to 2.77 s between the rows, so the walls are not a comparison; the counts do not depend
on load.

Rows in each trace, by the spellings AC10 names. xtrace prints the resolver's multi-line `-c`
argument ANSI-quoted, so its row reads `-c $'# >>> resolve_kit_dir`:

| Row | Old | New |
|---|---|---|
| `python3 -c 'import sys'` from `check-wiring.sh` | 9 | 1 |
| `python3 -c $'# >>> resolve_kit_dir` | 7 | 1 |
| `tr -d ' \t\r\n'` | 7 | 1 |
| `sed -n 's\|.*"` (the retired `json_str`) | 18 | 0 |

New's other `import sys` row is `merge-rows.sh`'s own probe, a child script this unit does not touch.

## The other criteria

- **AC1** — `ac1-probe.sh` lifted `json_str` from old and `read_fragment_keys` from new by their
  definition lines and compared all four keys, twice per file (the second from the cache), over the
  11 fragments `git ls-files` listed and eight fixtures: the spec's seven plus a key whose first value
  is empty and whose second is not. 152 comparisons, 0 differing. Staged breaks: a regex without the
  leading `.*` differed on the compact twice-written marker (`a` against `b`), and a loop without
  `|| [ -n "$_l" ]` lost the final unterminated `hook_path`.
- **AC2** — `ac2-probe.py` lifted both `matchers_of` with `settings-merge.py`'s own regex behind a
  stub `settings_json` and ran 17 triples over `.claude/settings.json` and a scratch file holding the
  spec's seven shapes: identical lines on both. The new no-argument call printed nothing and returned
  0. A staged break dropping the `]` cut differed on the scratch file.
- **AC3** — `python tools/settings-merge.py --selftest` printed `settings-merge selftest: PASS` and
  no `SKIP arm 17` line, in 44.7 s.
- **AC4** — `bash tools/check-hook-destinations.sh` exited 0 with 11 `ok` lines and neither refusal.
- **AC5** — old and new `--check` in the clone: stdout byte-identical (15 lines), stderr empty in
  both, both exit 1. With `GOV_SETTINGS_JSON` naming an absent file: stdout byte-identical (18 lines,
  the refusal's `note` lines included), stderr empty, both exit 1.
- **AC6, AC7, AC8** — one run in the clone with three independent breaks of shipped values: the
  scratch fragment without its `matcher` line, `Workflow|Agent` narrowed to `Workflow`, and
  `resume|compact` narrowed to `resume`. New printed `UNWIRED  scratch   —
  tools/hooks/scratch-guard.fragment.json declares no marker/matcher/event/hook_path`, `wired under
  matcher 'Workflow', not 'Workflow|Agent'` and `wired under matcher 'resume', not
  'resume|compact'`, and exited 1; old printed the same bytes. Restored, `git status` was clean on
  both files, and AC5's new run is the restored state: `ok       agent-cap`, `ok       scratch` for
  `PreToolUse` and `ok       card`.
- **AC9** — stubs `python3`, `python`, `py` exiting 9 first on `PATH` and `GOV_PYTHON` naming a
  fourth: old and new stdout and stderr byte-identical, both exit 1, seven `note     resolver` lines
  on stderr in each, `note     straggler — no usable python launcher resolved` on stdout, and no
  `skip     agent-cap`. The first pair of this run is void: the stub directory went on `PATH` in its
  `C:/` spelling, which the `:` separator split, so no stub shadowed anything.
- **AC11** — both inline blocks extracted with `awk` and diffed against `tools/lib/resolve-python.sh`
  and `tools/lib/resolve_kit_dir.py`: no output. A copy with one line inside the `resolve_kit_dir`
  markers changed printed that line.
- **AC12** — the arm's `awk` comparison over new lists seven literal call sites, six pairs, every one
  in `KIT_FILE_PAIRS`; with ` memory-tree merge-rows.py` cut from the list it prints
  `unlisted memory-tree merge-rows.py`.

## The three new suite arms (S7)

Sliced into a temporary script beside the checker (the suite's prologue, the three arms, and the
AC6 arm's own fixture lines), run alone, then deleted before `gen_map.py --write`:

| Checker | AC12 arm | AC9 arm | AC6 arm |
|---|---|---|---|
| built | 2/2 ok | 3/3 ok | 2/2 ok |
| scratch arm without its `[ -z "$smatcher" ]` test | 2/2 ok | 3/3 ok | FAIL on the `declares no` line |
| `PY_OK` never cleared | 2/2 ok | 3/3 FAIL | 2/2 ok |

## Found in the pass

The first `--check` pair differed: new skipped agent-cap, scratch, recall, routed and merge as not
adopted. A Windows python ends every line CRLF, and a bash `$(…)` drops only the last line's, so the
batched resolver's answers kept a CR on every line but the last. The pass strips it per line before
storing, and the per-call path strips the one it can carry. Every figure above is from the fixed
checker; that first pair is not.
