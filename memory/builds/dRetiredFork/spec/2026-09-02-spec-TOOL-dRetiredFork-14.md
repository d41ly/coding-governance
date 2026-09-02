# TOOL-dRetiredFork-14 — one hook copy is shipped and wired, not two

**Status:** OPEN · rev-1 · 2026-09-02 · node d · Tier-2 · base b0108f13 · streams tooling · order 4

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

gov ships three hooks to two destinations each and the pairs are byte-identical. Measured
2026-09-02: `tools/hooks/agent-cap.js` and `.claude/hooks/agent-cap.js` are identical at 1610 lines,
`scratch-guard.js` at 394, and `tools/memory-recall/recall-opened.js` against
`.claude/hooks/recall-opened.js` at 207 — 2211 duplicated tracked lines. Every policy value in those
files is therefore stated twice, which is why `nc carve-out 13/20` occupies eleven files: the
dual-ship doubles it before anyone edits anything.

## 2. Scope (IN)

- **S1** — Point the wired command at `{prefix}/hooks/agent-cap.js`. `tools/settings-merge.py`
  already takes `hook_path` as a parameter and merely DEFAULTS it to `.claude/hooks/agent-cap.js`,
  with `--hook-path` as the override, so this is a call-site change and not a new capability.
- **S2** — Drop the `.claude/hooks/` destinations from the hooks and memory-recall descriptors, so
  one copy ships.
- **S3** — The two-copy parity arm becomes SELF-ARMING on the resolved destination count: it must
  assert what it finds rather than assume two, and it must REFUSE on zero. A parity arm over a
  population of one that assumes two is the green-by-absence class this repo has already recorded.
- **S4** — `tools/check-wiring.sh` verifies the wired command names the shipped copy, and reports —
  not reds — when a legacy second copy is still present, so an adopter mid-migration is told rather
  than blocked.
- **S5** — Bump `KIT_AGENT_CAP_VERSION`, `KIT_SETTINGS_MERGE_VERSION` and `KIT_MEMORY_RECALL_VERSION`
  with every paired marker, which `tools/check-kit-versions.sh` derives from every tracked `*.js`.

## 3. Non-goals (OUT)

- **The cap VALUE.** This unit changes how many files state the number, never the number. Whether it
  becomes a declared key is parked at build level as an owner turn.
- Deleting an adopter's second copy. gov stops SHIPPING one; removing an installed one is a
  withdrawal, which `govkit update --write-withdrawals` performs on the adopter's own timing.

## 4. Design

### Inventory

| pair | lines | destination after |
|---|---|---|
| `agent-cap.js` | 1610 | `{prefix}/hooks/agent-cap.js` |
| `scratch-guard.js` | 394 | `{prefix}/hooks/scratch-guard.js` |
| `recall-opened.js` | 207 | `{prefix}/memory-recall/recall-opened.js` |

### Migration

gov's own `.claude/settings.json` is rewritten to the new command in the same commit, and gov's
SessionStart wiring check must pass immediately — gov is its own first adopter here, so a mistake is
visible on the next session rather than at an adopter.

An adopter's transition is two steps and they are ordered: the wired command must move to the
surviving copy BEFORE the second copy is withdrawn, or the hook is unwired for the window between.
`DEPL-dRetiredFork-3` is what makes that ordering enforceable rather than a runbook instruction.

### Alternatives rejected

Keeping both destinations and adding a parity gate. A parity gate over two copies is what gov has,
and it costs 2211 lines plus a doubled edit surface to buy a property that one copy has for free.

## 5. Production-readiness checklist

- security — the agent-cap hook is a security-shaped guard. A window in which it is unwired is the
  risk, and S4 plus the migration ordering exist for it.
- perf / scale — one fewer file to read at SessionStart.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — the parity arm REFUSES on a zero population; the wiring check
  REPORTS a legacy copy rather than redding.
- observability — `tools/check-wiring.sh` prints which copy is wired, every session.
- risks — an adopter whose settings file is not rewritten keeps pointing at a withdrawn path and
  loses the hook silently. This is the highest risk in the build and is why S4 reports rather than
  reds, and why the withdrawal is not part of this unit.
- testing + left-shift gates — the agent-cap suite, the wiring suite, and a fixture that verifies
  the two-step ordering.
- migration / rollback — restoring the second destination is a descriptor edit; nothing is deleted
  from an adopter by this unit.
- user docs — `WIRE-INTO-PROJECT.md` maintenance section, and `tools/hooks/README.md`.

## 6. Acceptance criteria

- **AC1** — After the change, `git ls-files` shows one tracked copy of each of the three hooks.
- **AC2** — When `python tools/settings-merge.py --hook-path tools/hooks/agent-cap.js` runs against
  gov's settings, the wired command names the shipped copy and `bash tools/check-wiring.sh` exits `0`.
- **AC3** — When only one copy exists, the parity arm asserts against a population of one and
  passes; when zero exist, it REFUSES. Observed via `bash .claude/hooks/agent-cap.test.sh`.
- **AC4** — When a legacy second copy is present, `bash tools/check-wiring.sh` REPORTS it and still
  exits `0`.
- **AC5** — `bash .claude/hooks/agent-cap.test.sh` passes against the surviving copy.
- **AC6** — `bash tools/check-kit-versions.sh` exits `0`, with every tracked `*.js` marker agreeing.

## 7. Gates

`agent-cap self-test` · `wiring` · `wiring self-test` · `kit versions` · `govkit selfcheck` ·
`agent-cap restatement parity`.

## 8. Open questions

- **F1 — does `.claude/hooks/` remain a legal destination for a project that wants it?** Dropping it
  from gov's descriptors does not forbid an adopter choosing it via a per-entry `kit`. Recommendation:
  keep it expressible, ship it unused.
- **F2 — what withdraws the second copy at an adopter, and when?** `--write-withdrawals` is the only
  verb that deletes, it defaults off, and the ordering constraint above makes premature use unsafe.
  Recommendation: leave the withdrawal to the adopter and say so in the maintenance docs; do not
  automate a delete whose wrong ordering unwires a security guard.

## 9. Revision log

- rev-1 · 2026-09-02 · initial draft. Duplication measured directly at b0108f13 rather than cited.

## 10. Reuse audit

The seam is `tools/settings-merge.py`'s existing `hook_path` parameter — `reuse_lookup.py` reports
the `agent-cap` affordance seam covering install and prefix concerns, and `merge(obj, hook_path,
frag)` at `tools/settings-merge.py:91` is the exact extension point, already parameterised and
already exercised by `--hook-path`. No new mechanism is built; a default is stopped from being a
decision.

Recall terms used: `agent-cap`, `dual-ship`, `settings-merge`, `hook_path`, `wiring`, `parity`,
`destination`, `descriptor`, `withdrawal`, `adopter`, `prefix`, `carve-out`.
