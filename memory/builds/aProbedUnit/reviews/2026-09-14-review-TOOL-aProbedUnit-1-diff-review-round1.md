**Serves:** diff-review TOOL-aProbedUnit-1 TOOL-aProbedUnit-2 TOOL-aProbedUnit-3 TOOL-aProbedUnit-4 TOOL-aProbedUnit-5 TOOL-aProbedUnit-6 TOOL-aProbedUnit-7

# Tier-2 diff review — build `aProbedUnit`, the cumulative diff landing on `main`, round 1

Written 2026-09-14 on node `a` by the unattended-build harness's closing review stage (`tools/workflows/tier2-review.js` under `tools/workflows/unattended-build.js`): four primed finder lenses, an adversarial skeptic per finding in five batches, one synthesis pass. Subject: the seven built units of `memory/builds/aProbedUnit/` as one diff at the integration boundary, read at the tip named on the range line, which is worktree HEAD `15697d57` on `branch/unattended-build-stalls-6d0f2b`. Source claims below stand as the skeptic stage confirmed them, and this record re-derived the following against that tree before adjudicating: `bash tools/unattended/unattended.sh --audit aProbedUnit` printing `TOOL-aProbedUnit-4 · dispatched 2026-09-14T13:35:33Z · elapsed 6677s · last-write 2221s ago · last-commit 2318s ago · STALLED` followed by the `remedy — stop the unit's task, then re-dispatch` line, exit 0, while every unit of the build is CLOSED; the twelve `dispatch · item b7250a7f TOOL-aProbedUnit-4` rows in `memory/builds/aProbedUnit/RUN.md`, one path each, against the one row each of the other six units; `git diff-tree --no-commit-id --name-only -r 5b4620a8` naming neither `memory/LIVE.md` nor `memory/ledger/2026-09.md`; the awk at `tools/unattended/unattended.sh:2959-2963` keeping `last[u]`, `check_pass_open` at `:4787-4805`, and `verb_dispatch`'s per-row `sibrows` loop at `:4944-4951`; `review_state` at `:4087-4095`, the `-le` at `:487`, the state gate at `:4223-4236`, `review_exit_note` at `:4137-4143`; `.unattended.conf` declaring `UNIT_STALL_BOUND="1800"` and `REVIEW_ROUNDS="1"`, with the run's `phase: REVIEWING` and `keepalive: 0f1dca63`; the harness template's checks at `tools/workflows/unattended-build.template.js:625-660`, the record step at `:682`, the disposal stage at `:790-848`, the note predicate at `:1032` (byte-identical in the rendered `tools/workflows/unattended-build.js`), and `DISPOSAL_SCHEMA` at `:340-350`; `tools/workflows/tier2-review.js` returning `blockers: null, confirmed: []` at `:373`, `:385` and `:475-484`; `check-unattended.sh` check 2 at `:513-531` and check 23's same-anchor union at `:2263-2275`; the suite arms at `tools/unattended/unattended.test.sh:118`, `:4569`, `:4678-4681` and `:5356`; the AC7 loop at `tools/workflows/unattended-build.test.sh:181-184`; `POSIX_ROOT_CONVENTIONAL` at `tools/hooks/scratch-guard.js:379-382` beside `DRIVE_ROOT_CONVENTIONAL` at `:342` and the expansion branch at `:309`; and the `/tmp/other` arm at `tools/hooks/scratch-guard.test.sh:213`. The mutation id 21 reports was NOT re-run here; its claim stands on the skeptic's own reproduction. Nothing else was independently re-measured.

Reviewed range, pinned: `1b000d1a83998506bd2199cc815e34a9b82cdbf0...15697d570746e47629013a10f11548fab0c5262b` · ROUND 1.

## Verdict: CLEAN WITH FIXES

No merge-bar leg is red, no suite is dead, and every fix below is local to the file it names, so the token means what it says: nothing here asks the roster for a rule. What it does NOT mean is that the diff should land as it stands. Two HIGH clusters must be closed first, and the severity rule promotes both. Cluster A is live on this run right now: the `--audit` verb this build shipped, run against this build's own record, reports a unit that CLOSED hours ago as STALLED and prints the remedy the Skill orders the keepalive to act on, so the keepalive at `0f1dca63` is being handed a kill-and-redispatch order for `TOOL-aProbedUnit-4` on every tick until the fix lands or the run reaches a terminal phase. Cluster B means the two promotions this record produces have no harness route to a spec audit: the operator must record each promoted spec's audit by hand under a fresh `--subject`, which `verb_review` accepts and the harness alone hardcodes away. Seven MEDIUM ids are the disposition and disposal machinery disagreeing with the severity rule it was amended to serve, at four seams; six LOW ids are a doc sentence, an off-by-one, a twice-typed default, a short allowlist, and a branch no arm can red.

**Review shape:** raw 23 · confirmed 18 · refuted 5 · unverified 0 · precision 0.78.

**Run integrity:** lenses 4/4 returned, 0 DIED; skeptic batches 5/5 returned, 0 DIED; 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates. Every lens and every skeptic batch came back, so the finding set is complete for the lenses that ran, and a zero count in the checklist sweep below is positive evidence for those lenses rather than the artefact of a dead one. The pipeline's duplicate pass found none; the clustering below is this record's own, because ids 1, 6 and 19 state one defect from three lenses, ids 5 and 10 one defect from two, and ids 7 and 16 one defect from two. The per-id table keeps all 18 rows so the integers returned to the caller agree with what was adjudicated here.

**Adjudicated severities:** BLOCKER 0 · HIGH 5 · MEDIUM 7 · LOW 6. Eleven clusters. Three severities were RAISED here so that one defect carries one severity: ids 1 and 6 from MEDIUM to HIGH because they are the same defect as id 19, and id 5 from MEDIUM to HIGH because it is the same defect as id 10. No severity was lowered. Counted per id, not per cluster, because that is what the caller's integers mean.

Severity meaning in this record: BLOCKER — the diff cannot land: a red merge-bar leg, a dead suite, or a data-loss path on the landing itself. HIGH — a shipped mechanism gives the wrong answer on its routine input and something acts on that answer, or a rule the diff installs has no route through the program that is supposed to carry it; fixable inside the file. MEDIUM — a claim, a guard or a gate disagrees with the rule it exists to enforce, so a reader or a record can be wrong, but nothing acts destructively on it and a build still lands green. LOW — a sentence, a constant or an arm does not reproduce; no verdict changes.

---

## Per-id severity table

| id | severity | unit | address | cluster |
|----|----------|------|---------|---------|
| 19 | HIGH | 3 | `tools/unattended/unattended.sh:2962` | A |
| 1 | HIGH | 3 | `tools/unattended/unattended.sh:2962` | A |
| 6 | HIGH | 3 | `tools/unattended/unattended.sh:2962`, against `:4944` | A |
| 10 | HIGH | 7 | `tools/workflows/unattended-build.template.js:813` | B |
| 5 | HIGH | 7 | `tools/workflows/unattended-build.template.js:682` | B |
| 20 | MEDIUM | 6 | `tools/unattended/unattended.sh:4224` | C |
| 4 | MEDIUM | 6 | `tools/unattended/unattended.sh:4224` | C |
| 12 | MEDIUM | 7 | `tools/unattended/unattended.sh:4231`, `check-unattended.sh:513` | C |
| 2 | MEDIUM | 7 | `tools/workflows/unattended-build.template.js:842`, schema `:347` | D |
| 11 | MEDIUM | 6 | `tools/workflows/unattended-build.template.js:1032` | E |
| 14 | MEDIUM | 7 | `tools/workflows/unattended-build.template.js:790` | F |
| 15 | MEDIUM | 7 | `tools/workflows/unattended-build.template.js:635` | F |
| 8 | LOW | 6 | `tools/unattended/SKILL.template.md:669` | G |
| 7 | LOW | 6 | `tools/unattended/unattended.sh:487` | H |
| 16 | LOW | 6 | `tools/unattended/unattended.sh:487` | H |
| 23 | LOW | 6 | `tools/unattended/unattended.sh:486` | I |
| 9 | LOW | 5 | `tools/hooks/scratch-guard.js:379` | J |
| 21 | LOW | 5 | `tools/hooks/scratch-guard.test.sh:213` | K |

---

## HIGH

### A — `--audit` grades a unit's openness from its LAST dispatch row alone (ids 19, 1, 6)

`tools/unattended/unattended.sh:2959-2963`, against `:4944-4951` and `check-unattended.sh:2263-2275`.

**Finding.** `print_audit`'s awk keeps `last[u] = iso "\t" g "\t" substr($3, 8)` per unit, so a unit that declared its set as several same-anchor rows is asked about the last row's paths only. `check_pass_open` (`:4787`) then answers OPEN whenever the pass commit wrote nothing inside THAT row's set, which is the conservative reading `--dispatch` wants for a disjointness proof and the wrong one for a stall clock. Reproduced at the tip: `TOOL-aProbedUnit-4` has twelve one-path rows at anchor `b7250a7f`; its pass commit `5b4620a8` wrote the first row's `tools/workflows/unattended-build.template.js` and eleven others but not the last row's `memory/ledger/2026-09.md`, so the verb has reported the unit open since `13:35:33Z`. When the pipeline observed it the verdict was `PROGRESSING`; by the time this record was written the tree had idled through the close's full bar, which writes only under the git dir, and `bash tools/unattended/unattended.sh --audit aProbedUnit` prints `TOOL-aProbedUnit-4 · ... · STALLED` plus `remedy — stop the unit's task, then re-dispatch TOOL-aProbedUnit-4`. `SKILL.template.md:30-33` orders the keepalive on `STALLED` to stop the unit's task, `--park`, and re-dispatch. The verb never consults spec status, so `--plan`, which grades all seven units CLOSED, and `--audit` give two answers to one question. Meanwhile `verb_dispatch`'s `sibrows` loop asks `check_pass_open` about EVERY row (`:4944`), so the comment at `:4942-4943` ("shared with `--audit` so the two verbs cannot disagree about whether a pass is open") is false: for the same pass the two verbs answer differently depending on row order, and check 23 of the gate already unions same-anchor rows per (anchor, unit) for exactly this reason (`check-unattended.sh:2263-2275`, "a run that took the driver's own published repair ... had its first declaration silently discarded"). The multi-row shape is not exotic: `--writes` is repeatable, the driver's published repair is "declare again", and this run's own harness produced twelve rows for one unit.

