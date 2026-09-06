# TOOL-aQuenchedHarness-7 — the longest leg on the bar is a repo check the hold never reaches

**Status:** OPEN · rev-3 · 2026-09-06 · node a · Tier-2 · base faaea5f5 · streams tooling · order 8

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-06-review-TOOL-aQuenchedHarness-1-spec-audit-round1.md](../reviews/2026-09-06-review-TOOL-aQuenchedHarness-1-spec-audit-round1.md) | spec-audit | TOOL-aQuenchedHarness-1 TOOL-aQuenchedHarness-2 TOOL-aQuenchedHarness-3 TOOL-aQuenchedHarness-4 TOOL-aQuenchedHarness-5 TOOL-aQuenchedHarness-6 |
| [2026-09-06-review-TOOL-aQuenchedHarness-1-spec-audit-round2.md](../reviews/2026-09-06-review-TOOL-aQuenchedHarness-1-spec-audit-round2.md) | spec-audit | TOOL-aQuenchedHarness-1 TOOL-aQuenchedHarness-2 TOOL-aQuenchedHarness-3 TOOL-aQuenchedHarness-4 TOOL-aQuenchedHarness-5 TOOL-aQuenchedHarness-6 TOOL-aQuenchedHarness-8 |

<!-- /gen:spec-records -->

## 1. Goal

Bring `unattended kit gate` down to a DECLARED target. It is the most expensive leg in
`tools/gate-legs.json` at its last recorded reading, it carries `subject = repo` so the self-test
hold never touches it, and wall clock cannot fall below the longest leg however wide the pool is — so
this one leg puts a floor under every full bar in the repository, and it is what makes the turnstile
cliff `TOOL-aQuenchedHarness-8` fixes reachable in the first place.

## 2. Scope (IN)

- **S1** — PROFILE it before changing it: an execution trace attributing its wall clock to process
  creations, with the count per loop site. The number is the artifact; the fix follows from it.
- **S2** — remove the per-item spawns the trace names, by the mechanism this repo has already used
  twice: read each file once instead of running a `grep`, an `awk` or a `git` per (item, file). The
  leg walks every tracked `RUN*.md` under `memory/builds/` — 49 today — and its cost scales with a
  population that grows monotonically as builds land.
- **S3** — DECLARE the target before doing the work: a post-change recorded-seconds figure and a
  post-change spawn count, both written into §2 with the reading they were derived from, and a
  requirement that `BUDGET_kit_gate` be LOWER after this unit than the 240 it carries now. Without a
  declared figure every acceptance criterion here passes on a 1.01x change.
- **S4** — a spawn-count REGRESSION arm pinning a NORMALISED count — spawns per `RUN*.md` walked —
  with the population size DERIVED at run time and printed beside it. An absolute pin is wrong here
  and S2 says why: the same spec states the population grows monotonically as builds land, so an
  absolute number would red on a landing that merely added a build, and would then be raised — in the
  build that exists because three sessions raised a pin instead of counting spawns. The seconds figure
  in S3 stays a READING; the normalised spawn figure is the GATE, and its denominator is derived,
  never typed.
- **S5** — `check-pass-order.sh` gets the PIN and not the rebuild. Its spawn removal already landed
  and is in this build's base: `4042505a` and `274aa39b` record 10184 s to 591 s to 510 s, one pass
  over history into a subject cache, summary byte-identical, self-test green at 72 arms. This unit
  pins that win against erosion and re-derives the leg's residual cost from the reading; it does not
  redo it.
- **S6** — no check is removed and no check's verdict changes. The before/after comparison is the
  leg's own stdout and exit status over the real tree, byte-identical.

## 3. Non-goals (OUT)

- Not making the leg a self-test or holding it off the bar. It reads the REPOSITORY's run records,
  which go stale with nobody editing the kit, and `tools/unattended/run-unattended-gates.sh`'s header
  states why that class stays on the bar. The owner ruling of 2026-08-23 already draws this line.
- Not rebuilding `check-pass-order.sh`. S5 states why: it is done, and its one remaining per-item
  spawn is a `git show` the rebuild's own message refuses to remove because translating the anchored
  exclusions into globs would risk the verdict to save about 70 s.
- Not the other repo-subject legs. `memory hygiene` and `govkit acceptance matrix` are the next two by
  recorded cost and are a follow-up backlog row, not scope here.
