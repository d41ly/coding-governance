# TOOL-aPairedLexer-10 — a name only ONE view binds is a disagreement, not an exemption

**Status:** SPECCED · rev-2 · 2026-08-31 · node a · Tier-2 · base 72dff924 · streams tooling · order 9

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-31-prompt-TOOL-aPairedLexer-6.md](../prompts/2026-08-31-prompt-TOOL-aPairedLexer-6.md) | research | TOOL-aPairedLexer-6 TOOL-aPairedLexer-7 TOOL-aPairedLexer-8 TOOL-aPairedLexer-9 TOOL-aPairedLexer-11 TOOL-aPairedLexer-12 |
| [2026-08-31-review-TOOL-aPairedLexer-6-7-8-9-10-11-12-spec-audit-round1.md](../reviews/2026-08-31-review-TOOL-aPairedLexer-6-7-8-9-10-11-12-spec-audit-round1.md) | spec-audit | TOOL-aPairedLexer-6 TOOL-aPairedLexer-7 TOOL-aPairedLexer-8 TOOL-aPairedLexer-9 TOOL-aPairedLexer-11 TOOL-aPairedLexer-12 |

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
- **S2** — sweep `\b(?:const|let|var)\s+(\w+)\s*=` over `_bl.code` and delete every name the clean
  view SAW but refused to resolve. A declaration the trusted view examined and rejected is stronger
  evidence than one the untrusted view invented.
- **S3** — re-baseline `rule3: an exposed const resolves the cap and the script admits` as a DENY
  with a clearer message. Resolving a cap out of a view the file has declared untrustworthy is the
  fail-open direction, and that arm pins it as the admit direction today.
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
- **AC4** — When the re-baselined arm runs, `rule3: an exposed const resolves the cap and the script
  admits` denies, and its replacement name states that a binding visible only to the distrusted view
  does not resolve a cap.
- **AC5** — When a script's view is CLEAN, `intConsts` binds the same table as before this unit,
  no name is deleted, and the verdict is unchanged.
- **AC6** — When a name is bound by BOTH views but the clean view SAW it in a declaration it
  refused to resolve (a real `const K = args.width` OUTSIDE any mis-lexed span, with the prose
  integer inside one), the denial names `K` as unresolvable. This is S2's own criterion, and it
  FAILS with S1 alone — without it S2 could be omitted entirely and nothing would red.
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

## 10. Reuse audit

Probes as `TOOL-aPairedLexer-6` §10, same session, same terms. **The seam is the cross-check
`TOOL-aPairedLexer-4` added, and this unit corrects its merge rule rather than adding a second
mechanism.** `intConsts` and `boundedK` are the existing consumers and neither changes signature.
`TOOL-aPairedLexer-11` then hoists the corrected merge so rule 2 shares it — which is the reuse this
finding's sibling exists to perform.
