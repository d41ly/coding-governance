**Serves:** spec-audit TOOL-aBatchedArm-3

# Tier-2 spec audit — TOOL-aBatchedArm-3, ROUND 1

*Adversarial pre-code pass over the unit that now meets this build's goal. Node `a`, 2026-09-10,
ROUND 1. Every finding below survived a skeptic prompted to REFUTE it, and every cited line was
re-read in the tree by the author of this report rather than transcribed from a lens. Each row
carries its address inside the spec, the fix, and the gate that would have caught it before a
reviewer had to.*

**Reviewed subject, pinned at blob:**

- `memory/builds/aBatchedArm/spec/2026-09-10-spec-TOOL-aBatchedArm-3.md`@`58c6b0cf8ecab624bc3edd4880e017b1306879b2` — rev-1, NEW, never reviewed.

The two sibling units are NOT in scope here. `TOOL-aBatchedArm-1` (batching) and
`TOOL-aBatchedArm-2` (the group linter) were audited in rounds 1 and 2, went NON-CONVERGENT with
disposition FOLD, and are now ordered BEHIND this unit. Their findings are not re-reported and
their rows are not re-graded.

## Verdict: BLOCKED

Eight rows at BLOCKER, four at HIGH, two at MEDIUM. Those fourteen rows collapse to **nine distinct
defects**; the table below names which rows share one, so a fold that repairs a defect repairs every
row under it rather than fourteen separately.

Two of the nine are enough on their own. The unit's central scope item **cannot be written into the
declaration as specced** — the checker that reads `selftest-budgets.txt` treats `1/8` as a path and
reds the always-on bar leg eight times (D-2). And the consumer the mandate actually names runs those
rows **serially**, so eight rows buy zero wall clock on the only path the goal sentence is about
(D-1). Between them, this unit can land with every acceptance criterion green and the mandate — a
verdict in under 20 minutes for an unattended run — still failing.

## Review shape

- raw 45 · confirmed 14 · refuted 31 · unverified 0 · precision 0.31

Precision at 0.31 is below the ~0.5 floor `AGENTS.md` §8 sets for adding agents. Read as scope
signal, not as a defect count: the target is a 200-line pre-code spec over a 3200-line suite, so
lenses generated a large volume of plausible-but-refutable structural claims. The confirmed set is
dense in verified file:line evidence rather than in inference.

## Run integrity

- lenses 4/4 returned, 0 DIED
- skeptic batches 5/5 returned, 0 DIED
- 0 contradictory verdict(s) demoted to unverified
- 0 spurious verdict(s) discarded
- 0 duplicate(s)

Nothing died. Every zero above is a measured zero and not an absence of evidence, so this round's
finding set is complete for the lenses that ran, and a fold may treat the UNVERIFIED bucket as
genuinely empty.

## The nine defects, and which rows carry each

| Defect | Rows | Severity |
|---|---|---|
| D-1 · the consumer path is SERIAL, so the split buys nothing where the mandate is measured | id=2, id=27 | blocker |
| D-2 · `--shard i/n` cannot be written into `selftest-budgets.txt`; the `1/8` token reds the bar | id=11, id=25 | blocker |
| D-3 · cross-region state is carried in git REFS, not shell variables, and one boundary already needs a hand-written replay | id=24 | blocker |
| D-4 · the reuse audit was declined; four records that decide this unit's arity, budget and measurement are absent | id=35 | blocker |
| D-5 · the join predicate is manifest-scoped, so AC5 has no predicate that can satisfy it | id=26 | blocker |
| D-6 · controls that LOSE THEIR MEANING WITHOUT FAILING when split, which neither AC1 nor AC6 can see | id=36, id=28, id=5 | blocker / high / high |
| D-7 · `PROLOGUE_ARMS` is undeclared, its written value is wrong, and two counts are conflated | id=4, id=29 | high |
| D-8 · section 7 names no leg that grades either file the unit edits | id=19 | medium |
| D-9 · `run-unattended-gates.sh` is omitted from Files touched, and S2 falsifies the line section 4 cites as authority | id=20 | medium |

