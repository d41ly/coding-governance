**Serves:** research TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-20

# Brief — dPlacedRequest: the eight asks the child builds filed, adopted as spec amendments

## The prompt

> /unattended dPlacedRequest

## The brief

### Goal

The build run of dPlacedRequest found eight open asks in this build's own `memory/builds/dPlacedRequest/BACKLOG.md`,
each filed on 2026-10-26 by a child build's spec run against one of this build's unbuilt specs. Every one is ADOPTED
(protocol §11, `discoveries-adopted`) as an amendment to the spec it names, so the specs the audit and the builders
read already carry them; no unit is added.

### Items

1. TOOL-dPlacedRequest-65 (MED) amends TOOL-dPlacedRequest-2 S7 and AC7: the card-import fixture's recorded verdict, read by `read_card_fixture_verdict`, is the switch that reads `always-resume` as `fresh-when-idle`; the `CLAUDE.md` import line is no longer consulted.
2. TOOL-dPlacedRequest-66 (LOW) amends TOOL-dPlacedRequest-13 S9: `scan_feed_writers` also flags a line pushing a `refs/gov/` ref without `--force-with-lease`, seen red on a planted plain push of `refs/gov/mail/fx/a/s1`.
3. TOOL-dPlacedRequest-67 (HIGH) amends TOOL-dPlacedRequest-1 S8: under `leases.renewal: progress`, a renew whose `--witness` is the commit of a mail message of kind `question` addressed to the lease's build, `open` on this node and inside its declared deadline by `check_mail_deadline`, writes `renews: yes` even when it equals the record's `witness`.
4. TOOL-dPlacedRequest-68 (MED) amends TOOL-dPlacedRequest-4 S4: the placement block carries an optional `reenters: <unit id>#<F-id>` line, seen on a fixture late answer.
5. TOOL-dPlacedRequest-69 (LOW) amends TOOL-dPlacedRequest-7's item table: the tester's actor is spelled `role:gov-tester`.
6. TOOL-dPlacedRequest-70 (LOW) amends TOOL-dPlacedRequest-2 S4: `--card --follow --terminal` writes no second `card` record when the newest one already names the same terminal state, seen on a fixture close that follows twice.
7. TOOL-dPlacedRequest-71 (MED) amends TOOL-dPlacedRequest-20 S1: `--lease offer unit <slug> <unit> --to <fleet tag>/<session>` writes `offer: <fleet tag>/<session>` and classes the lease `offered` for every other session, the named node included, until the deadline.
8. TOOL-dPlacedRequest-73 (MED) amends TOOL-dPlacedRequest-2 S11: `scan_reader_keys` (`check_policy.py`'s `READER_SHAPES`) returns a key whose one read in a shell file is `read_card_policy <key>`, seen red on the planted file before the row lands.

Per ask: read the ask row whole in BACKLOG.md and the spec section it amends; verify every name it cites against the
tree (a name a unit of this build or a parent creates is cited as that unit's spec does, and a contradiction with the
tree is returned, never invented around); amend the scope item so the ask's `accept` holds; add one acceptance
criterion observing it, on a staged break or a fixture and never a suite, the ask's own red case and its green where
it names one (66, 70, 73); add `closes <ask id>` to the spec's `**Status:**` header verbs beside the
`advances TOOL-dPlacedRequest-22` already there, one verb per ask; extend §5 Files touched where needed (73 adds
`tools/policy/check_policy.py` to TOOL-dPlacedRequest-2); bump each spec's rev once and add its §9 line naming each
ask id and this brief.

### Acceptance

Each of the six amended specs carries a `closes` verb per ask it takes, a scope item and a criterion the ask's `accept`
is implied by, one rev bump and a §9 line naming the ask ids; `bash tools/memory-tree/check-memory-hygiene.sh --only
2,12,25` over the staged specs returns no hit the return leaves unexplained. Each spec stays under the spec ceiling in `tools/template-size-limits.txt`. An amendment that needs a mechanism no
scope item names (a new document, gate, adopter, verb or write path) is still made, and the return says so per ask,
so the spec audit that follows reads it. Return per ask: the spec, the scope item, the criterion number and the new
rev, then each hygiene hit and what was done about it.

### Gates

The memory hygiene gate (`--only 2,12,25`) and the naming lexicon over the six specs; no other gate.

### Non-goals

No product code, no commit, no index render, no BACKLOG.md edit, no `**Carries:**` or `**Derived:**` line, no status
flip (the specs stay DEFERRED), and no spec beyond TOOL-dPlacedRequest-1, -2, -4, -7, -13 and -20.

### Reuse

The seams are the ones each amended spec's §10 already names; the recall probe for this build is recorded in the
kickoff card (terms: lease claim ref compare-and-swap epoch tombstone offer feed placement entry.claim request card).
