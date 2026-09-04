# TOOL-aStagedLane-4 — the carriers name the classifier and the attended route

**Status:** WONTDO · rev-4 · 2026-09-04 · node a · Tier-2 · base 15339de0 · streams tooling · order 4 · RETIRED: does not fit M1's 23-byte budget for memory/guides/BUILD-METHOD.md, and both fundings are owner turns under M3 veto 2 — parked, see S6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-04-review-TOOL-aStagedLane-1-spec-audit-round1.md](../reviews/2026-09-04-review-TOOL-aStagedLane-1-spec-audit-round1.md) | spec-audit | TOOL-aStagedLane-1 TOOL-aStagedLane-2 TOOL-aStagedLane-3 |
| [2026-09-04-review-TOOL-aStagedLane-1-spec-audit-round2.md](../reviews/2026-09-04-review-TOOL-aStagedLane-1-spec-audit-round2.md) | spec-audit | TOOL-aStagedLane-1 TOOL-aStagedLane-2 TOOL-aStagedLane-3 |

<!-- /gen:spec-records -->

## 1. Goal

The method's detect step tells a run to read the build README's units table and classify by hand,
while a working classifier sits in the driver and answers the same question in one command. Name it
where the method already discusses detection, and declare the attended harness route in the same
pass, so what the preceding units build is reachable without reading their source.

## 2. Scope (IN)

- **S1** — the detect paragraph of the build method names the plan verb as the way to obtain a
  unit's state. The classifier runs with no run-state file, measured on this node against a build
  that never had one. **This is a pure ADDITION and rev-2's wording was wrong about the tree.** It
  said "without the mandate qualifier the guide's only current mention carries", which implies the
  guide already mentions the plan verb. It does not: `grep -- '--plan' memory/guides/BUILD-METHOD.md`
  returns nothing, `grep -i plan` returns only line 38's "planned", and the guide's sole driver
  mention is `--resume` at :204 inside M7's regrounding list — that is the mention carrying the
  qualifier, and it is a different verb. So S1 replaces nothing, and it is funded from nothing.
- **S2** — the passes paragraph of the same guide names the harness as the route for spec and build
  passes, and names its two modes, so a session that is not under a mandate knows the route exists.
- **S3** — both halves of the byte-compared pair move in one commit:
  `tools/memory-tree/BUILD-METHOD.template.md` and the rendered `memory/guides/BUILD-METHOD.md`. The
  `kit/dogfood doc parity` leg compares them, so editing one alone reds the bar.
- **S4** — `memory/project/method-carriers.txt` keeps its existing row for the harness, and the
  conditional is RESOLVED rather than left hanging. That row classifies the file as a pointer that
  states no rule the method does not. Under F1's owner ruling the method carries the mode
  semantics and the header stays a pointer, so the row does not move — unconditionally, not "if
  unit 2's header additions make it state a rule". A spec that hedges on whether it edits a
  registry leaves the implementer to decide, which is the thing S7 exists to stop.
- **S5 — WITHDRAWN at rev-3. The charter is not edited by this unit at all.** Rev-2 required
  deleting the charter's description of the pass-order leg. There is no such description:
  `grep -inE 'pass.?order|check-pass-order|predates|built before|spec-before-build'` over `AGENTS.md`
  and `coding-governance-agents.template.md` returns nothing. The only prose description of the leg
  is the byte-compared pair `memory/guides/UNATTENDED-PROTOCOL.md:469` and
  `tools/unattended/PROTOCOL.template.md:469`, which §3's third non-goal refuses to touch and which
  unit 1 does not make false — it describes `PASS_ORDER_CUTOFF`, which is unchanged. So nothing in
  the charter goes stale when unit 1 lands, and there is nothing to delete. See F2.
