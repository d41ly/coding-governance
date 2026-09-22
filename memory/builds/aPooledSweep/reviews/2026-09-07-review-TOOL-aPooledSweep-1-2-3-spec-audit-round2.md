**Serves:** spec-audit TOOL-aPooledSweep-1 TOOL-aPooledSweep-2 TOOL-aPooledSweep-3

# aPooledSweep — spec audit of the three-unit set, round 2

*Node `a`, 2026-09-07. A Tier-2 adversarial pass over the rev-2 specs of the pooled-sweep set: a
primed finder fan, a skeptic stage prompted to REFUTE every finding, one synthesis. Every surviving
claim about the tree was re-checked against source before it was written here; two of the re-checks
narrowed a finding's impact and are named inside the finding that carried them. The subjects are the
three specs at the blobs below and nothing else — the build README, the RUN.md and the research
record were read for context and are not graded.*

**Round: 2.** Subjects, each pinned at the blob it was read at:

- `memory/builds/aPooledSweep/spec/2026-09-07-spec-TOOL-aPooledSweep-1.md@80cd4277cc1d65d65a1df923d849f8e1cb501921`
- `memory/builds/aPooledSweep/spec/2026-09-07-spec-TOOL-aPooledSweep-2.md@250847b3a4807c29717ce59d3d7fc4c04ae61c81`
- `memory/builds/aPooledSweep/spec/2026-09-07-spec-TOOL-aPooledSweep-3.md@89942bca10ce7492337d7d0eaf9723c9e2e2816a`

## Verdict: BLOCKED

Two blockers stand and they are unrelated to each other. Unit 2 cannot be built to its own
acceptance: §4 routes a pooled-tagged budgets row into `--rank`'s existing unbacked report, that
report is a blanket refusal that exits before anything ranks, and AC5 requires the serial row to
still rank. A builder who follows §4 reds AC5; a builder who satisfies AC5 silently converts an
existing verb's all-or-nothing refusal into a per-row exclusion that no section claims and §5 calls
additive. And unit 1's whole-run bound is borrowed from a profile row whose `wall` is 10800 s while
this population's largest declared budget is 13600 s — the run wall is smaller than the per-suite
bound derived from the same row, and only 19% above one suite's own quiet-box reading, so AC9's
staged failing case is the ordinary case.

Round 1's design answer survives intact and rev-2 closed real ground: the pool is bounded, reporting
is declaration-ordered, S7 exists at all, the fingerprint's second arm is deleted rather than
narrowed, and the `--rank` refusal is now built rather than assumed. What rev-2 did not do is finish
the two moves it started. The bound it added resolves from a probe the fixture cannot answer and the
spec gives it neither fallback nor override, having argued that exact case for the width three
paragraphs earlier. The refusal it added is specified against a loop shape the reader does not have,
twice, in the paragraph whose own opening sentence says the net is therefore BUILT rather than
assumed.

## Run integrity

Lenses 4/4 returned, 0 DIED. Skeptic batches 5/5 returned, 0 DIED. 0 contradictory verdicts demoted
to unverified, 0 spurious verdicts discarded, 0 duplicates. Nothing in this pass died, so the zero
counts here are evidence rather than silence, and the finding set is complete for the lenses that
were run. No finding is carried as UNVERIFIED.

That says the pipeline ran, not that coverage was total. The pass graded the specification a builder
would be handed, not an implementation — none exists yet — so every defect below is a defect in what
was written, and a spec that survives this audit is not thereby a mode that works.

## Review shape

Raw 38, confirmed 19, refuted 19, unverified 0, precision 0.50.

The 19 confirmed findings collapse to 14 distinct defects — 2 blocker, 7 high, 4 medium, 1 low —
and that distribution is what the integers beside this report report. Four folds, each of them two
or three sightings of one defect from different sections:

| Defect | Raw ids folded in |
|---|---|
| H1 the wall with no fallback, no override and no fixture | 3, 13, 20 |
| H2 the refusal specified against a loop that does not exist | 11, 22 |
| H3 the bound that is inert when `timeout` is absent, silently | 21, 32 |
| M4 the deleted arm that is still priced | 16, 34 |

