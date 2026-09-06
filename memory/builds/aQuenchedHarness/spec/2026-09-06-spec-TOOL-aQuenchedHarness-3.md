# TOOL-aQuenchedHarness-3 — a self-test never reaches an adopter, as a leg or as a file

**Status:** OPEN · rev-3 · 2026-09-06 · node a · Tier-2 · base faaea5f5 · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-06-prompt-TOOL-aQuenchedHarness-1.md](../prompts/2026-09-06-prompt-TOOL-aQuenchedHarness-1.md) | research | TOOL-aQuenchedHarness-1 TOOL-aQuenchedHarness-5 |
| [2026-09-06-review-TOOL-aQuenchedHarness-1-spec-audit-round1.md](../reviews/2026-09-06-review-TOOL-aQuenchedHarness-1-spec-audit-round1.md) | spec-audit | TOOL-aQuenchedHarness-1 TOOL-aQuenchedHarness-2 TOOL-aQuenchedHarness-4 TOOL-aQuenchedHarness-5 TOOL-aQuenchedHarness-6 TOOL-aQuenchedHarness-7 |
| [2026-09-06-review-TOOL-aQuenchedHarness-1-spec-audit-round2.md](../reviews/2026-09-06-review-TOOL-aQuenchedHarness-1-spec-audit-round2.md) | spec-audit | TOOL-aQuenchedHarness-1 TOOL-aQuenchedHarness-2 TOOL-aQuenchedHarness-4 TOOL-aQuenchedHarness-5 TOOL-aQuenchedHarness-6 TOOL-aQuenchedHarness-7 TOOL-aQuenchedHarness-8 |

<!-- /gen:spec-records -->

## 1. Goal

