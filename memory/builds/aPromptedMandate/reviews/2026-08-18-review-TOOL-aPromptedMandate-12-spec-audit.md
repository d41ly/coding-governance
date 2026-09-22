# aPromptedMandate — M4 spec audit, units 12 and 13

**Serves:** spec-audit TOOL-aPromptedMandate-12 TOOL-aPromptedMandate-13

## Verdict: BLOCKED

Spec-set audit (M4) at base `6517579f`, over the two units added at CLOSE of a finished six-unit
build after the owner ratified fixing both defects rather than overriding past them.

Eleven confirmed defects across seven distinct sites, fourteen refuted, none left unverified. Both
units' CENTRAL claims survive: the `unit_rows` narrowing is the right discriminator, and a live
control is the right way to stop a `timeout` from asserting a cause. What blocks is what each spec
left OUTSIDE its own scope:

- **Unit 7's seam is not a seam.** `verb_status` open-codes the identical pipeline inline
  (`unattended.sh:1424`) and never calls `unit_rows` or `nonterminal_units`. §10 certifies
  `unit_rows` as "the single reader"; the driver's own comment at :970-972 says a second copy would
  be "two answers to one question in the two verbs that report on the same region" — and post-fix
  that is exactly what ships. The second answer is already wrong and measurable today: `--status`
  on `aBranchedMandate` reports the record filename `2026-08-16-build-TOOL-aBranchedMandate-3-repro-c3.sh`
  as the next unit.
- **Unit 8's live control has no width.** The single load-bearing parameter is left as "a known-good
  width", and the clamp resolves the arm's own values to 1 and 64, neither of which the file's
  everywhere-else width (4) matches. Pick 4 and subject and control differ in width AND clamp path,
  so the spec's own rule ("control finished -> the clamp is the difference") readmits the false
  accusation under exactly the contention that produced the measured incident.
- **Unit 8's whole product is two branches nothing can execute.** Both new branches are reachable
  only when `timeout 60` expires, and neither §2 nor §4 gives the harness a lever to force that.
  `check-arms.py` excludes `*.test.sh` outright, so the meta-gate written for this class cannot see
  them either. AC1 is then the only criterion that runs, and it passes identically over a control
  that is correct, mis-wired, or absent — the arm-that-cannot-fire class, reproduced one level down
  inside the unit written to remove one.
- **Unit 8's AC4 is unsatisfiable in both readings**, and one reading reds a bar leg AC4 itself
  requires green.

Spanning both: **the two units' ids are double-allocated** against open backlog rows about different
subjects, which breaks every id-keyed reader in the tree and is not caught by any gate.

## How the audit ran

Tier-2 per `memory/guides/REVIEW-PROTOCOL.md`: **3 primed finder lenses** in one wave over both
specs, `memory/TEMPLATE-SPEC.md`, `memory/guides/BUILD-METHOD.md`, the build README and roster,
`memory/backlog/TOOL.md`, and the two subjects in source — `unit_rows` / `nonterminal_units` / the
`build-complete)` arm in `tools/unattended/unattended.sh`, and the clamp arm at
`tools/run-gates.test.sh:194-206` against the clamp itself at `tools/run-gates.sh:69-82`; then
**batched default-refute skeptics** within the protocol's 5-agent cap; then this synthesis pass,
which re-verified every confirmed row against source rather than against the skeptic's prose.

| Stage | Count |
|---|---|
| raw findings from the lenses | 25 |
| confirmed after the refute pass | 11 |
| refuted | 14 |
| unverified (no verdict returned) | 0 |
| distinct sites behind the confirmed set | 7 |
| precision — confirmed / (confirmed + refuted) | 0.44 |

