**Serves:** spec-audit TOOL-aBatchedArm-5

# Tier-2 spec audit — TOOL-aBatchedArm-5, ROUND 2

*The fold audit. Round 1 (BLOCKED, 3 blockers, 13 highs, 11 mediums, 1 low, precision 0.52) was
folded into rev-3 of the unit that replaces the pooled mode's `budget x sweep-ceiling-factor` hang
bound in `tools/run-gates/run-selftests.sh` with an evidence-derived one, declares a
`--pooled --calibrate` bootstrap, gives the runner its own tracked evidence file, and lands the DoD
flip dark for the build's landing step to complete. This round grades the FOLD — the four scope
decisions S1 through S4, the nine ACs, the rebuilt fixture and the derived §7 — and does not
re-report what round 1 found. Node `a`, 2026-09-14, ROUND 2. Every finding below survived a skeptic
prompted to REFUTE it, and every cited line, byte count, population and exit path was re-read or
re-run in the tree by the author of this report rather than transcribed from a lens: the charter was
re-measured with `tools/check-template-size.sh`, the carrier grep was re-run, the fourteen-row
population was re-listed, the sweep TSV rows were re-read, `derive-ceilings.py`'s `read_runs` and the
kit runner's `--all` branch were opened, and the held-leg split was re-derived from
`tools/gate-legs.json`. Each row carries its address inside the spec, the fix, and the gate that
would have caught it before a reviewer had to.*

**Reviewed subject, pinned at blob:**

- `memory/builds/aBatchedArm/spec/2026-09-13-spec-TOOL-aBatchedArm-5.md`@`fab55333537f3095278a4d3d3509083394922320` — rev-3, the fold of round 1's eleven defects. ROUND 2.

The sibling specs are NOT in scope and are not re-graded. Units 3 and 4 are CLOSED at this spec's
base `1c736fd9`; their rows, modes and oracle are read here only as the tree this unit consumes, and
a row below names one of them only where THIS unit's declaration about that sibling is wrong.

**Two owner rulings bind this build and were applied as facts, not findings.** 2026-09-13: build
first and verify once. 2026-09-14: no gate runs until every unit of the build is built. Every AC's
real-row half is therefore observed at the build's final gate pass, and several rows below are
severe precisely because that pass is the ONLY one the build gets: a red the spec did not write a
branch for is met there by a run with no owner turn.

## Verdict: BLOCKED

Two rows at BLOCKER, fifteen at HIGH, seven at MEDIUM, one at LOW. Those twenty-five rows collapse
to **eleven distinct defects**; the table below names which rows share one, so a fold that repairs a
defect repairs every row under it rather than twenty-five separately.

The fold got the four scope decisions right in shape. The population is the DoD command's RESOLVED
one and the spec says so where it counts; the flip is dark with an ordered landing; an uncalibrated
row refuses and the factor is retired with no fallback left to fall back on; the rule is claimed
whole with node in the key. What is wrong is that the landing order the fold wrote cannot execute on
the tree it names, at two of its three steps, and the spec presents both as contingent on the bound
holding rather than as decided by facts already in the tree.

**Step three gates the flip on a GREEN the build's own oracle forbids** (E-1). The eight shard rows
are RED at base by design — unit 3 AC11 says the suite is red at BASE and its §3 forbids changing
that, the build README says the RED baseline IS the oracle — and `run-unattended-gates.sh --pooled`
sets `st=1` whenever the runner exits nonzero, which the sweep renderer does on any `FAIL` row. So
`unattended gates RED` prints on the merged tree whatever the hang bound does, the pasted GREEN the
flip is gated on cannot exist, and the red-outcome clause fires by construction. **Step one is
predicted RED by the record the spec itself cites** (E-2). For the fourteen rows `--kit
tools/unattended --list` resolves the calibrate wall computes to max(ceil(20530/8), 3860) = 3860 s at
this node's width 8, which is 1.5x the driver suite's single serial reading as the bound on an
8-wide contended pool; the full-sweep TSV the spec's §1 and §4 rest on shows that same driver row
still running at 7722 s under the same width on the same node. A killed row writes no reading, S1
then refuses the graded run by name, and S4 writes an outcome only for a red at step THREE. §4 argues
that serial numbers cannot predict pooled cost and then derives the calibrate wall from them.

Behind those two, one defect makes the goal unreachable even if both steps went green: `kit.toml:126`
is declared the cost pass that keeps `--serial`, but `--all` runs the self-test half as well as the
checks, and the block binds both commands with "not done until this prints GREEN" — so the post-flip
DoD owes every self-test serially AND a pooled pass, and the flip removes nothing (E-3). The rest is
a reused rule that is not reused whole (E-5), an unsequenced tracked write inside a mode that reds on
tracked writes (E-6), a fixture rebuild that seeds one token where the suite produces two (E-7), a
final pass that holds the only leg observing the fixture ACs (E-8), a dark spelling that reds the
charter-size leg by eighteen bytes (E-4), a carrier set whose stated derivation yields a different
eight (E-9), a node key that is a hostname rather than the registry tag (E-10), and a §7 derivation
sentence false in both directions (E-11). Each row carries its line.

