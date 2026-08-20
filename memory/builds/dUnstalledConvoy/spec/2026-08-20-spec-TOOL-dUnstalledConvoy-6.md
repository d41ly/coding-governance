# TOOL-dUnstalledConvoy-6 — the leg refuses a roster amendment with no record behind it, and announces the case it cannot compare

**Status:** SPECCED · rev-2 · 2026-08-20 · node d · Tier-2 · base 2dc9df35 · streams tooling

## 1. Goal

Once a run may amend its own scope, the failure mode moves from stalling to drifting: a unit quietly
retired because it was inconvenient, with nothing in the record saying so. This unit adds one check
to the unattended gate that compares the roster at the run's pinned BASE against the roster now, and
refuses any transition no `rescope` row accounts for.

## 2. Scope (IN)

- **S1** — a new check inside `tools/unattended/check-unattended.sh`, not a new gate leg. It runs
  inside the existing anchor loop, where the recorded BASE and the build README are already resolved.
- **S2** — for each live run, the check derives two id sets from the build README's generated units
  region: the set at the recorded BASE, and the set at HEAD. Every id present at HEAD and absent at
  BASE must be accounted for by EITHER an `add` row naming it OR a `supersede` row naming it as the
  successor. Review fold: H3. Requiring an `add` alone made a correctly performed supersession red the
  bar: the successor is present at HEAD, absent at BASE, and the sibling verb refuses an `add` for an
  id already in the region, so the run had no legal repair.
- **S2a** — the comparison EXCLUDES an id whose spec was first committed at or before the commit where
  the run entered `BUILDING`. Review fold: H4. Keying the exemption on the phase AT CHECK TIME buys
  nothing, for two independent reasons the audit measured: the window is BASE-to-HEAD regardless of
  phase, so a spec authored during `SPECCING` is still absent at BASE once the run advances; and the
  authoritative run of this leg is the full bar at the push boundary, where `--close` has already set
  the phase to `LANDING`, which is `BUILDING` onward. A run that classified a unit MISSING and
  authored its spec — which M2 MANDATES — would red for obeying the method. The prompt-authorized
  mode makes it sharper: such a run starts with an empty units region at BASE, so every spec it
  legitimately authors would be unaccounted for.
- **S3** — for each unit whose status is `WONTDO` at HEAD and was not `WONTDO` at BASE, a
  `rescope · item retire <id>` or `rescope · item supersede <id> -> <successor>` row must exist.
- **S4** — a `supersede` row whose successor id is absent from the HEAD units region is a refusal. A
  supersession that never landed its replacement is a retirement wearing a better name.
- **S5** — the check does NOT re-implement the removal refusal. `check_authorization` already refuses
  a narrowed id set and `authorization-reachable` has no override, so a second copy here would
  recompute the driver's answer from the driver's inputs.
- **S6** — every case the check cannot compare ANNOUNCES itself with a named skip line: no recorded
  BASE, a BASE blob with no units region, a malformed marker pair on either side, or a BASE dated
  before `UNITS_REGION_CUTOFF`.
- **S6a** — **THIS UNIT OWNS THE LEG OUTPUT CONTRACT, and amends it in the same commit as the first
  skip line.** Review fold: H1, owner decision 2026-08-20. The leg header states that exit 0 with no
  output is clean and that anything printed is a violation, and its sibling test hard-asserts empty
  output in three places under a runner that folds stderr into stdout, so no channel escapes it. Four
  units in this build specify an announced skip; under the reordered plan this one lands first, so it
  decides the mechanism ONCE and the other three cite it. The disposition: a skip line is emitted on a
  dedicated REPORT channel the default run does not print, and the contract sentence gains that
  exception explicitly rather than being quietly falsified. The three green-control arms are amended
  in the same commit and NONE is deleted — deleting the green control removes the arm that makes every
  other arm in that file meaningful.
- **S7** — the check's header states what it does not buy, per the rule that a gate's header states
  what it does NOT check.

## 3. Non-goals (OUT)

- Grading whether an amendment was WISE. The check reads structure, never judgement.
- Grading a `rescope` row with no corresponding transition. A run may record an amendment and then
  find it unnecessary, and refusing that would punish a run for changing its mind honestly. The row
  is surfaced in the wrap-up either way.
- Any check on an attended build. The check runs per live run-state file, so a build with no run has
  no subject here.
- Terminal records. A finished record is frozen and its roster moved on; grading it would red a run
  that landed correctly months earlier.

## 4. Design

### Inventory

