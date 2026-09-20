# TOOL-dDerivedDocket-54 — the cross-run exclusion probe reads history unsimplified

**Status:** SPECCED · rev-1 · 2026-09-20 · node d · Tier-2 · base fb07ca25 · streams tooling · order 18

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Unit 19's terminal-record exclusion reads each merge on a witness's tail by asking which parent
reaches a commit since BASE that touched the record's run-state path. The predicate its §8 F8
resolved is a REACHABILITY question; the command its §4 writes for it is history-simplified and
answers a different one, because a merge that is TREESAME to one side for the path prunes the other
side entirely. Build that probe as one unsimplified predicate with the clause saying why, and the arm
whose merge resolves the run-state path to the other side's content, so the exclusion is computed
from commits the probe can actually see.

## 2. Scope (IN)

- **S1** One predicate in `tools/unattended/lib-unattended.sh`: given a commit, a BASE and a path, it
  answers whether a commit since BASE touching that path is reachable from that commit, walking
  UNSIMPLIFIED so that no side of a merge is pruned for being TREESAME to it. Observed by AC1.
- **S2** The probe answers EXISTENCE and nothing else. It returns yes or no, it names no commit to
  the caller, and it makes no claim about who authored either side. Its header says so, because a
  reachability answer reads as an attribution to everybody who did not write it. Observed by AC4.
- **S3** The one-clause WHY lives in the header beside the flag: the shape that triggers the
  simplification and the wrong answer it produces, so the next reader does not simplify it back on
  the ground that the path is already restricted. Observed by AC4.
- **S4** A liveness half. An unresolvable range, an unknown commit or an unreadable path is reported
  as CANNOT ANSWER, distinct from the no answer that means no touching commit is reachable, because
  the caller's walk is fail-closed on the second and must not treat the first as it. A BASE is
  REFUSED before the walk, and reported the same way, unless it RESOLVES TO A COMMIT; the kit's own
  spelling of that test is `tools/unattended/lib-unattended.sh:166`. It is not left to the walk to
  notice, because the walk misses it in BOTH directions (§4): an empty or blank BASE exits 0 printing
  nothing under one of the two natural spellings and is then byte-identical to the honest no, while a
  BASE that is a legal object of another TYPE — a blob or a tree sha — makes `^<object>` exclude
  nothing, so both spellings walk the whole history and answer a confident YES for a commit the range
  never contained. BASE is caller-supplied and the caller reads it from the graded record, so neither
  half is hypothetical. Observed by AC3.
- **S5** Arms in `tools/unattended/check-unattended.test.sh` staging the merge on both sides — the
  side from which a touching commit is reachable and the side from which none is — plus THREE
  cannot-answer arms: a BASE that is not an object, a BASE that is empty, and a BASE that is a legal
  object of another type. The suite's executed-assertion floor for
  `tools/unattended/check-unattended.sh` moves in the same commit. The three arms are separate
  because they fail differently: the first is caught by any spelling, the second only by the refusal
  S4 puts in front of the walk, and the third fails in the OPPOSITE direction to both — it answers
  YES rather than nothing, so an arm asserting only that the probe stayed quiet passes over it.
  Observed by AC2, AC3 and AC5.

## 3. Non-goals (OUT)

- Building the terminal-record exclusion function. That is unit 19's, and its §4 cross-run arm, its
  five merge shapes and its stated residual all keep their current text; this unit supplies the
  predicate that function calls.
- Changing what the two sides MEAN. Unit 19's residual says the function tells a merge's sides by
  where the record's commits are and not by who made the other commits; that limit is untouched. This
  unit changes which commits the probe can SEE, never what seeing one implies.
- The endpoint, the exclusion of the advertised tip, or the live-record case. All unit 19's, and none
  of them reaches this predicate.
- Re-spelling the leg's other path-scoped history reads. Each answers its own question and keeps its
  own flags; the introducing-commit resolution across a rotation rename is a separate unit with its
  own walk.
- Editing `memory/map/features/unattended.md`. This unit mints no inventory key, because the codebase
  map does not scan `.sh` — `python tools/codebase-map/reuse_lookup.py` prints `unscanned layers: .sh`
  on every run — and that dossier measured 20387 B of its 20480 B cap on 2026-09-20 (PINNED), so any
  prose refresh it is owed is a net-zero edit belonging with a unit that funds it.

### Edges

