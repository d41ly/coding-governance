# Acceptance ledger — DEPL-dRetiredFork-3

**Serves:** journal DEPL-dRetiredFork-3

Tier-2 · node d · 2026-09-03

## The headline: the spec's own mechanism was measured impossible, and the alternative it also
## specified is the one that shipped

The spec asks `update` to run each touched kit's `[adopt].argv` (S1) and any declared
`[[regenerate]]` blocks (S2). S1 was built first and then REMOVED, because running the adopter
cannot refresh a stale rendered row. `tools/memory-tree/adopt-memory-tree.sh:58` takes one of
exactly two branches on an adopted tree, and neither re-renders:

- marker present → prints `already scaffolded — nothing to do` and exits 0. A no-op.
- marker absent → `refusing to overwrite`, exits 1, which that kit's `kit.toml` declares as the
  outcome `refused-foreign-tree`.

Both reproduced on a fixture. That is CORRECT behaviour for an adopter and is why re-adoption was
never the missing piece. So the shipped runner executes `[[regenerate]]` blocks only, and a touched
kit that ships `rendered` rows while declaring no such block is DECLINED BY NAME.

## Acceptance criteria

**Evidences:** DEPL-dRetiredFork-3

- AC1 — NOT MET — `tools/memory-tree/adopt-memory-tree.sh:58` is what running the adopter does,
  and the reason is a measurement rather than a shortfall: and both of its
  branches were reproduced on a fixture. Recorded in the code at the decline site, not only here.
- AC2 — MET — `[[regenerate]]` blocks are read from the descriptor and executed per touched kit,
  in declaration order, with `{kit}`-style tokens resolved through `target_context`.
- AC3 — MET — the exit code is routed through `classify_outcome`, exactly as `_cmd_apply`'s
  CONFIGURE step does. Written as `rc != 0` first, which would have failed every update touching
  `memory-tree`, whose adopter exits non-zero BY DESIGN. Third caller to learn this independently;
  `DEPL-dRetiredFork-5` was the second, one unit ago.
- AC4 — MET — a kit named in `deploy.toml`'s `inert` list is declined without being run, asserted
  against the fixture. Running its adopter is a posture flip, which is why `apply` was never the
  workaround for any of this.
- AC5 — MET — a failing regenerate argv calls `r.fail`, so the existing post-write verification
  rolls the run back rather than committing a bad render.
- AC6 — MET, MEASURED — with `GOVKIT_RERENDER` unset, stdout is byte-identical to the pre-change
  binary across 64 lines read-only and 69 lines under `--write`, both at rc 0, over a fixture
  normalised only for its own temp path and throwaway gov sha. With the flag set the step speaks.
  A criterion asserting only silence is satisfied by deleting the feature, so both halves were run.
- AC7 — MET with a CORRECTED figure, from `python tools/govkit/selftest.py`'s `[-3] S6` note.
  The spec says 8 rendered rows at one adopter; the brief
  measured 9 installed. The kit-side population is larger still and is what the defect actually
  spans: **6 kits, 12 rendered rows, zero `[[regenerate]]` declarations** — `drift-audit` 1,
  `lexicon` 1, `memory-recall` 1, `memory-tree` 3, `unattended` 5, `workflows` 1. Printed by
  `python tools/govkit/selftest.py` on every run rather than typed here to rot.
- AC8 — MET — default-OFF, per the spec's own §4 Rollout. This is the first time `update` executes
  target-side code, so it lands dark and is flipped on after in-place verification.
- AC9 — MET — every declined kit is named with its reason under the flag: `GOVKIT_RERENDER=1`
  against a touched fixture printed `DECLINED memory-tree:` and the full sentence. A skip that
  looks like a pass is the class this build keeps closing.
- AC10 — **NOT MET, cannot be.** It requires `--write` against `C:/projects/nicocares/main`, a
  repository this run does not own, and it depends on `DEPL-dRetiredFork-1` S7, whose foreign-write
  question is PARKED for the owner. Not attempted.
- AC11 — **NOT MET, blocked on a pre-existing red.** `tools/govkit/check_runbook_parity.py` already
  exits 1 with 18 problems at HEAD and is invoked by no leg in `tools/gate-legs.json`. Filed as
  `TOOL-dRetiredFork-28`; not caused by this unit and not fixed inside it.
- AC12 — MET — `python tools/govkit/selftest.py` exits 0 with all arms held, and `selfcheck`
  exits 0. Both redded during this unit and both were fixed rather than waived: the declared
  population gate caught the new spawn site undeclared, then caught it mislabelled `gov` when its
  argv resolves target token values through `target_context`.

## Two defects found in this unit's own code before it landed

- **The vacuous selector.** The decline predicate read `role == "rendered"` out of `_d.get("file")`.
  The key is `files`. It parses, type-checks, runs, matches NOTHING, and reports `0 declined` over
  an empty population — indistinguishable from a healthy tree. Caught only because the count was
  zero on a fixture where a kit had been deliberately touched. Now gated: the `[-3] S6` arms assert
  the selector matches a LIVE population and that the wrong key matches nothing, so the class reds
  rather than passing quietly.
- **The naive exit test**, above as AC3.

Both are this repo's own recurring classes, hit inside the unit that exists to close a third one.

## What is deliberately NOT built

No kit gained a `[[regenerate]]` declaration. Every candidate needs a re-render entrypoint its
adopter does not have — `adopt-memory-tree.sh` takes only `--scaffold`, and adding a flag to it is
outside this unit's declared writes. The mechanism ships complete and dark; the declarations that
would use it are `TOOL-dRetiredFork-29`. Until one lands, the runner's observable effect under the
flag is the decline list, which is exactly the true statement about the tree.
