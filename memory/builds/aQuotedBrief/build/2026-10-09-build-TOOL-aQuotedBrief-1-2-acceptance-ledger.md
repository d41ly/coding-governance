# TOOL-aQuotedBrief-1 — acceptance ledger

**Serves:** journal TOOL-aQuotedBrief-1

Node a, 2026-10-09. No suite and no bar ran in this pass. The arms in `unattended.test.sh`'s region
three, beside check 89's, were run as a SLICE: the suite's prologue plus the new block, in a temp
script under the kit directory, deleted before the commit. Run against the pre-pass driver (the
HEAD blob copied beside the kit) it printed 8 FAIL lines over 44 executed assertions: the AC1, AC3,
AC5 and AC6 blank-key arms red. Run against this pass's driver it printed `SLICE PASS (44)`. AC4,
AC6's grandfather arm and AC7 are admit or as-today cases, green on both drivers by construction.

**Evidences:** TOOL-aQuotedBrief-1
- AC1 — `--preflight` over a bare `## The prompt` record with `PROMPT_BRIEF_CUTOFF="2026-07-01"` printed check 112 naming `rule 1` and the record, no `preflight OK`, and no `RUN.md` (slice, red on the pre-pass driver)
- AC2 — `grep -n "Drawn from the session" memory/guides/UNATTENDED-VERBS.md` hit line 541, step 2's mandatory confirmation, and line 562, inside step 3, which lists `## The brief`, `## Drawn from the session` and `## Owner confirmation` in that order; the render is byte-identical to the template
- AC3 — `--preflight` over a record quoting the session whose `## Owner confirmation` reads not asked printed `first rule failed, then the record: rule 5` (slice, red on the pre-pass driver)
- AC4 — `--preflight` over a conforming record with `## Drawn from the session` reading `none` printed `preflight OK` and no check 112 (slice)
- AC5 — `--preflight` over a prompt-mode build with no `## The prompt` record printed check 113 naming the empty population and wrote no `RUN.md` (slice, red on the pre-pass driver)
- AC6 — with `PROMPT_BRIEF_CUTOFF` blank, AC1's fixture printed `preflight OK` and the off NOTE (red on the pre-pass driver); with a cutoff of 2026-09-01 after the README's `opened:` 2026-08-01 it printed `preflight OK` with neither the NOTE nor check 112 (slice)
- AC7 — a `spec-audit:` README whose conforming record carries the opt-in phrase only under `## Drawn from the session` drew check 89's refusal, no admission and no check 112 (slice)
