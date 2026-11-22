**Serves:** research TOOL-dQuietDisk-28

# Spec task — dQuietDisk: TOOL-dQuietDisk-28, the history store resolves its policy switch once per process

You write specs only, in `memory/builds/dQuietDisk/spec/`. Do not commit. Read these first:

- the spec brief, `memory/builds/dQuietDisk/prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md`. Its rules bind
  this task;
- TOOL-dQuietDisk-1's spec, CLOSED, which built the store;
- the re-grounded specs of TOOL-dQuietDisk-2, -3 and -4, whose section 8 each records the cost as fork F1.

Author `memory/builds/dQuietDisk/spec/2026-11-22-spec-TOOL-dQuietDisk-28.md`, Tier 2, order 3, chain area dWitnessedBar
(Test), base `40def53f`.

## The finding

The order-2 re-grounds measured it, each with `GIT_TRACE2_EVENT`. Every verb of the history store spends about 8 git
processes before it reads or writes an item. Seven of those are the policy read that resolves the store's switch, and
one is a `rev-parse`. A leg that calls the store once per run pays it once. A leg that calls a verb per unit pays it per
unit. Unit 4 measured that its warm run would make 8 or 9 more git processes than the leg makes today.

## The change

- Resolve the store's switch, and anything else each verb asks git for that is constant for the life of a process,
  once per process. Hold it in the process, not in a file.
- The bash face, `tools/lib/history-store.sh`, hands one resolution to every verb a calling shell makes. It may export
  the resolved value to its children, keyed so that a child in another repository or worktree never reads it.
- The three byte-identical copies of `history_store.py` stay byte-identical, and the parity row that checks them still
  holds.
- The switch's default, its allowed values and what each value does are unchanged. A switch the policy reader cannot
  resolve falls back exactly as it does today.

## Acceptance to state

- The count, with `GIT_TRACE2_EVENT` set to an empty directory, of one store verb, and of ten verbs from one process,
  before and after: the after count for ten verbs is at most the before count for one verb, plus one process per item
  read.
- Every existing arm of `python tools/lib/history_store.py --selftest` passes unchanged.
- A child process started from another repository's worktree resolves its own switch, seen red first.
- The policy switch set to off still disables the store, read from the same source as today.

Name the consumers in section 4: units 2, 3 and 4 call the store and gain the saving. Their specs' bounds are upper
limits, so none of them moves. Name the files in Files touched. Unit 1's shell-role row for `tools/lib/history-store.sh`
grows only through `ratchet.py widen shell-role`, as unit 1's did.

## Before you return

- Run `bash tools/unattended/unattended.sh --check-specs dQuietDisk TOOL-dQuietDisk-28`.
- Run `check-memory-hygiene.sh --only 12 --spec <path>` and `python tools/check-spec-tokens.py --spec <path>`.
- Run `python tools/playbook/writing_practice.py check pinned-facts` and `python tools/playbook/positional.py check`
  through whatever your role allows, and mark every figure you quote PINNED, DERIVED or with an id.

Return the spec path, its order and its Files touched.
