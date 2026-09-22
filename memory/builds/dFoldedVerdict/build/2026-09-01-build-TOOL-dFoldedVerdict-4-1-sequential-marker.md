# TOOL-dFoldedVerdict-4 — the hook admits one loop, and only under a marker that names its bound

**Serves:** journal TOOL-dFoldedVerdict-4

*Node `d`, 2026-09-01, owner-present build under `memory/guides/BUILD-METHOD.md`.*

## What binds now

`tools/hooks/agent-cap.js` admits an `agent()` inside a `for` / `while` body under
`gov:sequential-agents(<K>)` on the loop header, and under nothing else. The spelling is the owner's
ruling of 2026-09-01.

The conflict it resolves was exact: `TOOL-cBriefedPilot-21` ratified `parallelism route: none` while
this hook denied a loop-body `agent()` unconditionally. **Bounded-parallel was permitted by the hook
and forbidden by the verdict; strictly sequential was required by the verdict and forbidden by the
hook.** A harness iterating a build's units sat in that gap and could not be written at all.

EIGHT clauses must all hold and the refusal names the FIRST that fails. Two carry the weight:

- the loop must iterate a **bare identifier this file already proves bounded**. The marker's number
  is the author's claim; the receiver is what makes the total real. Without this clause
  `gov:sequential-agents(5)` over an unbounded array would be admitted while spawning one agent per
  element, which is the shape the owner ruling names as the thing to refuse.
- the **one-call sweep**, judged after the scan because it is a property of a GROUP and no per-line
  pass can see one. Two awaited calls in one marked body spend twice the bound, so the marker would
  name a number the loop does not obey. F2 resolved to land this here rather than file it: a stated
  2x fail-open inside the guard's own admission path is the thing this unit exists to avoid.

Nested loops fail closed with no extra clause — the brace walk stops at the first enclosing loop, so
an inner loop needs its own marker and its own receiver.

## The unmarked denial keeps its exact bytes

A loop carrying no marker produces the shipped sentence with no suffix, byte for byte. That is
deliberate and it is why several existing arms stayed green: the marker is an AFFORDANCE, and a
refusal that changed wording for everyone would have made this unit's diff look like a rewrite of the
rule rather than an addition to it. A marked loop that fails a clause gets the same sentence plus
` — <the clause that failed>`.

## Evidence

**Evidences:** TOOL-dFoldedVerdict-4

`bash tools/hooks/agent-cap.test.sh` — **160 passed, 0 failed**, up from 149 passed / 1 failed at the
pre-image (that one failure was the deployed copy having drifted, which S10 fixes).

- **AC1** — the existing `rule2: loop-built thunks → deny` fixture still denies, and so does the new
  `seq: an unmarked loop is denied exactly as before` arm. This is the arm proving the marker did not
  weaken the rule for anyone who does not write it.
- **AC2** — a script binding `const MAX = 5` with a five-element literal receiver, a marked header
  and one awaited call **exits 0**. The admit path, observed.
- **AC3** — the same with a bare array LITERAL receiver and `gov:sequential-agents(3)` also exits 0.
- **AC4** — `const units = findings.map(...)` under the same marker **exits 2**, stderr naming the
  receiver `units` as one this file does not show to be bounded.
- **AC5** — a bare `gov:sequential-agents` with no bound token exits 2: `carries no bound token, and
  a bare marker claims concurrency one with an unbounded total`.
- **AC6** — a `gov:sequential-agents(K)` bound the file cannot RESOLVE exits 2 in both shapes that
  look resolved and are not: `(args && args.cap) || 5`, the caller-settable knob wearing a
  constant's clothes, and a `.length` expression. Arms `seq: an or-bound K → deny` and `seq: a .length K → deny`.
- **AC7** — `gov:sequential-agents(9)` exits 2 naming a bound this file does not resolve to an
  integer no greater than 5. Resolved by `boundedK` and by nothing else, per S3.
- **AC8** — a body reading `out.push(() => agent(...))` exits 2. It names the AWAIT clause rather
  than the thunk clause, because the clauses are ordered and that fixture breaks C7 first — which is
  why the C8 fixture below keeps its `await`.
