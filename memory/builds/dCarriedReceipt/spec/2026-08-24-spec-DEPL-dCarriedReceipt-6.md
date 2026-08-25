# DEPL-dCarriedReceipt-6 — the silenced-gate-leg bar, and the gov defect it finds

**Status:** SPECCED · rev-4 · 2026-08-24 · node d · Tier-2 · base 9ddcc5c9 · streams deployer · ratified 2026-08-24

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-24-review-DEPL-dCarriedReceipt-1-spec-precode.md](../reviews/2026-08-24-review-DEPL-dCarriedReceipt-1-spec-precode.md) | spec-audit | DEPL-dCarriedReceipt-1 DEPL-dCarriedReceipt-2 DEPL-dCarriedReceipt-3 DEPL-dCarriedReceipt-4 DEPL-dCarriedReceipt-5 DEPL-dCarriedReceipt-7 DEPL-dCarriedReceipt-8 |
| [2026-08-25-review-DEPL-dCarriedReceipt-1-round4.md](../reviews/2026-08-25-review-DEPL-dCarriedReceipt-1-round4.md) | spec-audit | DEPL-dCarriedReceipt-1 DEPL-dCarriedReceipt-2 DEPL-dCarriedReceipt-3 DEPL-dCarriedReceipt-4 DEPL-dCarriedReceipt-5 DEPL-dCarriedReceipt-7 DEPL-dCarriedReceipt-8 |

<!-- /gen:spec-records -->

## 1. Goal

`apply` emits a target's gate legs from each selected kit's `[[gate_leg]]` and refuses only on an
UNRESOLVED TOKEN in the argv (`:2686-2689`). It never asks whether the engine that argv would run
was shipped to that target. Four lines later it asks precisely that question of the leg's GUARDS
(`:2690-2699`), dropping one that matches no tracked path, with the reason written out at
`:2657-2660`. The same question, aimed at the thing the leg actually executes, is unasked — so gov
can hand an adopter a leg row that names a file gov never ships, record it in the receipt as
emitted coverage, and never notice. Measured at `9ddcc5c9`, the rule fires on exactly ONE LEG at
NicoCares, and that leg is a gov defect: `kickoff-manifest.kit.toml:60` declares a leg running
`{prefix}/check-template-size.sh` while `registry.toml:177` marks that file `[[exempt]]`, so no
adopter can ever receive it.

## 2. Scope (IN)

- **S1** — `silenced_legs(...)`: for each claimed kit and each `[[gate_leg]]`, resolve every argv
  element through `resolve_tokens` (`:516`) with `target_context` (`:535`); an element containing
  `/` that is not tracked in the target is a hit, carrying kit, leg name and element.
- **S2** — `cmd_apply` calls it inside the LEGS step (`:2662`) and, on a hit, does what the sibling
  branch at `:2686-2689` already does: `r.fail` naming the kit, the leg and the element, then
  `continue` without writing that leg row. It does not `raise Refusal`, so the install lands and the
  run exits 1 with a named problem rather than aborting an adopter over a defect they cannot fix.
- **S3** — `plan` reports the same hits as preview lines. At plan time nothing has been written, so
  the plan-side predicate is `tracked(target)` UNION this plan's own `write` destinations; without
  the union a preview reds every first install.
- **S4** — a gov-side `selfcheck` arm, which is where the class is actually gated: over every
  descriptor `[[gate_leg]]`, an argv element naming a path must be a path some kit ships, derived
  from the `shipped_owner` map arm 7h3 already builds at `:1067-1082`.
- **S5** — the gov defect: delete the `[[gate_leg]]` block at `kickoff-manifest.kit.toml:57-61` and
  add an `[[exempt_leg]]` row for `kickoff engine size <=18KiB` in `registry.toml`, carrying the
  reason its sibling `charter size` row (`registry.toml:235`) already states for the same script.
- **S6** — the LEGS step reads the index through `tracked()` (`:111`) instead of the inline
  `git ls-files` at `:2674-2675`, so the bar and the guard branch share ONE index reader.

## 3. Non-goals (OUT)

- **Not** shipping `tools/check-template-size.sh` to adopters. Its exemption is a decision on the
  record — an adopter's instantiated playbook carries no size ceiling — and this unit honours it
  rather than reversing it to make one leg resolve.
