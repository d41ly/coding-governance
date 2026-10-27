# TOOL-dFurnishedOrders-44 — the step's receipt homes held to the receipt `apply` writes: one govkit selftest arm applies every shipped kit to a scratch target with a per-kit override and compares both ways

**Status:** OPEN · rev-1 · 2026-10-27 · node d · Tier-2 · base 47d3a464 · streams tooling · order 8 · advances TOOL-dFurnishedOrders-21

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-3 promotions
(`memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-38-spec-audit-round1.md`)
confirmed finding **id 14 at HIGH**, report item **H1**. Id 1 shares that item and takes
`TOOL-dFurnishedOrders-43`, which corrects the derivation.

Id 14 is the reuse half of the item. `TOOL-dFurnishedOrders-40` S1 wrote a second formula for a
place `apply` already decides, and its criterion planted the receipt rows where that formula looks,
under the declared home, so the criterion and the formula agreed with each other and with nothing
`apply` does. The skeptic's probe showed the formula names no directory for any entry: review-harness
gives `tools/tools/workflows` against `apply`'s `tools/review-harness`, agent-cap `tools/tools/hooks`,
memory-recall `tools/tools/memory-recall`. A fixture an author writes by hand repeats the author's
model of `apply`; only a receipt `apply` wrote can contradict it.

This unit adds that contradiction as a standing gate: the receipt of a real `apply` over every shipped
kit is the oracle the step's homes are compared with. It repairs `TOOL-dFurnishedOrders-40` and builds
one step after it (order 8), after unit 43 by the dispatch's id sort.

## 2. Scope (IN)

- **S1** — The parity arm. `tools/govkit/selftest.py` gains `check_receipt_home_parity(tmp)`. It
  builds a scratch target with `make_target` (`tools/govkit/selftest.py:679`) whose `deploy.toml`
  sets `prefix = "scripts"`, `[kit.memory-recall]` `kit = "scripts/recall"`, and the answers
  `DEPLOY_FULL` (`:703`) carries; runs `apply --target <t> --all` through the suite's `run`
  (`:220`); and reads the receipt `apply` wrote. A refused `apply` fails the arm naming the refusal,
  never skips it. Observed by AC1.
- **S2** — The compare, both ways. For every receipt row of role `engine` whose `kit` has a gov
  descriptor not of kind `flat`, whose `source`, resolved by `resolve_prefix_token` against gov's tool
  root, lies under that kit's gov home `H`, and whose `path` ends in `/<rel>`, `rel` being the source
  after `H/`: the directory `path` minus `/<rel>` is in `derive_receipt_homes`'s answer for that kit
  (`TOOL-dFurnishedOrders-43` S1). And every home that answer holds is the directory of at least one
  such row. Each disagreement prints `home parity: <kit> <home> <side>` and fails the arm. Observed by
  AC1.
- **S3** — The arm cannot pass on nothing. It fails as `DEAD PROBE` when it compares no row, when no
  compared kit's target home differs from `<prefix>/<last segment of its gov home>`, or when
  memory-recall's answer is not exactly `scripts/recall`; it prints the counts of kits and rows it
  compared. Observed by AC2.

## 3. Non-goals (OUT)

- The derivation itself: `TOOL-dFurnishedOrders-43`, for id 1.
- Homes an adopter's `project-owned` copy sits in with no engine row beside it: S2 reads engine rows
  only, so `apply`'s receipt cannot witness them, and §4 "What it does not check" says which kits
  that leaves.
- The `govkit selftest` guard rows for the descriptors this arm reads: the minors batch
  `TOOL-dFurnishedOrders-46`, for id 22.
- The report's left-shift checklist entry and fixture rule: this arm is the gate they describe, for
  this step; no clause of this build names a wider one.

### Edges

- **consumes-from** `TOOL-dFurnishedOrders-43` — `derive_receipt_homes`, whose answer S2 compares with the receipt `apply` writes (ids 1, 14)
- **hands-off** `TOOL-dFurnishedOrders-46` — the registry descriptors S1's `apply` reads outside the `govkit selftest` guard, which unit 46 S8 adds to it (id 22)

## 4. Design

### The arm

```
t       := make_target(tmp/"home-parity", deploy with prefix "scripts", kit.memory-recall.kit, answers)
p       := run("apply", "--target", t, "--all");  p.returncode != 0 -> FAIL naming p's refusal
receipt := json of t/.governance/install.json
want    := derive_receipt_homes(gov_root, t, receipt, deploy)           # unit 43 S1
seen    := {kit: {path minus "/" + rel}} over engine rows of non-flat kits, rel = source after H/
for kit: seen[kit] - want[kit] -> "home parity: <kit> <home> receipt-only"
         want[kit] - seen[kit] -> "home parity: <kit> <home> derived-only"
rows compared == 0, no kit whose home moved off "<prefix>/<last segment of H>",
memory-recall != ["scripts/recall"]                                   -> DEAD PROBE
print "home parity: <k> kit(s), <r> row(s) compared"
```

### Why `apply`'s receipt and not `plan`'s rows

`plan` and `apply` share `resolve_rule_pool` and `resolve_dests`, so `plan` would make the same
claim about the same seam. The receipt is what `apply` wrote after landing each file, so it is the
nearest thing to the target's own tree the suite can read without a second implementation.

