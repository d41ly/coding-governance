**Serves:** spec-audit TOOL-aBatchedArm-4

# Tier-2 spec audit — TOOL-aBatchedArm-4, ROUND 1

*Adversarial pre-code pass over the unit that changes `tools/run-gates/run-selftests.sh`, the runner
that grades 61 kit self-test suites. A wrong change there reds every kit's self-test at once, so this
was run as the hardest audit of the build. Node `a`, 2026-09-13, ROUND 1. Every finding below
survived a skeptic prompted to REFUTE it, and every cited line was re-read in the tree by the author
of this report rather than transcribed from a lens. Each row carries its address inside the spec, the
fix, and the gate that would have caught it before a reviewer had to.*

**Reviewed subject, pinned at blob:**

- `memory/builds/aBatchedArm/spec/2026-09-13-spec-TOOL-aBatchedArm-4.md`@`5eac66f89c932feca2c79cfda88e81acde963c6b` — rev-1, NEW, never reviewed.

The three sibling units are NOT in scope. `TOOL-aBatchedArm-3` was audited in its own round 1
(BLOCKED, disposition FOLD, and its spec is still rev-1 as of this blob); `TOOL-aBatchedArm-1` and
`-2` went NON-CONVERGENT and are ordered behind it. Their rows are not re-graded here. Where a row
below names one of them, it is because THIS unit's declaration about that sibling is wrong, not
because the sibling is being reviewed.

## Verdict: BLOCKED

Eight rows at BLOCKER, eight at HIGH, five at MEDIUM, four at LOW. Those twenty-five rows collapse
to **twelve distinct defects**; the table below names which rows share one, so a fold that repairs a
defect repairs every row under it rather than twenty-five separately.

Three of the twelve are enough on their own. The unit's one guard against the pooled mode's recorded
failure — S5's factor — **cannot be calibrated as specced**: the run that sets it has no invocation
in the runner or the spec, and the factor's key, scope, base and derivation are stated four different
ways (D-1). Even calibrated, that factor is **the scalar-over-serial shape three ratified records
rejected**, and the tree already owns a different mechanism for a pooled hang bound (D-2). And S3
**wires the only standing consumer to `--serial`**, so after this unit lands no program in the tree
issues `--pooled`, and the build's 20-minute mandate is unreachable on any invocation that exists —
the exact shape the parked question and unit 3's audit B1 already named (D-3). This unit can land
with every acceptance criterion green and the mandate still failing.

## Review shape

- raw 44 · confirmed 25 · refuted 19 · unverified 0 · precision 0.57

Precision at 0.57 is above the ~0.5 floor `AGENTS.md` §8 sets for adding agents, so the lens fan was
scoped about right for this target. Read the confirmed count with the table below in hand: several
lenses hit the same seam independently (four rows on the five-versus-four arm count, five on the
factor), which the pipeline reports as zero duplicates because each row addresses a different section
of the spec.

## Run integrity

- lenses 4/4 returned, 0 DIED
- skeptic batches 5/5 returned, 0 DIED
- 0 contradictory verdict(s) demoted to unverified
- 0 spurious verdict(s) discarded
- 0 duplicate(s)

Nothing died. Every zero above is a measured zero and not an absence of evidence, so this round's
finding set is complete for the lenses that ran, and a fold may treat the UNVERIFIED bucket as
genuinely empty.

## The twelve defects, and which rows carry each

| Defect | Rows | Severity |
|---|---|---|
| D-1 · S5's factor cannot be calibrated as specced: no invocation takes the run, and its key, scope, base and derivation are four disagreeing statements | id=1, id=11, id=23, id=25, id=40 | blocker ×4 / high |
| D-2 · a scalar factor over a serial reading is the shape three records rejected; the tree's own pooled hang bound is ceiling evidence | id=35 | blocker |
| D-3 · S3 wires the only consumer to `--serial`; nothing issues `--pooled`, so the mandate is unreachable on every invocation that exists | id=37 | blocker |
| D-4 · the edges point the wrong way: `consumes-from none` while S5/AC6/AC7 rest on unit 3's rows, both at `order 1`, and the `hands-off` has no mirror so check 12 is RED | id=2, id=8, id=7 | blocker / blocker / high |
| D-5 · five bare-mode arms, not four, and the refusal's position against the liveness exit at `:383` is unpinned | id=3, id=38, id=14, id=26 | high |
| D-6 · `S6 before any shard row is staged` reds the install-prefix leg SLACK; the ban fires in both directions | id=4, id=9 | high |
| D-7 · S6's two counts are typed: 22 is off by one under the sibling's design, and the `run-selftests.sh` raise has no literal to justify it | id=17, id=29, id=30 | medium |
| D-8 · the pooled mode's two printed remedies and the usage line name the bare invocation S2 turns into exit 2 | id=27 | medium |
| D-9 · the everyday-command catalog teaches the bare invocation, and the manifest does not watch the runner | id=28 | medium |
| D-10 · §7 omits the unguarded `--check` leg that AC1 and AC3 are observed by | id=6, id=15 | low |
| D-11 · the caller count is two in §4/§5 and three in S3/F1 | id=20 | low |
| D-12 · Rollout defers S4 to unit 3 when the alias lands it with S2 | id=21 | low |