---

# BLOCKERS

## B1 · id=2 — AC4 names no runner MODE, and the mode the mandate names is serial

**Address:** section 6 AC4, with section 2 S2.

`tools/unattended/run-unattended-gates.sh:263` invokes `run-selftests.sh --kit tools/unattended`
with no flag. In that default mode `tools/run-gates/run-selftests.sh:296` sets `OUTER=1`, and
deliberately — its own comment says the loop is serial on purpose so each suite is graded against
its own declared budget without contention misattributing a breach. Only `--sweep` sets `OUTER=$W`
(line 298), and `--sweep` issues no cost verdict at all.

So eight rows in the default mode cost the unsharded time plus seven extra fixture prologues. AC4 as
written can go green with a longest shard of 18 minutes while an unattended run's verdict still takes
over two hours. That is the mandate failing with every criterion green.

The split does help `--sweep` — the pool floor drops from 9067 s, and the sweep hang bound derived
from the 13600 s row collapses. But the mode that would show the 20-minute figure grades no cost, and
the mode that grades cost gets no speed-up.

**Fix.** Add a section-2 item covering the consumer path: whether `run-unattended-gates.sh:263`
switches to `--sweep`, and what replaces the per-row cost verdict `--sweep` gives up. Restate AC4
against the exact command an unattended run issues — the wall clock of
`bash tools/unattended/run-unattended-gates.sh --selftests`, or of the named `run-selftests`
invocation — not against the longest shard in isolation.

**Left-shift gate.** A leg asserting that every suite whose declaration carries `--shard` is invoked
by at least one caller in a POOLED mode. Structural, cheap, and it reds the day a shard split is
declared against a serial consumer.

## B2 · id=27 — the only pooled mode issues no cost verdict, and stamps a condition `--rank` REFUSES

**Address:** section 6 AC4, and section 1's "the runner's pool executes concurrently".

Verified at `run-selftests.sh:283-298`: `OUTER=1` under the comment "THE OUTER POOL IS 1 IN THE
DEFAULT MODE, because that loop is serial on purpose: it grades each suite against its OWN declared
budget"; `OUTER=$W` only under `--sweep`, which by its own header answers "did any suite fail and
NOTHING about cost" and prints "$withheld cost verdict(s) WITHHELD". Nothing else executes this
population: `check-unattended.test.sh` has no `gate-legs.json` row, and `run-unattended-gates.sh`
delegates with a bare `--kit tools/unattended`.

So in every mode that grades a budget, the eight rows run one after another, buying zero wall clock
while paying the lines-55-298 prologue eight times. That is precisely the inertness section 4 says
this unit exists to avoid.

AC4's "recorded into `tools/run-gates/selftest-budgets.txt`" also collides with `run-selftests.sh:525`
`SWEEP_CONDITION="pooled@${OUTER}x${SELFTEST_INNER_WIDTH}"` and `:134` `REFUSED = [re.compile(r"pooled@")]`.
One unbacked row makes `--rank` print "NO share was computed" and exit 1 for the WHOLE population,
not just those rows. Mitigating: `--rank` and `--sweep` sit on no bar leg, so that half costs a verb
rather than the merge bar.

**Fix.** Name the mode in section 4 — state that the win exists only under `--sweep`, that `--sweep`
issues no cost verdict by design, and therefore where S2's eight budgets come from if not from the
pooled run. Rewrite AC4 to take its reading in a mode `--rank` accepts, or add a scope item for
teaching `--rank` a shard-shaped condition, plus an AC that `--rank` still exits 0 after the rows land.

**Left-shift gate.** Extend the existing `--check` direction with a third assertion: every budget row
whose recorded condition matches a `REFUSED` pattern reds at declaration time, rather than at the
next `--rank`.

