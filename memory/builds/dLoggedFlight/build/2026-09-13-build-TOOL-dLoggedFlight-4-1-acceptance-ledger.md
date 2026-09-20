# Acceptance ledger — TOOL-dLoggedFlight-4

**Serves:** journal TOOL-dLoggedFlight-4

Tier-2 · node d · 2026-09-14 · the build pass of the pre-push hook's run-log lines, against spec
rev-5, which this pass wrote before its code, and the fold of its bug-class checklist. Every line is
OBSERVED except AC8's verdict half, which is written as owed. `<suite>` is
`.githooks/pre-push.runlog.test.sh`, run directly from Git Bash and never through the gate runner.
Its three full runs at the build commit printed `PASS (226 assertions)` in 32 to 39 s, and its run
after the fold printed `PASS (228 assertions)` against a floor of 228, in 33 s. No gate leg was run,
per the owner's instruction of 2026-09-13, and no suite that existed under `tools/unattended/` before
this build ran. The closing diff review's round-1 fold of L1 bumped the spec to rev-6 and widened
AC2, whose line below records what that fold observed; its full run printed `PASS (240 assertions)`
against a floor of 240, in 28 s.

## The criteria

**Evidences:** TOOL-dLoggedFlight-4

- AC1 — `bash <suite>` (`check_ac1_decisions`) — a feature push under a red stub, a marked
  default-branch push under a green stub and an unmarked one wrote three START and END pairs on shared
  nonces. They read `skip-nondefault`, `full` and `refuse-raw`, with `rc` 0, 0 and 1, `lander` 0, 1
  and 0, `exit=clean`, and each START's `ref.1` the whole ref line git fed it. A refusal at the
  observed-default check wrote one `ev=once` line reading `refuse-default-branch` with its worktree,
  `lander=0` and no nonce. After every arm the journal read with no bad line and no END without its
  START. RED seen five ways: `trap - EXIT` before the feature exit, the ref line not kept, `lander`
  written only when 1, END's nonce changed, and the once line's writer call removed.
- AC2 — `bash <suite>` (`check_ac2_credentials`) — an `ssh://user:pass@` URL was reached through a
  stand-in for ssh, since git runs pre-push only once connected. The named remote wrote `remote=cred`
  and `url_userinfo=1`; the bare URL wrote `remote_unnamed=1` and `url_userinfo=1` with no `remote`;
  a refusal before the loop to that URL wrote an `ev=once` line with `remote_unnamed=1`,
  `url_userinfo=1` and `lander=0`. `grep -c pass` over the whole journal read 0 after every arm. RED
  seen with the URL added to the named fields, with `remote` written whenever `$1` is set, and with
  the once line writing `$1` itself instead of calling the shared renderer. The fold of L1 added a
  typed `https://user:pass@` URL that an `insteadOf` rule rewrites to the origin's own path, pushed
  and then refused before the loop. Both wrote `remote_unnamed=1` and `url_userinfo=1` with no
  `remote`, and no line of either held `://` or `@`. RED seen with `remote` written on the
  difference from `$2` alone, which wrote the typed URL whole and put `pass` on two lines, and with
  userinfo read off `$2` alone. AC7's exec counts read 3 and 10, as before the fold.
- AC3 — `kill -TERM` (`check_ac3_term`) read `exit=unclean` — sent to the hook only after the stub
  bar wrote its ready file and was checked alive, TERM ended the hook while the stub was still
  running. END kept `decision=full` and named the bar's `gate_run`. RED seen with
  `trap 'exit 143' TERM` added: the hook outlived the signal until the stub's 20 s sleep ended.
- AC4 — `bash <suite>` (`check_ac4_join`) — the stub bar was handed `GATE_RUN_ID=push-<digits>-<pid>`
  and END's `gate_run` was that value. A copy of the real runner then ran one fixture leg under the
  hook: its `gates.log` line read `run=` END's `gate_run`, and the leg recorded `<unset>`. RED seen
  with the id not exported (the stub saw none and the runner fell back to its own id), with a
  different value exported, and with the runner copy's `unset GATE_RUN_ID` removed, where the leg saw
  the push's id.
- AC5 — `GOV_RUNLOG=0` (`check_ac5_write_failure`) — with the journal directory replaced by a file,
  a green bar, a red bar and a refusal before the loop each kept their switch-off `rc` and stdout,
  and stderr gained ONE `pre-push: run log` line naming `runlog/pushes.log`, for two failed writes.
  `GOV_RUNLOG=0` wrote no line and printed no run-log line; `GOV_RUNLOG=1` wrote a pair. RED seen with
  the failed write exiting 5, with the warning on stdout, with the warn-once guard removed, and with
  the switch test removed.
- AC6 — `bash <suite>` (`check_ac6_many_refs`) — a real push of 21 refs, named short enough that
  eleven would fit the byte cap, wrote a START with `ref.10` naming the pushed sha, no `ref.11`,
  `ref_more=11`, under 2048 bytes, and every written ref a whole four-field line. RED seen with the
  count cap raised to 100: `ref.11` appeared and `ref_more` read 8. The first draft used names long
  enough that only ten fit, where the byte cap alone writes the same line; spec rev-5 records why the
  names changed.
