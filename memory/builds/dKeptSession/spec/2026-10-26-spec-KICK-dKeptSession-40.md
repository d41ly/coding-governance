# KICK-dKeptSession-40 — the preset store a recorded input of the JSON mirror, so a changed preset reads the mirror stale

**Status:** CLOSED · rev-5 · 2026-11-21 · node a · Tier-2 · base c2a407b0 · streams kickoff · order 4 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-30-promoted-fix-return.md](../build/2026-10-26-build-KICK-dKeptSession-30-promoted-fix-return.md) | research | KICK-dKeptSession-28 KICK-dKeptSession-36 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-30 |
| [2026-10-26-build-KICK-dKeptSession-40-deviation-401.md](../build/2026-10-26-build-KICK-dKeptSession-40-deviation-401.md) | deviation | — |
| [2026-11-21-build-KICK-dKeptSession-1-reground-orders-1-6-returns.md](../build/2026-11-21-build-KICK-dKeptSession-1-reground-orders-1-6-returns.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-33 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-34 KICK-dKeptSession-4 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-20 KICK-dKeptSession-32 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 |
| [2026-11-21-build-KICK-dKeptSession-40-1-acceptance-ledger.md](../build/2026-11-21-build-KICK-dKeptSession-40-1-acceptance-ledger.md) | journal | — |
| [2026-10-26-prompt-KICK-dKeptSession-30-promoted-fix-brief.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-30-promoted-fix-brief.md) | research | KICK-dKeptSession-28 KICK-dKeptSession-36 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-30 |
| [2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-33 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-34 KICK-dKeptSession-4 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-20 KICK-dKeptSession-32 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-30 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-51 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-43 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-17 KICK-dKeptSession-61 KICK-dKeptSession-18 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-11-21-prompt-KICK-dKeptSession-2-orders-3-4-reground-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-2-orders-3-4-reground-brief.md) | research | KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-34 |
| [2026-11-21-prompt-KICK-dKeptSession-3-precheck-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-3-precheck-brief.md) | research | KICK-dKeptSession-3 KICK-dKeptSession-34 |
| [2026-11-21-prompt-KICK-dKeptSession-40-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-40-build-brief.md) | research | — |
| [2026-10-26-review-KICK-dKeptSession-30-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-30-spec-audit.md) | spec-audit | KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-32 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-41 KICK-dKeptSession-44 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build's spec set
(`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md`)
confirmed finding **id 47 at HIGH**, report item **H7**, which no other id shares.

`KICK-dKeptSession-2`'s `read_preset_value` reads `tools/policy/presets.toml` as a resolution
input. dGroundRules' mirror records only the policy file's, the catalogue's and each `LEGACY_INPUTS`
file's blob ids (`tools/policy/policy.py#render_mirror`), and `policy-mirror.js` reads it FRESH while
every recorded id holds. A change to `presets.toml` without a re-render therefore leaves every hook
reading the old values, scratch-guard's `actions.free`, agent-cap and mail-notice among them, while
`policy.py get` returns the new ones. This unit records the store as a mirror input. It builds one
step after unit 2 (order 4).

## 2. Scope (IN)

- **S1** — id 47. The kit path. `derive_kit_rel(name)` in `tools/policy/policy.py` is
  `derive_catalogue_rel`'s body with the file name a parameter: the kit's `git rev-parse
  --show-prefix` plus `name`, a `Refusal` naming the file where the kit is in no repository. The
  existing `derive_catalogue_rel()` becomes one call, `derive_kit_rel(CATALOGUE)`, so the module's
  prefix read for a kit file lives once. Observed by AC1.
- **S2** — id 47. The input. `derive_mirror_inputs()` in `tools/policy/policy.py` returns
  `(*LEGACY_INPUTS, derive_kit_rel("presets.toml"))`. `render_mirror`'s `legacy_blobs` map and
  `cmd_mirror`'s working-tree walk over the inputs both iterate it in place of `LEGACY_INPUTS`, so
  the mirror records the store's blob, `mirror --write` refuses while the store is uncommitted, and
  `policy-mirror.js`, which compares every key of `legacy_blobs`, reads a changed store STALE with no
  edit. `LEGACY_INPUTS` keeps its literal line, which the `guard-mirror-inputs-join` scenario of
  `run_guard_case` rewrites to plant an input. `derive_kit_rel` refuses only where
  `derive_catalogue_rel` already refuses in the same render, so no caller of `render_mirror` gains a
  refusal. Observed by AC2, AC3 and AC4.
- **S3** — id 47. The render and the text. gov's `.governance/policy.json` is re-rendered by
  `python tools/policy/policy.py mirror --write`, gaining the store's entry under `legacy_blobs`, and
  the mirror section of `tools/policy/README.md` names the store among the recorded inputs, its JSON
  example included. The guard section of `help/policy.md`, whose parenthetical says the
  `legacy_blobs` record holds "today `.agent-cap.conf` alone", names its three inputs, the fanout
  conf, the instruction overlay and the policy kit's `presets.toml`, since the guard refuses a mirror
  staged beside a changed store from this unit on (`tools/policy/guard.py#check_mirror_render`).
  Observed by AC4 and AC5.

## 3. Non-goals (OUT)

- `KICK-dKeptSession-20`'s scenario step: it answers `None` with no build, and `policy.json` is
  rendered per revision and never per build, so the mirror never reads a scenario (the skeptic's
  corrected fix leaves unit 20 unchanged).
- The mirror's render and the JS reader's logic: dGroundRules', unchanged but for S2's input list.
- The README's rule for a unit adding a mirror input, which today names `LEGACY_INPUTS` alone:
  `KICK-dKeptSession-60` rewrites it to name both lists.
- The caps module's `derive_kit_rel()`, the no-argument prefix reader `budgets.py` keeps for its own
  census and limits paths: it answers `None` outside a repository, a contract its callers read, and
  it stays (F1).
- The report's left-shift fixture, every file the resolution order reads recorded as an input:
  AC2 is that observation for the one input this build adds.

### Edges

- **consumes-from** `KICK-dKeptSession-2` — `read_preset_value`'s read of `presets.toml`, the resolution input this unit records in the mirror (id 47), read beside the running `policy.py`, so this unit's case copies the store and `presets.py` into its kit copy
- **hands-off** `KICK-dKeptSession-49` — the store recorded under `legacy_blobs`, which that unit makes the JS reader expect rather than discover (id 22)
- **hands-off** `KICK-dKeptSession-50` — `derive_mirror_inputs` and the mirror's `legacy_blobs`, whose upgrade from a pre-unit mirror that unit observes (id 48)
- **hands-off** `KICK-dKeptSession-56` — `.governance/policy.json` as a write, the gates section's legs and the README's mirror text, the batch's S29, S25 and S42 (ids 40, 34, 41)

## 4. Design

### Evidence

- `LEGACY_INPUTS = (LEGACY_FANOUT, OVERLAY_REL)`, under the comment "A unit adding a resolution
  input adds its path here" (`tools/policy/policy.py#LEGACY_INPUTS`); both are repository-relative.
- `derive_catalogue_rel` runs `git rev-parse --show-prefix` from the kit and appends `CATALOGUE`
  (`tools/policy/policy.py#derive_catalogue_rel`); `render_mirror` records `catalogue_blob`,
  `legacy_blobs` over `LEGACY_INPUTS` and `policy_blob`; `cmd_mirror` walks `(POLICY_REL, cat,
  *LEGACY_INPUTS)` for uncommitted changes before it renders (`tools/policy/policy.py#cmd_mirror`).
- `policy-mirror.js` reads `Object.keys(doc.legacy_blobs)` and marks the mirror stale when any
  recorded id differs from the blob at the landed revision (`tools/policy/policy-mirror.js`, its
  `legacyStale` test); the policy guard reads the staged mirror's own `legacy_blobs` keys as the
  inputs a staged mirror must agree with (`tools/policy/guard.py#check_mirror_render`). Neither
  holds a list of its own, so neither is edited.
- `presets.toml` sits in the kit, so its path is the kit prefix plus the name, as the catalogue's is.
- A STALE mirror answers only where `policy-file.on-invalid` reads `last-valid`: it then returns the
  reader's answer, its reason prefixed `mirror stale at <L8>; `, and under any other value it refuses
  (`tools/policy/policy-mirror.js#readPolicy`), which is the `mirror-stale-refuse` branch's red.
- `build_landed_repo` copies `MIRROR_KIT_FILES`, which spreads `READER_FILES`
  (`tools/policy/check_policy.py#build_landed_repo`), and neither holds `presets.py` or
  `presets.toml` at `b3698899`, after `KICK-dKeptSession-2` landed: that unit copied `presets.py` only
  inside `run_resolution_order`. Its step reads the store beside the running `policy.py`
  (`tools/policy/policy.py#read_kit_presets`), so the shim's read in a copy lacking both files refuses
  naming `presets.py`. `KICK-dKeptSession-49` S3 widens `MIRROR_KIT_FILES` with both, at order 5,
  after this unit, so this unit's branch copies the two files itself and leaves the shared tuple to
  that unit. It edits strict's table in the copy by KICK-dKeptSession-1's store helper
  (`tools/policy/check_policy.py#set_preset_block`).
- `run_mirror_landed` ends every branch by `arm_mirror_landed` over its repository, which must find
  nothing for this branch as it does for `mirror-stale-legacy`; it compares only the keys the policy
  file sets, `preset` among them, none of which the store's edit moves.
- Every other `render_mirror` caller, `build_repo`, `set_landed`, `arm_mirror_parity` and the playbook's
  `read_tag_policy` (`tools/playbook/policy_value.py#read_tag_policy`), already reads
  `derive_catalogue_rel` in the same render. `adopt-policy.sh --scaffold` and its suite run gov's kit
  against an outside target, where the store's kit-relative path is absent on both sides of
  `cmd_mirror`'s walk, so its `mirror deferred` line still names the policy file first
  (`tools/policy/adopt-policy.test.sh`).

### Inventory

| Identifier | Kind | Home |
|---|---|---|
| `derive_kit_rel`, `derive_mirror_inputs` | functions | `tools/policy/policy.py` |
| `mirror-presets-stale` | fixture case, a branch of `run_mirror_landed` | `tools/policy/check_policy.py` |

### Migration

A mirror rendered before this unit carries no `presets.toml` entry, so `policy-mirror.js` reads it
stale once and the reader answers; the next `policy.py mirror --write` records the entry. gov's own
mirror is re-rendered in this unit (S3).

### Files touched (estimate)

- `tools/policy/policy.py`: S1 and S2
- `tools/policy/check_policy.py`: the `mirror-presets-stale` case, its `CASES` row, and the
  branch's own copy of `tools/policy/presets.py` and `tools/policy/presets.toml` into its kit copy,
  `MIRROR_KIT_FILES` left as it stands
- `tools/policy/README.md`: the mirror section
- `help/policy.md`: the guard section's list of the mirror's inputs
- `.governance/policy.json`: re-rendered by `mirror --write`
- `memory/map/generated/symbols.json`: the two new functions, regenerated as the commit hook's
  codebase-map leg requires

### Alternatives rejected

- **The store's path as a literal in `LEGACY_INPUTS`.** The kit's prefix in a repository is not known
  at import time; a literal would name the wrong path in an adopter.
- **Rendering the mirror on every preset edit.** It is the step the defect skips; the input record
  catches the skip.

## 5. Production-readiness checklist

- security — none: one more blob id read at the revision the mirror reads.
- perf / scale — one `git rev-parse` per render and per freshness check.
- error / empty / loading states — an absent store records `null`, as an absent legacy input does.
- observability — the stale reason names the revision whose recorded ids differ.
- risks — every existing mirror reads stale once after landing, by design.
- testing — the case of the acceptance section and the arm in the gates section.
- migration — the Migration sub-head above.
- user docs — `tools/policy/README.md`'s mirror section and `help/policy.md`'s guard section name
  the store among the inputs (S3).

## 6. Acceptance criteria

- **AC1** — When `grep -n "def derive_kit_rel\|def derive_catalogue_rel" policy.py` runs in the
  policy kit, both print, and `derive_catalogue_rel`'s body is one call to `derive_kit_rel(CATALOGUE)`.
  Red when: the prefix read is written twice.
- **AC2** — When the `mirror-presets-stale` branch of `run_mirror_landed` copies this kit's
  `presets.py` and `presets.toml` into the kit copy `build_landed_repo` made, LF-ended as that
  builder copies, commits them with `preset = "strict"` above `LANDED_POLICY`'s
  `policy-file.on-invalid = "last-valid"`, commits the mirror `render_mirror` gives at that commit and
  pushes it as L, then commits strict's `hooks.bypass` set to `allowed` in the copy's `presets.toml`
  by `set_preset_block` and pushes that alone, `node policy-mirror.js get
  hooks.bypass --repo <repo> --explain` exits 0 printing `allowed`, its stderr line reading
  `policy: hooks.bypass · preset · mirror stale at <L8>; ` and the reader's reason, and the branch's
  closing `arm_mirror_landed` finds nothing.
  Red when: the mirror reads FRESH and answers `refused`, or the read refuses.
- **AC3** — When `python policy.py mirror --print` runs in that case's repository, its
  `legacy_blobs` names the kit's `presets.toml` path beside `.agent-cap.conf` and
  `.governance/instructions.toml`.
  Red when: the store is absent from the recorded inputs.
- **AC4** — When `python tools/policy/policy.py mirror --check` runs in gov's checkout after S3's
  render, it prints `policy: mirror fresh`, and `.governance/policy.json`'s `legacy_blobs` holds
  the store's path in gov, the policy kit's directory plus `presets.toml`.
  Red when: gov's committed mirror predates the input.
- **AC5** — When `grep -n "legacy_blobs" policy.md` runs in the help directory, the guard section's
  line names `presets.toml` and no longer reads `.agent-cap.conf` alone.
  Red when: the page still names one input.

## 7. Gates

`policy fixtures` · `scratch-guard self-test` · `build-index selftest` · `gotchas selftest` · `routed-commits selftest` · `memory-recall kit selftest` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/policy/check_policy.py · covers AC2 AC3 · the `mirror-presets-stale` case, staged red by a copy of the kit whose input list omits the store · none

## 8. Open questions

- **F1 — Does the caps module's `derive_kit_rel()` fold into the new `policy.derive_kit_rel(name)`?**
  (a) No: the policy module gains `derive_kit_rel(name)`, refusing outside a repository, and
  `budgets.derive_kit_rel()` keeps its `None` answer for its census and limits paths; (b) yes:
  `budgets.py` calls the policy module's with an empty name and catches its refusal; (c) the policy
  module calls the caps module's, which imports it. RESOLVED (agent, 2026-11-21, delegated): (a),
  rung 3; (b) moves the caps module's no-repository answer, which its refusals name, with no clause
  asking for it, (c) inverts the import the caps module already makes of the policy module, and
  `KICK-dKeptSession-59` and `KICK-dKeptSession-63` spell `policy.derive_kit_rel(n)` as (a) has it.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit's H7 (id 47).
- rev-2 · 2026-10-26 · §3 · the Edges bullets to `KICK-dKeptSession-49`, `KICK-dKeptSession-50`,
  `KICK-dKeptSession-56` mirrored, the other ends of the edges the round-1 promotions' audit's
  disposal declared
- rev-3 · 2026-11-21 · §1 · S1 · S2 · S3 · §3 · §4 · §5 · AC2 · AC3 · AC4 · §7 · §8 F1 · §10 ·
  re-grounded on the landed dGroundRules at base c2a407b0 by
  2026-11-21-prompt-KICK-dKeptSession-2-orders-3-4-reground-brief: `LEGACY_INPUTS` re-read as the
  fanout conf and the instruction overlay; S2 narrowed to keep the literal line a guard scenario
  rewrites, and the guard and the JS reader named as needing no edit; rev-2's S3, unit 2's
  superseded bullet, dropped, unit 2 at rev-3 naming this unit; a new S3 takes gov's mirror render
  and the README text, so `.governance/policy.json` and `tools/policy/README.md` join Files touched;
  AC2 names its policy file and AC4 is added; F1 ruled for the caps module's same-named reader;
  every line citation re-cited by symbol; the guarded legs named.
- rev-4 · 2026-11-21 · S2 · S3 · §4 · §5 · AC2 · AC5 · §7 · checked for behaviour against the tree
  after KICK-dKeptSession-1 landed, by 2026-11-21-prompt-KICK-dKeptSession-3-precheck-brief: AC2's
  seed sets `policy-file.on-invalid = "last-valid"`, without which the helper refuses a stale mirror,
  lands each commit by a push, and names the closing `arm_mirror_landed`; the store's copy is named
  as unit 2's `READER_FILES` widening, and every other `render_mirror` caller checked; S3 and a new
  AC5 take `help/policy.md`'s guard line, so that page and the symbol map join Files touched.
- rev-5 · 2026-11-21 · §3 · §4 · AC2 · under 2026-11-21-prompt-KICK-dKeptSession-3-precheck-brief,
  folding the correction the KICK-dKeptSession-49 writer relayed at `b3698899`, after unit 2 landed:
  rev-4's claim that unit 2 puts `presets.py` and `presets.toml` in `READER_FILES` is false, since that
  unit copied `presets.py` inside `run_resolution_order` alone, so AC2's branch copies both files into
  its kit copy itself and edits the store by `set_preset_block`; `MIRROR_KIT_FILES` stays for unit
  49's S3, which builds after this unit; the Edges bullet and the evidence say so, and Files touched
  names the copy.

## 10. Reuse audit

The seam extended is dGroundRules' `LEGACY_INPUTS` with `derive_catalogue_rel`
(`tools/policy/policy.py#LEGACY_INPUTS`, `tools/policy/policy.py#derive_catalogue_rel`), whose
comment names this as the step a unit adding a resolution input takes, and the fixture's
`run_mirror_landed` with its `mirror-stale-legacy` branch, the same observation for the fanout conf.
`python tools/codebase-map/reuse_lookup.py "inputs a JSON mirror records so it reads stale when one
changes"` ranked `read_text`, `read`, `records` and `changed` by name stem only, and the kit-path
probe of the charter unit ranked `derive_kit_rel` in `tools/policy/budgets.py`,
`tools/playbook/instruction_units.py` and two other kits: the caps module's is this kit's one other
prefix reader, kept by F1, and the others are other kits' copies a kit may not import.

Recall terms used: `python tools/memory-recall/query.py "how does the policy mirror know a resolution input changed" --terms "policy-mirror LEGACY_INPUTS legacy_blobs stale fresh presets.toml render_mirror derive_catalogue_rel derive_kit_rel input"`