**Why HIGH and not BLOCKER.** The bar is green and the verb is a probe; what acts on it is an agent reading a prompt, not a line of code. But the probe's routine input yields a kill order against a closed unit, on this run, now, and that is the definition of HIGH above. Not lowered to MEDIUM because the remedy is destructive by design and the keepalive is told to act, not to ask.

**Fix.** Two edits, both in `print_audit`. First, union same-anchor rows per unit and let a NEW anchor replace, mirroring check 23's key: in the awk, `if (u in ga && ga[u] == g) dc[u] = dc[u] " " substr($3, 8); else { ga[u] = g; ts[u] = iso; dc[u] = substr($3, 8) }`, then print `u, ts[u], ga[u], dc[u]`. Second, before grading clocks, drop any unit whose spec status is terminal: `load_spec_facts` is already called by `verb_dispatch` for the same file set, so resolve the unit's status the way `--plan` does and `continue` on CLOSED/WONTDO. The union alone closes the reproduced case; the status guard closes the general one, where a pass legitimately declared a path it never wrote. Delete the false sentence at `:4942-4943` or make it true by hoisting the row selection into one helper both verbs and the leg call.

**Left-shift.** A suite arm in `tools/unattended/unattended.test.sh`: dispatch one unit twice with one path each at one anchor, commit a change inside the FIRST path only, assert `--audit` prints `no unit is dispatched and open`. A second arm: one row, pass commit touching none of its paths, spec status CLOSED, same assertion. Stage the red on the awk as written before landing either.