Under `memory/guides/BUILD-METHOD.md` the loop re-arms on a STRICTLY SMALLER confirmed-blocker
count: round 1 stood at three blocker rows, this round at two, so the fold converged and a round 3
is owed after the next fold. Disposition of both standing blockers: FOLD — each is a defect in the
document this review read, and the mechanism each needs (a FAIL-set-equivalence criterion in place
of a pasted GREEN; a calibrate wall floored at the serial SUM plus a written step-one red branch)
exists in this unit's own scope.

## Review shape

- raw 51 · confirmed 25 · refuted 26 · unverified 0 · precision 0.49

Precision at 0.49 sits just under the ~0.5 floor `AGENTS.md` §8 sets before tightening scope or
priming rather than adding agents; round 1 stood at 0.52 on a raw 54. The number is the pipeline's
and is reported as measured. Read the confirmed count with the table in hand: four rows hit the
charter-size defect independently, four hit the calibrate wall and four hit the reading witness,
which the pipeline reports as zero duplicates because each addresses a different section or a
different consequence.

## Run integrity

- lenses 4/4 returned, 0 DIED
- skeptic batches 5/5 returned, 0 DIED
- 0 contradictory verdict(s) demoted to unverified
- 0 spurious verdict(s) discarded
- 0 duplicate(s)

Nothing died. Every zero above is a measured zero and not an absence of evidence, so this round's
finding set is complete for the lenses that ran, and a fold may treat the UNVERIFIED bucket as
genuinely empty.

## The eleven defects, and which rows carry each

| Defect | Rows | Severity |
|---|---|---|
| E-1 · the flip is gated on `run-unattended-gates.sh --pooled` printing GREEN, and the population it grades is RED by the build's own oracle, so the third landing step cannot produce its precondition | id=28 | blocker |
| E-2 · the calibrate wall computes to 3860 s over the fourteen-row population at width 8, the tree's own sweep record shows the driver row alive at 7722 s under that width, and S4 has no branch for a red at step one | id=29, id=43, id=18, id=4 | blocker / high ×3 |
| E-3 · `kit.toml:126`'s `--all --serial` is declared the cost pass that stays, `--all` runs the self-tests too, and the block binds both lines as the DoD — the flip removes no pass | id=14, id=8 | high / medium |
| E-4 · the dark spelling on `AGENTS.md:519` adds 27 bytes to a charter with 9 to spare, and the `charter size` leg §7 lists reds by construction with no funding written | id=41, id=31, id=13, id=1 | high ×4 |
| E-5 · S2 records a reading for any row that exited on its own, dropping the ok-only clause and the trailer witness, while §4 and §10 say the rule is reused whole | id=15, id=42, id=5, id=35 | high ×3 / medium |
| E-6 · `--calibrate` writes a tracked file inside a mode whose closing fingerprint reds any tracked change, and the write is unsequenced against it | id=32 | high |
| E-7 · the fixture rebuild seeds one token; the suite's pooled arms produce two and one arm appends rows at run time, so untouched arms refuse under S1 and §7 mis-prices the floor | id=16, id=37 | high / medium |
| E-8 · §7 says every listed leg runs at the final pass, but the run's declared `GATE_CMD` holds nine of the seventeen, including the only leg that executes the fixture arms | id=30, id=49 | high / medium |
| E-9 · the carrier set is defined by a grep that returns the usage line and not `SESSION-KICKOFF.md:169`, so the enumerated eight is authored and AC5 pins it with no `figure:` | id=2, id=19 | high / medium |
| E-10 · the node key falls to a hostname on every real invocation, while the sibling evidence file and the spec's own §4 speak in registry-tag terms | id=46 | medium |
| E-11 · §7's "derived by guard" sentence omits eight legs the rule fires and names a leg that reads neither carrier; §10 parks the parity arm in that leg | id=47, id=11 | medium / low |

---

# BLOCKERS

## B1 · id=28 — the third landing step is gated on a GREEN the oracle forbids

**Address:** section 2 S4 (the landing order, third step) · section 6 AC5 (the landing half and
its red-when).

S4 orders the landing: calibrate, commit the evidence, then "`run-unattended-gates.sh --pooled` runs
and its GREEN is pasted; ONLY THEN the seven DoD lines drop `--serial`". AC5's landing half repeats
it: the command "completes GREEN on the merged tree … its GREEN pasted, and the flip commit follows
it". Verified at source, that GREEN cannot exist at this base. The population the command grades is
the fourteen rows `--kit tools/unattended --list` resolves, eight of which are the shard rows unit 3
landed RED by design: unit 3 AC11 reads "the suite is red at BASE and §3 forbids changing that", the
build README reads "The baseline is RED and is the oracle. Equivalence is the `FAIL` line set plus
the executed assertion count", and unit 3's ledger records the eight shards' FAIL sets as
3·1·0·0·6·0·11·0, twenty-one in all and identical to BASE. `check-unattended.test.sh` exits `$st`,
which is 1 on any FAIL; the sweep renderer marks a nonzero-rc row FAIL and exits 1;
`run-unattended-gates.sh:303` sets `st=1` on that, and the driver prints `unattended gates RED`.

So step three prints RED on the merged tree whatever the hang bound does, "on a red at the third
step the carriers stay `--serial`" fires by construction, and the unit's stated goal — the flip —
is unreachable while the spec reads as if it turned on the bound holding. S2 already knows the rows
complete with rc 1, since it records a reading for any completed rc, so the fold is internally
inconsistent: it admits red readings at step one and requires a green run at step three over the
same rows.

