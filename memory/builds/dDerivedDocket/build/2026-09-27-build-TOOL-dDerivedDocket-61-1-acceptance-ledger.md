# TOOL-dDerivedDocket-61 — acceptance ledger

**Serves:** journal TOOL-dDerivedDocket-61

The two lease models the origin/main merge left side by side are one. The per-slug lease file is
retired from the driver: no verb reads or writes a `.lease` file, `stage_or_fail` and `run_bounded`
refresh nothing, and `LEASE_STALE_AFTER` is gone from the driver, the kit gate's allow-list,
`kit.toml`, both confs and the protocol's key table. The lease is the six run-state facts
`write_lease` writes. `derive_last_move` is `print_liveness`'s four-signal clock, extracted, and
`check_lease_fresh` grades a run-state file with it against `RESUME_STALE_BOUND`. `--liveness`
reads `HELD` as its own state and verdict, and a LANDING whose landing commit the common dir's
`landed.<slug>.log` names as `TERMINAL`. The stop-guard allows a `HELD` stop with reason `held`
directly after `terminal`, and the resume tick skips a `HELD` run by name. The resume matrix is
re-keyed onto the facts: the holder writes nothing unless its session or pid moved or the record
carries no `lease-utc`, the same session under a new id is its own relaunch and takes the run over
through `run_takeover` unless its recorded pid is alive and is not `CLAUDE_PID` (a new check-58
branch), the leaseless rows keep the build folder's clock against the one bound and gain the
`--replaces` path, and a pushed landing `--landed` has not observed is re-bound, staged and never
committed, on a branch where that landing's `--landed` runs. `check_lease_only_diff` in the library
lets `read_landing_commit` and `--landed`'s `primary` clean check read a difference confined to the
six lease-fact lines as none. The keepalive read-back is `check_keepalive_reaped`, called by both
landing modes. Unit 28's ledger derives its path from `resolve_landed_log` and stamps the record's
`keepalive` fact. The carriers, renders, both dossiers, the kickoff manifest and the decision log
follow.

No merge bar, no gate leg and no `*.test.sh` suite ran in this pass. The direct checks were the
driver, the hook and the tick run over scratch fixtures built the way the driver suite's prologue
builds one, and the new suite blocks run alone behind hermetic replicas of their suites' prologues:
the driver block 98 assertions green (n 20 -> 118), the stop-guard arms 12 green, the tick arms 10
green. Each was staged RED: the driver block against the driver at this unit's parent (43 failures),
against a `derive_last_move` with its gate-log term cut (the AC20 arm red), against a
`check_lease_fresh` that reads a dead probe as stale (the AC21 arm red), and against the ledger
path through `resolve_sidecar_dir` and a fifth field stamped `-` (the AC24 arm); the stop-guard and
tick arms against the hook, driver and tick at the parent. The retargeted HELD, derived-terminal
and process-ledger blocks were re-run the same way: the HELD block's executed count is 159 at the
parent and now, and the whole file's static count moved by exactly the 98 new assertions.

Four reds that exist at the parent and are not this unit's surfaced on those replicas, each
reproduced against the parent's driver and suite unchanged: the HELD block's `AC4 the history row
does not record the unreachable node` (the row gained `· resume` in unit 5), the `--status` field
arm's `· parked 1` over a derived-LANDED fixture, and in region one the `--status`/`--resume`
agreement arm and `resume names the directive table`, plus the conf-default arm naming `CORE_FLOOR`.

AC2, AC13, AC15, AC18, AC19 and AC20 to AC24 carry `permission:` lines, so none gets a line here;
their direct checks ran in this pass all the same: the AC2 and AC13 greps read 0 where they must and
1 at the parent, every stop-contract witness reads exactly 1, the version pins read 1, no added kit
line spells a kit path, every new name answered `OK` to `lexicon.py --suggest`, no pinned row of
`memory/project/unarmed-branches.txt` moved, and AC20 to AC24's fixture runs matched their criteria.

**Evidences:** TOOL-dDerivedDocket-61
- AC1 — `find "$(git rev-parse --git-common-dir)" -name '*.lease'` — printed nothing inside every
  fixture after the AC3 to AC11 and AC21 to AC24 runs, and the code-line grep over the driver for the
  eight retired names and `RB_LEASE_` printed 0.
