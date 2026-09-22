**Serves:** spec-audit TOOL-aPooledSweep-1 TOOL-aPooledSweep-2 TOOL-aPooledSweep-3

# aPooledSweep — spec audit of the three-unit set, round 1

*Node `a`, 2026-09-07. A Tier-2 adversarial pass over the three specs of the pooled-sweep set: a
primed finder fan, a skeptic stage prompted to REFUTE every finding, one synthesis. Every claim a
surviving finding makes about the tree was re-checked against source before it was written down
here, and the re-check moved one finding's numbers — H7 below now names a figure neither spec
carries. Where a sub-claim did not survive, it is named inside the finding that carried it.*

**Round: 1.** Subjects, each pinned at the blob it was read at:

- `memory/builds/aPooledSweep/spec/2026-09-07-spec-TOOL-aPooledSweep-1.md@620f17e72114897d9b4cc4768c7acbdfe2c98be1`
- `memory/builds/aPooledSweep/spec/2026-09-07-spec-TOOL-aPooledSweep-2.md@22f9774d5bb19e083f184913e0c3603a3d79e53a`
- `memory/builds/aPooledSweep/spec/2026-09-07-spec-TOOL-aPooledSweep-3.md@e68b88e452a9187620a280ca1cf12f9b096adca0`

## Verdict: BLOCKED

Two blockers stand and they are independent. Unit 1's entire deliverable — concurrency, and a wall
clock that falls toward the longest suite — is observed by no acceptance criterion: all five of its
ACs pass unchanged against a `--sweep` that runs every suite serially and prints a width pair. And
the same unit backgrounds fifty-nine suites with no per-suite ceiling and no run wall, over a
population that contains a suite this repo has an OPEN row for hanging with zero output at 240 s,
while rendering every verdict only after the pool drains. One non-returning suite therefore
suppresses all fifty-nine verdict lines indefinitely, which is strictly worse than the serial mode
the flag is meant to improve on.

The design answer is not in dispute. A bounded outer pool is the right shape, withholding a cost
verdict from a contended clock is the right rule, and observing pool safety rather than asserting it
is the right instinct. What is wrong is downstream: the three units promise those properties in
their scope prose and then specify criteria that cannot fail if the properties are absent. Six of
the nine defects below are that one shape — the gate satisfied by its own prose — arriving in six
different places.

## Run integrity

Lenses 4/4 returned, 0 DIED. Skeptic batches 5/5 returned, 0 DIED. 0 contradictory verdicts demoted
to unverified, 0 spurious verdicts discarded, 0 duplicates. Nothing in this pass died, so the zero
counts below are evidence rather than silence, and the finding set is complete for the lenses that
were run. No finding is carried as UNVERIFIED.

That says the pipeline ran, not that the coverage was total. Two limits, so a green row is not
misread. The audit's subjects are the three specs as pinned above; the build README, the RUN.md and
the research record beside unit 1 were read for context but are not graded here. And the pass did
not attempt to review the unwritten implementation — every finding is a defect in the specification,
which is what a builder would be handed.

## Review shape

Raw 43, confirmed 10, refuted 33, unverified 0, precision 0.23.

The ten confirmed findings collapse to nine distinct defects: raw 7 and raw 23 are the same missing
observation seen from two sides, one at the acceptance criteria and one at the declared gate arms,
and they are folded into H4 at the higher of the two severities. The fold does not change any
severity count.

Precision at 0.23 is under half the ~0.5 floor `AGENTS.md` §8 sets before adding agents rather than
tightening scope, and the refuted set says why in the same way the last spec audit in this repo
found: lenses reading spec prose for rule-conformance produced almost every refutation, while lenses
required to check a spec's claim against a file in the tree produced almost every survivor. Every
finding below carries a path, a line or a derivation from the tree; that is not a coincidence, it is
the filter. The next pass over specs should require a `file:line` in the finding itself, not merely
a section address in the spec.

| Defect | Raw ids folded in |
|---|---|
| B1 the mode whose deliverable no criterion observes | 1 |
| B2 fifty-nine background suites and no hang bound | 36 |
| H1 the fixture that has no width to vary | 29 |
| H2 the fingerprint reads a directory other sessions write | 30 |
| H3 the nondeterminism an OPEN row already measured | 37 |
| H4 the git-dir arm that would land having only passed | 7, 23 |
| H5 the `--rank` refusal that does not refuse | 31 |
| H6 the exit-status half nothing runs | 2 |
| H7 one population, three numbers | 19 |

