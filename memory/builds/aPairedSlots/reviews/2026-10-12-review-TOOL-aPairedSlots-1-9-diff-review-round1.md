**Serves:** diff-review TOOL-aPairedSlots-1 TOOL-aPairedSlots-2 TOOL-aPairedSlots-3 TOOL-aPairedSlots-4 TOOL-aPairedSlots-5 TOOL-aPairedSlots-6 TOOL-aPairedSlots-7 TOOL-aPairedSlots-8 TOOL-aPairedSlots-9

# aPairedSlots: Tier-2 closing diff review, round 1

*Node `a`, 2026-10-12. This was an adversarial pass over the build's whole cumulative diff: five
primed finder lenses, then a skeptic stage prompted to REFUTE each finding, then one synthesis. The
build turns the gate runner's host-wide turnstile into a counting semaphore of `slots` holders,
gives doc-only bars an unbounded key of their own, holds a worktree to one slot, makes the common
dir's run log, shared full green and drift history safe for a second writer, and ships the
capability dark at `slots=1` after the two-bar A/B. The range starts at d19938f3, the merge-base
where aFrugalTurnstile landed. The run's pinned BASE 6dc23b58 predates the merge of that landing,
so a range from it would re-review aFrugalTurnstile. The author re-read the load-bearing lines at
b6cd9fa6 rather than transcribing them from a lens: `tools/run-gates/run-gates.sh:700-716`,
`:985-996`, `:1205-1262`, `:1362-1393`, `:1462-1502`, `:1675-1684` and the verdict writes at
`:4126`, `:4154` and `:4213`; `tools/drift-audit/drift_report.py:3790-3832` and the two-writers arm
in `tools/drift-audit/selftest.py`; the floor and arm 32 in `tools/run-gates/run-gates.turnstile.test.sh`;
and the two build instruments and the rule check under `memory/builds/aPairedSlots/build/`.*

**Reviewed range:** d19938f350d5fe9f5d85c288dcf585cc313fd26f...b6cd9fa6bd8bc416729b6369740cb3e938e205ef. **ROUND:** 1.

## Verdict: CLEAN WITH FIXES

No blocker survived. Four HIGH findings must be fixed before the close lands. None of them ships a
wrong gate verdict. Three are build instruments that grade nothing: the A/B instrument and the
two-bar check both read the run record's verdict file by line instead of by key, and the two-bar
check's overlap guard cannot fail. The registered VERIFYING two-writer check would therefore
mislead the next step whichever way it ran. The fourth is the drift history: two first writers
leave it permanently unreadable, and the new arm certifies that layout. The fifteen MEDIUM findings
are holes in the one-bar-per-worktree invariant, a mis-ordered reap guard, unraised assertion
floors, arms that cannot fail, a missing magnitude bound and three new lexicon offenders. One of
them (M3) needs an owner ask before it can be fixed, because the obvious fix contradicts the ruling
that a doc-only bar never waits. The eleven LOW findings are docs, records and dead state. The
shipped behaviour at the default `slots=1` is correct except for M3, which is live at one slot.

## Review shape

Intensity full: raw 38, confirmed 30, refuted 8, unverified 0 (0 uncertain), precision 0.79.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| security | yes | 6 | 4 | 2 | 0 | 0 | 0.67 |
| correctness | yes | 5 | 5 | 0 | 0 | 0 | 1.00 |
| seams | yes | 9 | 8 | 1 | 0 | 0 | 0.89 |
| verification | yes | 8 | 5 | 3 | 0 | 0 | 0.63 |
| intent | yes | 10 | 8 | 2 | 0 | 0 | 0.80 |

The adjudicated tally, counted two ways:

- **By item:** 0 BLOCKER, 4 HIGH, 9 MEDIUM, 8 LOW, which is 21 items.
- **By raw confirmed finding:** 0 blocker, 4 high, 15 medium, 11 low, which is 30 findings.

Items merge findings of one binding grade only. Where the same defect drew different binding
grades from different lenses, each grade keeps its own item and the items cross-reference:

- The drift-history header split is H1 (id 7, high) and M6 (ids 15, 32, medium).
- The A/B instrument's shifted verdict column is H2 (id 12, high) and L8 (id 38, low).
- The two-bar check's overlap guard is H4 (id 30, high) and M7 (id 14, medium).
- The unbounded slot count is M9 (id 31, medium) and L1 (ids 4, 11, low).
- The unraised canary floor is M4 (id 9, medium) and L3 (id 25, low).

## Run integrity

Every count that must be zero is zero, so the run is complete:

- Lenses: 5 of 5 returned, 0 died.
- Skeptic batches: 5 of 5 returned, 0 died.
- Verdicts: 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0
  duplicates.
