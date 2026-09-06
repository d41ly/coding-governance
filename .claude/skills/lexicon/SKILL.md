---
name: lexicon
description: Answer "what should I call this" from THIS repo's declared naming vocabulary, before writing the name. Use when about to name a new function, method, type, module or CLI subcommand; when a name will not fit and you are tempted to invent a verb; when renaming during a refactor; or when a gate has just refused a name and you need the replacement rather than the refusal. Also use before naming anything in an unfamiliar area, to see how the corpus already spells that concept. Routes through `python3 tools/lexicon/lexicon.py --suggest <identifier> --as <cell>`, which takes the SURFACE the name is for, reads the declaration at `.lexicon.conf` and the frozen canon beside it, and decides nothing. Do NOT use for ordinary code search — finding a symbol, a caller, a definition or a string is grep's job and this neither replaces nor intercepts it.
---

<!-- gov:kit lexicon@1.1 · RENDERED from tools/lexicon/SKILL.template.md — do not edit -->

# The declared lexicon

This repo declares a CLOSED verb table. A function name leads with one of its rows or the gate
refuses it. The table is not about spelling — it is about scoping: **"which verb is this?" is
answerable only when a function does ONE thing**, so a name that will not fit is reporting an unclear
responsibility or a seam in the wrong place. If your reflex on a refusal is to add a verb, the table
has become a synonym list and is buying nothing.

## Ask before you write

```bash
python3 tools/lexicon/lexicon.py --suggest <identifier> --as <ext>.<surface>
```

One line, no corpus pass. Either `OK`, or the replacement and the negative definition that bans what
you tried:

```
use `load_remote` — the declaration says `load`, NOT `fetch`: read a store into memory
```

**`--as` is REQUIRED and takes the full cell, never a bare surface.** The surface is the whole
question: it decides which predicates are armed on that name and which convention the answer is
spelled in. `--as py.function` answers in snake where the cell declares snake; the same name asked
for as `--as js.function` comes back in camel. Without it the tool would hand you a name in whatever
case you happened to type, which is how it used to suggest names its own gate refuses. A cell with no
`CELLS` row is refused rather than guessed at, and so is a surface with no language on it — the
refusal lists the cells that carry that surface.

It answers ONE identifier from two tables in a fixed precedence — this repo's declaration first,
then the canon the kit ships, asked only where no declared row bans the token by name — and from no
corpus at all. That is the whole point: you can ask before you write, and a verb that walks the
whole tree to answer one question is a verb nobody waits for. It cannot exit 1 and it prints no pin.
It is a report, structurally.

## The table

Each row is a verb, a gloss, and at least one NEGATIVE — the word it is NOT. **The negatives are the
product.** A row with only a positive gloss cannot tell two verbs apart, and the boundary is the
whole point.

- `build` — create a new value and return it — NOT `create`, which is reserved for side-effecting setup
- `load` — read a store into memory — NOT `fetch`, which implies a network call
- `read` — pull bytes or records from a named source — NOT `get`, which says nothing about cost
- `write` — persist to a store — NOT `save`, which hides whether anything was already there
- `parse` — turn text into structure, raising on text that is not that structure — NOT `convert`
- `render` — turn structure into text — NOT `format`, which reads as cosmetic
- `resolve` — turn a name into the thing it denotes, RUNNING the candidate where that is the only proof — NOT `lookup`, a lookup returns a row; resolve returns the thing, RUNNING the candidate
- `check` — assert a predicate and return a verdict — NOT `validate`, which implies mutation on failure
- `scan` — walk a population looking for matches — NOT `search`, which implies stopping at the first
- `extract` — pull a declared shape out of a larger one — NOT `pluck`, pluck names the taking; extract names the declared shape taken
- `measure` — count a population and report the number, deciding nothing — NOT `count`, count is the arithmetic; measure counts a population and decides nothing
- `derive` — compute a value from a source so it never has to be authored — the §5 rule, as a verb — NOT `compute`, compute says a value was produced, not that it never has to be authored
- `seed` — write an initial value the tool will not overwrite again — NOT `install`, install claims the tool owns the result after; a seed is never overwritten
- `init` — set up state at construction — NOT `setup`
- `run` — execute a process to completion and report its outcome — NOT `execute`, the same word twice, and this repo already runs processes
- `arm` — make a dormant check live; its opposite is a check that cannot fail — NOT `enable`, enable reads as a feature flag; arm makes a dormant CHECK live
- `add` — append to an existing collection — NOT `append`, append claims a position at the end; add claims only membership
- `remove` — detach without destroying — NOT `delete`, which is irreversible
- `set` — assign a known value — NOT `update`, which implies a diff against prior state
- `print` — write to stdout for a human — never a return value in disguise — NOT `log`, log implies a level, a sink and a filter; print writes to stdout for a human
- `main` — a module's CLI entry point; reserved, one per module — NOT `start`, start names a lifecycle event; main is a module's one CLI entry point
- `cmd` — a subcommand entry point, dispatched by name; reserved — NOT `do`, which names no role
- `test` — a test function; reserved for harnesses — NOT `assert`, assert is one statement inside a test; test is what a harness collects

## What the gate does with it

`python3 tools/lexicon/lexicon.py` grades every pin as a TWO-SIDED EQUALITY. A count that RISES above the declared pin
reds, and a count that FALLS below it reds just as loudly, printing the exact row to paste — a drain
lands in the declaration or it is not landed. Do not read a red as "somebody added an offender".

Every declared `CELLS` row is graded the same way: `<cell>.conv` counts the names in that cell that
miss its convention, and it is two-sided too, as are the `<cell>.debt` and `<cell>.unruled` rows on
a cell carrying the `vocab` flag.

It also reports, every run, the graded population and offender count PER PREDICATE, and the armed
share of the files that carry a definition at all. A zero there is printed rather than hidden.

Reserved rows behave differently from ordinary ones: `main` is a module's one CLI entry point, `cmd`
a subcommand entry point one level down, and `test` a function a harness collects. They name a
structural role, not an action.

## When a name genuinely will not fit

That is the signal the table exists to produce. In order:

1. **Re-read the function.** Two verbs in the name usually means two functions.
2. **Check the negatives.** The verb you want may be banned BY NAME, and the row that bans it names
   the replacement — that is what `python3 tools/lexicon/lexicon.py --suggest` prints.
3. **Only then consider the table wrong.** Adding a row is an owner decision and a change to a
   declared vocabulary, not a fix for one call site. Record what would not fit and why.