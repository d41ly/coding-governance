# KICK-dKeptSession-39 — `mailbox-message` a typed record kind, served as itself and joined to its file name both ways

**Status:** DEFERRED · rev-3 · 2026-11-21 · node a · Tier-2 · base c2a407b0 · streams kickoff · order 17 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-39-deviation-391.md](../build/2026-10-26-build-KICK-dKeptSession-39-deviation-391.md) | deviation | — |
| [2026-11-21-build-KICK-dKeptSession-45-reground-orders-14-19-returns.md](../build/2026-11-21-build-KICK-dKeptSession-45-reground-orders-14-19-returns.md) | research | KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-28 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-51 KICK-dKeptSession-36 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-1 |
| [2026-10-26-prompt-KICK-dKeptSession-1-parents-crosscheck.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-parents-crosscheck.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-20 KICK-dKeptSession-22 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-11-21-prompt-KICK-dKeptSession-1-build-brief-2.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-build-brief-2.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-33 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-4 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-20 KICK-dKeptSession-32 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-30 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-36 KICK-dKeptSession-51 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-43 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-17 KICK-dKeptSession-61 KICK-dKeptSession-18 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-33 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-4 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-20 KICK-dKeptSession-32 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-30 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-36 KICK-dKeptSession-51 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-43 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-17 KICK-dKeptSession-61 KICK-dKeptSession-18 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-11-21-prompt-KICK-dKeptSession-5-orders-16-17-reground-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-5-orders-16-17-reground-brief.md) | research | KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-51 |
| [2026-10-26-review-KICK-dKeptSession-30-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-30-spec-audit.md) | spec-audit | KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-32 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-36 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-41 KICK-dKeptSession-44 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build's spec set
(`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md`)
confirmed finding **id 32 at HIGH**, report item **H6**, which no other id shares.

`KICK-dKeptSession-5` S12 adds a record-factory row whose files are named `-mailbox-message-<n>.md`.
The factory refuses its own import when its per-kind table differs from `TYPED_RECORD_KINDS`, which
breaks every kind, the transition log channel the disposal writes through included; and the bindings
reader reads a record named for one kind and serving another as malformed. At base c2a407b0 both of
those rules are landed (PLAY-dOrderedCharter-42), `write_record` writes each record's Serves line as
its own kind, and unit 5 S12 now lands the tuple member with its row (F1). What is left is the
hygiene guide's closed `<kind>` list, which names every typed kind, and the observations that the
kind binds as itself. It builds one step after `KICK-dKeptSession-5` (order 17).

## 2. Scope (IN)

- **S1** — id 32. The tuple, observed. `KICK-dKeptSession-5` S12 adds `mailbox-message` to
  `TYPED_RECORD_KINDS` (`tools/memory-tree/tree_lib.py#TYPED_RECORD_KINDS`) in the commit that adds its
  `KINDS` row (`tools/memory-tree/build_records.py#KINDS`), so `RECORD_KIND_TOKENS` carries it and the
  factory's import holds. Satisfied by that unit and reduced to its observation (F1). Observed by AC1.
- **S2** — id 32. The binding, observed. `write_record` writes `**Serves:** <kind> <unit>` for the kind
  it is handed (`tools/memory-tree/build_records.py#write_record`), and `read_bindings` joins a typed
  record's file name to its Serves kind both ways (`tools/memory-tree/tree_lib.py#read_bindings`), so
  a `-mailbox-message-<n>.md` file serving another kind, and a `mailbox-message` record named
  otherwise, are each malformed with no code added. Satisfied by landed code and reduced to its
  observation. Observed by AC2 and AC3.
- **S3** — id 32. The closed list. The `<kind>` bullet of `tools/memory-tree/HYGIENE.template.md`'s
  "Record bindings — how a record names its spec" section, and its dogfood copy `memory/HYGIENE.md`,
  name `mailbox-message` as a backticked kind with a half-line naming its fields, as each typed kind's
  entry does; and the bullet's count of the typed kinds after `research` becomes a pointer to
  `TYPED_RECORD_KINDS`, so a later kind moves no count in prose. Observed by AC4.

