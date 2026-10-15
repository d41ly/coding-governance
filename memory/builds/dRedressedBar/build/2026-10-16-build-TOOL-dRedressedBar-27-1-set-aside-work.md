# Unit 27's set-aside work — dRedressedBar, the ledgers and the foreign ledger patch as built before its divergence

**Serves:** research TOOL-dRedressedBar-27

The builder built this, could not commit it, and returned DIVERGENCE. It is kept here verbatim for the redispatch, which restores it rather than rewriting it. Each embedded file's lines carry a `| ` prefix so no checker reads them as this record's own; strip the first two characters of each line to restore a file. The builder's return:

~~~~text
DIVERGENCE: spec 27 §4 "The six revision entries" gives the build pass five spec writes, as do S4, §3's second non-goal, §4 Files touched, AC4 and AC5. Each is one appended revision entry plus the status header's rev and date, in TOOL-aSparedSpawn-11 (rev-4), TOOL-aSparedSpawn-13 (rev-6), TOOL-aSparedSpawn-32 (rev-5), TOOL-aOrientedCast-22 (rev-2) and TOOL-dRedressedBar-18 (rev-9). The scratch-guard hook refused all five edits. .claude/roles.json lets only gov-spec-writer write a spec, and a gov-builder may move only the status and date cells of its own routed spec. The repo's precedent agrees: a records-fix revision to another spec is written by the unit's spec-writer pass (spec 18 rev-5 to rev-8, spec 9 rev-5 to rev-7).

What §4 would have to say: TOOL-dRedressedBar-27's spec-writer pass writes the five entries and header moves, and re-renders the three build READMEs' generated rows with gen_build_index.py --write, before the build pass. The build pass then writes only the eight ledgers, the re-collected returns record, the 37 foreign lines and this unit's own ledger. AC4's spec half and AC5's entry lookup would then grade the spec-writer commit.

Without those entries, the five U lines would cite revisions that do not exist, so I committed nothing. Every path this pass changed is restored, and the work is saved for the redispatch.

Nothing is committed. The tree is back at 3f052d89e, except spec 27's INPROGRESS header, which was already set when the session started and which I left alone. Until the spec is revised, --plan will keep naming this unit.

**Saved for the redispatch**, in C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-bar-profile-failures-b80cc3/8d2976c7-7629-4ba0-8a96-2098db6da20f/scratchpad/u27-wip/:
- HANDOFF.txt: the exact text of the five revision entries and header moves, and the findings below.
- ledgers/: the eight unit ledgers and the re-collected agent-returns record. The ledgers are units 2, 4, 5, 7, 9, 11 and 20 at -1-, from the interrupted pass, reviewed against each builder's return and commit body; unit 18's at -2- is new.
- foreign-ledgers.patch: the 37 foreign bullets rewritten. `git apply --check` passes against HEAD.
- The probe, its key files and added-tokens.tsv are in scratchpad/u27/.

**Unit 18's ledger** has 13 lines observed, three amended (AC1, AC2 and AC5 at rev-7, each carrying the rev-4 reading), and one unobserved (AC15, citing rev-9).

**Checks that ran.** These are probes, not gates. All ran with the saved work staged.
- The §4 probe re-derives hygiene check 23 and stands in for the `memory hygiene` leg's check 23.
  - Liveness: at the parent it printed exactly the spec's 102 keys (64 missing ledger answers, 8 lines in neither legal form, 30 unjoined answers).
  - Over the staged index it found none of those failures in any of the 793 units.
  - The 64 arm-1 keys and the 37 foreign keys all read observed or amended.
