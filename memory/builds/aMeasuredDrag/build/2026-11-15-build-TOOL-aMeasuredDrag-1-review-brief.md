**Serves:** research TOOL-aMeasuredDrag-1

# Review brief — the adversarial performance review, every lens

## Why

The owner's complaint: gov itself AND the repositories that adopt it (`C:/projects/incms/main`,
`C:/projects/nicocares/main`) deliver work extremely slowly under gov's governance. This review finds
WHY, with mechanisms and numbers, not opinions. Base sha `aebbb4a72`, node a (Windows + MSYS).

Read the evidence record beside this file first:
`memory/builds/aMeasuredDrag/build/2026-11-15-build-TOOL-aMeasuredDrag-1-evidence.md` (measured
gate-leg timings, commit mix, prior measurements). Prior measurements are leads to re-verify.

## Hard rules — you are read-only

- Write, edit, commit, stage, checkout or stash nothing. Run no verb with `--write`, `--land`,
  `--close`, `--prepare`, `--dispatch`. Touch the adopter repos only to read.
- Never run `tools/run-gates/run-gates.sh`, `tools/push-main.sh`, any `*.test.sh` suite,
  `run-selftests.sh`, `gen_build_index.py --write`, or a whole-tree hygiene run. Another unattended
  run may be live on this machine.
- You MAY time single read-only commands that finish within about 3 minutes. Take a spawn baseline
  first (`time (for i in 1 2 3 4 5 6 7 8 9 10; do /usr/bin/true; done)`) and report it beside every
  timing, so a loaded machine is visible.
- Code questions are Grep/Read/Glob. Count process spawns in loops: one spawn costs about 21 ms
  quiet and 0.6-0.8 s loaded on this node.

## What counts as a finding

Be adversarial toward the project: every check, hook, record and step must justify its wall-clock
and token cost. Be honest too: small cost x rare event is not a finding. Rank by cost per event x
events per week, and name who pays: gov, adopters, or both. Cite `path:line` for every mechanism.
Aim for 6-15 distinct findings; depth over breadth. Look for whole-tree work per commit, call or
unit; work repeated that could be cached or scoped; serialisation that could be parallel; and
ceremony whose cost exceeds what it protects.

## Return shape — exactly this, nothing else

One fenced `json` block holding:

    {"lens": "<lens key>",
     "findings": [{"id": "<lens key>-<n>", "title": "...",
       "mechanism": "what happens and why it is slow, with path:line",
       "evidence": ["each measurement with its baseline, ledger rows, counts, git facts"],
       "cost_per_event": "...", "frequency": "per commit/push/unit/session/week, how many",
       "weekly_cost_estimate": "wall-clock and/or tokens per week, with the arithmetic",
       "payer": "gov|adopters|both",
       "fix": "the smallest change removing most of the cost, and the guarantee it trades",
       "fix_effort": "S|M|L", "confidence": "measured|derived|suspected"}],
     "notes": "what you could not check, and why"}

The candidates-and-losing-test shape of your role maps onto this: each finding is a candidate cause,
its evidence is the test you ran, and the fix is the pick.