**Fix.** Replace "its GREEN is pasted" in S4 and AC5 with the criterion the oracle allows, and say
why GREEN is not the criterion, citing unit 3 AC11 and the README's oracle sentence. The landing
step's witness is the pooled pass's own output, pasted: no `TIMEOUT`, `WALL` or `UNRUN` row; peak
within outer; fingerprint MATCHED; and a `FAIL` line set byte-identical to the serial baseline's for
every row (the README's equivalence, applied per row). The driver's exit status is not the witness,
because it folds the oracle's red into the verdict. AC5's red-when becomes "a row is killed, the
fingerprint is not MATCHED, or any row's FAIL set differs from its serial one" in place of "the
landing pass kills a row and the flip lands anyway". If the kit runner is to print something a
landing can read, add to S4 that its pooled branch distinguishes "every FAIL set matched the serial
baseline" from "a row was killed" in its summary line, since today both are `st=1`.

**Left-shift gate.** The `run-selftests self-test` arm for the pooled verdict renderer asserts that a
fixture row exiting rc 1 on its own renders `FAIL` with its FAIL count and a row killed by its bound
renders `TIMEOUT`, and that the summary line counts them SEPARATELY — so a landing criterion that
needs the two told apart can be read off the summary rather than re-derived from the rows. Until
built, the documented fold check: any S item or AC whose witness is "GREEN" over a population names
that population's recorded baseline verdict, and a baseline that is RED by design makes "GREEN" a
malformed witness.

## B2 · id=29 — the calibrate wall is predicted RED by the record the spec cites, and step one has no branch

**Address:** section 2 S2 (the calibrate wall) · section 2 S4 (the landing order, first step) ·
section 8 F5 · section 6 AC3 (`cost:` and the real-row half).

S2 derives the calibrate wall as `ceil(sum of serial budgets / OUTER)` floored at the largest serial
budget, `SELFTEST_WALL` overriding. Arithmetic verified for the population S4 names: `--kit
tools/unattended --list` resolves fourteen rows summing to 20530 s with `unattended driver selftest`
largest at 3860 s; `run-gates.sh --print-profile` gives width 8 on this node and the runner sets
`OUTER=W` in sweep mode; ceil(20530/8) = 2567, floored at 3860, so the calibrate wall is 3860 s. That
is 1.5x the driver's own serial reading (2569 s, the budget's origin) as the bound on an 8-wide
contended pool. The tree's own measurement of that population under that width on this node —
`memory/builds/aPooledSweep/build/2026-09-08-build-TOOL-aPooledSweep-1-full-sweep-rows.tsv` slot
54 — shows `unattended driver selftest` at rc 124, 7722 s, still running past 2x its bound, and slots
51, 53, 56 and 57 show four more unattended rows killed at their 2x bounds. Unit 3 measured ~2x
per-assertion dilation beside two other runs. §4 of this spec cites `TOOL-dRetiredFork-40` refusing
to predict a loaded reading from a quiet one by multiplying, and then S2 derives the bound on a loaded
pool from quiet serial numbers.

Under S2 a wall-killed row writes NO reading and makes the calibrate exit RED; under S1 the graded
run then REFUSES for that row by name. S4 writes an outcome only "on a red at the third step".
Nothing says what an unattended landing does on a red at step one — re-run under `SELFTEST_WALL`, and
record what; or land without the flip — and F5 keeps `SELFTEST_WALL` out of the DoD as a typed number
while the runner's own remedy line says "Raise SELFTEST_WALL". A reachable red with no written branch,
at a landing with no owner turn.

**Fix.** Two parts. (1) S2 floors the calibrate wall at the SUM of the serial budgets, undivided —
the population fully serialized, the largest derivable backstop with no typed number; a pooled pass
exceeding its own serial sum is the fact the calibration exists to observe, not a hang. Keep
`SELFTEST_WALL` as the tightening override, print the derived wall and which term won. F5 records
that the divided form was rejected because the tree's own sweep record kills it. The alternative, if
the divided wall is kept: S4's landing order sets `SELFTEST_WALL` for the calibrate from the sweep
TSV's largest truncation for this population, derived at the landing by a named command, never
typed. (2) S4 adds the step-one branch: on a calibrate red the killed rows are named in the landing
record; the landing re-calibrates ONCE with `SELFTEST_WALL` set to the serial sum and the value
printed in the landing report as a bootstrap figure and never a carrier; a second red lands without
the flip exactly as a step-three red does, and AC3's real-row half is ledgered AMENDED naming the
killed rows. AC3's `cost:` and `Red when:` are re-derived from whichever wall is chosen, and its
red-when gains "a calibrate red with no recorded branch".

**Left-shift gate.** A `run-selftests self-test` arm that stages a fixture row sleeping past the
DIVIDED wall but under the SUM and asserts the calibrate records it — RED first with the divided
wall, then GREEN. On the record side, the documented fold check: every wall or ceiling a spec derives
from serial figures is checked against the tree's newest pooled record for the same population before
the spec cites that record as motivation; a derivation the cited record already kills is a defect at
fold time, not at the landing.

---

# HIGH

## H1 · id=43, id=18, id=4 — the same wall, filed against §4's own argument, F5, and AC3's red-when

**Address:** section 2 S2 · section 2 S4 · section 8 F5 · section 6 AC3.

