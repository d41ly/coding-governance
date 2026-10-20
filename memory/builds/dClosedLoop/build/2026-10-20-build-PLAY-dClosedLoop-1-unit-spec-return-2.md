# Return: the unit spec's writer, resumed to fix check 12's phantom label

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 233's return, verbatim, except that a title line would be demoted to keep one H1 per record.
Its question is in `prompts/2026-10-20-prompt-PLAY-dClosedLoop-1-60-spec-writer.md`.

---

I rewrote the §6 intro paragraph, which was the only line in the spec that began with `AC` and a digit, so check 12 should no longer open a phantom AC1 there. I ran no gate, so the main loop still needs to re-run memory hygiene.

The paragraph is lines 104-106 of `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\builds\dClosedLoop\spec\2026-10-20-spec-PLAY-dClosedLoop-1.md`. It keeps the same meaning.

Before:
```
AC1 to AC4 are the kickoff's acceptance check, (a) to (d). AC5 is the baseline taken, and AC6 to AC12 are Phase 0's
acceptance as the execution plan states it. Each criterion cites the record that shows it DONE or OPEN. Every probe
named below ran at `72b65c083` on 2026-10-20.
```

After:
```
The kickoff's acceptance check, (a) to (d), is criteria AC1 to AC4. The baseline taken is AC5, and Phase 0's
acceptance as the execution plan states it is AC6 to AC12. Each criterion cites the record that shows it DONE or
OPEN. Every probe named below ran at `72b65c083` on 2026-10-20.
```

I then searched the whole spec for any line starting with `AC` and a digit, with or without leading whitespace or `**`. Nothing matched. The only lines that still carry a criterion label at the start are the twelve criteria bullets (lines 108-176), each of which has its `Red when:` clause.

Nothing else in the file changed. The generated spec-records region at lines 5-9 is as the build index generator wrote it.
