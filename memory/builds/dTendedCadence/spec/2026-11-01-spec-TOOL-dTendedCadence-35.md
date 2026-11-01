# TOOL-dTendedCadence-35 — the maintenance record's key class: every family a sibling mints, one anchored pattern each, held at the write boundary

**Status:** OPEN · rev-2 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 3 · advances TOOL-dTendedCadence-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md) | journal | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 TOOL-dTendedCadence-36 TOOL-dTendedCadence-37 TOOL-dTendedCadence-38 TOOL-dTendedCadence-39 TOOL-dTendedCadence-40 TOOL-dTendedCadence-41 TOOL-dTendedCadence-42 TOOL-dTendedCadence-43 TOOL-dTendedCadence-44 TOOL-dTendedCadence-45 TOOL-dTendedCadence-46 TOOL-dTendedCadence-47 TOOL-dTendedCadence-48 TOOL-dTendedCadence-49 TOOL-dTendedCadence-50 TOOL-dTendedCadence-51 TOOL-dTendedCadence-52 TOOL-dTendedCadence-53 TOOL-dTendedCadence-54 TOOL-dTendedCadence-55 TOOL-dTendedCadence-56 TOOL-dTendedCadence-57 TOOL-dTendedCadence-58 TOOL-dTendedCadence-59 |
| [2026-11-01-prompt-TOOL-dTendedCadence-35-1-spec-writer.md](../prompts/2026-11-01-prompt-TOOL-dTendedCadence-35-1-spec-writer.md) | journal | — |
| [2026-11-01-prompt-TOOL-dTendedCadence-35-promoted-fix-brief.md](../prompts/2026-11-01-prompt-TOOL-dTendedCadence-35-promoted-fix-brief.md) | research | TOOL-dTendedCadence-39 TOOL-dTendedCadence-48 |
| [2026-11-01-review-TOOL-dTendedCadence-35-to-48-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dTendedCadence-35-to-48-spec-audit-round1.md) | spec-audit | TOOL-dTendedCadence-37 TOOL-dTendedCadence-42 TOOL-dTendedCadence-43 TOOL-dTendedCadence-47 TOOL-dTendedCadence-36 TOOL-dTendedCadence-46 TOOL-dTendedCadence-40 TOOL-dTendedCadence-38 TOOL-dTendedCadence-44 TOOL-dTendedCadence-45 TOOL-dTendedCadence-39 TOOL-dTendedCadence-41 TOOL-dTendedCadence-48 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 1 of `reviews/2026-11-01-review-TOOL-dTendedCadence-1-to-18-spec-audit-round1.md`,
HIGH, which shares item H1 with id 39 (TOOL-dTendedCadence-36). Unit 6 holds the record key to two
patterns, `^\d{4}-(\d{2}-\d{2}|W\d{2})$` and `^[a-z0-9][a-z0-9-]*\.[0-9a-f]{12}$`
(spec-6 §4 "The maintenance record", :202-206), and exits 2 on anything else. Unit 2 mints `s-<12hex>`
for `maintain.cadence: every-session` (spec-2 AC3, :241-243) and unit 16 hands the record step
`<period>.<node>` (spec-16 S6, :93-94); both fail both patterns, so those runs never write a record.
This unit makes `maintenance.py` own the whole key class, every family named once with its own
pattern, so every key a sibling mints is admitted and no key is a path.

## 2. Scope (IN)

- **S1** — The table. `RECORD_KEY_FAMILIES` in `tools/drift-audit/maintenance.py`, one row per family,
  each an anchored pattern matched with `re.fullmatch`, per §4 "The families": `daily`, `weekly`,
  `session`, `event` and `node`. Observed by AC1.
- **S2** — The classifier. `derive_record_family(key)` returns the one family whose pattern the key
  fully matches, or None; the patterns are disjoint by construction (§4), so no key matches two.
  `write_maintenance_record` and `python maintenance.py write --key <key>` call it first and exit 2
  on None with `maintenance — refused: key <key> is no record-key family (daily, weekly, session,
  event, node)`, before any write, as unit 6 S6 already exits. Observed by AC1 and AC2.
