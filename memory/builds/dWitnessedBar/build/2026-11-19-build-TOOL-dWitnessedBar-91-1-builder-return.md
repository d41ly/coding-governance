**Serves:** journal TOOL-dWitnessedBar-91

# TOOL-dWitnessedBar-91 — builder return 1 (run `wf_07b2835e-57d`), committed b7e2e3d8d

## Why

The rev-3 spec held when I checked it against the tree at f8a905a4b. The unedited built .githooks/pre-push printed 2 for grep -c 'rec_sha="', 0 for the anchored grep -c 'sha)[[:space:]]*rec_sha="', 1 for the read_green_file cut piped to grep -o 'sha)' | wc -l, and 2 for grep -c 'rec_sha=""'. grep -n 'sha)' named two arms, one in #read_green_file and one in #read_bar_file. All of that matches spec section 4. The unit writes records only, so I built it as written and found no divergence.

## Summary

I committed TOOL-dWitnessedBar-91 as b7e2e3d8d. It is a records-only pass: no code file changed and no function was added.

**What the commit holds:**
- A new acceptance ledger, C:/projects/coding-governance/.claude/worktrees/unattended-dwitnessedbar-2ed3b3/memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-91-1-acceptance-ledger.md, with one line per criterion, each on one physical line.
  - The AC1 line opens with the token `sha)` and records the four counts I read over the unedited built hook (2, 0, 1 and 2, pinned 2026-11-21). It marks the counts in the two clones as owed.
  - The AC2 line opens with the token `sha)[[:space:]]*rec_sha="` and marks as owed the note labelled `TOOL-dWitnessedBar-91 S2` in unit 90's ledger.
- The spec's status header changed from INPROGRESS to CLOSED (date 2026-11-21, already today), with no other hand edit to the spec. The generator also added the ledger's row to the spec's records list.
- `gen_build_index.py --write` rewrote three other files, all committed: memory/LIVE.md, memory/backlog/TOOL.md and memory/builds/dWitnessedBar/README.md.
- memory/builds/dWitnessedBar/RUN.md, with the dispatch row the main loop had staged.
- Trailers: `Decided:`, `Pass: TOOL-dWitnessedBar-91` and `Co-Authored-By:`.

**What the regeneration changed:** with unit 91 closed, the build rolls up as DEFERRED in LIVE.md and the build README. In the backlog, ask TOOL-dWitnessedBar-31 now reads DEFERRED and points at TOOL-dWitnessedBar-28, the unit deferred against asks 101 to 103. Unit 92 is still DEFERRED and has to be moved forward by the main loop.

**Checks that ran:** the probe of the unedited hook above. It stands in for nothing a gate checks; it confirms the spec's grounding and the reset figure that AC1 derives. The commit hook ran memory hygiene over the staged files and passed; the full `memory hygiene` leg is the bar's at the close. I ran `gotchas.py --for-diff HEAD~1..HEAD` and went through what it listed. The only classes these records could hit are a ledger token wrapped across lines, an inline fence, a pipe inside a table cell, and a record missing its Serves line, and none applies. No gate, suite or bar ran.

**Owed to the main loop at the close:**
- AC1: the three counts in each of unit 90 AC2's two quoted-arm clones (`rec_sha="$_rg_v"` and `rec_sha="${_rg_v}"`) under %TEMP%/<short-name>. The reset count is re-read from the unedited built hook at that time.
- AC2: write S2's note as a continuation line under the `- AC2` answer in 2026-11-19-build-TOOL-dWitnessedBar-90-1-acceptance-ledger.md. Then run the AC2 awk selector, which must print exactly one line opening `- AC2 `.
- Section 7's `memory hygiene`, `recall floor` and `recall floor arms` legs. The unit adds no new arm, so it owes no RED-first observation.

No command timed out, so nothing was skipped. The changes to help/reference/drive.md and help/reference/units.md were already in the working tree before I started; I left them unstaged.
