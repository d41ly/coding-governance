**Serves:** research TOOL-dQuietDisk-1 TOOL-dQuietDisk-14 TOOL-dQuietDisk-9 TOOL-dQuietDisk-19

# Spec task — dQuietDisk: re-ground order 1 on the new build base, fold ask 27 into unit 9, unit 19 last

You write specs only, in `memory/builds/dQuietDisk/spec/`. Do not commit. Read these first:

- the owner's ruling, `memory/builds/dQuietDisk/prompts/2026-11-22-prompt-TOOL-dQuietDisk-1-owner-build-on-land-branch.md`;
- the spec brief, `memory/builds/dQuietDisk/prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md`. Its rules bind
  this task.

## The new base

The run branch now holds the merge `b3f5a2bc3`. It brings in dWitnessedBar's land tip `fb6f1a74c`: its units built at
orders 23 to the end, its closing-review promotions up to TOOL-dWitnessedBar-110, its red fixes, and its prepared
merge `685a7a522` onto origin/main `c2a407b03`.

Every spec was written against `59e882afd`. Read the code each spec cites as it stands at `b3f5a2bc3`, which is
`HEAD`. The worktree is checked out there, so read files directly.

## 1. Re-ground TOOL-dQuietDisk-1 and TOOL-dQuietDisk-14 (order 1)

For each of the two specs:

- **Re-check every code fact.** Re-check each cited path, line, symbol, argv and behaviour at `HEAD`. Where a fact
  moved, re-cite it as `<path>@e4699ee75:<line>` or by symbol, and change the design to match.
- **Look for work dWitnessedBar already did.** Check whether a dWitnessedBar unit after `59e882afd` already did part
  of this unit's work. Grep its specs and `git log 59e882afd..fb6f1a74c -- <files>`.
  - Unit 1: a store or cache of history verdicts, a `cat-file --batch` helper in `tools/lib/`, or `verdict_flow.py`.
  - Unit 14: a self-test attestation, a held-leg record or a kit tree hash.
  - Where one did, extend it and say so in §10. Never write a parallel store.
- **Record the re-ground.** Bump the rev and add a revision-log line: `re-grounded at b3f5a2bc3 (dWitnessedBar's land
  tip merged), <what moved>`. Write `nothing moved` where nothing did.

## 2. TOOL-dQuietDisk-9 absorbs ask TOOL-dQuietDisk-27

The ask is in `memory/builds/dQuietDisk/BACKLOG.md`. The incms fix-4 session found two gaps in the runner's owned
temp root.

**(1)** `run-gates.sh` exports only `TMPDIR`, and a native Windows child reads `TEMP`/`TMP`. The fix:
- export `TEMP` and `TMP` to the same owned root;
- add a criterion observing a native `node -e "console.log(require('os').tmpdir())"` child landing under it.

**(2)** Nested under an adopter runner that exports its own owned `TMPDIR`, run-gates takes the outer scratch as its
ambient root. The fix:
- read an exported outer ambient root, when one is exported, for its `tmpdir_entries` count and its dead-work sweep;
- otherwise keep today's behaviour.

Name the variable. incms `scripts/gate.sh` will export it, so state its exact name in §2 and in an acceptance
criterion. Check the lexicon for the name: `python tools/lexicon/lexicon.py --suggest <NAME> --as constant`, or the
cell the lexicon names for an environment variable.

Add `closes TOOL-dQuietDisk-27` to unit 9's status header, and put both gaps in its Scope and §6. Re-ground unit 9 at
`HEAD` as section 1 describes. Bump the rev and add a revision-log line naming ask 27 and this task.

## 3. TOOL-dQuietDisk-19 moves to the last order

Change its `order 5` to `order 7`, after unit 9 at order 6. Then:
- drop the limit that says units 17 and 9 are not measured;
- restore AC3's late-commit check over every order below 7;
- re-ground it at `HEAD` as section 1 describes. Its B0 readings are being taken at `b3f5a2bc3` right now, so its
  Shas section's B0 row is that commit.

Bump the rev and add a revision-log line.

## Before you return

- Run `bash tools/unattended/unattended.sh --check-specs dQuietDisk TOOL-dQuietDisk-1 TOOL-dQuietDisk-14 TOOL-dQuietDisk-9 TOOL-dQuietDisk-19`.
- Run `bash tools/memory-tree/check-memory-hygiene.sh --only 12 --spec <path>` on each spec you touched.
- Run `python tools/check-spec-tokens.py --spec <path>` on each spec you touched.
- Fix every finding.

Return: the specs you changed with their new revs, what moved for each, any dWitnessedBar overlap you found, and the
variable name unit 9 chose.
