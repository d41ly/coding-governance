**Serves:** spec-audit TOOL-aUnblockedFleet-1 TOOL-aUnblockedFleet-2 TOOL-aUnblockedFleet-3 TOOL-aUnblockedFleet-4 TOOL-aUnblockedFleet-5

# Design review — aUnblockedFleet's five specs, read as designs

*Tier-2 adversarial pass over the spec set only. No code was changed. Every code claim below was
re-verified against the working tree at base `117de044` before this report was written.*

**Reviewed subjects, each pinned at the blob it was read at:**

- `memory/builds/aUnblockedFleet/spec/2026-08-31-spec-TOOL-aUnblockedFleet-1.md@ae6ec7dee42ee0e6ccc87edb18bce6126e8745ff`
- `memory/builds/aUnblockedFleet/spec/2026-08-31-spec-TOOL-aUnblockedFleet-2.md@63ad3b104cd3a7bcd9941895b3b74630343285a0`
- `memory/builds/aUnblockedFleet/spec/2026-08-31-spec-TOOL-aUnblockedFleet-3.md@526385ee1afe242bdae6c58e0985df487dd6c75e`
- `memory/builds/aUnblockedFleet/spec/2026-08-31-spec-TOOL-aUnblockedFleet-4.md@9bede106160aebbd5b2f3fa31c0bdc613b926bac`
- `memory/builds/aUnblockedFleet/spec/2026-08-31-spec-TOOL-aUnblockedFleet-5.md@4174bf6146578b5a310633cb97b980cfe4c4b32b`

**ROUND: 1.**

## Verdict: BLOCKED

Three blockers, seven highs, one medium, one low — twelve distinct defects after dedupe, from
sixteen confirmed raw findings. The build's central argument survives: the tree-wide singularity rule
really does protect a consumer that does not exist, and the by-construction measurement in unit 1 §4
is the right way to have established that. What is blocked is the *set*, not the thesis.

The headline is one sentence. **The build removes a wedge at the preflight layer and leaves an
identical wedge one layer down, unnamed.** `run-gates.sh` holds a repo-wide turnstile keyed on the
git common dir, so two concurrent `--close` calls in one clone serialize their merge bars — and the
queue wait sits *inside* the run's declared `GATE_BOUND`. Unit 1 §5 asserts the lander-marker race is
"the one real concurrency hazard admitted by this change". It is not, and the second one lands on the
case unit 1 §4 itself argues is the common one.

Two further blockers are mechanical and certain: the kit-version bump has a third carrier no unit
owns, and a shrink-only drift ratchet sits at exactly its ceiling while three units write into the
globs it measures. Both red the bar with no owner present to read the failure. For an unattended
build, a red bar nobody owns is the failure mode this build exists to reduce.

## Review shape

- **raw 37 · confirmed 16 · refuted 21 · unverified 0 · precision 0.43.**
- The 16 confirmed collapse to **12 distinct defects: 3 BLOCKER · 7 HIGH · 1 MEDIUM · 1 LOW.** Each
  section names the raw ids that reached it. Four pairs were independent rediscoveries of one defect,
  which is the expected shape when several lenses grep the same carrier set.
- Precision 0.43 is below the ~0.5 floor the charter §8 names. Read it as a signal about the target
  rather than the fan: a spec set is a prose surface, so lenses generate style-shaped candidates that
  a skeptic correctly refutes. The confirmed set is nonetheless dense in mechanical, re-runnable
  claims, which is what a spec audit is for.
- **Not covered, stated so a green row is not misread:** the full bar was NOT run for this review.
  The bar predictions in B2 and B3 are derived from the gate sources, not observed. No end-to-end
  two-clone concurrency scenario was constructed; B1's timing argument rests on `AGENTS.md`'s recorded
  measurement plus the turnstile's own constants, not on a staged race.

---

# BLOCKERS

## B1 — The merge-bar turnstile re-creates the wedge one layer down, and §5 makes a false exclusive claim about it

*(raw id 1)* · **`spec/…-TOOL-aUnblockedFleet-1.md` §5 `risks`, and its silent counterpart in
`…-2.md` §5**

