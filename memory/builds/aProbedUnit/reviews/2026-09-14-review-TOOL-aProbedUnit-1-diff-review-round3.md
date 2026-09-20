**Serves:** diff-review TOOL-aProbedUnit-1 TOOL-aProbedUnit-2 TOOL-aProbedUnit-3 TOOL-aProbedUnit-4 TOOL-aProbedUnit-5 TOOL-aProbedUnit-6 TOOL-aProbedUnit-7

# Tier-2 diff review — build `aProbedUnit`, the FOLD of closing diff review round 2, round 3

Written 2026-09-14 on node `a` by the unattended-build harness's closing review stage (`tools/workflows/tier2-review.js` under `tools/workflows/unattended-build.js`): four primed finder lenses, an adversarial skeptic per finding in five batches, one synthesis pass. Subject: the text the second fix pass `b2ec7945` introduced on top of round 2's tip `48dae3b4`, which is the fold of the eighteen findings in `reviews/2026-09-14-review-TOOL-aProbedUnit-1-diff-review-round2.md`. This round judges the FIX of each of those and any NEW defect the fix introduced; it does not re-raise the originals. It is the last fold round the run takes, so it names what would be a BLOCKER or HIGH at the landed tip and demotes the rest to the record. Source claims below stand as the skeptic stage confirmed them, and this record re-derived the following against the worktree at `1b117818` (the landed tip, one kit-version commit past `b2ec7945`, touching none of the files below) before adjudicating: `python tools/codebase-map/test_codebase_map.py` printing `FAIL test_generated_artifacts_are_fresh — STALE symbols.json` and exiting 1, then `gen_map.py --write` producing a ten-line delta that is exactly the two `writeRound` rows for `tools/workflows/unattended-build.js` and `.template.js`, restored to the tracked bytes afterwards; the last commit touching `memory/map/generated/symbols.json`, `10644061`, unit 5; the `codebase-map coverage + freshness` and `memory hygiene` legs in `tools/gate-legs.json`, both `subject: repo` with no `guard`; the hold at `unattended-build.template.js:1299-1315` and the `owed` derivation at `:1300`, byte-identical in the render at the same lines; the resolver prompt at `:645-647` and the harness's own statement at `:1211` that `specPath` is empty for every unit the spec stage just authored; `disposeFirst` at `:886-887`, the disposal prompt's `--rescope --act add` at `:988`, the deferred record at `:1102` and the terminal-subject throw at `:835-842`; the DEGRADED clause at `:1088`; `writeRound`'s definition at `:812`; the suite fixture `UNITS` at `unattended-build.test.sh:89` and arm D at `:828`; hygiene check 22 at `tools/memory-tree/check-memory-hygiene.sh:898-931` under `.memory-tree.conf:79` `REVIEW_VERDICT_CUTOFF="2026-08-22"`, and the word `Verdict` absent from the harness template; `FOLD_CUTOFF` at `tools/unattended/unattended.sh:511`, read at `check-unattended.sh:384`, keyed at `:520`, graded at `:562` and `:576`; `verb_review`'s `fail 37` at `unattended.sh:4190` and `:4252`; `REVIEW_ROUNDS_DEFAULT=1` at `:221` and `.unattended.conf:51`; `tools/unattended/SKILL.template.md:567-569` and `:654-659`; `memory/builds/aProbedUnit/README.md:45`; `.githooks/pre-commit`, which runs no map-freshness leg; and `python tools/memory-tree/gotchas.py --for-diff` over the range, which selected 28 classes. `bash tools/unattended/check-unattended.sh` run to completion at `1b117818`: exit 0, no `FAILED` line, so the round-2 BLOCKER's clause (check 2) is closed on the real corpus by this record's own measurement. `bash tools/memory-tree/check-memory-hygiene.sh` run twice at `1b117818`: once with this record untracked, exit 1 on check 12 alone (the §3 edge joins of specs 4, 5 and 6, stated below as an observation outside the range), and once with it intent-to-added, where check 9 additionally reports the build index stale by exactly this file — the fold commit regenerates it. The suite arms cited were read, not re-run; the run integrity figures are the pipeline's own.

Reviewed range, pinned: `48dae3b4a99e99f6c707a5829ba773484d92ae82...b2ec7945` · ROUND 3.

## Verdict: BLOCKED

