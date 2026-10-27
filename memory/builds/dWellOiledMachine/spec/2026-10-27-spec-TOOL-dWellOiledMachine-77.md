# TOOL-dWellOiledMachine-77 — a session is bound as the owner only when no machine launcher started it

**Status:** DEFERRED · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 18 · advances TOOL-dWellOiledMachine-62

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dWellOiledMachine-77-deviation-771.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-77-deviation-771.md) | deviation | — |
| [2026-10-27-review-TOOL-dWellOiledMachine-63-spec-audit.md](../reviews/2026-10-27-review-TOOL-dWellOiledMachine-63-spec-audit.md) | spec-audit | TOOL-dWellOiledMachine-72 TOOL-dWellOiledMachine-68 TOOL-dWellOiledMachine-69 TOOL-dWellOiledMachine-71 TOOL-dWellOiledMachine-67 TOOL-dWellOiledMachine-73 TOOL-dWellOiledMachine-63 TOOL-dWellOiledMachine-78 TOOL-dWellOiledMachine-74 TOOL-dWellOiledMachine-70 TOOL-dWellOiledMachine-66 TOOL-dWellOiledMachine-75 TOOL-dWellOiledMachine-76 TOOL-dWellOiledMachine-65 TOOL-dWellOiledMachine-64 TOOL-dWellOiledMachine-79 |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the spec audit of this build, round 1
(`memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-1-spec-audit.md`),
finding 63, item H14, at HIGH. TOOL-dWellOiledMachine-12 S3 binds `owner: yes` for every session whose
launch environment lacks `GOV_ACT`, which includes the node tick's headless
`claude -p --resume … <payload>` (`tools/unattended/resume-tick.sh:385`). A machine-written payload
is then recorded as an owner intake, and TOOL-dWellOiledMachine-27 S3 ratifies it; deny by default is
inverted. This unit marks every machine launch in the tree and binds `owner: yes` only for a session
no machine launcher started.

## 2. Scope (IN)

- **S1** — The bind rule. `bind` (`tools/runtime/session_binding.py`, 12 S3) sets `owner` to the act
  id when the launch environment carries `GOV_ACT`; else to `machine`, with `act: none`, when it
  carries `GOV_SESSION_KIND` of any value; else `owner: yes`. The record's `owner` field (12 S1) gains
  the value `machine`. Observed by AC1, AC2.
  Every reader of `owner` compares it with `yes` or reads an act id, and none spells `machine`:
  `intake.py hook` (TOOL-dWellOiledMachine-4 S4)
  writes only for `yes`; the record door's owner path (TOOL-dWellOiledMachine-58 S5) admits only
  `yes`; `scratch-guard.js`'s orientation check (TOOL-dWellOiledMachine-38 S4) applies the card rule to
  `yes` and exempts every other value as an act's, so a `machine` session is exempt as an act is.
- **S2** — The tick's launch marked. The launcher script `resume-tick.sh` writes before its
  `claude -p --resume` line (`:385`) exports `GOV_SESSION_KIND=machine`, so the tick's headless resume
  binds `machine` in the window before TOOL-dWellOiledMachine-6 S11 moves that launch onto
  `launch_act`. Observed by AC2.
- **S3** — The launcher's marker kept. `launch_act` already sets `GOV_SESSION_KIND=act`
  (TOOL-dWellOiledMachine-10 S7); TOOL-dWellOiledMachine-37's environment allowlist must keep it after
  its filter, which this unit hands to that unit (§3 Edges). Observed by AC3.
- **S4** — The security line corrected. 12 §5 prices only `GOV_ACT`; spec 12 takes a rev bump at this
  unit's pass stating S1's rule and its limit, its §9 line naming this unit and finding 63. The limit:
  a headless session a person starts by hand, outside every launcher, binds `owner: yes`, since that
  person is the owner. Observed by AC4.

## 3. Non-goals (OUT)

