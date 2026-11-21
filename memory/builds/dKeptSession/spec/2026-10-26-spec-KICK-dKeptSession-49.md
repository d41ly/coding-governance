# KICK-dKeptSession-49 — the JS mirror reader takes the inputs it compares from its own code, so a mirror missing the preset store reads stale

**Status:** INPROGRESS · rev-6 · 2026-11-21 · node a · Tier-2 · base 462d20f3 · streams kickoff · order 5 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-49-deviation-491.md](../build/2026-10-26-build-KICK-dKeptSession-49-deviation-491.md) | deviation | — |
| [2026-11-21-build-KICK-dKeptSession-1-reground-orders-1-6-returns.md](../build/2026-11-21-build-KICK-dKeptSession-1-reground-orders-1-6-returns.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-33 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-4 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-20 KICK-dKeptSession-32 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 |
| [2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-33 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-4 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-20 KICK-dKeptSession-32 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-30 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-51 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-43 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-17 KICK-dKeptSession-61 KICK-dKeptSession-18 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-11-21-prompt-KICK-dKeptSession-4-orders-5-reground-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-4-orders-5-reground-brief.md) | research | KICK-dKeptSession-4 KICK-dKeptSession-50 KICK-dKeptSession-54 |
| [2026-11-21-prompt-KICK-dKeptSession-4-precheck-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-4-precheck-brief.md) | research | KICK-dKeptSession-4 KICK-dKeptSession-50 KICK-dKeptSession-54 |
| [2026-11-21-prompt-KICK-dKeptSession-49-1-spec-writer.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-49-1-spec-writer.md) | journal | — |
| [2026-11-21-prompt-KICK-dKeptSession-49-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-49-build-brief.md) | research | — |
| [2026-11-21-prompt-KICK-dKeptSession-49-divergence-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-49-divergence-brief.md) | research | — |
| [2026-10-26-review-KICK-dKeptSession-45-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-45-spec-audit.md) | spec-audit | KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-56 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of this build's fifteen round-1 promotions
(`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-30-spec-audit.md`)
confirmed finding **id 22 at HIGH**, report item **H3**. Id 48 shares the item and is promoted as
`KICK-dKeptSession-50`, the upgrade path's half; id 9 is the same defect at MEDIUM, item M8, batched
into `KICK-dKeptSession-56`, whose item observes this fix.

`KICK-dKeptSession-40` records `presets.toml` as a mirror input and says a mirror rendered before it
"reads it stale once". It does not. `readMirrorAt` builds the list of recorded inputs it compares
from `Object.keys(doc.legacy_blobs)` of the stored mirror itself
(`tools/policy/policy-mirror.js#readMirrorAt`), so a mirror with no `presets.toml` key never has the
store compared and reads FRESH. Every hook that calls `readPolicy` then serves the old preset values
while `policy.py get` answers the new ones: the guard takes its input list from the state it guards.
This unit gives the reader its own expected list. It repairs `KICK-dKeptSession-40` and builds one
step after it (order 5).

## 2. Scope (IN)

- **S1** — id 22. The expected list. `MIRROR_KIT_INPUTS`, a new constant of
  `tools/policy/policy-mirror.js`, holds the kit-relative names the reader owes, `["presets.toml"]`.
  `readMirrorAt` compares, beside the policy file and the catalogue, every name of
  `MIRROR_KIT_INPUTS` spelled from `kitRel` exactly as the catalogue's path already is, and every
  key the stored `legacy_blobs` records that the first list does not hold, all in its one
  `git cat-file --batch-check` call. `legacyStale` holds where any path of that list has a recorded
  id differing from its id at the landed revision, a path absent from the stored map differing from
  every id, `null` included, so such a mirror reads STALE. The file's header comment, step 3 of its
  evaluation order, and `readMirrorAt`'s own comment name that list in place of "each path of the
  mirror's `legacy_blobs`". Observed by AC1 and AC2.
- **S2** — id 22. The sibling text superseded by name. `KICK-dKeptSession-40` S2's "and
  `policy-mirror.js`, which compares every key of `legacy_blobs`, reads a changed store STALE with no
  edit", its §4 Evidence sentence "Neither holds a list of its own, so neither is edited" for the JS
  reader, and its §4 Migration sentence read as S1 here: the JS is edited, and a pre-unit mirror reads
  stale because the reader expects the store, not because the mirror names it. Answered in this
  unit's own acceptance ledger,
  `memory/builds/dKeptSession/build/2026-11-21-build-KICK-dKeptSession-49-1-acceptance-ledger.md`,
  which quotes those three passages of unit 40's spec and states S1 supersedes them; unit 40 is
  CLOSED, so neither its spec nor its ledger is written (F1). Observed by AC1 and AC4.
- **S3** — The kit copy. `MIRROR_KIT_FILES` (`tools/policy/check_policy.py#MIRROR_KIT_FILES`) gains
  `presets.py` and `presets.STORE`, so `build_landed_repo` and `build_limit_repo`, its two users,
  copy both. A stale read falls through to the kit copy's `policy-shim.sh get`, and that copy's
  `policy.py` refuses a strict-named file with no `presets.py` beside it (§4), so AC1 and AC2 could
  not answer at all. This is the copy's second instance: `KICK-dKeptSession-40`'s
  `mirror-presets-stale` branch copies the same two files into the kit itself
  (`tools/policy/check_policy.py#run_mirror_landed`), so that branch's copy loop goes and its two
  names live in this list, written once. Every other case of the two builders names no preset, so
  `presets.py` is never imported there, and the store, committed in each, records one blob id on
  both sides. Observed by AC1 and AC2.
- **S4** — The kit README. The helper clause of `tools/policy/README.md#the-mirror`, "the helper
  reads a mirror whose recorded id differs at L, or that carries no `legacy_blobs`, as STALE",
  describes only the recorded keys. It is corrected to S1's list: the helper compares, beside the
  policy file and the catalogue, every name of `MIRROR_KIT_INPUTS` by the kit's prefix and every
  other key the mirror records, and reads STALE a mirror whose recorded id differs at L, that lacks
  an expected key, or that carries no `legacy_blobs`. The guard's sentence below it, which reads the
  staged mirror's own keys, stays true (§3). Observed by AC3.

## 3. Non-goals (OUT)

- The Python side. `policy.py mirror --check` compares the whole render, `legacy_blobs` a field of
  it (`tools/policy/policy.py#check_mirror_text`), so a pre-unit mirror already reads stale there.
- The policy guard. `check_mirror_render` reads the staged mirror's own `legacy_blobs` keys for its
  input walk, but then compares the staged bytes with `policy.py mirror --print`
  (`tools/policy/guard.py#check_mirror_render`), so a pre-unit mirror stays in its touched set.
- The repository-relative inputs, `LEGACY_INPUTS` of `policy.py`, which the reader still discovers
  from the stored map: KICK-dKeptSession-62 S24 adds their copy.
- The upgrade path that re-renders a pre-unit mirror, and the parity of the two input lists: id 48,
  `KICK-dKeptSession-50`, and `KICK-dKeptSession-59`.
- The report's left-shift checklist entry, that a freshness check takes its expected input list
  from code. No clause of this build names that checklist; AC1 is its arm here.

### Edges

- **consumes-from** `KICK-dKeptSession-40` — the store recorded under `legacy_blobs`, which this unit makes the JS reader expect rather than discover (id 22)
- **hands-off** `KICK-dKeptSession-56` — `MIRROR_KIT_INPUTS` and the stale read of a pre-unit mirror, which the batch's item for id 9, the same defect at MEDIUM, observes
- **hands-off** `KICK-dKeptSession-59` — `MIRROR_KIT_INPUTS` and §3's parity non-goal, which that unit gates and supersedes (id 10)
- **hands-off** `KICK-dKeptSession-60` — `MIRROR_KIT_INPUTS`, which that unit's rule names beside Python's list (id 23)
- **hands-off** `KICK-dKeptSession-62` — `readMirrorAt`'s expected list and its arm's leg, which the batch's S24 and S1 widen and record (ids 33, 2)

## 4. Design

### Evidence

Read at HEAD `c2a407b0`, 2026-11-21; S2, S3, S4 and the probe below re-read at `cd808f85`.

- `readMirrorAt(top, landed, kitRel)` sets `legacy` to `Object.keys(doc.legacy_blobs)`, asks
  `git cat-file --batch-check` for the policy file, `<kitRel>/catalogue.toml` and each of `legacy`
  at the landed revision, and sets `legacyStale` only where one of those recorded ids differs, or
  the map is absent (`tools/policy/policy-mirror.js#readMirrorAt`). `readPolicy` reads STALE on
  `legacyStale` and falls through to `policy-shim.sh get`, which a `last-valid` reading of
  `policy-file.on-invalid`, the catalogue default, admits (`tools/policy/policy-mirror.js#readPolicy`).
- The catalogue's path is spelled from `kitRel` in the reader, so the store's path takes the same
  spelling, and KICK-dKeptSession-40's `derive_kit_rel("presets.toml")` spells the same path on the
  Python side.
- `render_mirror` writes `legacy_blobs` from the inputs it records
  (`tools/policy/policy.py#render_mirror`), today `LEGACY_INPUTS`, both repository-relative.
- Probed at `b3698899` over `build_landed_repo` with `preset = "strict"` above `LANDED_POLICY`: a
  stale mirror read through a kit copy of `MIRROR_KIT_FILES` alone exits 2, its refusal line naming
  the kit copy's `presets.py` at line zero and saying the named presets' module does not import.
- Probed at `cd808f85`, unit 40 landed, by a scratch script in `tools/policy/` building AC1's
  fixture with `build_landed_repo`, the two preset files copied, `render_mirror` at HEAD with the
  `tools/policy/presets.toml` key removed, pushed as L. With the store changed and pushed, the
  landed reader exits 0 printing `refused`, its stderr line `policy: hooks.bypass · preset · preset
  strict at <L8>, the landed revision` with no `mirror stale at`, the defect. A scratch copy of
  `policy-mirror.js` carrying S1, `["presets.toml"]` spelled from `kitRel` and joined ahead of the
  recorded keys, exits 0 printing `allowed`, its stderr line opening `policy: hooks.bypass · preset ·
  mirror stale at <L8>; `; with the store unchanged it prints `refused` under the same prefix. In
  all four runs `arm_mirror_landed` found nothing over the 3 keys the policy file sets (DERIVED,
  that probe), since `hooks.bypass` is not one of them.
- `MIRROR_KIT_FILES` is `(*READER_FILES, "policy-mirror.js", "policy-shim.sh")`, and `READER_FILES`
  holds no preset file (`tools/policy/check_policy.py#MIRROR_KIT_FILES`). `KICK-dKeptSession-40`'s
  `mirror-presets-stale` branch copies `presets.py` and `presets.STORE` into its kit itself, in a
  loop of its own (`tools/policy/check_policy.py#run_mirror_landed`).
- The helper clause of `tools/policy/README.md#the-mirror` names only the recorded ids, and
  `MIRROR_KIT_INPUTS` appears nowhere in that README; `help/policy.md` names no mirror input.

### The check

```
expected := [POLICY_REL, kitRel/catalogue.toml]
          + [kitRel/<n> for n in MIRROR_KIT_INPUTS]
          + [k for k in keys(doc.legacy_blobs) if k not already listed]
stale    := any expected path past the first two whose recorded id (absent: none) differs from its blob at L
```

### Inventory

| Minted | Kind | Home |
|---|---|---|
| `MIRROR_KIT_INPUTS` | constant | `tools/policy/policy-mirror.js` |
| `mirror-pre-unit-stale` | fixture case, a branch of `run_mirror_landed` | `tools/policy/check_policy.py` |

### Migration

A mirror rendered before `KICK-dKeptSession-40` lacks the store's key, so this reader reads it
STALE and every key falls through to the reader shim, which answers from `policy.py`, until the
mirror is re-rendered. That is the stale-once the sibling spec meant, now true by construction.

### Files touched (estimate)

- `tools/policy/policy-mirror.js`: `MIRROR_KIT_INPUTS`, S1 in `readMirrorAt`, and its two comments
- `tools/policy/check_policy.py`: the `mirror-pre-unit-stale` branch and its `CASES` row, S3's two
  names in `MIRROR_KIT_FILES`, and the `mirror-presets-stale` branch's copy loop removed
- `tools/policy/README.md`: S4's helper clause
- `memory/builds/dKeptSession/build/2026-11-21-build-KICK-dKeptSession-49-1-acceptance-ledger.md`:
  S2's answer beside the criteria observed

No new function, so the symbol map does not move; the kickoff manifest watches none of these paths.

### Alternatives rejected

- **A schema version field in the mirror.** It works for this one change, but each later input
  needs a second edit to bump it, and the reader would still trust the artefact for the list.
- **The reader running `policy.py` to learn the inputs.** It is a spawn on every hook read, the cost
  the mirror exists to avoid.

## 5. Production-readiness checklist

- security — one more path in the one `--batch-check` call; no new process.
- perf / scale — unchanged spawn count per read.
- error / empty / loading states — an absent store at the landed revision reads `missing`, equal to a
  recorded `null`, as an absent legacy input does today.
- observability — the reason prefix `mirror stale at <L8>` the reader already prints.
- risks — every pre-unit mirror reads stale until re-rendered, by design; reads fall through to the
  shim, never to a wrong value. A mirror rendered by a policy kit at another path than the reader's
  records the store under that path, so the reader's expected path is absent and it reads stale; in
  an install the renderer and the reader are one kit copy, and the fixtures copy the kit to its own
  path (`tools/policy/check_policy.py#build_limit_repo`).
- testing — the case of §6 and the arm in §7.
- migration — §4.
- user docs — `help/policy.md` does not describe the mirror's inputs, so no page under `help/`
  moves; the kit README's helper clause is S4.

## 6. Acceptance criteria

The fixture is a branch of `run_mirror_landed` over `build_landed_repo`, as `mirror-stale-legacy`
is: a scratch repository under `%TEMP%` whose kit copy carries `presets.py` and `presets.toml` (S3),
its policy file `preset = "strict"` above `LANDED_POLICY` with `policy-file.on-invalid =
"last-valid"`, and `.governance/policy.json` planted from `render_mirror` at HEAD with the store's
key taken out of `legacy_blobs`, the bytes a pre-unit render writes, committed and pushed as the
landed revision. The branch ends, as every branch does, in `arm_mirror_landed`, which must find
nothing.

- **AC1** — When the `mirror-pre-unit-stale` case commits strict's `hooks.bypass` set to `allowed` in
  the kit copy's `presets.toml`, pushes it alone and runs `node policy-mirror.js get hooks.bypass
  --repo <repo> --explain`, it exits 0 printing `allowed`, its stderr line reading `policy:
  hooks.bypass · preset · mirror stale at <L8>; ` and the reader's reason.
  Red when: a copy taking its list from `Object.keys(doc.legacy_blobs)` reads FRESH and answers
  `refused`, as the probe in §4 did, or the read refuses for want of `presets.py`.
  fixture: `KICK-dKeptSession-2`'s step, landed at `b3698899`, and `KICK-dKeptSession-40`'s store
  key in the render, order 4.
- **AC2** — When the same case runs with `presets.toml` unchanged, the read exits 0 printing
  `refused`, its stderr line still reading `policy: hooks.bypass · preset · mirror stale at <L8>; `.
  Red when: a mirror that omits an input the reader expects reads FRESH because the omitted input
  happens not to have moved.
- **AC3** — `tr -s ' \r\n' ' ' < tools/policy/README.md | grep -c "the helper reads a mirror whose
  recorded id differs at L"` prints `0`, and the same pipe into `grep -c "MIRROR_KIT_INPUTS"` prints
  `1`: the squeezed README is one line, so each count is 0 or 1.
  Red when: the clause names only the recorded keys, as at `cd808f85`, where the two print `1` and
  `0`.
- **AC4** — `tr -s ' \r\n' ' '` over this unit's acceptance ledger piped into `grep -c "compares
  every key of"` prints `1`, and into `grep -c "Neither holds a list of its own"` prints `1`; and
  `git diff --name-only <pass base> HEAD --` over unit 40's spec and its
  `2026-11-21-build-KICK-dKeptSession-40-1-acceptance-ledger.md` prints nothing.
  Red when: S2's answer lands in a record of unit 40, or this unit's ledger quotes none of the
  passages it supersedes.

## 7. Gates

`policy fixtures` · `scratch-guard self-test` · `routed-commits selftest` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/policy/check_policy.py · covers AC1 AC2 · a planted pre-unit mirror, with and without a changed store, staged red by a copy of `policy-mirror.js` that lists only the mirror's recorded keys · none

## 8. Open questions

- **F1 — Where is S2's answer to unit 40's superseded wording recorded?** Unit 40 is CLOSED, built
  at order 4, and its ledger says nothing about the JS reader's input list. (a) Unit 40's acceptance
  ledger, a record of a closed unit written by a later one; (b) this unit's own acceptance ledger,
  naming the unit 40 spec text it supersedes. Recommendation (b): a CLOSED unit's records are never
  written by a later unit. RESOLVED (agent, 2026-11-21, delegated): (b), rung 3, the main loop's
  ruling in `2026-11-21-prompt-KICK-dKeptSession-49-divergence-brief`; (a) rejected.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 promotions' audit, H3 (id 22).
- rev-2 · 2026-10-26 · §3 · the Edges bullets to `KICK-dKeptSession-59`, `KICK-dKeptSession-60`,
  `KICK-dKeptSession-62` mirrored, the other ends of the edges the round-2 promotions' audit's
  disposal declared
- rev-3 · 2026-11-21 · §1 · S1 S2 · §3 · §4 · §5 · AC1 AC2 · §6 · §7 · §10 · re-grounded at HEAD
  `c2a407b0` by `2026-11-21-prompt-KICK-dKeptSession-4-orders-5-reground-brief`; mechanism, carries,
  order and status kept. Every line citation of dGroundRules' branch became a `path#symbol` citation
  of the landed kit. S1 states the union, the absent-key rule and the one call; S2 quotes unit 40's
  rev-3 wording; §3 gained the guard and the repository-relative inputs, each shown not to need the
  list; the fixture is named as a `run_mirror_landed` branch over `build_landed_repo`, and the ACs
  observe the reason prefix the reader prints. §7's leg line takes the guarded legs its paths trip.
- rev-4 · 2026-11-21 · S3 · §4 · §5 · §6 · AC1 · AC2 · checked for behaviour against the tree after
  units 1, 19, 33 and 2 landed, under the brief `2026-11-21-prompt-KICK-dKeptSession-4-precheck-brief`.
  S3 added: a probe at `b3698899` showed a stale read through the landed kit copy refuses for want of
  `presets.py`, so `MIRROR_KIT_FILES` carries it and the store, unit 40's branch being the copy's
  first instance. The fixture names its `on-invalid` line and its closing arm; AC1 and AC2 name the
  value, the source and the exit each read prints; §5 states the renderer and reader sharing a path.
- rev-5 · 2026-11-21 · §4 · the probe's refusal line is described instead of quoted, since its
  quoted path with a line suffix read as an unlisted line citation to the positional leg; under the
  brief `2026-11-21-prompt-KICK-dKeptSession-4-precheck-brief`.
- rev-6 · 2026-11-21 · S1 · S2 · S3 · S4 · §4 · §5 · AC3 · AC4 · §8 · the builder's divergence
  resolved under the brief `2026-11-21-prompt-KICK-dKeptSession-49-divergence-brief`. S2's answer
  moves to this unit's own ledger, F1 resolved (b); S4 corrects the kit README's helper clause, AC3
  observing it; AC4 observes the ledger; S3 removes unit 40's landed per-branch copy; S1 names the
  reader's two comments; §4 re-probed both criteria at `cd808f85`.

## 10. Reuse audit

The seam extended is `readMirrorAt`'s one `git cat-file --batch-check` call
(`tools/policy/policy-mirror.js#readMirrorAt`), with the reader's own `kitRel` spelling of the
catalogue; no second freshness walk is written. The case extends `run_mirror_landed`
(`tools/policy/check_policy.py#run_mirror_landed`) beside its `mirror-stale-legacy` branch, over
`build_landed_repo`. `python tools/codebase-map/reuse_lookup.py "inputs a JSON mirror records so it
reads stale when one changes"`, unit 40's probe, ranked `read_text`, `read`, `read_bytes`, `records`
and `read_policy_value` by name stem only; none reads the mirror, and the recall query below
surfaced `KICK-dKeptSession-40`, `KICK-dKeptSession-59` and TOOL-dGroundRules-31, the install-day
mirror deferral, which compares no input list. So no other seam fits beyond the reader extended.

Recall terms used: `python tools/memory-recall/query.py "how does a freshness check know which inputs a rendered mirror must record" --terms "mirror stale fresh legacy_blobs inputs policy-mirror render expected input list artefact"`