The B2 defect from three further angles, kept as their own rows because each names a sentence the
fold must change. id=43: §4 "Why the evidence shape and not a factor" cites `TOOL-dRetiredFork-40`
refusing to predict a loaded reading from a quiet one, and S2 then bounds the loaded calibrate by
quiet serial budgets — the spec's own rationale refutes its own derivation, and round-1 H7 offered the
serial-sum form as one of two candidates that the fold took without checking it against slot 54.
id=18: F5 rejects a REQUIRED `SELFTEST_WALL` because it "would put a typed number in the DoD", yet
the only escape from a step-one red is exactly that typed number, so F5's reasoning decides the wrong
way once the landing is walked. id=4: AC3's real-row half has no `Red when:` for the likeliest
outcome — a first-step kill — so the ledger has nowhere to record it in either form.

**Fix.** As B2. Additionally: §4's paragraph says plainly that the calibrate wall is a backstop
against a HANG and not a prediction of cost, which is why it is the serial sum; F5 records that the
serial-sum floor is the bootstrap's bound only and that `SELFTEST_WALL` at the landing, if used, is
printed as a bootstrap figure and never carried; AC3's real-row half gains the `Red when:` clause for
a killed row and names the amended form it is ledgered in.

**Left-shift gate.** As B2.

## H2 · id=14 — the flip removes no pass: `--all --serial` runs the self-tests too

**Address:** section 2 S4 (the cost line) · section 1 · section 4 "Why the flip is the build's
landing step" · section 5 perf.

S4 declares `kit.toml:126`, `run-unattended-gates.sh --all --serial`, "the cost pass" that "keeps
`--serial` after the flip", and AC5's red-when reds if "no line declares the serial cost pass".
Verified at source: `run-unattended-gates.sh:133` sets `ONLY=""` for `--all`, and line 288 runs the
self-test half when `[ "$ONLY" = selftests ] || [ -z "$ONLY" ]` — so `--all --serial` executes every
unattended self-test serially AND the checks; its own help reads "`--all` both". `kit.toml:122-126`
binds BOTH pasted commands with "Work touching `tools/unattended/` is not done until this prints
GREEN". After the flip the DoD as text is therefore pooled self-tests plus serial self-tests plus
checks — strictly more than today's serial plus checks. That contradicts §1 ("the carriers move to
`--pooled`"), §4 ("the act that makes the fast path the recorded DoD verdict"), §5 perf ("the pooled
path becomes the recorded one") and the build README's under-20-minute target. The flip as specified
removes nothing, and AC5's red-when locks it in.

**Fix.** Decide the cost pass and write it once. Either `kit.toml:126` becomes
`run-unattended-gates.sh --checks` (the legs beside the self-tests, no second self-test run) and the
serial self-test pass is ON DEMAND — the block's "not done until" sentence re-worded in the flip
commit to bind `--pooled` plus `--checks`, AC5's red-when re-cut to "no line declares `--checks`
beside the pooled DoD" — or §1, §4 and §5 state plainly that the DoD keeps the full serial pass and
the flip ADDS a hang-bounded pooled pass rather than replacing one. The first is what the goal says;
the second is honest about the cost. The dark commit inside this unit must already carry whichever
sentence is chosen, since the block is one of the eight carriers.

**Left-shift gate.** A parity arm over the DoD carriers that resolves each pasted argv through the
runner's own option parser (`ONLY`, `MODE`) and asserts the resolved SET of passes the DoD binds is
the one the descriptor's prose names — so a cost line whose flag runs more than its comment says reds
on the bar. Until built, the documented fold check: any line a spec calls "the cost pass" is resolved
through the runner's parser at fold time and the spec states what the flag actually runs.

## H3 · id=41, id=31, id=13, id=1 — the AGENTS.md dark spelling reds `charter size` by eighteen bytes

**Address:** section 2 S4 (the `AGENTS.md:519` carrier) · section 4 Files touched · section 7
(`charter size`) · section 6 AC5.

Measured now: `bash tools/check-template-size.sh AGENTS.md` prints `64503 / 64512 bytes (9 under)`,
and `tools/template-size-limits.txt:54` pins `AGENTS.md 64512` as a declared row that `--bump` does
not move (it re-records the high-water only). S4 gives `AGENTS.md:519` the words
`--pooled after calibration` beside `--serial`, 27 bytes with its space, which takes the charter to
64530 against 64512 — over by 18. `charter size` is unguarded (`tools/gate-legs.json`, subject
`repo`, no guard), §7 lists it, and under the 2026-09-14 ruling the build's final gate pass is the
first and only time it runs. Neither S4, §4 Files touched nor §5 says what funds the bytes; unit 4
S7/AC8 is the prior art for this exact line and budgeted a 9-byte edit against 18 as an AC, and
round-1 M4's fix flagged the cap ("and where, since AGENTS.md sits at its charter-size cap") — the
fold kept the enumeration and dropped the budget. The over-limit message refuses a limit raise as
the fix for the edit that hit it, and the declared row is written "by a person, deliberately", so
it is not the run's to raise.