- Fixes on confirmed findings: 21 judged sound, 9 judged UNSOUND (ids 2, 7, 8, 12, 14, 15, 29, 32
  and 38; each skeptic's corrected fix is written below), 0 with no fix proposed, 0 not judged.
- Severity on confirmed findings: 0 ungraded by the skeptic, 1 re-graded by the skeptic (id 29, from
  high to medium).
- Unverified findings: none. 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: supplied for verification and correctness.
- Intent: 11 spec documents were supplied as `specs`, beside the range's commit messages.
- Checklist: 50 items, each assigned to exactly one of 5 lenses (security 10, correctness 10,
  seams 10, verification 10, intent 10).
- By design: the caller's byDesign list.

## HIGH

### H1. Two first writers leave the drift history unreadable for good, and its arm certifies the layout (id 7)

- **Where:** `tools/drift-audit/drift_report.py:3802-3810` (the writer), `:3827-3829` (the reader
  keys on `lines[0]`), `tools/drift-audit/selftest.py:3672` (the arm).
- **Grade:** high, the binding grade. Finder and skeptic agree, and so does this report.
- **Defect:** the header is written by a second open (`ab`) after the exclusive create (`xb`) has
  closed. A writer that appends between the two lands its rows above the header.
  `read_history_groups` treats line 0 as the header and refuses the whole file. The split also adds
  an empty-file state: a creator killed, or whose `ab` open fails, between the two opens leaves a
  file that no later writer ever heads. `test_drift_history_two_writers` stages exactly the
  interleaving and passes, because it asserts `lines.count(header) == 1` and never the header's
  position. Reproduced on b6cd9fa6 with the arm's own wrapper: the file holds
  `['second\trow', <header>, 'first\trow']` and the reader returns
  `([], 'drift-history.tsv opens with a header this engine does not write')`.
- **Impact:** every later `--delta` prints `skipped` and `derive_dead_streaks` returns None on that
  node, so dead-probe streaks stop reporting. Nothing repairs it. The base's `tell() == 0` race
  wrote a duplicate header, which the reader survived, so this diff turned a benign outcome into a
  permanent one.
- **On the spec:** spec 7 §4 records the rows-above-header case as an accepted residual and says the
  reader skips such a history. A refuted sibling (id 21) leaned on that. The skip never ends,
  because every later write appends below the misplaced header, and the arm cannot tell the
  accepted residual from a correct file. The residual's permanence is the defect.
- **Fix (REJECTED by the skeptic; this is the skeptic's corrected fix):**
  1. Writer: write header plus rows to a sibling temp file and publish it with
     `os.link(tmp, path)`, then unlink the temp. On `FileExistsError`, append the rows only. On any
     other `OSError`, fall back to the append path.
  2. Reader: take the first line whose fields are a superset of `HISTORY_COLUMNS` as the header,
     parse every other non-header line, above or below it, as a row, and assume `HISTORY_COLUMNS`
     order when no header line exists.
  3. Arm: run the second writer from a wrapper around `dr.os.link`, not `open`. Assert
     `lines[0] == header`, and that `read_history_groups(path)` returns both rows with an empty
     reason. M6 adds that the rows must be full nine-column rows, or the reader yields zero groups
     even on correct code.
- **Left-shift gate:** class `line-claim-matched-over-the-whole-output`. Add a bug-class checklist
  entry: an arm over a record writer reads the result back through the record's one reader and
  asserts on the reader's answer, never on a count of lines. A cheap gate candidate is a scan of the
  kit self-tests for `.count(` applied to a header string, which is the shape that hid this.

### H2. The A/B instrument reads the verdict file's first line, so every finished bar's row shifts one column (id 12)

- **Where:** `memory/builds/aPairedSlots/build/2026-10-11-build-TOOL-aPairedSlots-1-ab-instrument.sh:147`
  (the read), `:176` (the MAKESPAN proofs, `print $13`), and
  `memory/builds/aPairedSlots/build/2026-10-11-build-TOOL-aPairedSlots-9-rule-check.py:14`.
- **Grade:** high, the binding grade. This report agrees: the committed decision stands, but the
  instrument the results record prescribes for the re-measure still carries the defect.
- **Defect:** every verdict write in the runner (`run-gates.sh:4126`, `:4154`, `:4213`) starts with
  `ended<TAB><time>`. `head -1` puts that TAB-bearing value in column 9, so every later field moves
  one place right. The MAKESPAN row's `proofs` then collects the bar's expected-leg count, and
  rule-check accepts any token except `NO`. The committed A1 MAKESPAN row reads `65`, and
  rule-check counted it proven.
- **Impact:** A1 really was proven (its shifted proof column reads `yes`), and B1 and C1 were
  unproven anyway, so this run's decision is correct. On the re-measure, any finished bar's real
  proof column is ignored. An arm with missing legs, or a fast REFUSED bar, reads as proven, and
  rule-check could set `slots=2` from a refusal timed against a run. That is the exact A/B failure
  the instrument's header says it prevents.
- **Fix (REJECTED by the skeptic; this is the skeptic's corrected fix):**
  1. In `measure_bar`, read the verdict by key:
     `verdict=$(awk -F'\t' '$1=="verdict"{print $2}' "${rec}verdict" 2>/dev/null); verdict=${verdict:--}`.
  2. In rule-check.py, derive each arm-run's proof from its c1 and c2 bar rows, not the MAKESPAN
     row. The proof is the field after `expected`: index 13 when field 8 reads `ended` (the A1
     shift the results record explains), 12 otherwise. Require both bars' proof to equal `yes`.
     Applied to the committed rows this still reads A1 proven and prints AGREE.
- **Left-shift gate:** the run record's files are key-TAB-value, and reading one by line number is
  the class. Add a grep gate over tracked `*.sh` that refuses `head -1` applied to a path ending in
  `verdict` or `header`, naming the by-key form. Separately, every TSV-emitting build instrument
  asserts each row's field count equals its header's before it writes the row.

### H3. The two-bar check's row predicate compares a timestamp with a leg count (id 13)

- **Where:** `memory/builds/aPairedSlots/build/2026-10-11-build-TOOL-aPairedSlots-5-two-bar-check.sh:64`
  (the read) and `:89` (the predicate).
- **Grade:** high, the binding grade. This report agrees: the check is the build's registered
  VERIFYING instrument and has not run yet, so it will mislead the next step.
- **Defect:** `ver=$(head -1 "$rec/verdict")` stores `ended<TAB><time>` in column 9, so every
  `check.tsv` row has 11 fields where the header declares 10. The predicate `$10 < ($6 + $7)` then
  compares the end timestamp with the leg count as strings and never reads the ledger-rows column.
- **Impact:** at gov's ~65 legs, `"2026-..." < "65"` is true, so every row reds as `row lost or
  torn` and points the VERIFYING run at TOOL-aPairedSlots-7's writers. At 100 to 199 legs it never
  flags anything, whatever the ledger kept. Either way the ledger-rows half grades nothing.
- **Fix (judged SOUND by the skeptic):** `ver=$(head -1 "$rec/verdict" 2>/dev/null | cut -f1)`, so
  `check.tsv` keeps its ten declared columns, and assert `NF == 10` on each row before the
  predicate reads `$10`.
- **Author's note on the fix:** `cut -f1` of that line is the literal `ended`. That restores the ten
  columns and keeps `$9 == "-"` meaningful as a presence test, but the `record_verdict` column then
  never holds a verdict. Reading by key, as H2's corrected fix does
  (`awk -F'\t' '$1=="verdict"{print $2}'`), gives both. Prefer it, and keep the `NF == 10` assertion.
- **Left-shift gate:** the same two gates as H2. The `head -1` grep would have refused line 64, and
  the field-count assertion would have caught the shift on the first row.

### H4. The two-bar check's overlap guard cannot fail (id 30)

- **Where:** `memory/builds/aPairedSlots/build/2026-10-11-build-TOOL-aPairedSlots-5-two-bar-check.sh:44-51`
  (`run_bar` stamps the window) and `:91` (the guard).
- **Grade:** high, the binding grade. This report agrees: the path is narrow, since slots normally
  take, but the consequence is a check certifying a concurrency it did not observe.
- **Defect:** `run_bar` stamps `date +%s` before and after the whole runner, so each window includes
  the turnstile queue wait. `cmd_run` starts both concurrent bars together, so `s1 < e2 && s2 < e1`
  holds even if the turnstile serialized them, for example when the slots override did not take.
  Nothing else in `cmd_run` catches serialization: the verdict comparison and the row checks pass
  either way.
- **Impact:** a serialized pair prints `TWO-BAR CHECK PASS` for the build's two-writer claim (spec 5
  S3, spec 7) without two writers ever running together. The comment at line 90 says the guard
  exists to catch exactly this.
- **Fix (judged SOUND by the skeptic):** judge the overlap from each bar's own run record: its
  `acquired` header key, or its `gate queue: acquired` line, against its end. Or assert that each
  concurrent bar's header records `queued_from held` and `queued 0`, with distinct `slot` values 1
  and 2. The skeptic adds that `queued 0` can red falsely, because the second bar may wait one 2 s
  tick at the FIFO head, and that distinct slots 1 and 2 alone prove the overlap, because
  `resolve_free_slot` takes slot 2 only while slot 1 exists. Apply it as M7's corrected fix states
  it: slot keys {1, 2}, each `acquired` before the other bar's end, and no `queued 0` test.
- **Left-shift gate:** a gate never seen red is not a gate. Give the check a staged-red mode that
  runs the same pair at `GATE_TURNSTILE_SLOTS=1` and requires `TWO-BAR CHECK FAIL`, and record that
  observation beside the green. Add a checklist entry: an overlap guard reads the admitted interval
  from the system under test, never the invocation interval around it.

## MEDIUM

### M1. The per-slot reap judges a holder before reading the nonce that guards its removal, and no arm can fail the guard (ids 1, 24)

- **Where:** `tools/run-gates/run-gates.sh:1371-1373` (pid, heartbeat, then nonce), `:1380` and
  `:1388` (the re-checks), and `scan_dead_docs_beacons` at `:1228` with its re-checks at `:1231`
  and `:1237`, which use the same order.
- **Grade:** medium for both, the binding grade. The base had no guard at all, so this is never
  worse than d19938f3, but the new guard is mis-ordered against its own spec.
- **Defect (id 1):** spec 2 S3 says the guard compares the nonce read when the slot was judged. The
  code reads the nonce after the pid and heartbeat, so the nonce it guards with may belong to a
  successor. The header comment at `:1366-1368` claims only the re-read-to-`rm` instant stays open,
  and that overstates it.
- **Defect (id 24):** arm 30 plants slot 2 with the constant nonce `planted30`, and arm 42 plants
  docs beacon `p42` the same way. Both re-checks always hold, so deleting either leaves every arm
  green. Spec 2 S3 says AC3 observes the guard, but AC3's red-when is only "walks slot 1 only".
- **Impact:** waiter B reads dead holder D's pid. Waiter A reaps D, and the head claims the slot and
  writes its nonce before B's nonce read. B re-reads a nonce equal to the successor's, the re-check
  passes, and B `rm -rf`s a live slot. The next claimant `mkdir`s it again, so two bars share one
  slot. If that claimant is in the same worktree, `check_worktree_unheld` no longer sees the first
  bar, and two bars write one git dir.
- **Fix (id 1, judged SOUND by the skeptic):** read the nonce first, then pid, heartbeat and ttl, and
  keep the re-check before the `rm`, so the judged facts belong to the nonce that guards their
  removal. Use the same order in `scan_dead_docs_beacons`. Correct the comment's residual-window
  sentence. Add an arm, staged red on a runner copy without the re-check, that swaps a slot's nonce
  between the judgement and the removal.
- **Fix (id 24, judged SOUND by the skeptic):** add a functional arm that sources `ts_try_reap` the
  way the canary's TOOL-aReapedSpinner-7 arm sources the reaping functions. Stub `ts_alive` to
  report dead, and shim `cat` so the slot's nonce file changes after the first read. Assert the slot
  directory survives and no reap line prints, and stage it red with the re-check deleted. Do the
  same for `scan_dead_docs_beacons`. One arm discharges both findings.
- **Left-shift gate:** class `witness-graded-against-a-fact-written-after-it`. Add a bug-class
  checklist entry: a token-guarded removal reads its token before every fact it judges, and its arm
  changes the token between judgement and removal.

### M2. A bar at a lower slot count skips the one-slot-per-worktree rule (id 2)

- **Where:** `tools/run-gates/run-gates.sh:1256` (`[ "${TS_SLOTS:-1}" -gt 1 ] || return 0`), and the
  loop at `:1257` over `TS_SLOT_DIRS`, which `:1213-1214` builds from slot 1 to this runner's own
  count only.
- **Grade:** medium, the binding grade. It needs a per-bar count difference inside one worktree,
  which is narrow, and it ships dark.
- **Defect:** `GATE_TURNSTILE_SLOTS` is a per-bar override (`:988-995`), and mixed counts are a
  documented host state (spec 2 Rollout, the README). Spec 5's premise that the predicate is
  unreachable at one slot does not hold then.
- **Impact:** a count-2 bar in worktree W holds slot 2. Slot 1 frees, and a count-1 bar in W reaches
  the head, skips the predicate and claims slot 1. Two bars then share W's git dir, which spec 5 S1
  and its non-goals forbid. A count-2 bar likewise cannot see slot 3 held by a count-3 bar in its
  worktree.
- **Fix (REJECTED by the skeptic; this is the skeptic's corrected fix):** run `check_worktree_unheld`
  at every count over every slot beacon present (`for d in "$TS_DIR_C" "$TS_DIR_C".*`). In the
  one-slot queue-line branch, test `check_worktree_unheld` before the "no bar holds this host, but a
  ticket sorts ahead" else, and name the same-worktree holder there. Extend arm 43 with a count-1
  bar from the worktree that holds slot 2, asserting that it waits and that its line names that
  holder. That line gives `TS_SAME` the reader L5 finds missing.
- **Left-shift gate:** spec 2 S5 already learned this for nesting: a predicate about other bars
  reads every beacon present, never 1 to this runner's own count. Make that a bug-class checklist
  entry, and add a canary grep that refuses a loop over `TS_SLOT_DIRS` inside a function that reads
  another bar's `repo` or `nonce`.

### M3. A doc-only bar runs beside another bar in its own worktree, at the shipped one slot (ids 8, 29)

- **Where:** `tools/run-gates/run-gates.sh:1479-1502` (the docs branch, which never calls the
  predicate) and `:1250-1262` (`check_worktree_unheld`, which reads slot beacons only).
- **Grade:** medium for both, the binding grade. The finder graded id 29 high, and the skeptic
  re-graded it medium. This report agrees with medium: verdicts are read per run id, so no verdict
  changes, and what is lost is evidence and cache on a narrow path.
- **Defect:** the docs key admits a doc-only bar with no same-worktree test, at every slot count.
  Before this build, at `slots=1`, that bar queued behind its worktree's holder. TOOL-aPairedSlots-5's
  invariant that every path under a worktree's git dir stays one bar's is therefore not built for
  doc-only bars, and the shared-path audit and spec 5 §4 both claim it is.
- **Impact:** a doc-only bar in worktree X (for example the pre-push hook's on a doc-only push) and
  any other bar in X run together and share X's git dir:
  - `gate-logs/<leg>.log` is keyed by leg name alone (`LOGDIR=$GD/gate-logs`), so a leg both bars
    run overwrites the other's log, and a red bar's failure pointer shows the other run's output.
  - `gate-run/current` is staged through the fixed `current.tmp` (`:2205`), and
    `gate-last-summary.txt` and `gate-last-failure.txt` name the last writer. `push-main.sh:252`
    sends the user to that summary after a red push.
  - The ledger's read-merge-move at exit (`:4009-4045`) loses one bar's rows when the exits overlap.
- **On the by-design ruling:** a refuted sibling (id 18) held that the owner's ruling covers this.
  The skeptics on ids 8 and 29 held that the ruling decided the docs key's count and that it never
  queues, not that it shares a git dir. This report follows the confirmed verdicts.
- **Fix (both REJECTED by the skeptics; this is their corrected fix, and the two agree):**
  1. Ask the owner first. Waiting contradicts the ruling "a doc-only bar never waits behind a
     non-doc bar" (build README), and spec 4 S6.
  2. If waiting is allowed: make `check_worktree_unheld` also scan `gate-docs-beacon/*` for entries
     whose `repo` equals `$ROOT`, at every count including 1. Call it in the non-doc claim, and give
     the docs branch a bounded wait on it, so both directions are covered.
  3. If not: record the same-worktree doc-only case as a COLLIDES row in the shared-path audit with
     a unit that owns the fix, and state the exception in spec 5 and the run-gates README. When a
     same-worktree beacon is live, point the doc-only bar's `LOGDIR`, `current` pointer and summary
     file at its own run record rather than the shared names.
- **Left-shift gate:** an invariant one admission path enforces must be re-checked against every
  other admission path: the slot claim, the docs key, nesting and the unqueued fail-open. Add that
  to the bug-class checklist, and give the shared-path audit one column per admission path, so a
  new path shows an empty cell instead of an implicit "S1 covers it".

### M4. Two suites' assertion floors were not raised for this build's arms (ids 9, 22)

- **Where:** `tools/run-gates/run-gates.turnstile.test.sh:154` (`FLOOR_ASSERTIONS=101`) and
  `tools/run-gates/run-gates.test.sh:125` (`FLOOR_ASSERTIONS=326`).
- **Grade:** medium for both, the binding grade. Id 25 (L3) reports the canary half again at low.
- **Defect:** arms 29 to 43 add 33 counted assertions to the turnstile suite (5, 3, 2, 2, 2, 2, 1,
  2, 2, 3, 2, 1, 2, 1 and 3, each counted on every branch), and section 11s adds nine unconditional
  `check_mp_value` assertions to the canary. Neither floor moved. Each suite's comment says the
  floor moves with new arms so a lost arm reds instead of being stranded. The runlog suite (211 to
  217) and the drift selftest (478 to 480) were raised in this same build.
- **Impact:** deleting or short-circuiting every slot, shared-width, docs-key, per-worktree and
  slots-knob arm leaves both suites green.
- **Fix (judged SOUND by the skeptics):** raise the turnstile floor to 134 (101 + 33) and the canary
  floor to 335 (326 + 9), each with a dated comment line naming TOOL-aPairedSlots-2 to -5 and -1,
  counted off the blocks, as the other floors in this build carry.
- **Left-shift gate:** make a slack floor red. Each suite already counts `n`. Where every arm counts
  on every branch, as both of these do, fail the suite when `n` exceeds `FLOOR_ASSERTIONS`, the way
  hygiene treats a pin above its measured count as slack. A forgotten raise then reds on the pass
  that added the arms.

### M5. The turnstile suite inherits the slot count, so arm 32 never exercises S5's case and enabling slots reds unrelated arms (ids 10, 17, 23)

- **Where:** `tools/run-gates/run-gates.turnstile.test.sh:135` (only `GATE_TURNSTILE_DIR` is
  exported), `:181` (`mk_repo` copies the real `gate-profiles.txt`), `:1223` (`nest32.sh` strips
  only `GATE_LEGS`) and `:1226` (the outer bar at `GATE_TURNSTILE_SLOTS=2`). The runner reads the
  override at `run-gates.sh:988` and never unsets it for legs.
- **Grade:** medium for all three, the binding grade.
- **Defect (ids 10, 23):** arm 32's inner runner inherits `GATE_TURNSTILE_SLOTS=2`, so its own
  `TS_SLOT_DIRS` already contains slot 2. A nesting test that iterated `TS_SLOT_DIRS`, the rev-1
  design spec 2 replaced, would still nest, and the arm stays green. Spec 2 S5 names the case the
  `"$TS_DIR_C".*` glob exists for, "a fixture bar whose own table declares fewer slots than the
  holder", and the arm never builds it.
- **Defect (id 17):** arms 1 to 28 take their count from the outer environment and the copied real
  table, and arms 33, 38 and 41f pass an empty override that falls through to the table. Neither
  source is pinned to 1.
- **Impact:** a regression of the nest scan to `TS_SLOT_DIRS` ships green, and a slot-1 leg runner
  started by a slot-2 holder then queues behind its own parent until the fail-open bound. Enabling
  slots through either documented path (`slots=2` on the `capable` row, or an exported
  `GATE_TURNSTILE_SLOTS=2`) reds arms 16, 23, 25 and 33 with failures that read as turnstile
  regressions. That is a misleading red, not a false green.
- **Fix (judged SOUND by the skeptics):** `export GATE_TURNSTILE_SLOTS=1` beside
  `export GATE_TURNSTILE_DIR`. Have arms 33, 38 and 41f select a fixture table with no `slots` key
  through `GATE_PROFILES` instead of an empty override. Start arm 32's inner runner with
  `GATE_TURNSTILE_SLOTS=1` (or `env -u GATE_LEGS -u GATE_TURNSTILE_SLOTS`), keep the `nested under`
  assertion, and stage it red against a runner copy whose nested test iterates `TS_SLOT_DIRS`.
  Prefer the explicit `=1`: the `-u` form falls back to the copied real table, and stops
  discriminating the day that table gains a `slots` key.
- **Left-shift gate:** a new runner knob owes a pin in every suite that runs the runner. Derive the
  set from the runner's `GATE_[A-Z_]*` reads and red a suite prologue that neither sets nor unsets
  one. The canary's `PINNED_KNOBS` already pins table keys this way; this extends the same parity to
  environment knobs.

### M6. The drift history's header split, graded at medium, and the empty file it can no longer heal (ids 15, 32)

- **Where:** `tools/drift-audit/drift_report.py:3802-3810` and `tools/drift-audit/selftest.py:3651-3672`.
- **Grade:** medium for both, the binding grade. Id 15 is H1's defect seen from the seams lens. This
  report would grade it high with H1, but the action is the same, so the grade changes nothing.
- **Defect (id 15):** H1's rows-above-header layout, which the arm certifies.
- **Defect (id 32):** the base wrote the header whenever `fh.tell() == 0`, so an empty file healed on
  the next write. Now the header goes only into a file this call created, so an existing empty file
  gains headerless rows forever. Triggers: an `OSError` such as ENOSPC on the append after a
  successful create, a kill between the two opens, or a touched or truncated file. All are narrow.
  Spec 7 S4 narrowed "absent or empty" to "absent" without naming this regression.
- **Impact:** `--delta` and the kickoff manifest's drift cell refuse the history permanently, with a
  visible skip or UNKNOWN and no repair.
- **Fix (both REJECTED by the skeptics; this is their corrected fix, applied once with H1's):**
  1. Create the history atomically with its header already in it: write the header to
     `path.with_name(f"{path.name}.tmp.{os.getpid()}")`, `os.link(tmp, path)`, treat
     `FileExistsError` as "another writer created it, no header", and unlink the temp in a
     `finally`. Then append the rows in the one binary write, as now.
  2. With creation atomic, heal outside truncation with `created or fh.tell() == 0`; no creation
     race is left for it to reopen.
  3. In the arm, replace the two-field rows with full nine-column rows carrying distinct `#utc` and
     `sha`, because `read_history_groups` skips any row shorter than the header and the current
     `'first\trow'` fixtures yield zero groups even on correct code. Assert `lines[0] == header` and
     that `read_history_groups` returns two groups.
- **Left-shift gate:** as H1.

### M7. The two-bar check's overlap guard, graded at medium (id 14)

- **Where:** `memory/builds/aPairedSlots/build/2026-10-11-build-TOOL-aPairedSlots-5-two-bar-check.sh:91`.
- **Grade:** medium, the binding grade. It is H4's defect seen from the seams lens. This report would
  grade it high with H4, and the action is the same.
- **Defect and impact:** as H4. If the second slot is not granted, the bars run serially, the windows
  still overlap, and the check prints `TWO-BAR CHECK PASS`.
- **Fix (REJECTED by the skeptic; this is the skeptic's corrected fix):** assert concurrency from the
  two concurrent bars' run-record headers. Their `slot` keys must be {1, 2}: a serialized second bar
  re-claims the lowest free slot, 1, and a bar at one slot writes no `slot` key. Also convert each
  header's `acquired` (UTC ISO) to epoch and require it to precede the other bar's end. Do not
  require `queued 0`: the head-only claim (`run-gates.sh:1565`) makes the bar whose ticket sorts
  second announce position 2 and sleep one `TS_TICK` (default 2 s) before it claims, so a genuinely
  concurrent second bar records `queued` of 1 or more.
- **Left-shift gate:** as H4.

### M8. Three new names lead with verbs outside the declared vocabulary (id 16)

- **Where:** `wait_registered` (`tools/run-gates/run-gates.turnstile.test.sh:1152`), `mk_docs_repo`
  (`:1321`) and the nested `open_with_a_second_writer` (`tools/drift-audit/selftest.py:3651`).
- **Grade:** medium, the binding grade.
- **Defect:** measured on clean checkouts with `python tools/lexicon/lexicon.py --offenders`: d19938f3
  lists 1068 verb offenders and b6cd9fa6 lists 1071, against a `VERB_OFFENDER_PIN` of 1063. The
  sorted difference is exactly these three names.
- **Impact:** the lexicon leg is already red at the base. This build adds three own offenders on top,
  which line-keyed red attribution reads as MIXED rather than inherited, so an inherited-red landing
  cannot be attributed clean.
- **Fix (judged SOUND by the skeptic):** rename to declared verbs, for example `check_registered` (or
  `measure_registered`), `build_docs_repo` and `run_second_writer_on_open`, and confirm the leg
  reads 1068 again. Do not raise the pin.
- **Left-shift gate:** branch bars skip the lexicon leg as unchanged against main, so it only fails
  at the lander. Key the leg's guard on "the diff adds a definition" instead, and have the pass brief
  run `/lexicon` before naming, as the charter's tools section asks.

### M9. The slot count has no upper bound (id 31)

- **Where:** `tools/run-gates/run-gates.sh:705` (the 15-digit cap), `:713` (the refusal below 1),
  `:988-993` (the override parse) and `:1212-1216` (the array build). `GATE_JOBS` is clamped to 64 at
  `:797`.
- **Grade:** medium, the binding grade. L1 reports the same defect at low twice.
- **Defect:** the row and `GATE_TURNSTILE_SLOTS` both accept any count of up to 15 digits. The
  runner then builds `TS_SLOT_DIRS` with one array append per slot before the queue, the wall and
  any fail-open bound, and `measure_held_slots` and `resolve_free_slot` walk the whole array on every
  tick. Spec 1 S2 says the knob follows `GATE_JOBS`'s rule, but `GATE_JOBS` clamps and this does not.
- **Impact:** `GATE_TURNSTILE_SLOTS=100000000`, or a mistyped row value, makes every bar spend minutes
  and gigabytes before dispatch, and nested runners inherit the value. A 15-digit value never
  finishes. It is a silent hang at the push boundary, reachable only through misconfiguration.
- **Fix (judged SOUND by the skeptic):** clamp the resolved count as `GATE_JOBS` is clamped, for
  example to 64 with a NOTE, or bound the accepted length to a few digits in both the row validator
  and the override parse. L1's sound fixes choose a cap of 64, refused in the row beside the
  `slots` 0 refusal (the `mempause` precedent) and ignored with the existing NOTE in the override.
  Pick that shape, so the row and the override follow the knob table's refuse-a-malformed-value rule.
- **Left-shift gate:** a knob that sizes an allocation declares a maximum beside its minimum. Add a
  canary arm per such knob with a value one above the cap, and a checklist entry for new knobs.

## LOW

### L1. The slot count has no upper bound, graded at low (ids 4, 11)

- **Where:** `tools/run-gates/run-gates.sh:1214`.
- **Grade:** low for both, the binding grade. M9 carries the same defect at medium, and this report
  would grade these medium with it. The fix is one change.
- **Fix (both judged SOUND by the skeptics):** refuse a row value above a small declared cap, for
  example 64, beside the existing `slots` 0 refusal. Treat an override above the cap like a
  malformed one: ignore it with the existing NOTE. Bound the count where it is validated.
- **Left-shift gate:** as M9.

### L2. A docs beacon interrupted before its traps are armed leaks forever (id 5)

- **Where:** `tools/run-gates/run-gates.sh:1484` (the `mkdir`), `:1486` (the heartbeat write, one
  `$(ts_now)` fork), `:1494-1497` (the traps), and `:1235` (`scan_dead_docs_beacons` `continue`s on
  an empty heartbeat).
- **Grade:** low, the binding grade.
- **Defect and impact:** Ctrl-C in that one-fork window leaves a beacon with neither pid nor
  heartbeat, and the sweep skips it on every run. `gate-docs-beacon/` grows, and every nested check
  spends one `cat` on it. It delays no bar.
- **Fix (judged SOUND by the skeptic):** in `scan_dead_docs_beacons`, treat a beacon with no numeric
  heartbeat and no pid as stalled once its directory's mtime is older than the ttl, under the same
  nonce guard. Or write pid and heartbeat before the beacon becomes visible, by staging it under a
  temporary name and renaming it into place. The rename removes the state rather than sweeping it,
  and costs no `stat` fork per tick.
- **Left-shift gate:** add a checklist entry: a beacon is published complete or swept on age. Add an
  arm that plants a pid-less, heartbeat-less docs beacon with an old mtime and asserts it is gone.

### L3. The canary's assertion floor was not raised (id 25)

- **Where:** `tools/run-gates/run-gates.test.sh:125` (`FLOOR_ASSERTIONS=326`), section 11s at
  `:3155-3181`.
- **Grade:** low, the binding grade. The same defect is half of id 9, graded medium in M4, and this
  report would grade it medium there. The fix is one change.
- **Fix (judged SOUND by the skeptic):** raise `FLOOR_ASSERTIONS` to 335, with a
  "326 -> 335, TOOL-aPairedSlots-1: the nine checks of section 11s, counted off the arm" line.
- **Left-shift gate:** as M4.

### L4. The docs sweep's stalled-holder branch has no arm (id 26)

- **Where:** `tools/run-gates/run-gates.sh:1236-1241`. Arm 42 (`run-gates.turnstile.test.sh:1388-1394`)
  plants only a dead pid with a fresh heartbeat.
- **Grade:** low, the binding grade. The branch reads correctly today.
- **Defect and impact:** spec 4 S5 scopes both sweeps, and its Messages table names both lines, but
  no arm greps `docs beacon of a stalled holder`. A wrong age sign or the waiter's ttl in place of
  the holder's would leave wedged doc-only beacons standing, and they keep nesting any process that
  carries their nonce.
- **Fix (judged SOUND by the skeptic):** plant a docs beacon whose pid is a live sleeper, with its
  heartbeat set to now minus 100 and its ttl to 5. Assert that the next doc-only bar prints
  `sweeping the docs beacon of a stalled holder` and that the directory is gone.
- **Left-shift gate:** derive coverage from the spec: every line a spec's Messages table names is
  grepped by some arm in the kit's suites. A token join from Messages tables to suite greps finds the
  unarmed lines before the close does.

### L5. `TS_SAME` is written and never read, and spec 5's inventory does not describe the code (ids 19, 35)

- **Where:** `tools/run-gates/run-gates.sh:1252-1260` (the global, its comment and two assignments)
  and `:1681` (the `one by this worktree` line, which prints every holder in `$ts_names`).
- **Grade:** low for both, the binding grade.
- **Defect:** the comment promises a reader for `TS_SAME` that does not exist. Spec 5 §4 says no
  function or variable is minted beyond a local in the claim, yet the unit minted the global
  function `check_worktree_unheld` and the global `TS_SAME`. Each `$ts_names` entry carries its
  `repo`, so spec 5's "names the same-worktree holder" is technically met.
- **Fix (judged SOUND by the skeptics):** name the `TS_SAME` slot's run, repo and pid in that line
  (one `cat` each of its `run`, `repo` and `pid` files), or delete `TS_SAME` and its comment. Amend
  spec 5's inventory to name `check_worktree_unheld`. Prefer the reader: M2's corrected fix already
  wants the one-slot queue line to name the same-worktree holder, which is this variable's job.
- **Left-shift gate:** a write-only global in a shell kit is the dead-code class `/drift-audit`'s
  hunt tier looks for. Run that tier over `tools/run-gates/` before the close.

### L6. The README never states the one-slot-per-worktree rule (ids 20, 34)

- **Where:** `tools/run-gates/README.md:192-262` (the turnstile section), cited at `:202` and `:212`.
- **Grade:** low for both, the binding grade. Docs only.
- **Defect:** spec 5 §5 says the head-of-line risk is "Stated in the README" and names the README's
  turnstile section as the user doc. That section states neither the rule, nor the head-of-line wait,
  nor the `held, one by this worktree` queue line. No commit in the range adds it.
- **Impact:** an operator who sees a second bar in one worktree queue while a slot is free has no
  documented reason for it. TOOL-aPairedSlots-5 is CLOSED, so the route gate refuses the text to a
  later pass of it.
- **Fix (judged SOUND by the skeptics):** add one paragraph after the slots paragraph, carried by a
  routed unit: above one slot a worktree holds at most one slot, a head whose worktree holds one
  waits and keeps later tickets behind it, and the queue line reads
  `<k> of <n> bar slots on this host are held, one by this worktree — …`.
- **Left-shift gate:** a spec's "stated in the README" claim is checkable. Join each backticked
  queue-line literal in a spec's Messages table against the kit README, the way check-spec-tokens
  joins §6 paths, so the `docs` practice is gated instead of remembered.

### L7. The shared-path audit's health.log row points at a scope item spec 7 deleted (id 33)

- **Where:** `memory/builds/aPairedSlots/build/2026-10-11-build-TOOL-aPairedSlots-5-shared-path-audit.md:33`,
  the build README roster row 7 (`memory/builds/aPairedSlots/README.md:69`) and spec 7 §5 (lines
  92-96).
- **Grade:** low, the binding grade. Records only.
- **Defect:** the row says the trim COLLIDES and is fixed by "TOOL-aPairedSlots-7 S2". Spec 7 rev-2
  removed S2 and moved the trim to ask TOOL-aPairedSlots-10, so spec 5 AC2 ("every COLLIDES row
  names the unit that fixes it") is false for this row. The README roster still lists "health log
  trim" under unit 7, and spec 7 §5 still describes a health lock that §4 says is not built.
- **Fix (judged SOUND by the skeptic):** point the audit row at ask TOOL-aPairedSlots-10 as deferred,
  drop "health log trim" from the README roster row 7 mechanism, and remove the health-lock lines
  from spec 7 §5.
- **Left-shift gate:** a `<unit> S<n>` reference in a record should resolve against that spec's
  current §2 items. A join in the records hygiene, beside the existing spec-token joins, would have
  red the audit when spec 7 rev-2 removed S2.

### L8. The rule check counts a MAKESPAN row as proven unless its proof column says NO (id 38)

- **Where:** `memory/builds/aPairedSlots/build/2026-10-11-build-TOOL-aPairedSlots-9-rule-check.py:14`,
  fed by the A/B instrument at `:147`, `:153` and `:176`.
- **Grade:** low, the binding grade. It is H2's defect seen from the checker's side, and this report
  would grade it high with H2. The committed decision is correct either way.
- **Defect and impact:** for A1 the proof column holds `65`, the shifted expected count, so
  `assert a_ok` can never fire on a missing proof. A bar that completed with a verdict but reported
  fewer legs would also read as proven, because its `NO` sits one column further right.
- **Fix (REJECTED by the skeptic; this is the skeptic's corrected fix):** in the instrument, take only
  the verdict's first field (`head -1 | cut -f1`), so the columns never shift. In rule-check.py,
  derive each arm's proof from its own c1 and c2 bar rows, not from the MAKESPAN proof column. Detect
  the one-place shift per row by its field count (17 rather than 16). Require a verdict other than
  `-` and `int(ok) + int(fail) == int(expected)` for A1, B1 and C1 alike.
- **Author's note on the fix:** as in H3, `head -1 | cut -f1` yields the literal `ended`, which works
  as a presence test but records no verdict. Apply H2's by-key read in the instrument, and keep this
  fix's rule-check half, which handles the committed shifted rows by field count.
- **Left-shift gate:** as H2.

review-shape kind=diff-review round=1 intensity=full at=synth raw=38 confirmed=30 refuted=8 unverified=0 blocker=0 high=4 medium=15 low=11 agents=11 out-tokens=528932

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | security | tools/run-gates/run-gates.sh:1371 | medium | medium | confirmed | At b6cd9fa6 ts_try_reap reads pid (1371) and heartbeat (1372) before hn (1373), so a slot reaped by another waiter and re-claimed through its nonce write between B's pid read and B's nonce read passes the re-check at 1380 and is rm -rf'd while live. Spec 2 S3 says the guard uses 'the nonce read when the slot was judged' and leaves alone a slot whose nonce changed 'between the judgement and the removal'. The code misses that window, and the header comment (1366-1368) overstates the narrowing. The race itself is TOOL-aReapedTicket-4: base d19938f3 had no guard at all, so this is never worse than base. The new guard is still mis-ordered against its own spec. AC3's arm 30 does not claim to test the guard. Medium: the residual path is narrow and pre-existing in kind. | sound | witness-graded-against-a-fact-written-after-it |
| 2 | security | tools/run-gates/run-gates.sh:1256 | medium | medium | confirmed | check_worktree_unheld returns 0 at TS_SLOTS 1 (1256) and otherwise loops TS_SLOT_DIRS, which hold slots 1..TS_SLOTS only (1213-1214). GATE_TURNSTILE_SLOTS is a per-bar override (988-995), and mixed counts are a documented host state (spec 2 Rollout, README). Example: a count-2 bar in W holds slot 2; slot 1 frees; a count-1 bar in W is head, skips the predicate, and claims slot 1. Two bars then share W's git dir, which spec 5 S1 and non-goals forbid. Spec 5's premise that the predicate is unreachable at one slot is false here. Before this diff only one slot existed, so the diff made this reachable. It needs a per-bar count difference inside one worktree, which is narrow, and it ships dark. | unsound | - |
| 3 | security | tools/run-gates/run-gates.sh:1479 | low | - | refuted | By design and documented. The README turnstile section at b6cd9fa6 says the docs key goes to 'A run whose docs mode resolved — a GATE_DOCS_BASE naming a commit, with GATE_FULL unset', whether the hook set it or a person did. The runner comment (371-376) defines GATE_DOCS_BASE as the caller's declaration that every changed path is in the doc class, and a hand-set value asks 'the same question'. Setting it on a code branch breaks that contract, which already changed leg decisions before this build. Spec 4 section 5 records misclassification skipping the queue as an accepted risk, and the owner ruled doc-only bars unbounded. Scheduling only, with no verdict change. The finding's second fix is already the README text. | unsound | - |
| 4 | security | tools/run-gates/run-gates.sh:1214 | low | low | confirmed | Row validation (700-714) caps slots only at 15 digits and refuses below 1. The override (988-995) accepts any 1-15 digit count. Lines 1213-1214 then build TS_SLOT_DIRS with a bash while loop of TS_SLOTS iterations before the queue, the wall and any fail-open bound. A value like 10000000 spends minutes and hundreds of MB, and a 15-digit value never finishes. mempause already has a semantic cap (>100 refused), so a cap is house style. Low: it needs an absurd operator value. | sound | - |
| 5 | security | tools/run-gates/run-gates.sh:1235 | low | low | confirmed | In the new docs branch, mkdir of $TS_DOCS_ROOT/$TS_RUN (1484) is followed by the heartbeat write (1486, a $(ts_now) fork) before any trap is armed (1494-1497). No earlier INT trap exists on this path. A beacon interrupted in that window has no pid and no heartbeat. scan_dead_docs_beacons skips the pid branch on an empty pid and then hits continue at 1235 on an empty heartbeat, so the beacon is never swept. The nested check (1469) then cats its nonce on every nested run. Nothing waits on docs beacons, so the effect is a leaked directory and one cat per nested check. The window is one fork wide. | sound | - |
| 6 | security | tools/run-gates/run-gates.turnstile.test.sh:1298 | low | - | refuted | Arm 37 can be red. A runner whose pause reads any source other than the shared GATE_MEMINFO (/proc/meminfo, a per-run path, or no reading) does not pause at the fixture's 95 percent and leaves pauses empty. That is AC4's Red-when, 'either bar reads a private source'. The TOOL-aPairedSlots-3 acceptance ledger records the red as staged: 'with the second bar pointed at a source of its own, it did not pause'. So it was seen red. Overlap of the two bars is not part of AC4's claim, which is that the pause needs no second mechanism. The section 7 mutant covering only AC1-AC3 does not make AC4 unobserved. | unsound | fixture-passes-by-finding-nothing |
| 7 | correctness | tools/drift-audit/drift_report.py:3802 | high | high | confirmed | Reproduced on b6cd9fa6's drift_report.py with the arm's own open-wrapper. The file came out ['second\trow', <header>, 'first\trow'], and read_history_groups returned ([], 'drift-history.tsv opens with a header this engine does not write'). The reader keys on lines[0] (3827-3829), so the history stays unreadable for every later --delta and dead-streak read. Base's tell()==0 writer produced a duplicate header, which the reader survived. The new xb-then-ab split also adds an empty-file state: a creator killed, or whose ab open fails, between the two opens leaves a file that later writers never give a header. test_drift_history_two_writers checks only lines.count(header)==1 and both rows present, so it certifies a file the reader rejects. High: narrow real path (first-ever concurrent write), report-only history, and an arm certifying the broken outcome. | unsound | line-claim-matched-over-the-whole-output |
| 8 | correctness | tools/run-gates/run-gates.sh:1479 | medium | medium | confirmed | The docs branch (1479-1502) admits with no same-worktree test, and check_worktree_unheld reads slot beacons only, so a doc-only bar in W runs beside W's slot holder or another doc-only bar in W. At base slots=1 it queued behind W's holder, so the diff made this reachable. Spec 5 section 4 and the shared-path audit claim every git-dir path stays one bar's because of S1, and that is now false. Real collisions: gate-logs/<leg>.log is keyed by leg name (LOGDIR=$GD/gate-logs), and legs without doc_reads run in both bars. gate-run/current and gate-last-summary.txt name the last writer. The ledger loss is overstated: the merge reads $LEDGER at exit (4042), so rows are lost only when exits overlap. The owner ruling covers not waiting, not the git-dir sharing. Effect is misleading logs and pointers, not verdicts. | unsound | amendment-leaves-its-other-half-standing |
| 9 | correctness | tools/run-gates/run-gates.turnstile.test.sh:154 | medium | medium | confirmed | At b6cd9fa6 the turnstile suite keeps FLOOR_ASSERTIONS=101 (line 154), the same as at d19938f3. Its own comment says the floor moves with new arms so they are not STRANDED. Arms 29-43 add 33 counted assertions: 5+3+2+2+2+2+1+2+2+3+2+1+2+1+3, each counted on every branch. run-gates.test.sh keeps 326 although section 11s adds 9 unconditional check_mp_value calls (each one n=$((n+1))), and section 11 sits inside no host-conditional block. In this same build the runlog suite moved 211->217 and drift CHECK_FLOOR moved 478->480. With the floors unraised, every new arm can be deleted while both suites stay green. | sound | - |
| 10 | correctness | tools/run-gates/run-gates.turnstile.test.sh:1223 | medium | medium | confirmed | The runner never unsets GATE_TURNSTILE_SLOTS: it is read at run-gates.sh:988 and inherited by legs, unlike GATE_DOCS_BASE. So nest32.sh's inner runner, which strips only GATE_LEGS, runs at TS_SLOTS=2, and its TS_SLOT_DIRS already includes gate-bar-beacon.2. A nesting test that looped TS_SLOT_DIRS instead of the `"$TS_DIR_C".*` glob (rg.sh:1469) would still nest, and arm 32 would stay green. Spec 2 S5 names that one-slot inner bar as the case the glob exists for and says AC5 observes it. AC5's stated red-when (slot 1 only) is caught; S5's distinguishing case is not. The kit's gate-profiles.txt rows carry no slots key, so `-u GATE_TURNSTILE_SLOTS` gives the inner runner one slot, and the arm then discriminates. | sound | observed-by-claim-no-arm-discharges |
| 11 | correctness | tools/run-gates/run-gates.sh:1214 | low | low | confirmed | The row parser (rg.sh:706-714) refuses only values below 1 or longer than 15 digits. The env override (rg.sh:988-993) accepts any positive count up to 15 digits. rg.sh:1213-1214 then appends one TS_SLOT_DIRS entry per slot, and the reap and held-count walks stat each entry on every tick. An absurd value therefore costs O(n) time and memory before the queue. It is reachable only through operator misconfiguration, so the effect is contained to that bar. The comment's 'safe scheduling preference' holds for the row's value, not for an accepted override. Unlike width, which bounds nothing it allocates, this knob sizes an array. | sound | - |
| 12 | seams | memory/builds/aPairedSlots/build/2026-10-11-build-TOOL-aPairedSlots-1-ab-instrument.sh:147 | high | high | confirmed | Every verdict write at rg.sh:4126, 4154 and 4213 starts with `ended\t<time>`, so `head -1` puts a TAB-bearing value into column 9 and shifts every later field one place right. The committed results.tsv shows it: A1 c1/c2 read `ended 2026-... 55 10 65 yes`, and the A1 MAKESPAN proofs field is `65`, because awk's $13 is now `expected`. rule-check.py:14 accepts any token except NO, so it counted `65` as proven. A1 really was proven (shifted proof column = yes) and B1/C1 were unproven anyway, so this run's decision stands. The results record nonetheless prescribes a re-measure 'with the instrument above', and there any finished bar's real proof column is ignored, so an arm with missing legs (or a fast REFUSED bar) reads as proven. The BY-DESIGN note covers the copied A1 rows, not the instrument or the checker that still carry the defect. | unsound | ab-arm-never-did-the-work |
| 13 | seams | memory/builds/aPairedSlots/build/2026-10-11-build-TOOL-aPairedSlots-5-two-bar-check.sh:64 | high | high | confirmed | two-bar-check.sh:64 stores `ended\t<time>` (every verdict file's first line, rg.sh:4126/4154/4213), so each check.tsv row has 11 fields. Reproduced: a row with ok 50 + fail 15 gives NF=11, and `$10 < ($6+$7)` compares the timestamp string with 65 and flags the row. At gov's ~65 legs every row reds as 'row lost or torn', pointing the VERIFYING run at TOOL-aPairedSlots-7's writers. At 100-199 legs the ledger-rows half never flags. Either way that half grades nothing. The check is the build's registered VERIFYING instrument and has not yet been run, so this will mislead the next step. | sound | row-driver-emits-a-plausible-file-with-rows-missing |
| 14 | seams | memory/builds/aPairedSlots/build/2026-10-11-build-TOOL-aPairedSlots-5-two-bar-check.sh:91 | medium | medium | confirmed | Line 91 compares start/end wall windows recorded around the whole runner invocation, and those windows include the queue wait. If the second slot were not granted, the second bar would sit in the claim loop (rg.sh:1565-1697) for the first bar's whole run. Its window would still overlap, the verdicts and rows would still match, and the check would print PASS on a serial run. The guard's stated purpose ('actually overlapped ... two writers') goes unchecked. | unsound | ab-arm-never-did-the-work |
| 15 | seams | tools/drift-audit/drift_report.py:3804 | medium | medium | confirmed | Reproduced with the arm's own interleaving against drift_report.py at b6cd9fa6. Run with full-width rows, the file reads [row2, header, row1], and read_history_groups returns ([], 'drift-history.tsv opens with a header this engine does not write'). That refusal is permanent for the clone. test_drift_history_two_writers passes on exactly this layout because it counts headers and never checks their position. The base's tell()==0 race wrote a duplicate header that kept lines[0] readable, so this diff turned a benign failure into an unreadable file. The race needs two first writers within one open-to-write window, so the reach is narrow, but the arm certifies a layout the history's only reader refuses. | unsound | - |
| 16 | seams | tools/run-gates/run-gates.turnstile.test.sh:1152 | medium | medium | confirmed | Measured on clean clones with `python tools/lexicon/lexicon.py --offenders`: d19938f3 lists 1068 verb offenders and b6cd9fa6 lists 1071. The sorted diff is exactly three new rows: selftest.py open_with_a_second_writer, turnstile.test.sh mk_docs_repo and turnstile.test.sh wait_registered. The pin stays 1063. So the leg is already red at the base, and this build adds three own offenders on top, which line-keyed red attribution reads as MIXED rather than inherited. The proposed targets lead with declared verbs (check, measure, build and run all appear as declared, from DEBT suggestions or existing non-offenders such as measure_bar and run_slot_bar), and none collides with an existing name. | sound | naming-leg-grades-what-python-named |
| 17 | seams | tools/run-gates/run-gates.turnstile.test.sh:135 | medium | medium | confirmed | At b6cd9fa6 the suite exports only GATE_TURNSTILE_DIR (test.sh:135). mk_repo copies the real gate-profiles.txt (test.sh:181). The runner takes PROF_SLOTS from the selected row's slots= key (run-gates.sh:736) and lets GATE_TURNSTILE_SLOTS override it (:988-994). It never unsets that variable for legs. Arms 1-28 pass no count, so they inherit both sources, and arms 33, 38 and 41f pass an empty override, which falls through to the table. The new knob introduced this dependency: before this diff there was no count to inherit. Arm 23 asserts peak 1 across two repositories (test.sh:1031), and arms 16, 23 and 25 grep the one-slot 'another bar holds this host' line. Both checks red at slots=2. So enabling the capability through either documented path (slots=2 on a row, or an exported GATE_TURNSTILE_SLOTS=2) reds the suite with failures that read as turnstile regressions. Today's table has no slots key, so the suite is green now. The effect is a misleading red, not a false green, so the grade is medium. | sound | - |
| 18 | seams | tools/run-gates/run-gates.sh:1479 | medium | - | refuted | The behaviour is real: the docs branch (run-gates.sh:1479) never calls check_worktree_unheld, and each docs beacon is keyed by run id. But the stated BY DESIGN covers it: a docs-only bar is unbounded on its own key by owner ruling and never waits for a non-doc slot. Spec 4 S2 and its Non-goals ('A cap on doc-only bars; the owner chose none'), the runner's comment and the README ('Nothing caps how many run at once (owner, 2026-10-11)') all record that ruling. Admitting a doc-only bar beside a same-worktree non-doc holder is exactly 'never waits for a non-doc slot'. Two doc-only bars in one worktree is exactly 'unbounded'. What remains is that the shared-path audit and spec 5 do not name this exception, which is a documentation gap inside the owner's ruling, not a defect this review can hold against the code. | unsound | - |
| 19 | seams | tools/run-gates/run-gates.sh:1260 | low | low | confirmed | check_worktree_unheld sets TS_SAME (run-gates.sh:1252-1260), and grep finds no reader of it anywhere in the runner. The 'held, one by this worktree' line (:1681) prints $ts_names, the list of every holder. The finding overstates one point. Each entry carries '<repo> run <id> pid <pid>', and repo is the holder's top level, so a reader can find this worktree's entry by its path, and spec 5's 'names the same-worktree holder' is technically met. The remaining defect is a variable this diff mints and never reads. That is dead plumbing with no behavioural effect. | sound | - |
| 20 | seams | tools/run-gates/README.md:202 | low | low | confirmed | Spec 5 section 5 says the head-of-line risk is 'Stated in the README', and its user-docs line names 'the README's turnstile section'. That section at b6cd9fa6 (README.md:192-262) has paragraphs on slots, shared width and the docs key. It never states one slot per worktree, never mentions the head-of-line wait, and never gives the 'held, one by this worktree' queue line. The README states only the all-held line shape. The promised documentation is missing, with no behavioural effect. | sound | - |
| 21 | verification | tools/drift-audit/selftest.py:3671 | high | - | refuted | The mechanics are as described. The arm's wrapper runs the second writer inside the creator's open(path,'xb'). The second writer's create fails, so it appends 'second\trow' before the creator's 'ab' write lands the header. read_history_groups then returns [] with 'opens with a header this engine does not write' (drift_report.py:3826-3829). But spec 7 section 4 records this exact case as an accepted residual: 'a second writer that appends in the instant between the first writer's exclusive create and its one write lands its rows above the header ... the reader skips a history that does not open with its header rather than misreading it.' AC4 asks only that the file carry exactly one header line, which the arm checks and which reds against the old size-check writer. The arm certifies what AC4 states, not 'the history is readable'. The window is one open plus one write, on the first-ever write to a clone's history, so it is a by-design residual and not a false certificate. | unsound | - |
| 22 | verification | tools/run-gates/run-gates.turnstile.test.sh:154 | medium | medium | confirmed | FLOOR_ASSERTIONS is still 101 at b6cd9fa6 (test.sh:154), and its last comment is TOOL-aFrugalTurnstile-5's raise for arms 23-28. Counted off the blocks, arms 29-43 contribute 5, 3, 2, 2, 2, 2, 1, 2, 2, 3, 2, 1, 2, 1 and 3, which is 33 executed assertions. Arms 1-28 are unchanged by this diff, so a passing run reaches 134 against a floor of 101. The suite's own comment says arms left under an unraised floor are 'STRANDED rather than red'. No spec in this build waives the raise. The drift selftest (478 -> 480) and runlog suite floors did move, so this one was missed. The effect is a lost guard against silent arm loss, contained to this suite. | sound | - |
| 23 | verification | tools/run-gates/run-gates.turnstile.test.sh:1223 | medium | medium | confirmed | The outer bar in arm 32 runs with GATE_TURNSTILE_SLOTS=2 (test.sh:1226). The runner never unsets that variable: its only unsets are lines 232, 242, 386, 2221, 2226 and 2688. nest32.sh strips only GATE_LEGS, so the inner runner computes TS_SLOT_DIRS = [beacon, beacon.2]. A nested test that iterated TS_SLOT_DIRS, the rev-1 design spec 2's revision log replaced, would still find slot 2's nonce and pass. S5 names the case this arm misses: 'a fixture bar whose own table declares fewer slots than the holder'. AC5's own red-when (slot 1 only) is caught, but the S5 mechanism is not discriminated. The gap is contained: a regression would make a nested runner queue to fail-open behind its parent. | sound | - |
| 24 | verification | tools/run-gates/run-gates.sh:1380 | medium | medium | confirmed | The base ts_try_reap (d19938f3) had no nonce re-check, so the guard at run-gates.sh:1380-1393 is new in this diff. Arm 30 plants slot 2 with a constant nonce 'planted30', and arm 42 plants docs beacon 'p42' the same way. Both re-checks always hold in those arms, and no other arm changes a nonce between judgement and removal. Deleting the re-check in ts_try_reap or scan_dead_docs_beacons leaves every arm green. Spec 2 S3 claims the guard is 'Observed by AC3', but AC3's red-when is only 'walks slot 1 only'. The guard narrows a tracked race rather than closing it, so its loss is contained. | sound | - |
| 25 | verification | tools/run-gates/run-gates.test.sh:125 | low | low | confirmed | At b6cd9fa6, run-gates.test.sh:125 still reads FLOOR_ASSERTIONS=326, the same value as at d19938f3. The range adds section 11s (lines 3155-3181), which holds nine check_mp_value calls. Each call does n=$((n+1)) (line 3129). The section sits at top level outside any host conditional, so all nine run on every host. The PINNED_KNOBS edit adds no count. The floor's own history shows it is raised for every new unconditional assertion. Deleting 11s would leave the executed count at the floor, so nothing would go red. HEAD (the merge 0b4954c9) still reads 326. The effect is limited to coverage of one section. | sound | - |
| 26 | verification | tools/run-gates/run-gates.sh:1238 | low | low | confirmed | scan_dead_docs_beacons (run-gates.sh:1223-1245) is new in this range, and its stalled branch is lines 1236-1241. Spec 4 S5 puts both the dead sweep and the stalled sweep in scope, and its Messages table names both lines. AC5 and arm 42 (turnstile.test.sh:1388-1394) plant only a dead pid, from `sh -c 'exit 0'`, with a fresh heartbeat, so they reach only the dead branch. No arm in either suite greps 'docs beacon of a stalled holder'. A wrong age sign or a wrong ttl source in that branch would not go red. The branch reads correctly today, so this is a coverage gap with contained effect. | sound | - |
| 27 | verification | tools/run-gates/run-gates.sh:1736 | low | - | refuted | The facts are accurate: TS_DOCS=1 is set before the mkdir (line 1481), the failure branch records queued_from docs (line 1736), and no arm covers it. It is still not a defect. Spec 4 S3 asks for queued_from `docs` on a doc-only run. Spec 4 section 5 asks only that a docs beacon that cannot be created 'runs the bar UNQUEUED with a NOTE', and line 1499 prints that NOTE. The recorded `queued 0 from docs` is true either way: the bar was doc-only and waited 0. The unticketed/expired split this finding cites exists to keep the invariant that an expired run is never 0, and no invariant or reader here depends on telling a named docs run from an unnamed one. Skipping the traps and the HOLDER export is correct when there is no beacon to release. The finder graded it low, and the effect is purely observational. | unsound | one-value-field-records-a-mixed-outcome |
| 28 | verification | tools/run-gates/run-gates.turnstile.test.sh:1306 | low | - | refuted | Arm 37 implements spec 3 AC4 exactly as written: two fixture bars share one GATE_MEMINFO at 95 percent under mempause=90, and both records carry a non-empty `pauses`. AC4's stated red case is 'either bar reads a private source'. A mutation that gives read_mem_used a per-bar source would turn the arm red, so the arm can fail for the property it pins. Spec 3 S4 says deliberately that this unit adds no pause code, so the arm characterizes an unchanged property and does not test a new mechanism. Whether the bars overlapped does not affect that property, because the reading is one static file. A serialized pair would still show correctly that both bars read the shared source. The concurrency wording in the label is at most a cosmetic overstatement. | unsound | - |
| 29 | intent | tools/run-gates/run-gates.sh:1479 | high | medium | confirmed | The docs branch (run-gates.sh:1479) is gated only on DOCS_BASE and no --hold, so it is live at the shipped slots=1. check_worktree_unheld returns 0 at once when TS_SLOTS<=1, and above 1 it reads only TS_SLOT_DIRS, never gate-docs-beacon. At d19938f3 a doc-only bar took a ticket and queued behind any holder, so it never overlapped another bar in its own worktree. Now a doc-only push from worktree X and any other bar in X run together, and either may start first. They share $gd: the ledger's read-merge-mv at exit (lines 4009-4045, a lost-update window), `gate-run/current` through the fixed current.tmp (line 2205), gate-logs/<leg>.log (line 265, named per leg, and the legs overlap), and gate-last-summary.txt and gate-last-failure.txt. push-main.sh:252 sends the user to that summary after a red push. The shared-path audit marks every one of these paths 'per-worktree; S1', and the README goal says two concurrent bars 'lose no ledger row, run-log line or run record'. Spec 4 never considers the same-worktree case. The owner's ruling decided the docs key's count (unbounded) and that it does not queue, not this collision, so the BY DESIGN item does not cover it. Severity is medium, not high. Verdicts are read per run id (pre-push reads gate-run/$RUNLOG_GATE_RUN), so no verdict changes. Ledger rows are advisory and are lost only in a narrow exit window. A same-worktree overlap of a doc-only push with another bar is uncommon under the one-unit-per-worktree rule. What is lost is evidence and cache, on a narrow path. | unsound | - |
| 30 | intent | memory/builds/aPairedSlots/build/2026-10-11-build-TOOL-aPairedSlots-5-two-bar-check.sh:91 | high | high | confirmed | run_bar (lines 44-51) stamps `date +%s` before and after the whole runner, so the window includes the queue wait. cmd_run starts both concurrent bars together (line 78), so s1 and s2 are about equal and each end is later than both starts. The guard at line 91 (s1<e2 && s2<e1) is therefore true even if the turnstile serialized the pair, for example if the slots override did not take. Nothing else in cmd_run catches serialization: the verdict comparison and the row-loss checks pass either way. The comment at line 90 says the guard exists to catch exactly this. A serialized pair would print TWO-BAR CHECK PASS for the build's VERIFYING two-writer check (spec 5 S3, spec 7) without the two writers ever running together. The path is narrow, since slots normally take, but the consequence is a check certifying what it did not observe. The proposed fix works through its first alternative: the header carries `acquired` (line 2562) and, above one slot, `slot` (line 2555). In the second alternative, `queued 0` can go red falsely when the second bar waits one 2 s tick at the FIFO head. The distinct-slot test (1 and 2) alone already proves the overlap, because resolve_free_slot takes slot 2 only while slot 1 exists. | sound | - |
| 31 | intent | tools/run-gates/run-gates.sh:1214 | medium | medium | confirmed | The row validator refuses only values over 15 digits (line 705) and 0 (line 713). The override parse accepts any 1 to 15 digit positive value (lines 990-993). Nothing bounds the magnitude. TS_SLOT_DIRS is then built by a bash loop from 2 to TS_SLOTS (lines 1212-1216), and measure_held_slots and resolve_free_slot walk the whole array. A value like 100000000, from a row or from an exported GATE_TURNSTILE_SLOTS that nested runners inherit, means a loop of about 10^8 iterations and gigabytes of path strings before dispatch, which is a hang at the push boundary. GATE_JOBS clamps over-long values to 64 (line 797) for the same hang class. Spec 1 S2 allows 'at most 15 digits' for parse safety and never considered magnitude. The defect is real but needs a misconfiguration, so its effect is contained. | sound | - |
| 32 | intent | tools/drift-audit/drift_report.py:3802 | medium | medium | confirmed | At d19938f3, write_drift_history wrote the header whenever fh.tell()==0, so an empty file healed itself on the next write. At b6cd9fa6 the header is written only when this call's `xb` create succeeded (drift_report.py:3802-3810). An existing empty file now gains headerless rows forever. read_history_groups (line 3818) and manifest-check.sh's drift cell then refuse the history permanently, and no tool repairs it. Reachable triggers: ENOSPC or another OSError on the append after a successful create, a kill between the two opens, or a touched or truncated file. All are narrow. The effect is contained to the report-only delta and the kickoff drift cell, both of which print a visible skip or UNKNOWN. The proposed fix is unsound. In the very race S4 closes, writer A creates the file and writer B appends before A writes. Under the fix, B sees tell()==0 and writes a header, then A, having created the file, writes a second one. That is the two-header outcome, and the AC4 arm (selftest.py, two-writers) turns red because its wrapper runs the second writer after the first one's real create. The fix's second alternative, skipping leading non-header lines, does not cure an empty file that never gets a header, and manifest-check.sh reads line 1 separately. (The current AC4 arm also passes with the header on line 2, which is the spec's accepted residual.) | unsound | - |
| 33 | intent | memory/builds/aPairedSlots/build/2026-10-11-build-TOOL-aPairedSlots-5-shared-path-audit.md:33 | low | low | confirmed | At b6cd9fa6 the audit's health.log row says 'the trim COLLIDES; TOOL-aPairedSlots-7 S2'. Spec 7 rev-2 removed S2 and put the trim in ask TOOL-aPairedSlots-10 (spec 7 §1 and §3). Spec 5 AC2 requires that every COLLIDES row names the unit that fixes it, and this row names a scope item that no longer exists. The build README roster row 7 still lists 'health log trim'. Spec 7 §5 still has 'the health lock costs builtins only', 'a trim that cannot take its lock skips the trim' and 'risks — the stated trim residual', while §4 says no lock is built. All three are records only and change no behaviour. | sound | - |
| 34 | intent | tools/run-gates/README.md:212 | low | low | confirmed | The turnstile section of tools/run-gates/README.md at b6cd9fa6 (lines 192-240) cites TOOL-aPairedSlots-2, -3, -4 and -9. It never states the one-slot-per-worktree rule, the queue line 'held, one by this worktree' (run-gates.sh:1681) or the head-of-line cost. Spec 5 §5 says that risk is 'Stated in the README' and names the README's turnstile section as the user doc. No commit in the range adds this text. The consequence is a gap in the docs only. | sound | - |
| 35 | intent | tools/run-gates/run-gates.sh:1252 | low | low | confirmed | Running git grep at b6cd9fa6 finds TOOL-aPairedSlots-5's TS_SAME in exactly four places: the global init at run-gates.sh:1252, the comment at 1253, and the assignments at 1255 and 1260. Nothing reads it: the 'one by this worktree' line at 1681 prints $ts_names, and no test reads it. Spec 5 §4's inventory says 'No function or variable is minted beyond a local in the claim', yet the unit minted the global check_worktree_unheld function and the global TS_SAME. This is dead state with no effect on behaviour. | sound | - |
| 36 | intent | tools/run-gates/README.md:217 | low | - | refuted | The README sentence is accurate. Spec 9 §4's rule, which the A/B applies, sets TS_SHARE_RULE to `half` only when B_1 < C_1 is shown, and to `full` otherwise. The results record's F2 states exactly that: neither was shown, so the other branch gives `full`. The runner comment 'until that measurement says otherwise' also still holds, because the measurement did not say otherwise. Neither text claims that `full` was measured to beat `half`. An owner who follows the build README's Parked slot is told to 're-measure on a freshly booted host first'. Neither text is wrong, so there is no defect beyond wording a reader could misread. | sound | - |
| 37 | intent | tools/run-gates/run-gates.sh:1469 | low | - | refuted | The nest test that matches on the nonce alone is pre-existing. At d19938f3, run-gates.sh:1332 also matched the single beacon's nonce with no liveness check. So an orphaned leg of a SIGKILLed slot holder nested at base too, until a later waiter reaped the beacon. What this build adds is narrower than claimed. The exposure lasts as long as the orphaned descendant that carries the nonce lives, not 'indefinitely', because only processes descended from the killed bar carry GATE_TURNSTILE_HOLDER. A doc-only bar runs only legs that declare doc_reads, for seconds, and it must be SIGKILLed (TERM, INT and HUP all release through its trap). One of its orphans must then start a runner. Even then the only consequence is one unqueued bar contending for cores. It does not produce a wrong verdict. | sound | - |
| 38 | intent | memory/builds/aPairedSlots/build/2026-10-11-build-TOOL-aPairedSlots-9-rule-check.py:14 | low | low | confirmed | The instrument writes the first line of the run record's verdict file (abi.sh:147). For any bar that has a verdict, that line carries a tab and the end time, so every column from `ok` on moves one place right. The proof test at abi.sh:153 requires verdict != '-', so every proven bar is shifted. MAKESPAN's proof is then built from awk $13 (abi.sh:176), which for such bars holds the expected count. The committed A1 MAKESPAN row therefore has '65' in the proof column, and rule-check.py's `proven = 'NO' not in f[12]` reads it as proven without checking ok+fail. A bar that completed with a verdict but reported fewer legs would also read as proven, because its NO sits in f[13], so `assert a_ok` cannot fire on such a row. The decision committed here is correct: A1's bar rows show 55+10=65 'yes', and B1 and C1 are lower bounds that fail on makespan anyway. The flaw is contained to a one-shot record check. | unsound | - |
