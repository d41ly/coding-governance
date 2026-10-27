# TOOL-dWellOiledMachine-64 — the moved hooks' message renderer and table moved with them into the runtime kit

**Status:** OPEN · rev-1 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 62 · advances TOOL-dWellOiledMachine-62

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dWellOiledMachine-64-deviation-641.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-64-deviation-641.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the spec audit of this build, round 1
(`memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-1-spec-audit.md`),
finding 2, item H1, at HIGH. TOOL-dWellOiledMachine-28 S1 moves `gate-guard.js`, `stop-guard.js`,
`stall-recorder.js` and `run-lease.js` into `tools/runtime/`, but not the renderer, message table and
instruction units TOOL-dWellOiledMachine-21 S5 gave the unattended kit, so every refusal of a moved
hook either fails to load its sibling `render-message.js` or reads no table, and under
`runtime.hook-failure` `closed` a crashed pack refuses every gated call. This unit moves the three
files' content with the hooks and re-points the render target, and proves each moved hook loads and
still names its rule.

## 2. Scope (IN)

- **S1** — The renderer moved. Where `tools/runtime/render-message.js` does not exist,
  `tools/unattended/render-message.js` moves there with `git mv`; where it exists, the unattended copy
  is deleted, since TOOL-dWellOiledMachine-21 S5 makes each kit's copy the same module over its own
  table. Either way no file under `tools/unattended/` is named `render-message.js`. Observed by AC1.
  **Readers:** by name: READER NOT IN TREE — the three hooks TOOL-dWellOiledMachine-28 moves into the runtime kit,
  each requiring its sibling renderer by `__dirname`; `tools/unattended/kit.toml`, whose file rows drop
  it. by value: NO VALUE READERS — the module is required, never read as data.
- **S2** — The instruction units moved. Every unit of `tools/unattended/instructions.toml` whose key
  is `hook.gate-guard.*`, `hook.stop-guard.*` or `hook.stall-recorder.*` moves, byte for byte, into
  `tools/runtime/instructions.toml` (which TOOL-dWellOiledMachine-12 S9 creates); a unattended file
  left holding no unit is deleted. Observed by AC2.
  **Readers:** by name: READER NOT IN TREE — the unattended kit's instruction file is TOOL-dWellOiledMachine-21's, unbuilt at HEAD. by value: `tools/playbook/render_playbook.py`, the renderer that reads the units.
- **S3** — The table re-rendered. The `messages` render scope's `[[target]]` row in
  `tools/playbook/renderers.toml` (TOOL-dWellOiledMachine-21 S4) names `tools/runtime/messages.json`
  for those units and no longer `tools/unattended/messages.json`, which is deleted once it renders
  empty; `render_playbook.py --render-scope messages` then writes the runtime table, and every
  unit's `enforced-by` names the runtime kit. Observed by AC2.
  **Readers:** by name: READER NOT IN TREE — the renderers table and the unattended message table are TOOL-dWellOiledMachine-21's, unbuilt at HEAD. by value: `tools/playbook/render_playbook.py`, which writes the table from the scope row.
- **S4** — The load probe. `tools/runtime/selftest.py --case hooks-load` requires each of the four
  moved modules from `tools/runtime/` with `node` and fails naming the module and the require that
  did not resolve; the population is every `*.js` under `tools/runtime/` whose source carries
  `require(path.join(__dirname`, refused when empty. Observed by AC3.
- **S5** — One moved refusal end to end: `gate-guard.js` run from `tools/runtime/` on a planted
  run-lease refusal ends its deny with `rule — run-lease` (TOOL-dWellOiledMachine-31 S3) and carries no
  `message … unavailable` line. Observed by AC4.

## 3. Non-goals (OUT)