## Findings

| # | Severity | Unit | Address | One line |
|---|---|---|---|---|
| B1 | blocker | 1 | §2 S1 and all of §6 | Every AC passes against a serial `--sweep`; concurrency and wall clock are observed by nothing. |
| B2 | blocker | 1 | §2 (no S-line) and §4 "The pool" | No per-suite ceiling and no run wall, over a population holding a suite with an OPEN hang row. |
| H1 | high | 1 | §6 AC2 and AC3, against §7 | `run-selftests.sh` never reads `GATE_JOBS`, and the fixture has no width resolver, so both ACs are constant. |
| H2 | high | 3 | §2 S2 and §4 "The fingerprint" | The git common dir is shared by every worktree and the bar writes two files at its top level. |
| H3 | high | 3 | §2 (no S-line) and §5 risks | `TOOL-dSpentCeiling-8` measured two of these suites redding under load; no unit owns a pooled red. |
| H4 | high | 3 | §2 S2, §6 AC2, §7 | The git-dir arm of a two-armed fingerprint has no staged break and can be inert while §6 stays green. |
| H5 | high | 2 | §2 S5, observed by §6 AC3 | `--rank`'s second pattern accepts any condition text, so a pooled reading sorts as `direct`. |
| H6 | high | 1 | §2 S4, against §6 | S4 declares two halves and only the non-zero one is run; an always-failing sweep passes §6. |
| H7 | high | 1 and 3 | §8 F1 and §4, against 3's §4 | Two specs state 1 and 4 suites on the inner harness; the tree says 3, and F1's arithmetic rests on 1. |

---

### B1 — blocker — unit 1 §2 S1 and the whole of §6, with §1 and §5

**The defect.** S1 commissions "a bounded pool of concurrent suite processes" and §1 states the
purpose as a wall clock that "falls toward the longest suite". No acceptance criterion observes
either property. Walk §6 against an implementation of `--sweep` that resolves the population, runs
every suite one at a time exactly as the serial loop does, and prints a width pair before the first
verdict:

- AC1 wants a verdict line per suite and a non-zero exit over a population containing a failure. The
  serial impostor prints them and exits non-zero.
- AC2 wants two sweeps at two widths to be byte-identical "apart from the width pair and the elapsed
  figures". The impostor's stdouts are byte-identical, and the exclusion clause is doing the damage:
  the elapsed figures are the only place concurrency would have shown.
- AC3 wants the chosen pair printed and its product within the profile width. `1 x 1` satisfies it.
- AC4 wants an empty population to refuse. Unaffected by execution shape.
- AC5 wants the default mode unchanged. Unaffected, and best satisfied by changing nothing.

So the unit's whole deliverable can be absent and §6 is green in five places. §5's risk row makes
this sharper rather than softer: it names the `wait -n` collapse — the recorded trap where the pool
degenerates to a barrier while still printing a width — and asserts "AC3 observes the width and the
elapsed sum makes the collapse visible". No criterion reads the elapsed sum. The one failure mode
the author predicted is the one the criteria are blind to, and AC2's own wording excludes the figures
that would have caught it.

Nothing in §3 withholds this. The non-goals cover porting suites, concurrency-as-default, sharding,
and the two sibling units; none of them says the pool's concurrency is unobserved on purpose.

**Fix.** Add a criterion that observes overlap directly, and phrase it as a comparison rather than as
a threshold, since a threshold on a shared machine is a flake. Over a fixture population of N suites
that each sleep a known interval, at outer width W greater than 1: assert the sweep's wall clock is
below the sum of the per-suite elapsed figures by a stated margin, or assert that the start and end
stamps in two suites' verdict files overlap. Red when: wall clock equals the elapsed sum, which is
precisely the `wait -n` degeneration §5 names. Then narrow AC2's exclusion clause, so it excludes the
elapsed figures from the byte-comparison without excluding them from observation altogether.

**Left-shift.** The runnable half is the arm itself, in `tools/run-gates/run-selftests.test.sh`: a
sleeping fixture population whose wall clock is asserted against its own elapsed sum, staged red once
by forcing `_rs_waitn` to the no-`wait -n` path so the pool collapses and the arm is watched to fail
before it is trusted. The general half is a spec-audit checklist entry, because no gate can read
intent: *a unit whose goal is a performance property carries an AC that observes that property, not
only the side effects that would survive its absence — walk every AC against an implementation that
does nothing the goal asks for, and if the set stays green the set is the defect.*

