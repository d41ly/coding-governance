# dFoldedAudit — orientation: the spec-audit disposition machinery

**Serves:** research TOOL-dFoldedAudit-1

## The question

# Orientation question 1: the spec-audit disposition machinery

The owner is changing BUILD-METHOD M4 for SPEC audits only. Closing DIFF reviews stay exactly as they are.
Today every confirmed finding at a SPEC exit is PROMOTED to a new unit and `fold` is refused. The new rules:

R1. A declared review chain STOPS when no blockers stand (blockers are BLOCKER and HIGH) AND every spec is fully
    reviewed. If no blockers stood but the audit promoted new units (new mechanisms), those specs are still reviewed
    before the chain stops.
R2. Local fixes fold in place: a wording or citation, a missing witness, an edge mirror, a criterion's reach, small
    fixes. They are folded into their specs with revisions bumped.
R3. In spec reviews, promote ONLY findings that need new mechanisms.
R4. A repair unit may edit its sibling's spec with a rev bump, rather than patching it from outside. This removes
    the "H1/H7 class".
R5. Stop the chain at the first round whose highs ALL sit in the previous round's own promotions.

Report, read-only, as a list of file:line rows, every place that ENCODES today's rule and what each must become.
Cover at least: tools/memory-tree/BUILD-METHOD.template.md M4; tools/workflows/REVIEW-PROTOCOL.template.md;
tools/unattended/PROTOCOL.template.md (§8), VERBS.template.md, STOPS.template.md; tools/unattended/unattended.sh
verb_review (REVIEW_DISPOSITIONS, check 37, review_exit_note); tools/unattended/check-unattended.sh and
run-unattended-gates.sh (the promotion clause, specs-audited, closing-review items in --close); tools/unattended/
check-pass-order.sh; tools/workflows/unattended-build.template.js (the DISPOSAL stage and its count reconciliation,
including the comment near line 2012 saying an earlier stage disposed by NATURE and why that was removed);
tools/workflows/tier2-review.template.js; tools/roles/agents/ (spec-writer, spec-reviewer, synthesizer) and
.claude/roles.json write classes; tools/policy/catalogue.toml (is REVIEW_ROUNDS or a review precision floor a policy key);
tools/memory-tree HYGIENE and SPEC-TEMPLATE, the deviation machinery; each test suite that pins these literals.

Then answer these specifically:
Q1. Which owner rulings and ids set the present rule (DIFF 2026-10-04, SPEC 2026-10-05, TOOL-aEvidencedLens-7/-8,
    TOOL-aBatchedMinors-2)? Quote why the disposal stopped being by nature. A new predicate must survive that reason.
