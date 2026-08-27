# TOOL-aPrimedKeepalive-2 — the adoption rule: a strictly beneficial discovery joins the running build, decided at once

**Status:** CLOSED · rev-3 · 2026-08-27 · node a · Tier-2 · base b4e1d5be · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-27-build-TOOL-aPrimedKeepalive-1-7-acceptance-ledger.md](../build/2026-08-27-build-TOOL-aPrimedKeepalive-1-7-acceptance-ledger.md) | journal | TOOL-aPrimedKeepalive-1 TOOL-aPrimedKeepalive-3 TOOL-aPrimedKeepalive-4 TOOL-aPrimedKeepalive-5 TOOL-aPrimedKeepalive-6 TOOL-aPrimedKeepalive-7 TOOL-aPrimedKeepalive-8 TOOL-aPrimedKeepalive-9 |
| [2026-08-27-prompt-TOOL-aPrimedKeepalive-1-1.md](../prompts/2026-08-27-prompt-TOOL-aPrimedKeepalive-1-1.md) | research | TOOL-aPrimedKeepalive-1 TOOL-aPrimedKeepalive-3 TOOL-aPrimedKeepalive-4 TOOL-aPrimedKeepalive-5 |
| [2026-08-27-review-TOOL-aPrimedKeepalive-1-6-spec-audit-round1.md](../reviews/2026-08-27-review-TOOL-aPrimedKeepalive-1-6-spec-audit-round1.md) | spec-audit | TOOL-aPrimedKeepalive-1 TOOL-aPrimedKeepalive-3 TOOL-aPrimedKeepalive-4 TOOL-aPrimedKeepalive-5 TOOL-aPrimedKeepalive-6 |
| [2026-08-27-review-TOOL-aPrimedKeepalive-1-7-spec-audit-round2.md](../reviews/2026-08-27-review-TOOL-aPrimedKeepalive-1-7-spec-audit-round2.md) | spec-audit | TOOL-aPrimedKeepalive-1 TOOL-aPrimedKeepalive-3 TOOL-aPrimedKeepalive-4 TOOL-aPrimedKeepalive-5 TOOL-aPrimedKeepalive-6 TOOL-aPrimedKeepalive-7 |
| [2026-08-27-review-TOOL-aPrimedKeepalive-1-7-spec-audit-round3.md](../reviews/2026-08-27-review-TOOL-aPrimedKeepalive-1-7-spec-audit-round3.md) | spec-audit | TOOL-aPrimedKeepalive-1 TOOL-aPrimedKeepalive-4 TOOL-aPrimedKeepalive-6 TOOL-aPrimedKeepalive-7 |
| [2026-08-27-review-TOOL-aPrimedKeepalive-1-9-closing-diff.md](../reviews/2026-08-27-review-TOOL-aPrimedKeepalive-1-9-closing-diff.md) | diff-review | TOOL-aPrimedKeepalive-1 TOOL-aPrimedKeepalive-3 TOOL-aPrimedKeepalive-4 TOOL-aPrimedKeepalive-5 TOOL-aPrimedKeepalive-6 TOOL-aPrimedKeepalive-7 TOOL-aPrimedKeepalive-8 TOOL-aPrimedKeepalive-9 |

<!-- /gen:spec-records -->

## 1. Goal

An unattended run that finds something good outside its scope currently parks it and waits for a
reader who has left. Every mechanism adoption needs already exists — M2's ADD act, M3's delegated
scope, the `--rescope` verb — and nothing tells a run to use them. State the rule, with a test that
keeps it from becoming a licence to widen a build on taste.

## 2. Scope (IN)

- **S1** — a new numbered section in `tools/unattended/PROTOCOL.template.md` states the adoption
  rule. It lives there rather than in the build method because M10's delta 1 already owns "never ask,
  and here are the substitutes" and because the protocol has the HEADROOM, not because it is
  unbudgeted — **it is budgeted, and the first draft of this line said otherwise.** Hygiene check 6
  caps every `memory/guides/*.md` at `GUIDE_CAP_BYTES=61440` and `GUIDE_CAP_LINES=750`, and
  `.memory-tree.conf` does not override either. Measured: 613 lines / 50 437 B at BASE.
- **S2** — the rule defines DISCOVERY, defines STRICTLY BENEFICIAL as a three-part test rather than
  an adjective, and names the disposition for a discovery that fails each part.
- **S3** — the rule covers a BLOCKER the run can resolve, not only a discovery it would be nice to
  have. This widening is evidenced: this run reproduced the defect by asking the owner about a
  blocker whose resolution it had already measured.
- **S4** — the rule states that adoption is the M2 ADD act and nothing new, names `--rescope` as the
  verb that records it, and states the re-push obligation the `published` anchor imposes on a grown
  roster.
- **S5** — `memory/guides/BUILD-METHOD.md` M10's first delta gains ADOPT in its substitute list,
  which today reads *"The substitutes are derive, park and abort"*, and points at the new protocol
  section. It states no rule of its own: M1 forbids a rule stated both there and in a carrier M11
  points at.
