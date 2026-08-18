# TOOL-aLoosenedCeiling-4 — the NicoCares adopter's read-path ceiling, raised against its measured growth

**Status:** OPEN · rev-1 · 2026-08-18 · node a · Tier-1 · base 6382c564 · streams tooling

## 1. Goal

The NicoCares package repo sits at 109998 B of read path against a 110000 B ceiling — two bytes.
Raise the ceiling to a number derived from that repo's own measured growth, repair the comment
block that has stopped describing its own value, and move the one governing-doc citation a gate
there holds against it.

## 2. Scope (IN)

- **S1** — `READ_PATH_CEILING` in that repo's `.memory-tree.conf` moves from 110000 to 241070.
- **S2** — the comment block above it gains an entry recording the measurement, the rate it was
  derived from, and the fact that the block had gone stale: its narrative ends at a value fourteen
  thousand bytes above the live pin, because a merge wrote a value neither parent held and reverted
  the prose with it.
- **S3** — the governing-doc citation of the old value moves in the SAME commit. That repo runs a
  citation gate which harvests integer constants from its conf and reds any governing document
  citing one at a stale value, and its kickoff manifest carries exactly that citation.
- **S4** — the conf records, beside the raise, that the alternative its own comment recommends is
  spent: rotation of the backlog shard frees 646 B today, against a two-byte headroom.
- **S5** — the change is committed in that repo and NOT pushed.

## 3. Non-goals (OUT)

- `READ_PATH_HEADROOM` is NOT declared there. That repo's installed kit is seventeen releases
  behind and its `do_measure` still carries the literal, so the key would be read by nothing. A
  declaration that does nothing is worse than an absent one: the next reader believes the tree is
  configured. The unit records this instead and leaves the key out.
- No kit re-adopt. Taking this build's kit into that repo would red its check 6 on two files, drop
  a check that exists only in its fork, and require seven carve-outs to be re-applied. That is a
  build, not a line in this one.
- No rotation, no trimming of the charter's citation list, no touching that repo's own backlog.
- No push, in either repo.

## 4. Design

### The measurement

Read path today: 109998 B over seven members. Two files are 83% of it and 90% of all growth ever
recorded on that path — an append-only decisions log at 57604 B and a backlog shard at 34113 B.

Growth was measured four independent ways over that repo's history, rename-aware across the flatten
that moved three of the members:

| basis | window | rate |
|---|---|---|
| daily sampling, gross additions | 43 days | 3513 B/day |
| daily sampling, gross | last 14 days | 3791 B/day |
| per-commit sampling on first parents | 17 days | 5255 B/day |
| ceiling raises actually committed | 4 days | 4000 B/day |

Gross rather than net, deliberately. Rotation removes bytes, and the ceiling is consumed by
additions whether or not a later rotation gives some back. The planning rate is 4000 B/day, which
two independent bases agree on; 5255 B/day is the conservative one.

The other number that sizes headroom is the largest single landing observed: 10998 B. Headroom has
to clear one merge, not an average, and that repo's own stated convention of about two units of
headroom is roughly 2500 B, which does not clear the median merge in its recent history.

### The number, and why not a bigger one

131072 B of headroom, so 109998 + 131072 = 241070.

That is the smallest round figure buying one calendar month at the planning rate without assuming
rotation happens, and about two months if it does. It clears eleven of the largest observed
landings. The candidates below it buy roughly two weeks, which is not distinguishable from the
cadence being fixed — that repo committed eleven raises in four days.

There is a hard limit above it, and it is why a year of runway is not on the menu. The capped
members of that read path each carry that repo's flat index cap of 153600 B, summing to 614400 B. A
ceiling above that sum can never fire before check 6 does, so it stops measuring anything. Today's
110000 binds 5.6 times tighter than that sum; 241070 binds 2.5 times tighter. Past roughly three
months of runway the instrument dissolves, and this is the largest raise that keeps it an
instrument.

### The honest part

That repo's own hygiene document already ratifies the rule that a raise is the LAST resort and
rotation comes first. That rule is satisfied here, not waived: rotation ran twice, collected the
reserve the conf comment still advertises, and what remains to rotate is 646 B — the shard now
holds three closed rows out of a hundred and thirty-four. Rotation cannot reach the ceiling, which
is the precondition the rule names.

What this raise does not fix is the diagnosis the conf comment already got right: an append-only
log against a shrink-only ratchet grows forever, and no headroom is a structural answer to that.
The untried lever is trimming the charter's own citations so fewer files enter the read set at all,
which that repo has a row for and which is not this unit's to spend.

### Files touched (estimate)

Two files, both in the adopter repo: its `.memory-tree.conf` and the governing document holding the
gated citation.

## 5. Production-readiness checklist

- risks — the ceiling is being loosened 2.2x in a repo where it has been loosened eleven times
  already. The mitigation is that the number is derived rather than incremented, and that the
  derivation and its expiry are written beside it, so the next session raising it has to argue with
  a measurement rather than with a habit.
- testing + left-shift gates — that repo's CI runs its hygiene gate on every push and pull request;
  the citation gate runs in the same workflow. Both are the test.
- migration / rollback — one declared value; rollback is restoring it, which reds immediately since
  the path is already two bytes under the old number.
- everything else — N/A, this unit changes two declarations in another repo.

## 6. Acceptance criteria

- **AC1** — When `python scripts/corpus_ids.py --report` runs in the adopter repo, the read-path
  total is under the new ceiling with headroom in the hundreds of kilobytes.
- **AC2** — When `bash scripts/check-memory-hygiene.sh` runs there, it is silent.
- **AC3** — When `python scripts/check_citations.py --report` runs there, it is green, which
  requires the governing-doc citation to have moved in the same change as the conf.
- **AC4** — When the adopter repo's `git log` is read, the raise is one commit, unpushed, whose
  message carries the measured rate and the runway the number buys.

## 7. Gates

In the adopter repo: `bash scripts/check-memory-hygiene.sh` · `python scripts/corpus_ids.py
--check` · `python scripts/check_citations.py --report` · `python scripts/gen_build_index.py
--check`. Nothing in this repo's bar is affected, because nothing in this repo references that one.

## 8. Open questions

none — the owner authorised the cross-repo edit at kickoff and delegated the number to a derivation
from the measured growth rate, which section 4 records.

## 9. Revision log

- rev-1 · 2026-08-18 · initial draft.

## 10. Reuse audit

Satisfied for the set by unit 1's section 10. This unit extends no seam: it moves one declared
value and one citation in a repository that installs this kit, and the mechanism it uses is the
kit's own conf. The reuse question that MATTERS here was asked in the other direction and is
recorded in section 3 — whether the adopter should take this build's keyed kit rather than keep its
forked copy of the check-6 awk block. It should, eventually, because the keys are exactly the seam
that would let it delete a carve-out it re-applies on every kit release; and it must not do so in
this unit, because that re-adopt reds its check 6 on two files.