- Not fixing `TOOL-aBoundedCeiling-9`, the separate reason this leg has been RED on main. Its own
  defect, its own row; the profiling will confirm whether it still reproduces and will say so.

## 4. Design

### The method, which is not a guess

`memory/gotchas/process-creation-is-the-suite-cost.md` records the diagnosis and this repo has
applied the fix twice with measurements on both sides. The trace in S1 answers WHERE, and the
transformation is mechanical once it does: hoist a per-item `git` or `grep` out of the loop, read the
file once, and do the per-item work in the shell or in one `awk` pass.

### The budget and the ceiling are TWO figures, and this unit stops pretending otherwise

Rev-1 asked `BUDGET_kit_gate` and the leg's `ceiling` in `tools/gate-legs.json` to "stop being two
answers to one question". They are two answers to two questions, and three other carriers say so:
`TOOL-aQuenchedHarness-2` §3, `TOOL-aQuenchedHarness-4` §3, and `run-unattended-gates.sh`'s own
comment — "that row is a kill bound and this one is a cost verdict. The claim that they are one
figure was deleted with this edit."

So there is no join. Each carrier gains a POINTER to the other and one sentence saying why the two
differ: the ceiling is a kill bound sized against the 8-wide pool's worst reading, the budget is a
cost verdict calibrated idle. `BUDGET_kit_gate` stays where it is, in `run-unattended-gates.sh`,
which `TOOL-aQuenchedHarness-4` S7 keeps rather than dissolving.

### Inventory

- The profile artifact, under `memory/builds/aQuenchedHarness/build/`, naming spawns per loop site
  before and after.
- The spawn pins and their arms, in `tools/unattended/check-unattended.test.sh` and
  `tools/unattended/check-pass-order.test.sh`, both held self-tests that do not join the bar.

### Files touched (estimate)

`tools/unattended/check-unattended.sh` · `tools/unattended/check-unattended.test.sh` ·
`tools/unattended/check-pass-order.test.sh` · `tools/unattended/run-unattended-gates.sh` (the budget
row and its pointer) · `tools/gate-legs.json` (its ceiling, via `TOOL-aQuenchedHarness-2`) · one
build record.

### Alternatives rejected

Raising the ceiling was rejected on this repo's own history: three sessions raised `pass-order`'s
ceiling before anybody counted its spawns, and counting them took it from 10184 s to 510 s. A ceiling
raise is what a team does instead of fixing the leg, and this build exists because that happened.
Rev-1 said so in prose and then wrote acceptance criteria that a re-declaration would satisfy, which
is the gate-satisfied-by-its-own-comment shape; S3 replaces the prose with a number.

## 5. Production-readiness checklist

- security — N/A: the same checks over the same files.
- perf / scale — the unit's subject. The population grows with every landed build, so a per-item
  spawn compounds, which is why S4's pin matters more than the one-time fix.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — unchanged; no check's report shape moves.
- observability — the spawn count becomes a reported, pinned number rather than an inference.
- risks — a refactor that changes a verdict while making the leg faster. S6's byte-identical
  comparison over the real tree is the guard, and it is a comparison rather than a review.
- testing + left-shift gates — S4's spawn pins are the left-shift: the CLASS gets a gate, not the
  instance.
- migration / rollback — one commit per checker, revertible independently.
- user docs — none owed.

## 6. Acceptance criteria

- **AC1** — When `bash tools/unattended/check-unattended.sh` runs over the real tree before and after
  the change, its stdout and exit status are byte-identical, proving no verdict moved.
- **AC2** — When `bash tools/unattended/check-unattended.sh` is run under the spawn counter after the
  change, its NORMALISED count — spawns divided by the `RUN*.md` population derived at run time — is
  at or below the figure S3 declares — an absolute number written before the work, not "a factor the build
  record states".
- **AC3** — When `unattended kit gate` is timed after the change in the conditions S3 names, its
  recorded seconds are at or below S3's declared target, and `BUDGET_kit_gate` in
  `tools/unattended/run-unattended-gates.sh` is LOWER than the 240 it carries today.
- **AC4** — When a per-item spawn is reintroduced into a loop, the pinned-count arm in
  `tools/unattended/check-unattended.test.sh` reds — the gate's own failing case, observed before
  landing.
