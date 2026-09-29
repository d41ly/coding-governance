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
reproduced against the parent's driver and suite unchanged: the HELD block's unreachable-node arm,
`AC4 the history row does not record the unreachable node` (the row gained `· resume` in unit 5),
the `--status` field
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
- AC2 — `grep -c 'LEASE_STALE_AFTER'` — over the `git show` blobs of all ten files the criterion
  names it prints 0 at the build commit c9c1927a, against 5, 2, 1, 2, 2, 1, 1, 1, 1 and 6 in the
  criterion's order at its first parent cd4127f4, and 0 in each at 364278a8. Check 22's join is
  the `unattended kit gate` leg, which exited 0 at 364278a8 with no check-22 finding.
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
- AC7 — `skip · HELD` — the tick's `--dry-run` over the HELD fixture printed its `skip · HELD`
  decision, naming the durable schedule `--hold` printed as the restart, and no `resumed ·`; at
  BUILDING it printed `resumed · attempt 1`.
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
- AC13 — `tools/unattended/STOPS.template.md` — `git show` at the build commit c9c1927a and its
  first parent cd4127f4: every zero-count string the criterion lists, 25 readings over the files
  it names, prints 0 at c9c1927a and at least 1 at cd4127f4, and still 0 at 364278a8; the six row
  texts units 62 and 63 key on each print exactly 1 at c9c1927a; `non-terminal and not` prints 1
  in both the Skill and the protocol template. At c9c1927a the Skill's tick paragraph names checks
  10, 26 and 51, the Skill names no `LEASE` line where cd4127f4's line 840 did, placements 2 and
  3 of Record the run name `primary` beside an in-place placement naming `--prepare`, and the
  `--liveness` entry of `tools/unattended/VERBS.template.md` lists `HELD`. At 364278a8 the
  `unattended skill wiring` leg exited 0 printing
  `in sync (skill rendered from template + .unattended.conf)`, and `unattended kit gate` exited 0.
- AC14 — `wc -l` — against the parent's `git cat-file -s` and line counts: protocol template and
  render -133 bytes and -1 line, stop contract and render -9 and -12, verb carrier and render -85 and
  -1, the `unattended` dossier -49 and 0, the `unattended-stops` dossier -1 and 0, the kickoff
  manifest -4 lines; none grew.
- AC15 — amended rev-11 — `tools/unattended/unattended.test.sh`, like the stop-guard and resume-tick
  suites, is not run for this landing, by the owner's ruling of 2026-09-29, so the three suites'
  `verdict clean` is waived and every arm it names stays unobserved. The floor figures, read with
  `git show` at the build commit and its first parent, are not a suite run and the ruling does not
  reach them; this ledger records no reading of them. Section 9, rev-11.
- AC16 — `TOOL-dDerivedDocket-61` — `memory/DECISIONS.md`'s TOOL heading carries one row keyed by it,
  294 characters, naming the one lease record, the one bound and the HELD carve-outs.
- AC17 — `grep -c 'one lease and one restart path' memory/guides/SESSION-KICKOFF.md` — prints 0.
- AC18 — `KIT_UNATTENDED_VERSION=1.29` — `grep -c` prints 1 over `tools/unattended/unattended.sh`
  and over `tools/unattended/check-unattended.sh` at the build commit c9c1927a and at da80b2e5,
  as at the parent, so the unit moved no version; 364278a8 carries 1.42 from later units.
  `unattended@1.29` counts 1 in each of the nine kit templates at both c9c1927a and cd4127f4. No
  added line of the unit's diff, cd4127f4 to da80b2e5, spells a `tools/<kit>/` literal, and the
  `install-prefix (shipped surface)` leg exited 0 at 364278a8 with no undeclared spelling.
- AC19 — `python tools/lexicon/lexicon.py --suggest` — run in the frozen worktree at 364278a8
  with `--as sh.function`, it printed `OK` for each of the six names §4's Inventory mints and for
  `check_lease_fresh`, and the `lexicon naming predicates` leg exited 0 there. The new check-58
  branch's text is asserted by a `hit` line in `tools/unattended/unattended.test.sh` and has no
  row in `memory/project/unarmed-branches.txt`, and the
  `harness arms (fail branches armed or pinned)` leg exited 0. That registry is byte-unchanged
  from cd4127f4 to da80b2e5, and that diff adds or removes no `fail 9`, `fail 27`, `fail 29`,
  `fail 49` or `fail 56` line in the driver.
- AC20 — amended rev-11 — `tools/unattended/unattended.test.sh` is not run for this landing, by the
  owner's ruling of 2026-09-29, so the driver suite's run of this arm is waived and stays
  unobserved. The pass's fixture run and its staged RED against a `derive_last_move` with the
  gate-log term cut stand as the prose above reads them. Section 9, rev-11.
- AC21 — amended rev-11 — `tools/unattended/unattended.test.sh` is not run for this landing, by the
  owner's ruling of 2026-09-29, so the driver suite's run of the repeating arm is waived and stays
  unobserved. The direct fixture runs stand observed in this pass, as the prose above reads, and so
  does the staged RED against a `check_lease_fresh` that reads a dead probe as stale. Section 9,
  rev-11.
- AC22 — amended rev-11 — `tools/unattended/unattended.test.sh` is not run for this landing, by the
  owner's ruling of 2026-09-29, so the driver suite's run of the repeating arm is waived and stays
  unobserved. The direct fixture runs stand observed in this pass, as the prose above reads. Section
  9, rev-11.
- AC23 — amended rev-11 — `tools/unattended/unattended.test.sh` is not run for this landing, by the
  owner's ruling of 2026-09-29, so the driver suite's run of the repeating arm is waived and stays
  unobserved. The direct fixture runs stand observed in this pass, as the prose above reads. Section
  9, rev-11.
- AC24 — amended rev-11 — `tools/unattended/unattended.test.sh` is not run for this landing, by the
  owner's ruling of 2026-09-29, so the driver suite's run of the repeating arm is waived and stays
  unobserved. The direct fixture runs stand observed in this pass, as the prose above reads, and so
  does the staged RED against the ledger path through `resolve_sidecar_dir` and a fifth field
  stamped `-`. Section 9, rev-11.