---

# BLOCKERS

## B1 · id=1 — AC6's precondition is forbidden by the spec's own rule, and F2's escape names no invocation

**Address:** section 2 S5 · section 8 F2 · section 5 error states · section 6 AC6.

AC6 opens "When the first pooled run of the eight shard rows completes". Section 5 says "a factor
that is absent or non-numeric refuses the pooled run rather than defaulting", and the runner does
exactly that today: `run-selftests.sh:420-425` exits 2 on an absent, non-numeric or zero
`sweep-ceiling-factor`. F2 answers "what factor before the first run" with "none", then says the
first run "is taken with the bound disabled and a wall bound only". No S item adds that knob. The
per-suite bound is `budget * SWEEP_FACTOR` at `:562`, handed to `timeout` at `:571`,
unconditionally; the run wall is DERIVED from the same product at `:459-467` and floored at
`SWEEP_LARGEST`, and `:476-482` REFUSES any `SELFTEST_WALL` below that floor. So "bound disabled,
wall only" has no path through the code: an absent factor refuses before a wall exists, a present
factor bounds every suite, and a huge factor makes the required wall meaningless. Section 3 hands
"the calibration run that measures S5's factor" to `TOOL-aBatchedArm-3`, whose spec never mentions a
factor.

The calibration run that sets the factor therefore cannot be started under the spec as written. AC6
is a criterion with no reachable observation. A builder invents the escape hatch — a flag, an env
knob, a temporary factor — and a reviewer cannot tell an invented one from the intended one.

Three further gaps compound it, each verified:

- **Which key.** S5: "re-declared from the 2" (the existing `sweep-ceiling-factor` line, present
  today at `selftest-budgets.txt:53`, so F2's "until the factor row exists" can never fire).
  Section 10: "one declared factor beside the one that exists" (a second header key).
- **Which rows.** "The shard rows" has no predicate anywhere in sections 2-6. `run_sweep_one` at
  `:556-563` applies ONE `SWEEP_FACTOR` to every row, so under a single key the other 53 rows keep
  running at the 2 that killed 14 of 58, and under two keys nothing says how the runner tells a
  shard row from any other.
- **Which base, which derivation.** The header says the factor is an integer because the derivation
  is shell arithmetic. S5 says "over the serial READING"; the code multiplies the BUDGET (`:562`),
  which is already reading × 1.5. No headroom and no width pair are named, so "a re-run at that
  factor kills no shard" passes or fails on noise.

**Fix.** Name in S5: the header key (new or re-valued); the row predicate it governs (for instance:
argv contains `--shard`, reusing S1's regex over the tokens); the base it multiplies (the budget, as
`:562` does, or the reading with the parser that implies); the derivation as an integer with stated
headroom (for instance `ceil(max observed / serial) + 1`) and the width pair and node recorded beside
it. Name in S2, or a new S7, the calibration invocation — for instance `--pooled --calibrate`, which
bounds each suite by the OLD factor rather than disabling the bound (see id=40), REFUSES without an
explicit `SELFTEST_WALL`, and prints per-row observed/serial ratios — and give it its own AC. Rewrite
AC6's red condition as an observation: "the second run at the written factor renders TIMEOUT for any
shard row".

**Left-shift gate.** Check 12's witness arm is armed (`SPEC_WITNESS_CUTOFF=2026-08-15`) and AC6
passes it on the strength of its backticked `figure:` and `cost:` labels — any backticked token
satisfies the arm. A witness on a `figure: DERIVED` criterion should have to spell the command that
derives it; had it, AC6 would have had to name an invocation the spec cannot name, which is this
defect at spec time rather than at the first calibration attempt.

## B2 · id=11 — four descriptions of one factor, none of them the same

**Address:** section 2 S5 · section 10 · section 8 F2 · section 5 error states.

Same seam as B1, kept as its own row because it addresses the internal contradiction rather than the
missing invocation. S5: "re-declared from the 2". Section 10: "one declared factor beside the one
that exists". F2: "the pooled mode REFUSES to run the shard rows until the factor row exists" — a
row-class-scoped factor needing a selector no section defines. Section 5: "a factor that is absent …
refuses the pooled run", while F2 says the first pooled run is taken "with the bound disabled and a
wall bound only". An implementer cannot tell whether the whole 61-row population's hang bound is
re-set from eight shard readings (which §4 itself says vary fifteen-fold across conditions), whether
shard rows get their own factor, or how the calibration run is invoked.

**Fix.** Collapse to one statement in S5: the key's name, its scope (all rows, or rows whose argv
carries `--shard`), what happens when it is absent, and the exact invocation of the calibration run.
Then add that invocation's refusal arm to §7 and align §5's error-states line with F2.

