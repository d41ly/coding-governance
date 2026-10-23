# policy — one file for a repository's policy, and the catalogue that is its schema

A repository's policy lives in ONE file, `.governance/policy.toml`, TOML 1.0, read through `tomllib`
and never sourced. This kit owns that file's schema: the catalogue `catalogue.toml`, one `[[key]]`
row per policy key, taken row for row and in order from the design's `[policies]` table, each row's
`name` and `owner` that table's own. Contract: TOOL-dGroundRules-1.

The kit lands dark: one reader reads `.governance/policy.toml`, `policy.py get` (TOOL-dGroundRules-2),
in one resolution order (TOOL-dGroundRules-3), and an invalid file never reads defaults
(TOOL-dGroundRules-4); no consumer calls the reader yet. The JSON mirror and the guard are later units
of dGroundRules, and each re-points one consumer.

## Files

| File | What it is |
|---|---|
| `catalogue.toml` | the schema: one row per key |
| `unsummarised-keys.txt` | GENERATED, shrink-only: the rows with no `summary` or no `usage` |
| `policy.py` | the module: `load_catalogue`, `read_catalogue_row`, `check_value`, `check_shape`, `derive_bounds`, `check_direction`, `derive_unsummarised`, `resolve_compare_base`, the reader `resolve`, the file's one judge `validate`, and the `lists`, `scaffold`, `get` and `check` verbs |
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
- `python <prefix>/policy/check_policy.py --fixture [--strict-from <dir>] [<case>]` — one scratch
  repository per case under the system temp directory (`pol-` prefix): each case plants its break,
  its arm must red naming the planted key, and the unplanted copy must be green. It ends with an
  executed-assertion count. A `<case>` runs that case alone; a name no case carries is exit 2.
  `--strict-from` names the directory holding the design record whose `[presets]` table
  `on-invalid-strict` reads: the one file directly in it whose name ends `-architecture-v2.md`, red
  naming the count when there is none or more than one. Without it that case prints `NOT RUN`, never
  a pass. Gov's `policy fixtures` leg always passes it.
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
- `python <prefix>/policy/policy.py check [--rev <rev>]` — run in the repository to check: the policy
  file in that commit, `HEAD` by default, the candidate a push lands. Exit 0 with one
  `policy: check · ...` line when the file is valid, absent, or invalid with a last valid revision
  under `last-valid`, the line saying which; exit 2 with the refusal line otherwise.

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
  value. `resolve` runs `RESOLUTION_ORDER`, the one order, and the first step to answer wins; each
  step takes `(path, row, table, sha, how)`, `table` None for an absent file. `read_file_value`
  answers `Resolution(value, "file", reason)` where the file sets the key; `read_default_value`
  answers the row's `default` with source `default` and a reason naming the case, absent or not
  set, and any `preset` the file names, which no step applies until dKeptSession adds its step
  between the two. A row with no `default` refuses, naming it in the catalogue.
- **An invalid file** (TOOL-dGroundRules-4). `validate(text)` is the file's one judge, and
  `arm_schema` grades through it: a list of `Problem(line, key, why)`, empty for a valid file. Text
  that is not TOML is one problem at the decoder's line, key `""`; text that parses has one per leaf
  `check_value` refuses and one per leaf no catalogue row matches, at the line `derive_key_line`
  finds (`0` inside an inline table). `resolve` parses valid text only. For text with a problem it
  takes `read_last_valid_value`: `read_last_valid` walks `git rev-list --first-parent <sha> --
  .governance/policy.toml` to the newest revision whose file is present and valid, an absent file
  counting as no valid revision. `policy-file.on-invalid` is read from THAT revision by
  `RESOLUTION_ORDER`, never from the invalid file, so an out-of-set value of it is one more problem.
  With no valid revision, or with `refuse`, the read refuses at the first problem's line. With
  `last-valid`, the default, the WHOLE file falls back, never one key: the key resolves over the
  valid revision's table, with source `last-valid` and a reason naming the invalid sha, the line,
  the problem and the valid sha. An absent file is not invalid and reads defaults.
- **Git's environment.** Every git call drops the location variables git exports to a hook
  (`GIT_LOCATION_VARS`), so a reader started inside a hook or a fixture reads the repository it was
  pointed at.

## The arms

