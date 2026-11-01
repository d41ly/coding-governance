**Serves:** journal TOOL-dSafePassage-101

# TOOL-dSafePassage-101 — acceptance ledger

The unit as built, at spec rev-2. Product writes: `tools/push-main.test.sh` (S5: arms 25 and 35 read
their lines from `$tmp/out25.txt` and `$tmp/out35.txt`, each written by a `printf` above its loop),
`tools/lib/resolve-python.test.sh` (S5: the floor-statement count reads `$TMP/floor-rev.txt`),
`tools/govkit/selftest.py` (S6: `stub92 = root92 / HERE.name`) and `tools/govkit/upgrade_walk.py`
(S6: the release-engine grader's pins under `gk.derive_tool_root(gk.repo_root())`, `"scripts"` and
the root, numbered, each at `gkn`; the plant-root grader's plant under `poln`; the grader loop's
tuple widened to `(Stop, OSError, LookupError, ValueError, RuntimeError)`). Records: seven ledger
lines given the OBSERVED form (S2), three answers given a joining token (S3), and the dead citation
in `BACKLOG.md` repaired (S4). S1 landed at `a78d6affc` by a gov-spec-writer pass. No function
added, so `memory/map/generated/symbols.json` is not regenerated.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. Every criterion below was
observed on node a (Windows 11) from this worktree's root, the greps over the pass's tree as
committed. The scratch copies of AC15 and AC17 were made by `git archive` of a `git stash create`
commit of the pass's tree, under `%TEMP%` (the short-path exception for fixture repositories), and
removed afterwards.

Owed at the close: S2's TOOL-dSafePassage-80/AC2 line, which §3 Edges rests on the main loop's run
of `python tools/run-gates/derive-ceilings.py --check` (G1 refuses it to a role agent); that line is
left as 80's pass wrote it, so AC2, AC5 and AC14's first command stay red until the main loop writes
it from its run. Also owed: AC5, AC7 and AC11 (G1 legs), AC13 and AC15's selftest half (G3), the §7
legs at the bar, and the four `New arm:` lines' RED-first observations.

