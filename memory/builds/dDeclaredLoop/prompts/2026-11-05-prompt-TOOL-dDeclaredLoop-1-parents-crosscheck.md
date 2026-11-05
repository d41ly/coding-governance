**Serves:** research TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-56

# Brief: dDeclaredLoop's specs cross-checked against the unread parent revision `63669d505`

## The prompt

> Cross-read and re-ground seven dClosedLoop chain builds against two parent revisions they have never
> read: `dWitnessedBar`, `dPlacedRequest`, `dTotalRecall`, `dRankedPlan`, `dDeclaredLoop`,
> `dLinkedLibrary` and `dIndexedDesign`. dIndexedDesign also gets a FULL first cross-read against all
> its parents, since it has never had one. The owner asked for this on 2026-11-05.

— the dClosedLoop session's hand-off to this session, 2026-11-05, relaying the owner's ask after a
verification that found two parent revisions never read by their children.

## The brief

### Goal

Classify every assumption the named dDeclaredLoop specs make about a revised parent unit as AGREES, MISMATCH
or UNKNOWN UNTIL BUILT, against the parents' specs (dOrderedCharter and dFairHearing) as they stand on origin/main at `ab976b5b3`.
This build's last cross-read was `783f1ad3a`. Since then `git log 783f1ad3a..ab976b5b3 -- memory/builds/<parent>/spec/`
names only these revisions, generated-region rewrites and a no-op merge apart:

- **`63669d505`** (2026-11-02, TOOL-dFoldedAudit-8, the owner's 2026-11-01 ruling on spec audits):
  TOOL-dDeclaredLoop-20 rev-3 (§4's `item.review.dispose` row, S9), TOOL-dDeclaredLoop-32 rev-3 (§1, S2,
  S3, S4, §4's `review_state` grammar, AC11) and TOOL-dFairHearing-17 rev-4 (§3's chain non-goal). Its
  record is `memory/builds/dFoldedAudit/build/2026-11-01-build-TOOL-dFoldedAudit-8-deviation-81.md`;
  `git show 63669d505 -- memory/builds/dDeclaredLoop/spec/ memory/builds/dFairHearing/spec/` shows
  what moved.

`git show 783f1ad3a:<spec>` reads a parent as this build's last cross-read read it.

The first population is by citation: every spec that cites TOOL-dFairHearing-17, as
`TOOL-dFairHearing-17`, a bare `dFairHearing-17` or `fh17` (2 specs): 21 (fh17 at :56, :62, :126,
:197, :301) and 32 (fh17 at :354, :397). Spec 32 is itself revised by `63669d505`; read its
citations of fh17 as they stand at rev-3.

The second population is the revision's siblings. `63669d505` revised two of this build's own
units, dl20 and dl32, from another build (TOOL-dFoldedAudit-8), after every other dDeclaredLoop spec
was written and cross-read; no sibling has read them since. A text probe for `review_state`,
`no-fall`, `NON-CONVERGENT`, `non-decrease`, `strict fall`, `precision floor`, `until-clean`,
`review.design.rounds`, `promotion_target`, `item.review.dispose`, `chain stop`, `review.max-rounds`,
`review.follow-up` and `rework budget`, outside the generated regions, named these candidates: 2, 10,
13, 14, 18, 22, 30, 31, 33, 48, 49, 50 and 56. A sibling relying on dl20's dispose row or S9, or on
dl32's stopping rule, target rule or `review_state` grammar, is bound by SA as if it cited them.

The probes are a heuristic. Verify every hit: a hit no rule binds is a line in your return, not a row.

The rules, as the parents now state them. The parent specs win where this summary differs:

- **SA, the spec-audit rules (`63669d505`).** A spec subject, a spec audit under
  `review.design.rounds`' `until-*`, `one` or `fixed-count` values, leaves the strict-fall exit:
  `verb_review` passes `review_state` a sixth argument, `no-fall`, so the subject ends at its target or
  its bound and never NON-CONVERGENT, and whether another generation runs is the chain's derived
  verdict (`--chain-verdict`, BUILD-METHOD M4), not the loop's (dl32:47-55, the grammar at :123-125,
  AC11 at :330-336). A spec subject's promotion target is always ` · to units`, and `promotion_target`
  is not called for it (dl32:56-63). Closing-review follow-ups under `while-*` and fix passes keep the
  strict-fall rule. `review_state` reads `<prior counts> <count> <bound> [<route-backs>] [<target>]
  [<no-fall>]`. TOOL-dDeclaredLoop-20 rev-3: the `item.review.dispose` row sends a local finding on an
  unbuilt spec to `item.review.fold`, and only built work or a new mechanism to units or asks by
  `review.findings` (dl20:128); S9 points at BUILD-METHOD M4's disposal paragraphs as
  TOOL-dFoldedAudit-1 rewrote them (dl20:86-89; `memory/guides/BUILD-METHOD.md:146`, a spec exit
  disposes by nature). TOOL-dFairHearing-17 rev-4: a chain's stop is M4's derived verdict, and the
  precision floor has left M4 (fh17:64-65; `memory/guides/BUILD-METHOD.md:148`). A spec that ends a
  spec audit NON-CONVERGENT on a non-decrease, routes a spec audit's findings by the rework budget or to
  asks, disposes a spec-audit finding by severity, gives `review_state` a fixed shape a sixth argument
  breaks, or reads a precision floor or `REVIEW_ROUNDS` as a chain's stop, is a MISMATCH when it relies
  on one of the three revised units for that.