- **consumes-from** external — the shared library's own discipline at HEAD: it is sourced and never
  executed and defines functions only (`tools/unattended/lib-unattended.sh:1-4`), and every history
  read goes through the pinned wrapper at `tools/unattended/lib-unattended.sh:45`, so replace refs
  cannot rewrite what this predicate answers.
- **hands-off** `TOOL-dDerivedDocket-19` — the spelling of the probe its cross-run arm writes as
  `git rev-list -1 <parent> ^<BASE> -- <run-state path>`, and the arm whose merge resolves the
  run-state path to the other side's content. Without it that arm's walk takes no exclusion at a
  pruned merge, so an owner's `may:` commit reds the record for ever, or the wrong side is excluded
  and the run's own grant leaves the range.
- **hands-off** external — applying the same reading to the leg's other path-restricted walks,
  deferred outside this build.

## 4. Design

### The measurement

Reproduced in a scratch repo at HEAD on 2026-09-20 (PINNED). BASE holds one file at its first
content; a run-branch commit changes it; a default-branch commit touches only an unrelated file; a
merge resolves the file back to the BASE content, so the merge is TREESAME to the default-branch
parent for that path.

| Probe, for that path, since BASE | Answer |
|---|---|
| simplified, from the merge | nothing |
| unsimplified, from the merge | the merge |
| simplified, from the run-branch parent | the run commit |
| unsimplified, from the default-branch parent | nothing |

Row 1 is the defect: a touching commit IS reachable from that merge and the probe prints nothing. Row
4 is the near-miss that had to be measured too — the flag does not make the probe answer yes for
every parent, so the walk does not start stopping at every merge once it is applied. Rows 2 and 4
together are the pair the arm asserts.

The same reading is already recorded twice in this tree for the same reason. The drift signal that
walks product commits carries it as a comment with its own scratch-repo reproduction
(`tools/drift-audit/drift_report.py:806-818`), and the rotation-mode check records that a first-add
search returns EMPTY for two of this repo's four archives because the rotation landed inside a merge
(`tools/memory-tree/row_grammar.py:335-340`). Neither is a guess about this class; both are
measurements of it.

### The BASE that fails open

§8 F2 settles where the predicate lives, not how its walk is spelled, and the two natural spellings
disagree about an EMPTY BASE, while a THIRD value defeats both of them. Measured on this tree on
2026-09-20 (PINNED) over a tracked run-state path:

| Call | Exit | Output |
|---|---|---|
| a BASE that is not an object, `<commit> ^<bad-sha>` | 128 | `fatal: bad object` |
| an EMPTY BASE, caret spelling, `<commit> ^` | 128 | `fatal: bad revision` |
| an EMPTY BASE, range spelling, `..<commit>` | 0 | nothing |
| a BASE that is a BLOB or a TREE sha, either spelling | 0 | a commit — the exclusion silently dropped |
| an honest no — a real BASE, a path nothing touched | 0 | nothing |

Rows 3 and 5 are byte-identical, and that is the first hazard. An empty BASE is reachable whenever
the recorded fact is missing or the caller's variable is unset, and under the range spelling it
arrives as a clean negative the caller's fail-closed rule then trusts. Row 4 is the second hazard and
it fails the OTHER way: a blob or tree sha is a legal object, `^<object>` therefore excludes no
commit, and both spellings answer a commit from outside the range as though the range had been
applied. No quiet-probe assertion can see that one, because the probe is not quiet — it is confident
and wrong. BASE reaches this predicate from the caller, which reads it from the record being graded
(`tools/unattended/check-unattended.sh:1195`), so the value is one a run writes.

The empty half's trap is already recorded in this tree at
`tools/memory-tree/row_grammar.py:337-338`, where `git log ""..HEAD -- <path>` exits 0
printing nothing and an unresolved baseline reports a clean archive — the passage this spec cites
elsewhere for the simplification lesson, carrying this one in the same sentence. Rows 1 and 2 fail
closed, so which spelling the build picks decides whether the EMPTY-BASE defect exists at all; the
row-4 defect exists under both. That is why the refusal is not left to the spelling and is not a
non-empty test either: S4 puts a resolves-to-a-commit test in front of the walk, which is the shape
`tools/unattended/lib-unattended.sh:166` already uses on an anchor.

### The predicate

One function taking a commit, a BASE and a path, answering yes, no or cannot-answer.

