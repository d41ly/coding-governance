# TOOL-dDerivedDocket-62 — acceptance ledger

**Serves:** journal TOOL-dDerivedDocket-62

One worktree answers for a slug. `resolve_holder_worktree` keys a record to the worktree whose own
HEAD is its run's branch, `run-branch` else `branch-ref`, and `--liveness` reads every other copy
`ELSEWHERE`, second after `TERMINAL`, printing a fifteenth key, `holder-ref`; an unreadable HEAD is
the existing check-52 dead probe. The resume tick skips `ELSEWHERE` by name and skips a record
naming no branch as `NO RUN BRANCH` wherever its verdict would act. The stop-guard allows an
`ELSEWHERE` stop with reason `elsewhere`, directly after `held`. `check_holder_worktree` holds one
new check-58 branch, called once in `verb_resume`, for a record carrying `lease-utc`, after unit 61's
observed-landing row and ahead of the first HELD row: it names the run's branch, the worktree that
has it checked out or that none does or that no such branch exists, and this worktree's HEAD, and
writes nothing. The verb carrier, the stop contract's §8, the protocol's KEEPALIVE paragraph and the
Skill's tick, what-wakes and Resume text follow, every render re-rendered, and the
`unattended-stops` dossier gains the rule.

No merge bar, no gate leg and no `*.test.sh` suite ran in this pass. The direct checks were the
driver, the tick and the hook run over a scratch two-worktree fixture (main worktree on `run`, a
linked one added on `wave` after the record commit), and each new suite block run alone behind a
replica of its suite's prologue, with HERE pointed at a kit copy: the driver block 39 assertions
green (n 20 -> 59), the tick arms 18 green beside the AC7, AC14, U61 AC10 and U13 AC4 arms they
retarget or share a fixture with (53 of 53), the stop-guard arm 5 green. Each was staged RED: the
driver block against a `check_holder_worktree` that always returns 0 (12 failures), one called only
inside the working branch (the HELD arm, 2), one called for every record (AC14, 4), one also at the
head of the derived-terminal branch (AC6, 6) and one ahead of the observed-landing row (AC6's
observed read, 2); the tick arms against a driver whose verdict chain drops ELSEWHERE (10), one
placing it after FINISHED-UNSTAMPED (3) and a tick without the NO RUN BRANCH row (3); the stop-guard
arm against a hook without the `elsewhere` row (3). Spec rev-7 records that the no-run-branch tick
arm is RED against the tick copy, not the driver one. Acting on the bug-class checklist's
two-answers class, unit 61's re-bind row now reads the run's branch and this worktree's HEAD
through `resolve_holder_worktree` rather than a second spelling of the same key, with its behaviour
unchanged: its AC23 arm ran green beside this unit's block behind the same replica, 47 of 47.

AC3, AC9, AC11, AC12, AC13 and AC14 carry `permission:` lines, so none gets a line here; their direct
checks ran all the same. AC3's dry-run printed `skip · HELD` for the run worktree and
`skip · ELSEWHERE` for the linked one and no `resumed ·`. Every AC9 grep read its figure: 1, 1, 1, 1,
1 and 0 in the protocol, 1, 1 and 1 in the Skill, and 2, 5 and 3 in the tick and hook. AC12's three
names answered `OK` to `lexicon.py --suggest --as sh.function`, the new check-58 branch is armed by
the driver block's full-signature `hit`, `memory/project/unarmed-branches.txt` is untouched, the
version pin reads 1, and no added kit line spells a kit path. AC13's dry-run printed one
`resumed · attempt 1`, for the run worktree reading FINISHED-UNSTAMPED, and `skip · ELSEWHERE` for
the sibling. AC14's run-worktree calls matched a copy whose `check_holder_worktree` returns 0, output
with digits folded and `git status --porcelain` alike.

**Evidences:** TOOL-dDerivedDocket-62
- AC1 — `verdict: ELSEWHERE` — with a gate log touched five minutes ahead under the run worktree's
  git dir only, `--liveness tRun` printed `verdict: LIVE` there and `verdict: ELSEWHERE` in the
  linked worktree, each on stdout the fourteen keys in their order then `holder-ref: refs/heads/run`
  last; with the log removed the run worktree read STALE and the linked one still ELSEWHERE.
