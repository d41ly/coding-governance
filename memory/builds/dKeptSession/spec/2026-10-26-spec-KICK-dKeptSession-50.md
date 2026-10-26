# KICK-dKeptSession-50 — the mirror's upgrade path observed on a pre-unit mirror: re-rendered by the kit's update, and refused by its check where the update skips it

**Status:** OPEN · rev-2 · 2026-10-26 · node a · Tier-2 · base 462d20f3 · streams kickoff · order 5 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-50-deviation-501.md](../build/2026-10-26-build-KICK-dKeptSession-50-deviation-501.md) | deviation | — |
| [2026-10-26-review-KICK-dKeptSession-45-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-45-spec-audit.md) | spec-audit | KICK-dKeptSession-49 KICK-dKeptSession-54 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-56 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of this build's fifteen round-1 promotions
(`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-30-spec-audit.md`)
confirmed finding **id 48 at HIGH**, report item **H3**. Id 22 shares the item and is promoted as
`KICK-dKeptSession-49`, which makes the JS reader expect the store; this unit is the upgrade path's
half of the same fix.

`KICK-dKeptSession-40` AC2 renders the mirror after the unit lands, so no criterion of that unit
ever meets a mirror rendered before it, and its §4 Migration names no step that re-renders one. The
kit has two such steps already: in this repository the `[[generated]]` row for
`.governance/policy.json` re-renders the mirror at each landing, and in an adopter the
`[[regenerate]]` row runs `adopt-policy.sh --scaffold`, which renders it, on every update unless
`GOVKIT_RERENDER=0` is exported (`git show 3c8c4718a:tools/policy/kit.toml`, lines 39-52, and
`adopt-policy.sh` lines 9-18). Where neither runs, `arm_mirror_parity` reds a working-tree mirror
that differs from its render at HEAD (`check_policy.py:23-25` at `3c8c4718a`). This unit observes
all three on a planted pre-unit mirror and states that path as the migration. It repairs
`KICK-dKeptSession-40` and builds one step after it (order 5).

## 2. Scope (IN)

- **S1** — id 48. The upgrade re-renders. A fixture case `mirror-upgrade` in
  `tools/policy/check_policy.py` plants a pre-unit mirror in an adopter's scratch repository, runs
  the `[[regenerate]]` row's argv, `bash <kit>/adopt-policy.sh --scaffold --target <dir>`, and reads
  the rewritten mirror. Observed by AC1.
- **S2** — id 48. A skipped upgrade is refused. The same case, run with the re-render skipped as
  `GOVKIT_RERENDER=0` skips it, runs `bash <kit>/adopt-policy.sh --check --target <dir>`. Observed by
  AC2.
- **S3** — id 48. The migration stated where the kit documents the mirror. `tools/policy/README.md`'s
  mirror paragraph gains one: a mirror rendered before the store became an input is re-rendered by the
  landing's `[[generated]]` row here and by the `[[regenerate]]` row in an adopter; with
  `GOVKIT_RERENDER=0` it stays as it was, `adopt-policy.sh --check` refuses it, and the hooks read it
  stale (`KICK-dKeptSession-49`). Observed by AC3.
