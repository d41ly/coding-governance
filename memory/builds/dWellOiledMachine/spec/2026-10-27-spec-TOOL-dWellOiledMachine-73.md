# TOOL-dWellOiledMachine-73 — the orientation card stored through the runtime kit where it resolves, and at its legacy home where it does not

**Status:** DEFERRED · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 19 · advances TOOL-dWellOiledMachine-62

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dWellOiledMachine-73-deviation-731.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-73-deviation-731.md) | deviation | — |
| [2026-10-27-review-TOOL-dWellOiledMachine-63-spec-audit.md](../reviews/2026-10-27-review-TOOL-dWellOiledMachine-63-spec-audit.md) | spec-audit | TOOL-dWellOiledMachine-72 TOOL-dWellOiledMachine-68 TOOL-dWellOiledMachine-69 TOOL-dWellOiledMachine-71 TOOL-dWellOiledMachine-67 TOOL-dWellOiledMachine-77 TOOL-dWellOiledMachine-63 TOOL-dWellOiledMachine-78 TOOL-dWellOiledMachine-74 TOOL-dWellOiledMachine-70 TOOL-dWellOiledMachine-66 TOOL-dWellOiledMachine-75 TOOL-dWellOiledMachine-76 TOOL-dWellOiledMachine-65 TOOL-dWellOiledMachine-64 TOOL-dWellOiledMachine-79 |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the spec audit of this build, round 1
(`memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-1-spec-audit.md`),
finding 50, item H10, at HIGH. TOOL-dWellOiledMachine-38 S2 stores the card through the runtime kit's
`session_binding.py put-card`, while `tools/govkit/entries/kickoff-manifest.kit.toml` keeps
`requires = []` and no resolver or absent-kit behaviour is specified. An adopter without the optional
runtime kit then writes no card, and 38 S4's route gate refuses every routed write for every session.
This unit names the resolver and the behaviour without the kit: the legacy card home, which 38 S4's
gate already reads.

## 2. Scope (IN)

- **S1** — The resolver. `manifest-check.sh` finds the runtime kit through its inline
  `resolve_kit_dir` (`skills/session-kickoff/manifest-check.sh:791`), home `runtime`, anchor
  `session_binding.py`, once per run, as it already finds sibling kits. Observed by AC1.
- **S2** — The fallback. When the runtime kit does not resolve, `--card --write`, `--card --append`,
  `--card --replay`, `--card --check` and `--card --path` act on the legacy card file
  `<git-common-dir>/orientation/<sid>.md` byte for byte as before TOOL-dWellOiledMachine-38, and the
  first such write in a run prints one line `card — legacy home · runtime kit not installed`. Where the
  kit resolves, 38 S2's route through `put-card` and `read --card` stands. Observed by AC1, AC2.
- **S3** — The retirement narrowed. 38 S1 retires `<git-common-dir>/orientation/<sid>.md` as a write
  home; after this unit it is retired only where the runtime kit is installed, and spec 38 takes a
  rev bump at this unit's pass saying so, its §9 line naming this unit and finding 50. Observed by AC3.
  **Readers:** by name: `skills/session-kickoff/manifest-check.sh`, the card's writer, and READER NOT IN TREE for spec 38's runtime-kit reader, unbuilt. by value: `tools/hooks/scratch-guard.js` (`readCard`), which reads the card where it stays.
- **S4** — The descriptor states it. `tools/govkit/entries/kickoff-manifest.kit.toml` keeps
  `requires = []` and its comment names the optional reach: the runtime kit, resolved at run time,
  with S2's fallback. Observed by AC3.

## 3. Non-goals (OUT)

