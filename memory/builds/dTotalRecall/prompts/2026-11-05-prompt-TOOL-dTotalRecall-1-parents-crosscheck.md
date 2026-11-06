**Serves:** research TOOL-dTotalRecall-1 TOOL-dTotalRecall-3 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-11 TOOL-dTotalRecall-19 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-43 TOOL-dTotalRecall-50 TOOL-dTotalRecall-61 TOOL-dTotalRecall-70 TOOL-dTotalRecall-89

# Brief: dTotalRecall's specs cross-checked against the unread parent revisions `63669d505`, `66f7b8d32` and `58b395b6e`

## The prompt

> Cross-read and re-ground seven dClosedLoop chain builds against two parent revisions they have never
> read: `dWitnessedBar`, `dPlacedRequest`, `dTotalRecall`, `dRankedPlan`, `dDeclaredLoop`,
> `dLinkedLibrary` and `dIndexedDesign`. dIndexedDesign also gets a FULL first cross-read against all
> its parents, since it has never had one. The owner asked for this on 2026-11-05.

— the dClosedLoop session's hand-off to this session, 2026-11-05, relaying the owner's ask after a
verification that found two parent revisions never read by their children.

## The brief

### Goal

Classify every assumption the named dTotalRecall specs make about a revised parent unit as AGREES, MISMATCH
or UNKNOWN UNTIL BUILT, against the parents' specs (dDeclaredLoop, dWitnessedBar and dPlacedRequest) as they stand on origin/main at `ab976b5b3`.
This build's last cross-read was `794a0f5fb`. Since then `git log 794a0f5fb..ab976b5b3 -- memory/builds/<parent>/spec/`
names only these revisions, generated-region rewrites and a no-op merge apart:

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

`git show 794a0f5fb:<spec>` reads a parent as this build's last cross-read read it.

The first population is by citation: every spec that cites a revised parent unit (1 spec): 11
(dl20 at :44, :91, :115, :319, :320, :356). No spec cites dl32 or fh17.

The second population is the siblings of tr1 and tr2. The owner's picks revised two of this
build's own units after its last cross-read; no sibling has read them since. RH's probe (`--claims`,
`read_claims`, `refs/gov/leases`, `--lease status`, `lease-mode class`, `holder verb`) named 3, 6 and
19 beside tr2 itself; HD's probe (`hand` on a line naming a door or a row, `fields-form`) named 7, 8,
24, 25, 43, 50, 61, 70 and 89 beside tr1 and tr2. The main loop's first look: 25:188 says tr2's door
"replaces `hand` when the planner registers" and 43 S8 is "the door's registry rewrite of `hand`
rows"; 3:74, 6:94, 6:142, 19:46 name the lease ref and may read no holder. Verify every hit.

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
  Quote both sides with `file:line`, and state in one or two sentences the change the dTotalRecall spec
  needs.
- **UNKNOWN UNTIL BUILT:** neither spec decides it, and only the parent's build run can.

Groups, one reviewer each. The spec your task block's `input:spec` names leads one group. Check every
spec of that group, and no other:

- **Group A, citation and siblings, led by spec 11:** specs 11, 3, 6, 7, 8, 19, 24, 25, 43, 50, 61, 70, 89. Check every assumption 11 makes about dl20 and apply SA to it; apply RH and HD to the siblings, reading tr1 and tr2 at rev-5 and rev-8.

The spec files are `memory/builds/dTotalRecall/spec/2026-1?-??-spec-TOOL-dTotalRecall-<n>.md`, and a parent's are
`memory/builds/<parent>/spec/2026-1?-??-spec-<FAMILY>-<parent>-<n>.md`. Read every mention of a
parent unit in each of your specs, then the cited parent text, its §9 rev lines first. A sibling
session is folding the owner's picks on the chain's open forks into some of these specs concurrently;
read `ab976b5b3` as it is, and the main loop re-checks your rows after that fold lands. The precedent
cross-check, `memory/builds/dShippedRelease/build/2026-11-03-build-DEPL-dShippedRelease-1-parents-crosscheck.md`,
shows the shape and the classes that turned up.

Aliases: `dlN:L` dDeclaredLoop, `fhN:L` dFairHearing, `trN:L` dTotalRecall, `prN:L` dPlacedRequest, `wbN:L` dWitnessedBar, `rpN:L` dRankedPlan, `llN:L` dLinkedLibrary, `idN:L` dIndexedDesign, `ksN:L` dKeptSession, `brN:L` dBoundRoles, `ocN:L` dOrderedCharter: line L of that build's spec N at `ab976b5b3`.

Return, in this shape and nothing else:

1. A table, one row per assumption: `| Spec | Assumption about the parent | Rule | Verdict | Evidence |`,
   with `trN:L` for line L of dTotalRecall spec N and the aliases above for the parents. `Rule` is `cite`
   for a citation assumption, else the rule's tag.
2. Per MISMATCH, a bullet: both sides quoted, then `Change:` and the revision the dTotalRecall spec needs,
   then `Cause:` either the revision (the parent text moved in the commit you name) or pre-existing (it
   already read so at the build's last cross-read, `794a0f5fb`).
3. Per UNKNOWN UNTIL BUILT, one line on what decides it.
4. Per rule-wide hit a rule does not bind, one line saying why.
5. One line per citation spec: the revised parent sections it cites that none of its assumptions
   depend on.
6. Parent text that looks wrong, one line each: never a row, never an edit.

### Non-goals

- No file is written: every probe reads.
- No re-audit of rules an earlier re-ground applied and this build's last cross-read already read.
- No defect in dTotalRecall's own design that no parent unit causes.
- No verdict on a parent spec: parent text that looks wrong is one line under 6, never a row.
- No read of dOrderedCharter's or dFairHearing's build runs, live on another node: their specs on
  origin/main only.
