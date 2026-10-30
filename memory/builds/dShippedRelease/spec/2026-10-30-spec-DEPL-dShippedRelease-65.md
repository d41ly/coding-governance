# DEPL-dShippedRelease-65 — every failure line of `check-kit-versions.sh` gets a home in `derive_version_findings` or a named retirement

**Status:** OPEN · rev-1 · 2026-10-30 · node d · Tier-2 · base f4597719 · streams deployer · order 2 · advances DEPL-dShippedRelease-32

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md](../build/2026-10-30-build-DEPL-dShippedRelease-1-agent-ledger.md) | journal | DEPL-dShippedRelease-1 DEPL-dShippedRelease-2 DEPL-dShippedRelease-3 DEPL-dShippedRelease-4 DEPL-dShippedRelease-5 DEPL-dShippedRelease-6 DEPL-dShippedRelease-7 DEPL-dShippedRelease-8 DEPL-dShippedRelease-9 DEPL-dShippedRelease-10 DEPL-dShippedRelease-11 DEPL-dShippedRelease-12 DEPL-dShippedRelease-13 DEPL-dShippedRelease-14 DEPL-dShippedRelease-15 DEPL-dShippedRelease-16 DEPL-dShippedRelease-17 DEPL-dShippedRelease-18 DEPL-dShippedRelease-19 DEPL-dShippedRelease-20 DEPL-dShippedRelease-21 DEPL-dShippedRelease-22 DEPL-dShippedRelease-23 DEPL-dShippedRelease-24 DEPL-dShippedRelease-25 DEPL-dShippedRelease-26 DEPL-dShippedRelease-27 DEPL-dShippedRelease-28 DEPL-dShippedRelease-29 DEPL-dShippedRelease-30 DEPL-dShippedRelease-31 DEPL-dShippedRelease-49 DEPL-dShippedRelease-50 DEPL-dShippedRelease-51 DEPL-dShippedRelease-52 DEPL-dShippedRelease-53 DEPL-dShippedRelease-54 DEPL-dShippedRelease-55 DEPL-dShippedRelease-56 DEPL-dShippedRelease-57 DEPL-dShippedRelease-58 DEPL-dShippedRelease-59 DEPL-dShippedRelease-60 DEPL-dShippedRelease-61 DEPL-dShippedRelease-62 DEPL-dShippedRelease-63 DEPL-dShippedRelease-64 DEPL-dShippedRelease-66 DEPL-dShippedRelease-67 DEPL-dShippedRelease-68 DEPL-dShippedRelease-69 DEPL-dShippedRelease-70 DEPL-dShippedRelease-71 DEPL-dShippedRelease-72 DEPL-dShippedRelease-73 DEPL-dShippedRelease-74 DEPL-dShippedRelease-75 DEPL-dShippedRelease-76 DEPL-dShippedRelease-77 DEPL-dShippedRelease-78 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 30 of `reviews/2026-10-30-review-DEPL-dShippedRelease-1-spec-audit-round1.md`,
HIGH, item H9. Unit 10 S8's fold lists arm 5's well-formedness, arm 5c's marker compare, the epoch
state, `dates` and the template marker, and S9 deletes `tools/check-kit-versions.sh`. The script
asserts more than that: the manifest format, a per-file no-marker rule, a constant restated across
scripts with its same-line marker, and the drift-audit harness versions. Those checks would vanish
with no signal, and unit 10's AC9 plants none of them.

## 2. Scope (IN)

- **S1** — The table of §4 is the disposition of every `kit-versions:` line at `f4597719`,
  re-derived at the pass by `grep -n 'kit-versions:' tools/check-kit-versions.sh`. Every line has a
  home or a reason. A line the table does not hold stops the pass. Observed by AC1.
- **S2** — `derive_marker_findings(root)` in `tools/govkit/govkit.py`, called by
  `derive_version_findings`, holds the per-file arms S8 lacks: `manifest-format`,
  `template-no-marker`, `restated-constant` and `workflow-meta`, each raising one finding that names
  the file. Observed by AC2, AC3, AC4, AC5.
- **S3** — Unit 10 §8 F5 is read with this table beside it, and AC9's "any of the five checks" reads
  every row of it. Observed by AC1.

## 3. Non-goals (OUT)

- The legs' retirement: DEPL-dShippedRelease-66.
- A spec-lint on retired scripts: the audit's left-shift item, which no clause of this build names.

### Edges

- **consumes-from** `DEPL-dShippedRelease-10` — `derive_version_findings`, `cmd_version` and the deletion S9 states; without the fold there is no arm to extend

## 4. Design

### Evidence

- `tools/check-kit-versions.sh:185` compares `MANIFEST-TEMPLATE.md`'s `kickoff-manifest: v` with `MANIFEST_FORMAT`; `:276` and `:318` fail a template with no marker; `:303` and `:307` hold
  `KIT_UNATTENDED_VERSION` and its same-line marker across scripts; `:361` and `:364` hold drift-audit `meta.version`.
