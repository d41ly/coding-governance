# DEPL-dShippedRelease-140 — the `mint-` cases move to `tools/govkit/matrix.py`, so no gov-only fact sits in a shipped kit file

**Status:** DEFERRED · rev-1 · 2026-11-01 · node d · Tier-2 · base f4597719 · streams deployer · order 32 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-87 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-119 DEPL-dShippedRelease-120 DEPL-dShippedRelease-121 DEPL-dShippedRelease-122 DEPL-dShippedRelease-123 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125 DEPL-dShippedRelease-126 DEPL-dShippedRelease-127 DEPL-dShippedRelease-128 DEPL-dShippedRelease-129 DEPL-dShippedRelease-130 DEPL-dShippedRelease-131 DEPL-dShippedRelease-132 DEPL-dShippedRelease-133 DEPL-dShippedRelease-134 DEPL-dShippedRelease-135 DEPL-dShippedRelease-136 DEPL-dShippedRelease-137 DEPL-dShippedRelease-138 DEPL-dShippedRelease-141 DEPL-dShippedRelease-142 DEPL-dShippedRelease-143 DEPL-dShippedRelease-144 DEPL-dShippedRelease-145 |
| [2026-11-01-build-DEPL-dShippedRelease-140-round5-disposal-return.md](../build/2026-11-01-build-DEPL-dShippedRelease-140-round5-disposal-return.md) | research | DEPL-dShippedRelease-141 DEPL-dShippedRelease-142 DEPL-dShippedRelease-143 DEPL-dShippedRelease-144 DEPL-dShippedRelease-145 |
| [2026-11-01-build-DEPL-dShippedRelease-144-token-fix-return.md](../build/2026-11-01-build-DEPL-dShippedRelease-144-token-fix-return.md) | research | DEPL-dShippedRelease-144 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 23 of `reviews/2026-11-01-review-DEPL-dShippedRelease-126-spec-audit-round1.md`, HIGH, item H2. Units 127 and 128
put a `read_descriptors` walk and a `target_context` call in `tools/integrations/ci/ci_emit.py`. That file ships, its
in-file arms run as the kit's `emitted ci self-test` leg, and an adopter has no registry and no em-dash answer, so
the cases exit 1 and red that adopter's bar on a fact about gov, the failure unit 54's goal records. In-process calls
also break "a kit imports no sibling", and a second classification walk stands beside `tools/govkit/matrix.py:188`.
This unit gives every gov-only `mint` case one home in the deployer's own harness, which never travels, and repairs
units 127 and 128, order 31, at the next step. Id 49, item M24, is the same defect's guard half, in
DEPL-dShippedRelease-144.

## 2. Scope (IN)

- **S1** — The door. `python tools/govkit/matrix.py --case <name>` runs one entry of `MINT_CASES`, a dict in that file,
  and exits as that case does. With no argument `main` runs every entry after `check_outcome_probes`. An unknown name
  exits 2 naming it. Observed by AC1.
- **S2** — The move. `mint-moved-kit` (units 122 and 127), `mint-answer-dash` (unit 126), `mint-regenerate-kits` and
  `mint-no-outcome-kit` (unit 128) move from `tools/integrations/ci/ci_emit.py` to `MINT_CASES`, each keeping its plant
  and its printed lines. Unit 138's `mint-no-descriptor` and `mint-memory-tree-stop` are built there, by this unit's
  edge to that unit. Observed by AC1.
- **S3** — The liveness term. `check_answers_armed(deploy, descs)` in `tools/govkit/matrix.py` holds unit 127 S2's term,
  reading `ROOT`'s tracked `.governance/deploy.toml` with no clone, and `mint-moved-kit` calls it first. Observed by AC2.
- **S4** — Nothing gov-only stays. `tools/integrations/ci/ci_emit.py` holds no `mint-` case, no govkit import, and no
  spawn of `tools/push-main.sh`. Unit 127 AC3's lander run moves out with them, and its new home is the arm id 24
  states in DEPL-dShippedRelease-144. Observed by AC3.
