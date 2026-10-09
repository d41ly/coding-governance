**Serves:** diff-review PLAY-aDistilledCharter-5 TOOL-aDistilledCharter-8

# Tier-2 closing diff review — aDistilledCharter, ROUND 3

One read-only lens over round 2's fold only, run as a direct agent on 2026-10-09, primed with round
2's record and its blocker. The main loop re-read each finding's cited code as the skeptic.

**Reviewed range:** `18e3874fe...0ae6e6952` (the fold of round 2). **ROUND: 3.**

## Verdict: CLEAN WITH FIXES

Round 2's blocker is FIXED: the registry is BASE's again, the two sections moved word for word, and
no reader of the review protocol or of the spec template's structure depends on where they sit. No
new blocker. Six findings, the same count as round 2, so the loop does not re-arm: the review has
CONVERGED. Per BUILD-METHOD M4 the six are promoted as one batch, `TOOL-aDistilledCharter-9`.

## Review shape

- Raw 6, confirmed 6, refuted 0.

## Findings and their disposition

| # | Sev | Where | Finding | Disposition |
|---|---|---|---|---|
| T1 | MEDIUM | `PLAY-aDistilledCharter-2` spec and the ledger | PLAY-2's AC1 places the sections in the review protocol, which PLAY-5 emptied | batched: PLAY-2's AC1 amended in its rev-2 |
| T2 | MEDIUM | the runbook, the review protocol | "every adoption carries them" assumes a memory tree no declaration requires | batched: the sentences say what holds; making `playbook` require `memory-tree` is parked for the owner |
| T3 | LOW | the runbook, `render_playbook.py`, `playbook.kit.toml` | three places still send the outbound rules to the review protocol | batched |
| T4 | LOW | `SPEC-TEMPLATE.template.md` | the moved Tier-2 bullet says "the pattern below", which is in another document | batched |
| T5 | LOW | `render_playbook.py` | `checkout_dir` is read from `[charter]`, which refuses any key naming no placeholder | batched |
| T6 | LOW | `render_playbook.py`, `playbook.kit.toml` | `RETIRED_BLOCKS` is a typed copy of the descriptor's legacy blocks, and a v4.0 template carrying a legacy fence is not refused | batched |