Precision at 0.50 sits exactly on the floor `AGENTS.md` §8 names, up from round 1's 0.23, and the
reason is the change round 1 asked for: this pass required a `file:line` in the finding itself
rather than a section address in the spec. Every survivor below carries a path, a line, or an
arithmetic derivation from a tracked file. The refuted half is again almost entirely lenses reading
spec prose for rule-conformance. Keep the requirement; it is the filter.

One shape dominates again, but a different one. Round 1's recurring defect was the criterion that
cannot fail. Round 2's is the claim about the surrounding system that was never checked against the
file that decides it: B1, H1, H2, H3, H7 and L1 are all a spec asserting how existing code behaves,
and all six are wrong or incomplete against the source they cite. Six of fourteen, and every one of
them a single grep from being right.

## Findings

| # | Severity | Unit | Address | One line |
|---|---|---|---|---|
| B1 | blocker | 2 | §4 "The refusal that did not exist" vs §6 AC5 | The unbacked report is a blanket that exits before ranking; AC5 requires the serial row to still rank. |
| B2 | blocker | 1 | §4 "The hang bound", §2 S7, §6 AC9 | The run wall (10800 s) is below this population's largest per-suite bound (13600 s) and 19% above one suite's own reading. |
| H1 | high | 1 | §4 "The hang bound" and "Inventory", §6 AC9 | The wall rides the `--print-profile` probe §4 concedes fails in the fixture, with no override and no fallback declared. |
| H2 | high | 2 | §4 "The refusal that did not exist" | A `CONDS` match is what RANKS a row, and the lenient `measured` entry already matches the pooled spelling first. |
| H3 | high | 1 | §2 S7, §4 "The hang bound", §5 | `lib-selftest.sh` PROBES for `timeout` and runs unbounded without it; `run-gates.sh` already ships the announcement this needs. |
| H4 | high | 1 | §2 S3, §6 AC3 and AC6 | The composite width invariant is observed on the PRINTED pair; no criterion bounds the concurrency actually reached. |
| H5 | high | 3 | §2 S2, §6 AC2 and AC4 | S2 promises a before-and-after comparison; every criterion observes only the after-state. |
| H6 | high | 2 | §2 S1, §6 AC1 and AC5 | No criterion reads the tag the runner emits; AC5's fixture hand-types the spelling it then matches. |
| H7 | high | 3 | §4 "The fingerprint…", §3, §8 F1 | `git status --porcelain` reports untracked paths and hides ignored ones, so F1 is resolved against a property the command lacks. |
| M1 | medium | 1 | §4 "The pool", §5 observability | The verdict file is specified exhaustively and holds no output, so a pooled FAIL prints an exit code and no evidence. |
| M2 | medium | 1 | §2 S3, §6 AC3 | AC3's product clause and its override clause cannot both hold when `SELFTEST_OUTER_WIDTH` exceeds the resolved width. |
| M3 | medium | 3 | §2 S5, §6 AC5, §7 | AC5 conjoins a fixture that must not red with an observation that only exists when something reds. |
| M4 | medium | 3 | §5 perf/scale, against §2 S2 and §4 | The readiness checklist still prices the two directory listings rev-2 deleted. |
| L1 | low | 2 | §4 "The refusal that did not exist" | Three of the eleven `measured Ns` rows carry a width clause, not one. |

---

### B1 — blocker — unit 2 §4 "The refusal that did not exist" against §6 AC5, and `tools/run-gates/run-selftests.sh:120-129`

**The defect.** §4 routes a pooled-tagged budgets row "to the same unbacked report an unrecognised
condition takes". That report is not a per-row exclusion. `run-selftests.sh:120-129` prints the
unbacked names and raises `SystemExit(1)` with "NO share was computed" BEFORE any ranking output is
produced, so on that path the serial row is never printed at all. AC5 requires the run to "still
rank the serial row" and reds when "the refusal is a blanket that also drops the serial row".

The two cannot both hold. A builder following §4 reds AC5. A builder satisfying AC5 converts
`--rank`'s existing all-or-nothing refusal into a per-row exclusion — a behaviour change to a
shipped verb that §3 does not claim, that §5's migration line calls "additive", and that contradicts
the rationale written into the source itself, that a denominator missing its largest members is not
a majority of anything.

