# policy — one file for a repository's policy, and the catalogue that is its schema

A repository's policy lives in ONE file, `.governance/policy.toml`, TOML 1.0, read through `tomllib`
and never sourced. This kit owns that file's schema: the catalogue `catalogue.toml`, one `[[key]]`
row per policy key, taken row for row and in order from the design's `[policies]` table, each row's
`name` and `owner` that table's own. Contract: TOOL-dGroundRules-1.

The kit lands dark: nothing reads `.governance/policy.toml` yet. The reader, the resolution order,
the invalid-file branch, the JSON mirror and the guard are later units of dGroundRules, and each
re-points one consumer.

## Files

| File | What it is |
|---|---|
| `catalogue.toml` | the schema: one row per key |
| `unsummarised-keys.txt` | GENERATED, shrink-only: the rows with no `summary` or no `usage` |
| `policy.py` | the module: `load_catalogue`, `check_value`, `check_shape`, `derive_unsummarised`, `resolve_compare_base`, and the `lists` and `scaffold` verbs |
| `check_policy.py` | the arms' home: `ARMS` over a repository, and `--fixture`, which runs `CASES` |
| `adopt-policy.sh` | the adopter: `--scaffold` and `--check` |

## A catalogue row

```toml
[[key]]
name = "budgets.enforce"          # the design's Key cell, verbatim
allowed = ["warn", "refuse"]      # the grammar below
default = "warn"                  # a TOML value, or { derived = "<the design's Default cell>" }
summary = "Whether a size cap's breach warns or refuses, for every cap not pinned."
usage = 'budgets.enforce = "refuse"'
owner = "dGroundRules"            # the design's Owner cell
```

Required: `name`, `allowed`, `default`, `owner`. Optional: `empty`, `summary`, `usage`, `registry`,
`direction`. Any other field is refused by the shape audit.

A `name` is dotted segments of `[A-Za-z0-9_-]+`; a segment may be a placeholder `<word>`, or `*` as
the last segment. A placeholder or `*` matches exactly one segment of a file key, and an exact name
outranks a placeholder name. File keys are compared as segment tuples, never as joined strings,
because a quoted segment such as `budgets."AGENTS.md"` carries a dot.

## The `allowed` grammar

| The design's cell | `allowed` |
|---|---|
| a closed list of words or numbers | `["a", "b"]`, `[1, 2, 3]` |
| a list ending "or a registered X" | `{ type = "enum", of = [...], registry = "<X>" }` |
| a subset, a set, one or more, none or a set | `{ type = "set", of = [...] }` or `{ type = "set", item = "<regex>" }`, plus `empty` |
| an ordered list | `{ type = "list", ... }`, plus `empty` |
| each of named members, on or off | `{ type = "map", of = ["on", "off"] }` |
| a retry, round, route-back or agent count | `{ type = "retry-count" }`, `round-count`, `route-back-count` or `agent-count`, with `min`, `max` |
| any other count | `{ type = "count", min = 0 }` |
| hours, days or seconds | `{ type = "hours" }`, `days` or `seconds`, with `min` |
| a formatted string | `{ type = "pattern", regex = "<regex>" }` |
| the values another surface defines | `{ type = "name", item = "<regex>", registry = "<the design's words>" }` |

A typed value may also carry `or`, literal alternatives such as `["all"]`, and a count may carry
`pattern`, an alternative string form such as `flow.rework-budget`'s `<base>+<per-unit>`. Counts are
TOML integers, durations TOML numbers. A set-valued row (`set` or `list`) declares `empty = "never"`
or `empty = "allowed"`, and only a set-valued row declares it.

The value check denies by default: a member outside a closed list is refused even where `registry`
names members a registry will add, because no registry exists yet. A cross-key rule the design states
in prose, such as a round count held at or below `review.max-rounds`, is its owning build's to check.

## The CLIs

- `python <prefix>/policy/check_policy.py [--repo <dir>]` — every arm over the repository, the git
  top level of the working directory by default. One line per arm,
  `policy-check: <arm> · <n> finding(s) · <population>`, then each finding. A population of zero is
  a finding. Exit 0 green, 1 red.
- `python <prefix>/policy/check_policy.py --fixture` — one scratch repository per case under the
  system temp directory (`pol-` prefix): each case plants its break, its arm must red naming the
  planted key, and the unplanted copy must be green. It ends with an executed-assertion count.
- `python <prefix>/policy/policy.py lists --check` — red on a row the catalogue owes and the list
  lacks, a row the list carries that the catalogue no longer owes (stale), and a row the list at the
  compare base did not carry. The base is the merge-base of HEAD and the remote default branch where
  that is a proper ancestor of HEAD, else the remote tip; no fetched ref is no base, and a list
  absent at the base is no comparison, never an empty one. Exit 0 green, 1 red, 2 usage.
- `python <prefix>/policy/policy.py lists --write` — drain the list: it keeps the rows the catalogue
  still owes and never adds one. An absent list is seeded with every owed row.
- `python <prefix>/policy/policy.py scaffold` — print the starter policy file: each row this kit's
  build owns that has a literal default, one table per first segment.

## The arms

| Arm | Reads | Finds |
|---|---|---|
| `arm_schema` | `.governance/policy.toml`, the catalogue | each key `check_value` refuses, each key no row matches |
| `arm_shape` | the catalogue | a set-valued row with no `empty`, `empty` on any other row, a missing required field, an unknown field, a literal default or a `usage` its own row refuses, a `usage` that does not parse |
| `arm_summaries` | the catalogue, the list, the list at the base | each `lists --check` finding |

The fixture's cases: one `schema-empty-<name>` per never-empty row, then `shape-no-empty`,
`shape-unknown-field`, `usage-out-of-set`, `summary-new-key`, `usage-new-key` and `list-grew`.

## The adopter

`bash <prefix>/policy/adopt-policy.sh --scaffold [--target <repo>]` writes `.governance/policy.toml`
from the scaffold only where no file exists, and says "kept" otherwise: the file is the
repository's own from its first write. `--check [--target <repo>]` runs `check_policy.py --repo`.
The `policy check` leg ships to adopters; `policy fixtures` is gov's own.

## What this kit does not check

It proves each file key is a value its row admits and each row is well formed. It does not prove a
row's `allowed` and `default` say what the design means: that is the build's acceptance probe, which
compares the catalogue with the design's table. Nothing reads the file yet, so a valid value changes
no behaviour until a later unit re-points its consumer.
