# TOOL-cBriefedPilot-15 — M6's parallelism inversion, or the finding that it has no mechanism

**Status:** OPEN · rev-2 · 2026-08-14 · node c · Tier-2 · base 37c05e1b · streams tooling

## 1. Goal

Under a standing mandate, make concurrency the claim that is OWED rather than the claim that must be
substantiated — but only if unit 21 finds a route that dispatches a build pass without voiding the
directive layer. This spec is written in two branches on purpose. If no route survives, the unit ships
that finding and M6 is left byte-unchanged, and that is a completed unit, not a failed one.

## 2. Scope (IN)

- **S1** — read unit 21's verdict token, `parallelism route: <R-id>` or `parallelism route: none`, and
  pick the branch from it. The token is the selector; no other reading of unit 21's recording decides
  this unit.
- **S2** — BRANCH A, a route survives. `tools/memory-tree/BUILD-METHOD.template.md` replaces M6's
  opening sentence with the folded one in §4, and `memory/guides/BUILD-METHOD.md` is RE-RENDERED from
  it, never hand-edited.
- **S3** — BRANCH A. M6's three conditions, the write-set rule and the fallback sentence stay
  byte-identical. The replacement is one sentence in, one sentence out.
- **S4** — BRANCH B, no route survives. M6 is not touched. The build README's design section that
  promises the inversion is corrected so the record does not describe a rule that did not ship, and
  this spec's §8 is marked RESOLVED naming unit 21's recording as the evidence.
- **S5** — either branch: the measured line and byte cost is written into §9's revision line, because
  the budget it spends is authorial and nothing else records the spend.

## 3. Non-goals (OUT)

- **Finding the route.** Unit 21 does that and is sequenced before this unit for exactly that reason.
- **Naming a route inside M6.** The mechanism clause is route-agnostic. A method section that named a
  dispatch tool would rot at the next tool change, and M1 forbids this file stating what a carrier
  owns.
- **M8, M9 and M10's pointers.** Unit 16 owns them, and its delta count depends on which branch this
  unit takes — see §4.
- **A gate over the obligation.** Nothing observes whether two passes actually ran concurrently. The
  build README classifies `parallel-when-disjoint` as observed by nothing, and this unit does not
  quietly promote it.
- **Any change to the fan-out or concurrency ceilings.** M6 already points at
  `memory/guides/REVIEW-PROTOCOL.md` for both, and this unit is about WHICH work is parallel.

## 4. Design

### The replaced sentence, branch A

Out, at `memory/guides/BUILD-METHOD.md` M6: *Sequence is the default; parallelism is a claim you
substantiate.* In:

> **Sequence is the default; parallelism is a claim you substantiate — except under a standing
> mandate, where the claim is owed the other way: two passes meeting all three conditions below SHOULD
> run concurrently, because nobody is waiting to be asked. The concurrency must not cost the passes
> their instruction layer or spend a budget that cannot reset inside a run; where no such mechanism
> exists for the work in hand, sequencing it is a park with a reason, not a violation.**

The second half is what unit 21 exists to keep honest. Without a surviving route the clause would be
an excusing sentence attached to an obligation nobody can discharge, which is what the owner refused
on 2026-08-14.

### The measured cost, and which cap actually binds

Measured in this worktree: `memory/guides/BUILD-METHOD.md` is 236 lines and 16466 B; the template is
236 lines and 16720 B. The replacement is 409 B longer than the sentence it replaces and turns M6's
seven-line paragraph into eleven, so branch A costs **+4 lines and +409 B**, leaving the live file at
240 lines and 16875 B.

Three caps exist and only one of them is a gate on this file:

| Cap | Value | Binding here |
|---|---|---|
| M1's own budget | 250 lines, 20 KB | authorial — nothing enforces it |
| hygiene rule 6, guides class | 750 lines, 61440 B | a gate, and far away |
| check 16 read path | 86476 B total, 68989 B measured today | a gate, and shared |

**The design pass's acceptance criterion "hygiene rule 6 (≤250 lines, ≤20 KB) green" is wrong against
source and must not be copied.** Rule 6 splits by class at
`tools/memory-tree/check-memory-hygiene.sh`: a file under `memory/guides/` carries 61440 B and 750
lines, three times the row-document cap, and the comment beside the split says the line count is a
PROXY and the read-path ceiling is the real budget. So M6 could grow past 250 lines with every leg
green. The 250-line budget is M1's own sentence, justified by M7 re-reading the file whole at every
pass boundary, and the only thing that holds it is a reviewer counting. That is why S5 puts the spend
in the revision line.

The read path is shared: `memory/DECISIONS.md` and `memory/LIVE.md` are members and both grow with
this build. 17487 B of headroom is not this unit's to spend alone.

### The render discipline

The live copy is a render of the template and is never hand-edited —
`bash tools/memory-tree/kit-dogfood-parity.test.sh --render` writes template to live. Worth stating
because the parity leg is GUARDED on `tools/memory-tree/` and two `memory/` files, and
`memory/guides/BUILD-METHOD.md` is not in that guard list: a commit touching only the live copy would
SKIP the parity leg on the diff-scoped bar and be caught only at the push boundary, where
`GATE_FULL=1` bypasses every guard. Editing the template is what keeps the early signal.

### What branch B ships

M6 unedited, and the record made to match: the build README's "Three deltas" section drops the
inversion to two, and this spec closes with §8 resolved against unit 21's token. The backlog row and
the `memory/DECISIONS.md` row are unit 20's to derive — writing either here would duplicate a later
unit's job over a file M6's condition (3) names verbatim.

### Files touched (estimate)

