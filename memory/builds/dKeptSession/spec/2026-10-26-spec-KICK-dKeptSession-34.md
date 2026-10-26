# KICK-dKeptSession-34 — the reader's preset step answers None for a row the preset leaves unassigned, so a derived default reads with source default under every preset

**Status:** OPEN · rev-2 · 2026-10-26 · node a · Tier-2 · base 462d20f3 · streams kickoff · order 4 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 |
| [2026-10-26-build-KICK-dKeptSession-34-deviation-341.md](../build/2026-10-26-build-KICK-dKeptSession-34-deviation-341.md) | deviation | — |
| [2026-10-26-review-KICK-dKeptSession-30-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-30-spec-audit.md) | spec-audit | KICK-dKeptSession-33 KICK-dKeptSession-40 KICK-dKeptSession-32 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-41 KICK-dKeptSession-44 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build's spec set
(`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md`)
confirmed finding **id 2 at HIGH**, report item **H2**. Id 17 is the same defect, found by the
grounding lens, and shares the item; it is promoted as `KICK-dKeptSession-33`. Unit 33 is the store's
rule for the eight derived-default rows, and this unit is the reader's half of the same fix.

`KICK-dKeptSession-2` S1 already says a preset assigning a key no value answers `None`, but its AC3
and S3's `preset-every-key` case require every presettable key to read its preset value with source
`preset`. Under unit 33's rule six derived rows and the `review.<stage>` pattern are assigned in no
preset, so that criterion cannot pass, and a reader built to pass it would write values over the
evidence-derived caps and role efforts. This unit states the step's answer for an unassigned row and
rewrites the case to it. It repairs `KICK-dKeptSession-2` and builds one step after it (order 4).

## 2. Scope (IN)

- **S1** — id 2. The answer. `read_preset_value` answers `None` for every row
  `derive_derived_rows` (`KICK-dKeptSession-33` S1) returns and the named preset's assignment does not
  hold, by path or by the matched row's name, so `read_default_value` answers next with source
  `default`. A derived default keeps dGroundRules' `DerivedDefault` route, so `budgets.*` reads its
  cap's value through that route as it does with no preset named. Observed by AC1 and AC2.
- **S2** — id 2. The case. `preset-every-key` in `tools/policy/check_policy.py` reads each assigned
  key at its preset value with source `preset`, each unassigned derived row at its default with
  source `default`, and each `never` key at its default. Observed by AC1.
- **S3** — id 2. A fixture case `preset-derived-cap`: a policy file setting only `preset = "strict"`,
  then `policy.py get` on one census cap of `budgets.*`. Observed by AC2.
- **S4** — id 2. `KICK-dKeptSession-2` S3's "each presettable key answering its preset's value" and
  AC3's criterion are superseded by name here and answered in that unit's acceptance ledger with
  AC1's output. Observed by AC1.

## 3. Non-goals (OUT)

- Which rows are unassigned: `KICK-dKeptSession-33`'s rule.
- The step's place in the order and its other answers: `KICK-dKeptSession-2`'s, unchanged.
- The mirror's inputs: id 47, item H7, `KICK-dKeptSession-40`.

### Edges

- **consumes-from** `KICK-dKeptSession-2` — `read_preset_value` and the `preset-every-key` case, whose answer for an unassigned row this unit states and whose criterion it rewrites (id 2)
- **consumes-from** `KICK-dKeptSession-33` — `derive_derived_rows` and the unassigned rows, without which the step cannot tell an unassigned derived row from a missing assignment
- **hands-off** `KICK-dKeptSession-54` — `read_preset_value`'s answer for an unassigned derived row and the two cases, whose expectations that unit restates (id 21)
- **hands-off** `KICK-dKeptSession-56` — AC2 and §7's legs, the batch's S38 and S25 (ids 14, 34)

## 4. Design

### Evidence

- `KICK-dKeptSession-2` S1: "A preset that assigns the key no value answers `None`"; its AC3: "every
  presettable key at its preset value with source `preset`" (spec-2 lines 38 and 160-163).
- dGroundRules' `render_mirror` omits a key whose resolution reaches a derived default, which
  raises `DerivedDefault` (`git show 3c8c4718a:tools/policy/policy.py`, `render_mirror` at line
  840, the omission at 863).

### The answers under `preset = "strict"`

| Key | Source | Value |
|---|---|---|
| `hooks.bypass` | `preset` | `refused` |
| `maintain.fixes` | `preset` | `reap`, `regenerate stale` |
| `roles.effort.default` | `default` | its derived default |
| one census cap of `budgets.*` | `default` | the cap's derived value |
| `runtime.agents-in-flight` | `default` | `6`, a `never` key |

### Inventory

| Identifier | Kind | Home |
|---|---|---|
| `preset-derived-cap` | fixture case | `tools/policy/check_policy.py` |

### Migration

None beyond `KICK-dKeptSession-2`'s.

### Files touched (estimate)

- `tools/policy/policy.py`: S1 in `read_preset_value`
- `tools/policy/check_policy.py`: S2 and S3

### Alternatives rejected

- **The step answering the preset's prose for an unassigned row.** It is prose `check_value`
  refuses, and it would hide the derived value.

## 5. Production-readiness checklist

- security — none: a read-only answer in the reader.
- perf / scale — one membership test per read.
- error / empty / loading states — a derived default with no reader keeps dGroundRules' refusal.
- observability — `get --explain` prints source `default` with dGroundRules' reason.
- risks — a reader may expect a preset source for every key; S2's case states the three classes.
- testing — the cases of §6 and the arm in §7.
- migration — none.
- user docs — `help/policy.md`'s order paragraph, `KICK-dKeptSession-2` S4, names the three
  sources; no change.

## 6. Acceptance criteria

- **AC1** — When `python check_policy.py --fixture preset-every-key` runs, each preset's line reads
  its assigned keys with source `preset`, `roles.effort.default` with source `default`, and its
  `never` keys at their defaults.
  Red when: an unassigned derived row reads a `preset` source, or the case reds on one.
- **AC2** — When the `preset-derived-cap` case runs `python policy.py get <cap> --explain` for one
  census cap under `preset = "strict"`, it prints the cap's derived value with source `default`.
  Red when: the cap reads a preset value, or refuses where no preset reads it.

## 7. Gates

`lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/policy/check_policy.py · covers AC1 AC2 · `preset-every-key` rewritten and `preset-derived-cap`, staged by a copy of the step answering a value for an unassigned row · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit's H2 (id 2).
- rev-2 · 2026-10-26 · §3 · the Edges bullets to `KICK-dKeptSession-54`, `KICK-dKeptSession-56`
  mirrored, the other ends of the edges the round-1 promotions' audit's disposal declared

## 10. Reuse audit

The seam extended is `KICK-dKeptSession-2`'s `read_preset_value` in dGroundRules' `RESOLUTION_ORDER`
(`tools/policy/policy.py` at `3c8c4718a`), reading `KICK-dKeptSession-33`'s class rather than a second
list of the rows. `python tools/codebase-map/reuse_lookup.py "policy reader resolution order step
between file and default"`, unit 2's probe, ranked name stems only; the policy kit is not at this
base, so no existing seam in the tree fits.

Recall terms used: `python tools/memory-recall/query.py "what does the preset step answer for a key
whose default is derived" --terms "read_preset_value preset-every-key derived default unassigned
DerivedDefault budgets strict source preset"`