- AC2 — `skip · ELSEWHERE` — `resume-tick.sh --repo <fixture> --dry-run` printed `skip · verdict LIVE`
  for the run worktree and `skip · ELSEWHERE` naming `refs/heads/run` for the linked one, and no
  `resumed ·`; with the gate log removed, one `resumed · attempt 1`, for the run worktree, beside the
  same ELSEWHERE skip.
- AC4 — `tRun.procs` — in the linked worktree on `wave`, session `T`'s `--resume tRun --keepalive-id C`
  refused at check 58 naming `refs/heads/unit` and the run worktree's path, and the no-id call printed
  the status block and then the same refusal; both worktrees' `git status --porcelain` printed
  nothing and the planted one-line ledger was byte-unchanged. Aged past the bound the linked call
  still refused, and the run worktree printed `presumed-stopped` and took the run over. HELD arm: a
  HELD record committed before the sibling was added read `verdict: ELSEWHERE` there and its
  take-over refused at 58, writing nothing in either worktree, while the run worktree took it over.
- AC5 — `a detached HEAD` — detached, the linked worktree's refusal ended
  `This worktree: a detached HEAD`; with the run worktree on `parked` it said no worktree on this
  node has `refs/heads/unit` checked out; with `unit` deleted it said no branch of that name exists
  and named creating it at a commit carrying the record; re-created and checked out, the run
  worktree's call met unit 61's live-session row at 58 with no holder message.
- AC6 — `this worktree is not on the run's branch` — under `in-place`, `--status` printed
  `phase LANDED (derived:`; on a new `rerun` branch `--resume tRun --keepalive-id k9` printed unit
  61's out-of-scope row unobserved, `nothing to resume` observed, and the observed-landing row with
  the remote gone; under `primary` on `main` it re-bound; none printed that text or a check 58, and
  the unobserved, observed and `primary` calls' folded output and `git status --porcelain` matched
  a copy whose `check_holder_worktree` always returns 0, each run from the same fixture state.
- AC7 — `"reason":"elsewhere"` — `node tools/unattended/stop-guard.js` fed a payload bound to the
  record's session with its `cwd` at the linked worktree, over the real driver, exited 0, printed
  nothing and wrote `"reason":"elsewhere"`; the same payload with `cwd` at the run worktree, reading
  BUILDING and LIVE, was blocked `run-open`.
- AC8 — `skip · NO RUN BRANCH` — with `run-branch` removed from both copies and no gate log,
  `--liveness` printed `holder-ref: absent` and `verdict: STALE` in both worktrees and the tick's
  `--dry-run` printed two `skip · NO RUN BRANCH` decisions and no `resumed ·`; on the driver
  fixture with both branch facts removed, `--resume tRun --keepalive-id k1` printed the no-run-branch
  announcement and then the holder row's orientation.
- AC9 — `unattended skill wiring` — at 364278a8 the leg exits 0 printing `in sync`, which it reaches
  only past its drift refusals on the installed stop contract, with the Skill rendered from its
  template. The `unattended kit gate` leg exits 0 with no check 10 finding, and its report channel,
  re-run over that tree, reads `check 10 byte-compared 3 of its 3 pairs: protocol verbs asks`. The
  greps are the in-pass reads above.
- AC10 — `git cat-file -s` — against the first parent's figures: protocol template and render 64456
  -> 64424 bytes and 703 -> 703 lines, stop contract and render 35321 -> 35303 and 518 -> 517, verb
  carrier and render 19142 -> 19136 and 209 -> 208; none grew.
- AC12 — `lexicon naming predicates` — at 364278a8 the leg exits 0 ending `lexicon OK`, and there
  `lexicon.py --suggest <name> --as sh.function` answers `OK` for `resolve_holder_worktree`,
  `check_holder_worktree` and `add_sibling_worktree`. The
  `harness arms (fail branches armed or pinned)` leg exits 0 with no finding, and
  `check-arms.py --report` there lists check 58 branch 1, the text
  `this worktree is not on the run's branch`, as ARMED. The `kit version markers` and
  `install-prefix (shipped surface)` legs each exit 0 clean. The version pin, the pin file and the
  added-line reads are the in-pass reads above.
