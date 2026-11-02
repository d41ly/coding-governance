# dFoldedAudit — unit 1's carrier fold return

**Serves:** journal TOOL-dFoldedAudit-1

TOOL-dFoldedAudit-1 is authored at rev-5, dated 2026-11-02, and its status stays INPROGRESS. The full hygiene gate had not finished when I returned, and the lexicon was never reached, because they run in sequence in one background job. Nothing is committed and only this one spec changed.

**Changes in the spec**
- **S14 (new):** line 27 of the memory-tree README states unit 6's exemption as built, observed by AC14.
- **§4:** a new sub-head, `### The memory-tree README`, holds the exact row text, the code citations, and why no render, size row or new leg is owed. `tools/memory-tree/README.md` joins Files touched.
- **AC14 (new):** `sed -n 27p` piped to `grep -c`. `check_audit_fold`, `spec-audit`, `joins neither revision arm` and `still reported` must each print 1, and `§` must print 0.
- **§9:** a rev-5 line was added.
- **Unchanged:** §3's sentence on `coding-governance-agents.template.md` and `memory/HYGIENE.md`, and M4's target text and byte figures.

**Additions the brief did not list**
- The `TOOL-dFoldedAudit-6` edge in §3 now also says the README row states the exemption.
- §10's seam list gains the README row.
- The §4 sub-head is new, so the builder has exact text to write.

**Where S14 departs from the brief's wording**
- It says "revision-log entry", not "§9 entry", because `REV_LOG_HEAD` finds the log by heading at any ordinal, and S11 refuses a section number in new carrier text.
- It states the rule per commit, every revision the commit moved, because that is what `check_audit_fold` asks.
- It says "bound", because `tools/memory-tree/deviation_join.py:572` filters on that state.
- The row text also reports a material edit moving no header, which the code never treats as a fold.

**Checks**
- **Row text:** I applied the §4 text to an in-memory copy of line 27. The old clause matches exactly once, all five AC14 literals come out as specified, and the row's next sentence survives.
- **At HEAD:** the four required literals print 0, so AC14 is red today.
- **Hygiene gate:** the run did not finish within its 300-second timeout and is still running in the background, so I have no exit code yet.
- **Hygiene findings so far:** the output so far names this build only under check 9, as index drift. Check 9 lists this spec, the build's README, and the specs of units 4, 6 and 7. That is yours to clear with `gen_build_index.py --write`, because I regenerate nothing. Check 25's output has already printed with no finding on this spec. I could not tell whether check 12 has run; it has no finding here so far.
- **Lexicon:** it has not started, and this revision mints no names.

**File**
- `C:\projects\coding-governance\.claude\worktrees\gov-build-m4-spec-audit-694e7b\memory\builds\dFoldedAudit\spec\2026-11-01-spec-TOOL-dFoldedAudit-1.md`
