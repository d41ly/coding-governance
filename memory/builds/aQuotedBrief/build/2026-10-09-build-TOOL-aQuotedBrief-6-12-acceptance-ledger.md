# TOOL-aQuotedBrief-6 — acceptance ledger

**Serves:** journal TOOL-aQuotedBrief-6

Node a, 2026-10-09. No suite and no bar ran in this pass. The host was saturated by other sessions'
pooled suites and full bars: a slice of the suite's prologue plus ONE `--preflight` did not return
inside its 580 s bound, four times, run alone and three at a time. So the new arms in
`unattended.test.sh`'s region three were NOT run as fixtures here. Each criterion was observed instead
by a DIRECT check on the function it changes, extracted from three drivers: this pass's, the pre-pass
driver (the HEAD blob) and copies of this pass's driver with a staged break. The temp copies and
scripts were deleted before the commit. The arms themselves are owed to the main loop's bar (shard 3),
which runs once after every unit is terminal.

**Evidences:** TOOL-aQuotedBrief-6
- AC1 — `verb_preflight` now reads `[ -z "$_pf_first" ] || check_prompt_brief`, the gate `check_branch_carried` uses on the next line, so a re-`--preflight` does not grade the join; the arm expecting `preflight OK` after a grown roster is owed to the bar (the slice running it exceeded its bound)
- AC2 — `grep -n "^PROMPT_BRIEF_CUTOFF=" .unattended.conf` printed `495:PROMPT_BRIEF_CUTOFF="2026-10-10"`
- AC3 — `read_brief_items` over an item reading `[stale]` printed kind `none` for item 2, which the `--preflight` join refuses at rule 1, and `[parked]` likewise; `[stale it is true]` still printed `stale` (direct; red on the pre-pass driver, which printed `stale` and `parked` for the bare forms)
- AC4 — `read_brief_items` over `### Items` holding `1. U. [planned A-x-1]` and `- The docs.` printed `- none - The docs.` for the second line, which the `--preflight` join refuses at rule 1 naming the line (direct; red on the pre-pass driver, which printed only item 1)
- AC5 — over a repository holding `2026-10-09-prompt-mandaté.md`, the listing as this driver spells it twice (`-c core.quotepath=off`) printed the name raw and `git show` read the record, so `--preflight` grades it (direct; red on the pre-pass listing, which printed the C-quoted name and the read failed, the record skipped)
- AC6 — against a run-state file whose only park names `brief item 2:` with ` · item brief item 1:` in its reason, the `--close` term-7 match this driver spells reported item 1 unmet, and a real `brief item 1:` park met it (direct; red on the pre-pass driver's `grep -qF`, which met item 1 from the reason)
- AC7 — the arms of S8 are written; their predicates were observed by direct checks: `check_prompt_brief`'s structural awk printed `rule 2`, `rule 3`, `rule 4`, `rule 1` and `rule 1` for the five broken records and nothing for the conforming one, and printed none of those with the five predicates staged out; `read_brief_items` printed `many` for two dispositions and `stale` with that reading staged out; the slice runs of the join-loop arm printing `rule 3, a roster unit no planned item names` and of the three close arms are owed to the bar
