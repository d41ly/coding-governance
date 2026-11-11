**Serves:** research TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-13 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-31 TOOL-dIndexedDesign-32 TOOL-dIndexedDesign-33 TOOL-dIndexedDesign-34 TOOL-dIndexedDesign-38 TOOL-dIndexedDesign-46

# Brief: dIndexedDesign's specs cross-checked against the parent revisions `63669d505`, `66f7b8d32` and `58b395b6e`, a full first cross-read

## The prompt

> Cross-read and re-ground seven dClosedLoop chain builds against two parent revisions they have never
> read: `dWitnessedBar`, `dPlacedRequest`, `dTotalRecall`, `dRankedPlan`, `dDeclaredLoop`,
> `dLinkedLibrary` and `dIndexedDesign`. dIndexedDesign also gets a FULL first cross-read against all
> its parents, since it has never had one. The owner asked for this on 2026-11-05.

— the dClosedLoop session's hand-off to this session, 2026-11-05, relaying the owner's ask after a
verification that found two parent revisions never read by their children.

## The brief

### Goal

Classify every assumption the named dIndexedDesign specs make about ANY unit of its parents (dDeclaredLoop, dTotalRecall, dKeptSession, dBoundRoles and dLinkedLibrary) as AGREES,
MISMATCH or UNKNOWN UNTIL BUILT, against the parents' specs as they stand on origin/main at
`ab976b5b3`.