Unit 1 §5 states that "the one real concurrency hazard admitted by this change is two runs landing
from one clone racing on the shared lander marker". A second one exists and no spec names it.

`tools/run-gates/run-gates.sh:415-441` holds a repo-wide turnstile keyed on `git rev-parse
--git-common-dir`, resolved absolutely, with `GATE_TURNSTILE` defaulting to `1`. Its own header says
it plainly: "one bar per repo". Every worktree of one repository shares that key. So two concurrent
`--close` calls in one clone do not run two bars — they run one, then the other.

The bound is on the wrong side of the queue. `.unattended.conf:32` declares `GATE_BOUND="3600"`, and
`--close` runs `GATE_CMD` through `run_bounded`, so **the queue wait is inside the timed command**.
The turnstile's own bounded wait is `TS_MAXWAIT = TS_TTL * 4`, which is at least 7200 s — twice the
run's bound. `AGENTS.md` records a full bar at 4926 s of leg-sum with its longest leg at 1565 s,
which puts a 26-minute floor under wall clock however wide the pool is.

So the second run's bar can plausibly spend its entire 3600 s queued and never start. `run_bounded`
returns 124 or 137, and `--close` writes the Definition-of-Done text at `unattended.sh:2852`: *the
merge bar did not answer within the declared 3600s bound … this item is unmet because the bar never
returned rather than because a leg failed.* An unattended run fails its DoD for pure contention,
with no owner present.

Before this build, the second concurrent run in one clone was refused at preflight. The refusal was
wrong for the reason the build says it was, but it did incidentally keep two bounded bars off the
same turnstile. That is a safety property the removal loses. And it is not the edge case: unit 1 §4
rejects node-partitioning precisely because "same-node concurrency is the COMMON case here".

No section 2 item, no non-goal, and no acceptance criterion in any of the five specs touches it.

**Fix.** Add a scope item or an explicit non-goal naming the turnstile: state that two concurrent
closes serialize their bars, and either derive `GATE_BOUND` against the turnstile's own bounded wait
or file a backlog row beside unit 5's S4 marker-race row. Then correct §5's enumeration from "the one
real concurrency hazard" to the two it now admits, and add an AC that observes the queued case — a
second `--close` whose bar waits reports the wait, rather than surfacing as an unexplained unmet
`gates-green`.

**Left-shift gate.** `run_bounded` should distinguish "the command ran and timed out" from "the
command never started". Make the turnstile export the seconds it queued (it already tracks `TS_WAITED`),
have `--close` subtract that from the elapsed time before grading `gates-green`, and add an arm to
`unattended.test.sh` that stubs a queued bar and asserts the DoD text names the wait. That converts a
silent contention failure into a named one, which is the class §7 calls green-by-absence in reverse.

## B2 — The kit-version bump has three template carriers; the specs name one, so two gate legs red with no owner

*(raw id 11)* · **`spec/…-TOOL-aUnblockedFleet-3.md` §2 S5 and §4 files-touched, against §7 Gates**

`tools/check-kit-versions.sh:159-172` asserts that **every** tracked `tools/unattended/*.template.md`
carries a `gov:kit unattended@<version>` marker equal to the constant. There is no exemption. `git
ls-files 'tools/unattended/*.template.md'` returns three files:

```
tools/unattended/PLAYBOOK-TEMPLATE.template.md
tools/unattended/PROTOCOL.template.md
tools/unattended/SKILL.template.md
```

All three markers, and all three renders, currently read `1.12`. Unit 3's files-touched table lists
PROTOCOL + its render, SKILL + its render, and the two `KIT_UNATTENDED_VERSION` shell constants.
`tools/unattended/PLAYBOOK-TEMPLATE.template.md:1` and its render `memory/guides/PLAYBOOK-TEMPLATE.md:1`
appear in no unit of the set.

Both legs unit 3 §7 names as binding therefore go red. `check-kit-versions.sh` reds on the unbumped
third marker. And bumping that marker without re-running the adopter reds `adopt-unattended.sh
--check` — the "unattended skill wiring" leg — which verifies three installed artifacts at
`adopt-unattended.sh:265-271` with its own refusals for each. No unit owns the fix, so the build
discovers it at the bar, unattended.

