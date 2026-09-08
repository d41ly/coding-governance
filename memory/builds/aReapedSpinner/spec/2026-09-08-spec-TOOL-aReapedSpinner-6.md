# TOOL-aReapedSpinner-6 — the kit skeleton: a declared population an adopter joins by declaration

**Status:** CLOSED · rev-4 · 2026-09-08 · node a · Tier-2 · base e2b82a53 · streams tooling · order 1 · ratified 2026-09-08

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-08-prompt-TOOL-aReapedSpinner-6-brief.md](../prompts/2026-09-08-prompt-TOOL-aReapedSpinner-6-brief.md) | journal | — |
| [2026-09-08-review-TOOL-aReapedSpinner-1-closing-diff-round1.md](../reviews/2026-09-08-review-TOOL-aReapedSpinner-1-closing-diff-round1.md) | diff-review | TOOL-aReapedSpinner-1 TOOL-aReapedSpinner-2 TOOL-aReapedSpinner-3 TOOL-aReapedSpinner-4 TOOL-aReapedSpinner-5 TOOL-aReapedSpinner-7 |
| [2026-09-08-review-TOOL-aReapedSpinner-1-spec-audit-round1.md](../reviews/2026-09-08-review-TOOL-aReapedSpinner-1-spec-audit-round1.md) | spec-audit | TOOL-aReapedSpinner-1 TOOL-aReapedSpinner-2 TOOL-aReapedSpinner-3 TOOL-aReapedSpinner-4 TOOL-aReapedSpinner-5 TOOL-aReapedSpinner-7 |
| [2026-09-08-review-TOOL-aReapedSpinner-1-spec-audit-round2.md](../reviews/2026-09-08-review-TOOL-aReapedSpinner-1-spec-audit-round2.md) | spec-audit | TOOL-aReapedSpinner-1 TOOL-aReapedSpinner-2 TOOL-aReapedSpinner-3 TOOL-aReapedSpinner-4 TOOL-aReapedSpinner-5 TOOL-aReapedSpinner-7 |
| [2026-09-08-review-TOOL-aReapedSpinner-1-spec-audit-round3.md](../reviews/2026-09-08-review-TOOL-aReapedSpinner-1-spec-audit-round3.md) | spec-audit | TOOL-aReapedSpinner-1 TOOL-aReapedSpinner-2 TOOL-aReapedSpinner-3 TOOL-aReapedSpinner-4 TOOL-aReapedSpinner-5 TOOL-aReapedSpinner-7 |

<!-- /gen:spec-records -->

## 1. Goal

Land `tools/process-monitor/` as a DECLARED govkit entry — descriptor, conf, adopter, README — so
that every later unit's file has a home the deployer already knows about, and an adopter installs
the monitor by declaring its roots rather than by porting a script.

## 2. Scope (IN)

- **S1** — `tools/process-monitor/kit.toml`, the descriptor: id, home, scope, `version_from`, the
  `[[files]]` roles, the `[adopt]` and `[check]` argv, and the `[[gate_leg]]` rows this kit brings.
  **`version_from` pins at `adopt-process-monitor.sh`**, a file THIS unit ships, carrying a
  `KIT_PROCESS_MONITOR_VERSION=` line. Observed by AC1, AC7.
- **S2** — a `[[entry]]` row in `tools/govkit/registry.toml` pointing at that descriptor. Observed
  by AC1.
- **S3** — `.process-monitor.conf` at the repo root, holding every value the kit READS and nothing
  it could derive: the scope roots, the age ceiling, the spin rate, the reap mode, and the report
  throttle. **No scratch or temp root is among them** — see §4.
  Every key carries its reason in a comment beside it, as the sibling confs do. Observed by AC2.
- **S4** — `tools/process-monitor/adopt-process-monitor.sh`, with a `--check` mode that verifies
  wiring without repairing it. Observed by AC3.
- **S5** — `tools/process-monitor/README.md`, carrying a section stating what the kit does NOT
  check. Observed by AC4, AC6.
