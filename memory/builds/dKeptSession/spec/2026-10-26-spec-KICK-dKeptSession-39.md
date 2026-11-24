# KICK-dKeptSession-39 — `mailbox-message` a typed record kind, served as itself and joined to its file name both ways

**Status:** CLOSED · rev-6 · 2026-11-23 · node a · Tier-2 · base f81e565e · streams kickoff · order 17 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-39-deviation-391.md](../build/2026-10-26-build-KICK-dKeptSession-39-deviation-391.md) | deviation | — |
| [2026-11-21-build-KICK-dKeptSession-39-1-acceptance-ledger.md](../build/2026-11-21-build-KICK-dKeptSession-39-1-acceptance-ledger.md) | journal | — |
| [2026-11-21-build-KICK-dKeptSession-45-reground-orders-14-19-returns.md](../build/2026-11-21-build-KICK-dKeptSession-45-reground-orders-14-19-returns.md) | research | KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-28 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-51 KICK-dKeptSession-36 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-1 |
| [2026-11-24-build-KICK-dKeptSession-1-runlog-31fbb903.md](../build/2026-11-24-build-KICK-dKeptSession-1-runlog-31fbb903.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 KICK-dKeptSession-67 KICK-dKeptSession-69 KICK-dKeptSession-79 KICK-dKeptSession-80 KICK-dKeptSession-89 |
| [2026-10-26-prompt-KICK-dKeptSession-1-parents-crosscheck.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-parents-crosscheck.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-20 KICK-dKeptSession-22 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-33 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-4 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-20 KICK-dKeptSession-32 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-30 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-36 KICK-dKeptSession-51 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-43 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-17 KICK-dKeptSession-61 KICK-dKeptSession-18 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-11-21-prompt-KICK-dKeptSession-23-precheck-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-23-precheck-brief.md) | research | KICK-dKeptSession-23 KICK-dKeptSession-36 KICK-dKeptSession-51 KICK-dKeptSession-27 |
| [2026-11-21-prompt-KICK-dKeptSession-39-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-39-build-brief.md) | research | — |
| [2026-11-21-prompt-KICK-dKeptSession-5-orders-16-17-reground-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-5-orders-16-17-reground-brief.md) | research | KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-51 |
| [2026-11-22-prompt-KICK-dKeptSession-39-reground-brief.md](../prompts/2026-11-22-prompt-KICK-dKeptSession-39-reground-brief.md) | research | — |
| [2026-11-23-prompt-KICK-dKeptSession-39-1-spec-writer.md](../prompts/2026-11-23-prompt-KICK-dKeptSession-39-1-spec-writer.md) | journal | — |
| [2026-10-26-review-KICK-dKeptSession-30-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-30-spec-audit.md) | spec-audit | KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-32 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-36 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-41 KICK-dKeptSession-44 |
| [2026-11-23-review-KICK-dKeptSession-69-closing-diff-review-round1.md](../reviews/2026-11-23-review-KICK-dKeptSession-69-closing-diff-review-round1.md) | diff-review | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 KICK-dKeptSession-67 KICK-dKeptSession-69 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build's spec set
(`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md`)
confirmed finding **id 32 at HIGH**, report item **H6**, which no other id shares.

`KICK-dKeptSession-5` landed the `mailbox-message` kind at merge 422dcef95. Its S12 row sits in
`tools/memory-tree/build_records.py#KINDS`, read by `read_mailbox_message`, and the member sits in
`tools/memory-tree/tree_lib.py#TYPED_RECORD_KINDS` from the same commit. The factory's import check
and the bindings reader's two-way file-name join already hold for the kind with no code added (S1,
S2). What is left is the hygiene guide's closed `<kind>` list. It names every typed kind except this
one, and it counts sixteen typed kinds against a tuple of seventeen. This unit adds the entry and
turns the count into a pointer to the tuple (S3). It builds one step after `KICK-dKeptSession-5`
(order 17).

## 2. Scope (IN)