- **S6 — THE BUDGET IS THE BINDING CONSTRAINT, AND THE UNIT DOES NOT FIT IT.**
  `memory/guides/BUILD-METHOD.md` is 24553 bytes against M1's declared ≤24 KB (24576), and the line
  half is 317 of 350 — M1 says the BYTE half binds first and this is what that looks like. **23 bytes
  remain, and S1 and S2 are both pure additions.** Rev-3 planned to fund them by having S1 replace an
  existing plan-verb mention; there is none (see S1). The path literal
  `tools/workflows/unattended-build.js` that AC7 requires is 35 bytes by itself, before the sentence
  around it and before both mode values. The arithmetic does not close, and it is not close to
  closing.
  Neither remaining source of funding is available to this run. **Raising the budget is not**: M3 puts
  M1's own budget inside veto 2's governance-carrier clause BY NAME, so a raise is an owner turn.
  **Deleting method prose to make room is not either**: M1's rule that a duplicated obligation is "a
  defect HERE" does sanction deletion in principle, but choosing what to delete from a governance
  carrier is a change to a governance carrier beyond the scope the owner ratified at rev-2, which is
  veto 2 again. The owner approved ADDING two names to the method; nobody approved removing anything
  from it.
  **So this unit PARKS.** The decision is recorded and is the owner's: raise M1's budget, name a
  sanctioned deletion that funds the edit, or drop the unit. Under F1's owner ruling the cost is
  larger still — see the reconciliation below, which puts the mode SEMANTICS in the method rather
  than merely its two names.
- **S7 — WHICH DOCUMENT CARRIES THE MODE SEMANTICS: F1's owner ruling, and the other two texts move
  to match it.** Three documents currently hold three positions. §3's second non-goal says unit 2's
  file header owns them. §8 F1, an OWNER ruling, says "keep it a pointer; the method carries the mode
  semantics". Unit 2's S5 and AC6 require that header to enumerate five named losses, which is mode
  semantics in the header, and `memory/project/method-carriers.txt:19` asserts of that same file that
  "It states no rule the method does not". A delegated run does not get to pick between an owner
  ruling and a non-goal, so it does not: **F1's ruling is the owner's and it governs.** The non-goal
  is inverted to match it, and S4's conditional hedge is resolved the same way — under F1 the row
  does not move, so unit 2's header must stay a pointer, which means the five losses are NAMED there
  and their semantics live in the method. That is what makes S6's arithmetic worse rather than
  better, and it is why the park is the honest outcome rather than a shortfall of effort.

## 3. Non-goals (OUT)

- Not adding a restatement of the classifier's grades to the method. The four states and their
  precedence are the driver's, and a second spelling is a second answer. Phrased as what this unit
  ADDS, because the method already spells all four in M2's "Classify, first match wins" block: a
  non-goal written as though the tree were already clean reads as licence to delete that block, and
  nothing here covers deleting the method's own act rule.
- Not leaving the harness's mode semantics in unit 2's file header. **INVERTED at rev-4**, because
  the rev-2 wording was the exact opposite of §8 F1's owner ruling, which says the METHOD carries
  them and the header stays a pointer. S7 records the reconciliation; a non-goal contradicting a
  ratified fork resolution in the same document is a defect in the non-goal.
- Not editing the rendered protocol guide. It documents the mandate contract, which none of these
  units changes.
- Not adding a new carrier file. Every claim here lands in a document that already exists.
- Not editing the charter at all, in either its instance or its template. S5 is withdrawn at rev-3;
  there was no description of the pass-order leg there to delete, and adding one would red the
  `charter size` leg at six bytes of headroom.
- Not auditing the charter for descriptions that duplicate a source. That sweep is a separate unit,
  and after S5's withdrawal this build contributes nothing to it.
- Not raising `memory/guides/BUILD-METHOD.md`'s own byte budget to fit S1 and S2. M3 puts M1's
  budget inside veto 2 by name, so the raise is an owner turn; S6 says the unit parks instead.

## 4. Design

### Why the carriers are a separate unit

The preceding three units each change behaviour, and each would otherwise carry a fragment of the
same document edit. Splitting the documents into one unit keeps the byte-compared pair moving in a
single commit, which is what the parity leg requires, and leaves each behaviour unit with one
mechanism as the decompose rule demands.

