**Serves:** research TOOL-dSafePassage-11

# Owner instruction — node a provisioned at Python 3.15, the held run resumed

## The prompt

> I've now installed Python 3.15 final for daily-agent on COMPEETO-AGENT (py -0p lists it). Resume dSafePassage.

— owner, 2026-10-26, answering the run's parked decision "TOOL-dSafePassage-11 needs Python 3.15 on the build node", after the run held `host-owner-action` at `4cbd011d5`.

## How the run applies it

- Observed before resuming: `py -0p` lists `-V:3.15[-64] *` at `pythoncore-3.15-64`, and `python3`, `python` and `py` each report 3.15.2.
- The parked question is answered by option (a): the owner provisioned the build node per AP-31. The run resumed with `--resume` and builds TOOL-dSafePassage-11 next, then its dependants in the specs' `consumes-from` order.
- Every other node (b, c, d) still needs 3.15 before it can commit past TOOL-dSafePassage-11's pass; that is §4 Rollout's stated landing cost, carried to the wrap-up.