**Fix.** S5 enumerates all six carriers explicitly: two `KIT_UNATTENDED_VERSION` constants with
their same-line markers, three template markers, three renders. §4's table gains
`tools/unattended/PLAYBOOK-TEMPLATE.template.md` and `memory/guides/PLAYBOOK-TEMPLATE.md`. Add an AC
asserting `gov:kit unattended@` resolves to exactly one value across all of them.

**Left-shift gate.** The carrier set is already machine-derivable — `check-kit-versions.sh` globs it.
Make the spec stop enumerating carriers at all: add a one-line preflight helper
(`bash tools/check-kit-versions.sh --carriers unattended`) that prints every path holding the marker,
and have the unit's AC diff the bumped set against that output. A spec that types a derived
population is the "count in prose beside the source that owns it" class §7 already forbids.

## B3 — The `drift-audit records` ratchet is at its ceiling; three units write into the globs it measures

*(raw id 32)* · **`spec/…-TOOL-aUnblockedFleet-1.md` §7 Gates, and the same gap in `…-2.md` §7 and `…-3.md` §7**

`python tools/drift-audit/drift_report.py --check` currently prints:

```
non_terminal_specs_cited_by_product_source             2     23  ok (pin 2, drain it)
```

Value 2 against pin 2 — exactly at the ceiling, zero headroom. The signal returns `gateable: True`
(`drift_report.py:479`), so `value > pin` reds. Its leg, `drift-audit records`, carries **no guard**
in `tools/gate-legs.json`, so it runs on every bar including the push boundary.

The oracle greps each non-terminal spec's own id, `-w -F`, across `PRODUCT_GLOBS` — which contains
`tools/`, `skills/` and `.claude/`, i.e. every file units 1 through 3 touch. Unit 1 S1 rewrites
`check_single_live()`'s header. Unit 2 S6 rewrites check 7's header. Unit 3 rewrites two templates.
Charter §6 mandates inline provenance ids on exactly this kind of non-obvious rule. A header citing
`TOOL-aUnblockedFleet-1` while that spec still reads `SPECCED` or `INPROGRESS` drives the signal to 3
and reds the bar.

The obvious escape is blocked by design: the key is listed in `RATCHETS` with `weakens: up`
(`drift_signals.py:276-277`), so raising the pin prints `RATCHET WEAKENED`. And the trap is already
documented *inside the file unit 1 edits* — `unattended.sh:4205-4209`: "shipped source that spells an
unbuilt id reads to the drift oracle as a status header nobody updated."

Prior art nobody cited: `TOOL-aBoundedVerdict-30` (CLOSED) measured this same signal at 10 against
pin 2, with "shipped source naming UNBUILT ids" as one root cause. No spec in this set names it.

This finding is conditional on the builder actually writing the unit id into the rewritten headers.
That is what the charter tells them to do and what the sibling headers in both files already do, so
treat the condition as met unless the specs say otherwise.

**Fix.** Add `drift-audit records` to units 1, 2 and 3 §7 as a binding leg, and state the landing
order: either the rewritten source headers cite no unit id until those specs reach a terminal status,
or the status flip lands inside the same commit range as the source edit. Forbid raising the pin
explicitly, in the spec text.

**Left-shift gate.** Have `drift_report.py` name the offending pair in its failure output — which
non-terminal spec, cited from which product path — rather than reporting a bare count. A ratchet at
its ceiling that fails with a number tells an unattended run nothing it can act on; one that names
`tools/unattended/unattended.sh → TOOL-aUnblockedFleet-1` tells it the landing-order fix directly.

---

# HIGH

## H1 — The Skill states a consequence the build removes, in the file unit 3 edits, invisible to unit 3's own acceptance

*(raw ids 2, 12)* · **`spec/…-TOOL-aUnblockedFleet-3.md` §2 S3 and §6 AC2**

S3 drops one clause from the `--preflight` refusal list at `SKILL.template.md:175`. The same file
carries a second binding claim, at `SKILL.template.md:706` and its render
`.claude/skills/unattended/SKILL.md:706`:

> …until it is committed, every later run still counts yours as live and the bar reds on the second one.

