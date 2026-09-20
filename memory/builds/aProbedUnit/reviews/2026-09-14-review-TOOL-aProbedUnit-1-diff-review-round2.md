**Serves:** diff-review TOOL-aProbedUnit-1 TOOL-aProbedUnit-2 TOOL-aProbedUnit-3 TOOL-aProbedUnit-4 TOOL-aProbedUnit-5 TOOL-aProbedUnit-6 TOOL-aProbedUnit-7

# Tier-2 diff review — build `aProbedUnit`, the FOLD of closing diff review round 1, round 2

Written 2026-09-14 on node `a` by the unattended-build harness's closing review stage (`tools/workflows/tier2-review.js` under `tools/workflows/unattended-build.js`): four primed finder lenses, an adversarial skeptic per finding in five batches, one synthesis pass. Subject: the text the fix pass `48dae3b4` introduced on top of round 1's tip `15697d57`, which is the fold of the eighteen findings in `reviews/2026-09-14-review-TOOL-aProbedUnit-1-diff-review-round1.md`. This round judges the FIX of each of those and any NEW defect the fix introduced; it does not re-raise the originals. Source claims below stand as the skeptic stage confirmed them, and this record re-derived the following against the tree at `48dae3b4` before adjudicating: `bash tools/unattended/check-unattended.sh` printing `UNATTENDED check 2 FAILED` as its first line and naming sixteen tracked run-state files under the `disposition fold beside a NON-ZERO blocker count` message, with the working tree carrying only an uncommitted two-line `witness:` delta in `memory/builds/aProbedUnit/RUN.md` that touches none of the sixteen; the first-commit date of each of those sixteen files via `git log --follow --diff-filter=A --format=%cs`, every one on or after the `DISPOSITION_CUTOFF="2026-09-01"` that `.unattended.conf:268` declares, the earliest two exactly on it; `rv_graded` at `tools/unattended/check-unattended.sh:485-498` and the `foldbad` clause at `:541` and `:552-553`; `load_spec_facts` at `tools/unattended/unattended.sh:1905-1927` and its three other callers at `:2103`, `:3529` and `:4874` against the `--audit` call at `:2985`; `review_state` at `:4111-4119` and the terminal-subject refusal at `:4237-4240`; the harness template at `:232-234`, `:593-600`, `:640`, `:682-687`, `:726`, `:769`, `:784`, `:901`, `:968-973` and `:1151-1154`, byte-identical in the render; `tier2-review.js` at `:110`, `:339`, `:347`, `:385` and `:474-484`; `specs-audited` at `unattended.sh:3683-3735`; `tools/unattended/SKILL.template.md:680` and the rendered `.claude/skills/unattended/SKILL.md:680`; `memory/builds/aProbedUnit/RUN.md:80`; and `python tools/memory-tree/gotchas.py --for-diff` over the range, which selected 29 classes. The suite arms cited by the round-1 clusters were read, not re-run; the run integrity figures are the pipeline's own.

Reviewed range, pinned: `15697d570746e47629013a10f11548fab0c5262b...48dae3b4` · ROUND 2.

## Verdict: BLOCKED

One BLOCKER, and it is the merge bar: the `foldbad` clause cluster C's fix added to check 2 grades every record first-committed on or after `DISPOSITION_CUTOFF`, sixteen tracked append-only run-state files the DRIVER wrote under the contract that accepted `fold` at a blocker-bearing exit carry exactly that row, and `check-unattended.sh` is a leg of `tools/gate-legs.json`. The bar is red at `48dae3b4` on the real corpus and no verb can rewrite the rows, so the diff cannot pass the push boundary until the refusal takes its own cutoff. Everything else is MEDIUM or LOW, and every one of it is the same shape: a fix that closed the round-1 defect on the path its own arm exercises and left a sibling path with the pre-fix behaviour or a new one. Eleven of the round-1 clusters closed; the fixes for A, B, C and F each carried one or two new defects, and the fixes for D, E, G, H, I, J and K hold with nothing new.

**Review shape:** raw 20 · confirmed 18 · refuted 2 · unverified 0 · precision 0.90.

**Run integrity:** lenses 4/4 returned, 0 DIED; skeptic batches 5/5 returned, 0 DIED; 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates. Every lens and every skeptic batch came back, so the finding set is complete for the lenses that ran, and a zero count in the checklist sweep below is positive evidence for those lenses rather than the artefact of a dead one. The pipeline's duplicate pass found none; the clustering below is this record's own, because ids 2, 7, 11 and 17 state one defect from four lenses, ids 8, 12 and 13 one defect from three, and each of the pairs 3/15, 5/18 and 10/19 one defect from two. The per-id table keeps all 18 rows so the integers returned to the caller agree with what was adjudicated here.

