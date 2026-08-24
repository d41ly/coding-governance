# TOOL-dUnstalledConvoy-26 — a kit's self-tests become an owner-adjustable, on-demand population instead of bar legs

**Status:** SPECCED · rev-1 · 2026-08-23 · node d · Tier-2 · base b164a296 · streams tooling

## 1. Goal

A kit's self-tests read THE KIT. They stage a break into a copy of a checker and assert the checker
still catches it, so they have a job when the kit's source changes and none at all in a repo that
copy-installs the kit and never edits it. Today they are ordinary bar legs, so every adopter runs them
on every full gate.

`f5f4732a` fixed this for one kit by DELETING seven legs. That is an instance fix: it left twenty-nine
descriptor legs across eleven other kits, took the coverage away from this repo too, and installed no
mechanism to stop the next kit repeating it. The owner's ruling is that emitting and running them
should be ADJUSTABLE rather than decided once by deletion.

## 2. Scope (IN)

- **S1 — a self-test leg DECLARES itself.** `[[gate_leg]]` gains `on_demand = true`. The population is
  declared in the descriptor, never inferred from `.test.sh` appearing in an argv — an inferred
  population is a spelling test, and this repo already carries a leg whose script does not end in
  `.test.sh` and one that is a self-test without saying so.
- **S2 — `run-gates` skips an `on_demand` leg unless asked**, and `GATE_FULL=1` does NOT ask. That is
  the whole point: `changed()` returns 0 the moment `GATE_FULL` is set, so today's `guard = ["{kit}/"]`
  is bypassed at exactly the push boundary where an adopter feels it.
- **S3 — the ask is one switch**, `GATE_SELFTESTS=1`, and it is the only thing that unlocks them. With
  it set they run; without it they are reported as skipped by name, never omitted.
- **S4 — the skip ANNOUNCES itself**, in the run's own summary, with a count. A leg that vanishes from
  a green bar is the shape this repo has redded for twice.
- **S5 — the twenty-nine descriptor legs are migrated**, derived by reading each `kit.toml` rather than
  from a list typed here: `agent-instructions` 1, `codebase-map` 2, `drift-audit` 1, `agent-cap` 2,
  `lexicon` 1, `memory-recall` 1, `memory-tree` 11, `playbook-render` 1,
  `pytest-parallel-guardrails` 1, `run-gates` 5, `review-harness` 3.
- **S6 — this repo's own manifest carries the same flag**, on the 47 of its 85 legs that are
  self-tests, so the descriptor↔manifest cross-check keeps agreeing in both directions.
- **S7 — govkit's cross-check learns the field.** A leg declared `on_demand` in a descriptor must be
  `on_demand` in the manifest, and the mismatch is a refusal — otherwise the two spellings drift and
  the deployer's own thesis goes unapplied to the deployer again.
- **S8 — the adopter is told how to run them**, once at adoption and on demand after, in the text
  govkit already prints at the end of an install.
- **S9 — every change lands with its arm, and the arms that can fail are observed failing first.**

## 3. Non-goals (OUT)

- **Deleting any self-test.** The unattended kit's seven stay deleted because that was an owner ruling
  on that kit; this unit does not restore them, and does not remove any other.
- **Changing what a self-test asserts.** This unit moves WHEN they run, never what they check.
- **A per-kit or per-leg opt-out in the target's `deploy.toml`.** One switch, repo-wide. A per-kit
  matrix is a configuration surface nobody will audit, and the failure mode is a kit silently exempt.
- **Making `GATE_FULL` unlock them.** `GATE_FULL` means "ignore every guard"; if it also meant "run the
  kit's own tests" there would be no way to ask for a complete bar without them.
- **The `impure` and `chunk` fields**, the timing cache, and the chunk reporting. Untouched.

## 4. Design

The runner already carries per-leg fields on its wire format — `name`, `guard`, `argv`, `impure`,
`chunk`, `\x1e`-separated, one row per leg — so `on_demand` is a sixth field beside them rather than
new machinery. The reader emits it, the dispatcher consults it, and a leg that is skipped keeps its
index, which the manifest's 1:1 row correspondence already depends on.

S1 is declared rather than inferred because the alternative is a predicate over argv text, and this
build has now twice written such a predicate, measured it, and thrown it away. A descriptor field is
checkable in both directions and cannot be fooled by a rename.

S2's argument is the measurement: `changed() { [ -n "${GATE_FULL:-}" ] && return 0; ... }`. The guard
these legs already carry is bypassed whenever `GATE_FULL` is set, and `.githooks/pre-push` sets it when
it decides a full run is owed. So the existing guard does not do the job the leg descriptors imply it
does, and no adopter can tell from reading them.

S4 exists because the alternative is a bar that got smaller without saying so. The count is reported
the way a skipped leg is already reported, which is the shape the charter requires and this repo has
twice landed a defect against.

