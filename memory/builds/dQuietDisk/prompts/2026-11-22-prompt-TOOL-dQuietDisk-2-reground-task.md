**Serves:** research TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8

# Spec task — dQuietDisk: re-ground order 2 on the built order 1

You write specs only, in `memory/builds/dQuietDisk/spec/`. Do not commit. Read these first:

- the owner's ruling, `memory/builds/dQuietDisk/prompts/2026-11-22-prompt-TOOL-dQuietDisk-1-owner-build-on-land-branch.md`;
- the spec brief, `memory/builds/dQuietDisk/prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md`. Its rules bind
  this task.

## The base

Order 1 is built and CLOSED. `HEAD` carries:
- the merge `e4699ee75`, which brought in dWitnessedBar's land tip `ed833f684`;
- TOOL-dQuietDisk-1, the history verdict store, at `09435f431` and its red fixes: `tools/lib/history_store.py`, its
  byte-identical copies in `tools/unattended/` and `tools/memory-tree/`, `tools/lib/history-store.sh` and the block it
  adds to `tools/unattended/lib-unattended.sh`;
- TOOL-dQuietDisk-14, the kit attestation, at `6749bfa8d`.

The six order-2 specs still say `base 609cd40b`. Read the code each one cites as it stands at `HEAD`. The worktree is
checked out there, so read files directly.

## Re-ground each of units 2, 3, 4, 5, 7 and 8

- **Re-check every code fact.** Re-check each cited path, line, symbol, argv and behaviour at `HEAD`. Where a fact
  moved, re-cite it by symbol or as `<path>@<blob>:<line>`, and change the design to match.
- **Units 2, 3 and 4 consume the store as built, not as unit 1's spec described it.** Read `tools/lib/history_store.py`
  and `tools/lib/history-store.sh` whole. Name the functions, verbs, keys and file layout each unit calls, exactly as
  they are spelled there. Where the built store differs from what a spec assumed, follow the store. Unit 1 is
  CLOSED; a gap in the store is that unit's deviation, and the consuming spec names it in §8 with its pick.
- **Look for work dWitnessedBar already did.** Grep its specs and `git log 609cd40b1..ed833f684 -- <files>` for each
  unit's files. Where one of its units did part of this unit's work, extend it and say so in §10.
- **State the files.** Each spec's Files touched names every path its pass writes, generated outputs included where
  the pass regenerates them. The main loop declares the union in `--dispatch`.
- **Say which order-2 units share a file.** In each spec's §4, name any other order-2 unit whose Files touched shares
  a path with this one. Same-order units with disjoint files build in parallel; a shared path makes them sequential.
- **Record the re-ground.** Change the header's base to `6749bfa8`, bump the rev and add a revision-log line:
  `re-grounded at 6749bfa8d (order 1 built), <what moved>`. Write `nothing moved` where nothing did.

Nothing in a unit's goal moves. Where the re-ground changes scope or acceptance, say why in the revision-log line.

## Before you return

- Run `bash tools/unattended/unattended.sh --check-specs dQuietDisk TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8`.
- Run `check-memory-hygiene.sh --only 12 --spec <path>` and `python tools/check-spec-tokens.py --spec <path>` on each
  spec.
- Fix every finding.

Return: each spec with its new rev, what moved, and the order-2 units whose Files touched share a path.
