# TOOL-dScriptedRepeat-3 — the playbook validity gate

**Status:** SPECCED · rev-4 · 2026-08-20 · node d · Tier-2 · base d2a40aa8 · streams tooling · ratified 2026-08-20

## 1. Goal

Gate a playbook file: its canon, its declared step selector and floor, the `GATE`/`CHECK` tag grammar
over every step it selects, the witness drain census, and whether each named leg is actually runnable
— with a declared coverage mode and a NAMED refusal wherever it cannot see.

## 2. Scope (IN)

- **S1.** `tools/unattended/check-playbook.sh`, a new merge-bar leg over every tracked file that IS a
  playbook. Membership is TREE-DERIVED, not seam-derived: a tracked file is in the population when it
  carries unit 2's declaration block, or matches a glob the project declares. Unit 4's `playbook:` is a
  POINTER INTO that population, never its definition — the previous revision defined the population as
  "what the declaration seam names", which excluded the fixture this same spec ships, excluded a freshly
  created playbook no README names yet (unit 11's whole output), and contradicted F2's ruling that a
  tracked playbook is graded from the moment it is tracked. It is a LEG rather than a check inside the existing kit gate because it runs
  over a different population — an adopter's playbooks, not the kit's own tree — and because unit 4
  makes its input a second blob read.
- **S2.** The DECLARED STEP SELECTOR. A playbook declares `step_selector` in its declaration block, as
  a regular expression, plus `step_floor`, a shrink-only minimum count. The gate refuses a selector
  that matches fewer lines than the floor. This exists because the two reference playbooks disagree by
  construction about what a step is — nine or zero, depending on whose regex — so a hardcoded selector
  reports "every step is tagged" over an EMPTY selection on one of the two files the canon was derived
  from. That is green-by-absence inside the rule meant to prevent it.
- **S3.** The TAG GRAMMAR. Every selected step carries `GATE <leg>` or `CHECK <why>`. Parsing is
  STRUCTURAL over the step's whole window, bounded at the next step OR the next heading, never
  line-wise: in the reference, two invariants have never once been validated by the reference's own
  validity gate because they appear only in line-wrapped tags.
- **S4.** The WITNESS DRAIN CENSUS. A `CHECK` may carry `· witness <field>`. The gate validates every
  witness present, counts them against the total, PRINTS the drain, and does not red on absence. Fork
  11's ruling, with the census as the thing that makes voluntary adoption visible.
- **S5.** The RUNNABILITY ORACLE. A playbook declares `legs`, mapping each leg NAME used in a `GATE`
  tag to a RESOLVABLE TARGET — an argv, or a path that must exist in the adopting tree. The codomain is
  specified because without it the oracle compares a document's tags against a table inside that same
  document, which is the assertion-between-two-derived-values class unit 1 names. The gate reds a `GATE`
  naming a leg absent from the registry AND a registry ENTRY whose target does not resolve.
- **S5b.** `coverage` is DECLARED and GRADED, not merely recorded. Each mode is defined by what the
  oracle does: `resolvable` = every target resolves, and a playbook declaring it over an unresolvable
  target REDS; `probe` = existence-only, with its incompleteness printed on every run; `dark` = a named
  refusal. An UNDECLARED mode reds. Three modes with no observable difference would be a declaration
  nothing grades, which is the defect this key exists to avoid.
- **S6.** The CANON check: the twelve required sections present, in order, each non-empty, each either
  filled or carrying `none — <why>`. Present-but-empty and `none — <why>` are distinguished.
- **S7.** The EXEMPLAR check: a quoted sentence in a playbook must be marked prohibited or point at a
  tracked fixture path that resolves.
- **S8.** The DERIVED LENGTH BUDGET, computed per addressable segment and printed on every run.
- **S9b.** THE LEG'S VERDICT CHANNEL, named against what the runner can actually express.
  `tools/run-gates/run-gates.sh:844-849` maps a leg's own exit: `0` prints `GATE ok`, anything else
  `GATE FAIL`; `skip` comes ONLY from a guard file written before dispatch, and `run-gates.test.sh`
  refuses a guard pathspec matching no tracked path. So a leg cannot say `skipped`, and this repo tracks
  no playbook — meaning this leg would print `GATE ok` over an empty population forever while unit 5's
  reader, unit 7's set records and unit 8's refusal all rode on it. The leg therefore exits NON-ZERO on
  an empty PLAYBOOK population and prints an enumerated-count line, and ships ONE TRACKED FIXTURE
  PLAYBOOK under `tools/unattended/` so the dogfood population is never empty and a guard on that path
  passes the canary.
  **THE PIECE level is graded differently, and the two must not share one rule.** The fixture ships
  pieces under its own grain AND the verb-written records for them, so the piece population is non-empty
  too. But a zero-PIECE enumeration is REPORTED and non-blocking on the leg, per unit 5 S9's grading
  rule — the reader classifies and never grades. The previous revision's single rule ("non-zero when it
  can name a population and resolves none of it") reached the piece level too and therefore either red
  the dogfood bar permanently or re-opened green-by-absence, with no spec saying which.
- **S9c.** `curated:` is resolved HERE rather than deferred. The gate reds a playbook whose `curated:`
  is absent or empty, with no run binding involved — the freeze is a tree property like everything else
  this leg reads, and it is the only machine consequence fork 4 has. Unit 2 AC5 states the same rule.
- **S9.** A self-test, `check-playbook.test.sh`, with every arm's failing case staged and observed RED
  before the arm lands. The candidate predicates in S2, S3 and S7 are run over BOTH reference
  playbooks first, printing hits AND near-misses, before any of them is wired.

## 3. Non-goals (OUT)

- The gate does not judge whether a step is a GOOD step, whether a `CHECK`'s `<why>` is true, or
  whether a leg passes. It reads SHAPE. Its own header says so, per the charter's rule that a gate
  states what it does not check — and the reason is that a structural check reads as a semantic one to
  everybody who did not write it.
- No opinion on content kind. A playbook that emits executables is the ordinary case for a playbook
  that generates tests, which the owner's ask names as a content kind.
- No migration of existing playbooks. Fork 11's soft witness rule and S2's DECLARED selector exist so
  a playbook written before this gate can declare its own shape and pass.

## 4. Design

### Why the selector is declared and not fixed

A fixed selector is the defect. Measured on the two references: one carries many step-shaped lines
under a bold-id regex and the other carries NONE under that same regex while carrying nine numbered
steps under a different one. A kit-fixed selector therefore either misses one file's steps entirely —
and reports every step tagged over an empty set — or is loose enough to select prose. Declaring it
moves the choice to the author, who knows; the FLOOR is what stops the author declaring a selector
that quietly selects nothing. The reference implementation already ships this guard, redding when its
own step count falls below a floor, which is the precedent.

### Why the window is structural

A step's tag may be line-wrapped. Reading tags line-wise silently drops those, and the reference
corpus contains live instances of exactly that: leg names that appear only in wrapped tags and are
therefore invisible to the gate that claims to validate every tag. The window runs from a selected
step to the next selected step or the next heading, whichever comes first — the reference's own window
rule, which has an observed failing case recorded in its source.

### The coverage mode, and the named refusal

Borrowed in substance from the lexicon kit's coverage modes. A playbook declares how well its leg
registry can decide runnability: fully resolvable, probe-only, or explicitly dark. An UNDECLARED
coverage mode is a named refusal, never a silent skip, because a gate that quietly skips what it
forgot looks exactly like coverage. An unarmed predicate REDS rather than passing green.

The research established that this is the one place fork 5 needed new machinery and that a lens
recommending REUSE was wrong: the unattended kit never reads this repo's gate manifest, and an adopter
receives no such file. The registry is therefore a per-playbook declaration, which is also where it
belongs — the legs a playbook's steps name are a property of that playbook.

### What this gate cannot see, stated in its own header

A `CHECK` whose `<why>` is false. A `GATE` whose named leg exists and does not test what the step
says. A step that is followed in letter and violated in spirit. A playbook that is internally
consistent and wrong about its subject. Each is named in the script header, and S4's census is the
only quantitative handle on the third.

## 5. Production-readiness checklist

- security — the gate reads playbook files and a declared registry. It does not EXECUTE a declared
  leg during validation; runnability is a registry-membership question, not an invocation. Stated
  because executing an adopter-declared command from a gate would be a new execution surface.
- perf / scale — one pass per tracked playbook; the population is small by construction.
- a11y — N/A.
- i18n — the tag keywords are ASCII and closed; a playbook's prose is not constrained.
- error / empty / loading states — no playbook in the tree is NOT a legitimate state: the leg exits
  non-zero and the bar prints `GATE FAIL` with the reason. There is no `skipped` verdict a leg can emit,
  which S9b establishes and this row previously contradicted. A declared selector matching zero lines
  reds via the floor; a zero-PIECE enumeration is reported and does not red here.
- observability — the drain census and the derived budget print on every run, so a playbook's
  trajectory is visible without opening it.
- risks — the biggest is a gate that passes because its predicate never matched. S9's requirement to
  run every candidate predicate over both references first, printing hits and near-misses, is the
  control, and it is the charter's rule rather than this spec's invention.
- testing + left-shift gates — S9. No arm lands without its RED observed.
- migration / rollback — a new leg. It joins `tools/gate-legs.json` and a `[[gate_leg]]` row in
  `kit.toml`; the research measured that adding a leg trips a GROWING set of meta-gates, so the full
  bar runs rather than a named list.
- user docs — the template (unit 2) documents the declaration block; this gate's header documents its
  own blind spots.

## 6. Acceptance criteria

- **AC1** — When a playbook declares a `step_selector` matching fewer lines than its `step_floor`,
  `bash tools/unattended/check-playbook.sh` REDS naming both numbers. Staged and observed.
- **AC2** — When a step carries a LINE-WRAPPED `GATE` tag, the gate SEES it. Verified by staging the
  wrapped form and observing the tag counted; the reference implementation fails this case today, which
  is why it is an acceptance criterion and not an assumption.
- **AC3** — When a step is untagged, `bash tools/unattended/check-playbook.sh` REDS naming the
  step's own id and line.
- **AC4** — When a `GATE` names a leg absent from the declared `legs` registry, the gate REDS.
- **AC5** — When no `coverage` is declared, the gate REDS with a named refusal, and the message states
  that a missing declaration is not a pass. Observed, because a silent skip is the failure mode.
- **AC5b** — When a playbook declares `coverage = resolvable` and one registry target does not resolve,
  `bash tools/unattended/check-playbook.sh` REDS. Staged and observed — this is what makes the
  declaration graded rather than recorded.
- **AC5c** — When `curated:` is absent or empty, `bash tools/unattended/check-playbook.sh` REDS.
  Staged and observed.
- **AC6** — When `check-playbook.sh` runs over BOTH reference playbooks unmodified, its output names
  every hit AND near-miss and the run does not claim coverage it does not have. This is a measurement
  gate on the gate, run before wiring.
- **AC7** — When a required canon section is present but EMPTY the gate REDS; when it carries
  `none — <why>` the gate PASSES. Two arms, because one arm cannot distinguish them.
- **AC8** — When no tracked file carries a declaration block or matches the declared glob,
  `bash tools/unattended/check-playbook.sh` exits non-zero and the bar prints `GATE FAIL` with the
  reason; and when the shipped fixture is the only playbook, the leg exits 0 having enumerated a
  non-zero playbook population AND a non-zero piece population, printing both counts. Two arms against
  the TREE-DERIVED predicate of S1, and the second is what proves the first is not a permanent red.
- **AC8b** — When a playbook resolves zero pieces under its grain, the leg REPORTS the dead probe with
  its count and exits 0; the same tree at `--close` BLOCKS via `pieces-complete`. Two observations of
  one state, which is what keeps the leg's grading rule and unit 5 S9's from contradicting each other.

## 7. Gates

The new leg itself, plus `bash tools/unattended/check-playbook.test.sh`,
`bash tools/govkit/govkit.py selfcheck` (a leg needs a `[[gate_leg]]` row in its kit's `kit.toml`, or
an exempt row), and `bash tools/run-gates/run-gates.sh` in full — the meta-gate set that a new leg
trips grows, so the full bar is the check rather than an enumerated list.

## 8. Open questions

none — every fork below is RESOLVED in place.

- **F1 — one leg or a check inside the existing kit gate?** RESOLVED (agent, 2026-08-20, delegated): a
  SEPARATE leg, and the cheaper option is declined deliberately. A check inside the kit gate costs less
  meta-gate churn, but this predicate's population is an ADOPTER's playbooks rather than the kit's own
  tree, and it needs a second blob read. Folding an adopter-facing predicate into the kit's self-check
  would make one leg answer two questions about two populations, which is the two-answers defect one
  level up. The meta-gate cost is paid rather than avoided.
- **F2 — does the gate red on a playbook whose `curated:` line is absent?** RESOLVED (agent,
  2026-08-20, delegated) in S9c: YES, with no run binding. The previous revision deferred this to unit
  4, which has no notion of an ACTIVE playbook and never received the deferral, while unit 2 AC5
  asserted the opposite answer — three specs, two rulings and a dangling handoff. A draft not ready to
  be graded is not yet a tracked playbook.

## 9. Revision log

- rev-4 · 2026-08-20 · folded the round-2 spec audit, which returned BLOCKED at precision 0.625 over
  the fold range. Every change here repairs a place where two sentences in this build ordered opposite
  implementations and neither was marked the loser.
- rev-3 · 2026-08-20 · pre-code fork sweep under the mandate (M3). Every §8 fork RESOLVED in
  place with its resolver and authority named, and §8's first non-blank line made machine-legal —
  the driver classified nine of eleven specs FORKED on that line alone.
- rev-1 · 2026-08-20 · initial draft. S2's declared selector and S3's structural window both come from
  measured defects in the reference implementation of this same rule.
- rev-2 · 2026-08-20 · folded the M4 spec audit. F11 is the important one: the `skipped` verdict four
  specs rested on does not exist in the gate runner's leg protocol, so this leg would have printed
  `GATE ok` over an empty population forever while carrying the mode's entire enforcement. S9b names the
  real channel and ships a tracked fixture playbook. F12 gave the `legs` registry a codomain and made
  `coverage` graded. F13 resolved `curated:` here instead of deferring it to a unit that never received
  the deferral.

## 10. Reuse audit

The COVERAGE-MODE-with-a-named-refusal shape is the lexicon kit's and is reused in substance: declare
per subject how completely the predicate can decide, refuse an undeclared one, and never let an
unarmed predicate pass green. The WINDOW rule and the step FLOOR are both reused from the reference
implementation, which already ships them with observed failing cases in its own source — this is the
rare case where the prior art is in another repository and is still the best available evidence,
because it is the only running implementation of this exact predicate. The ARM discipline (an arm
carries the branch's entire literal signature, and adding branches renumbers per-check ordinals) is
this repo's, and applies unchanged. No existing seam covers the tag grammar or the drain census; those
are genuinely new. Recall terms used: gate leg predicate selector floor window structural tag census
coverage mode named refusal unarmed green by absence arm signature staged red.