### Why this unit lands last

A carrier declares what exists. Landing the declaration before the behaviour would put a document in
the tree describing a route the tree does not have, which is the drift class this repository audits
for.

### Files touched (estimate)

`tools/memory-tree/BUILD-METHOD.template.md` and `memory/guides/BUILD-METHOD.md` — the byte-compared
pair, which move together — plus `memory/project/method-carriers.txt` only if S4's re-classification
proves necessary. Two files, possibly three. `AGENTS.md` was on this list at rev-2 and is off it: S5
is withdrawn, so the charter is not touched.

### Alternatives rejected

Folding these edits into the units that motivate them was rejected: the byte-compared pair would then
be edited by two units in two commits, and the parity leg reds between them.

Leaving the method silent and relying on the harness's own header was rejected because a session
that does not already know the harness exists never reads that header.

## 5. Production-readiness checklist

- security — N/A. Document edits only.
- perf / scale — N/A.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — N/A. No runtime surface.
- observability — N/A.
- risks — the live one is `memory/guides/BUILD-METHOD.md`'s own budget, at 23 bytes of headroom
  (24553 of 24576) with 33 lines spare, so the byte half binds exactly as M1 says it does. The
  charter size gate was named here at rev-2 and is no longer a risk: S5 is withdrawn and neither
  charter subject is touched.
- testing + left-shift gates — the parity leg and the method-carriers leg both already exist and
  both grade these files; no new gate is needed and none is added.
- migration / rollback — reverting restores the current text exactly.
- user docs — this unit IS the docs change.

## 6. Acceptance criteria

- **AC1** — When `bash tools/memory-tree/check-method-carriers.sh` runs after the edits, it exits 0
  and reports no undeclared pointer.
- **AC2** — When the `kit/dogfood doc parity` leg runs, the template and the rendered guide compare
  equal, proving both halves moved in this commit.
- **AC3** — When `bash tools/run-gates/run-gates.sh` runs the `charter size` leg
  (`check-template-size.sh AGENTS.md`, against the 64512 row), it exits 0 — trivially, since S5 is
  withdrawn and `AGENTS.md` is not touched. The BARE `check-template-size.sh` measures
  `coding-governance-agents.template.md`, a file this unit also does not edit; rev-2 named the bare
  command while meaning the charter, which are two different subjects and two different legs.
- **AC3b** — When `wc -c memory/guides/BUILD-METHOD.md` and `wc -l` on the same file are run after
  this unit, the results are at most 24576 and at most 350. This is a DOCUMENTED MANUAL CHECK, not
  a leg: no gate in this repository enforces M1's pair, which is exactly why the guide reached 23
  bytes of headroom with nobody noticing. It is the criterion S1 and S2 actually fail, and S6
  records that they fail it.
- **AC4** — When the detect paragraph of `memory/guides/BUILD-METHOD.md` is read, it names the plan
  verb without a mandate qualifier, and THIS UNIT introduces no second spelling of the four unit
  states. The rev-2 wording — "the guide contains no second spelling" — is false of the tree today,
  since M2's "Classify, first match wins" block spells all four with their precedence, and taken
  literally it would require deleting the method's own act rule, which no scope item covers.
- **AC7** — When the passes paragraph of `memory/guides/BUILD-METHOD.md` is read, it names
  `tools/workflows/unattended-build.js` and both mode values, spelled exactly `attended` and
  `unattended`. Rev-2 left S2 as the only scope item in this unit with no criterion of any kind,
  which for a documentation unit means half its product shipped unobserved behind a green bar.