- **S6** — a `[[hole]]` declaration for the one value that ships unfillable: `PROCMON_ROOTS`, which
  is the adopter's own paths and cannot be seeded from this tree. Observed by AC5.

## 3. Non-goals (OUT)

- **No engine.** This unit ships declarations, an adopter and a README. `census.py`, `scope.py`,
  `classify.py`, `reap.py` and the hook belong to units 1 to 5, and this unit must land green
  WITHOUT them. `version_from` therefore may not name one — rev-1 did, which is what made this
  unit unlandable (D1).
- **No `KIT_PROCESS_MONITOR_VERSION` in a python module.** The constant lives in the shell
  adopter this unit ships. Unit 1 mints no version marker and needs none.
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
- **hands-off** `TOOL-aReapedSpinner-7` — the ABSENCE of a scratch root. That unit's legs are in
  scope by ancestry under unit 2's closure, so nothing here declares the directory they run in.
- **consumes-from** external — `tools/govkit/registry.toml` and its `[surface]` globs, which
  already claim `tools/*` and therefore already reach this directory.

## 4. Design

### Inventory

Identifiers this unit MINTS, each beside the cell that grades it. **Every row's `Where` names a
file THIS unit ships** — rev-1 pointed one at `census.py`, which unit 6 is forbidden to ship, and
`govkit.py:1194` reds on a `version_from` naming an absent file (D1).

| Name | Cell | Where |
|---|---|---|
| `PROCMON_ROOTS` | conf key, ungraded | `.process-monitor.conf` |
| `PROCMON_AGE_CEILING` | conf key, ungraded | `.process-monitor.conf` |
| `PROCMON_SPIN_RATE` | conf key, ungraded | `.process-monitor.conf` |
| `PROCMON_REAP_MODE` | conf key, ungraded | `.process-monitor.conf` |
| `PROCMON_THROTTLE_S` | conf key, ungraded | `.process-monitor.conf` |
| `KIT_PROCESS_MONITOR_VERSION` | `sh` assignment, ungraded | `adopt-process-monitor.sh` |

### The conf, and why each key is DECLARED rather than derived

`PROCMON_ROOTS` cannot be derived: an adopter's agent work lives where that adopter puts it, and the
scratchpad root is outside the repo entirely. `PROCMON_AGE_CEILING` cannot be derived either — this
repo's own bar has a 26-minute floor and a 3600 s `GATE_BOUND`, so a ceiling below those would kill
a healthy bar. `PROCMON_REAP_MODE` is the adopter's risk tolerance and is the one key whose default
is stated in §8. The remaining two are tuning.

**BLANK `PROCMON_ROOTS` is a REFUSAL, not an empty set.** An unfilled roots list would make the
scope fence match nothing, and a monitor that reports zero because it was never configured is
indistinguishable from a clean tree. That is why S6 declares it as a `[[hole]]`.

**WHAT THIS REPO'S OWN `PROCMON_ROOTS` MAY NOT CONTAIN, and AC8 grades it.** Not the shared temp
root, and not any ancestor of it. Measured: every Claude Bash-tool shell on this machine
carries an `export TEMP=` assignment naming the user's temp directory inside its argv, so a
substring root naming that directory admits every agent session in every repository on the box
(D11). Unit 7 needs the runner's legs reapable, and rev-2 answered that by declaring the scratch parent — which on
this node IS the temp root (`run-gates.sh:940` is a bare `mktemp -d` with no `TMPDIR` anywhere),
so the conf told its own author two opposite things and no criterion graded either (D16).
**Unit 2's rev-3 tree closure removes the need entirely**: a leg is in scope because its ancestry
is, so no scratch root is declared and the contradiction does not exist. The README states this,
because an adopter reading only the conf would reach for the obvious value.

### Files touched (estimate)

New: `tools/process-monitor/{kit.toml,adopt-process-monitor.sh,adopt-process-monitor.test.sh,README.md}`,
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

