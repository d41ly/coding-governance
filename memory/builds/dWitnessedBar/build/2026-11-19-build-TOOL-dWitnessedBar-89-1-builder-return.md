**Serves:** journal TOOL-dWitnessedBar-89

# TOOL-dWitnessedBar-89 — builder return 1 (run `wf_ed08853c-0c9`), committed 05fdf49d3

## Why

Built TOOL-dWitnessedBar-89 from spec rev-4 as one pass commit. Before writing anything I probed the spec's claims against the tree: the line numbers cited at 8bed2005c, FLOOR_ASSERTIONS=80, a `Raised` count of 7, a shell-role row of 850, and the region/verb_plan behaviour all hold, so I found no divergence. One change goes beyond what the spec states, and it is recorded as deviation 893: the canary call site now also reds on a return of 3 and leaves rgf_ok at 0. Without it, an empty slot list on a 3 would certify the canary. The round-1 audit's id 7 fix asks for exactly this.

## Summary

Commit 05fdf49d3 is on branch/unattended-dwitnessedbar-2ed3b3, base 4d5152195, with trailers `Pass: TOOL-dWitnessedBar-89` and Co-Authored-By. In that same commit the spec's status header is set to CLOSED (the date was already 2026-11-21), and the generator refreshed its records region.

What changed in C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/tools/run-gates/run-gates.gov.test.sh:
- **S4:** `check_canary_keys` now returns 3 when its visited count fails, and still prints the visited line on stderr. `check_key_variant` returns 3 without printing, ahead of its rc-2 branch. On a 3, the liveness loop sets fail=1, adds nothing to `a` or `rgf_whys`, and adds the key to no `rgf_seen` (`rgf_kvr` and `rgf_k3` are new variables, no new functions). The canary call site takes its `unread` slot only on a 2; on a 3 it sets fail=1 and leaves rgf_ok at 0 (the deviation-893 change).
- **S6:** the `<key>)` sed match is now the spec's whole-token form, with replacement `\1<rep>\3`.
- **S7/S10:** no increment moved. FLOOR_ASSERTIONS is still 80, and the floor comments are unchanged.

Records:
- The shell-role row was widened with `ratchet.py widen shell-role` (record ...-89-widen-24.md). The widen door wrote 851, so I then set the row to the measured 852, as unit 84 did. That count edit was a TAB-safe python byte replace.
- The acceptance ledger is written at memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-89-1-acceptance-ledger.md, and the deviation record is ...-89-deviation-893.md.
- I ran `gen_build_index.py --write` and committed what it changed: README, memory/backlog/TOOL.md, memory/LIVE.md, and the dClosedLoop as-built view, whose deviation count moved. That as-built path was declared with `--dispatch --writes` before I staged it.
- `gen_map.py --write` changed nothing.

Checks that ran (probes only; they stand in for the `run-gates gov canary` arm and the `portability (shell lines only shrink)` leg):
- **AC4:** I cut `check_cr_reached` and `check_canary_keys` and ran them with `CANARY_KEYS=()`. The built suite returned 3 with empty out and `the canary visited 0 of 0` on stderr; the base blob returned 2. A stub probe of the canary call site plus liveness loop: on rc 3 there was no unread line and no (rc 2) line, fail=1, rgf_ok=0, rgf_seen was empty and a=2. On rc 0, a=6 and both keys were seen.
- **AC6:** the built sed line made one change on each of the six spellings and none on `${_rg_v%$'\r'}`, `${_rg_v:-}`, `$_rg_vx` or the fingerprint arm. The base line also changed the modifier arms. Over the live hook, each key and each replacement changed exactly one line.
- **AC3:** a scratch ledger gave a count of 2.
- **AC7:** the awk/grep count printed 0.
- **AC10:** FLOOR_ASSERTIONS=80, the anchored count is 1, and the -B1 line is the TOOL-aShardedFloor-2 comment.
- **AC12:** the derivation printed 28 and spec/...-90.md. A scratch clone under %TEMP%/p89 with a second units pair printed MALFORMED REGION and exited 3, and `--plan` there printed `not exactly one well-formed pair`. The clone was removed.
- **AC13:** after the commit, `gen_build_index --write` left `git status --porcelain` empty on all three renders.
- `bash -n` passed, and `sh_hygiene --measure` gives 852.
- `gotchas.py --for-diff HEAD~1..HEAD` exited 0 and I went through its list. Following up `amendment-leaves-its-other-half-standing`, I checked the return-contract comments: no other copy of the contract exists, and `check_canary_keys` and `check_key_variant` have no callers outside this suite. No other class applied.

Owed at the close (main loop):
- The `New arm:` RED-first observations: a scratch suite whose `check_canary_keys` returns 2 on a visited failure, and a match whose braces are each optional.
- AC1's two skip-placement clones, AC4's first-pair-stop clone, AC5's no-last-byte clone, AC6's modifier-arm hook clone, and AC10's `PASS (<n> assertions)`.
- AC9's re-derived length.
- Every ledger line of units 74, 76, 85, 86, 87 and 88 that AC1 to AC3, AC5, AC7, AC8, AC10 to AC13 grep.
- Gates: run-gates gov canary, testsuite counts, portability, ratchet, recall floor, recall floor arms, and memory hygiene.

No command timed out or was skipped. The working-tree changes to help/reference/drive.md and units.md were there before I started, show no content diff, and I left them alone.
