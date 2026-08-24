**Serves:** diff-review TOOL-dUnstalledConvoy-26

# Spec audit — the switch is buildable, but its population is the wrong set and it retires the push boundary's only proof

**Reviewed range:** `b164a296...HEAD` (HEAD = `02f8495e`, 2 commits, 6 files: one new spec plus the
records that put the build into REVIEWING). **ROUND: 1.**

**Review shape:** raw 40 · confirmed 34 · refuted 6 · unverified 0 · precision 0.85. Deduplicated to
17 findings below, because several lenses landed on the same defect from different sides.

## Verdict: BLOCKED

**Three blockers, eight highs, five mediums, one low.** There is no product code in this diff, so
every finding is a design defect of one of three kinds: a scope item that cannot be built as written,
an acceptance criterion a wrong implementation also satisfies, or a claim about the base that is
false at `b164a296`.

**What is right, and it is not a small thing.** The owner's ruling is correctly read: a self-test's
subject is the kit, and running it in a repo that never edits the kit buys nothing. S1's refusal to
infer the population from `.test.sh` in an argv is correct and the reasoning is correct — this repo
has written that predicate twice and thrown it away twice, and `tools/check-testsuite-counts.sh:36`
still carries a live instance of it. S2's measurement is exact: `run-gates.sh:148` is
`changed() { [ -n "${GATE_FULL:-}" ] && return 0; ... }`, so `guard = ["{kit}/"]` really is bypassed
at the push boundary, which is the one place an adopter pays for it. F1 and F2 are resolved with
reasons that hold. The wire-format read in §4 is accurate as far as it goes.

**What blocks it is that the spec never names the artifact the whole merge bar rests on.** Forty-seven
skipped legs land in a counter that is one of five preconditions for `<git-dir>/gate-full-green`, and
that record is what `.githooks/pre-push` reads to decide whether a landing owes a full bar. The spec
mentions neither the stamp, nor the counter, nor the hook. §5 says "security — none". That is exactly
backwards: this unit's blast radius is the authorization record of the push boundary.

**And the population is the subset, not the population.** S5 derives 29 legs from `tools/*/kit.toml`
and stops there. `govkit.read_descriptors` also loads `tools/govkit/entries/*.kit.toml`, which
declares ten more self-tests, all ten inside the 47 that S6 marks. S7 makes a descriptor/manifest
disagreement a refusal in both directions, so the unit reds govkit's own cross-check at its own
landing.

**Then the unit switches off its own acceptance evidence.** §7 names `run-gates`' self-tests and
govkit's selftest as the legs that exercise this change, and `GATE_FULL=1` as the Definition of Done —
and S2/F2 state in the same document that `GATE_FULL` does not run them. AC1 through AC6, AC8 and
AC11 are observed by legs the declared DoD invocation skips.

---

## Derived populations (measured at `b164a296`, not taken from the brief)

Every figure below was re-derived through `govkit.load_toml` and `json.load` rather than counted by
eye. The brief's five measured facts all reproduce; two of its figures are right about a subset and
wrong about the population, which is finding B2.

| Population | Count | How derived |
|---|---|---|
| Manifest legs | 85 | `len(json.load(open("tools/gate-legs.json")))` |
| Manifest chunk split | selftests 42 · declarations 20 · product 9 · wiring 9 · records 3 · e2e 2 | `Counter(l["chunk"])` |
| `[[gate_leg]]` rows in `tools/*/kit.toml` | 49 | across 13 descriptors |
| `[[gate_leg]]` rows in `tools/govkit/entries/*.kit.toml` | 19 | across 11 descriptors |
| `[[exempt_leg]]` rows in `registry.toml` | 17 | — |
| Sum | 85 | 49 + 19 + 17, and `manifest - claimed - exempt` is empty |
| S5's self-test subset | 29 | matches S5's per-kit list exactly |
| Entry-descriptor self-tests S5 misses | 10 | see B2 |
| Exempt self-tests no descriptor claims | 8 | see H4 |
| S6's 47 | 29 + 10 + 8 | and no single predicate over the tree yields it — see H6 |

The 47 also equals `chunk == "selftests"` (42) plus exactly five legs gov classifies otherwise:
`codebase-map adopter e2e`, `run-gates adopter e2e`, `kit/dogfood doc parity`, `marker contracts`,
`review-protocol parity (kit vs dogfood)`. That is the only reproduction of the number, and three of
those five are the repository-subject legs of H1.

---

## The seven questions the hunt asked, answered

1. **Buildable as written?** No, in two places. The reader/dispatcher seam named in §4 is the wrong
   one and reds the bar with 47 phantom failures if built literally (H2). And §3's claim that the
   `chunk` field is untouched is false: `chunk` is the wire format's LAST field, so appending a sixth
   changes how `chunk` parses (M5). The 1:1 row correspondence and the drop sentinel survive untouched,
   and the timing cache is keyed on leg name so it is unaffected.
2. **Is one switch enough, and does `GATE_FULL` not unlocking it surprise?** One switch is enough. The
   surprise is severe and unaddressed: with the switch default-off no run can ever stamp a full green
   again, so pre-push forces `GATE_FULL=1` on every push forever and the forced run also stamps
   nothing (B1). A complete bar is obtainable, but only as `GATE_SELFTESTS=1 GATE_FULL=1`, which the
   spec never writes down.
