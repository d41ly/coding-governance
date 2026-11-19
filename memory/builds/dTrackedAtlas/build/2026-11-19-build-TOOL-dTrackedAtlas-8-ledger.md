# TOOL-dTrackedAtlas-8 — acceptance ledger

**Serves:** journal TOOL-dTrackedAtlas-8

No merge bar, gate or self-test suite ran in this pass. Each criterion was observed by the spec's own
probe or command, with `$FX` a `--shared` clone of the worktree at `%TEMP%/ta8fx` checked out at
`9e21ac760`, removed after; the real repository's refs were never written. The probe scripts and every
JSON and stderr capture sat in the run's scratch directory. The probe loads
`memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-build-state.py` by path and calls
`scan_forks("$FX", {key: TEXT}, "2026-09-30")` with the spec's TEXT, whose section 7 holds `F1`. Each red
was observed on the shape the criterion names: the module as it stood at the pass's start, byte-equal to
it at `81cfc29dc`, or a staged break made by a scratch probe that loads the changed module and swaps
`SPEC_NAME` before calling its `main`, so no tracked file was edited to stage a red.

**Evidences:** TOOL-dTrackedAtlas-8
- AC1 — with `$KEY_BAD`, the probe printed the set holding
  `memory/builds/dX/spec/2026-11-19-spec-a'$(touch pwned)'.md`, and `test -e "$FX/pwned"` exited `1`.
  Red: the module at `81cfc29dc` raised `StateError the driver's plan_state graded 0 of 1 specs, exit 0`,
  awk naming the cut path `.../0/2026-11-19-spec-a.md`, and created `$FX/pwned`.
- AC2 — with `$KEY_OK` and `TMPDIR`, `TEMP` and `TMP` all `"$FX/o'q"`, the probe printed the set holding
  `memory/builds/dX/spec/2026-11-19-spec-TOOL-dX-1.md`. Red: the module at `81cfc29dc` raised
  `StateError` reading `graded 0 of 1 specs, exit 2: _: -c: line 1: unexpected EOF while looking for matching`.
- AC3 — a scratch branch in the clone committed `$PLANT` with `**Status:** OPEN` as `519504b7b31a`; the
  CLI at `--ref HEAD --claims none` exited `2`, its stderr the one line
  `build-state: refused spec file name memory/builds/dWitnessedBar/spec/2026-11-19-spec-a'$(touch pwned)'.md at 519504b7b31a: not [A-Za-z0-9._-]+\.md`,
  stdout empty, and `test -e "$FX/pwned"` exited `1`. Red: the module at `81cfc29dc` exited `2` with
  `plan_state graded 1102 of 1103 specs` (PINNED at `519504b7b31a`) and created `$FX/pwned`; with
  `SPEC_NAME` staged to `.*` and the quoting kept, the run exited `0`, no `pwned`, and dWitnessedBar's
  `counts` read `{'DEFERRED': 88, 'OPEN': 1}` (PINNED at `519504b7b31a`). The branch was deleted after.
- AC4 — `--ref 9e21ac760 --claims none` in the unplanted clone exited `0`, and `cmp` of its JSON
  against the one taken at the pass's start, before any edit, exited `0`. Red: `SPEC_NAME` staged as
  `^[A-Za-z0-9._]+\.md$` exited `2` with
  `build-state: refused spec file name memory/builds/dTrueNorth/spec/2026-10-21-spec-TOOL-dTrueNorth-1.md at 9e21ac760dc0: not [A-Za-z0-9._-]+\.md`.
- AC5 — `"$PY" -c` loading the module by path printed a `__doc__` whose exit-2 sentence holds
  `[A-Za-z0-9._-]+\.md` as the refused spec file name, and whose `WHAT IT DOES NOT CHECK` ends naming a
  spec whose name git's listing quotes as one not listed as a spec at all. The docstring is now a raw
  string, so the backslashes it quotes are not escapes. Red:
  `grep -c` for `A-Za-z0-9._-` or `listing quotes` over the module at `81cfc29dc` counted `0`.

Owed to the close: the plain bar, whose legs section 6 names. No suite arm is added, so no `New arm:`
observation is owed.