- AC3 — `verdict: LIVE` — with the recorded session's transcript touched and the commit aged,
  `--liveness` read LIVE and the same session's `--resume --keepalive-id k2` printed
  `lease replaced · keepalive k1 -> k2` with no check 58; a recorded pid alive and not `CLAUDE_PID`
  refused at 58 naming both pids, byte-unchanged, and session `T` refused at 58, byte-unchanged.
- AC4 — `stale: yes` — aged past the bound, `--liveness` read stale, `--status` printed
  `presumed-stopped` naming the 5400 s bound `--liveness` prints as `stale-bound`, and `T` took the
  run over; inside the bound `--liveness` read `stale: no` and the same call refused at 58.
- AC5 — `verdict: HELD` — over an aged HELD fixture `--liveness` printed `state: held` and
  `verdict: HELD` with `stale: yes`, and its fourteen keys in their order.
- AC6 — `"reason":"held"` — the hook fed the HELD fixture's session exited 0, printed nothing, and
  its sidecar line carried `"reason":"held"`; the same fixture at BUILDING was blocked `run-open`.
- AC7 — `skip · HELD` — the tick's `--dry-run` over the HELD fixture printed `skip · HELD · its
  restart is the durable schedule --hold printed, never this tick` and no `resumed ·`; at BUILDING it
  printed `resumed · attempt 1`.
- AC8 — `phase LANDED (derived:` — `T`'s `--resume --keepalive-id k2` over a pushed LANDING recorded
  session `T` and keepalive `k2`, printed both, staged the record and left it deriving LANDED;
  `primary` `--landed` from `T` passed checks 2 and 55 and wrote `LANDED`, `in-place` reached the
  derivation; a hand-edited witness read `not committed as it stands` and, re-bound, refused
  `--landed` at check 2; `--preflight` over the re-bound record and `--hold` over a record differing
  only in `session` each refused at check 2.
- AC9 — `keepalive-reaped: checked` — under `in-place`, a listing naming the recorded keepalive
  refused at 53, one free of it printed `keepalive-reaped: checked` on the line before
  `phase LANDED (derived`, and `CLAUDE_CODE_SESSION_ID=T` refused at 55.
- AC10 — `landed.<slug>.log` — landed from linked worktree W1, the line sat under the path
  `git -C W1 rev-parse --git-common-dir` prints and nowhere under W1's own git dir; from W2 detached
  at the landing commit `--liveness` read `TERMINAL`, the hook allowed `terminal`, `--status` printed
  `landed · observed by --landed at`, and with the remote gone and the tree aged `--status` printed no
  `presumed-stopped` while `--resume --keepalive-id C` printed nothing to resume and wrote nothing; a
  later LANDING committed in W1 read `FINISHED-UNSTAMPED`.
- AC11 — `git status --porcelain` — the holder's `--resume --keepalive-id k1` under the recorded
  session and pid exited 0 with the tree clean; `CLAUDE_PID=Q` re-recorded the pid and staged;
  session `S2` re-recorded the session beside pid `P` and staged; a record keeping `keepalive` alone
  gained the other five facts at its holder's resume.
- AC12 — `--resume --keepalive-id C` — from another session it took over a HELD fixture whose
  condition was met and returned it to `held-from`; with `lease-utc` set after `held-at` on a fresh
  clock it refused at 58 and wrote nothing; over a leftover `<slug>.lease` naming `k9`,
  `--hold --reaped k9` refused at 56 naming `k1`, the holder's resume wrote nothing, and the leftover
  file was byte-unchanged.
- AC14 — `wc -l` — against the parent's `git cat-file -s` and line counts: protocol template and
  render -133 bytes and -1 line, stop contract and render -9 and -12, verb carrier and render -85 and
  -1, the `unattended` dossier -49 and 0, the `unattended-stops` dossier -1 and 0, the kickoff
  manifest -4 lines; none grew.
- AC16 — `TOOL-dDerivedDocket-61` — `memory/DECISIONS.md`'s TOOL heading carries one row keyed by it,
  294 characters, naming the one lease record, the one bound and the HELD carve-outs.
- AC17 — `grep -c 'one lease and one restart path' memory/guides/SESSION-KICKOFF.md` — prints 0.
