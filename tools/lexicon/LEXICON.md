<!-- gov:kit lexicon@1.1 -->
# LEXICON.md — how to write the table this gate reads

The engine grades against `.lexicon.conf`. This file is how a human decides what goes in it. It is
the counterpart to the kit's `README.md`, which describes the machinery; nothing here is a rule the
gate enforces, and that is deliberate — a vocabulary is a judgement, and the gate only holds you to
the judgement you recorded.

## A verb table is a scoping instrument, not a spelling one

The question the table makes answerable is "which verb is this?", and it is answerable only when the
function does ONE thing. So the table earns its cost at the moment it *fails*: a name that will not
fit is telling you the responsibility is unclear or the seam is in the wrong place. If your reflex
on a refusal is to add a verb, the table is doing nothing — you have converted a design signal into
a synonym list.

## Write the NEGATIVE definitions

A row with only a positive gloss is decoration. The rows that carry weight are the ones pinned by
what they are NOT:

```
build   create a new value and return it — NOT `create`, which is reserved for side-effecting setup
load    read from a store into memory — NOT `fetch`, which implies a network call
remove  detach without destroying — NOT `delete`, which is irreversible
set     assign a known value — NOT `update`, which implies a diff against prior state
```

The pair is what makes the boundary checkable by a reader. Without it, two verbs drift into synonyms
and the table stops being closed in any sense that matters.

## How the table reaches whoever is writing the name

A gate that only REFUSES teaches the table one rejected commit at a time. The failure mode this kit
actually attacks is ABSENCE — an author who would have used your verb if they had known it — so the
declaration is delivered three ways, and none of them is the gate.

- **The rendered Skill.** `adopt-lexicon.sh --render` writes `.claude/skills/lexicon/SKILL.md` from
  the declaration, rows and negatives included, so an agent carries the table without opening the
  conf. Its own gate re-renders and byte-compares, so an edit nobody re-rendered reds.
- **`python tools/lexicon/lexicon.py --suggest <name>`** answers ONE identifier from the declaration
  alone: whether its leading verb is declared, and if not, which row's NOT clause names it and what
  that row means. The suggestion keeps your separator, case, acronyms and digits — it hands back a
  name you can type, not one you have to edit.
- **`python tools/lexicon/lexicon.py --brief <file>`** lists the OBJECTS a file already defines, so a
  new function in it can be named alongside its neighbours rather than against the whole repo.

Read the table when you are naming something, not when a gate stops you.

## Do not inherit somebody else's table

`--scaffold` reads YOUR corpus to decide which concepts are live in it, and takes what each concept
is CALLED from the kit's frozen canon. Inheriting another repo's ratified table skips the first half:
you get somebody else's concept set, which is a vocabulary for a domain you are not in. Seed from
your own corpus, delete what you did not mean, write the negative definitions your domain needs, then
stamp `ratified`.

The seed cannot exceed the canon's cluster count, and is usually well under it — only a concept with
a live definition site enters. That ceiling is `CLUSTERS` in `tools/lexicon/canon.py`; this sentence
deliberately does not restate the number, because the sentence it replaced said "twenty-five verbs is
the seed size" and the canon has never held twenty-five. If curation takes you past forty rows, the
table is describing the code rather than constraining it.

## Banned suffixes

A type named `…Manager` is a type nobody scoped. The seeded eight are prescriptive and safe to
inherit, unlike the verb table. Scope is DEFINITION sites only: a blanket ban breaks on contact with
imported names and with parameters, and Go's `context` is the standing example.

## Layers

`LAYERS` states an intended architecture as a FORBIDDEN DIRECTION, which is the form a machine can
check. There is no derived proposal for it, because a frequency count cannot observe intent. Declare
the direction you actually mean:

```
LAYERS:
  src/core/* -> src/adapters/*
```

An empty `LAYERS` reds. That is not an oversight to work around — it is the difference between a
predicate that is satisfied and one that was never asked.

## Pins are a starting position, not a target

The three offender pins are MEASURED at scaffold and are shrink-only. A non-zero day-one pin is
honest; `ORPHAN_ID_PIN` is the precedent for a pin that is legitimately non-zero on arrival. What the
kit does NOT have is a guard against lowering a pin for the wrong reason — a `probe`-mode extractor
that matches less than it should produces a smaller offender set that looks like repair. The mode is
declared and reported on every run so a reader can see which languages are incomplete, and nothing
refuses the lower automatically. That limit is recorded rather than papered over.
