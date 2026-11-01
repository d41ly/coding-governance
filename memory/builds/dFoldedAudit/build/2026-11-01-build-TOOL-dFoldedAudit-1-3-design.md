# dFoldedAudit — the design every spec of this build derives from

**Serves:** research TOOL-dFoldedAudit-1 TOOL-dFoldedAudit-2 TOOL-dFoldedAudit-3 TOOL-dFoldedAudit-4 TOOL-dFoldedAudit-5 TOOL-dFoldedAudit-6 TOOL-dFoldedAudit-7 TOOL-dFoldedAudit-8

The owner's words are in `prompts/2026-11-01-prompt-TOOL-dFoldedAudit-1-brief.md`. The seams, citations and evidence
are in `build/2026-11-01-build-TOOL-dFoldedAudit-1-1-orient-enforcement.md` and
`build/2026-11-01-build-TOOL-dFoldedAudit-1-2-orient-dclosedloop.md`. Everything below is decided: a spec states it
exactly and may not re-open it. What a spec must still derive is marked DERIVE.

[scope]
SPEC audits only. A closing DIFF review, its exit rows, `closing-review-recorded`, M8 and the DIFF half of M4's
disposal keep every byte of behaviour. Every change branches on the spec subject through `verb_review`'s existing
`subj = slug` split or the harness's spec path, never by rewording a shared branch.

[nature] The disposal predicate, independent of severity.
A confirmed finding NEEDS A NEW MECHANISM when its fix adds a document, gate, adopter, generated artifact, verb or
write path that no unit's Scope names; this is M2's own one-mechanism test. Every other finding is LOCAL: a wording
or citation, a missing witness, an edge mirror, a criterion's reach, any small fix.
- LOCAL folds into the spec or specs it touches, rev bump and a §9 line naming the review record and the finding id.
- NEW MECHANISM is promoted to a unit. The mediums and lows among them still batch into one unit, two across
  disjoint write sets. A BLOCKER or HIGH takes its own unit.
- A LOCAL BLOCKER folds too. The owner's rule is "promote only findings that need new mechanisms".

[survive] The reason disposal stopped being by nature must stay answered.
Template lines 2013-2018 of the build harness record it: the old stage's predicate read the verdict, not the
outstanding count, and a high could reconcile into prose. Three properties are therefore mandatory:
1. Disposal runs on the outstanding count, never on the verdict word.
2. A fold names its target: every folded finding id joins to a unit id and that unit's new rev, and the §9 line in
   that spec names the finding. A fold return without the join is refused by the reconciliation.
3. A record whose counts claim fold cannot hide a HIGH: the row carries `folded` and `promoted`, they sum with
   refuted and standing to the outstanding count, and check 2 grades it.

[row] The spec subject's exit row past the cutoff.
`blockers <b> · <EXIT> · highs <h> · minors <m> · folded <f> · promoted <p>[ · disposition fold|promote]`.
`f + p` counts findings, not units, and equals `b + h + m` plus any UNVERIFIED finding the disposal adjudicated.
Disposition stays the LAST field because check 2 reads it there. It is `promote` when p > 0, `fold` when p = 0 and
f > 0, absent when nothing stood. Rows before the cutoff keep their shape and their grading.

[cutoff] In-flight runs finish under the old rule.
A new conf key beside `DISPOSITION_CUTOFF` and `SPEC_COUNTS_CUTOFF`, read the way those are. It keys on the date the
run was PREFLIGHTED, never on the README's `opened:`, because 22 chain builds were opened in October and those not
yet started must inherit the new M4. DERIVE the key's name through `/lexicon` and the conf precedent. Its value is
the landing date this build writes at the close.

[fold-stage] Where folds happen.
A spec exit folds at the disposal, in the same DISPOSAL stage that promotes. Non-exit rounds keep folding as today.
`CONVERGED is terminal for its subject, rev bumps included` narrows: on a spec subject a blocker confirmed later takes
[nature]'s disposition through the chain, and `--review`'s check-37 refusal of a further round on ONE subject stays,
because generations are fresh subjects `<slug>-spec-set-r<N>`.

[repair] R4, the sibling edit.
Where a promoted unit corrects text in a sibling spec, the disposal rewrites the sibling's text itself, rev bump and
§9 line naming the repair unit, instead of writing "superseded by name" into the repair spec. Only an UNBUILT sibling:
a sibling whose status is CLOSED stays frozen, which is dClosedLoop's P19 too, and a correction to it is a new unit
built on top. The disposal return carries `siblingEdits: [{unit, rev}]` and the reconciliation refuses a CLOSED unit
there. A sibling edit is a fold for [chain] purposes: it enters that round's folded set. The class gate: a spec past
the cutoff carrying the phrase "superseded by name" reds; run the predicate over the real tree first and exempt by
cutoff, never by list. DERIVE the gate's home.