## 3. Non-goals (OUT)

- The record's fields, its reader and the disposal that writes it: `KICK-dKeptSession-5` S10 and S12.
- The tuple member and the factory row: `KICK-dKeptSession-5` S12 (F1).
- The tuple, the factory, the Serves line and the file-name join themselves: PLAY-dOrderedCharter-42
  and -7, landed.
- A bindings fixture case of its own: the factory's `typed-kinds` plant already writes and binds one
  record of every kind of the tuple, and `gen_build_index.py`'s selftest holds the mis-served typed
  record case, so a mailbox case would gate an instance of a class those arms hold.
- The report's left-shift hygiene check, every factory row's kind in the tuple: the factory's import
  refusal is that check.

### Edges

- **consumes-from** `KICK-dKeptSession-5` — S12's factory row and its `TYPED_RECORD_KINDS` member, whose closed-list entry in the hygiene guide this unit writes (id 32)
- **hands-off** `KICK-dKeptSession-56` — AC1's observation of the tuple member and §7's legs, the batch's S13, S40 and S26 (ids 11, 26, 35)

## 4. Design

### Evidence

- `TYPED_RECORD_KINDS` holds twelve kinds at base c2a407b0 (DERIVED: `python -c "import sys;
  sys.path.insert(0, 'tools/memory-tree'); import tree_lib; print(len(tree_lib.TYPED_RECORD_KINDS))"`),
  `RECORD_KIND_TOKENS` is the four base kinds plus that tuple, and `build_records.py` raises
  `ImportError` naming each kind where `KINDS` and the tuple differ.
- `read_bindings` refuses a typed record whose file-name kind and Serves kind differ, its malformed
  reason naming the record as the other kind; `gen_build_index.py`'s selftest holds that case over a
  `-deviation-1.md` file serving `research` (`tools/memory-tree/gen_build_index.py#cmd_selftest`).
