**Serves:** research TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73

# Round-7 fix pass — the spec writer's returns

The returns of the agent dispatched from `memory/builds/dWitnessedBar/prompts/2026-10-25-prompt-TOOL-dWitnessedBar-68-1-spec-writer.md`, run direct/a747764c8dd825f2c, one per stop, extracted from its transcript by script.

## Return 1

I cleared every finding in the round-7 fix brief in all six units, TOOL-dWitnessedBar-68 to TOOL-dWitnessedBar-73. Each was edited in place at rev-1, and nothing else changed: no other spec, no `order` verb, no deviation record, nothing staged or committed, no index regenerated.

**Checks:**
- `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` now prints no finding for units 68 to 73. It still prints five dWitnessedBar lines, but none is a finding: each is a "check 25 did not grade … READER NOT IN TREE covers it" notice on TOOL-dWitnessedBar-20 S2 and TOOL-dWitnessedBar-24 S14. Those were there before and are outside these units.
- My role doesn't allow running `tools/check-spec-tokens.py`, so I haven't run it. Instead I copied its `[path]` and `[bar]` rules into a scratch scan of the six specs' §6. That scan finds no untracked full path and no suite token the bar rule matches. The main loop's own run is still owed.

**Check 25: none of the flagged items retires a name, so all were reworded and none got a `**Readers:**` clause.** In each case the trigger word described a CR strip, a staged break or an assertion count, not a retirement. Function names, `rec_*` variables and keys all stay.
- **68 S3:** "the reader removes the CR" now reads "strips the CR". The CR strip on that line is a normalisation, not a retired name.
- **69 S1:** "one trailing CR is removed from the value" now reads "the value is stripped of one trailing CR". `read_green_file` and its seven `rec_*` variables stay. The `$(awk ...)` reads it swaps out are code, not names, and `git grep` finds them only in `.githooks/pre-push:1354-1368`. "In place of" stays, since check 25 doesn't trigger on it.
- **69 S2:** "removes one trailing `'\r'`" now reads "strips". This is the same normalisation as 69 S1.
- **70 S1:** "CR strip deleted by `sed`" now reads "a mutant … that lacks its CR strip, made by `sed …`". The mutant is a staged break.
- **70 S3:** "the CR strip deleted from `read_green_file`" now reads "a `read_green_file` that lacks its CR strip". This is also a staged break.
- **71 S3:** "`--ref-format=files` deleted from the fixture builder" now reads "a scratch copy whose fixture builder lacks `--ref-format=files`". This is a staged break.
- **72 S1:** "strip-deleted mutant" now reads "mutant, which lacks the CR strip". This is unit 70's staged break.
- **72 S3:** the staged break is now "a `read_green_file` that lacks its CR strip".
- **73 S13:** "`__pycache__` removed" now reads "cleared", which matches the wording AC13 already used. The three "drop" breaks are now named as the breaks that leave out `timeout=`, the prefix check and the sweep's `OSError` catch, the wording of unit 67's New-arm line.
- **73 S15:** "assertions replaced by one `rec_sha` compare" now reads "one `rec_sha` compare in place of … assertions". It describes how unit 66's assertion count changes, not a retirement.

**Spec-token fixes:**
- **[path]:**
  - **68 AC3 and 69 AC4:** these now cite `verdict_backends.py` by basename. 69 AC4's grep is told to run in `tools/run-gates/`, a trailing-slash directory that the path rule skips.
  - **73 AC5:** now reads "the `tools/lib/` copy of `legacy_ledger.py`".
  - **73 AC6:** now passes the file in as `sys.argv[1]`, with `tools/gate-legs.json` as the argument (a tracked file). I ran the rewritten command at HEAD and it prints the canary's guard list.
- **[bar]:**
  - **71 AC2:** now reads "section `2l` runs from a scratch copy with S1's exports deleted".
  - **73 AC1:** now reads "a scratch copy of section `2l`".
  - Both specs already name `tools/lib/resolve-python.test.sh` on a §7 `New arm:` line. The full path also stays in §2, §4 and Files touched.

**TOOL-dWitnessedBar-51 is 48741 bytes.** I did not edit it.

Files edited:
- C:\projects\coding-governance\.claude\worktrees\unattended-dwitnessedbar-d0e46e\memory\builds\dWitnessedBar\spec\2026-10-25-spec-TOOL-dWitnessedBar-68.md
- C:\projects\coding-governance\.claude\worktrees\unattended-dwitnessedbar-d0e46e\memory\builds\dWitnessedBar\spec\2026-10-25-spec-TOOL-dWitnessedBar-69.md
- C:\projects\coding-governance\.claude\worktrees\unattended-dwitnessedbar-d0e46e\memory\builds\dWitnessedBar\spec\2026-10-25-spec-TOOL-dWitnessedBar-70.md
- C:\projects\coding-governance\.claude\worktrees\unattended-dwitnessedbar-d0e46e\memory\builds\dWitnessedBar\spec\2026-10-25-spec-TOOL-dWitnessedBar-71.md
- C:\projects\coding-governance\.claude\worktrees\unattended-dwitnessedbar-d0e46e\memory\builds\dWitnessedBar\spec\2026-10-25-spec-TOOL-dWitnessedBar-72.md
- C:\projects\coding-governance\.claude\worktrees\unattended-dwitnessedbar-d0e46e\memory\builds\dWitnessedBar\spec\2026-10-25-spec-TOOL-dWitnessedBar-73.md

## Return 2

TOOL-dWitnessedBar-73's H1 is shortened, in place, with no rev bump and nothing staged. The line is now 189 characters (191 bytes, because the em dash takes three bytes), under your 200 limit:

### TOOL-dWitnessedBar-73 — the round-1 audit of units 66 and 67, its 23 minors batched: fixtures, populations, the hook guard, every key and filesystem call exercised, predicates and records

- **Line count:** the old H1 measured 323 characters, not the 325 in your message.
- **Shortened wording:** my first try kept "counting predicates and corrected records", but that line was 208 characters. I shortened the ending to "predicates and records", which still covers S12's count and the ledger corrections.
- **Index row:** I did not regenerate the build README index, so I have not seen the row's new rendered length or run check 7. Both happen when you commit.
- **Hygiene re-run:** `--only 2,12,25` still shows no finding for units 68 to 73.
- **Other specs:** only line 1 of the 73 spec changed, and no other spec's H1 was touched.

The earlier round-7 fixes stand as I reported them.

The file is C:\projects\coding-governance\.claude\worktrees\unattended-dwitnessedbar-d0e46e\memory\builds\dWitnessedBar\spec\2026-10-25-spec-TOOL-dWitnessedBar-73.md