### B — a promoted unit's spec has no audit route through the harness (ids 10, 5)

`tools/workflows/unattended-build.template.js:682` and `:806-816`; `tools/unattended/unattended.sh:486`, `:4209-4211`, `:3659-3706`.

**Finding.** The disposal prompt at `:813` tells the agent to promote every BLOCKER and HIGH via `--rescope --act add` and author its spec "so it is audited once as a spec and built like any other". Nothing performs that audit. The harness's only audit subject is the literal `slug + '-spec-set'` at `:682`. With the kit default `REVIEW_ROUNDS=1` (`:486`), any blocker confirmed at round 1 exits `BOUNDED` and the subject is terminal; on `CONVERGED` it is terminal too. A re-invocation at round N+1 sends its recording agent into `verb_review`'s `fail 37` ("this subject already carries a terminal review round", `:4209-4211`), the `--disposition promote` retry at `:688-690` hits the same refusal, `rv.token` is not a string, and `:695` throws "the round was not recorded". The Skill's dispatch loop (`SKILL.template.md:582-590`) builds whatever `--plan` grades READY with no audit step, and BUILD-METHOD M4 (`memory/guides/BUILD-METHOD.md:140`) mandates the promoted unit be "audited as a SPEC". At `--close`, `specs-audited` (`:3659-3706`) requires every CLOSED unit id to appear on a tracked `**Serves:** spec-audit` line; the round-1 record names only the ids the set defined then, so every promoted unit that closes reds the item and forces `--override specs-audited` or a hand-written record. Under the one-round default this is every promotion, and in this corpus round-1 spec audits confirm a blocker essentially always. This record's own two promotions will hit it.