- The factory's `typed-kinds` plant writes one record of every tuple kind through `write_record` and
  asserts each binds and `--print-bindings` prints no `A` row
  (`tools/memory-tree/build_records.py#KINDS`, the module's "ONE KIND LIST" paragraph); the hygiene
  self-test runs it (`tools/memory-tree/check-memory-hygiene.test.sh`, the PLAY-dOrderedCharter-42 S4
  case).
- The closed list's bullet ends by counting the typed kinds after `research`, a count each new kind
  moves by hand and that no gate compares to the tuple (PLAY-dOrderedCharter-42 AC5 is a probe).

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `mailbox-message` | a closed-list entry of the hygiene guide | none |

### Migration

None: no mailbox-message record exists before `KICK-dKeptSession-5`.

### Files touched (estimate)

- `tools/memory-tree/HYGIENE.template.md`: S3
- `memory/HYGIENE.md`: S3, the dogfood copy

### Alternatives rejected

- **`journal` as the Serves kind.** The file-name join makes the file name and the kind agree, so a
  `-mailbox-message-` file serving `journal` is malformed.
- **A file name outside the typed grammar.** It would hide the record from the kind's readers, the
  wait graph over open questions among them (`cl-dClosedLoop-0328`).
- **Keeping the count and moving it to thirteen.** It is a second statement of the tuple's length,
  stale at the next kind any build adds.

## 5. Production-readiness checklist

- security — none: a closed vocabulary's guide gains one member.
- perf / scale — none.
- error / empty / loading states — a malformed record is named by `read_bindings` with its reason.
- observability — `gen_build_index.py --print-bindings` lists the record with its kind.
- risks — a sibling build adding a typed kind concurrently edits the same bullet; the merge is one
  entry each, and no count moves.
- testing — the probes of §6; the arms are the landed ones §3 names.
- migration — none.
- user docs — `memory/HYGIENE.md`, S3.

## 6. Acceptance criteria

- **AC1** — When `python -c "import sys; sys.path.insert(0, 'tools/memory-tree'); import tree_lib,
  build_records; print('mailbox-message' in tree_lib.TYPED_RECORD_KINDS, set(build_records.KINDS)
  == set(tree_lib.TYPED_RECORD_KINDS))"` runs after `KICK-dKeptSession-5` lands, it prints `True True`,
  the import of `build_records` itself exiting 0 being the factory's own refusal not firing.
  Red when: the factory row exists and the tuple lacks the kind, so the import refuses.
- **AC2** — When `python tools/memory-tree/gen_build_index.py --print-bindings` runs over a scratch
  build holding `KICK-dKeptSession-5` AC6's record, it binds that record with kind `mailbox-message`.
  Red when: the record serves `journal` and reads malformed.
- **AC3** — When the same scratch build holds a `-mailbox-message-2.md` record serving `journal`, the
  probe names it malformed with the file-name reason.
  Red when: a mis-served mailbox record binds.
- **AC4** — When `grep -c 'mailbox-message' tools/memory-tree/HYGIENE.template.md memory/HYGIENE.md`
  runs, each file prints at least `1`, the closed list's bullet naming it backticked, and
  `grep -n 'TYPED_RECORD_KINDS' tools/memory-tree/HYGIENE.template.md` finds the bullet's pointer.
  Red when: the closed list omits a member of the tuple, or still counts them.

## 7. Gates

`kit/dogfood doc parity` · `memory-hygiene self-test` · `build-index selftest` · `recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

## 8. Open questions

- **F1 — Which unit adds `mailbox-message` to `TYPED_RECORD_KINDS`?** Options: (a)
  `KICK-dKeptSession-5` S12, in the commit adding its `KINDS` row; (b) this unit, at order 17, as rev-2
  had it; (c) this unit first, beside a declared-pending `KINDS` entry naming unit 5. (b) leaves unit
  5's commit refused at the factory's import, every typed kind with it, until order 17; (c) blocks
  unit 5's own disposal records, since `write_record` refuses a pending kind.
  RESOLVED (agent, 2026-11-21, delegated): (a), rung 1; the import check in
  `tools/memory-tree/build_records.py` makes the row and the member one commit, and
  `KICK-dKeptSession-56` S13 already lands them in one write set in unit 5's pass. widens: none ·
  relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit's H6 (id 32).
- rev-2 · 2026-10-26 · §3 · the Edges bullets to `KICK-dKeptSession-56` mirrored, the other ends of
  the edges the round-1 promotions' audit's disposal declared
- rev-3 · 2026-11-21 · §1 · S1 S2 S3 · §3 · §4 · §5 · AC1 AC4 · §7 · §8 F1 · §10 · re-grounded on base
  c2a407b0 by brief 2026-11-21-prompt-KICK-dKeptSession-5-orders-16-17-reground-brief:
  PLAY-dOrderedCharter-42 is landed, its line citations re-cited by symbol. Narrowed: S1's tuple member
  moved to `KICK-dKeptSession-5` S12 under F1, S2's Serves line and join satisfied by landed code,
  both reduced to observations; the old S4, unit 5's `journal` Serves line, dropped as already
  superseded by that unit's rev-8; the `gen_build_index.py` arm dropped for the landed class arms; S3
  replaces the list's count with a pointer to the tuple.

## 10. Reuse audit

The seam is PLAY-dOrderedCharter-42's `TYPED_RECORD_KINDS` (`tools/memory-tree/tree_lib.py#TYPED_RECORD_KINDS`),
the one list the bindings reader and the record factory share, landed with twelve members and each
member's half-line in the hygiene guide's closed list, the bullet this unit extends. `python
tools/codebase-map/reuse_lookup.py "the closed set of record kinds a Serves line may name"` ranked
`records` (`tools/memory-tree/gotchas.py`), `build_records`, `read_records`, `unfenced_lines` and
`write_record` by name stem; `write_record` is the writer S2 observes, and none holds a second kind
list, so no list is minted.

Recall terms used: `python tools/memory-recall/query.py "how is a new typed record kind added to the
bindings reader" --terms "TYPED_RECORD_KINDS RECORD_KIND_TOKENS record kind mailbox-message
build_records KINDS factory Serves journal file name join closed list"`
