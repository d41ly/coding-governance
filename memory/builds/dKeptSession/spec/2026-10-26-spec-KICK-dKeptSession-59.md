# KICK-dKeptSession-59 — the JS reader's kit inputs held equal to the Python mirror's by a parity case

**Status:** OPEN · rev-3 · 2026-10-26 · node a · Tier-2 · base 462d20f3 · streams kickoff · order 6 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-59-deviation-591.md](../build/2026-10-26-build-KICK-dKeptSession-59-deviation-591.md) | deviation | — |
| [2026-10-26-review-KICK-dKeptSession-57-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-57-spec-audit.md) | spec-audit | KICK-dKeptSession-58 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-57 KICK-dKeptSession-62 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of this build's twelve round-2 promotions
(`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-45-spec-audit.md`)
confirmed finding **id 10 at HIGH**, report item **H3**. Id 23 shares the item and is promoted as
`KICK-dKeptSession-60`, the rule's half; id 33 is the same defect at MEDIUM, item M16, batched into
`KICK-dKeptSession-62`, whose item widens this unit's case to the whole list.

`KICK-dKeptSession-49` S1 adds a hand-typed JS list, `MIRROR_KIT_INPUTS = ["presets.toml"]` in
`tools/policy/policy-mirror.js`, beside Python's `derive_mirror_inputs` (`KICK-dKeptSession-40` S2).
Its §3 hands "the parity of the two input lists" to `KICK-dKeptSession-50`, which has no item,
criterion or arm for it. The next kit input added on the Python side alone is then recorded by the
render but never expected by the reader, so a mirror rendered before it reads FRESH in JS while
`policy.py get` answers the new value: the defect unit 49 closes, back on the next input. This unit
adds the parity case. It repairs `KICK-dKeptSession-49` and builds one step after it (order 6).

## 2. Scope (IN)

- **S1** — id 10. The case. A fixture case `mirror-input-parity` in `tools/policy/check_policy.py`
  reads `policy-mirror.js`'s text, takes the one `MIRROR_KIT_INPUTS = [...]` array literal by regex
  and parses it as JSON, and asserts that `{derive_kit_rel(n) for n in MIRROR_KIT_INPUTS}` equals
  `set(derive_mirror_inputs()) - set(LEGACY_INPUTS)`, both read from the kit's own `policy.py`. A
  missing or unparseable literal reds the case, never passes it. Observed by AC1 and AC2.
- **S2** — id 10. The sibling text superseded by name. `KICK-dKeptSession-49` §3's second bullet,
  "the parity of the two input lists: id 48, `KICK-dKeptSession-50`", reads as S1 here: this unit
  owns the parity, and unit 50 owns only the upgrade path. Answered in unit 49's acceptance ledger.
  Observed by AC3.

## 3. Non-goals (OUT)

- The repository-relative inputs, `LEGACY_INPUTS`, which the JS reader still discovers from the
  stored mirror: id 33, `KICK-dKeptSession-62`, which extends S1's case to the whole list.
- The rule a later unit follows to add an input: id 23, `KICK-dKeptSession-60`.
- One shared input file both languages read. §4 records why the parity case is taken instead.

### Edges

- **consumes-from** `KICK-dKeptSession-49` — `MIRROR_KIT_INPUTS` in `policy-mirror.js` and §3's parity non-goal, which this unit gates and supersedes (id 10)
- **hands-off** `KICK-dKeptSession-60` — the `mirror-input-parity` case, which that unit's rule paragraph names as the check a new input meets (id 23)
- **hands-off** `KICK-dKeptSession-62` — the `mirror-input-parity` case, which the batch's item for id 33 widens to the repository-relative inputs
- **hands-off** `KICK-dKeptSession-63` — the `mirror-input-parity` case's literal read and §7's leg line, which the batch's S8 and S26 anchor and count and its S13 completes at reconcile (ids 11, 31, 18)
- **hands-off** `KICK-dKeptSession-64` — §4's literal-read sketch, whose ledger answer the batch's S4 reads (id 1)

## 4. Design

### Evidence

- spec-49 S1 mints `MIRROR_KIT_INPUTS` as `["presets.toml"]`, each name spelled `<kitRel>/<name>`;
  its §3 hands the parity to unit 50, and spec-50's S1 to S4 cover only the upgrade re-render.