- **Yes** — a commit since BASE touching the path is reachable from the commit. The walk is
  unsimplified, so it follows all parents of a merge even where the merge is TREESAME to one of them,
  and it stops at the first hit rather than enumerating.
- **No** — the walk completed and reached none. This is the answer the caller's fail-closed rule
  depends on, and it is why the cannot-answer outcome may not share its shape.
- **Cannot answer** — the range, the commit or the path could not be resolved, or the BASE was empty
  or blank and the walk was never started. It is a distinct return and a named line (S4), never the
  silent zero that reads as a clean walk.

The probe is EXISTENCE only (S2). The caller asks it once per parent of a merge and decides from the
pair of answers; it never asks which commit, because a named commit invites the reading that the
probe knows who wrote the side, which unit 19's residual says plainly it does not.

### Why the clause is scope, not a comment

The simplified spelling is the natural one. A reader who sees a path restriction and a range already
believes the walk is narrow, and removing an extra flag from a narrow walk looks like a tidy-up. The
clause names the shape that punishes it — a merge TREESAME to one side for the path — and the
outcome, which is an answer of the wrong sign rather than a slower run. A flag with no clause beside
it is a fix that survives until the next reader is tidy, which is the class this finding belongs to.

### Fail codes

None. This predicate returns a value; the `fail` branches that red on a wrong exclusion are unit
19's, and the arms that grade them are its own.

### Rollout

**Order 18, sharing the step with unit 18.** Unit 19's cross-run arm calls this predicate and is
order 19, so 18 is the latest step that leaves it in place before its consumer, and every order from
1 to 38 is taken. Sharing a step is how a promoted unit reaches a consumer at all, and it is legal: a
consumes-from target may share its consumer's order, it may not be LATER than it. A shared value
declares a parallel group, and M6 in
`memory/guides/BUILD-METHOD.md` requires parallel passes only where disjointness is PROVEN. It is not
proven for this pair, on clause 1: both write `tools/unattended/check-unattended.test.sh` and both
move a floor in `.memory-tree.conf`, and unit 18 writes
`tools/unattended/lib-unattended.sh` too where its matcher is not already there. So the pair runs in
sequence. The roster is handed out ordered by step and then by id, which puts unit 18 first and this
unit second — the order this unit needs anyway, since its only requirement is to land before unit 19.

Dark by construction. Nothing calls the predicate at this unit's commit, and no record carries an
`asks:` fact or a `may:` grant until later units arm them, so every arm here is a scratch fixture.

### Inventory

One shell function in `tools/unattended/lib-unattended.sh` and one cannot-answer line prefix. No new
conf key, no new fact, no new verb, no new leg code. Any new shell function is named through
`python tools/lexicon/lexicon.py --suggest <identifier> --as <cell>`.

### Files touched (estimate)

`tools/unattended/lib-unattended.sh` · `tools/unattended/check-unattended.test.sh` ·
`.memory-tree.conf` for the suite's executed-assertion floor.

### Alternatives rejected

- **Per-parent merge diffs.** They answer a richer question than existence and cost a diff per merge,
  and the rotation-mode record already measures that the plain, unsimplified and per-parent spellings
  disagree on the same population (`tools/memory-tree/row_grammar.py:335-340`). A predicate whose
  answer depends on which of three spellings a reader picked is the defect one level up.
- **First-parent-only walking.** It answers "did the mainline touch this", which is neither of the
  two questions here, and it would exclude exactly the side the run's own commits sit on in one of
  unit 19's five shapes.
- **Enumerating the range and diffing each commit.** Correct and unbounded. The unsimplified walk
  with a first-hit stop gets the same answer in one process; the cost question that remains is the
  negative answer's, and §8 F3 leaves the cap to the caller's budget.
- **Leaving the spelling in unit 19's §4.** That is the state this finding came out of: one command
  in prose, a resolution in §8 that the command does not implement, and no arm that could tell them
  apart.

## 5. Production-readiness checklist

- security — this predicate is one half of a guard that keeps a run from granting itself authority. It
  reads the commit graph and a tracked path and writes nothing, so the run it grades cannot move a
  RESOLVED answer without moving history. Its BASE is the exception, and it is why S4's refusal is a
  guard rather than a nicety: the caller reads that value from the record being graded
  (`tools/unattended/check-unattended.sh:1195`), and a value that is a legal object of the wrong type
  turns the exclusion off while the probe goes on answering (§4).
