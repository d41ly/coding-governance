**Serves:** research TOOL-dSafePassage-1

# Owner instruction — builders run at high effort from the next unit

## The prompt

> change builders to run at high effort instead of xhigh from the next unit.

— owner, 2026-10-26, in the run's session while TOOL-dSafePassage-1's build pass (`wf_b6ea5cfe-f84`) was running
at `efforts.builder: xhigh`, the level `handoff.py stage-efforts build` prints.

## How the run applies it

- TOOL-dSafePassage-1's running pass is not restarted; it finishes at `xhigh`.
- Every later `unattended-unit.js` dispatch in this run passes `efforts: { builder: "high" }`, overriding the
  catalogue's `xhigh` for this run only. The catalogue itself is not changed.
