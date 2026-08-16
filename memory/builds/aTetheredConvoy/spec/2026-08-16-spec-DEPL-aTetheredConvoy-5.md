# DEPL-aTetheredConvoy-5 — check stops printing states and starts carrying evidence

**Status:** OPEN · rev-2 · 2026-08-16 · node a · Tier-2 · base 0f0a121d · streams deployer+tooling

## 1. Goal

Turn `check` from a verb that prints per-kit state words into one that carries evidence. Measured: on
a target whose landed files were all DELETED, whose receipt's every commit was rewritten to zeros and
whose every hash was rewritten to a nonsense value, `check` exits 0. It contains exactly one
filesystem test, never opens the receipt's file list, never reads the checksum sidecar it writes, and
calls no hash function. Everything the contract asks it to verify is absent.

## 2. Scope (IN)

- **S1 — receipt integrity, role-scoped.** An `engine` row must exist on disk and hash to its recorded
  value. A `seed` row carries an EXISTENCE claim only, because the role's whole contract is that the
  target owns the file after one copy — hashing it reds every target that did what the role permits.
  `project-owned` and `generated` likewise, and reported AS their role rather than as drift.
- **S2 — the sidecar and the receipt are asserted against EACH OTHER.** They are two spellings
  written from one list and the sidecar is read by nothing in this repo today. Verifying one and
  trusting the other leaves the artifact a target verifies with bash alone unasserted forever.
- **S3 — byte provenance at check time.** For each `engine` row, resolve the recorded source at the
  recorded commit from the gov index and compare. An unresolvable row names the source, the commit AND
  the gov root consulted, and states both causes: this is a different clone than the receipt recorded,
  or the commit is not fetched here. A gov root differing from the recorded one is a NOTE, not a
  failure — a target legitimately checks from a second clone.
- **S4 — the adopter fan-out, plus the wiring arm that makes it non-vacuous.** Where a kit declares a
  check arm, run it and surface its own refusal. A new `selfcheck` arm derives, in both directions,
  whether a script named by a descriptor accepts the arm: a script that does and is not wired reds, and
  a wired script with no such arm reds. Measured, six shipped scripts accept it and four are wired.
- **S5 — `rendered` rows recorded, and their equality discharged by the kit's OWN renderer.** `apply`
  does not render; after configure it OBSERVES, recording the destination, its template, the
  substitution inputs with their hashes, and the output hash. A destination absent after configure is a
  FINDING. `check` discharges equality through the kit's own check arm and REPORTS which mechanism did
  it — verified by that kit's renderer, or UNVERIFIED where the kit declares none. Never green by
  silence.
- **S6 — a rendered difference is REPORTED and fails nothing on its own.** A rendered artifact
  legitimately changes when the target edits its conf. The recorded output hash exists so an update can
  separate an adopter-written change from a hand edit, not so `check` can call it drift.
- **S7 — machine-scoped entries: an order at apply, `undischargeable` at check.** `apply` writes an
  order for every machine-scoped or linked rule, reusing the planner's own predicate so the planner's
  order set and the outbox become the same set by construction — measured, they differ today. The link
  command is DERIVED from the platform, printing the host's form first and the other labelled beneath.
  `check` prints `undischargeable` naming the destination and the reason, and reds only on the order's
  ABSENCE, because there is no probe for a destination outside the repository.
- **S8 — `check` READS the outbox.** The contract names it and the verb never opens it. Every order the
  receipt records must exist; an order for a hole no selected kit declares is stale and is a finding.
- **S9 — the `[[outcome]]` evaluator.** Nine outcome blocks across six descriptors are read by zero
  code. An adopter's exit code plus a filesystem probe yields the declared meaning, which is what lets
  a fixture assert a MEANING rather than an integer — a distinction unit 7's arms require and cannot
  otherwise satisfy.
- **S10 — entry-level `scope` becomes derived.** Every descriptor declares it and the engine reads only
  the rule-level spelling. Derive the entry scope (machine iff every rule is) and add a `selfcheck` arm
  asserting the declared value equals the derived one, so the contract's machine-scoped criterion has a
  referent instead of eighteen dead declarations.
- **S11 — every loop prints a DERIVED count and reds when that count is zero over a population the
  DESCRIPTORS say is non-empty.** The expectation comes from the descriptors, not from the receipt: a
  receipt that lost its rows and a target that is clean are otherwise the same output.

