# TOOL-aQuenchedHarness-7 — the longest leg on the bar is a repo check the hold never reaches

**Status:** OPEN · rev-1 · 2026-09-06 · node a · Tier-2 · base faaea5f5 · streams tooling · order 7

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Bring `unattended kit gate` down to a declared budget. It is the single most expensive leg in
`tools/gate-legs.json` at its last recorded reading, it carries `subject = repo` so the self-test
hold never touches it, and wall clock cannot fall below the longest leg however wide the pool is — so
this one leg puts a floor under every full bar in the repository.

## 2. Scope (IN)

- **S1** — PROFILE it before changing it: an execution trace attributing its wall clock to process
  creations, with the count per loop site. The number is the artifact; the fix follows from it.
- **S2** — remove the per-item spawns the trace names, by the mechanism this repo has already used
  twice: read each file once instead of running a `grep`, an `awk` or a `git` per (item, file). The
  leg walks every tracked `RUN*.md` under `memory/builds/`, and its cost scales with that population,
  which grows monotonically as builds land.
- **S3** — a declared budget for it in `tools/run-gates/selftest-budgets.txt`, or — since it is a
  repo check and not a self-test — in whichever declaration `TOOL-aQuenchedHarness-4` gives repo
  legs, with the reading beside it. It already has one in
  `tools/unattended/run-unattended-gates.sh` (`BUDGET_kit_gate`), and that value and the leg's
  `ceiling` in `tools/gate-legs.json` must stop being two answers to one question.
- **S4** — the same treatment for `pass-order history`, its sibling in the same kit and the same
  shape: `subject = repo`, no hold, and a recorded cost the ledger names. `TOOL-aStagedLane-1`
  already widened its population, and this repo's own memory records the class — a git spawn per
  commit turned one leg into hours until the spawns were counted.
- **S5** — a spawn-count REGRESSION arm: the leg's spawn count over a fixed fixture is pinned, so a
  future edit that reintroduces a per-item spawn reds instead of merely getting slower. Slowness that
  only annoys never gets fixed.
- **S6** — no check is removed and no check's verdict changes. The before/after comparison is the
  leg's own output over the real tree, byte-identical.

## 3. Non-goals (OUT)

- Not making the leg a self-test or holding it off the bar. It reads the REPOSITORY's run records,
  which go stale with nobody editing the kit, and `tools/unattended/run-unattended-gates.sh`'s header
  states exactly why that class stays on the bar. Holding it would be the wrong fix and the owner
  ruling of 2026-08-23 already draws this line.
- Not the other repo-subject legs on the bar beyond S4's sibling. `memory hygiene` and
  `govkit acceptance matrix` are the next two by recorded cost and are a follow-up backlog row, not
  scope here.
- Not fixing `TOOL-aBoundedCeiling-9`, the separate reason this leg has been RED on main. That is its
  own defect with its own row and this unit must not quietly absorb it — though the profiling work
  will confirm whether it still reproduces.

## 4. Design

### The method, which is not a guess

`memory/gotchas/process-creation-is-the-suite-cost.md` records the diagnosis and this repo has
applied the fix twice with measurements on both sides. The trace in S1 answers WHERE, and the
transformation is mechanical once it does: hoist a per-item `git` or `grep` out of the loop, read the
file once, and do the per-item work in the shell or in one `awk` pass.

### Data model

No data change. The leg's checks, their order and their verdicts are unchanged; only the number of
processes used to reach them moves.

### Inventory

- The profile artifact, under `memory/builds/aQuenchedHarness/build/`, naming spawns per loop site
  before and after.
- The spawn pin and its arm, in `tools/unattended/check-unattended.test.sh`, which is a held
  self-test and therefore does not itself join the bar.

### Files touched (estimate)

