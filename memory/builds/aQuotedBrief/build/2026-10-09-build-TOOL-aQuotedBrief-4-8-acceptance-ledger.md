# TOOL-aQuotedBrief-4 — acceptance ledger

**Serves:** journal TOOL-aQuotedBrief-4

Node a, 2026-10-09. No suite and no bar ran in this pass. The arms in `unattended.test.sh`'s region
three were run as SLICES: the suite's prologue, the region's epoch setup and the arms, in temp scripts
under the kit directory, deleted before the commit. Against this pass's driver the unit 1 block printed
`PASS (53 assertions)`, and the unit 3 block, cut into five slices to fit the command bound, printed
`PASS` on each (36, 26, 23, 25 and 25 assertions, each counting the prologue's 20 and its own setup).
Against the pre-pass driver (the HEAD blob) the new preflight arms printed 3 FAIL lines and the new
close arms 3.

**Evidences:** TOOL-aQuotedBrief-4
- AC1 — `--preflight tBr` over a default branch declaring `PROMPT_BRIEF_CUTOFF="2026-07-01"`, with `PROMPT_BRIEF_CUTOFF=""` committed on the run branch, printed `first rule failed, then the record: rule 1` and no NOTE (slice; red on the pre-pass driver, which printed the NOTE and graded nothing)
- AC2 — `--close`, run as `--close tRun` after `PROMPT_BRIEF_CUTOFF=""` was committed past preflight, with the planned unit WONTDO, printed `item 1 planned, and not CLOSED: ARCH-tRun-1` and no `close OK` (slice; red on the pre-pass driver, which closed OK)
- AC3 — `--close tRun` over a default branch whose conf leaves the key blank printed `close OK` and the `build-complete` note naming `PROMPT_BRIEF_CUTOFF` as OFF (slice; red on the pre-pass driver, which was silent)
- AC4 — `--preflight tBr` over a default-branch conf ending in `return` printed `UNATTENDED check 116 FAILED` and no `preflight OK` (slice; red on the pre-pass driver, which read the working copy's grandfathering date)
- AC5 — `grep -c "PROMPT_BRIEF_CUTOFF" tools/unattended/unattended.test.sh`'s prompt-record arms now commit the cutoff on the fixture's main through `write_default_conf` or `build_brief_run`, and every one passed in the slice of its block, the grandfathered and blank arms included
