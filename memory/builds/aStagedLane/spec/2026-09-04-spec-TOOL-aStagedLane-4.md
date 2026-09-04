# TOOL-aStagedLane-4 — the carriers name the classifier and the attended route

**Status:** SPECCED · rev-3 · 2026-09-04 · node a · Tier-2 · base 15339de0 · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-04-review-TOOL-aStagedLane-1-spec-audit-round1.md](../reviews/2026-09-04-review-TOOL-aStagedLane-1-spec-audit-round1.md) | spec-audit | TOOL-aStagedLane-1 TOOL-aStagedLane-2 TOOL-aStagedLane-3 |

<!-- /gen:spec-records -->

## 1. Goal

The method's detect step tells a run to read the build README's units table and classify by hand,
while a working classifier sits in the driver and answers the same question in one command. Name it
where the method already discusses detection, and declare the attended harness route in the same
pass, so what the preceding units build is reachable without reading their source.

## 2. Scope (IN)

- **S1** — the detect paragraph of the build method names the plan verb as the way to obtain a
  unit's state, without the mandate qualifier the guide's only current mention carries. The
  classifier runs with no run-state file, measured on this node against a build that never had one.
- **S2** — the passes paragraph of the same guide names the harness as the route for spec and build
  passes, and names its two modes, so a session that is not under a mandate knows the route exists.
- **S3** — both halves of the byte-compared pair move in one commit:
  `tools/memory-tree/BUILD-METHOD.template.md` and the rendered `memory/guides/BUILD-METHOD.md`. The
  `kit/dogfood doc parity` leg compares them, so editing one alone reds the bar.
- **S4** — `memory/project/method-carriers.txt` keeps its existing row for the harness. That row
  classifies the file as a pointer that states no rule the method does not, and the attended mode
  must not change that classification. If unit 2's header additions make it state a rule, the row is
  re-classified in this unit rather than left disagreeing.
- **S5 — WITHDRAWN at rev-3. The charter is not edited by this unit at all.** Rev-2 required
  deleting the charter's description of the pass-order leg. There is no such description:
  `grep -inE 'pass.?order|check-pass-order|predates|built before|spec-before-build'` over `AGENTS.md`
  and `coding-governance-agents.template.md` returns nothing. The only prose description of the leg
  is the byte-compared pair `memory/guides/UNATTENDED-PROTOCOL.md:469` and
  `tools/unattended/PROTOCOL.template.md:469`, which §3's third non-goal refuses to touch and which
  unit 1 does not make false — it describes `PASS_ORDER_CUTOFF`, which is unchanged. So nothing in
  the charter goes stale when unit 1 lands, and there is nothing to delete. See F2.
- **S6 — THE BUDGET IS THE BINDING CONSTRAINT ON S1 AND S2, and it is 23 bytes.**
  `memory/guides/BUILD-METHOD.md` is 24553 bytes against M1's declared ≤24 KB (24576), and the line
  half is 317 of 350 — M1 says the BYTE half binds first and this is what that looks like. S1 and S2
  are therefore authored as net-≤23-byte edits: S1 REPLACES the mandate qualifier on the guide's
  existing plan-verb mention rather than adding a sentence, and S2 is spent from what S1 returns
  plus any deletion M1's own rule already mandates — a rule stated both here and in an M11 carrier
  is "a defect HERE" whose resolution is deletion, so removing one is in scope and is not a budget
  raise. **Raising the budget is NOT available to this run**: M3 puts M1's own budget inside veto 2's
  governance-carrier clause by name, so a raise is an owner turn and a run that took one would be
  amending the constraint it is judged by. If S1 and S2 cannot be written inside 23 bytes without a
  sanctioned deletion, the unit PARKS rather than growing the file.

## 3. Non-goals (OUT)

- Not adding a restatement of the classifier's grades to the method. The four states and their
  precedence are the driver's, and a second spelling is a second answer. Phrased as what this unit
  ADDS, because the method already spells all four in M2's "Classify, first match wins" block: a
  non-goal written as though the tree were already clean reads as licence to delete that block, and
  nothing here covers deleting the method's own act rule.
- Not restating the harness's mode semantics. Unit 2's file header owns them; this unit points.
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
- **AC3b** — When `memory/guides/BUILD-METHOD.md` is measured after this unit, it is at most 24576
  bytes and at most 350 lines. This is the criterion S1 and S2 are actually at risk of failing:
  23 bytes of headroom, not the charter's six.
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
`tools/gate-legs.json`, and `bash tools/memory-tree/check-memory-hygiene.sh`, whose guide caps are
what S6's 23 bytes are measured against. The full bar is `bash tools/run-gates/run-gates.sh`.
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
  leg that actually measures the charter, and the unit keeps S1–S4 — the method edits, which were
  always the load-bearing half.

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