**Adjudicated severities:** BLOCKER 1 · HIGH 0 · MEDIUM 11 · LOW 6. Ten clusters. Two severities moved so that one defect carries one severity: id 17 RAISED from LOW to MEDIUM because it is the same defect as ids 2, 7 and 11; id 13 LOWERED from HIGH to MEDIUM because it is the same defect as ids 8 and 12, and its reachability rests on an argument the Skill never names and the harness's own args block does not list, so the shape is not the routine input the HIGH definition requires. No other severity moved. Counted per id, not per cluster, because that is what the caller's integers mean.

Severity meaning in this record, unchanged from round 1: BLOCKER — the diff cannot land: a red merge-bar leg, a dead suite, or a data-loss path on the landing itself. HIGH — a shipped mechanism gives the wrong answer on its routine input and something acts on that answer, or a rule the diff installs has no route through the program that is supposed to carry it; fixable inside the file. MEDIUM — a claim, a guard or a gate disagrees with the rule it exists to enforce, so a reader or a record can be wrong, but nothing acts destructively on it and a build still lands green. LOW — a sentence, a constant or an arm does not reproduce; no verdict changes.

---

## Per-id severity table

| id | severity | unit | address | cluster |
|----|----------|------|---------|---------|
| 6 | BLOCKER | 6 | `tools/unattended/check-unattended.sh:541`, `:552` | A |
| 2 | MEDIUM | 7 | `tools/workflows/unattended-build.template.js:769` | B |
| 7 | MEDIUM | 7 | `tools/workflows/unattended-build.template.js:769` | B |
| 11 | MEDIUM | 7 | `tools/workflows/unattended-build.template.js:769` | B |
| 17 | MEDIUM | 7 | `tools/workflows/unattended-build.template.js:769` | B |
| 8 | MEDIUM | 7 | `tools/workflows/unattended-build.template.js:593`, `:600` | C |
| 12 | MEDIUM | 7 | `tools/workflows/unattended-build.template.js:593`, `:600` | C |
| 13 | MEDIUM | 7 | `tools/workflows/unattended-build.template.js:593`, `:600` | C |
| 3 | MEDIUM | 7 | `tools/workflows/unattended-build.template.js:682`, against `unattended.sh:3683` | D |
| 15 | MEDIUM | 7 | `tools/workflows/unattended-build.template.js:726`, against `unattended.sh:3683` | D |
| 14 | MEDIUM | 7 | `tools/workflows/unattended-build.template.js:640` | E |
| 16 | MEDIUM | 7 | `tools/workflows/unattended-build.template.js:971`, schema `:382` | F |
| 9 | LOW | 7 | `tools/workflows/unattended-build.template.js:232`, `:234` | G |
| 5 | LOW | 3 | `tools/unattended/unattended.sh:2985` | H |
| 18 | LOW | 3 | `tools/unattended/unattended.sh:2985` | H |
| 10 | LOW | 6 | `tools/unattended/SKILL.template.md:680` | I |
| 19 | LOW | 6 | `tools/unattended/SKILL.template.md:680` | I |
| 20 | LOW | 6 | `memory/builds/aProbedUnit/RUN.md:80` | J |

---

## How each round-1 fix stands

Stated cluster by cluster in round 1's lettering, because that is the question this round was asked. The letters below this section are THIS record's clusters and do not correspond.