- **S4** — id 48. The sibling text superseded by name. `KICK-dKeptSession-40` §4 Migration ("reads it
  stale once and the reader answers; the next `policy.py mirror --write` records the entry") and §5's
  risks line read as S3 here, and unit 40 AC2 is joined by AC1 and AC2 for the pre-unit mirror it
  never sees. Answered in unit 40's acceptance ledger. Observed by AC1.

## 3. Non-goals (OUT)

- The JS reader's expected list: id 22, `KICK-dKeptSession-49`.
- A new upgrade step. The kit's `[[regenerate]]` and `[[generated]]` rows already re-render; this unit
  observes them and documents the one skip.
- The committed `.governance/policy.json` moving under unit 40 and unit 41: id 40, the batch's item,
  `KICK-dKeptSession-56`.

### Edges

- **consumes-from** `KICK-dKeptSession-40` — `derive_mirror_inputs` and the mirror's `legacy_blobs`, whose upgrade from a pre-unit mirror this unit observes (id 48)
- **hands-off** `KICK-dKeptSession-62` — the `mirror-upgrade` arm, whose leg the batch's S1 records (id 2)

## 4. Design

### Evidence

- `[[regenerate]] argv = ["bash", "{kit}/adopt-policy.sh", "--scaffold"]` and the `[[generated]]` row
  for `.governance/policy.json`, generator `policy.py` (`kit.toml:39-52` at `3c8c4718a`).
- `adopt-policy.sh` renders `policy.py mirror --write` on every `--scaffold`, kept file or written
  (lines 11-14 and 122 at `3c8c4718a`), and `--check` is `check_policy.py --repo <repo>`.
- `arm_mirror_parity` reds a working-tree mirror differing from its render at HEAD
  (`check_policy.py:23-25` and `:316` at `3c8c4718a`).

### The pre-unit mirror

```
plant: .governance/policy.json, the render less legacy_blobs[<kit>/presets.toml]
adopt-policy.sh --scaffold          -> legacy_blobs gains <kit>/presets.toml · mirror --check exit 0
GOVKIT_RERENDER=0, then --check     -> exit 1, arm_mirror_parity · legacy_blobs
```

### Inventory

| Minted | Kind | Home |
|---|---|---|
| `mirror-upgrade` | fixture case | `tools/policy/check_policy.py` |

### Migration

S3 is this unit's migration statement; no stored state is changed by this unit.

### Files touched (estimate)

- `tools/policy/check_policy.py`: the `mirror-upgrade` case
- `tools/policy/README.md`: S3

### Alternatives rejected

- **A forced re-render inside the hook.** A hook that writes the mirror is a write path in a read
  surface, and the reader shim already answers a stale mirror correctly.
- **Refusing `GOVKIT_RERENDER=0`.** It is an owner's declared switch (TOOL-dGroundRules-21 S37); the
  check refusing the stale mirror is the visible result it already has.

## 5. Production-readiness checklist

- security — none: a fixture case and a README paragraph.
- perf / scale — none.
- error / empty / loading states — S2's refusal names the mirror and its first differing field.
- observability — `arm_mirror_parity`'s line, and `mirror --check`'s `run: ... mirror --write` remedy.
- risks — none new.
- testing — the case of §6 and the arm in §7.
- migration — S3.
- user docs — `tools/policy/README.md`, S3; no page under `help/` describes the mirror's upgrade.

## 6. Acceptance criteria

The fixture is the policy kit copied into a scratch adopter repository under `%TEMP%` with one
commit, and `.governance/policy.json` planted from the unit's render with the `presets.toml` key
removed from `legacy_blobs`, the bytes a pre-unit render writes for that repository.

- **AC1** — When the `mirror-upgrade` case runs `bash adopt-policy.sh --scaffold --target <dir>`, the
  rewritten mirror's `legacy_blobs` names the kit's `presets.toml` path, and `python policy.py mirror
  --check` in `<dir>` exits 0.
  Red when: the upgrade leaves the pre-unit mirror in place, so its hooks keep the old values.
- **AC2** — When the case skips the re-render and runs `bash adopt-policy.sh --check --target <dir>`,
  it exits 1 with an `arm_mirror_parity` finding naming `legacy_blobs`.
  Red when: a skipped upgrade leaves a pre-unit mirror that every check reads green.
- **AC3** — When `grep -n "GOVKIT_RERENDER=0" README.md` runs in the policy kit, it prints S3's
  sentence in the mirror paragraph.
  Red when: the migration is described as a stale read the code does not perform.

## 7. Gates

`lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/policy/check_policy.py · covers AC1 AC2 · a planted pre-unit mirror upgraded and then left un-upgraded, staged red by a copy of `adopt-policy.sh` that skips the mirror on a kept policy file · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 promotions' audit, H3 (id 48).
- rev-2 · 2026-10-26 · §3 · the Edges bullet to `KICK-dKeptSession-62` mirrored, the other ends of
  the edges the round-2 promotions' audit's disposal declared

## 10. Reuse audit

The seams reused are the kit's own re-render rows, `[[regenerate]]` and `[[generated]]`
(`tools/policy/kit.toml:39-52` at `3c8c4718a`), and `arm_mirror_parity`
(`tools/policy/check_policy.py:316` at `3c8c4718a`); no upgrade step is minted. `python
tools/codebase-map/reuse_lookup.py "inputs a JSON mirror records so it reads stale when one
changes"`, unit 40's probe, ranked name stems only; the policy kit is not at this base, so no
existing seam in the tree fits and the branch's rows are the ones observed.

Recall terms used: `python tools/memory-recall/query.py "how is a policy mirror rendered before a
new input re-rendered on upgrade" --terms "mirror upgrade regenerate generated GOVKIT_RERENDER
adopt-policy scaffold arm_mirror_parity legacy_blobs presets"`