- **S1** — id 32. The tuple, observed. `mailbox-message` is a member of
  `tools/memory-tree/tree_lib.py#TYPED_RECORD_KINDS` and a key of
  `tools/memory-tree/build_records.py#KINDS`, so `RECORD_KIND_TOKENS` carries it and the factory's
  import holds. Landed by `KICK-dKeptSession-5` S12 under F1, and reduced to its observation.
  Observed by AC1.
- **S2** — id 32. The binding, observed. `write_record` writes `**Serves:** <kind> <unit>` for the
  kind it is handed (`tools/memory-tree/build_records.py#write_record`). `read_bindings` joins a typed
  record's file name to its Serves kind both ways (`tools/memory-tree/tree_lib.py#read_bindings`).
  So a `-mailbox-message-<n>.md` file that serves another kind, and a `mailbox-message` record with
  any other name, each read as malformed with no code added. Landed code, reduced to its
  observation. The Serves line `write_record` writes for the kind is the factory's `typed-kinds`
  plant's to observe, so this unit's probes hand-write theirs. Observed by AC2 and AC3.
- **S3** — id 32. The closed list. The `<kind>` bullet of `tools/memory-tree/HYGIENE.template.md`'s
  "Record bindings — how a record names its spec" section gains `mailbox-message` as a backticked
  kind with a half-line naming its fields and its writer, as the `card` and `probe-trigger` entries
  do. The bullet's sentence counting the typed kinds after `research` becomes a pointer to
  `TYPED_RECORD_KINDS`, so a later kind moves no count in prose. The dogfood copy
  `memory/HYGIENE.md` is re-rendered from the template and carries the same text. Observed by AC4.

## 3. Non-goals (OUT)

- The record's fields, its reader and the transition writer that writes it: `KICK-dKeptSession-5`
  S10 and S12, landed.
- The tuple member and the factory row: `KICK-dKeptSession-5` S12 (F1), landed.
- The tuple, the factory, the Serves line and the file-name join themselves: PLAY-dOrderedCharter-42
  and -7, landed.
- A grammar section of its own for the kind, like the one "Transition records" has. The factory's
  module docstring holds the field grammar, in its "THE MAILBOX-MESSAGE KIND" paragraph of
  `tools/memory-tree/build_records.py`, and the closed list's half-line names the fields, as the
  `card` entry does.
- No kit version: the lander mints the memory-tree kit's (`tools/push-main.sh@3a5bf825e879:27`).
- A bindings fixture case of its own: the factory's `typed-kinds` plant already writes and binds one
  record of every kind of the tuple, and `gen_build_index.py`'s selftest holds the mis-served typed
  record case, so a mailbox case would gate an instance of a class those arms hold.
- The report's left-shift hygiene check, every factory row's kind in the tuple: the factory's import
  refusal is that check.
- A gate comparing the closed list to the tuple. AC4's probe is that comparison, and gating it is a
  unit of its own; the pointer S3 writes keeps the prose from going stale meanwhile.

### Edges

- **consumes-from** `KICK-dKeptSession-5` — S12's factory row and its `TYPED_RECORD_KINDS` member, whose closed-list entry in the hygiene guide this unit writes (id 32)
- **hands-off** `KICK-dKeptSession-56` — AC1's observation of the tuple member and §7's legs, the batch's S13, S40 and S26 (ids 11, 26, 35)

## 4. Design

### Evidence

All of it was read at HEAD f81e565e, which holds merge 422dcef95.

- `TYPED_RECORD_KINDS` holds seventeen kinds, `mailbox-message` last (DERIVED: `python -c "import
  sys; sys.path.insert(0, 'tools/memory-tree'); import tree_lib; print(len(tree_lib.TYPED_RECORD_KINDS))"`).
  `RECORD_KIND_TOKENS` is the four base kinds plus that tuple. `build_records.py` raises
  `ImportError` naming each kind where the keys of `KINDS` and the tuple differ, and AC1's probe
  prints `True True` today.