---

### B2 — blocker — unit 1 §2 (no S-line) and §4 "The pool", against `tools/run-gates/selftest-budgets.txt` and `tools/gate-legs.json`

**The defect.** The spec adopts no hang bound of any kind, and three records already decided where
one lives.

`tools/run-gates/selftest-budgets.txt`'s own header says it in capitals: "A BUDGET IS A COST VERDICT,
NOT A HANG BOUND. The hang bound is the `ceiling` in `tools/gate-legs.json`". The manifest carries
one for every held leg — fifty-two of them, the largest at 13200 s. `run-gates.sh` additionally
carries a whole-run `wall` from `TOOL-aQuenchedHarness-1`, and it is already emitted on the
`--print-profile` line this spec's §4 calls for the width. So both bounds exist, both are declared
rather than guessed, and the mode that most needs them reads neither.

The population makes this concrete rather than theoretical. `TOOL-aBoundedVerdict-10` is OPEN and
records `unattended driver selftest` hanging inside its first `--preflight` with zero output at
240 s; that suite is a row in `selftest-budgets.txt`, so `--sweep` will run it. The row's own text
says the anchor half was fixed and "the PER-LEG DEADLINE half is not, and stays open here; it belongs
to `run-gates.sh`" — this unit's kit.

The design turns that from equal-to-serial into worse-than-serial. §4 renders verdicts "by builtin in
declaration order after the pool drains", so a single non-returning suite suppresses all fifty-nine
verdict lines indefinitely, with no partial output an operator could read. Unit 3's after-fingerprint
never runs either, so the sweep is also ungraded. In the serial mode an operator watches one suite
at a time and knows which one stopped. It also falsifies §5's perf row, which claims the mode "is
bounded above by the longest suite": with no ceiling it is bounded above by nothing.

**Fix.** Add an S-line that consumes the bounds that already exist rather than inventing one. For a
population row that is a manifest leg, take its `ceiling` from `tools/gate-legs.json`; for the six
rows that are not manifest legs — the `run-unattended-gates.sh` suites the 2026-08-23 ruling removed
from both manifests — declare one in the same act, since a row with no resolvable bound must red
rather than run unbounded. Take the run `wall` from the `--print-profile` output the spec already
reads. A breached suite is killed and rendered as a distinguishable state, not as a pass and not as
an ordinary `FAIL`. If the set genuinely wants to ship without this, then §3 gets a non-goal that
says so and names `TOOL-aBoundedVerdict-10` as the owner — but a new mode that makes an OPEN hang
worse should not ship silent about it.

**Left-shift.** A gate, and a cheap one, because both populations are already declared: a check that
every row of `tools/run-gates/selftest-budgets.txt` resolves to a hang bound — a `ceiling` in
`tools/gate-legs.json`, or a declared bound for a row that is not a held leg — and reds naming any
row that resolves to none. That is the same both-directions assertion the budgets header already
describes for the population itself, applied to the bound instead of to the cost, and it reds on the
next suite added without one rather than at 2 a.m. on a wedged bar. Beside it, an arm asserting that
a suite exceeding its bound is killed and reported, staged red first.

---

### H1 — high — unit 1 §6 AC2 and AC3, against §7's fixture arm and `tools/run-gates/run-selftests.test.sh`

**The defect.** AC2 varies the width "by running `bash tools/run-gates/run-selftests.sh --sweep`
under two values of `GATE_JOBS`". `run-selftests.sh` does not read `GATE_JOBS`. Its only mention of
the name is a comment at line 200 explaining that the knob lives inside `run-gates.sh`; the width
comes from line 203, `W=$(bash "$HERE/run-gates.sh" --print-profile 2>/dev/null | awk ...)`, with
`case "${W:-}" in ''|*[!0-9]*) W=2 ;; esac` immediately after.

In the real tree that indirection is correct and deliberate — the comment above it says
re-implementing the resolver here would be the two-spellings drift. In the fixture the arms actually
run in, it collapses. `run-selftests.test.sh`'s `build_repo` copies exactly one file into the scratch
repo, `cp "$RUNNER" tools/run-gates/run-selftests.sh`; there is no `run-gates.sh` there. The probe
therefore fails, its stderr is swallowed by the `2>/dev/null`, and `W` falls back to the hard-coded
2 for every arm regardless of the ambient `GATE_JOBS`.