- No `requires = ["runtime"]`: §8 F1.
- No change to the card's derivations, cells or cap.
- No change to 38 S3 and S4: the gate already reads a binding first and a legacy card otherwise.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-38` — S2's card store through `put-card` and S4's gate reading a binding or a legacy card, which this unit's fallback joins
- **consumes-from** `TOOL-dWellOiledMachine-12` — `session_binding.py`, the anchor S1 resolves the runtime kit by
- **hands-off** `TOOL-dWellOiledMachine-90` — the card fallback on any `put-card` failure and the held suite's guard (findings 45, 62)

## 4. Design

### Evidence

- `tools/govkit/entries/kickoff-manifest.kit.toml:12` reads `requires = []`.
- `manifest-check.sh` carries the resolver inline (`:785-836`) and already asks it for sibling kits
  (`:859`).
- TOOL-dWellOiledMachine-1 S1 ships the runtime kit with `requires = ["policy"]`, an optional kit.
- The policy fixtures plant `--card --write` in a scratch repository with no runtime kit
  (`tools/policy/check_policy.py:3438-3441`).

### Files touched (estimate)

- `skills/session-kickoff/manifest-check.sh`: S1, S2
- `skills/session-kickoff/manifest-check.test.sh`: the no-kit case
- `tools/govkit/entries/kickoff-manifest.kit.toml`: S4's comment
- `memory/builds/dWellOiledMachine/spec/2026-10-26-spec-TOOL-dWellOiledMachine-38.md` (S3's rev bump)

### Alternatives rejected

- **`requires = ["runtime"]`.** §8 F1.
- **Refusing `--card --write` with a named line when the kit is absent.** A refused card leaves 38 S4
  refusing every routed write, the outage this unit exists to prevent.

## 5. Production-readiness checklist

- security — the route gate keeps its deny for a session with neither a binding nor a card; S2 only
  restores the card the gate reads.
- perf / scale — one resolver call per run.
- error / empty / loading states — S2's one line says which home was used.
- observability — `--card --path` prints the home in use.
- risks — two homes exist across adopters; a node gains the binding home by installing the kit, and
  38's migration moves nothing back.
- testing — AC1 to AC3 and the arm in §7.
- migration — none: an adopter without the kit keeps today's home.
- user docs — `manifest-check.sh`'s `--card` usage text names the fallback;
  `skills/session-kickoff/SKILL.md` is not touched.

## 6. Acceptance criteria

- **AC1** — When `bash skills/session-kickoff/manifest-check.sh --card --write --session <sid>` runs in
  a scratch repository with no runtime kit, the card lands at `<git-common-dir>/orientation/<sid>.md`,
  the run prints `card — legacy home`, and `--card --path` prints that file.
  Red when: the write fails or writes nowhere because `put-card` cannot be found.
- **AC2** — When a routed write is attempted in that repository's session after AC1's card carries a
  `## route` naming a buildable unit, `scratch-guard.js` allows it; with the runtime kit installed the
  card lands in the binding and the same write is allowed.
  Red when: a routed write is refused for want of a card the session wrote.
- **AC3** — When `grep -n "legacy home" skills/session-kickoff/manifest-check.sh tools/govkit/entries/kickoff-manifest.kit.toml`
  runs, both name the fallback, and spec 38's §9 carries the rev line naming this unit.
  Red when: the descriptor or the engine leaves the fallback unstated.

## 7. Gates

`manifest-check self-test` · `scratch-guard self-test` · `lexicon naming predicates` · `policy fixtures` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `memory hygiene` · `recall floor`

New arm: skills/session-kickoff/manifest-check.test.sh · covers AC1 AC2 · the no-kit card write staged against a store that calls `put-card` unconditionally · none

## 8. Open questions

- **F1 — What does the card store do without the runtime kit?** (a) Fall back to the legacy card home,
  which 38 S4's gate already reads; (b) `requires = ["runtime"]` on the kickoff engine; (c) refuse the
  write with a named line. (b) makes an optional kit mandatory for every adopter of the kickoff
  engine, a new install obligation and a kit-contract change (M3 veto 2); (c) refuses every routed
  write on such an adopter, the defect itself. Rung 3, the only survivor. RESOLVED (agent,
  2026-10-27, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit round 1, finding 50 (H10).
- rev-2 · 2026-10-27 · §3 · Edges: the reciprocal of each edge the spec audit of the round-1
  promotions' promoted units declare on this unit, mirrored from TOOL-dWellOiledMachine-90.

## 10. Reuse audit

The seam reused is `manifest-check.sh`'s inline `resolve_kit_dir` (`:791`), the engine's one
sibling-kit reach, and the card writer it already holds for the legacy home. The probe
`python tools/codebase-map/reuse_lookup.py "store the orientation card when the runtime kit is absent"`
ranked `resolve_kit_dir`, `kit_rel`, `kit_dir` and `resolve_kit_file`, the first being the resolver
S1 uses; no other seam fits.

Recall terms used: `python tools/memory-recall/query.py "where is the orientation card written without
the runtime kit" --terms "orientation card session binding put-card kickoff manifest runtime kit
requires fallback legacy"`
