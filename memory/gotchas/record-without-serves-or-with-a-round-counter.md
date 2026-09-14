---
name: record-without-serves-or-with-a-round-counter
description: a new build record owes a Serves line and a filename that projects it, and a round counter in that filename mints an id nothing defines
kind: class
---

# A new build record owes a `Serves:` line, and its filename may not mint an id

## Symptom

A record lands in a build folder's `build/`, `prompts/` or `reviews/` and the hygiene leg
reds twice on it. Check 21: no conformant `**Serves:**` line in its head. Check 14: the filename
was written `…-<slug>-1-2.md` to mean "round 2", the recording-filename grammar reads the trailing
number as an ORDINAL, and `<FAMILY>-<slug>-2` is now an id cited by a file and defined by nothing —
a phantom that reaches the build README's derived `ids:` front matter on the next render.

## Where it bit

Carried in the kickoff manifest as a trap after a round-numbered review record put a phantom id
into a build README's front matter. The two obligations are graded by two checks that each name
only their own, so a record fixed for one is re-run for the other. The round-counter form is the
sharper one: the fix for a check-14 red looks like "define the id", and defining it is the wrong
move — the id was never meant to exist.

## The fix

Within the record's first twelve unfenced lines, `**Serves:** <kind> <id> [<id> …]`, with `<kind>`
one of `spec-audit` · `diff-review` · `journal` · `research`; the grammar and its `none — <why>`
escape are `memory/HYGIENE.md`, "Record bindings". Name the file so it PROJECTS the binding —
family, slug, ordinal of the LOWEST id served — and put a round in a suffix that is not a number:
`…-<slug>-1-round2.md`. Check `ids:` on the README after `gen_build_index.py --write`; a phantom
there is the tell.

Gated by hygiene checks 21 and 14 in `tools/memory-tree/check-memory-hygiene.sh`, each for its own
half; the class is that a record satisfies one and trips the other, and the round-counter red
invites the wrong repair.