- **Not** removing a leg from a target that already holds one. Withdrawal from an installed manifest
  is `-11`'s `withdrawn` work. Measured: neither live target's leg manifest carries this leg today,
  so no removal path is needed and none is built.
- **Not** validating that a leg is CORRECT, or that its failure means what its name says. The bar
  answers one question: was the engine shipped.
- **Not** teaching `update` to re-emit or repair a leg row. `UPDATE_ROLE["gate-leg"]` becomes
  `report` in `-2` and stays there.
- **Not** widening the predicate past the `/` rule. §8 F2 pins what that leaves uncovered.
- **Land-alone:** this unit leaves both trees green on its own. Its dependency on `-1` is an ORDER
  rather than a conflict, in the vocabulary `-14` §8 F3 ratifies: AC6 asserts the post-`-1` world of
  exactly ONE surviving leg at each target, and the pre-`-1` inCMS tree shows two. The reason is
  measured rather than structural — see §4. Nothing here depends on `-2`; the `UPDATE_ROLE` line in
  §3 is a non-goal pointing at where that disposition is decided, not a landing order.

## 4. Design

The bar lives in the LEGS step (`:2662`) and nowhere earlier, and that placement is load-bearing.
`apply` stages everything it wrote at `:2475-2480`, and that stage precedes the legs step, so by the
time the bar runs, `tracked(target)` already includes this run's own writes. The identical predicate
at preflight would red every first install at every adopter. It is stated first here because it is
the single change a later reader is most likely to make while tidying.

### Inventory

The predicate was run over both live trees before being wired, printing hits and near-misses, which
is this repo's standing rule for a candidate gate. Two predicates were measured, because the
question "is this engine absent" has a different answer before and after the run's own writes:

Both columns count HIT LEGS, not hit argv elements. The two are not the same number and the spec
says which it means, because a finding is reported per leg and names every offending element in it:

| target | tracked-only hit legs | tracked ∪ this run's writes | survivor |
|---|---|---|---|
| NicoCares | 1 | 1 | `kickoff engine size <=18KiB` |
| inCMS | 17 | 2 | that leg, plus `pre-push self-test` |

At element granularity NicoCares' one hit leg carries TWO offending elements, both from
`kickoff-manifest.kit.toml:60` — `{prefix}/check-template-size.sh`, the engine, and
`skills/session-kickoff/SKILL.md`, the leg's SUBJECT. inCMS's column is measured against a
descriptor reconstructed from `.governance/kits.json`, because inCMS has no `.governance/deploy.toml`
at `9ddcc5c9`; reproducing it needs that reconstruction to carry inCMS's `[kit.*]` layout overrides,
without which the reading runs high.

The second predicate is the one `apply` uses, and the gap between the columns is the whole design.
inCMS's 17 measure the tree AS IT STANDS — the same partial adoption `-4` counts from the other
side — and 15 of them evaporate because `apply` writes those engines itself. The two survivors are
the ones no run can fix: `check-template-size.sh` because gov never ships it, and
`.githooks/pre-push.test.sh` (`push-main.kit.toml:63`) because `-1`'s resolver writes it to the
target root as `pre-push.test.sh`. So after `-1` lands, BOTH targets show exactly one hit and it is
the same gov defect — which is what makes S5 the difference between a bar that greets an adopter
with a finding and one that does not.

Near-misses, from the same run: the argv elements carrying no `/` are `bash`, `python`, `python3`,
`node`, `.`, `18432`, `--check`, `--check-format`, `--selftest` and `--target`. None is a path, so
none of them is graded.

What the rule does NOT do is tell an engine from a leg's SUBJECT, and rev-1's "zero false positives"
overstated that. `kickoff-manifest.kit.toml:60`'s third argv element is
`skills/session-kickoff/SKILL.md`, a file the leg READS, and no target holds it at that spelling —
the kit ships `SKILL.md` as a machine-scoped link to `{user_skills}/session-kickoff`, so the argv
names a gov-relative path in a command a target runs. Under S1's rule that is a hit, and it is a
TRUE one: the path is absent from the target and the leg cannot run. It is simply not an ENGINE
absence, so the finding is reported per LEG and names every offending element rather than claiming
each is a missing engine. No narrowing is attempted — separating an engine from a subject means
grading argument strings by guessing what they are, which is exactly the widening §8 F2 rejects.
S5 withdraws that whole leg, so both of its elements are cured by one edit and the class is not
reachable from today's shipped descriptors afterwards.

