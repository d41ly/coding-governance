**Serves:** research TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65

# Round-5 fix pass — the spec writer's return

The returns of the agent dispatched from `memory/builds/dWitnessedBar/prompts/2026-10-25-prompt-TOOL-dWitnessedBar-64-1-spec-writer.md`, run direct/a315ab26ba071d734, one per stop, extracted from its transcript by script.

## Return 1

I've fixed all three path hits in units 64 and 65. In each, a §6 criterion now names the untracked file by its basename, and the command that reads it runs inside the file's directory. Nothing else changed: no rev bump, no other spec or deviation record touched, nothing staged or committed, and no index regenerated.

- **TOOL-dWitnessedBar-64**, AC3: the probe now reads "a scratch copy of `legacy_ledger.py`, taken from `tools/lib/`". The full path is still in §4 and Files touched (lines 119-121).
- **TOOL-dWitnessedBar-65**, AC15: both greps now read `grep -n 'TAIL_GRACE_S' verdict_backends.py` and `grep -nE 'another kit' verdict_backends.py`, each "run in `tools/run-gates/`". A path ending in `/` is never graded as a path. The full path is still in §2 S21 (line 130) and Files touched (line 222).

**Checks.** I didn't run `tools/check-spec-tokens.py`, because my role allows only the hygiene gate and the lexicon. Instead I checked by hand: every backticked path-shaped token in either unit's §6 is now tracked by `git ls-files`. I couldn't fully confirm that the checker accepts a bare `verdict_backends.py`. It does grade bare file names on a root install. But `legacy_ledger.py`, which is just as untracked, already appeared bare in 64's AC1 and 65's AC6/AC7 and wasn't flagged. So the bare form shouldn't produce a new hit. The main loop's run of the checker will confirm it.
- `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` exited 0 and printed no line for unit 64 or 65.
- `python tools/lexicon/lexicon.py` exited 0 ("lexicon OK") and printed no line for unit 64 or 65.

**Byte count:** TOOL-dWitnessedBar-51 is 48653 bytes. I didn't edit it.

Files changed:
- C:\projects\coding-governance\.claude\worktrees\unattended-dwitnessedbar-d0e46e\memory\builds\dWitnessedBar\spec\2026-10-25-spec-TOOL-dWitnessedBar-64.md
- C:\projects\coding-governance\.claude\worktrees\unattended-dwitnessedbar-d0e46e\memory\builds\dWitnessedBar\spec\2026-10-25-spec-TOOL-dWitnessedBar-65.md