- No change to the messages themselves, their slots or their rule names.
- No change to which hooks move: TOOL-dWellOiledMachine-28 S1's set stands.
- No renderer for a kit with no hook: the unattended kit carries none once its hooks moved.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-28` — the four moved hook modules in `tools/runtime/`, whose sibling renderer this unit supplies; without the move there is nothing to repair
- **consumes-from** `TOOL-dWellOiledMachine-21` — `render-message.js`, `messages.json`, the instruction units and the `messages` `[[target]]` row this unit moves
- **consumes-from** `TOOL-dWellOiledMachine-12` — `tools/runtime/instructions.toml`, the runtime kit's instruction file the units join

## 4. Design

### Evidence

- TOOL-dWellOiledMachine-21 lists `tools/unattended/render-message.js`, `messages.json` and
  `instructions.toml` in its Files touched (`spec-21.md:164-167`), and its S5 gives each hook kit one
  sibling module reading the kit's own table (`spec-21.md:57-61`).
- TOOL-dWellOiledMachine-28 S1 moves only the hooks, their fragments and suites
  (`spec-28.md:31-40`), and its Files touched names none of the three (`spec-28.md:276-297`).
- The hooks require siblings by `__dirname` (`tools/unattended/gate-guard.js:710`,
  `tools/unattended/stop-guard.js:84`, `tools/unattended/stall-recorder.js:40`), and each runs
  `main()` only under `require.main === module` (`gate-guard.js:795`, `stop-guard.js:248`,
  `stall-recorder.js:92`), so requiring one from a probe executes nothing.

### Files touched (estimate)

- `tools/runtime/render-message.js` (moved from `tools/unattended/`, or the unattended copy deleted)
- `tools/runtime/instructions.toml`, `tools/unattended/instructions.toml`
- `tools/runtime/messages.json` (rendered), `tools/unattended/messages.json` (deleted)
- `tools/playbook/renderers.toml`
- `tools/runtime/kit.toml`, `tools/unattended/kit.toml`
- `tools/runtime/selftest.py`

### Alternatives rejected

- **The moved hooks requiring `../unattended/render-message.js`.** A kit imports no sibling kit
  (TOOL-dGroundRules-1 §4), and an adopter may install the runtime kit at another prefix.

## 5. Production-readiness checklist

- security — a moved hook that loads refuses as before; S4 makes a broken require a red probe
  rather than a fail-closed outage.
- perf / scale — none: the same module and one table read per refusal.
- error / empty / loading states — the probe refuses an empty population.
- observability — S4 names the module and the require that failed.
- risks — a unit outside the three hooks' keys left in the unattended file keeps its own table; S2
  moves only the hook keys.
- testing — AC1 to AC4 and the arm in §7.
- migration — none for adopters beyond TOOL-dWellOiledMachine-28's upgrade steps: the files move
  inside one kit move.
- user docs — none: no user-visible text changes.

## 6. Acceptance criteria

- **AC1** — When `git ls-files tools/unattended | grep -cE 'render-message|messages.json'` runs after
  the unit, it prints `0`, and `git ls-files tools/runtime` lists `render-message.js`.
  Red when: the renderer or its table stays behind in the unattended kit.
- **AC2** — When `python tools/playbook/render_playbook.py --check-render --scope messages` runs, it
  exits 0, and `grep -c 'hook.gate-guard' messages.json` prints a non-zero count.
  Red when: the runtime table lacks a moved hook's units, or a table drifts from its units.
- **AC3** — When `node -e "require('./gate-guard.js')"` and its siblings run in the runtime kit's
  directory, each moved module loads and exits 0; with `render-message.js` renamed in a scratch copy
  it exits 1 naming `gate-guard.js` and `render-message.js`.
  Red when: a moved hook with an unresolvable require passes.
- **AC4** — When `node gate-guard.js` gets a planted run-lease refusal payload, its stderr ends with `rule — run-lease` and holds no
  `unavailable`.
  Red when: the refusal falls back to `message … unavailable` or loses its rule line.

## 7. Gates

`check-wiring self-test` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `govkit acceptance matrix` · `playbook render selftest` · `policy fixtures`

The unattended kit's self-test suites are waived for this build's landing (README rule 8).

New arm: tools/runtime/selftest.py · covers AC3 · the load case staged with the renderer renamed away · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit round 1, finding 2 (H1).

## 10. Reuse audit

The seam extended is TOOL-dWellOiledMachine-21's renderer and `messages` render scope, moved rather
than copied, and TOOL-dWellOiledMachine-28's `git mv` of the kit's hooks. The probe
`python tools/codebase-map/reuse_lookup.py "move a kit's hook message renderer with the hooks that require it"`
ranked `resolve_kit_dir`, `kit_rel` and `kit_dir` by the name stem `kit`, each a resolver of a kit's
directory and none a renderer or a mover; `render-message.js` is minted by TOOL-dWellOiledMachine-21
and unbuilt at this base, so no existing seam fits beyond those two units.

Recall terms used: `python tools/memory-recall/query.py "which kit owns the hook message table after
the unattended hooks move" --terms "hook message renderer render-message messages.json
instructions.toml unattended dissolved runtime kit move"`