3. **S4's announced skip and the empty-population case.** Neither is stated precisely enough to build.
   The verb is unchosen and both naive choices break a reader (H3); the refusal is a predicate over the
   manifest while its observable is a run outcome, and the identical zero-leg state stays reachable
   through guards (M1). It does not collide with the pop-guard or canary legs directly, but it does
   make two shipped kits un-adoptable standalone (M2).
4. **Does S6+S7 keep the both-directions check honest?** No. It creates exactly the asymmetry the
   question asks about, twice: ten entry-declared legs marked in the manifest and not in their
   descriptor (B2), and eight exempt legs marked in the manifest with no descriptor to disagree with
   (H4).
5. **A criterion a wrong implementation also satisfies.** AC6 is a tautology (H5), AC9 is not
   observable by its stated observer (H6), and AC11 is satisfied by a run that executes none of the
   arms (B3). AC7 requires an emission no scope item builds (M3).
6. **Is F3 right?** Default-OFF is right *conditional on* the membership criterion being the owner's —
   subject entirely inside the kit. As the population currently stands it is wrong, because three
   repository-subject legs and the whole manifest-integrity canary ride out with it (H1). Fix H1 and
   F3 stands; leave H1 and F3 turns off drift detection in the one repo that dogfoods.
7. **False claims about the base.** Three. §3's "`chunk` untouched" (M5); §10's "a fifth in the same
   shape" with no consumer named, when the key set is a closed pin in two places (M4); and
   `tools/run-gates/kit.toml:108`'s `run_all_env = "GATE_FULL=1"`, which becomes false the moment F2
   lands and which the spec does not update (L1).

---

# BLOCKERS

## B1 — the on-demand skip destroys the full-green stamp, and the spec picks neither branch

