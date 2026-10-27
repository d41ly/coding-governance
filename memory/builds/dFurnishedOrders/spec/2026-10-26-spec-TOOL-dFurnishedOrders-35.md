# TOOL-dFurnishedOrders-35 — the call-site scan's kit files defined on every target kind: gov's own kit source, a receipt, or the directories a `kit.toml` homes, so gov's own update walk passes

**Status:** DEFERRED · rev-2 · 2026-10-27 · node d · Tier-2 · base 8c395e3c · streams tooling · order 6 · advances TOOL-dFurnishedOrders-21

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-review-TOOL-dFurnishedOrders-31-spec-audit-round1.md](../reviews/2026-10-27-review-TOOL-dFurnishedOrders-31-spec-audit-round1.md) | spec-audit | TOOL-dFurnishedOrders-36 TOOL-dFurnishedOrders-31 TOOL-dFurnishedOrders-32 TOOL-dFurnishedOrders-33 TOOL-dFurnishedOrders-34 TOOL-dFurnishedOrders-37 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-1 promotions
(`memory/builds/dFurnishedOrders/reviews/2026-10-26-review-TOOL-dFurnishedOrders-22-spec-audit-round1.md`)
confirmed finding **id 10 at HIGH**, report item **H4**. Id 25 shares that item and takes
`TOOL-dFurnishedOrders-36`.

`TOOL-dFurnishedOrders-25` S1 subtracts "installed kit files as unit 4 already excludes them", and
`TOOL-dFurnishedOrders-4` §4 gives that phrase no rule for a target without an install receipt. gov
has none: `.governance/` holds `deploy.toml`, `policy.json` and `policy.toml` at `8c395e3c`. So on
gov the subtraction is empty, and unit 25 §4 measures the population only "outside tools/" without a
rule that drops `tools/`. A probe of unit 25's rules over this tree, with that subtraction empty,
named `tools/workflows/unattended-build.js`, its template and its suite for `checklist`, the suite
for `prebuild`, and `tools/govkit/selftest.py` among six files spelling the per-pass command (measured
at `8c395e3c`; PINNED). `witness . checklist` and `up` would still exit 1 on gov, while unit 25 AC5,
which rules out only hits under `memory/` or in `*.md`, passes.

This unit defines the kit files for every target kind and observes the walk on this repository. It
repairs `TOOL-dFurnishedOrders-25` and builds one step after it (order 6).

## 2. Scope (IN)

- **S1** — Gov's kit source. In `derive_call_sites` (`tools/govkit/steps/retired_dispatch_args.py`,
  `TOOL-dFurnishedOrders-25` S1), a target holding gov's kit source subtracts every tracked path under
  its tool root, receipt or not: the scan subtracts them. The test is `derive_tool_root(target)` (`tools/govkit/govkit.py:154-175`),
  which answers for gov's own checkout and for a tree holding `<govkit>/registry.toml`, and raises
  `Refusal` for any other tree. The step loads `govkit.py` from its own tool root by file path under the
  private module name `gov_govkit`, as `tools/govkit/govkit.py:3145` loads `check-arms.py`, never from
  the target. Observed by AC2 and AC3.
- **S2** — A target with no receipt. A target that is not gov's kit source and holds no
  `.governance/install.json` subtracts every tracked path under a directory holding a `kit.toml`: a kit
  dir a copy-install placed with `cp -r` (`WIRE-INTO-PROJECT.md`). A target with a receipt keeps unit
  4's receipt rule. Observed by AC1.
- **S3** — The scan line names the rule. Unit 25 S5's line gains `, <j> kit file(s) by <rule>`, the
  rule one of `kit source <tool root>/`, `receipt` or `kit.toml homes`, so a run that subtracted
  nothing says which rule found nothing. Observed by AC1 and AC2.
- **S4** — Gov's own walk observed. `witness` and `up` of both `checklist` and `prebuild` exit 0 on
  this repository, which replaces unit 25 AC5; unit 25's ledger answers AC5 in the AMENDED form,
  naming this unit's AC2. Observed by AC2.

## 3. Non-goals (OUT)

- The kits' own suites on a receipt-holding target: `TOOL-dFurnishedOrders-36`, for id 25.
- The memory-root and markdown subtractions, the key and command hits and `down`:
  `TOOL-dFurnishedOrders-25` S1 to S5, unchanged.
