# TOOL-dGroundRules-27 — every policy case that drives the deployer runs it from the snapshot, and a call over the source's own root refuses

**Status:** CLOSED · rev-4 · 2026-10-24 · node d · Tier-2 · base 3708a705 · streams tooling · order 9 · advances TOOL-dGroundRules-12

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-27-deviation-15.md](../build/2026-10-23-build-TOOL-dGroundRules-27-deviation-15.md) | deviation | — |
| [2026-10-23-build-TOOL-dGroundRules-27-ledger.md](../build/2026-10-23-build-TOOL-dGroundRules-27-ledger.md) | journal | — |
| [2026-10-24-build-TOOL-dGroundRules-27-deviation-77.md](../build/2026-10-24-build-TOOL-dGroundRules-27-deviation-77.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dGroundRules-27-build-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-27-build-brief.md) | journal | — |
| [2026-10-24-prompt-TOOL-dGroundRules-27-1-spec-writer.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-27-1-spec-writer.md) | journal | — |
| [2026-10-24-prompt-TOOL-dGroundRules-27-divergence-brief.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-27-divergence-brief.md) | research | — |
| [2026-10-25-prompt-TOOL-dGroundRules-21-close-arms-brief.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-21-close-arms-brief.md) | research | TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-29 TOOL-dGroundRules-31 |
| [2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-65 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-51 TOOL-dGroundRules-52 |
| [2026-10-23-review-TOOL-dGroundRules-26-32-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-26-32-spec-audit-round1.md) | spec-audit | TOOL-dGroundRules-26 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 |
| [2026-10-25-review-TOOL-dGroundRules-1-71-closing-diff-round1.md](../reviews/2026-10-25-review-TOOL-dGroundRules-1-71-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-52 TOOL-dGroundRules-55 TOOL-dGroundRules-56 TOOL-dGroundRules-60 TOOL-dGroundRules-61 TOOL-dGroundRules-62 TOOL-dGroundRules-63 TOOL-dGroundRules-64 TOOL-dGroundRules-65 TOOL-dGroundRules-66 TOOL-dGroundRules-67 TOOL-dGroundRules-68 TOOL-dGroundRules-69 TOOL-dGroundRules-70 TOOL-dGroundRules-71 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 22 to 25
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-22-25-spec-audit-round1.md`)
exited CONVERGED with finding **id 7 at HIGH**, which shares item **H1** with id 1
(`TOOL-dGroundRules-26`) and id 23 (`TOOL-dGroundRules-28`). This unit is id 7's promotion. Id 7
named the cases that inherited the defect: `TOOL-dGroundRules-25` S9 and S12 drove `govkit.py plan`
and `apply` from the source, so they read the source's HEAD.

That half is already repaired at HEAD. Units 25 and 26 put `legacy-homes-withheld-install`,
`census-default-adopter` and `adopter-fresh-target` on `build_source_snapshot`'s clone, through
`build_install_target` and `run_install_verb`. What is still open is the class: `run_install_verb`
runs whatever deployer path it is handed and compares no roots, so a case added later can pass the
source's own deployer and grade HEAD with nothing to say so.

This unit's change is `run_govkit` replacing `run_install_verb`: it takes the snapshot root and the
source root, refuses the two when they resolve equal, and owns the deployer path check and
derivation that `build_install_target` holds today. It repairs `TOOL-dGroundRules-25`, which sits at
order 8, so it builds at order 9.

## 2. Scope (IN)

- **S1** — The helper. `run_install_verb` in `tools/policy/check_policy.py` is renamed and widened
  to `run_govkit(snapshot_root, source_root, *argv)`, so the kit holds one function that runs the
  deployer for a case. It refuses, by raising `RuntimeError` before any process starts, a
  `snapshot_root` that resolves to `source_root`, the message naming that root and
  `build_source_snapshot`. It then derives `<snapshot_root>/<tool root>/govkit/govkit.py` with the tool
  root read from the kit's `--show-prefix` as `build_install_target` reads it today, raises
  `RuntimeError` naming the path it looked at when no file is there, and runs that file with `argv`,
  `GOVKIT_NO_REMOTE_PROBE=1` and the memory-tree kit's `GIT_ENV_LEAKS` stripped from the environment.
  It returns the exit status and the output with carriage returns stripped, as `run_install_verb`
  does. Observed by AC3.
- **S2** — `legacy-homes-withheld-install` (`TOOL-dGroundRules-25` S9). Its snapshot already holds:
  `build_install_target` takes it. What remains is that its `plan` and `apply` call `run_govkit` with
  the snapshot root and the source's toplevel, and `build_install_target` returns the target and the
  snapshot root and nothing else. Its existing `except` already records a `RuntimeError` as the
  case's `WRONG`. Observed by AC1.
- **S3** — `census-default-adopter` (`TOOL-dGroundRules-25` S12). Its snapshot already holds, through
  the same builder. What remains is that its `apply` calls `run_govkit` as S2's calls do. Observed by
  AC2.
- **S4** — The rule, scoped to deployer runs. `adopter-fresh-target` (`TOOL-dGroundRules-26` S2)
  calls `run_govkit` for its `apply`, and that call sits under the `except` that records a
  `RuntimeError` as the case's `WRONG`. After this unit no line of `check_policy.py` outside
  `run_govkit` runs the deployer as a process or derives its path for a run. The one exception is
  `budgets-ships-join`'s in-process `importlib` load in `run_ships_join`, which reads the source's
  working tree by design and is no run; `TOOL-dGroundRules-34` S7's `resolve_govkit` sanctions it, and
  this unit leaves it as it is. Prose outside those two functions that spells the deployer's file
  name, the module docstring, four case or builder docstrings and the refused-`apply` message, names
  it as the deployer, so the spelling AC4 greps for has no copy left to imitate. Observed by AC2 and
  AC4.
- **S5** — The refusal's case. `govkit-source-root-refused` in `CASES` calls `run_govkit` with the
  source's toplevel as both roots and `--help` as its argument. It passes when the call raises a
  `RuntimeError` naming that root and `build_source_snapshot`, and prints `WRONG` naming the exit and
  the output when the call returns. Observed by AC3, and it is the arm §7 declares.

## 3. Non-goals (OUT)

- The snapshot itself: `TOOL-dGroundRules-26`, id 1's promotion, CLOSED.
- `resolve_govkit` and the in-process load's route through it: `TOOL-dGroundRules-34` S7. Building it
  here is refused by this run's ruling; it is that unit's scope.
- Refusing every root no snapshot made, beyond the equal-root refusal: `TOOL-dGroundRules-34` S9.
- One target builder shared by the three cases, writing the `[answers]` each closure needs: finding
  12, an item of `TOOL-dGroundRules-32`.
- Any change to `govkit.py` or to `tools/govkit/matrix.py`, which applies from its own checkout's
  HEAD and is not a policy case.

### Edges

- **consumes-from** `TOOL-dGroundRules-26` — `build_source_snapshot` and the snapshot-installed fresh target, which this unit's helper requires of every case
- **consumes-from** `TOOL-dGroundRules-25` — the cases `legacy-homes-withheld-install` and `census-default-adopter`, which this unit moves onto `run_govkit`
- **hands-off** `TOOL-dGroundRules-32` — `run_govkit`, which that unit's shared target builder (finding 12) calls
- **hands-off** `TOOL-dGroundRules-34` — `run_govkit` and its refusal, which that unit widens to every root no snapshot made and routes through `resolve_govkit`, and `budgets-ships-join`'s in-process load, which S7 there sanctions (ids 3, 23, 4, 34 and 20 of the round-1 spec audit of units 26 to 32)

## 4. Design

### Evidence

The deployer lines were read at base `3708a705` on 2026-10-23 and hold unchanged at `7599845c2`.
The `check_policy.py` lines were read at `8f56d0875` on 2026-10-24; nothing under `tools/` moved
between `7599845c2` and `8f56d0875`.

- `_cmd_apply` installs the bytes of `git rev-parse HEAD` of the checkout `govkit.py` lives in
  (`tools/govkit/govkit.py:7533`, `:7882-7884`), and `blob_at` never reads the working tree
  (`:6706-6716`). `read_descriptors` reads each descriptor from the working tree (`:13238-13253`).
- The two cases already run from the snapshot. `build_install_target`
  (`tools/policy/check_policy.py:1029-1064`) clones the tree under test with `build_source_snapshot`
  (`:958-996`) and returns the clone's deployer path (`:1064`); `run_legacy_withheld_install` runs
  `plan` and `apply` over it (`:1234-1240`), `run_census_default_adopter` runs `apply` (`:1272-1273`)
  and `run_fresh_target` runs `apply` (`:1122-1126`). The builder's probes at `7599845c2` saw both
  cases print `0 wrong` from a snapshot.
- `run_install_verb` (`:1067-1072`) takes a deployer path and runs it with
  `GOVKIT_NO_REMOTE_PROBE=1`. It compares no roots, so handed the source's own deployer it installs
  the source's HEAD; and it passes `os.environ` through with `GIT_ENV_LEAKS` kept.
- The deployer path check and derivation sit in `build_install_target`: the `is_file` refusal at
  `:1038-1040` and the derivation at `:1064`.
- `run_fresh_target` catches `RuntimeError` around `build_install_target` alone (`:1121-1124`); its
  `apply` call at `:1126` sits outside that `except`. The other two cases catch around their whole
  body (`:1248`, `:1286`).
- `run_ships_join` loads the source's deployer in-process through `importlib` (`:3478-3490`), deriving
  its path at `:3479`. It runs no process.
- `govkit.py` is spelled at lines 42, 149, 961, 1034, 1038, 1039, 1064, 1083, 1097, 1128, 1227, 3479
  and 3489. Of those, 3479 and 3489 sit in `run_ships_join`; 1038, 1039 and 1064 are the check and
  derivation that move; the rest are prose.
- `govkit.py --help` writes its usage and exits 0 (`tools/govkit/govkit.py:14049-14051`), so S5's
  argument is harmless if the refusal fails.

### The helper

```text
run_govkit(snapshot_root, source_root, *argv):
    if resolve(snapshot_root) == resolve(source_root):
        raise RuntimeError("run_govkit: <root> is the tree under test; take build_source_snapshot first")
    govkit = <snapshot_root>/<parent of the kit's --show-prefix>/govkit/govkit.py
    if govkit is not a file:
        raise RuntimeError("no deployer to install with: looked at <govkit>")
    p = run([sys.executable, govkit, *argv], env = environ less GIT_ENV_LEAKS, GOVKIT_NO_REMOTE_PROBE=1)
    return p.returncode, (p.stdout + p.stderr) less "\r"
```

Each case passes `derive_source_top()` (`check_policy.py:2910`) as `source_root`, the same toplevel
`build_install_target` snapshots.

### Rollout

Order 9 holds `TOOL-dGroundRules-30` and `TOOL-dGroundRules-31` beside this unit, and
`TOOL-dGroundRules-31` also writes `tools/policy/check_policy.py`. The inline author builds this unit
first and `TOOL-dGroundRules-31` after it. Run concurrently, the pair is refused by `--dispatch`
condition 1 in `tools/unattended/unattended.sh`, the block under its `CONDITION 1` comment, whose
refusal reads "declares a path a sibling pass in the same group already declared".

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `run_govkit` | py.function | `tools/policy/check_policy.py` |
| `govkit-source-root-refused` | `CASES` entry | `tools/policy/check_policy.py` |

`lexicon.py --suggest run_govkit --as py.function` answered OK on 2026-10-23.

### Files touched (estimate)

- `tools/policy/check_policy.py`
- `tools/policy/README.md`
- `memory/map/generated/symbols.json`

The README's paragraph on the three install cases gains one sentence: their deployer runs go through
`run_govkit`, which refuses the source's own root, and `govkit-source-root-refused` observes it.

### Alternatives rejected

- **A second helper beside `run_install_verb`.** Two functions that run the deployer, one without the
  refusal, is the route the rule closes.
- **Each case takes its own snapshot inline.** Three copies of one rule, and a fourth case can forget
  it with nothing to say so.
- **A source grep for `govkit.py` alone.** A presence probe: it passes a call spelled through a
  variable and says nothing about which root ran. AC4 keeps it only beside AC1 to AC3, which observe
  the runs.

## 5. Production-readiness checklist

- security — N/A: gov-only cases under the temporary directory; nothing shipped changes.
- perf / scale — one snapshot per case that installs, as `TOOL-dGroundRules-26` prices it; a missing
  deployer is now found after the snapshot rather than before, one clone's cost on a broken tree.
- error / empty / loading states — a call over the source's own root, or a snapshot with no deployer,
  is a named `WRONG`, never a silent grade of HEAD.
- observability — the refusal names the root and the function to call first.
- risks — a case that runs the deployer through a variable-spelled path without `run_govkit`; AC4's
  grep cannot see it, and AC1 to AC3 observe only the cases that exist.
- testing — the three install cases and S5's case under `--fixture`, with AC1 to AC4.
- migration — none.
- user docs — N/A: gov-only cases; the kit README sentence is the only prose.

## 6. Acceptance criteria

Every command runs in the kit's directory of a scratch clone of the built tree. The criteria spell
the kit's files by bare name, `check_policy.py` and `policy.py` under the kit, as
`TOOL-dGroundRules-5` §6 does.

- **AC1** — When the clone's `run_govkit` is staged to raise `RuntimeError` with the message `run_govkit staged` before anything else, `python check_policy.py --fixture legacy-homes-withheld-install` prints `WRONG` carrying `run_govkit staged` for its target; with the staging undone, the same command prints `0 wrong`.
  Red when: the case's `plan` or `apply` reaches the deployer by a route other than `run_govkit`.
- **AC2** — With the same staging, `python check_policy.py --fixture census-default-adopter` and `python check_policy.py --fixture adopter-fresh-target` each print `WRONG` carrying `run_govkit staged`; with it undone, each prints `0 wrong`.
  Red when: the census case or the fresh-target case runs the deployer without `run_govkit`, or the fresh-target case lets the raise escape rather than record it.
- **AC3** — When a `python -c` probe under the kit calls `run_govkit` with the clone's own toplevel as both roots and `--help` as its argument, it raises `RuntimeError` naming that toplevel and `build_source_snapshot`, and returns no exit status.
  Red when: a case can drive the deployer over the tree under test's HEAD.
- **AC4** — When `grep -n govkit.py check_policy.py` runs under the kit, every printed line sits inside `run_govkit` or inside `run_ships_join`, and `grep -n run_install_verb check_policy.py` prints nothing.
  Red when: a case keeps a second route to the deployer that skips the refusal.

## 7. Gates

`codebase-map coverage + freshness` · `lexicon naming predicates` · `memory hygiene` · `recall floor` · `recall floor arms` · `policy fixtures`

The policy legs `TOOL-dGroundRules-1` declares run the cases; S5's case is named by the arm line,
because it does not exist at this spec's base.

New arm: tools/policy/check_policy.py --fixture govkit-source-root-refused · covers AC3 · `run_govkit` staged to accept equal roots, so the case's call over the source root runs the deployer where it must refuse, and the case prints WRONG · none

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
- rev-3 · 2026-10-24 · §7 · the policy fixtures leg added to the leg line, owed by its guard, which a §4 path trips; no design change.
- rev-4 · 2026-10-24 · §1 to §4, §6, §7, §10 · the builder's DIVERGENCE at `7599845c2`, ruled by the run. Disagreements: S4 and AC4 forbade any spelling of the deployer's file name outside `run_govkit`, which `budgets-ships-join`'s in-process load breaks; §1, §4 Evidence, S2 and S3 described a defect units 25 and 26 had already repaired, so AC1, AC2 and the arm were green at HEAD and could not tell this unit built; §10 said no helper runs the deployer for a fixture, but `run_install_verb` does; §4 Rollout cited condition 1 by a line that had moved. Rulings: S4 scopes the rule to deployer runs, names the in-process load as the one exception until `TOOL-dGroundRules-34` S7, and AC4 excludes `run_ships_join` by name, building `resolve_govkit` here refused; §1, §4 and S2/S3 say the snapshot already holds and the change is `run_govkit` renamed from `run_install_verb` with the equal-root refusal and the moved path check and derivation; §10 names that seam; AC1 and AC2 stage `run_govkit` to raise, the arm moves to S5's new refusal case so its break targets the refusal, and AC3 stays the probe; Rollout cites condition 1 by its comment and refusal text.

## 10. Reuse audit

The seam extended is `run_install_verb` (`tools/policy/check_policy.py:1067`), the one function
that runs the deployer for a case: it is renamed `run_govkit` and gains the root refusal, the path
check and the derivation, so no second helper is added. `build_source_snapshot`
(`TOOL-dGroundRules-26`), `build_install_target` and `derive_source_top` are reused unchanged in
role, the builder returning one value fewer. The three install cases keep their assertions and
change only the call that runs the deployer.

`python tools/codebase-map/reuse_lookup.py "run the deployer govkit for a policy fixture case from a snapshot root"`
on 2026-10-24 ranked `run`, `fixture`, `repo_root` and `run_git` and did not rank `run_install_verb`;
reading `check_policy.py` found it. The rev-1
probe at base `3708a705` ranked no such helper because units 24 to 26 had not yet added one.
`tools/govkit/matrix.py` runs the deployer through its own `run` from its own checkout, which is
not a policy case, so it is not reused. The recall probe returned this audit's H1 and
`DEPL-dRatifiedSeam-6`, the govkit selftest grading commit topology rather than the tree; both agree
with this design and with source.

Recall terms used: `python tools/memory-recall/query.py "how does a fixture grade uncommitted working
tree bytes when the deployer reads HEAD" --terms "govkit apply blob_at HEAD working tree uncommitted
snapshot scratch clone fixture source revision"`