- **AC9** — a body collecting an unawaited `agent(...)` exits 2 on the await-adjacency clause.
- **AC10** — a `gov:sequential-agents` token inside a single-quoted string on a non-loop line
  blesses nothing: the loop below it is denied with the plain unmarked sentence, because no claim was
  made on its own header.
- **AC11** — two awaited `agent(` calls in one marked body exit 2, stderr naming the sweep:
  `admits ONE awaited agent() in its body and this body holds 2`.
- **AC12** — the no-regress property line reads `population 1316 scanned` with 54 denied at BASE,
  0 denials lost and 1 ratified. Zero lost over 1316 real scripts, and the ratification count is
  non-zero, which is what stops that branch passing by never running.
- **AC13** — the `nrfix` fixture holding an UNMARKED braceless loop is denied by BOTH hooks, so it
  contributes to `denied` and to neither `lost` nor `ratified`. That is the control proving the
  affordance is scoped to the marker and not to loops in general.
- **AC14** — the ratification strip is CLASS-SCOPED, keyed on `gov:sequential-agents` and on no
  path list: a lost denial is ratified only when deleting every such token from that file's bytes
  RESTORES the denial. No `GOV_BASE_SHA` bump either. Exactly one ratification fired, on the marked fixture.
- **AC15** — `bash tools/workflows/check-verifier-fanout.sh` exits 0 over the committed harnesses.
- **AC16** — `bash tools/check-agent-cap-restatement.sh` reports `clean — 78 markdown file(s)
  scanned, 2 waiver(s)` after the carriers moved.
- **AC17** — `grep -c 'gov:sequential-agents' tools/hooks/README.md` returns a hit; the README OWNS
  the grammar and the charter is untouched, which N4 requires.
- **AC18** — `diff tools/hooks/agent-cap.js .claude/hooks/agent-cap.js` reports no difference, and
  `bash tools/check-kit-versions.sh` exits 0 with `KIT_AGENT_CAP_VERSION` at 1.11 across every
  carrier its own derived population names — including both `scratch-guard.js` copies, which carry
  the agent-cap marker and which a "both copies of agent-cap" reading would have missed.
- **AC19** — `python tools/lexicon/lexicon.py` reports `P1 verb graded=1035 offenders=461`, the
  pinned figure. It read 463 first: the new predicate was called `seqRefusal`, whose leading token
  `seq` is not in the declared table, once per deployed copy. `--suggest` was asked rather than
  guessed and returned the table; renamed `checkSeqMarker`, and the count returned to 461.
- **AC20** — `gov:sequential-agents` appears in the hook, its deployed copy, the test suite, the
  README, the REVIEW-PROTOCOL template and its render, and both amended dossiers.

## What this pass did NOT do, and one clause it could not reach

**C5 was never observed failing.** It refuses a marker sitting on a line that is not a loop header in
the literal-blanked view. Every fixture that puts the marker inside a string ends up with the marker
on a DIFFERENT line from the loop header, which C2 refuses first by finding no claim at all. C5 is a
defensive ordering clause and it is shipped unexercised — stated here rather than counted as covered,
because an arm I could not write is not an arm.

`for await (` and `do { … } while ( )` still bypass the loop ban outright, both measured. That is a
hole in the DENY side; this unit widened the ADMIT side, and one closing diff carrying both widenings
is unreviewable. Filed as `TOOL-dFoldedVerdict-8`.

`tools/workflows/unattended-build.js` was NOT rewritten into a per-unit loop. Its `ordered` list
comes from `--plan` and is not a receiver this hook can size, so this unit does not by itself make
that loop legal — only a loop over a bounded grouping of it. Both forced shapes in that file's header
comment are kept because both remain CORRECT, and the comment now says which and why.

**A dossier overflow this unit caused, and one it inherited.** The S11b amendment pushed
`memory/map/features/unattended.md` past `DOSSIER_CAP_BYTES` and it took three compressions to fit —
it now sits at 20478 of 20480. Separately, `TOOL-dFoldedVerdict-3` landed a map-coverage RED: it
created `memory/gotchas/one-value-field-records-a-mixed-outcome.md` and regenerated the build index
but not the map, so the new `gotcha-classes` key went unclaimed. Claimed here in
`memory/map/features/build-method.md`, which already owns the two fold classes and is the right home
for an M4 disposition rule — and not in the unattended dossier, which had no bytes for it.