- How `MEMORY_ROOT` is read and refused: the minors batch `TOOL-dFurnishedOrders-37`, for ids 12, 36,
  18 and 19.
- A call site in gov's own tool root: gov's kits are rendered from it by the walk, so nothing in it is
  an adopter's call site (§4).

### Edges

- **consumes-from** `TOOL-dFurnishedOrders-25` — `derive_call_sites`, its population and its scan line, which S1 to S3 give a kit-file rule for every target kind, and AC5, which S4 replaces (id 10)
- **hands-off** `TOOL-dFurnishedOrders-36` — the kit homes S2 reads from `kit.toml` directories, which unit 36's suite subtraction reads beside a receipt's rows (ids 10 and 25)
- **hands-off** `TOOL-dFurnishedOrders-37` — the step's by-path load of `govkit.py`, through which unit 37 S8 and S34 read the conf (ids 36, 19)
- **hands-off** `TOOL-dFurnishedOrders-40` — the step's by-path `gov_govkit` load, through which unit 40 S1 reads gov's descriptors (id 28 of the third audit)
- **hands-off** `TOOL-dFurnishedOrders-41` — S1's kit-source test, S2's `kit.toml` homes and AC2, which unit 41 S1, S2 and S4 to S6 settle (ids 9, 32, 14, 19, 34 of the third audit)

## 4. Design

### The kit files, by target kind

```
derive_tool_root(target) answers <tr>       -> drop <tr>/**         rule "kit source <tr>/"
else .governance/install.json present       -> drop the receipt's rows (unit 4)   rule "receipt"
else                                        -> drop <d>/** for each <d> holding kit.toml   rule "kit.toml homes"
```

A source-mode receipt at gov (TOOL-dSafePassage-8, DEFERRED) records only the destinations its plan
accepts, which leaves the `project-owned` suites (`tools/workflows/kit.toml:35-37`) and govkit's own
files in the population, so the kit-source test runs first whatever receipt gov holds.

### The population on this repository

