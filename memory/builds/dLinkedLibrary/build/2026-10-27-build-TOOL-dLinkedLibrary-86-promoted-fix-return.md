**Serves:** research TOOL-dLinkedLibrary-86

# The round-5 promoted-fix pass's return — dLinkedLibrary

The spec writer's final return, extracted from its transcript by script, never retyped.

I fixed all four findings in `TOOL-dLinkedLibrary-86`, and the hygiene run (checks 2, 12, 13 and 25) now exits 0 without naming the spec. The first run, before the edits, named it for AC7 and for S19 and S20, matching the brief. I edited the spec in place, with no rev bump, no §9 line and no commit.

1. **Check 12, AC7 had no witness.** AC7 now names its command, `python adopt_program.py --fixture --plant ci-census` running `adopt census`. Its output witness is the `refused:` line that each job of each refusing tree prints.
2. **Check 25, S19.** I reworded it rather than adding a Readers clause, because it retires nothing named. The only thing it took away was a possible duplicate call, which nothing reads by name. S19 now says `tools/memory-tree/gotchas.py` holds exactly one `resolve_bash` call, the one inside `resolve_observed_argv`. This is the same condition AC17 counts with `ast`, and no retirement word remains.
3. **Check 25, S20.** S20 does retire something: one half of 80 AC1, the "lists no file under `memory/`" check. So I added a Readers clause:
   - **By name:** `2026-10-27-spec-TOOL-dLinkedLibrary-80.md` (AC1) and `2026-10-27-review-TOOL-dLinkedLibrary-75-spec-audit.md` (L1). Apart from this spec, these are the only files a `git grep` for the phrase finds. I cited both by basename because check 25 accepts a tracked file named by the end of its path, and both are in the index.
   - **By value:** `NO VALUE READERS`, on one line, with the reason. No code, gate or fixture reads that half, and 80's acceptance ledger is not written until 80's pass.
4. **check-spec-tokens, the untracked interpreter path in AC14.** That case now reads "a `comm` of `python3.12` against an absolute executable path whose basename is `python3.12` matches", so no path appears in §6.

The edited file is `C:\projects\coding-governance\.claude\worktrees\unattended-dlinkedlibrary-4f9fd9\memory\builds\dLinkedLibrary\spec\2026-10-27-spec-TOOL-dLinkedLibrary-86.md`.