- perf / scale — one bounded git read per parent per merge on a witness's tail, stopping at the first
  hit. A negative answer walks the range, which is the cost §8 F3 leaves open; the positive answer is
  the common one on the shapes unit 19 enumerates.
- error / empty / loading states — S4 is the whole of this row: cannot-answer is a third outcome and
  never a quiet no, and an empty BASE reaches it through a refusal in front of the walk rather than
  through whatever the walk happens to print.
- observability — the cannot-answer line names the commit and the path it could not resolve, so a
  fail-closed stop is attributable to the probe rather than to the walk that consumed it.
- risks — a caller that treats cannot-answer as no, which turns a broken probe into a confident
  fail-closed stop. Nothing here can see that; the separation of the two outcomes is what makes it
  visible to the caller's own arms.
- testing — the arms of S5, over scratch fixture repos built by the leg suite. Both signs are
  asserted, because an arm that only proves the flag finds MORE cannot tell a fix from a predicate
  that now matches everything.
- migration — none. No stored shape changes and no record is re-graded by this unit alone, because
  nothing calls the predicate at its commit.
- user docs — N/A — the predicate is kit-internal and no user-facing page describes it; the authority
  rule's carriers belong to other units.

## 6. Acceptance criteria

- **AC1** — When the predicate in `tools/unattended/lib-unattended.sh` is called over a fixture whose
  witness is a merge that resolves the run-state path to the other side's content, it answers YES for
  the parent from which the run's touching commit is reachable, and the arm asserts the simplified
  spelling answers nothing for that same parent — rows 1 and 2 of §4's measurement table, reproduced
  by the suite rather than quoted from this spec.
  Red when: the walk is simplified, so the merge is pruned for that path, neither parent reads as the
  run side, a caller's walk stops with no exclusion, and an owner's default-branch grant reds a record
  that can then never be cleared.
  new arm: staged RED first. The arm may not pass until it has been SEEN RED with the simplified
  spelling in place.
  permission: the criterion asserts the PREDICATE's answer, because check 19 grades no `may:` grant at
  HEAD — at `tools/unattended/check-unattended.sh:1432-1455` it grades the authorization mode, the
  playbook and the piece count — and unit 19's cross-run arm is the first caller, at a LATER order.
  The check-19 verdict half is therefore observed at unit 19's commit and not in this unit's pass.
- **AC2** — When the same fixture's probe in `tools/unattended/lib-unattended.sh` is asked about the
  parent from which NO touching commit is reachable, it answers no, so exactly one side is excluded and the walk descends rather than
  stopping.
  Red when: the unsimplified walk reports a hit for a parent reaching no touching commit, so every
  merge reads as both sides and the fail-closed stop fires on correct histories.
- **AC3** — When the probe in `tools/unattended/lib-unattended.sh` is pointed at a BASE that is not an
  object, it reports cannot answer on its own line naming the commit and the path, textually distinct
  from the no answer. When it is pointed at an EMPTY BASE it reports the same way, and the arm asserts
  it did so WITHOUT walking — so the verdict does not depend on which range spelling the build chose.
  When it is pointed at a BASE that is a legal object of another TYPE, a blob or a tree sha, it
  reports the same way, and the arm asserts the probe gave NO ANSWER rather than a yes.
  Red when: an unresolvable range returns the same empty as a completed clean walk, so a broken probe
  is indistinguishable from an honest negative and the caller stops fail-closed for the wrong reason;
  or the empty BASE is handed to the walk, which under the range spelling exits 0 printing nothing and
  reports a confident NO for a fact nobody resolved — rows 3 and 5 of §4's BASE table, and the shape
  `tools/memory-tree/row_grammar.py:337-338` already records on a different path class; or the refusal
  tests only that BASE is non-empty, so a blob or tree sha passes it, `^<object>` excludes nothing,
  and the probe answers a confident YES over the whole history for a range it never applied — row 4
  of that table, which is the caller's exclusion turned off by a value the graded run wrote.
  new arm: staged RED first for the empty-BASE half, with the range spelling in place, since the caret
  spelling passes that arm for free and would certify coverage this predicate does not have; and
  staged RED first for the wrong-type half against a non-empty test, which no spelling catches.