- spec-40 S2: `derive_mirror_inputs()` returns `LEGACY_INPUTS` plus `derive_kit_rel("presets.toml")`.
- `policy.py` at `3c8c4718a`: `LEGACY_INPUTS = (LEGACY_FANOUT,)` (line 813), its comment telling a
  unit adding an input to add it there (lines 810-812).

### The case

```
js     := json.loads(re.search(r"MIRROR_KIT_INPUTS\s*=\s*(\[[^\]]*\])", text).group(1))
want   := set(policy.derive_mirror_inputs()) - set(policy.LEGACY_INPUTS)
green  := {policy.derive_kit_rel(n) for n in js} == want
```

### Inventory

| Minted | Kind | Home |
|---|---|---|
| `mirror-input-parity` | fixture case | `tools/policy/check_policy.py` |

### Migration

None: the case reads the kit's own two files.

### Files touched (estimate)

- `tools/policy/check_policy.py`: the `mirror-input-parity` case

### Alternatives rejected

- **One input file both languages read.** It moves `derive_mirror_inputs`' list out of dGroundRules'
  `policy.py` into a data file and adds a read to every hook's path; the charter's `[contract]` rule
  is met by a parity gate against a live re-derivation, which S1 is.
- **The JS reader spawning `policy.py` for the list.** A spawn on every hook read, which unit 49 §4
  already rejects.

## 5. Production-readiness checklist

- security — none: the case reads two kit files.
- perf / scale — one regex and one import per run.
- error / empty / loading states — an absent or unparseable literal reds with its reason.
- observability — the red names each input present on one side only.
- risks — a JS literal reformatted across lines still matches, since the regex spans newlines inside
  the brackets; a literal built at runtime would red, which is the safe direction.
- testing — the criteria of §6 and the arm in §7.
- migration — none.
- user docs — none: the case is the kit's own check; unit 60's paragraph names it for maintainers.

## 6. Acceptance criteria

The fixture is the policy kit's own checkout, the case reading `policy-mirror.js` and importing
`policy.py` beside it.

- **AC1** — When `python check_policy.py --fixture mirror-input-parity` runs, it passes.
  Red when: the two kit lists differ.
- **AC2** — When the case runs over a scratch copy of the kit under `%TEMP%` whose
  `derive_mirror_inputs` adds `derive_kit_rel("extra.toml")` to the Python list only, it reds naming
  `extra.toml`.
  Red when: the one-sided addition passes, so a later input is recorded by the render and never
  expected by the reader.
- **AC3** — When unit 49's acceptance ledger is read, its §3 parity non-goal is answered by
  `mirror-input-parity`.
  Red when: the ledger still points the parity at unit 50.

## 7. Gates

`lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The policy kit's `policy fixtures` leg runs the case once dGroundRules has landed it; the arm line
below declares it.

New arm: tools/policy/check_policy.py · covers AC1 AC2 · the parity case, staged red by a scratch kit whose Python list carries an input the JS list lacks · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-2 promotions' audit, H3 (id 10).
- rev-2 · 2026-10-26 · §3 · the Edges bullet to `KICK-dKeptSession-63` mirrored, the other ends of
  the edges the round-3 promotions' audit's disposal declared
- rev-3 · 2026-10-26 · §3 · the Edges bullet to `KICK-dKeptSession-64` mirrored, the other ends of
  the edges the round-4 minors batch's audit's disposal declared

## 10. Reuse audit

The seams reused are `derive_mirror_inputs` and `derive_kit_rel` (`KICK-dKeptSession-40` S1 and S2)
and the kit's `--fixture` case table in `check_policy.py` (`3c8c4718a`, line 4370 onward); the case
re-derives the Python list live rather than copying it. `python tools/codebase-map/reuse_lookup.py
"parity between two hand typed input lists in two languages"` ranked `corpus_inputs`,
`read_id_list` and `read_view_inputs` by name stem, none a cross-language parity; the policy kit is
not at this base, so no existing seam in the tree fits and the branch's case table is the one
extended.

Recall terms used: `python tools/memory-recall/query.py "how is a promoted unit placed when it
repairs an earlier unit's pass" --terms "promoted order pass commit ledger superseded batch minors
hands-off consumes-from parity mirror"`