| Transition at HEAD versus BASE | Required row | Absent row |
|---|---|---|
| id present now, absent at BASE | `rescope · item add <id>` | refusal naming the id |
| status now `WONTDO`, not `WONTDO` at BASE | `retire <id>` or `supersede <id> -> <succ>` | refusal naming the id and both acts |
| `supersede` row whose successor is absent at HEAD | — | refusal naming the successor |
| id absent now, present at BASE | none — owned by `check_authorization` | silent here, by S5 |
| BASE unreadable or pre-cutoff | none | named SKIP line |

### What this check cannot buy, and why it is still worth adding

It detects an amendment made with NO record. It cannot detect a record that is truthful in shape and
false in substance, because both of its inputs are inside the run's reach: the run wrote the rows and
the run made the edits. This repo already names that class — a check whose inputs are all supplied by
the thing it distrusts is not a check, however sound its logic.

What makes it worth adding anyway is that the two inputs are produced by different acts at different
times, so the cheap failure — retiring a unit and saying nothing — is caught, while the expensive
failure requires a run to deliberately author a matching lie. The header says exactly that, in those
terms, so nobody reads a green row as proof the amendment was honest.

### Why a check and not a leg

Adding a gate LEG trips a set of meta-gates that grows as new legs land, and costs a manifest row, a
kit descriptor row and a coverage assert. A new check inside an existing gate costs an `ARMS_FLOORS`
bump and one arm per `fail` call site. This is a recorded trap in the kickoff manifest, and units 11
and 13 in this build make the same choice for the same reason.

### The skip is the correctness risk

A comparison between two id sets is vacuously satisfied when either set is empty, and this check has
four ways to reach an empty set — no recorded BASE, no region at BASE, a malformed pair, or a BASE
before the cutoff. Every one of them must print a named skip rather than pass silently, because a
skip that looks like a pass is indistinguishable from coverage. This is the single most likely way
for this unit to ship as a check that cannot fail.

### Files touched (estimate)

| File | Change |
|---|---|
| `tools/unattended/check-unattended.sh` | one check inside the anchor loop, four skip lines, four refusals, AND the header output contract plus its three green-control arms (S6a) |
| `tools/unattended/unattended.sh` | the id pattern promoted to a named constant the leg extracts, review fold M14 |
| `tools/unattended/check-unattended.test.sh` | the cases in §6 and the `ARMS_FLOORS` bump |
| `.memory-tree.conf` | the `ARMS_FLOORS` entry this unit moves — a BUILD-WIDE shared write, review fold M7 |

### Alternatives rejected

- **Comparing the roster against the working tree rather than the BASE blob.** Rejected: the working
  tree is entirely inside the run's reach, so the comparison would have no independent side at all.
- **Refusing a `rescope` row with no transition.** Rejected in §3, with the reason.
- **Reading the id set from the authored `roster:units` table.** Rejected: only four build READMEs in
  this tree carry that pair and nothing creates it, which is the defect that once made the
  `build-complete` item unmeetable on every other build.

## 5. Production-readiness checklist

- security — the check grades a record the run wrote against edits the run made, and its header says
  what that does and does not buy.
- perf / scale — two region reads and one row scan per live run, inside a loop that already reads the
  same blob.
- a11y — N/A — a shell gate with no user surface.
- i18n — N/A — the same.
- error / empty / loading states — S6 is this checklist item. Four named skips, no silent pass.
- observability — the four refusals and the four skip lines.
- risks (concurrency, data-loss, rollback hazards) — read-only.
- testing + left-shift gates — the cases in §6. Each new `fail` branch is armed with its entire
  literal signature, and adding branches renumbers the per-check ordinals below the insertion point,
  which invalidates any unarmed-branch row beneath it.
- migration / rollback — existing live runs carry no `rescope` rows and have made no amendments, so
  the check is silent on them. The cutoff skip covers older BASEs.
- user docs — the check's OWN SOURCE HEADER, which is what documents all twenty-one existing checks
  in this leg and which S7 already requires. Review fold: M8. The first draft promised a row in the
  protocol's check inventory; the installed protocol has ten sections and none of them is one, and the
  unit this obligation was delegated to never creates one. Inventing an eleventh protocol section
  would spend read-path margin this build is already spending elsewhere.

## 6. Acceptance criteria

- **AC1** — A fixture whose HEAD units region carries an id absent at BASE, with no matching row,
  reds with a message naming the id, observed in `tools/unattended/check-unattended.test.sh`.
