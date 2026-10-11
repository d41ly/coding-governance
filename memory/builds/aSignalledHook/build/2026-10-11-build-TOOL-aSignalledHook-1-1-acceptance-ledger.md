# TOOL-aSignalledHook-1 — acceptance ledger

**Serves:** journal TOOL-aSignalledHook-1

No merge bar ran in this pass and no suite ran whole. Each criterion was observed on node a (git
2.54.0.windows.1, MSYS bash 5.3.9) by a SLICE: the suite's prologue plus the new block, run as a
temporary script inside the kit directory and removed before the commit. Every arm was also run
against a staged break: the hook or the lander as it stood at b726385f, copied into the fixture by a
forward-slash path, and the hook with its bar moved back into the foreground. A first old-hook run
was invalid: a backslash path left the fixture's hooks directory empty, so every push "landed". The
fixture now refuses to grade without its hook, and the runs below are the corrected ones. The whole
`pre-push self-test`, `pre-push run-log line` and `push-main self-test` legs are owed at the close.

**Evidences:** TOOL-aSignalledHook-1
- AC1 — `git push` — with the stub bar sleeping, `TERM` and `HUP` to the hook each refused (git rc 1), left the remote unmoved, wrote `signalled` to `pre-push-refusal` and stopped the bar; the b726385f hook LANDED both pushes.
- AC2 — `sleep` — the signal was handled 6 to 8 s after it was sent, against the stub's 30 s sleep; with the bar moved back into the foreground it was handled after 32 and 34 s.
- AC3 — `push-main.sh` — through a hook that wrote `pre-push-bar` as default and exited 0 with no `pre-push-allow`, the lander printed `landed UNGATED`, exited 4 and wrote no lander marker; the b726385f lander exited 0 and called the push landed.
- AC4 — `pre-push-allow` — after the tracked-bar landing of case 9b the record named the pushed HEAD and `push-main.sh` printed `landed` with the marker written.
- AC5 — `exit=clean` — the run-log AC3 arm read `exit=clean`, `decision=refuse-signal` and `rc=143` on END with the bar stopped (26 assertions with the `EXITS` arm); the b726385f hook read `unclean` and `full|0`.
- AC6 — `TERM` — a fixture `gate-env.sh` that signals the shell sourcing it ended the push as `signalled`; the b726385f hook LANDED it.
- AC7 — `254` — a bar exiting 254 was refused as `gate-red` by the hook, and by the b726385f hook too: the fork-failure shape was never a fail-open, and the arm pins that.