- Arm 5c's `seen == 0` is per entry (`tools/govkit/govkit.py:2222-2290`, report id 30), so a template sibling losing its marker is not seen.

### The disposition

| Lines | What the line asserts | Home |
|---|---|---|
| `:23`, `:118` | the script locates itself and a python | retired with the script: `govkit.py version` is that python, and `:13602`'s usage names it |
| `:140`, `:164` | a declared carrier's marker, and a `meta.version` marker | arm 5c's compare in `derive_version_findings` |
| `:182`, `:185` | manifest seed against `MANIFEST_FORMAT` | `manifest-format` |
| `:191` | `KIT_MANIFEST_VERSION`'s same-line marker | `restated-constant` |
| `:200`, `:214`, `:219` | agent-cap constant, a population of zero, each carrier | arm 5c, its zero case kept as a finding |
| `:232`, `:235`, `:236`, `:244`, `:338`, `:348`, `:385`, `:396`, `:406` | one kit's constant against its named markers | arm 5c |
| `:264`, `:271`, `:276`, `:279` | memory-tree templates: constant, population, no marker, wrong marker | `template-no-marker` and arm 5c |
| `:298`, `:303`, `:307` | `KIT_UNATTENDED_VERSION` restated across four scripts | `restated-constant` |
| `:313`, `:318`, `:321` | unattended templates | `template-no-marker` and arm 5c |
| `:361`, `:364` | drift-audit harness `meta.version` | `workflow-meta` |
| `:411`, `:412` | the script's own clean and count lines | retired with the script: `cmd_version` prints its own |

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `derive_marker_findings` | function, `tools/govkit/govkit.py` | `py.function`, OK by `--suggest` at writing |
| `manifest-format`, `template-no-marker`, `restated-constant`, `workflow-meta` | finding names | none |

### Files touched (estimate)

- `tools/govkit/govkit.py`: S2
- `tools/govkit/selftest.py`: the plants of §6

## 5. Production-readiness checklist

- security — N/A — no new write path, stored-content class, outbound call or automation surface.
- perf / scale — reads the tracked templates and scripts once, under a second.
- error / empty / loading states — the criteria of §6 name each refused and empty state.
- observability — each state prints the line §2 names, on green and red.
- risks — a line added to the script between this spec and the pass has no row; S1's derivation
  stops the pass on it.
- testing — the criteria of §6 and the arm of §7.
- migration — N/A — the code it changes lands in this same build, so no installed state moves.
- user docs — N/A — no surface a reader of `help/` meets changes.

## 6. Acceptance criteria

- **AC1** — When `grep -c 'kit-versions:' tools/check-kit-versions.sh` runs at the pass, its count
  equals the lines the disposition table lists.
  Red when: a failure line has no row, so a check vanishes with the script.
  figure: the count is DERIVED at observation time; 33 is PINNED at `f4597719` by the same grep.
- **AC2** — When `python tools/govkit/govkit.py version` runs on a scratch copy whose
  `MANIFEST-TEMPLATE.md` marker is one value behind `MANIFEST_FORMAT`, it exits 1 naming
  `manifest-format`.
  Red when: an adopter can be seeded with a manifest its checker rejects.
- **AC3** — When `version` runs on a copy with one shipped template's marker deleted while a sibling
  keeps one, it exits 1 naming that template and `template-no-marker`.
  Red when: arm 5c's per-entry `seen` count hides the file.
- **AC4** — When it runs on a copy with a restated `KIT_UNATTENDED_VERSION` one value behind, it
  exits 1 naming `restated-constant`.
  Red when: the driver and its leg disagree about the kit with no finding.
- **AC5** — When it runs on a copy with `drift-audit-code.js`'s `meta.version` one value behind, it
  exits 1 naming `workflow-meta`.
  Red when: a harness tells an adopter the wrong version with no finding.

## 7. Gates

`recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `policy fixtures` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

New arm: tools/govkit/selftest.py · covers AC2 AC3 AC4 AC5 · one plant per row kind, its failing case `derive_marker_findings` cut out · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-30 · initial draft, promoted from review id 30 (HIGH, item H9) of the round-1 spec audit.

## 10. Reuse audit

The seam extended is DEPL-dShippedRelease-10's `derive_version_findings`, over arm 5c at
`tools/govkit/govkit.py:2222`.
`python tools/codebase-map/reuse_lookup.py "compare kit version markers with their constants"`
ranked `resolve_kit_dir`, `kit_rel` and `default_kits`, name-stem hits and no second marker reader.
The recall probe surfaced report item H9 and TOOL-aBoundedVerdict-29, which records that a marker
remedy once named three of five sites; both agree that the sites must be listed.

Recall terms used:
`python tools/memory-recall/query.py "which checks does check-kit-versions assert that a single version verb must carry" --terms "kit version markers epoch MANIFEST_FORMAT KIT_UNATTENDED_VERSION meta.version retired leg successor"`