- **S3** — The planted cases, one per family and the refusals, as the criteria in §6 name them, in
  the drift-audit selftest arm unit 6's §7 already declares. Observed by AC1 and AC2.

## 3. Non-goals (OUT)

- Where each key is minted. `derive_period` (TOOL-dWellOiledMachine-13 S5, ask TOOL-dTendedCadence-29)
  mints the period and session keys, `derive_event_key` (TOOL-dTendedCadence-8 S6) the event key, and
  the per-node lease of ask TOOL-dTendedCadence-32 the node key. This unit admits them and mints none.
- Refusing a key before the walk takes side effects: TOOL-dTendedCadence-36, id 39 of the same item.
- The security review's own record key: TOOL-dTendedCadence-39 adds that family to this table.
- The path grammar beyond the key. `<date>-maintenance-<key>.md` under the home stays unit 6's.

### Edges

- **consumes-from** `TOOL-dTendedCadence-6` — `maintenance.py` and `write_maintenance_record`, whose key check this unit replaces; without them there is no writer to hold the key at
- **hands-off** `TOOL-dTendedCadence-36` — `derive_record_family`, the classifier that unit's walk calls on its key before any item runs
- **hands-off** `TOOL-dTendedCadence-39` — `RECORD_KEY_FAMILIES`, to which that unit adds the security review's family
- **hands-off** `TOOL-dTendedCadence-43` — `RECORD_KEY_FAMILIES`, whose rows that unit gives a run kind
- **hands-off** `TOOL-dTendedCadence-16` — the `node` family, which admits the `<period>.<node>` key its node pass writes the record under
- **hands-off** `TOOL-dTendedCadence-2` — the `session` family, which admits the `s-<12hex>` key an `every-session` run writes the record under
- **hands-off** `TOOL-dTendedCadence-55` — the `node` family, by whose key's node segment that unit groups the records the leg reads (review id 2)
- **hands-off** `TOOL-dTendedCadence-59` — the refusal line's family list, the `node` row's pipe and the `\d` patterns, which the minors batch repairs (review ids 10, 11, 21, 53)

## 4. Design

### The families

| Family | Pattern | Minted by |
|---|---|---|
| `daily` | `\d{4}-\d{2}-\d{2}` | the period key, `2026-11-01` |
| `weekly` | `\d{4}-W\d{2}` | the period key, `2026-W44` |
| `session` | `s-[0-9a-f]{12}` | `every-session`, `s-` and 12 hex of SHA-256 over the session id |
| `event` | `[a-z][a-z0-9-]*\.[0-9a-f]{12}` | `derive_event_key`, `default-branch-red.0123456789ab` |
| `node` | `(\d{4}-\d{2}-\d{2}|\d{4}-W\d{2})\.[a-z0-9][a-z0-9-]{0,62}` | the node pass, `2026-11-01.node-a` |