`memory/builds/dUnstalledConvoy/spec/2026-08-23-spec-TOOL-dUnstalledConvoy-26.md:26-28` (S3, S4),
with `:52` (§3's "untouched" list) as the place it should have been decided.

**The chain, verified end to end.** `tools/run-gates/run-gates.sh:902` increments `skips` for any leg
whose rc sentinel is `skip`. `tools/run-gates/run-gates.sh:1095` writes `$gd/gate-full-green` only
when `[ "$fails" = 0 ] && [ "$skips" = 0 ] && [ "$reuses" = 0 ] && [ "$tree_moved" = no ] &&
[ "$TREE_CLEAN" = yes ]`. `.githooks/pre-push:133` reads that record and `:143` forces on its absence:
`[ -n "$rec_sha" ] || force="no recorded full green"`. `.githooks/pre-push:199-201` then exports
`GATE_FULL=1`.

**Both branches are damaging, and the spec chooses neither.**

- If on-demand skips increment `skips` — the natural reading of S4's "reported the way a skipped leg
  is already reported" — then with F3 defaulting the switch off, every run on this repo skips 47 legs
  and `gate-full-green` is never written again. Predicate 1 fires on every default-branch push
  forever. `GATE_FULL_MAX_LAG=10` (`.githooks/pre-push:129`) becomes permanently unreachable and
  predicates 2 through 7 become dead code. That silently reinstates the unconditional force the block
  at `.githooks/pre-push:108-129` was written to remove — and per S2 the forced run still skips the
  47, so it stamps nothing either. It fails in the expensive direction, which is the direction nobody
  notices.
- If the builder routes them around `skips` to keep the stamp alive, a record literally named
  `gate-full-green` is stamped over a bar that executed 38 of 85 legs, and the push boundary later
  treats it as proof that the whole bar passed at that sha. Nothing in the record distinguishes the
  two populations. `tools/run-gates/run-gates.evidence.test.sh:301` is a live negative control pinning
  today's meaning ("full-green stamped despite a skipped leg"), so this branch also silently redefines
  what that arm certifies.

The comment at `tools/run-gates/run-gates.sh:1087-1094` says it outright: the five preconditions "are
the whole of what makes its name true", and each has its own negative control precisely because an
implementation that forgets one still passes every arm written for the others.

**Fix.** Decide it in the spec, in S3 and S4.

- An on-demand skip is counted in its OWN tally and never in `skips`, so the five full-green
  preconditions are unchanged in meaning by this unit.
- The full-green stamp gains a `selftests\t0|1` field recording the population it was earned on, and
  its precondition becomes `skips == 0 AND on_demand_skipped == 0` — only a `GATE_SELFTESTS=1` run on
  a clean tree may stamp. That keeps the record's name true and keeps the staleness machinery alive,
  at the cost of one full-and-selftests run per ten commits, which is what `GATE_FULL_MAX_LAG` was
  chosen to buy.
- Add an AC: a default bar over a manifest containing on-demand legs writes no `gate-full-green`, a
  `GATE_SELFTESTS=1 GATE_FULL=1` clean-tree run does, and a guard-skipped leg still suppresses it.

**Left-shift gate.** `tools/run-gates/run-gates.evidence.test.sh` already holds every negative control
for the stamp. Add a sixth: an on-demand-skipped leg and the stamp's verdict, plus an arm asserting
the stamp file carries a `selftests` field. Second arm in `.githooks/pre-push.test.sh`: a recorded
green whose `selftests` field is 0 does not satisfy predicate 1.

## B2 — S5's population is `tools/*/kit.toml` only; ten more self-tests live in `tools/govkit/entries/`, and S6+S7 land in mutual contradiction

`memory/builds/dUnstalledConvoy/spec/2026-08-23-spec-TOOL-dUnstalledConvoy-26.md:30-33` (S5) against
`:34-38` (S6, S7).

**Measured.** `govkit.read_descriptors` (`tools/govkit/govkit.py:2978`) loads every `[[entry]]` in
`registry.toml`, and `claimed_legs` at `tools/govkit/govkit.py:864` is built over that whole set. The
arithmetic closes exactly: 49 rows in `tools/*/kit.toml` + 19 in `tools/govkit/entries/*.kit.toml` +
17 `[[exempt_leg]]` = 85 = the manifest, with `manifest - claimed - exempt` empty. S5's per-kit list
sums to 29 and reproduces `tools/*/kit.toml` exactly, so the entries descriptors are simply outside
the population it names.

Ten entry-declared legs are self-tests and all ten are inside S6's 47: `micro-format gate selftest`,
`line-length gate selftest`, `placeholder-catalogue self-test`, `testsuite counts self-test`,
`agent-cap restatement self-test`, `install-prefix self-test`, `check-wiring self-test`,
`push-main self-test`, `pre-push self-test`, `settings-merge selftest`.

**Why it blocks.** S7 makes a descriptor/manifest `on_demand` disagreement a refusal in both
directions. Marking the manifest per S6 while migrating only the eleven `kit.toml` files per S5 reds
`govkit selfcheck` on ten rows at this unit's own landing. Leaving them unmarked contradicts S6's 47.
There is no build that satisfies both sentences. Separately, those entries install into targets
exactly like kits (`tools/govkit/govkit.py:2424-2478` walks `d.get("gate_leg")` for every selected
entry), so an adopter keeps receiving ten self-test legs and §5's "an adopter's full gate loses 29
legs' worth of work" is wrong by ten.

**Fix.** Restate S5 over the descriptor set `read_descriptors` actually returns — `tools/*/kit.toml`
plus `tools/govkit/entries/*.kit.toml` — and delete the typed eleven-entry list. The sentence already
says the population is derived; typing it beside the derivation is the two-answers-to-one-question
class this repo gates for. Then say which of those descriptor legs are self-tests by the criterion of
H1, not by a count.

**Left-shift gate.** An arm in `tools/govkit/selftest.py` asserting that the descriptor set the
migration walks is the same set `govkit.read_descriptors()` returns — so the two can never be
enumerated differently again. That arm gates the class rather than this instance.

## B3 — §7 declares as the Definition of Done a run that skips every leg observing AC1–AC6, AC8 and AC11

`memory/builds/dUnstalledConvoy/spec/2026-08-23-spec-TOOL-dUnstalledConvoy-26.md:121-122` (§7) against
`:23-25` (S2), `:50-51` (F2 in §3) and `:129-131` (F2 resolved).

**Verified by deriving the populations.** `run-gates canary` is `bash {kit}/run-gates.test.sh`, one of
the five self-test rows in `tools/run-gates/kit.toml`, so it is inside S5's 29 and inside the 47
derived from the manifest. So are `run-gates evidence`, `run-gates turnstile` and
`profile-bar selftest`. `govkit selftest` is an `[[exempt_leg]]` row with `chunk: selftests`, also
inside the 47. Only `govkit acceptance matrix` (`chunk: declarations`, exempt) survives a switch-off
run, so AC7 is the single acceptance criterion its own declared gate can still see.

§7 therefore names as this unit's gates precisely the legs S2 and S6 switch off, and names
`GATE_FULL=1` as the DoD invocation while F2 states in the same document that `GATE_FULL` does not
unlock them. A wrong implementation — one where the switch does nothing, or where the skip is
silent — passes the stated DoD unchanged, and AC11's "the full bar is green" is satisfied by a
38-of-85 run that never touched a single arm written for this change. This is green-by-absence one
altitude above the single-leg case the runner already reds on at `tools/run-gates/run-gates.sh:968`,
landing inside the unit's own acceptance criteria.

**Fix.** §7's DoD invocation becomes `GATE_SELFTESTS=1 GATE_FULL=1 bash tools/run-gates/run-gates.sh`.
AC11 stops saying "green" and states the observed leg count (85 of 85 with the switch on) AND names
the legs that exercise this unit as having reported `GATE ok`, not merely as present. S9 gains an
explicit sentence: every arm for this unit lives in a leg the unit itself marks on-demand, so the DoD
invocation is not the default one.

**Left-shift gate.** This class — a unit whose acceptance evidence rides in legs the unit disables —
is not gateable by a script over one diff. Route it into the recurring-bug-class checklist
(`tools/memory-tree/gotchas.py`) as a gotcha anchored on `gate-legs.json` and `run-gates.sh`: a spec
that changes which legs run must state its DoD invocation, and that invocation must include the legs
observing its own acceptance criteria.

---

# HIGH

## H1 — the population sweeps in legs whose subject is the REPOSITORY, and S1 never states the membership criterion

`memory/builds/dUnstalledConvoy/spec/2026-08-23-spec-TOOL-dUnstalledConvoy-26.md:19-22` (S1, which
gives the mechanism and no criterion) and `:30-33` (S5, which gives counts and no criterion).

The counts force the membership. `memory-tree` reaches 11 only by including `kit/dogfood doc parity`
and `marker contracts`; `review-harness` reaches 3 only by including
`review-protocol parity (kit vs dogfood)`. Without them S5's total is 26, not 29. Their own guards say
what they grade.

- `kit/dogfood doc parity` guards on `{memory_root}/HYGIENE.md`, `{memory_root}/TEMPLATE-SPEC.md`,
  `{memory_root}/guides/BUILD-METHOD.md` and `{kit}/` — it diffs the kit's rendered templates against
  the installed copies in the target's tree. `tools/memory-tree/kit.toml:113-121` carries a comment
  saying the guard was widened to those docs precisely so the leg would not skip when only a doc moved.
- `review-protocol parity (kit vs dogfood)` guards on `{memory_root}/guides/REVIEW-PROTOCOL.md`.
- `marker contracts` is UNGUARDED, so it reads the whole tree.

Gov's own manifest classifies all three as `chunk: declarations`, not `selftests`. They red when a
repository document moves and the kit does not — in an adopter as much as here — which is the exact
criterion `AGENTS.md` cites for keeping three unattended legs on the bar when `f5f4732a` deleted the
other seven.

The same gap reaches further, and this is the half that matters most. `run-gates canary` is in the
population, and `tools/run-gates/run-gates.test.sh:55` resolves `LEGS_FILE` to the tree's REAL
`tools/gate-legs.json`. Its arms are the only checks that the manifest key set is the pinned one
(`:96`, `:125`), that `argv[0]` is in `{bash, python, python3, node}` (`:56-75`), that no leg is a
launcher-only silent no-op, and that no guard pathspec names an untracked path — "the leg would skip
forever" (`:143-152`), a property `AGENTS.md` states as live. `run-gates gov canary` (exempt, in the
47) holds the only arms asserting `.githooks/pre-push` still has a forcing path at all and that its
bound is a source constant (`tools/run-gates/run-gates.gov.test.sh:168-172`). Today `GATE_FULL` forces
those legs at the push boundary, which in an adopter is their only automatic enforcement point, since
their descriptor guard is `{kit}/` and does not cover the target's manifest. Under S2 they run nowhere
automatic, in gov or anywhere.