`tools/unattended/check-unattended.sh` · `tools/unattended/check-pass-order.sh` ·
`tools/unattended/check-unattended.test.sh` · `tools/unattended/run-unattended-gates.sh` (the budget
row) · `tools/gate-legs.json` (the ceiling, via `TOOL-aQuenchedHarness-2`'s derivation) · one build
record.

### Alternatives rejected

Raising the ceiling was rejected on this repo's own history: three sessions raised `pass-order`'s
ceiling before anybody counted its spawns, and counting them took it from 10184 s to 510 s. A ceiling
raise is what a team does instead of fixing the leg, and this build exists because that happened.

## 5. Production-readiness checklist

- security — N/A: the same checks over the same files.
- perf / scale — the unit's subject. The population grows with every landed build, so a per-item
  spawn is a cost that compounds, which is why the pin in S5 matters more than the one-time fix.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — unchanged; no check's report shape moves.
- observability — the spawn count becomes a reported number rather than an inference.
- risks — the real hazard is a refactor that changes a verdict while making the leg faster. S6's
  byte-identical output comparison over the real tree is the guard, and it is a comparison rather
  than a review.
- testing + left-shift gates — S5's spawn pin is the left-shift: the CLASS gets a gate, not the
  instance.
- migration / rollback — one commit per checker, revertible independently.
- user docs — none owed; `AGENTS.md`'s measured-cost paragraph is refreshed by
  `TOOL-aQuenchedHarness-4`'s work, not restated here.

## 6. Acceptance criteria

- **AC1** — When `bash tools/unattended/check-unattended.sh` runs over the real tree before and after
  the change, its stdout and exit status are byte-identical, proving no verdict moved.
- **AC2** — When `bash tools/unattended/check-unattended.sh` is run under the spawn counter, its
  process count falls by a factor the build record states, measured on the same node in the same conditions as the baseline.
- **AC3** — When a per-item spawn is reintroduced into a loop, the pinned-count arm in
  `tools/unattended/check-unattended.test.sh` reds — the gate's own failing case, observed before
  landing.
- **AC4** — When `bash tools/unattended/run-unattended-gates.sh --checks` runs, `kit gate` is inside
  its declared `BUDGET_kit_gate`, and that value and the leg's `ceiling` in `tools/gate-legs.json`
  are joined rather than independently authored.
- **AC5** — When the same treatment is applied to `check-pass-order.sh`, `pass-order history`
  likewise produces byte-identical output and a lower spawn count.

## 7. Gates

`bash tools/run-gates/run-gates.sh` · `unattended kit gate` and `pass-order history`, the two legs
this unit changes · `bash tools/unattended/run-unattended-gates.sh --all` at the Definition of Done,
which is this kit's declared compensating check · `GATE_SELFTESTS=1` for the kit's held suites.

## 8. Open questions

- **F1 — FACT-QUESTION · is the cost per-file or per-check?** The probe is S1's trace: attribute the
  spawn count to loop sites and read whether it scales with the tracked `RUN*.md` population or with
  the check count. The observation that decides it is the attribution table; the liveness assertion
  is that a trace producing no attribution at all is reported as a failed probe, not as an absence of
  spawns. Resolved by measurement during the build.
- **F2 — does `TOOL-aBoundedCeiling-9` still reproduce?** RESOLVED (agent, 2026-09-06, delegated):
  observe it while profiling and RECORD the answer against that row, but do not fix it here. A unit
  that absorbs a neighbouring defect makes both unreviewable, and §3 already draws that line.

## 9. Revision log

- rev-1 · 2026-09-06 · initial draft.

## 10. Reuse audit

The seam is `tools/unattended/check-unattended.sh` itself, extended in place rather than replaced,
together with the spawn-reduction technique already applied to this same kit and recorded in
`tools/unattended/run-unattended-gates.sh`'s header — 469 spawns per invocation reduced to 220 by
reading each file once. `tools/codebase-map/reuse_lookup.py` returned `.unattended.conf` [unattended]
as the affordance seam for this area. Nothing new is built: this unit applies a recorded fix to a
second instance of a recorded class, and adds the pin that stops the class returning, which is
charter §7's left-shift rule applied to cost rather than to correctness.

Recall terms used: `selftest gate leg ceiling guard GATE_SELFTESTS run-gates scratch repo mktemp
spawn wall-clock adopter kit.toml`