**Why HIGH.** A rule the diff installs (unit 7's severity disposition, unit 6's one-round default) has no route through the program that is supposed to carry it, and the failure surfaces at `--close` as a refusal of a run that followed every instruction it was given. Not BLOCKER: the driver's `--review` accepts any `--subject`, so an operator can record the audit by hand, and the bar is green.

**Fix.** Key the recorded subject per invocation, `slug + '-spec-set-r' + roundNo`, so each re-invocation after a disposal is its own one-round bounded subject, and scope round N+1's `subjects` to the specs not yet named by a tracked spec-audit record (the ids `--rescope --act add` just created). Have the disposal stage return the promoted unit ids in its schema so the caller can do that without re-reading the roster. State the re-invoke-after-promotion step in the Skill's BOUNDED bullet. Until a line of the program does it, delete the "audited once as a spec" clause from the prompt: a promise the harness cannot keep is a claim, not a contract. The `verb_review` refusal should also come back to the harness as a distinct outcome rather than stderr, so `:695` can say "the subject is terminal, re-key it" instead of "the round was not recorded".

**Left-shift.** A `tools/workflows/unattended-build.test.sh` arm: a BOUNDED round with `blockers 1` and a disposal return of `promoted 1`, then a `round: 2` invocation over the promoted id, asserting the record step ran under a subject that is NOT `<slug>-spec-set` and that the run did not throw. And a driver arm in `unattended.test.sh`: after a BOUNDED round on `S-r1`, `--review ... --subject S-r2` is accepted.

**For this run.** The two promotions this record produces (clusters A and B) have no harness audit route by cluster B's own defect. Record each promoted spec's audit by hand: `bash tools/unattended/unattended.sh --review aProbedUnit --subject <new-unit-id> --verdict <token> --blockers <n>`, with the review record carrying `**Serves:** spec-audit <new-unit-id>`.

---

## MEDIUM

### C — the disposition field's legal set is out of step with the severity rule at both ends (ids 20, 4, 12)

`tools/unattended/unattended.sh:4223-4236`, `:494`, `:4139`; `tools/unattended/check-unattended.sh:513-531`; `VERBS.template.md:114-117`.

**Finding, first end (ids 20, 4).** `review_state` returns `CONVERGED` for count 0 unconditionally (`:4090`), so every exit that reaches the disposition gate — `NON-CONVERGENT`, `CEILING`, `BOUNDED` — carries at least one BLOCKER by construction. The severity rule this diff installs (VERBS `:116`: "promote whenever a blocker or high stood at the exit") promotes every BLOCKER, so `fold` can never be the legitimate value at any exit that takes a disposition. Yet `REVIEW_DISPOSITIONS=fold|promote` (`:494`) admits it, the state gate checks only presence, `review_exit_note fold` prints "the severity rule never folds a BLOCKER or HIGH" beside a row reading `blockers 3 · BOUNDED · disposition fold`, VERBS `:117` documents an unreachable "else `fold`", and check 2 reads `fold` as demanding NOTHING (`:530-531`). A `blockers 3 · disposition fold` row therefore passes check 2 with zero new unit ids while three blockers stand unpromoted — the hole the disposition field was added to close, reopened by the amendment leaving the old clause standing. The suite pins it legal at `unattended.test.sh:4678-4681`.

