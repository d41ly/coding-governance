**Serves:** research TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-5 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26

# Spec task — dQuietDisk: every open spec's figures pinned and its positional references tagged

You write specs only, in `memory/builds/dQuietDisk/spec/`. Do not commit. The specs of units 2 to 19 and 26 are
open. TOOL-dQuietDisk-1 is CLOSED and frozen, so do not touch it.

Unit 1's pass legs read two legs red on this build's specs. Each spec is graded whole, so every pass's legs would
read them red until they are fixed.

## 1. writing practice, pinned-facts

`python tools/playbook/writing_practice.py check pinned-facts` lists each line that quotes a number before a unit
word and carries no pin, for example `1,761 s`, `120 s` or `11,442 files`.

The pin goes on the same line: an id, a `path@<oid>:<n>` citation, `PINNED` or `DERIVED`.
- Use `PINNED` for a figure read from a record or a measurement.
- Use `DERIVED` for one computed from others.
- Reword instead where the figure is not a fact the spec depends on.

The check skips text inside fences and inline code. Do not move a figure into inline code just to hide it.

## 2. positional

`python tools/playbook/positional.py check` lists citations of a section by its number after the build method's
name. Cite each section by its tag instead:
- M2: `doc.build-method#m2-the-spec-set-decompose-detect-classify-act`
- M3: `doc.build-method#m3-forks-the-decision-rule-and-the-limit-of-your-authority`
- M5: `doc.build-method#m5-recall-and-reuse`
- M6: the tag `git grep -o "doc.build-method#m6[a-z0-9-]*"` finds

Give each symbol citation that names a bare basename, such as `` `upgrade_steps.py#blob_at` ``, its full path, such as
`` `tools/govkit/upgrade_steps.py#blob_at` ``.

## Rules

- These are wording changes. Nothing in a spec's design, scope or acceptance moves.
- Bump each changed spec's rev, and add a revision-log line naming this task by its file stem.
- A spec with no hit is not touched.

## Before you return

- Run `writing_practice.py check pinned-facts` and `positional.py check`. Neither may name a dQuietDisk spec of units
  2 to 19 or 26.
- Run `check-memory-hygiene.sh --only 12 --spec <path>` and `check-spec-tokens.py --spec <path>` on each changed spec.
- Run `bash tools/unattended/unattended.sh --check-specs dQuietDisk` with every unit id you touched.

Return: each spec you changed, with its new rev and its hit count before and after.
