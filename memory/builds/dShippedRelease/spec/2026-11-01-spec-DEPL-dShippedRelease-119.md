# DEPL-dShippedRelease-119 — the census states its predicate for a list argv, so a subprocess spawn is read and a non-spawn is not

**Status:** OPEN · rev-2 · 2026-11-01 · node d · Tier-2 · base f4597719 · streams deployer · order 21 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-120 DEPL-dShippedRelease-121 DEPL-dShippedRelease-122 DEPL-dShippedRelease-123 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125 DEPL-dShippedRelease-126 DEPL-dShippedRelease-127 DEPL-dShippedRelease-128 DEPL-dShippedRelease-129 DEPL-dShippedRelease-130 DEPL-dShippedRelease-131 DEPL-dShippedRelease-132 DEPL-dShippedRelease-133 DEPL-dShippedRelease-134 DEPL-dShippedRelease-135 DEPL-dShippedRelease-136 DEPL-dShippedRelease-137 DEPL-dShippedRelease-138 DEPL-dShippedRelease-140 DEPL-dShippedRelease-141 DEPL-dShippedRelease-142 DEPL-dShippedRelease-143 DEPL-dShippedRelease-144 DEPL-dShippedRelease-145 |
| [2026-11-01-build-DEPL-dShippedRelease-108-round3-disposal-return.md](../build/2026-11-01-build-DEPL-dShippedRelease-108-round3-disposal-return.md) | research | DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-120 DEPL-dShippedRelease-121 DEPL-dShippedRelease-122 DEPL-dShippedRelease-123 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125 |
| [2026-11-01-review-DEPL-dShippedRelease-108-spec-audit-round1.md](../reviews/2026-11-01-review-DEPL-dShippedRelease-108-spec-audit-round1.md) | spec-audit | DEPL-dShippedRelease-123 DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-124 DEPL-dShippedRelease-121 DEPL-dShippedRelease-120 DEPL-dShippedRelease-122 DEPL-dShippedRelease-125 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 5 of `reviews/2026-11-01-review-DEPL-dShippedRelease-79-spec-audit-round1.md`, HIGH, item H5. Unit 102 S1's
"a call whose string arguments include the literal" does not cover a list argv. Direct arguments alone
reproduce the pinned files and miss `subprocess.run([sys.executable, gov, 'update', ...])`, the natural
spelling of unit 16's offer spawn, so that harness lands undeclared and reds on the first tag. A nested
reading adds calls that are no spawn, and unit 106 AC4 cannot pass. This unit defines the predicate
exactly and pins its output.

## 2. Scope (IN)

- **S1** — The direct arm. A `.py` call counts when a positional argument is a string literal in
  `CENSUS_VERBS` and the callee's last name is not in `CENSUS_NOT_A_SPAWN`, so a helper such as
  `run_in_gov` is read. Observed by AC1, AC2.
- **S2** — The argv arm. A `.py` call counts when the callee's last name is in `CENSUS_SPAWN_CALLS`
  (`run`, `Popen`, `check_output`, `check_call` and `call`), its first positional argument is a list or
  tuple literal holding a string literal in `CENSUS_VERBS`, and that literal's first element is not `git`.
  Observed by AC1, AC3.
- **S3** — The non-spawns. `append`, `write_fixture` and a `frozenset` constant fall outside S2 by its
  callee test, so `CENSUS_NOT_A_SPAWN` stays `get` and `run_git`. Observed by AC1.
- **S4** — The plants. `harness_census.py --selftest` carries one planted file per spelling: a helper
  string, a `subprocess.run` list, a `Popen` tuple, a `git` argv, an `append`, and a `write_fixture`. Each
  reads as §4's table says. Observed by AC1.
- **S5** — The pin. §4 re-pins the file list from this predicate, the list unit 106 §4 "The census at
  base" compares. Observed by AC2.

## 3. Non-goals (OUT)

- `*.sh`: review id 63, in the minors batch, states the shell half, and at base no shell file spawns the deployer.
- A list built in a variable and passed by name: unit 102 §5 prices it, and it reds the refusal's own line after the first tag.
- The verbs `adopt` and `update`: unit 106 S8 widens `CENSUS_VERBS`, which this unit names and sets to `apply`.

### Edges

- **consumes-from** `DEPL-dShippedRelease-102` — S1, whose predicate this unit restates, and §4's evidence
- **consumes-from** `DEPL-dShippedRelease-61` — S2's harness rule, which the census enforces
- **hands-off** `DEPL-dShippedRelease-106` — `CENSUS_VERBS`, which S8 widens, and the predicate AC4 reads
- **hands-off** `DEPL-dShippedRelease-125` — the predicate, whose shell half and leg that unit states (round-3 ids 37, 62, 63)
- **hands-off** `DEPL-dShippedRelease-138` — the text and code the batch repairs (round-4 ids 19, 38, 67, 68)

## 4. Design

### Evidence

Measured by an `ast` walk over the 104 tracked `.py` files under `tools/` but `tools/govkit/govkit.py`, PINNED at `3f8ecfad`:

- Direct string arguments of `apply`, `adopt` or `update`, by file and callee: `tools/govkit/matrix.py` (`run`, `run_in_gov`), `tools/govkit/selftest.py` (`run`, `run_in_gov`, `run_gov`, `run_gov13`, `run_gov17`, `run_govkit`, `run_pv_govkit`, `gov_run`, `fork_gov`, `run_ungraded_update`, `run_fragment_merges`, `remove_wired_fragments`) and `tools/policy/check_policy.py` (`run_govkit`), plus `get` in `tools/check-kit-placeholders.py`, `tools/playbook/render_playbook.py`, `tools/policy/check_policy.py` and `tools/govkit/selftest.py`, and `run_git` in `tools/branch-reconcile/selftest.py`.
- A list or tuple first argument holding such a literal: `tools/govkit/selftest.py` (`run`, `Popen`) and `tools/policy/check_policy.py` (`append`).
- With `CENSUS_VERBS` at `apply` alone, the direct arm prints the same three files.
- Report id 5 also read `write_fixture` in `tools/run-gates/check-receipt.py` and a `frozenset` in `tools/codebase-map/map_extractors.py`; id 63 did not reproduce the second, and neither is a first-argument list in a call S2 names.

### The planted spellings

| Plant | Arm | Listed |
|---|---|---|
| `run_in_gov("apply", ...)` | S1 | yes |
| `subprocess.run([py, gov, "apply"])` | S2 | yes |
| `Popen((py, gov, "apply"))` | S2 | yes |
| `subprocess.run(["git", "apply", p])` | S2, its `git` test | no |
| `rows.append(["apply", 1])` | S2, its callee test | no |
| `write_fixture(["apply"])` | S2, its callee test | no |
| `conf.get("apply")` | S1, `CENSUS_NOT_A_SPAWN` | no |

### The census at base, from this predicate

`tools/govkit/matrix.py`, `tools/govkit/selftest.py`, `tools/policy/check_policy.py`. PINNED at `3f8ecfad`.

### Supersedes

- Unit 102 S1's "a call whose string arguments include the literal `apply`".
- Unit 102 §4's second Evidence bullet: the pin above stands in its place.
- Unit 106 S10's list of helpers reads as this predicate's output, and §4 "The census at base" compares this pin.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `CENSUS_VERBS`, `CENSUS_SPAWN_CALLS` | module constants, `tools/govkit/harness_census.py` | none |

### Files touched (estimate)

- `tools/govkit/harness_census.py`: S1 to S4

### Alternatives rejected

- **Every nested string in a call.** It reads a list passed to `append` and to `write_fixture`, so unit 106 AC4's file list cannot be stated, as report id 63 measured.

## 5. Production-readiness checklist

- security — N/A — no new write path, stored-content class, outbound call or automation surface.
- perf / scale — N/A — one more arm of a walk over tracked files.
- error / empty / loading states — unit 102 §5 stands for an unparseable file and an empty census.
- observability — one line per listed file, as unit 102 §5 states.
- risks — a spawn helper outside `CENSUS_SPAWN_CALLS` taking a list reads only by the direct arm, and reds the refusal's own line after the first tag; S4's plants name what is read.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — N/A — no surface a reader of `help/` meets changes.

## 6. Acceptance criteria

- **AC1** — When `python harness_census.py --selftest` runs, each row of §4's table reads as listed, and a
  plant cut from the arm reds naming it.
  Red when: a subprocess spawn lands undeclared, or a non-spawn is demanded a declaration.
- **AC2** — When `python harness_census.py` runs at the pass, its file lines hold §4's three, and every
  other line names a harness a unit of this build added.
  Red when: the stated predicate and the pinned list disagree, as they did at unit 102.
  fixture: `offer.py` lands at order 20, so the pass reads it too.
- **AC3** — When a scratch copy gains a file spawning `subprocess.run([sys.executable, gov, "apply"])`
  with no assignment, the module exits 1 naming that file.
  Red when: the natural spelling of unit 16's spawn passes the census.

## 7. Gates

`recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/govkit/harness_census.py · covers AC1 AC3 · one planted file per spelling, its failing case the argv arm cut out · none

## 8. Open questions

- **F1 — Which calls read a list?** Options: (a) spawn names only; (b) a first-argument list in any call,
  with non-spawns listed in `CENSUS_NOT_A_SPAWN`; (c) every nested string. (c) cannot state unit 106 AC4's
  list, and (b) grows an exemption per non-spawn. RESOLVED (agent, 2026-11-01, delegated): (a), rung 3,
  the report's stated predicate. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 5 (HIGH, item H5) of the round-3 spec audit.
- rev-2 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the round-4 spec audit's promoted units declare toward this unit (units 138); no scope, design or criterion moved.

## 10. Reuse audit

The seam extended is `derive_deployer_spawns` (unit 102 S1).
`python tools/codebase-map/reuse_lookup.py "detect a subprocess spawn of a verb through a list argv"`
ranked `leading_verb` in `tools/lexicon/subtokens.py`, a name-stem hit, and no spawn reader, because the
module is specced and unbuilt, so no existing seam fits outside the parent's own module. The recall
probe surfaced unit 102 and TOOL-dPolishedVitrine-7, which agree with this reading.

Recall terms used:
`python tools/memory-recall/query.py "how does the install-from census find a harness" --terms "census GOVKIT_INSTALL_FROM spawn subprocess Popen argv harness declaration apply adopt update"`