- **AC5** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs over the tree, it exits 0.
- **AC6 — REPLACED at rev-3, together with S5.** The rev-2 criterion asserted that the charter
  carries no description of the pass-order leg, which is already true of the tree as it stands, so
  it could not distinguish a landed unit from an unlanded one — the vacuous-selector class, and
  worse than useless here, because paired with AC3's LOWER clause it rewarded editing nothing. What
  replaces it observes the withdrawal instead: when
  `git diff --name-only <this unit's base>..HEAD -- AGENTS.md coding-governance-agents.template.md`
  runs, it outputs NOTHING. Neither charter subject is touched by this unit, and a criterion that
  can fail is the whole difference from the one it replaces.

## 7. Gates

`bash tools/memory-tree/check-method-carriers.sh`, the `kit/dogfood doc parity` leg named in
`tools/gate-legs.json`, and `bash tools/memory-tree/check-memory-hygiene.sh`. **That leg does NOT
measure M1's budget** — `check-memory-hygiene.sh:63` sets `GUIDE_CAP_BYTES=61440` and
`GUIDE_CAP_LINES=750`, so it passes this guide up to 60 KiB, two and a half times the 24576 S6
works against, and M1 itself says of its own pair "No gate enforces the pair". Rev-3 claimed the
opposite, which would have made a green hygiene leg read as proof the budget held — green-by-
absence on the one constraint this spec calls most likely to stop it. The full bar is `bash tools/run-gates/run-gates.sh`.
The two `check-template-size.sh` legs — the bare one over the playbook template and `charter size`
over `AGENTS.md` — are listed here only to be told apart: rev-2 named the bare command while meaning
the charter, and after S5's withdrawal this unit edits neither subject.

## 8. Open questions

- **F1 — does unit 2's mode documentation turn the harness from a pointer into a rule-stater?** The
  carriers file currently classifies it as a pointer that states no rule the method does not. A
  header describing which refusals attended mode omits may cross that line.
  Options: keep the header short enough to stay a pointer and put the mode semantics in the method;
  re-classify the row and accept the harness as a rule carrier; split the description across both.
  Recommendation: keep it a pointer and let the method carry the semantics. A rule with two carriers
  is the drift shape this repository already pays to detect.
  RESOLVED (owner, 2026-09-04): keep it a pointer; the method carries the mode semantics. S4 stands
  and the carriers row does not move.

- **F2 — should the charter sentence in S5 be spent at all?** The charter has a hard ceiling and the
  pass-order leg is already described there in terms that will be wrong after unit 1.
  Options: correct the sentence in place, which costs nothing net; add a new sentence; delete the
  charter's description and point at the manifest.
  Recommendation: correct it in place. The existing sentence becomes false when unit 1 lands, so
  leaving it is not an option, and correcting it spends no headroom.
  RESOLVED (owner, 2026-09-04): delete the description and point at the manifest, with a short
  instruction on what to do with it. This goes AGAINST the recommendation above, which is recorded
  rather than rewritten, and it is the stronger reading of the derive-over-author rule: correcting
  the sentence would have left a description to go stale again. S5 and AC6 carry it, and the
  instruction half is what keeps the pointer usable rather than merely accurate.
  **RE-PUT at rev-3: EVERY option above rests on a sentence that does not exist.** The fork asked
  whether to correct, add or delete the charter's description of the pass-order leg, and the ruling
  turned on "the existing sentence becomes false when unit 1 lands, so leaving it is not an option".
  The charter has no such sentence, in either the instance or the template, and the only description
  of the leg in the tree is in a guide §3's own non-goal refuses to touch and that unit 1 does not
  falsify. So the premise of the fork and of the ruling on it are both false.
  Options, re-put: re-point the deletion at the guide that DOES hold the description; add a pointer
  to the charter as a pure addition; or withdraw the charter edit entirely.
  RESOLVED (agent, 2026-09-04, delegated): withdraw it. The first option is discarded by veto 1 —
  §3's third non-goal forbids editing that guide, and a non-goal is exactly what veto 1 names. The
  second is discarded twice over: `AGENTS.md` stands at 64506 bytes against a declared 64512, so a
  pointer plus its instruction reds the `charter size` leg named in this spec's own §7, which is
  veto 1 again; and editing the charter is a change to a governance carrier, which is veto 2 and
  therefore an owner turn this run does not hold. Withdrawal trips no veto and leaves no follow-up:
  there is no stale sentence to come back for. S5 and AC6 are withdrawn, AC3 is re-pointed at the
  leg that actually measures the charter, and the unit keeps S1–S4 plus the new S6 — the method
  edits and the budget that binds them, which were always the load-bearing half.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft.
