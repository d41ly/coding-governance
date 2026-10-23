# TOOL-dGroundRules-24 — the fresh target installed by the deployer, so the case grades an install govkit makes

**Status:** OPEN · rev-3 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 3

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-24-deviation-12.md](../build/2026-10-23-build-TOOL-dGroundRules-24-deviation-12.md) | deviation | — |
| [2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-13 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-51 TOOL-dGroundRules-52 |
| [2026-10-23-review-TOOL-dGroundRules-22-25-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-22-25-spec-audit-round1.md) | spec-audit | TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-25 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 13 to 21
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-13-21-spec-audit-round1.md`)
exited CONVERGED with finding **id 17 at HIGH**, item **H2**, which id 36 shares at a binding
MEDIUM grade (`TOOL-dGroundRules-25`, its own item). This unit is id 17's promotion. It repairs
`TOOL-dGroundRules-16`, which sits at order 2, so it builds at order 3.

`TOOL-dGroundRules-16`'s `adopter-fresh-target` copies the policy kit's directory whole, and each
kit its `requires` names, into a fresh target. A whole-directory copy carries files the deployer
withholds, `tools/policy/legacy-homes.txt` among them once `TOOL-dGroundRules-17` S1 claims it as
`project-owned`, so the case grades an install no deployer makes and stays red with every unit
built. Its §3 rejected the deployer because it "never travels", but the case runs only in the
`policy fixtures` leg, which is gov's alone, beside the deployer. This unit builds the target with
`govkit.py apply`, asserts the target holds exactly what the receipt records, and runs the kit's
own adopter there.

## 2. Scope (IN)

- **S1** — The install. `adopter-fresh-target` in `CASES` of `tools/policy/check_policy.py` builds
  its target as `tools/govkit/selftest.py:679-700` builds one: `git init`, a pinned
  `core.autocrlf=false`, a one-line `README.md` and a `.governance/deploy.toml` naming `gov_source`,
  `prefix` and `kits`, committed once. It then runs
  `python <source tool root>/govkit/govkit.py apply --target <t> --kits <ids>` with
  `GOVKIT_NO_REMOTE_PROBE=1`, `<ids>` being `policy` and every id the closure of its `kit.toml`
  `requires` names, passed as registry ids. A non-zero `apply` fails the case with its output.
  Observed by AC1.
- **S2** — The install asserted. Every file under the target's tool root is a `path` of a row of the
  target's `.governance/install.json`, and every engine or seed row's `path` exists; a stray or a
  missing file fails the case naming it. Observed by AC1, AC2.
- **S3** — The adopter run. The case locates the installed `adopt-policy.sh` through the receipt row
  of kit `policy` whose `path` ends in that name, and runs `TOOL-dGroundRules-16` S1's sequence
  there: `--scaffold`, `--check` with the install staged and uncommitted, a commit, and `--check`
  again, each read per arm as `TOOL-dGroundRules-16` §4 step 5 reads it. Observed by AC1.
- **S4** — Every path derived. `govkit.py` is located from the kit's own resolved tool root, and the
  descriptor's `prefix` is that tool root's name, never a literal kit segment. A source tree with no
  `govkit.py` fails the case naming where it looked, never a skip. Observed by AC3.

## 3. Non-goals (OUT)

- The legacy-home announce in the installed target and the absence of `legacy-homes.txt` there:
  finding id 36's item in `TOOL-dGroundRules-25`. That list and its withholding are built at orders
  4 and 6, after this unit.
- Re-observing a target whose HEAD does not resolve. `apply` lands into a committed target, as every
  `govkit` fixture does; `TOOL-dGroundRules-21`'s `mirror-absent-adopter` runs over a target with no
  commit.
- `govkit.py check --target` as a second verdict. The case reads `--check` per arm, which `check`
  would reduce to one exit status.
- Any change to `govkit.py` or to the policy kit's descriptor.

### Edges

- **consumes-from** `TOOL-dGroundRules-16` — `adopter-fresh-target`, its two `--check` runs and its per-arm reading, which this unit re-bases on the deployer
- **hands-off** `TOOL-dGroundRules-25` — the installed target, which that unit's items for findings 36, 15 and 23 assert against
- **hands-off** `TOOL-dGroundRules-26` — `adopter-fresh-target`'s `apply` from the source tree, which that unit points at a commit of the working tree made in a scratch clone (finding 1)
- **hands-off** `TOOL-dGroundRules-32` — the fresh target's set-up, receipt compare and guard lines, which that unit moves into one builder with `[answers]`, a local identity and `govkit.py check` (findings 8, 12, 16, 21, 29)
- **hands-off** `TOOL-dGroundRules-34` — S4's tool-root derivation and its locate refusal, which that unit moves into `resolve_govkit` (ids 3 and 23 of the round-1 spec audit of units 26 to 32)

## 4. Design

### Evidence

Every line below was read at base `3708a705` on 2026-10-23.

- `TOOL-dGroundRules-16` §4 "The case" step 2 copies `Path(__file__).resolve().parent` and each kit
  `requires` names; its §3 third bullet rejects the deployer because it "never travels".
- `tools/govkit/selftest.py:679-700` (`make_target`) builds a fixture target: `git init`, pinned
  `core.autocrlf`, a `README.md` and `.governance/deploy.toml`, committed as `base`.
- `load_deploy` refuses a target with no `.governance/deploy.toml`, "Refusing to guess"
  (`tools/govkit/govkit.py:1540-1548`).
- `apply` refuses a selection whose `requires` is neither selected nor claimed by the receipt, and
  never widens the selection (`tools/govkit/govkit.py:7550-7565`, `derive_unsatisfied_requires` at
  `:950-975`).
- `apply` stages every path it lands (`tools/govkit/selftest.py:586-592`), and its receipt records
  each row's `path`, `role` and `kit` (`tools/govkit/govkit.py:7893-7895`).
- `GOVKIT_NO_REMOTE_PROBE` turns off the deployer's remote probe (`tools/govkit/govkit.py:637-638`),
  as the selftest sets it (`tools/govkit/selftest.py:1242`).

### The case after this unit

1. `t` under the system temp directory with the fixture mode's short prefix; `git init`, the
   descriptor, one commit.
2. `apply --target t --kits <policy and its requires closure>`; non-zero exit fails the case.
3. The receipt read; the tool root's files compared with its `path` column.
4. `adopt-policy.sh --scaffold --target t`, then `--check --target t`: exit 0 expected.
5. `git -C t add -A`, `git -C t commit`, then `--check --target t`: exit 0 expected.
6. Each `--check` output read per arm, as `TOOL-dGroundRules-16` §4 step 5 states.

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `adopter-fresh-target` | `CASES` entry, re-based | `tools/policy/check_policy.py` |

No function is minted.

### Files touched (estimate)

- `tools/policy/check_policy.py`
- `tools/gate-legs.json`

The `policy fixtures` row gains `{prefix}/govkit/govkit.py` and `{prefix}/govkit/registry.toml`, the
two files whose edit moves this case's verdict, each one the row does not already carry.

### Alternatives rejected

- **Copy only what `govkit.py plan` lists as write rows.** A second reading of the deployer's output
  that `apply` performs itself, and it still skips `apply`'s own refusals.
- **Keep the directory copy and exclude `legacy-homes.txt` by name.** It certifies an install shape
  no deployer makes, one special case at a time.

## 5. Production-readiness checklist

- security — N/A: a gov-only fixture under the temp directory; nothing shipped changes.
- perf / scale — one `apply` of two or three kits per run, a few seconds more than the copy.
- error / empty / loading states — an `apply` refusal, a stray file and a missing `govkit.py` each
  fail the case naming the cause, never a pass.
- observability — the case prints `apply`'s refusal or the stray path, then the arm that went red.
- risks — the deployer's install shape moves; the case then follows it, which is the point.
- testing — the case under `--fixture`, with AC1 to AC3.
- migration — none.
- user docs — N/A: a gov-only case.

## 6. Acceptance criteria

Every command runs from the repository root. The criteria spell the kit's files by bare name,
`check_policy.py` and `kit.toml` under the kit, as `TOOL-dGroundRules-5` §6 does.

- **AC1** — When `python check_policy.py --fixture adopter-fresh-target` runs on the built tree, it
  reports `apply` exiting 0 into its target and no stray or missing receipt path, then reads both
  `--check` runs per arm.
  Red when: the target is assembled by a copy, or `apply` refused and the case went on.
  permission: every arm green only once `TOOL-dGroundRules-17`, `TOOL-dGroundRules-21` and
  `TOOL-dGroundRules-25` are built; this unit's pass observes the install half, and the close
  observes the arms.
- **AC2** — When the case plants one extra file under the target's tool root after `apply` and
  before the receipt compare, it prints `WRONG` naming that file as no receipt row's path.
  Red when: the case grades files the deployer never installed.
- **AC3** — When `govkit.py` is absent from a scratch copy of the source tree and the same case
  runs there, it prints `WRONG` naming where it looked for `govkit.py`.
  Red when: a missing deployer reads as a skip or a pass.

## 7. Gates

`run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `memory hygiene` · `recall floor` · `recall floor arms`

The policy legs `TOOL-dGroundRules-1` declares run the case; they are named by the arm line, because
neither exists at this spec's base.

New arm: tools/policy/check_policy.py (`--fixture adopter-fresh-target`) · covers AC2 AC3 · an extra file planted under the installed tool root, then `govkit.py` absent from a scratch copy of the source · none

## 8. Open questions

- **F1 — How is the fresh target installed?** (a) `govkit.py apply` with `policy` and its requires
  closure, the receipt then compared with the tool root. (b) A copy of what `govkit.py plan` lists as
  write rows. (c) The directory copy with a list of exclusions. (c) installs what no deployer
  installs, which keeps `TOOL-dGroundRules-16` AC1 red on a correct build (veto 1). (b) meets the
  criteria and re-reads the deployer's plan without its refusals. (a) meets every criterion and adds
  `apply`'s refusals to what the case observes. Recommendation (a). Rung 3.
  RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 17 (HIGH, item H2) of the round-1 spec
  audit of units 13 to 21, from the review's sound fix, corrected for `apply`'s refusal of an
  unselected `requires`, with govkit and its selftest read at base `3708a705`.
- rev-2 · 2026-10-23 · §3 · the **hands-off** edges to TOOL-dGroundRules-26, TOOL-dGroundRules-32 added, each the reciprocal of that unit's **consumes-from** line: the promotions of the round-1 spec audit of units 22 to 25 that build on this unit. No scope, design or acceptance moved here; the repair is the promoted unit's.
- rev-3 · 2026-10-23 · §3 · the **hands-off** edge to TOOL-dGroundRules-34 added, each the reciprocal of that unit's **consumes-from** line: the promotions of the round-1 spec audit of units 26 to 32 that build on this unit. No scope, design or acceptance moved here; the repair is the promoted unit's.

## 10. Reuse audit

The seams extended are `TOOL-dGroundRules-16`'s `adopter-fresh-target`, which keeps its per-arm
reading, and govkit's own `apply` with the fixture shape `make_target`
(`tools/govkit/selftest.py:679-700`) already uses. `python tools/codebase-map/reuse_lookup.py
"install a kit into a scratch target with the deployer and read its receipt"` ranked `read`,
`read_text`, `scratch`, `kit_rel` and `resolve_kit_dir`; none installs a target, and the deployer
was found by reading `tools/govkit/govkit.py:7503-7565`. The probe and source disagree in one place
the review did not see: the sound fix said `apply --kits policy` "takes `requires` with it", and
source refuses that selection instead, so the case passes the closure. The recall probe returned
`DEPL-aLevelledCopy-2` and `TOOL-dRetiredFork-27`, asks about what `govkit apply` leaves in a fresh
target, a new engine row's file mode and a duplicate manifest row; neither bears on what this case
asserts, and neither disagrees with source.

Recall terms used: `python tools/memory-recall/query.py "how does a fixture install a kit into a
scratch target with govkit apply" --terms "govkit apply scratch target deploy.toml receipt
install.json fixture requires project-owned withheld"`