- **AC5** — When `bash tools/unattended/check-pass-order.sh` is run under the spawn counter, its count
  normalised count is at or below the pin S5 records for the ALREADY-LANDED rebuild, so `274aa39b`'s win cannot
  silently erode. This is a regression assertion, not an improvement claim.
- **AC6** — When `tools/unattended/run-unattended-gates.sh` and `tools/gate-legs.json` are read, each
  carries a pointer to the other's figure for this leg and one sentence saying why the two differ.

## 7. Gates

`bash tools/run-gates/run-gates.sh` · `unattended kit gate` and `pass-order history`, the two legs
this unit touches · the `lexicon naming predicates` leg, which grades any new shell function the
rewrite defines and the `VERB_OFFENDER_PIN` move it forces ·
`bash tools/unattended/run-unattended-gates.sh --all` at the Definition of Done,
which is this kit's declared compensating check · `GATE_SELFTESTS=1` for the kit's held suites.

## 8. Open questions

- **F1 — FACT-QUESTION · is the cost per-file or per-check?** The probe is S1's trace: attribute the
  spawn count to loop sites and read whether it scales with the tracked `RUN*.md` population — 49
  files today — or with the check count. The observation that decides it is the attribution table;
  the liveness assertion is that a trace producing no attribution at all is reported as a FAILED
  PROBE, not as an absence of spawns. Resolved by measurement during the build, and S3's declared
  target is written from it before any code changes.
- **F2 — does `TOOL-aBoundedCeiling-9` still reproduce?** RESOLVED (agent, 2026-09-06, delegated):
  observe it while profiling and RECORD the answer against that row, but do not fix it here. A unit
  that absorbs a neighbouring defect makes both unreviewable.
- **F3 — is `pass-order history` still worth attention after the landed rebuild?** RESOLVED (agent,
  2026-09-06, delegated): not as a rebuild. At 591 s recorded it is sixth by cost, behind four held
  self-tests, so the remaining work in this area is units 5 and 6's, not this unit's. S5 pins it and
  stops.

## 9. Revision log

- rev-1 · 2026-09-06 · initial draft.
- rev-3 · 2026-09-06 · folded spec-audit round 2. H7: the spawn pin is NORMALISED — spawns per
  `RUN*.md` walked, denominator derived at run time — because the same spec says the population grows
  monotonically, so an absolute pin would red on a landing and then be raised, which is the exact
  habit this unit exists to end. H3: §7 names the lexicon leg.
- rev-2 · 2026-09-06 · folded spec-audit round 1. H8: S4's `check-pass-order.sh` rebuild ALREADY
  LANDED in this build's base at `4042505a`/`274aa39b`, 10184 s to 510 s; S5 replaces it with a
  regression pin and AC5 is now an assertion against that pin rather than an improvement claim. H7:
  S3 declares an absolute target and an absolute spawn count BEFORE the work, and AC3 requires
  `BUDGET_kit_gate` to fall — rev-1's criteria were all satisfiable by a 1.01x change or by a
  sanctioned budget re-declaration. H5: the budget/ceiling JOIN is withdrawn; the two are a cost
  verdict and a kill bound, three carriers already say so, and each now carries a pointer to the
  other with the reason they differ. §3 records what the before-state is, including that the idle
  budget is calibrated idle.

## 10. Reuse audit

The seam is `tools/unattended/check-unattended.sh` itself, extended in place rather than replaced,
together with the spawn-reduction technique already applied to this same kit and recorded in
`tools/unattended/run-unattended-gates.sh`'s header — 469 spawns per invocation reduced to 220 by
reading each file once. `tools/codebase-map/reuse_lookup.py` returned `.unattended.conf` [unattended]
as the affordance seam for this area. The second instance of that technique is `check-pass-order.sh`'s
own rebuild, landed at `274aa39b` and in this build's base — which rev-1 cited as history in §4 while
scheduling the same work in §2, and which the audit caught. Nothing new is built: this unit applies a
recorded fix to a remaining instance of a recorded class, and adds the pins that stop the class
returning, which is charter §7's left-shift rule applied to cost rather than to correctness.

Recall terms used: `selftest gate leg ceiling guard GATE_SELFTESTS run-gates scratch repo mktemp
spawn wall-clock adopter kit.toml`
