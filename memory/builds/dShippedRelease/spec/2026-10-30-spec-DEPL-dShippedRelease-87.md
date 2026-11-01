# DEPL-dShippedRelease-87 — `ci_emit.py render` exits a reserved code when no table is declared

**Status:** OPEN · rev-2 · 2026-11-01 · node d · Tier-2 · base f4597719 · streams deployer · order 29 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-65 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 DEPL-dShippedRelease-108 DEPL-dShippedRelease-109 DEPL-dShippedRelease-110 DEPL-dShippedRelease-111 DEPL-dShippedRelease-112 DEPL-dShippedRelease-113 DEPL-dShippedRelease-114 DEPL-dShippedRelease-115 DEPL-dShippedRelease-116 DEPL-dShippedRelease-117 DEPL-dShippedRelease-118 DEPL-dShippedRelease-119 DEPL-dShippedRelease-120 DEPL-dShippedRelease-121 DEPL-dShippedRelease-122 DEPL-dShippedRelease-123 DEPL-dShippedRelease-124 DEPL-dShippedRelease-125 |
| [2026-11-01-build-DEPL-dShippedRelease-79-round2-disposal-return.md](../build/2026-11-01-build-DEPL-dShippedRelease-79-round2-disposal-return.md) | research | DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-86 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-90 DEPL-dShippedRelease-91 DEPL-dShippedRelease-92 DEPL-dShippedRelease-93 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-100 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-103 DEPL-dShippedRelease-104 DEPL-dShippedRelease-105 DEPL-dShippedRelease-106 |
| [2026-11-01-review-DEPL-dShippedRelease-79-spec-audit-round1.md](../reviews/2026-11-01-review-DEPL-dShippedRelease-79-spec-audit-round1.md) | spec-audit | DEPL-dShippedRelease-100 DEPL-dShippedRelease-81 DEPL-dShippedRelease-82 DEPL-dShippedRelease-93 DEPL-dShippedRelease-103 DEPL-dShippedRelease-92 DEPL-dShippedRelease-94 DEPL-dShippedRelease-95 DEPL-dShippedRelease-79 DEPL-dShippedRelease-80 DEPL-dShippedRelease-83 DEPL-dShippedRelease-84 DEPL-dShippedRelease-85 DEPL-dShippedRelease-90 DEPL-dShippedRelease-86 DEPL-dShippedRelease-91 DEPL-dShippedRelease-105 DEPL-dShippedRelease-101 DEPL-dShippedRelease-102 DEPL-dShippedRelease-104 DEPL-dShippedRelease-96 DEPL-dShippedRelease-97 DEPL-dShippedRelease-98 DEPL-dShippedRelease-99 DEPL-dShippedRelease-88 DEPL-dShippedRelease-89 DEPL-dShippedRelease-106 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 3 of `reviews/2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md`, HIGH, which shares item H1 with ids 49 and 89
(DEPL-dShippedRelease-88, -89). `classify_outcome` matches an exit code and filesystem probes only
(`tools/govkit/govkit.py:6581-6600`), and unit 8 S3 exits 0 with no `[gate_runner.ci]`, so an adopter
that declared no table and one whose render was lost are both exit 0 with `gov-bar.yml` absent. No
probe can read the table. This unit makes the two exits differ.

## 2. Scope (IN)

- **S1** — The code. `ci_emit.py render` with no `[gate_runner.ci]` prints `ci emit — not declared` and
  exits `EXIT_NOT_DECLARED`, 3, and writes nothing. Exit 0 means it wrote the file. Observed by AC1.
- **S2** — The refusal stands. Exit 2 keeps unit 8 S3's meaning, a destination holding no `# gov:ci-emit`
  marker. Observed by AC2.

## 3. Non-goals (OUT)

- The `[[outcome]]` row: DEPL-dShippedRelease-88.
- The stale-file case: DEPL-dShippedRelease-89.
- `OUTCOME_PROBE_KEYS`: a term reading the table is §8 F1's rejected option.

### Edges

