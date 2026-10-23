# TOOL-dGroundRules-27 — every policy case that drives the deployer runs it from the snapshot, and a call over the source's own root refuses

**Status:** OPEN · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 9

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-27-deviation-15.md](../build/2026-10-23-build-TOOL-dGroundRules-27-deviation-15.md) | deviation | — |
| [2026-10-23-review-TOOL-dGroundRules-26-32-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-26-32-spec-audit-round1.md) | spec-audit | TOOL-dGroundRules-26 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 22 to 25
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-22-25-spec-audit-round1.md`)
exited CONVERGED with finding **id 7 at HIGH**, which shares item **H1** with id 1
(`TOOL-dGroundRules-26`) and id 23 (`TOOL-dGroundRules-28`). This unit is id 7's promotion. Id 7
names the cases that inherit the defect: `TOOL-dGroundRules-25` S9 and S12 build their own targets
"as `TOOL-dGroundRules-24` S1 does" and drive `govkit.py plan` and `apply` from the source, so they
read the source's HEAD exactly as the fresh-target case did. It repairs `TOOL-dGroundRules-25`, which
sits at order 8, so it builds at order 9.

`TOOL-dGroundRules-26` makes the snapshot and installs the fresh target from it. This unit moves
every other deployer call in the policy kit's cases onto that snapshot, and closes the class: one
helper runs the deployer for a case, and it refuses a root that is the tree under test, so a case
added later cannot grade HEAD by accident.

## 2. Scope (IN)

- **S1** — The helper. `run_govkit(snapshot_root, source_root, *argv)` in
  `tools/policy/check_policy.py` runs `<snapshot_root>/<tool root>/govkit/govkit.py <argv>` with
  `GOVKIT_NO_REMOTE_PROBE=1` and returns its exit status and output. It refuses, as the case's
  `WRONG`, a `snapshot_root` that resolves to `source_root`, naming both and
  `build_source_snapshot`. Observed by AC3.
- **S2** — `legacy-homes-withheld-install` (`TOOL-dGroundRules-25` S9) takes a snapshot with
  `build_source_snapshot` and runs `plan` and `apply` through `run_govkit`. Observed by AC1.
- **S3** — `census-default-adopter` (`TOOL-dGroundRules-25` S12) runs `apply` through `run_govkit`
  over the same kind of snapshot. Observed by AC2.
- **S4** — `adopter-fresh-target` (`TOOL-dGroundRules-26` S2) runs its `apply` through `run_govkit`.
  After this unit no line of `check_policy.py` outside `run_govkit` spells the deployer's file name.
  Observed by AC4.

## 3. Non-goals (OUT)

- The snapshot itself: `TOOL-dGroundRules-26`, id 1's promotion.
- One target builder shared by the three cases, writing the `[answers]` each closure needs: finding
  12, an item of `TOOL-dGroundRules-32`.
- Any change to `govkit.py` or to `tools/govkit/matrix.py`, which applies from its own checkout's
  HEAD and is not a policy case.

### Edges

- **consumes-from** `TOOL-dGroundRules-26` — `build_source_snapshot` and the snapshot-installed fresh target, which this unit's helper requires of every case
- **consumes-from** `TOOL-dGroundRules-25` — the cases `legacy-homes-withheld-install` and `census-default-adopter`, which this unit moves onto the snapshot
- **hands-off** `TOOL-dGroundRules-32` — `run_govkit`, which that unit's shared target builder (finding 12) calls
- **hands-off** `TOOL-dGroundRules-34` — `run_govkit` and its refusal, which that unit widens to every root no snapshot made and routes through `resolve_govkit` (ids 3, 23, 4, 34 and 20 of the round-1 spec audit of units 26 to 32)

## 4. Design

### Evidence

Every line below was read at base `3708a705` on 2026-10-23.

- `_cmd_apply` installs the bytes of `git rev-parse HEAD` of the checkout `govkit.py` lives in
  (`tools/govkit/govkit.py:7533`, `:7882-7884`), and `blob_at` never reads the working tree
  (`:6706-6716`).
- `read_descriptors` reads each descriptor from the working tree (`tools/govkit/govkit.py:13238-13253`),
  so `plan` over the source mixes working-tree descriptors with HEAD's file bytes.
- `TOOL-dGroundRules-25` S9 runs `govkit.py plan` and `apply` over a target built "as
  `TOOL-dGroundRules-24` S1 does", and S12 runs `apply` the same way; neither names a source revision.

### The helper

```text
run_govkit(snapshot_root, source_root, *argv):
    if resolve(snapshot_root) == resolve(source_root):
        WRONG "run_govkit: <root> is the tree under test; take build_source_snapshot first"
    govkit = <snapshot_root>/<tool root derived as TOOL-dGroundRules-24 S4 derives it>/govkit/govkit.py
    return run([python, govkit, *argv], env = environ less GIT_ENV_LEAKS, GOVKIT_NO_REMOTE_PROBE=1)