## B3 · id=25 — the `1/8` token reds the always-on declaration leg, reproduced

**Address:** section 2 S2 and section 10 ("the declaration seam … eight rows need no format change").

`run-selftests.sh:357-361` is

```
for tok in $argv; do
  case "$tok" in
    */*) git ls-files --error-unmatch -- "$tok" >/dev/null 2>&1 \
           || { echo "run-selftests: row '$name' names '$tok', which git does not track" >&2; fails=1; } ;;
  esac
done
```

That unquoted `$argv` word-splits, so the token `1/8` matches `*/*` and git does not track it. I ran
the exact matcher over `bash tools/unattended/check-unattended.test.sh --shard 1/8` and it printed
the RED. All eight S2 rows fail.

That check IS the merge-bar leg `every held leg is budgeted, every budget row resolves`
(`tools/gate-legs.json`, argv `bash tools/run-gates/run-selftests.sh --check`, subject `repo`, **no
`guard` key**, so it runs on every bar). And `check-unattended.test.sh` has no manifest leg, so its
rows cannot dodge this by leaving argv empty.

The escape hatch is closed too: `check-unattended.test.sh:30-33` reads `[ "${1:-}" = --shard ]` with
the value as `$2`, so `--shard=1/8` takes the unrecognised-argument exit at line 33.

**Fix.** Add to S2 the change the row grammar actually needs — either narrow the token check in
`run-selftests.sh` to path-shaped tokens only, or change the shard value's spelling — and name that
file as a third touched file in section 4. Add an AC that `bash tools/run-gates/run-selftests.sh --check`
exits 0 with the eight rows present, staged and observed RED first.

**Left-shift gate.** The gate already exists and already reds; what is missing is the spec declaring
the file it must edit. The durable left-shift is an AC that runs `--check` as part of S2's own
acceptance, so the row format is proven writable before eight rows are written.

## B4 · id=11 — S2's central scope item cannot land without an undeclared change

**Address:** section 2 S2, against section 10's reuse audit.

Same defect as B3, filed independently and verified independently; kept as its own row because it
addresses section 10 rather than section 2. Section 10 says "the row grammar already carries a
per-row argv, so eight rows need no format change". That is true of the row GRAMMAR and false of the
CHECKER that reads it. The suite accepts only the `<i>/<n>` spelling
(`check-unattended.test.sh:40-42` refuses anything without a slash), so the eight rows cannot avoid
the token.

**Fix.** Restrict the `*/*` tracked-file case at `run-selftests.sh:~357-363` to tokens that are not
flag values, or spell the shard flag without a slash; name that file in section 4's Files touched.

**Left-shift gate.** A spec-audit leg that joins every path-shaped literal a spec's section 2 proposes
to write into a declaration against the checker that reads that declaration. Cheaper substitute: make
"run the declaration checker against the proposed rows" a DoR item for any unit that edits a
declaration file.

## B5 · id=24 — the existing seam already replays NON-variable cross-region state, by hand and by index literal

**Address:** section 4 · "Why the split is safe, measured rather than assumed".

`check-unattended.test.sh:1277-1293` opens region two with

```
if [ "$SH_I" = 2 ]; then
  git checkout -qf main && git merge -q --no-edit unit >/dev/null 2>&1
  git push -q -f origin main >/dev/null 2>&1
  git checkout -qf unit
fi
```

That is a compensation for git ref, branch and remote state that region one leaves, keyed on the
literal index `2`. Its own comment records the measured consequence of removing it: the merge becomes
a real one, it CONFLICTS on `memory/builds/tRun/RUN.md`, `>/dev/null 2>&1` swallows the conflict
whole, `--preflight` refuses on check 34, and THREE arms fail with none naming the cause.

So coupling between regions demonstrably exists, is carried in REFS rather than shell variables, and
fails silently-misattributed. Section 4's safety argument — "zero variables are assigned only inside
one `in_shard` region and read in another" — is measuring the wrong carrier, and the counterexample
sits at the same seam in the same file.