- **`63669d505`** (2026-11-02, TOOL-dFoldedAudit-8, the owner's 2026-11-01 ruling on spec audits):
  TOOL-dDeclaredLoop-20 rev-3 (§4's `item.review.dispose` row, S9), TOOL-dDeclaredLoop-32 rev-3 (§1, S2,
  S3, S4, §4's `review_state` grammar, AC11) and TOOL-dFairHearing-17 rev-4 (§3's chain non-goal). Its
  record is `memory/builds/dFoldedAudit/build/2026-11-01-build-TOOL-dFoldedAudit-8-deviation-81.md`;
  `git show 63669d505 -- memory/builds/dDeclaredLoop/spec/ memory/builds/dFairHearing/spec/` shows
  what moved.
- **`66f7b8d32`** (2026-11-02) and **`58b395b6e`** (2026-11-03), the owner's two picks on
  TOOL-dTotalRecall-2 §8 F6: TOOL-dTotalRecall-2 rev-7 then rev-8 (§3's external edge, §4 "Minting",
  §8 F6) and TOOL-dTotalRecall-1 rev-5 (§4's writer bullet and the note under the rows). Records:
  `memory/builds/dTotalRecall/build/2026-11-02-build-TOOL-dTotalRecall-2-deviation-24.md`,
  `…/2026-11-03-build-TOOL-dTotalRecall-2-deviation-25.md` and
  `…/2026-11-03-build-TOOL-dTotalRecall-1-deviation-13.md`.

`git show 4bf0f400d:<spec>` reads a parent as this build's last cross-read read it.

This build has never been cross-read. Its spec run began at `4bf0f400d`, which holds every earlier
re-ground of its parents (dDeclaredLoop `e5de11e9e`, dTotalRecall `2bd5e10d4`, dBoundRoles
`fffe4aadf`, dKeptSession `0689e7fa1`, dLinkedLibrary `933e67399`). Since then `git log
4bf0f400d..ab976b5b3 -- memory/builds/<parent>/spec/` names three commits only: `63669d505`,
`66f7b8d32` and `58b395b6e`. This is a FULL first cross-read: every assumption a spec makes about ANY
parent unit is classified against today's text, whether or not a revision touched it.

The population is by citation: every spec citing a unit of the five parents, as `TOOL-<build>-<n>`, a
bare `<build>-<n>` or the build's bare name (23 specs). By parent unit (`dl`, `tr`, `ks`, `br`, `ll`,
`0` the build named bare): 1 (dl 0, 12, 13) · 2 (tr1; dl 0, 12) · 3 (dl 0, 18, 19, 22; br 0, 21) · 4
(ll 0, 1, 2, 3) · 5 (br 0, 16, 20; ll 0, 2, 13, 30; dl 0, 11, 24) · 7 (tr1, tr9) · 8 (tr 0, 1, 2, 19;
dl 12, 13, 24) · 9 (tr 0, 9, 43) · 10 (tr 1, 2, 16, 18, 25, 42; ks18; dl1) · 11 (tr 1, 16, 18, 42) ·
12 (dl 0; ll 17, 22; tr 0, 19, 43) · 13 (ll 0, 2, 3; tr1; dl 12, 29) · 14 (ll 0, 2, 24; br 0, 16, 20) ·
15 (tr 4, 18, 25, 42; br 0, 1; dl 0, 12) · 16 (tr 0, 8; ll 0) · 20 (tr1; dl 0, 12, 13, 24) · 31 (ll2) ·
32 (tr 1, 25; ll8) · 33 (tr1; ll2) · 34 (tr1) · 38 (dl 13, 19; tr1; br 0, 1) · 46 (dl13). The other 17
(6, 35, 36, 37, 39 to 45, 47 to 53) cite no parent unit: their edges name dIndexedDesign siblings only,
and they are out of this pass.

The rules of the two unread revisions apply to the same specs. The SA probe named 3 (:97) and 14
(:307); RH's probe named none; HD's probe named 1 (:357, a hand-off, unbound) and 8 (:141, "their
writer is `hand`, the class TOOL-dTotalRecall-2 replaces").

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
- **RH, the lease holder read (`66f7b8d32`, `58b395b6e`).** A build lease's `fleet-tag`, `session`
  and `epoch` are read through TOOL-dPlacedRequest-34 S22's read-only `unattended.sh --lease status
  build <slug>`, which prints one TAB line `<tail> <fleet tag> <session> <status> <verdict> <epoch>`
  (pr34:106-109, AC22 at :468-470). tr2 §8 F6's ask narrows to a seventh TAB field holding the
  `lease`-mode class (`mine` or foreign), appended after `<epoch>`, the six-field prefix kept
  (tr2:196-203, :345-369). No new holder verb over `read_claims` is built or asked for, and `--claims`
  prints five fields with no session and no epoch. A spec that reads a lease's holder, session, class or
  epoch through `--claims`, parses a lease commit itself, files a second ask, names tr2 rev-7's new
  holder verb over `read_claims`, still reads tr2 F6 as open, or relies on a six-field `--lease status`
  line that a seventh field breaks, is a MISMATCH when it relies on tr2 for that read.
- **HD, the `hand` writer (`58b395b6e`).** TOOL-dTotalRecall-1 rev-5: `hand` is legal on any registry
  row TOOL-dTotalRecall-2 S9 does not move. S9 moves only the `fields`-form `hand` rows onto its door;
  a `hand` row of another form keeps `hand`, its door's owner named in that pass's `Decided:` trailer,
  and `backlog-row` and `dossier` keep `hand` (tr1:196-201, :223-226; tr2 S9 at tr2:84-88). The promise
  that tr2 gives every `hand` row a door is dropped. A spec that relies on tr2 giving a non-`fields` row,
  or every `hand` row, a door, or reads `hand` as legal only until tr2 registers a door, is a
  MISMATCH.

Verdicts:

- **AGREES:** today's parent text says what the assumption says, whether or not a revision touched it.
- **MISMATCH:** today's parent text says something else: a moved reader, a fork resolved another way,
  a section renumbered or a line cite moved, a refusal the parent now states, or a rule above broken.
  Quote both sides with `file:line`, and state in one or two sentences the change the dIndexedDesign spec
  needs.
- **UNKNOWN UNTIL BUILT:** neither spec decides it, and only the parent's build run can.

Groups, one reviewer each. The spec your task block's `input:spec` names leads one group. Check every
spec of that group, and no other:

- **Group A, full, led by spec 1:** specs 1, 2, 3, 4, 5, 7, 8. Check every assumption each makes about any parent unit, and apply SA, RH and HD to the same specs.
- **Group B, full, led by spec 9:** specs 9, 10, 11, 12, 13, 14, 15. Check every assumption each makes about any parent unit, and apply SA, RH and HD to the same specs.
- **Group C, full, led by spec 16:** specs 16, 20, 31, 32, 33, 34, 38, 46. Check every assumption each makes about any parent unit, and apply SA, RH and HD to the same specs.

The spec files are `memory/builds/dIndexedDesign/spec/2026-1?-??-spec-TOOL-dIndexedDesign-<n>.md`, and a parent's are
`memory/builds/<parent>/spec/2026-1?-??-spec-<FAMILY>-<parent>-<n>.md`. Read every mention of a
parent unit in each of your specs, then the cited parent text, its §9 rev lines first. A sibling
session is folding the owner's picks on the chain's open forks into some of these specs concurrently;
read `ab976b5b3` as it is, and the main loop re-checks your rows after that fold lands. The precedent
cross-check, `memory/builds/dShippedRelease/build/2026-11-03-build-DEPL-dShippedRelease-1-parents-crosscheck.md`,
shows the shape and the classes that turned up.

Aliases: `dlN:L` dDeclaredLoop, `fhN:L` dFairHearing, `trN:L` dTotalRecall, `prN:L` dPlacedRequest, `wbN:L` dWitnessedBar, `rpN:L` dRankedPlan, `llN:L` dLinkedLibrary, `idN:L` dIndexedDesign, `ksN:L` dKeptSession, `brN:L` dBoundRoles, `ocN:L` dOrderedCharter: line L of that build's spec N at `ab976b5b3`.

Return, in this shape and nothing else:

1. A table, one row per assumption: `| Spec | Assumption about the parent | Rule | Verdict | Evidence |`,
   with `idN:L` for line L of dIndexedDesign spec N and the aliases above for the parents. `Rule` is `cite`
   for a citation assumption, else the rule's tag.
2. Per MISMATCH, a bullet: both sides quoted, then `Change:` and the revision the dIndexedDesign spec needs,
   then `Cause:` either the revision (the parent text moved in the commit you name) or pre-existing (it
   already read so at the build's last cross-read, `none (spec base 4bf0f400d)`).
3. Per UNKNOWN UNTIL BUILT, one line on what decides it.
4. Per rule-wide hit a rule does not bind, one line saying why.
5. One line per citation spec: the revised parent sections it cites that none of its assumptions
   depend on.
6. Parent text that looks wrong, one line each: never a row, never an edit.

### Non-goals

- No file is written: every probe reads.
- No re-audit of rules an earlier re-ground applied and this build's last cross-read already read.
- No defect in dIndexedDesign's own design that no parent unit causes.
- No verdict on a parent spec: parent text that looks wrong is one line under 6, never a row.
- No read of dOrderedCharter's or dFairHearing's build runs, live on another node: their specs on
  origin/main only.
