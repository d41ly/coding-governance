# TOOL-aReapedSpinner-6 — the kit skeleton: a declared population an adopter joins by declaration

**Status:** OPEN · rev-1 · 2026-09-08 · node a · Tier-2 · base e2b82a53 · streams tooling · order 1

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Land `tools/process-monitor/` as a DECLARED govkit entry — descriptor, conf, adopter, README — so
that every later unit's file has a home the deployer already knows about, and an adopter installs
the monitor by declaring its roots rather than by porting a script.

## 2. Scope (IN)

- **S1** — `tools/process-monitor/kit.toml`, the descriptor: id, home, scope, `version_from`, the
  `[[files]]` roles, the `[adopt]` and `[check]` argv, and the `[[gate_leg]]` rows this kit brings.
  Observed by AC1.
- **S2** — a `[[entry]]` row in `tools/govkit/registry.toml` pointing at that descriptor. Observed
  by AC1.
- **S3** — `.process-monitor.conf` at the repo root, holding every value the kit READS and nothing
  it could derive: the scope roots, the age ceilings, the reap mode, and the report throttle.
  Every key carries its reason in a comment beside it, as the sibling confs do. Observed by AC2.
- **S4** — `tools/process-monitor/adopt-process-monitor.sh`, with a `--check` mode that verifies
  wiring without repairing it. Observed by AC3.
- **S5** — `tools/process-monitor/README.md`, stating what the kit checks AND what it does not.
  Observed by AC4.
- **S6** — a `[[hole]]` declaration for the one value that ships unfillable: `PROCMON_ROOTS`, which
  is the adopter's own paths and cannot be seeded from this tree. Observed by AC5.

## 3. Non-goals (OUT)

- **No engine.** This unit ships declarations, an adopter and a README. `census.py`, `scope.py`,
  `classify.py`, `reap.py` and the hook belong to units 1 to 5, and this unit must land green
  WITHOUT them.
- **No gate legs that run an engine that does not exist yet.** The `[[gate_leg]]` rows S1 declares
  are the kit's own wiring check only; the engine legs arrive with the units that build them.
- **No adopter-facing ceilings measured against THIS corpus.** A pin measured here and shipped into
  a tree that never measured it is vacuous or permanently red — the rule
  `build-readme-slot-limits.txt` states about its own values.

### Edges

- **hands-off** `TOOL-aReapedSpinner-1` — this unit creates the directory and the descriptor's
  `[[files]]` rule that will CLAIM `census.py`. Without it, `govkit selfcheck` reds the moment any
  file under `tools/process-monitor/` becomes tracked, because that leg asserts every tracked path
  in the surface is a member of some entry. That coupling is why this unit is `order 1`.
- **hands-off** `TOOL-aReapedSpinner-2` — `PROCMON_ROOTS`, the one key whose blank value is a
  refusal rather than an empty set.
- **hands-off** `TOOL-aReapedSpinner-3` — `PROCMON_AGE_CEILING` and `PROCMON_SPIN_RATE`.
- **hands-off** `TOOL-aReapedSpinner-5` — the conf keys S3 declares are what the hook reads for its
  throttle; the hook declares no value of its own.
- **hands-off** `TOOL-aReapedSpinner-4` — `PROCMON_REAP_MODE` is declared here and CONSUMED there.
- **consumes-from** external — `tools/govkit/registry.toml` and its `[surface]` globs, which
  already claim `tools/*` and therefore already reach this directory.

## 4. Design

### Inventory

Identifiers this unit MINTS, each beside the cell that grades it:

| Name | Cell | Where |
|---|---|---|
| `PROCMON_ROOTS` | conf key, ungraded | `.process-monitor.conf` |
| `PROCMON_AGE_CEILING` | conf key, ungraded | `.process-monitor.conf` |
| `PROCMON_SPIN_RATE` | conf key, ungraded | `.process-monitor.conf` |
| `PROCMON_REAP_MODE` | conf key, ungraded | `.process-monitor.conf` |
| `PROCMON_THROTTLE_S` | conf key, ungraded | `.process-monitor.conf` |
| `KIT_PROCESS_MONITOR_VERSION` | `py.constant`, SCREAMING_SNAKE | `census.py`, per `version_from` |

### The conf, and why each key is DECLARED rather than derived

`PROCMON_ROOTS` cannot be derived: an adopter's agent work lives where that adopter puts it, and the
scratchpad root is outside the repo entirely. `PROCMON_AGE_CEILING` cannot be derived either — this
repo's own bar has a 26-minute floor and a 3600 s `GATE_BOUND`, so a ceiling below those would kill
a healthy bar. `PROCMON_REAP_MODE` is the adopter's risk tolerance and is the one key whose default
is stated in §8. The remaining two are tuning.

**BLANK `PROCMON_ROOTS` is a REFUSAL, not an empty set.** An unfilled roots list would make the
scope fence match nothing, and a monitor that reports zero because it was never configured is
indistinguishable from a clean tree. That is why S6 declares it as a `[[hole]]`.

### Files touched (estimate)

New: `tools/process-monitor/{kit.toml,adopt-process-monitor.sh,README.md}`,
`.process-monitor.conf`. Edited: `tools/govkit/registry.toml` (one entry row), `.gitattributes`
(LF pins for the shell and conf).