- **AC1** — When `govkit.py selfcheck` runs with the entry row landed and NO engine file present,
  it exits 0 and names `process-monitor` among the entries. Observed by `govkit.py`.
  Red when: a tracked file under the kit dir is claimed by no `[[files]]` rule, or the descriptor
  claims a path the kit does not ship — the assertion is bidirectional and both directions red.
- **AC2** — When `.process-monitor.conf` carries a BLANK `PROCMON_ROOTS`, `--check` exits non-zero
  naming that key. Observed by `adopt-process-monitor.test.sh`, arm `test_blank_roots_refuses`.
  Red when: a blank roots list is read as an empty set and `--check` passes, which would ship a
  monitor reporting a clean tree it never examined.
- **AC3** — When `adopt-process-monitor.sh --check` runs in this tree after adoption it exits 0;
  against a scratch tree missing the conf it exits non-zero naming the missing file, and that
  scratch tree is UNCHANGED afterwards. Observed by `adopt-process-monitor.test.sh`, arm
  `test_check_refuses_without_repairing`.
  Red when: `--check` repairs anything. It is the non-repairing mode by contract, the same split
  `.unattended.conf` records for `WIRING_CHECK`.
- **AC4** — When the descriptor declares a placeholder token the adopter never fills,
  `check-kit-placeholders.py` exits non-zero. Observed by `check-kit-placeholders.py`.
  Red when: the placeholder join is not on this unit's bar at all — rev-1 omitted the leg from §7
  while naming the checker as an observer (D2).
- **AC5** — When `govkit.py selfcheck` runs, the `procmon-roots` hole is reported as declared with
  a discharge probe. Observed by `govkit.py`.
  Red when: the hole is declared without one.
- **AC5b** — When the discharge probe is RUN against a blank `PROCMON_ROOTS`, it exits non-zero.
  Observed by `adopt-process-monitor.test.sh`, arm `test_roots_hole_probe_fails_when_blank`.
  Red when: the probe cannot fail. rev-2 folded this conjunct into AC5 with `govkit.py` as its
  only witness, and that command reports whether a probe is DECLARED, never whether anyone ran
  it — an assertion with no witness (D26).
- **AC8** — When the shipped `.process-monitor.conf` is read, no entry in `PROCMON_ROOTS` is an
  ancestor of the resolved system temp directory. A pure text assertion over the conf, gradable at
  `order 1`. Observed by `adopt-process-monitor.test.sh`, arm
  `test_shipped_roots_exclude_the_temp_root`.
  Red when: the prohibition is prose nobody grades (D16). **The counterpart — that the declared
  roots actually ADMIT this repo's own work — is unit 2's AC15**, because it needs a census and a
  closure and neither exists at `order 1`; rev-3 asked this unit for it and named a `--check-path`
  mode no unit ships (D36).
- **AC6** — When `README.md` is searched for the negative-scope heading, it is present and its
  section is non-empty. Observed by `adopt-process-monitor.test.sh`, arm
  `test_readme_states_what_it_does_not_check`.
  Red when: the section is absent. rev-1 witnessed this with `check-kit-placeholders.py`, whose own
  header says it grades DECLARATIONS and never opens a README — a criterion its own command could
  not show (D2).
- **AC7** — When the descriptor's `version_from` is resolved, the file it names is one this unit's
  `[[files]]` rules ship, and `govkit.py selfcheck` exits 0 with no engine file present. Observed
  by `adopt-process-monitor.test.sh`, arm `test_version_from_names_a_file_this_unit_ships`.
  Red when: `version_from` points into another unit's file, which reds `govkit selfcheck` and
  `kit version markers` on every bar until that unit lands (D1) — both are `subject: repo` with no
  guard, so there is no scoped run that hides it.

## 7. Gates

`govkit selfcheck` · `govkit refusal join` · `govkit acceptance matrix` · `kit placeholders (a declared token its adopter substitutes)` · `line length` · `dead-path carriers (deleted files still named)` · `hook destinations (every declared hook path ships)` · `kit version markers`

New arm: `tools/process-monitor/adopt-process-monitor.test.sh` · stages a missing conf, a blank
`PROCMON_ROOTS`, a descriptor claiming an absent path, a `version_from` naming a file this unit
does not ship, and a README with the negative-scope section removed · no assertion floor yet, this suite is new.