Eight regions means seven such boundaries, each needing its own replay derived by hand from whatever
the preceding seven leave. S1 describes the whole job as "re-cut the two `in_shard` regions into
eight" and section 10 calls the seam already-implemented, so nothing in the unit budgets for this.

**Fix.** Add a section-2 item for deriving a per-boundary replay — the `SH_I = 2` block generalised to
indices 2..8. Rewrite section 4's safety argument to state that the zero-variable measurement covers
shell state only, that ref/tree/remote state is the actual coupling channel, and that the existing
seam is the proof. Add an AC that each index's replay is observed FAILING when removed, mirroring the
recorded three-arm measurement.

**Left-shift gate.** Per-shard, assert the fixture's ancestry precondition directly at the top of each
region — `git merge-base --is-ancestor unit main` or its equivalent — so a shard deprived of a
predecessor's ref state REDS on a named precondition instead of on three unrelated waiver arms.

## B6 · id=26 — F1 resolves the join question against a surface that does not contain the subject

**Address:** section 6 AC5 and section 8 F1, with section 10's "join seam".

`run-gates.gov.test.sh:346-406` is `legs = json.load(open(legs_file))` and both directions iterate
only legs in that manifest: forward over legs whose `argv` array contains `--shard`, reverse over
`{t for l in legs for t in argv if t.endswith(".sh")}`. `check-unattended.test.sh` appears NOWHERE in
`tools/gate-legs.json` — grep returns zero hits, and the manifest contains zero occurrences of
`shard` today, the 2026-08-23 ruling having removed the `*.test.sh` legs. So the canary's predicate
never sees this suite, before or after the split.

`run-selftests.sh` has ZERO occurrences of `shard`, and its `--check` does only forward held-leg
coverage and reverse tracked-argv — no index completeness. Deleting one of eight shard rows passes
silently. **AC5 has no predicate that can satisfy it**, and F1's RESOLVED marks a question answered
against the wrong surface.

The two seams are also mutually exclusive: the manifest form wants `--shard` and `i/n` as separate
JSON array elements, and the declaration's token check rejects `i/n` (B3).

**Fix.** Reopen F1. State in section 4 that the gov canary's predicate is manifest-scoped and that
applying it to a TSV declaration is a PORT, not a reuse. Move S4 from "a shard-join assertion" to
"port the manifest-shaped join to the declaration's row format", and list
`run-gates.gov.test.sh` (or `run-selftests.sh`) in section 4's Files touched rather than the vague
"may touch `tools/run-gates/`".

**Left-shift gate.** Add index-completeness to `run-selftests.sh --check`: any script the declaration
calls with `--shard` must be called at every index 1..n, exactly once. That is the arm AC5 describes,
placed where the population actually lives, and it lands on the already-unguarded bar leg.

## B7 · id=36 — the suite already records the failure mode AC1 is offered against, and records that AC1's class cannot see it

**Address:** section 4 "Why the split is safe" and section 6 AC1.

Immediately below the `FLOOR_ASSERTIONS` block, `tools/unattended/check-unattended.test.sh` reads:

> TWO CONTROLS LOSE THEIR MEANING WITHOUT FAILING when this file is split, and they are named here
> because no gate sees it: a "the tree is still clean after N mutations" control is a control only if
> those N mutations ran in the same process. Split away from them it degrades into a duplicate of the
> opening control — still green, and no longer evidence.

The degraded control still executes and still increments `n`, so AC1's count identity holds
PRECISELY while the evidence is gone. Section 4's safety argument measures variable coupling only,
which cannot reach a control whose validity depends on N mutations having run in ONE process. Section
5 nonetheless offers AC1's union identity as the mitigation for exactly this risk class, and it is
not one. Going from arity 2 to arity 8 divides the surviving N again.

The live instance is at `:1505-1513` — "the tree is still clean after nine mutations", sitting in
region two with its nine mutations.