- **S5** — The adopter. A scratch install of the integrations kit runs its `--fixture` and exits 0 with no `mint-` line,
  and `tools/govkit/matrix.py` travels nowhere, so these cases owe no skip. Observed by AC4.

## 3. Non-goals (OUT)

- What `mint-regenerate-kits` runs: DEPL-dShippedRelease-145.
- The leg that reds a respelled answer at its landing, and which answers count: review ids 15 and 49, in
  DEPL-dShippedRelease-144.
- Running every kit's fixture cases in a scratch adopter install, as a gate: the audit's left-shift item, a gate of
  its own.
- A `[gate_leg.gov]` value on `emitted ci self-test`: nothing gov-only stays in that leg's arms to scope.

### Edges

- **consumes-from** `DEPL-dShippedRelease-122` — AC1's `mint-moved-kit` and §7's arm, which this unit moves
- **consumes-from** `DEPL-dShippedRelease-126` — AC3's `mint-answer-dash` and §7's arm, which this unit moves
- **consumes-from** `DEPL-dShippedRelease-127` — S2's term, AC1, AC2 and §7, which this unit moves
- **consumes-from** `DEPL-dShippedRelease-128` — S1, S2 and §7's first arm, which this unit moves
- **hands-off** `DEPL-dShippedRelease-138` — AC18's and AC19's cases, whose home is `MINT_CASES` and never `tools/integrations/ci/ci_emit.py`
- **hands-off** `DEPL-dShippedRelease-145` — `MINT_CASES` and `--case`, the home of that unit's run
- **hands-off** `DEPL-dShippedRelease-144` — `MINT_CASES` and `check_answers_armed`, which ids 15, 17, 24 and 49 read

## 4. Design

### Evidence

- `tools/govkit/registry.toml:492-494` is the `[[gov_only_pin]]` row for `{prefix}/govkit/*`, "the deployer itself, which never travels", and `:496-497` exempts `govkit acceptance matrix` on the same ground.
- `tools/push-main.sh:799-800` says govkit stays in gov, so `mint` never runs at an adopter.
- `tools/govkit/matrix.py:668` is `main`, and `:188` is `check_outcome_probes`, which already walks `read_descriptors`.
- `tools/gate-legs.json` gives `govkit acceptance matrix` a ceiling of 7030, where unit 8 §5 prices `emitted ci self-test` at "seconds at most", and no spec supersedes that line.
- `tools/govkit/govkit.py:1200` is `resolve_shell_argv`, which `matrix.py` can call and `ci_emit.py` may not, because a kit imports no sibling.
- `git grep -l` over the spec folder finds the six case names in units 122, 126, 127, 128 and 138 alone. PINNED at `e4c33972`.

### Supersedes

- Unit 122 AC1's and AC3's `python ci_emit.py --fixture --case`, and §7's second New arm: the door of S1, with AC3's run at id 24's arm.
- Unit 126 AC3's command and §7's New arm: the door of S1.
- Unit 127 S2's "calls `target_context` for `integrations` on the clone": S3 here. AC1 and AC2 read the door of S1, and §7's New arm reads `tools/govkit/matrix.py`.
- Unit 128 S1's home, AC1's and AC2's command, and §7's first New arm's home.
- Unit 138 AC18's and AC19's command, and §7's `ci_emit.py` arm: the door of S1.
- Each unit's `tools/integrations/ci/ci_emit.py` line under Files touched, for these cases.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `check_answers_armed` | function, `tools/govkit/matrix.py` | `py.function`, OK by `--suggest` at writing |
| `MINT_CASES` | constant, `tools/govkit/matrix.py` | none |
| `--case` | flag of `tools/govkit/matrix.py` | none |

### Files touched (estimate)

- `tools/govkit/matrix.py`: S1, S2, S3
- `tools/integrations/ci/ci_emit.py`: S2, S4

### Alternatives rejected

