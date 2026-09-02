# DEPL-dRetiredFork-5 — `check` runs the `[[outcome]]` probe instead of grading an exit code

**Status:** OPEN · rev-1 · 2026-09-02 · node d · Tier-1 · base b0108f13 · streams deployer · order 6

<!-- gen:spec-records -->

*No record names this unit.*

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

## 9. Revision log

- rev-1 - 2026-09-02 - initial draft, authored from the dRetiredFork fork classification
  against gov at b0108f13.