**Fix.** Cite the note in section 4. Add a scope item enumerating the accumulation-dependent controls
in the file and pinning each to a single shard with the mutations it counts (or re-arming it per
shard), and give it its own AC. Delete the section 5 sentence that hands this risk to AC1.

**Left-shift gate.** Give each such control a counter: it asserts the number of mutations observed in
ITS OWN process against the number its message claims, and REDS when they differ. That converts a
silent degradation into a named failure, which is the whole point of the note.

## B8 · id=35 — the reuse audit was declined, and four records that decide this unit are absent

**Address:** section 10 Reuse audit.

Section 10 asserts the `TOOL-aBatchedArm-1` probes "cover this unit's subject" and declines to re-run
them. That assertion is falsified: four records that bear directly on this unit appear nowhere in the
spec.

- **TOOL-aPacedTurnstile-8** (CLOSED, `memory/backlog/TOOL.md`) measured the crossover for THESE two
  suites: "TWO shards each is sufficient: past that the bar is throughput-bound at ~766s and further
  splitting buys exactly zero, so target that crossover and not a floor number." That is a measured
  ruling against arity, on the bar; the unit picks 8 without acknowledging it.
- **TOOL-aScannedThrottle-6** (OPEN) records 1.5-1.85x in-pool dilation and says in terms that it
  "belongs on any future sharding estimate — a shard measured alone will look cheaper than it lands".
  That lands squarely on AC4's "frozen clone on an idle box" measurement and on the ~6% headroom at
  9067/8.
- **TOOL-dNarrowedAnchor-3** (OPEN) records this exact suite's derived budget low by 2.6x — 1342 s
  extrapolated from a sharded pair against 3565 s measured end to end. That is the precise failure
  mode S2's eight per-shard budgets will reproduce if they are derived rather than observed.
- The suite's own post-floor shard contract note (B7's text), which no probe surfaced and which moves
  AC1.

Partial correction: section 8's F2 does cite an owner arity ruling of 2026-08-29, so "no record ruled
on arity" would overstate it. The dilation correction and the measured crossover are nonetheless
genuinely absent, and each moves an AC.

**Fix.** Re-run the probes with THIS unit's own terms — shard arity, crossover, throughput-bound,
dilation, budget derivation, whole-suite claim — and rewrite section 10 to name what they return and
what it changes. The subject here is sharding, not batching; a probe run for a different unit is not
a reuse audit for this one.

**Left-shift gate.** A spec-lint arm asserting that section 10's retrieval arguments contain at least
one term from the unit's own section-1 goal sentence. Mechanical, and it reds exactly the reuse where
the probe was inherited from a sibling with a different subject.

---

# HIGH

## H1 · id=29 — `PROLOGUE_ARMS` is undeclared, its written value is wrong, and the two counts differ

**Address:** section 6 AC1 and section 2 S3.

`PROLOGUE_ARMS` is a real constant only in the SIBLING driver suite
(`tools/unattended/unattended.test.sh:5447`, value 18). In `check-unattended.test.sh` it occurs
exactly once, at `:3153`, inside a comment asserting it is 0.

That assertion is false at HEAD. The C21 batched-join block sits AFTER `fi # ---- end REGION TWO`
(`:3114`) with no `in_shard` guard, and executes two `n=$((n+1))` arms unconditionally. So
sum-of-shards = unsharded + 2 today, and + 14 at arity 8. The file's own "84 + 146 = 230 EXACTLY …
PROLOGUE_ARMS is 0" partition claim no longer holds.

Worse for S3: the floor comparison `[ "$n" -ge "$FLOOR" ]` fires BEFORE those two increments, while
`PASS ($n assertions)` prints after. **The number a measurer reads off the PASS line is 2 higher than
the number the floor grades.** Against a ~3% headroom at roughly 37 arms per shard, 2 is about one
arm — so every per-shard floor taken from the PASS line is high enough to red on arrival.

