**Serves:** journal DEPL-aHoistedPass-1

# Brief — DEPL-aHoistedPass-1

**Provenance.** The mandate's roster named
`memory/builds/aHoistedPass/prompts/brief-DEPL-aHoistedPass-1.md` and no file existed at it, for any
of the ten units; that name is also unwritable, because hygiene check 5 derives the record kind from
the `prompts/` subfolder. Derived by the building run from the roster line and the spec.

## What this unit is

`memory/builds/aHoistedPass/spec/2026-09-04-spec-DEPL-aHoistedPass-1.md`, **rev-5**, Tier-2, order 2,
parallel with `TOOL-aHoistedPass-3`. Read it whole, and read section 8 first.

`requires` in a kit descriptor buys install ORDERING and nothing else, so a descriptor can name a
dependency no verb checks and no gate reds. The unit adds the `review-harness` edge and makes plain
`requires` mean something at both places it can: a registry-name arm in `selfcheck` (arm A) and an
installed-set refusal in `_cmd_apply` (arm B), with a printed row in `cmd_plan` that moves no exit
code.

## The one thing rev-5 changed, and it is the reason to read section 8 first

**The `unattended` 1.17-to-1.18 bump is PARKED to the owner and is not this unit's to take.** rev-3
resolved it here while asserting the picks add no carrier beyond ratified scope; that is false —
`tools/unattended/SKILL.template.md` is one of the eight graded carriers and ruling D1 puts it on the
M3 veto-2 list, which the mandate's delegation does not reach. S8 is narrowed to
`KIT_GOVKIT_VERSION`. **So this unit is NOT an owner turn**, and it ships a changed `unattended`
payload at an unchanged `unattended` version, which AC10 states plainly rather than borrowing the
checker's green.

## What the run must not do here

Do not move any `gov:kit unattended@` marker or any of the three engine constants. Do not add a
bypass flag — a new public surface is veto 2 and a gate that ships its own escape hatch is not a gate.
Do not auto-expand the selection: arm B refuses and names what to add. Neither new refusal string may
spell a `tools/` path literal, because `install-prefix` is a shrink-only BAN.

## What is expensive and already priced

Arm B refuses nine selections that are legal today, and nine of gov's own selftest `--kits` call sites
are among them. Section 4 measured the repair — nine one-token edits — and measured that no exit code
and no assertion moves. F2 is RESOLVED at REFUSE with those repairs in scope.

## The acts this pass owes the record

`--dispatch` with the write set, `--brief` with this file, one commit carrying the unit id, then
`python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD`. `memory/backlog/DEPL.md` is a declared
SHARED_RECORD, so the dispatch declaration cannot carry it. `python tools/govkit/selftest.py` is run
BY HAND and its exit code reported, because no boundary runs it.
