# TOOL-dTendedCadence-72 — the close's "every carrier" version criterion reads its population from govkit's registry, never a glob over `tools/*/kit.toml`

**Status:** OPEN · rev-1 · 2026-11-01 · node a · Tier-1 · base f4597719 · streams tooling · order 23 · advances TOOL-dTendedCadence-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md) | journal | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 TOOL-dTendedCadence-35 TOOL-dTendedCadence-36 TOOL-dTendedCadence-37 TOOL-dTendedCadence-38 TOOL-dTendedCadence-39 TOOL-dTendedCadence-40 TOOL-dTendedCadence-41 TOOL-dTendedCadence-42 TOOL-dTendedCadence-43 TOOL-dTendedCadence-44 TOOL-dTendedCadence-45 TOOL-dTendedCadence-46 TOOL-dTendedCadence-47 TOOL-dTendedCadence-48 TOOL-dTendedCadence-49 TOOL-dTendedCadence-50 TOOL-dTendedCadence-51 TOOL-dTendedCadence-52 TOOL-dTendedCadence-53 TOOL-dTendedCadence-54 TOOL-dTendedCadence-55 TOOL-dTendedCadence-56 TOOL-dTendedCadence-57 TOOL-dTendedCadence-58 TOOL-dTendedCadence-59 TOOL-dTendedCadence-60 TOOL-dTendedCadence-61 TOOL-dTendedCadence-62 TOOL-dTendedCadence-63 TOOL-dTendedCadence-64 TOOL-dTendedCadence-65 TOOL-dTendedCadence-66 TOOL-dTendedCadence-67 TOOL-dTendedCadence-68 TOOL-dTendedCadence-69 TOOL-dTendedCadence-70 TOOL-dTendedCadence-71 TOOL-dTendedCadence-73 TOOL-dTendedCadence-74 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 24 of `reviews/2026-11-01-review-TOOL-dTendedCadence-49-to-59-spec-audit-round1.md`,
HIGH, item H6. Unit 59 S37 and AC35 draw the version carriers from `git grep "^version_from = { file"
-- 'tools/*/kit.toml'`, 16 rows (spec-59 §4 Evidence, AC35). govkit's registry holds four more that
declare a `file`, in `tools/govkit/entries/*.kit.toml`: `check-wiring.sh`'s
`KIT_CHECK_WIRING_VERSION`, `skills/session-kickoff/manifest-check.sh`'s `KIT_MANIFEST_VERSION`, the
agents template's `governance-template: v` marker and `settings-merge.py`'s
`KIT_SETTINGS_MERGE_VERSION`. A hand-bump of any of them passes a criterion that claims "every
carrier", and `manifest-check.sh` is a file this build's commits touch. This unit reads the population
where the lander's own mint reads it.

## 2. Scope (IN)

- **S1** — The population. Unit 59 AC35's carrier set is every entry of `read_descriptors(root,
  load_registry(root), Report())` (`tools/govkit/govkit.py:13238`, `:247`) whose `version_from`
  declares a `file`, its carrier path the entry's `home` joined to that `file`, as
  `write_version_carriers` resolves `src` (`govkit.py:842-843`), and its pattern the entry's
  `pattern`. Graded over TOOL-dTendedCadence-58's population, as AC35 already grades. Observed by AC1.
- **S2** — The floor. AC35's "at least sixteen carriers" reads "at least the registry's count of
  entries declaring a `file`", 20 at base, DERIVED by S1's probe. Observed by AC1.
- **S3** — The in-place text. Spec-59 S37, its §4 Evidence sentence on the sixteen rows and AC35 are
  corrected to S1 and S2, a rev bump with a §9 line naming review id 24. Observed by AC2.

## 3. Non-goals (OUT)

- The Skill's byte measure in AC35's second half: item M6 of the same report, TOOL-dTendedCadence-74.
- Changing govkit: the registry is read, never written.

### Edges

- **consumes-from** `TOOL-dTendedCadence-59` — S37 and AC35, whose carrier population this unit reads from the registry
- **consumes-from** `TOOL-dTendedCadence-58` — the population of the build's own commits, over which the carriers are graded

## 4. Design

```python
import pathlib, sys; sys.path.insert(0, "tools/govkit"); import govkit as g
root = pathlib.Path(".").resolve()
descs = g.read_descriptors(root, g.load_registry(root), g.Report())
carriers = [(rid, f"{d['home'].rstrip('/')}/{d['version_from']['file']}" if d.get("home")
             else d["version_from"]["file"], d["version_from"]["pattern"])
            for rid, (d, _p) in descs.items() if "file" in (d.get("version_from") or {})]
```

Each carrier's added lines matching its pattern are then listed over unit 58's population, as AC35
states. Probe at writing, 2026-11-01: `len(descs)` 30, `len(carriers)` 20, no problem reported, the
four `entries/` carriers among them.

### Files touched (estimate)

- `memory/builds/dTendedCadence/spec/2026-11-01-spec-TOOL-dTendedCadence-59.md`: S3

## 5. Acceptance criteria

- **AC1** — When the probe of §4 runs at the close, it lists at least 20 carriers, `check-wiring`,
  `kickoff-manifest`, `playbook` and `settings-merge` among them, and no carrier's pattern matches an
  added line over TOOL-dTendedCadence-58's population; with a staged commit in that population
  hand-bumping `KIT_MANIFEST_VERSION` in `skills/session-kickoff/manifest-check.sh`, the probe lists
  that line.
  Red when: a registered carrier outside `tools/*/kit.toml` is hand-bumped and nothing lists it.
  figure: 20 is DERIVED by the probe at observation time; at base it printed 20.
- **AC2** — When `grep -n "tools/\*/kit.toml" 2026-11-01-spec-TOOL-dTendedCadence-59.md` runs in the
  spec folder, no hit sits in S37 or AC35, and `grep -c "read_descriptors"` over the same file prints
  at least 1.
  Red when: the criterion still draws its population from a glob.

## 6. Gates

`memory hygiene` · `recall floor` · `recall floor arms`

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 24 (HIGH, item H6) of the round-1 spec
  audit of units 49 to 59.

## 9. Reuse audit

The seam is govkit's registry reader, `load_registry` and `read_descriptors`, and the carrier path
rule of `write_version_carriers` (`tools/govkit/govkit.py:247`, `:801-843`, `:13238`), which the
lander's mint reads. `python tools/codebase-map/reuse_lookup.py "list every kit version carrier from
the registry"` ranked name stems only, `resolve_kit_dir`, `kit_rel`, `kit_dir` and `default_kits`, and
missed the registry reader, so the seam is named here from source.

Recall terms used: `python tools/memory-recall/query.py "which files carry a kit's version constant"
--terms "version_from carrier registry entries govkit read_descriptors load_registry hand-bump mint
KIT_MANIFEST_VERSION"`
