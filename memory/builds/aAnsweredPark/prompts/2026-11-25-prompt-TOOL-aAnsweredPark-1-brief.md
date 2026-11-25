# Brief — aAnsweredPark: an answered owner decision no longer interrupts its build

**Serves:** research TOOL-aAnsweredPark-1

The prompt arrived as the first message of a session started from another session, which forwarded the
owner's choice. Its task paragraphs are quoted below; the owner's later answer was relayed by that session.

## The prompt

> Fix `tools/loop/position.py` on main so that an owner decision that has been answered no longer counts as an open `owner-decision` interrupt, then land it on `origin/main`.
>
> Fetch and build on current `origin/main`.
>
> First find how the records already say a decision is answered or disposed (run-state rows, the disposition record of `item.flow.on-exhausted`, the `resume` after a hold, `memory/guides/UNATTENDED-ASKS.md`, `UNATTENDED-STOPS.md`, `UNATTENDED-VERBS.md`) and reuse that seam. Only a record of the owner's answer may settle a row: never the passage of time, never the run's own decision alone, and an unanswered row must still interrupt. If the records hold no such answer form, or if choosing one is a real fork (for example whether a `resume` after an owner hold settles all earlier rows, or whether the run may proceed on other items while a decision is open), stop and ask the owner before building. Also check the hold branch of the same function stays correct.
>
> Done when: a regression case was seen red before the fix and green after, an unanswered decision still interrupts, the fix is on `origin/main` with its sha, and your final message says what the engine now answers for dBoundRoles and which answer records, if any, the dBoundRoles run still needs.

## The brief

### Goal
The position engine counts as an open owner decision only a parked `decision` row with no answer record of
its own, and a hold of a run whose phase is HELD.

### Items
1. A parked `decision` row settles only by its own tracked disposition record. The row's tag is
   `item.parked.` and the row's timestamp lowercased with each `:` written `-`, for example
   `item.parked.2026-11-24t23-07-16z`; the record's Disposition is `answered` and its Reason, which quotes
   the owner, is present. The newest record of that tag decides, so a later record of another word
   re-opens the row. A second decision row carrying one timestamp takes the tag ending `.2`, and so on, so
   no record settles two rows.
2. Only `decision` rows and a live hold interrupt. The `rescope`, `handoff`, `abort`, `override` and `waiver`
   rows do not.
3. One unsettled decision still answers `awaiting` for the whole build.
4. A hold interrupts only while the run-state `phase` fact reads `HELD`; its until condition is read as today.
5. The rule is stated in `position.py`'s docstring and `help/loop.md`: that it replaces the wording of
   TOOL-dDeclaredLoop-7, which counted every owed kind; that a newly parked decision stops the run until
   answered; and that a record is typed by an agent, so the quoted words are the evidence.

### Acceptance
Fixture cases of `position.py --fixture --plant`, seen red before and green after: an answered decision acts;
an unanswered one awaits; a record of another row, of another word, or with no Reason does not settle; two rows
of one second settle apart; a `rescope` and a `handoff` row do not interrupt; a resumed hold does not interrupt
and a HELD one does. A read of dBoundRoles at its committed tip says what it answers.

### Gates
`loop position fixtures` and every leg the spec's files trip.

### Non-goals
`actions.free`, `.governance/policy.toml`, any hook, the card's read bound, `tools/memory-tree/routed_commits.py`,
the unattended kit, the disposition grammar, and any dBoundRoles file. The read's cost is an ask, not a fix.
A `flow.on-exhausted` or owner-gate row is a decision row as any other: its own item's disposition does not
settle the parked row.

### Limitations
Only a record of the owner's answer settles a row. Closed specs stay frozen: the superseded wording is named here.

### Reuse
`adapt.py`'s `read_disposition_release` answers the newest disposition record of a tag as `(stem, word)`; it
drops the Reason, so extend it at that seam rather than re-deriving newest. `build_records.py new disposition`
is the door. Prototyped 2026-11-25 in a scratch repository: the door refuses `item.parked.2026-11-24T23:07:16Z`
as no tag, writes `item.parked.2026-11-24t23-07-16z` disposed `answered`, the reader answers it once staged and
not before, and `check_disposition_record` answers None, unarmed, for that undeclared item. `adapt.py` does not
import `position.py`. Recall terms used: parked decision owed owner-decision settle answer resume hold
disposition PARK_KINDS_OWED position awaiting interrupt.

## Drawn from the session

> Yes, A, A, A (Recommended)
— owner, 2026-11-25, relayed by the session that started this one; its question named the hold as interrupting only while the phase is HELD

> (1) a parked decision row settles only by its own disposition record quoting the owner, item.parked.<row timestamp>; (2) only decision rows and a live hold interrupt, so rescope, handoff, abort, override and waiver rows no longer do; (3) one unanswered decision still stops the whole run.
— agent, the session that started this one, as it put the question to the owner

## Owner confirmation

Asked: settle a row by its own record, interrupt on decision rows and a live hold only, one unanswered decision stops the run
Answer: Yes, A, A, A (Recommended)