**Fix.** Add to S3 the derivation and declaration of a real `PROLOGUE_ARMS` constant in this file
(currently 2, from the epilogue), correct the stale `:3153` comment, and state in section 4 which of
the two counts — floor-graded or PASS-printed — every reading in S3 and AC1 is taken from.

**Left-shift gate.** Move the floor check to the very end of the file, after every increment, so the
graded figure and the printed figure are the same number by construction. That deletes the class
rather than documenting it.

## H2 · id=4 — AC1's allowance cites a constant this suite does not declare

**Address:** section 6 AC1, with section 2 S1.

Same defect family as H1, filed against AC1 rather than S3. AC1 reads "equals the unsharded count,
allowing for the declared `PROLOGUE_ARMS`" — a criterion stated against an undeclared constant whose
only written value in this file is wrong. AC1 also does not say WHICH figure it reads, and the two
available figures differ by 2. An unstated allowance over an undeclared constant is a criterion that
can absorb any discrepancy.

AC1 is the spec's own named answer to section 5's residual-risk bullet, so this is not a wording
nitpick: the control either reds spuriously or absorbs the very thing it exists to catch.

**Fix.** S1 must add a real `PROLOGUE_ARMS` declaration derived from the arms outside both `in_shard`
regions, rather than asserted as 0. AC1 must name which printed figure it reads and state the
identity arithmetically: `sum(eight executed counts) == unsharded + (SHARD_ARITY - 1) * PROLOGUE_ARMS`,
red on any other value.

**Left-shift gate.** Have the suite PRINT the identity's three terms itself — executed, mode, and
prologue-arm count — so a union check is a comparison of printed numbers rather than an arithmetic
claim a reader has to reconstruct.

## H3 · id=28 — the split-induced degradation is invisible to BOTH a count identity and a FAIL-set identity

**Address:** section 5 risks ("which is what AC1's union identity is for") and section 6 AC1/AC6.

An arm that runs in the wrong shard still executes and still increments `n`, so AC1's sum is
unchanged. It stays green, so it appears in neither FAIL set and AC6 is unchanged. AC2 does not
rescue it either: an arm that goes vacuously green when deprived of state does not RED, and AC2's
break has to be staged by hand.

This is a documented case at the CURRENT arity of two. Seven more seams multiply it, and section 4
never names it.

**Fix.** Add to section 4 the class AC1 cannot see — an arm that executes and passes vacuously — and
either add an AC that identifies the affected controls by name and pins them into one shard together,
or record explicitly in section 5 that this class is uncovered and that the count identity is not a
substitute.

**Left-shift gate.** Same as B7: a per-control mutation counter. One mechanism closes B7, H3 and H4.

## H4 · id=5 — the variable scan structurally cannot see the coupling that matters here

**Address:** section 6 (no criterion) and section 4 "Why the split is safe".

`check-unattended.test.sh:3172-3175` states it in the file. The coupling is process-local tree state,
not a shell variable, so the measured ZERO cross-region variable coupling in section 4 is measuring
the wrong carrier for this class. AC1 counts assertions and sees no change; AC6 compares FAIL sets and
sees no change; AC2 grades a break that has to be staged by hand. Going from two regions to eight
multiplies the degradation by four with every criterion green.

**Fix.** Add a section-2 item enumerating these N-mutation controls BY LINE and pinning each into the
same shard as the mutations it counts, plus an AC that reds when a control's observed mutation count
inside its own shard is below the number it asserts — so a control separated from its mutations FAILS
instead of degrading.

**Left-shift gate.** As above. Additionally, a lint over the suite: any assertion whose message
contains a mutation count (`after N mutations`) must sit in the same `in_shard` region as N mutating
lines. Textual, cheap, and it reds on a mis-cut before the suite is ever run.

---

# MEDIUM

## M1 · id=19 — section 7 names no leg that grades either file the unit edits

