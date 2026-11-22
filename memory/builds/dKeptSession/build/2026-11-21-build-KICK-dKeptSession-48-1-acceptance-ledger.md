# KICK-dKeptSession-48 — acceptance ledger

**Serves:** journal KICK-dKeptSession-48

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on win32
at the pass's base `7212620cd` by one probe under the session scratchpad, which plants unit 30's
`context-window` and `context-window-sibling` scenarios from `tools/runlog/fixtures/transcripts.json`
itself, without importing the self-test or running any arm, into one scratch projects root, and reads
the `context-window` transcript with `runlog.py context`, the config and home roots aimed at an empty
scratch, once with `CLAUDE_CODE_MAX_CONTEXT_TOKENS` removed and once set to 200000. The same probe
read a copy of the kit whose `extract.py` consults the variable only when no observation is found,
ranking the observation above it. `python tools/lexicon/lexicon.py` exited non-zero on its
verb-offender pin, 1432 offenders (DERIVED, that run), the count unit 47's ledger read before this
pass; this unit adds no function, and `writing_practice.py check pinned-facts` read green.

Owed to the close: every leg the spec's section 7 names; the runlog self-test, whose one new check in
`test_extract_context_window` and floor are below; and the `New arm:` line's RED-first observation,
that check staged against a copy of `extract.py` ranking the observation above the variable.

## Decisions taken in the build

- S3's check reads through a fresh `build_arm_env(base)` copy, so the AC4 read's 500000 does not
  carry into it, and the following `x` read keeps its own copy as before.
- The `RAISED` comment prices the one check and no decoy check, since no `test_` function is added.

## Unit 30's superseded wording (S4)

Unit 30 is CLOSED, so its spec and ledger stay as they are and the answer is here (F2).

- Unit 30's risks line reads: "a model never observed past 200k on a node reads the 200k rung, so
  its first session there errs towards going fresh, the cheaper error by RT-1's measurement, until
  one session passes 200k or the variable is set." It prices one direction only. Read it beside S1
  of this unit: no transcript record names the window, so every session of a model observed past
  200000 under the root reads the 1M rung, a 200k session of that model included, and that session
  errs towards a late boundary act unless it sets `CLAUDE_CODE_MAX_CONTEXT_TOKENS=200000`.
- Unit 30's AC2 reads: "When `runlog.py context` reads the `context-window` transcript, a
  150000-token turn, from a root that also holds `context-window-sibling`, it prints `15%`." That
  `15%` is a 1M session's share; a 200k session reading the same turn is at 75% of its own window,
  which it reads only under the variable at 200000, as AC1 of this unit observes. S1 and this item
  supersede both passages.

**Evidences:** KICK-dKeptSession-48
- AC1 — from a root holding `context-window` and `context-window-sibling`, `runlog.py context` with `CLAUDE_CODE_MAX_CONTEXT_TOKENS=200000` exited 0 printing `75%`, with `context: window 200000 · env` on stderr (DERIVED, that probe); without the variable it printed `15%` with `context: window 1000000 · observed 900000 on fixture-model` (DERIVED, that probe). The copy ranking the observation above the variable printed `15%` under 200000, the red the criterion names (DERIVED, that probe).
- AC2 — the whitespace-joined `derive_context_window.__doc__` counts `CLAUDE_CODE_MAX_CONTEXT_TOKENS=200000` 1 and `a 200k session of that model included` 1 (DERIVED, a `python -c` in `tools/runlog/` at the commit).
- AC3 — `grep -n` for the variable at 200000 over `help/orientation-card.md` prints one line, below the heading "When a session resumes", the page's last section, and the joined page counts `a 200k session reads its fill against the 1M window` 1 (DERIVED, `grep` and `tr` at the commit).
- AC4 — both passages are quoted above, and the joined ledger counts each 1; `git diff --name-only` from the pass's base over unit 30's spec and its acceptance ledger prints nothing, since this commit writes neither (DERIVED, that probe at the commit).
- AC5 — over the joined `tools/runlog/README.md`, `a 200k session of that model included` counts 1 and unit 47's `whose newest earlier main usage in the same transcript is on that model` counts 1, and `grep -c` for the variable at 200000 prints 1 (DERIVED, `tr` and `grep` at the commit).
- `ASSERTION_FLOOR` rises from 1629 to 1630: the one check S3 adds and no decoy check (PINNED, the count its `RAISED` comment prices).
