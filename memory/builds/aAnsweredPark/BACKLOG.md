# aAnsweredPark — asks

## Asks

- TOOL-aAnsweredPark-2 · filed 2026-11-25 · THE POSITION READ EXCEEDS THE CARD'S READ BOUND ON A LARGE BUILD. One read of dBoundRoles took 69 to 91 s on node a (PINNED 2026-11-25), against the card's 10 s bound (PINNED 2026-11-25), so the card's item reads skipped and the `actions.free` guard disarms. The bound and the guard are not the fix. · seen `tools/loop/position.py` matching `def derive_position` · accept the read of a build that size answers inside the card's bound, measured on node a
- TOOL-aAnsweredPark-3 · filed 2026-11-25 · A RUN THAT PARKS IS REFUSED THE COMMIT OF ITS OWN PARK ROW. An unsettled decision answers `awaiting`, the card then reads `item — none`, and `actions.free` at `read-only-probes` admits reads only, so the run cannot commit the row, nor the record that answers it. Read from the hook's code, not run. · seen `tools/hooks/scratch-guard.js` matching `item — none` · accept the owner rules who writes a park's row and its answer record, and the guard admits that act
- TOOL-aAnsweredPark-4 · filed 2026-11-25 · THE POSITION HAND-OVER'S OWED LINE IS READ BY NOTHING. After TOOL-aAnsweredPark-1 the engine counts `decision` rows alone, so the `owed` line the driver prints into the hand-over selects nothing. Removing it edits the unattended kit. · seen `tools/unattended/unattended.sh` matching `PARK_ACTS_OWED` · accept the hand-over prints no line its reader does not use
- TOOL-aAnsweredPark-6 · filed 2026-11-25 · THE DRIVER'S PARK NO-OP MATCHES AN ANSWERED ROW. `--park` writes nothing for an item and reason already parked, and `--exhausted` keeps the first ending, and neither asks whether the standing row is answered, so a question asked again in the same words raises no interrupt while the driver reports success (the closing review's M1). · seen `tools/unattended/unattended.sh` matching `decision already parked, unchanged` · accept a park over an answered row says it is answered and names the act that raises a new question, with an arm for `--park` and one for `--exhausted`

## Dispositions

- SEV · TOOL-aAnsweredPark-2 · MED · the card's item is unread on a large build and the guard is disarmed there
- SEV · TOOL-aAnsweredPark-3 · MED · a parked run needs another session to record the owner's answer
- SEV · TOOL-aAnsweredPark-4 · LOW · a hand-over line no reader uses
- KEEP · TOOL-aAnsweredPark-2 · awaiting the owner
- KEEP · TOOL-aAnsweredPark-3 · awaiting the owner
- KEEP · TOOL-aAnsweredPark-4 · awaiting the owner
- SEV · TOOL-aAnsweredPark-6 · MED · a re-asked question is settled in advance, contained by the identical item and reason
- KEEP · TOOL-aAnsweredPark-6 · awaiting the owner