- `read_bindings` marks a typed record malformed when its file-name kind and its Serves kind differ.
  Its reason reads `named as a <kind> record, -<kind>-<n>.md in a build/ folder, and its Serves kind
  is <served>, not <kind>`. `gen_build_index.py`'s selftest holds that case over a `-deviation-1.md`
  file serving `research`, in the TOOL-dTrueNorth-4 AC8 arms
  (`tools/memory-tree/gen_build_index.py#cmd_selftest`). The AC2 and AC3 probe prints its `S` and `A`
  rows today. It also prints a `B` row for AC2's record, because no spec H1 in the scratch tree
  defines `KICK-fx-1`.
- The factory's `typed-kinds` plant writes one record of every tuple kind. A kind outside `DOORS`,
  `mailbox-message` among them, goes through `write_record`. The plant asserts each record binds and
  that `--print-bindings` prints no `A` row (`tools/memory-tree/build_records.py#run_fixture`). The
  hygiene self-test runs it in its PLAY-dOrderedCharter-42 S4 case
  (`tools/memory-tree/check-memory-hygiene.test.sh`).
- The closed list's bullet opens at `tools/memory-tree/HYGIENE.template.md@4ca9528c9967:668` and
  names the sixteen typed kinds from `deviation` to `probe`. It has no `mailbox-message` entry. Its
  sentence at `tools/memory-tree/HYGIENE.template.md@4ca9528c9967:686` opens `The sixteen after
  research are the typed kinds`, and no gate compares that count to the tuple. AC4's probe prints
  `['mailbox-message']` and that sentence for each file today.
- `memory/HYGIENE.md` is the template's rendered dogfood copy, not an authored file. The parity
  suite's `--render` writes it from the template, and its DIRECTION paragraph says never to
  hand-edit it (`tools/memory-tree/kit-dogfood-parity.test.sh@ddb1994d86c0:30`). Its bullet and
  count sit at the same lines (`memory/HYGIENE.md@b76a74c0f1e1:668`).

### The text S3 writes

After the `probe` entry's closing parenthesis, and before ` The sixteen after `, the bullet gains
this entry:

```
 · `mailbox-message` (one mailbox message a build's transition disposed, fields `Id`, `From`, `To`,
  `Kind`, `Subject`, `Answers`, `State`, `Reply` and `Ref` and its body in one `~~~~` fenced block,
  written by the loop kit's transition writer)
```

The counting sentence's opening, `The sixteen after` then the backticked `research` then `are the
typed kinds:`, becomes:

```
The typed kinds, `TYPED_RECORD_KINDS` in `{{KIT_DIR}}/tree_lib.py`, are those after `research`:
```

The new sentence must not open with `The` and one word before the backticked `research`, because
AC4's count pattern matches that shape for any count word, the word `kinds` included. The rest of
that sentence, the file-name grammar and the two-way join, stays as it is. The builder
re-wraps the bullet's lines to the guide's width. It then writes the dogfood copy with the parity
suite's `--render` mode (`tools/memory-tree/kit-dogfood-parity.test.sh`), which renders
`{{KIT_DIR}}` as `tools/memory-tree`. That render rewrites all four live copies, and the other three
are already at parity, so `git status --short` names only the two files of Files touched.

### Shipped texts left as they are

- `tools/memory-tree/tree_lib.py#TYPED_RECORD_KINDS`'s comment and the "THE MAILBOX-MESSAGE KIND"
  paragraph of `tools/memory-tree/build_records.py` already name the kind, which unit 5 wrote.
- `WIRE-INTO-PROJECT.md@132794668e69:434` names "the closed list in HYGIENE.md" by reference and
  holds no member or count, so it stays true.
- `help/loop.md@ddaf6f288169:606` and `tools/loop/README.md@0675ad843db2:409` name the record's file
  and its writer, neither of which this unit moves.
- `tools/memory-tree/gen_build_index.py#cmd_latest_records`'s docstring says a kind the tuple gains
  is read with no edit, which the pointer agrees with.
- No `tools/policy/catalogue.toml` summary and no page under `help/` states the closed list, by a
  `git grep` for `probe-trigger` and for `typed kinds` outside `memory/builds/`. So no policy mirror
  moves and no anchor fingerprint is owed.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `mailbox-message` | a closed-list entry of the hygiene guide | none |

### Migration

None: the guide gains prose, and no record is rewritten.

