# TOOL-dMindYourWords-38 — check 7c2 resolves `{prefix}` in a leg's argv before it looks for the file

**Status:** DEFERRED · rev-1 · 2026-10-29 · node d · Tier-2 · base ccd1292e · streams tooling · order 4 · advances TOOL-dMindYourWords-18

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md) | journal | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 TOOL-dMindYourWords-22 TOOL-dMindYourWords-23 TOOL-dMindYourWords-24 TOOL-dMindYourWords-25 TOOL-dMindYourWords-26 TOOL-dMindYourWords-27 TOOL-dMindYourWords-28 TOOL-dMindYourWords-29 TOOL-dMindYourWords-30 TOOL-dMindYourWords-31 TOOL-dMindYourWords-32 TOOL-dMindYourWords-33 TOOL-dMindYourWords-34 TOOL-dMindYourWords-35 TOOL-dMindYourWords-36 TOOL-dMindYourWords-37 TOOL-dMindYourWords-39 TOOL-dMindYourWords-40 TOOL-dMindYourWords-41 TOOL-dMindYourWords-42 TOOL-dMindYourWords-43 TOOL-dMindYourWords-44 TOOL-dMindYourWords-45 TOOL-dMindYourWords-46 TOOL-dMindYourWords-47 TOOL-dMindYourWords-48 TOOL-dMindYourWords-49 TOOL-dMindYourWords-50 TOOL-dMindYourWords-51 TOOL-dMindYourWords-52 |
| [2026-10-29-build-TOOL-dMindYourWords-38-deviation-381.md](../build/2026-10-29-build-TOOL-dMindYourWords-38-deviation-381.md) | deviation | — |
| [2026-10-29-prompt-TOOL-dMindYourWords-38-promoted-fix-brief.md](../prompts/2026-10-29-prompt-TOOL-dMindYourWords-38-promoted-fix-brief.md) | research | TOOL-dMindYourWords-40 TOOL-dMindYourWords-48 TOOL-dMindYourWords-51 TOOL-dMindYourWords-52 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 7 of `reviews/2026-10-29-review-TOOL-dMindYourWords-30-to-37-spec-audit-round1.md`,
HIGH, which shares item H5 with id 33 (TOOL-dMindYourWords-39). Check 7c2 of `govkit selfcheck` keeps a
leg's argv element only when it is literally a tracked path, so a `{prefix}/…` argv element is never
read. Seven of the eight legs 7c2 grades spell their argv file that way, `lexicon naming predicates`
among them, so TOOL-dMindYourWords-34's widened population is graded on one leg and none of the legs
it was widened for. This unit resolves the token before the tracked-set test, as check 7c already does
for a guard.

## 2. Scope (IN)

- **S1** — The resolution. In check 7c2 (`tools/govkit/govkit.py:2606-2655`) each argv element is
  resolved with `resolve_prefix_token(a, _tr)`, the tool root 7c already derives at
  `tools/govkit/govkit.py:2559`, before it is tested against the tracked set, and the resolved path is
  the one read and named in the failure line. An element carrying no token passes unchanged, so the
  literal `straggler-guard arms` argv is read as before. Observed by AC1 and AC2.
- **S2** — The fixture spells the token. The 7c2 arms of `tools/govkit/selftest.py` (from `:6142`)
  spell their leg's argv as the literal `{prefix}/<kit>/<script>` the real manifest spells, never a
  pre-resolved path, so the arm and gov's manifest take the same branch. Observed by AC1.

## 3. Non-goals (OUT)

- A leg whose argv names no readable file at all: TOOL-dMindYourWords-39 (id 33) refuses it, so a
  resolution that still finds nothing cannot pass as a graded leg.
- The registry's `[[ledger]]` tables in the population: the minors batch TOOL-dMindYourWords-51.
- Resolving any other manifest token (`{memory_root}`, `{kit}`) in argv: no graded leg spells one
  (`tools/gate-legs.json` at base), and 7c resolves only `{prefix}` in a guard.
- Kit version constants: minted at landing (`tools/push-main.sh:26-31`), so this unit moves none.

### Edges

- **consumes-from** `TOOL-dMindYourWords-34` — S2's 7c2 over the widened root-file population; without it the resolved argv file is graded against the conf alone
- **hands-off** `TOOL-dMindYourWords-39` — the resolved argv read, over which that unit refuses a graded leg that names no readable file

## 4. Design

### Evidence

- 7c2 builds `argv_files = [a for a in (leg.get("argv") or []) if isinstance(a, str) and a in
  tracked_set]` with no resolution (`tools/govkit/govkit.py:2614-2615`), while 7c resolves each guard
  with `resolve_prefix_token(g, _tr)` (`:2566`), `_tr` being `derive_tool_root(root)` (`:2559`).