After unit 2 converts check 7's `fail 7` into a report, the bar does not red on the second one. AC2
greps only for `a second run is already live`, which occurs at line 175 and nowhere else — so every
acceptance criterion of unit 3 passes with a falsified sentence left standing in the exact carrier
the unit edits. Check 10's parity gate compares template against render, never the Skill's prose
against the code, so nothing reds.

This is the `TOOL-dClosedLexicon-11` phantom that unit 3 §1 cites as its own reason to exist. It is
also the sentence that *motivates* committing the `--landed` record before stopping — and its real
remaining reason (the record is named as live in every later run's report until it is committed) goes
unstated, so the reader loses the motivation along with the false consequence.

**Fix.** S3 names line 706 as a second edit: replace the bar-reds clause with the reason that
survives. AC2 gains `grep -n "the bar reds on the second one" tools/unattended/SKILL.template.md
.claude/skills/unattended/SKILL.md` returning nothing.

**Left-shift gate.** Add a leg that greps the kit's shipped prose for the vocabulary of removed
refusals — a small deny-list file of phrases (`the bar reds`, `refuses`, `a second run is already
live`) checked against the set of `fail <n>` codes the driver and leg actually still call. A prose
claim about a refusal that no `fail` call backs is exactly the contract-outlives-enforcement class,
and it is gateable at the phrase level.

## H2 — A third in-code carrier of the deleted rule survives in the driver, one function from the change

*(raw ids 15, 31)* · **`spec/…-TOOL-aUnblockedFleet-1.md` §2 S1 and §4 files-touched; `…-3.md` §2 S1/S3 and AC1**

`tools/unattended/unattended.sh:1109-1110` states the removed rule verbatim:

> At most one run-state file may be non-terminal, or "the run" is not well-defined and anything keyed
> on it must either OR the phases together or pick one arbitrarily.

It is a stranded comment block: `check_method()` opens at `:1124` and `check_single_live()` at
`:1210`, roughly a hundred lines below. Unit 1's "the function's header rewritten" does not reach it.
Unit 3's carrier census covers two prose templates and their renders, and its AC1 greps that phrase
in only `PROTOCOL.template.md` and `memory/guides/UNATTENDED-PROTOCOL.md` — the one file that would
still match goes unchecked.

The build would ship product source stating the removed rule as binding, inside the very file whose
function stopped enforcing it. That is the corpus's own
`memory/gotchas/amendment-leaves-its-other-half-standing.md` class, which `gotchas.py --for-paths`
selects over this build's files and which no spec in the set cites.

Incidentally, unit 1's line cites are stale against its own base: it names `check_single_live` at
`:1224` and check 7 at `:1112`, while the tree has them at `:1210` and `:1174`.

**Fix.** Name `tools/unattended/unattended.sh:1109-1110` explicitly in unit 1 S1 — it is a misplaced
block, so removing it also repairs `check_method`'s header. Widen unit 3 AC1 to
`grep -rn "not well-defined" tools/unattended/ memory/guides/` returning only the rewritten text.
Cite `amendment-leaves-its-other-half-standing` in unit 1 §5 risks. Re-derive the line cites.

**Left-shift gate.** Same leg as H1: the removed rule's own sentence goes on a deny-list checked
across `tools/unattended/**` (both `.sh` and `.template.md`), not just the two protocol paths. A
carrier census scoped to prose cannot see a comment, and comments are where this repo keeps its
rationale.

## H3 — Two in-code justifications cite check 7 as a live refusal; both become false and neither is in scope

*(raw ids 3, 27)* · **`spec/…-TOOL-aUnblockedFleet-2.md` §3 non-goals and §2 S6**

Two shipped sources justify themselves by citing the counter this build removes.

`tools/unattended/check-unattended.sh:716-720`, in check 4's own header:

> …this is its own branch rather than a consequence of the live-run rule below. Check 7 is `nlive <= 1`,
> which fires at TWO — so a `RUN.md` that has reached LANDED plus one archived record hand-edited back
> to RUNNING gives nlive=1 and the leg says nothing.

After unit 2, check 7 fires at nothing at all. The same claim is duplicated in the test file's
comment at `check-unattended.test.sh:646-653`.

`tools/unattended/unattended.sh:2027`, justifying `refuse_if_terminal --phase`:

> …returns the run to check_single_live and leg check 7, which is the counter this whole unit exists
> to free.

After units 1 and 2, neither counts.

Unit 2 §3 declares check 4 "Untouched" while simultaneously arguing it "becomes MORE load-bearing
after this unit: it is what keeps the per-build-folder live count at one" — and leaves the code a
reader actually opens saying the opposite. S6 scopes the header rewrite to check 7's own `# ---- 7:`
block. Unit 3 reaches neither file. Check 10's parity gate covers renders, not source comments.

The consequence is not cosmetic: a future editor reading check 4's header will believe a tree-wide
rule still backstops it, and may weaken the one check that after this build is the sole enforcement
of per-folder singularity.

**Fix.** Add both sites to unit 2 S6 as carriers rewritten in the same commit — check 4's header
states the invariant it now holds alone; `--phase`'s refusal states the reason that survives (a
finished record is not something to re-open) instead of the counter that no longer exists. Extend
unit 3 §3's "verified by grep" to a grep of `tools/unattended/*.sh` for `check 7` and
`check_single_live`. Add an AC asserting neither phrase survives.