So AC2's "two different widths" are one width. Its byte-identical stdout assertion passes for the
wrong reason and observes nothing about order-stability under a varying pool, which is the whole of
S2. And AC3's right-hand side — "the width `run-gates.sh --print-profile` reports" — has no producer
in that repo at all, so the criterion is comparing the printed pair against nothing.

This needs a spec decision rather than an implementer's guess, which is why it is here and not in a
build note: either the fixture grows a width source, or the sweep grows one.

**Fix.** State in §4 where the fixture gets a width, and name that source in AC2 and AC3. Two
options, and the spec should pick: stage `run-gates.sh` plus `tools/run-gates/gate-profiles.txt`
into `build_repo` so the real resolver answers in the fixture, which keeps one width resolver in the
product; or give `--sweep` an explicit outer-width variable it reads directly, which the spec's own
§4 "Alternatives rejected" argues against for the mode switch but not for the width. Whichever is
chosen, AC3's comparison needs a right-hand side that exists inside the fixture.

**Left-shift.** An arm that asserts the fixture's own precondition before the width-dependent arms
run: the fixture repo resolves a width greater than 1, and if it cannot, the arm announces itself as
skipped and names the missing resolver rather than passing. That is the announced-skip shape the
runner already uses for held legs, applied to a fixture capability. The checklist entry: *an AC that
varies behaviour through an environment knob names the file that READS that knob, and the reviewer
greps for it in the fixture the arm runs in, not only in the product.*

---

### H2 — high — unit 3 §2 S2 and §4 "The fingerprint", against `tools/run-gates/run-gates.sh`

**The defect.** The fingerprint's second arm is "a listing of `git rev-parse --git-common-dir` at one
level, names and sizes". That directory is not private to the sweep. It is shared by every worktree
of the repository, and this repo's own node registry and worktree conventions assume concurrent
sessions in sibling worktrees. Worse, the bar itself writes at exactly the level the listing reads:
`run-gates.sh` resolves `TS_COMMON` from `git rev-parse --git-common-dir` at line 537, and at lines
731-732 places `gate-bar-beacon` and `gate-bar-queue` at that directory's top level, the beacon
created when a run claims the turnstile and removed when it releases. In a primary tree,
`gate-ledger.tsv` and `gate-logs/` land there too, and git's own `index`, `logs/`, `refs/` and
`ORIG_HEAD` move whenever anything touches the repository.

So any other session running the bar in any worktree, at any point during a sweep, flips the listing
between the before and after readings. The sweep's floor is the longest suite and the population's
worst declared reading is 2547 s, so that window is tens of minutes wide. S4 then forbids the
refusal from naming a culprit, and the operator gets an unattributable RED for something the sweep
did not do. An instrument that reds on innocent runs is ignored within two sightings, and §4's own
claim for it — that it "is never wrong about the thing it claims" — is falsified.

Nothing withholds it: §3's non-goals are attribution, a budgets column, sandboxing and untracked
files, and §5's only recorded risk is an in-flight cleanup race, which is the opposite failure.

**Fix.** Make §4 name the volatile top-level entries the fingerprint EXCLUDES — at minimum
`gate-bar-beacon`, `gate-bar-queue`, `gate-ledger.tsv`, `gate-logs`, `index`, `logs`, `refs`,
`ORIG_HEAD` — or invert it and fingerprint only entries no sanctioned tool writes. Either way the
exclusion list is written down with the reason beside each entry, since an unexplained exclusion is
the next reader's mystery. And state the otherwise-idle-repository assumption as a declared
precondition rather than leaving it implied, so a red carries the right first question.

**Left-shift.** The negative arm, which is the one this class always lacks: during a fixture sweep,
touch `$(git rev-parse --git-common-dir)/gate-bar-beacon` and assert the sweep does NOT red. Run it
in the same suite as H4's positive arm, so the pair pins both edges of the predicate — one entry that
must red, one that must not. This repo's §7 rule about running a candidate predicate over the real
tree before wiring it applies directly: list the git common dir on a live checkout and read what is
actually in there before deciding what the fingerprint compares.

---

### H3 — high — unit 3 §2 (no S-line) and §5 risks, against `TOOL-dSpentCeiling-8`