### Files touched (estimate)

- `tools/memory-tree/HYGIENE.template.md`: S3, the authored source
- `memory/HYGIENE.md`: S3, re-rendered by the parity suite's `--render`, never hand-edited

The unit does not edit the unattended driver's script, so it adds no refusal site against that
script's harness-arms ceiling. It adds no suite plant or arm, so no suite floor and no budget row
moves. No kickoff manifest in this tree watches either path.

### Alternatives rejected

- **`journal` as the Serves kind.** The file-name join makes the file name and the kind agree, so a
  `-mailbox-message-` file serving `journal` is malformed.
- **A file name outside the typed grammar.** It would hide the record from the kind's readers, the
  wait graph over open questions among them (`cl-dClosedLoop-0328`).
- **Keeping the count and moving it to seventeen.** It is a second statement of the tuple's length,
  stale at the next kind any build adds.
- **Hand-editing `memory/HYGIENE.md` beside the template.** The parity suite would hold the two
  equal, but the copy is a render, and an edit by hand is the drift that suite exists to catch.

## 5. Production-readiness checklist

- security — none: a closed vocabulary's guide gains one member.
- perf / scale — none.
- error / empty / loading states — a malformed record is named by `read_bindings` with its reason.
- observability — `gen_build_index.py --print-bindings` lists the record with its kind.
- risks — a sibling build adding a typed kind at the same time edits the same bullet; the merge is
  one entry each, and no count moves.
- testing — the probes of §6; the arms are the landed ones §3 names.
- migration — none.
- user docs — `memory/HYGIENE.md`, S3; no page under `help/` states the list.

## 6. Acceptance criteria

- **AC1** — When `python -c "import sys; sys.path.insert(0, 'tools/memory-tree'); import tree_lib,
  build_records; print('mailbox-message' in tree_lib.TYPED_RECORD_KINDS, set(build_records.KINDS)
  == set(tree_lib.TYPED_RECORD_KINDS))"` runs, it prints `True True`. The import of `build_records`
  exiting 0 shows the factory's own refusal does not fire.
  Red when: the factory row exists and the tuple lacks the kind, so the import refuses.
  figure: PINNED, observed `True True` at f81e565e.

The probe for AC2 and AC3 is a scratch git repository under `%TEMP%`. It holds a copy of this tree's
`.memory-tree.conf` and the records below under `memory/builds/fx/build/`, staged with `git add -A`.
`python <this checkout>/tools/memory-tree/gen_build_index.py --print-bindings` runs in it, reading
the staged files and this checkout's `TYPED_RECORD_KINDS`, and exits 0. Each record is a `# m`
heading, a blank line and its Serves line.

- **AC2** — When the scratch repository holds `2026-11-21-build-KICK-fx-1-mailbox-message-1.md`
  carrying `**Serves:** mailbox-message KICK-fx-1`, the probe prints an `S` row for it whose kind
  field is `mailbox-message`. It also prints a `B` row for the same record, naming `KICK-fx-1` as an
  id no spec H1 defines; that row comes from the scratch tree and is not a finding.
  Red when: the tuple lacks the member, so the record reads as an `A` row whose first token is not
  a kind.
  fixture: none in the tree; the probe writes its own repository and removes it.
- **AC3** — When it also holds `2026-11-21-build-KICK-fx-1-mailbox-message-2.md` carrying
  `**Serves:** journal KICK-fx-1`, the probe prints an `A` row for that record reading `named as a
  mailbox-message record, -mailbox-message-<n>.md in a build/ folder, and its Serves kind is
  journal, not mailbox-message`.
  Red when: a mis-served mailbox record binds.
