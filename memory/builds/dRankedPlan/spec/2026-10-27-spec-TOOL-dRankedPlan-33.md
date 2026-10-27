# TOOL-dRankedPlan-33 — the shared `plan.exit` fixtures plant a witnessed plan record, so the precondition holds only where a plant removes it

**Status:** OPEN · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 11 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dRankedPlan-30-promoted-fix-return.md](../build/2026-10-27-build-TOOL-dRankedPlan-30-promoted-fix-return.md) | research | TOOL-dRankedPlan-30 TOOL-dRankedPlan-32 TOOL-dRankedPlan-37 |
| [2026-10-27-build-TOOL-dRankedPlan-33-deviation-331.md](../build/2026-10-27-build-TOOL-dRankedPlan-33-deviation-331.md) | deviation | — |
| [2026-10-27-prompt-TOOL-dRankedPlan-30-promoted-fix-brief.md](../prompts/2026-10-27-prompt-TOOL-dRankedPlan-30-promoted-fix-brief.md) | research | TOOL-dRankedPlan-30 TOOL-dRankedPlan-32 TOOL-dRankedPlan-37 |
| [2026-10-27-review-TOOL-dRankedPlan-30-spec-audit.md](../reviews/2026-10-27-review-TOOL-dRankedPlan-30-spec-audit.md) | spec-audit | TOOL-dRankedPlan-34 TOOL-dRankedPlan-35 TOOL-dRankedPlan-30 TOOL-dRankedPlan-31 TOOL-dRankedPlan-32 TOOL-dRankedPlan-36 TOOL-dRankedPlan-37 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 19 to 29
(`memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-19-spec-audit.md`) confirmed
**finding 21 at HIGH**, item **H3**. Findings 1 and 32 are the same defect at MEDIUM, item M1, and
`TOOL-dRankedPlan-37` closes them. `TOOL-dRankedPlan-19` S1 puts a witnessed plan record, read through a
resolved memory-tree kit, in front of every `plan.exit` admission. The shared `ratify.py --fixture`
(`TOOL-dRankedPlan-9` S7, `TOOL-dRankedPlan-10` §4 "The plants") plants a loop kit copy, a policy file
and a build in `planning`, with no memory-tree kit and no plan record. So from order 10 every plant
that records an admitted `plan.exit` move reads `held · item.plan.record unread` and stays red. Unit
19 names none of them, and the cheap way out is to weaken its precondition. This unit gives the shared
fixture one seed, a copied memory-tree kit and a witnessed plan record for `tFix`, used by every plant
except the three that remove it on purpose and by unit 10's driver fixture. It repairs
`TOOL-dRankedPlan-19`, so it sits one order above it.

## 2. Scope (IN)