### Alternatives rejected

- *`raise Refusal` and abort the install.* The condition is a gov defect in a gov-authored
  descriptor. Blocking the adopter's whole install over it hands them a failure with no local fix,
  and `r.fail` already yields a named problem and exit 1 without destroying the install.
- *Drop the leg silently, the way a guard is dropped.* The file's own comment at `:2687-2689` says
  why the two are not symmetric: a dropped guard costs an unnecessary run, a dropped leg costs
  coverage. A skip must announce itself.
- *Gate only at the target.* The defect is gov's, and a target-side bar catches it once per adopter,
  forever, instead of once at the author. S4 is the class gate; S1 is the backstop for the adopter
  whose gov is older than the arm.
- *Assert descriptor argv against gov's own `tools/gate-legs.json`.* Tempting, because arm 7h
  already joins the two — but only on NAME and SUBJECT, never on argv, and the two argvs for this
  very leg already disagree: the descriptor carries a fourth element `"18432"` that gov's manifest
  row dropped when the limit moved into `tools/template-size-limits.txt`. Closing that is a real
  finding and a separate unit; making it a precondition of this one would stall a defect fix behind
  a contract change.

### Migration

None for a target. `registry.toml` and one kit descriptor change in gov; `subject-pins.tsv` does
not, because arm 7h2 pins over the MANIFEST rather than the descriptors (`:975-978`), and the
manifest row for this leg is untouched. Arm 7h's "claimed by no descriptor and carried by no
`[[exempt_leg]]`" loop goes green on the new row. `check-kit-versions.sh` asserts that a version
constant is present and well-formed, not that one bumps on a descriptor edit, so it stays green
without touching `manifest-check.sh` — which is correct here, since the kit's engine bytes do not
move and no adopter holds the withdrawn leg.

### Files touched (estimate)

`tools/govkit/govkit.py` (~40 lines across `silenced_legs`, the legs step, `cmd_plan` and one
`selfcheck` arm), `tools/govkit/entries/kickoff-manifest.kit.toml` (−5 lines),
`tools/govkit/registry.toml` (+4 lines), `tools/govkit/selftest.py` (5 arms),
`tools/govkit/refusal_join.py` (`BRANCH_PIN`, re-derived).

## 5. Production-readiness checklist

- security — a leg row is a command a target's bar executes. This unit narrows what may be written
  into that manifest and never widens it; nothing becomes newly executable.
- perf / scale — S6 replaces one inline `git ls-files` with the existing `tracked()` call, so the
  run performs the same single index read it already did.
- a11y — N/A: CLI.
- i18n — N/A.
- error / empty / loading states — a kit declaring no `[[gate_leg]]` takes no new path. A hit prints
  the kit, the leg name and the offending element, so the reader knows which of the three to fix.
  S6 also closes a smaller silence: the inline reader swallows a `git ls-files` failure and yields an
  empty tracked set, which drops every guard. That costs unnecessary runs rather than coverage, so
  it is a secondary correction and is named as one, not as this unit's point.
- observability — every dropped leg is a named finding and a nonzero exit; the receipt does not
  record a leg that was not written, so gov stops claiming coverage it did not deliver.
- risks — the real risk is a false positive stopping a legitimate leg from reaching an adopter. It
  is bounded by measurement rather than by argument: the predicate was run over both live trees and
  every hit was triaged by hand, with the near-miss set printed and inspected.
- testing + left-shift gates — S4 is the left-shift. The class is "a kit declares a leg whose engine
  the kit does not ship", gated over every registry entry rather than over the one entry that
  exposed it, and AC5 is its red-first observation.
- migration / rollback — see §4. Revertible as a pure addition plus one descriptor row moving
  between two declaration sites in gov.