- `lexicon naming predicates` has argv `["python", "{prefix}/lexicon/lexicon.py"]`
  (`tools/gate-legs.json:1455-1458`).
- Simulated over gov's manifest at base 2026-10-29: of the 8 legs 7c2 grades, resolving the token makes
  all 8 argv files readable, and 5 of them name a declared root conf (`kit/dogfood doc parity`,
  `lexicon naming predicates`, `transition-audit arms`, `straggler-guard arms`, `govkit acceptance
  matrix`), each already in its leg's guard; unresolved, 1 file is read. PINNED 2026-10-29.

### The read

```
for a in leg.argv:
    rel = resolve_prefix_token(a, _tr)       # the 7c spelling, one call per element
    if rel in tracked_set: argv_files.append(rel)
```

### Inventory

Minted: none.

### Rollout

Live at landing, one order after TOOL-dMindYourWords-34. On gov's tree every newly read leg already
guards its conf, so the first bar after the pass stays green and prints a larger `root-conf readers`.

### Files touched (estimate)

- `tools/govkit/govkit.py`: S1
- `tools/govkit/selftest.py`: S2 and the arm of §7

### Alternatives rejected

- **Resolve at manifest load for every reader**: the manifest's token form is what 7c, the emitter
  and the adopter's render each read on purpose (`tools/govkit/govkit.py:4383-4392`); one resolution
  at 7c2's read is the seam 7c already uses.
- **Match the unresolved token against a tokenized tracked set**: a second spelling of the tracked set
  for one check.

## 5. Production-readiness checklist

- security — N/A — a classifier over the deployer's own manifest; no write path or surface.
- perf / scale — one string replace per argv element of eight legs.
- error / empty / loading states — an element that resolves to no tracked path is skipped as before;
  a leg left with no readable file is TOOL-dMindYourWords-39's refusal.
- observability — the note line `guarded bar legs graded <n> · root-conf readers <n>` now counts the
  prefixed legs, and a failure names the resolved argv path.
- risks — a leg whose resolved argv file names a root conf its guard lacks now reds where it passed;
  that is the check's purpose, and none does on gov's tree at base.
- testing — AC1, AC2 and the arm of §7.
- migration — none.
- user docs — N/A — govkit's internal check.

## 6. Acceptance criteria

- **AC1** — When `python <prefix>/govkit/govkit.py selfcheck` runs in a scratch gov tree whose one guarded
  bar leg spells its argv through the `{prefix}` token to the planted `<fixture>/demo/reader.py`, a
  tracked file naming `.demo.conf`, and whose guard lacks `.demo.conf`, it exits 1 printing `reads root conf .demo.conf` and the resolved argv path.
  Red when: the token is tested unresolved and the leg greens.
  fixture: a scratch gov tree under `%TEMP%/<short>` holding one kit, its descriptor declaring
  `[config] file = ".demo.conf"`, the planted break `resolve_prefix_token` cut from 7c2's loop.
- **AC2** — When `python tools/govkit/govkit.py selfcheck` runs on gov's own tree after the pass, it
  exits 0 and its note line prints `root-conf readers` followed by a number of at least 2.
  Red when: only the literal `straggler-guard arms` leg is read and the count prints 1.
  figure: DERIVED at observation from `tools/gate-legs.json`; 5 at base by the simulation in §4.

## 7. Gates

`govkit selfcheck` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `policy fixtures`

New arm: tools/govkit/selftest.py · covers AC1 · a scratch leg whose argv spells `{prefix}/demo/reader.py`, its failing case the resolution cut from 7c2, under which the leg greens without `.demo.conf` in its guard · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-29 · initial draft, promoted from review id 7 (HIGH, item H5, shared with id 33) of the
  round-1 audit of units 30 to 37.

## 10. Reuse audit

The seam is check 7c's own token resolution, `resolve_prefix_token` with `derive_tool_root`
(`tools/govkit/govkit.py:154`, `:180`, used at `:2566`), applied at 7c2's argv read, and the 7c2 arms
at `tools/govkit/selftest.py:6142-6250`. `python tools/codebase-map/reuse_lookup.py "resolve a manifest
token in a gate leg argv before reading the file"` ranked `resolve_prefix_token` among the generic
readers; it is the function this unit calls, so no new resolver is minted.

Recall terms used: `python tools/memory-recall/query.py "how does govkit classify a guard pathspec naming a root file a kit owns" --terms "root-conf guard pathspec class derive_root_confs 7c 7c2 selfcheck argv prefix token resolve"`
