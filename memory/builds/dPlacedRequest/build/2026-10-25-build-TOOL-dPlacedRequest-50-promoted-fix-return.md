**Serves:** research TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52

# The promoted-fix pass — dPlacedRequest round 4, its return

The return of the gov-spec-writer dispatched from `memory/builds/dPlacedRequest/prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-9-spec-writer.md`, run direct/a65f76e434521cf17, extracted from its transcript by script.

All three hits are fixed, and spec 34 is now **47040 bytes**, under the 47104 target. `check-memory-hygiene.sh --only 2,12,25` exits 0 over the staged specs. I didn't run `check-spec-tokens.py`; the main loop runs it, so the `[path]` and `[size]` fixes are confirmed only by the cause each message names and by `wc -c`.

**Hit dispositions:**

- **[path] on TOOL-dPlacedRequest-52:** fixed. AC7 now names the file by its basename, `gov-feed.sh`, as "the file `TOOL-dPlacedRequest-13` creates" (unit 13 S1 creates it). The full path stays where it is allowed, in S7's prose and in §4's Files touched.
- **[size] on TOOL-dPlacedRequest-34:** fixed, 49387 down to 47040 bytes. I tightened prose and dropped repetition only:
  - Three citations that §4 Evidence already holds (S30's two, S39's one) now point at §4.
  - S14's exit codes now point at §4's offline table, and S57 now points at §4's deletion record.
  - The code block in §4 "The bounded walk (S43)" became one sentence; the heading is kept because unit 35 cites it.
  - The §9 entries for rev-1 to rev-6 are shorter.
  - "The full bar runs once, at the close." was dropped from §7 as a restatement.
  - All 59 items, 59 criteria, 32 edges, 4 forks, 5 **Readers:** clauses, 40 Files-touched paths, the §7 leg line and the `New arm:` lines are unchanged in count. A diff of the backticked tokens before and after loses only those moved citations, a `git grep` mention that AC13 still runs, and the code fence.
- **Check 12, failure mode, on TOOL-dPlacedRequest-52 AC22:** fixed. The red case now sits on one line: `Red when: the second pass's walk lost the first pass's stop.`

**Your decision:** spec 34 has only 64 bytes of headroom. The next records render will probably add rows for the round-4 promoted fix brief and its fix return (both serve unit 34), about 200 bytes each. That would put the spec near 47.4 KB. It stays well under the 49152 ceiling and under the 48128 that unit 52 S9 sets as unit 43 AC22's bound, but above the 47104 that unit 43 AC22 checks at its current wording. Getting another 400 bytes out without dropping content would mean cutting edge descriptions or the §4 records that unit 43 S22 already plans to move into a research record at its own pass. Say if you want that done now.

**Revisions:** spec 34 is at rev-7 and spec 52 at rev-2, each with its §9 line. I staged both specs so the hygiene gate would read them; nothing is committed or rendered.

Edited files:
- C:\projects\coding-governance\.claude\worktrees\unattended-dplacedrequest-f41432\memory\builds\dPlacedRequest\spec\2026-10-25-spec-TOOL-dPlacedRequest-34.md
- C:\projects\coding-governance\.claude\worktrees\unattended-dplacedrequest-f41432\memory\builds\dPlacedRequest\spec\2026-10-25-spec-TOOL-dPlacedRequest-52.md