One BLOCKER, and it is the merge bar again, from the other direction: the fold added a column-0 function to both harness files, the codebase-map enumerator indexes it, and `memory/map/generated/symbols.json` was not regenerated, so the unguarded `codebase-map coverage + freshness` leg is RED at the landed tip and `.githooks/pre-push` blocks the push. The fix is one command and a ten-line committed delta. Two HIGHs ride the clean-round hold that cluster D's fix installed, and both are the hold contradicting the term it exists to satisfy: the ids it tells the caller to bind are the roster's, not the audited set's, so the record it demands can certify a unit no audit read; and the record it specifies carries no verdict heading, so the armed hygiene check reds the file the harness told the run to write. Everything else is MEDIUM or LOW and goes to the record. All ten round-2 clusters closed on the path their arms exercise; the fixes for B and D each carried new defects, and the fixes for A, C, E, F, G, H, I and J hold with the A and I fixes each carrying one record-grade item. One fact from outside the reviewed range binds the landing and is stated in its own section below rather than counted: the `memory hygiene` leg is ALSO red at the landed tip, on check 12, over §3 edges the SPEC stage wrote at `2bdd0b0f` and no round since has run the leg over. Regenerating `symbols.json` is not the whole distance to a green bar.

**Review shape:** raw 13 · confirmed 12 · refuted 1 · unverified 0 · precision 0.92.

**Run integrity:** lenses 4/4 returned, 0 DIED; skeptic batches 5/5 returned, 0 DIED; 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates. Every lens and every skeptic batch came back, so the finding set is complete for the lenses that ran, and a zero count in the checklist sweep below is positive evidence for those lenses rather than the artefact of a dead one. The pipeline's duplicate pass found none; the clustering below is this record's own, because ids 2, 4, 9 and 11 state one defect from four lenses and ids 1 and 6 one defect from two. The per-id table keeps all 12 rows so the integers returned to the caller agree with what was adjudicated here.

**Adjudicated severities:** BLOCKER 1 · HIGH 3 · MEDIUM 5 · LOW 3. Eight clusters. Two severities moved so that one defect carries one severity, the rule round 2 set: id 6 RAISED from LOW to HIGH because it is the same defect as id 1 at the same line with the same fix, reached by a narrower route; id 9 RAISED from LOW to MEDIUM because it is the same defect as ids 2, 4 and 11. No other severity moved. Counted per id, not per cluster, because that is what the caller's integers mean.

Severity meaning in this record, unchanged from rounds 1 and 2: BLOCKER — the diff cannot land: a red merge-bar leg, a dead suite, or a data-loss path on the landing itself. HIGH — a shipped mechanism gives the wrong answer on its routine input and something acts on that answer, or a rule the diff installs has no route through the program that is supposed to carry it; fixable inside the file. MEDIUM — a claim, a guard or a gate disagrees with the rule it exists to enforce, so a reader or a record can be wrong, but nothing acts destructively on it and a build still lands green. LOW — a sentence, a constant or an arm does not reproduce; no verdict changes.

---

## Per-id severity table

| id | severity | unit | address | cluster |
|----|----------|------|---------|---------|
| 7 | BLOCKER | 7 | `memory/map/generated/symbols.json`, against `tools/workflows/unattended-build.template.js:812` | A |
| 1 | HIGH | 7 | `tools/workflows/unattended-build.template.js:1300` | B |
| 6 | HIGH | 7 | `tools/workflows/unattended-build.template.js:1300` | B |
| 10 | HIGH | 7 | `tools/workflows/unattended-build.template.js:1302-1311` | C |
| 2 | MEDIUM | 7 | `tools/workflows/unattended-build.template.js:886`, `:1102` | D |
| 4 | MEDIUM | 7 | `tools/workflows/unattended-build.template.js:886`, `:1102` | D |
| 9 | MEDIUM | 7 | `tools/workflows/unattended-build.template.js:886`, `:1102` | D |
| 11 | MEDIUM | 7 | `tools/workflows/unattended-build.template.js:835-850`, `:1102` | D |
| 5 | MEDIUM | 6 | `tools/unattended/unattended.sh:511`, `check-unattended.sh:520` | E |
| 8 | LOW | 7 | `tools/workflows/unattended-build.template.js:1299` | F |
| 12 | LOW | 7 | `tools/workflows/unattended-build.template.js:1088` | G |
| 13 | LOW | 6 | `tools/unattended/SKILL.template.md:567-569` | H |

---

## How each round-2 fix stands