**Left-shift gate.** Same as B1. Documented check for the fold: every noun the spec introduces (here,
"the factor") is defined in exactly one S item, and every other mention points at it.

## B3 · id=23 — one factor or two, and no shard-row predicate

**Address:** section 2 S5 · section 8 F2 · section 10.

Two factors: the 50-odd non-shard rows stay at factor 2 under `--pooled`, which is exactly the shape
that killed 14 of 58 — and S2 makes `--pooled` a general flag over the whole population, with nothing
restricting it to `--kit tools/unattended`. One factor: a value measured on eight shard rows is
asserted as the hang bound for 53 rows it never observed. F2's "refuses to run the shard rows" needs
a shard-row predicate; `run_sweep_one` (`:556`) has none, and the non-goal that withholds a per-row
MODE column withholds neither the factor count nor a classification rule, so this is not a detail a
non-goal covers.

**Fix.** State it in S5: two factors; the shard predicate is S1's regex over the row's argv tokens,
reused; and a `--pooled` dispatch that would bound any row by the unmeasured 2 either refuses or
prints, per row, that its bound is the factor that killed 14 — pick one and add its arm to §7.

**Left-shift gate.** A `--check` assertion: every budget row's argv resolves to exactly one declared
hang-bound factor, printed with `--list`, so a row bounded by an unmeasured factor is visible on the
bar rather than at the kill.

## B4 · id=25 — "bound disabled and a wall bound only" is not expressible by the runner

**Address:** section 8 F2 · section 4 Files touched · section 7 · section 10.

Verified at source: `:420-425` exits 2 on an absent, non-numeric or zero factor; `:476-482` exits 2
on any wall below `SWEEP_LARGEST = budget × factor`. Both paths refuse the calibration shape F2
describes. Section 4's files list no calibration knob, §7 stages no arm for one, and §10 says
"nothing is invented". The implementer discovers this at the first calibration attempt.

**Fix.** Name the calibration entry — a `--calibrate` modifier on `--pooled`, or a declared spelling
for the shard factor that the runner accepts as "measure me" — add it to Files touched, and add a §7
arm that stages its refusal RED (calibrate without a wall, or with a factor row already present).

**Left-shift gate.** A spec-audit DoR check: every "When X completes" precondition in §6 names a
command that either the tree or an S item of this spec can issue. It is a reading check, not a gate;
the witness tightening in B1 is the gateable form.

## B5 · id=35 — S5 is the rejected design with a larger integer

**Address:** section 2 S5 · section 4 "Why a pooled cost verdict is withheld and not scaled" · section 6 AC6.

S5 keeps the pooled HANG bound as one scalar factor over the SERIAL reading — the existing
`sweep-ceiling-factor` shape at `run-selftests.sh:413-425` — calibrated from the first pooled run of
the eight shard rows only. Three records already rejected that shape and one already replaced it:

- `TOOL-dRetiredFork-40` (quoted by `tools/run-gates/ceiling-margin.txt:9`) rejected predicting a
  loaded reading from a quiet one by multiplying, having measured 443 s under load against 583 s
  quiet.
- `TOOL-aPooledSweep-2` §3 refused "a correction factor derived from one suite … applied to
  fifty-eight it was never measured on".
- The full-sweep record the spec itself cites
  (`memory/builds/aPooledSweep/build/2026-09-08-build-TOOL-aPooledSweep-1-the-full-sweep-and-what-it-refutes.md:102-103`)
  states the remedy as re-sizing the bound against POOLED rather than serial readings.
- The tree's existing mechanism for a pooled hang bound is `tools/run-gates/derive-ceilings.py`:
  worst OBSERVED reading under the condition, MONOTONE evidence, plus a declared margin of
  `max(floor, fraction × max)` from `ceiling-margin.txt`.

The spec's own §4 says dilation on this population is not a scalar (3 to 15x under the sweep) and
that "a number that cannot be predicted from the declared condition is a number a verdict must not
rest on". A TIMEOUT kill is such a verdict. Worse, the suites killed at factor 2 were the SMALL ones
(8 s → 121 s, 15x); eight long fork-bound shards of one suite will show a LOWER ratio, so a factor
read off them under-bounds exactly the members that died, and AC6 grades only shards. The design's
stated guard against the pooled mode's one recorded failure is the shape that recorded it, and no
non-goal withholds it: non-goal 1 covers cost verdicts, not the hang bound.

**Fix.** Reuse the ceiling-evidence shape instead of a factor: a per-row pooled reading carrying the
condition token the runner already composes (`pooled@<outer>x<inner>`, node, date), monotone, with
`ceiling-margin.txt`'s floor-plus-fraction as the headroom; a row with no pooled reading REFUSES the
pooled run or falls back to the declared factor, stated either way. If the factor stays, S5 must say
why it survives `dRetiredFork-40`, `aPooledSweep-2` §3 and the sweep record's stated remedy, and must
carry its width pair and node beside it — `TOOL-aQuenchedHarness-6` S3a: no reading without its
condition.

