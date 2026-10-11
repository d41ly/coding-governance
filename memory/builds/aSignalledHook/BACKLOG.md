# aSignalledHook — asks

## Asks
- TOOL-aSignalledHook-2 · filed 2026-10-11 · the unattended kit does not handle push-main's exit 4 (`landed UNGATED`): its skill says to run `--landed` after the lander returns, `--landed` then fails check 34 with "the lander wrote none", and no command turns a green bar on the remote into a lander marker. Name exit 4 in the skill and `memory/guides/UNATTENDED-PROTOCOL.md` as an owner-decision handoff, or add a certify path that writes the marker after a green bar on the remote tip. · accept the unattended skill and `memory/guides/UNATTENDED-PROTOCOL.md` name push-main's exit 4, and an unattended run that meets it stops with a handoff naming the ungated commit instead of failing `--landed` check 34

## Dispositions
- SEV · TOOL-aSignalledHook-2 · MED · an unattended run that hits exit 4 stops with a misleading check-34 message; no wrong verdict, the landing is still refused the name landed
- KEEP · TOOL-aSignalledHook-2 · found by the closing review of TOOL-aSignalledHook-1 on 2026-10-11 and not folded: the fix is a protocol change to the unattended kit, outside this unit
