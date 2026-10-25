**Serves:** research TOOL-dWitnessedBar-63

# Round-4 fix pass — the spec writer's return

The returns of the agent dispatched from `memory/builds/dWitnessedBar/prompts/2026-10-25-prompt-TOOL-dWitnessedBar-63-1-spec-writer.md`, run direct/a2c8c18ec142d202a, one per stop, extracted from its transcript by script.

## Return 1

I cleared all four round-4 findings in TOOL-dWitnessedBar-63. I edited the spec in place at rev-1 and left it unstaged. `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` now exits 0 with no dWitnessedBar finding (before the edits it exited 1 on S13, S31 and S34). My role isn't allowed to run `python tools/check-spec-tokens.py`, so that check is still yours to run.

**Check 25: S13, S31 and S34 retire nothing, so I reworded each one.** None of them gets a `**Readers:**` clause. In each case a single verb tripped the check's retirement word list, and the meaning is unchanged:
- **S13:** "with `os.path.commonpath` replaced by one raising `ValueError`" now reads "with a stand-in for `os.path.commonpath` that raises `ValueError`". This describes a fake swapped in during the test, not a retired name.
- **S31:** "names post-merge's dropped knobs" now reads "names the knobs post-merge scrubs from the environment it inherits". `PM_SCRUB` is still there and is still read as a list (`tools/run-gates/post-merge.sh:35-43`).
- **S34:** "A second staged break removes `TOOL-dWitnessedBar-40`'s decline, and the arm reds on it" now reads "A second staged break, a scratch copy with `TOOL-dWitnessedBar-40`'s decline taken out, reds the arm". This is a test break on a scratch copy, not a retirement.

**Check-spec-tokens [bar]: the hit was AC20.** Its bare backticked token `run-gates.gov.test.sh` looks to the bar check like a run of the suite. AC20 was never observed by running that suite: it greps the comment above `_gknobs` in `tools/unattended/unattended.sh`. So I rewrote it as two greps over that file, `grep -n 'BAR_CLEARED_KNOBS' tools/unattended/unattended.sh` and `grep -n 'run-gates.gov.test.sh' tools/unattended/unattended.sh`, each naming that comment. A suite name inside a command that starts with grep doesn't count as a run. §7 needs no new `New arm:` line: the gov suite is already declared there for AC1 and AC2, and AC20 isn't a suite arm.

To check this I copied the checker's regex into a scratch probe and ran it over §6. The committed copy of the spec gives one hit, `run-gates.gov.test.sh`; the edited spec gives none.

I made no other changes: no other spec or deviation record, no rev bump, no staging, no commit, no index regeneration.

TOOL-dWitnessedBar-51 is **48631 bytes** (not edited).

Files:
- `C:\projects\coding-governance\.claude\worktrees\unattended-dwitnessedbar-d0e46e\memory\builds\dWitnessedBar\spec\2026-10-25-spec-TOOL-dWitnessedBar-63.md` (edited)
- `C:\projects\coding-governance\.claude\worktrees\unattended-dwitnessedbar-d0e46e\memory\builds\dWitnessedBar\spec\2026-10-25-spec-TOOL-dWitnessedBar-51.md` (byte count only)
