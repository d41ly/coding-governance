# KICK-dKeptSession-40 — the preset store a recorded input of the JSON mirror, so a changed preset reads the mirror stale

**Status:** DEFERRED · rev-2 · 2026-10-26 · node a · Tier-2 · base 462d20f3 · streams kickoff · order 4 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-30-promoted-fix-return.md](../build/2026-10-26-build-KICK-dKeptSession-30-promoted-fix-return.md) | research | KICK-dKeptSession-28 KICK-dKeptSession-36 KICK-dKeptSession-43 KICK-dKeptSession-44 |
| [2026-10-26-build-KICK-dKeptSession-40-deviation-401.md](../build/2026-10-26-build-KICK-dKeptSession-40-deviation-401.md) | deviation | — |
| [2026-10-26-prompt-KICK-dKeptSession-30-promoted-fix-brief.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-30-promoted-fix-brief.md) | research | KICK-dKeptSession-28 KICK-dKeptSession-36 KICK-dKeptSession-43 KICK-dKeptSession-44 |
| [2026-10-26-review-KICK-dKeptSession-30-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-30-spec-audit.md) | spec-audit | KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-32 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-41 KICK-dKeptSession-44 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build's spec set
(`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md`)
confirmed finding **id 47 at HIGH**, report item **H7**, which no other id shares.

`KICK-dKeptSession-2`'s `read_preset_value` reads `tools/policy/presets.toml` as a resolution
input, and its §3 says the mirror "carries the preset's values without an edit". dGroundRules'
mirror records only the policy file's, the catalogue's and each `LEGACY_INPUTS` file's blob ids, and
`policy-mirror.js` reads it FRESH while those ids hold. A change to `presets.toml` without a
re-render therefore leaves every hook reading the old values, scratch-guard's `actions.free`,
agent-cap and mail-notice among them, while `policy.py get` returns the new ones. This unit records
the store as a mirror input. It repairs `KICK-dKeptSession-2` and builds one step after it
(order 4).

## 2. Scope (IN)

- **S1** — id 47. The kit path. `derive_kit_rel(name)` in `tools/policy/policy.py` is
  `derive_catalogue_rel`'s body with the file name a parameter, and `derive_catalogue_rel()` becomes
  `derive_kit_rel(CATALOGUE)`, so the kit's repository-relative spelling lives once. Observed by AC1.