**Left-shift gate.** When a `fail <n>` call is deleted from a kit checker, every remaining reference
to that check number in the kit's own sources should have to justify itself. A small leg that greps
`tools/unattended/**` for `check <n>` and cross-references the set of live `fail <n>` calls turns
this whole class into a red row instead of three separate archaeology finds.

## H4 — The announcement threshold drops to one; the liveness notice's guard does not, so the exclusion's own case reports green-by-absence

*(raw id 9)* · **`spec/…-TOOL-aUnblockedFleet-1.md` §2 S4, against §2 S3 and §5 error/empty states**

Unit 1 S3 sets the announcement's threshold at one concurrent run ("nothing is printed at zero
concurrent runs"). The `UNAVAILABLE` liveness notice keeps its existing guard, which is
`[ "$n" -gt 1 ] && [ -z "$anc" ]` at `tools/unattended/unattended.sh:1254`.

`check_single_live` runs at `:2400` and `scaffold_runmd` at `:2487`, so at first preflight `n` counts
only *other* tracked live records. At exactly one concurrent record with no anchor observed, the
driver names that record as a live competitor and says nothing about the exclusion being
uncomputable.

That is the single state the `LANDING` exclusion exists for — a finished run missing its stamp — and
its liveness assertion is silently absent. Before the change the state was silent because the refusal
did not fire at `n=1` either; after it, the announcement fires and its liveness half does not. It is
the green-by-absence shape that S4 and §5 both claim to be preserving.

Note the leg does not have this problem: unit 2 S3 says "SILENT at `nlive <= 1`", matching the leg's
own `UNAVAILABLE` guard at `nlive > 1`. The leg's two thresholds agree; the driver's do not. AC4
asserts only "the existing arm text", so no unit and no criterion can see the hole.

**Fix.** S4 gains a sentence lowering the `UNAVAILABLE` guard to the announcement's own threshold —
fire whenever a record is announced and no anchor was observed. §6 gains an AC: one concurrent
record, no anchor observed, output carries **both** the announcement and the `UNAVAILABLE` notice.

**Left-shift gate.** Bind the two thresholds to one expression in source rather than to two
independently-written comparisons, and add an arm that asserts the pair moves together: when the
announcement fires, the liveness notice's guard is evaluated. A liveness assertion behind a different
predicate than the signal it qualifies is the "guard that shares no variable with the thing it
guards" failure inverted, and it is cheap to make structural.

## H5 — Unit 1 and unit 4 both own the same two test edits, and unit 1 disagrees with itself

*(raw id 13)* · **`spec/…-TOOL-aUnblockedFleet-1.md` §2 S5 and §4 files-touched, against §5 testing and `…-4.md` §2 S1/S2**

Unit 1 S5 puts the `unattended.test.sh` check-5 arm rewrite in its IN scope, and its files-touched
table claims both edits — "the check-5 arm asserts the announcement and the non-refusal; a new arm
asserts silence at zero concurrent runs". Unit 1 §5 then says "unit 4 owns the arms". Unit 4 S1 and
S2 specify the identical two edits, with the identical rationale, in unit 4's own table.