**Address:** section 7 Gates, against section 2 S2 and S3.

None of section 7's four named legs grades either edited file. `unattended kit gate` runs
`check-unattended.sh` (the checker, not the suite). `testsuite counts self-test` runs
`tools/check-testsuite-counts.test.sh`, whose subject is a file this unit does not touch.
`run-gates canary` runs `run-gates.test.sh`, which contains no reference to `selftest-budgets` or
shards. `memory hygiene` is unrelated.

The omitted leg is `every held leg is budgeted, every budget row resolves`
(`tools/gate-legs.json`, argv `bash tools/run-gates/run-selftests.sh --check`, subject `repo`, no
`guard`) — the only leg over `selftest-budgets.txt`, which S2 rewrites, and it WILL red (B3). So the
implementer meets it at the lander rather than at the spec.

**Partially refuted, and the refutation is recorded rather than dropped.** The finding also named
`testsuite counts (every bar self-test prints one)` as a leg S3 would red.
`tools/check-testsuite-counts.sh:35` derives its population from `*.test.sh` strings in
`tools/gate-legs.json`, and `check-unattended.test.sh` appears nowhere in that manifest, so this suite
is outside that leg's population entirely. That half does not hold.

**Fix.** Replace `testsuite counts self-test` in section 7 with
`every held leg is budgeted, every budget row resolves`, and note in S3 that `FLOOR_ASSERTIONS` must
survive as a non-zero integer assignment that is still dereferenced.

**Left-shift gate.** A spec-lint arm joining each section-4 "Files touched" entry against
`tools/gate-legs.json` — every leg whose `guard` or `argv` names a touched file must appear in section
7. That is derivable, so it should be derived rather than typed.

## M2 · id=20 — the file section 4 cites as its authority is omitted from Files touched, and S2 falsifies it

**Address:** section 4 Files touched.

`tools/unattended/run-unattended-gates.sh:157-158` prints "The suites are run UNSHARDED on purpose …
so the whole-suite claim exists only here", and section 4 cites that exact line as the authority for
the arity constant being inert.

But that file DELEGATES its self-test half — lines 258-264,
`bash "$ROOT/tools/run-gates/run-selftests.sh" --kit tools/unattended`. Once S2 replaces the one
unsharded row with eight shard rows, this file runs the suite SHARDED, and the whole-suite claim
exists nowhere on demand. The cited sentence is falsified by the unit's own S2, the file is absent
from Files touched, and no scope item covers it. S4 addresses the semantic gap (a join) but not this
stale text; the same claim also sits in the suite's own shard-contract comment.

**Fix.** Add the file to Files touched, plus a scope item retargeting that paragraph — and the suite's
shard-contract note — at S4's join, so the whole-suite claim points at the mechanism that now carries
it.

**Left-shift gate.** The drift audit already owns this class. Add one probe: a file whose prose
asserts a property of a declaration it delegates to must be re-read when that declaration's rows for
its kit change. Cheaper interim: name `run-unattended-gates.sh` in S4's acceptance so the text is
edited in the same commit as the join.

---

## What a fold should do first

The two rows that decide whether this unit is buildable at all are B3/B4 (the declaration cannot hold
the rows) and B1/B2 (the consumer runs them serially). Both are answerable before any code: run
`run-selftests.sh --check` against a staged eight-row declaration, and decide what
`run-unattended-gates.sh` invokes. If the answer to the second is "`--sweep`", then the unit inherits
`--sweep`'s no-cost-verdict property and AC4 needs a new home for its measurement — which is a scope
change, not a wording fix.

B5 (seven hand-derived replays) and B8 (the measured crossover at two) between them raise a question
the fold should answer explicitly rather than by re-drafting: whether eight is still the right arity
once the per-boundary replay cost is priced against a record that measured further splitting buying
exactly zero on the bar. F2's owner ruling covers the arity; it does not cover the replay cost, which
this round is the first to price.