**This is also the answer to F3.** Default-OFF is defensible for a population whose subject is
entirely inside the kit dir. It is not defensible for a population containing the repository's own
manifest-integrity gate and its doc-parity checks. Fix the criterion and F3 stands as resolved.

**Fix.** S1 states the CRITERION, not just the mechanism: a leg is `on_demand` only if its verdict is
a function of kit source alone — it stages a break into a copy of a checker and reads nothing of the
surrounding tree. Machine-checkable proxy: no declared guard names a path outside `{kit}/`. Name the
exclusions explicitly in S5 and S6 — anything reading `tools/gate-legs.json`, anything reading
`.githooks/`, and anything asserting kit-versus-dogfood parity stays on the bar. The two `adopter e2e`
legs qualify as on-demand only because they build their target under `mktemp -d`; say so on the record.
Add an AC: the manifest-wellformedness and guard-liveness refusals still fire on a default run.

**Left-shift gate.** In `tools/govkit/selftest.py`: no leg carrying `on_demand` declares a guard
pathspec outside its own `{kit}/`. That is the criterion, machine-checked, and it reds the day
somebody marks a repository-subject leg.

## H2 — "the dispatcher consults it" names the wrong seam; built literally the bar reds with 47 phantom failures

`memory/builds/dUnstalledConvoy/spec/2026-08-23-spec-TOOL-dUnstalledConvoy-26.md:58` (§4).

`tools/run-gates/run-gates.sh:988` is the dispatch loop's only skip test:
`{ [ -z "${names[$k]}" ] || [ -f "$WORK/$k.rc" ]; } && continue` — and the loop knows only how to
`continue`. `report_one` at `tools/run-gates/run-gates.sh:895-898` treats an absent `$WORK/$i.rc` as
`GATE FAIL  <name>  (no result)`, increments `fails`, and appends to `FAILED_LEGS`. So an
implementation that adds an `on_demand` term at line 988 without writing an rc file reds the bar on
every self-test leg.

The precedent §4 should have named is the serial guard pre-pass at
`tools/run-gates/run-gates.sh:710-716`, which writes `printf 'skip' > "$WORK/$i.rc"` before dispatch.

Ordering matters for a second reason. The reuse pass at `tools/run-gates/run-gates.sh:806-826` does
`[ -f "$WORK/$i.rc" ] && continue` — "already decided by the guard pass". An on-demand decision made
AFTER it lets `GATE_REUSE=1` stamp an on-demand leg `reuse`, which both defeats AC3 on that path and
touches `reuses`, itself a full-green precondition.

**Fix.** §4 states that the decision is a serial pre-pass writing its own rc sentinel, placed beside
the guard pass at `tools/run-gates/run-gates.sh:711-715` and therefore ahead of the reuse pass. Add an
AC arm that runs the switch-off bar with `GATE_REUSE=1` set and asserts the leg reports its on-demand
verb — not `reuse`, not `(no result)`.

**Left-shift gate.** `tools/run-gates/run-gates.test.sh` gains the `GATE_REUSE=1` plus on-demand arm,
and a control asserting no leg ever reports `(no result)` on a switch-off run.

## H3 — S4 does not choose the verb, and both naive choices break a downstream reader

`memory/builds/dUnstalledConvoy/spec/2026-08-23-spec-TOOL-dUnstalledConvoy-26.md:28-29` (S4) and
`:101-102` (AC3).

