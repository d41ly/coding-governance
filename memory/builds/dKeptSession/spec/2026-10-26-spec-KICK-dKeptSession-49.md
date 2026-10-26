# KICK-dKeptSession-49 — the JS mirror reader takes the inputs it compares from its own code, so a mirror missing the preset store reads stale

**Status:** OPEN · rev-1 · 2026-10-26 · node a · Tier-2 · base 462d20f3 · streams kickoff · order 5 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 |
| [2026-10-26-build-KICK-dKeptSession-49-deviation-491.md](../build/2026-10-26-build-KICK-dKeptSession-49-deviation-491.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of this build's fifteen round-1 promotions
(`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-30-spec-audit.md`)
confirmed finding **id 22 at HIGH**, report item **H3**. Id 48 shares the item and is promoted as
`KICK-dKeptSession-50`, the upgrade path's half; id 9 is the same defect at MEDIUM, item M8, batched
into `KICK-dKeptSession-56`, whose item observes this fix.

`KICK-dKeptSession-40` records `presets.toml` as a mirror input, and its §4 Migration says a mirror
rendered before it "reads it stale once". It does not. dGroundRules' `policy-mirror.js` builds the
list of inputs it compares from `Object.keys(doc.legacy_blobs)` of the stored mirror itself
(`git show 3c8c4718a:tools/policy/policy-mirror.js`, lines 111-118), so a mirror with no
`presets.toml` key never has the store compared and reads FRESH. Every hook that calls `readPolicy`
then serves the old preset values while `policy.py get` answers the new ones: the guard takes its
input list from the state it guards. This unit gives the reader its own expected list. It repairs
`KICK-dKeptSession-40` and builds one step after it (order 5).

## 2. Scope (IN)

- **S1** — id 22. The expected list. `readMirrorAt` in `tools/policy/policy-mirror.js` compares the
  policy file, the kit's catalogue and every path of `MIRROR_KIT_INPUTS`, a new constant holding the
  kit-relative names the reader owes (`["presets.toml"]`), each spelled `<kitRel>/<name>` exactly as
  the catalogue's path already is, together with every key the stored `legacy_blobs` records. A path
  of the expected list that the stored `legacy_blobs` does not hold reads as a differing id, so the
  mirror reads STALE. Observed by AC1 and AC2.
- **S2** — id 22. The sibling text superseded by name. `KICK-dKeptSession-40` S2's "and
  `policy-mirror.js`, which reads every key of `legacy_blobs`, compares it with no edit" and its §4
  Migration sentence read as S1 here: the JS is edited, and a pre-unit mirror reads stale because the
  reader expects the store, not because the mirror names it. Answered in unit 40's acceptance
  ledger. Observed by AC1.

## 3. Non-goals (OUT)

- The Python side. `policy.py mirror --check` compares the whole render (`check_mirror_text`,
  `policy.py:886-903` at `3c8c4718a`), so a pre-unit mirror already reads stale there.
- The upgrade path that re-renders a pre-unit mirror and the parity of the two input lists: id 48,
  `KICK-dKeptSession-50`.
- The report's left-shift checklist entry, that a freshness check takes its expected input list
  from code. No clause of this build names that checklist; AC1 is its arm here.

### Edges

- **consumes-from** `KICK-dKeptSession-40` — the store recorded under `legacy_blobs`, which this unit makes the JS reader expect rather than discover (id 22)
- **hands-off** `KICK-dKeptSession-56` — `MIRROR_KIT_INPUTS` and the stale read of a pre-unit mirror, which the batch's item for id 9, the same defect at MEDIUM, observes

## 4. Design

### Evidence

- `readMirrorAt(top, landed, kitRel)` computes `legacy = Object.keys(doc.legacy_blobs)`, asks
  `git cat-file --batch-check` for `[POLICY_REL, <kitRel>/catalogue.toml, ...legacy]` at the landed
  revision, and sets `legacyStale` only when one of those recorded ids differs (lines 111-118 at
  `3c8c4718a`). `readPolicy` reads STALE on `legacyStale` (line 142).
- The catalogue's path is already spelled from `kitRel` in the reader, so the store's path takes
  the same spelling.

### The check

```
expected := [POLICY_REL, kitRel/catalogue.toml] + [kitRel/<n> for n in MIRROR_KIT_INPUTS] + keys(doc.legacy_blobs)
stale    := any expected path whose recorded id (absent: none) differs from its blob at the landed revision
```

### Inventory

| Minted | Kind | Home |
|---|---|---|
| `MIRROR_KIT_INPUTS` | constant | `tools/policy/policy-mirror.js` |
| `mirror-pre-unit-stale` | fixture case | `tools/policy/check_policy.py` |

### Migration

A mirror rendered before `KICK-dKeptSession-40` lacks the store's key, so this reader reads it
STALE and every key falls through to the reader shim, which answers from `policy.py`, until the
mirror is re-rendered. That is the stale-once the sibling spec meant, now true by construction.

### Files touched (estimate)

- `tools/policy/policy-mirror.js`: S1 in `readMirrorAt`
- `tools/policy/check_policy.py`: the `mirror-pre-unit-stale` case

### Alternatives rejected

- **A schema version field in the mirror.** It works for this one change, but each later input
  needs a second edit to bump it, and the reader would still trust the artefact for the list.
- **The reader running `policy.py` to learn the inputs.** It is a spawn on every hook read, the cost
  the mirror exists to avoid.

## 5. Production-readiness checklist

- security — one more blob id in the one `--batch-check` call; no new process.
- perf / scale — unchanged spawn count per read.
- error / empty / loading states — an absent store at the landed revision reads `missing`, equal to a
  recorded `null`, as an absent legacy input does today.
- observability — the stale reason the reader already prints names the mirror's state.
- risks — every pre-unit mirror reads stale until re-rendered, by design; reads fall through to the
  shim, never to a wrong value.
- testing — the case of §6 and the arm in §7.
- migration — §4.
- user docs — none: `help/policy.md` does not describe the mirror's inputs.

## 6. Acceptance criteria

The fixture is the policy kit's scratch repository under `%TEMP%`, as `KICK-dKeptSession-40` AC2
builds it, with `.governance/policy.json` planted from the unit's render with the `presets.toml`
key removed from `legacy_blobs`, the bytes a pre-unit render writes for that repository.

- **AC1** — When the `mirror-pre-unit-stale` case commits one changed strict value in the kit's
  `presets.toml` and runs `node policy-mirror.js get hooks.bypass`, it reports the mirror stale and
  answers the new value.
  Red when: a copy taking its list from `Object.keys(doc.legacy_blobs)` reads FRESH and answers the
  old value.
- **AC2** — When the same case runs with `presets.toml` unchanged, the read still reports stale.
  Red when: a mirror that omits an input the reader expects reads FRESH because the omitted input
  happens not to have moved.

## 7. Gates

`lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/policy/check_policy.py · covers AC1 AC2 · a planted pre-unit mirror, with and without a changed store, staged red by a copy of `policy-mirror.js` that lists only the mirror's recorded keys · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 promotions' audit, H3 (id 22).

## 10. Reuse audit

The seam extended is `readMirrorAt`'s one `git cat-file --batch-check` call in dGroundRules'
`policy-mirror.js` (lines 111-118 at `3c8c4718a`), with the reader's own `kitRel` spelling of the
catalogue; no second freshness walk is written. `python tools/codebase-map/reuse_lookup.py "inputs a
JSON mirror records so it reads stale when one changes"`, unit 40's probe, ranked name stems only,
and the recall query below surfaced `KICK-dKeptSession-40` itself and TOOL-dGroundRules-31, the
install-day mirror deferral, which compares no input list. The policy kit is not at this base, so no
existing seam in the tree fits and the branch's reader is the one extended.

Recall terms used: `python tools/memory-recall/query.py "how does a freshness check know which
inputs a rendered mirror must record" --terms "mirror stale fresh legacy_blobs inputs policy-mirror
render expected input list artefact"`