What this does NOT buy: it does not verify that a kit's self-tests still PASS in an adopter's repo. It
moves them off the automatic bar; running them is then the owner's choice and their result is the
owner's to read. A green adopter bar after this says nothing about the kit's own health, and S8's text
says so where an adopter will see it.

## 5. Production-readiness checklist

- **security** — none. Fewer things run by default; nothing new is executed and nothing gains reach.
- **perf/scale** — an adopter's full gate loses 29 legs' worth of work. This repo's own bar is
  unchanged by default and loses 47 legs when the switch is off, which is the point of the switch.
- **a11y / i18n** — N/A.
- **error/empty/loading states** — a manifest with EVERY leg `on_demand` and the switch off must
  report a bar of zero legs as a refusal, not as green. That is the empty-population class.
- **observability** — S4 is the observability, and it is in scope rather than assumed.
- **testing/gates** — `run-gates`' own self-tests, govkit's selftest and matrix, plus the full bar.
- **migration/rollback** — an adopter that wants today's behaviour sets `GATE_SELFTESTS=1` in their
  runner's environment. Rollback needs no code change and no re-deploy.
- **help/ docs** — govkit's install summary (S8), `tools/run-gates/README.md`, and `AGENTS.md`'s merge
  bar section, which currently describes guards without mentioning that `GATE_FULL` overrides them for
  this population.

## 6. Acceptance criteria

- **AC1** — a manifest leg marked `on_demand` does not run on a default bar AND does not run under
  `GATE_FULL=1`, observed in `tools/run-gates/run-gates.test.sh`.
- **AC2** — the same leg RUNS with `GATE_SELFTESTS=1`, observed in
  `tools/run-gates/run-gates.test.sh`.
- **AC3** — a skipped `on_demand` leg is reported by name with a count, not omitted, observed in
  `tools/run-gates/run-gates.test.sh`.
- **AC4** — a manifest whose every leg is `on_demand`, with the switch off, refuses rather than
  reporting green, observed in `tools/run-gates/run-gates.test.sh`.
- **AC5** — `on_demand` in a descriptor and in the manifest must agree, and a mismatch is a refusal in
  both directions, observed in `tools/govkit/selftest.py`.
- **AC6** — the 29 descriptor legs carry the flag, asserted by DERIVING the self-test population from
  each `kit.toml` and requiring every member to declare it, observed in `tools/govkit/selftest.py`.
- **AC7** — a target installed by govkit receives the flag on those legs, observed in
  `tools/govkit/matrix.py`.
- **AC8** — govkit's install summary names how to run them once and on demand, observed in
  `tools/govkit/selftest.py`.
- **AC9** — this repo's own bar is unchanged with the switch on and loses exactly the self-test legs
  with it off, observed by `bash tools/run-gates/run-gates.sh`.
- **AC10** — every arm that can fail was observed failing against the pre-fix code, observed in
  `2026-08-23-build-TOOL-dUnstalledConvoy-26-1-red-first.md`.
- **AC11** — the full bar is green, observed by `bash tools/run-gates/run-gates.sh`.

## 7. Gates

`bash tools/run-gates/run-gates.sh`, with `run-gates`' own self-tests and govkit's selftest and matrix
as the legs that exercise this. `GATE_FULL=1` for the Definition of Done.

## 8. Open questions

- **F1 — one repo-wide switch, or per-kit?** RESOLVED: one. A per-kit matrix is a surface nobody
  audits, and its failure mode is a kit silently exempt from its own tests — the shape this repo
  already refuses for path exemptions.
- **F2 — should `GATE_FULL` unlock them?** RESOLVED: no. `GATE_FULL` means "ignore every guard", and
  conflating it with "run the kit's own tests" leaves no way to ask for a complete bar without them.
  It is also the exact bypass that makes today's `guard = ["{kit}/"]` ineffective.
- **F3 — does the flag default to on or off for THIS repo?** RESOLVED: off, like every adopter. This
  repo dogfoods its kits, so it is the one place the switch will routinely be set — but a default that
  differs between the source repo and its targets is two behaviours for one mechanism, and the first
  thing that drifts.

## 9. Revision log

- rev-1 · 2026-08-23 · initial draft. Written against the code: the runner's wire format and its
  `changed()` guard were read before the design, and the 29-leg population was derived from the
  descriptors rather than counted by hand.

## 10. Reuse audit

The runner's per-leg wire format already carries four optional fields and this adds a fifth in the
same shape. `[[gate_leg]]` already carries `guard` and `red_after_land`, and `kind` is an established
descriptor idiom. The descriptor↔manifest cross-check already runs in both directions and already
refuses a stale exemption; S7 extends it rather than adding a second checker. No new file, no new kit.