**Fix.** Choose one and write it in S4. (a) `AGENTS.md:519` takes NO dark spelling: the flip swaps
`--serial` for `--pooled`, eight bytes for eight, so the cap is untouched at the landing; AC5 excludes
that line from the dark set and says why. (b) The dark spelling is funded from the same paragraph —
shorten the compensating-check sentence at `AGENTS.md:519-520` by at least 18 bytes in the same
commit — and AC5 gains a `figure:` line stating the before/after bytes are DERIVED by
`tools/check-template-size.sh AGENTS.md` at build time, in unit 4 AC8's shape. (a) is the smaller
diff. Either way §4 Files touched names the trim or the exclusion.

**Left-shift gate.** The leg already exists and would have caught it; what was missing is the
arithmetic at fold time. The documented fold check: any spec edit to a file in
`tools/template-size-limits.txt` states the measured headroom and the bytes added, by the leg's own
command, in the S item that adds them.

## H4 · id=15, id=42, id=5 — S2's reading witness admits the fast red the reused clause exists to exclude

**Address:** section 2 S2 (the reading witness) · section 2 S1 (the bound) · section 4 "Why the
evidence shape" · section 6 AC3 · section 10 second bullet.

S2 records a reading "ONLY for a row that exited on its own: rc captured, not killed by the wall,
the rc written beside the seconds", and S1 derives the bound from the worst reading with no rc
filter. §4 says the rule is reused in "all five parts", and §10 paraphrases the fifth as "`read_runs`
counts completed runs only". Verified at `derive-ceilings.py:90-107`: `read_runs` keeps only
`p[1] == "ok"` rows, with the reason "a leg that FAILED may have failed fast, and a maximum taken
over failures is a measurement of the failure and not of the work". An rc-1 row that exited on its
own is exactly what that clause excludes, so the paraphrase is the opposite of the source. Two more
witnesses the fold dropped: unit 3 AC4 rev-7 replaced the rc witness with the suite's TRAILER because
"a red-but-complete run prints neither", and `memory/gotchas/ab-arm-never-did-the-work.md` defines a
timing with no completion artifact as no reading; round-1 H8's fix carried "trailer present where the
suite prints one" and rev-3 dropped that clause.

The hazard is live, not hypothetical: the eight shard rows are RED at base, so the spec HAD to admit
red readings — but it then cannot tell a completed red (1000+ s, the 21-FAIL set) from a fast red (a
shard dying at 30 s on a missing fixture). With `ceiling-margin.txt` at floor 120 / fraction 1.0 a
30 s reading bounds the row at 150 s against a 925-1546 s serial reading, and the next graded
`--pooled` kills the repaired suite as TIMEOUT. Only `--calibrate` writes, so the graded pass cannot
correct it — the class round-1 H9 named, one level down. And the single `rc` column has no stated
meaning once several readings are folded into one monotone max.

**Fix.** S2's witness is the positive artifact unit 3 AC4 names: rc captured AND, where the suite
prints a trailer, that trailer in the captured output — `this leg ran shard` for a shard row, the
`PASS (` line for `lib-selftest`/`check-unattended` greens, the last `FAIL` line followed by exit for
red-but-complete. A row lacking its trailer writes NO reading and reds the calibrate the way a killed
row does; a suite with no known trailer takes `derive-ceilings`' rc-0-only rule verbatim. The `rc`
column is defined as the rc of the reading that set the max. The calibrate summary counts red
readings separately from green ones (`calibrated <n> row(s), <r> red, graded none`). AC3's red-when
adds "a trailer-less row's seconds land in the file". §10's sentence is corrected to say the ok-only
clause is DEPARTED from for red-by-design rows and what replaces it. §7's arm list adds the
trailer-less refusal.

**Left-shift gate.** A `run-selftests self-test` arm staging a fixture row that exits rc 1 at 0.3 s
with no trailer and asserting the calibrate writes no reading for it and names it — RED first under
rev-3's witness. Until built, the documented fold check: a spec claiming a rule is "reused whole"
quotes each clause beside the sentence that reuses it, so a paraphrase that inverts one is visible
at fold time.

## H5 · id=32 — the calibrate's tracked write is unsequenced against the sweep's closing fingerprint

**Address:** section 2 S2 (when the reading is written) · section 2 S3 · section 5 testing.

`--calibrate` is a flag on the sweep branch and the spec drops nothing from that branch, so the
pool-safety fingerprint is carried: `read_tree_fingerprint()` at `run-selftests.sh:581` is
`git status --porcelain --untracked-files=no`, taken as `FP_BEFORE` at 586 before dispatch and as
`FP_AFTER` at 798 after the pool drains, and any difference prints "THE SWEEP IS UNSOUND" and reds
the run. S3 makes `selftest-pooled-evidence.txt` TRACKED. The natural implementation writes each
reading as its worker's verdict is decoded — the render loop where rc and seconds are read from
`$d/v` — and that loop runs BEFORE `FP_AFTER`, so every real calibrate reds itself for a tracked
write its own runner made. The spec never says whether the write is per row or in the render pass
after the fingerprint. The fixture cannot catch the wrong choice unless its seeded evidence file is
`git add`ed, which Files touched does not say.

**Fix.** S2 states that readings are written AFTER the closing fingerprint, in one pass over the
collected verdicts, or that the fingerprint excludes the runner's own evidence file by path; name
which. Files touched says the fixture's seeded evidence file is tracked in `build_repo`. §5 testing
adds the arm "a calibrate over a clean fixture reports the fingerprint MATCHED and the file
changed", and §7's arm list carries it.

**Left-shift gate.** That arm. Until built, the documented fold check: a mode that writes a tracked
file inside a run that fingerprints the tracked tree states the order of the two.