- **consumes-from** `DEPL-dShippedRelease-8` — `ci_emit.py render`, whose no-table exit this unit moves
- **consumes-from** `DEPL-dShippedRelease-74` — the fork this unit re-opens by evidence, its S1 and S2
- **hands-off** `DEPL-dShippedRelease-88` — `EXIT_NOT_DECLARED`, the code that unit's row keys on
- **hands-off** `DEPL-dShippedRelease-122` — `EXIT_NOT_DECLARED`, the exit this unit routes (round-3 id 47)
- **hands-off** `DEPL-dShippedRelease-125` — the text and code which the round-3 minors batch repairs (round-3 ids 18)

## 4. Design

### Evidence

- `tools/govkit/govkit.py:6581-6600` matches `oc.get("code") != rc`, then the probe keys, with no read of a descriptor table.
- `tools/memory-tree/kit.toml:141-149` is the model: `code = 1`, a probe, `means = "seed-and-stop"`, `ok = true`, a declared non-zero stop.
- Unit 8 S3 uses exit 2 for its refusal, and unit 6's and unit 15's codes are their own verbs', so 3 collides with nothing `render` prints.

### Supersedes

- Unit 8 S3's "prints `ci emit — not declared` and exits 0", and its §5 line "no `[gate_runner.ci]` is one line and exit 0".
- Unit 74 §8 F1's premise that exit 0 can carry the row.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `EXIT_NOT_DECLARED` | module constant, `tools/integrations/ci/ci_emit.py` | none |

### Files touched (estimate)

- `tools/integrations/ci/ci_emit.py`: S1

## 5. Production-readiness checklist

- security — N/A — no new write path, stored-content class, outbound call or automation surface.
- perf / scale — N/A — a read or a compare on a path that already runs once per landing.
- error / empty / loading states — the criteria of §6 name each refused and empty state.
- observability — each state prints the line §2 names, on green and red.
- risks — a caller reading `render`'s exit outside `apply` sees 3 where unit 8 said 0; `update`'s `[[regenerate]]` row reads the same outcome block.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — N/A — no surface a reader of `help/` meets changes.

## 6. Acceptance criteria

- **AC1** — When `python ci_emit.py render --target <scratch>` runs with no `[gate_runner.ci]`, it
  prints `ci emit — not declared`, exits 3 and writes no file; with the table it exits 0 and writes
  `gov-bar.yml`.
  Red when: exit 0 means two things, so the row cannot tell a stop from a loss.
- **AC2** — When it runs with a `gov-bar.yml` holding no marker, it exits 2 and the bytes are unchanged.
  Red when: the reserved code swallowed the refusal.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/integrations/ci/ci_emit.py · covers AC1 AC2 · a scratch target with no table, its failing case exit 0 on no table · none

## 8. Open questions

- **F1 — How are the two told apart?** Options: (a) by exit, a reserved code; (b) an `OUTCOME_PROBE_KEYS`
  term that reads the table. (b) grows the probe grammar for one kit, and (a) needs no new key.
  RESOLVED (agent, 2026-11-01, delegated): (a), rung 3, the shape `seed-and-stop` already has. widens:
  none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 3 (HIGH, item H1) of the round-2 spec audit.
- rev-2 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the round-3 spec audit's promoted units declare toward this unit (units 122, 125); no scope, design or criterion moved.

## 10. Reuse audit

The seam extended is `classify_outcome` at `tools/govkit/govkit.py:6557`, by an exit it already reads, with `seed-and-stop` at `tools/memory-tree/kit.toml:144` as the model.
`python tools/codebase-map/reuse_lookup.py "decide an install outcome from an exit code and a probe"`
ranked `probe`, `classify_outcome`, `outcome_accepted` and `decide`, which is that seam. The recall
probe surfaced TOOL-dRedressedBar-9, an accepted stop of the same shape, and report item H1.

Recall terms used:
`python tools/memory-recall/query.py "how does an adopter tell a declared stop from a lost render" --terms "classify_outcome outcome row stopped_ok rendered must_not_exist adopter exit seed-and-stop gate_runner ci"`
