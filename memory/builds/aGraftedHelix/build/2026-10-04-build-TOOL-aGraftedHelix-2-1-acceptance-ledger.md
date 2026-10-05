# Acceptance ledger — TOOL-aGraftedHelix-2

**Serves:** journal TOOL-aGraftedHelix-2

Node `a`, 2026-10-05. The build commit is `4b516468`, over the spec's rev-3 commit `7143e8f6`. No
merge bar and no self-test suite ran in this pass. The card suite's new `claims —` block was run
ALONE, behind the suite's prologue and its card fixture, as a slice outside the tree with `TMPDIR`
under a short `%TEMP%` root: 25 of 25 green against the built checker. Every arm the checker can
move was then observed RED against staged checker copies, eight of them carrying nineteen breaks,
each copy built by an exact-once replacement and never committed. Three arms are liveness probes of
the fixture (the stub driver's marker, the held stdin, the driver's own journal write); they go red
when the fixture cannot fail, not when the checker breaks. The whole suite is the main loop's at
VERIFYING, and the slice count is the evidence for its floor of 205.

**Evidences:** TOOL-aGraftedHelix-2
- AC1 — `claims — 7 on the remote · 5 shown · 2 hidden` — over the seven seeded claims the card
  listed zLive, yHeld, xBare, wStale and vLanded in verdict order, xBare as `beat -` and `unknown`,
  with uStaleOld and tAborted hidden. Red when the order key was the slug alone, when the hide test
  dropped its verdict guard (the held claim hid), and when the cell moved below `recent —`.
- AC2 — `UNVERIFIED` — the line after `live —` was the `claims —` head, and `--card --check` over
  that card printed no `UNVERIFIED` line. Red when the cell was rendered after the recent block, and
  red when a row carried a path token (`x/y.md`), which the check then graded UNVERIFIED.
- AC3 — `claims — skipped: no .unattended.conf in this tree` — with the conf moved aside the card
  wrote, exit 0, and carried that line. Red when the conf test was deleted: the driver ran.
- AC4 — `UNATTENDED check 91 FAILED` — with the remote re-pointed at a path that does not exist the
  card wrote, exit 0, its cell `claims — skipped: UNATTENDED check 91 FAILED — …` cut to 160 of 160
  bytes, and no `none on the remote` anywhere. Red when the refusing branch printed none, and red at
  284 bytes when the cut was deleted.
- AC5 — `claims — skipped: --claims did not answer within 2s` — a driver replaced by `sleep 30` with
  `CARD_CLAIMS_BOUND=2` gave that cell and the write returned in 5 s. Red when the read ran without
  `timeout`: the cell read none and the write took 32 s. A separate arm reads the shipped defaults
  from the checker, 15 and 86400, red under a default of 16 and under 86401.
- AC6 — `FETCH_HEAD` — HEAD, `for-each-ref refs/heads refs/remotes` and the absence of FETCH_HEAD in
  both the worktree's git dir and the common dir were unchanged across the AC1 write, while the
  liveness arm counted the seven claims under `refs/gov/` in the clone, the driver's private cache.
  Red when the read also fetched into `refs/remotes/origin/claims/*`, which wrote FETCH_HEAD too, and
  the liveness arm red when the read was replaced by a canned `claims: none`.
- AC7 — `bash tools/check-install-prefix.sh` — exit 0, `clean — 331 tracked file(s) graded`, no line
  of the engine named. Red, exit 1, naming `skills/session-kickoff/manifest-check.sh:299` and the
  `unattended` kit, when the driver line was staged as `$ROOT/tools/unattended/unattended.sh`.
- AC8 — `git diff --name-only 5266d22e -- skills/session-kickoff/` — at `4b516468` it listed
  `skills/session-kickoff/manifest-check.sh` and `skills/session-kickoff/manifest-check.test.sh`
  and nothing else. The post-landing half, `bash tools/check-wiring.sh` in the primary tree, is the
  main loop's after the landing and did not run here.
- AC9 — `bash tools/check-kit-versions.sh` — exit 0, `clean — 16 declared carrier(s) under tools/`;
  `bash skills/session-kickoff/manifest-check.sh` exit 0 after the re-stamp at `7143e8f6`; and
  `python tools/govkit/govkit.py epoch --base 5266d22e` printed `kickoff-manifest · clean · 1.17`.
  Before the pin and cut arms were folded into the build commit, the same epoch printed
  `kickoff-manifest · FAILED · last bump 7cc4e3f19d precedes last move cc69469c31`, which is why
  the unit is one build commit.
- AC10 — `--card --replay --session t2` — with the remote broken the replay printed the stored head
  `claims — 7 on the remote · 5 shown · 2 hidden` unchanged, and a replay with no stored card wrote
  `claims — skipped: --card --replay reads no remote`. Red when the replay re-rendered as a write
  (check 91 printed instead), and the no-card arm red when the replay guard was deleted. Wall on
  node `a`, 2026-10-05, with 17 bash processes on the node, card write in the fixture worktree:
  5360 ms and 6497 ms with the claims read, 1574 ms and 1742 ms without it, in two green runs.
- AC11 — `CARD_CLAIMS_ROWS` — over nine landed claims and a fresh live `zzLive` the card printed
  `claims — 10 on the remote · 10 shown · 0 hidden`, eight rows read from the checker's constant,
  zzLive first, then `… 2 more`. Red when the rows ignored the cap, when the order key was the slug,
  and when the head counted only the printed rows as shown.
- AC12 — `claims — skipped: no unattended driver resolves in this tree` — with the driver deleted
  the cell read that line; with a `timeout` shim failing every `-k` call the cell named
  `timeout -k` and the stub's marker did not exist; with the card's stdin a read-write fifo held
  open (amended rev-3, not a `sleep 30 |` pipeline) and `CARD_CLAIMS_BOUND=2` the stub that reads
  stdin answered `claims — none on the remote`. Red when the empty-driver test was deleted, when
  the `timeout -k` probe was deleted (the stub ran and touched its marker), and when the driver's
  `</dev/null` was deleted.
- AC13 — `grep -c "SUPERSEDES KICK-aReplayedCard-1's no-fetch clause and its card budget:" memory/DECISIONS.md` — printed 1 over the records commit that carries this ledger.
- AC14 — `driver.log` — with `GOV_RUNLOG` unset in the caller, a card write left the journal's line
  count unchanged, and the driver called directly the same way then added lines to it. Red when the
  call's `GOV_RUNLOG=0` was deleted.