- **S2** — id 47. The input. `derive_mirror_inputs()` returns `LEGACY_INPUTS` plus
  `derive_kit_rel("presets.toml")`; `render_mirror`'s `legacy_blobs` and the freshness check's input
  walk (dGroundRules' `policy.py` lines 882 and 1400 at `3c8c4718a`) both iterate it, so the
  mirror records the store's blob and `policy-mirror.js`, which reads every key of `legacy_blobs`,
  compares it with no edit. Observed by AC2 and AC3.
- **S3** — id 47. `KICK-dKeptSession-2` §3's JS-mirror bullet, "carries the preset's values without
  an edit", is superseded by name here and answered in that unit's acceptance ledger with AC2's
  output. Observed by AC2.

## 3. Non-goals (OUT)

- `KICK-dKeptSession-20`'s scenario step: it answers `None` with no build, and `policy.json` is
  rendered per revision and never per build, so the mirror never reads a scenario (the skeptic's
  corrected fix leaves unit 20 unchanged).
- The mirror's render and the JS reader's logic: dGroundRules', unchanged but for S2's input list.
- The report's left-shift fixture, every file the resolution order reads recorded as an input:
  AC3 is that observation for the one input this build adds.

### Edges

- **consumes-from** `KICK-dKeptSession-2` — `read_preset_value`'s read of `presets.toml`, the resolution input this unit records in the mirror (id 47)
- **hands-off** `KICK-dKeptSession-49` — the store recorded under `legacy_blobs`, which that unit makes the JS reader expect rather than discover (id 22)
- **hands-off** `KICK-dKeptSession-50` — `derive_mirror_inputs` and the mirror's `legacy_blobs`, whose upgrade from a pre-unit mirror that unit observes (id 48)
- **hands-off** `KICK-dKeptSession-56` — `.governance/policy.json` as a write, §7's legs and the README's mirror text, the batch's S29, S25 and S42 (ids 40, 34, 41)

## 4. Design

### Evidence

- dGroundRules' `policy.py` at `3c8c4718a`: "A unit adding a resolution input adds its path here",
  `LEGACY_INPUTS = (LEGACY_FANOUT,)` (lines 809-813); `derive_catalogue_rel` runs `git rev-parse
  --show-prefix` from the kit (:826-834); `render_mirror` records `catalogue_blob`, `legacy_blobs`
  and `policy_blob` (:881-882).
- `policy-mirror.js` reads `Object.keys(doc.legacy_blobs)` and marks the mirror stale when any
  recorded id differs from the blob at the landed revision (lines 111-118 at `3c8c4718a`).
- `LEGACY_INPUTS` holds repository-relative paths, while `presets.toml` sits in the kit, so its path
  is the kit prefix plus the name, as the catalogue's is.

### Inventory

| Identifier | Kind | Home |
|---|---|---|
| `derive_kit_rel`, `derive_mirror_inputs` | functions | `tools/policy/policy.py` |
| `mirror-presets-stale` | fixture case | `tools/policy/check_policy.py` |

### Migration

A mirror rendered before this unit carries no `presets.toml` entry, so `policy-mirror.js` reads it
stale once and the reader answers; the next `policy.py mirror --write` records the entry.

### Files touched (estimate)

- `tools/policy/policy.py`: S1 and S2
- `tools/policy/check_policy.py`: the `mirror-presets-stale` case

### Alternatives rejected

- **The store's path as a literal in `LEGACY_INPUTS`.** The kit's prefix in a repository is not known
  at import time; a literal would name the wrong path in an adopter.
- **Rendering the mirror on every preset edit.** It is the step the defect skips; the input record
  catches the skip.

## 5. Production-readiness checklist

- security — none: one more blob id read at the revision the mirror reads.
- perf / scale — one `git rev-parse` per render and per freshness check.
- error / empty / loading states — an absent store records `null`, as an absent legacy input does.
- observability — the stale reason names the input whose id differs.
- risks — every existing mirror reads stale once after landing, by design.
- testing — the case of §6 and the arm in §7.
- migration — §4.
- user docs — `tools/policy/README.md`'s mirror paragraph names the store among the inputs.

## 6. Acceptance criteria

- **AC1** — When `grep -n "def derive_kit_rel\|def derive_catalogue_rel" policy.py` runs in the
  policy kit, both print, and `derive_catalogue_rel`'s body is one call to `derive_kit_rel(CATALOGUE)`.
  Red when: the prefix read is written twice.
- **AC2** — When the `mirror-presets-stale` case renders the mirror, commits a change to one strict
  value in `presets.toml` without re-rendering, and runs `node policy-mirror.js get hooks.bypass`, it
  reports the mirror stale and answers the new value.
  Red when: the mirror reads FRESH and answers the old value.
- **AC3** — When `python policy.py mirror --print` runs in that case's repository, its
  `legacy_blobs` names the kit's `presets.toml` path.
  Red when: the store is absent from the recorded inputs.

## 7. Gates

`lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/policy/check_policy.py · covers AC2 AC3 · the `mirror-presets-stale` case, staged red by a copy of the kit whose input list omits the store · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit's H7 (id 47).
- rev-2 · 2026-10-26 · §3 · the Edges bullets to `KICK-dKeptSession-49`, `KICK-dKeptSession-50`,
  `KICK-dKeptSession-56` mirrored, the other ends of the edges the round-1 promotions' audit's
  disposal declared

## 10. Reuse audit

The seam extended is dGroundRules' `LEGACY_INPUTS` with `derive_catalogue_rel` (`tools/policy/policy.py`
at `3c8c4718a`, lines 809-834), whose comment names this as the step a unit adding a resolution input
takes. `python tools/codebase-map/reuse_lookup.py "inputs a JSON mirror records so it reads stale
when one changes"` ranked `read`, `read_text`, `records` and `changed` by name stem only; the policy
kit is not at this base, so no existing seam in the tree fits and the branch's list is the one
extended.

Recall terms used: `python tools/memory-recall/query.py "how does the policy mirror know a resolution
input changed" --terms "policy-mirror LEGACY_INPUTS legacy_blobs stale fresh presets.toml render_mirror
derive_catalogue_rel input"`