- user docs — `WIRE-INTO-PROJECT.md` gains a line beside the apply step naming the condition, and
  the `[[exempt_leg]]` row's `why` is itself the documentation for the withdrawn leg.

## 6. Acceptance criteria

- **AC1** — At `9ddcc5c9`, `python tools/govkit/govkit.py selfcheck` exits 0 while
  `kickoff-manifest.kit.toml:60` names `{prefix}/check-template-size.sh` and `registry.toml:177`
  exempts `tools/check-template-size.sh` from shipping. Observe this green-on-a-defect first; it is
  the reason the unit exists.
- **AC2** — After S4, the same `selfcheck` reds on that entry by name BEFORE S5 is applied, and
  exits 0 after it. Both halves are asserted, because an arm only ever seen passing is an assertion
  about nothing.
- **AC3** — Against a SCRATCH CLONE of NicoCares — never the live submodule — `govkit.py apply
  --target <clone>` at `9ddcc5c9` writes a leg row named `kickoff engine size <=18KiB` into
  `scripts/gate-legs.json`; after this unit no such row is written and the run says why. Measured
  precondition: `grep "kickoff engine size" <NC>/scripts/gate-legs.json` is empty today, so this is
  an emission that never happens rather than a removal.
- **AC4** — Against a fixture whose kit ships its own leg engine, `apply` emits the leg and the run
  exits 0. This is the arm that fails if the predicate is evaluated before the STAGE step at
  `:2478`, and it is the false-positive guard for every legitimate first install.
- **AC5** — A fixture leg whose argv names `{prefix}/absent-engine.sh` produces exactly one finding,
  no row in the target's `gate-legs.json`, and exit 1 — not a `Refusal`, and not an aborted install:
  the receipt is still written and the other legs are still emitted.
- **AC6** — `govkit.py plan --target <inCMS>` names exactly ONE surviving leg, `kickoff engine size
  <=18KiB`, and not the fifteen that this run's own writes would satisfy — which is the union
  predicate of S3 observed directly. `pre-push self-test` is a hit only BEFORE `-1`, whose resolver
  writes `.githooks/pre-push.test.sh` to the target root; this unit lands after `-1`, so a second leg
  in that output is a regression in `-1` rather than a defect in this predicate. Both live targets
  therefore print the same single leg, which is what §4 already says and what rev-1's AC6 did not.
- **AC7** — `python tools/govkit/govkit.py selfcheck` stays green over arms 7h, 7h2 and 7h3 after
  S5, and `git diff --exit-code -- tools/govkit/subject-pins.tsv` is clean.

## 7. Gates

`bash tools/run-gates/run-gates.sh` full bar; specifically `govkit selfcheck`, `govkit selftest`,
`govkit acceptance matrix` and `govkit refusal join`. The join is an obligation, not a mention: this
unit adds refusal branches and `BRANCH_PIN (a shrink-only FLOOR, so it is re-derived at landing
rather than pinned to a literal here)` in `tools/govkit/refusal_join.py:40` is
shrink-only, so it is re-derived and moved in the SAME commit with both values named, and every new
branch gets an arm asserting it. The `kit version markers` leg stays green untouched, for the reason
given in §4.

## 8. Open questions

- **F1 — does the bar run against the SELECTION or against every claimed kit?** The selection, which
  is what `apply` is emitting legs for. A kit outside this run's selection contributes no leg row,
  so grading it would report a condition the run is not creating.
  RESOLVED (agent, 2026-08-24, delegated): the selection, under the full-scope approval.
- **F2 — what does the `/` rule leave uncovered?** A leg naming a repo-ROOT file with no slash —
  `AGENTS.md`, `CLAUDE.md` — slips through, and gov's own manifest has exactly such a leg in
  `charter size`. It is claimed by no descriptor today, so the gap is unreachable from the shipped
  set, and it is pinned here rather than implied away. Widening the rule to "any element that is not
  a flag and not an integer" was considered and rejected: it grades argument STRINGS by guessing
  what they are, which is how a predicate starts reporting `18432` as a missing file.
  RESOLVED (agent, 2026-08-24, delegated): keep the `/` rule; the gap is pinned, not closed.
