**Serves:** journal TOOL-dWitnessedBar-26

# TOOL-dWitnessedBar-26 — the first builder return (run `wf_9a057cc8-2c5`), a divergence

Committed: no. The pass stopped before keeping product code and handed the spec back.

## Why

DIVERGENCE: the probe command in spec §4 "The rule" cannot produce what §6 AC1 and AC3 require on node d, and §4 never says whether the resolver stops at the first candidate that passes, which AC1 depends on. A spec-writer revision is needed before this unit can be built as written.

(1) The probe, §4's code block versus AC1 and AC3. I measured this on node d against a copy of C:/Windows/System32/bash.exe under the scratchpad's u26/wsl folder. Running the spec's argv `[cand, "-c", 'u=$(uname -s) && printf "%s\n" "$u" && { [ -z "$1" ] || test -f "$1"; }', "_", script]` through the copy exits 0 and prints only `\n`. The cause is the WSL launcher: it passes the -c string through an outer shell, so `$u` comes back empty, and it drops the positional arguments (`echo "$0|$1"` printed `/bin/bash|`). As a result the copy cannot be reported as `answered Linux`, which AC1 requires. Under AC3's `--host posix` it is not a bash that "runs" either: it printed no `uname` line. The plain probe `uname -s && { [ -z "$1" ] || test -f "$1"; }` does work. Under the copy it printed `Linux` with rc 0. Under Git's bin/bash.exe it printed `MINGW64_NT-10.0-22621` with rc 0 for a file that exists and rc 1 for a missing one. §4 needs to name a probe whose first output line is uname's own, and to state that the launcher drops `$1`, so `test -f` never refuses WSL. Only the uname test does.

(2) The order, §4 versus AC1. §4 orders the candidates GOV_BASH, then Git's bin/bash.exe, then PATH. AC1 stages PATH as the copy, then System32, then Git's cmd, and expects `bash:` to name Git's bash while `tried:` names both the copy and System32's launcher. That only holds if every candidate after GOV_BASH is run and reported, with `found` being the first that passed. A resolver that stops at the first pass never reaches PATH: my draft printed only `C:/Program Files/Git/bin/bash.exe: runs` until I made it run every candidate. §4 must state which it is, and §5's cost line should account for the extra probes.

Further findings the revision should settle in the same pass:

(3) §4's sites table and Files touched miss two places that still fall back to a bare or PATH-only bash. `tools/loop/factories.py@835d45ef:360` has `[resolve_bash(gate.as_posix()) or "bash", …]`. `tools/run-gates/regen.py@4a65b7ea:281` has `(BASH if run[0] == "bash" else "") or shutil.which(run[0]) or run[0]`, while the sites table says regen is "unchanged". The S6 query finds neither.

(4) `loop_witness.resolve_bash` is imported by name by `tools/loop/breakpoints.py@52627944:85`, `tools/loop/budget.py@bfef8c85:1341`, `tools/loop/factories.py@835d45ef:358`, `tools/loop/loop_lib.py@7d5c58fe:759` and `tools/loop/position.py@710b2d07:135`. The sites table only names loop_witness's own calls. The copy must therefore keep its `path or None` contract through an adapter, not the block's 3-tuple. The same name clash holds for profile_bar, corpus_ids, the lexicon and runlog selftests, handoff and govkit, as brief item 1 says. `policy-mirror.js`'s module-level `resolveBash` clashes with the twin's function name, so it must be renamed. It is internal, so no caller is affected.

(5) govkit selftest `check_floor_bash`, around `tools/govkit/selftest.py@b19bf481:4884-4965`. Once Git's bin/bash.exe is step 2, PATH `path87` still contains Git's `cmd` directory, which holds no bash. So on a Git for Windows node a bash resolves there. The premise of `[dSP-94]` and `[dSP-95]` ("no bash resolves") no longer holds, and the inversion the spec names needs a staged PATH that also drops git. The narrowed-catch anchor `returncode == 0\n        except OSError:` disappears once the block is inlined, so that arm needs a new anchor inside the block.

I restored `tools/lib/resolve_bash.py` with `git checkout`, and `git status` shows only the RUN.md row the main loop staged before this pass. My draft of the block is at C:/Users/d41ly/AppData/Local/Temp/claude/06f17fbb3b45b392/0a586af7-47fb-45dc-b963-7ee82521f7da/scratchpad/u26/resolve_bash.draft.py for the revised spec to reuse. It runs every candidate after GOV_BASH and keeps the spec's probe text.

## Summary

Nothing is committed. The unit stopped at a divergence before any product code was kept. The pass started from base 35b89d99c71a895903055547cc31143bfb347deb.

What ran:
- `--brief` reported the brief already recorded at 419685535ef7.
- A route for TOOL-dWitnessedBar-26 was appended to this session's orientation card, because scratch-guard refused the first write without one.
- The naming lexicon accepted `scan_bare_bash`, `resolve_bash_canonical`, `read_bash_found` and `resolveBash`.
- A scratch `ast` probe of §4's three query shapes, over 241 tracked `*.py` and 37 `*.js`, found the twelve hits the rev-4 spec and the brief name: branch-reconcile 1041; govkit selftest 4887, 4895 and 5910; upgrade_steps 410 and 435 (435 is unit 51's); lexicon 65; corpus_ids 382; handoff 319; runlog 8124; settings-merge 932; stop-guard.js 123.
- A draft of the Python canonical was run through its CLI on node d, with the copy of System32's bash.exe staged on PATH. These probes stand in for the `python resolver` leg and section 2j's truth table, neither of which ran:
  - AC2 and AC4 behave as the spec says: exit 2 naming every tried line, and GOV_BASH refused with one tried line.
  - AC4's positive case printed Git's bash.
  - AC1 and AC3 cannot be met. The spec's probe argv makes the WSL copy print an empty line with rc 0, so it is never reported as `answered Linux` and is never accepted under `--host posix`.

The draft was then restored, so no path under tools/ changed. No gate, suite or bar ran. `gotchas.py --for-diff` was not run because there is no commit.

Owed at the close once the spec is revised and the unit re-dispatched, per §7: the `New arm:` RED-first observations for resolve-python.test.sh (AC1 to AC6), measure_legs.py (AC7), corpus_ids.py (AC4) and govkit selftest (AC8).