Stated cluster by cluster in round 2's lettering, because that is the question this round was asked. The letters below this section are THIS record's clusters and do not correspond.

- **Round-2 A** (the `foldbad` clause reds sixteen pre-rule records). CLOSED for this repository. `FOLD_CUTOFF="2026-09-14"` sits beside `DISPOSITION_CUTOFF` in the driver (`unattended.sh:511`) with a header saying why it is a kit constant; `check-unattended.sh` reads it through `core_of` (`:384`), refuses a malformed one by name (`:440-443`), derives `rv_foldgraded` from the same first-commit date by the same `sort -C` (`:520`), and accumulates `foldbad` only under it (`:562`); the message names the cutoff and no longer asserts the row was hand-written (`:576`). The whole leg exits 0 at the landed tip. The grandfathered-control fixture is in `check-unattended.test.sh`. One record-grade item rides the constant: cluster E below, the adopter's window.
- **Round-2 B** (the CONVERGED disposition decided before the disposal could promote). CLOSED. `writeRound` is a function (`template.js:812`), `disposeFirst = blockers === 0 && outstanding > 0` (`:886`) skips the record, the disposal runs, and the record follows at `:1102` with ` --disposition promote` iff `promotedIds.length`. The suite arm round 2 asked for exists. The reordering carries the one ordering defect this record clusters as D, plus the attended-mode note in G — and it is the reordering that made the BLOCKER: `writeRound` is the column-0 definition the map indexes.
- **Round-2 C** (`subjects` bypassed `auditIds`). CLOSED. The pair is refused by name at the args block (`:272-283`), the `scoped to` log fires only inside the resolver branch (`:638-640`), and the `nextAction` says "no `subjects`". Nothing new.
- **Round-2 D** (a clean round leaves no spec-audit record). CLOSED as asked, by the second of the two routes offered: the harness withholds the roster on `cleanRound && !attended` and names the ids in `nextAction` (`:1299-1315`); the backlog row `TOOL-aProbedUnit-12` is filed and names the callee-side route as the follow-up. Three new defects ride the hold: clusters B, C and F below. B and C are the HIGHs of this round.
- **Round-2 E** (the callee handed the invocation round). CLOSED. `round: roundNo - subjectRound + 1` at `:684`. Nothing new.
- **Round-2 F** (no honest route for a refuted unverified finding). CLOSED. `refuted: {type: 'integer', minimum: 0}` in `DISPOSAL_SCHEMA` (`:426`), read at `:964`, in the sum. Nothing new.
- **Round-2 G** (`subjectRound` and `auditIds` coerced). CLOSED. Both refuse by name in the typed-args table (`:236-248`), beside `round`. Nothing new; cluster D below notes the guard checks type and cannot check terminality, which is not a defect of the guard.
- **Round-2 H** (`print_audit` swallowed `load_spec_facts`). CLOSED. `|| dead="load_spec_facts over $M/builds/$slug/spec"` at `unattended.sh:2999` reaches the existing `fail 51`. Nothing new.
- **Round-2 I** (the Skill said "per invocation"). CLOSED. The BOUNDED bullet (`SKILL.template.md:677-688`) now says per spec-set generation, names `auditIds` and `subjectRound`, and says the pair is refused. One record-grade item: the harness bullet two hundred lines above it was not amended for the new HELD state — cluster H below.
- **Round-2 J** (no ruling recorded for the folded HIGHs). CLOSED. `README.md:45` records that the closing diff review's HIGHs were folded, scopes the one-round-and-promote rule to spec audits, and says rounds 2 and 3 are unrecordable under the terminal slug subject. Nothing new.

---

## BLOCKER

### A — the fold added `writeRound` and did not regenerate `symbols.json`; the map freshness leg is RED at the landed tip (id 7)

`memory/map/generated/symbols.json`, against `tools/workflows/unattended-build.template.js:812` and the render at the same line; `tools/codebase-map/map_lib.py:406-416` (`JS_DEFINITION_RULES`); `tools/gate-legs.json`, leg `codebase-map coverage + freshness`.

**Finding.** Round-2 cluster B's fix turned the record into a function, `async function writeRound(disposition)` at column 0 in both harness files. The map enumerator's first JS rule matches exactly that shape, so the live derivation gains two `function` rows; the committed artifact was last regenerated at `10644061`, unit 5, before the harness existed in this form. Reproduced at `1b117818`: `python tools/codebase-map/test_codebase_map.py` prints `FAIL test_generated_artifacts_are_fresh — STALE symbols.json` and exits 1, and `gen_map.py --write` yields a ten-line insertion that is the two `writeRound` rows and nothing else (the tree was restored to the tracked bytes after the measurement). The leg is `subject: repo` with no `guard`, so every bar runs it, and `.githooks/pre-push` runs the bar on a default-branch push.