**Finding, second end (id 12).** The same rule disposes highs at `CONVERGED` (Skill: "its confirmed highs, mediums and lows are still disposed"; "the merge bar reads that field"), but `verb_review` refuses `--disposition` on `CONVERGED` as "not a terminal exit" (`:4231-4234`) and check 2's `needs` regex excludes `CONVERGED` rows (`:513`). A round converging at 0 blockers with N highs — the `aCollapsedScan` shape the diff cites as motivation — promotes N units through the harness's disposal stage with no recordable disposition, so the bar demands no ids for it and a promotion that never happened is invisible.

**Why MEDIUM.** The harness path always records `promote` at a terminal exit (the retry at `:688-690`), so the first hole needs an operator typing `fold`; the second leaves a promotion unobservable rather than undone. Nothing acts destructively; the record can be wrong.

**Fix.** At the state gate's `NON-CONVERGENT|CEILING|BOUNDED)` arm, refuse `fold`: `[ "$disposition" = fold ] && { fail 37 "--review exits $state with $blockers blocker(s) standing, and the severity rule promotes every blocker, so fold cannot be this exit's disposition"; return 1; }`. Accept an optional `--disposition promote` on `CONVERGED` (never required there), write it into the row, and extend check 2's `needs` to `CONVERGED · disposition promote` rows so `nneed` counts them. Have the harness record prompt append `--disposition promote` when `auRaw.highs > 0` at a `CONVERGED` exit, as it already does on the refusal path. Reword VERBS `:117` and the Skill's `fold|promote` bullet: `promote` is the only value a terminal exit can record; `fold` survives as the value for a record that exited with nothing above MEDIUM, which the driver can only reach at `CONVERGED` with highs 0, and that row needs no field. Drop check 2's "fold demands nothing" branch or make it red on `fold` beside a non-zero blocker count.

**Left-shift.** Flip the B2/D2 arms at `unattended.test.sh:4678-4681` to expect the refusal; add a `CONVERGED · disposition promote` arm to `check-unattended.test.sh` asserting `nneed` counts it; add an arm asserting `blockers 3 · disposition fold` is refused at write time.

### D — the disposal reconciliation never checks `promoted == blockers + highs` (id 2)

`tools/workflows/unattended-build.template.js:841-842`, `DISPOSAL_SCHEMA` at `:347-348`.

**Finding.** The one machine guard the severity rule has refuses only `promoted + folded + standing.length !== confirmed`. `au.blockers` and `au.highs` are in scope on that line, integers by the refusal at `:640`, and never compared. The schema puts no `minimum` on either integer. So `{disposed: true, standing: [], promoted: 0, folded: 10}` against confirmed 10 / blockers 2 / highs 3 reconciles, as does a negative `promoted`, and the roster is handed out with two blockers folded into prose. The round was already recorded `--disposition promote` by the retry at `:688-690` before disposal ran; `review_exit_note promote` then claims every BLOCKER was promoted; check 2 demands only one new id per exited subject, so one promotion beside two blockers passes the gate.

**Fix.** Extend the guard with the two equalities the rule implies once `standing` is empty: `d.promoted !== au.blockers + au.highs || d.folded !== au.confirmed - au.blockers - au.highs`, with a matching `why` string, and add `minimum: 0` to `promoted` and `folded` in `DISPOSAL_SCHEMA`. Same edit in the rendered `unattended-build.js`, or re-render.

**Left-shift.** A test-double arm in `unattended-build.test.sh` returning `promoted: 0, folded: confirmed` with `blockers > 0`, asserting the `disposal: NOT done` line and an empty roster.

### E — the hand-out note labels every BOUNDED exit DEGRADED (id 11)

`tools/workflows/unattended-build.template.js:1032`, byte-identical in the render.

**Finding.** The note is composed from `verdict !== 'CONVERGED'`, so `BOUNDED` — the routine spec-subject exit whenever a blocker is confirmed at round 1 under the kit default — yields `DEGRADED — 0 spec(s) refused, verdict BOUNDED`. The diff added `BOUNDED` to `REVIEW_TOKENS` and the record prompt and never touched the predicate. A real degradation (dead writers, refused specs) is now indistinguishable from a by-design exit in the one field a caller reads for run integrity, and the AC7 loop (`unattended-build.test.sh:181-184`) asserts only the roster for the four terminals, never the note.