- **Round-1 A** (`--audit` graded from the last row). CLOSED. `print_audit` unions same-anchor rows per `(anchor, unit)` and lets a new anchor replace (`unattended.sh:2967-2975`), and skips a unit whose spec is CLOSED or WONTDO (`:2985-2990`); the `sibrows` comment at `:4985-4992` now says the two verbs ask one predicate over two populations on purpose. The two arms round 1 asked for exist. The status guard carries a new defect: cluster H below.
- **Round-1 B** (no audit route for a promoted spec). CLOSED on the path the Skill drives. The subject is `<slug>-spec-set-r<N>` keyed on `subjectRound` (`template.js:232-233`), `auditIds` scopes the resolver (`:597-599`), the disposal return carries `promotedIds`, the hand-out's `nextAction` orders the re-invoke (`:1151-1154`), and the terminal-subject refusal is its own throw (`:784-791`). Four new defects ride the fix: clusters C, E, G and I below.
- **Round-1 C** (the disposition's legal set). CLOSED at the driver and the gate: `fold` is refused at `NON-CONVERGENT|CEILING|BOUNDED` (`unattended.sh:4266-4269`), `--disposition promote` is accepted at `CONVERGED` and never required (`:4270`), check 2 reads a `CONVERGED · disposition …` row into `needs` (`check-unattended.sh:524-527`), and the four fixtures round 1 asked for are in `check-unattended.test.sh`. Two new defects ride it: the BLOCKER, cluster A below, and cluster B.
- **Round-1 D** (the reconciliation never checked the split). CLOSED. `minimum: 0` on both integers, `promoted >= blockers + highs` and `folded >= confirmed - promoted` as floors, and the `promoted > 0` / `promotedIds.length > 0` pairing (`template.js:968-973`). Nothing new here; the floors are what cluster B rides through, but that is the record order's defect, not the guard's.
- **Round-1 E** (BOUNDED labelled DEGRADED). CLOSED. `verdict !== 'CONVERGED' && verdict !== 'BOUNDED'` at `:1188`; CEILING and NON-CONVERGENT keep the label.
- **Round-1 F** (two callee shapes misread). CLOSED as asked: `unverified`, `lensesDead` and `skepticsDead` are read, `cleanRound` at `:682-684` distinguishes the clean shapes from the dead-lens one, the disposal runs over `confirmed + unverified` (`:901`), and the throw names the deaths. Two new defects: clusters D and F below.
- **Round-1 G, H, I** (the BOUNDED bullet's sentence; `-le`; the default typed twice). CLOSED. The bullet and the driver's BOUNDED echo at `:4295` both say "every CONFIRMED finding is DISPOSED BY SEVERITY"; the comparison is `-lt` with a sentence that says "at or above" (`:494`); `REVIEW_ROUNDS_DEFAULT=1` at `:221` is interpolated into the NOTE and the suite reads it out of the driver (`unattended.test.sh:5415`). Nothing new.
- **Round-1 J, K** (the POSIX root set; the expansion arm). CLOSED. `users`, `applications`, `library`, `system`, `nix`, `snap` join the set with a header stating why the list is wider than the corpus; the `TEMP=/tmp` arm asserts the tmp sentence; the `/Users/Shared/f` near-miss is beside the `/usr/local/x` control. Nothing new.

---

## BLOCKER

### A — the `foldbad` clause reds sixteen tracked records the driver wrote under the pre-rule contract (id 6)

`tools/unattended/check-unattended.sh:541` and `:552-553`, against `.unattended.conf:268` and the `rv_graded` derivation at `:485-498`.

**Finding.** Cluster C's fix added `else if (bl[it] > 0) foldbad = foldbad " " it "=" bl[it]` under the graded path and prints it as "the driver refuses this at write time, so the row reached this record by HAND". Graded means first-committed on or after `DISPOSITION_CUTOFF`, which this repo declares as `2026-09-01`. Sixteen tracked run-state files carry a `blockers N · NON-CONVERGENT|BOUNDED · disposition fold` row with N > 0, and every one of them was first-committed between `2026-09-01` and `2026-09-10`: `aGradedDialect` (`RUN.md` and `RUN.ABORTED.f76bcbd8.md`), `aHoistedPass`, `aKeyedAnnotation`, `aLeakedHandle`, `aPooledSweep`, `aQuenchedHarness`, `aReapedSpinner`, `aStagedLane`, `aSurfacedLexicon`, `aTunedCompass`, `aWeldedTribunal`, `dBriefedPass`, `dMispairedQuote`, `dSealedTally`, `dTracedLattice`. The driver accepted `fold` at every terminal exit until `48dae3b4` added the `fail 37` refusal in the same commit as the clause, so each row was written by the driver under the contract in force, and the message's "by HAND" is false for all sixteen. Reproduced here: `bash tools/unattended/check-unattended.sh` at `48dae3b4` prints `UNATTENDED check 2 FAILED` as its first line and names all sixteen. `tools/gate-legs.json` carries the leg, run-state files are append-only records no verb rewrites, and the push boundary runs the bar. The suite arm that observed the clause red (`check-unattended.test.sh`, "A FOLD BESIDE A NON-ZERO BLOCKER COUNT IS A REFUSAL") runs in a scratch fixture and never saw the corpus, which is §7's "run a candidate gate predicate over the real tree before wiring it" not done.

**Why BLOCKER.** A red merge-bar leg on the landing itself, not clearable by any edit the protocol permits to the rows it names. Raising `DISPOSITION_CUTOFF` is not a fix: every record before the new cutoff would fall back to the id-delta proxy, which demands one new unit id per exited subject and reds the same files for a different reason.

**Fix.** Give the fold refusal its own grandfather, using the idiom the loop already has. A core value `FOLD_CUTOFF="2026-09-14"` beside `DISPOSITION_CUTOFF` in the driver's `core_of` set (the day the severity rule made `fold` illegal at a blocker-bearing exit), `rv_foldgraded` derived from the same `rv_fc` date by the same `sort -C`, passed to the awk as `-v foldgraded=`, and `foldbad` accumulated only when `foldgraded == 1`. Reword the message to name the cutoff — "first-committed on or after FOLD_CUTOFF, after which the driver refuses this at write time" — and drop the assertion that the row was hand-written, because for the whole existing population it was not. The `fail 37` in the driver stays as it is; only the gate's reading of history changes.

**Left-shift.** Two fixtures in `check-unattended.test.sh`: a `blockers 2 · NON-CONVERGENT · disposition fold` row first-committed BEFORE the new cutoff that stays green (the grandfathered control), beside the existing post-cutoff one that reds. And a one-time observation before landing: `bash tools/unattended/check-unattended.sh` over the real tree exits 0, stated in the commit message with the sha it ran at. The gotcha class is `fixture-passes-by-finding-nothing`'s inverse — a fixture that reds correctly over a population the real tree does not have — and a candidate entry for `memory/gotchas/`: a ratchet that grades history needs a cutoff for EACH rule it grades, because a single cutoff dates the field, not every later rule about the field's value.

---

## MEDIUM

### B — the CONVERGED disposition is decided from `auHighs` before the disposal stage can promote an unverified finding (ids 2, 7, 11, 17)

`tools/workflows/unattended-build.template.js:769`, against `:901`, `:914-934` and `:968-973`; `check-unattended.sh:524-527`; `unattended.sh:4237-4240`.

**Finding.** The record command appends ` --disposition promote` iff `auBlockers === 0 && auHighs > 0`, and `auHighs` is the synthesis count over CONFIRMED findings. The round is recorded at `:761-779`; the disposal stage runs afterwards at `:892` onward, and cluster F's fix widened its population to `confirmed + unverified` with a prompt telling the agent to adjudicate each UNVERIFIED finding and PROMOTE any it grades BLOCKER or HIGH. The reconciliation at `:968-973` uses floors so that exactly this promotion is legal. So the shape `blockers 0, highs 0, unverified N` records a bare `CONVERGED` row, then disposal returns `promoted 1, promotedIds [X]`, and the hand-out carries `promotedIds` while the row carries no field. Probed by two lenses independently with the suite's runner: `review_out 0 0 0 1` plus a promoting double produced `--review tB --subject tB-spec-set-r1 --verdict "CLEAN" --blockers 0` and a hand-out with `promotedIds:["A-tB-9"]`. The subject is terminal after that row (`verb_review` refuses another round at `:4237`), the record is append-only, and check 2 enters a CONVERGED subject into `needs` only when its last field is `disposition …`, so this promotion demands no unit id from the bar. Reachable from the real callee, not only the double: `tier2-review.js:474` early-returns only when `confirmed + unverified` is 0, so `confirmed 0, unverified 1` runs synthesis and returns integer `blockers 0, highs 0`.

**Why MEDIUM.** The record is wrong and the bar cannot see the promotion — the exact blindness cluster C was raised for, one population over — but the harness's own reconciliation still forces `promotedIds` and the `nextAction` still orders the audit, so the promoted unit is not lost, only unobserved by check 2. Nothing acts destructively. Id 17 raised to MEDIUM to match its three siblings; the four ids are one defect at one line.

**Fix.** Order the stages so the field is derived from what was actually promoted. At `auBlockers === 0` the exit is CONVERGED before the driver names it — the comment at `:757-760` already says so — so on that path run the disposal stage FIRST and append ` --disposition promote` iff `promotedIds.length > 0` (equivalently `promoted > 0`); keep the current record-then-dispose order for `auBlockers > 0`, where the driver names the exit and every such exit records `promote`. At minimum, throw when `verdict === 'CONVERGED'`, no disposition was sent, and `promotedIds.length > 0`, naming the row the bar will not read. Mirror in the render.

**Left-shift.** A harness-suite arm: `review_out 0 0 0 2` with a disposal returning `promoted 1, promotedIds ["A-tB-9"]` must yield a `prompt:audit:record:r1:` line carrying `--disposition promote`. Stage the arm against the current order and observe it red before landing.

### C — a caller-supplied `subjects` array silently bypasses the `auditIds` scoping, and the log claims the scoping happened (ids 8, 12, 13)

`tools/workflows/unattended-build.template.js:593`, `:597-600`, `:605` and `:642`; the args block at `:138-156`; the hand-out at `:1151-1154`; `unattended-build.test.sh:731`.

**Finding.** `subjects` is taken verbatim from args when it is an array (`:593`), and the in-code contract at `:590-592` calls a caller-supplied set authoritative. `auditUnits` (`:597-599`) is consumed only inside `if (!subjects)` via `renderRoster` at `:605`, so with `subjects` present the scoping narrows nothing and `tier2-review.js` runs over the caller's set at `:642` under the fresh `<slug>-spec-set-r<N>` key. The log at `:600` fires on `auditIds.length` alone. Probed against the render with the suite's runner: `round:2, auditIds:["A-tB-3"], subjects:[s1,s2]` logged `scoped to 1 promoted unit(s) — A-tB-3 · subject tB-spec-set-r2`, spawned no resolver, handed the callee `s1,s2` only, recorded CONVERGED under `tB-spec-set-r2`, and rostered `A-tB-3` READY with its spec `s3` never audited. The suite's own round-2 arm strips `subjects` with the comment "so the resolver stage actually runs" (`:731`): the fixture worked around the seam instead of the code refusing it. `specs-audited` would catch the un-audited unit at `--close`, after it was built.

**Why MEDIUM, and id 13 lowered from HIGH.** The log line asserts a scoping that did not happen — `degradation-known-but-unreported`, inverted — and a record can be wrong. But `subjects` is absent from the harness's documented args block, absent from the Skill (grep: zero hits), and present only in the suite's fixtures and the comment at `:590`; the routine input, the Skill-driven first invocation and the `nextAction` re-invoke, takes the resolver path and is scoped correctly. A HIGH needs the routine input to give the wrong answer, and this one needs an argument only a reader of the source would pass. The stale-generation audit it produces is real when reached, which is why it does not drop to LOW.

**Fix.** When `auditIds.length` and `Array.isArray(a.subjects)`, refuse by name: "pass `auditIds` OR `subjects`, never both — a supplied subject set cannot be scoped to the promoted units by a runtime that cannot read their specs". Or intersect: `subjects = subjects.filter(s => auditUnits.some(u => u.specPath === s.path))` and throw if any `auditIds` unit's `specPath` is missing from the supplied set. Either way emit the `scoped to` log only after the scoping applied, and name `subjects` in the `nextAction` text ("and no `subjects`"). Mirror in the render; either fix is a handful of lines.

**Left-shift.** A harness-suite arm that keeps `subjects` and passes `auditIds`, asserting the refusal (or, under the intersect fix, that the `workflow` call's `subjects` names only the promoted spec — which needs the `workflow` double to record its args, since today it records `ref` only; that recording is the same change cluster E's arm needs).

### D — a clean round leaves no `**Serves:** spec-audit` record, and `specs-audited` reds every unit closed after it (ids 3, 15)

`tools/workflows/unattended-build.template.js:682-688` and `:726`, against `tools/workflows/tier2-review.js:385` and `:478`, `unattended.sh:3683-3735`, and `memory/builds/aProbedUnit/spec/2026-09-14-spec-TOOL-aProbedUnit-7.md:353-355`.

**Finding.** `tier2-review.js` returns `report: null` on both clean paths — zero findings at `:385`, all refuted at `:478` — and writes the binding line only in the synthesis pass those paths skip. Cluster F's fix accepts that shape as `cleanRound`, logs "no report written", passes `:726` with `lastReport` empty, and proceeds to the full hand-out. `specs-audited` is a machine `DOD_CORE` item: at `--close` it joins every CLOSED unit id against the first twelve unfenced lines of every tracked `.md` under the build for a `**Serves:** spec-audit` line, and with none at all returns 1 with "no TRACKED record under this build carries a spec-audit binding line at all". So a run whose audit round was clean builds every unit and then cannot close without `--override specs-audited`, with nothing to point the override at. Before the fold the same shape threw at the audit stage before any unit was built. Neither the log line at `:686` nor `nextAction` says a record is owed; BUILD-METHOD M4 says to record the round with the binding line regardless of verdict. Spec 7's rev-4 line names this as "surfaced and does not close" and attributes it to `tier2-review.js` and the DoD; no row in `memory/backlog/TOOL.md` or the build README tracks it.

**Why MEDIUM.** The bar is green and the refusal is a DoD item that is overridable by design, so a build lands. But the harness's contract on its cleanest path now contradicts the DoD that grades the same run, the contradiction is untracked, and the failure moved from an early named refusal to a late one with nothing to point at. Not HIGH because the mechanism that gives the wrong answer is the callee's report-writing, outside this diff, and the operator has M4's instruction and the override; the diff's part is having made that gap silent.

**Fix.** Make the evidence a required act rather than an absence. Either have the spec-mode callee write its zero-finding report with the binding line (it knows `kind` and the subject ids on both clean paths), or have the harness refuse the hand-out on `cleanRound` in unattended mode until a tracked `**Serves:** spec-audit <ids>` record exists, stated in `nextAction` with the ids it must name. Either way file the backlog row now, because a surfaced-and-unclosed sentence in a spec's rev line is not a tracked item.

**Left-shift.** A harness-suite arm driving `{confirmed: [], blockers: null, lensesDead: 0, unverified: 0, report: null}` and asserting the refusal or the record demand in `nextAction`. Under the callee fix, a `tier2-review` arm asserting a report path on the all-refuted return.

### E — the callee is handed the invocation round, so a promoted generation's first audit is primed as a FOLD review (id 14)

`tools/workflows/unattended-build.template.js:640`, against `tools/workflows/tier2-review.js:110`, `:339`, `:347` and `:537`.

**Finding.** The `workflow` call passes `round: roundNo` and never `priorFindings`. Under the kit default `REVIEW_ROUNDS=1` every promoted-spec audit lands at `roundNo >= 2`, so the callee takes `round: 2` and primes every lens with "this is a FOLD review. Aim at the text the previous round's fixes introduced, which is the only text in these documents nobody has reviewed" beside "PRIOR ROUND'S FINDINGS: none - this is a first-round review of the whole spec set", and tells synthesis to state the ROUND as 2 — over a spec nobody has reviewed at all. The harness holds the subject's own round, `roundNo - subjectRound + 1`, and keys the driver record with it correctly; the callee never receives it. This is the primary path cluster B routes, not an edge.

**Why MEDIUM.** The one audit a promoted spec gets is under-primed by construction and its report mislabels its round, so a record can be wrong; nothing acts destructively and the audit still runs.

**Fix.** Pass `round: roundNo - subjectRound + 1` to the sub-workflow (1 for a fresh generation, N for its Nth fold) and keep `roundNo` for the harness's own labels. Mirror in the render.

**Left-shift.** Extend the suite's `workflow` double to record its args, then an arm on the post-disposal shape (`round: 2, auditIds, no subjectRound`) asserting the callee received `round: 1`, and one on the fold shape (`round: 2, subjectRound: 1`) asserting `round: 2`.

### F — an UNVERIFIED finding the disposal agent judges not a defect has no honest route (id 16)

`tools/workflows/unattended-build.template.js:914-934`, `:971`, `DISPOSAL_SCHEMA` at `:382`; `memory/guides/BUILD-METHOD.md:140`.

**Finding.** The disposal prompt casts the agent as the substitute skeptic for the unverified population — "read the code yourself and take it at the severity you adjudicate" — then says M4 "admits no third route", "never parked, never waived, never retired, never re-reviewed", and "NAME in `standing` every finding you did NOT dispose". The schema has only `promoted`, `folded`, `standing` and `promotedIds`; the guard demands `promoted + folded + standing === confirmed + unverified`, and any non-empty `standing` returns DEGRADED with an empty roster. So a false positive left by a dead skeptic batch must be promoted to a unit, folded as a rev-N bump — which under `REV_SCOPE_CUTOFF` must name a section that MOVED, a false record for a non-defect — or named standing, which stalls the run. M4 scopes the severity rule to CONFIRMED findings; the fix applied it to findings no skeptic confirmed without adding the one verdict the skeptic would have supplied.

**Why MEDIUM.** A guard disagrees with the rule it enforces: forced spec pollution or a degraded run on any rate-limited verify phase, which is the case cluster F was written for. Nothing lands wrong; a record can be.

**Fix.** Add an optional `refuted: {type: 'integer', minimum: 0}` to `DISPOSAL_SCHEMA`, bounded by `au.unverified`, include it in the sum (`promoted + folded + refuted + standing === outstanding`), keep the severity floors as they are, and tell the agent it may refute an UNVERIFIED finding with a one-line reason in `summary`. Mirror in the render.

**Left-shift.** A harness-suite arm: `review_out 0 2 0 1` with a disposal returning `promoted 0, folded 2, refuted 1, promotedIds []` hands out the roster; the same with `refuted 2` (above `unverified`) is refused.

---

## LOW

### G — `subjectRound` and `auditIds` coerce a wrong-typed value to their defaults instead of refusing (id 9)

`tools/workflows/unattended-build.template.js:232` and `:234`, against the three by-name refusals that follow them.

**Finding.** A present-but-wrong-typed `subjectRound` (the string `"2"` an agent copying a log line produces) folds into `roundNo`, and a non-array `auditIds` into `[]`, while `mode`, `scratch` and `units` in the same block refuse by name. A string `subjectRound` on a fold re-invoke yields a fresh subject every round, so under `REVIEW_ROUNDS > 1` the driver's sequence resets and BOUNDED and NON-CONVERGENT can never fire — the loop the header at `:158-165` says the field exists to prevent. Only live under a raised `REVIEW_ROUNDS`, and the `auditIds` half is cost-only, since the fallback audits the whole set including the promoted spec; hence LOW.

**Fix.** Throw when `a.subjectRound !== undefined && !(Number.isInteger(a.subjectRound) && a.subjectRound > 0)` and when `a.auditIds !== undefined && !Array.isArray(a.auditIds)`, naming the field and the received JSON.

**Left-shift.** Two harness-suite arms passing `subjectRound: "2"` and `auditIds: "A-tB-3"`, each asserting the refusal.

### H — `print_audit` swallows `load_spec_facts`'s own refusal, and it is the one probe in the function with no liveness assertion (ids 5, 18)

`tools/unattended/unattended.sh:2985`, against `:1905-1927`, `:2952-2961`, `:2992`, `:3529-3531` and `:4874-4878`.

**Finding.** `load_spec_facts … >/dev/null 2>&1 || true` discards the producer's two REFUSING lines and its status, so on a failed read the maps are partial or empty, `st` reads empty, the `CLOSED|WONTDO` skip never fires, and the verb falls through to `check_pass_open` and the stall clock — grading a CLOSED unit STALLED and printing the kill-and-redispatch remedy the keepalive acts on, which is the round-1 cluster A behaviour with the cause discarded. `print_audit` sets `dead=` on `date`, `git log`, `stat` and `date -d`; this probe alone has none. The sibling at `:3529` announces the same failure as a skip and `:4874` fails safe with exit 49. Reachability is narrow (awk failing on a file `-r` accepted, or an index entry with no worktree file), and a re-dispatch of the closed unit is refused at `:4874-4878`, so LOW.

**Fix.** Treat it like the other probes: `load_spec_facts $(…) >/dev/null 2>&1 || dead="load_spec_facts over $M/builds/$slug/spec"`, so the run reaches the existing `fail 51` dead-probe exit instead of a false verdict. Or, at minimum, one stderr NOTE naming the exit code and that openness is graded from rows alone.

**Left-shift.** A driver arm: a spec path in the index whose worktree file is deleted, `--audit` exits 51 naming the probe (or prints the NOTE).

### I — the Skill's BOUNDED bullet says the harness keys a fresh subject "per invocation" (ids 10, 19)

`tools/unattended/SKILL.template.md:680`, rendered `.claude/skills/unattended/SKILL.md:680`; against `unattended-build.template.js:158-165` and `:232-233`.

**Finding.** The harness keys per spec-set GENERATION and its header names keying on the invocation round alone as the rejected design; a fold re-invoke under `REVIEW_ROUNDS > 1` must copy `subjectRound` to stay on one subject, and the Skill mentions neither `subjectRound` nor `auditIds` anywhere. Two answers to one question, Skill vs harness. Unreachable at the kit default, and the CONVERGING return's `nextAction` spells `subjectRound`, so LOW.

**Fix.** Reword the sentence: "It keys the `--review` subject per spec-set generation: a post-disposal re-invoke passes `auditIds` and no `subjectRound` and takes a fresh subject; a fold re-invoke copies the `subjectRound` the CONVERGING return handed back." The render follows.

**Left-shift.** None that fits beyond the byte-compare the Skill already has; a `grep -c 'per invocation'` arm on the template pins the count at 0.

### J — this build's own closing round-1 row carries no disposition beside five adjudicated HIGHs, and no note records the ruling to fold them (id 20)

`memory/builds/aProbedUnit/RUN.md:80`, against `reviews/…-diff-review-round1.md`, `README.md:41`, `SKILL.template.md:656-659` and `BUILD-METHOD.md:140`.

**Finding.** The row is `review · item aProbedUnit · reason verdict CLEAN WITH FIXES · blockers 0 · CONVERGED`, no field. The record it names adjudicated HIGH 5 and its own disposition section says clusters A and B are PROMOTED; the fix commit folded all eighteen, spec 3's rev-4 line records a HIGH cluster folded, and the roster still lists units 1..7. The Skill bullet this diff ships and the README's owner line both say a HIGH becomes a UNIT. No note in README, RUN.md or the specs records an owner ruling to fold the closing diff review's highs. With `DISPOSITION_CUTOFF=2026-09-01` the record is graded and check 2 reads the row as demanding nothing. The slug subject is terminal, so this round has no recordable `--review` row and the round-1 row cannot be amended. One caveat keeps it LOW: when `6c6fd1c6` wrote the row the driver still refused `--disposition` on CONVERGED, fixed in `48dae3b4`, so the row could not have carried the field; the gap is the unrecorded ruling.

**Fix.** At the close, record the ruling in the build README's build-level rules: the closing diff review's HIGHs were folded rather than promoted, by whose call, and that round 2 is unrecordable under the terminal slug subject. Decide whether the closing diff review's CONVERGED-with-highs case should re-arm the loop (fold and re-review, which is what this run did) rather than promote — the Skill's promote-at-CONVERGED bullet binds the slug subject too as written, and this run is the counter-example.

**Left-shift.** None machine-shaped: the ruling is a record, not a gate. The documented check is the README line.

---

## The recurring-bug-class checklist for this range — 29 classes swept

The classes `python tools/memory-tree/gotchas.py --for-diff` selected for `15697d57..48dae3b4`, each with where it fired or the statement that it did not. Every lens returned, so a "no finding" below is positive evidence for what four lenses and five skeptic batches read, not a claim about what they did not.

| class | fired | where |
|-------|-------|-------|
| fixture-passes-by-finding-nothing | yes | A (the foldbad fixture reds in scratch, never over the corpus); C (the round-2 arm strips `subjects` so the seam is never armed) |
| two-answers-to-one-question | yes | I (Skill vs harness header); J (the record vs the rule it ships) |
| amendment-leaves-its-other-half-standing | yes | B (disposal widened to unverified, the disposition decision not moved after it); D (the clean round accepted, the DoD term not consulted); F (the severity rule applied to unverified, the refute verdict not added) |
| degradation-known-but-unreported | yes | C (a log line claiming a scoping that did not happen); H (the refusal discarded) |
| one-value-field-records-a-mixed-outcome | yes | B (bare CONVERGED beside a promotion) |
| fold-text-is-unreviewed-surface | yes | every cluster here is in text `48dae3b4` introduced, which is what this round exists for |
| two-readers-of-one-config-one-re-derived | yes | E (the harness holds the subject round, the callee re-derives from the invocation round) |
| two-guards-one-question-two-answers | yes | H (four probes assert liveness, the fifth does not) |
| containment-tested-one-way | no | D's floors are deliberate and B rides them by ordering, not by containment |
| allowlist-narrower-than-the-root-it-guards | no | — |
| arm-literal-strands-on-message-edit | no | — |
| assertion-between-two-derived-values | no | — |
| bounded-through-a-pipe-is-unbounded | no | — |
| empty-field-collapses-unless-it-is-last | no | — |
| fallback-fabricates-the-passing-value | no | — |
| fixture-inherits-ambient-machine-state | no | — |
| fixture-removes-the-path-under-test | no | — |
| format-derived-from-arity | no | — |
| heredoc-escape-reaches-the-regex | no | — |
| id-matched-as-a-substring | no | — |
| inline-fence-swallows-the-rest-of-the-file | no | — |
| inputs-inside-the-subjects-reach | no | — |
| process-creation-is-the-suite-cost | no | — |
| second-implementation-is-not-a-second-opinion | no | — |
| staged-break-substitutes-a-synthetic-value | no | — |
| status-set-in-a-subshell | no | — |
| structured-record-split-on-whitespace | no | — |
| text-mode-read-eats-a-bare-cr | no | — |
| trace-profile-measures-itself | no | — |

Eight classes fired across the ten clusters; twenty-one did not. One candidate addition for `memory/gotchas/`, because no existing class names it: a ratchet that grades history against ONE cutoff dates the field, not every later rule about the field's value, so a new refusal about that field reds every record written between the field's cutoff and the rule's (cluster A).

---

## Disposition, as this record's severities imply

Under BUILD-METHOD M4 and the severity rule: cluster A is a BLOCKER and the rule PROMOTES it to a unit of this build, specced at Tier 1 (one cutoff, one awk guard, two fixtures, one real-tree observation) — but it is also the only thing between this diff and a green bar, and nothing may land before it does. Clusters B through J are FOLDED into the specs of units 3, 6 and 7 as `rev-N` bumps with §9 lines; cluster J's fold is a README line and a ruling, not a spec edit. Nothing is parked, waived or retired.

Two facts about this round's own record. First, the subject of a closing diff review is the build slug, and `RUN.md:80` already carries its CONVERGED row from round 1, so `verb_review` refuses a round-2 row (`unattended.sh:4237-4240`) and this record's binding line and the README are where the round lives — cluster J asks that the README say so. Second, because the bar is red at `48dae3b4`, the merge-scoped gate the landing protocol owes cannot be recorded green against this tip; the fix pass for cluster A is owed before any other fold here is worth verifying at the push boundary.