**Left-shift gate.** The spec's §10 lists the retrieval hits (`TOOL-aPooledSweep-1` through `-7`,
the full-sweep record) and says the fan "read each at source", yet designed the shape `-2` §3
refused. The check is therefore on DISPOSITION, not retrieval: every record id §10 cites carries one
of `REUSED`, `REFUSED-BY` or `NOT-THIS-SEAM`, and a design that reproduces a shape a cited record
refused reds the audit. Check 12 already grades §10 for the probe result; the disposition token is
the same predicate one token wider.

## B6 · id=37 — S3 pins the only consumer to `--serial`, and nothing in the tree issues `--pooled`

**Address:** section 2 S3 · section 4 "Why the mode is per invocation".

S3 makes `run-unattended-gates.sh:263` pass `--serial`. That is the only standing invocation of the
unattended rows: the tree's other two programs naming the runner are the DoD command
`.githooks/gate-env.sh:27` records, `run-unattended-gates.sh --selftests` (which delegates to that
line), and `gate-legs.json`'s `--check` leg (which executes nothing). After this unit lands, no program issues `--pooled`. The
build's own records already decided this is the blocker: `RUN.ABORTED.7742ee67.md` item 2 recorded
"the mode that would show 20 minutes grades no cost and the mode that grades cost gets no speed-up",
and unit 3's audit B1 demanded the criterion be restated "against the exact command an unattended
run issues". The spec's own §4 concedes that the 20-minute figure is unit 3 AC4's hand-run pooled
measurement on a frozen clone.

Once unit 3's eight rows land, the wired `--serial` path runs them one after another and pays seven
extra prologues, so the DoD verdict gets SLOWER, not faster. The owner ruling — "serial stays
possible when deliberately declared" — is pooled-primary in its framing; the spec inverts it for the
one consumer and wires no pooled path at all. Every AC can go green with the README target unmet on
any invocation that exists.

**Fix.** Say in S3 which invocation carries the build's goal and that the kit runner's `--selftests`
wall is unchanged; or give `run-unattended-gates.sh` a declared pooled path for the verdict, with the
serial cost pass named as its own invocation (the periodic serial sweep `TOOL-aQuenchedHarness-9`
already calls owed), and restate against that command.

**Left-shift gate.** The gate unit 3's audit B1 proposed is still owed and this round confirms it: a
leg asserting that every budget row whose argv carries `--shard` is invoked by at least one caller in
a pooled mode. Structural, cheap, and it reds the day a shard split is declared against a serial
consumer — which is the state this spec writes.

## B7 · id=2 — `consumes-from none` is false: AC6 and S5 rest on unit 3's rows

**Address:** section 3 Edges · section 6 AC6 · status header `order 1`.

AC6 ("the first pooled run of the eight shard rows"), AC7 ("when the eight shard rows are staged")
and S5 ("a value the first pooled run of the shard rows measures") all break without unit 3's S2
rows and its `SHARD_ARITY` raise. Section 3 assigns both to `TOOL-aBatchedArm-3` under `hands-off`
and declares `consumes-from none` — a declared absence that is false. TEMPLATE-SPEC §3 names this
the edge defect, "a criterion resting on something the unit does not build", and check 12 cannot see
it because it tests reciprocity only, so an edge declared in the wrong direction passes. Both specs
sit at `order 1`, so the README's derived build-order region reads "parallel: yes" for a pair where
this unit's AC6 is ungradeable until the other lands. The "one-off `--serial` pass of the eight rows"
that section 3 says produces the shard budgets is owned by neither unit.

