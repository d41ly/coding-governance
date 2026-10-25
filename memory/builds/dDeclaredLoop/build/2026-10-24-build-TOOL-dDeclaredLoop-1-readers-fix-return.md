**Serves:** research TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-29

# Readers-fix pass — the spec writer's return

The return of the agent dispatched from `memory/builds/dDeclaredLoop/prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-1-4-spec-writer.md`, run direct/ad69ae8e236175976, extracted from its transcript by script.

Check 25 now prints no dDeclaredLoop line. Re-running `bash tools/memory-tree/check-memory-hygiene.sh --only 25` shows none of the five specs and no "did not grade" notice for any dDeclaredLoop spec. The command still exits 1, though, because `--only 25` also runs check 12 (see the last section).

I edited five specs in place, with no rev bump, nothing staged and nothing committed. I touched no deviation record and no other spec, and did not run the index generator.

## What each hit got

**Added a `**Readers:**` clause** — these two really do retire something:

- **TOOL-dDeclaredLoop-21 S7.** The upgrade step deletes an adopter's `REVIEW_ROUNDS` conf line.
  - *by name:* the copies of this kit installed in an adopter's tree that read the line. That is `tools/unattended/unattended.sh` (:779, `read_bound_key`), `tools/unattended/check-unattended.sh` (:1859-1876, `read_rounds_of`), `tools/unattended/kit.toml` (:174, `optional_keys`) and `tools/unattended/.unattended.conf.example` (:118). S4 re-points all of them in this same unit, and the clause says the full list lives in S4. Gov's own line, `.unattended.conf` (:111), is handled by S9.
  - *by value:* the adopter's N, read by `verb_review`'s bound (`unattended.sh:12769`) and by check 19 through `read_rounds_of`. After S4 and S6, both read `review.design.round-count`.
  - I checked each cited line with `git grep -n` at HEAD.
- **TOOL-dDeclaredLoop-6 S1.** Six `kind` rows leave `tools/playbook/core-pending.txt`.
  - *by name:* `READER NOT IN TREE`. That file and its only reader, the meta-check in `core.py`, come from PLAY-dOrderedCharter-7, which is DEFERRED at rev-3. Neither file exists at HEAD, which I confirmed with `git grep`.
  - *by value:* `NO VALUE READERS`. A pending row's value is its arming build, and the meta-check only prints it in a count. The six kind names stay in the register.
  - I left the by-name names unbackticked so the escape wouldn't print two "did not grade" notices.

**Reworded** — these four retire nothing; the trigger was firing on wording:

- **TOOL-dDeclaredLoop-4 S3.** "a `[[hook]]` row for a removed hook" is just an example of a stale claim. It now reads "a `[[hook]]` row naming a hook the tree no longer holds".
- **TOOL-dDeclaredLoop-25 S6.** "a removed stage tag" is the gate's red case. It now reads "the successor of each stage tag that leaves the composition, so a stage tag gone from it with no change record reds the gate".
- **TOOL-dDeclaredLoop-29 S1.** The literal `widens = "remove"` was firing the trigger. S1 now points at the direction unit 24's §4 table gives `needs` ("widening as it shrinks"). That table row holds the literal, so a builder still finds it there.
- **TOOL-dDeclaredLoop-29 S6.** `dropped` is a name the join gives an unanswered row. It is not a retirement, and it mirrors the clause's "drops a row", so I kept it. The trigger also needs an identifier-shaped token, so I replaced the path with "in S4's module" (S4 already names `tools/loop/upstream.py`) and added "classing each handed row by its answer". The meaning is unchanged, but this fix works by removing the trigger's second condition rather than the wording that reads as a retirement.

## Outside this brief (not fixed)

- **Check 12 still fails.** It flags TOOL-dDeclaredLoop-26, whose §3 says it consumes from TOOL-dDeclaredLoop-7, while unit 7 declares no matching hands-off back to 26. Neither spec was in my brief, so I left both alone. This is why the command exits 1.
- **S4 of TOOL-dDeclaredLoop-21 misses one reader.** Its readers list leaves out `tools/unattended/runlog-writer.test.sh`, which spells `REVIEW_ROUNDS` at :388 and :396. S3 lists that file only for `RUNAWAY_CEILING`. Check 25 can't see the gap because it never grades a list for completeness. It needs an S4 edit, which the brief didn't allow.

Files edited:
- C:\projects\coding-governance\.claude\worktrees\unattended-declared-loop-82e374\memory\builds\dDeclaredLoop\spec\2026-10-24-spec-TOOL-dDeclaredLoop-21.md
- C:\projects\coding-governance\.claude\worktrees\unattended-declared-loop-82e374\memory\builds\dDeclaredLoop\spec\2026-10-24-spec-TOOL-dDeclaredLoop-6.md
- C:\projects\coding-governance\.claude\worktrees\unattended-declared-loop-82e374\memory\builds\dDeclaredLoop\spec\2026-10-24-spec-TOOL-dDeclaredLoop-4.md
- C:\projects\coding-governance\.claude\worktrees\unattended-declared-loop-82e374\memory\builds\dDeclaredLoop\spec\2026-10-24-spec-TOOL-dDeclaredLoop-25.md
- C:\projects\coding-governance\.claude\worktrees\unattended-declared-loop-82e374\memory\builds\dDeclaredLoop\spec\2026-10-24-spec-TOOL-dDeclaredLoop-29.md