Reusing the guard's `skip` sentinel makes `report_one` print
`GATE skip  <name>  (unchanged vs main)` (`tools/run-gates/run-gates.sh:902`) for all 47 — a stated
reason that is false, on precisely the run where an operator needs to know why the bar shrank. It also
collapses the two populations into one number: the summary tail at `tools/run-gates/run-gates.sh:1055`
is a single `($skips skipped)`, and that same single number reaches `gate-last-summary.txt` and the
run record's `skipped` key.

Introducing a brand-new verb instead hits the closed set at `tools/run-gates/profile_bar.py:65`:
`VERDICT = re.compile(r"^GATE (ok|skip|FAIL|reuse)\s+(.*)$")`, and `parse_verdicts` drops
non-matching lines silently. The comment directly above it records that exact regression for
`GATE reuse` — "dropped every `GATE reuse` line silently, which under-counts the bar without reporting
anything". A new verb would also break `observed_skipped = ["GATE skip  {name}"]`
(`tools/run-gates/kit.toml:118`), which is how the deployer reads a target's verdicts.

A third route exists and the spec should name it: keep the `skip` verb (satisfying the regex, since
only the verb is closed) with a DISTINCT parenthesised tail, plus a separate tally. That satisfies
`profile_bar`, satisfies the two-space tail contract, and states a true reason.

**Fix.** S4 picks the verb and its tail text, and states that the on-demand count is reported
separately from the guard-skip count in stdout, in `gate-last-summary.txt`, and in the run record.
AC3 asserts both halves. Add `tools/run-gates/profile_bar.py` and its selftest to the change set.

**Left-shift gate.** An arm in `tools/run-gates/profile_bar.test.sh` asserting every verb the runner
can emit is counted by `parse_verdicts` — derived from the runner's own `report_one`, not from a typed
list. That gates the class the `GATE reuse` regression already demonstrated once.

## H4 — S7's both-directions rule cannot reach the eight exempt self-tests, and the spec picks neither build

`memory/builds/dUnstalledConvoy/spec/2026-08-23-spec-TOOL-dUnstalledConvoy-26.md:36-38` (S7) and
`:105-106` (AC5).

`tools/govkit/govkit.py:884-905` runs both directions over NAMES only: `claimed_legs` from descriptors
against the manifest, `exempt_legs` against the manifest, then `manifest - claimed - exempt`. An
`[[exempt_leg]]` row is by construction claimed by no descriptor, so there is no second spelling of
`on_demand` to compare against.

`registry.toml` carries 17 exempt rows. Eight are `chunk: selftests` and therefore inside S6's 47:
`branch-guard self-test`, `recall floor arms`, `dead-path carriers self-test`, `govkit selftest`,
`manifest-check self-test`, `run-gates gov canary`, `template size gate selftest`,
`playbook parity selftest`. One correction to the brief on this point: its list swapped
`recall floor arms` for `python resolver (behaviour + inline parity + idiom ban)`, and the resolver leg
is `chunk: wiring`, so it is NOT in the 47.

Taken literally — "on_demand in the manifest implies on_demand in its descriptor" — AC5 reds on all
eight. Scoped to claimed legs, which is the only workable build, it asserts nothing about them, and
S6's justification that the cross-check "keeps agreeing in both directions" is void over a fifth of
the manifest — including `run-gates gov canary`, whose arms are the only assertion that the push
boundary can still force at all.

**Fix.** Extend `[[exempt_leg]]` with a required `on_demand` boolean and make selfcheck refuse (a) a
manifest leg marked `on_demand` whose exempt row does not declare it, and (b) an exempt row declaring
`on_demand` that the manifest does not carry — the same both-directions shape, applied to the escape
hatch. State it in S7 and add it to AC5.

**Left-shift gate.** The extended check in `tools/govkit/govkit.py` selfcheck section 7h is itself the
gate; arm it in `tools/govkit/selftest.py` with a staged mismatch in each direction.

## H5 — AC6 is circular: the only derivable population is "legs declaring the flag"

`memory/builds/dUnstalledConvoy/spec/2026-08-23-spec-TOOL-dUnstalledConvoy-26.md:107-108` (AC6)
against `:19-22` (S1).

A `[[gate_leg]]` row is read by govkit for `name`, `argv`, `guard`, `red_after_land` and
`history_depth`, and nothing else. `[[files]]` roles across every shipped descriptor are only
engine / merged / project-owned / rendered / seed — nothing marks a test. The one in-tree derivation
of a self-test population, `tools/check-testsuite-counts.sh:36`, is exactly the `.test.sh`-in-argv
text predicate S1 bans, and the same argument kills a name-text predicate.

So "DERIVING the self-test population from each `kit.toml` and requiring every member to declare it"
is either the banned predicate or a read of `on_demand` itself, in which case it is true by
construction. An implementation marking 3 of the 39 descriptor legs passes AC6 unchanged. That is a
gate satisfied by its own declaration — the shape `AGENTS.md` §7 refuses by name.

**Fix.** Name a SECOND, independent source and grade the two against each other. The workable one: the
descriptor `on_demand` set must equal gov's manifest `chunk == "selftests"` set, plus an explicitly
listed set of exceptions each carrying its reason (the five legs of H1 and H6). Then AC6 has a
population it did not define itself, and a partial marking reds. Drop the word "deriving".

**Left-shift gate.** That equality, as an arm in `tools/govkit/selftest.py`. It also anchors H6's count
so the number never has to be typed anywhere.

## H6 — AC9 is not observable by its stated observer, and 47 is a prose count with no predicate