- **Keeping each case in `ci_emit.py` with a named skip, moving only the walk.** It leaves two clone builders in two kits, with no shared home, a bash spawn that kit cannot resolve, and a leg priced at seconds running clones.
- **A `[gate_leg.gov]` value on the leg.** It scopes the leg at an adopter and leaves a gov-only import in a shipped file.
- **A ctx override on `check_outcome_states`.** With unit 145 the population reads `cmd_mint`'s exit, so no classification needs a second context.

## 5. Production-readiness checklist

- security — N/A — fixture code moved between two gov files.
- perf / scale — the clone cases leave a leg priced at seconds for one whose ceiling is 7030, and S1 runs one case alone.
- error / empty / loading states — S1 names the unknown case, and each moved case keeps its own failures.
- observability — each moved case prints the lines its unit states.
- risks — a builder at orders 30 and 31 writes these cases in `ci_emit.py` as those specs say, and this pass moves them; a case left behind reds AC3.
- testing — the criteria of §6 and the arms of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — N/A — no surface a reader of `help/` meets changes.

## 6. Acceptance criteria

- **AC1** — When `python tools/govkit/matrix.py --case mint-moved-kit` runs at gov's root it exits 0 printing
  `ci-not-declared`, and `--case nope` exits 2 printing `nope`.
  Red when: a moved case lost its plant, or a misspelt name reads as an empty run.
  cost: one clone and one `mint`, under 20 seconds, PINNED at `e4c33972`.
- **AC2** — When `python -c` calls `check_answers_armed` with `ROOT`'s tracked `.governance/deploy.toml` it returns true
  naming `answers.stream_ownership`, and with that answer respelled in the loaded dict it returns false.
  Red when: the term reads a fixture, so a respelled answer leaves it green over an empty population.
- **AC3** — When `git grep -n -e 'mint-' -e 'push-main.sh' -e 'target_context' -e 'read_descriptors' -e 'import govkit' -- ci_emit.py`
  runs at the close in the `tools/integrations/ci` folder, it prints nothing.
  Red when: a gov-only case stays in a file that ships.
- **AC4** — When `python tools/govkit/govkit.py apply --target <scratch> --kits integrations` runs and the installed
  `ci_emit.py --fixture` runs in `<scratch>`, it exits 0 and its output holds no `mint-` line.
  Red when: a case bound to gov's tree reds an adopter's bar.
  fixture: a scratch adopter install under `%TEMP%`; the tree holds none today.

## 7. Gates

`recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/govkit/matrix.py · covers AC1 AC2 · the moved cases and `check_answers_armed`, its failing case `stream_ownership` respelled in the loaded dict · none

New arm: tools/integrations/ci/ci_emit.py · covers AC4 · a scratch adopter install's `--fixture`, its failing case one `mint-` case left in the module · none

## 8. Open questions

- **F1 — Which cases move?** The report's fix moves S1's walk and unit 127 S2's term, and keeps in `ci_emit.py` the
  cases that spawn `mint` as a child. Options: (a) as the report states, with a named adopter skip on each case left;
  (b) every gov-only case moves. (a) leaves two clone builders in two kits for ids 16, 17, 32 and 48 to fix twice, and
  a bash spawn id 17 must resolve inline. (b) restates five units' commands and leaves nothing to skip. RESOLVED (agent,
  2026-11-01, delegated): (b), rung 3, one home for one family of cases. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 23 (HIGH, item H2) of the round-5 spec audit.

## 10. Reuse audit

The seam extended is `check_outcome_probes` and `main` in `tools/govkit/matrix.py:188` and `:668`, the deployer's own harness.
`python tools/codebase-map/reuse_lookup.py "classification walk over descriptors inside a kit gate module"`
ranked the name-stem helper `walk` and missed `matrix.py`, the seam the report's citation found, so the probe and the
source disagree and the source stands. The recall probe surfaced DEPL-dCarriedReceipt-6 and this round's report,
which agree with this reading.

Recall terms used:
`python tools/memory-recall/query.py "which gate module holds a walk over kit descriptors for gov only facts" --terms "matrix check_outcome_probes read_descriptors adopter skip shipped kit gate_leg gov-only fixture cases sibling import"`