One edit, two owners, and the owning unit contradicts itself inside one document. Unit 1's AC2, AC3
and AC4 are assertions about arms that do not exist until order 4, so unit 1 as written cannot be
verified at its position. A builder following S5 writes the arms, then meets unit 4 re-specifying
them; a builder following §5 leaves unit 1 unverifiable for three units.

**Fix.** Delete the test-file clause from S5 and the test-file row from §4's table, and restate
AC2–AC4 as asserted by unit 4's arms with the dependency named. Or move unit 4 to order 2 and have
units 1 and 2 cite it as a predecessor. Either resolves it; leaving both is the failure.

**Left-shift gate.** A build with ordered units can assert single ownership mechanically: every path
in every unit's files-touched table appears in at most one unit, unless a unit explicitly declares a
shared-carrier exception with a reason. That is one pass over the spec set's tables and it catches
this class before a builder does.

## H6 — Unit 2 claims a test file unit 4 owns and a version bump unit 3 owns

*(raw id 14)* · **`spec/…-TOOL-aUnblockedFleet-2.md` §4 files-touched and §4 Rollout, against §5 testing and `…-3.md` §2 S5**

Two ownership collisions in one section. Unit 2's files-touched table assigns "the check-7 RED arm
becomes a report arm; its GREEN control is kept and a silent-at-one arm added" to
`check-unattended.test.sh`, while unit 2 §5 says "testing + left-shift gates — unit 4" and unit 4 S3
and S4 specify those same edits in unit 4's own table. AC1 through AC5 all assert against those arms
from order 2.

Separately, unit 2's Rollout narrates the kit-version bump ("the kit version bumps in both
`unattended.sh` and `check-unattended.sh` … and the rendered Skill re-stamps") which unit 3 S5 also
claims — while unit 2's own table lists no template and no render to carry the bumped marker.

One correction to the raw finding, recorded because it matters: AC6 is scoped "at the landing tip",
i.e. after all five units, so the "unreachable at that commit" reading does not stand. The ownership
collision does.

**Fix.** Rollout drops the bump and points at unit 3 as its owner. The table drops the test file.
AC1–AC5 name unit 4 as the arms' owner.

**Left-shift gate.** Same table-ownership pass as H5, extended to Rollout prose: a unit whose Rollout
narrates an artifact its own files-touched table does not list is describing someone else's work.

## H7 — The arming unit has no fixture at the one threshold the build moves

*(raw id 18)* · **`spec/…-TOOL-aUnblockedFleet-4.md` §2 S2, with S1**