**Evidences:** TOOL-dSafePassage-101
- AC1 — `a78d6affc` — the edge grep printed nothing, exit 1; the header grep printed 99's line 3, `**Status:** CLOSED · rev-3`; the §9 grep printed line 332; the Edges probe printed `none`; the paragraph count printed 1.
- AC2 — `tools/memory-tree/check-memory-hygiene.sh` — its form predicate as a `git grep -P` printed one line, 80's line 28, the line owed above; the other six of the seven print no more.
- AC3 — `2026-10-23-spec-TOOL-dSafePassage-43.md` — the first grep printed exactly three lines: 59's line 38, 77's line 33 and 82's line 38; the second printed 59's line 37 alone.
- AC4 — `upgrade_walk.py:944` — the grep printed nothing, exit 1; `tools/govkit/upgrade_walk.py` is still cited once on `BACKLOG.md` line 7.
- AC5 — `bash tools/memory-tree/check-memory-hygiene.sh` — owed at the close (G1); it reds on check 23 until 80's AC2 line is written from the main loop's run.
- AC6 — `done <<<"$out25"` — the grep printed exactly one line, `tools/unattended/unattended.sh:4016`.
- AC7 — `python tools/gate-lint/sh_hygiene.py memory/project/substitution-fed-loops.txt` — owed at the close (G1).
- AC8 — `f25=1` — arm 35's cut, lines 1363 to 1385 with `lander`, `tmp`, `ok` and `bad` set, printed `  ok   — 35 no deployer beside the lander is one skip line and exit 0; a deployer with no python refuses`; with its `printf` line removed bash named the missing `out35.txt` and it printed `  FAIL — 35 the skip line was printed 0 time(s) over two absent-deployer runs:`. Arm 25's feed, lines 915 to 918 over a one-line `out25`, printed `f25=1`; with its `printf` line removed bash named the missing `out25.txt` and it printed `f25=0`.
- AC9 — `n1c=7` — the floor block, lines 263 to 269 with `ROOT`, `HERE`, `PFX`, `REALPY` and `TMP` set as the suite sets them, printed no `FAIL` line and `n1c=7`; with its `printf` line removed it printed `FAIL python_floor.py check --rev 3708a705 did not print the seven pinned statements:`.
- AC10 — `root92 / "govkit"` — the five-pattern grep printed nothing, exit 1.
- AC11 — `bash tools/check-install-prefix.sh` — owed at the close (G1).
- AC12 — `python -B tools/govkit/upgrade_walk.py --list` — with the kit's `__pycache__` removed, exit 0 in 16 s, eight grader lines all `ok`, `upgrade-walk: grader · release-engine · ok` and `upgrade-walk: grader · plant-root · ok` among them.
- AC13 — `[dSP-92]` — owed at the close (G3).
- AC14 — `not recorded` — the 95 and 96 commands each printed one line, 95's line 27 and 96's line 26; the 80 command is owed with 80's AC2 line above.
- AC15 — `upgrade-walk: grader · release-engine · ok` — `python -B upgrade_walk.py --list` from `gk2` in the pass's copy printed it, every grader line `ok`, then exit 2 on `the pin 60d90cb71db51e651aa1c5efe3f6d48ba21a997d names no commit in gov`, the copy's empty history, after the line AC15 reads. Over a `70273a468` copy built the same way it printed no release-engine line and ended in a `Traceback` naming `upgrade_steps.Refusal: cannot derive the tool root under …/pin-tools: 0 gk2/registry.toml candidate(s) found`, exit 1. The `[dSP-92]` half is owed (G3).
- AC16 — `stub92 = root92 / HERE.name` — the six-pattern grep piped through `sort -u` printed exactly six lines, one per pattern.
- AC17 — `upgrade-walk: RED: a grader of this leg reads wrong, so nothing it would measure is trusted` — from the copy's `govkit` with `tools/policy` removed, the run printed `upgrade-walk: grader · plant-root · RED · it raised LookupError: no policy kit holding adopt-policy.sh in this install: looked in …`, then that line, exit 1, and no `Traceback`.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Observed by the main loop at `6d6fe589b`: the three legs run on the tree read `sh-hygiene: OK — 58 declared site(s) in 43 row(s)`, memory hygiene exit 0, and install-prefix `3 kit-path spelling(s) on 3 line(s)` (the `ceiling-evidence.txt` rows of TOOL-dSafePassage-85), as AC7, AC5 and AC11 state. In a `git clone --shared` (`dsp101`): `upgrade_walk.py` GREEN `grader · release-engine · ok` and `grader · plant-root · ok`; RED with `want` spelled under `gkx`, `grader · release-engine · RED · a pin at tools derived ...`, under `python -B` with `__pycache__` removed. `selftest.py` GREEN, all seven `[dSP-92]` lines `ok` and `[]` (AC13); RED with the stub named `gkx`, `check_floor_bash` exits 1 on an uncaught `upgrade_steps.Refusal: cannot derive the tool root under .../dsp92: 0 govkit/registry.toml candidate(s) found`, a crash before any `[dSP-92]` line rather than the FAIL line the arm names. `resolve-python.test.sh` GREEN `PASS — resolve-python: 502 assertions held`; RED with the `printf` line cut, `FAIL python_floor.py check --rev 3708a705 did not print the seven pinned statements`. The lander suite's arms 25 and 35 were observed red and green on cut copies by the build pass only (AC8). AC15, in a `git archive` copy with the kit renamed `gk2`: the walk half reads `grader · release-engine · ok`; the selftest half did not run, refused at import by `tools/gk2/steps.toml [[upgrade]] row 1 key up: '{gov}/govkit/steps/receipt_schema_4.py' ... not a tracked file`, so it is recorded as not run, never as red.