- **F3 — should the kickoff kit's version bump when its leg is withdrawn?** No. The kit's engine
  bytes do not move, no adopter holds the withdrawn leg, and bumping `KIT_MANIFEST_VERSION` would
  advertise an engine change that did not happen — which is the inverse of the version-detectability
  defect the audit filed, and would make the constant less trustworthy rather than more.
  RESOLVED (agent, 2026-08-24, delegated): no bump.

## 9. Revision log

- rev-4 · 2026-08-24 · round-3 fold: the literal `BRANCH_PIN` value is withdrawn, for the reason
  `-5` records; and the README's deps cell now mirrors this spec's own §3 rather than
  contradicting it.
- rev-3 · 2026-08-24 · round-2 fold: §3's land-alone bullet states the `-1` dependency as an ORDER
  rather than a conflict, matching what AC6 and §4 already assert and using the vocabulary `-14` §8
  F3 ratifies; it also says plainly that `-2` is not a landing order for this unit, because §3's
  `UPDATE_ROLE["gate-leg"]` line reads like one. One review premise did NOT reproduce and is
  recorded rather than folded: this spec was said to state the coverage figure `55` without a
  vintage label, and it states no coverage figure at all — its inventory counts hit LEGS (`1` and
  `1` at NicoCares, `17` and `2` at inCMS), which is a different object from `-4`'s gap rows.
- rev-2 · 2026-08-24 · folded the pre-code review: AC6 now asserts the post-`-1` world this unit
  lands in — exactly ONE surviving leg at each target, reconciling it with §4, which already said so
  while AC6 asserted two — and §4's inventory now declares that its columns count hit LEGS, with the
  element-level reading spelled out beside it. The "zero false positives" claim is withdrawn and
  replaced by a measured statement: `kickoff-manifest.kit.toml:60`'s third argv element,
  `skills/session-kickoff/SKILL.md`, is a `/`-carrying leg SUBJECT rather than an engine path, the
  rule hits it, and the hit is TRUE — no target holds that spelling — so the finding is reported per
  leg naming every offending element, and no engine-versus-subject narrowing is attempted because
  §8 F2 already ruled that out.
- rev-1 · 2026-08-24 · initial draft, from the kit-sync design pass. Everything cited was read at
  `9ddcc5c9`, and the predicate was run over both live trees before being specified. Four
  corrections to the brief are folded in rather than repeated. The argv refusal is at `:2686-2689`
  (`if miss:` at `:2686`), not `:2685`, which is the `miss += m` above it. The dependency stated as
  `-4` is not a code dependency: `silenced_legs` needs `planned_writes` (`:1359`) and `tracked`
  (`:111`), both present at base, and nothing in it reads a coverage row — the ordering dependency
  that IS real is on `-1`, because without it inCMS shows a second hit that is the resolver defect
  rather than a silenced leg. The measured `17` on inCMS is a reading of the tree as it stands; the
  predicate `apply` actually evaluates reads `2` there, and `1` once `-1` has landed, so both
  numbers are kept in §4 with the question each answers. And "fails on an argv token" is `r.fail`
  rather than `Refusal`, matching the sibling branch four lines above it — the difference decides
  whether an adopter's install lands.

## 10. Reuse audit

The bar is assembled from seams that already exist and adds no second answer to any of them.
`resolve_tokens` (`:516`) and `target_context` (`:535`) render the argv exactly as the emitter does,
so the bar cannot grade a different string from the one that ships. `tracked` (`:111`) is the index
reader, and S6 exists precisely to stop there being two: the legs step currently re-implements it
inline at `:2674-2675`, which is the two-answers-to-one-question class this file names in its own
comments. The refusal shape is the `Report.fail` channel (`Report` at `:565`, `Refusal` at `:78`)
and the new branches are counted by the existing `refusal_join.py` contract rather than a new
counter. The gov-side arm wires through arm 7h3's `shipped_owner` derivation (`:1067-1082`) instead
of re-deriving the shipped set from `claims` — 7h3's own comment measured `claims` covering 13 of 58
file rules, so a second derivation would be confidently wrong over the other 45. The remedy for the
defect reuses `[[exempt_leg]]`, which the registry already carries for seventeen legs including the
three siblings of this very script, so no new declaration kind is invented for it.
