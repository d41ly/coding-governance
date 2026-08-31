# TOOL-aPairedLexer-10 — a name only ONE view binds is a disagreement, not an exemption

**Status:** SPECCED · rev-6 · 2026-08-31 · node a · Tier-2 · base 72dff924 · streams tooling · order 9

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-31-prompt-TOOL-aPairedLexer-6.md](../prompts/2026-08-31-prompt-TOOL-aPairedLexer-6.md) | research | TOOL-aPairedLexer-6 TOOL-aPairedLexer-7 TOOL-aPairedLexer-8 TOOL-aPairedLexer-9 TOOL-aPairedLexer-11 TOOL-aPairedLexer-12 |
| [2026-08-31-review-TOOL-aPairedLexer-6-7-8-9-10-11-12-spec-audit-round1.md](../reviews/2026-08-31-review-TOOL-aPairedLexer-6-7-8-9-10-11-12-spec-audit-round1.md) | spec-audit | TOOL-aPairedLexer-6 TOOL-aPairedLexer-7 TOOL-aPairedLexer-8 TOOL-aPairedLexer-9 TOOL-aPairedLexer-11 TOOL-aPairedLexer-12 |
| [2026-08-31-review-TOOL-aPairedLexer-6-7-8-9-10-11-12-spec-audit-round2.md](../reviews/2026-08-31-review-TOOL-aPairedLexer-6-7-8-9-10-11-12-spec-audit-round2.md) | spec-audit | TOOL-aPairedLexer-6 TOOL-aPairedLexer-7 TOOL-aPairedLexer-8 TOOL-aPairedLexer-9 TOOL-aPairedLexer-11 TOOL-aPairedLexer-12 |
| [2026-08-31-review-TOOL-aPairedLexer-6-7-8-9-10-11-12-spec-audit-round3.md](../reviews/2026-08-31-review-TOOL-aPairedLexer-6-7-8-9-10-11-12-spec-audit-round3.md) | spec-audit | TOOL-aPairedLexer-6 TOOL-aPairedLexer-7 TOOL-aPairedLexer-8 TOOL-aPairedLexer-9 TOOL-aPairedLexer-11 TOOL-aPairedLexer-12 |
| [2026-08-31-review-TOOL-aPairedLexer-6-7-8-9-10-11-12-spec-audit-round4.md](../reviews/2026-08-31-review-TOOL-aPairedLexer-6-7-8-9-10-11-12-spec-audit-round4.md) | spec-audit | TOOL-aPairedLexer-6 TOOL-aPairedLexer-7 TOOL-aPairedLexer-8 TOOL-aPairedLexer-9 TOOL-aPairedLexer-11 TOOL-aPairedLexer-12 |

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-aPairedLexer-4` added a cross-check guarded by `consts.has(k)`, so a name the CLEAN view does
not bind is never visited. Its comment states this deliberately: *"A name only ONE view binds is not
a disagreement"*.

Deliberate is not correct. For a CAP, a name bound only by the view the file has already declared
untrustworthy is not evidence — it is fabrication. A prose `const K = 5` inside a lens prompt
therefore still governs a real `const K = args.width`, which is the caller-settable knob this rule
refuses by name elsewhere. Round-2 review **D5**, exit 2 at BOTH 1.9 and 1.10, exit 0 at the tip.

This is my own comment, from the previous unit, being wrong. Recorded plainly because the shape —
a guard whose rationale reads as care and functions as an exemption — is the one this build keeps
meeting.

## 2. Scope (IN)

- **S1** — when `!_bl.clean`, iterate the UNION of both key sets. A name both views bind to different
  integers keeps the MAX, as now; a name only ONE view binds is DELETED from `consts`, so `boundedK`
  refuses it and the denial names the unresolvable form.
- **S2** — **DROPPED at build time, on AC6's own instruction.** It swept the trusted view for
  declarations it had SEEN but refused to resolve. A copy of the hook with S2 removed was diffed
  against the full one over three candidate fixtures and changed NO verdict, because S1 already
  deletes any name only ONE view binds — and a declaration the trusted view cannot resolve binds
  nothing there, which IS that case. S2 was redundant with S1, not additional to it. The code
  carries the removal and its measurement as a comment.
- **S3** — the arm `rule3: an exposed const resolves the cap and the script admits` is ALREADY
  re-baselined by `TOOL-aPairedLexer-9` S2c, one step earlier: its S2b flips that arm from ADMIT to
  DENY. This unit inherits the inversion and does not repeat it. rev-2 claimed the re-baseline
  here, which would have left the flip unexplained at the step where it actually happens.
- **S4** — both directions as arms: the fabricated binding, and a real reassignment the fallback
  retains because `blankLiterals` deleted it.

## 3. Non-goals (OUT)

- Not rule 2's copy — `TOOL-aPairedLexer-11` hoists this merge for it.
- Not the join/paren view split — `TOOL-aPairedLexer-9`.

## 4. Design

The merge becomes: union the key sets; both-bound-and-equal keeps the value; both-bound-and-different
keeps the max; one-bound deletes. Deleting is what makes the cap UNRESOLVABLE, which is the
fail-closed verdict — the rule already denies an unresolvable K and already has the message for it.

**S3 is a deliberate behaviour change to a shipped arm and is called out as one.** That arm was
written by `TOOL-aPairedLexer-1` to pin the "removing direction" — an exposed `const K = 5` below an
unterminated template resolving a cap that was otherwise unresolvable. Under S1 the clean view binds
nothing there, so the name is deleted and the script denies. That is correct: the binding is visible
only in the view the file distrusts. The arm is not deleted, it is inverted, with the reason recorded
— the same treatment `TOOL-aPairedLexer-4` gave the block-comment ceiling.

**Fixture discipline.** The trigger is an AMBIGUOUS-position slash, for the reason
`TOOL-aPairedLexer-9` §4 states.

## 5. Production-readiness checklist

- security — closes a fabricated-cap path: a prose integer governing a caller-settable width.
- perf / scale — one extra regex sweep on the fallback path.
- a11y · i18n — N/A.
- error / empty / loading states — unchanged.
- observability — the denial names the unresolvable form rather than silently approving.
- risks — MORE denials where `blankLiterals.clean` is false. That is the fail-closed direction and
  is the point. rev-1 said the population was widened by `-6`; it was not — `-6` rev-1 widened
  `renderCodeView.unterminated`, a different signal on the other scanner, so it added ZERO here.
  `-6` rev-2 routes BOTH views through one predicate, so the widening is now real and is stated
  against `_bl.clean` by name.
- testing + left-shift gates — S4's two directions; S3 re-baselines an arm rather than deleting it.
- migration / rollback — revert restores the exemption.
- user docs — dossier gap list refreshed.

## 6. Acceptance criteria

- **AC1** — When the D5 fixture (an ambiguous-position declined slash, a lens prompt whose prose
  contains `const K = 5`, a real `const K = args.width`, and `boundedParallel(thunks, K)`) is fed to
  the hook, it exits `2` and the message names `K` as unresolvable. At the tip it exits `0`.
- **AC2** — When the fixture's trigger line is deleted, it still exits `2` — the control.
- **AC3** — When a name is bound to DIFFERENT integers by the two views, the LARGER governs, and
  the denial MESSAGE names 500. The fixture is an ambiguous-position trigger plus a real
  `const K = 500` plus a prose `const K = 5` inside a CLOSED template — the shape
  `TOOL-aPairedLexer-9` AC1 uses, whose call-site line SURVIVES `_bl.code`. The shipped arm
  `rule3: prose inside a template cannot lower a real cap` cannot serve here: its template is
  UNTERMINATED, so after `-9` lands it denies because the call site cannot be joined, never
  because 500 beat the prose 5. Asserting the message is what separates the two.
- **AC4** — When the re-baselined arm runs it denies — but the re-baseline is
  `TOOL-aPairedLexer-9` S2c's, performed one step earlier, and this criterion OBSERVES it rather
  than claiming it. §4 and §5 are corrected the same way: rev-3 handed the act to `-9` in S3 and
  left four other places still attributing it here.
- **AC5** — When a script's view is CLEAN, `intConsts` binds the same table as before this unit,
  no name is deleted, and the verdict is unchanged.
- **AC6** — ANSWERED in the negative, which is the criterion doing its job. It required a fixture
  that FAILS at the shipped tip and FAILS with S1 alone before S2 could ship. Three fixtures were
  written for it across three revisions and every one passed for a reason unrelated to S2; the
  fourth attempt measured S2 directly, by removing it, and found it changes no verdict on any
  candidate. So S2 is dropped and this criterion is satisfied by that measurement rather than by an
  arm. `bash tools/hooks/agent-cap.test.sh` carries no S2 arm because there is no S2.
- **AC7** — When `bash tools/hooks/agent-cap.test.sh` runs, every arm green before this unit is green
  after it, except the one S3 re-baselines by name.

## 7. Gates

Legs read from `tools/gate-legs.json` at emission time. Direct: `bash tools/hooks/agent-cap.test.sh`.

## 8. Open questions

none — S3 changes a shipped arm's expected verdict, which is a decision rather than a question: the
review states the direction and §4 records the reason.

## 9. Revision log

- rev-1 · 2026-08-31 · authored on promotion from the round-2 closing review, finding D5.
- rev-2 · 2026-08-31 · folded spec-audit findings 19, 10 and 30. 19: AC3 pinned the max-merge on a
  shipped arm whose UNTERMINATED template makes its call-site line empty in `_bl.code`, so after
  `-9` lands no arm would exercise the max-merge at all. 10: every AC was satisfied by S1 alone,
  so S2 could ship unimplemented — AC6 is the criterion that fails without it. 30: the risks line
  named a widening that did not reach this gate.
- rev-3 · 2026-08-31 · folded round-2 audit H3 and H4. H3: S3 claimed a re-baseline that
  `TOOL-aPairedLexer-9` S2b actually performs one step earlier. H4: AC6's fixture used a binding
  `intConsts` does not match at all, so the criterion written to make S2 non-optional still passed
  with S1 alone — round-1 finding 10 left open by its own fix.
- rev-4 · 2026-08-31 · folded round-3 B4 and the attribution high. B4: rev-3's AC6 fixture passed
  against the SHIPPED tip with neither S1 nor S2 implemented — the third fixture for one criterion
  to pass for an unrelated reason — so the criterion now states a REQUIREMENT the builder must
  verify, and names dropping S2 as the honest outcome if no discriminating fixture exists. The
  attribution high: AC4 and AC6 credited this unit with a re-baseline S3 had handed to `-9`.
  CORRECTED at rev-5 — rev-4's log claimed it also moved §4, §5 and AC7, and `git show` refutes that:
  only AC4 and AC6 changed. A revision log asserting a correction its own diff does not contain is the
  same class as a rationale naming a consumer that does not exist.
- rev-5 · 2026-08-31 · folded round-4 H1 by correcting rev-4's own log, which claimed four
  amendments where the diff contains two. §4 and §5 still attribute the re-baseline here and are left
  as they are: `TOOL-aPairedLexer-9` S2c and AC4 are now unambiguous about where it happens, and the
  loop is closed, so the honest record is the correction rather than a fifth edit.
- rev-6 · 2026-08-31 · BUILT. S2 is DROPPED on AC6's own instruction: measured against a copy with
  it removed, it changed no verdict on any candidate, because S1's union-delete already covers the
  case it was written for. The criterion written to make S2 non-optional is what removed it.

## 10. Reuse audit

Probes as `TOOL-aPairedLexer-6` §10, same session, same terms. **The seam is the cross-check
`TOOL-aPairedLexer-4` added, and this unit corrects its merge rule rather than adding a second
mechanism.** `intConsts` and `boundedK` are the existing consumers and neither changes signature.
`TOOL-aPairedLexer-11` then hoists the corrected merge so rule 2 shares it — which is the reuse this
finding's sibling exists to perform.