- rev-2 · 2026-09-04 · both forks resolved at the owner's scope-approval turn. F1 confirmed S4
  unchanged; F2 was ruled AGAINST the recommendation, replacing the charter correction with a
  deletion plus a pointer and instruction, which rewrote S5, added a non-goal and added AC6.
- rev-3 · 2026-09-04 · round-1 spec audit folded: B1, H9, H10, M3, plus one defect the audit did not
  reach. F2 RE-PUT and re-resolved under the mandate: the charter carries no pass-order description
  in either the instance or the template, so every option the owner chose between had a false
  premise. Withdrawal is the only option surviving M3's vetoes — the guide is behind a non-goal, and
  a charter addition both reds the `charter size` leg at 6 bytes of headroom and is a governance-
  carrier change this run may not make. S5 and AC6 are withdrawn; AC6 was in any case satisfied by
  the unmodified tree, and paired with AC3's LOWER clause it rewarded editing nothing. AC3 now names
  the `charter size` leg rather than the bare command, which measures the template — a different
  file, a different leg, neither of them touched. AC4's second clause was false of the tree and
  destructive if read literally, so it is scoped to what this unit introduces. AC7 added, because S2
  was the one scope item in a documentation-only unit with no observation at all.
  **The new defect: `memory/guides/BUILD-METHOD.md` has 23 bytes of headroom**, not the charter's
  six, and S1 and S2 both add to it. That is now S6, and it is the constraint most likely to stop
  this unit; raising the budget is explicitly outside the mandate, so the alternative to fitting is
  parking.
- rev-4 · 2026-09-04 · round-2 spec audit folded: both blockers and findings 3 and 11, and the
  unit is PARKED as a result. Blocker 1: rev-3's funding plan rested on an existing plan-verb
  mention in the guide, and there is none — the sole driver mention is `--resume` at :204, a
  different verb. S1 is a pure addition, S2 is a pure addition, and 23 bytes does not hold them;
  the reintroduced false premise is the same class round 1 blocked on, which is the cost of
  writing fold prose without re-running the grep. Blocker 2: §3's second non-goal was the exact
  inverse of §8 F1's OWNER ruling, with unit 2's S5 header taking a third position against
  `method-carriers.txt:19`; F1 governs, the non-goal is inverted, and S4's hedge is resolved
  unconditionally — all recorded in the new S7. Finding 3: S6 had no criterion; AC3b now is one.
  Finding 11: §7 claimed the hygiene leg measures the budget, and it caps guides at 61440/750 —
  the claim is corrected and AC3b is stated as the documented manual check it has to be.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "classify units MISSING THIN FORKED READY for an attended
build"` returned `build_reference_index` in `tools/codebase-map/map_lib.py` and `classify` in
`tools/memory-tree/check-arms.py` among its candidates, both matched on name stem and neither related
to unit classification in a build. The corpus is Python symbols and the classifier this unit points
at is a shell function, so the tool could not have found it. The seam found by reading is the plan
verb in `tools/unattended/unattended.sh`, which already computes the classification and already runs
without a run-state file, and the method-carriers registry, which already holds a row for the
harness; this unit adds no mechanism and reuses both.

Recall terms used: `M2 detect roster units region plan_state classifier BUILD-METHOD carrier
attended mandate restate`. The query was what the method's detect step tells an attended run to use;
it returned 40 hits, and the binding one is the parent build's spec-audit finding that the method
states its grading in terms the classifier had abandoned, which is the same carrier-drift class this
unit exists to keep closed.