Stop shipping this repo's kit self-tests into adopter repositories. Enumerated at HEAD rather than
described: the kit descriptors carry **52** `[[gate_leg]]` rows, **27** of which name a leg whose row
in `tools/gate-legs.json` satisfies the runner's hold predicate, `subject == kit OR chunk ==
selftests`. `govkit`'s apply copies all 52 into a target's manifest, because `chunk` reaches no
adopter manifest and the apply path never opens gov's own. An adopter therefore runs 27 suites that
grade kit source they never edit, on every bar.

## 2. Scope (IN)

- **S1** — ONE helper, in `tools/govkit/govkit.py`, that reads `tools/gate-legs.json` and returns the
  two name-keyed maps `subject` and `chunk`. Both `selfcheck` and `_cmd_apply` call it, so the hold
  predicate has ONE spelling. Rev-2 said the apply path could read maps `selfcheck` already builds;
  it cannot — they are locals of `selfcheck`, and `_cmd_apply` (`:4258`) reads `subject` off the
  DESCRIPTOR and never opens the manifest at all.
- **S2** — at APPLY time, a descriptor `[[gate_leg]]` row whose gov-manifest twin satisfies the hold
  predicate is DROPPED. The 27 rows §1 enumerates are that set today.
- **S3** — at APPLY time, a descriptor row naming a leg the gov manifest does not carry is a REFUSAL,
  not a shipped row. `selfcheck` already refuses this, but a selfcheck-time property does not bind an
  apply run, and rev-2 asserted a guarantee from the wrong verb. At HEAD the set is empty, which is
  why the arm staging one is mandatory rather than optional.
- **S4** — the self-test FILES are withheld by the mechanism the tree ALREADY uses: a second
  `[[files]]` rule claiming the self-test paths with `role = "project-owned"`, exactly as
  `tools/run-gates/kit.toml` already withholds `run-gates.gov.test.sh`. Rev-2 said "drop the claim",
  which is not an operation `govkit` offers and which states the contract backwards: an unclaimed path
  is not withheld, it is unowned.
- **S5** — **THE TWO HALVES ARE JOINED: no emitted leg's argv may name a file the emit does not
  ship.** Enumerated at HEAD: of the 25 rows that keep shipping, exactly three name a `.test.sh` —
  `kit/dogfood doc parity` and `marker contracts` (`tools/memory-tree/kit.toml`) and
  `review-protocol parity (kit vs dogfood)` (`tools/workflows/kit.toml`). All three are
  `subject = repo` checks an adopter SHOULD run, so their files KEEP SHIPPING and S4's
  `project-owned` rule must not claim them. That is the disposition, decided by enumeration.
- **S6** — the apply REPORTS what it withheld, per target: every leg by name and every file by path,
  with a withheld count of zero printed as a zero rather than as silence.
- **S7** — a gate leg asserting THREE properties over a freshly emitted fixture target: no emitted leg's
  gov twin satisfies the hold predicate; no emitted leg's argv names a file the target did not
  receive (S5's join); and the emitted leg count is strictly less than 52, so a filter that drops
  nothing cannot report clean.
- **S8** — `tools/run-gates/run-gates.sh` is NOT touched. The local hold predicate, the set of legs it
  holds, and `GATE_SELFTESTS` are all exactly as they are today.
- **S9** — arms staging: a descriptor leg whose twin is `subject = kit`; one whose twin is
  `chunk = selftests`; one whose twin is neither; one naming a leg the gov manifest does not carry;
  a `project-owned` file rule; and an emitted manifest hand-edited to contain a held leg.

## 3. Non-goals (OUT)

- Not adding `chunk` to the descriptor schema. `TOOL-aScouredKit-27` records why that is a
  five-declaration act against a PINNED key set the `run-gates canary` asserts. S1 makes it
  unnecessary rather than doing it.
- Not deriving anything from a filename. Rev-1 did, and the measurement is why it is gone: that
  predicate selects 53 of 94 legs and four of them are `subject = repo` on purpose, one being the
  codebase-map coverage gate `AGENTS.md` §5 and §7 forbid exempting.
- Not withholding the three `subject = repo` test files S5 names. They belong to checks an adopter
  runs.
- Not changing which legs run in THIS repo. S8 states it and AC6 measures it as an EQUALITY.
- Not the on-demand runner, which is `TOOL-aQuenchedHarness-4`.
- Not removing an adopter's ability to obtain the withheld suites. They are in the public repository
  and S4's rule records where; what stops is the automatic copy and the bar leg.

## 4. Design

### Data model

No new key. The fields that decide are `subject` and `chunk` in `tools/gate-legs.json`, and the
withholding marker is `role = "project-owned"`, which `tools/run-gates/kit.toml` already uses. What is
NEW, and rev-2 wrongly denied, is one shared reader: `_cmd_apply` does not open the manifest today, so
the predicate cannot be evaluated there without one. S1 makes it a single helper rather than a second
spelling, which is §12's single-source rule applied to the thing this build keeps citing.

### Rollout

An adopter's next apply produces a manifest with 25 rows instead of 52 and a file set without the
withheld suites. Nothing in their tree breaks: the removed legs graded files they do not edit, files
already on disk are not deleted by an apply, and S5's join guarantees no surviving leg names a file
they no longer receive.

### Inventory

- `read_leg_holds` — the shared helper returning the two name-keyed maps; named for what it reads.
- `no self-test reaches an adopter` — the new gate leg's name in `tools/gate-legs.json`.

### Files touched (estimate)

`tools/govkit/govkit.py` · every `tools/*/kit.toml` gaining a `project-owned` files rule ·
`tools/gate-legs.json` · `tools/govkit/selftest.py` · `WIRE-INTO-PROJECT.md`.

### Alternatives rejected

**A filename-derived predicate** — rev-1's design — rejected by measurement: 53 of 94 legs selected,
four repository checks held off every bar. It also re-decides by filename the population
`run-gates.sh:875-885` records as decided by what a FAILURE MEANS, which `TOOL-dUnstalledConvoy-30`
says "decided four legs wrongly" the last time it was tried.

**Reusing `selfcheck`'s maps from the apply path** — rev-2's design — rejected because they are
locals of a different verb and the apply path never opens the manifest.

**Dropping the `[[files]]` claim** — rev-2's design — rejected because it is not an operation the
deployer offers, and because an unclaimed path is unowned rather than withheld.

## 5. Production-readiness checklist

- security — an adopter receiving fewer executable legs and fewer executable files is a narrowing.
  S5's join is what stops the narrowing producing a manifest that points at nothing.
- perf / scale — one manifest read per apply, two dictionary lookups per descriptor leg.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — a descriptor leg with no manifest twin REFUSES at apply time (S3);
  a withheld count of zero is printed as zero; an unreadable manifest fails rather than shipping
  everything.
- observability — S6's per-target report, both counts and both name lists.
- risks — a false positive now requires a leg to be MIS-DECLARED in `tools/gate-legs.json`, which the
  `run-gates canary` and `govkit selfcheck` already grade. The residual risk is a leg correctly held
  here that an adopter wants; S4's rule records where to get it.
- testing + left-shift gates — S9's arms, each observed RED before landing, plus S7's three-property
  leg.
- migration / rollback — reverting the helper call sites restores today's apply. No adopter state is
  written that needs undoing.
- user docs — `WIRE-INTO-PROJECT.md` gains one sentence on what adopters no longer receive and where
  the withheld suites live.

## 6. Acceptance criteria

- **AC1** — When `govkit` applies to a fixture target, the emitted manifest carries 25 rows against
  gov's 52, and no emitted row's gov twin satisfies `subject == kit OR chunk == selftests`.
- **AC2** — When a descriptor names a leg `tools/gate-legs.json` does not carry, the apply REFUSES
  naming it, rather than shipping the row.
- **AC3** — When the manifest `govkit` emits is checked against the emitted file set, no leg's argv
  names a file the target did not receive — S5's join, asserted over a real fixture emit.
- **AC4** — When the three `subject = repo` rows S5 names are examined in a fixture target, their
  `.test.sh` files ARE present, so the withholding did not over-reach.
- **AC5** — When the filter is made vacuous, the arm in `tools/govkit/selftest.py` reds, because the
  emitted leg count is not less than 52.
- **AC6** — When `bash tools/run-gates/run-gates.sh` runs without `GATE_SELFTESTS`, the set of legs it
  holds is EQUAL to today's set, compared name-for-name against a set captured before the change.
- **AC7** — When `govkit selfcheck` runs after the descriptors gain their `project-owned` rules, it is
  green. It carries no guard and runs on every bar, so this unit's first commit is where a broken
  descriptor would otherwise be discovered.

## 7. Gates

`bash tools/run-gates/run-gates.sh` · the new `no self-test reaches an adopter` leg ·
`govkit selfcheck`, which carries no guard and runs on every bar · `govkit acceptance matrix` and
`govkit refusal join`, which run when their `tools/govkit/` guard fires, as this unit's edits make it
· `GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` for `govkit selftest` and the
`run-gates canary` at the Definition of Done.

## 8. Open questions

- **F1 — the owner's own either/or.** RESOLVED (agent, 2026-09-06, delegated), revised at rev-2 and
  unchanged at rev-3: take the FIRST clause. Neither the held legs nor their files ship. The owner's
  own sentence gives the reason — "adopters do not need to modify this kit, so self-checks are not
  required there" — and rev-1's middle position created a suite that sources a library an adopter's
  tree cannot contain.
- **F2 — how is a file withheld?** RESOLVED (agent, 2026-09-06, delegated), CORRECTED at rev-3: with
  a `[[files]]` rule carrying `role = "project-owned"`. Rev-2 said no marker was needed and that an
  unclaimed file is not copied; that states the contract backwards, and the marker it argued away
  already exists and is already used in this tree.
- **F3 — do the three shipping `subject = repo` test files stay?** RESOLVED (agent, 2026-09-06,
  delegated): yes, enumerated in S5. They belong to checks an adopter runs, so withholding their
  files would break legs the emit deliberately keeps.

## 9. Revision log

- rev-1 · 2026-09-06 · initial draft.
- rev-2 · 2026-09-06 · folded spec-audit round 1: the filename predicate removed (B1), the
  shared-reader claim withdrawn (B6), the files stopped shipping (B3), §7's guard claim corrected
  (U1), AC5 changed from superset to equality.
- rev-3 · 2026-09-06 · folded spec-audit round 2, which found three blockers in rev-2's own fold text.
  B4: `manifest_subject`/`manifest_chunk` are locals of `selfcheck` and `_cmd_apply` never opens the
  manifest, so S1 now adds ONE shared helper both verbs call, and S3 makes the missing-twin refusal an
  apply-time property rather than one borrowed from another verb. B5: "drop the file claim" is not an
  operation `govkit` offers and F2 stated the contract backwards; S4 uses `role = "project-owned"`,
  the marker `tools/run-gates/kit.toml` already uses. B6: S5 joins the two halves and enumerates the
  three `subject = repo` rows whose files must keep shipping. §1's population is now ENUMERATED — 52
  descriptor rows, 27 held — where rev-2 carried a stale "thirty".

## 10. Reuse audit

The seam is `tools/govkit/govkit.py`'s apply path and the `[[files]]` role vocabulary the tree already
uses — `role = "project-owned"` in `tools/run-gates/kit.toml`, which withholds
`run-gates.gov.test.sh` today and is the exact precedent S4 follows. What rev-2 got wrong and the
round-2 audit corrected is that the manifest maps live in `selfcheck` and not in the apply path, so
this unit DOES add one reader, declared as a single shared helper rather than a second spelling.
`tools/codebase-map/reuse_lookup.py` returned `registry.toml` [govkit] and
`KITDIR`/`ROOTN`/`KITREL`/`LEGS_FILE` [run-gates] as the affordance seams. `TOOL-aScouredKit-27`
scopes the gap and its warning is why the descriptor-key route stays rejected;
`TOOL-dUnstalledConvoy-30` is why the filename route stays rejected.

Recall terms used: `govkit apply emit descriptor gate_leg files role project-owned adopter manifest
subject chunk hold withhold`