[chain] The stop verdict. One derived function, one reader.
For a chain, round N holds these sets. H(N) is the confirmed BLOCKERs and HIGHs, each with its spec address, the
non-empty set of unit ids its fix would change. P(N) is the units that round promoted. F(N) is the specs folded for a
BLOCKER or HIGH that round, sibling edits included; a spec folded only for mediums or lows is not in F(N), because
M4 already counts a review's own fold as reviewed.
Evaluated in this order after round N's disposal:
1. UNREVIEWED: some roster spec outside P(N) is named by no `spec-audit` record. CONTINUE, auditing those with P(N)
   and F(N). This is "all the specs fully reviewed". Round 1 is the whole set. Read as TOOL-dFoldedAudit-5 F1 (b)
   resolved it: taken literally, the first wording would pre-empt R5 and the ceiling on any promoting round.
2. CLEAN: H(N) empty and P(N) empty. STOP, reason `clean`.
3. R5: N >= 2, H(N) non-empty, and every high's address is a subset of P(N-1) union F(N-1). STOP, reason `own-work`.
   This round's own disposal still runs: local highs fold, a new-mechanism high is promoted once more and built from
   its spec unaudited, and those units close under a recorded `--override specs-audited`.
4. CEILING: N >= the chain ceiling. HOLD for the owner with `--hold`, never a silent stop. The default ceiling is 4.
5. Otherwise CONTINUE, auditing P(N) union F(N). Round 2 therefore reads only what round 1 changed.
Consequences to state in the spec, not to fight: a HIGH naming one older spec keeps the chain alive; most chains end
at round 2; an empty H(N) can never read as R5, which is the `fixture-passes-by-finding-nothing` class, so the arm
must carry a population. A HIGH with an empty address is refused at synthesis, and a round with H(N) non-empty but
P(N) and F(N) both empty is a refusal, because every confirmed HIGH was disposed somewhere.
Precision no longer bounds anything. The floor sentence leaves M4, and REVIEW-PROTOCOL's tuning lever stays a lever.

[address] Where H(N), P(N) and F(N) live, durable in both modes.
`tier2-review`'s synthesis adds a required `specs` list to each BLOCKER or HIGH on a spec subject; the report also
prints it as a machine line under the finding. The disposal hand-out carries one `dispositions` array:
`{id, severity, nature, specs, unit, rev}`. The main loop records that array through one new verb into one append-only
build record, and the stop verdict is a second new verb that reads only that record and the roster. Both work with no
run-state file, because attended `/build` runs the same harness and no `--review` row exists there. The verdict is
computed in exactly one place, the driver, never a second copy in the JS. DERIVE both verb names through `/lexicon`.

[fold-records] R2 must not multiply hand records.
`deviation_join.scan` counts every material rev move past the pin as an `audit` member owing a hand `spec-revised`
record, and dMindYourWords carried 26. A rev move whose §9 line cites a spec-audit review record of this build that
names that spec owes none. A rev move with no such citation is still reported. `derive_past_pin_ids` reads the same
predicate. M4's "by anything but that review's own fold" gains the disposal's sibling edit.

[switches] Every behaviour is a switch. The answer is the default, the old rule an allowed value.
- the disposal: `by-nature` (default), `promote-all` (today's rule, the refusal of `fold` included)
- the chain stop: `own-work` (default, R1 with R5), `clean-only` (R1 alone)
- the chain ceiling: integer, default 4
`policy.py get` reports each. A kit read through `.unattended.conf` keeps working in an adopter without the policy
kit. DERIVE the keys' names and homes from `tools/policy/catalogue.toml`, `tools/policy/legacy-homes.txt` and how
`REVIEW_ROUNDS` is registered. `review.design.rounds` is not this: it counts one subject's rounds.

[closedloop] What changes in the chain.
Unbuilt specs only, each by rev bump and §9 line citing this build: DL-32 (split spec subjects out of its strict-fall
exit; follow-ups and fix passes keep it), DL-20 (its dispose row limited to built work or a new mechanism, S9 rebased
on the rewritten M4 sentence), FH-17 (re-point its chain rule to the new stop). dClosedLoop v2 is frozen: `cl-0117`
and its neighbours at v2:1260 and v2:1261 change by a deviation record quoting the owner's prompt, per FQ:193-194.
PLAY-dClosedLoop-1 restates no design fact and needs nothing. Historic text that records why a unit exists stays.
dSafePassage, and any build whose run claim reads `live` at the pass, is not touched; DL-*, FH-* and the claim state
are re-read at that pass.

[order] Build order, by what reads what.
7 switches, 2 row and grading, 3 disposal stage, 4 repair, 5 chain verdict, 6 deviation, 1 method text as built, 8
dClosedLoop. Unit 1 owns every prose carrier so that it describes what shipped: BUILD-METHOD M4, REVIEW-PROTOCOL,
PROTOCOL, VERBS, and the agent role text. Code units write only code, comments and suites. Unit 6 is disjoint and
may run beside any other.

[limits]
BUILD-METHOD's ceiling is 30720 bytes and it stands at 29354; M4's rewrite must fit, and the precision sentence's
removal funds it. New protocol text uses tags, not positional references. Kit version markers bump where a kit moves.
Unit agents run no gate and no suite; arms are owed to the main loop at the close. A spec H1 takes an em dash, and a
**Serves:** line names spec ids only.
