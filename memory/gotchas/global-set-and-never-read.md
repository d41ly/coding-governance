---
name: global-set-and-never-read
description: a kit script assigns a global on every branch of a function and no line reads it, so the fact it carries reaches no reader and its assignments drift with nothing to catch them
kind: class
universal: false
---

# A global set and never read

## Symptom

A function in a kit script assigns a global on each branch it takes, the header comment names it as
an output, and no other line of the tree reads it. Nothing reds: the value is computed, stored and
dropped. A later edit moves one branch and leaves its assignment saying the old thing, and no reader
notices, because there is none. A reviewer reading the header takes the global for a contract.

## The instance

`read_card_stored` in `skills/session-kickoff/manifest-check.sh` set `CARD_STORED_FROM` to `ref`,
`cache` or `record` on each branch, and `grep -rn CARD_STORED_FROM skills tools` printed only the
lines that assigned it and the comment naming it (dPlacedRequest closing review, round 2, L1).
TOOL-dPlacedRequest-99 S6 gave it its reader: each `card —` success line `write_build_card` prints
in `stored` mode carries ` · tail from <ref|cache|record>`, the store a re-rendered card's tail came
from, which the freshness rule of S4 made the one fact a reader of that card needs.

## The fix

Give the global a reader where the fact is wanted, or delete it with its assignments and its
mention. Either way, a grep for the name prints a line that reads it, or prints nothing.

## Gating

No machine gate: the class belongs to the shell-hygiene checker, another write set, which would need
a per-kit symbol table to tell an assignment from a read. This record is the checklist entry,
claimed by the kickoff engine's codebase-map dossier, so `gotchas.py --for-paths` selects it for a
diff touching the engine.
