# The whole-design audit: the design walked step by step before any chain spec

**Serves:** research PLAY-dClosedLoop-1

The owner chose, at FQ-1, a whole-design audit before any chain spec: mechanical checks, a paired walk sliced two
ways and graded on past defects planted back into a sealed copy, then the paired closing review
(`build/2026-10-19-build-PLAY-dClosedLoop-1-final-questions.md` `[audit]`, which designs it). This record runs it: the
owner's words, the order of work, each instrument as built and seen red, and, as the audit runs, its findings, its
fold and its witness.

## [words] The owner's words, 2026-10-19

> Session compacted. What're the next steps to conduct a whole-design audit as suggested + proceed with questions 2
> and 3?

The answer set out five steps, `[plan]`'s, and the owner replied:

> go

## [plan] The order of work

The final-questions record's `[sequence]` put the audit's instruments in its step 3, and its `[bootstrap]` puts three
more in this build: the carries join, the deviation population and the as-built renderer, which questions 2 and 3
rest on and which no step had scheduled. They are built beside the audit's, so the walk reads them and the closing
pair reviews them, and `[sequence]` now says so.

1. **The tooling, with no agents.** Stage 0's checks (`[stage0]`); the walk's briefs, its table and the critical
   rubric; the sealed seeding and a scorer that reads `[tag]` addresses; the carries join with its coverage report,
   the deviation population and the as-built renderer; and wall-time capture. Each is seen red before it is trusted.
2. **The owner's word on v2's four open readings,** SA-1, SA-5, CL-3 and `wait` (v2 `[open]`), so the walk reads
   one design.
3. **The audit,** as final-questions `[audit]` designs it: Stage 0, the paired walk over the seeded copy, the recall
   scored, the owner's forks, the fold, the paired closing review from `6ba4eaaa1`, which also covers the review
   debt, and Stage 0 again.
4. **The baseline,** on the owner's word that the design is whole: v2 frozen at that commit, and every later change a
   deviation record.
5. **The chain opened,** dTrueNorth first, each Design exit read through its coverage report.

"No critical gap left" is claimed only when Stage 0 is green with every check seen red, both walk tables are
complete, the recall bar is met, no critical finding is open, and the closing pair finds no new critical one.

## [stage0] Stage 0: the mechanical checks

`build/2026-10-19-build-PLAY-dClosedLoop-1-stage0.py` runs five new arms, one per class research-final-audit `[2]`
says a table can check, and re-runs the design's existing checks in the same tree.

| Arm | Reads | Red on | Left to the walk |
|---|---|---|---|
| K1 items | the 90 flow items and the 26 expansion items | an actor of no declared kind or role, or a core item naming an expansion role; a missing Needs cell, or a dash there off its step's first item; a need naming no item; a cycle among needs; no witness; no Then or Routes cell; an owner that is no chain build | whether a witness is actor-typed (P2), and whether an outcome is the right one |
| K2 routes | every Then and Routes cell, branch by branch | a route to an item-shaped tag that is neither an item nor a key; a target in no declared form; an item that ends nowhere; an item no entry reaches; and, through the reconciliation probe's `--all-routes`, a route target that neither its source's owner nor an ancestor builds | whether a terminal, return, wait, owner, ask, policy or program target does end; a policy's routes per value; the `[transitions]` join `gap-flow-15` owes |
| K3 kinds | the map's record kinds against layer-memory's kind table | a kind with no row; a row naming no writer item; a kind no item waits on or names, and no other build's clause names | a reader or writer that is a gate, a renderer or a hook |
| K4 keys | the catalogue's keys against every chain clause and item | a key read by none, marked guard-bearing where one of its values loosens | whether an unread key bears a guard beyond its values' words |
| K5 principles | v2's `[enforcement]` against `[chain]`'s minted ids | a principle with no row, or a row naming no clause; an id no clause carries, or a retired one; a clause citing a principle by id outside that principle's row | whether a named clause enforces its principle |

The re-runs are the design map, the atlas, fold state, the reconciliation probe, the clause scan, the clause ids, the
gap join, the preset check, the critical path, line coverage and the review debt. Seven of them lived only in the
session's scratchpad or inside a record: each is promoted beside the map, byte for byte but for its Serves line and
one note, so Stage 0 runs in any tree, the walk's seeded copy among them. Line coverage now reads the shape audits'
`Subjects (round N):` line, where it had stopped (research-final-audit `[1b]`).

A finding stands unless a row of `[stage0-classes]` names its arm, its node and a class from that arm's closed set,
and a row no finding needs is itself a finding. The audit's fold fixes each red or classes it there; the walk takes
the reds and each arm's "left out" lines as its leads.

**Seen red.** Each arm's plants, on an in-memory copy, turn it red for their own reason, and the run is in the night
pass's instruments record, `[stage0]`. The reconciliation probe's default run passes a plan item planted with a route
to `deploy.land`, and its `--all-routes` run reds it.

**The first run,** on the folded tree before its commit: 184 findings, K1 4, K2 46, K3 79,
K4 55 and K5 none, every re-run green. They are the audit's first leads, listed whole in the instruments
record's `[stage0]`:
- K1: three expansion items whose actor cell opens "the owner", where the kind is `owner`; and `design.streams`,
  whose Needs cell names the policy key that shares its spelling, read as needing itself;
- K2: prose targets the forms do not read, most in the expansions' Routes cells; the release and distribution
  programs ending only through them; fourteen items reached from no entry, since a prose need names no item: the
  Build step's five from `build.recommend` on, `maintain.levels`, `maintain.record`, `loop.record` and six of
  distribution's; and 21 routes into a build that comes later in the chain;
- K3: 36 kinds whose row names no writer item, and 43 no item waits on or names;
- K4: keys that no clause and no item reads, 18 of them guard-bearing.

**K5's leads.** Two principles have rows that name clauses carrying only part of them: no clause builds P3's
remote-CI verdict slot, and none names P18's ranking of a fork's options, the most feature-rich and then the most
expandable.

## [stage0-classes] Stage 0's classes

Empty until the audit's fold classes what it does not fix.

| Arm | Node | Class | Reason |
|---|---|---|---|
