# Brief — dRedressedBar: every traced red of the full bar with self-tests at ebce889c7, fixed

**Serves:** research TOOL-dRedressedBar-1 TOOL-dRedressedBar-2 TOOL-dRedressedBar-3 TOOL-dRedressedBar-4 TOOL-dRedressedBar-5 TOOL-dRedressedBar-6 TOOL-dRedressedBar-7

## The prompt

> Run the full bar in gov including all self-tests. Profile the entire run. Make a full list of reds and their causes.

> let the canary run, confirm 12-15 then fix all the traced reds

## The brief

### Goal
`GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` over local main `ebce889c7` refused
on a stale generated output, and with `GATE_REGEN_CHECK=0` reported 16 of 140 legs red, the run-gates
canary still retrying. Each traced red is fixed at its root cause, one mechanism per unit, so the same
bar with no knob reads green apart from the canary. Every leg log is under
`.git/worktrees/gov-bar-profile-failures-b80cc3/gate-logs/`; the standalone re-runs of push-main,
govkit, unattended-build and the turnstile reproduced their reds without the knob.

### Items
1. **TOOL-dRedressedBar-1 — stale suite fixtures, re-armed.** Test-only edits, each restoring an arm a
   landing disarmed:
   - `tools/workflows/unattended-build.test.sh` GH33 (26 failures, line 2462 `$2: unbound variable`):
     TOOL-aOrientedCast-27 made `build_gh33_writer` take `<unit id> <authored-json>`, and every call
     site still glues the two into one word (`build_gh33_writer A-tB-1'["A-tB-1"]'`, no space).
   - `tools/workflows/tier2-review.test.sh:70-78` extracts the prelude between the meta block's `}` and
     `const reviewDir = a.reviewDir` and dies without `badSubject` and `baseLooksPinned`, so 0 of the
     322-assertion floor runs. TOOL-aOrientedCast-27 moved the code: `badSubject` now sits below
     `reviewDir` (tier2-review.js:357), and `baseLooksPinned` resolves nowhere. Re-anchor the
     extraction on the code as it stands and keep the liveness die.
   - `tools/run-gates/run-gates.turnstile.test.sh:1499` arm 44 routes `cat "$d/pid"` through a
     nonce-swapping reader, but `ts_try_reap` and `scan_dead_docs_beacons` now read
     `{ IFS= read -r hpid < "$d/pid"; }`, so the routed count is 0 and both arms red ("a slot whose
     nonce changed after its pid was read was reaped", "a docs beacon … was swept"). Route the new
     spelling; keep the routed-count assertion.
   - `.githooks/pre-push.test.sh`: eleven arms (RP AC12, AC13, AC14 and its control, S10;
     TOOL-aSparedSpawn-32 AC8 and its control; TOOL-aSparedSpawn-33 AC1, AC2 twice, AC4) read
     `pre-push: the merge-loss check did NOT run … the lexicon kit is installed neither under …`
     where they expect the decision line. That skip line is `.githooks/pre-push:952`
     (TOOL-aMendedFleet-3). Root-cause why these fixtures now reach it, then give them the lexicon
     kit or read past the skip line, whichever the arm's subject needs.
   - `foreign-prefix parity` reds `roles adopter self-test` (`tools/roles/adopt-roles.test.sh`):
     "an undeclared whole run: it printed no probe marker". Take the probe stop its sibling suites
     carry, or a `WHOLE_RUN` row with a reason in `tools/run-gates/foreign-prefix.gov.test.sh`.
2. **TOOL-dRedressedBar-2 — the verb offender over the pin.** `lexicon naming predicates` and
   `lexicon wiring` read 1088 against `VERB_OFFENDER_PIN="1087"`. Diffing `--offenders` against
   `301a36664`, which set 1087, the one arrival is `tools/unattended/gate-guard.js:689`
   `const clean = (v) => …` (strips control bytes and caps a quoted question at `ASK_QUOTE_MAX`).
   Rename it to a declared verb (`lexicon.py --suggest` calls `clean` a scoping question), all three
   uses, so the pin holds at 1087.
3. **TOOL-dRedressedBar-3 — the govkit selftest's reds.** 56 failures in the bar, reproduced
   standalone. Diagnose to root causes before fixing; symptoms seen: `and re-stamps the receipt at the
   new commit` (selftest.py:3307); `aQuenchedHarness-3: govkit: 'agent-cap' requires
   'kickoff-manifest'` outside the selection; `OC13 AC4 … roles: entry 3 (spec-write) harness
   {prefix}/workflows/unattended-build.js is not held by this tree`; `OC8 AC4 … ION-STYLE.md: not
   rendered — 'memory-tree' stopped at an accepted outcome`; `[-12] AC4/AC9` and `[-8] AC1/AC4`
   diverged; about forty `[-PV]` arms cascading from `STOP: block 1 has not finished clean`.
4. **TOOL-dRedressedBar-4 — shipped-surface homonyms.** `install-prefix (shipped surface)` reds two
   lines whose `workflows` is Claude Code's own session directory, not the kit, which the gate's rule 4
   reads as a kit path: `tools/hooks/format-guard.js:333`
   `path.join(sessionDir, 'subagents', 'workflows', runId, 'journal.jsonl')` and
   `tools/roles/adopt-roles.test.sh:228` `sub / "workflows" / "wf_00000001-aaa"`. The gate is a pure
   ban with no waiver; hold the harness directory's name in one named constant, the form the gate
   header states it does not read.
5. **TOOL-dRedressedBar-5 — fork idioms past the registry.** `shell hygiene (a fork spent on builtin
   work)`: `tools/branch-reconcile/adopt-branch-reconcile.sh` 3 `path-subst`, 3 `var-pipe`;
   `tools/roles/adopt-roles.sh` 3 `path-subst`, 1 `var-pipe`; `tools/roles/adopt-roles.test.sh` 1
   `date-fmt`, 2 `path-subst`, 12 `var-pipe`; `tools/hooks/format-guard.test.sh` 1 `path-subst`;
   `tools/workflows/unattended-build.test.sh` grew `printf-subst` 66→71 and `var-pipe` 62→70 past its
   registry rows. Convert each to the no-fork form the leg names; register nothing new.
6. **TOOL-dRedressedBar-6 — adopt-roles exits armed.** `harness arms (fail branches armed or pinned)`:
   `tools/roles/adopt-roles.sh:209` (`/adopt-roles.sh --scaffold`) and `:217` (`roles: the agent render
   refused, so nothing more was written — fix what it named and re-run`) have no positive assertion of
   their failure text. Add an arm for each in `tools/roles/adopt-roles.test.sh`, observed red on a
   staged break.
7. **TOOL-dRedressedBar-7 — records, measured last.** Re-render `memory/gotchas/INDEX.md` with
   `gotchas.py --write`: merge `ebce889c7` resolved it `merge=ours` to local main's copy and dropped
   origin's `a-gate-that-walks-the-repo-root-reads-other-worktrees` and
   `a-merge-of-the-default-branch-read-as-additions` rows (memory hygiene check 17, the regen
   preflight, push-main arms 28 and 29, whose fixture clones HEAD's stale index). Declare
   `.claude/agents/gov-reuse-scout.md` in `memory/project/method-carriers.txt` (`method carriers`
   check 3). Bump each kit whose shipped bytes the build moved, as `govkit.py epoch --base ebce889c7`
   names them.

### Acceptance
Each unit's own red leg reads green when its argv runs alone at the unit's tip; a re-armed arm is
observed red on its staged break before it is called armed. At the close, the full bar with
`GATE_FULL=1 GATE_SELFTESTS=1` and no `GATE_REGEN_CHECK` override reads every one of the 16 legs
`GATE ok`, the run-gates canary judged on its own.

### Gates
`unattended-build self-test` · `tier2-review self-test` · `run-gates turnstile` · `pre-push self-test` · `foreign-prefix parity (every self-test at three prefixes)` · `lexicon naming predicates` · `lexicon wiring` · `govkit selftest` · `install-prefix (shipped surface)` · `shell hygiene (a fork spent on builtin work)` · `harness arms (fail branches armed or pinned)` · `memory hygiene` · `method carriers (every pointer declared)` · `kickoff-manifest ratchet` · `push-main self-test`

### Non-goals
- The run-gates canary until its retry reports, and `GATE_REGEN_CHECK` reaching nested runners.
- No pin, ceiling or registry row raised to absorb a red that a code change can fix.
- No edit to `tools/run-gates/run-gates.sh`.
- No merge to local main and no push without the owner's ask.

### Limitations
- Children run no bar and no whole suite; each verifies with the one check that exercises its change
  and returns a suite verdict it needs to the main loop.
- No `tools/unattended/` self-test suite runs (standing owner instruction, 2026-08-23).
- Under MSYS, `/tmp` and `C:/…/Temp` name one directory; compare through git.

### Reuse
The precedent build `memory/builds/aSweptBar/` (same shape, same day); the remedies each leg prints;
the probe stop `tools/hooks/scratch-guard.test.sh:179-180` and `WHOLE_RUN`'s reasons; the turnstile
arm's own routed-count seam; `lexicon.py --suggest`; the comment ledger above each pin.
Recall terms used: merge=ours re-render gotchas INDEX regen held self-tests GATE_SELFTESTS post-merge
full bar aOrientedCast landing.

## Drawn from the session

> let the canary run, confirm 12-15 then fix all the traced reds
— owner, after the red list

## Owner confirmation

Asked: Ready — say go and I'll start, or adjust any field.
Answer: go
