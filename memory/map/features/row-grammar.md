# row grammar — one id, one row per document (hygiene check 20)

```toml
feature = "row-grammar"
title = "Check 20: id collisions inside a single row document"
status = "shipped"
streams = ["tooling"]
decisions = []

[claims]
gate-legs = ["row-grammar selftest"]
kits = []
git-hooks = []
workflow-scripts = []
skill-engines = []
rendered-skills = []
gotcha-classes = []
guides = []
backlog-shards = []
[paths]
globs = [
  "tools/memory-tree/row_grammar.py",
]
```

## Constraints & why

The assertion is UNIQUENESS WITHIN A FILE, and the obvious alternative was rejected on measurement.
"Every row parses" is a check that cannot fail here — 137 of 137 rows keyed on the day it shipped —
over a property `merge-rows.py` already enforces at merge time, where it can actually be violated.
Shipping it would have been a second answer to a question another leg answers, and a fixture that
passes by finding nothing. Keyability survives only as the precondition that makes the uniqueness
census meaningful: an id the grammar stops recognising drops silently out of both counts.

Uniqueness had live violations nothing else on the bar could see. `corpus_ids.py`'s collision scan is
scoped to build folders, check 8 does not cover the decision index, and the merge driver's duplicate
guard only runs during a merge — both original collisions arrived by ordinary single-parent commits.
The check found a third on its first exposure to another node's rows during the landing merge.

SCOPE IS PER FILE. Corpus-wide uniqueness would red 19 ids on day one, every one of them the designed
backlog-row-plus-decision-row pair — the shape `corpus_ids.py` refused in writing for the same reason.
NAMED GAP: the live index and its rotated archive are two files, so a row that rotates out and is
re-minted is not caught here.

THE PIN IS A COUNT, NOT A REGISTRY. A membership list would put the offending ids in a second place
and let a deletion there pass unnoticed. An undeclared pin is a refusal, because omitting the key is
the quietest way to disarm a gate.

TWO PREDICATES, DELIBERATELY. The row grammar admits a revision suffix (`-9b`); the roster derivation
in `gen_build_index.py` excludes it. A roster answers "which ids belong to this build", where an
amendment is not a member; a row answers "what is on this line", where it is.

## Shared seams

- `.memory-tree.conf` — `FAMILIES` is the one declaration both this module and the index generator
  build their id patterns from, so neither copies the other.
- `check-memory-hygiene.sh` — delegates check 20 the way it delegates 13-19, so the check costs no
  new gate leg of its own; only its selftest is a leg.
- The vacuity precondition uses a family-INDEPENDENT id shape on purpose. Deriving it from the
  declared families would assert one value against another the same call derives, which is the
  tautology that let the wrong-families arm pass by finding nothing.

## Reuse affordance

seam: `id_pattern(conf)` — reuse for building an id matcher from the DECLARED families rather than
importing the recall kit's grammar; extend via the `FAMILIES` key in `.memory-tree.conf`, which is the
one declaration this module and the index generator both read.
seam: `GENERIC_ID` — reuse for a vacuity precondition that must NOT be derived from the thing under
test; extend by widening the family character class, never by rebuilding it from the conf.

## Gaps

- The fence toggle is a bare boolean and is not checked at EOF, so an unterminated fence hides every
  remaining row in that file, and `~~~` fences are not recognised at all.
- The `unkeyed` assertion is zero-tolerance with no waiver, and it reports a bare count rather than
  the path and line the duplicate branch prints.
- The root is resolved from the tree being audited, but the first cut walked up from the module's own
  location and graded the kit's repo instead. The arm that covers it shells out with a foreign cwd,
  because every other arm passes an explicit root and so cannot reach the resolver at all.