```

### Rollout

Order 9 holds `TOOL-dGroundRules-30` and `TOOL-dGroundRules-31` beside this unit, and
`TOOL-dGroundRules-31` also writes `tools/policy/check_policy.py`. The inline author builds this unit
first and `TOOL-dGroundRules-31` after it; `--dispatch` condition 1 refuses the pair run concurrently
(`tools/unattended/unattended.sh:13845-13880`).

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `run_govkit` | py.function | `tools/policy/check_policy.py` |

`lexicon.py --suggest run_govkit --as py.function` answered OK on 2026-10-23.

### Files touched (estimate)

- `tools/policy/check_policy.py`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- **Each case takes its own snapshot inline.** Three copies of one rule, and a fourth case can
  forget it with nothing to say so.
- **A source grep for `govkit.py` inside `CASES`.** A presence probe: it passes a call spelled
  through a variable and says nothing about which root ran.

## 5. Production-readiness checklist

- security — N/A: gov-only cases under the temporary directory; nothing shipped changes.
- perf / scale — one snapshot per case that installs, as `TOOL-dGroundRules-26` prices it.
- error / empty / loading states — a call over the source's own root is a named `WRONG`, never a
  silent grade of HEAD.
- observability — the refusal names both roots and the function to call first.
- risks — a future case that shells out to the deployer without the helper; S4 leaves no second
  spelling in the file for it to copy.
- testing — the three cases under `--fixture`, with AC1 to AC4.
- migration — none.
- user docs — N/A: gov-only cases.

## 6. Acceptance criteria

Every command runs from the repository root. The criteria spell the kit's files by bare name,
`check_policy.py` and `policy.py` under the kit, as `TOOL-dGroundRules-5` §6 does.

- **AC1** — When a scratch clone of the built tree commits the deletion of its kit's `policy.py`,
  restores the file uncommitted, and runs `python check_policy.py --fixture legacy-homes-withheld-install`,
  the case prints no `does not resolve at` and no `WRONG`.
  Red when: the case's `apply` installs the clone's HEAD.
- **AC2** — When the same clone runs `python check_policy.py --fixture census-default-adopter`, the
  case prints no `does not resolve at` and no `WRONG`.
  Red when: the census case grades an install of HEAD rather than of the tree under test.
- **AC3** — When `run_govkit` is called from a `python -c` probe with the source repository's own
  root as both arguments, it reports `WRONG` naming that root and `build_source_snapshot`, and runs no
  deployer.
  Red when: a case can drive the deployer over the tree under test's HEAD.
- **AC4** — When `grep -n "govkit.py" check_policy.py` runs under the kit, every printed line sits
  inside `run_govkit` or names the snapshot's tool root there.
  Red when: a case keeps a second route to the deployer that skips the refusal.

## 7. Gates

`codebase-map coverage + freshness` · `lexicon naming predicates` · `memory hygiene` · `recall floor` · `recall floor arms`

The policy legs `TOOL-dGroundRules-1` declares run the cases; they are named by the arm line, because
neither exists at this spec's base.

New arm: tools/policy/check_policy.py (`--fixture legacy-homes-withheld-install`, `--fixture census-default-adopter`) · covers AC1 AC2 · a kit file deleted at the clone's HEAD and restored uncommitted · none

## 8. Open questions

- **F1 — How is every deployer call in the policy cases kept off the source's HEAD?** (a) One helper
  that takes the snapshot root and refuses the source's own root. (b) Each case snapshots inline.
  (c) A grep over `check_policy.py` for the deployer's file name. (b) meets AC1 and AC2 and fails AC3,
  having no refusal (veto 1). (c) is a presence probe that a call spelled through a variable passes,
  and it fails AC3 (veto 1). (a) meets every criterion. Recommendation (a). Rung 3.
  RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 7 (HIGH, item H1) of the round-1 spec
  audit of units 22 to 25, for the cases `TOOL-dGroundRules-25` S9 and S12 that inherit the defect,
  with govkit's `apply` and `read_descriptors` read at base `3708a705`.
- rev-2 · 2026-10-23 · §3 · the **hands-off** edge to TOOL-dGroundRules-34 added, each the reciprocal of that unit's **consumes-from** line: the promotions of the round-1 spec audit of units 26 to 32 that build on this unit. No scope, design or acceptance moved here; the repair is the promoted unit's.

## 10. Reuse audit

The seams extended are `TOOL-dGroundRules-26`'s `build_source_snapshot` and the two cases
`TOOL-dGroundRules-25` adds, which keep their assertions and change only the root they run the
deployer from. `python tools/codebase-map/reuse_lookup.py "commit the working tree under test into a scratch clone so a tool reading HEAD sees uncommitted edits"`
ranked `read`, `read_text`, `tree`, `scratch` and `add_scratch_worktree`, and no helper that runs
`govkit.py` for a fixture: `tools/govkit/matrix.py` runs it through its own `run` from its own
checkout, which is the defect this unit closes, so it is not reused here. The recall probe returned
this audit's H1 and `DEPL-dRatifiedSeam-6`, the govkit selftest grading commit topology rather than
the tree; both agree with this design and with source.

Recall terms used: `python tools/memory-recall/query.py "how does a fixture grade uncommitted working
tree bytes when the deployer reads HEAD" --terms "govkit apply blob_at HEAD working tree uncommitted
snapshot scratch clone fixture source revision"`
