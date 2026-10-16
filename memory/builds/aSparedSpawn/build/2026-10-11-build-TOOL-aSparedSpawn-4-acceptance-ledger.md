# Acceptance ledger — TOOL-aSparedSpawn-4

**Serves:** journal TOOL-aSparedSpawn-4

Node `a`, 2026-10-12, bash 5.3 under MSYS with Git for Windows, beside other sessions' work. The pass
ran no bar, no suite, no held leg and no slice of a suite. Every runner observation drove the real
runner over hand-built fixture repositories through the instrument committed beside this ledger,
`2026-10-12-build-TOOL-aSparedSpawn-4-direct-checks.sh`, against a copy of the parent runner at
`4f1913b1` (the "base") and the working tree's (the "cut"), both kept outside the fixture trees so a
copy's own bytes are no input of a key. Two first drafts of the cut runner redded there and were
fixed before these readings: a CRLF-ending output differed from the `$(cat …)` capture, because the
MSYS substitution strips a trailing CRLF as one newline, and the closed-descriptor specimen read
zero instead of refusing. `bash -n` passed on the runner, the instrument and every one of the 34
re-rendered suites. Every suite arm this unit adds or moves is OWED at VERIFYING and says so.

**Evidences:** TOOL-aSparedSpawn-4
- AC1 — `direct-checks.sh bytes` — a `sleep 1` leg's `.leg` seconds field read `1.694` (and `1.160`
  on an earlier draft), three decimals from `EPOCHREALTIME`. The evidence suite's AC1 arm and its
  scale-lost variant are OWED at VERIFYING.
- AC2 — `direct-checks.sh bytes` — the run-record `.out` copy and the `gate-logs` copy of all eight
  fixture legs, trailing newlines, a NUL, CRLF lines with a `\r\r\n` end, no output, a credential URL,
  a userinfo-free URL and a multibyte name, equal the base runner's byte for byte; the base also
  printed one `ignored null byte` warning the cut runner no longer prints. The evidence suite's AC2
  arms are OWED at VERIFYING.
- AC3 — `direct-checks.sh bytes` — the eight `gate-logs` names equal the base's, and `sp é/x y` maps to
  `sp____x_y.log`, one underscore per byte; a locale probe showed the expansion WITHOUT the C locale
  gives `a___b_c` where `tr` gives `a____b_c`. The evidence suite's locale-dropped variant is OWED.
- AC4 — `direct-checks.sh bytes` — the credential leg's copy reads `fetch https://***:***@host/x`, the
  userinfo-free one reads as printed, and both match the base. Modes read `-rw-r--r--` for the base's
  `chmod 600` copy and the cut runner's alike: MSYS on this node does not honour `chmod 600`, so the
  mask is unobservable here and the evidence suite announces that as a skip; its mode arms are OWED.
- AC5 — `direct-checks.sh pool` — over six legs, one red and one sleeping, the cut runner's `GATE` and
  `----` lines at `GATE_JOBS=1` equal those at `GATE_JOBS=4` and the base runner's, and no leg reads
  `(no result)`, on the final runner. The canary's pool-equivalence arm is OWED at VERIFYING.
- AC6 — `direct-checks.sh keys` — over a dirty tree (an edited tracked file, an untracked file under a
  guard, a staged edit), all six `input_key` ledger keys, a directory guard, a nested one, two files, a glob that
  takes the per-leg path, an absent path and an unguarded leg, equal the base runner's, and a
  `GATE_REUSE` bar reused all six on the precomputed keys, on the final runner. The base is the
  parent, which carries the reuse-key unit's definition. The evidence suite's per-leg and
  backwards-union arms are OWED at VERIFYING.
- AC7 — `direct-checks.sh git` — in a primary tree and a linked worktree the header's `head` and
  `worktree`, the log dir and the rc equal the base's; on an unborn branch `worktree`, log dir and rc
  equal the base's and `head` reads empty where the base read the literal `HEAD`, as S7 specifies.
  Read on a draft whose S7 lines are the final runner's; later edits touched only the output, the
  redaction and the ledger seconds.
  The evidence suite's AC7 arms are OWED at VERIFYING.
- AC8 — `direct-checks.sh forks` — the counter read the specimen's declared 5 forks and 1 exec, and the
  same specimen with its trace descriptor (the one its `PS4` trace writes to) closed first refused
  with 2. The run-log suite's SPAWNS arm
  carries the same counter and is OWED at VERIFYING.
- AC9 — `direct-checks.sh forks` — per-leg events, forks plus execs over ceiling-declaring legs at width
  1 with the spawn floor pinned: base 40 (25 forks, 15 execs), twice; cut 5 (2 forks, 3 execs), twice;
  the copy with one added `$(date +%s)` in `runleg` 7, its per-leg sites led by that line at +2. figure:
  `SPAWN_CEILING=5`, pinned in the run-log suite with its date and node from these readings, since the
  arm's own first run is OWED at VERIFYING. An unpinned floor read 10 and 7 on two runs of the same
  runner, the floor write landing in one trace only, which is why the arm pins it.
- AC10 — `direct-checks.sh procmon` — python execs before the first dispatch, base against cut: found
  kit 4 and 3, missing kit 3 and 2, refusing scope 4 and 3; the `run-gates: process-monitor:` line
  (which prints `PROCMON_WHY`) equals the base's for all three, the refusal's paths included. The SPAWNS arm's in-suite form is OWED.
- AC11 — `direct-checks.sh parity` — the marked region of all 67 copies equals
  `tools/lib/resolve_kit_dir.py`, the population covers every file `git grep -l '>>> resolve_kit_dir'`
  lists outside `memory/`, and no file there still captures the heredoc with `cat`. The re-render's
  own checker refused on any moved byte inside the markers and reported none; the parity suite is
  OWED at VERIFYING.
- AC12 — `direct-checks.sh ban` — the S12 predicate over a scratch copy of `agent-cap.test.sh` with its
  wrapper reverted (to `"$(cat <<'RKD'`) fired once, at line 73, and stayed silent on a comment spelling the idiom. The
  resolve-python suite's ban arm is OWED at VERIFYING.

Also observed directly: `fork-count.sh --only` on a frozen root read the one-leg row at 72 twice (its
ceiling 72; the parent read 95) and the two-leg row at 74 twice (the parent read 130), so the two-leg
row is lowered to 74; `sh_hygiene.py --spawn-idioms` narrowed to the runner reported no rising count in
the runner or any touched suite once the runner's `cat-file` row fell to 15 and its `printf-subst` row
went; `check-arms.py --check` still reports the same six unarmed exit sites in the runner.
