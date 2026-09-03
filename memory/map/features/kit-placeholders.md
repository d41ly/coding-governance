# kit placeholders — a declared token is one its own adopter substitutes

```toml
feature = "kit-placeholders"
title = "The join from a descriptor's declared placeholders to its adopter's substitutions"
status = "shipped"
streams = ["tooling"]
decisions = []

[claims]
gate-legs = ["kit placeholders (a declared token its adopter substitutes)", "kit-placeholders self-test"]
kits = []
git-hooks = []
workflow-scripts = []
skill-engines = []
rendered-skills = []
gotcha-classes = []
guides = []
backlog-shards = []
lexicon-verbs = []
[paths]
globs = [
  "tools/check-kit-placeholders.py",
  "tools/check-kit-placeholders.test.sh",
]
```

## Constraints & why

A `[[files]]` rule declares `placeholders = [...]`; the kit's adopter script is what turns those
tokens into values. Nothing joined the two, so a descriptor could declare a token its own adopter
has never heard of and the unresolved `{{TOKEN}}` brace would ship into every adopter's committed
tree. The data was already declared on BOTH sides — this is a join, not a heuristic.

**It is one-directional on purpose: declared is a subset of substituted.** The reverse is
legitimate, because an adopter may substitute into a file no rule declares a placeholder list for.
The reverse is REPORTED by `--list` and gated by nothing.

**It reads the adopter TEXTUALLY and says so in its own header.** Running an adopter inside gov's
tree would write into gov, so the gate greps for the `{{TOKEN}}` spelling instead. A token
substituted through a variable is therefore invisible to it. That is a stated blind spot rather than
an implied one, because a structural check reads as a semantic one to everyone who did not write it.

**THE SPELLING IS ESCAPED, AND THAT IS THE WHOLE TRAP.** Real adopters write the substitution as
`${out//\{\{KIT_DIR\}\}/…}`, with the braces backslash-escaped because bare ones are shell syntax. A
predicate matching only the bare form finds NOTHING in the one file it exists to read. The
pre-wiring run over the real tree caught exactly that: the first draft redded 17 innocent tokens
across five kits and would have blocked every contributor. The self-test's escaped-spelling arm is
what stops it regressing.

**An adopter-less kit must DECLARE that it is one.** `tools/workflows/kit.toml` carries
`argv = []` with a `why_no_adopter` reason — its render is performed by the parity gate's own
`--render` mode. That declared exemption is honoured, counted and NAMED on every run, because an
exemption is not coverage. A kit with no adopter and no stated reason still reds.

## Shared seams

- `tools/govkit/govkit.py`'s `load_toml` — the corpus's one descriptor reader, imported rather than
  re-implemented, so this gate cannot disagree with `govkit` about what a descriptor says.
- The `[adopt]` block's own `argv` — the adopter is RESOLVED from the descriptor rather than guessed
  from a filename convention, so a kit that renames its adopter does not silently fall out of the
  population.
- `memory/project/*.txt` is deliberately NOT used: this gate needs no waiver registry, because every
  exemption it honours is already declared in the descriptor that owns it.

## Reuse affordance

seam: the DECLARED-EXEMPTION read — reuse for any gate whose population contains legitimate
non-participants; extend via the descriptor key that states the reason, and keep the count on the
green line so an exemption can never grow silently.

seam: the escaped-spelling scanner — reuse for any check that must find a token inside shell source
rather than inside data; extend by adding a spelling to the alternation, never by loosening the
token pattern, which is what turns a join into a heuristic.

## Affordances

- `python tools/check-kit-placeholders.py` — the leg. Silent plus exit 0 is compliance.
- `python tools/check-kit-placeholders.py --list` — every kit, both directions, exit 0. The
  authoring aid and the pre-wiring instrument.
- `python tools/check-kit-placeholders.py --root <path>` — grade another tree. It exists for the
  self-test: without it the hermetic arms silently graded the real tree and three of them passed
  because the real tree happens to be green.

## Gaps

- **A variable-substituted token reads as unsubstituted.** The textual read is the ratified trade;
  no adopter does this today and nothing watches for the day one starts.
- **Comments count.** The scanner reads the whole adopter file, so a token named inside explanatory
  prose is counted as substituted. It can only ever add a spurious entry to the REPORTED reverse
  direction, never cause a RED, because the gated direction is declared-subset-of-substituted.
- **It grades declarations, never rendered output.** A brace that survives a real render is the
  adopter's own surviving-placeholder arm, one stage later.