- No terminal test: a SessionStart hook has no terminal, so `[ -t 2 ]` would bind every owner session
  as a machine (the skeptic's reading of finding 63).
- No harness-reported print-mode fact: the launchers in this tree are the population, and each is
  marked.
- No change to act bindings or to `GOV_ACT`.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-12` — `bind` and the binding record's `owner` field, whose rule this unit narrows
- **consumes-from** `TOOL-dWellOiledMachine-10` — S7's `GOV_SESSION_KIND=act` set by `launch_act`, the marker S1 reads
- **hands-off** `TOOL-dWellOiledMachine-37` — `GOV_SESSION_KIND` and `GOV_ACT`, which `derive_launch_env`'s allowlist must keep after its filter so an act launch never binds `owner: yes`
- **hands-off** `TOOL-dWellOiledMachine-90` — the `owner: machine` value, given an explicit arm in each reader of `owner` (finding 38)

## 4. Design

### Evidence

- 12 S3 sets `owner: yes` and `act: none` whenever `GOV_ACT` is absent (`spec-12.md:45-47`).
- `resume-tick.sh:385` writes `claude -p --resume %q --dangerously-skip-permissions --max-turns %q %q`
  into a launcher script with no `GOV_ACT` and no other marker (`tools/unattended/resume-tick.sh:380-386`).
- `git grep -n "claude -p"` over `tools`, `skills` and `.githooks` finds that line as the only
  hand-built headless launch outside tests; TOOL-dWellOiledMachine-1 S2's `launch_act` is the other
  launcher, and 10 S7 makes it set `GOV_SESSION_KIND=act` (`spec-10.md:77-80`).

### Files touched (estimate)

- `tools/runtime/session_binding.py`: S1, its fixture plant
- `tools/unattended/resume-tick.sh`: S2
- `memory/builds/dWellOiledMachine/spec/2026-10-26-spec-TOOL-dWellOiledMachine-12.md` (S4's rev bump)

### Alternatives rejected

- **Binding a marked session with no act as `owner: yes`.** It keeps the defect for every machine
  launch that carries no act, the tick's resume first among them.

## 5. Production-readiness checklist

- security — deny by default restored: only an unmarked, hand-started session is the owner, and every
  in-tree machine launcher is marked.
- perf / scale — none.
- error / empty / loading states — an empty `GOV_SESSION_KIND` still marks a machine launch.
- observability — the binding names `owner: machine`.
- risks — a new launcher added without the marker binds `owner: yes`; S4 states the population, and
  `launch_act` is the one route TOOL-dWellOiledMachine-6 S11 and -28 move the rest onto.
- testing — AC1 to AC4 and the arms in §7.
- migration — none: existing bindings keep their value until the session rebinds.
- user docs — `help/runtime.md`'s session-binding section names `machine`.

## 6. Acceptance criteria

- **AC1** — When `python session_binding.py --fixture --plant resume-tick-env` runs `bind` under the
  environment the tick's launcher script exports, the binding reads `owner: machine` and `act: none`.
  Red when: it binds `owner: yes`, as 12 S3 alone binds it.
- **AC2** — When the same plant runs with no `GOV_SESSION_KIND` and no `GOV_ACT`, the binding reads
  `owner: yes`; with `GOV_ACT=a-1` it reads `owner: a-1`; and `grep -n "GOV_SESSION_KIND=machine" tools/unattended/resume-tick.sh`
  prints the export.
  Red when: an interactive start loses the owner, or the tick's launcher carries no marker.
- **AC3** — When `launch_act` builds an act launch in TOOL-dWellOiledMachine-1's fixture, its returned
  environment carries `GOV_SESSION_KIND=act`.
  Red when: an act launch carries no marker.
- **AC4** — When `grep -n "TOOL-dWellOiledMachine-77" 2026-10-26-spec-TOOL-dWellOiledMachine-12.md`
  runs over spec 12, its §9 carries the rev line and its §5 states the rule and its limit.
  Red when: spec 12 still prices only `GOV_ACT`.

## 7. Gates

`unattended kit gate` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms`

The unattended kit's self-test suites are waived for this build's landing (README rule 8).

New arm: tools/runtime/session_binding.py · covers AC1 AC2 · the tick-environment plant staged against a `bind` that reads only `GOV_ACT` · none

## 8. Open questions

- **F1 — What marks a machine launch?** (a) `GOV_SESSION_KIND`, which `launch_act` already sets and
  the tick's launcher gains; (b) a harness-reported print-mode fact the spike would measure; (c) a
  terminal test. (c) binds every owner session as a machine, since a SessionStart hook has no
  terminal; (b) needs a measurement no unit owns and still misses a machine launch that does not use
  print mode. (a) reuses 10 S7's marker. Rung 3. RESOLVED (agent, 2026-10-27, delegated): (a).
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit round 1, finding 63 (H14).
- rev-2 · 2026-10-27 · §3 · Edges: the reciprocal of each edge the spec audit of the round-1
  promotions' promoted units declare on this unit, mirrored from TOOL-dWellOiledMachine-90.

## 10. Reuse audit

The seam reused is TOOL-dWellOiledMachine-10 S7's launch marker `GOV_SESSION_KIND`, read by `bind`
beside `GOV_ACT`, and the tick's existing launcher script. The probe
`python tools/codebase-map/reuse_lookup.py "bind a headless machine session as not the owner"` ranked
`note`, `extract_session`, `owners_of` and `read_bindings` by name stem, none a launch marker, so no
other seam fits.

Recall terms used: `python tools/memory-recall/query.py "how is a session bound as owner or act at
session start" --terms "session binding owner GOV_ACT GOV_SESSION_KIND headless resume tick launch
marker machine"`