## H6 · id=16 — the fixture rebuild seeds one token; the suite produces two, and one arm grows the population

**Address:** section 2 S1 (whole-population refusal) · section 4 Files touched (the fixture
rebuild) · section 7 New arm.

Files touched seeds evidence "for every fixture row under the fixture's own token and node" — one
token. Verified in `run-selftests.test.sh`: `build_repo` copies only `run-selftests.sh` into the
fixture, so `run-gates.sh --print-profile` is absent and `W` falls to 2 (`run-selftests.sh:289`).
Default pooled arms therefore emit `pooled@2x1`, and the arms at lines 428, 436, 457 and 465 that set
`SELFTEST_OUTER_WIDTH=1` emit `pooled@1x2` — two tokens. The UNRUN arm at line 456 appends rows
`three` and `four` to the budget file in its setup and then runs `--sweep`; under S1's
whole-population refusal those rows have no evidence and the arm refuses with rc 2 before reaching
the rc 1 `NEVER RUN and are UNGRADED` assertion. §7 prices only two arms as moving (`run wall 140s`
and the factor TIMEOUT), so `run-selftests self-test` reds at the final pass on arms whose
assertions this unit never touched.

**Fix.** Files touched states the seed covers every token the arms produce — captured per token, as
round-1 H12's fix said — and that an arm adding rows at run time seeds their evidence in the same
setup string under the token that arm runs at. §7's New arm line enumerates every pooled arm re-cut:
the factor TIMEOUT, `run wall 140s`, the UNRUN arm, the WALL-kill arm at `SELFTEST_WALL=10` and the
below-largest arm at `SELFTEST_WALL=5` (H10 below), names the retired refusal arm at line 279, and
re-derives the floor as ten added minus one retired.

**Left-shift gate.** The leg catches it; the fold did not. The documented fold check: a fixture
rebuild that seeds keyed evidence lists the key VALUES the suite's arms produce, derived by running
the suite's setup strings, not one value assumed.

## H7 · id=30 — the final pass as declared holds the only leg that observes the fixture ACs

**Address:** section 7 Gates ("every one of them runs at the build's final gate pass").