The patterns are disjoint. `daily` and `weekly` carry no dot. `session` carries no dot and opens with
`s-`, which no period opens with. `event` opens with a letter before its dot, and `node` opens with a
digit, so the two dotted families never share a key. The node segment is lowercase letters, digits
and hyphens, at most 63 characters, the label grammar of a host name, so `.`, `/`, `\` and `..` are
outside every family and no key becomes a path segment other than the file name.

`2026-W44.daily-pc` is therefore a `node` key, and `2026-11-01.0123456789ab` a `node` key whose node
segment is twelve hex: the classifier reads the opening digit, never the tail.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `RECORD_KEY_FAMILIES` | module constant, `maintenance.py` | none |
| `derive_record_family` | function, `maintenance.py` | `py.function`, OK by `lexicon.py --suggest` at writing |

### Files touched (estimate)

- `tools/drift-audit/maintenance.py`: S1, S2
- `tools/drift-audit/selftest.py`: S3
- `tools/drift-audit/README.md`: the maintenance record section names the five families

### Alternatives rejected

- **Units 2 and 16 derive keys the two existing patterns admit.** The node name is not twelve hex and
  the session key has no dot, so each sibling would bend its key to fit a regex it does not own. The
  test: `2026-11-01.node-a` against the event pattern is False, measured by the skeptic of id 39.
- **One permissive pattern, `[0-9A-Za-z.-]+`.** It admits `..` and loses the family a key belongs to,
  which TOOL-dTendedCadence-43 reads to tell a period record from an event record.

## 5. Production-readiness checklist

- security — the write boundary keeps its deny-by-default shape: a key outside the five families exits
  2 before any path is built, and every family excludes `/`, `\` and `..`.
- perf / scale — one `re.fullmatch` per family per write.
- error / empty / loading states — an empty key matches no family and is refused by name.
- observability — the refusal line names the key and the five families.
- risks — a sixth family a later unit mints is refused until it joins the table, which is the intended
  failure: loud at the first write, never a silent path.
- testing — the criteria of §6, in the arm unit 6's §7 declares.
- migration — N/A — no record exists at base; the home is new in this build.
- user docs — N/A — the key class is internal; `help/maintain.md` names no key grammar.

## 6. Acceptance criteria

- **AC1** — When `python maintenance.py write --key <k> --base <sha>` runs in a scratch worktree with
  two in-pin readings on stdin, for each `<k>` of `2026-11-01`, `2026-W44`, `s-0123456789ab`,
  `default-branch-red.0123456789ab`, `2026-11-01.node-a` and `2026-W44.daily-pc`, it writes one file
  under the home named for that key, and `derive_record_family` answers `daily`, `weekly`, `session`,
  `event`, `node` and `node` in turn.
  Red when: a family a sibling mints is refused, or one key is answered by two families.
- **AC2** — When the same command runs with `--key ../escape`, `--key 2026-11-01/x`, `--key
  2026-11-01.Node`, `--key s-0123` or an empty key, it exits 2 with the refusal line naming the five
  families, and `git status --porcelain` shows no file written anywhere.
  Red when: a key reaches the path unvalidated, or an uppercase node segment is admitted.

## 7. Gates

`drift-audit selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/drift-audit/selftest.py · covers AC1 AC2 · one planted key per family and the five refused keys, staged against unit 6's two-pattern check · none

## 8. Open questions

- **F1 — What grammar does a node name take inside the key?** Options: (a) the host-label grammar,
  `[a-z0-9][a-z0-9-]{0,62}`; (b) any non-empty run without `/`, `\` or `.`; (c) the fleet's declared
  node tags only. (b) admits uppercase and spaces into a file name; (c) needs a read of the fleet at
  the write boundary, a second source for a value the lease already carries. RESOLVED (agent,
  2026-11-01, delegated): (a), rung 3, the narrowest grammar that admits every node tag this repo
  writes (`a`, `d`, `node-a`). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 1 (HIGH, item H1) of the round-1 spec
  audit.
- rev-2 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the promoted units of the round-1 spec audit of units 35 to 48 declare toward this unit (units 55 and 59); no scope, design or criterion moved.

## 10. Reuse audit

The seam extended is unit 6's write-boundary key check in `tools/drift-audit/maintenance.py`
(spec-6 §4, :202-206), replaced by a table rather than a third pattern beside the two. `python
tools/codebase-map/reuse_lookup.py "validate a record key at the write boundary so no key becomes a
path"` ranked name stems only (`key`, `write`, `keys`, `write_text`), none a key-family classifier,
and `maintenance.py` does not exist at base, so no existing seam fits beyond unit 6's own. The recall
probe surfaced TOOL-cMendedVintage-19, the ruling that places a promoted repair after the unit it
repairs, which this unit's order follows.

Recall terms used: `python tools/memory-recall/query.py "how is a spec audit finding promoted to a
repair unit placed after the unit it repairs" --terms "spec audit promoted repair unit order hands-off
consumes-from minors batch maintenance record key grammar over-pin"`
