# DEPL-dRetiredFork-5 — `check` runs the `[[outcome]]` probe instead of grading an exit code

**Status:** CLOSED · rev-3 · 2026-09-03 · node d · Tier-1 · base b0108f13 · streams deployer · order 6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-03-build-DEPL-dRetiredFork-5-1-acceptance-ledger.md](../build/2026-09-03-build-DEPL-dRetiredFork-5-1-acceptance-ledger.md) | journal | — |
| [2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round1.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round1.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-4 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 TOOL-dRetiredFork-1 TOOL-dRetiredFork-2 TOOL-dRetiredFork-3 TOOL-dRetiredFork-4 TOOL-dRetiredFork-5 TOOL-dRetiredFork-6 TOOL-dRetiredFork-7 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-10 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-18 |
| [2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round2.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round2.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-4 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 TOOL-dRetiredFork-1 TOOL-dRetiredFork-2 TOOL-dRetiredFork-3 TOOL-dRetiredFork-4 TOOL-dRetiredFork-5 TOOL-dRetiredFork-6 TOOL-dRetiredFork-7 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-10 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-18 |

<!-- /gen:spec-records -->

## 1. Goal

`run_kit_check` ends `return ("adopted" if rc == 0 else "landed-but-inert")`, and
`classify_outcome` — the function whose whole docstring is that an `[[outcome]]` block decides the
meaning of an exit code by a filesystem PROBE — has exactly one call site, inside `_cmd_apply`. So a
descriptor's `[[outcome]]` with `probe = { must_exist = … }` is dead code for `check`. Measured on
inCMS: `adopt-lexicon.sh --check` exits `0` by ABSENCE, so `check` printed `lexicon: adopted` for a
kit with no conf, no Skill and no importable module. The docstring says `adopted` means "a check arm
that ran and passed"; the arm passes when the kit is not there. This is `TOOL-aFlaggedScaffold-5`.

## 2. Scope (IN)

- **S1** — `run_kit_check` routes its exit code through `classify_outcome` with the entry's
  `[[outcome]]` blocks, exactly as `_cmd_apply` does.
- **S2** — An entry with no `[[outcome]]` keeps today's behaviour, so no descriptor is retroactively
  broken; the difference is that a descriptor which DID declare a probe now has it honoured.
- **S3** — An arm reproducing the measured inCMS case: a kit whose adopter exits `0` by absence and
  whose probe's `must_exist` is not satisfied reports `landed-but-inert`, not `adopted`. Observed
  RED first.
- **S4** — Re-run `check` read-only against both adopters and record which kit verdicts change. Ten
  of NicoCares' fifteen currently report `landed-unmeasured`, so the moving set is not obvious.

## 3. Non-goals (OUT)

- Adding `[[outcome]]` blocks to descriptors that lack one. That is per-kit authoring and belongs
  with each kit.
- Changing what `landed-unmeasured` means. It is a declared absence with a stated reason and stays.

## 6. Acceptance criteria

- **AC1** — When a kit's adopter exits `0` and its `[[outcome]]` probe's `must_exist` path is
  absent, `python tools/govkit/govkit.py check --target <fixture>` reports `landed-but-inert`; the
  pre-change command reported `adopted`.
- **AC2** — When the probe is satisfied, the same command reports `adopted`.
- **AC3** — When an entry declares no `[[outcome]]`, its verdict is unchanged from the pre-change run.
- **AC4** — A read-only `check` against both adopters is recorded with every changed verdict named.
- **AC5** — `python tools/govkit/selftest.py` and `selfcheck` exit `0`.

## 7. Gates

`govkit selfcheck` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix`.

## 8. Open questions

none - `classify_outcome` has exactly one call site and the probe it runs is the one
its own docstring describes; there is nothing to choose between. This section is present
because a section 8 with neither an item nor a `none` form is a refusal, not a pass, and both
this spec's readers grade it that way.

## 9. Revision log

- rev-1 - 2026-09-02 - initial draft, authored from the dRetiredFork fork classification
  against gov at b0108f13.
- rev-2 . 2026-09-02 . added the section 8 `none` declaration both readers require;
  no design content changed.

- rev-3 . 2026-09-03 . BUILT. `run_kit_check` routes its exit code through `classify_outcome`, so a
  declared `[[outcome]]` probe is read by `check` and not only by `apply`. THREE KITS AT NICOCARES
  moved off a false `adopted` -- drift-audit, memory-recall and run-gates -- with the counts going
  adopted 5 to 2 and landed-but-inert 1 to 4. At inCMS NOTHING changed, which is S2's
  no-descriptor-broken property measured on a real tree rather than asserted.

  The staged break is the join itself: replacing the call with None reds the arm with "the probe is
  still dead code for `check`", which is the state the codebase was in.