- **S1** — The seed. `seed_plan_witness(repo, slug)` in `tools/loop/ratify.py` copies the memory-tree
  kit into the scratch repository beside its loop kit copy. The kit is found by the loop kit's inline
  `resolve_kit_dir("memory-tree", "plan_record.py", here)`, and the kit's example conf,
  `.memory-tree.conf.example`, becomes the scratch repository's `.memory-tree.conf`. It then writes the
  build's plan record through the copied door, `gov_record.py new plan --build <slug> --unit
  TOOL-<slug>-1 --title "Plan — <slug>"`, with `Problem` and `Goal` set and every other field `none`
  (`TOOL-dRankedPlan-16` S3), and commits it. Last, it runs the copied `plan_record.py check <slug>` and
  raises naming the line unless it reads `item.plan.record — witnessed`, so a field check that refuses
  the seed reds the fixture at its base and never inside a plant. `python tools/loop/ratify.py
  --fixture --seed <dir> --build <slug>` runs S1 over an existing repository. Observed by AC1.
- **S2** — The shared base. Every plant of `ratify.py --fixture` is seeded by S1 for `tFix` before its
  own steps, except these three, which keep their own state: `plan-record-absent` leaves the build
  with no record, `plan-record-unread` leaves the repository with no copied memory-tree kit, and
  `plan-record-open-probe` writes its own record with its eleven fields in place of the seed
  (`TOOL-dRankedPlan-19` S3). This supersedes the "build in planning"
  base of `TOOL-dRankedPlan-10` §4 "The plants" and `TOOL-dRankedPlan-9` S7. Observed by AC2, AC3 and
  AC4.
- **S3** — The driver's fixture. The fixture of `TOOL-dRankedPlan-10` AC8 in
  `tools/unattended/unattended.test.sh` seeds its repository through S1's `--fixture --seed` before its
  `--phase` move. The loop kit is found by the suite's existing `resolve_kit_dir` route, as it finds the
  memory-tree kit (`tools/unattended/unattended.test.sh:81`). Observed by AC5.

## 3. Non-goals (OUT)

- The precondition itself: `TOOL-dRankedPlan-19` S1, unchanged.
- The other fixtures that record an admitted `plan.exit` move, meaning `gen_build_index.py`'s
  `drafts-cross-session` plant and `plan_revision.py --selftest` (findings 1 and 32):
  `TOOL-dRankedPlan-37` seeds them through S1.
- Reconciling unit 19 AC2 with unit 10 AC6 in their texts (finding 32): `TOOL-dRankedPlan-37`'s. Under S2
  the two hold over different states, a seeded record and a removed one.
- Any plan field's check: units 11 to 14. The seed is the record those checks already admit.

### Edges

- **consumes-from** `TOOL-dRankedPlan-19` — S1's witnessed-record precondition, which makes the seed necessary, and the three `plan-record-*` plants S2 leaves unseeded
- **consumes-from** `TOOL-dRankedPlan-9` — S7's `ratify.py --fixture` and its scratch repository, the base S2 seeds
- **consumes-from** `TOOL-dRankedPlan-10` — §4's plants and AC8's driver fixture, which S2 and S3 seed and AC2 and AC5 re-run
- **consumes-from** `TOOL-dRankedPlan-16` — S3's door form and `plan_record.py check`, the record S1 writes and the witness line it asserts
- **consumes-from** `TOOL-dRankedPlan-25` — the `fallback-reentry` and `codex-reentry` plants, which AC3 re-runs over the seeded base
- **consumes-from** `TOOL-dRankedPlan-26` — the `holding-ask` plant, whose following `continue` record AC3 re-runs over the seeded base
- **consumes-from** external — dTotalRecall's door `gov_record.py new` (TOOL-dTotalRecall-2 S1), run from the copied memory-tree kit
- **hands-off** `TOOL-dRankedPlan-37` — S1's `--fixture --seed`, through which that unit's item for finding 1 seeds the `drafts-cross-session` plant and `plan_revision.py --selftest`
- **hands-off** `TOOL-dRankedPlan-45` — `seed_plan_witness`, `--seed`, S2's plants and §5's perf line, which that unit's items for findings 5, 11, 37 and 32 correct; carry S5, S8, S21 and S31 of that unit into this unit's pass (spec audit of units 30 to 37)

## 4. Design

### Evidence

- `TOOL-dRankedPlan-19` S1: the precondition holds "before every admission: `met`, `before-placement`
  and a disposition record alike", and a missing memory-tree kit refuses `unread`.
- `TOOL-dRankedPlan-10` §4 "The plants": the fixture is "a loop kit copy, a policy file, a build in
  `planning`", joined to `TOOL-dRankedPlan-9` S7's repository, claim ref, request record and policy file.
  Unit 9 plants a plan record only for `signed-commit` (§4 "The plants").
- The plants recording an admitted move at order 10 and later: unit 10 AC1, AC2 and AC6; unit 21 AC1,
  over unit 10 AC2's move; unit 25 AC1 and AC2; unit 26 AC1. The audit's appendix rows for ids 21 and
  32 list them.
- `tools/unattended/unattended.test.sh:81` already resolves the memory-tree kit with
  `resolve_kit_dir "$_rkd_py" memory-tree gen_build_index.py "$HERE"`, the route S3 takes to the loop kit.

### The base after this unit

| Plant | Memory-tree kit | Plan record | Expected after unit 19 |
|---|---|---|---|
| every plant but the three below | copied | the seed, witnessed | as its own unit states |
| `plan-record-absent` | copied | removed | refused, `unwitnessed` |
| `plan-record-unread` | removed | the seed | refused, `unread` |
| `plan-record-open-probe` | copied | its own, `Probes owed` set | refused, then admitted once the probe returns |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `seed_plan_witness` | function, `tools/loop/ratify.py` | `py.function`; `python tools/lexicon/lexicon.py --suggest seed_plan_witness --as py.function` answered OK |
| `--seed`, used with `--build` | flags of `ratify.py`, under `--fixture` | none |

### Rollout

Live at landing. The plants that read red from order 10 read green again at this unit's tip.

### Files touched (estimate)

- `tools/loop/ratify.py`: S1, S2
- `tools/unattended/unattended.test.sh`: S3

### Alternatives rejected

- **A fixture bypass of the precondition.** It would be a fail-open path in the gate, the shape the
  audit names as the cheap way out.
- **A plan record typed into the fixture as a file.** It would be a second writer of the kind beside its
  door, and a field check that later refuses it would not be seen until a plant failed for an unrelated
  reason. The door and the asserted witness see both at the base.
- **A seed in each fixture.** `TOOL-dRankedPlan-37` needs the same seed in two more fixtures, and the
  charter's `[reuse]` rule asks for one helper at the second instance.

## 5. Production-readiness checklist

- security — no new write path in the product: S1 writes only inside a scratch repository or the
  directory `--seed` names, which the callers create.
- perf / scale — one door run, one commit and one check per plant.
- error / empty / loading states — a seed the check does not witness raises naming the check's line;
  a kit that does not resolve raises naming the anchor.
- observability — the raise names the witness line, and the fixture's plants keep their own lines.
- risks — every plant now depends on the memory-tree kit resolving beside the loop kit, which
  `TOOL-dRankedPlan-13` S8 already requires of the loop kit.
- testing — AC1's seed check and the re-run plants, red without the seed and green with it.
- migration — none.
- user docs — N/A — fixture only.

## 6. Acceptance criteria

- **AC1** — When `python ratify.py --fixture --seed <dir> --build tFix` runs over a fresh scratch
  repository holding a loop kit copy, `python plan_record.py check tFix` in that repository prints
  `item.plan.record — witnessed`.
  Red when: the seed writes a record the check does not witness, or no memory-tree kit is copied.
- **AC2** — When the plants `claude-adapter` and `pre-placement` run at the pass tip, with
  `TOOL-dRankedPlan-19` S1 in place, the `plan.exit` move through `python loop_transition.py record`
  exits 0 in each.
  Red when: a plant built on the shared base reads `item.plan.record unread` or `unwitnessed`.
- **AC3** — When the plants `fallback-reentry` and `codex-reentry` run, the second move exits 0 once
  its new disposition record is committed, and when the plant `holding-ask` runs, its following
  `continue` record admits the move.
  Red when: a repair plant of order 5 stays red after the precondition lands.
- **AC4** — When the plants `plan-record-absent` and `plan-record-unread` run, each move still exits 1
  printing `unwitnessed` and `unread` respectively.
  Red when: the seed leaks into a plant that removes the record or the kit on purpose.
- **AC5** — When unit 10 AC8's fixture, seeded by `ratify.py --fixture --seed`, runs `bash
  tools/unattended/unattended.sh --phase tFix RESEARCHING --witness <sha>`, the move is refused and
  its `decision` row carries `intake not installed`; after a disposition record naming that row is
  committed, the move is admitted.
  Red when: the driver's plan gate holds on `item.plan.record` instead of the fallback.
  fixture: the repository unit 10 AC8 builds, under a short `%TEMP%` path.

## 7. Gates

`unattended kit gate` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

New arm: tools/loop/ratify.py · covers AC1 AC2 AC3 AC4 · the shared base seeded by `seed_plan_witness`, staged by a base with no seed, where AC2's plants read `item.plan.record unread` · none

New arm: tools/unattended/unattended.test.sh · covers AC5 · unit 10 AC8's arm over the seeded fixture, staged by its fixture without the seed · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 19 to 29, finding 21 (HIGH,
  item H3; findings 1 and 32 are its medium face), repairing `TOOL-dRankedPlan-19`.
- rev-2 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-45`, each the reciprocal of that promoted unit's own edge (spec audit of units 30 to 37, `reviews/2026-10-27-review-TOOL-dRankedPlan-30-spec-audit.md`); no other section moves.

## 10. Reuse audit

The seams extended are `TOOL-dRankedPlan-9` S7's fixture, which every plan.exit plant already shares,
and the plan record kind's own door and check (`TOOL-dRankedPlan-16` S3), reached through the inlined
`resolve_kit_dir` (`tools/lib/resolve_kit_dir.py`). No code exists at base 0689e7fa, where the loop kit
and the plan kind are unbuilt. `python tools/codebase-map/reuse_lookup.py "seed a fixture repository
with a witnessed record before each plant"` ranked `before`, `seed`, `fixture` and `build_fixture`
(`tools/lib/lib-selftest.sh`, `tools/memory-tree/routed_commits.py`), each a shell or Python builder of
its own kit's scratch tree that writes no plan record, so no existing seam fits beyond the fixture this
unit extends. The recall query returned TOOL-dLoggedFlight-26 and -28, whose arms assert over what a
shared fixture builder placed, and this audit's H3 item, and they agree.

Recall terms used: `python tools/memory-recall/query.py "what does a shared fixture owe when a gate gains a precondition" --terms "shared fixture precondition plan record witnessed plants re-green memory-tree kit copy seed"`