- AC7 — `bash -x` (`check_ac7_spawns`) — traced with the function and line on every trace line, the
  skip-nondefault and full paths from a primary clone and from a linked worktree made 3 and 10
  external execs each, equal to a baseline copy whose six writer functions return at once, and the
  writer owned none of them. Through `PPRL_BEFORE=<the hook at 5347a5d8>` the same four paths made
  3, 10, 3 and 10 against the hook before this unit. All four wrote to `<common-dir>/runlog/pushes.log`,
  each naming its own tree, with nothing under the worktree's own git dir. A clone's first push paid
  one `mkdir`, the writer's. RED seen with a `date` in the writer, with an unconditional `mkdir -p`,
  with the `commondir` read skipped, with a primary tree resolving no journal, and with a `git` call
  added beside the journal-root line.
- AC8 — `GATE_SELFTESTS=1` — OWED to the post-build gate run, which records it: the
  `pre-push run-log line` leg at or above its floor inside its budget row, and `govkit selfcheck`
  green with the suite claimed by the `push-main` entry as `project-owned`. What this pass observed is
  the declarations, through `check_ac8_declarations`: the project-owned rule, the budget row, one held,
  guarded and bounded manifest leg, and the registry's `[[exempt_leg]]` row. RED seen with each of the
  four undone on a mirror.
  MET at the post-build run: `pre-push run-log line` is GREEN, printing `PASS (240 assertions)`
  against its floor of 240 in 37.6 s, inside its 60 s budget row, and `govkit selfcheck` is GREEN
  over 27 of 27 registry entries with 0 unclaimed.

## The decisions AC1 does not reach, and the exits

`check_dec_rest` observed `skip-delete`, `refuse-manifest`, `refuse-head` and `scoped`, and the other
two refusals before the loop, each by its own message and its own line. `check_exits` enumerates the
hook's eleven exit sites by their code: the two above the journal root exempt, the three once
refusals between it and the trap, and every site below the trap carrying `RUNLOG_CLEAN=1` beside its
exit. Every decision the table names was written by some arm. Each run it stages an unarmed exit, an
unmarked one, a second copy of an armed code, an exemption below the root, and a comment-and-string
control into copies. RED seen with an unarmed `exit 7` added below the hook's trap, with a decision
never written, and with the delete and scoped decisions mislabelled.

## The fit

The runlog grammar asks a producer that truncates to produce what `render_line` produces, and
`check_cap_fit` holds the hook to it on both steps, byte for byte. Step one: twelve refs with
200-character names, where the count cap wrote `ref_more=2` and whole `ref.<i>` fields then dropped
into it. Step two: no ref and a remote name over the cap, in ASCII, behind three-byte characters
where a cut landed inside one, and behind TABs where a cut halved an escape. RED seen with step one
off, with the fit off, with the character repair removed, with the escape repair removed, and with
the lowest index dropped first.

## Staged RED

36 breaks, each applied to a MIRROR of the unit's files in a scratch dir, never to the working tree,
and each run through the mirror's own copy of the suite with its target arm selected, or whole for
the floor and the decision join. All 36 went RED on a FAIL line carrying the text its break aimed at,
and an unmodified mirror printed `PASS (226 assertions)` before and after the batch. One break first
came back NOT RED: a `git` call added at the top level passed AC7, because the baseline runs the same
top-level line. AC7 then gained the writer attribution, and the break went RED.

The checklist over the build commit selected `two-answers-to-one-question`, and the suite held two
second copies. AC7 listed the writer's six function names by hand, twice, so a NEW writer function
called from the top level ran on both sides of the baseline and was owned by nobody: staged on a
mirror, the build commit's suite passed it and the folded suite, which reads the names from the hook
by their `*_push_*` form, went RED. CAP's reconstruction typed the hook's count cap of 10, and now
reads it from the hook: its control, the cap raised to 11 on a mirror, stays green.

## Owed to the post-build gate run

Every leg of the spec's section 7, and the run records each verdict after it:

- `pre-push self-test`, `pre-push run-log line` and `push-main self-test`;
- `run-gates run-log line`, `run-gates canary` and `run-gates evidence`, since the runner changed;
- `testsuite counts (every bar self-test prints one)`;
- `every held leg is budgeted, every budget row resolves`;
- `govkit selfcheck`, `codebase-map coverage + freshness` and `lexicon naming predicates`;
- `install-prefix (shipped surface)`;
- `shell hygiene (a loop fed by a command substitution)` and `memory hygiene`.

The post-build run happened at `9e948546`, the whole bar with every guard lifted and the kit
self-tests on: 111 legs ran and 110 are GREEN, in 690.8 s of wall at width 8 against the profile's
declared 21600 s. Every leg listed above is GREEN; `pre-push run-log line` printed
`PASS (240 assertions)` and `run-gates run-log line` printed `PASS (192 assertions)`. The run's
one RED, `govkit selftest`, is on none of these legs: its 30 failing assertions are the IDENTICAL
set `origin/main` carries, pre-existing, untouched by this build and being fixed in a separate
session. It is not called green here.

## Residue

- The runner now removes `GATE_RUN_ID` once read, a line in the gate runner's file that the spec named
  only at rev-5. The hook's export would otherwise reach every leg, and the runner's own suites start
  several nested bars per scratch clone. None of those suites ran in this pass.
- `tools/install-prefix-carried.txt` did not move. The new registry reason names a descriptor one
  directory below its kit dir, which the carried predicate does not count, measured by applying its
  pattern to the registry by hand before and after.
- `tools/govkit/subject-pins.tsv` gained its row by hand, not by `govkit selfcheck --write`, which
  runs the selfcheck gate as it writes.
- The leg's ceiling is 600 s against a worst direct reading of 39 s, and its budget row is the file's
  60 s floor.
- The hook's lines appear only once the primary tree has checked this change out, because
  `core.hooksPath` resolves there; the hook's header says so.