## 8. Open questions

- **F1 — what is the DEFAULT `PROCMON_REAP_MODE`?**
  Options: `report` (never kill without an explicit verb), `reap-orphans` (auto-kill only rows whose
  parent is dead AND which are past the age ceiling), `reap-all` (auto-kill every flagged row).
  RESOLVED (agent, 2026-09-08, delegated): `reap-orphans`. The owner's prompt names KILL as a
  required capability, so `report` under-delivers; `reap-all` would put an irreversible action on a
  single-sample heuristic, which template §9 forbids by default. `reap-orphans` is the class whose
  evidence is strongest — a process whose parent is dead and hours past its ceiling has no live
  claimant by construction.
  **Re-examined at rev-2 against D11 and HELD, but CONDITIONALLY.** The audit showed that
  `reap-orphans`, plus a naive substring root, plus the shared temp directory, reaps sibling agent
  sessions on the same machine — one such session in the live table already carries `ppid 1` and
  would grade ORPHAN. The mode is defensible only once unit 2 matches PROGRAM PATHS rather than raw
  strings, which is now that unit's AC8, and only while this repo's own roots exclude the temp root
  per §4. If either of those is relaxed, the default must fall back to `report`. `reap-all` stays
  reachable by declaration and is never this kit's default.

## 9. Revision log

- rev-4 · 2026-09-08 · AC8 · folded round 3 at its NON-CONVERGENT exit. D36: AC8 splits — the
  temp-root prohibition stays here as a text assertion gradable at `order 1`, and the
  roots-admit-this-repo half moves to unit 2 AC15, which has the census and the closure. rev-3
  folded round 2's suggested fix literally and reintroduced D1's class: an order-1 unit citing
  a mode shipped at order 3.
- rev-1 · 2026-09-08 · initial draft.
- rev-3 · 2026-09-08 · S3 · §3 Edges · §4 · AC5 · AC5b · AC8 · folded round 2. D16: the scratch
  root leaves S3 — unit 2's tree closure makes it unnecessary — and the temp-root prohibition
  gains AC8, which grades both halves of a fork that rev-2 left to prose. D26: AC5's
  "probe has been RUN" conjunct becomes AC5b with a real arm, since `govkit.py` can only
  report that a probe is declared. D23: the hook destination row moves to unit 5, which ships
  the file.
- rev-2 · 2026-09-08 · S1 · S5 · §3 · §4 · AC1 · AC4 · AC5 · AC6 · AC7 · §7 · §8 · folded
  spec-audit round 1. D1: `version_from` moved off `census.py` onto the shell adopter this unit
  ships, the version row with it, AC7 added to assert the resolution. D2: AC4 split — the
  placeholder join keeps its checker, the negative-scope section gets AC6 and a real arm, and the
  `kit placeholders` leg joins §7. D11: §4 gains the rule that this repo's roots may not name the
  shared temp directory.

## 10. Reuse audit

The seam this unit EXTENDS is `tools/govkit/registry.toml` and the descriptor grammar
`tools/drift-audit/kit.toml` demonstrates — `python tools/codebase-map/reuse_lookup.py "kill a hung
or idle background process and report it to the session"` returned the `govkit` dossier and
`registry.toml` as an affordance seam, and that is the one hit in the probe that was a real seam
rather than a name collision. The descriptor is copied in SHAPE from `drift-audit`, which is the closest structural sibling: one directory, one engine, a conf
owned elsewhere, a self-test withheld from adopters. **The `version_from` spelling is taken from
the sibling set rather than invented** — `codebase-map`, `drift-audit`, `hooks` and `lexicon` all
pin at a file the entry itself ships, and `agent-instructions` and `gate-lint` use the
`{ none = "<reason>" }` escape; rev-1 matched neither and named another unit's file. Verified
against source at BASE.

Recall terms used: `gate runner wall clock bound timeout kill children orphan process leg pool
watchdog GATE_WALL background subprocess reaper`