**Fix.** Add `consumes-from TOOL-aBatchedArm-3` naming the eight rows, the arity raise and the
one-off serial pass, and assign that pass to one unit explicitly. Or split: keep in this unit only
what it can observe alone (the factor parser, the refusal when the key is absent, the calibration
invocation's own refusals) and move AC6's measurement into unit 3's AC set, so this unit's `order 1`
is honest.

**Left-shift gate.** Check 12, one arm wider: a unit id cited inside a §6 acceptance bullet that is
neither this unit's own nor in its `consumes-from` list reds. AC6 and AC7 do not spell the id, but
S5 and section 3 do, and the row-level predicate "an AC whose precondition names an artifact another
unit's S item builds" is a reading check the fold runs by hand.

## B8 · id=8 — the dependency is mutual, and one order value plus one `hands-off` cannot express it

**Address:** section 3 Edges · section 6 AC6, AC7 · section 2 S5 · status header `order 1` · section 4 Rollout.

Same edge defect as B7, plus the sequence point. Unit 3's rows carry `--shard i/8` tokens that the
glob at `:357-361` reds on the unguarded `--check` leg until this unit's S1 lands; this unit's
S5/AC6/AC7 cannot be observed until unit 3's rows land. §4 Rollout itself interleaves them — S1
first, S6 before the rows, S4/S5 with unit 3 — so the spec knows the sequence and the header denies
it. The build-order region derived from the headers says nothing true about the pair.

**Fix.** Either split — S1/S2/S3/S6 stay `order 1` with `hands-off TOOL-aBatchedArm-3`, and S4/S5
plus AC5–AC7 move to a follow-on unit at `order 2` declaring `consumes-from TOOL-aBatchedArm-3` — or
keep one unit and declare BOTH edges (`consumes-from` for the rows, `hands-off` for the regex and
mode), with both mirrors written into spec 3.

**Left-shift gate.** A `hands-off` names work the OTHER unit does after this one, so its target's
`order` must be strictly greater than this unit's. That is derivable from two status headers, which
the README's build-order region already parses; a `hands-off` at an equal or lower order reds.

---

# HIGH

## H1 · id=40 — the calibration run F2 describes is the unbounded-pool shape the runner's own record forbids

**Address:** section 8 F2 · section 2 S5.

Even once a calibration knob exists (B1, B4), "bound disabled" is not an acceptable spelling of it.
`TOOL-aPooledSweep-1` S7 makes every pooled suite being bounded a REQUIREMENT of the mode, and its F3
refuses a host without `timeout` for exactly this class — a mode whose stated property is silently
absent. Its F2 derives the run wall as the LARGEST per-suite bound, so with per-suite bounds absent
the wall has no derivation and the `:476-482` refusal compares against nothing. A run of eight
fork-bound shards with no per-suite bound is the one that most needs one.

**Fix.** State the calibration run's bounds: per suite, the budget times the OLD factor, or the
recorded serial reading times a declared calibration ceiling; for the run, an explicit
`SELFTEST_WALL` that is REQUIRED for the calibration pass and refused when unset. Never "disabled".

**Left-shift gate.** A §7 arm: the calibration invocation without `SELFTEST_WALL` exits 2, staged
RED first. Plus the existing `:420-425` refusal, which stays live and is the reason "disabled" must
not be a spelling.

## H2 · id=7 — the `hands-off` has no mirror in spec 3, and check 12 is RED on the committed spec set

**Address:** section 3 Edges · section 7 Gates.

`bash tools/memory-tree/check-memory-hygiene.sh` on this tree: exit 1, check 12 FAILED naming this
file — "§3 declares **hands-off** `TOOL-aBatchedArm-3` and that unit declares no matching
**consumes-from** `TOOL-aBatchedArm-4` back". Spec 3's Edges declare `consumes-from none`
(`2026-09-10-spec-TOOL-aBatchedArm-3.md:48`). §7 of this spec names `memory hygiene` as its own gate,
and that gate is red on the spec set as committed. Spec 3 already carries the same defect against
unit 1, so this adds a second row to an existing red rather than opening a new class; it is HIGH and
not BLOCKER for that reason and because the repair is one line.

**Fix.** Add the mirror edge to spec 3 §3 — `consumes-from TOOL-aBatchedArm-4`, the slash-tolerant
row checker and `--pooled`, without which its S2 rows red the `--check` bar leg — in the same commit,
and re-run check 12 NON-staged: the joins are HELD under `--staged`, so the pre-commit leg cannot see
this.

**Left-shift gate.** Exists and fired. What is missing is the habit: a spec that declares an edge
runs check 12 non-staged before it is committed, because the staged leg holds the join arms by
design.

## H3 · id=3 — five bare-mode arms, not four, and the refusal's position decides whether the fifth reds

**Address:** section 2 S2 · section 2 S3 · section 6 AC4.

Counted at source. `tools/run-gates/run-selftests.test.sh` invokes `$R` with no mode flag FIVE
times: lines 166, 170, 174, 179, 193. S3 and AC4 say four and enumerate only the strings of
170/174/179/193 (`self-tests GREEN|RED`, `OVER BUDGET`, the unresolved-row `FAIL` line). Line 166 is
`$R --kit tools/nowhere`, and its arm asserts exit 2 PLUS the substring "so this run graded NOTHING
at all" — the filter liveness refusal at `run-selftests.sh:383-386`. `lib-selftest`'s `arm` grades
rc AND substring, and both refusals exit 2, so only the message separates them.

S2 pins the mode refusal only as "AFTER the `--check` exit at `:322`", which leaves it anywhere in
`:363-390`. Placed after `--list` (`:374`) and before the liveness check (`:383`) — the natural
reading — line 166 prints the mode refusal instead, the substring misses, and the
`run-selftests self-test` leg reds. That leg is guarded on the very file this unit edits, so it runs
on every bar for this unit. AC4 reads green because it enumerates four.

**Fix.** Pin the refusal's position relative to the liveness check at `:383` in S2 — either AFTER
it (an empty filter refuses before a missing mode; line 166 is untouched, and S3 says so) or BEFORE
it (line 166 is the fifth caller and gets `--serial` in the same commit). Either way, S3 and AC4
count five, or four plus the reason the fifth is exempt.

**Left-shift gate.** The leg that reds is the left-shift; what is missing is naming the arm. AC4
should list the liveness arm's string beside the other four so the builder meets it in the spec and
not in the leg. Charter §7: no count of a derived population in prose — S3 should say "every arm
that invokes `$R` with no mode flag" and let the commit enumerate them.

## H4 · id=38 — the three counts in S3, AC4 and F1 all disagree with the tree

**Address:** section 2 S3 · section 6 AC4 · section 8 F1.

Same seam as H3, kept because it adds the third count: S3 says "four arms", AC4 "the four bare-mode
arms", F1 "exactly three" callers — none matches the tree, which has five no-mode arms in one test
file plus one program. The `--sweep` twin of the liveness arm sits at test line 238, so the
mode-independence of that refusal is already asserted by the suite; a mode refusal that precedes it
changes the suite's own claim about the runner.

**Fix.** Count five in S3 and AC4, add `--serial` to line 166 as well, and state in S2 where the
refusal sits relative to `:383` so AC2's "executes no suite" and the filter arm are both satisfied
by construction.

**Left-shift gate.** As H3.

## H5 · id=14 — the fifth arm's string is absent from AC4's red condition

**Address:** section 2 S3 · section 6 AC4.

If the refusal precedes the `:383` liveness exit, line 166 reds on its string and AC4's "any of the
four asserted strings changes" never sees it. Either AC2 is satisfied and `:166` reds, or `:166`
keeps passing because the refusal sits after the liveness exit and AC2 ("any invocation with no
mode flag exits 2 naming both") is violated for a `--kit` invocation that matches nothing. The
spec fixes neither.

**Fix.** Count five in S3, add the liveness string to AC4's list, or pin the refusal after `:383`
and say so in S2.

**Left-shift gate.** As H3.

## H6 · id=26 — the ordering that spares `:166` is itself a rule, and it is unstated

**Address:** section 2 S3 · section 6 AC4.

The `run-selftests self-test` leg carries `SELFTEST_FLOOR=43`; a mode refusal placed before the
liveness check reds one existing arm while the floor still reads as met by the arms added. If the
fold chooses "liveness refuses first", that is a rule — an empty filter is refused before a missing
mode — and S2 should say it, because it decides what AC2 means for a filtered invocation.

**Fix.** List all five lines in S3, or state in S2 that the mode refusal sits AFTER the filter
liveness refusal at `:383`, and say that this is an ordering rule rather than an accident.

**Left-shift gate.** As H3.

## H7 · id=4 — `S6 before any shard row is staged` reds the install-prefix leg, because the ban fires both ways

**Address:** section 2 S6 · section 4 Rollout · section 6 AC7.

`tools/check-install-prefix.sh:466` prints `SLACK <path> <pin> -> <measured>` and sets `bad++`
(exit 1) whenever a pinned count exceeds the measured one, and the measurement greps working-tree
content of tracked files. Pinning `selftest-budgets.txt` at 22 while the file still measures 14 is
red on every bar until the eight rows — unit 3's S2 — land. §4 Rollout's "S6 before any shard row is
staged" therefore cannot produce a green install-prefix leg at the S6 commit, and AC7's red condition
names only `ROSE`, so the verdict the builder actually meets is one the spec says cannot happen. The
`run-selftests.sh` raise has the same shape: it can only ride the commit that adds a literal, never
an earlier one.

**Fix.** Rewrite Rollout: each hand raise rides the commit that adds the literals it justifies —
`run-selftests.sh` with the S2/S3 commit if a literal is added at all (see M3), `selftest-budgets.txt`
with the commit that stages the eight rows, which is unit 3's, so record it on the edge. AC7's red
condition: "the leg reds `ROSE` or `SLACK`", and the count is DERIVED at landing, as the carried
row for `unattended-build.test.sh` already records.

**Left-shift gate.** Exists: the ratchet reds SLACK. What is missing is that its README and the
carried file's header state the rule a spec author needs — the ban fires in BOTH directions, so a
pin is raised only in the commit that adds the literal — and that AC7 name both verdicts.

## H8 · id=9 — AC7 observes the leg after the rows are staged, contradicting the rollout two sections earlier

**Address:** section 4 Rollout · section 6 AC7 · section 2 S6.

Same mechanism as H7, filed against the contradiction: AC7 grades the leg "when the eight shard rows
are staged", §4 says S6 lands "before any shard row is staged". Landing the 14 → 22 raise ahead of
the literals that justify it is a red bar, not a safe pre-step.

**Fix.** S6 lands in the SAME commit as unit 3's eight rows, or the same commit as any literal it
justifies, never before; state that the ban reds in both directions.

**Left-shift gate.** As H7.

---

# MEDIUM

## M1 · id=17 — 22 is off by one under the sibling's declared design

**Address:** section 2 S6 · section 6 AC7 · against `TOOL-aBatchedArm-3` S2.

Reproduced the checker's own regex over `selftest-budgets.txt`: 14 hits today, of which row 114
(`unattended gate selftest … bash tools/unattended/check-unattended.test.sh`) is exactly one.
`TOOL-aBatchedArm-3` S2 says "replace the single unsharded row with eight rows" and its AC3 says
"eight rows and not one", so the post-split count is 14 − 1 + 8 = 21. S6's 22 comes from the
"observed `ROSE 14 -> 15` with one row staged" — an ADD with the old row still present, which is not
the sibling's design. A pin at 22 against a measured 21 reds `SLACK` (`:466`), so AC7's "green with
the two raised counts" cannot be met at either number until one spec changes. Charter §7 also forbids
a derived count typed in prose.

**Fix.** Write the raise as "to the count the checker measures at the commit that stages the rows",
drop the 22 and the 15 observation, or reconcile with spec 3 on whether the unsharded row stays.

**Left-shift gate.** Charter §7 already states the rule. Documented check for the fold: an S item
that names `install-prefix-carried.txt` names the command that derives the count
(`bash tools/check-install-prefix.sh`), never the number.

## M2 · id=29 — the 22 presupposes the whole-suite row survives, which defeats the pooled floor

**Address:** section 2 S6 · section 6 AC7.

Same arithmetic as M1, with the consequence it hides: the typed 22 is only right if unit 3 KEEPS the
`unattended gate selftest` row (13600 s, the population's longest member) beside the eight shard
rows. Section 4 of this spec says "the whole-suite figure derived from the eight", so it does not
expect the row to survive. If it stays under `--kit tools/unattended`, the pooled wall is floored at
that member's own bound (`SWEEP_LARGEST`, `:467`) and the eight shards buy nothing toward the goal by
construction, independent of the spawn path. If it is retired, the count is 21 and 22 reds. The
finding's "a header reading naming the shard argv adds a 23rd literal" is speculative and is not
graded here.

**Fix.** State in S5/S6 whether the whole-suite row is retired when the shards land (it must be, for
the pooled floor to move), and replace the typed count with the rule — one literal per shard row,
minus one for the retired whole row — leaving the figure to the staging.

**Left-shift gate.** As M1. The pooled-floor half is caught by B6's gate: a shard row's whole-suite
sibling still invoked by a pooled caller reds.

## M3 · id=30 — the `run-selftests.sh` raise names no new literal

**Address:** section 2 S6.

Reproduced the epoch-2 predicate over `run-selftests.sh`: exactly six hits, at `:9`, `:42`, `:77`,
`:82`, `:199`, `:229`, matching the carried row. Every remedy the runner prints uses the derived
`$SELF` (`:29-33` explain that this exists precisely to stay under the ban), the existing refusal
shape at `:301-315` spells no path, and the usage line at `:77` is edited in place for
`--serial`/`--pooled` rather than duplicated. Nothing in S1-S5 or §5's `--help` item requires a new
literal. If the implementation follows the file's own discipline the count stays at 6 and a
hand-raised row reds `SLACK`; if it spells the path, the spec has not said which line or why
derivation is refused there.

**Fix.** Either name the line that will carry the new literal and the reason it cannot use `$SELF`,
or drop `run-selftests.sh` from S6 and keep only the `selftest-budgets.txt` raise.

**Left-shift gate.** As M1.

## M4 · id=27 — the pooled mode's own printed remedies name the invocation S2 refuses

**Address:** section 2 S2 · section 2 S4.

Verified at `:746` ("for a cost verdict, run the serial mode: bash $SELF") and `:757-758` ("Confirm
it with the serial re-run: bash $SELF"), plus the usage text's "(no flag) run the declared
population" at `:78`. All three name the bare invocation, which S2 turns into exit 2. The self-test
arms at `:251` and `:293` assert only the prefix strings, so nothing reds if the suffix is left stale,
and the spec — which otherwise names line numbers for every seam it touches and claims "no recorded
invocation breaks" — names neither remedy. Section 5's user-docs line covers `--help` only. The
pooled mode's own remedy, the one an operator is told to run after a pooled RED, would refuse when
followed.

**Fix.** Add both remedies and the usage line to S2's edit list (`bash $SELF --serial`), and add a
§7 arm that greps a pooled RED's remedy line for `--serial`.

**Left-shift gate.** A self-test arm over the runner's source: every `bash $SELF` the runner prints
is followed by a mode or a no-run verb (`--serial|--pooled|--check|--list|--rank`), so a remedy that
would refuse when followed reds at the suite rather than at the operator.

## M5 · id=28 — the everyday-command catalog teaches the bare invocation, and no ratchet watches the runner

**Address:** section 8 F1 · section 4 Files touched.

`memory/guides/SESSION-KICKOFF.md:132` is `bash tools/run-gates/run-selftests.sh` bare, in the
gate-command catalog every kickoff loads. The manifest's `watch:` line (`:6`) lists `run-gates.sh`
and `gate-legs.json` but not `run-selftests.sh`, so `manifest-check` cannot red on the stale line.
After this unit lands every session is handed a command that exits 2. Charter §1 DoD owes the
manifest edit plus a `last-audit` re-stamp when a gate command changes; Files touched names neither,
and F1's "exactly three" counts programs only.

**Fix.** Add `memory/guides/SESSION-KICKOFF.md` to §4 Files touched with the `--serial` spelling and
the re-stamp, and correct F1 to "three programs and one documented catalog line".

**Left-shift gate.** Add `tools/run-gates/run-selftests.sh` to the manifest's `watch:` line in this
unit. One token, and from then on any change to the runner reds the manifest ratchet until the
catalog line is re-audited.

---

# LOW

## L1 · id=6 — §7 omits the unguarded `--check` leg AC1 and AC3 are observed by

**Address:** section 7 Gates.

`tools/gate-legs.json` carries the unguarded repo leg `every held leg is budgeted, every budget row
resolves` (`bash tools/run-gates/run-selftests.sh --check`). S1 rewrites the predicate that leg runs,
S2's whole placement argument is about not redding it, AC1 is observed by it and AC3 names it. §7's
leg line — `memory hygiene · install-prefix (shipped surface) · run-selftests self-test · run-gates
canary` — omits it. Low because the leg is unguarded and runs regardless; real because §7 is defined
as the legs this unit must keep green.

**Fix.** Add `every held leg is budgeted, every budget row resolves` to §7 by its manifest name.

**Left-shift gate.** The spec-lint arm unit 3's audit M1 proposed and this round owes again: join
each §4 Files touched entry against `tools/gate-legs.json`, and every leg whose `guard` or `argv`
names a touched file must appear in §7. Derivable, so derive it.

## L2 · id=15 — the leg most at stake in the unit is the one its gates section does not name

**Address:** section 7 Gates · section 2 S1/S2 · section 6 AC1/AC3.

Same omission as L1, filed against the reading: a DoD that runs §7 runs everything except the leg
whose red is the reason S1 exists.

**Fix.** As L1.

**Left-shift gate.** As L1.

## L3 · id=20 — two callers in §4/§5, three in S3/F1

**Address:** section 2 S3 · section 4 "both callers declare" · section 5 migration · section 8 F1.

S3 reads "the three callers declare their mode" and lists two things; §4 says "both callers", §5
"the two callers", F1 "both callers are edited … and there are exactly three of them" in one
sentence. The tree has three programs naming the runner (`run-unattended-gates.sh`, the test file,
the `--check` leg) but the third takes no mode and is not edited. A reader of F1 looks for a third
edit that does not exist.

**Fix.** F1: "three programs invoke the runner; two invoke the run mode and both are edited". Fix S3
to match, and see M5 for the fourth site that is a document rather than a program.

**Left-shift gate.** None; a documented consistency check. State a count once.

## L4 · id=21 — S4 lands with S2 by construction, not with unit 3

**Address:** section 4 Rollout · section 2 S2/S4.

S2 makes `--pooled` an alias of `--sweep`. Every S4 behaviour AC5 observes already exists under
`--sweep` today: the serial loop alone grades budgets, the sweep withholds every verdict, counts
them (`:659-664`) and prints the count with the width pair (`:745`). Once S2's refusal lands, "cost
verdicts issued ONLY under `--serial`" is true by construction. The rollout's justification — "since
the factor is measured from its rows" — applies only to S5.

**Fix.** Rollout: "S4 lands with S2 by construction (the alias); only S4's header prose and S5 wait
for unit 3's rows".

**Left-shift gate.** None; a wording fix.

---

## What a fold should do first

Three decisions precede any redraft, and each is a scope call rather than a wording one.

1. **Whether the hang bound is a factor at all** (B5). If the fold reuses the ceiling-evidence
   shape, D-1's four contradictions dissolve with the factor — there is no key, scope or derivation
   to reconcile, only a per-row reading the runner already knows how to record. If the factor stays,
   B1 through B4 and H1 must each be answered in S5, and S5 must say why it survives three records.
2. **Which invocation carries the goal** (B6). The owner ruling was pooled-primary. Either
   `run-unattended-gates.sh` gets a declared pooled path and the serial cost pass becomes its own
   named invocation, or the spec states outright that the kit runner's wall is unchanged and the
   20-minute figure lives only in unit 3 AC4's hand-run. The second is honest; it also means this
   build does not reach the mandate on any wired path, and the README should say so.
3. **Whether this is one unit or two** (B7, B8). S1/S2/S3/S6 are observable alone and belong at
   `order 1`; S5 and AC6/AC7 are observable only after unit 3's rows exist. Splitting them is what
   makes the headers true and lets check 12's build-order region mean something.

After those, the mechanical set — five arms not four (H3–H6), the raise riding the literal (H7, H8,
M1–M3), the two remedy strings and the catalog line (M4, M5) — is a single pass over S2, S3, S6 and
§4 Rollout, each with a line number already in hand. H2's mirror edge is one line in spec 3 and
should land in the same commit as this spec's rev-2, with check 12 run non-staged before the commit.