**Fix.** `verdict !== 'CONVERGED' && verdict !== 'BOUNDED'`; keep `NON-CONVERGENT` and `CEILING` as degradations, because the driver's own CEILING line calls it a defect.

**Left-shift.** A `has` arm asserting the BOUNDED hand-out's `note` does not open with `DEGRADED`, and one asserting CEILING's does.

### F — the harness misreads two of the callee's return shapes (ids 14, 15)

`tools/workflows/unattended-build.template.js:625-660` and `:790`; `tools/workflows/tier2-review.js:373`, `:385`, `:449`, `:475-484`, `:499`.

**Finding, id 14.** The harness reads `blockers`, `confirmed`, `highs` and `report` from the audit return and nothing else; `tier2-review.js:449` computes `unverified` (no usable skeptic verdict, or contradictory ones), `:499` labels them "OUTSTANDING, not cleared", and `:571` counts `blockers`/`highs` over CONFIRMED findings only. A round with 0 confirmed and N unverified is recorded `CLEAN --blockers 0`, `CONVERGED`, logs "confirmed no finding, so nothing stands to dispose" at `:791`, and hands out the full roster over N outstanding findings. With confirmed > 0 beside unverified, the reconciliation at `:842` makes disposing an unverified finding a DEGRADED refusal, so the stage cannot dispose them either. A verify stage degraded by dead skeptic batches — the rate-limiter case the charter names — reads as clean.

**Finding, id 15.** The comment at `:635` calls the callee's all-refuted return one of "three degraded paths" and the new `Number.isInteger(auRaw.confirmed)` check at `:640` throws on its `confirmed: []`. That return's own note is "all findings adjudicated and refuted", a RESULT, degraded only when `lensesDead > 0`; the zero-findings return at `:379-386` is `clean: 0 findings`. Both carry `blockers: null`, so `:625` throws first (pre-existing since `78eb7488`) and the cleanest possible audit halts the run as "a DEGRADED run". The diff touches exactly this spot and makes the misreading load-bearing prose beside the check.

**Why MEDIUM.** Both are the adapter reading the wrong field or the wrong meaning; nothing lands wrong, but a degraded round can be read as clean (14) and a clean round cannot be read at all (15).

**Fix.** Read `auRaw.unverified`, `lensesDead` and `skepticsDead` beside `confirmed`. Run the disposal stage when `confirmed + unverified > 0`, hand the agent both populations, reconcile against their sum, and carry `unverified` out on every return as a stated integer. Distinguish the shapes on the callee's own fields: `confirmed` an empty array with `unverified === 0` and `lensesDead === 0` is CONVERGED at 0 (record it, announce the disposal skip, hand out the roster); keep the throw for `blockers: null` beside `lensesDead > 0`; reword `:635` to name the one degraded path it is. Same edits in the render.

**Left-shift.** Three test-double arms: `{confirmed: [], blockers: null, unverified: 0, lensesDead: 0, note: 'all findings adjudicated and refuted'}` hands out the roster; `{confirmed: 0, unverified: 2}` runs the disposal stage; `{blockers: null, lensesDead: 4}` still throws.

---

## LOW

### G — the Skill's BOUNDED bullet keeps the pre-severity-rule sentence (id 8)

`tools/unattended/SKILL.template.md:669-670`, rendered `.claude/skills/unattended/SKILL.md`; and the driver's own BOUNDED line at `tools/unattended/unattended.sh:4249`.

**Finding.** The BOUNDED bullet reads "exactly as at NON-CONVERGENT: every blocker still standing is DISPOSED", while the NON-CONVERGENT bullet it mirrors disposes "every CONFIRMED finding ... BY SEVERITY". Commit `15697d57` fixed the identical sentence in the section intro at `:640` and left this bullet standing. The driver's BOUNDED echo at `:4249` says "every standing blocker is disposed by severity", the same class one file over; this record adds it to the fix rather than as a finding, because it is the same amendment left half-applied.

**Fix.** "every CONFIRMED finding is DISPOSED BY SEVERITY, exactly as at NON-CONVERGENT"; the same words at `:4249`; re-render the Skill.