- **S6** — the Skill's "While it runs" section gains the counterweight to its park bullet, so a
  reader meeting `--park` also meets what may not be parked.
- **S7** — all three renders are regenerated in the same commit.

## 3. Non-goals (OUT)

- Widening M3's two bounds. The GOAL statement stays unamendable and the governance-carrier clause
  stays an owner turn. Adoption ADDS a unit beside the goal; it never rewrites the goal, and M2's
  ADD act is already delegated, so this unit grants no authority that does not already exist.
- A new verb. `--rescope --act add` already writes the row and needs no sibling.
- A machine check that a run adopted what it should have. Nothing can observe a discovery a run did
  not record, so the rule has no gate — stated in the contract rather than implied away.
- Any change to `--park`. Parking stays correct for what the test excludes, and its refusals are
  untouched.
- The `discoveries-adopted` directive handle. That is `TOOL-aPrimedKeepalive-3`, sequenced after
  this one because a directive whose carrier section does not exist yet points at nothing.

## 4. Design

### What the rule says

**A DISCOVERY is anything the run learns that it was not looking for** — a defect in a path it read,
a measurement that contradicts a record, a cheaper mechanism for something the tree already does, or
a blocker standing between the run and its own landing. Orientation is where most of them happen,
and orientation is before the spec set exists, which is why the rule binds from the run's first act
rather than from its first pass.

**STRICTLY BENEFICIAL is a test.** A discovery qualifies when all three hold:

1. it makes an observable this repo ALREADY measures strictly better — a gate that reds where it
   should, a leg that costs less wall clock, a record that stops being false — and the improvement is
   MEASURED, not argued;
2. nothing this repo measures gets worse: no acceptance criterion, no gate leg, no declared budget
   or pin, no security, data or write surface;
3. it survives M3's three vetoes unchanged.

**The dispositions, and choosing between them is not optional.** Fails 1 or 2 → a BACKLOG row naming
what was seen and why it was declined; that is a decision the run TOOK. Trips a veto → PARKED with
the question, the options and the refusal; that is a decision the run REFUSED. Passes all three →
ADOPTED, now, by the run that found it.

**Veto 2 is the one that bites**, and the rule says so: a discovery needing a new dependency, a new
install location, a new public surface or a change to a governance carrier is an owner turn.

### Why the rule has to say "at once"

A discovery adopted late costs a second pass over the same code. A discovery deferred costs the whole
finding, because the reader it is deferred to is the one who left. `aGroundedOrientation` measured a
sixteen-fold improvement, parked it, was told to proceed, and parked it again — the second park is
the evidence that "record it and move on" is not a stable state under a mandate.

### What it does NOT license

Not a licence to widen a build with work that is merely good. A refactor nobody measured, a rename, a
"while we are here" is not a discovery — it is taste, and taste is the owner's. Clause 1's word is
MEASURED: a run that cannot state the measurement has not made a discovery.

### Where it goes, and where it does not

The protocol, because it is the binding contract for unattended runs and — measured, not assumed —
has the headroom. It carries a real budget: check 6's `GUIDE_CAP_LINES=750`, against 613 lines at
BASE. This build spends about 68 of the 137 remaining lines, which is HALF the remaining headroom in
one build and is the number the next author needs. NOT the build method: M10's delta 1 already owns "never ask, and here are the substitutes", and
adoption is a fourth substitute for asking rather than a fourth delta. M10 therefore gains one word
and a pointer, keeping "Three deltas, and no others" true.

### Migration

**Price the edit against the BINDING half, which is the TEMPLATE.** At BASE
`tools/memory-tree/BUILD-METHOD.template.md` sits 19 B under M1's 24 576 B budget while
`memory/guides/BUILD-METHOD.md` sits 30 B under it; the 11 B gap is the render substitution and is
structural, not slack. Sizing against the render is how this build spent 8 B it did not have — guide
24 573, template 24 584 — and only AC6 caught it, after the bytes were gone. M1's budget is a
governance carrier's own stated constraint that M3's delegation does not reach, so this unit may not
raise it.
The M10 edit is priced first; if it does not fit, the donor is M1's own budget-history paragraph,
which narrates three past raises that git already records and which charter §5's derive-over-author
rule makes removable. Re-measure with `wc -c` over BOTH halves, never from a number in a spec, and let the template's
figure decide.

### Files touched (estimate)

`tools/unattended/PROTOCOL.template.md` · `tools/unattended/SKILL.template.md` ·
`tools/memory-tree/BUILD-METHOD.template.md` · the three installed copies.

### Alternatives rejected

**State the rule in `BUILD-METHOD.md` M10 as a fourth delta.** It is where a reader of the method
would look, and it costs a bullet the file has no bytes for. Rejected on M1's budget, which this run
may not raise, and on M10's own structure: adoption is a substitute for asking, and delta 1 is the
"never ask" delta.

**Make adoption conditional on the discovery being inside the build's stated goal.** That is the
current behaviour by omission and it is what parked the hygiene fix: a run's goal rarely covers what
it stumbles on. Rejected because it would ratify the defect.