### What it does not check

- A kit whose only files in a directory are `project-owned`: agent-cap's `{kit}` directory, where its
  three `project-owned` rules would land (`TOOL-dFurnishedOrders-43` §4). No engine row reaches it, so
  S2's forward half cannot see it, and unit 43 S2 answers it only when the directory exists, which it
  does not in this fixture.
- Conditional entries `--all` does not select: none is graded, and the arm prints the count it did
  grade.
- An edit to a sibling kit's descriptor alone, under a scoped bar, until unit 46 S8 lands the guard
  rows; the push boundary's full bar runs the leg regardless.

### Inventory

Minted: the arm `check_receipt_home_parity` and its printed tokens `home parity:` and the
`receipt-only` and `derived-only` sides. `check` is a VERBS member of `.lexicon.conf`.

### Migration

None: a selftest arm stores nothing.

### Rollout

Live at landing, at order 8, beside unit 43.

### Files touched (estimate)

- `tools/govkit/selftest.py`

### Alternatives rejected

- **A hand-planted receipt per kit shape.** It is unit 40 AC1's shape: the author's model of `apply`
  on both sides of the compare.
- **Compare against `target_context(...)["kit"]`.** It is a third formula, and §4 of unit 43 measured
  it wrong for agent-cap and playbook-render.
- **Grade only the kits of unit 43's fixtures.** It certifies the instances already known; `--all`
  grades the class and every kit added later.

## 5. Production-readiness checklist

- security — the arm writes only its scratch target under the suite's temp root.
- perf / scale — one `apply --all` into one scratch repository per suite run.
- error / empty / loading states — a refused `apply` and an empty compare each fail by name (S1, S3).
- observability — each disagreement prints its kit, home and side; the counts line prints always.
- risks — `--all` couples the arm to every kit's answers; a new answer a kit asks for reds the arm
  until the fixture carries it, by S1's rule.
- testing — AC1 and AC2 by the pass's probe; the arm of §7 at the close.
- migration — none.
- user docs — none: a selftest arm.

## 6. Acceptance criteria

- **AC1** — When the pass's probe builds S1's scratch target, runs `python tools/govkit/govkit.py
  apply --target <t> --all`, and compares the receipt with `derive_receipt_homes` as S2 states, it
  prints no `home parity: <kit>` disagreement line and a counts line naming at least one kit; with
  unit 40's `{prefix}/<home>` formula staged into the step in place of unit 43's walk, it prints a
  disagreement line naming `review-harness` and one naming `memory-recall`.
  Red when: a home derived beside `apply`'s seam agrees with a hand-planted fixture and nothing reads
  the receipt.
  fixture: a scratch target repository under `%TEMP%`, built by the pass.
  cost: one full `apply` of every non-conditional entry, tens of seconds.
- **AC2** — When the same probe runs over a receipt from which every row of a kit whose home moved is
  deleted, and again with the `kit.memory-recall.kit` line taken out of the `deploy.toml`, it prints
  `DEAD PROBE` each time.
  Red when: the arm passes on a population that cannot tell `apply`'s layout from gov's.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `policy fixtures` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC2 · `apply --all` into a scratch target at prefix `scripts` with a per-kit `kit` override, compared both ways with the step's homes, staged by restoring unit 40's formula · none

## 8. Open questions

- **F1 — What is the oracle for a receipt kit's home?** Options: (a) the receipt a real `apply --all`
  writes; (b) `plan`'s printed rows; (c) hand-planted receipts. (b) shares the seam it would judge;
  (c) repeats the author's model. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3, the
  skeptic-judged left-shift of id 14. widens: none · relaxes: none
- **F2 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent,
  2026-10-27, delegated): `**Derived:**` naming `PLAY-dClosedLoop-2`, rung 3, the precedent
  `TOOL-dBoundRoles-39` §8 F1 records. widens: none · relaxes: none
- **F3 — The units this one reads are unbuilt.** `TOOL-dFurnishedOrders-40` and `-43` are specced and
  unbuilt at `47d3a464`. RESOLVED (agent, 2026-10-27, delegated): the build run re-grounds on each at
  the pass and stops this unit if `derive_receipt_homes` is still absent then, rung 1, the brief's
  rule for unbuilt parents. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of the round-3 promotions, id 14
  (HIGH, item H1, shared with id 1).

## 10. Reuse audit

The seams extended: the suite's own `make_target` (`tools/govkit/selftest.py:679`), `run` (`:220`),
which threads the receipt pin through every `apply`, and `DEPLOY_FULL` (`:703`); `govkit.py apply
--all` (`tools/govkit/govkit.py:13728`); `resolve_prefix_token` (`:180-191`). `python
tools/codebase-map/reuse_lookup.py "compare a derived path set against the receipt apply wrote"`
ranked `resolve_compare_base`, `build_spec_path_re` and `derive_baseline_additions`, none a
receipt compare, so no wider seam fits. The recall probe returned TOOL-dGroundRules-29 and
TOOL-aRepatriatedFork-24's ledger, each an arm grading `apply` through a scratch target, neither
disagreeing with source.

Recall terms used: `python tools/memory-recall/query.py "which arm holds a derived install path to
the receipt apply actually wrote" --terms "parity arm receipt apply landing derived home live
re-derivation selftest scratch target kit override"`
