# TOOL-aQuotedBrief-3 — acceptance ledger

**Serves:** journal TOOL-aQuotedBrief-3

Node a, 2026-10-09. No suite and no bar ran in this pass. The new arms in `unattended.test.sh`'s
region three, after the carried-branch arms, were run as SLICES: the suite's prologue plus the arms,
in temp scripts under the kit directory, deleted before the commit. Against this pass's driver the
preflight slice printed `PASS (36 assertions)` (20 prologue, 16 new) and the close slice
`PASS (32 assertions)` (20 prologue, 12 new). Against the pre-pass driver (the HEAD blob) the
preflight arms printed 9 FAIL lines across AC1, AC2 and AC3, and the close slice 3 FAIL lines: AC4's
two and AC5's WONTDO-successor arm. AC5's CLOSED-successor arm, which the pre-pass driver passes by
having no term, printed its one FAIL line against a copy of this pass's driver with the chain walk
staged out (`nsup=0`).

**Evidences:** TOOL-aQuotedBrief-3
- AC1 — `--preflight tBr` over a prompt record whose item 2 is `2. The docs.` printed check 115 ending `rule 1, not exactly one disposition among planned, stale, duplicate and parked: item 2`, no `preflight OK`, and wrote no `RUN.md` (slice, red on the pre-pass driver, which admitted it)
- AC2 — `--preflight` over `[planned ARCH-tBr-9]` against a roster holding only `ARCH-tBr-1` printed `rule 2, a planned unit the authored roster does not carry, ARCH-tBr-9: item 1`; a brief whose only item is `stale` printed `rule 3, a roster unit no planned item names: ARCH-tBr-1` (slice, both red on the pre-pass driver)
- AC3 — item 2 `[duplicate 3]` beside item 3 `[stale ...]` printed `rule 4, a duplicate of item 3, which is not planned: item 2` (slice, red on the pre-pass driver)
- AC4 — `--close tRun`, prompt mode past the cutoff, item 1 planning `ARCH-tRun-1` ended WONTDO, printed `· item 1 planned, and not CLOSED: ARCH-tRun-1, with no parked line naming brief item 1:` and no `close OK`; after `--park tRun --item "brief item 1: the unit"` the term-7 message was gone (slice, red on the pre-pass driver, which closed OK)
- AC5 — the `--rescope --act supersede --successor` chain: `--rescope --act supersede --item ARCH-tRun-1 --successor ARCH-tRun-2` with the successor CLOSED printed no term-7 message; with it WONTDO it printed `not CLOSED: ARCH-tRun-2` (slice; the WONTDO arm red on the pre-pass driver, the CLOSED arm red with the chain walk staged out)
- AC6 — `grep -n "\[planned" memory/guides/UNATTENDED-VERBS.md` hit line 575, inside the prompt path's step 3, showing `[planned <unit-id> ...]` `(step 1 decides all four)` `[stale <evidence>]` `[duplicate <n>]` `[parked <reason>]`; step 1 says to decide every brief item's disposition there, and `adopt-unattended.sh --check` printed `in sync`
- AC7 — `--close` over a prompt-mode build whose README (opened 2026-08-01) predates the fixture's `PROMPT_BRIEF_CUTOFF="2099-01-01"` and a slug-mode build, each with its unit WONTDO, printed `close OK` and no term-7 message (slice; the same verdict as the pre-pass driver)