Q2. What today stops or discourages a repair unit editing a sibling spec? Look at --dispatch --writes checks,
    the spec-revised records, ROUTED_PATHS, check 21 review bindings ("a spec whose rev moved ... by anything but that
    review's own fold"), and --review on a rev-bumped spec.
Q3. What is the "H1/H7 class"? Search recent spec-audit review records (dMindYourWords, dShippedRelease, dSafePassage,
    dKeptSession, dLinkedLibrary, dTotalRecall) for H1 and H7 findings where a repair unit patched a sibling from
    outside, and state the class with citations.
Q4. Can a round's record identify which highs sit in which specs, so "all highs in the previous round's own
    promotions" is DERIVABLE by a verb rather than asserted? What does `--review` record now, and where is the
    promoted-unit list (promotedIds, --rescope rows) durable?
Q5. Does a promoted unit's audit run under a fresh subject today, and how is its round numbered?

Write nothing in the repository. Return at most 120 lines. Cite every claim by path:line.

## The return, verbatim

# Reuse scout result: TOOL-dFoldedAudit-1, spec-audit disposition machinery

All cites are relative to `C:\projects\coding-governance\.claude\worktrees\gov-build-m4-spec-audit-694e7b\`. Nothing was written.

**Decision: wire through existing seams. No new verb, harness or stage.**
- `seam: verb_review (tools/unattended/unattended.sh:12673)`: reuse for the spec exit; extend via its existing `subj = slug` split (:12694).
- `seam: DISPOSAL stage (unattended-build.template.js:2004)`: reuse for fold versus promote; extend via `DISPOSAL_SCHEMA` and the reconciliation (:2207-2224).
- `seam: check 2 awk (check-unattended.sh:821)`: reuse for grading; extend via a third cutoff beside `FOLD_CUTOFF` and `SPEC_COUNTS_CUTOFF` (unattended.sh:1013, :1023; read at check-unattended.sh:635-639).
- `seam: deviation_join.scan members (deviation_join.py:589-606)` and `derive_past_pin_ids` (gen_build_index.py:1612-1615): reuse for the fold-aware "unreviewed" reading.
- Keep fail-37 branches inline. check-arms finds them by literal check number (unattended.sh:12742-12744).

## Sites encoding today's rule

**Method and protocol**
- `tools/memory-tree/BUILD-METHOD.template.md:144`: "every CONFIRMED finding... DISPOSED BY SEVERITY... None is... folded". Rewrite for SPEC only (R2, R3); DIFF keeps it. The "CHAIN... bounded by PRECISION" sentence becomes R1/R5.
- `BUILD-METHOD.template.md:121-122`: "rev moved... by anything but that review's own fold". Must admit a repair unit's sibling bump (R4) or state that it re-owes audit.
- `BUILD-METHOD.template.md:141-142`: fold only "on a round that is not an exit". Now folds at an exit too.
- `BUILD-METHOD.template.md:146-148`: CONVERGED is terminal "rev bumps included". Must say a blocker there takes the new disposition.
- `BUILD-METHOD.template.md:274`: "highs, mediums and lows carry to the exit, where M4 promotes them". This is DIFF (M8); keep it, and confirm that M4's wording split doesn't orphan it.
- Size limit: `tools/template-size-limits.txt:129` caps the guide at 30720 bytes and it is 29354 now, so about 1366 bytes of headroom.
- `tools/workflows/REVIEW-PROTOCOL.template.md:179`: the only precision text, "Below 0.5, tighten the scope". M4 calls this the floor, but it says nothing about ending a chain. Align or retire it.
- `tools/unattended/PROTOCOL.template.md:487`: `REVIEW_ROUNDS` row, unchanged unless R1 adds a chain bound. `:529` `DISPOSITION_CUTOFF` row, add a sibling row for the new cutoff.
- `tools/unattended/VERBS.template.md:246-264`: `--review` entry ("`promote` is the ONLY value", `fold` refused). Rewrite for spec subjects.
- `VERBS.template.md:784-786, :790-804, :808-818`: state list and "Every terminal exit promotes EVERY confirmed finding". Same split.
- `tools/unattended/STOPS.template.md:710`: "a promoted finding... is never carried". Still true; no change. No other disposition text in STOPS.

**Driver and gate**
- `tools/unattended/unattended.sh:999`: `REVIEW_DISPOSITIONS="fold|promote"`. Set can stay; legality moves.
- `unattended.sh:12659-12672`: `review_exit_note` (fold "recordable at NO exit"). Needs a live fold arm for spec subjects.
- `unattended.sh:12687-12693`: header cites the old rulings. Update.
- `unattended.sh:12793-12798`: fold refused on spec subjects. DIFF only. A standing BLOCKER still cannot fold, unless the owner says otherwise.
- `unattended.sh:12806-12832`: `owe = blockers + highs + minors>0` (:12823). On a spec subject owe must become the promoted count, so the row needs a new field. Check 2 reads disposition as the LAST field (:12849), so counts stay before it.
- `unattended.sh:12852-12862`: exit sentences. `BOUNDED` still says "DISPOSED BY SEVERITY".
- `unattended.sh:12603-12613`: bound comment and the `review_state` predicate (:12614). R1/R5 are chain-level, so they do not belong in this per-subject function.
- `unattended.sh:22`: usage line, fine as is.
- `tools/unattended/check-unattended.sh:834-851`: counted row and `specbad` ("never folds"). Add a date gate for the new cutoff.
- `check-unattended.sh:880-890, :900-914`: `owe` recomputed and `closefold`. A fold on a counted spec row reds today. The refusal text at :907 says "any subject"; narrow it.
- `unattended.sh:11897-11991`: `specs-audited` is "has ever named" (:11913-11916). R1's "every spec fully reviewed" is stronger than this. Promoted units close by override today (M4:144).
- `unattended.sh:11767-11896`: `closing-review-recorded` is DIFF. No change. Note :11855-11859: the incentive reasoning is worth keeping in mind.
- `tools/unattended/run-unattended-gates.sh`: no match for promotion, disposition or specs-audited. The clause lives in check-unattended. No change.
- `tools/unattended/check-pass-order.sh:21`: comment naming `specs-audited` only. No change.

**Harness and agents**
- `tools/workflows/unattended-build.template.js:2057-2112`: disposal prompt. "BY SEVERITY and admits no third route" (:2068), "Nothing is folded: return `folded` as 0" (:2093).
- Template :2150-2224: reconciliation and bounds. `d.folded !== 0` (:2221) and `promoted >= confirmed`, `unitFloor`, `unitCeiling` (:2207-2211) all assume promote-all.
- Template :2214-2218 says two arms are unreachable; that changes once fold loosens.
- Template :2236-2238: refusal "never folded (owner, 2026-10-05)".
- Template :1855-1872: `writeRound` passes `--highs/--minors` and `--disposition promote`. It needs the new row shape.
- Template :2004-2028: history comment, extend it. :9: Disposal stage detail. :2290: the by-hand note. The rendered `tools/workflows/unattended-build.js` must regenerate.
- `tools/workflows/tier2-review.template.js:698`: comment citing TOOL-aProbedUnit-9, stale. :1524 and :1565: precision is computed and logged only.
- `tools/roles/agents/gov-spec-writer.agent.md:41`: "no file outside the spec folder you were handed" already permits a sibling. Add the R4 sentence.
- `gov-spec-reviewer.agent.md`, `gov-synthesizer.agent.md`: no disposition rule. No change unless R5 needs a per-item spec field (`gov-synthesizer` :10).
- `.claude/roles.json`: writes classes need no change. Disposal already runs as `gov-spec-writer` (`tools/roles/workflows.toml:37`).
- `tools/policy/catalogue.toml`: no `REVIEW_ROUNDS` and no precision key. `REVIEW_ROUNDS` is a legacy `owner-policy` home (`tools/policy/legacy-homes.txt:106`). Nearest keys are `review.design.rounds` :710, `review.max-rounds` :723, `review.findings` :1230, all owned by dDeclaredLoop. Owner-side bound guard: check-unattended.sh:2717.
- `tools/memory-tree/SPEC-TEMPLATE.template.md:67, :344-346, :469, :590`: already carry the fold plus rev-bump shape; reuse. `HYGIENE.template.md`: no M4 or promotion text. :463-466 pin grammar stands.

**Test suites pinning the literals (grep counts)**
- `tools/unattended/unattended.test.sh`: 39 (e.g. :7128-7154).
- `tools/unattended/check-unattended.test.sh`: 20 (:1408, :1443, :1527).
- `tools/workflows/unattended-build.test.sh`: 7 on those strings, plus the disposal fixtures with `"folded":0` throughout (:757, :855, :914, :1246-1289, and the `minimum: 0` count at :1289).
- Mutation arms exist for both cutoffs (check-unattended.test.sh:1428, :1547).

## Q1. Rulings, and why disposal stopped being by nature

- **Log ids** (the orientation names spec ids; the decision rows are these):
  - TOOL-aProbedUnit-9, 2026-09-14: mediums and lows FOLDED (`memory/DECISIONS.md:114`).
  - Row TOOL-dGatedProse-4: precision bound (:216).
  - TOOL-aBatchedMinors-5, DIFF 2026-10-04 (:219).
  - TOOL-aEvidencedLens-17, SPEC 2026-10-05, "Supersedes the fold half" of aProbedUnit-9 (:220). The new ruling supersedes this one for spec audits.
- **Specs:**
  - `memory/builds/aBatchedMinors/spec/2026-10-04-spec-TOOL-aBatchedMinors-2.md:18`.
  - `memory/builds/aEvidencedLens/spec/2026-10-05-spec-TOOL-aEvidencedLens-7.md:20`.
  - aEvidencedLens-8 §8 F3 (:304-315) parked the generation bound for the owner. R1/R5 answer that parked question.
- **Reason, quoted** (template:2013-2018): "a predicate on the wrong integer: `CONVERGED` means zero BLOCKERS this round and says nothing about highs, mediums or lows". The recorded shape was 8 highs, 6 mediums, 1 low, disposed nothing (aProbedUnit-7.md:25-28).
- **The flaw was the verdict gate, not nature as such.** A nature predicate survives only if all of these hold:
  1. It runs on the outstanding count, not the verdict.
  2. It cannot reconcile a high into prose. Cluster D: "`promoted 0, folded 10` reconciled... two blockers folded into prose" (template:2131-2133). Also aBatchedMinors-2.md:18-24, "vanish into a fold nothing reads".
  3. A row claiming fold cannot leave a blocker "under a field that says nothing was" (check-unattended.sh:909).
- **Implication:** "needs a new mechanism" (R3) is asserted by the disposal agent. Each folded id should therefore name its spec and the bumped rev, joined to the §9 line, and the gate should read that. SPEC-TEMPLATE:344-346 is the likely hook.

## Q2. What stops a repair unit editing a sibling spec

- **No hard refusal for the spec-writer role.** scratch-guard admits any `writes = spec` agent on any spec, and passes `routed` only for the product role's status flip (`tools/hooks/scratch-guard.js:1097-1106`, :1170-1178). A builder cannot edit specs at all.
- **ROUTED_PATHS is irrelevant.** It may not cover MEMORY_ROOT (scratch-guard.js:924).
- **`--writes` / check 23 is soft.** It counts only a dispatched pass whose window overlapped a sibling, against a budget (check-unattended.sh:4331, :4370). A pass's own "review fold or spec bump" sits outside the window by construction (:4008-4009).
- **M4:121-122 is the real discouragement.** A foreign bump reads as unreviewed. This is rendered only ("Ids whose spec moved past its audited revision", gen_build_index.py:1614); `specs-audited` does not grade the rev.
- **The cost is deviation_join.py:589-606.** Any material change past the pin is an `audit` member with hand `spec-revised`. There is no fold exemption, and a grep of the file shows none. dMindYourWords carries 26 such records (e.g. `memory/builds/dMindYourWords/build/2026-10-29-build-TOOL-dMindYourWords-10-deviation-101.md`). R2 alone would multiply this unless it exempts folds.
- **`--review` on a bumped spec:** same-subject rounds are refused (unattended.sh:12766), but subjects are per generation, so a bumped sibling just isn't re-audited. Scoped audits read only `auditIds` (template:1393-1394). `auditIds` may name any roster unit (:413), so siblings can be added there without a new input.
- **The disposal prompt licenses exactly one sibling edit**, the §3 mirror as a rev bump (template:2094-2096). That is the precedent for R4.

## Q3. The H1/H7 class

No record uses that label; the only literal "H1, H7" hit is unrelated (aHoistedPass). The best match is the report `memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-30-spec-audit.md`, H1 (:62) and H7 (:110).

- H1 was promoted to KICK-45 (`dKeptSession/RUN.md:72`), "repairs `KICK-dKeptSession-30`" (`spec/2026-10-26-spec-KICK-dKeptSession-45.md:32`).
- H7 was promoted to KICK-54 (RUN.md:90), "repairs `KICK-dKeptSession-34`" (`spec/...-54.md:32`).
- Both specs carry a clause "The sibling text superseded by name" (-45:43, -54:47).
- KICK-34 still reads its wrong sentence (`spec/...-34.md:1`, :40), and its rev-2 touched only Edges (:136).

**Class:** a one-line correction to spec A becomes a whole unit B that overrides A's text from outside, while A stays wrong, built first, and re-audited as new surface. Its costs are on record:
- The repair itself drew a high: KICK-54 AC2 (`...-KICK-dKeptSession-45-spec-audit.md:69`).
- Repairs ordered after their target, with the target's ACs red at its own pass: `dTotalRecall/reviews/...-54-spec-audit-round1.md:58, :66`. Also `dTotalRecall/reviews/...-44-spec-audit-round1.md:66`.
- A pure amender unit whose criterion is green before the pass: `dTotalRecall/reviews/...-61-spec-audit-round1.md:65`.
- Same shape: dLinkedLibrary-63 repairing -51 (`dLinkedLibrary/RUN.md:102`), where -51 got an Edges bump only (`spec/*-51.md:158`).
- `dShippedRelease` has no review records.

## Q4. Is "all highs in the previous promotions" derivable?

**Partly, and the obvious derivation is vacuous.**
- **Row:** `--review` records subject, verdict and counts only (unattended.sh:12850; e.g. `dMindYourWords/RUN.md:64, :82, :120`). It names no spec.
- **`promotedIds`** is a return value (template:2445). Its durable form is the `rescope · item add` rows. They sit immediately before their round's review row, because the record follows disposal (RUN.md:48-62 then :64; :90-118 then :120). Round attribution is derivable by position, but the reason text is free prose with no fixed grammar (compare dKeptSession RUN.md:72 with dMindYourWords RUN.md:90). Attended runs have no rows at all, only README rows (template:2070-2072).
- **Audited set:** the `**Serves:** spec-audit <id>@rev-N` line, a durable machine-read join.
- **High to spec:** only the report's `Where:` prose. Synthesis items carry severity and ids (tier2:1925-1932). Finders carry `file` (tier2:749), but I did not establish that it persists in machine form. So it is not derivable today.
- **Vacuity warning:** from round 2 on the audit reads only the promotions (template:1393), so a Serves-based test is true by construction. R5 would have stopped dMindYourWords at round 2. A real test needs per-high addresses, and `Where:` can also span surfaces ("spec-36 §2 S3... against spec-33", `...-30-to-37-spec-audit-round1.md`).
- **Evidence shape:** highs 7, 7, 13; promotions 8, 8, 15 (RUN.md:84, :122). Precision was 0.97, 0.90, 0.89, so the floor was never in reach, and no code reads precision to end a chain (grep over the driver, gate and build harness finds only template:1671). The owner stopped it by hand (`dMindYourWords/prompts/2026-10-30-prompt-TOOL-dMindYourWords-1-owner-stop-chain.md:16-19`).

**Owner decisions to surface:**
1. R1 says stop when no HIGH stands, R5 says stop with highs standing. What disposes R5's highs: fold, or promoted and built unaudited, as M4:144 does today?
2. Does R5 mean the spec address, or the surface (the ruling's "landed on hardening the promotions added")?
3. Does the precision sentence in M4 survive?

## Q5. Fresh subject and numbering

Yes. The subject is `<slug>-spec-set-r<N>` (template:218-226, :354-355), so `REVIEW_ROUNDS` re-arms per generation (M4:144). N is the invocation round, passed as `round` with no `subjectRound` (:1887-1888, :2456). The harness's own round is `roundNo - subjectRound + 1` (:393), so each generation reports round 1 (`dMindYourWords/reviews/...-22-to-29-spec-audit-round1.md`). The chain generation is therefore the `r<N>` suffix. A verb can read it from the rows, and no chain-level counter exists.