**Precision is BELOW the protocol's 0.5 floor and is recorded as such rather than rounded past.** The
target was two short specs, and the lenses over-fanned on them: four of the fourteen refutations are
the same term-numbering nit raised independently (ids 3, 12, 24) or the same perf-line nit raised
twice (15, 22), and three pairs/triples of the CONFIRMED set are one defect found by more than one
lens (1/17, 6/9/19, 8/21). Counted by distinct site the precision is 7/21 = 0.33. The lesson matches
the protocol's own guidance: two small specs did not earn three lenses.

The lenses were briefed with the by-design list — the owner's ratification of both fixes, unit 8's
deliberate non-raising of the timeout, its deliberate non-change to run-gates' output surface, and
the no-retroactive-edit rule for landed builds — so nothing below re-litigates those. Findings carry
the audit-batch id in the first column so each traces back.

## Confirmed — the folds

Seven sites. Severity is the skeptic's, after refutation.

### Unit 7 — `TOOL-aPromptedMandate-12`

| id | Sev | Site | Defect | Fold |
|---|---|---|---|---|
| 1, 17 | blocker | §10 Reuse audit, §2 S1, §4 Files touched | `unit_rows` is NOT "the single reader". `verb_status` (`unattended.sh:1424`) open-codes `region … \| grep -E '^\| \[' \| grep -vE '\| (CLOSED\|WONTDO) \|' \| head -1 \| sed …` inline and never calls `unit_rows` or `nonterminal_units` — grep finds `nonterminal_units` only at its definition (:978) and in `build-complete` (:1587). A builder following §4's "one function" narrows :977 alone, and `--close` then reads the units table while `--status` keeps reading the records table. Already live and measurable: `--status aBranchedMandate` prints `next 2026-08-16-build-TOOL-aBranchedMandate-3-repro-c3.sh`; `aStandingWrit` prints `next 2026-08-11-review-TOOL-aStandingWrit-1-1.md`. The extraction's own S6 comment says the duplicate is the thing it exists to remove, and claims the pipeline was "extracted out of verb_status's inline pipeline" while that copy is still live. | Add **S1b**: `verb_status`'s `unit=` derivation is replaced by `nonterminal_units "$(readme_of "$slug")" \| head -1 \| sed …`, so both verbs read one selector. Add an AC: `--close`'s and `--status`'s views of one region agree — `--status` on a landed build whose units are all CLOSED reports `next (no non-terminal unit)`, never a record filename. Name `verb_status` in §4 and correct §10's single-seam claim. |
| 16 | low | §4 (the proposed `unit_rows` body) | `grep -E '^\| \[[^]]*\]\(spec/'` silently DROPS any unit row whose label contains a `]`, and a dropped unit row is a false GREEN — `nonterminal_units` cannot see it, so `build-complete` passes over an unfinished unit. `gen_build_index.py:590` builds the label as `f"{u['id']} — {u['title']}"` with no escaping, and the title comes from `H1_RE`'s `(?P<title>.+?)`, so any character reaches the row. Executed against a bracket-carrying row: the proposed selector drops it, the current `^\| \[` keeps it. S3 and §5 arm only TOTAL vacuity, never partial loss; `missing_units` cannot catch it because the spec file exists. The narrowing INTRODUCES a blind spot the current selector does not have. | Split the two questions instead of one fragile pattern: `region … \| grep -E '^\| \[' \| grep -F '](spec/'`. Same cost, no bracket sensitivity, and the link-target rule stays the single discriminator §4 argues for. |
| 23 | medium | §4 The discriminator, measured | The `aPromptedMandate` row (`9` rows matching `^\| \[`, `6` linking `spec/`) is stale: the tree yields 11 / 8, and `git show 721ed41:memory/builds/aPromptedMandate/README.md` — the commit that ADDED this spec — already yielded 11 / 8, so the row disagreed with its own commit's tree. The other two rows reproduce exactly (13/6, 3/1), so a builder checking the design finds one row wrong and two right and cannot tell whether the selector, the measurement or the tree moved. The sentence it carries ("the `spec/` count equals the unit count in all three") is the section's load-bearing claim and holds only at the corrected numbers. | Re-measure the row to 11 / 8, or state that it was taken at the six-unit roster and that rostering units 7-8 moves both columns by two while the equality holds. The charter names this class outright — "after the spec twice stated a figure the tree then moved underneath". |

### Unit 8 — `TOOL-aPromptedMandate-13`

| id | Sev | Site | Defect | Fold |
|---|---|---|---|---|
| 8, 21 | blocker | §6 AC2 + AC3, §2 S1-S3, §4 | The unit's entire deliverable is two branches reachable ONLY when `timeout 60` expires, and nothing in S1-S4, the §4 pseudocode, or the files-touched list gives the harness a knob to force an expiry — the only recorded reproduction is environmental ("with four concurrent full bars on this node"), which is not a harness capability. On a healthy host AC2 and AC3 are conditionals whose antecedent never occurs, leaving AC1 ("exits 0 as it does today") as the only criterion that runs over the new code — and it passes identically whether the control branch is correct, wrong, or absent. `run-gates.test.sh` is a bar leg, so the branches cannot be exercised by deliberately reddening the suite either, and `check-arms.py:121` excludes `*.test.sh` outright, so the meta-gate for this class cannot see them. | Split the DECISION from the MEASUREMENT: extract a `clamp_verdict` helper taking the subject rc and the control rc, returning clamped / spun / undecidable plus its message, and assert all three on synthetic rcs (0 and 124) as ordinary in-suite arms, leaving `timeout` as the only real-timing part. Optionally make the budget injectable (`${GATE_CANARY_BUDGET:-60}`) so one arm forces a genuine expiry deterministically. Neither edit raises the timeout nor touches run-gates' output surface, so §3's non-goals stand. |
| 6, 9, 19 | blocker | §6 AC4, §4 Files touched | AC4 names a witness that does not exist and, satisfied literally, reds a gate AC4 requires green. `tools/run-gates.test.sh` prints no assertion count at all — no `n` counter, no `FLOOR_ASSERTIONS`, no `PASS (… assertions)` line; it ends `[ "$fail" = 0 ] && exit 0 \|\| exit 1` — and it is a live row in `memory/project/testsuite-count-waivers.txt`. So "its printed assertion count has grown" is unobservable. Add the counter to satisfy it and `compliant()` in `check-testsuite-counts.sh:48-62` starts matching, firing the stale-waiver branch ("a testsuite-count waiver names a suite that now complies") and redding a bar leg (`gate-legs.json:685`) — and §4 lists only `run-gates.test.sh` plus the backlog, so the registry edit that would resolve it is out of scope. AC4 was copied from unit 7, where it is sound: `unattended.test.sh` carries `FLOOR_ASSERTIONS=315` and prints the shape. | Either DROP AC4 — the suite is a declared waiver and this unit is not the one that retires it — replacing it with a criterion naming a real witness for this unit (the two new messages); or scope it fully: add the count, the non-zero `FLOOR_ASSERTIONS` and the comparison, delete the row from `memory/project/testsuite-count-waivers.txt`, and list that registry in §4. |
| 5 | high | §2 S1, §5 risks, §6 AC2 | The control is specified at "a known-good width" that is neither width the clamp yields, so it differs from the subject in width AND clamp path — the same unsound inference the unit exists to remove. `run-gates.sh:81-82` (`case "$JOBS" in *[!0-9]*) JOBS=1 ;; ?????*) JOBS=64 ;; esac` then `[ "$JOBS" -lt 1 ] && JOBS=1`) resolves `0`, `-3` and `nonsense` to width **1** and the two 20-digit values to **64**. §5's mitigation points at "a width the same file already exercises everywhere else" — 4. On the three values §4's MEASURED incident actually fired on, the subject is a SERIAL run and the control would be 4-wide over the same fixture; under the four-concurrent-bar load that produced the incident, the 4-wide control finishing while the serial subject expires is ordinary contention, and the spec's rule converts that straight back into the false accusation. AC2 blesses that outcome. | Run the control at the width the clamp is SUPPOSED to yield for that `w` — `GATE_JOBS=1` for `0`/`-3`/`nonsense`, `GATE_JOBS=64` for the two 20-digit values (both are ≤4 chars and ≥1, so they pass the `case` untouched). Then subject and control differ only by whether the value went through the clamp, which is the thing being blamed, and the discriminator is sound in both directions. State the mapping in §4 instead of "a known-good width", and re-word AC2 to name it. |

### Both units

| id | Sev | Site | Defect | Fold |
|---|---|---|---|---|
| 18 | high | 7 §2 S4 + §6 AC5; 8 §2 S4 + §6 AC5 | The two units' ids are DOUBLE-ALLOCATED. `memory/backlog/TOOL.md` carries `TOOL-aPromptedMandate-12` OPEN about the no-write arm's unanchored `mv\|rm\|cp\|sed -i\|tee` grep, `-8` OPEN about `build-complete` being unsatisfiable, and `-10` OPEN about the canary timeout. Spec 7's H1 is `TOOL-aPromptedMandate-12` carrying row 8's subject, and its AC5 closes row `-8`; spec 8's H1 is `TOOL-aPromptedMandate-13` carrying row 10's subject. So id 7 names two mechanisms and id 8 names two, in one file pair — while rows 11-16 give units 1-6 ids matching their specs exactly, which is the convention this breaks. Every id-keyed reader resolves these to two things: check 21's record→spec binding, the closing review, memory-recall, the drift signals, and the README's already-generated `Ids no record names: TOOL-aPromptedMandate-7 TOOL-aPromptedMandate-13`. Ungated — `corpus_ids` check 13 fires only across build FOLDERS, and both collisions are inside one folder. | Re-key onto the ids already minted for exactly these observations: unit 7 → `TOOL-aPromptedMandate-13`, unit 8 → `TOOL-aPromptedMandate-10`, editing the spec H1s, the filenames, the `roster:units` region, the roster table and each §2 S4 / AC5. The roster then reads 1-6, 8, 10 — `roster_ids` greps ids, not positions — and each unit's backlog row becomes its own row. Failing that, mint fresh ids and leave 7 / 8 / 10 to the backlog. Note this record's own filename inherits the collision and should be renamed with the re-key. |

## Notable refutations

Recorded so nobody re-raises them.

| id | Claim | Why it does not hold |
|---|---|---|
| 3, 12, 24 | Unit 7 calls `unit_rows` non-empty "term 3"; the driver's comment and the suite's arm labels number it **term 4** (term 3 is `missing_units`). | The ordinal slip is REAL but cannot misdirect a builder, and §3 enumerates four terms under which non-emptiness IS term 3. S3 names the predicate in the same clause ("term 3 of `build-complete` (`unit_rows` non-empty)"), and AC3 specifies the CASE — a region with records but no `spec/`-linked row — which `missing_units` (roster ids against tracked spec FILES, never the region) cannot see. The code, the fixture and the arm all come out correct. Prose nit; fix it in passing, do not block on it. |
| 2 | Unit 7's anti-vacuity arm is green on the PRE-fix code too, so it gates nothing. | Green pre-fix is what a regression guard LOOKS like. POST-fix on that fixture `unit_rows` is empty, so term 5 passes vacuously and the non-empty term becomes the sole reason `build-complete` is unmet — deleting it reds the arm. A live guard on exactly the failure S3 names. |
| 11 | `build-complete` collapses its terms into one unlabelled "unmet", so an arm can never observe WHICH term fired. | The observability premise is true (`unattended.sh:1580-1589` sets `DOD_OUT` only on the roster-region branch, then blanks it) and a per-term `DOD_OUT` would be a genuine improvement — but AC2/AC3 name the WHOLE suite as witness, and it opens the `build-complete` block with a green control (`unattended.test.sh:619-623`: `hit "close OK"` + `miss "build-complete"`). A narrowed-to-nothing selector empties `unit_rows`, `--close` blocks, `close OK` never prints, the suite reds. Nothing ungated. |
| 10 | Unit 7 gives the discriminating direction no criterion, and nothing gated fails over the un-fixed code. | S2 already mandates that exact arm — "a build whose specs are all terminal AND WHICH CARRIES RECORDS satisfies the item" — and it rides `unattended.test.sh`, which IS a bar leg. The verification behind the claim described the CURRENT fixture (which renders no records table), i.e. the pre-build state rather than the specified one. |
| 20 | Unit 8's control at 64 is not comparable to a 4-wide subject. | Refuted on mechanism, though the width gap is real and lands as **id 5** for a different reason. The 3f loop replaces both timed fixtures with `instant.sh`, so the manifest is four instant legs and the dispatch loop is bounded by `[ "$di" -lt "$ndisp" ]` with `ndisp=4` — `GATE_JOBS=64` dispatches 4 workers, not 64. The 3g measurement leaned on is a 30-leg READER-race fixture and does not transfer. |
| 14 | Unit 8's S3 ("the starved-host outcome is a FAILURE") specifies no behaviour change, since the current branch already does `fail=1; continue`. | S3 is a design CONSTRAINT on code that does not exist yet, not a claim of changed behaviour, and §4 spends a named paragraph on why fail-not-skip is the live fork. The current branch's exit behaviour makes S3 a floor the fix must not fall through, not a vacuity. |
| 15, 22 | "One extra fixture run" understates the cost — the control sits in a five-iteration loop. | §4 and §5 scope the sentence per-expiry, and the cost never buys a wrong verdict: both expiry outcomes end `fail=1`, so extra budgets only lengthen a run that is already RED. The suggested hoist (cache one control across iterations) is also WORSE — it breaks the contemporaneity that makes the control a discriminator between clamp defect and host load, which is the whole of S1. |
| 25 | Unit 7's AC1 cannot pass until unit 8 is also CLOSED. | `build-complete` is a whole-build predicate by construction, and AC1's witness is the build-CLOSE verb, so the ordering is named by the criterion itself. True of every unit in every build here; not a defect of this spec. |
| 4 | The BINDING protocol's DoD table states the post-fix requirement wrongly in both parity-gated copies. | The sentence at `:244` in both copies states the term's PURPOSE (anti-vacuity), which this unit does not change; it was already a loose paraphrase pre-fix. `check-unattended.sh` joins the DoD table on item NAMES, not on the Asserts prose, and neither copy moves, so parity is unaffected. |
| 7 | Unit 8's AC3 cannot be observed by any arm, so the undecidable branch ships unexecuted. | Refuted AS STATED — the standard would condemn every `\|\| { echo …; fail=1; }` branch on this bar, and the objection was not applied to AC2, which carries the identical property. The underlying concern is real and is confirmed at **id 8** on the sharper ground that AC1 is then the ONLY criterion that runs. |

One sub-claim inside a confirmed finding is recorded as WRONG: id 1 additionally alleged that
`unattended.test.sh:1129` re-derives `want_unit` with the broad selector and would RED a correctly
routed `verb_status`. The tRun fixture's generated region (`unattended.test.sh:68-74`) carries
exactly one row — a single `ARCH-tRun-1` unit whose link target is under the fixture's own `spec/`
dir — which both selectors match, so the
control is selector-agnostic. Finding 1 stands on its primary claim alone; a builder should not
expect that arm to red.

## Unverified

None. Every raised finding returned a verdict.


## Renumbering note

The two units were minted as `-7` and `-8`, ids the backlog already held for two different
findings the same run had filed. Finding 18 of this audit caught the collision; the specs and
this record were renumbered to `-12` and `-13`. References above read in the new numbering.