| Branch | Files |
|---|---|
| A | `tools/memory-tree/BUILD-METHOD.template.md` · re-rendered `memory/guides/BUILD-METHOD.md` |
| B | `memory/builds/cBriefedPilot/README.md` only |

### Alternatives rejected

- **Shipping the inversion with the clause and no hunt.** The clause reads as a bound and behaves as
  an exemption when no mechanism exists. Rejected by the owner as P2.
- **Weakening M6 to a recommendation.** It is already a default plus a substantiation rule; weakening
  it removes the write-set discipline, which is the part that works.
- **Putting the inversion in M10 instead of M6.** M10 is where unattended DELTAS are indexed, but the
  rule it modifies lives in M6, and stating it in M10 would put two answers in two sections — the M1
  defect this build exists to avoid. Unit 16 adds a pointer there, not a copy.

## 5. Production-readiness checklist

- security — N/A, prose in a procedure.
- perf / scale — the file is re-read whole at every pass boundary; +409 B is the whole cost and it is
  measured above.
- a11y · i18n — N/A.
- error / empty / loading states — branch B is the empty case and is specified, not left implicit.
- observability — nothing observes whether passes ran concurrently, and the build README says so.
- risks — the obligation could be read as licence to parallelize work that is not disjoint. The three
  conditions and the write-set rule are unchanged for exactly that reason, and S3 makes their byte
  identity an acceptance item.
- testing + left-shift gates — the parity leg proves the render matches; nothing tests the rule,
  because a procedure is not executable.
- migration / rollback — one sentence; reverting the template and re-rendering is the rollback.
- user docs — the method IS the doc. The Skill's table already names the handle, unit 9.

## 6. Acceptance criteria

- **AC1** — When unit 21's recording is present, this unit's branch is chosen from its verdict token
  and §9 names which branch and why.
- **AC2** — BRANCH A: M6's opening sentence in `memory/guides/BUILD-METHOD.md` is the §4 sentence, and
  a diff of the M6 section shows exactly one sentence replaced.
- **AC3** — BRANCH A: the three numbered conditions, the write-set sentence and the ceilings pointer
  are byte-identical to their pre-change form.
- **AC4** — BRANCH A: `bash tools/memory-tree/kit-dogfood-parity.test.sh --check` is green, and the
  live copy differs from a fresh render by nothing.
- **AC5** — BRANCH A: `wc -l memory/guides/BUILD-METHOD.md` reads at most 250, and the measured value
  is written into §9. A green rule 6 is NOT the observation, because rule 6 admits 750.
- **AC6** — BRANCH B: `git diff` over `tools/memory-tree/BUILD-METHOD.template.md` and
  `memory/guides/BUILD-METHOD.md` is empty for this unit's commit, and the build README no longer
  promises the inversion.
- **AC7** — Either branch: `bash tools/memory-tree/check-method-carriers.sh` is green, so no carrier
  gained a copy of an M-section.

## 7. Gates

`kit/dogfood doc parity` (`tools/memory-tree/kit-dogfood-parity.test.sh`) ·
`method carriers (every pointer declared)` · `memory hygiene (20 checks)` · the full bar at the push
boundary. No new leg.

## 8. Open questions

none — the fork below is RESOLVED by unit 21's recorded verdict, not by an argument made here.
  The token reads `parallelism route: none`, so this unit takes BRANCH B: M6 is not touched and the
  finding ships. The evidence is `build/2026-08-15-build-cBriefedPilot-2-parallelism-routes.md`,
  which records per-route observations rather than conclusions. §8 said the resolution would be a
  READ and not a design decision, and it was.
**Which branch does this unit take?** Unresolved, and it cannot be resolved here: the resolver is
unit 21's recorded verdict token, which does not exist yet. Options are branch A, the inversion, and
branch B, the finding; both are fully specified above, so the resolution is a read, not a design
decision. Recommendation: take whichever the token names, with no adjudication — a route the hunt
recorded as failing is not rescued by an argument made in this spec. This §8 goes RESOLVED, naming
unit 21's recording, in the same commit that takes the branch; until then the unit is FORKED by M2's
classification and correctly so.

## 9. Revision log

- rev-1 · 2026-08-14 · initial draft, from the design panel at
  `build/2026-08-14-build-cBriefedPilot-1-design-pass.md` §1f and the owner's P2 resolution. Two
  corrections to that pass fold in here: its acceptance cited hygiene rule 6 at 250 lines, which is
  the ROW-document cap and not the guides cap this file falls under; and its unit-15 entry listed no
  dependency, which the owner's resolution made 21.

- rev-2 · 2026-08-15 · branch B taken on unit 21's token. M6 is UNCHANGED, so this unit spends
  ZERO lines and ZERO bytes of the method's budget — the measured cost S5 asks for, and the only
  branch where that number is nil. The build README's design section is corrected so the record
  does not describe a rule that did not ship.
## 10. Reuse audit

- **`tools/memory-tree/kit-dogfood-parity.test.sh`** — the render seam, extended by using it rather
  than by changing it. Its `PAIRS` list already carries the method pair, so a new sentence needs no
  wiring at all; the unit's whole build step is edit-then-`--render`.
- **M6's existing three conditions** — the seam inside the document. The inversion changes which way
  the claim runs and reuses the disjointness test unchanged, which is what keeps the edit to one
  sentence.
- **`tools/memory-tree/check-method-carriers.sh`** — already grades every carrier for a copied
  `## M<n>` section, so the structural half of pointer-not-copy is covered with no new registry row.

Recall terms used: parallelism concurrency pass dispatch agent spawn budget workflow sidechain hooks
directive mandate unattended write-set disjoint.

No seam exists for the obligation itself; it is a sentence, and the only machinery it needs already
renders it.
