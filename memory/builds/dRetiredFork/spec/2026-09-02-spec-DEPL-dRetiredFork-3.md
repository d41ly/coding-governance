# DEPL-dRetiredFork-3 — `update` re-runs the adopters, renderers and generators it invalidates

**Status:** OPEN · rev-4 · 2026-09-02 · node d · Tier-2 · base b0108f13 · streams deployer · order 7 · ratified 2026-09-02

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round1.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round1.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-4 DEPL-dRetiredFork-5 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 TOOL-dRetiredFork-1 TOOL-dRetiredFork-2 TOOL-dRetiredFork-3 TOOL-dRetiredFork-4 TOOL-dRetiredFork-5 TOOL-dRetiredFork-6 TOOL-dRetiredFork-7 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-10 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-18 |
| [2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round2.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round2.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-4 DEPL-dRetiredFork-5 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 TOOL-dRetiredFork-1 TOOL-dRetiredFork-2 TOOL-dRetiredFork-3 TOOL-dRetiredFork-4 TOOL-dRetiredFork-5 TOOL-dRetiredFork-6 TOOL-dRetiredFork-7 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-10 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-18 |
| [2026-09-02-review-TOOL-dRetiredFork-3-21-and-depl-1-9-spec-audit-round3.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-3-21-and-depl-1-9-spec-audit-round3.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 DEPL-dRetiredFork-8 DEPL-dRetiredFork-9 TOOL-dRetiredFork-3 TOOL-dRetiredFork-5 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-19 TOOL-dRetiredFork-20 TOOL-dRetiredFork-21 |

<!-- /gen:spec-records -->

## 1. Goal

Bytes landing is not an update finishing. `UPDATE_ROLE["rendered"]` is `"adopter"` but the
disposition CAPS at report, and the write loop's first act is to skip anything whose `how` is not
`table`, printing "reported only … this role is never written by update". No `[adopt].argv` is
spawned anywhere in `update`; the only subprocess it runs per kit is `[check].argv`, a verifier. So
eight rendered destinations at NicoCares — including both binding protocols and three `SKILL.md`
files — go ONE VINTAGE STALE on every update, and the two adopter CI jobs that byte-compare them
red. This is the difference between "the bytes arrived" and "the update ran".

## 2. Scope (IN)

- **S1** — After the write loop, `update` re-runs the `[adopt].argv` of every entry whose landed set
  invalidated a rendered destination, in dependency order, and REPORTS what it ran.
- **S2** — A generator obligation table: an entry declares which of its artifacts must be
  regenerated when its version moves, so `codebase-map`'s `gen_map.py --write` on a
  `KIT_CODEBASE_MAP_VERSION` bump and `memory-tree`'s `gen_build_index.py --write` are performed
  rather than described in a runbook. The obligation is DECLARED in `kit.toml`, because a rule that
  lives only in `WIRE-INTO-PROJECT.md` is a rule an unattended run cannot honour.
- **S3** — A `role` change on an existing row is handled in place: a file moving from `engine` to
  `rendered`, which `TOOL-dRetiredFork-12` performs, must not revert silently because `engine`
  asserts the recorded OID.
- **S4** — Post-write verification already exists — `DEPL-dCarriedReceipt-14` re-runs each touched
  kit's `[check].argv` and rolls back from recorded OIDs on red. This unit extends it to cover the
  re-render and regeneration steps, so a bad render is rolled back rather than committed.
- **S5** — The ordering constraint `TOOL-dRetiredFork-14` depends on: a wired command must move to
  the surviving hook copy BEFORE the second copy is withdrawn, enforced by the engine rather than by
  a runbook sentence.
- **S6** — Arms for each: a rendered row re-rendered; a version bump triggering its declared
  generator; a role change surviving a round trip; a failed render rolling back; and a target
  whose wired command still names the copy S5 would withdraw.

## 3. Non-goals (OUT)

- Running an adopter for a kit the target holds deliberately INERT. That is a posture flip and is
  exactly why "just run `apply`" is not the workaround. An inert kit's adopter is not run, and the
  run says so.
- The `merged` role. Its code says plainly that no writer exists yet, and building one is out of
  scope; `DEPL-dRetiredFork-7` records it.
- Writing a `generated` file's BYTES. `update` never does that, by declared design — but a
  `[[regenerate]]` argv declared by a gov descriptor IS run by this verb, which is S2's whole
  content, so this disclaims AUTHORSHIP and not INVOCATION. Such rows are otherwise produced in
  the target by the target's own tooling.
  The report NAMES which generators are owed; running the target's own tooling is the adopter's.

## 4. Design

### Data model

A new `[[regenerate]]` block per entry: `when = "version_moves"`, `argv = [...]`, `why = "…"`. It is
additive and defaulted — an entry declaring none behaves as today — which satisfies the
forward-compatible-data rule and means no adopter's install breaks on the pull.

### Rollout

The re-render step is gated OFF by default for its first release and flipped on after in-place
verification against a fixture and then one adopter, because it is the first time `update` executes
target-side code. That is `AGENTS.md` §1's dark-landing rule applied to the deployer itself.

### Alternatives rejected

Telling the operator which generators to run. That is the status quo — `WIRE-INTO-PROJECT.md`'s
maintenance section already does it — and it is the reason a kit pull is a build. A rule a person
must remember is not a mechanism.

## 5. Production-readiness checklist

- security — `update` begins executing target-side declared argv. Every argv is gov-authored in a
  gov descriptor, but it runs in the target's tree under the operator's uid, and the trust boundary
  is exactly the one `AGENTS.md` §9 states: a check running under the run's own uid can be defeated
  by whoever runs it. The mitigation is that the argv comes from gov's descriptor and never from the
  target's `deploy.toml`, and that the strict path class grades every interpolated fragment.
- perf / scale — one adopter invocation per touched entry, not per file.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — a render that produces an empty artifact must REFUSE, because
  empty-versus-empty passing is the class `TOOL-aBranchedMandate-5` already records for
  `adopt-drift-audit.sh`.
- observability — the run prints every adopter it invoked, every generator it ran, and every one it
  DECLINED to run with the reason. A skip that looks like a pass is the class this build keeps
  closing.
- risks — executing code in a repository gov does not own, after a write, with a rollback that must
  itself work. Highest-risk unit in the build. Mitigated by the default-OFF flag, by S4's rollback
  extension, and by the fixture-then-one-adopter rollout.
- testing + left-shift gates — one arm per S6 item, plus the acceptance matrix.
- migration / rollback — the `[[regenerate]]` block is additive and defaulted; the feature flag is
  the rollback.
- user docs — `WIRE-INTO-PROJECT.md` maintenance section SHRINKS, because the obligations it lists
  become declarations. That shrinkage is an acceptance criterion, not a side effect.

## 6. Acceptance criteria

- **AC1** — When a landed template invalidates its rendered artifact, `python
  tools/govkit/govkit.py update --target <fixture> --write` re-renders it and names the adopter it
  ran; the pre-change run left the artifact one vintage stale.
- **AC2** — When an entry's version moves and it declares a `[[regenerate]]` argv, the run performs
  it and the target's freshness gate exits `0` immediately afterwards.
- **AC3** — When a render produces an empty artifact, the run REFUSES and rolls back from the
  recorded OIDs. Observed via `python tools/govkit/govkit.py update --target <fixture> --write`.
- **AC4** — When a row's role changes from `engine` to `rendered`, a round trip preserves the
  rendered artifact rather than reverting it.
- **AC5** — When a kit is held INERT by the target, its adopter is NOT run and the report says so. Observed via `python tools/govkit/govkit.py update --target <fixture> --write`.
- **AC6** — When the feature flag is off, the run's output is byte-identical to the pre-change run. Compared across `python tools/govkit/govkit.py update --target <fixture>` runs.
- **AC7** — A read-only run against `C:/projects/nicocares/main` names all eight rendered
  destinations and the generators each would owe.
- **AC9** — When a target's settings still name the withdrawn hook copy, `python
  tools/govkit/govkit.py update --target <fixture> --write` REFUSES the withdrawal naming the
  unwired window. This is S5, the constraint `TOOL-dRetiredFork-14` §4 delegates here and its §5
  calls the highest risk in the build; rev-1 carried it in scope and observed it nowhere.
- **AC10** — THE BUILD'S DONE-CONDITION, and the only criterion in the set that observes it. With
  the re-render flag ON, `python tools/govkit/govkit.py update --target C:/projects/nicocares/main
  --write` lands every stale row, re-renders every rendered row, runs every declared generator,
  re-stamps `gov_commit`, and the tree afterwards needs no hand merge — recorded in the acceptance
  ledger. **inCMS's half of the done-condition is DEFERRED, and §3 says so**: no unit in this
  roster repairs that receipt, so a criterion gated on the repair would be permanently neither
  green nor red — worse than a missing one, because it looks covered.
- **AC11** — `python tools/govkit/check_runbook_parity.py` exits `0`, and
  `WIRE-INTO-PROJECT.md`'s maintenance section is strictly SHORTER than at `b0108f13`,
  and every obligation it drops is carried by a `[[regenerate]]` block in a kit descriptor. §5
  calls that shrinkage an acceptance criterion rather than a side effect, and rev-1 wrote none.
- **AC12** — `python tools/govkit/selftest.py` and `selfcheck` exit `0`.

## 7. Gates

`govkit selfcheck` · `govkit selftest` · `govkit acceptance matrix` · `govkit refusal join`.

## 8. Open questions

- **F1 — does the generator obligation live in `kit.toml` or in the receipt?** The descriptor is
  gov's and travels; the receipt is the target's and records what happened. Recommendation:
  descriptor, with the receipt recording that it ran.
- **F2 — what happens when a re-render needs an answer the target's `deploy.toml` does not carry?**
  `intake` refuses to rewrite an existing descriptor by design, so the run cannot add the key.
  Recommendation: REFUSE the re-render naming the missing key, and leave the bytes landed — the same
  shape `apply` already uses when a destination needs an unanswered key.
- **F3 — is the default-OFF flag removed after the first successful adopter run, or kept?**
  Recommendation: keep it for one release, then remove it in a follow-up, so a regression has a
  documented switch rather than a revert.

**RESOLVED (owner, 2026-09-02): every fork above is settled by its own stated Recommendation.** The owner ratified them as written on 2026-09-02 with the instruction to fold the recommendations. No fork is resolved against its recommendation and none by silence; where a later measurement contradicts a ratified pick, that is a new fork with a new id.

## 9. Revision log

- rev-1 · 2026-09-02 · initial draft. `UPDATE_ROLE`, the report cap and the absence of any
  `[adopt].argv` spawn inside `update` were read at `b0108f13`.
- rev-2 · 2026-09-02 · folded spec-audit round 1, findings B1 and B6. B6: S5 — the ordering
  constraint `TOOL-dRetiredFork-14` delegates here and calls the build's highest risk — appeared in
  no acceptance criterion and no S6 arm, so it could ship unbuilt while both units passed their DoD.
  AC9 and a sixth arm now observe it. B1: every `--write` criterion in the whole 25-spec set targeted
  a fixture and every adopter-facing one was read-only, so the union could not imply the README's
  done-condition. AC10 is that observation, and this unit owns it.
- rev-3 · 2026-09-02 · folded spec-audit round 1, finding M3. §5 declared the runbook's shrinkage an acceptance criterion
  and §6 carried none; AC11 is it.
- rev-4 · 2026-09-02 · folded spec-audit round 2, findings 6, 12, 14, 23 and 28. 6: AC10's inCMS half was
  gated on a repair no unit performs, so it could neither discharge nor fail; DEFERRED in
  writing now. 12: the `generated` non-goal contradicted S2 — it disclaims authorship, not
  invocation. 14: a stale arm count becomes a pointer. 23: AC11 lost its gate when `runbook
  parity` proved not to be a leg; it invokes the program directly. 28: AC8 sat after AC11.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py` was run for this build and reports the
`govkit` affordance seam plus the `derive_*` family in `tools/govkit/govkit.py`. The seam is `_cmd_apply`'s existing adopter invocation plus `classify_outcome`, which already spawn
and grade a kit's declared argv — this unit lifts that pair out of `apply` and reuses it from
`update` rather than writing a second spawner. `DEPL-dCarriedReceipt-14`'s post-write verification
and its rollback from recorded OIDs is the second live seam, extended rather than duplicated.

Recall terms used: `govkit`, `update`, `rendered`, `adopter`, `argv`, `regenerate`, `freshness`,
`rollback`, `outcome`, `inert`, `receipt`, `role`, `vintage`, `generator`.