- **AC2** — The same fixture with a `rescope · item add <id>` row present passes.
- **AC3** — A fixture flipping a unit to `WONTDO` with no `retire` or `supersede` row reds, naming
  the id and both acts.
- **AC4** — A fixture with a `supersede` row whose successor id is absent from the HEAD region reds,
  naming the successor.
- **AC5** — A fixture whose recorded BASE carries no units region prints a named skip line and does
  NOT red, and the skip text names which comparison went unexercised, observed in `tools/unattended/check-unattended.test.sh`.
- **AC6** — A fixture removing an id from the region is NOT reported by this check, confirming S5,
  and is still refused by `authorization-reachable` in the driver.
- **AC7** — Each new refusal and each skip is observed against a fixture before the unit lands, and
  the arms count in `ARMS_FLOORS` matches the new `fail` call sites.
- **AC8** — A fixture performing a FULL supersession — original flipped to `WONTDO`, replacement
  present at HEAD, exactly one `supersede` row and no `add` row — passes, observed in
  `tools/unattended/check-unattended.test.sh`. Review fold: H3, the case AC4 inverted and never covered.
- **AC9** — A fixture whose run authored a spec during `SPECCING` and then entered `BUILDING` does NOT
  red, and a fixture whose BASE units region names no unit is outside this check entirely. Both in
  `tools/unattended/check-unattended.test.sh`. Review fold: H4.
- **AC10** — With S6a in place, `bash tools/unattended/check-unattended.sh` on a conforming tree still
  prints nothing on its default channel, and the leg's three green-control arms in
  `tools/unattended/check-unattended.test.sh` still pass with their intent unchanged. Review fold: H1.
- **AC11** — The header of the new check STATES what it cannot buy, observed by `grep` over
  `tools/unattended/check-unattended.sh`. Review fold: L1.

## 7. Gates

`unattended kit gate` · `unattended kit selftest` · `harness arms` · the full bar at the push
boundary.

## 8. Open questions

- **F1 — RESOLVED (agent, 2026-08-20): key the exemption on WHEN the id appeared, not on the phase.**
  The first draft recommended a phase guard from `BUILDING` onward; the audit measured that it bounds
  nothing, and S2a now carries the resolution. A phase guard decides when the comparison RUNS while
  the window stays BASE-to-HEAD, and the authoritative run happens at `LANDING`, which is past any
  such guard. Review fold: H4.

## 9. Revision log

- rev-1 · 2026-08-20 · initial draft.
- rev-2 · 2026-08-20 · folded the spec audit: H3 (a supersede row accounts for its own successor),
  H4 (the exemption keys on when the id appeared, and F1 is resolved rather than left open), H1 (this
  unit OWNS the leg output contract by owner decision, S6a), M8 (the documentation is the check's own
  source header, because the protocol section it named does not exist), M14 (§10 corrected — the leg
  holds no id pattern, and the repair is a driver-side edit too), L1 (a criterion observing the
  honest-limit header). Five new criteria.

## 10. Reuse audit

**One dependency this unit needs is NOT in the leg, and the audit caught the reuse audit claiming it
was.** Review fold: M14. S2 derives two id SETS, and the leg carries no id pattern of any kind —
grepping it for the driver's `_ids_of` helper returns nothing. The seam that DOES exist is the leg's
existing parse of the driver's core sets out of the driver source, which its own header defends: the
core sets are read from the driver and never restated in the leg, because a second spelling is the
drift the leg exists to catch. The id pattern rides that same parse, or becomes a named driver
constant the leg extracts. Either way it is a DRIVER-side edit as well as a leg edit, and the
Files-touched table names `tools/unattended/unattended.sh` for it.

`python tools/codebase-map/reuse_lookup.py "a gate compares a build roster at two commits"` returns
the `build-readme-surface` dossier and `apply_region` as its affordance seam, plus the `unattended`
dossier. The seam this unit extends is the leg's existing anchor loop, which already resolves the
recorded BASE and reads the build README, and the `region` helper whose exit status distinguishes
absent from malformed — a distinction S6 depends on and which a previous unit's header records as
having been collapsed once, letting a second block go uncompared.

`python tools/memory-recall/query.py "how does the unattended gate grade what the driver recorded
without recomputing the driver's own answer" --terms "check second opinion driver recompute roster
units region base head subset skip vacuous announce arms floor"` returns the second-opinion class,
the vacuous-selector class and the arms-floor mechanics. All three bear on this unit: the first on
S5, the second on S6, the third on the testing line in §5.

Recall terms used: check second opinion driver recompute roster units region base head subset skip
vacuous announce arms floor.
