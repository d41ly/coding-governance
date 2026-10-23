# policy — one file for a repository's policy, and the catalogue that is its schema

A repository's policy lives in ONE file, `.governance/policy.toml`, TOML 1.0, read through `tomllib`
and never sourced. This kit owns that file's schema: the catalogue `catalogue.toml`, one `[[key]]`
row per policy key, taken row for row and in order from the design's `[policies]` table, each row's
`name` and `owner` that table's own. Contract: TOOL-dGroundRules-1.

The kit lands dark: one reader reads `.governance/policy.toml`, `policy.py get` (TOOL-dGroundRules-2),
and no consumer calls it yet. The resolution order, the invalid-file branch, the JSON mirror and the
guard are later units of dGroundRules, and each re-points one consumer.

## Files

| File | What it is |
|---|---|
| `catalogue.toml` | the schema: one row per key |
| `unsummarised-keys.txt` | GENERATED, shrink-only: the rows with no `summary` or no `usage` |
| `policy.py` | the module: `load_catalogue`, `read_catalogue_row`, `check_value`, `check_shape`, `derive_bounds`, `check_direction`, `derive_unsummarised`, `resolve_compare_base`, the reader `resolve`, and the `lists`, `scaffold` and `get` verbs |
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
`direction`. Any other field is refused by the shape audit. A loop bound or deadline row must carry
`direction`, below.

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

## Loop bounds and deadlines: `direction`

Every loop ends and every wait expires, so raising a loop bound or a deadline loosens the policy.
Each such row declares it: `direction = "raise-loosens"`, the field's one allowed value
(TOOL-dGroundRules-11). The population is derived, never listed by name: `derive_bounds` selects
each row whose `allowed` is a typed range of a noun in `LOOP_BOUND_TYPES` (`retry-count`,
`round-count`, `route-back-count`) or `DEADLINE_TYPES` (`hours`, `days`, `seconds`). A duration that
bounds no loop, such as a retention window, is in the population too, because over-inclusion fails
safe. A row outside it may carry `direction`, and only `raise-loosens`. `check_direction` reds a
member with no `direction` and any row with another value. Nothing reads the declaration yet: the
owner-silence rule that declines a raise is a later build's reader.

## The CLIs

- `python <prefix>/policy/check_policy.py [--repo <dir>]` — every arm over the repository, the git
  top level of the working directory by default. One line per arm,
  `policy-check: <arm> · <n> finding(s) · <population>`, then each finding. A population of zero is
  a finding. Exit 0 green, 1 red.
- `python <prefix>/policy/check_policy.py --fixture [<case>]` — one scratch repository per case under
  the system temp directory (`pol-` prefix): each case plants its break, its arm must red naming the
  planted key, and the unplanted copy must be green. It ends with an executed-assertion count. A
  `<case>` runs that case alone; a name no case carries is exit 2.
- `python <prefix>/policy/policy.py lists --check` — red on a row the catalogue owes and the list
  lacks, a row the list carries that the catalogue no longer owes (stale), and a row the list at the
  compare base did not carry. The base is the merge-base of HEAD and the remote default branch where
  that is a proper ancestor of HEAD, else the remote tip; no fetched ref is no base, and a list
  absent at the base is no comparison, never an empty one. Exit 0 green, 1 red, 2 usage.
- `python <prefix>/policy/policy.py lists --write` — drain the list: it keeps the rows the catalogue
  still owes and never adds one. An absent list is seeded with every owed row.
- `python <prefix>/policy/policy.py scaffold` — print the starter policy file: each row this kit's
  build owns that has a literal default, one table per first segment.
- `python <prefix>/policy/policy.py get <key> [--rev <rev>] [--explain]` — run in the repository to
  read: the key's value on stdout, a string as itself, a number or a boolean in TOML's spelling, a
  list one member per line, LF-ended. `--explain` adds `policy: <key> · <source> · <reason>` on
  stderr, the reason naming the sha8 and how the revision was found. Exit 0, or 2 with one
  `policy: refused · <path>:<line> · <why>` line.

## The reader

`resolve(key, repo=".", rev=None)` is the one reader every consumer calls, `get` its CLI. It carries
`read_policy_key`'s contract (the unattended kit, `THE POLICY IS READ AT R AND NEVER FROM THE TREE`)
to TOML: the file as committed at a revision, read with `git show`, parsed with `tomllib`, never
sourced and never opened from the working tree. The shell parser and its copies stay as they are
for the legacy homes.

- **The revision.** `rev` given: the commit it names, else a refusal. `rev` absent, the landed
  revision: `refs/remotes/<remote>/<branch>`, the remote and branch the inlined remote ladder
  resolves (`GOV_REMOTE`, the branch's remote, the only remote; `GOV_DEFAULT_BRANCH`, the remote's
  HEAD, else `main`); with no remote at all, the local `refs/heads/<branch>`, which the reason says.
  A ladder refusal is the reader's. Nothing is fetched, so a clone that never fetched reads a stale
  tip, and the reason's sha shows which.