`.unattended.conf:22` declares `GATE_CMD="bash tools/run-gates/run-gates.sh"`, bare. `run-gates.sh`
writes `ondemand` for every `subject=kit` or `chunk=selftests` leg unless `GATE_SELFTESTS=1` is set,
and `.githooks/gate-env.sh` no longer sets it (owner ruling 2026-08-27: "ON DEMAND ONLY: no boundary
sets it"). Re-derived from `tools/gate-legs.json` for the seventeen legs §7 lists: NINE are held
under that bar — `run-selftests self-test`, `run-gates canary`, `run-gates gov canary`, `run-gates
evidence`, `run-gates turnstile`, `run-gates adopter e2e`, `profile-bar selftest`, `push-main
self-test`, `check-wiring self-test` — and eight run. `run-selftests self-test` is the only leg that
executes the fixture arms behind AC1, AC2, AC7, AC8, AC9 and the fixture halves of AC3 and AC4. Under
the pass as declared no fixture AC is observed by anything, and a green `gates-green` at `--close`
certifies none of them — the green-by-absence class the charter names. Unit 4's §7 said "run on the
kit-work bar"; this spec dropped it.

**Fix.** §7 states that this unit is KIT work, that the run's declared `GATE_CMD` holds nine of the
seventeen legs (named), and that the final pass therefore ALSO runs `GATE_FULL=1 GATE_SELFTESTS=1
bash tools/run-gates/run-gates.sh` — the kit-work DoD `AGENTS.md` already names — or at minimum
`bash tools/run-gates/run-selftests.test.sh` on demand, with its verdict pasted into the landing
record beside `gates-green` rather than assumed inside it. Every fixture AC's `fixture:` line names
that invocation as its witness.

**Left-shift gate.** A memory-hygiene arm (or a `gen_build_index.py` predicate) that, for a spec
whose §7 names a leg marked `chunk: selftests` or `subject: kit`, requires the spec to name the
invocation that runs it — so "runs at the final pass" over a held leg is a finding at fold time.
Until built, the documented fold check: every §7 leg is looked up in `gate-legs.json` for its
`chunk`/`subject` and the held ones are marked.

## H8 · id=2 — the carrier set's stated derivation yields a different eight

**Address:** section 2 S4 (the carrier set) · section 6 AC5.

S4 says "The carrier set is the grep at fold time for `run-unattended-gates.sh` beside `--serial`,
eight lines in six files". Re-ran it over the tracked tree, excluding `.git`, `builds` and `archive`:
it yields eight lines in FIVE files — `.githooks/gate-env.sh:27`, `AGENTS.md:519`,
`tools/unattended/kit.toml:125` and `:126`, `tools/unattended/README.md:66`, and
`run-unattended-gates.sh:27`, `:142` and `:233`. Line 142 is the usage string, already
`(--serial|--pooled)`, and is NOT in the spec's list. `memory/guides/SESSION-KICKOFF.md:169` reads
"`--selftests --serial` only when they ask" with no script name on the line, is NOT returned by the
grep, and IS in the spec's list — the one line S4 says outranks the others. So the sentence is false
at source: the set S4 heads as DERIVED is authored, its derivation contradicts it, and AC5 pins "the
eight carrier lines" with no `figure:`. A builder re-running the named derivation edits the usage
grammar at 142 into `(--serial|--pooled after calibration)` and leaves the owner's correction entry
reading `--serial` only.

**Fix.** Either make the enumeration the set and drop the grep as its definition, stating that 142
is excluded because it already names both modes; or write the predicate that actually yields the
eight — `--serial` on a line that names the kit runner OR its DoD command (`--selftests`), excluding
the runner's own usage and argv-parsing lines — and keep the enumeration as its result at this base.
Add a `figure:` line under AC5 saying the count is DERIVED by that predicate at build time.

**Left-shift gate.** The carrier-parity arm H2's gate describes, whose row set is the predicate's
output — a carrier the predicate reaches and the spec does not name reds. Until built, the
documented fold check: a set a spec calls derived is re-derived by its own stated command at fold
time and the output pasted beside the enumeration.

---

# MEDIUM

## M1 · id=8 — the cost line's binding sentence is unowned

**Address:** section 2 S4 (the cost line).

The H2 defect from the descriptor side, kept as its own row because the fix is in a different
sentence. `kit.toml:122-124` binds both pasted lines with "Work touching `tools/unattended/` is not
done until this prints GREEN and the verdict is in the landing report". S4 flips `:125` and keeps
`:126`, and says nothing about that sentence; after the flip it still owes a full serial run at every
unattended-touching landing, and no unit owns re-wording it.

**Fix.** As H2: S4 states whether the cost line is DoD-owed after the flip or on demand, and if on
demand, the re-wording of the block's "not done until" sentence is listed in the flip commit's
contents and in AC5's landing half.

**Left-shift gate.** As H2.

## M2 · id=19 — the same carrier-set defect, filed against AC5's "the eight"

**Address:** section 2 S4 · section 6 AC5.

The H8 defect from the AC side: AC5 is stated over "the eight carrier lines", so WHICH eight is
load-bearing, and the definition and the list disagree. The usage line at 142 would take a
nonsense dark spelling and the owner's correction entry would be missed.

**Fix.** As H8.

**Left-shift gate.** As H8.

## M3 · id=35 — a fast red bounds the repaired row below its own serial budget

**Address:** section 2 S2 · section 2 S3 · section 5 risks.

The H4 defect from the bound side. A fixture refusal at 0.3 s writes 0.3 s; with the 120 s floor the
row is bounded at ~120 s; the next graded `--pooled` TIMEOUTs the repaired suite until somebody
re-calibrates. §5 risks says the shape "errs toward not killing", which is false in this direction,
and §4's "all five parts" is false for this part.

**Fix.** Beyond H4's witness: floor a row's derived bound at its SERIAL budget — a pooled row cannot
legitimately need less than its serial budget, so a bound below it is a fast-red artefact — print
when the floor took over, and add the arm to §5 testing. Correct §5 risks to name the direction it
does not cover.

**Left-shift gate.** The arm: a fixture row with a 0.3 s seeded reading and a 60 s serial budget is
bounded at 60 s plus headroom, not 120 s.

## M4 · id=37 — the pooled arms that depend on the factor arithmetic are more than two

**Address:** section 7 New arm · section 6 AC6.

The H6 defect from the arm inventory side. Beyond the two §7 names: the UNRUN arm (line 456) appends
rows with no evidence; the WALL-kill arm at `SELFTEST_WALL=10` (line 428) needs the seeded largest
bound at or under 10 s and the row to outlive it, which a captured suite-long reading cannot satisfy;
the below-largest arm at `SELFTEST_WALL=5` (line 277) refuses only if the seeded largest bound exceeds
5. AC6 protects serial arms only, so the self-test leg reds at the final pass on arms the spec says
are untouched and the build discovers the set by running it.

**Fix.** As H6: enumerate every pooled arm re-cut, seed evidence for the rows arms append, and state
the seeded readings the fixture margin is sized against so the WALL and below-largest arms are
arithmetically reachable.

**Left-shift gate.** As H6.

## M5 · id=49 — `run-selftests self-test` is a held leg and §7 does not say so

**Address:** section 7 (leg line: `run-selftests self-test`).

The H7 defect from the leg side: `tools/gate-legs.json` marks the leg `chunk: selftests`,
`subject: kit`; the ten new arms are the sole witness for AC1, AC2, AC3's fixture half, AC6, AC7,
AC8 and AC9; and §7 asserts the pass runs it without spelling `GATE_SELFTESTS=1`.

**Fix.** As H7: mark the leg held and name the invocation that runs it at the final pass.

**Left-shift gate.** As H7.

## M6 · id=46 — the node key is a hostname on every real invocation, not the registry tag

**Address:** section 2 S3 (node = `GOV_NODE` or hostname) · section 4 "Why the node is in the key"
· section 10.

Verified at source: `GOV_NODE` is read at `tools/run-gates/derive-ceilings.py:180` and set nowhere
in the tree, so S3's "`GOV_NODE` when set" clause is dead and every real calibrate writes the
hostname — on this box a name absent from the charter's §2 registry, while `USERNAME` resolves to
node `a` through the seam the tree already has, `tools/drift-audit/drift_report.py
_resolve_node_tag` (line 1790), which matches USERNAME/USER against the §2 table. The sibling
`ceiling-evidence.txt` keys this same machine `a` on every row, and §4's own rationale is written in
registry-node terms ("node `a`", a fast node against a slow one) its key cannot express. Because S1
refuses by (row, token, node), a `GOV_NODE` exported for the calibrate and not for the DoD run is a
refusal on evidence the same box just wrote. `TOOL-aCollapsedScan-9` (OPEN) names the per-node
reading as a candidate and is uncited.

**Fix.** S3 resolves the node as the registry TAG — `GOV_NODE` when set, else USERNAME/USER against
the charter's §2 table the way `_resolve_node_tag` does — refusing by name when no row matches (the
announced-unarmed state), never a hostname. §10 cites `_resolve_node_tag` as the seam and
`TOOL-aCollapsedScan-9` as the record. A follow-up backlog row for `derive-ceilings.py`'s `or "a"`
default, the same class.