`memory/builds/dUnstalledConvoy/spec/2026-08-23-spec-TOOL-dUnstalledConvoy-26.md:113-114` (AC9) and
`:34` (S6).

Measured over `tools/gate-legs.json`: 35 legs carry `.test.sh` in an argv, 37 match `/self-?test/` in
the name, 12 carry a selftest token in an argv, and the union of all three is 48. No predicate yields
47. It is reproducible only as the union of `chunk == "selftests"` (42) and the five legs gov
classifies as `declarations` or `e2e` — which is a human judgment, not a rule.

So "loses exactly the self-test legs" cannot be graded: an implementation marking 42, or 24, satisfies
AC9 as written just as well as one marking 47. And "unchanged with the switch on" has no before-image
once the change lands — the pre-change bar cannot be re-run — so that half can only be a recollection.
The charter's own rule is that no count of a derived population is written in prose, and S5 one bullet
earlier says the population is derived rather than typed.

**Fix.** Restate AC9 mechanically. The set of on-demand-skipped leg NAMES on a switch-off run equals
the set of manifest rows carrying `on_demand`; the count is derived at emission time and never typed;
a switch-on run reports zero on-demand skips. Both halves are then a comparison a script makes. Give
S6 a RULE rather than a number: for a claimed leg the descriptor owns the flag and the manifest must
agree (that is S7); for an exempt leg the `[[exempt_leg]]` row owns it (that is H4). Then the manifest
carries no independently-authored population and the count disappears from the spec.

**Left-shift gate.** The name-set equality arm in `tools/run-gates/run-gates.test.sh`, plus H5's
descriptor/manifest equality in `tools/govkit/selftest.py`. Between them nothing is left to type.

## H7 — `govkit apply` refuses every upgrade re-apply against an already-adopted target, and AC7's arm structurally cannot see it

`memory/builds/dUnstalledConvoy/spec/2026-08-23-spec-TOOL-dUnstalledConvoy-26.md:109-110` (AC7).

`tools/govkit/govkit.py:2504-2509` fails with `leg '<n>' was green before and did not execute after —
the install broke its guard` on any green-to-skipped transition. Both maps come from
`read_gate_verdicts` (`tools/govkit/govkit.py:1691`), whose docstring says it runs WITHOUT the
run-everything escape, deliberately, so that a skipped leg stays observable. S3 and S4 report an
on-demand skip the way a skip is already reported, so the after-read classifies it `skipped` via
`observed_skipped = ["GATE skip  {name}"]`.

Any already-adopted target whose before-read returns green for these legs — a target with no
resolvable `origin/HEAD` (BASE empty, so `changed()` returns 0 for every leg) or one whose branch
already touched the kit dir — gets one refusal per migrated leg, and the upgrade cannot land.
`tools/govkit/matrix.py:228-232` installs into a fresh `git init` scratch repo, so `before_map` is
empty there and the arm is structurally unreachable on AC7's only observation path. The reachable class
is narrower than "every target" — one whose guards do scope reads `skipped` before and after, and no
refusal fires — but it is real and the spec handles it nowhere.

**Fix.** Teach the after-map check that green-to-skipped is EXPECTED when the emitted row declares
`on_demand` — the flag is already in scope in `emitted`. Add an AC covering re-apply over a target
that already had the leg green, i.e. the upgrade path, not only the scratch install.

**Left-shift gate.** A `tools/govkit/matrix.py` shape that applies twice — once into scratch, once over
the result with the flag newly set — and asserts the second apply lands. That is the upgrade path the
matrix does not currently cover for any field.

## H8 — nothing durable records that the switch was set, so two runs at one sha are indistinguishable in the record the boundary reads

`memory/builds/dUnstalledConvoy/spec/2026-08-23-spec-TOOL-dUnstalledConvoy-26.md:87` (§5
observability) and `:28-29` (S4, which puts the announcement only in stdout).

The run header already pairs value and source four times, deliberately: `base`/`base_from`,
`full`/`full_from`, `profile_row`/`profile_from`, `queued`/`queued_from`
(`tools/run-gates/run-gates.sh:761-790`). The comment at `:786-789` says why the fourth pair sits
OUTSIDE the run-envelope block: `run-gates.evidence.test.sh` asserts that block is four keys and
selects them by name, so an additive key outside it is safe. `full`/`full_from` exists for `GATE_FULL`
— an input of exactly the same class as `GATE_SELFTESTS`.

After this change, a 38-leg run and an 85-leg run at the same sha with the same manifest blob differ
in the verdict's `ran` and `skipped` counts (`tools/run-gates/run-gates.sh:1075-1077`) but nowhere say
WHY, and the `gate-full-green` stamp — the record `.githooks/pre-push` decides against — carries no
such field at all. A leg population decided by an unrecorded environment variable is the same class as
the `GOV_DEFAULT_BRANCH` fail-open the hook's own comment documents.

**Fix.** S4 gains the durable half: the header gains `selftests` / `selftests_from` (outside the
four-key envelope block, as `queued` already is), the verdict gains an `ondemand_skipped` count, and
the stamp records the population it was earned on — which is also B1's fix. Add an AC observing the
header key.

**Left-shift gate.** `tools/run-gates/run-gates.evidence.test.sh` already grades the header's key set
by name; add the pair to it, and keep the arm that the envelope block is still exactly four keys so
the new pair cannot be added in the wrong place.

---

# MEDIUM

## M1 — the empty-population refusal is a predicate over the manifest; its observable is a run outcome, and the two diverge