At `8c395e3c` this tree tracks 373 files that are neither under `memory/` nor `*.md`; 28 of them sit
outside `tools/` (PINNED, measured by the pass's own `git ls-files -z` probe). After S1 none of the 28
names `unattended-unit.js` with a retired key or spells the per-pass command. Unit 25 §1's 127 quoting
files are not "every one a markdown record": `.claude/skills/unattended/SKILL.md` is a rendered Skill,
and the markdown subtraction still takes it.

### What it does not check

- A call site an adopter writes inside a directory a `kit.toml` homes, on a target with no receipt:
  the directory is the kit's, and an update re-copies it.

### Inventory

Minted: the private module name `gov_govkit`; the three rule words of S3. No function: S1 and S2 are
branches of `derive_call_sites`.

### Migration

None: the steps have never run, since unit 4 lands them in this build.

### Rollout

Live at landing, beside unit 25.

### Files touched (estimate)

- `tools/govkit/steps/retired_dispatch_args.py`
- `tools/govkit/selftest.py`

### Alternatives rejected

- **Inline the gov-checkout test in the step.** A second copy of `derive_tool_root`'s rule, beside the
  one the deployer keeps.
- **Drop `tools/` by literal.** gov's tool root is `derive_tool_root`'s answer, and an adopter's prefix
  may be another directory.
- **Require a receipt.** gov's walk would refuse until TOOL-dSafePassage-8 lands, and a copy-install
  adopter never holds one.

## 5. Production-readiness checklist

- security — the step reads the target and writes nothing; `govkit.py` is loaded from the step's own
  tool root, never from a target path.
- perf / scale — one `derive_tool_root` call and one `kit.toml` glob per run.
- error / empty / loading states — S3's rule word names which rule ran, including one that dropped
  nothing.
- observability — the scan line on every `witness` and `up`.
- risks — an adopter's own script inside a copied kit dir is not scanned (§4).
- testing — AC1 to AC3 by fixtures and probes; the arm of §7 at the close.
- migration — none.
- user docs — none: the step's printed line is what the update walk shows.

## 6. Acceptance criteria

- **AC1** — When `python retired_dispatch_args.py witness <target> checklist` runs over a scratch
  target with no receipt holding `tools/workflows/kit.toml` and `tools/workflows/unattended-build.js`,
  which names `unattended-unit.js` and spells `checklist: 'x'`, it exits 0 and its scan line names
  `kit.toml homes`; once a `run.js` under the target's `scripts` directory, naming `unattended-unit.js` and passing `checklist: 'x'`
  is added, it exits 1 naming that file alone.
  Red when: a copy-installed kit's own file stops an adopter's walk.
  fixture: a scratch target repository under `%TEMP%`, built by the pass.
- **AC2** — When `python retired_dispatch_args.py`, run from `tools/govkit/steps`, runs `witness . checklist`,
  `witness . prebuild`, `up . checklist` and `up . prebuild` on this repository, each exits 0 and its
  scan line names `kit source tools/`.
  Red when: gov's own update walk stops on its kit source, which dropping S1 shows by naming govkit's
  own self-test file, the one file outside a kit home that spells the per-pass command.
  figure: the counts are DERIVED at observation time.
- **AC3** — When the AC1 target also holds `tools/govkit/registry.toml`, its scan line names
  `kit source tools/`; when the step's `govkit.py` load is pointed at a missing file, it exits 1 naming
  that file and scans nothing.
  Red when: a clone of gov reads as an adopter, or a failed load passes as an empty subtraction.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `policy fixtures` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC3 · a copy-install target, an adopter script beside it and a tree holding the registry, staged by dropping S1 and S2 so the kit's own file hits · none

## 8. Open questions

- **F1 — What are a target's kit files when it holds no receipt?** Options: (a) gov's tool root for a
  tree holding gov's kit source, else every directory a `kit.toml` homes; (b) every path under the
  deploy prefix; (c) none, so a receipt is required. (b) needs a `deploy.toml` a copy-install adopter
  may not hold; (c) leaves gov's walk blocked, the defect. RESOLVED (agent, 2026-10-26, delegated):
  (a), rung 3, the skeptic-judged fix in the report. widens: none · relaxes: none
- **F2 — How does the step tell gov's source from an adopter?** Options: (a) `derive_tool_root`,
  loaded from the step's own tool root; (b) the same test inlined in the step. (b) copies a rule the
  deployer owns. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, reuse of the seam M5 found.
  widens: none · relaxes: none
- **F3 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-26,
  delegated): `**Derived:**` naming `PLAY-dClosedLoop-2`, rung 3, the precedent `TOOL-dBoundRoles-39`
  §8 F1 records. widens: none · relaxes: none
- **F4 — The units this one extends are unbuilt.** `TOOL-dFurnishedOrders-4` S7 and `-25` are specced
  and unbuilt at `8c395e3c`. RESOLVED (agent, 2026-10-26, delegated): the build run re-grounds on each
  at the pass and stops this unit if a named section is still absent then, rung 1, the brief's rule for
  unbuilt parents. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the spec audit of the round-1 promotions, id 10
  (HIGH, item H4, shared with id 25).
- rev-2 · 2026-10-27 · §3 · the Edges block gains the **hands-off** bullet(s) mirroring TOOL-dFurnishedOrders-40, TOOL-dFurnishedOrders-41, promoted from the spec audit of the round-2 promotions (`memory/builds/dFurnishedOrders/reviews/2026-10-27-review-TOOL-dFurnishedOrders-31-spec-audit-round1.md`); nothing else moved.

## 10. Reuse audit

The seams extended: `derive_call_sites` (`TOOL-dFurnishedOrders-25` S1); `derive_tool_root`
(`tools/govkit/govkit.py:154-175`), the deployer's one test for gov's own checkout; the by-path load
precedent at `tools/govkit/govkit.py:3145`. `python tools/codebase-map/reuse_lookup.py "files a kit
homes on a target with no install receipt"` ranked `resolve_kit_dir`, `kit_rel` and `kit_dir`;
`resolve_kit_dir` finds one kit's file through a receipt or a probe and lists no kit's files, so no
existing seam fits the subtraction beyond the ones named. The recall probe returned TOOL-dSafePassage-8's
source-mode receipt, which §4 reads, and unit 25, neither disagreeing with source.

Recall terms used: `python tools/memory-recall/query.py "which kit files does an upgrade step skip on
gov's own checkout and on an adopter without an install receipt" --terms "install receipt kit.toml
project-owned suite call site retired key upgrade step witness tool root"`
