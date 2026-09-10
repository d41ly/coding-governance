# Build brief — TOOL-aLeakedHandle-2

**Serves:** journal TOOL-aLeakedHandle-2

The pass this brief was handed to builds unit 2 of `aLeakedHandle` at rev-3. The spec is
`memory/builds/aLeakedHandle/spec/2026-09-10-spec-TOOL-aLeakedHandle-2.md` and it is authoritative.
This brief adds only what two audit rounds settled, so the pass does not re-litigate them.

## What the pass builds

The admission rule in `tools/run-gates/derive-ceilings.py`. A `.leg` row whose verdict is not `ok`
becomes admissible ceiling evidence when its seconds fall in the CLOSED WINDOW
`[ceiling, ceiling + 35]`, and not otherwise. The write set was declared with `--dispatch` before
this brief existed.

## The blocker this rule already survived, and must keep surviving

Round 2 confirmed a BLOCKER against the first draft of this rule, and the window is what answers it.
`seconds >= ceiling` is NOT proof the bound expired. `run-gates.sh:1393` sets `bound=0` and runs
every leg UNBOUNDED when the `CEILINGS_LIVE` capability probe at `:371` fails, and the `.leg` row
carries no bound field, so a leg that ran unbounded and failed on its own would have been admitted as
evidence — the exact failure-duration-as-floor case the `ok`-only filter exists to prevent. A ceiling
edited after a row was recorded breaks it the same way. Both states are named in the spec's
*What the rule cannot tell apart*, and the upper edge is observed by a third fixture leg.

**Do not widen the window back to an open comparison.** If you believe 35 s is wrong, argue it in a
rev bump with a measurement, and keep it closed.

**One discriminator was considered and rejected on the record**, so do not re-discover it as new:
`run-gates.sh:1315` writes `leg_ceilings live|inert` into `<git-dir>/gate-run/<runid>/header`. It
covers only one of the two breaking states and older run dirs carry no such key. It is in §4
Alternatives. Reach for it only if the window itself proves unworkable, and say so.

## What the audit already decided

- An UNBACKED ceiling stays REPORTED, not failed. §8 F1 carries the reasoning and a RESOLVED mark.
- No ceiling VALUE is re-declared. The raise-or-optimise question is parked with the owner.
- The eighth-`.leg`-field fix is rejected on the record in §4 Alternatives, not worked around.
- The `consumes-from TOOL-aLeakedHandle-3` edge is an acknowledgement, not a data dependency, and its
  rev-2 sentence is marked false in place. Leave both alone.

## The rules this pass is bound by

- The failing case of every new arm is OBSERVED RED before the unit closes. Stage the break, confirm
  red, unstage. The left-shift arm round 2 asked for is a fixture carrying a `fail` row at four times
  its leg's ceiling, asserted EXCLUDED — that gates the CLASS, not the 900.240 s instance.
- Commit at the end of the pass with the unit id in the subject, then run
  `python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD` and act on what it names first.
- Flip the spec's status header in the same commit as the code.
- Note what unit 1 landed before you: `memory/project/readme-contract.txt` is now in
  `SHARED_RECORDS`, and two new gate legs exist. Read `.unattended.conf` rather than assuming.

## What the pass must not do

- Do not refresh `tools/run-gates/ceiling-evidence.txt` with a live `--write` over this tree. §3
  forbids it, and its first consequence would be a red on a ceiling the owner has parked. The path is
  in the write set only for a fixture-scoped or reset-scoped edit the spec calls for.
- No sibling unit's files. Unit 3 owns the `report_one` tail in `run-gates.sh`.