**The defect.** The build's load-bearing rule is that concurrency is admissible for the SWEEP verdict
and inadmissible only for the COST verdict: unit 2 withholds the budget grading, and unit 1 S4 keeps
each suite's exit status feeding the sweep's. An OPEN backlog row says that rule is false for at
least two of these fifty-nine suites.

`TOOL-dSpentCeiling-8` records, in capitals, "THE FULL BAR IS NONDETERMINISTIC UNDER ITS OWN
CONCURRENCY, on at least two legs" — `run-gates turnstile` and `row-keyed merge driver replay` — and
carries the measurement: three runs of one merged tree, run 1 red on the turnstile leg, run 2 red on
the merge-driver leg, run 3 green 85/85, with no commit and no working-tree change between runs 2 and
3, both legs green standalone. Its conclusion is the part this set needs: "THE DEFECT IS THE ARMS,
not the mechanisms they guard: each reports a red that cannot distinguish 'the mechanism is broken'
from 'this machine was too busy'."

Both legs are rows in this population (`run-gates turnstile`, budget 3630; `row-keyed merge driver
replay`, budget 1620), and `run-gates.turnstile.test.sh` really does drive concurrent bars on TTLs of
2 and 3 seconds, so its arms are timing-sensitive by construction. A pooled sweep is the saturated
condition that row measured.

No unit owns the consequence. Unit 1 §5 routes cross-suite interference to unit 3. Unit 3 defines
soundness as write-confinement only and its instrument is a tree fingerprint, which is blind to a
suite that REDS under load rather than writing outside its scratch. Unit 3's four non-goals do not
cover it. Unit 2 withholds cost verdicts and explicitly not sweep verdicts. A grep of all three specs
for cross-suite, load, nondeterministic or flake returns nothing outside the cost-clock discussion.
So the sweep will emit load-sensitive reds that nobody can distinguish from real breaks, and the row
that predicted this is not cited anywhere in the set.

**Fix.** Cite `TOOL-dSpentCeiling-8` in unit 3 §3 or §5 and take one of two positions explicitly.
Either add an S-line for how a pooled red is to be READ — the row's own remedy is a `GATE_JOBS=1`
serial re-run, and the sweep can print that instruction in its RED line, which costs one string and
converts an ambiguous verdict into an actionable one. Or add a non-goal recording that load-sensitive
verdicts are out of scope and stay owned by that row, so the next reader knows the ambiguity was seen
rather than missed.

**Left-shift.** An arm asserting the sweep's RED line names the serial re-run as the disambiguation
step, which is cheap and pins the operator-facing half. The class-level entry belongs on the
spec-audit checklist rather than in a gate: *before a unit claims a property is observed, grep the
backlog for an OPEN row measuring that property's failure over the same population, and cite it or
say why it does not apply.* This whole finding is a backlog grep that no lens had to be clever to
run.

---

### H4 — high — unit 3 §2 S2 and §6 AC2, with §7's declared arms

*(Raw 7 and raw 23 folded: the same missing observation, raised once against the criteria and once
against the gate declaration. The §7 half was independently rated medium; the fold keeps the higher
severity, since a criterion and a gate arm that are both absent is the same hole seen twice.)*

**The defect.** S2 declares a two-armed fingerprint: "the tracked working tree AND the git common
dir, which are the two places a suite writing outside its scratch would land". §4 gives the second
arm the stronger justification — it is where "the runner's ledger, its logs and the lander marker
live", which is exactly where an escaping suite is most likely to write. Only the first arm is
observed.

AC2 stages a fixture suite writing into a tracked file. AC3 stages a stubbed `git` on `PATH`, which
makes BOTH arms fail indiscriminately and therefore demonstrates liveness, not that the git-dir arm
contributes to the comparison. AC4 asserts only that a clean sweep says the fingerprint matched, and
the §4 liveness rule requires the BEFORE reading to be non-empty in its git-dir arm — which an
implementation satisfies by listing the directory and then never diffing it. §7's declared new arms
are the same two: a fixture suite writing into a tracked path, and a stubbed `git`. So an
implementation whose git-dir arm is listed, non-empty, and never compared passes all four criteria
and both declared arms.

That is the shape `AGENTS.md` §7 names outright — a new gate is not landed until its failing case has
been observed, and gate the class rather than the instance. The git-dir half would land having only
ever been watched pass, and a predicate error confined to it (wrong directory resolution, wrong
listing depth, a comparison that comes out equal because it compares nothing) is undetectable by the
declared set. Staging the break is one file write under `$(git rev-parse --git-common-dir)`.