Unit 4's two driver fixtures are two concurrent records (S1's `hit`) and zero (S2's `miss`). The
boundary the design actually moves — exactly **one** concurrent record — has no arm.

The fixture at `unattended.test.sh:474-482` seds a phase into `tRun`'s own record and adds `tTwo`,
then preflights `tRun`, so `check_single_live` counts `n=2` with the run's own record included. S2's
silence fixture is the base tree, where `tRun/RUN.md` carries no phase line and is skipped by
`[ -n "$p" ] || continue` — zero live records. Neither arm reaches `n=1`: a fresh slug's first
preflight with exactly one other live record.

A driver that keeps the inherited `n > 1` trigger announces in S1's fixture, stays silent in S2's,
and passes both arms — while being silent in precisely the case unit 1 S3 requires an announcement
for, which is the commonest case this build exists to enable. That is the
`fixture-passes-by-finding-nothing` shape unit 4 §4 itself cites, landing on the one threshold the
change alters, in the unit whose entire job is arming. It is also the state where H4's `UNAVAILABLE`
gap lives, so one fixture buys both.

**Fix.** Add a third arm at exactly one concurrent record asserting the announcement is present, and
an AC that observes it RED when the threshold is written as `n > 1`.

**Left-shift gate.** Make the observed-failing-case rule (unit 4 S5) enumerate *thresholds* rather
than *arms*: for every comparison the change moves, one arm on each side of the new boundary and one
on the old boundary. Recording that as the build's arming rule turns "we armed it" into a countable
claim instead of a judgement.

---

# MEDIUM

## M1 — The load-bearing verb census is taken over the dispatch case, not over the verb population

*(raw id 26)* · **`spec/…-TOOL-aUnblockedFleet-1.md` §4, "All fourteen driver verbs take a `<slug>` (`unattended.sh:4248-4261`)"**

This sentence is where the build's safety argument is made, and its population is wrong. The driver
declares `VERBS_SLUG` (14 verbs) at `unattended.sh:86` **and** `VERBS_INLINE="--plan --phase
--version"` at `:88-89`, joined by `verbs_all()` at `:90`. The three inline verbs exit inside the
parse loop at `:4220`, before the cited case at `:4247-4262` is ever reached. The dispatched
population is 17, not 14.

§4's own probe table then names `--plan` — a verb outside the fourteen it counts — so the spec
measures outside the set it claims to have enumerated, and §10 claims the verb dispatch table was
verified against source.

The conclusion survives: `--plan` and `--phase` take a positional slug and `--version` reads no run
at all. But a completeness argument stated over the wrong population is not a completeness argument,
and the next reader re-deriving from `verbs_all()` gets a different number with no way to tell
whether a verb was missed.

**Fix.** Restate the claim over `verbs_all()` citing `:86-89`: fourteen slug verbs, plus `--plan` and
`--phase` which take a positional slug, plus `--version` which reads no run. Say which of the three
was probed and which needed no probe.

**Left-shift gate.** The driver already single-sources its verb population and already joins the
carriers in other files by a gate leg. Extend that leg to assert the count: any prose in the kit or
in a spec citing a verb total is compared against `verbs_all()` at check time. A number typed beside
a source that owns it is §7's own named failure, and this one sits under the build's central claim.

---

# LOW

## L1 — AC5 invokes a Python program under `bash`, and the two specs spell it differently

*(raw ids 21, 30)* · **`spec/…-TOOL-aUnblockedFleet-1.md` §6 AC5**

`bash tools/memory-tree/check-arms.py` cannot run — the file opens `#!/usr/bin/env python3` followed
by a docstring, and bash parses the Python source. Running it produces `line 35: fail: command not
found`, a command-substitution syntax error, and exit 141. The criterion can never pass.

Unit 4's AC6 spells the same program `python tools/memory-tree/check-arms.py`, and
`tools/gate-legs.json` invokes it the same way. Two specs in one set give two invocations for one
program and one of them fails by construction.

Second half: "finds every remaining branch armed" is already false at base. `check-arms` reports
`unattended.sh` at 175 branches / 172 armed, with the three unarmed carried by
`memory/project/unarmed-branches.txt` (rows for `fail 9`, `27` and `29`). An AC that fails for
reasons unrelated to the change, worded so the obvious way to satisfy it is to edit the pin, is worse
than no AC.

**Fix.** `python3 tools/memory-tree/check-arms.py --check`, worded as "every branch armed or pinned,
with no pin row and no `ARMS_FLOORS` entry edited".

**Left-shift gate.** The hygiene leg already grades acceptance-witness tokens as backticked names.
Extend it one step: a backticked command in an AC whose first token is an interpreter is checked
against the target file's shebang. It is a one-line predicate and it catches every future
`bash foo.py`.

---

# What was refuted, and one thing worth saying about it

Twenty-one candidates did not survive. The recurring refuted shapes were: objections to §5 checklist
entries marked `N/A` on a shell driver (correct as written), claims that unit 5's `TOOL-aReapedTicket-5`
narrowing should have been a close (unit 5 §4 argues the opposite convincingly and the charter backs
it), and several readings of unit 1 §4's rejected alternatives as under-argued that did not survive
contact with the measurement table.

Worth recording: **the by-construction measurement in unit 1 §4 is the strongest thing in this spec
set.** Neutering both enforcement points in a scratch copy with two genuinely live records, then
running the full leg and every verb, is the right way to establish a negative — and it is what makes
the thesis survive twelve defects. The defects are all in the *carrier* work around that measurement,
not in the measurement. None of the twelve findings above disputes that nothing is keyed on tree-wide
singularity.

The one place the measurement did not look is one layer out from the leg and the driver, at the merge
bar itself, which is B1.