**Why BLOCKER.** A red merge-bar leg at the landing itself, and the charter forbids exempting the map legs to unblock. The coverage test passes, so no dossier claim is owed; only the artifact is stale.

**Fix.** `python tools/codebase-map/gen_map.py --write` and commit the ten-line `symbols.json` delta in the fold commit, the charter's same-commit rule for a generated artifact beside the edit that moved it. Nothing else.

**Left-shift.** The gate that caught this exists; what failed is that the fold commit was made without running it, and the tracked pre-commit runs no map leg (`.githooks/pre-commit:47-58` run hygiene, the manifest ratchet and the template size, each staged-scoped). Add a fourth: when a staged path matches the enumerator's inputs (`tools/**/*.{js,py,sh}`), run `gen_map.py` into a scratch and diff against the tracked artifact, refusing on a delta — it is seconds, and it turns a bar-time red on the push into a commit-time red on the edit. Stage this very state (the tip minus the regen) and observe it RED before wiring, the §7 rule for a new gate.

### Observed outside the range — the `memory hygiene` leg is red at the landed tip on check 12, and no round's lenses could have raised it

`memory/builds/aProbedUnit/spec/2026-09-14-spec-TOOL-aProbedUnit-4.md:103`, `…-5.md:93`, `…-6.md:110`, against `tools/memory-tree/check-memory-hygiene.sh:1764-1798` under `.memory-tree.conf:268` `SPEC_EDGES_CUTOFF="2026-09-08"`; `tools/gate-legs.json`, leg `memory hygiene`.

**Observation, not a finding of this round.** This is not one of the twelve confirmed ids and is not counted in the integers above: the text is outside `48dae3b4...b2ec7945`, so no lens was pointed at it, and the finding set's completeness claim does not reach it. It is stated because this round was asked what would block at the landed tip, and the answer is not cluster A alone. `check-memory-hygiene.sh` at `1b117818` exits 1 on check 12 with four lines: spec 4 declares **hands-off** `TOOL-aProbedUnit-5` and unit 5 declares no **consumes-from** `TOOL-aProbedUnit-4` back; spec 5 declares **hands-off** `TOOL-aProbedUnit-4` and unit 4 declares no **consumes-from** `TOOL-aProbedUnit-5` back; spec 6 declares **hands-off** `TOOL-aProbedUnit-7` and unit 7 declares no **consumes-from** `TOOL-aProbedUnit-6` back; and spec 5's **hands-off** `TOOL-aProbedUnit-4` points at `order` 4, which is BEFORE unit 5. Every one of those edges is byte-identical at `2bdd0b0f`, `15697d57`, `48dae3b4` and `b2ec7945` (traced), so the SPEC stage wrote them and every round since has carried them. Why nobody saw it: the edge joins are HELD under `--staged` by the check's own design (`:1764-1766`, "the push-boundary run is where the joins bind"), so the pre-commit that ran on every commit of this build never joined them; the `memory hygiene` leg is unguarded on the bar, but the last recorded full green (`<git-dir>/gate-full-green`, sha `1afd26c9`) predates `2bdd0b0f` and is not an ancestor of this tip, and each closing round ran only the leg its own finding named — round 2 `check-unattended.sh`, this round the map test — which is exactly the §7 sentence about a check nobody runs.

**What it takes.** Three lines and no judgement, since the verbs are a vocabulary: unit 5's edge to unit 4 is a **consumes-from** (unit 4 hands it the scratch path, unit 5 denies the wrong destinations — its own prose says so), so flip the verb at `…-5.md:93` and the order rule is satisfied with it; unit 5 then needs no further line because unit 4's **hands-off** `TOOL-aProbedUnit-5` at `…-4.md:103` is now mirrored; and unit 7 owes one **consumes-from** `TOOL-aProbedUnit-6` line in its `### Edges` block at `…-7.md:122-152`, which is what `…-6.md:110` already says it hands off. Both specs are CLOSED, so each edit rides a `rev-N` line under `REV_SCOPE_CUTOFF`, and unit 7's spec already takes one for clusters B and C. Then `bash tools/memory-tree/check-memory-hygiene.sh` at the fold commit, exit 0, stated in the commit message with the sha — the same one-time observation round 2 asked for `check-unattended.sh` and got.