`memory/builds/dUnstalledConvoy/spec/2026-08-23-spec-TOOL-dUnstalledConvoy-26.md:85-86` (§5) and
`:103-104` (AC4).

There is no zero-leg refusal in the runner today. With every leg guard-skipped,
`tools/run-gates/run-gates.sh:1126` prints `gates GREEN — 0/0 legs passed (85 skipped)` and exits 0,
and pre-push accepts it. The only empty-population check is on the manifest FILE
(`tools/run-gates/run-gates.sh:676`), which a fully on-demand manifest passes.

Built on the manifest property, the identical zero-executed state stays reachable the other way: a
manifest of 84 on-demand legs plus one guarded leg whose guard does not fire executes zero legs and
does not meet the stated condition. Built on the run outcome without care, it reds every legitimate
all-guard-skipped scoped run. Either way, one zero-leg bar refuses and an identical one reports green,
which is a worse signal than either rule alone.

The runner already implements the correct predicate one level down: `chunk_close`
(`tools/run-gates/run-gates.sh:966-968`) reds a chunk to `skipped` when
`c_ran == 0 && c_reuse == 0 && c_skip > 0`, with a comment calling the alternative "the loudest
possible green-by-absence".

**Fix.** State the refusal over the RUN, over non-sentinel rows: zero legs ran AND zero reused is a
refusal, whatever mixture of guard and switch produced it. Restate AC4 against that condition, add the
mixed-source negative control (one guarded leg unchanged plus one on-demand leg, switch off), and say
EXPLICITLY whether the existing all-guard-skipped green becomes a refusal too — it is the same
green-by-absence and it is in this diff's blast radius either way.

**Left-shift gate.** `tools/run-gates/run-gates.test.sh` arms for all three zero-leg routes: guards
only, switch only, and mixed.

## M2 — two shipped kits become un-adoptable standalone, and `govkit apply` refuses into such a target

`memory/builds/dUnstalledConvoy/spec/2026-08-23-spec-TOOL-dUnstalledConvoy-26.md:85-86` (§5).

`tools/hooks/kit.toml` declares exactly two legs, both self-tests (`scratch-guard self-test`,
`agent-cap self-test`). `tools/pytest-parallel-guardrails/kit.toml` declares exactly one, a self-test.
A target adopting either or both, with its own manifest runner, gets a manifest whose every row is
`on_demand` — so under §5 its merge bar refuses on every invocation until the operator sets
`GATE_SELFTESTS=1`, with nothing in the refusal path telling them so. Second-order:
`tools/govkit/govkit.py:2043-2048` raises `DEAD PROBE` when the baseline read parses legs and not one
is green or red, so `govkit apply` into such a target refuses as well — and `on_demand` makes that
permanent, where guards at least fire situationally.

**Fix.** Require the refusal message to name `GATE_SELFTESTS=1`. Add the all-on-demand adopter to §5's
migration note as a known shape, and say what an adopter of only `agent-cap` is expected to do.

**Left-shift gate.** A `tools/govkit/matrix.py` shape that installs `agent-cap` alone and asserts the
target's bar and `govkit apply` both give an actionable refusal rather than a bare `DEAD PROBE`.

## M3 — no scope item builds AC7: the emitter deliberately drops every descriptor field but name, argv and a non-empty guard

`memory/builds/dUnstalledConvoy/spec/2026-08-23-spec-TOOL-dUnstalledConvoy-26.md:109-110` (AC7).

`tools/govkit/govkit.py:2451` builds `row = {"name": nm, "argv": argv}` and adds `guard` only when
non-empty. `impure`, `chunk`, `history_depth` and `red_after_land` are all dropped today. Without an
explicit scope item the flag stops at the descriptor and never reaches an adopter's emitted manifest —
which is the whole point of the unit — while AC7 is the only place that requirement appears at all.
Separately, the receipt at `tools/govkit/govkit.py:2466` records
name/kit/argv/guard/guard_dropped/history_depth, and the drift comparison at
`tools/govkit/govkit.py:2458` tests argv and guard only, so a target that flips the flag by hand is
invisible to the next apply.

**Fix.** Add a scope item: the emitter carries `on_demand` into the target's manifest row AND into the
`emitted` receipt entry, and the receipt-drift comparison at `:2458` includes it.

**Left-shift gate.** Extend the existing matrix arm that reads the target's emitted `gate-legs.json` to
assert the flag survived, and add a receipt-drift arm that hand-flips the flag in a target and expects
a reported drift.

## M4 — the manifest key set is a CLOSED pin in two places; adding the key reds the canary, and §10 names no consumer

