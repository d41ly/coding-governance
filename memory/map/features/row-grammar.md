# row grammar — one id, one row per document (hygiene check 20)

```toml
feature = "row-grammar"
title = "Check 20: id collisions inside a single row document"
status = "shipped"
streams = ["tooling"]
decisions = []

[claims]
gate-legs = ["row-grammar selftest", "marker contract"]
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
and let a deletion there pass unnoticed. An undeclared pin means ZERO — the strictest value, never a refusal and never off. Refusing one was the first design and it cost every hygiene fixture and every freshly scaffolded adopter a red bar: a default that can only TIGHTEN needs no ceremony.

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

### The marker contract

Four live readers parse the generated-region markers: `apply_region` in the index generator
(Python, writes), `region()` in the unattended checker and in its driver (awk, read), and
`splice()` in the driver (awk, WRITES). The contract is column 0, exact equality after one
trailing CR is stripped, and it lives in the case table of `marker-contract.test.sh` rather than
in any reader's prose. The Python side used to be permissive AND mutating — it accepted an
indented marker and one carrying trailing whitespace, then re-emitted the bare marker, editing a
line the author wrote. The test drives the SHIPPED bytes of each awk reader, sliced out at run
time rather than transcribed, so an edit to a kit moves the verdict.

## Reuse affordance

seam: `id_pattern(conf)` — reuse for building an id matcher from the DECLARED families rather than
importing the recall kit's grammar; extend via the `FAMILIES` key in `.memory-tree.conf`, which is the
one declaration this module and the index generator both read.
seam: `GENERIC_ID` — reuse for a vacuity precondition that must NOT be derived from the thing under
test; extend by widening the family character class, never by rebuilding it from the conf.

## Gaps

- CLOSED by TOOL-aMouldedFolio-5: fence handling delegates to the index generator's reader, so
  `~~~` and marker-matched close come for free, and an unterminated fence is now a named refusal
  naming the file and the opening line. The five shell replicas of `_unfenced` keep the defect —
  they exit 0 with the fence open — and that is a named non-goal, not an oversight.
- CLOSED by TOOL-aMouldedFolio-5: `unkeyed` reports path and line per offender.
- The root is resolved from the tree being audited, but the first cut walked up from the module's own
  location and graded the kit's repo instead. The arm that covers it shells out with a foreign cwd,
  because every other arm passes an explicit root and so cannot reach the resolver at all.