## 5. Production-readiness checklist

- security — the adopter writes only inside the target's own tree and never sets git config; the
  `--check` mode writes nothing at all.
- perf / scale — declarations only; no runtime cost.
- error / empty / loading states — a blank `PROCMON_ROOTS` refuses (§4); a missing conf refuses
  naming the key it wanted.
- observability — `--check` names every unwired item rather than reporting one aggregate verdict.
- risks — the govkit surface assertion is bidirectional, so a descriptor claiming a path this kit
  does not ship reds exactly as loudly as an unclaimed file. The `[[files]]` rule is `**`, which
  makes both directions automatic.
- testing — the kit's own `--check` is the wiring gate; `govkit selfcheck` grades the registry join.
- migration — none; new kit. No adopter has it today, so nothing upgrades.
- user docs — S5 is the doc.

## 6. Acceptance criteria

- **AC1** — When `python tools/govkit/govkit.py selfcheck` runs with the entry row landed, it exits
  0 and its output names `process-monitor` among the entries. Observed by
  `tools/govkit/govkit.py`.
  Red when: a tracked file under the kit dir is claimed by no `[[files]]` rule, or the descriptor
  claims a path the kit does not ship — the assertion is bidirectional and both directions red.
- **AC2** — When `.process-monitor.conf` is present with a BLANK `PROCMON_ROOTS`, the adopter's
  `--check` exits non-zero naming that key. Observed by `adopt-process-monitor.sh`, arm staged in
  `adopt-process-monitor.test.sh`.
  Red when: a blank roots list is read as an empty set and `--check` passes, which would ship a
  monitor that reports a clean tree because it was never configured.
- **AC3** — When `adopt-process-monitor.sh --check` runs in this tree
  after adoption, it exits 0; when run against a scratch tree missing the conf, it exits non-zero
  naming the missing file. Observed by `adopt-process-monitor.test.sh`.
  Red when: `--check` repairs anything. It is the non-repairing mode by contract, the same split
  `.unattended.conf` records for `WIRING_CHECK`.
- **AC4** — When `README.md` is read, it carries a section stating what this kit does NOT check.
  Observed by `check-kit-placeholders.py`, which already refuses an unfilled placeholder in a kit
  README.
  Red when: the README ships with template placeholders unfilled.
- **AC5** — When `python tools/govkit/govkit.py selfcheck` runs, the `procmon-roots` hole is
  reported as a declared hole with a discharge probe, and the probe exits non-zero on a blank
  `PROCMON_ROOTS`. Observed by `tools/govkit/govkit.py`.
  Red when: the hole is declared with a probe that cannot fail — the discharge command must be run
  against a blank value before this unit closes, not merely written.
- **AC6** — When this unit lands, `bash tools/run-gates/run-gates.sh` is green with NO engine file
  present under the kit dir. Observed by `tools/run-gates/run-gates.sh`.
  Red when: a `[[gate_leg]]` row declared here runs an engine unit 1 has not built, which would make
  this unit unlandable on its own and collapse the build's ordering.
  `cost:` a full bar, roughly 26 minutes of wall at this repo's floor.

## 7. Gates

`govkit selfcheck` · `govkit refusal join` · `govkit acceptance matrix` · `line length` · `dead-path carriers (deleted files still named)` · `hook destinations (every declared hook path ships)` · `kit version markers`

New arm: `tools/process-monitor/adopt-process-monitor.test.sh` · stages a missing conf, a blank
`PROCMON_ROOTS`, and a descriptor claiming an absent path · no assertion floor yet, this suite is new.

## 8. Open questions

- **F1 — what is the DEFAULT `PROCMON_REAP_MODE`?**
  Options: `report` (never kill without an explicit verb), `reap-orphans` (auto-kill only rows whose
  parent is dead AND which are past the age ceiling), `reap-all` (auto-kill every flagged row).
  RESOLVED (agent, 2026-09-08, delegated): `reap-orphans`. The owner's prompt names KILL as a
  required capability, so `report` under-delivers; `reap-all` would put an irreversible action on a
  single-sample heuristic, which template §9 forbids by default. `reap-orphans` is the class whose
  evidence is strongest — a process whose parent is dead and which is hours past its ceiling has no
  live claimant by construction — and it is the class every example in the prompt belongs to. The
  vetoes pass: no criterion or non-goal is broken, no dependency is added, and the write surface
  does not widen beyond what the unit was scoped for. `reap-all` stays reachable by declaration.

## 9. Revision log

- rev-1 · 2026-09-08 · initial draft.

## 10. Reuse audit

The seam this unit EXTENDS is `tools/govkit/registry.toml` and the descriptor grammar
`tools/drift-audit/kit.toml` demonstrates — `python tools/codebase-map/reuse_lookup.py "kill a hung
or idle background process and report it to the session"` returned the `govkit` dossier and
`registry.toml` as an affordance seam, and that is the one hit in the probe that was a real seam
rather than a name collision. The descriptor is copied in SHAPE from `drift-audit`, which is the
closest structural sibling: one directory, one engine, a conf owned elsewhere, a self-test withheld
from adopters. Verified against source at BASE.

Recall terms used: `gate runner wall clock bound timeout kill children orphan process leg pool
watchdog GATE_WALL background subprocess reaper`
