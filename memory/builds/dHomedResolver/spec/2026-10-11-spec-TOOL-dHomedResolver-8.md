# TOOL-dHomedResolver-8 — the three reds the reconcile brought in, which this landing cannot carry

**Status:** CLOSED · rev-1 · 2026-10-11 · node d · Tier-1 · base 584e6557 · streams tooling · order 6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-build-TOOL-dHomedResolver-8-1-acceptance-ledger.md](../build/2026-10-11-build-TOOL-dHomedResolver-8-1-acceptance-ledger.md) | journal | — |
| [2026-10-11-prompt-TOOL-dHomedResolver-8-1-build-brief.md](../prompts/2026-10-11-prompt-TOOL-dHomedResolver-8-1-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The close's flagged bar over the prepared merge onto `origin/main` at `b726385f` read seven legs red.
Two were this build's (an adopter named in shipped comments, fixed by `TOOL-dHomedResolver-5`); the
other five red identically at `b726385f` itself. Three of those five read OWN on any landing of this
build: the hygiene suite because this build edits it (KF3), and push-main's suite and the
routed-commits leg because their graders' directories are ones this build or its mint touch. Fix
those three; the remaining two, govkit's self-test and the foreign-prefix leg, stay inherited.

## 2. Scope (IN)

- **S1** — The hygiene suite's python-key parity arm exempts `ROUTED_PATHS`, `ROUTED_COMMIT_CUTOFF`
  and `ROUTED_COMMIT_WAIVED`, each with its reason: the example declares them COMMENTED because
  `adopt-memory-tree.sh` appends them only when neither is assigned, so an uncommented blank would
  skip that append. It also exempts `GATE_PUSH_BASE`, an environment variable. Observed by AC1.
- **S2** — `push-main.test.sh` arm 26's fixture commits a spec defining `TOOL-tFix-26` beside the
  runlog edit, because the lander's mint names only a unit a spec at HEAD defines
  (TOOL-aRoutedQuill-12 S2). Observed by AC2.
- **S3** — `.memory-tree.conf`'s `ROUTED_COMMIT_WAIVED` gains `36db2dbf`, aBenchedProbe's docs
  commit that reached this branch by the reconcile of `b726385f`, re-derived as the list's own header
  says. Observed by AC3.

## 3. Non-goals (OUT)

- govkit's self-test and the foreign-prefix leg: red at `b726385f` in kits this build does not touch,
  so they read INHERITED and land under the declared `land` policy.
- Uncommenting the routed keys in the example, which would break the adopter's scaffold.

## 4. Design

### Files touched (estimate)

- `tools/memory-tree/check-memory-hygiene.test.sh`
- `tools/push-main.test.sh`
- `.memory-tree.conf`

### Alternatives rejected

- **Declare the routed keys uncommented and blank in the example.** Rejected: `adopt-memory-tree.sh`
  copies the example and appends the routed keys only when neither is assigned, so a blank line
  would silently disarm the write gate on every new adopter.

## 6. Acceptance criteria

- **AC1** — When `check-memory-hygiene.sh`'s suite runs its python-key parity arm, it prints no
  `does not declare` line for `ROUTED_PATHS`, `ROUTED_COMMIT_CUTOFF`, `ROUTED_COMMIT_WAIVED` or
  `GATE_PUSH_BASE`. Red when: the exemption list loses a name, or names one no module reads.
- **AC2** — When the push-main suite's arm 26 runs, it prints `26 the attended mint commit names the
  range's newest unit`. Red when: the fixture's unit has no spec.
- **AC3** — When `routed_commits.py` runs with `GATE_PUSH_BASE` unset, it lists no FAILED commit.
  Red when: a landed commit naming no unit is neither fixed nor waived.

## 7. Gates

`memory-hygiene self-test` · `push-main self-test` · `routed commits name a specced unit` · `memory hygiene` · `kit/dogfood doc parity` · `recall floor` · `transition-audit arms` · `straggler-guard arms` · `spec tokens (a spec's own names resolve)`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft, from the close's flagged bar over the prepared merge.

## 10. Reuse audit

No new seam: each fix extends the existing exemption list, the existing arm-26 fixture and the
existing waiver list, the last re-derived as its own header instructs. `reuse_lookup.py` was not
re-run: nothing here is a mechanism.

Recall terms used: gen_build_index ids derived git ls-files untracked archive rotation half-staged write check drift corpus membership
