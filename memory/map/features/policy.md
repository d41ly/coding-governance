# policy — one file for a repository's policy, and the catalogue that is its schema

```toml
feature = "policy"
title = "The policy file .governance/policy.toml, the policy kit's catalogue that is its schema, the value check and shape audit over them, and the shrink-only list of keys that carry no summary or usage"
status = "shipped"
streams = ["tooling"]
decisions = ["TOOL-dGroundRules-1"]

[claims]
gate-legs = ["policy check", "policy fixtures"]
kits = ["policy"]
git-hooks = []
harness-hooks = []
workflow-scripts = []
skill-engines = []
rendered-skills = []
gotcha-classes = []
guides = []
backlog-shards = []
lexicon-verbs = []
[paths]
globs = ["tools/policy/**", ".governance/policy.toml", "help/policy.md"]
```

There was no single answer to "what is this repository's policy" (`gap-spine-06`): owner switches
sat in kit confs, gate environments and a bash `KEY=value` parser copied into several hooks. This
kit is where the answer lives. It lands dark: no consumer reads the file until later dGroundRules
units re-point each one.

## Constraints & why

**The catalogue IS the schema, and it is the design's table row for row.** Every row of the design's
`[policies]` table is one `[[key]]` row, in the table's order, with its name and owner verbatim, so
the acceptance probe can compare the two files directly instead of trusting a hand transcription.

**Deny by default.** A member outside a closed list is refused even where the design admits "or a
registered" member, because no registry exists yet; the row's `registry` keeps the design's words
for the build that adds one. Admitting any string would loosen every such key before a registry
could vouch for it.

**File keys are segment tuples.** A quoted TOML segment such as `budgets."AGENTS.md"` carries a
dot, so a joined-string compare would split it. An exact name outranks a placeholder.

**The summary list only shrinks, against the landed revision.** A row with no summary or usage
must be listed, and `lists --check` also reds a row the list at the compare base did not carry, so
a new undocumented key cannot be waved through by listing it beside itself. The compare base is the
map kit's rule, copied because a kit may not import a sibling: no fetched remote ref is no base, and
a list absent at the base is no comparison rather than an empty one.

**Every arm prints its population, and zero is red.** An arm that read nothing cannot pass, and the
fixture asserts each planted break reds NAMING the planted key, so a red for another reason is
`WRONG`, not a pass.

**Kit paths are derived, never spelled.** The fixture places its copy at the kit's own path in its
repository, read from git, because a literal kit segment is wrong at any other install prefix.

## Shared seams

- `resolve_remote` — the remote ladder, inlined byte-identically from `tools/lib/resolve_remote.py`
  and held to it by the resolve-python parity arm.
- `resolve_compare_base` — the map kit's compare base, copied rule for rule because a kit may not
  import a sibling.
- `ARMS` and `CASES` in `check_policy.py` — the seams the later dGroundRules units fill with their
  arms and fixture cases.

## Reuse affordance

seam: `policy.check_value` — reuse for any question of whether a value is one a policy key admits;
extend via a new `type` in the `allowed` grammar, never a second value checker.

seam: `policy.scan_keys` — reuse for any walk of a parsed policy document to its graded keys and the
catalogue rows naming them; extend via the row matcher `read_catalogue_row`, never a joined-string compare.

seam: `policy.resolve` — reuse for any read of a policy key's value, at the landed revision or a
named one, parsed and never sourced; extend via a step named in `RESOLUTION_ORDER`, never a second
order, a second reader or a working-tree read.

seam: `policy.validate` — reuse for any verdict on a whole policy file's text, problems with their
lines; extend via `check_value` for a value rule, never a second judge, and never read a default
for text it refuses (`read_last_valid_value` is the one fallback).

## Gaps

- The value check reads one key at a time: a cross-key rule the design states in prose, such as a
  round count held at or below `review.max-rounds`, is its owning build's to check.
- Names the design spells as a value and as a table at once, such as `leases` and
  `leases.granularity`, cannot both be written to one TOML file; their owning builds decide how.