**Fix.** Add a criterion mirroring AC2 for the metadata arm, and a third arm to §7: a fixture suite
writes a file into `$(git rev-parse --git-common-dir)`, and the sweep REDS after the pool drains,
naming that entry and stating the sweep is unsound without naming a culprit. Red when: the sweep
exits 0 over a dirtied git dir. Pair it with H2's negative arm so the two together pin the
predicate's edges rather than only its positive side.

**Left-shift.** The arm above is itself the left-shift, and it belongs in
`tools/run-gates/run-selftests.test.sh` beside AC2's. The class entry for the spec-audit checklist:
*an S-line declaring a predicate over N places owes N staged breaks, one per place, and a liveness
arm that fails all of them at once counts as zero of the N.* That is a rule a reviewer can apply
mechanically to any multi-armed check, and it is the rule this repo's own
`tools/run-gates/run-selftests.test.sh` header was written to pay off.

---

### H5 — high — unit 2 §2 S5, observed by §6 AC3, against `tools/run-gates/run-selftests.sh:80-81`

**The defect.** S5 asserts a safety net: "the condition string a pooled reading carries is one
`--rank` already refuses, so a pooled reading that reached the budgets file would red the ranking
rather than be silently sorted against serial ones." The ranking refuses no such thing.

`--rank`'s condition vocabulary is two regexes, and the second is
`measured (\d+)s (?:on )?(.+?)(?:,|$)`, whose second group accepts any text up to a comma or the end
of the line. Run against the tag S1 composes: `measured 42s pooled@8x1 on node a, x1.5` matches,
yields `('42', 'pooled@8x1 on node a')`, and ranks as a `direct` reading. Move the tag —
`measured 42s on node a pooled@8x1, x1.5` — and it matches too. The vocabulary is closed on the two
reading SHAPES, not on the condition text after the seconds, and the comment above it
("a phrasing not listed here is not ranked leniently; it is reported as unbacked") describes the
shapes, which is a narrower promise than S5 reads into it.

The house style makes this the likely spelling rather than a contrived one: eleven of the fifty-nine
rows in `tools/run-gates/selftest-budgets.txt` already read `measured Ns on node a ...`, one of them
already carrying a width clause ("at its exported width 8"). So a pooled reading written the way
every other row in that file is written sorts silently against serial ones — which is precisely the
ranking-the-conditions defect the closed vocabulary was built to prevent.

AC3 does not catch it. AC3 asserts `git status --porcelain` over the budgets file is empty after a
pooled run, which observes that unit 2 writes nothing. It never observes what `--rank` would do with
a pooled row that arrived by any other hand, which is the only scenario S5's net exists for.

**Fix.** Make the refusal real rather than assumed. Either add the pooled tag to `CONDS` as an
explicitly REFUSED condition, so a matching row is reported unbacked by name; or state in §4 that the
tag must be spelled so no `CONDS` pattern can match it, and say which character makes that true.
Then give AC3 a second arm that stages a pooled-style reading into a fixture budgets file and asserts
`--rank` refuses it and computes no share from it.

**Left-shift.** That arm is the gate, and it is worth staging both ways: the pooled row is refused,
and an ordinary serial row beside it still ranks, so the refusal is not a blanket. The general rule
for the checklist: *a spec that leans on an existing tool's refusal quotes the predicate that
refuses and runs one example through it — a refusal asserted from a comment is an assumption with a
citation, not a check.*

---

### H6 — high — unit 1 §2 S4, against §6

**The defect.** S4 is two claims joined by a comma: the run's exit status is "non-zero when any suite
failed, zero when none did". It cites AC1 and AC4 as observing both. Neither observes the second.

AC1 sweeps a fixture population that includes a suite exiting non-zero, so its expected exit is
non-zero. AC2 re-sweeps that same population. AC4 stages a `--kit` filter matching nothing, which
refuses and exits non-zero. AC3 asserts only the printed width pair; AC5 is about the default mode.
§7's fixture note — "one suite that exits non-zero and one that exits zero, swept" — still describes
a single run whose expected exit is non-zero, because it contains the failing suite.