**Left-shift.** None that fits: the Skill is rendered and byte-compared, so the fix cannot rot once made. A `grep -c 'blocker still standing'` arm on the template, like the one the round-2 audit re-derived for the driver, pins the count at 0.

### H — `REVIEW_ROUNDS -le RUNAWAY_CEILING` accepts the one value its own sentence refuses (ids 7, 16)

`tools/unattended/unattended.sh:487`, `review_state` at `:4092-4093`.

**Finding.** `-le` accepts `REVIEW_ROUNDS=8`; `review_state` tests `n+1 >= RUNAWAY_CEILING` before `n+1 >= bound`, so a declared bound of 8 can never surface as BOUNDED, which is exactly the condition the refusal sentence ("the ceiling would fire first and the declared bound could never be reached") says it refuses. At that exit the CEILING branch tells a correctly configured project the predicate is defective and to record it in the README. The suite pins the mismatch (`unattended.test.sh:4569`, "the ceiling fires before a bound equal to it") and `mkconf` defaults the seventh positional to 8 (`:118`) as an off switch.

**Fix.** `-lt`, and default `mkconf`'s seventh positional to 7; no verb arm records seven rounds on a spec subject, so the existing arms hold. Or keep `-le` and say in the refusal that equality is unreachable too; the first is one character.

**Left-shift.** An arm asserting `REVIEW_ROUNDS=8` is refused at startup with exit 2.

### I — the REVIEW_ROUNDS default is typed twice (id 23)

`tools/unattended/unattended.sh:486`, against `:326-327`.

**Finding.** The two siblings pass `"$GATE_BOUND_DEFAULT"` / `"$UNIT_STALL_BOUND_DEFAULT"` and interpolate the same constant into their NOTE; this call passes literal `1` and types "kit default of 1 round" as prose, and the NOTE arm at `unattended.test.sh:5356` pins the prose copy. Raising the argument to 2 leaves the NOTE saying 1 and the arm green, in the one hoist whose purpose (`:300-306`) was one reader for three keys.

**Fix.** `REVIEW_ROUNDS_DEFAULT=1` beside the other two constants; `read_bound_key REVIEW_ROUNDS "$REVIEW_ROUNDS_DEFAULT" rounds "a spec-audit subject exits BOUNDED after the kit default of ${REVIEW_ROUNDS_DEFAULT} round(s)"`.

**Left-shift.** A `grep -c 'kit default of [0-9]'` arm on the driver pinning 0 literal-digit defaults in `read_bound_key` calls.

### J — `POSIX_ROOT_CONVENTIONAL` is narrower than the macOS root it guards (id 9)

`tools/hooks/scratch-guard.js:379-382`, against `:342` and `:87-100`.

**Finding.** The POSIX set holds `private` and `volumes`, so macOS was in scope, but not `users`, `applications`, `library` or `system`, while `DRIVE_ROOT_CONVENTIONAL` lists `users` and `resolveHomeRoots` mines `/users/<name>` homes. On a macOS adopter `echo x > /Users/Shared/f` is denied as "creates a NEW TOP-LEVEL entry at the POSIX root", a false sentence on every macOS host. No registered node is macOS, hence LOW; the kit is copy-installed and project-agnostic.

**Fix.** Add `users`, `applications`, `library`, `system`, and `nix`, `snap` for Linux.

**Left-shift.** One near-miss arm `echo x > /Users/Shared/f -> allow` beside the `/usr/local/x` control in `scratch-guard.test.sh`.

### K — no arm can red the non-empty temp-variable expansion (id 21)

`tools/hooks/scratch-guard.test.sh:213`, against `scratch-guard.js:309` and `README.md:185`.

**Finding.** Every set temp variable the fixture uses is itself an allowed root, so `$TMPDIR/y` and `$TEMP/a.log` are allowed whether or not they expand, and the one value that is not a root, `/tmp`, is exercised only through the literal `/tmp/other`. The skeptic's mutation (dropping `env[t[1]] ||` from `buildResolvedTarget`) left the suite at 97 passed. The branch is live — `TEMP=/tmp; echo x > $TEMP/other` is denied with it and allowed without — and has no observed failing case, which is the class §7 names.

