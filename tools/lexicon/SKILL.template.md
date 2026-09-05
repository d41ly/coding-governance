---
name: lexicon
description: Answer "what should I call this" from THIS repo's declared naming vocabulary, before writing the name. Use when about to name a new function, method, type, module or CLI subcommand; when a name will not fit and you are tempted to invent a verb; when renaming during a refactor; or when a gate has just refused a name and you need the replacement rather than the refusal. Also use before naming anything in an unfamiliar area, to see how the corpus already spells that concept. Routes through `{{SUGGEST_CLI}} <identifier> --as <cell>`, which takes the SURFACE the name is for, reads the declaration at `{{CONF}}` and the frozen canon beside it, and decides nothing. Do NOT use for ordinary code search — finding a symbol, a caller, a definition or a string is grep's job and this neither replaces nor intercepts it.
---

<!-- gov:kit lexicon@{{KIT_VERSION}} · RENDERED from tools/lexicon/SKILL.template.md — do not edit -->

# The declared lexicon

This repo declares a CLOSED verb table. A function name leads with one of its rows or the gate
refuses it. The table is not about spelling — it is about scoping: **"which verb is this?" is
answerable only when a function does ONE thing**, so a name that will not fit is reporting an unclear
responsibility or a seam in the wrong place. If your reflex on a refusal is to add a verb, the table
has become a synonym list and is buying nothing.

## Ask before you write

```bash
{{SUGGEST_CLI}} <identifier> --as <ext>.<surface>
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

{{VERBS_TABLE}}

## What the gate does with it

`{{GATE_CLI}}` grades every pin as a TWO-SIDED EQUALITY. A count that RISES above the declared pin
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
   the replacement — that is what `{{SUGGEST_CLI}}` prints.
3. **Only then consider the table wrong.** Adding a row is an owner decision and a change to a
   declared vocabulary, not a fix for one call site. Record what would not fit and why.