`memory/builds/dUnstalledConvoy/spec/2026-08-23-spec-TOOL-dUnstalledConvoy-26.md:145-148` (§10, "a
fifth in the same shape").

`tools/run-gates/run-gates.test.sh:96` and `:125` both hardcode
`KNOWN = {"name", "argv", "guard", "impure", "chunk"}` — once in the canary predicate, once in its
arming control — and the predicate exits 1 on any row carrying a key outside the set, graded against
the tree's real manifest (`LEGS_FILE`, `:55`). Adding `on_demand` to `tools/gate-legs.json` reds
`run-gates canary` until both copies are edited. The reuse audit claims the wire format "already
carries four optional fields and this adds a fifth in the same shape" and names neither site.

Worse afterwards: that pin exists to catch a near-miss spelling (`on_demmand`, `On_demand`), and
`run-gates canary` is itself in the 47 — so once the flag lands with the switch off, the manifest the
switch rides on is unvalidated on every default and every `GATE_FULL` bar. The mis-spelling's failure
direction is benign (a typo'd flag reads as not-on-demand, so the leg still runs), which is what caps
this below blocker; the coverage loss belongs to H1.

**Fix.** Name both `KNOWN` sites in the change set explicitly, and add the near-miss control for
`on_demand` beside the existing `impur` one so the new key is armed the same way the old one is.

**Left-shift gate.** Derive `KNOWN` once in that file rather than typing it twice — a single constant
consumed by both the predicate and its arming control removes the class.

## M5 — §3 says `chunk` is untouched; `chunk` is the wire format's LAST field, so a sixth field necessarily changes how it parses

`memory/builds/dUnstalledConvoy/spec/2026-08-23-spec-TOOL-dUnstalledConvoy-26.md:52` (§3) against
`:56-59` (§4).

The emitter at `tools/run-gates/run-gates.sh:690-693` writes
`name \x1e guard \x1e argv \x1e impure \x1e chunk`, and the reader at
`tools/run-gates/run-gates.sh:701` is `IFS=$'\x1e' read -r nm gd_ av im ch <<<"$line"` — five variables
for five fields. `read` puts every remaining field into the LAST variable, so appending `on_demand`
after `chunk` without adding a sixth variable silently makes `chunks[i]` become `selftests\x1e1`. That
corrupts the chunk-boundary comparison at `tools/run-gates/run-gates.sh:984` and the chunk rollup, and
it does so with no parse error anywhere.

The rest of §4's trace holds: the 1:1 row correspondence and the empty-name drop sentinel
(`tools/run-gates/run-gates.sh:698-703`) survive an appended field untouched, and the dispatch hint is
keyed on leg NAME by the python side, so the timing cache is unaffected.

**Fix.** §3 stops claiming `chunk` is untouched and says instead that `chunk` keeps its MEANING while
its read gains a sixth variable. State the field order explicitly in §4.

**Left-shift gate.** An arm in `tools/run-gates/run-gates.test.sh` asserting the reader's variable count
equals the emitter's field count, derived from both sources rather than typed — that gates every future
field addition, not this one.

---

# LOW

## L1 — F2 falsifies `run_all_env`, a declaration the deployer's completeness check rests on

`memory/builds/dUnstalledConvoy/spec/2026-08-23-spec-TOOL-dUnstalledConvoy-26.md:50-51` (F2 in §3) and
`:129-131` (F2 resolved).

`tools/run-gates/kit.toml:105-108` declares `run_all_env = "GATE_FULL=1"` under the comment "The
environment that makes a run TOTAL. Required by the deployer for a complete `manifest` promotion; a
partial one is refused rather than silently accepted." `tools/govkit/govkit.py:1637` lists
`run_all_env` in `GR_REQUIRED` and `:1662` refuses a promotion missing it — but checks PRESENCE only,
never truth. After F2 the declared total-run environment leaves 29 legs unrun in every adopter, and
`tools/govkit/govkit.py:2954` seeds the claim onward into each target's `deploy.toml`.

§5's help/docs row names the install summary, `tools/run-gates/README.md` and `AGENTS.md`, and not this
file.

**Fix.** Either set `run_all_env = "GATE_FULL=1 GATE_SELFTESTS=1"` in the seed, or rewrite the comment
to say what "total" now excludes and why. Add `tools/run-gates/kit.toml` to §5's help/docs row.

**Left-shift gate.** None worth building — a truth check on `run_all_env` would have to run the
target's whole bar twice. This is a documented check: the descriptor comment is the record, and
`govkit selfcheck`'s existing presence check stays as it is.

---

## What was refuted, and why it is worth saying

Six of forty raw findings did not survive the skeptic. Two are worth recording, because both are
places where a lens overstated a real defect and the residue is what the report kept.

- A claim that the missing announcement made 38-leg and 85-leg runs "byte-indistinguishable in every
  durable record" — false. The verdict file records `ran` and `skipped`
  (`tools/run-gates/run-gates.sh:1075-1077`), so the SIZE of the difference is visible; only its cause
  is not. H8 is narrowed to that residue.
- A claim that the drop-sentinel rows would break the empty-population predicate — weak. The canary's
  first arm already forbids an empty-name leg in a tracked manifest, so the sentinel is a rendered-
  adopter shape rather than a gov one. The predicate should still exclude them, which M1's fix does.

## Recommendation

Return to rev-2. The mechanism is right and the measurements behind it are right; what is missing is
three decisions the spec leaves to the builder, and one population that is the wrong set. In priority
order:

1. Decide the `skips`-versus-stamp question (B1). It is the only finding whose wrong branch degrades
   the merge bar's authorization record rather than merely costing coverage.
2. Re-derive the population over every descriptor `read_descriptors` returns, and state the membership
   CRITERION rather than counts (B2, H1, H6). Most of the other findings dissolve once the criterion
   exists.
3. Fix §7 and AC11 so this unit's own evidence is not produced by the legs it disables (B3).
4. Name the seam, the verb, and the durable record (H2, H3, H8) — three sentences, each replacing a
   builder coin-flip.

Nothing here argues against the owner's ruling. It argues that the ruling applies to a smaller set
than the spec currently names, and that turning legs off requires deciding what the record of a green
bar means afterwards.