- **AC4** — When `python -c "import sys, re; sys.path.insert(0, 'tools/memory-tree'); import
  tree_lib; q = chr(96); print([(f, [k for k in tree_lib.TYPED_RECORD_KINDS if q + k + q not in b],
  re.findall('The [a-z]+ after ' + q + 'research', b)) for f in
  ('tools/memory-tree/HYGIENE.template.md', 'memory/HYGIENE.md') for b in
  [open(f, encoding='utf-8').read().split('<kind>' + q + ' is closed', 1)[1].split('- ' + q +
  '<id>', 1)[0]]])"` runs, it prints both paths, each beside two empty lists. And
  `grep -n 'TYPED_RECORD_KINDS' tools/memory-tree/HYGIENE.template.md memory/HYGIENE.md` finds the
  bullet's pointer in each file.
  Red when: the closed list omits a member of the tuple, still counts the typed kinds, opens its
  pointer sentence as `The <word> after` the backticked `research`, or the dogfood copy was not
  re-rendered.
  figure: DERIVED, the tuple read at observation time. PINNED at b2303b53b: the probe prints
  `['mailbox-message']` and the sixteen sentence for each file, and over §4's text applied to the
  template, raw and rendered, it prints two empty lists.

## 7. Gates

`kit/dogfood doc parity` · `memory-hygiene self-test` · `build-index selftest` · `recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

No `New arm:` line: the unit adds and moves no arm.

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
- rev-4 · 2026-11-21 · S2 · §3 · AC2 · AC3 · checked for behaviour under
  `2026-11-21-prompt-KICK-dKeptSession-23-precheck-brief`: `--print-bindings` reads the repository
  it runs in, its tracked and staged files, so AC2 and AC3 name the scratch repository, its conf and
  hand-written records, and the `S` and `A` rows a probe over a planted `deviation` pair shows today;
  unit 5 AC6's record is written inside a fixture that removes itself, so AC2 no longer names it; §3
  states the lander mints the kit version. Nothing narrowed: no landed unit since rev-3 touches the
  tuple, the factory or the guide.
- rev-5 · 2026-11-23 · §1 · S1 S2 S3 · §3 · §4 · §5 · AC1 AC2 AC3 AC4 · §7 · §10 · re-grounded on HEAD
  f81e565e by brief 2026-11-22-prompt-KICK-dKeptSession-39-reground-brief: `KICK-dKeptSession-5`
  landed at merge 422dcef95, and the tuple now holds seventeen kinds, not twelve. AC1, AC2 and AC3
  already hold, and AC2 names the `B` row its scratch tree prints. S3 now names the guide's
  "sixteen" sentence and the text that replaces it, and re-renders `memory/HYGIENE.md` through the
  parity suite's `--render` instead of editing it by hand. AC4 now compares the closed list to the
  tuple in both files. §4 cites the `typed-kinds` plant by `run_fixture`, re-pins
  `tools/push-main.sh` at its current blob, and says why each other shipped text naming the kind
  stays true. Nothing narrowed.
- rev-6 · 2026-11-23 · §4 · AC4 · the builder's divergence on run wf_26b710f4-4e9, under the
  main loop's ruling (b): §4's pointer sentence opened `The kinds after` the backticked `research`,
  which AC4's count pattern matches, so AC4 could never print two empty lists. The sentence now
  reads `The typed kinds, ... are those after` the backticked `research`, and §4 says why. AC4's
  pattern is unchanged, and its Red when and figure lines now name that shape and pin the probe at
  b2303b53b. Nothing narrowed.

## 10. Reuse audit

The seam is PLAY-dOrderedCharter-42's `TYPED_RECORD_KINDS` (`tools/memory-tree/tree_lib.py#TYPED_RECORD_KINDS`).
It is the one list the bindings reader and the record factory share, now holding seventeen members,
and the hygiene guide's closed list gives each member a half-line. That bullet is the one this unit
extends. `python tools/codebase-map/reuse_lookup.py "the closed set of record kinds a Serves line may
name"`, re-run at f81e565e, ranked `records` (`tools/memory-tree/gotchas.py`), `build_records`,
`set_env_aside`, `write_record` and `read_records` by name stem. `write_record` is the writer S2
observes, and none of them holds a second kind list, so this unit mints no list.

Recall terms used: `python tools/memory-recall/query.py "how is a new typed record kind added to the
bindings reader" --terms "TYPED_RECORD_KINDS RECORD_KIND_TOKENS record kind mailbox-message
build_records KINDS factory Serves journal file name join closed list"`
