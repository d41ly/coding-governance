**Serves:** research TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8

# Spec task — dQuietDisk: re-ground order 2 on the built order 1

You write specs only, in `memory/builds/dQuietDisk/spec/`. Do not commit. Read these first:

- the owner's ruling, `memory/builds/dQuietDisk/prompts/2026-11-22-prompt-TOOL-dQuietDisk-1-owner-build-on-land-branch.md`;
- the spec brief, `memory/builds/dQuietDisk/prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md`. Its rules bind
  this task.

## The base

Order 1 is built and CLOSED, and dWitnessedBar has landed. `HEAD` carries:
- the merge `b3f5a2bc3`, which brought in dWitnessedBar's land tip `fb6f1a74c`;
- TOOL-dQuietDisk-1, the history verdict store, at `10c54981f` and its red fixes: `tools/lib/history_store.py`, its
  byte-identical copies in `tools/unattended/` and `tools/memory-tree/`, `tools/lib/history-store.sh` and the block it
  adds to `tools/unattended/lib-unattended.sh`;
- TOOL-dQuietDisk-14, the kit attestation, at `69c9c5cb8`;
- the merge `40def53f7` of main at `8b8b1374c`, dWitnessedBar's landing. It brings in the 27 commits [DERIVED: `git rev-list --count fb6f1a74c..8b8b1374c`] past `fb6f1a74c`.
  Among others they change `tools/unattended/check-pass-order.sh`, `tools/unattended/check-brief-recorded.sh`,
  `tools/unattended/lib-unattended.sh` and `tools/run-gates/run-gates.sh`: `git diff fb6f1a74c 8b8b1374c -- <file>`.

Read the code each spec cites as it stands at `HEAD`. The worktree is checked out there, so read files directly.

TOOL-dQuietDisk-2 was re-grounded at `69c9c5cb8` (its rev-4). For it, re-check only what `fb6f1a74c..8b8b1374c`
moved in the files it cites, and record the result as below.

## Re-ground each of units 2, 3, 4, 5, 7 and 8

- **Re-check every code fact.** Re-check each cited path, line, symbol, argv and behaviour at `HEAD`. Where a fact
  moved, re-cite it by symbol or as `<path>@<blob>:<line>`, and change the design to match.
- **Units 2, 3 and 4 consume the store as built, not as unit 1's spec described it.** Read `tools/lib/history_store.py`
  and `tools/lib/history-store.sh` whole. Name the functions, verbs, keys and file layout each unit calls, exactly as
  they are spelled there. Where the built store differs from what a spec assumed, follow the store. Unit 1 is
  CLOSED; a gap in the store is that unit's deviation, and the consuming spec names it in §8 with its pick.
- **Look for work dWitnessedBar already did.** Grep its specs and `git log 59e882afd..fb6f1a74c -- <files>` for each
  unit's files. Where one of its units did part of this unit's work, extend it and say so in §10.
- **State the files.** Each spec's Files touched names every path its pass writes, generated outputs included where
  the pass regenerates them. The main loop declares the union in `--dispatch`.
- **Say which order-2 units share a file.** In each spec's §4, name any other order-2 unit whose Files touched shares
  a path with this one. Same-order units with disjoint files build in parallel; a shared path makes them sequential.
- **Record the re-ground.** Change the header's base to `40def53f`, bump the rev and add a revision-log line:
  `re-grounded at 40def53f7 (order 1 built, dWitnessedBar landed), <what moved>`. Write `nothing moved` where
  nothing did.

Nothing in a unit's goal moves. Where the re-ground changes scope or acceptance, say why in the revision-log line.

## Before you return

- Run `bash tools/unattended/unattended.sh --check-specs dQuietDisk TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8`.
- Run `check-memory-hygiene.sh --only 12 --spec <path>` and `python tools/check-spec-tokens.py --spec <path>` on each
  spec.
- Fix every finding.

Return: each spec with its new rev, what moved, and the order-2 units whose Files touched share a path.