**Fix.** Decide it in §4, in one sentence, and make §6 and §5 agree with the decision. Either the
pooled row takes the existing blanket — it is named, NOTHING ranks, exit 1, and AC5 is reworded to
expect that — or S5 gains the per-row semantics explicitly, AC5 keeps its current wording, and §5
loses the word "additive" because the change is not.

**Left-shift.** The class is a spec whose §4 mechanism and §6 criterion were written against
different mental models of the same existing code. The cheap check belongs in the spec-audit
checklist and costs one grep: *where §4 says "the same X the existing code does", open X and read
what it does to the OTHER rows.* Where a fold changes an existing verb's semantics, the migration
line is the gate — "additive" is a claim, and a claim that the diff contradicts is exactly what a
reviewer can be asked for by name.

---

### B2 — blocker — unit 1 §4 "The hang bound" (the per-run bullet), §2 S7 and §6 AC9, against `tools/run-gates/gate-profiles.txt:66` and `tools/run-gates/selftest-budgets.txt:104`

**The defect.** The whole-run bound is taken from `--print-profile`'s `wall`. Node `a` resolves the
`capable` row, whose `wall=10800`. This population's largest declared budget is `unattended gate
selftest` at 13600 s, with a recorded reading of 9067 s. Two consequences, both bad:

- The per-suite bound for that row is `13600 x sweep-ceiling-factor`, which is at least 13600 and
  therefore can never fire — the run wall kills the sweep first, every time.
- The run wall sits 19% above that one suite's own QUIET-box reading, in a 59-row population summing
  55280 s. At outer width 8 the pool term alone is 6910 s on top of a 9067 s floor, on a box the
  budgets header itself says varies 5.5x median under contention.

So AC9's staged failing case is the ordinary case, and `--sweep` reds a healthy run. `gate-profiles.txt`
sized `wall=10800` against the BAR — 13644 s of leg-sum, longest leg 3837 s — a population whose
longest member is a third of this one's, and its own comment argues (`TOOL-dRetiredFork-40`) that a
bound firing on a healthy run is strictly worse than a loose one. §4's "both come from numbers that
already exist" took the number without checking that it covers this population.

**Fix.** State the relation the run bound must satisfy: `wall >= max(budget x sweep-ceiling-factor)`
over the resolved population. Then either declare the sweep's OWN wall in `selftest-budgets.txt`'s
header beside `sweep-ceiling-factor`, where the population that needs it lives, or make `--sweep`
REFUSE when the profile wall is below the largest derived per-suite bound. AC9 then stages its
breach against a fixture wall rather than against the profile's.

**Left-shift.** This one is genuinely gateable and should be a leg, not a checklist row: derive
`max(budget) x sweep-ceiling-factor` from `selftest-budgets.txt` and the resolved `wall` from
`gate-profiles.txt`, and RED when the wall is the smaller. It is a few lines of the same shell the
budgets file is already parsed with, it fires the day either number moves, and it is the
derive-don't-restate rule applied to two files that already disagree.

---

### H1 — high — unit 1 §4 "The hang bound" and "Inventory", §6 AC9 and §7 arm 3, against `tools/run-gates/run-selftests.test.sh:29-55` and `tools/run-gates/run-gates.sh:511-515`

*Folds raw 3, 13 and 20 — the unstageable fixture, the missing override, and the missing fallback
are three views of one hole.*

**The defect.** §4's "The width" paragraph concedes that `build_repo` copies only `run-selftests.sh`
into the fixture, so `bash run-gates.sh --print-profile` cannot resolve there, its stderr is
swallowed, and `W` falls back to the hard-coded 2. That is why rev-2 added `SELFTEST_OUTER_WIDTH` —
it is the fold of round 1's H1. The `wall` rides the SAME emission (`run-gates.sh:515` prints width,
timeout and wall on one line), and §4 gives it neither an override nor a fallback. The Inventory
lists `SELFTEST_OUTER_WIDTH`, `sweep-ceiling-factor`, `TIMEOUT`, `SWEEP_ROOT` and `_rs_waitn`, and no
wall knob. §4 then explicitly rejects staging `run-gates.sh` and `gate-profiles.txt` into the
fixture, closing the other route. `GATE_WALL` does not help: it feeds `run-gates.sh`'s own
resolution, which is the thing that failed.

Two harms. AC9 and §7's third arm ("a population whose wall is exceeded") cannot be staged in the
fixture this spec declares — an implementer could stub a profile printer, which §4's rejection does
not strictly forbid, so this half is the weaker one. The other half is not weak: in ANY tree where
that probe fails — an adopter, a scratch repo, a damaged profile table — the width quietly becomes 2
and the whole-run bound silently does not exist, while S7 states that the whole run is bounded. That
is green-by-absence in the half of S7 that exists to stop a hang suppressing all 59 verdict lines.

**Fix.** Give the wall exactly what §4 already gave the width, for the reason §4 already recorded.
Add a wall override to the Inventory beside `SELFTEST_OUTER_WIDTH`. State what the wall IS when the
profile line carries none — and make that a REFUSAL rather than an unbounded run, since an
unresolvable bound and a generous one are indistinguishable from the outside. Name the override in
AC9's fixture line, the way AC8 already names its budgets fixture.

**Left-shift.** Checklist row, phrased as a symmetry test: *when a fold adds an escape hatch for one
value read off a line, walk every other value read off that same line and give each the same
treatment or a stated reason.* The width and the wall arrive on one `--print-profile` line; the fold
that fixed one of them looked at the value, not the line. Cheap to apply, and it is the same
question round 1's H1 answered for the width.

---

### H2 — high — unit 2 §4 "The refusal that did not exist", against `tools/run-gates/run-selftests.sh:102-109`

*Folds raw 11 and 22 — the ordering error and the loop-shape error are one wrong reading of one
loop.*

**The defect.** §4 specifies the net as "`CONDS` gains a pattern matching the pooled tag that routes
the row to the same unbacked report". The reader is:

```
for rx, take in CONDS:
    m = rx.search(reading)
    if m:
        rows.append(...)
        break
