# Brief — aAnsweredPark: the revision of TOOL-aAnsweredPark-1's files touched

**Serves:** research TOOL-aAnsweredPark-1

## The prompt

> The unit harness's builder (run `wf_5a7a9476-d1a`) returned `diverged: true` before committing any code, with the `why` quoted whole below as the Goal.

## The brief

### Goal
DIVERGENCE: spec section 4 "Files touched (estimate)". The design builds as written. The file list cannot be committed in the one commit the task requires, the one that also flips the spec to CLOSED.

I found this late, at my one commit attempt: the pre-commit hook refused it. I missed it in the pre-edit check. Two paths the hook needs are undeclared.

(1) ACCEPTANCE LEDGER. Hygiene check 23 refuses a CLOSED Tier-2 spec whose AC1 to AC10 no journal record evidences. Section 4 would have to list `memory/builds/aAnsweredPark/build/2026-11-25-build-TOOL-aAnsweredPark-1-1-acceptance-ledger.md`. It is a journal record with one line per AC1 to AC10, each sharing a backticked token with its criterion. The dKeptSession specs (44, 56, 62, 63, 79, 89) all name theirs.

(2) KEEP ROWS. This unit is the build's only unit, so its CLOSED makes the build CLOSED. Verdict V10 then reds hygiene check 9 on TOOL-aAnsweredPark-2, -3 and -4, which derive OPEN with no status row. `memory/builds/aAnsweredPark/BACKLOG.md` needs a `- KEEP · <id> · <why>` row for each under its Dispositions heading. Either the main loop commits those first, as 642e16c9d did for dKeptSession, or section 4 lists the file and says what each row reads. Disposing asks is not a builder's call under this spec.

The hook itself renders `memory/LIVE.md`, `memory/builds/aAnsweredPark/README.md` and the spec's gen:spec-records block; section 4 may name those as generated. No kickoff re-stamp is needed.

That list is complete. In a throwaway clone, the built change plus the ledger and the three KEEP rows committed with rc=0 and every pre-commit leg ok (GOV_DEFAULT_BRANCH set there only because a clone is a primary tree). Nothing else in the spec failed. AC1 to AC10 were each observed as stated, and the base-tree claims I checked held.

### Items
1. Add to section 4's files touched `memory/builds/aAnsweredPark/build/2026-11-25-build-TOOL-aAnsweredPark-1-1-acceptance-ledger.md`,
   the journal record evidencing AC1 to AC10, one line each. The three KEEP rows are committed by the main loop,
   so `memory/builds/aAnsweredPark/BACKLOG.md` is not listed.
2. Name `memory/LIVE.md`, `memory/builds/aAnsweredPark/README.md` and the spec's records block as rendered by the hook.
3. Bump the rev and add the section 9 line naming this record. Nothing else changes.

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
Copied from the build's brief: `adapt.py`'s `read_disposition_release` and the `build_records.py new disposition` door.