**Leave the disposition open — "adopt, park or backlog, use judgement".** A rule whose branches are
not decided is a rule that resolves to whatever the run already wanted to do, which is parking.

## 5. Production-readiness checklist

- security — clause 2 names security, data and write surfaces explicitly, so a discovery touching one
  cannot qualify; clause 3 routes it to veto 3.
- perf / scale — N/A.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — the two failure dispositions ARE the branches, and both are
  specified rather than left to judgement.
- observability — an adopted discovery leaves a `--rescope` row, a spec and a unit in the roster; a
  declined one leaves a backlog row; a parked one leaves a parked entry. All three are readable
  after the fact, which is the property parking-everything destroyed.
- risks — the real risk is scope creep dressed as adoption. Clause 1's MEASURED requirement and the
  explicit "not a licence" paragraph are the fence; there is no machine half and §3 says so.
- testing + left-shift gates — the parity legs cover the renders. The rule is prose an agent reads.
- migration / rollback — documentation only; revert is the rollback. The budget migration is in §4.
- user docs — the Skill is the user doc and S6 is in scope.

## 6. Acceptance criteria

- **AC1** — When `memory/guides/UNATTENDED-PROTOCOL.md` is read, it carries a numbered section
  stating the adoption rule, and that section defines DISCOVERY and gives the three-clause test.
- **AC2** — When that section of `memory/guides/UNATTENDED-PROTOCOL.md` is read, it names all three
  dispositions — adopt, backlog, park — and binds each to a specific clause failure rather than to
  judgement.
- **AC3** — When that section is read, it names `--rescope --act add` as the recording verb and
  states the re-push obligation a grown roster carries on the `published` anchor.
- **AC4** — When that section of `memory/guides/UNATTENDED-PROTOCOL.md` is read, it states that a
  BLOCKER the run can resolve is a discovery, citing this run's own reproduction of the defect.
- **AC5** — When `memory/guides/BUILD-METHOD.md` M10 is read, its first delta's substitute list names
  ADOPT and points at the protocol section, and M10 still opens "Three deltas, and no others".
- **AC6** — When `wc -c` runs over BOTH `memory/guides/BUILD-METHOD.md` and
  `tools/memory-tree/BUILD-METHOD.template.md`, each is at or below `24576`. The template is the
  tighter half by 11 B and grading only the render passes over a breach.
- **AC9** — When `wc -lc memory/guides/UNATTENDED-PROTOCOL.md` runs, it is at or below
  `GUIDE_CAP_LINES=750` and `GUIDE_CAP_BYTES=61440`, and the wrap-up states the remaining headroom in
  lines, because half of it was spent here.
- **AC7** — When `.claude/skills/unattended/SKILL.md` "While it runs" is read, the park bullet is
  followed by the counterweight naming what may not be parked.
- **AC8** — When `bash tools/unattended/check-unattended.sh` runs, check 10 is green and the
  `unattended skill wiring` leg is green.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `memory tree hygiene` · `kit version markers` ·
`template size`, and `bash tools/run-gates/run-gates.sh` at the push boundary.

## 8. Open questions

none

## 9. Revision log

- rev-3 · 2026-08-27 · folded spec-audit round 2, finding 10. rev-2 fixed AC6 to grade both halves
  and left §4's Migration paragraph pricing the edit against the render, 11 B too generous — so the
  builder's own sizing number stayed wrong while the criterion that catches the overrun was correct.
- rev-2 · 2026-08-27 · folded spec-audit round 1, findings 12 and 23. S1 and §4 claimed the protocol
  "has no byte budget"; it has one — check 6's guide caps — and that false clause was the sole stated
  reason for choosing this carrier over the build method. Replaced with the measured headroom and a
  criterion that grades it. AC6 now grades both halves of the BUILD-METHOD pair.
- rev-1 · 2026-08-27 · initial draft. S3's widening — a blocker counts as a discovery — comes from
  the owner's correction of this run's own AskUserQuestion, recorded in the prompt record.

## 10. Reuse audit

The seams this unit wires through, all cited by path and all verified at BASE:

- `memory/guides/BUILD-METHOD.md` M2's AMEND act, which already names RETIRE, SUPERSEDE and ADD.
- M3's delegation sentence, which already extends a standing mandate to "that build's own scope by
  M2's AMEND acts" — so the AUTHORITY exists and only the instruction to use it is missing.
- `tools/unattended/unattended.sh`'s `--rescope` verb, which already records the row and already
  refuses a removal, because the authorization compares BASE against HEAD as a subset.
- `memory/guides/UNATTENDED-PROTOCOL.md` section 10's pointer-not-copy design, which is the shape the
  M10 edit follows.

No new mechanism is built, which is the finding: `python tools/memory-recall/query.py` with terms
`keepalive preflight orientation park discovery scope rescope amend mandate delegated fork veto stall
unattended directive` returned `dUnstalledConvoy-4`'s spec — the unit that ADDED the amendment
vocabulary — and its own §10 records the same conclusion one level up. The gap was never authority
or machinery; it was the decision rule.
