---
slug: aProvenReuse
node: a
opened: 2026-08-31
streams: tooling
roster: TOOL
ids: TOOL-aProvenReuse-1 TOOL-aProvenReuse-2 TOOL-aProvenReuse-3 TOOL-aProvenReuse-4 TOOL-aProvenReuse-5 TOOL-aProvenReuse-6
authorized-by: prompt
---

# aProvenReuse — the reuse-first rule gets a machine half

## The problem this build exists to solve

`reuse-first` is a directive of every unattended run and was enforced by nothing: `grep -n reuse`
over `tools/unattended/unattended.sh` returned one hit, the handle's own name in `DIRECTIVES_CORE`.
The kit's Skill said so — *"Waiving it is SILENT ... nothing machine-checks a spec's reuse section
for content"* — so `N/A — none` was a passing reuse audit and `BUILD-METHOD` M7's regrounding step 5
had no terms to re-run. The size is a derived population and AGENTS.md §7 bans a prose count of one;
the figures, their populations and their dates are in
[the acceptance ledger](build/2026-08-31-build-TOOL-aProvenReuse-1-acceptance-ledger.md) and in
`TOOL-aProvenReuse-1` §6. The owner's prose is the mandate, recorded under
[prompts/](prompts/2026-08-31-prompt-TOOL-aProvenReuse-1.md).

## Expected improvements

- A post-cutoff Tier-2 spec cannot land claiming a reuse audit it did not record; everything landed
  is grandfathered by the same cutoff idiom four sibling keys already use.
- M7 regrounding step 5 becomes executable for specs written from the cutoff on.
- A run that never probed cannot reach `--close` silently, and a `reuse-first` waiver stops being
  silent — `reuse-probed` names the waiver and its reason.

## Detriments if this is not built

- Every future build keeps paying to rediscover seams the tree already has.
- The waiver mechanism keeps reporting coverage it does not have.
- `reuse-first` stays the one handle in a 16-handle set whose satisfaction leaves no trace on disk.

## Build-level rules

- **Classification (M2)**: all three units MISSING at open, authored this run. Units 1 and 2 are
  **Tier-2** — each changes a kit's contract and the pair is cross-kit. Unit 5 is Tier-1, and its §8
  Q1 records why a contract DISCLOSURE is not a contract change.
- **Two mechanisms, two units, split on the tracked/local boundary.** Unit 1's evidence is a tracked
  file, so it works in any clone and belongs on the bar. Unit 2's is a node-local log in the git
  common dir, so it could never be a bar leg.
- **Neither unit may red a landed spec — and "landed" includes other branches.** Round 1 found that
  rule broken by the build that wrote it; the cutoff is dated ahead of every dated spec on every live
  branch, which costs this build the ability to grade its own specs. Recorded in unit 1 §4 Migration.
- **Two populations, not interchangeable.** The all-tiers §10-bearing count and the Tier-2 subset the
  predicate actually reaches are different numbers; a criterion pinned to the wrong one fails a
  correct implementation. Confirmed three times across two rounds. Both are derived where used.
- **Both review loops exited NON-CONVERGENT** — spec audit at 4, 4 and closing diff review at 2, 1,
  1. Every standing blocker was folded as a `rev` bump rather than promoted to a unit: none was a
  MECHANISM, so a promoted unit is one M2 forbids, and its spec would owe an audit — the regress
  non-convergence exists to stop. The rule's gap is `TOOL-aProvenReuse-3`.
- **Every round's blocker was in the FOLD, never in the code the fold was closing**, and the rate did
  not fall. That is why the loop stopped, rather than a reason to run another round. The rounds are
  in [reviews/](reviews/).

## Parked decisions

None. Nothing was refused for the owner: every fork was resolvable under the delegated authority, and
every finding was folded, adopted as a unit, or filed. Parked entries would live in `RUN.md`.

**Filed rather than built**, because a finding with no disposition is a finding discarded:
`TOOL-aProvenReuse-3` (M4's NON-CONVERGENT disposition has no referent when the subject is a spec),
`TOOL-aProvenReuse-4` (the `reuse_lookup.py` liveness gap needs a cross-kit dependency, so it fails
protocol §11's strictly-beneficial test), `TOOL-aProvenReuse-6` (the unattended suite's
bounded-observation arms are wall-clock assertions that flake under fleet load, measured three
times).

**One review claim REFUTED rather than folded**, written here so nobody re-derives it: round 3
reported that a fenced `--terms` invocation now reds where it previously passed. Reproduced through
the SHIPPED fence machine, which unfences `body[]` before the arm runs — that section reds on the
TERMS arm, identically at both revisions. The round tested with a standalone predicate that does not
strip fences, which is `second-implementation-is-not-a-second-opinion`.

**One hole DECLARED rather than fixed**: a §10 writing its terms VALUES first and the marker last
puts those values in the probe blob, so one line can satisfy both arms. Nothing here is written that
way and no gate catches it; the spec template says so in its own §10 section.

<!-- roster:units -->

| # | Unit | Status | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aProvenReuse-1` | CLOSED | hygiene check 12 grades §10's CONTENT, behind a declared cutoff |
| 2 | `TOOL-aProvenReuse-2` | CLOSED | a `reuse-probed` DoD item joins the run to the recall query log |
| 3 | `TOOL-aProvenReuse-5` | CLOSED | the example-conf parity arm reaches bare presets |

*All three spec headers read `CLOSED` too. Round 2's F14 found the fold flipping these cells while
leaving both headers at `OPEN`, and the generated table below — which DERIVES from those headers —
still saying `OPEN` in the same commit.*
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 3 unit(s) · node a · opened 2026-08-31 · streams tooling
ids TOOL-aProvenReuse-1 TOOL-aProvenReuse-2 TOOL-aProvenReuse-3 TOOL-aProvenReuse-4 TOOL-aProvenReuse-5 TOOL-aProvenReuse-6

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aProvenReuse-1 — hygiene check 12 grades §10's CONTENT, behind a declared cutoff](spec/2026-08-31-spec-TOOL-aProvenReuse-1.md) | 1 | 2 | CLOSED | rev-5 | 2026-08-31 |
| [TOOL-aProvenReuse-2 — a `reuse-probed` DoD item joins the run to the recall query log](spec/2026-08-31-spec-TOOL-aProvenReuse-2.md) | 2 | 2 | CLOSED | rev-7 | 2026-08-31 |
| [TOOL-aProvenReuse-5 — the example-conf parity arm reaches bare presets](spec/2026-08-31-spec-TOOL-aProvenReuse-5.md) | 3 | 1 | CLOSED | rev-1 | 2026-08-31 |
<!-- /gen:build-units -->

Records: 7 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-aProvenReuse-5.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aProvenReuse-1` | no |
| 2 | `TOOL-aProvenReuse-2` | no |
| 3 | `TOOL-aProvenReuse-5` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