else:
    unbacked.append(...)
```

Matching a `CONDS` pattern is precisely what makes a row RANKED. `unbacked` is the `for ... else`
fallthrough, reached only when NO pattern matched. So a pattern added to `CONDS` produces the
opposite of the outcome AC5 demands, and no `take` lambda routes out of that branch without changing
the loop the spec is describing.

It is wrong a second time in the same sentence. `CONDS` is first-match-wins and its second entry is
the lenient `measured (\d+)s (?:on )?(.+?)(?:,|$)`, which already matches §4's own worked example
`measured 42s pooled@8x1 on node a, x1.5`. An entry appended after it never fires at all. An
implementation following §4 literally therefore leaves the pooled row ranked as a `direct` reading —
the exact defect rev-2 added S5 to close — and AC5 reds with no diagnosis, because the spec says the
net was built. The paragraph opens by announcing that the net is BUILT rather than assumed, having
been the rev-2 correction of a rev-1 error about this same reader.

**Fix.** State the actual seam. Either a DENY list evaluated BEFORE the `CONDS` walk whose hit
appends to `unbacked`, or a sentinel return from `take` that the loop routes to `unbacked`. Say
explicitly that evaluation order relative to the `measured` entry is load-bearing, because that
entry already matches the pooled spelling. Add the red to AC5: *red when the pooled row still parses
under the `measured` pattern because the new check sits after it.*

**Left-shift.** Same checklist row as B1's, and this is its second instance in one document: *a §4
sentence naming an existing function, loop or table cites the `path:line` and quotes the branch it
claims to reach.* Round 1 made `file:line` a requirement for FINDINGS and precision doubled; the
same requirement on spec MECHANISM prose would have caught both halves of this before ratification.

---

### H3 — high — unit 1 §2 S7 and §4 "The hang bound", against `tools/lib/lib-selftest.sh:49,153` and `tools/run-gates/run-gates.sh:362-371,493-494,516`

*Folds raw 21 and 32 — the missing refusal and the missing liveness announcement are one hole with
two acceptable fixes.*

**The defect.** §4 cites `timeout -k` as "the same enforcement `lib-selftest.sh` uses per arm". That
harness PROBES: `_st_timeout=""; command -v timeout >/dev/null 2>&1 && _st_timeout=timeout`, and at
line 153 the bound is applied only `[ -n "$_st_timeout" ]`. Absent the binary, the arm runs
UNBOUNDED and nothing in the output says so. S7 states EVERY POOLED SUITE IS BOUNDED, in capitals,
and the spec declares no refusal, no announcement and no alternative for the absent-binary case. On
such a host every pooled suite runs unbounded and the sweep prints its width pair and its verdict
lines exactly as a bounded run does. AC8 observes the bounded path only, so the mode's central safety
claim is unfalsifiable anywhere `timeout` is missing.

This repo already decided this question and shipped the answer. `TOOL-aBoundedCeiling-1` S5 gave
`run-gates.sh` a `CEILINGS_LIVE` probe that RUNS `timeout -k 1s 10 true` rather than probing for the
binary (`:362-371`), prints "this host has no runnable `timeout -k`, so EVERY leg's declared ceiling
is INERT and every leg runs unbounded this run" (`:494`), and already emits `ceilings` on the very
`--print-profile` line `run-selftests.sh:203` parses for the width. The reuse §4 names inherits the
silent shape instead of the announced one. No non-goal withholds this; the `aBoundedVerdict-10`
non-goal concerns `run-gates.sh`'s per-leg deadline.

The asymmetry inside this build is the tell: unit 3 makes the fingerprint's liveness a scope item
(S3) and an acceptance criterion (AC3), while unit 1's S7 asserts a bound with no liveness at all,
over the mode that becomes the primary run path for 59 suites.

**Fix.** Either refuse `--sweep` when `timeout` will not run — the runner already refuses a missing
python the same way at line 32 — or take the shipped answer: add to S7 that the bound announces
itself INERT on stderr when `timeout` will not run, that suites still run rather than being skipped,
and cite `TOOL-aBoundedCeiling-1` S5 with the existing wording. Add an AC that stubs an unrunnable
`timeout` and observes the announcement, and put the refusal or the announcement on §5's
error-states line so the skip announces itself.

**Left-shift.** Gateable and worth gating, because the probe already exists: assert that
`--print-profile`'s `ceilings` value reaches the sweep's own output, and add a self-test arm that
shadows `timeout` with a non-executable stub and greps for the INERT announcement. That is the
charter's probe-liveness rule applied to the one bound this mode's safety rests on, and it is a
copy of a check this repo already passes elsewhere.

---

### H4 — high — unit 1 §2 S3 and §6 AC3 and AC6

**The defect.** S3 states the composite width invariant in capitals. AC3 grades the STRING the
runner prints: the pair is printed, its product is at most the resolved width, the override is
echoed. AC6 sets a LOWER bound on concurrency — at least two suites overlap — and no upper one. AC1,
AC2, AC4, AC5, AC7, AC8 and AC9 bound nothing about peak concurrency either.

So an implementation that prints `outer 8 · inner 1` and backgrounds all 59 suites at once passes
every criterion in §6. The invariant is observed by a print statement — the gate satisfied by its own
prose — and the harm is the one §4 itself names, that backgrounding 59 suites with no bound is
strictly worse than the serial loop.

**Fix.** Extend AC6, which already reads the verdict files' start and end stamps: derive the MAXIMUM
number of intervals overlapping at any instant and assert it is at most the printed outer width. Red
when the observed peak exceeds the declared outer, and red when it equals 1 at an outer above 1 —
the second half keeps AC6 from being satisfied by a serial run.

**Left-shift.** The evidence is already collected; only the assertion is missing, which is the
cheapest kind of left-shift there is. As a checklist row: *a capitalised invariant is observed by a
measurement of the thing it constrains, never by the run's report of its own intention.* Round 1's
B1 walk-through — take §6 as a set and imagine the laziest implementation that passes all of it —
finds this one in a minute, and it is the fourth instance of that shape across two rounds.

---

### H5 — high — unit 3 §2 S2 and §6 AC2 and AC4

**The defect.** S2 promises a before-and-after comparison. AC2 stages a write into a CLEAN fixture
tree; AC4 stages a CLEAN tree. Both are satisfied by a single after-read that reds on any non-empty
`git status --porcelain`. AC3 forces a pre-run liveness attempt but does not require that the BEFORE
value be retained or compared, so an implementation may probe, discard, and red on non-empty.

The design is buildable correctly — §4 pins two call sites and the Inventory names `_rs_fingerprint`
— but the criterion set cannot see the wrong build, and the wrong build reds on every developer tree
carrying an unrelated edit. That is the reds-on-innocent-runs failure mode §4 deleted the
git-common-dir arm to avoid, arriving through the front door. Same class as round 1's B1, which this
build has already folded once.

**Fix.** Add AC6: with a tracked file modified BEFORE the sweep starts and untouched by any suite,
`--sweep` does not red and its report names no path. Red when a pre-existing modification is reported
as sweep-caused, and red when the before-reading is never taken.

**Left-shift.** Checklist row, and it generalises past this build: *a differential instrument is
observed by an arm that stages the difference's LEFT side — a dirty before, a populated baseline, a
non-empty prior — because an arm that starts clean cannot tell a differential from a single reading.*
Mechanically, the same arm is the gate: dirty the fixture before the sweep and assert green.

---

### H6 — high — unit 2 §2 S1 and §6 AC1 and AC5

**The defect.** S1 says it is "Observed by AC1". AC1 observes only the row states `OVER` and
`withheld`; it never reads the tag the runner emits. Nor does anything else — AC2 counts withheld
rows, AC3 reads `git status`, AC4 reads `--help`. AC5 AUTHORS `pooled@<outer>x<inner>` into its own
fixture budgets file, so the emitter's spelling and the `CONDS` pattern's spelling are never compared
to each other.

If the runner prints `pooled 8x1`, or omits the tag entirely — which S4 arguably invites, since it
forbids writing it into any artifact — both criteria stay green and rev-2's whole refusal net catches
nothing a real paste would carry. The realistic path into a budgets file is a human pasting a printed
sweep reading, and the net is graded against a hand-typed string instead. Two answers to one
question, which is the class §4 of unit 1 selects for.

**Fix.** Amend AC1 to assert the emitted tag literally: a serial run's rows carry `serial`, a
`--sweep` run's carry `pooled@<outer>x<inner>` with the same pair unit 1's AC3 prints. Amend AC5's
fixture to build its pooled budgets row from a tag CAPTURED from a real sweep's output rather than a
typed literal.

**Left-shift.** Gateable directly, and the gate is the fix: the self-test arm captures the emitter's
output and feeds it to the reader, so emitter and reader are compared to each other rather than each
to a constant. As a checklist row: *when a producer and a consumer must agree on a spelling, no test
may contain that spelling as a literal on both sides.*

---

### H7 — high — unit 3 §4 "The fingerprint, and the arm that was dropped", with §2 S2 and §8 F1, against `tools/run-gates/run-gates.sh:1011-1032`

**The defect.** Two statements are false as written about the command the spec names. `git status
--porcelain` reports untracked-and-unignored paths as `??` BY DEFAULT, and reports ignored files only
under `--ignored`. So §4's "`git status --porcelain` over TRACKED paths" is not a property the
command has, and §3's justification for excluding untracked paths — that `.gitignore`d build output
would red every sweep — describes a behaviour the command does not exhibit. F1 is resolved against a
property that is not there.

The spec never names `-uno` / `--untracked-files=no` anywhere in the build folder, so an implementer
following §4 literally gets a fingerprint that reds when a suite leaves a NEW untracked artifact
during the sweep — the case §3 declares out of scope. That is a self-contradiction, not a detail a
non-goal withholds. (The impact is narrower than first stated: pre-existing untracked files appear in
BOTH readings of a differential and would not red. It is new ones that do.)

There is also an in-tree precedent for this exact predicate and it reached the opposite conclusion,
with its reason written down: `run-gates.sh:1011-1032` records that CLEAN means `git status
--porcelain` EMPTY, "untracked-and-unignored files included", and that the runner deliberately keeps
ONE porcelain walk because the status walk is the expensive part of startup at 2136 ms. §10's reuse
audit cites only `gate-fingerprint.sh` and never this. The sweep and the bar may end up disagreeing
about what a clean tree is, with nobody having noticed they were both answering it.

**Fix.** Name the exact invocation in §4 — `git status --porcelain --untracked-files=no`, or
porcelain plus an explicit `??` filter — and re-resolve F1 against what the command actually reports.
Cite the `run-gates.sh` precedent and add one sentence on why the sweep's answer differs from the
bar's, since they now differ deliberately rather than accidentally.

**Left-shift.** Checklist row: *a spec that names a command's behaviour names the FLAGS that produce
it, and the audit runs the command once.* This one costs `git status --porcelain --help` and thirty
seconds. Pair it with the reuse-audit rule §10 already carries — grep the tree for the predicate, not
just for the helper — which would have surfaced the `run-gates.sh` comment on the first pass.

---

### M1 — medium — unit 1 §4 "The pool" (verdict-file contents) and §5 observability, against `run-selftests.sh:~305` and `tools/lib/lib-selftest.sh:147-151`

**The defect.** The verdict file is enumerated exhaustively as "the suite's exit status, its start
stamp and its end stamp". §5's observability line lists one verdict line per suite, the width pair,
and the stamps. AC1 requires only "a verdict line for every suite". Meanwhile the existing serial
FAIL path prints up to four matched lines out of the captured `out=$(eval "$argv" 2>&1)`.

So a pooled FAIL row emits an exit code and no evidence, over a mode intended to run 59 suites, and
no non-goal withholds it — the seven listed cover porting, defaulting, sharding, streaming,
`aBoundedVerdict-10`, contended readings and pool safety. The carry-over is genuinely blocked, which
is why this needs a decision rather than an oversight fix: `lib-selftest.sh:147-151` records that
`out=$(timeout N cmd)` reads to EOF, so the bound applies to the verdict rather than the clock — 51.4
s against a 1 s bound. The serial capture cannot be reused under S7's `timeout -k`, and the spec
commissions no replacement.

**Fix.** Add the captured output FILE to the verdict-file contents in §4, and state that the pooled
FAIL row renders the same excerpt from it that the serial mode renders. Redirecting to a file rather
than capturing into a variable is also what makes the `timeout -k` bound apply to the clock instead
of to the verdict, so this fix and S7 want the same shape.

**Left-shift.** Checklist row: *when a new execution path replaces an existing one, diff the two
paths' OUTPUT, not just their verdicts — an excerpt, a warning line, or a summary silently dropped is
the ordinary way a port loses information.* As an arm: assert that a pooled FAIL row and a serial
FAIL row for the same suite carry the same excerpt lines.

---

### M2 — medium — unit 1 §2 S3 and §6 AC3, against `run-selftests.sh:205-217`

**The defect.** AC3 demands simultaneously that the printed product be "at most the resolved width"
and that `SELFTEST_OUTER_WIDTH` be "what the outer half reports". §4 says the override sets the outer
half directly, with no clamp. The inner half floors at 1 (`:217`), and in the declared fixture `W` is
the hard-coded 2 by §4's own admission. So any override above 2 makes the product exceed the resolved
width and reds AC3's product clause; clamping instead reds AC3's override clause. The spec decides
neither.

Not hypothetical: AC2 requires sweeping at two override values and AC6 at one above 1, with no bound
stated on what those values may be, and AC3's own red list invites staging a product that exceeds the
resolved width. S3 asserts the composite invariant is PRESERVED while the mechanism it specifies
provides an unclamped way to break it — the same `8x8=64` class the source comment at `:205-215`
records a prior spec audit catching.

**Fix.** One sentence in §4 "The width": an override above `W` either clamps to `W` and prints the
clamp, or REFUSES naming the resolved width. Mirror the choice in AC3's red list instead of leaving
both clauses absolute.

**Left-shift.** Checklist row: *an override introduced to make a value stageable is specified against
the invariant that value participates in — clamp, refuse, or exempt, stated.* An escape hatch added
for a fixture is still a code path in production.

---

### M3 — medium — unit 3 §2 S5, §6 AC5 and §7

**The defect.** AC5 conjoins two scenarios: a git-dir-write fixture asserted NOT to red, and "when
any suite reds, the summary NAMES the serial re-run". In the first fixture nothing reds, so the
second clause is vacuous there — and no arm stages a red suite to observe the re-run text. §7's two
new arms are the tracked-path write with stubbed git and the git-dir negative; §5's testing bullet
names a suite that writes into the checkout and one staging an unreadable fingerprint. None of them
reds. So S5 — the rev-2 answer to round 1's H3 — lands observed by nothing, and the arm that does run
goes green while the clause never fires. A skip that looks like a pass.

**Fix.** Split AC5. AC5a keeps the git-dir negative arm. AC5b asserts that the red produced by AC2's
tracked-write arm prints the serial re-run as the disambiguation step — and, if unit 1's TIMEOUT arm
also reds the sweep, that it does so there too. Put the assertion on §7's first arm rather than
adding a fourth.

**Left-shift.** Checklist row: *a criterion that conjoins a must-not-red fixture with an
observation that only exists on a red is two criteria, and the second one has no arm.* Mechanically:
any AC whose text contains both "does not red" and "when ... reds" is split at ratification.

---

### M4 — medium — unit 3 §5 production-readiness, perf/scale, against §2 S2 and §4

*Folds raw 16 and 34.*

**The defect.** §5 still prices the run as "two `git status` reads and two directory listings per
sweep". The listings were the git-common-dir arm, which rev-2 DELETED outright — §4 says "DELETED
rather than narrowed", S2 restates it as "One place, not two", §3 declares the residual gap a
non-goal, and AC5 pins it with a negative arm. Nothing else in rev-2's design lists a directory; the
private scratch is a `mktemp -d`. So a deleted instrument survives, priced, in the section an
implementer reads as scope. (A perf bullet prices rather than commissions, and the binding sections
are unambiguous, which is why this is medium and not high — but a builder pricing the work from §5
can re-add in good faith the listing AC5's negative arm exists to forbid.)

**Fix.** Cut "and two directory listings" from §5, leaving "two `git status` reads per sweep, not per
suite".

**Left-shift.** Checklist row, and it is the cheapest one in this report: *a rev that deletes a
mechanism greps the spec for the mechanism's name before ratifying.* Two rows in §5 and one grep for
"listing" would have caught it.

---

### L1 — low — unit 2 §4 "The refusal that did not exist", against `tools/run-gates/selftest-budgets.txt`

**The defect.** §4 states "eleven of the fifty-nine rows already use that spelling, one of them
already carrying a width clause". Eleven is right. Three carry a width clause, not one:
`extract-arms self-test` and `run-selftests self-test` at "inner width 4", and `line-length gate
selftest` at "its exported width 8". The spec inherited the single example from round 1's H5 finding
and restated it as a census, so the collision surface is understated threefold in the document that
ratifies the net built to handle it. The error understates in the direction of the spec's own
conclusion, so the argument survives — this is wrongness, not a broken design.

**Fix.** Correct the count to three and name them, or drop the sub-count and keep the eleven. The
argument does not need the smaller figure.

**Left-shift.** §7's existing rule already covers it — *no count of a derived population is written
in prose* — and the spec-audit application is: a figure a spec states about a tracked file is either
derived by a named command in the spec's own prose, or the audit re-derives it. This pass found it
with one `grep -cE "measured [0-9]+s"`.

---

## What a fix round owes

The two blockers are independent and neither is a rewrite. B1 is one sentence in unit 2's §4 choosing
between the two semantics, plus the matching edit to AC5 or to §5's "additive". B2 is one relation
stated in unit 1's §4 and a decision about where the sweep's wall is declared.

Six of the fourteen defects share a cause and it is not the one round 1 named. B1, H1, H2, H3, H7 and
L1 are all claims about existing code, made confidently, none checked against the file that decides
it — and H2 is the second consecutive round in which unit 2's §4 has been wrong about
`run-selftests.sh`'s `CONDS` loop while announcing that it had checked. Fixing them one at a time
will produce six edits and leave the habit. The cheaper move is the walk: take every sentence in a §4
that says how the surrounding system already behaves, open the file, and quote the branch. There are
not many of them, and this pass found all six that way.

The other cluster is round 1's, surviving in reduced form: H4, H5, H6 and M3 are the criterion that
cannot fail. Round 1 asked for a fix-round walk-through — take §6 as a set, imagine the laziest
implementation that satisfies every criterion, and ask what that implementation does — and the rev-2
edits closed the four instances round 1 named without running the walk again over the new criteria.
Run it once on the rev-3 set and these four fall out together.

Three defects deserve real gates rather than checklist rows, and all three are small: the
wall-versus-largest-budget arithmetic (B2), the `ceilings` liveness reaching the sweep's output (H3),
and the captured-tag round trip from emitter to reader (H6). Each fires the day the fact it guards
moves, which is more than any of the checklist rows can promise.