So no criterion runs an all-passing sweep. A `--sweep` that always exits non-zero satisfies every
criterion in §6, and the failure surfaces later as a mode nobody can use: at the push boundary, as a
permanently red bar that no arm attributes to this unit. The cited observation coverage is
demonstrably wrong for half a scope item, which is the same defect as B1 at smaller scale.

**Fix.** Extend AC1 or add a criterion: over a fixture population where every suite exits zero,
`--sweep` prints no `FAIL` line and exits 0. Red when: an all-green sweep exits non-zero. That is one
more fixture population and one more arm, and it makes S4's second half a claim someone has seen
fail.

**Left-shift.** The arm, in `run-selftests.test.sh`, staged red once by forcing the sweep's exit
expression to a constant. The checklist entry, which would have caught this by reading alone: *an
S-line stating two outcomes cites an AC per outcome, and the reviewer checks that the cited ACs
differ in the outcome they expect — two criteria expecting the same exit status observe one half
twice.*

---

### H7 — high — unit 1 §8 F1 and §4 "The width", against unit 3 §4 "The private scratch"

**The defect.** F1 resolves the width split — outer `W`, inner 1 — on an arithmetic claim: "The
population is 59 suites and exactly one of them is on the inner harness, so inner width buys
parallelism for 1/59th of the work while outer width buys it for all of it." Unit 3 §4 states, of the
same population and the same harness, that "four of those run on `tools/lib/lib-selftest.sh`".

Both are wrong. Derived over the tree — every tracked `tools/**.test.sh` that sources the harness at
top level — the suites that actually run on `tools/lib/lib-selftest.sh` are three:
`tools/check-line-length.test.sh` (`line-length gate selftest`), `tools/lib/extract-arms.test.sh`
(`extract-arms self-test`) and `tools/run-gates/run-selftests.test.sh` (`run-selftests self-test`).
`tools/lib/lib-selftest.test.sh` does not source it — it tests it as a subject — and
`tools/check-testsuite-counts.test.sh` only writes the harness spelling inside fixture strings, which
is why a naive grep for the filename returns five and both spec figures are off in opposite
directions.

So a resolved fork rests on a number no record in the set gets right, and the two sub-specs
contradict each other about it. The resolution itself probably survives — three of fifty-nine is
still a small enough share that outer width is where the parallelism is — but "probably survives" is
not what a RESOLVED fork is supposed to mean, and the next reader cannot tell which figure was
measured and which was remembered.

Unit 1 §4 compounds it in the same paragraph: "the population is 59 suites and one ported suite"
reads as sixty, when the ported suite is one of the fifty-nine. `tools/run-gates/selftest-budgets.txt`
holds exactly 59 non-comment rows.

**Fix.** Derive the figure once, name the derivation command in the spec, and cite the same number in
both sub-specs. Restate F1's arithmetic against it — three of fifty-nine, not one — and confirm the
resolution still holds at that share, in one sentence, rather than leaving the reader to redo it.
Fix §4's phrasing so the population size is one number.

**Left-shift.** Derive rather than restate, which is the rule the specs are breaking here: the count
comes from a command in the spec's own prose, not a literal — the population size from
`bash tools/run-gates/run-selftests.sh --list`, the harness share from a grep for the top-level
source line. Where a literal must appear because a fork's arithmetic needs it, the spec-audit
checklist entry applies: *a figure cited by two records of one build is derived once, the derivation
is named, and the audit greps the set for a second spelling of the same figure* — this pass found it
by grepping both specs for "59" and reading what followed.

---

## What a fix round owes

The two blockers are independent and neither is a rewrite. B1 is one criterion plus a narrowing of
AC2's exclusion clause. B2 is an S-line consuming two bounds that already exist in the tree, or a
non-goal that says out loud what is being deferred and to whom.

Six of the nine defects are the criterion-that-cannot-fail shape, and they cluster: B1, H1, H4 and H6
are all "the property is claimed and nothing would fail if it were absent". A fix round that fixes
them one at a time will produce four edits and miss the fifth instance; the cheaper move is the
walk-through — take each unit's §6 as a set, imagine the laziest implementation that satisfies every
criterion, and ask what that implementation actually does. That exercise is what produced B1, and it
would have produced the other three for free.

H2, H3 and H5 are a different class and share one cause: three claims about how the surrounding
system behaves — that the git common dir is quiet, that a suite's red means the suite is broken, that
`--rank` refuses an unlisted condition — none of which was checked against the file that decides it.
Each is a single grep away, and each is currently written as though it had been done.
