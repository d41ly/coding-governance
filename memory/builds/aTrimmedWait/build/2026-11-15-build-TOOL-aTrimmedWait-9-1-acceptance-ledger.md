# TOOL-aTrimmedWait-9 acceptance ledger

**Serves:** journal TOOL-aTrimmedWait-9

No merge bar, no self-test suite and no `*.test.sh` ran in this pass. Every observation below was
made on node a, one command at a time with nothing else running, over the spec at rev-3, from the
worktree root at base `d07bb02a7`. The probes are §4's `p9.sh`, `p9c.js` and `p9m7.py`, saved in the
run's scratch directory; `p9.sh` writes its stderr to a named scratch file instead of a bare
`mktemp`, and `p9c.js` also prints the built module's verdict counts. The base module of `p9c.js` is
`git show 2a13de8b6:tools/hooks/scratch-guard.js` beside `agent-cap.js` from the same commit. The
changed code is `tools/hooks/scratch-guard.js#scanCommandHeads`, the role-arm paragraph of the
hook's header, `tools/hooks/scratch-guard.test.sh#run_role_bash` rows W9-AC1 to W9-AC4 with
`FLOOR_ASSERTIONS`, and arm 23 of `tools/roles/adopt-roles.test.sh#run_agents23` with its
`A23_EDIT` mode `bad`.

**Evidences:** TOOL-aTrimmedWait-9
- AC1 — `bash "$SCRATCH/p9.sh"` over the built hook printed the `argv` line for `sleep 9 # x` as
  `[["sleep","9"]]`; rows C1 and C3 printed `exit 0` with nothing after it; rows C2, C4 and C5
  printed `exit 2 row P3 sleep at or over 5 s`. Before the edit, the same command printed `exit 2 row P3` for C1 and C3, the red the criterion names. <!-- DERIVED from scratch-guard.js#POLL_SLEEP_FLOOR_S -->
- AC2 — the same run printed the `argv` line for C6's command as `[["tools/hooks/agent-cap.test.sh"]]`,
  one word, and row C6 printed `exit 2 row G3 suite`. Before the edit C6 printed `exit 0` and its
  argv held `"#","--render"`.
- AC3 — `node "$SCRATCH/p9c.js"` over the module at `2a13de8b6` and the built
  `tools/hooks/scratch-guard.js`, with §4's transcript directory and this checkout, printed
  `commands 9301 · same 9301 · moved 0 · comment 155`, `{}`, and live verdicts admit 9069, G1 63, G3 8, P1 104, P2 38 and P3 19. <!-- DERIVED at observation, 2026-11-15 -->
- AC4 — the `p9.sh` run of AC1 printed `exit 2 row P3 sleep at or over 5 s` for rows F1 to F5 and <!-- DERIVED from scratch-guard.js#POLL_SLEEP_FLOOR_S -->
  `exit 0` with nothing after it for rows F6 and F7, identical to the run before the edit.
- AC5 — `grep -c '^run_role_bash "W9-AC' tools/hooks/scratch-guard.test.sh` printed 13, and
  `grep -c '^FLOOR_ASSERTIONS=388$' tools/hooks/scratch-guard.test.sh` printed 1. <!-- DERIVED, 388 is 375 plus the 13 rows -->
- AC6 — `python -I "$SCRATCH/p9m7.py" tools/roles "$SCRATCH/p9m7"` printed
  `append resumed: bad 7 · result a1 · notified ['toolu_A'] | cold: bad 0 · result a1 · notified ['toolu_A']`
  and the same line for `torn`.
- AC7 — `grep -c '"$A23_EDIT" "$A23D" bad' tools/roles/adopt-roles.test.sh` printed 2, and
  `grep -c ': 7 line(s) did not parse' tools/roles/adopt-roles.test.sh` printed 2. `bash -n` over <!-- DERIVED from the bad count A23_EDIT seeds -->
  both edited suites exited 0, and `node -e 'require("./tools/hooks/scratch-guard.js")'` loaded it.
- Verdict parity — `p9.sh` before and after the edit gave the same exit and row for C2, C4, C5 and
  F1 to F7. What moved is C1 and C3, refused as P3 before and admitted after, which is review item
  M2's defect, and C6, admitted before and refused as G3 after, the one move §8 F1 accepts. `p9c.js`
  run before the edit, over the base module and a copy of the hook at `d07bb02a7`, printed the same
  `moved 0` and the same live verdict counts as after, so no verdict a real command reached moved.
- Timing — the same command at base and after, one run each, one at a time:
  `bash "$SCRATCH/p9.sh"` took 2.568 s before and 2.430 s after; `p9c.js` took 10.149 s before and 9.764 s after. <!-- PINNED 2026-11-15 -->
- Owed to the close: the three `New arm:` lines of §7, observed RED-first by the main loop — the
  W9-AC1 C1 to C5 and W9-AC2 C6 rows with the cut removed and with the cut opening at any `#`, the
  W9-AC4 F1 to F7 rows with `>=` become `>` in `checkPollWait` and with the `m` multiplier become 1,
  and arm 23's append and torn arms with `read_session_record` taking a record only at `offset` equal
  to the file size; both floors confirmed from real runs (`FLOOR_ASSERTIONS` 388 in the hooks suite,
  69 in the roles suite); and the gate legs §7 lists.
