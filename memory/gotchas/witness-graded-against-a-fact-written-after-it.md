---
name: witness-graded-against-a-fact-written-after-it
description: a sidecar line that outlives the lease it was written under is graded against the id the new lease replaced, so a dead incarnation's witness passes the check the live one owes
kind: class
universal: false
---

# The newest line was written by whoever came before

## Symptom

A verb grades a witness — the newest line of a sidecar log some hook appends to — against a fact
in the record: is this id absent from that listing. The line is the newest, the fact is the current
one, and the comparison is right. But the record's fact was REPLACED after the line was written, by
a resume that re-leased the run, and the hook writes only for the session the lease names — so the
newest line is the dead incarnation's, its listing predates the id it is now graded against by
construction, and the check passes on evidence about a job that no longer exists. The verb's own
NOT CHECKED list did not name a line older than the fact.

## The instance

`tools/unattended/unattended.sh` `verb_landed`, `read_stop_listing`, at spec rev-5 of
`TOOL-aWokenSentinel-7`: the stop-guard writes a LANDING line on EVERY stop of a bound session at
LANDING, allowed or blocked, and `--resume --keepalive-id` replaced `keepalive` without writing to
the stop log. After a stall and a resume, the new incarnation's one-turn `--landed` read the old
LANDING line, printed `keepalive-reaped: checked` against the new id, and stamped LANDED while the
new idle-wake fired on — the false pass the read-back exists to refuse (closing review id 15).

## The remedy

Stamp the fact when it is written and refuse a witness older than the stamp: `write_lease` records
`lease-utc`, and `--landed` treats a newest line whose `utc` is older as the pre-close case, so only
a listing the CURRENT incarnation's session produced can pass. Wherever a sidecar outlives a lease
— any log a hook appends per session beside a record a resume rewrites — the grader compares the
line's time to the lease's, or it grades the previous tenant's mail.

## Gating

Gated by `tools/unattended/unattended.test.sh`, the `AC16` arm beside the `keepalive-reaped`
read-back arms: a LANDING `[]` line stamped now, the lease replaced one second later by
`--resume --keepalive-id`, and `--landed` refusing through check 54 naming the line as older than
the lease it lost to. Observed RED against a driver copy without the `lease-utc` compare: the line
passed as `checked` and the record landed. The class is gated for `--landed` alone.
