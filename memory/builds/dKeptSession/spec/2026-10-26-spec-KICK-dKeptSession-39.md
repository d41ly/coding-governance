# KICK-dKeptSession-39 — `mailbox-message` a typed record kind, served as itself and joined to its file name both ways

**Status:** OPEN · rev-2 · 2026-10-26 · node a · Tier-2 · base 462d20f3 · streams kickoff · order 17 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 |
| [2026-10-26-build-KICK-dKeptSession-39-deviation-391.md](../build/2026-10-26-build-KICK-dKeptSession-39-deviation-391.md) | deviation | — |
| [2026-10-26-review-KICK-dKeptSession-30-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-30-spec-audit.md) | spec-audit | KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-32 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-36 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-41 KICK-dKeptSession-44 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build's spec set
(`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md`)
confirmed finding **id 32 at HIGH**, report item **H6**, which no other id shares.

`KICK-dKeptSession-5` S12 adds a record-factory row whose files are named `-mailbox-message-<n>.md`
and serves them as `**Serves:** journal <anchor id>`, and never adds the kind to `TYPED_RECORD_KINDS`.
PLAY-dOrderedCharter-42 S2 refuses the factory's import when its per-kind table differs from that
tuple, which breaks every kind, the transition log channel the disposal writes through included;
otherwise its S3 reads the records as malformed. This unit makes `mailbox-message` a typed kind in
the reader's one list and serves the records as that kind. It repairs `KICK-dKeptSession-5` and
builds one step after it (order 17).

## 2. Scope (IN)

- **S1** — id 32. The tuple. `TYPED_RECORD_KINDS` in `tools/memory-tree/tree_lib.py`
  (PLAY-dOrderedCharter-42 S1) gains `mailbox-message`, so `RECORD_KIND_TOKENS` carries it through
  that unit's composition and the factory's kind list equals the tuple. Observed by AC1.
- **S2** — id 32. The binding. A mailbox-message record opens `**Serves:** mailbox-message <anchor
  id>`, and the factory row of `KICK-dKeptSession-5` S12 in `tools/memory-tree/build_records.py`
  writes that line. The file-name join of PLAY-dOrderedCharter-42 S3 then holds both ways: a
  `-mailbox-message-<n>.md` file in a `build/` folder serving another kind, and a
  `mailbox-message` record named otherwise, are each malformed. Observed by AC2 and AC3.
- **S3** — id 32. The closed list. The `<kind>` list in `tools/memory-tree/HYGIENE.template.md`
  (lines 627-630 at base) and its dogfood copy `memory/HYGIENE.md` (line 630) name `mailbox-message`
  as a backticked kind, as PLAY-dOrderedCharter-42 AC5 requires of every member. Observed by AC4.
- **S4** — id 32. `KICK-dKeptSession-5` S12's `**Serves:** journal <anchor id>` is superseded by name
  here and answered in that unit's acceptance ledger with AC2's output. Observed by AC2.

## 3. Non-goals (OUT)

- The record's fields and the disposal that writes it: `KICK-dKeptSession-5` S10 and S12.
- The tuple, the factory and the file-name join themselves: PLAY-dOrderedCharter-42 and -7, which
  build before this build run.
- The report's left-shift hygiene check, every factory row's kind in the tuple: PLAY-dOrderedCharter-42
  S2's import refusal is that check.

### Edges

- **consumes-from** `KICK-dKeptSession-5` — S12's factory row for `mailbox-message`, whose Serves kind and tuple membership this unit makes agree (id 32)
- **hands-off** `KICK-dKeptSession-56` — the tuple member, AC1 and §7's legs, the batch's S13, S40 and S26 (ids 11, 26, 35)

## 4. Design

### Evidence

- PLAY-dOrderedCharter-42 S1 defines `TYPED_RECORD_KINDS = ("deviation", "exception", "override",
  "change")` and `RECORD_KIND_TOKENS` as the four base kinds plus that tuple; S2 has
  `build_records.py` import the tuple and refuse a per-kind table that differs; S3 joins
  `-<kind>-<n>.md` to the Serves kind both ways
  (`memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-42.md:35-47`, `:94-95`).
- At this base `tree_lib.py:406` still holds the five-token `RECORD_KIND_TOKENS` and no
  `TYPED_RECORD_KINDS`; `read_bindings` refuses a first token outside it (`:544-565`).
