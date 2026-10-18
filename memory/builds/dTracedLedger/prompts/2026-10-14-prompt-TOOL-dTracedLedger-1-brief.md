# Brief — dTracedLedger: check 23's reds at origin/main traced and routed to their owners

**Serves:** research TOOL-dTracedLedger-1

## The prompt

> FINDING (measured 2026-10-14 by session 1799cb98, build dClosedLoop, recorded in memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-research-maintain.md, instrument 4): in a detached worktree at origin/main ebce889c7d7104fe4811707d6f17b2a486bf0fd6, `bash tools/memory-tree/check-memory-hygiene.sh` exits 1 with two check 23 failures: [the two failure lines and their row lists]. LEDGER_LABEL_CUTOFF and LEDGER_TOKEN_CUTOFF are both 2026-09-08 in .memory-tree.conf. The rule is memory/HYGIENE.md "Acceptance ledger".
>
> DO:
> - Reproduce at the current origin/main in a detached worktree under a short %TEMP% path (MAX_PATH), never in the primary tree.
> - Find why the merge bar did not catch it: is the `memory hygiene` leg guarded, was the push scoped, or did the records land after the last full bar? `GATE_ATTRIBUTE` and `.githooks/pre-push`'s scoped-versus-full decision are the probes.
> - Check who owns the lines: aSparedSpawn has a held unattended claim by node a (`git ls-remote origin 'refs/gov/runs/*'`). If that build is live, file the fix as an ask in memory/builds/aSparedSpawn/BACKLOG.md rather than editing another node's live records; otherwise fix the journal records' ledger lines to the legal forms.
> - Do not merge to main or push without the owner's explicit ask.

## The brief

### Goal
Record why 37 check-23 rows reached origin/main `ebce889c7` past the merge bar, and hand each row's
fix to the build that owns it as an ask, editing no other build's records.

### Items
1. Reproduce the failure at origin/main in a detached worktree under `%TEMP%`.
2. Establish why the bar did not stop it: guard, scope, or landing after the last full bar.
3. Establish who owns the rows and whether their builds are live.
4. File the fixes as asks for the owners, with the evidence and an instrument recorded.

### Acceptance
The research record states the reproduction, the bisect landing for every row, the attribution
against the remote tip the push went over, and each owner's run state. The asks name every row,
classed. `git diff ebce889c7..HEAD` touches no path under aSparedSpawn's or aOrientedCast's
`spec/` or `build/`.

### Gates
`memory hygiene` (red at BASE on check 17 and the 37 check-23 rows; this build adds none),
`build README slot contract`, `kickoff-manifest ratchet`, `line length`.

### Non-goals
No edit to another build's spec or ledger; no `tools/` change; no merge to main; no push.

### Limitations
aSparedSpawn and aOrientedCast are HELD runs of node `a`. An ask lives only in its own slug's
folder (`tools/memory-tree/README.md`, row kinds), so the asks are filed in this build's
`BACKLOG.md` with pointers to the owners. The push's own run-log line is on node `a`.

### Reuse
The ask rows follow the grammar in `tools/memory-tree/README.md`; the build opens as `f079464e2`
opened dRedressedBar. Recall returned TOOL-aHoistedPass-39, a check-23 ask filed by its own build.

## Drawn from the session

> If that build is live, file the fix as an ask in memory/builds/aSparedSpawn/BACKLOG.md rather than editing another node's live records
— owner, the opening message

## Owner confirmation

Asked: Ready — say go and I'll start, or adjust any field.
Answer: go