**Left-shift gate.** A `--check` arm asserting every node value in `selftest-pooled-evidence.txt`
is a tag present in the §2 registry table — a hostname row reds on the bar.

## M7 · id=47 — the `unattended skill wiring` leg reads neither carrier, and §10 parks the parity arm there

**Address:** section 7 (derivation sentence) · section 10 "The kit runner's wiring leg".

§7 says the leg "reads `kit.toml` and `run-unattended-gates.sh`", and §10 names it the parity arm's
"natural home". Verified at source: the leg is `bash tools/unattended/adopt-unattended.sh --check`,
which renders the Skill from `.unattended.conf` and the `*.template.md` files and diffs four rendered
artifacts; grep over the adopter, `lib-unattended.sh` and every template for `kit.toml` or
`run-unattended-gates` returns nothing. The sentence is inherited verbatim from unit 4 §7. So §7
lists a leg that cannot fire on this unit's files and §10 names as the compensating check's home a
leg whose inputs do not include the carriers — an exemption pointing at coverage that does not exist
(charter §7), the class rev-2 corrected once already.

**Fix.** Drop the sentence from §7's derivation (the leg still runs, unguarded, not because of these
files). §10 names a real home for the carrier-parity arm: `tools/check-playbook-parity.sh`, whose job
is retyped constants compared against the source that owns them, or the `govkit selfcheck` leg, the
one reader of every `kit.toml`.

**Left-shift gate.** The documented fold check: a sentence saying a leg "reads" a file is verified
by grepping the leg's command and its inputs for that file before the spec cites it.

---

# LOW

## L1 · id=11 — §7's "derived by guard over the files touched" omits eight legs the rule fires

**Address:** section 7 (derivation sentence).

Verified against `tools/gate-legs.json` and `run-gates.sh`'s `changed()` prefix match: the touched
`.githooks/gate-env.sh` fires `branch-guard self-test` and `pre-push self-test` (guard `.githooks/`),
and the `tools/` guard fires `python resolver`, `settings-merge selftest`, `install-prefix
self-test`, `dead-path carriers self-test`, `kit-placeholders self-test` and `spec-tokens self-test`
— none in §7's list, while two other `tools/`-guarded legs (`push-main self-test`, `check-wiring
self-test`) are. The list is presented as a derivation it is not. Low under the one-final-pass
ruling, since the full bar decides the set; still a wrong claim in the spec.

**Fix.** Either re-derive the line with the rule the prose states and include the omitted legs, or
reword the prose to say the list names the legs whose SUBJECT this unit changes and that the full
bar at the final pass decides the rest.

**Left-shift gate.** A `gen_build_index.py` predicate that, given a spec's Files touched, prints the
legs `run-gates.sh`'s own `changed()` would fire and diffs it against §7 — so "derived by guard" is
checked by the guard.

---

## What the fold should do first

Ordered by leverage, not by severity: one decision under each defect repairs every row under it.

1. **Rewrite the landing criterion (B1).** The witness at step three is the pasted pooled output
   with the FAIL set matched per row against the serial baseline, not a GREEN the oracle forbids.
   This also decides what "red at the third step" means, which nothing else can.
2. **Floor the calibrate wall at the serial SUM and write the step-one branch (B2, H1).** The
   divided form is killed by slot 54 of the record the spec cites; the branch is one retry under a
   printed bootstrap wall, then land without the flip.
3. **Decide the cost pass (H2, M1).** `--all` runs the self-tests. Either `:126` becomes `--checks`
   and the block's binding sentence moves with it, or §1/§4/§5 stop claiming the flip replaces a
   pass.
4. **Take the dark spelling off `AGENTS.md:519` (H3).** Eight bytes for eight at the flip keeps the
   cap untouched; anything else owes a measured trim and an AC.
5. **Reuse the reading witness whole (H4, M3).** rc plus trailer, or rc 0 where no trailer exists;
   a red-only row refuses the graded run; the bound floors at the serial budget.
6. **Sequence the tracked write after `FP_AFTER` (H5)** and say the fixture's evidence file is
   tracked.
7. **Seed both tokens and enumerate every pooled arm (H6, M4).** Ten added minus one retired.
8. **Name the invocation that runs the held legs at the final pass (H7, M5).** Nine of seventeen
   are held under the declared `GATE_CMD`.
9. **Make the carrier derivation produce the list (H8, M2)**, and the node the registry tag (M6),
   and correct the two §7/§10 leg claims (M7, L1).

Once folded, a round 3 reads the fold; the loop re-armed at two blockers against three.