- **AC4** — When `git grep -c` runs over `tools/unattended/lib-unattended.sh` for the header sentence
  naming the simplification, it returns 1 at this unit's commit and 0 at its parent, and that sentence
  names both the TREESAME shape that triggers it and the existence-only limit of S2.
  Red when: the flag lands with no clause beside it, so the next reader removes it as redundant on a
  walk that is already path-restricted.
- **AC5** — When the arms of S5 land, `.memory-tree.conf`'s executed-assertion floor for
  `tools/unattended/check-unattended.sh` reads a higher armed count at this unit's commit than at its
  parent, read with `git show` at both.
  Red when: arms land and the floor holds, so deleting them later costs nothing.
  figure: DERIVED at observation time from the two commits; no count is written into this spec.
  permission: the floor is graded by the harness-arms leg over the real tree, which this run may not
  execute; the observation is made at the build's one post-build bar.

## 7. Gates

`unattended kit gate` · `harness arms (fail branches armed or pinned)` · `shell hygiene (a loop fed by a command substitution)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: `tools/unattended/check-unattended.test.sh` · a merge resolving the run-state path to the
other side's content, graded from both parents, a BASE that is not an object, an empty BASE, and a
BASE that is a blob or a tree sha · the leg suite's
executed-assertion floor, and `ARMS_FLOORS` for `tools/unattended/check-unattended.sh`

## 8. Open questions

- **F1** — Which reading? Options: (a) the unsimplified walk; (b) per-parent merge diffs; (c) walk the
  range and diff every commit.
  RESOLVED (agent, 2026-09-20, delegated): (a). §4's table measures (a) right on both signs; (b) is
  the spelling the rotation-mode record already measured disagreeing with the others on this repo's
  own history; (c) is correct and unbounded for the answer that already costs the most.
- **F2** — Where does the predicate live? Options: (a) `tools/unattended/lib-unattended.sh`, beside
  the exclusion function that calls it; (b) inline in the leg.
  RESOLVED (agent, 2026-09-20, delegated): (a). Unit 19 places the exclusion function there and
  shares it with a later unit, so an inline copy would be a second spelling of one rule in a file
  whose own header says that is what it exists to prevent.
- **F3** — Does the negative answer need a cap, and what does a truncated walk mean? A positive answer
  stops at the first hit; a negative walks the range, which on a long-lived default branch is every
  commit since BASE. S4 already gives truncation somewhere to go, since a truncated negative is a
  cannot-answer and not a no. What the cap VALUE should be belongs with the caller's own budget, which
  unit 19 sets when it wires the walk. Left OPEN on that ground: this unit's scope binds either way.

## 9. Revision log

- rev-1 · 2026-09-20 · initial draft, promoted from the G3 round-2 spec audit's H6, and the same
  day's promotion close-out: S4, S5, §4 and AC3 gained the EMPTY-BASE case after the verifier
  reproduced the range spelling exiting 0 printing nothing, byte-identical to the honest no, while
  the caret spelling fails closed — so the refusal moved in front of the walk rather than resting on
  a spelling §8 does not fix; and AC1 now asserts the predicate's own answer, since check 19 grades
  no `may:` grant until unit 19 lands · and the verifier pass that followed widened that refusal from
  non-empty to RESOLVES-TO-A-COMMIT (S4, S5, §4's table and prose, AC3, §5's security row, §7) after
  measuring a blob or tree sha exit 0 and answer a commit, with the exclusion silently dropped.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "reachability of a commit touching a path from a merge
parent"` returns no seam for this work: its ranked candidates are python path helpers in the map and
govkit kits, none above fan-in 2, and its own header prints `unscanned layers: .sh`, which is the
layer this predicate is written in. So no existing seam fits, and the evidence is that the corpus the
probe reads does not contain the layer. The prior art it cannot see was found by reading source: the
same flag and the same rationale at `tools/drift-audit/drift_report.py:806-818`, and the measurement
of three spellings disagreeing on this repo's own archives at
`tools/memory-tree/row_grammar.py:335-340`. This unit reuses that reading rather than either call
site, both of which answer different questions.

Recall terms used: `python tools/memory-recall/query.py "why does a path-scoped rev-list miss a merge
and when must history simplification be turned off" --terms "rev-list history simplification TREESAME
--full-history merge parent exclusion run-state path cross-run arm reachable BASE"`. It returned the
drift signal's own spec, which is where the flag's rationale entered this corpus, and the spec audit
entry this unit is promoted from.