- **The key.** `parse_key` admits one TOML key, bare or quoted segments, and walks tomllib's load of
  `<key> = 0`, so `budgets."CLAUDE.md"` is two segments. `read_catalogue_row` finds its row by the
  name rule above; no row refuses, naming the catalogue.
- **The value.** `parse_policy` maps each leaf's segment tuple to its value; a table is never a
  value. `read_file_value` answers `Resolution(value, "file", reason)` where the file sets the key.
- **Until TOOL-dGroundRules-3 and -4.** An absent file and a key the file does not set refuse, since
  no default is read yet; text that is not TOML refuses naming the decoder's line.
- **Git's environment.** Every git call drops the location variables git exports to a hook
  (`GIT_LOCATION_VARS`), so a reader started inside a hook or a fixture reads the repository it was
  pointed at.

## The arms

| Arm | Reads | Finds |
|---|---|---|
| `arm_schema` | `.governance/policy.toml`, the catalogue | each key `check_value` refuses, each key no row matches |
| `arm_shape` | the catalogue | a set-valued row with no `empty`, `empty` on any other row, a missing required field, an unknown field, a literal default or a `usage` its own row refuses, a `usage` that does not parse |
| `arm_summaries` | the catalogue, the list, the list at the base | each `lists --check` finding |
| `arm_direction` | the catalogue | each `check_direction` finding; its population is the loop bound and deadline rows |

The fixture's cases: one `schema-empty-<name>` per never-empty row, then `shape-no-empty`,
`shape-unknown-field`, `usage-out-of-set`, `summary-new-key`, `usage-new-key`, `list-grew`,
`direction-missing` (the first selected row loses its `direction`), `direction-new-bound` (a new
`retry-count` row `zz.loop` with none), `direction-wrong-value` (the first selected row declares
`raise-tightens`), `adopter-fresh-target`, an outcome case with no plant, below, and the reader's two
outcome cases. `reader-landed` builds a bare remote whose `main` sets `warn` and a clone whose
unpushed commit and working tree set `refuse`: `get` must print `warn`, `--rev HEAD` `refuse`, and
refuse an unknown key, a malformed key and a revision naming no commit; then a two-remote clone,
which refuses with `GOV_REMOTE` unset and reads the second remote with it set, and a remote-less
repository, which reads its local `main`. `reader-parsed` commits a policy file whose first line is
`touch <marker>`, which must refuse naming line 1, and one whose comments carry `$(touch <marker>)`
and a backticked `touch`, which must read its value; the marker must not exist after both.

## Each arm in an adopter

The `policy check` leg ships, so every arm in `ARMS` runs in an adopter's tree as well as in gov's.
The table says what each one grades there. `check_policy.py --fixture adopter-fresh-target` joins its
first column to `ARMS` both ways, so an arm added with no row reds as unlisted and a row whose arm
left reds as stale. The same case copies this kit, and each kit its `kit.toml` `requires`, into a
fresh `git init` at the path each holds in its own repository, runs `adopt-policy.sh --scaffold`, then
runs `--check` before the first commit and again after it. Both runs must exit 0, and every arm must
print a graded line with no finding or an announce line, `policy-check: <arm> · not graded · <why>`.

| Arm | In an adopter it grades | When its subject is absent |
|---|---|---|
| `arm_schema` | the target's `.governance/policy.toml`, each key against the installed catalogue | a finding: no policy file is a zero population, so `--scaffold` comes before the first `--check` |
| `arm_shape` | the installed kit's catalogue, row by row | a finding: the catalogue ships in the kit, and one that does not read or parse reds |
| `arm_summaries` | the installed shrink-only list against the installed catalogue, and against the list at the target's compare base | a finding per row an absent list owes; no remote or no fetched ref is no base, which its line says, and the catalogue alone is compared |
| `arm_direction` | the installed catalogue's loop bound and deadline rows | a finding: the catalogue ships in the kit, and one that does not read or parse reds |

## The adopter

`bash <prefix>/policy/adopt-policy.sh --scaffold [--target <repo>]` writes `.governance/policy.toml`
from the scaffold only where no file exists, and says "kept" otherwise: the file is the
repository's own from its first write. `--check [--target <repo>]` runs `check_policy.py --repo`.
The `policy check` leg ships to adopters; `policy fixtures` is gov's own.

## What this kit does not check

It proves each file key is a value its row admits and each row is well formed. It does not prove a
row's `allowed` and `default` say what the design means: that is the build's acceptance probe, which
compares the catalogue with the design's table. No consumer reads the file yet, so a valid value
changes no behaviour until a later unit re-points its consumer.