Verdicts:

- **AGREES:** today's parent text says what the assumption says, whether or not a revision touched it.
- **MISMATCH:** today's parent text says something else: a moved reader, a fork resolved another way,
  a section renumbered or a line cite moved, a refusal the parent now states, or a rule above broken.
  Quote both sides with `file:line`, and state in one or two sentences the change the dDeclaredLoop spec
  needs.
- **UNKNOWN UNTIL BUILT:** neither spec decides it, and only the parent's build run can.

Groups, one reviewer each. The spec your task block's `input:spec` names leads one group. Check every
spec of that group, and no other:

- **Group A, citation, led by spec 21:** specs 21, 32. Check every assumption each makes about fh17, and apply SA to the same specs.
- **Group B, siblings, SA only, led by spec 30:** specs 2, 10, 13, 14, 18, 22, 30, 31, 33, 48, 49, 50, 56. Check every assumption each makes about dl20 and dl32 against their rev-3 text, and SA.

The spec files are `memory/builds/dDeclaredLoop/spec/2026-1?-??-spec-TOOL-dDeclaredLoop-<n>.md`, and a parent's are
`memory/builds/<parent>/spec/2026-1?-??-spec-<FAMILY>-<parent>-<n>.md`. Read every mention of a
parent unit in each of your specs, then the cited parent text, its §9 rev lines first. A sibling
session is folding the owner's picks on the chain's open forks into some of these specs concurrently;
read `ab976b5b3` as it is, and the main loop re-checks your rows after that fold lands. The precedent
cross-check, `memory/builds/dShippedRelease/build/2026-11-03-build-DEPL-dShippedRelease-1-parents-crosscheck.md`,
shows the shape and the classes that turned up.

Aliases: `dlN:L` dDeclaredLoop, `fhN:L` dFairHearing, `trN:L` dTotalRecall, `prN:L` dPlacedRequest, `wbN:L` dWitnessedBar, `rpN:L` dRankedPlan, `llN:L` dLinkedLibrary, `idN:L` dIndexedDesign, `ksN:L` dKeptSession, `brN:L` dBoundRoles, `ocN:L` dOrderedCharter: line L of that build's spec N at `ab976b5b3`.

Return, in this shape and nothing else:

1. A table, one row per assumption: `| Spec | Assumption about the parent | Rule | Verdict | Evidence |`,
   with `dlN:L` for line L of dDeclaredLoop spec N and the aliases above for the parents. `Rule` is `cite`
   for a citation assumption, else the rule's tag.
2. Per MISMATCH, a bullet: both sides quoted, then `Change:` and the revision the dDeclaredLoop spec needs,
   then `Cause:` either the revision (the parent text moved in the commit you name) or pre-existing (it
   already read so at the build's last cross-read, `783f1ad3a`).
3. Per UNKNOWN UNTIL BUILT, one line on what decides it.
4. Per rule-wide hit a rule does not bind, one line saying why.
5. One line per citation spec: the revised parent sections it cites that none of its assumptions
   depend on.
6. Parent text that looks wrong, one line each: never a row, never an edit.

### Non-goals

- No file is written: every probe reads.
- No re-audit of rules an earlier re-ground applied and this build's last cross-read already read.
- No defect in dDeclaredLoop's own design that no parent unit causes.
- No verdict on a parent spec: parent text that looks wrong is one line under 6, never a row.
- No read of dOrderedCharter's or dFairHearing's build runs, live on another node: their specs on
  origin/main only.
