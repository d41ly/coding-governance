**Serves:** research TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-34

# Brief: dPlacedRequest's specs cross-checked against the unread parent revision `63669d505`

## The prompt

> Cross-read and re-ground seven dClosedLoop chain builds against two parent revisions they have never
> read: `dWitnessedBar`, `dPlacedRequest`, `dTotalRecall`, `dRankedPlan`, `dDeclaredLoop`,
> `dLinkedLibrary` and `dIndexedDesign`. dIndexedDesign also gets a FULL first cross-read against all
> its parents, since it has never had one. The owner asked for this on 2026-11-05.

— the dClosedLoop session's hand-off to this session, 2026-11-05, relaying the owner's ask after a
verification that found two parent revisions never read by their children.

## The brief

### Goal

Classify every assumption the named dPlacedRequest specs make about a revised parent unit as AGREES, MISMATCH
or UNKNOWN UNTIL BUILT, against the parents' specs (dDeclaredLoop) as they stand on origin/main at `ab976b5b3`.
This build's last cross-read was `2740f0a3d`. Since then `git log 2740f0a3d..ab976b5b3 -- memory/builds/<parent>/spec/`
names only these revisions, generated-region rewrites and a no-op merge apart:

- **`63669d505`** (2026-11-02, TOOL-dFoldedAudit-8, the owner's 2026-11-01 ruling on spec audits):
  TOOL-dDeclaredLoop-20 rev-3 (§4's `item.review.dispose` row, S9), TOOL-dDeclaredLoop-32 rev-3 (§1, S2,
  S3, S4, §4's `review_state` grammar, AC11) and TOOL-dFairHearing-17 rev-4 (§3's chain non-goal). Its
  record is `memory/builds/dFoldedAudit/build/2026-11-01-build-TOOL-dFoldedAudit-8-deviation-81.md`;
  `git show 63669d505 -- memory/builds/dDeclaredLoop/spec/ memory/builds/dFairHearing/spec/` shows
  what moved.

`git show 2740f0a3d:<spec>` reads a parent as this build's last cross-read read it.

The first population is by citation (4 specs): 3 (dl20 at :182, :342), 5 (dl20 at :70, :89, :267,
:280, :288), 7 (dl20 at :71, :174, :402) and 34 (dl20 at :269). No spec cites dl32 or fh17.

The second population is by rule. The SA probe (`review_state`, `no-fall`, `NON-CONVERGENT`,
`non-decrease`, `strict fall`, `precision floor`, `until-clean`, `review.design.rounds`,
`promotion_target`, `item.review.dispose`, `chain stop`, `review.max-rounds`, `review.follow-up`,
`rework budget`) named 3 (:383), 14 (:40, :246, :252) and 16 (:28, :84).

One line more, not a row: TOOL-dTotalRecall-2 rev-8, this build's child, now asks pr34 S22's `--lease
status` for a seventh TAB field after `<epoch>`, the six-field prefix kept (tr2:345-369). Say whether
any dPlacedRequest spec (pr34 S22 and AC22 first, pr34:106-109, :468-470) pins the line at exactly six
fields, so that the asked field would red it.

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
  Quote both sides with `file:line`, and state in one or two sentences the change the dPlacedRequest spec
  needs.
- **UNKNOWN UNTIL BUILT:** neither spec decides it, and only the parent's build run can.

Groups, one reviewer each. The spec your task block's `input:spec` names leads one group. Check every
spec of that group, and no other:

- **Group A, citation and SA, led by spec 3:** specs 3, 5, 7, 14, 16, 34. Check every assumption 3, 5, 7 and 34 make about dl20, and apply SA to all six.

The spec files are `memory/builds/dPlacedRequest/spec/2026-1?-??-spec-TOOL-dPlacedRequest-<n>.md`, and a parent's are
`memory/builds/<parent>/spec/2026-1?-??-spec-<FAMILY>-<parent>-<n>.md`. Read every mention of a
parent unit in each of your specs, then the cited parent text, its §9 rev lines first. A sibling
session is folding the owner's picks on the chain's open forks into some of these specs concurrently;
read `ab976b5b3` as it is, and the main loop re-checks your rows after that fold lands. The precedent
cross-check, `memory/builds/dShippedRelease/build/2026-11-03-build-DEPL-dShippedRelease-1-parents-crosscheck.md`,
shows the shape and the classes that turned up.

Aliases: `dlN:L` dDeclaredLoop, `fhN:L` dFairHearing, `trN:L` dTotalRecall, `prN:L` dPlacedRequest, `wbN:L` dWitnessedBar, `rpN:L` dRankedPlan, `llN:L` dLinkedLibrary, `idN:L` dIndexedDesign, `ksN:L` dKeptSession, `brN:L` dBoundRoles, `ocN:L` dOrderedCharter: line L of that build's spec N at `ab976b5b3`.

Return, in this shape and nothing else:

1. A table, one row per assumption: `| Spec | Assumption about the parent | Rule | Verdict | Evidence |`,
   with `prN:L` for line L of dPlacedRequest spec N and the aliases above for the parents. `Rule` is `cite`
   for a citation assumption, else the rule's tag.
2. Per MISMATCH, a bullet: both sides quoted, then `Change:` and the revision the dPlacedRequest spec needs,
   then `Cause:` either the revision (the parent text moved in the commit you name) or pre-existing (it
   already read so at the build's last cross-read, `2740f0a3d`).
3. Per UNKNOWN UNTIL BUILT, one line on what decides it.
4. Per rule-wide hit a rule does not bind, one line saying why. And the one line on `--lease status`'s seventh field.
5. One line per citation spec: the revised parent sections it cites that none of its assumptions
   depend on.
6. Parent text that looks wrong, one line each: never a row, never an edit.

### Non-goals

- No file is written: every probe reads.
- No re-audit of rules an earlier re-ground applied and this build's last cross-read already read.
- No defect in dPlacedRequest's own design that no parent unit causes.
- No verdict on a parent spec: parent text that looks wrong is one line under 6, never a row.
- No read of dOrderedCharter's or dFairHearing's build runs, live on another node: their specs on
  origin/main only.