| Arm | Reads | Finds |
|---|---|---|
| `arm_schema` | `.governance/policy.toml`, the catalogue | each problem `validate` finds: each key `check_value` refuses, each key no row matches |
| `arm_shape` | the catalogue | a set-valued row with no `empty`, `empty` on any other row, a missing required field, an unknown field, a literal default or a `usage` its own row refuses, a `usage` that does not parse |
| `arm_summaries` | the catalogue, the list, the list at the base | each `lists --check` finding |
| `arm_direction` | the catalogue | each `check_direction` finding; its population is the loop bound and deadline rows |
| `arm_on_invalid` | `.governance/policy.toml` as committed at HEAD, its history | the refusal `policy.py check` prints: an invalid file with no valid revision before it, or one whose last valid revision sets `policy-file.on-invalid = "refuse"` |

`arm_on_invalid` is how an invalid file with no fallback reaches the push and landing gates: the
`policy check` leg carries no guard, so the pre-push bar and every landing run it on a push that
changes only the policy file.

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
`resolution-order` reads one repository per scenario at `--rev HEAD`: a file setting
`budgets.enforce = "refuse"` must read `refuse` from `file` and `runtime.agents-in-flight` its
default `6` as `not set in`; a commit with no file must read `warn` as `is absent at`; a file setting
only `preset = "strict"` must read `warn` with the unapplied preset in its reason, and `refuse` once
it sets the key too; and a copy of this kit whose `budgets.enforce` row carries no `default` must
refuse, naming `catalogue.toml` and the row. `on-invalid-classes` plants each failure class of the
invalid-file branch in its own repository, V a valid revision and C the one after it: an absent
file reads defaults; a malformed C after V reads V with source `last-valid` and `check` names the
fallback; a malformed revision with nothing before it refuses `get` and `check` naming its line,
and `arm_on_invalid` reds over it and goes green once the file is made valid; a missing key reads
its default; an out-of-set C and a C setting `runtime.agents-in-flite`, a key no row matches, read
V whole; V setting `policy-file.on-invalid = "refuse"` refuses a malformed C; and C setting that key
to `"never"` refuses every read after a V that sets `refuse`, and reads V after a V that sets
nothing. `on-invalid-strict` reads v2's `[presets]` table from the one `-architecture-v2.md` file in
the directory `--strict-from` names, keeps each key whose
`strict` cell its catalogue row admits as a value other than its default, names every excluded row
with why (no row, a placeholder key, a cell that is no value, the default, a dotted prefix of a kept
key), and reads each kept key at a malformed revision after a valid one setting them all: every read
must be strict's value from `last-valid`, and an empty population reds.

## Each arm in an adopter

The `policy check` leg ships, so every arm in `ARMS` runs in an adopter's tree as well as in gov's.
The table says what each one grades there. `check_policy.py --fixture adopter-fresh-target` joins its
first column to `ARMS` both ways, so an arm added with no row reds as unlisted and a row whose arm
left reds as stale. The same case installs this kit the way an adopter gets it: a fresh `git init`
with a `.governance/deploy.toml`, committed once, then `govkit.py apply` with this kit and the closure
of its `kit.toml` `requires`. A refused `apply`, or a `govkit.py` absent from the tool root, reds the
case. Every file under the target's tool root must be a path the receipt records, and every engine or
seed row of the receipt must be present. The case then runs the installed adopter,
`adopt-policy.sh --scaffold`, and `--check` with the install staged and again once it is committed.
Both runs must exit 0, and every arm must print a graded line with no finding or an announce line,
`policy-check: <arm> · not graded · <why>`.

| Arm | In an adopter it grades | When its subject is absent |
|---|---|---|
| `arm_schema` | the target's `.governance/policy.toml`, each key against the installed catalogue | a finding: no policy file is a zero population, so `--scaffold` comes before the first `--check` |
| `arm_shape` | the installed kit's catalogue, row by row | a finding: the catalogue ships in the kit, and one that does not read or parse reds |
| `arm_summaries` | the installed shrink-only list against the installed catalogue, and against the list at the target's compare base | a finding per row an absent list owes; no remote or no fetched ref is no base, which its line says, and the catalogue alone is compared |
| `arm_direction` | the installed catalogue's loop bound and deadline rows | a finding: the catalogue ships in the kit, and one that does not read or parse reds |
| `arm_on_invalid` | the target's `.governance/policy.toml` as committed at HEAD, against the installed catalogue | an absent file at HEAD grades clean, since it reads defaults; a HEAD that names no commit, before the first commit, is a finding until TOOL-dGroundRules-21 announces it |

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
