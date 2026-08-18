# TOOL-aLoosenedCeiling-4 — the NicoCares adopter's read-path ceiling, raised against its measured growth

**Status:** OPEN · rev-3 · 2026-08-18 · node a · Tier-1 · base 6382c564 · streams tooling

## 1. Goal

The NicoCares package repo sits at 109998 B of read path against a 110000 B ceiling — two bytes.
Raise the ceiling to a number derived from that repo's own measured growth, repair the comment
block that has stopped describing its own value, and move BOTH governing-doc citations of the old
figure — only one of which a gate there can see.

## 2. Scope (IN)

- **S1** — `READ_PATH_CEILING` in that repo's `.memory-tree.conf` moves from 110000 to 241070.
- **S2** — the comment block above it gains an entry recording the measurement, the rate it was
  derived from, and the fact that the block had gone stale. The staleness is TWO separate things
  and the first draft of this scope item merged them into one wrong sentence. The narrative stops
  at a raise to 116600, which is 6600 above the live 110000, and BOTH merge parents already carried
  that same stale ending — so the prose stopped being maintained several raises before any merge.
  Separately, the merge wrote 110000, a pin neither parent held; they held 124000 and 123000. The
  merge did not revert the prose. It only reset the value.
- **S3** — the governing-doc citations of the old value move in the SAME commit. There are TWO in
  `.claude/SESSION-KICKOFF.md`, and only one is gated: that repo's citation gate matches an ALLCAPS
  constant name adjacent to a number, so it sees the key-equals-value line and is blind to the
  prose sentence naming the same figure. Moving only the gated one leaves a stale number in a
  document contracted to describe the current tree, with the gate green. The second is a manual
  obligation and is written down here because nothing will remind the builder.
- **S4** — the conf records, beside the raise, that the alternative its own comment recommends is
  spent: rotation of the backlog shard frees 646 B today, against a two-byte headroom.
- **S5** — the change is a path-scoped commit of exactly those two files, on that repo's `main`,
  and NOT pushed. Path-scoped rather than all-tracked, so nothing else in that tree rides along.

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

There is a SOFT limit above it, and it is why a year of runway is not on the menu. FOUR of that
read path's seven members carry that repo's flat index cap of 153600 B, summing to 614400 B, and a
ceiling above that sum can no longer fire on those four before check 6 does. The other three are
named in that repo's `READ_PATH_WAIVER` and carry no byte cap at all, so above 614400 the aggregate
ceiling is still the only thing watching them. That is why this is a soft limit, and the first
draft of this paragraph overstated it as absolute. Those three are 11763 B of the current total and
have been static since adoption, so they are not what spends the budget; the honest cost of this
raise is 2.2 times more slack on three files nothing else watches. Today's 110000 binds 5.6 times
tighter than the capped sum, and 241070 binds 2.5 times tighter. Past roughly three months of
runway the instrument dissolves for the capped members, and this is the largest raise that keeps it
an instrument.

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

Two files, both in the adopter repo at `C:/projects/incms/main/vendor/nicocares-package`:

- `.memory-tree.conf` — the pin and its comment block.
- `.claude/SESSION-KICKOFF.md` — both citations of the old value, the gated one and the prose one.

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
- **AC3** — When `python scripts/check_citations.py --report-only` runs there, it is green. The
  flag is `--report-only`; that script parses argv by substring and has no argument parser, so
  `--report` is silently ignored and runs a different mode, which is what the first draft of this
  criterion asked for by mistake.
- **AC4** — When `grep -n 'pin is 110000' .claude/SESSION-KICKOFF.md` runs there, it returns
  nothing: no sentence states the old value as the CURRENT pin. A bare search for the number is
  the wrong witness and was the first draft's — the movement record names the value it replaced,
  exactly as the conf's own comment convention does, so demanding zero occurrences would have
  forced the history out. This is the witness for the UNGATED half of S3, which AC3 cannot see.
- **AC5** — When the adopter repo's `git log` on `main` is read, the raise is one commit naming
  exactly two paths, unpushed, whose message carries the measured rate and the runway it buys.

## 7. Gates

In the adopter repo: `bash scripts/check-memory-hygiene.sh` · `python scripts/corpus_ids.py
--check` · `python scripts/check_citations.py --report-only` · `python scripts/gen_build_index.py
--check`. Nothing in this repo's bar is affected, because nothing in this repo references that one.

## 8. Open questions

none — the owner authorised the cross-repo edit at kickoff and delegated the number to a derivation
from the measured growth rate, which section 4 records.

## 9. Revision log

- rev-1 · 2026-08-18 · initial draft.
- rev-2 · 2026-08-18 · folded spec-audit round 1.
- rev-3 · 2026-08-18 · AC4's witness was wrong in the build pass that ran it: it searched for the
  bare number, which the movement record correctly still names as the value it replaced. Narrowed
  to the sentence that would assert it as current. Two of S2's factual claims were wrong and are
  rewritten against what the adopter's history actually shows. The sum-of-caps bound in section 4
  was overstated as absolute: three of the seven members are waived and carry no cap, so the raise
  buys them slack nothing else watches, and that cost is now stated rather than hidden by the
  arithmetic. S3 gained the second, ungated citation and AC4 its witness. AC3's flag was wrong and
  would have run a different mode silently. Files touched and S5 now name the absolute path, the
  two files and the branch.

## 10. Reuse audit

Satisfied for the set by unit 1's section 10. This unit extends no seam: it moves one declared
value and one citation in a repository that installs this kit, and the mechanism it uses is the
kit's own conf. The reuse question that MATTERS here was asked in the other direction and is
recorded in section 3 — whether the adopter should take this build's keyed kit rather than keep its
forked copy of the check-6 awk block. It should, eventually, because the keys are exactly the seam
that would let it delete a carve-out it re-applies on every kit release; and it must not do so in
this unit, because that re-adopt reds its check 6 on two files.
