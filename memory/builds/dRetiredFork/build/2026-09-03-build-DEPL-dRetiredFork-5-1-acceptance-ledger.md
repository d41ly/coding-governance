# Acceptance ledger — DEPL-dRetiredFork-5

**Serves:** journal DEPL-dRetiredFork-5

Tier-1 · node d · 2026-09-03

`classify_outcome` — the function whose entire docstring is that an `[[outcome]]` block decides what
an exit code MEANS, by probing the filesystem — had exactly ONE call site, inside `_cmd_apply`. Every
declared probe was dead code for `check`.

## Acceptance criteria

**Evidences:** DEPL-dRetiredFork-5

- AC1 — MET — `python tools/govkit/selftest.py` arm `[-5] S3`: the same descriptor with its probe
  path ABSENT does not classify as ok, and `run_kit_check` now routes its exit code through
  `classify_outcome`. Staged and observed RED: with the call replaced by `None` the arm fails with
  "the probe is still dead code for `check`"
- AC2 — MET — the same descriptor with the path PRESENT classifies ok, so the arm cannot pass by
  refusing everything
- AC3 — MET — an entry with no `[[outcome]]` is unchanged: `classify_outcome` returns None both when
  no block matches and when none is declared, so the fall-through is today's answer exactly. At
  inCMS **no verdict changed at all**, which is that property observed on a real tree
- AC4 — MET — recorded below
- AC5 — MET — `selftest` reports all arms held and `selfcheck` exits 0

## AC4 — the verdicts that changed, on real adopters

**NicoCares: three kits moved off a false `adopted`.**

| kit | before | after |
|---|---|---|
| `drift-audit` | `adopted` | `landed-but-inert` |
| `memory-recall` | `adopted` | `landed-but-inert` |
| `run-gates` | `adopted` | `landed-but-inert` |

Counted: `adopted` 5 → 2, `landed-but-inert` 1 → 4, `landed-unmeasured` 9 → 9 unchanged.

**inCMS: no verdict changed.** 2 adopted, 2 landed-but-inert, 10 landed-unmeasured, before and
after. That is AC3's property measured rather than assumed — and it is worth stating plainly,
because a unit that changed nothing anywhere would be indistinguishable from one that did not run.

The nine `landed-unmeasured` rows at NicoCares are untouched by design: §3 keeps that meaning, and it
is a declared absence with a stated reason rather than a verdict this unit could improve.

## What the false `adopted` actually was

The measured case: an adopter's `--check` exits `0` **by absence** — it finds nothing to check and
succeeds. `run_kit_check`'s own docstring says `adopted` means "a check arm that ran and passed", and
the arm passed precisely because the kit was not there.

Three kits at one adopter were reporting installed while being inert. Nothing else in the deployer
would have caught it: the probe that could tell the difference was written, declared in six
descriptors, and never read outside `apply`.