- TOOL-dDeclaredLoop-16 and -17 add `disposition` and `acceptance` to the tuple the same way, and
  -17's criterion is red on a record that "serves as journal" (the audit's reading of origin/main).

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `mailbox-message` | member of `TYPED_RECORD_KINDS` and a Serves kind | none |

### Migration

None: no mailbox-message record exists before `KICK-dKeptSession-5`.

### Files touched (estimate)

- `tools/memory-tree/tree_lib.py`: S1
- `tools/memory-tree/build_records.py`: S2's Serves line
- `tools/memory-tree/HYGIENE.template.md`: S3
- `memory/HYGIENE.md`: S3, the dogfood copy

### Alternatives rejected

- **`journal` as the Serves kind.** PLAY-dOrderedCharter-42 S3 makes the file name and the kind
  agree, so a `-mailbox-message-` file serving `journal` is malformed.
- **A file name outside the typed grammar.** It would hide the record from the kind's readers, the
  wait graph over open questions among them (`cl-dClosedLoop-0328`).

## 5. Production-readiness checklist

- security — none: a closed vocabulary gains one member.
- perf / scale — none.
- error / empty / loading states — a malformed record is named by `read_bindings` with its reason.
- observability — `gen_build_index.py --print-bindings` lists the record with its kind.
- risks — a sibling build adding a typed kind concurrently edits the same tuple; the merge is one
  line each.
- testing — the probes of §6 and the arm in §7.
- migration — none.
- user docs — `memory/HYGIENE.md`, S3.

## 6. Acceptance criteria

- **AC1** — When `python -c "import sys; sys.path.insert(0, 'tools/memory-tree'); import tree_lib,
  build_records; print('mailbox-message' in tree_lib.TYPED_RECORD_KINDS, set(build_records.KINDS)
  == set(tree_lib.TYPED_RECORD_KINDS))"` runs, it prints `True True`.
  Red when: the factory row exists and the tuple lacks the kind, so the import refuses.
- **AC2** — When `python tools/memory-tree/gen_build_index.py --print-bindings` runs over a scratch
  build holding `KICK-dKeptSession-5` AC6's record, it binds that record with kind `mailbox-message`.
  Red when: the record serves `journal` and reads malformed.
- **AC3** — When the same scratch build holds a `-mailbox-message-2.md` record serving `journal`, the
  probe names it malformed with the file-name reason.
  Red when: a mis-served mailbox record binds.
- **AC4** — When `grep -c 'mailbox-message' tools/memory-tree/HYGIENE.template.md memory/HYGIENE.md`
  runs, each file prints at least `1`, the closed list's bullet naming it backticked.
  Red when: the closed list omits a member of the tuple.

## 7. Gates

`kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `build-index selftest` · `memory-hygiene self-test` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/gen_build_index.py · covers AC2 AC3 · its selftest's bindings fixture gains a mailbox-message record served as itself and one served as `journal`, the second staged red against a tuple lacking the kind · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit's H6 (id 32).
- rev-2 · 2026-10-26 · §3 · the Edges bullets to `KICK-dKeptSession-56` mirrored, the other ends of
  the edges the round-1 promotions' audit's disposal declared

## 10. Reuse audit

The seam extended is PLAY-dOrderedCharter-42's `TYPED_RECORD_KINDS` in `tools/memory-tree/tree_lib.py`,
the one list the bindings reader and the record factory share, as TOOL-dDeclaredLoop-16 and -17 extend
it. `python tools/codebase-map/reuse_lookup.py "the closed set of record kinds a Serves line may
name"` ranked `records` (`tools/memory-tree/gotchas.py`), `check_line`, `render_line`,
`extract_records` and `parse_conf_line` by name stem only; none holds a kind list. The list at this
base is `RECORD_KIND_TOKENS` (`tools/memory-tree/tree_lib.py:406`), which DOC-42 composes from the
tuple, so no second list is minted.

Recall terms used: `python tools/memory-recall/query.py "how is a new typed record kind added to the
bindings reader" --terms "TYPED_RECORD_KINDS RECORD_KIND_TOKENS record kind mailbox-message
build_records factory Serves journal file name join"`