**Left-shift.** The pre-commit holds the joins because the staged selection is one-sided; the bar is where they bind, and the bar did not run. The instrument that would have caught this on day one is the one this repository already declares and the run did not use: `gates-green` at `--close` runs the whole bar, so the DoD would have caught it — at the close, after every unit was built, which is the latest possible moment. Earlier and cheaper: `tools/unattended/unattended.sh --dispatch` (or the SPEC stage's commit step) could run `check-memory-hygiene.sh` unstaged over the build's own folder after the specs are committed, since a spec set is the one population whose edges are all present at once and joinable. Record beside `TOOL-aProbedUnit-8`, whose ruling that gates run once per session is the reason the bar was not run mid-build, and which this red is the first measured cost of.

---

## HIGH

### B — the clean-round hold binds the roster's ids, not the audited set's, so the record it demands certifies units no audit read (ids 1, 6)

`tools/workflows/unattended-build.template.js:1300`, against `:629-650` (the resolver and `auditUnits`), `:1211` (the harness's own note on `specPath`), `unattended.sh:3697-3745` (`specs-audited`); `unattended-build.test.sh:89` and `:828`.

**Finding.** `owed` is `auditUnits` minus `specRefused`. What `tier2-review.js` audited is `subjects`: caller-supplied, or resolver-returned only for units that HAVE a `specPath` and whose blob resolves at `HEAD`, with the prompt at `:645-647` ordering that an unspecced unit be omitted. The two sets diverge on the routine route, not an exotic one: the harness's own comment at `:1211` says `specPath` is empty for every unit the spec stage just authored, the spec writers are told AUTHOR ONLY, DO NOT COMMIT (`:534`), and no commit happens between stage 1 and stage 2 inside this script. So a first-generation run with any freshly-authored spec beside an already-present one audits the present ones, and the hold names all of them. Id 6 reaches the same line by a narrower route: a writer that drops a unit from all three of `authored`, `alreadyPresent` and `refused` (the merge at `:553-584` reconciles nothing against the writer's group) leaves it unspecced, omitted, unread, and named. The suite pins the wrong answer: `UNITS` at `:89` carries subjects `s1`, `s2` over three units, and arm D at `:828` asserts `**Serves:** spec-audit A-tB-1 A-tB-2 A-tB-3` — `A-tB-3`, spec `s3`, was never a subject.

**Why HIGH.** The mechanism gives the wrong answer on its routine input and a record acts on it: `specs-audited` at `--close` joins CLOSED ids against any tracked record's first-twelve-line Serves binding and is, by its own header, a has-ever-named lower bound. A record hand-authored on this instruction satisfies the term for a unit whose spec reached no reviewer — the never-audited-unit-closes class round 2's cluster C was raised for, now produced as tracked evidence. Id 6 raised from LOW to match id 1: one defect, one line, one fix.

**Fix.** Derive `owed` from what was handed to the callee, which this runtime holds: `auditUnits.filter(u => specRefused.indexOf(u.id) === -1 && u.specPath && subjects.some(s => s.path === u.specPath)).map(u => u.id)`. Throw by name when the intersection is empty — a clean round that covered no unit cannot be recorded as an audit of any, and the empty-subjects refusal at `:652` already states the principle. Say in the `nextAction` which units were NOT covered and that they owe a later audit, so the gap is named rather than closed by the binding line. Flip arm D to expect `A-tB-1 A-tB-2` and add an arm asserting `A-tB-3` is absent from the demanded line; regen the render.

**Left-shift.** The two arms above, staged against the current filter and observed RED first. The gotcha class is `assertion-between-two-derived-values`' cousin: the hold derived its ids from the roster while the audit derived its subjects from the tree, and the suite asserted the roster's answer. Candidate `memory/gotchas/` entry: a record whose ids are derived from the plan rather than from the act it records certifies the plan.

### C — the record the hold demands has no `## Verdict:` heading, and hygiene check 22 reds the file the harness told the run to write (id 10)

`tools/workflows/unattended-build.template.js:1302-1311`, rendered verbatim at `unattended-build.js:1302-1311`; against `tools/memory-tree/check-memory-hygiene.sh:898-931` under `.memory-tree.conf:79`; `tools/workflows/tier2-review.js:548-551`.

**Finding.** The hand-out prescribes a record whose first line is the Serves binding line and whose body "records the clean round", and the word `Verdict` appears nowhere in the harness. Check 22 is armed in this repo by `REVIEW_VERDICT_CUTOFF="2026-08-22"`, selects every tracked file under `memory/builds/*/reviews/` whose basename date is at or after it, and fails on `nv == 0` with "no `## Verdict:` line, so the record states no conclusion anything can read". The callee's own synthesis prompt orders that heading by name for exactly this check, and all four records under this build's `reviews/` carry exactly one. The `memory hygiene` leg is `subject: repo`, unguarded, and the `--close` DoD's `gates-green` term runs the bar; the tracked pre-commit also runs the staged hygiene leg when `memory/` is touched, so the red lands at the caller's commit of the demanded record.

**Why HIGH.** A rule the diff installs — write this record, then dispatch — has no route through the program that carries it: a caller following the instruction literally writes the one file the withholding exists to demand and the bar reds on that file. In an unattended run that is a halt, or a full-bar re-run at its 26-minute floor, on the harness's own instruction. Not BLOCKER because this repository's tip carries no such record and the bar is not red on it today.

**Fix.** State the record's opening order the callee already uses, in the `nextAction` text: first line `**Serves:** spec-audit <ids>`; a title line; a line naming each reviewed subject path and blob (the `subjects` array is in scope) and the round; then a heading that is exactly `## Verdict: CLEAN`; then the body quoting the callee's note. One `has` arm beside the cluster-D arms at `unattended-build.test.sh:826-831` asserting the withheld `nextAction` carries `## Verdict: CLEAN`. Regen the render.

**Left-shift.** The arm above, plus the structural one: the harness cannot run hygiene, but the caller can — the `nextAction` should name `bash tools/memory-tree/check-memory-hygiene.sh --staged` as the check to run before the commit, so the record grammar is verified where it is written rather than remembered. Class: `two-answers-to-one-question`, the harness's record grammar against the hygiene gate's, with the harness holding the shorter answer.

---

## MEDIUM

### D — on the dispose-first path the terminal-subject refusal fires after the disposal has written (ids 2, 4, 9, 11)

`tools/workflows/unattended-build.template.js:886-887` and `:1102`, against `:835-850` (the two `writeRound` throws), `:988` (the disposal prompt's `--rescope --act add`), `unattended.sh:4252` (`fail 37`, terminal subject), `:4780-4790` (`verb_rescope`'s exact-row dedupe).

**Finding.** Round-2 B's reordering moved the record after the disposal at zero blockers with something outstanding. The only place the harness learns that a review subject is terminal is the driver's `--review` refusal, surfaced as `terminalSubject: true` inside `writeRound`; `--rescope` is guarded by `refuse_if_terminal` on the RUN phase, never on the review subject. So on this path a re-keyed-wrong invocation — a stale `subjectRound` after process death or compaction, the resume route the Skill itself names, or a re-run after a HELD clean round instead of a dispatch from `--plan` — runs the disposal first: rescope rows on the append-only run record, authored promoted specs, rev-N bumps on folded ones; then the refusal. `verb_rescope` dedupes a byte-identical `(act, unit, reason)` row, but a re-run disposal mints fresh session-scoped ids under §2, so it adds a DIFFERENT unit and a second spec and the dedupe never fires. The throw at `:835-842` carries no `promotedIds` (they reach only the log line at `:1080`), its remedy says to pass "the hand-out's `promotedIds`" though no hand-out is returned, and the `!rv` throw at `:844-850` says nothing about a disposal that already ran. On the record-first path the same refusal fires before any mutation, as it did on both paths before the fold.

**Why MEDIUM, and id 9 raised.** A refusal placed after the side effects it exists to prevent is an ordering defect, not a design choice — the cluster-B comment at `:800-811` justifies dispose-before-record and never addresses the terminal-subject case. But it is reached only by caller error at the resume seam, the writes are recoverable from the RUN.md rescope rows, and no landing is wrong. Four ids, one defect, one severity. Follow-up, not a fold item: record it beside `TOOL-aProbedUnit-12`.

**Fix.** Probe before the disposal. The resolver agent at `:641-650` already holds a shell before the audit: have it also grep the run-state file for a terminal `review · item <subject> · reason …` row and return `subjectTerminal: boolean` (one optional key in `SUBJECTS_SCHEMA`), and throw the existing re-key error there, before any stage writes. On the dispose-first path compose both `writeRound` throws with the disposal's outcome — `promoted N · units <promotedIds>` and the hand-record command the DEGRADED note at `:1088-1092` already spells — so a caller can record by hand and audit the promoted ids rather than re-invoke over a mutated set. Mirror in the render.

**Left-shift.** One harness-suite arm on the dispose-first shape with the record double returning `terminalSubject: true`, asserting that no `agent:dispose:` line precedes the throw under the probe fix, or that the throw text carries `promotedIds` under the message fix. Class: `amendment-leaves-its-other-half-standing` — the reorder moved the record and not the refusal that rode on it.

### E — `FOLD_CUTOFF` is a kit date, so an adopter's own pre-rule rows red on the day it updates (id 5)

`tools/unattended/unattended.sh:511`, against `check-unattended.sh:384`, `:520`, `:562` and `:576`; `.unattended.conf:269`.

**Finding.** The cutoff names the day THIS driver's contract moved. The disposition field shipped at `7bd33a4d` on 2026-09-01 and the fold refusal at `48dae3b4` on 2026-09-14, so a kit version that accepts `fold` at a blocker-bearing exit and carries the field shipped for two weeks. An adopter that copy-installed in that window and updates later has every `blockers N · … · disposition fold` row its own driver wrote after 2026-09-14 graded as illegal from a date its driver never enforced — the round-2 BLOCKER's class, moved from this repository to the adopter. No in-contract remedy exists: check 2 reads no waiver registry, `--review` refuses a terminal subject so no corrected row can follow, and the kit's copy-install-never-edit model makes hand-editing the constant the only route. It fires only where the adopter declares `DISPOSITION_CUTOFF` (blank disarms `rv_graded` and so `rv_foldgraded`). For this repository the tip is green.

**Why MEDIUM.** A gate disagrees with the rule it enforces for one population — records written under a contract that permitted them — and the adopter can be wrong with nothing to point at. Nothing lands wrong here. Adopter-window only, so a record item.

**Fix.** Read the cutoff the way `DISPOSITION_CUTOFF` is read: an adopter-declared `.unattended.conf` key that the kit installer stamps at install or update, defaulting to the kit constant when unset and announcing the source on stdout, keeping the malformed-is-a-refusal arm. Or key the grandfather on the kit version recorded in the run-state file's authored half rather than on a date. One fixture: a record first-committed after 2026-09-14 under a conf cutoff later than it reads as grandfathered.

**Left-shift.** The fixture above. The class is the one round 2 proposed for `memory/gotchas/` and this is its second instance: a ratchet that grades history needs a cutoff per rule it grades, and the cutoff must be the ADOPTER's date for that rule, not the kit's.

---

## LOW

### F — the hold fires on a fold re-invoke whose round-1 report already carries the binding line (id 8)

`tools/workflows/unattended-build.template.js:1299`, against `:770` and `tier2-review.js:563`.

**Finding.** The hold is `cleanRound && !attended` with no test on `subjectRound < roundNo`. On a fold re-invoke the round-1 audit necessarily wrote a report (the CONVERGING path throws at `:770` when `!lastReport && !cleanRound`), and that report's first line is the Serves binding line for the same ids; `specs-audited` is has-ever-named, so the round-1 record already satisfies it and the demanded record is redundant. Reachable only where an adopter declares `REVIEW_ROUNDS >= 2`; under the kit default a spec subject exits BOUNDED at round 1.

**Fix.** Skip the hold when `subjectRound < roundNo`, or have the caller pass the prior report path so the hold can name it as the record. Record beside `TOOL-aProbedUnit-12`.

**Left-shift.** One arm: the fold shape (`round: 2, subjectRound: 1`) with a clean return hands out the roster.

### G — the DEGRADED hand-record note hands an attended caller a verb that refuses (id 12)

`tools/workflows/unattended-build.template.js:1088`, against `unattended.sh:4190` and GROUND at `:453-454`.

**Finding.** The clause is gated on `disposeFirst` alone and tells the caller to run `--review … --verdict "CLEAN" --blockers 0`; in attended mode there is no run-state file and `verb_review` fails 37 on its first line. GROUND already says the recording verbs are unavailable in that mode, so the return contradicts its own ground text.

**Fix.** Gate the clause on `disposeFirst && !attended`; in attended mode say the promotion is a README roster row, as the disposal prompt at `:985-987` already does.

**Left-shift.** One `has`/`lacks` arm pair on the attended dispose-first shape.

### H — the Skill's harness bullet lists no HELD state (id 13)

`tools/unattended/SKILL.template.md:567-569` and `:654-659`; rendered `.claude/skills/unattended/SKILL.md`.

**Finding.** The bullet still says the harness "hands back the ordered roster only on a terminal `--review` verdict", and the CONVERGED bullet says the loop is done for that subject, while the fold returns a terminal CONVERGED with `roster: []`, a `HELD AT HAND-OUT` note and a `nextAction` demanding a record and a `--plan --paths` dispatch. Only the BOUNDED bullet was amended. The return's text is explicit, so no wrong act follows.

**Fix.** One sentence in the harness bullet naming the withheld clean-round shape and that `nextAction` carries the record grammar and the resume route; the render follows and its byte-compare gate catches an unrendered edit.

**Left-shift.** None beyond the byte-compare the Skill already has. Class: `amendment-leaves-its-other-half-standing`.

---

## The recurring-bug-class checklist for this range — 28 classes swept

The classes `python tools/memory-tree/gotchas.py --for-diff` selected for `48dae3b4..b2ec7945`, each with where it fired or the statement that it did not. Every lens returned, so a "no finding" below is positive evidence for what four lenses and five skeptic batches read, not a claim about what they did not.

| class | fired | where |
|-------|-------|-------|
| fixture-passes-by-finding-nothing | yes | B (arm D pins the roster's ids, so the seam between roster and subjects is never armed) |
| amendment-leaves-its-other-half-standing | yes | D (the record moved, the refusal riding on it did not); H (the BOUNDED bullet amended, the harness bullet not) |
| two-answers-to-one-question | yes | C (the harness's record grammar against hygiene check 22's); E (the kit's date against the adopter's) |
| assertion-between-two-derived-values | yes | B (ids derived from the plan, subjects derived from the tree, the record asserts the plan) |
| fold-text-is-unreviewed-surface | yes | every cluster here is in text `b2ec7945` introduced, which is what this round exists for; A is the purest case — a definition added by a fold, indexed by a gate nobody ran |
| degradation-known-but-unreported | yes | D (the terminal-subject throw carries no `promotedIds` after a disposal that ran) |
| two-guards-one-question-two-answers | no | — |
| one-value-field-records-a-mixed-outcome | no | — |
| two-readers-of-one-config-one-re-derived | no | — |
| containment-tested-one-way | no | — |
| arm-literal-strands-on-message-edit | no | — |
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

Six classes fired across the eight clusters; twenty-two did not. One candidate addition for `memory/gotchas/`, because no existing class names it and cluster A is its cleanest instance: a generated artifact goes stale on the commit that adds the definition it indexes, and the gate that would catch it runs at the push boundary while the edit happens at the commit — the same-commit rule for generated artifacts needs a commit-time check, or it is remembered.

---

## Disposition, as this record's severities imply

Under BUILD-METHOD M4 and the severity rule, read with `README.md:45`, which scopes promote-at-CONVERGED to spec audits and lets the closing diff review converge by fixing: cluster A is the BLOCKER and is one regenerated artifact in the fold commit; nothing may land before it. Clusters B and C are the HIGHs and fold into unit 7's spec as a `rev-6` bump with §9 lines — each is a handful of lines in the hold plus two suite arms and a regen of the render. Clusters D, E, F, G and H are demoted to the record as this round was asked to do: D, F and G beside `TOOL-aProbedUnit-12`, whose row already names the hold; E and H as their own backlog rows under `TOOL`. Nothing is parked, waived or retired.

Two facts about this record. First, the subject of a closing diff review is the build slug, `RUN.md` carries its CONVERGED row from round 1, and `README.md:45` already says rounds 2 and 3 live under `reviews/` — this file is where round 3 lives, and it adds one to the README's generated record count, so the fold commit that carries it regenerates the build index. Second, two legs are measured red at `1b117818`: `codebase-map coverage + freshness` on cluster A, which this diff introduced, and `memory hygiene` on check 12, which the SPEC stage introduced at `2bdd0b0f` and which is stated above as an observation outside the range. Once `symbols.json` is regenerated and the three edge lines are written, no measured leg is red on this tip; the two HIGHs are defects in an instruction the harness emits, not in a leg the bar runs. The legs this record measured are those two plus `check-unattended.sh`; the rest of the bar was not run here and is owed at the push boundary as always.