## 3. Non-goals (OUT)

- **Merged-block drift.** Designed in unit 6 and shipped there, because `apply` refuses every merged
  rule before writing — an arm whose precondition cannot occur is the second named defect class,
  shipped inside the verb built to detect it. Unit 1 reserves the receipt row; unit 6 fills it and adds
  the drift arm in the same diff.
- **Asserting that a render is CORRECT.** Measured, this repo's own renders are install-prefix-correct
  and not memory-root-correct, so a comparison against gov's installed copy asserts correctness and is
  false on any target that renamed its memory root. `check` never diffs a target's rendered artifact
  against gov's own, and that is a refusal with an arm, not a convention.
- **Repairing the kits that ship no check arm.** Two genuinely have none. Both ship runnable verifiers
  a descriptor could point at; S4's arm names them and the descriptor author decides. Wiring them is a
  per-kit judgment this unit refuses to make on their behalf.
- **The baseline, the emitter and anything reading the gate-runner declaration.** Unit 4.

**Assumes:** units 1 (schema, roles, state vocabulary), 3 (the correspondence arms live in the same
`selfcheck`) and 4 (`check --observe` and the emitted-leg presence loop are that unit's).

## 4. Design

### The measured starting point

`check` today: one filesystem test, on the receipt's own path. It never opens the receipt's file list,
never reads the sidecar, never hashes anything, and its docstring says exit 0 requires every selected
kit to be adopted. Measured against that docstring: a kit declaring nothing prints the inert state and
exits 0. Measured against the contract: the delete-everything-and-corrupt-the-receipt fixture exits 0.
The sidecar has one write site and one existence assertion, and its CONTENT is compared with nothing by
any code path.

### Role scoping is the whole design of S1

An unscoped hash loop is the contract's own unscoped-quantifier mistake committed a second time. A
`seed` file's installed bytes may legitimately diverge — that is what the role is for — so the loop
must dispatch on unit 1's frozen role table rather than treat every row as gov's.

This is also why this unit cannot land before unit 1: role scoping depends on roles being true, and
measured, they are not.

### Liveness, and where the expectation comes from

Every loop prints a derived count. The subtlety the adversarial pass bought: a zero-count guard that
derives its population from the RECEIPT cannot distinguish zero-of-zero from clean, and the receipt is
measurably lossy — two applies of a seed-bearing kit leave the file list empty. So the expectation
comes from the DESCRIPTORS: a kit the receipt claims, whose descriptor declares at least one landable
rule, must have rows. Fewer is a finding. That turns unit 1's receipt fix into something `check`
OBSERVES rather than something it assumes.

The provenance loop takes the same treatment in the other direction: resolving zero of a non-zero
number of engine rows prints DEAD PROBE and reds, which is the doctrine this repo's drift audit already
applies to a signal that cannot move.

### Rollout

1. **S1, S2, S11** — integrity, the sidecar agreement, and the derived-count discipline. The commit
   that makes `check` capable of failing.
2. **S3** — provenance, with its dead-probe half.
3. **S4, S5, S6** — the fan-out, its wiring arm, and the rendered rows.
4. **S7, S8, S9, S10** — orders, the outbox reader, the outcome evaluator and the derived scope.

### Files touched (estimate)

| Area | Files | Note |
|---|---|---|
| Core | `tools/govkit/govkit.py` | the check loops, the apply-side rendered observation and order writer, two `selfcheck` arms |
| Descriptors | those gaining a check arm or a declared absence | unit 1 landed the declared-absence blocks; this unit wires what it can |
| Tests | `tools/govkit/selftest.py` | the check path has ZERO coverage today — its five existing check arms all target a kit declaring no check block |
| Map | `memory/map/features/govkit.md` | the evidence seams |

### Alternatives rejected

**Make `check` a thin fan-out over adopter check arms.** Rejected on measurement: four of the entries
have one. The other thirteen need S1, S3, S5 and S7 to be measured at all.

**Assert the sidecar against disk instead of against the receipt.** Rejected: they are two spellings
written from one list, and the sidecar's entire purpose is verification by a target with no Python. An
arm that checks each against disk separately still never asks whether they agree.

**Let a rendered difference be drift.** Rejected: it is the expected outcome of the target editing its
own conf, and calling it drift makes `check` red on a correctly-configured target.

## 5. Production-readiness checklist

- security — read-only, except that S4 runs a kit's own check arm, which is gov-authored code the
  target already installed. No target-authored code runs here; that is unit 4's.
- perf / scale — one hash per engine row and one `git show` per engine row.
- a11y — N/A: a command-line tool.
- i18n — N/A: developer tooling.
- error / empty / loading states — S11 IS this line: every loop distinguishes "verified nothing" from
  "nothing to verify".
- observability — `check` becomes the observability surface the contract claims it is.
- risks — the biggest is that this unit's arms all quantify over the receipt, so unit 1's receipt fix
  is a hard prerequisite rather than a nicety; AC1's regression arm asserts it from this side too, so
  the dependency is observed rather than assumed. Second: S4 runs installed code, so a kit whose check
  arm is slow makes `check` slow.
- testing + left-shift gates — the check code path has zero selftest coverage today; this unit is its
  first. Every arm carries its liveness half.
- migration / rollback — additive; a schema-1 receipt lacks the rendered and order rows and is reported
  as unverifiable for those, never as clean.
- user docs — the Skill gains what each state now means in evidence terms.

## 6. Acceptance criteria

- **AC1** When `apply --kits <a seed-bearing kit>` runs twice and then
  `python tools/govkit/govkit.py check --target <fixture>` runs, the integrity loop reports a non-zero
  row count. Liveness: measured today the second apply leaves the receipt's file list EMPTY, so this
  arm reds before unit 1 lands — it is this unit's own observation of that dependency.
- **AC2** When one `engine` file in an installed fixture is modified, `check` exits 1 naming the path,
  the expected hash and the actual. Liveness: a modified `seed` file must NOT red and must be reported
  as owner-owned; and the clean run prints `integrity: N/N` with N derived and non-zero.
- **AC3** When a receipt claims a kit whose descriptor declares at least one landable rule and the
  receipt holds zero rows for it, `check` reds — the population expectation comes from the descriptor,
  not the receipt.
- **AC4** When one hash in `.governance/install.sums` is hand-edited, `check` exits 1 naming the
  disagreement and which side carries which value. Liveness: the untouched pair exits 0 printing the
  compared row count, so an empty sidecar cannot pass as agreement.
- **AC5** When a receipt's recorded commit is rewritten to a nonsense value, `check` exits 1 naming the
  file, the recorded commit and the gov root consulted. Liveness: `provenance: M/M` on a clean run, and
  a fixture whose rows are ALL unresolvable prints DEAD PROBE and reds. Measured today that exact
  mutation, plus deleting every landed file, exits 0.
- **AC6** When a wired kit's rendered artifact is overwritten, `check` exits 1 carrying that adopter's
  OWN refusal text. Liveness: this is also the first selftest coverage of the fan-out branch — the
  existing check arms all target a kit that declares no check block, so the branch is executed by
  nothing on the bar today.
- **AC7** When `python tools/govkit/govkit.py selfcheck` runs, it reds naming any entry whose named
  script accepts a check arm that the descriptor does not wire, and any `[check].argv` naming a script
  with no such arm. Liveness: the already-wired entries must NOT red, and the arm reports how many
  scripts it READ — a scan that opened zero scripts is a finding.
- **AC8** When `apply` completes, the receipt carries a `rendered` row per rendered rule with its
  template and inputs; a destination absent after configure is a FINDING naming it. Liveness: today
  every non-landable role vanishes with no message, so the absent case reds before unit 1's closure.
- **AC9** When a rendered artifact is deleted, `check` reds; when it differs from the recorded output
  hash it REPORTS and exits 0 on that row alone; and the finding text names a temporary render or the
  adopter and NEVER a path inside the gov checkout — the forbidden correctness comparison, asserted as
  an absence.
- **AC10** When `plan` and `apply` run over one fixture, the ORDER destinations `plan` prints equal the
  set of files in `.governance/outbox` afterwards, asserted as SETS. Liveness: measured today they
  differ, so the arm reds before the fix.
- **AC11** When a machine-scoped entry is selected, `check` prints `undischargeable` naming the
  destination and the reason, reds when that order file is deleted, and the order carries the host
  platform's link command first with the other labelled beneath.
- **AC12** When the outbox holds an order for a hole no selected kit declares, `check` reds calling it
  stale.
- **AC13** When an adopter exits non-zero and its descriptor declares matching `[[outcome]]` probes,
  `check` and `apply` report the declared MEANING rather than the integer. Liveness: an exit code
  matching no outcome probe is reported as unclassified and names the code, so the evaluator cannot
  invent a meaning.
- **AC14** When a descriptor's declared entry-level scope differs from the value derived from its
  rules, `selfcheck` reds naming both. Liveness: gov's own eighteen declarations must be silent after
  the derivation lands.

## 7. Gates

`bash tools/run-gates.sh` green at the push boundary; `GATE_FULL=1` for the DoD. No new leg — the arms
ride `govkit selftest` and `govkit selfcheck`.

One shipped kit declares a hole whose discharge probe can never pass, by construction and honestly. Any
fixture asserting `check` exit 0 over an all-kits selection is therefore unsatisfiable, and every
fixture here names its selection deliberately rather than reaching for `--all`.

The kit version constant moves.

Before review: `python tools/memory-tree/gotchas.py --for-diff 0f0a121d..HEAD`. The
`assertion-between-two-derived-values` class is live in S2 and S11 — both compare two things this
engine composes.

## 8. Open questions

none — the forks below are RESOLVED. Authority: the owner's instruction to execute this build
delegates resolver authority for THIS build only, and every fork here is one the spec already stated,
which is exactly M3's condition. Each was taken through M3's veto order; none was discarded by a veto,
and the two that touch a write or security surface are called out in the wrap-up as owner-review items
rather than treated as settled by silence.

- **F1 — do the two kits with no check arm get one wired, or a declared absence?** RESOLVED (agent,
  2026-08-16, delegated): a declared absence in this unit, plus a backlog row per kit. Each kit's
  runnable verifier IS that kit's own gate leg, so wiring it into `check` would make `check` run a
  gate, which is a different verb's job.
- **F2 — does the provenance loop run by default or behind a flag?** RESOLVED (agent, 2026-08-16,
  delegated): by default. It is one object read per engine row against a local database, and it is the
  arm that catches the case the contract calls the receipt's whole provenance claim.

## 9. Revision log

- rev-2 · 2026-08-16 · M3 fork sweep: F1 and F2 resolved in place under the owner's
  execute-the-build delegation. No veto fired.
- rev-1 · 2026-08-16 · initial draft. Grounded on a twelve-agent audit that measured the
  delete-everything-and-corrupt-the-receipt fixture exiting 0, the sidecar read by nothing, and the
  check code path carrying no selftest coverage at all. Two decisions came from the adversarial pass:
  the population expectation for every zero-count guard comes from the DESCRIPTORS rather than the
  receipt, because a lossy receipt makes a receipt-derived guard vacuous; and merged-block drift moved
  OUT to unit 6, because its precondition cannot occur while `apply` refuses every merged rule.

## 10. Reuse audit

Ran `python tools/codebase-map/reuse_lookup.py` for the integrity, provenance and fan-out loops.

`blob_at` is AC5's whole comparison, and its existing not-found branch is already the signal that the
commit or path does not resolve in THIS clone — it needs a finding text, not a new function.

The hole-probe loop supplies the four failure directions S9's outcome evaluator reuses verbatim,
including its proof that a probe which cannot launch is a finding rather than a pass.

The derived-`mutates_index` arm is the template for S4's wiring arm and S10's scope arm: derive from
the named artifact, assert against the declaration, both directions. Scoping the scan to the NAMED
script is what excludes two known false positives with no waiver list.

The planner's machine-scope branch already emits an order row; S7 moves that same predicate into the
apply-side outbox loop, which today iterates holes only — making the two sets identical by construction
rather than by two implementations agreeing.

`foreign_kit_present`'s walk locates a landed destination by probing an entry's DECLARED destinations
at both prefixes rather than guessing a path from the id; S1's per-kit `not-landed` state and S5's
rendered destinations reuse it, which is also how neither spells a prefix.

The report channel and its exit contract need no new vocabulary: every new arm is a failure, every
derived count is a note.

No seam exists for receipt-versus-disk verification of any kind — the engine has exactly one hash call
site, in the receipt writer — nor for reading the sidecar, which nothing reads. Both are new and small.