- The word check (AC4's word half): 0 lost words over 37 bullets, after fixing one comma I had attached to an existing word.
- AC5's token half: every token added to a foreign observed line was found by `git grep -F` at a named commit and path (0 missing).
- AC7 by diff: unit 18's rev-4 return is present, no line under `## Returns` was removed, and no `**Evidences:**` line was added.
- The bug-class checklist (gotchas.py --for-diff) did not run, because there is no commit.
- Owed at the close once the unit is rebuilt: the `memory hygiene`, `recall floor` and `recall floor arms` legs. No new arm is declared, so no RED-first observation is owed.

**Spec facts found wrong while confirming.** Each saved line follows the evidence:
1. aSparedSpawn-8/AC11: the table spells the template token `skipped — <id> — <why>`, but spec 8 (:351) spells `skipped — <id> · <why>`. The table's spelling would leave the line unjoined.
2. aSparedSpawn-4/AC12: `"$(cat <<'RKD'` is not in the instrument, which builds the idiom at run time. The literal is the wrapper the revert restores, at 989e9234b:tools/hooks/agent-cap.test.sh:72.
3. aSparedSpawn-3/AC7: the "before" runner is 286b839a, not 22efab65. It carries `NR==FNR` at :4036.
4. aSparedSpawn-16/AC12: the instrument's base is f53211e6c, not f479ba42. Its runner spells the file `age.${heldkeys[$i]}` at :3097 and :3115.
5. AC5's `git grep -F` finds the tokens spelled as in the criterion (`age.*`, `NR == FNR`, the two templates, `git diff 6e8f8b1da main -- F`) only in the owning spec.
6. Files touched omits the generated records rows the eight new ledgers add to specs 2, 4, 5, 7, 9, 11, 18 and 20.
7. AC4 pins the entry and header date at 2026-10-15; the pass now runs on 2026-10-16.
~~~~

## Files

### HANDOFF.txt

~~~~text
| TOOL-dRedressedBar-27 — work set aside at the DIVERGENCE of 2026-10-16, for the spec writer and the redispatch.
| Parent: 3f052d89e. Nothing was committed; the tree was restored, apart from the dispatcher's INPROGRESS header on spec 27.
| 
| WHY IT STOPPED
| scratch-guard refused every spec write the build pass was assigned: the five revision entries and header
| rev/date moves of spec 27 §4 "The six revision entries" (also S4, §3's second non-goal, Files touched, AC4, AC5).
| .claude/roles.json lets gov-spec-writer write the spec class; a builder may move only the status and date cells
| of its own routed spec. The repo's precedent (spec 18 rev-5..rev-8, spec 9 rev-5..rev-7) is that another
| spec's records-fix revision is written by the unit's SPEC-WRITER pass, so the entries belong there.
| 
| SAVED HERE
| ledgers/   the eight unit ledgers (2, 4, 5, 7, 9, 11, 20 at -1-, 18 at -2-) and the re-collected
|            agent-returns record (unit 18's rev-4 return at :5556; only the header sentence above
|            `## Returns` changed, every new return appended after the last old one, 0 `**Evidences:**` lines).
| foreign-ledgers.patch   the 37 foreign bullets rewritten, `git diff --cached` against 3f052d89e, 15 files.
| ../u27/probe23.py       the §4 probe (grade/red/words/show/bullet; `@file` key lists).
| ../u27/added-tokens.tsv every token added to a foreign O line, with the commit and path `git grep -F` finds it at.
| ../u27/{arm1,arm2,arm3,foreign}.keys   the 102 keys of Today's red, from `red` at the parent.
| 
| Verified with that tree staged (probe, not check 23): `red INDEX` printed GAP 0 BAD 0 TOKBAD 0 ORPH 0 over
| 793 units; the 64 arm-1 keys and the 37 foreign keys all `ok obs` / `ok amd`; `words HEAD INDEX` 0 LOST;
| `ev.py check added-tokens.tsv` 0 MISSING. The five U lines cite entries that do not exist yet.
| 
| THE FIVE ENTRIES THE U LINES CITE (the spec writer's to write; header rev and date move with each)
| aSparedSpawn-11  header rev-3 · 2026-10-11 -> rev-4 · 2026-10-15
| - rev-4 · 2026-10-15 · AC6 · AC10 · records, TOOL-dRedressedBar-27: AC6's suite run and AC10's
|   timings were owed at VERIFYING, and no record observes either. The criteria do not move, and the
|   status stays CLOSED.
| aSparedSpawn-13  header rev-5 · 2026-10-12 -> rev-6 · 2026-10-15
| - rev-6 · 2026-10-15 · AC11 · records, TOOL-dRedressedBar-27: the two whole bars were never run, and
|   no record observes them. The criterion does not move, and the status stays CLOSED.
| aSparedSpawn-32  header rev-4 · 2026-10-12 -> rev-5 · 2026-10-15
| - rev-5 · 2026-10-15 · AC1 · records, TOOL-dRedressedBar-27: the range was read at origin's moved tip
|   `6e8f8b1da`, where rev-4's §4 (f) moved the merge, and never at `37200355d`. The criterion does
|   not move, and the status stays CLOSED.
| aOrientedCast-22  header rev-1 · 2026-10-13 -> rev-2 · 2026-10-15
| - rev-2 · 2026-10-15 · AC7 · records, TOOL-dRedressedBar-27: the live refusal was owed to the main
|   loop's session at the close, and no record observes it. The criterion does not move, and the
|   status stays CLOSED.
| dRedressedBar-18  header rev-8 · 2026-10-15 -> rev-9 · 2026-10-15
| - rev-9 · 2026-10-15 · AC15 · records, TOOL-dRedressedBar-27: the turnstile arm runs the real
|   runner's hold verb inside `--selftest`, which no pass ran, and no record observes it. The
|   criterion does not move, and the status stays CLOSED.
| Then `gen_build_index.py --write` re-renders the three build READMEs' rows.
| 
| SPEC FACTS FOUND WRONG WHILE CONFIRMING (each built to the evidence in the saved work)
| - aSparedSpawn-8/AC11: the table's token `skipped — <id> — <why>` is not the criterion's; spec 8 spells
|   `skipped — <id> · <why>` (d5e7fc276, spec :351). The em-dash spelling would leave the line TOKBAD.
| - aSparedSpawn-4/AC12: `"$(cat <<'RKD'` is NOT in the instrument (it composes the idiom at run time,
|   :279-281); the literal is the wrapper the revert restores, 989e9234b:tools/hooks/agent-cap.test.sh:72.
| - aSparedSpawn-3/AC7: the "before" runner is 286b839a (the unit's ledger :9), not 22efab65; NR==FNR at :4036.
| - aSparedSpawn-16/AC12: the instrument's base is f53211e6c (the unit's ledger :8), not f479ba42; the
|   per-name age file is age.${heldkeys[$i]} at :3097/:3115 there. The literal `age.*` is only the criterion's.
| - AC5's "git grep -F at the commit and path its entry names" finds the criterion-spelling tokens
|   (`age.*`, `NR == FNR`, the two templates, `git diff 6e8f8b1da main -- F`) only in the owning SPEC.
| - Files touched omits the generated records rows the eight new ledgers add to specs 2, 4, 5, 7, 9, 11,
|   18 and 20, which gen_build_index.py --write renders.
| - The entry and header date is fixed at 2026-10-15 by AC4; the pass now runs on 2026-10-16.
~~~~

### foreign-ledgers.patch

~~~~text
| diff --git a/memory/builds/aOrientedCast/build/2026-10-13-build-TOOL-aOrientedCast-22-1-acceptance-ledger.md b/memory/builds/aOrientedCast/build/2026-10-13-build-TOOL-aOrientedCast-22-1-acceptance-ledger.md
| index a5b5863c1..85e100521 100644
| --- a/memory/builds/aOrientedCast/build/2026-10-13-build-TOOL-aOrientedCast-22-1-acceptance-ledger.md
| +++ b/memory/builds/aOrientedCast/build/2026-10-13-build-TOOL-aOrientedCast-22-1-acceptance-ledger.md
| @@ -32,4 +32,5 @@ the build's rules forbid: its pre-commit checks never ran, and the close's bar i
|  - AC4 — `LANDED ABORTED` — the `node -p` read printed `LANDED ABORTED` and the grep printed `PHASES_TERMINAL="LANDED ABORTED"`.
|  - AC5 — `Bash|PowerShell|AskUserQuestion` — the grep printed 1 for `gate-guard.fragment.json` and 0 for `.claude/settings.json`, and `settings-merge.py --check` exited 1 naming the missing `Bash|PowerShell|AskUserQuestion` hook: the settings half is the main loop's second-pass merge, which this pass may not write.
|  - AC6 — `KIT_UNATTENDED_VERSION=1.105` — the count printed 1, and `git grep -l "gov:kit unattended@1.104"` printed no path under `tools/`; it printed the five rendered guides, the rendered Skill (the second pass's), and this unit's own spec, whose §4 and §6 quote the string.
| -- AC7 — `PreToolUse` — owed to the main loop's live session at the close, after the merge and a restart; not observable by a fixture.
| +- AC7 — amended rev-2, the spec's entry recording that this criterion was never observed — NOT OBSERVED —
| +  `PreToolUse` — owed to the main loop's live session at the close, after the merge and a restart; not observable by a fixture. Never seen live: the refusal of an `AskUserQuestion` call.
| diff --git a/memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-1-acceptance-ledger.md b/memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-1-acceptance-ledger.md
| index c0ef1e67b..19e8a9696 100644
| --- a/memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-1-acceptance-ledger.md
| +++ b/memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-1-acceptance-ledger.md
| @@ -20,8 +20,9 @@ and every other leg section 7 names are owed at VERIFYING.
|  - AC4 — `run-gates.evidence.test.sh` AC4 arm, sliced — green: no reuse across a `PYTHONUTF8`
|    change and two reuses on the repeat; with the env lines and the utf8 field out of the digest it
|    redded. The `GATE_REUSE` half is the suite's first reuse arm, which passed in the same slice.
| -- AC5 — `run-gates.evidence.test.sh` AC5 arm, sliced — green 3 of 3; with the schema line out of
| -  the digest it redded. The first draft placed its control before the miss and stayed green on
| -  that break, because a run that reuses every leg empties the ledger; reordered, rev-3 records it.
| +- AC5 — `run-gates.evidence.test.sh` AC5 arm, sliced — green 3 of 3; with the schema line
| +  (`REUSE_SCHEMA`) out of the digest it redded. The first draft placed its control before the miss
| +  and stayed green on that break, because a run that reuses every leg empties the ledger;
| +  reordered, rev-3 records it.
|  - AC6 — `run-gates.evidence.test.sh` AC6 arm, sliced — green: a `touch` with identical bytes on a
|    dirty guarded file reused both legs. Its red case, a key reading mtime, has no staged break here.
| diff --git a/memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-10-acceptance-ledger.md b/memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-10-acceptance-ledger.md
| index 329d117f9..af841adfe 100644
| --- a/memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-10-acceptance-ledger.md
| +++ b/memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-10-acceptance-ledger.md
| @@ -47,10 +47,10 @@ unattended driver's suite and the fixture.
|    and the scan measures 2"; after it exited 0, "58 declared site(s) in 43 row(s), no undeclared loop
|    fed by a command substitution", with the registry untouched. The changed arm itself runs in the
|    driver suite's shard 1 at VERIFYING.
| -- AC9 — `bash tools/gate-lint/fork-count.sh memory/project/fork-ceilings.txt . --only
| -  run-gates-2leg` — calibrated on its 5-fork specimen, then "ok run-gates-2leg · measured 95 ·
| -  ceiling 99 · base 97"; the row's reason names the stated margin, the readings it sits over and the
| -  stale direction's bound at 95.
| +- AC9 — `bash tools/gate-lint/fork-count.sh memory/project/fork-ceilings.txt . --only run-gates-2leg`
| +  — calibrated on its 5-fork specimen, then "ok run-gates-2leg · measured 95 · ceiling 99 · base
| +  97"; the row's reason names the stated margin, the readings it sits over and the stale
| +  direction's bound at 95.
|  
|  Checked as well, none of them a bar leg run: `sh_hygiene.py --spawn-idioms` with the leg's pathspecs
|  exited 0 with every registered count unchanged; `sh_hygiene.py --location-probes` exited 0;
| diff --git a/memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-11-acceptance-ledger.md b/memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-11-acceptance-ledger.md
| index 1ded6cad0..49fcf3385 100644
| --- a/memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-11-acceptance-ledger.md
| +++ b/memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-11-acceptance-ledger.md
| @@ -19,12 +19,13 @@ owed at VERIFYING and says so.
|    then put through the runner's parity mode against real `node`, both hooks each: 148 verdicts, 0
|    disagreements, 144 s. The suite's own summary line beside base `22efab65` on one tree is OWED at
|    VERIFYING; the Python loop at base is about 3700 spawns.
| -- AC2 — `direct-checks.sh runner` with the exit stub staged to drop its code in a copy of the runner —
| -  the parity mode exited 1 with 5 disagreements, the first "DISAGREE BASE hook on ...fix/raw.js:
| -  in-process exit 0, node exit 2"; unstaged, 28 verdicts over 14 payloads, 5 real denies, 0
| -  disagreements. The same break in a scratch copy of the suite is OWED at VERIFYING.
| -- AC3 — `direct-checks.sh runner` with the marker strip staged to a no-op — the property exited 1:
| -  "73 denied at BASE, 2 denial(s) lost, 0 ratified". The suite-copy form is OWED at VERIFYING.
| +- AC2 — `direct-checks.sh runner` with the exit stub (`process.exit`) staged to drop its code in a
| +  copy of the runner — the parity mode exited 1 with 5 disagreements, the first "DISAGREE BASE hook
| +  on ...fix/raw.js: in-process exit 0, node exit 2"; unstaged, 28 verdicts over 14 payloads, 5 real
| +  denies, 0 disagreements. The same break in a scratch copy of the suite is OWED at VERIFYING.
| +- AC3 — `direct-checks.sh runner` with the marker strip (`gov:sequential-agents`) staged to a no-op
| +  — the property exited 1: "73 denied at BASE, 2 denial(s) lost, 0 ratified". The suite-copy form
| +  is OWED at VERIFYING.
|  - AC4 — `direct-checks.sh onesignal` — over a hand-built repository the derived map named 27 signals
|    for 27 entries of `SIGNALS`, and all 27 in-process records equalled `report()` over their own
|    fields. One `report()` took 14.2 s and the 27 reads 124.9 s, 4.6 s a read. The suite arm
| @@ -35,11 +36,13 @@ owed at VERIFYING and says so.
|    lexicon arm, `_ASK_SIGNALS` at the ask-signal arm); no name map exists, the map is
|    `SIGNAL_ORDER`, filled from `report()`'s order. `CHECK_FLOOR` rose 478 to 482, COUNTED off the
|    arm; the executed count is OWED at VERIFYING.
| -- AC6 — `check-hook-destinations.test.sh` — OWED at VERIFYING, with the staged reset removal. Read in
| -  the diff: one `scratch` builds the tree once and resets it per arm to the recorded fixture commit,
| -  all nine `d=$(scratch)` calls are bare `scratch`, and no arm deletes the shared tree.
| +- AC6 — amended rev-4, the spec's entry recording that this criterion was never observed —
| +  NOT OBSERVED — `check-hook-destinations.test.sh` — OWED at VERIFYING, with the staged reset
| +  removal. Read in the diff: one `scratch` builds the tree once and resets it per arm to the
| +  recorded fixture commit, all nine `d=$(scratch)` calls are bare `scratch`, and no arm deletes the
| +  shared tree. Never run: the hook-destinations suite, in which `git archive` runs once.
|  - AC7 — `direct-checks.sh ac7` — "u=WANT,WANT m=WANT,WANT other= capped=WANT walks undeclared=2
| -  declared=3": two declared calls over one range walked once, the other range and the capped
| +  declared=3": two declared `build_commit` calls over one range walked once, the other range and the capped
|    newest-first window walked their own, and every answer equalled the undeclared one. With the key
|    staged to omit the range in a copy of the library the third call answered from the memo
|    (`other=WANT`, `declared=2`) and the step redded. The suite arm in `check-unattended.test.sh`,
| @@ -50,8 +53,10 @@ owed at VERIFYING and says so.
|    on PATH — with `AI_AGENT` unset the log stayed absent; with `AI_AGENT=claude-code_2-1-286_agent`
|    one write logged one call and its cell read the stub's 2.1.178, which is the leak the prologue's
|    unset closes. The suite arm is OWED at VERIFYING, and arms only where the runner set `AI_AGENT`.
| -- AC10 — each touched suite and the two checkers timed at base and after on a frozen clone — OWED at
| -  VERIFYING; no figure exists yet. The AC4 arm adds two reports and 54 in-process reads per run.
| +- AC10 — amended rev-4, the spec's entry recording that this criterion was never observed —
| +  NOT OBSERVED — each touched suite and the two checkers timed at base and after on a frozen clone
| +  — OWED at VERIFYING; no figure exists yet. The AC4 arm adds two reports and 54 in-process reads
| +  per run. Never timed: `check-pass-order.sh` and `check-brief-recorded.sh`.
|  
|  Checked as well, none of them a bar leg over a suite: `sh_hygiene.py --spawn-idioms` with the changed
|  files as pathspecs found no count change for any of them, `sh_hygiene.py` over the substitution-fed
| diff --git a/memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-12-acceptance-ledger.md b/memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-12-acceptance-ledger.md
| index 86fc8ce0f..3cd77b929 100644
| --- a/memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-12-acceptance-ledger.md
| +++ b/memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-12-acceptance-ledger.md
| @@ -45,10 +45,11 @@ arms 23b and 23c of `.githooks/pre-push.test.sh` (AC7), and the two `[aSS-12 AC8
|    owed at VERIFYING.
|  - AC5 — `direct-checks.sh` — with a kx record present, a bar where kx moved and `KX_RED=1` printed
|    `GATE FAIL  kx suite` and left no kx record. With ky's record removed and a tracked file dirtied,
| -  ky executed green and no ky record was written. The suite arm is owed at VERIFYING.
| +  under which the runner's `TREE_CLEAN` reads `no`, ky executed green and no ky record was written.
| +  The suite arm is owed at VERIFYING.
|  - AC6 — `direct-checks.sh` — after a commit adding `ky/extra.sh`, which no kit ships, ky was held
|    while the stub govkit answered. With `GOVKIT_STUB_OFF=1` the bar printed `govkit is not reachable`
| -  exactly once, ky ran naming `ky/extra.sh moved since <sha8>`, and kx was held unchanged on its
| +  exactly once, ky ran by its `guard` naming `ky/extra.sh moved since <sha8>`, and kx was held unchanged on its
|    diff. In the default mode a held leg still printed `set GATE_SELFTESTS=1 to run` and no selection
|    line appeared. The suite arm is owed at VERIFYING.
|  - AC7 — `direct-checks.sh` — the `gate-full-green` of a `changed` run read `selftests changed`, a
| diff --git a/memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-13-acceptance-ledger.md b/memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-13-acceptance-ledger.md
| index 60c233c3a..d13a8100a 100644
| --- a/memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-13-acceptance-ledger.md
| +++ b/memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-13-acceptance-ledger.md
| @@ -38,13 +38,13 @@ section 9d of `tools/run-gates/run-gates.test.sh`; and the `RP` arms of `.githoo
|    executed and `pure` was reused; a second bar at that HEAD reused `hist`. The suite arm is owed at
|    VERIFYING.
|  - AC3 — `direct-checks.sh` — with `GATE_REUSE_DAY=1` against an earning bar on today's day, `clk`
| -  executed and `pure` was reused. The suite arm is owed at VERIFYING.
| +  (which reads `clock`) executed and `pure` was reused. The suite arm is owed at VERIFYING.
|  - AC4 — `direct-checks.sh` — a `GATE_REUSE` bar in a worktree added after the earning bar printed
|    `GATE reuse` for `pure` and `clk`. The suite arm is owed at VERIFYING.
|  - AC5 — `direct-checks.sh` — on a cleared cache a bar with `RED=1` left no entry under the red leg's
| -  key and wrote its green sibling's. A bar on a tree holding an untracked guarded file left the entry
| -  count at 7. A reused leg's entry bytes were unchanged after the reusing bar. The suite arm is owed
| -  at VERIFYING.
| +  key and wrote its green sibling's. A bar on a tree holding an untracked guarded file (under which
| +  the runner's `TREE_CLEAN` reads `no`) left the entry count at 7. A reused leg's entry bytes were
| +  unchanged after the reusing bar. The suite arm is owed at VERIFYING.
|  - AC6 — `direct-checks.sh` — at `GATE_REUSE_SAMPLE=1` with `FLIP=1` the bar exited 1, printed
|    `cache disagreement · flip · <key>` with the key the record holds and `nondeterministic · nd`,
|    erased flip's entry and wrote two quarantine files. After a clean bar earned flip's key again, a
| @@ -60,9 +60,10 @@ section 9d of `tools/run-gates/run-gates.test.sh`; and the `RP` arms of `.githoo
|  - AC10 — `direct-checks.sh` — the legacy `impure` leg executed on the bar that reused every other
|    leg. After a push of a new branch to the fixture remote, its key moved with the `remote` leg's while
|    `pure`'s did not. The suite arm is owed at VERIFYING.
| -- AC11 — not run — it needs two whole bars with the self-test tier on a frozen clone, hours on node
| -  `a`, which no pass may run. It is owed at VERIFYING as the reused count and seconds a second bar in
| -  a fresh worktree reports.
| +- AC11 — amended rev-6, the spec's entry recording that this criterion was never observed —
| +  NOT OBSERVED — not run — it needs two whole bars with the self-test tier on a frozen clone, hours
| +  on node `a`, which no pass may run. It is owed at VERIFYING as the reused count and seconds a
| +  second bar in a fresh worktree reports.
|  - AC12 — `direct-checks.sh` — under `GATE_REUSE_PUSH` naming HEAD, the probed tip and the
|    advertisement digest, `rem` and `hist` were reused and `pure` and `based` executed. A moved tip,
|    another advertisement digest, another pushed sha and a commit moving a guarded file each executed
| diff --git a/memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-14-acceptance-ledger.md b/memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-14-acceptance-ledger.md
| index 41fc06fb7..b65cd55c9 100644
| --- a/memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-14-acceptance-ledger.md
| +++ b/memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-14-acceptance-ledger.md
| @@ -37,11 +37,11 @@ on this tree and identically on the batch parent's extract.
|  - AC2 — `check-arms.py --selftest` — a planted row missing its `survivor` field and one missing its
|    `replay` field each red naming the field; staged breaks `survivor field` and `replay field` each
|    turn their arm red.
| -- AC3 — `check-arms.py --selftest` — a fixture gate whose census is one above its ceiling reds
| -  naming the gate and the retirement review; at the ceiling it passes; staged break
| -  `ceiling compare` turns the arm red.
| +- AC3 — `check-arms.py --selftest` — a fixture gate whose census is one above its ceiling (its
| +  `REFUSAL_CEILINGS` token) reds naming the gate and the retirement review; at the ceiling it
| +  passes; staged break `ceiling compare` turns the arm red.
|  - AC4 — `check-arms.py --selftest` — tokens lacking a date and lacking an id each red naming the
| -  token, an id the fixture decision log does not carry reds, an id carried only as a prefix of a
| +  token, an id the fixture decision log (`memory/DECISIONS.md`) does not carry reds, an id carried only as a prefix of a
|    longer one is not carried, and a valid ceiling prints
|    `ceiling <gate> 2/2 · 2026-10-12 · TOOL-tBudget-1`; staged breaks `ceiling date` and
|    `ceiling id carried` each turn an arm red.
| @@ -53,7 +53,7 @@ on this tree and identically on the batch parent's extract.
|    the registry reads 5 rows, and the only reds are the six inherited `run-gates.sh` sites;
|    `check-arms.py --report` lists 31 unbudgeted gates by name.
|  - AC7 — `check-arms.py --selftest` — a family pattern matching no site in the planted gate reds
| -  naming the family; staged break `family dead pattern` turns the arm red.
| +  under `--check` naming the family; staged break `family dead pattern` turns the arm red.
|  - AC8 — `direct-checks.sh` — the driver on a slug with no run-state file prints
|    `UNATTENDED check 10 FAILED — no run-state file, so there is no run to report on: memory/builds/aNoSuchRun/RUN.md`,
|    rc 1; `check-arms.py --report` counts one `no run-state file` site, inside `check_run_state`; the
| diff --git a/memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-2-acceptance-ledger.md b/memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-2-acceptance-ledger.md
| index d0ceb2f8d..207166138 100644
| --- a/memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-2-acceptance-ledger.md
| +++ b/memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-2-acceptance-ledger.md
| @@ -14,11 +14,11 @@ every other leg section 7 names are owed at VERIFYING; this pass ran no suite wh
|  
|  **Evidences:** TOOL-aSparedSpawn-2
|  - AC1 — `2026-10-11-build-TOOL-aSparedSpawn-2-width-ab.sh` — OWED at VERIFYING. The instrument is written and passes `bash -n`, but its six bars were not run, because a pass runs no bar. THETA (90) and every row's `spawnpause` (0, dark) stay provisional until its rows exist.
| -- AC2 — `check_sp_value` arm 12a — the seam's rates flat after K=4 picked 4 and rates still rising picked 8, under a `false` spawn command that reds any timed loop. With the selection changed to take the maximum, the flat case picked 6 and the arm redded.
| +- AC2 — `check_sp_value` arm 12a — the seam's rates (`GATE_CALIBRATION_RATES`) flat after K=4 picked 4 and rates still rising picked 8, under a `false` spawn command that reds any timed loop. With the selection changed to take the maximum, the flat case picked 6 and the arm redded.
|  - AC3 — `check_sp_value` arm 12b — the cache held one line of four fields, and `--print-profile`, its line and a real bar's header all read width 4 from `calibrated`. With the bar's cache read pointed at nothing, all three redded on `8|row`.
|  - AC4 — `check_sp_value` arm 12c — absent, malformed, 2020-dated and other-boot caches each left width 8 and named their cause, and `GATE_JOBS=3` outranked a valid cache. With the age test removed, the 2020 cache was used and the arm redded. In the first break run the arm redded for the wrong cause: its cache carried `-` for the boot, so the boot test refused it as `another boot`. The arm now stamps this boot, so only the age test can refuse it.
|  - AC5 — `check_sp_value` arm 12d — a reading of 5000 us against a 2x ratio of a 1000 us floor held at least one episode, each ending `drained` or `bound` and held by `spawn`, with three `GATE ok` lines and one `spawn:` line. A reading of 1500 us held nothing. Arm 12f's sampler-driven hold ended `drained` by `spawn`. With the spawn reading never consulted, 12d and 12f both redded.
| -- AC6 — `check_sp_value` arm 12e — with no floor recorded, one `run-gates: NOTE` and one `spawn: … INERT` line printed, no pauses row was written, and three legs reported. With the absent floor read as 0, both lines vanished and two pauses rows were written, so the arm redded.
| +- AC6 — `check_sp_value` arm 12e (its row declares `spawnpause=2`) — with no floor recorded, one `run-gates: NOTE` and one `spawn: … INERT` line printed, no pauses row was written, and three legs reported. With the absent floor read as 0, both lines vanished and two pauses rows were written, so the arm redded.
|  - AC7 — `PINNED_KNOBS` — with `spawnpause` dropped from the slice's pinned set, the runner-set half redded naming `run-gates.sh implements knob key 'spawnpause'`, beside the table half's existing red.
|  
|  Outside the criteria, two regressions found in the continuation were fixed and observed directly.
| diff --git a/memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-3-acceptance-ledger.md b/memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-3-acceptance-ledger.md
| index 39d5b7fd1..007c0cc78 100644
| --- a/memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-3-acceptance-ledger.md
| +++ b/memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-3-acceptance-ledger.md
| @@ -20,23 +20,25 @@ VERIFYING and says so.
|    line, the reworded deferral apart: `GATE ok    sleeper`, the deferral, the pending chunk line,
|    `GATE ok    once  (retried after timeout)`, `---- retry: green  (1 retried, 0 failed)`, `----`.
|    The canary's 9k byte-equality arm is OWED at VERIFYING.
| -- AC3 — `direct-checks.sh ac3` — after, a 30 s ceiling under a 50 s wall: the breach printed
| -  `still running at the wall: stall (its serial retry)` and no `GATE ok` or `GATE FAIL` line for the
| -  leg. A first draft at a 10 s ceiling and an 18 s wall named only the sleeper, because the release
| +- AC3 — `direct-checks.sh ac3` — after, a 30 s ceiling under a 50 s wall: under `GATE_WALL=50` the
| +  breach printed `still running at the wall: stall (its serial retry)` and no `GATE ok` or
| +  `GATE FAIL` line for the leg. A first draft at a 10 s ceiling and an 18 s wall named only the sleeper, because the release
|    came 10 to 14 s after the first attempt's end on this host; both arms now carry the wider window.
|    The canary's 9l arm is OWED at VERIFYING.
| -- AC4 — `direct-checks.sh ac4` — after: one FAIL line for the leg, reading "timed out after 3s, again
| -  on its serial retry" with the serial attempt's HOST note; the set-aside `1.tail.leg` reads
| -  `timeout` and started before the sleeper ended, and `1.retry.leg` started after it. Its first run
| -  read a floor an earlier case had written to the shared floor path, which the instrument and the
| -  canary's 9m arm now remove first. The 9m arm is OWED at VERIFYING.
| +- AC4 — `direct-checks.sh ac4` — after: one FAIL line for the leg, reading
| +  "`timed out after 3s, again on its serial retry`" with the serial attempt's HOST note; the
| +  set-aside `1.tail.leg` reads `timeout` and started before the sleeper ended, and `1.retry.leg`
| +  started after it. Its first run read a floor an earlier case had written to the shared floor path,
| +  which the instrument and the canary's 9m arm now remove first. The 9m arm is OWED at VERIFYING.
|  - AC5 — `direct-checks.sh ac5` — before: the header's `dispatch` key read `0 1 2`; after: `1 2 0`.
|    The evidence suite's AC5 arm is OWED at VERIFYING.
|  - AC6 — `direct-checks.sh ac6` — before: `0 1 2 3`; after: `0 1 3 2`, the ledger placing `a` and a
|    40 s ceiling over the median ratio 10 placing `d` between `b` and `c`. The evidence suite's AC6 arm
|    is OWED at VERIFYING.
| -- AC7 — `direct-checks.sh ac7` — before: a second bar that reused its one leg left
| -  `gate-ledger.tsv` with 0 rows; after: 1 row. The canary's 9d assertion is OWED at VERIFYING.
| +- AC7 — `direct-checks.sh ac7` — before: on the base runner at 286b839a, whose ledger merge is the
| +  `NR == FNR` program the criterion names (spelled `NR==FNR` there), a second bar that reused its
| +  one leg left `gate-ledger.tsv` with 0 rows; after: 1 row. The canary's 9d assertion is OWED at
| +  VERIFYING.
|  
|  Checked as well, none of them a bar leg over the tree: `check-arms.py --check` reports the same six
|  unarmed `run-gates.sh` exit sites as before this pass; `sh_hygiene.py --spawn-idioms` over the leg's
| diff --git a/memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-4-acceptance-ledger.md b/memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-4-acceptance-ledger.md
| index 097150941..4ebd0aa76 100644
| --- a/memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-4-acceptance-ledger.md
| +++ b/memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-4-acceptance-ledger.md
| @@ -33,7 +33,7 @@ re-rendered suites. Every suite arm this unit adds or moves is OWED at VERIFYING
|    `----` lines at `GATE_JOBS=1` equal those at `GATE_JOBS=4` and the base runner's, and no leg reads
|    `(no result)`, on the final runner. The canary's pool-equivalence arm is OWED at VERIFYING.
|  - AC6 — `direct-checks.sh keys` — over a dirty tree (an edited tracked file, an untracked file under a
| -  guard, a staged edit), all six ledger keys, a directory guard, a nested one, two files, a glob that
| +  guard, a staged edit), all six `input_key` ledger keys, a directory guard, a nested one, two files, a glob that
|    takes the per-leg path, an absent path and an unguarded leg, equal the base runner's, and a
|    `GATE_REUSE` bar reused all six on the precomputed keys, on the final runner. The base is the
|    parent, which carries the reuse-key unit's definition. The evidence suite's per-leg and
| @@ -45,7 +45,8 @@ re-rendered suites. Every suite arm this unit adds or moves is OWED at VERIFYING
|    redaction and the ledger seconds.
|    The evidence suite's AC7 arms are OWED at VERIFYING.
|  - AC8 — `direct-checks.sh forks` — the counter read the specimen's declared 5 forks and 1 exec, and the
| -  same specimen with its trace descriptor closed first refused with 2. The run-log suite's SPAWNS arm
| +  same specimen with its trace descriptor (the one its `PS4` trace writes to) closed first refused
| +  with 2. The run-log suite's SPAWNS arm
|    carries the same counter and is OWED at VERIFYING.
|  - AC9 — `direct-checks.sh forks` — per-leg events, forks plus execs over ceiling-declaring legs at width
|    1 with the spawn floor pinned: base 40 (25 forks, 15 execs), twice; cut 5 (2 forks, 3 execs), twice;
| @@ -55,14 +56,14 @@ re-rendered suites. Every suite arm this unit adds or moves is OWED at VERIFYING
|    runner, the floor write landing in one trace only, which is why the arm pins it.
|  - AC10 — `direct-checks.sh procmon` — python execs before the first dispatch, base against cut: found
|    kit 4 and 3, missing kit 3 and 2, refusing scope 4 and 3; the `run-gates: process-monitor:` line
| -  equals the base's for all three, the refusal's paths included. The SPAWNS arm's in-suite form is OWED.
| +  (which prints `PROCMON_WHY`) equals the base's for all three, the refusal's paths included. The SPAWNS arm's in-suite form is OWED.
|  - AC11 — `direct-checks.sh parity` — the marked region of all 67 copies equals
|    `tools/lib/resolve_kit_dir.py`, the population covers every file `git grep -l '>>> resolve_kit_dir'`
|    lists outside `memory/`, and no file there still captures the heredoc with `cat`. The re-render's
|    own checker refused on any moved byte inside the markers and reported none; the parity suite is
|    OWED at VERIFYING.
|  - AC12 — `direct-checks.sh ban` — the S12 predicate over a scratch copy of `agent-cap.test.sh` with its
| -  wrapper reverted fired once, at line 73, and stayed silent on a comment spelling the idiom. The
| +  wrapper reverted (to `"$(cat <<'RKD'`) fired once, at line 73, and stayed silent on a comment spelling the idiom. The
|    resolve-python suite's ban arm is OWED at VERIFYING.
|  
|  Also observed directly: `fork-count.sh --only` on a frozen root read the one-leg row at 72 twice (its
| diff --git a/memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-6-acceptance-ledger.md b/memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-6-acceptance-ledger.md
| index 3c0b88bc7..59c4416f3 100644
| --- a/memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-6-acceptance-ledger.md
| +++ b/memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-6-acceptance-ledger.md
| @@ -33,19 +33,20 @@ observe is owed at VERIFYING and says so.
|    `check-arms.py --emit-floors` prints `374:360` for the driver where `.memory-tree.conf` holds the
|    floor `362:348`; the row set is unchanged, so the emission is the one the unchanged rows give and
|    the token does not move. It does not literally reproduce the token, and the gap predates this unit.
| -- AC6 — not run — owed at the owner's equivalence run: each shard once with
| -  `UNATTENDED_HARNESS=process` and once with `inproc`, compared by assertion count and sorted
| +- AC6 — amended rev-2, the spec's entry that names AC6 and makes this run the owner's equivalence
| +  run once the harness landed dark — not run — owed at the owner's equivalence run: each shard once
| +  with `UNATTENDED_HARNESS=process` and once with `inproc`, compared by assertion count and sorted
|    assertion multiset.
|  - AC7 — `unattended.sh --plan aSparedSpawn`, as a process and as `( load_driver_conf && main … )` in
|    a shell that sourced the driver — 17 lines byte-identical, rc 0 and 0, `git status` unchanged. A
|    grep of the parity rows against `VERBS_SLUG`, `VERBS_INLINE` and `--overlaps` found every verb
|    carried by a row. The parity table itself and its staged `read_bound_key` break are owed at
|    VERIFYING with shard 1.
| -- AC8 — the two tail predicates, each confirmed byte-identical to the suite's text and run alone —
| -  the top-level-exit scan found only the declared missing-library exit on line 90 of the real driver,
| -  and also line 731 in a copy staged with an undeclared `exit 3`. The namespace comparison read empty
| -  on two dumps of the 327 sourced definitions. It named `readme_of` and `verb_list` once one was
| -  doubled and the other unset, and read empty again after re-sourcing the driver. The arms inside
| -  their shard are owed at VERIFYING.
| +- AC8 — `exit 3` — the two tail predicates, each confirmed byte-identical to the suite's text and
| +  run alone — the top-level-exit scan found only the declared missing-library exit on line 90 of
| +  the real driver, and also line 731 in a copy staged with an undeclared `exit 3`. The namespace
| +  comparison read empty on two dumps of the 327 sourced definitions. It named `readme_of` and
| +  `verb_list` once one was doubled and the other unset, and read empty again after re-sourcing the
| +  driver. The arms inside their shard are owed at VERIFYING.
|  - AC9 — not run — owed at VERIFYING: the staged zero under `UNATTENDED_HARNESS=inproc` and the green
|    process-mode shard are shard runs.
| diff --git a/memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-8-acceptance-ledger.md b/memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-8-acceptance-ledger.md
| index d40183575..ed6cea8eb 100644
| --- a/memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-8-acceptance-ledger.md
| +++ b/memory/builds/aSparedSpawn/build/2026-10-11-build-TOOL-aSparedSpawn-8-acceptance-ledger.md
| @@ -38,10 +38,10 @@ identical output but for `--liveness`'s wall-clock age.
|    on its specimen and silent on its near miss, a quoted-heredoc specimen and a commented one firing
|    nothing. Two breaks staged in scratch copies each turned it RED: a BANNED row honoured instead of
|    refused, and `$(<f)` with no second redirect graded a site.
| -- AC6 — `python3 tools/gate-lint/sh_hygiene.py --spawn-idioms memory/project/spawn-idiom-sites.txt .
| -  ':!*.test.sh' ':!memory/'` over the tree — exit 0, each class's scanned, gated and near-miss counts
| -  printed, 0 sites for each BANNED class, 2099 registered sites in 292 rows; over a scratch copy of the
| -  shell population with `x=$(date +%s)` appended to `tools/check-wiring.sh` it exited 1 printing
| +- AC6 — `python3 tools/gate-lint/sh_hygiene.py --spawn-idioms memory/project/spawn-idiom-sites.txt . ':!*.test.sh' ':!memory/'`
| +  over the tree — exit 0, each class's scanned, gated and near-miss counts printed, 0 sites for each
| +  BANNED class, 2099 registered sites in 292 rows; over a scratch copy of the shell population with
| +  `x=$(date +%s)` appended to `tools/check-wiring.sh` it exited 1 printing
|    `tools/check-wiring.sh:1772: [epoch-date] x=$(date +%s) — use $EPOCHSECONDS…`, and with a pathspec
|    selecting nothing it refused with 2. Every count in the registry was derived by the scan.
|  - AC7 — the parent's `resolve_kit_dir` wrapper against the converted one in `lib-unattended.sh`, over
| @@ -57,19 +57,19 @@ identical output but for `--liveness`'s wall-clock age.
|  - AC9 — `bash tools/gate-lint/fork-count.sh --selftest` — the specimen counted 5 forks on both runs, equal to its declaration, and a scratch copy with
|    `SPECIMEN_FORKS=6` refused with exit 2 and the line "the counter cannot move"; PASS (2 assertions),
|    repeated on the final file.
| -- AC10 — `bash tools/gate-lint/fork-count.sh memory/project/fork-ceilings.txt <scratch root> --only
| -  unattended-status --sites` over a scratch repository holding the kits with `_ac10=$(:)` inserted
| -  below the driver's `set -u`, and over its unbroken twin — the staged root redded `measured 48 ·
| -  ceiling 47 · delta +1 · base 57` with the top ten `file:line` sites and the `--sites` hint, the twin
| -  read `ok … measured 47`, and the two `--sites` tables differed by `unattended.sh:58` alone once the
| -  sites below it were shifted back by one line. A first staged root that was no git repository read
| -  76, which is why every fixture here is a repository.
| +- AC10 — `bash tools/gate-lint/fork-count.sh memory/project/fork-ceilings.txt <scratch root> --only unattended-status --sites`
| +  over a scratch repository holding the kits with `_ac10=$(:)` inserted below the driver's `set -u`,
| +  and over its unbroken twin — the staged root redded `measured 48 · ceiling 47 · delta +1 · base 57`
| +  with the top ten `file:line` sites and the `--sites` hint, the twin read `ok … measured 47`, and the
| +  two `--sites` tables differed by `unattended.sh:58` alone once the sites below it were shifted back
| +  by one line. A first staged root that was no git repository read 76, which is why every fixture
| +  here is a repository.
|  - AC11 — `bash tools/gate-lint/fork-count.sh <copy of the ceilings> .` — with `check-wiring` raised to 54 against its count of 50 (max(3, 5 %)
|    is 3) redded `STALE ceiling 54 is more than 3 above the measured 50`, and a row whose setup is
| -  `exit 3` printed `skipped — unbuildable · its fixture setup exited 3…` and the summary read `0 passed
| -  · 1 red · 1 skipped`.
| +  `exit 3` printed `skipped — unbuildable · its fixture setup exited 3…` (an instance of
| +  `skipped — <id> · <why>`) and the summary read `0 passed · 1 red · 1 skipped`.
|  - AC12 — `bash tools/gate-lint/fork-count.sh` over each fixture, the tree at base `22efab65` and at
| -  the pass's tip side by side — forks per invocation, base then tip: `unattended-status` 57 → 47, `check-unattended` 709 →
| +  the pass's tip side by side — forks per invocation, base then tip: `unattended-status` (the row whose command runs `tools/unattended/unattended.sh`) 57 → 47, `check-unattended` 709 →
|    684, `run-gates-1leg` 72 → 72, `run-gates-2leg` 97 → 95, `memory-hygiene` 219 → 221 (the fixture
|    copies the tree's conf, which grew), `manifest-check` 108 → 108, `check-wiring` 55 → 50. Every tip
|    count repeated exactly on three runs except `run-gates-2leg`, which read 95, 95, 95 and 96, its pool
| diff --git a/memory/builds/aSparedSpawn/build/2026-10-12-build-TOOL-aSparedSpawn-16-acceptance-ledger.md b/memory/builds/aSparedSpawn/build/2026-10-12-build-TOOL-aSparedSpawn-16-acceptance-ledger.md
| index ef344c1d7..d596a40ed 100644
| --- a/memory/builds/aSparedSpawn/build/2026-10-12-build-TOOL-aSparedSpawn-16-acceptance-ledger.md
| +++ b/memory/builds/aSparedSpawn/build/2026-10-12-build-TOOL-aSparedSpawn-16-acceptance-ledger.md
| @@ -16,13 +16,14 @@ and its AC11 moved to the build's exit at rev-3 and are not observed here.
|  - AC4 — `python tools/memory-tree/check-arms.py --check` — exit 0 and no `HYGIENE check-arms: tools/run-gates/run-gates.sh` line; at the unit's base it named the six sites. The canary arms 12a2 and 9d3 that arm them are OWED at VERIFYING; the two refusals 12a2 asserts were observed by running `--calibrate-width` directly in a scratch repo, each exiting 1 with its whole text.
|  - AC6 — `direct-checks.sh push` — changed hook: `pre-push: not honoured from the environment by this bar: GATE_REUSE_SAMPLE GATE_REUSE_DAY`, and the stub bar saw `unset|unset`; base hook: no such line, and the stub bar saw `0|1`. The suite arm `RP S6` is OWED at VERIFYING.
|  - AC10 — `grep -n 'by TOOL-aSparedSpawn-13 and -16' tools/run-gates/run-gates.evidence.test.sh` — one `RAISED 163 -> 208` line, and `FLOOR_ASSERTIONS` is 208. Whether the executed count reaches 208 is OWED at VERIFYING.
| -- AC11 — `--dispatch` — MOVED to the build's exit with S10 at rev-3, so no check observes it in this unit; it is an ask, not a discharge.
| -- AC12 — `direct-checks.sh reuse` — changed runner: with K1's count at 9, a K2 execution on a dirty tree, then a K1 reuse, the next K1 run printed `GATE ok    pa  (executed: reused on 10 runs in a row)` and the age line; base runner: that run printed `GATE reuse pa`. The evidence arm `16-AC12` is OWED at VERIFYING.
| +- AC11 — amended rev-3, the spec's entry that moved S10 with this criterion to the build's exit as a named ask —
| +  `--dispatch` — MOVED to the build's exit with S10 at rev-3, so no check observes it in this unit; it is an ask, not a discharge. The spec's rev-4 entry names that ask, `TOOL-aSparedSpawn-25`.
| +- AC12 — `direct-checks.sh reuse` — changed runner: with K1's count at 9, a K2 execution on a dirty tree, then a K1 reuse, the next K1 run printed `GATE ok    pa  (executed: reused on 10 runs in a row)` and the age line; base runner: counting in its per-name `age.*` file (`age.${heldkeys[$i]}` at f53211e6c) that run printed `GATE reuse pa`. The evidence arm `16-AC12` is OWED at VERIFYING.
|  - AC13 — `grep -n 'sleep 1[25]' tools/run-gates/run-gates.test.sh` — finds neither the 9k nor the 9m sleeper, each now polling for its signal file. The fork-loaded run of both arms is OWED at VERIFYING.
|  - AC14 — `direct-checks.sh contended` — shipped runner: the contended leg's key holds no cache entry and the spinner's does; a copy whose cache writer reads `.retry.rc` wrote the contended entry, which the new 9f assertion reds on. The arm itself is OWED at VERIFYING.
|  - AC15 — `python tools/run-gates/held_halves.py --selftest` — 34/34 arms; with `load_half`'s `newline=""` removed it printed `FAIL held-halves selftest: S14 a CR in a failing leg's output splits off no verdict row` and 33/34.
|  - AC16 — `git grep -n 'ts_now' -- tools/` — prints nothing; `grep -c 'EPOCHSECONDS:-' tools/run-gates/run-gates.sh` prints 0.
|  - AC17 — `direct-checks.sh reuse` — changed runner: the nondeterministic red's `log:` file opens `# run-gates | leg pa | exit 1`; base runner: `exit 0`, the sample's second look. The evidence arm `16-AC17` is OWED at VERIFYING.
| -- AC18 — `direct-checks.sh reuse` — changed runner: `GATE ok    pa  (sampled against a cached ok)` on a drawn leg, the aged tail on a count of 10, and `GATE FAIL  pa  (exit 1) (sampled against a cached ok)` on a drawn red; base runner: the plain lines. The canary arm 9d2 is OWED at VERIFYING.
| +- AC18 — `direct-checks.sh reuse` — changed runner: `GATE ok    pa  (sampled against a cached ok)` (an instance of `GATE ok    <leg>  (sampled against a cached ok)`) on a drawn leg, the aged tail on a count of 10, and `GATE FAIL  pa  (exit 1) (sampled against a cached ok)` on a drawn red; base runner: the plain lines. The canary arm 9d2 is OWED at VERIFYING.
|  - AC19 — `direct-checks.sh reuse` — changed runner, with a `git` that fails `hash-object` first on PATH: a reusing bar and a clean plain bar each printed `the input keys could not be measured (the toolchain digest)` once, a dirty plain bar none; base runner: silent on all three. The canary arm 9d3 is OWED at VERIFYING.
|  - AC20 — `grep -n 'print_env_failure' memory/builds/aSparedSpawn/spec/2026-10-09-spec-TOOL-aSparedSpawn-14.md` — prints AC11's line, S10's, the §7 arm line and the rev-4 and rev-5 log lines; AC11 names the five checks 27, 29, 56, 69 and 88.
| diff --git a/memory/builds/aSparedSpawn/build/2026-10-12-build-TOOL-aSparedSpawn-32-acceptance-ledger.md b/memory/builds/aSparedSpawn/build/2026-10-12-build-TOOL-aSparedSpawn-32-acceptance-ledger.md
| index daf419251..048315377 100644
| --- a/memory/builds/aSparedSpawn/build/2026-10-12-build-TOOL-aSparedSpawn-32-acceptance-ledger.md
| +++ b/memory/builds/aSparedSpawn/build/2026-10-12-build-TOOL-aSparedSpawn-32-acceptance-ledger.md
| @@ -18,8 +18,10 @@ rev-4 `764b145d1` (`Pass: none`); and the pass commit after it, which composes t
|  §4 and closes the unit.
|  
|  **Evidences:** TOOL-aSparedSpawn-32
| -- AC1 — the two-parent diff over the staged merge (`git diff -U0 69e0ff0f5 6e8f8b1da -- F`, every
| -  added line searched for in the index) — 11 files; origin's added lines absent from the result: 4 in
| +- AC1 — amended rev-5, the spec's entry recording that this criterion's range was never read —
| +  NOT OBSERVED at the range the criterion names — the two-parent diff over the staged merge
| +  (`git diff -U0 69e0ff0f5 6e8f8b1da -- F`, every added line searched for in the index) — 11 files;
| +  origin's added lines absent from the result: 4 in
|    the runner, 5 in the hook, 4 in the evidence suite, 1 in the README, 1 in `.memory-tree.conf`, 1 in
|    `agent-cap.test.sh`, 1 in the hygiene suite, 2 in the dossier, 0 elsewhere. Each is a line both
|    sides rewrote, kept as its composite: `HEAD_SHA=$RG_HEAD` (origin's read, this build's no-spawn
| @@ -27,7 +29,9 @@ rev-4 `764b145d1` (`Pass: none`); and the pass commit after it, which composes t
|    scoped decision lines carrying both sides' fields, `lineage_reuses=0` initialised beside this
|    build's `reuses=0`, the summed `FLOOR_ASSERTIONS` (evidence 208 + 26 = 234, hygiene 613 + 5 = 618),
|    the `ARMS_FLOORS` line with both pairs, `agent-cap`'s `node nr.js` calls with origin's
| -  `unset GIT_DIR GIT_WORK_TREE`, and dossier prose condensed to its 20480-byte cap.
| +  `unset GIT_DIR GIT_WORK_TREE`, and dossier prose condensed to its 20480-byte cap. Never read:
| +  `git diff 69e0ff0f5 37200355d -- F`, the range the criterion names; the pass read origin's moved
| +  tip 6e8f8b1da, where the spec's §4 (f) took the merge.
|  - AC2 — the same diff from `01ba3a815` — this build's absent lines: 1 in the runner, 13 in the
|    hook, 3 in the evidence suite, 1 in the README, 1 in `.memory-tree.conf`, 2 in `agent-cap`, 1 in
|    the hygiene suite, 12 in the dossier. Each is the same composite seen from this side, plus
| @@ -76,9 +80,9 @@ rev-4 `764b145d1` (`Pass: none`); and the pass commit after it, which composes t
|    with an empty `full`, and `GATE_FULL=1 GATE_REUSE_LINEAGE=1` executes `pa` and records `lineage`.
|  - AC11 — `grep -c 'WHAT LINEAGE REUSE DOES NOT CHECK' tools/run-gates/README.md` prints 1, the
|    precedence table's header row occurs once, and the cache's not-checked sentence once.
| -- AC12 — the fixture's runner section — RED at the merge; GREEN on the pass tree: full with both
| -  knobs records `lineage` and prints `not used: GATE_REUSE`, and without the full flag records `env`
| -  and prints `GATE_REUSE_LINEAGE is not used without GATE_FULL`.
| +- AC12 — the fixture's runner section — RED at the merge; GREEN on the pass tree: full with both knobs records `lineage`
| +  and prints `not used: GATE_REUSE`, and without the full flag records `env` and prints
| +  `GATE_REUSE_LINEAGE is not used without GATE_FULL`.
|  
|  ## Arms written and owed at VERIFYING
|  
| diff --git a/memory/builds/aSparedSpawn/build/2026-10-13-build-TOOL-aSparedSpawn-34-acceptance-ledger.md b/memory/builds/aSparedSpawn/build/2026-10-13-build-TOOL-aSparedSpawn-34-acceptance-ledger.md
| index 903254344..65fca7144 100644
| --- a/memory/builds/aSparedSpawn/build/2026-10-13-build-TOOL-aSparedSpawn-34-acceptance-ledger.md
| +++ b/memory/builds/aSparedSpawn/build/2026-10-13-build-TOOL-aSparedSpawn-34-acceptance-ledger.md
| @@ -42,7 +42,7 @@ How the hand-merged hunks compose:
|    build's `if check_selected 1; then`.
|  
|  **Evidences:** TOOL-aSparedSpawn-34
| -- AC1 — the two-parent diff over the staged merge: every line `git diff -U0 6e8f8b1da main -- F` adds, searched for in the result, per conflicted product or suite file — absent, and each a composite named above: 11 in the runner (the knob list, the profile initialiser, the template line, and the eight lines local main added that call `ts_now`), 3 in the driver, 2 in the unattended suite, 2 in the run-gates suite, 1 each in the run-log suite, the hygiene suite, the drift-audit selftest, the manifest-check suite and the pre-push suite (each a floor or a union list), and 0 in `gate-profiles.txt` and `check-memory-hygiene.sh`.
| +- AC1 — the two-parent diff over the staged merge: every line `git diff -U0 6e8f8b1da main -- F` (the criterion's `git diff 6e8f8b1da main -- F`, whose added lines `-U0` does not change) adds, searched for in the result, per conflicted product or suite file — absent, and each a composite named above: 11 in the runner (the knob list, the profile initialiser, the template line, and the eight lines local main added that call `ts_now`), 3 in the driver, 2 in the unattended suite, 2 in the run-gates suite, 1 each in the run-log suite, the hygiene suite, the drift-audit selftest, the manifest-check suite and the pre-push suite (each a floor or a union list), and 0 in `gate-profiles.txt` and `check-memory-hygiene.sh`.
|  - AC2 — the same diff from `249b4ab6`'s side (`git diff -U0 6e8f8b1da HEAD -- F` before the merge commit) — absent, each the same composite seen from this side: 9 in the runner (the knob list, the initialiser, the `spawnpause` case arm split from its `esac`, the renamed `prof_sp` line, the template line and its two comment lines moved above `render_prof_line`, one comment line extended, and the reap's clock line indented into the slot loop), 3 in the driver, 3 in the run-gates suite (the floor, the pin and its comment), 2 in the unattended suite, 2 in the pre-push suite (the knob list and `decide_on`), and 1 floor each in the run-log, hygiene, drift-audit and manifest-check suites. No line of the reuse composition or the digest view is absent: `reused_cache`, `GATE_REUSE_DIGEST_ENV` and `REUSE_SCHEMA` are present in the runner, `GATE_REUSE_DIGEST_ENV` in the hook, and the header's `reuse` key is written once.
|  - AC3 — `python tools/codebase-map/gen_map.py --check` exit 0 on the merge commit; `python tools/memory-tree/gen_build_index.py --write` re-run on the merge commit left no diff.
|  - AC4 — `grep -n 'last-audit\|last-body-change' memory/guides/SESSION-KICKOFF.md` — the merge took local main's stamps, `last-audit … @ cfce31b6f` and `last-body-change 5e4b391e`; the body kept this build's `--calibrate-width` bar line, which git auto-merged. The re-stamp at the merge's sha is the records commit after the pass, so AC4's observation follows it.
~~~~

### ledgers/2026-10-15-build-TOOL-dRedressedBar-11-1-acceptance-ledger.md

~~~~text
| # TOOL-dRedressedBar-11 — acceptance ledger
| 
| **Serves:** journal TOOL-dRedressedBar-11
| 
| Written by TOOL-dRedressedBar-27 on 2026-10-15, after the unit closed with no ledger, from what its
| builder recorded. Nothing was re-run for it. The unit was built against spec 11 rev-3 in the one
| pass commit `b65688cde`. Spec 11's rev-4, rev-5 and rev-6 are records fixes that move no criterion
| text, so the readings answer the criteria as they stand. The readings are the builder's, from that
| commit's body and from its return in `2026-10-14-build-TOOL-dRedressedBar-1-2-agent-returns.md`,
| under the heading `2026-10-14T18:29:21 · gov-builder · wf_551a7d53-a85/aabed9b0e2ce4380b` at line
| 5180. The builder ran the `<p10>` halves over unit 10's block at `07feb3b38`. No merge bar, no
| self-test suite and no gate leg ran in the build pass, and the section 7 legs were owed to the
| close.
| 
| **Evidences:** TOOL-dRedressedBar-11
| - AC1 — `must_not_resolve` — the descriptor's code-2 block read back with all five parts, and
|   `("must_exist", True)` no longer appears in `tools/govkit/govkit.py`. The grep for
|   `must_not_resolve` printed the `OUTCOME_PROBE_KEYS` line and the docstring, plus a third line,
|   the `if key != "must_not_resolve"` branch the evaluation needs; the builder noted that AC1's red
|   condition does not cover that line.
| - AC2 — `refusing to wire` — an in-process program got the expected verdict in all seven states.
|   The adopter's stderr carried `cannot read` in the receipt row and `refusing to wire` with no
|   receipt. The same program over unit 10's block, from `git show 07feb3b38`, read ACCEPTED on the
|   receipt row, the red half.
| - AC3 — `govkit: kit 'settings-merge'` — on fixture A, by the CLI under `%TEMP%`, the second apply
|   exited 1 with exactly one such line, carrying `cannot read` and `settings.json`, and no
|   `no-agent-cap-to-wire` anywhere. Over a clone at `07feb3b38`, fixture A exited 0 with
|   `[accepted stop]`.
| - AC4 — `gov_commit` — on fixture B, `update --write` exited 1, printed the same single line, and
|   `gov_commit` stayed at `24f39915`. Over the `07feb3b38` clone it exited 0, re-stamped the receipt
|   and printed the accepted line. Spec 11's rev-5 records that the criterion's "Before the commit"
|   was inexact and that `TOOL-dRedressedBar-13`'s AC15 observed its corrected form.
| - AC5 — `[accepted stop]` — fixture A-absent exited 0 and printed it. The record names no re-run
|   of unit 9's AC2 program at the tip.
| - AC6 — `must_not_resolves` — with `check` replaced by a recorder, every label read true: 19
|   key-rule labels (18 blocks plus unit 9's), the liveness label, exactly the two `lexicon ` labels,
|   and six settings-merge rows. With `must_not_resolve` renamed to `must_not_resolves`, exactly two
|   labels went false: the settings-merge key-rule label and the receipt-only row. Spec 11's rev-5
|   records the halves of this criterion that `TOOL-dRedressedBar-13`'s AC7 and AC9 observed in
|   their corrected form.
| - AC7 — `scan_text_io` — `git diff 07feb3b38 b65688cd -- tools/govkit/` changed no `def` or
|   `class` line. `scan_text_io` counted 36 subprocess sites in `govkit.py`, none in `matrix.py`, and
|   24 subprocess plus 1 file-io in `selftest.py`, matching the registry.
~~~~

### ledgers/2026-10-15-build-TOOL-dRedressedBar-18-2-acceptance-ledger.md

~~~~text
| # TOOL-dRedressedBar-18 — acceptance ledger
| 
| **Serves:** journal TOOL-dRedressedBar-18
| 
| Written by TOOL-dRedressedBar-27 on 2026-10-16, after the unit closed with no ledger, from what its
| builders recorded. Nothing was re-run for it. This build's `-1-` record for unit 18 is the
| set-aside work of its first build, which diverged. The unit was then built against spec 18 rev-4
| in two commits: the pass commit `6783992aa`, which restored the set-aside code verbatim and
| changed it only where rev-4 requires, and `997fc294f`, which renamed four nested helpers and
| re-ran the serial and concurrent fixture manifests with the same readings. The readings below are
| the rev-4 builder's, from those commits' bodies and from its return in
| `2026-10-14-build-TOOL-dRedressedBar-1-2-agent-returns.md`, under the heading
| `2026-10-14T22:31:47 · gov-builder · wf_0e7a57a1-02c/acf19d67f5fb8f3f3` at line 5556, collected
| into that record by TOOL-dRedressedBar-27. AC8's reading is the first build's, under the heading
| `2026-10-14T21:36:47 · gov-builder · wf_2e958a62-4b6/af9e8721f060c270a` at line 5496. Every
| reading is a direct run of the tool on node d or a probe of its code. No merge bar, no self-test
| suite and no gate leg ran in the build pass, and the full `--selftest` run was owed to the close.
| 
| Spec 18's rev-5 to rev-8 are records fixes. Of them, only rev-7 moved criterion text, in AC1, AC2
| and AC5, and it says "Unit 18 built against its criteria as written". Those three lines are
| AMENDED and carry the rev-4 reading. AC15 was never observed, and spec 18's rev-9 records that.
| 
| **Evidences:** TOOL-dRedressedBar-18
| - AC1 — amended rev-7 — spec 18's rev-7 entry, a records fix for TOOL-dRedressedBar-22, rewrote
|   this criterion after the build: its resolution red half now says `TOOL-dRedressedBar-22` first
|   read both legs at verdict `ok` (its AC15). The rev-4 reading, from the return's table: on the
|   serial fixture run, `spawn six` 8 less `spawn none` 2 read 6, under the interpreter
|   `C:/Users/d41ly/AppData/Local/Python/pythoncore-3.14-64/python.exe`, and the spawn leg held 6
|   child rows, each with every field. With the resolution disabled the difference read 0. With the
|   breakaway staged, the run refused with exit 2 naming the interpreter, and with the verification
|   also skipped the difference read 0.
| - AC2 — amended rev-7 — spec 18's rev-7 entry rewrote this criterion after the build: its
|   resolution red half now says `TOOL-dRedressedBar-22` first read memio's verdict and its
|   `memio: wrote 200 MiB` line (its AC15). The rev-4 reading, from the return's table: the memio
|   leg's `peak_job_mem_b` read 225 MB and its `write_bytes` 209715204, and `spawn_s_est` matched
|   its formula. With the resolution disabled, `peak_job_mem_b` read 6963200 and `write_bytes` 0.
|   The rev-4 table gives no reading of the `extract_runner_function` red half; the first build's
|   return says the extraction refusal held.
| - AC3 — `census.FIELDS` — unchanged. The row carried `peak_mem_b` and `mem_b` as ints and its
|   `command` intact, the POSIX rows read None, and the red staging read `'300'`.
| - AC4 — `concurrent.json` — on the concurrent fixture run no admission sat above 80% CPU while a
|   leg ran, and the cap was exercised.
| - AC5 — amended rev-7 — spec 18's rev-7 entry rewrote this criterion after the build: it names the
|   widened call `check_admit(mode, pending, running, cpu, mem, fresh)` and a loop half, both
|   `TOOL-dRedressedBar-22`'s (its AC6). The rev-4 reading, over the five rows as rev-4 wrote them:
|   `check_admit` returned hold, admit, hold, hold and admit.
| - AC6 — `sleep` — the stall leg held 1 episode with `sleep` in its tree, the steady leg held none,
|   and every leg's rc read 0.
| - AC7 — `churn.py` — the churn leg held no episode, and 5 of its windows were decided by the job
|   veto.
| - AC8 — `measure_foreign` — the first build's parity probe: the runner's own `measure_foreign`,
|   with `ps` shimmed, and the port both gave 2 roots, `200:lib9/runner.sh` and
|   `300:probe/two/selftest.py`, and the port without the `selftest.py` rule gave 1. The rev-4 return
|   says that code is unchanged from the set-aside build and was not re-run, and `6783992aa`
|   restored the set-aside code verbatim.
| - AC9 — `serial.json` — the return's table reads AC9 as holding on the serial fixture run, and
|   gives no finer reading.
| - AC10 — `envelope.json` — the return's table reads AC10 as holding on the same serial run: the run
|   dir held the records the criterion lists.
| - AC11 — `printenv.py` — the return's table reads AC11 as holding on the same serial run, whose
|   `printenv.py` leg carries the planted credential.
| - AC12 — `linux` — `resolve_job_backend` refused, naming `linux` and the Job Object API.
| - AC13 — `measure-legs selftest` — all four declaration files carry the leg, with equal name,
|   subject and argv.
| - AC14 — `help/measure-legs.md` — the run-gates marker pair read an equal 1.41, the process-monitor
|   markers all read 0.19, and the help page carries every required token.
| - AC15 — amended rev-9 — NOT OBSERVED. Spec 18's rev-9 entry records that this criterion was never
|   observed. The rev-4 return says "the turnstile arm runs the real runner's hold verb, so I did not
|   run it", and owes it at the close with "the full `--selftest` run", which no pass may run. No
|   record of this build observes it since. Never observed: `<ml> --selftest`'s turnstile arm and
|   `queued.sh`'s `ts_wait_s`.
| - AC16 — `check_app_alias` — it returned True for the alias and False for its own interpreter and
|   for a missing path. The `SUBSTITUTED` line printed, and the `substitutions` entry, its `applied`,
|   the probe's counts 3 and 2, and `GOV_PYTHON` in the log all held. With an `islink` test staged,
|   the run refused with exit 2, naming `python3`.
| - AC17 — `scratch_posix` — on AC1's run both converted spellings start with a drive letter,
|   `scratch` is a directory, and both posix spellings start with `/`. With the bash spelling
|   printed, the run refused, naming the scratch dir. The half on AC15's run is owed: the return says
|   "Neither half of AC17 on AC15's run was observed either".
~~~~

### ledgers/2026-10-15-build-TOOL-dRedressedBar-2-1-acceptance-ledger.md

~~~~text
| # TOOL-dRedressedBar-2 — acceptance ledger
| 
| **Serves:** journal TOOL-dRedressedBar-2
| 
| Written by TOOL-dRedressedBar-27 on 2026-10-15, after the unit closed with no ledger, from what its
| builder recorded. Nothing was re-run for it. The unit was built against spec 2 rev-3, which is
| still its current revision, in the one pass commit `c7a9213d1`. The readings below are the
| builder's, from that commit's body and from its return in
| `2026-10-14-build-TOOL-dRedressedBar-1-2-agent-returns.md`, under the heading
| `2026-10-14T14:23:16 · gov-builder · wf_eb13c24a-b41/af59039234e86d2c9` at line 4655. No merge
| bar, no self-test suite and no gate leg ran in the build pass. Every reading is a direct probe, and
| the section 7 legs were owed to the close.
| 
| **Evidences:** TOOL-dRedressedBar-2
| - AC1 — `grep -nw clean` — over `tools/unattended/gate-guard.js` it printed nothing, and
|   `grep -n renderAskQuote` printed exactly lines 689, 694 and 696: the declaration and the two
|   calls, all inside `extractAskQuestions`.
| - AC2 — `extractAskQuestions` — a node probe ran it on the tip's file and on
|   `git show ebce889c:tools/unattended/gate-guard.js` written to scratch, over a payload with a
|   400-character question carrying a BEL and a C1 byte, a label carrying a NUL, a non-string label,
|   a blank question and a null question, then `{}`. The two outputs were byte-identical. The first
|   question read 300 characters, and `{}` read `[{"question":"(no question text)","labels":[]}]`.
| - AC3 — `--measure` — it printed `VERB_OFFENDER_PIN="1087"`, matching `.lexicon.conf:268`.
|   `--suggest renderAskQuote --as js.function` printed `OK — renderAskQuote leads with render...`,
|   and `--offenders` listed 1087 verb offenders and no line naming the gate guard. The builder ran
|   the three again after the map regeneration and read the same.
| - AC4 — `memory/map/generated/symbols.json` — at the tip it held `renderAskQuote` once and `clean`
|   zero times for the gate guard, and the `3d1adca9` copy held `renderAskQuote` zero times and
|   `clean` once. `gen_map.py --check` exited 0. `git show --name-only --format= c7a9213d1` listed
|   the gate guard and `symbols.json`, and no other path under `memory/map/`.
~~~~

### ledgers/2026-10-15-build-TOOL-dRedressedBar-20-1-acceptance-ledger.md

~~~~text
| # TOOL-dRedressedBar-20 — acceptance ledger
| 
| **Serves:** journal TOOL-dRedressedBar-20
| 
| Written by TOOL-dRedressedBar-27 on 2026-10-15, after the unit closed with no ledger, from what its
| builder recorded. Nothing was re-run for it. The unit was built against spec 20 rev-2, which is
| still its current revision, in three commits: the code commit `404d45c8c`, the restore commit
| `21c2d1531`, and `566c6d831`, which moves the status header alone. The readings are the builder's,
| from those commits' bodies and from its return in
| `2026-10-14-build-TOOL-dRedressedBar-1-2-agent-returns.md`, under the heading
| `2026-10-14T17:20:54 · gov-builder · wf_505af0b9-122/a737641ff163ce752` at line 5022. The code
| commit's first parent is `20112bce8`. No merge bar, no self-test suite and no gate leg ran in the
| build pass, and the section 7 legs and the `New arm:` observation were owed to the close.
| 
| **Evidences:** TOOL-dRedressedBar-20
| - AC1 — `git diff -U0` — in a clone of `20112bce8` the writer printed the one tuple
|   `('tools/playbook/render_playbook.py', 'playbook-render', 'playbook-render', '3.5', '1.28')`, and
|   `git diff -U0` changed line 1646 only. In a clone of `404d45c8c` it printed `[]` with a clean
|   status. The commit body reads the green half over the code's bytes copied into the first
|   clone, where `git status --porcelain` named only the two copied files.
| - AC2 — `version: '9.99'` — with `KIT_DRIFT_AUDIT_VERSION` at 9.99, the writer made 14 rewrites,
|   two in each harness, and `grep -c "version: '9.99'"` printed 1 for each of the four.
| - AC3 — `epoch: playbook-render · clean · 1.28` — `mint --base ebce889c7` in a fresh clone of
|   `404d45c8c` exited 0 with `->` lines for agent-cap, branch-reconcile, roles and unattended only,
|   and `tools/playbook/` stayed clean. After a scratch commit, `epoch` printed that line and no
|   FAILED line at all. The builder recorded one deviation: the scratch commit in the clone took
|   `--no-verify`.
| - AC4 — `[dRB-20]` — the `arm` probe, run alone with `__pycache__` deleted first, exited 1 over
|   the base writer with FAIL lines naming `[dRB-20]` and the count (9), and exited 0 with every
|   line ok over the fix, again at HEAD. Its `tempfile.mkdtemp` took `dir=` the scratchpad.
| - AC5 — `grep -c "ANY entry's"` — it printed 0, and the scope sentence's grep printed 1.
| - AC6 — `tools/govkit/govkit.py` — the code commit's diff names exactly it and
|   `tools/govkit/selftest.py`, and adds or removes no `def` line.
| - AC7 — `v3.5` — at `21c2d1531`, lines 1397 and 1646 both read it, and the code-to-restore diff is
|   one file and changes line 1397 only. In a clone of the restore commit the writer printed `[]`
|   with a clean status, and `epoch` printed `epoch: playbook-render · FAILED · moved in 21c2d1531d`,
|   the move unit 7's mint dates.
| - AC8 — `<!-- governance-template: v3.5 --> True True True` — `v3render`, run from a scratch script
|   at the restore commit, exited 0 and printed it. With the marker at `v4.0` in a scratch clone, it
|   refused, naming the `when:node-table` fence, so the probe can go red.
~~~~

### ledgers/2026-10-15-build-TOOL-dRedressedBar-4-1-acceptance-ledger.md

~~~~text
| # TOOL-dRedressedBar-4 — acceptance ledger
| 
| **Serves:** journal TOOL-dRedressedBar-4
| 
| Written by TOOL-dRedressedBar-27 on 2026-10-15, after the unit closed with no ledger, from what its
| builder recorded. Nothing was re-run for it. The unit was built against spec 4 rev-2 in the one
| pass commit `305ea9c20`. Spec 4's rev-3 then corrected §3, §5 and §7 as a records fix and moved no
| criterion, so the readings answer the criteria as they stand. The readings are the builder's, from
| that commit's body and from its return in `2026-10-14-build-TOOL-dRedressedBar-1-2-agent-returns.md`,
| under the heading `2026-10-14T14:59:54 · gov-builder · wf_dd507e84-fcf/a9cc4903461cf4d48` at line
| 4707. No merge bar, no self-test suite and no gate leg ran in the build pass. Every reading is a
| direct probe, and the section 7 legs were owed to the close.
| 
| **Evidences:** TOOL-dRedressedBar-4
| - AC1 — `WORKFLOW_RUNS_DIR` — the quoted-literal search over `tools/hooks/format-guard.js` printed
|   one line, the declaration. The constant search printed the declaration and the
|   `readJournalAgents` join, and nothing else.
| - AC2 — `{"started":["a1"],"ended":["a1"]}` — `readJournalAgents` over a journal planted in the
|   scratchpad printed it. On a scratch copy with the constant set to `workflowz`, it printed the
|   unreadable-journal error (ENOENT), the red half.
| - AC3 — `WORKFLOW_RUNS_DIR = "workflows"` — the same quoted-literal search over
|   `tools/roles/adopt-roles.test.sh` printed only that line, and the
|   `wf = sub / WORKFLOW_RUNS_DIR /` line was found.
| - AC4 — `sess/x/subagents/workflows/wf_00000001-aaa/journal.jsonl` — the A9_WRITE program,
|   extracted to a file, carried 0 apostrophes, exited 0 and wrote that journal. On a copy with the
|   constant changed, the file was not there, the red half.
~~~~

### ledgers/2026-10-15-build-TOOL-dRedressedBar-5-1-acceptance-ledger.md

~~~~text
| # TOOL-dRedressedBar-5 — acceptance ledger
| 
| **Serves:** journal TOOL-dRedressedBar-5
| 
| Written by TOOL-dRedressedBar-27 on 2026-10-15, after the unit closed with no ledger, from what its
| builder recorded. Nothing was re-run for it. The builder's return says the probe output "was not
| committed: no acceptance ledger exists for any unit of this build, so the main loop records it at
| the close"; this is that record. The unit was built against spec 5 rev-5 in the one pass commit
| `ecdca277e`. Spec 5's rev-6 names AC1 and AC2 and says "no criterion text moves", so the readings
| answer the criteria as they stand. The readings are the builder's, from that commit's body and
| from its return in `2026-10-14-build-TOOL-dRedressedBar-1-2-agent-returns.md`, under the heading
| `2026-10-14T15:57:14 · gov-builder · wf_295d6b9f-6a5/a5092d46835faecff` at line 4882. Every probe
| ran under bash 5.3.9. No merge bar, no self-test suite and no gate leg ran in the build pass, and
| the section 7 legs were owed to the close.
| 
| **Evidences:** TOOL-dRedressedBar-5
| - AC1 — `grep -nE '\$\((basename|dirname|date) '` — over the four files it printed nothing.
| - AC2 — `var-pipe` — the count printed 0, 0 and 0 for the branch-reconcile adopter, the roles
|   adopter and the roles suite, and 62 for `tools/workflows/unattended-build.test.sh`, equal to that
|   file's row. Imported, sh_hygiene's own `scan_spawn_file` read 0 registry-class sites in the four
|   row-less files, and printf-subst 66, var-pipe 62, pure-fn-subst 28, path-subst 6 and cat-file 1
|   for the suite, each equal to its row.
| - AC3 — `printf -v _wfj` — the whole-file `$(printf ` count fell from 288 to 275. The commit's diff
|   holds five `-` lines with a pipe-free `$(printf `, and their `+` lines say `printf -v _wfj`.
| - AC4 — `${CH%/*}` — the forms probe ran 186 specimen pairs, among them the specimens the
|   criterion names and every converted site read at its converted line, and every pair matched.
|   Both staged wrong forms differed: `${CH%/*}` alone on `AGENTS.md`, and the CR strip inside
|   `$( )`. A second probe ran arm 9's compare over the suite's own A9L1 and A9L2 values: 4 of 4
|   matched, and the wrong form failed on the CRLF value.
| - AC5 — `TMPDIR` — in a clone under `%TEMP%/u5fx`, with `TMPDIR` set to the scratchpad, the
|   `ebce889c` adopters and the converted ones printed the same lines and statuses from the root,
|   from each kit directory, by absolute path and as `./`. That clone's fixture passed 25 of 25
|   checks across AC5 to AC7.
| - AC6 — `.claude/skills/branch-reconcile/SKILL.md` — in the same clone, the recognised render there
|   was withdrawn, a foreign file was kept, a near-miss name was kept, a CRLF render was withdrawn,
|   and the `tools/` hits printed indented, as the criterion states.
| - AC7 — `{{UNKNOWN_TOKEN}}` — in the same clone, the refusal printed the
|   `    line <n>:{{UNKNOWN_TOKEN}}` line.
| - AC8 — `memory/project/spawn-idiom-sites.txt` — its diff at the pass commit is empty.
| - AC9 — `mkdir -p "${SKILL%/*}" || exit 1` — the pin file's diff is one hunk with one `-` line and
|   one `+` line, five fields each, agreeing on fields 1, 2, 3 and 5. Row 178 was re-keyed to that
|   converted line in field 4 only, and the file holds 181 lines at both commits.
| - AC10 — `scan_refusal_sites` — check-arms' own `scan_refusal_sites` and `parse_pin` found all 11
|   pins of the branch-reconcile adopter live, with 13 sites in total (11 + 2). The staged red, the
|   `<pass>~1` adopter against the pass rows, reported row 178 stale and the old key unpinned. The
|   two roles sites carried equal keys before and after.
~~~~

### ledgers/2026-10-15-build-TOOL-dRedressedBar-7-1-acceptance-ledger.md

~~~~text
| # TOOL-dRedressedBar-7 — acceptance ledger
| 
| **Serves:** journal TOOL-dRedressedBar-7
| 
| Written by TOOL-dRedressedBar-27 on 2026-10-15, after the unit closed with no ledger, from what its
| builder recorded. Nothing was re-run for it. The unit was built against spec 7 rev-4 in the one
| pass commit `671f25c71`. Spec 7's rev-5 rewords AC4 to name every unit ordered before this one and
| says "this unit's ledger still answers it", because the kit set AC4 derives from its own `epoch`
| run is unchanged; the reading below is that run's. The readings are the builder's, from that
| commit's body and from its return in `2026-10-14-build-TOOL-dRedressedBar-1-2-agent-returns.md`,
| under the heading `2026-10-14T17:30:21 · gov-builder · wf_7000bf13-341/a41438c689c4a68eb` at line
| 5035. No merge bar, no self-test suite and no gate leg ran in the build pass. Every reading is a
| direct probe, and the section 7 legs were owed to the close.
| 
| **Evidences:** TOOL-dRedressedBar-7
| - AC1 — `memory/gotchas/INDEX.md` — its diff from the base adds exactly the two class rows S1
|   names, with the count line. Its freshness was read through `regen.py --check`, which declares
|   the index and read `12 declared · 12 fresh · 0 stale`. The record names no separate run of
|   `gotchas.py --check`.
| - AC2 — `0 stale` — `regen.py --check` read `12 declared · 12 fresh · 0 stale` and exited 0. The
|   baseline before the pass read `12 declared · 11 fresh · 1 stale`, naming the gotchas index.
| - AC3 — `memory/project/method-carriers.txt` — after the mint, the files that mention the method
|   and the registry differed by one path, `.claude/agents/gov-reuse-scout.md`. Its row now sits
|   between the gov-researcher and gov-skeptic rows, the two lists match, and the agent file holds no
|   `## M<n>` heading.
| - AC4 — `FAILED` — before any write, `govkit.py epoch --base ebce889c7` exited 1 with `FAILED` for
|   exactly five kits, agent-cap (1.38), branch-reconcile (1.4), playbook-render (1.28), roles (1.5)
|   and unattended (1.106), and read run-gates `clean`. At the tip the same command printed no
|   `FAILED` line and exited 0.
| - AC5 — `git grep -nF "gov:kit <kit>@<old>"` — partly met, as the builder reported it. The mint
|   printed `agent-cap · 1.38 -> 1.39`, `branch-reconcile · 1.4 -> 1.5`,
|   `playbook-render · 1.28 -> 1.29`, `roles · 1.5 -> 1.6` and `unattended · 1.106 -> 1.107`, each
|   value moving by its last component. Over the whole tree at the tip, the literal probe printed two
|   lines, both in `memory/builds/aOrientedCast/`: line 35 of the TOOL-aOrientedCast-27 acceptance
|   ledger and line 11 of the TOOL-aOrientedCast-25 fold brief. Both quote old markers in prose and
|   were already tracked at `ebce889c7`, so neither is a carrier. Outside `memory/builds/` it printed
|   nothing for all five kits.
| - AC6 — `memory/guides/SESSION-KICKOFF.md` — the probe over its watch list printed nothing: no
|   watched path moved in `ebce889c7..HEAD` or in the pass commit, so no stamp was written.
| - AC7 — `render_playbook.py` — `git diff -U0 HEAD~1 HEAD` over it changed line 1839 only, and lines
|   1397 and 1646 both read `v3.5`. The commit's changed files fall only in the categories AC7 allows.
~~~~

### ledgers/2026-10-15-build-TOOL-dRedressedBar-9-1-acceptance-ledger.md

~~~~text
| # TOOL-dRedressedBar-9 — acceptance ledger
| 
| **Serves:** journal TOOL-dRedressedBar-9
| 
| Written by TOOL-dRedressedBar-27 on 2026-10-15, after the unit closed with no ledger, from what its
| builder recorded. Nothing was re-run for it. The unit was built against spec 9 rev-4 in the one
| pass commit `59f11096a`. Spec 9's rev-5, rev-6 and rev-7 are records fixes that move no criterion,
| so the readings answer the criteria as they stand. The readings are the builder's, from that
| commit's body and from its return in `2026-10-14-build-TOOL-dRedressedBar-1-2-agent-returns.md`,
| under the heading `2026-10-14T14:39:35 · gov-builder · wf_df00997e-69f/aeeca0787c1024036` at line
| 4681. The probes ran on scratch targets under `%TEMP%/p9fx`. No merge bar, no self-test suite and
| no gate leg ran in the build pass, and the section 7 legs were owed to the close.
| 
| **Evidences:** TOOL-dRedressedBar-9
| - AC1 — `[[outcome]]` — the grep over `tools/govkit/entries/settings-merge.kit.toml` showed the one
|   block: code 2, `must_exist` `{prefix}/settings-merge.py`, `must_not_exist`
|   `{prefix}/hooks/agent-cap.js`, `means = "no-agent-cap-to-wire"` and `ok = true`. The diff of the
|   four files that must not move was empty against `ebce889c`.
| - AC2 — `no declared outcome accepts that` — before the block, on `a50d04eb`, the narrow update
|   exited 1 with that line, and `gov_commit` stayed at `24f39915`. With the block it exited 0,
|   printed `adopter exit 2 — no-agent-cap-to-wire` and `check-wiring.fragment.json wired`,
|   re-stamped at HEAD, and the receipt claimed check-wiring, run-gates and settings-merge.
| - AC3 — `[accepted stop]` — `apply --kits settings-merge` went from exit 1 to exit 0 with that
|   mark, and no `settings.json` was created.
| - AC4 — `must_not_exist` — the engine read the three exit-2 states as ACCEPTED, REFUSED and
|   REFUSED. With `must_not_exist` dropped, held in memory and not written, the both-present state
|   read ACCEPTED.
| - AC5 — `missing` — the dirty-README shape and the committed-deletion shape both exited 0, and the
|   deletion printed `missing`. The builder did not re-run them over the old descriptor, and wrote
|   that the red half "was observed when the spec was written".
| - AC6 — `agent-cap.js` — the full install still printed adopter exit 0 for both kits, never
|   printed the stop, and wired `agent-cap.js`.
| - AC7 — `check_outcome_states` — `symbols.json` lists it for `tools/govkit/matrix.py`, and
|   `gen_map.py --check` exited 0. The return lists `matrix.py` and `symbols.json` among the pass
|   commit's paths, and the commit body says `gen_map.py --write` run alone moved only
|   `symbols.json`. The record names no reading of the `3d1adca9` map.
~~~~