**Fix.** Inside the `sg_probe = /tmp` branch add `run "TEMP=/tmp: \$TEMP/other expands and is denied (tmp)" 2 'echo x > $TEMP/other' Bash "$PRE_TMP"` and assert `$SENT_TMP` in stderr.

**Left-shift.** That arm is the gate; stage the mutation once to observe it red before landing.

---

## The recurring-bug-class checklist for this range — 31 classes swept

The classes `python tools/memory-tree/gotchas.py --for-diff` selected, each with where it fired or the statement that it did not. Every lens returned, so a "no finding" below is positive evidence for what four lenses and five skeptic batches read, not a claim about what they did not.

| class | fired | where |
|-------|-------|-------|
| two-guards-one-question-two-answers | yes | A (`--audit` vs `--dispatch` vs check 23); C (driver vs gate on `fold`) |
| two-answers-to-one-question | yes | A (`--plan` CLOSED vs `--audit` open); G; I |
| second-implementation-is-not-a-second-opinion | yes | A (`print_audit` re-selects rows the leg already unions); F (the harness re-decides what the callee calls degraded) |
| amendment-leaves-its-other-half-standing | yes | C (the `fold` clause); E (the note predicate); G (the BOUNDED bullet and `:4249`) |
| one-value-field-records-a-mixed-outcome | yes | C (`blockers 3 · disposition fold`; CONVERGED with highs and no field) |
| containment-tested-one-way | yes | D (the sum is checked, the split is not) |
| degradation-known-but-unreported | yes | F (`unverified` computed by the callee, read by nobody); E |
| fixture-passes-by-finding-nothing | yes | K; E (the AC7 loop asserts the roster, never the note) |
| fixture-removes-the-path-under-test | yes | K (the fixture's temp variables are roots, so expansion is never load-bearing) |
| allowlist-narrower-than-the-root-it-guards | yes | J |
| two-readers-of-one-config-one-re-derived | yes | I (the default, typed twice); H (the refusal and `review_state` disagree at equality) |
| fallback-fabricates-the-passing-value | no | — |
| staged-break-substitutes-a-synthetic-value | no | — |
| arm-literal-strands-on-message-edit | no | — |
| assertion-between-two-derived-values | no | — |
| bounded-through-a-pipe-is-unbounded | no | — |
| empty-field-collapses-unless-it-is-last | no | — |
| fixture-inherits-ambient-machine-state | no | — |
| fold-text-is-unreviewed-surface | no | — |
| format-derived-from-arity | no | — |
| heredoc-escape-reaches-the-regex | no | — |
| hookspath-resolves-into-another-checkout | no | — |
| id-matched-as-a-substring | no | — |
| inline-fence-swallows-the-rest-of-the-file | no | — |
| inputs-inside-the-subjects-reach | no | — |
| naming-leg-grades-what-python-named | no | — |
| process-creation-is-the-suite-cost | no | — |
| status-set-in-a-subshell | no | — |
| structured-record-split-on-whitespace | no | — |
| text-mode-read-eats-a-bare-cr | no | — |
| trace-profile-measures-itself | no | — |

Eleven classes fired across the eleven clusters; twenty did not. Two candidate additions for `memory/gotchas/`, because no existing class names them: a probe shared between a verb that wants the conservative answer and a verb that acts on the answer (cluster A: the same predicate is a refusal in one caller and a kill order in the other), and a prompt that promises a stage the program has no route to (cluster B). Both are left-shifted above as arms; the gotcha entries are the documented check for the class where no arm fits.

---

## Disposition, as this record's severities imply

Under BUILD-METHOD M4 and the severity rule this diff installs: clusters A and B are PROMOTED to units of this build, specced at Tier 2 and Tier 2 respectively, and their specs are audited by hand under a fresh `--subject` each, because cluster B is the reason the harness cannot do it. Clusters C, D, E and F are FOLDED into the specs of units 6 and 7 as `rev-N` bumps with §9 lines. Clusters G through K are FOLDED into units 5 and 6. Nothing here is parked, waived or retired.

The subject of this round is the build slug, so its bound is the runaway ceiling and it converges: 0 blockers this round is CONVERGED, and the round is recorded without a disposition, which is cluster C's second end applied to this very record — the two promotions it produces will be observable to check 2 only through the ids `--rescope --act add` creates, not through a field on the row.
