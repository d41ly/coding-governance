# policy — one file for a repository's policy, and the catalogue that is its schema

A repository's policy lives in ONE file, `.governance/policy.toml`, TOML 1.0, read through `tomllib`
and never sourced. This kit owns that file's schema: the catalogue `catalogue.toml`, one `[[key]]`
row per policy key, taken row for row and in order from the design's `[policies]` table, each row's
`name` and `owner` that table's own. Contract: TOOL-dGroundRules-1.

The kit lands dark: one reader reads `.governance/policy.toml`, `policy.py get` (TOOL-dGroundRules-2),
in one resolution order (TOOL-dGroundRules-3), and an invalid file never reads defaults
(TOOL-dGroundRules-4); no consumer calls the reader yet. The JSON mirror the hooks read,
`.governance/policy.json`, is rendered at every landing and read by one helper (TOOL-dGroundRules-5);
no hook reads it yet. The minimal guard, `guard.py`, refuses an agent's commit to the policy file and
its three neighbours but one shape (TOOL-dGroundRules-6), and later units re-point consumers.

## Files

| File | What it is |
|---|---|
| `catalogue.toml` | the schema: one row per key |
| `unsummarised-keys.txt` | GENERATED, shrink-only: the rows with no `summary` or no `usage` |
| `legacy-homes.txt` | GENERATED, shrink-only: one row per key a legacy policy home holds, with its mark (TOOL-dGroundRules-7); gov's own, withheld from installs by a `project-owned` rule in `kit.toml` (TOOL-dGroundRules-17) |
| `policy.py` | the module: `load_catalogue`, `read_catalogue_row`, `check_value`, `check_shape`, `derive_bounds`, `check_direction`, `derive_unsummarised`, `resolve_compare_base`, the reader `resolve` over `read_revision` and `resolve_read`, the file's one judge `validate`, the mirror's `render_mirror`, the legacy homes' `derive_legacy_homes` and `check_legacy_homes`, and the `lists`, `scaffold`, `get`, `check` and `mirror` verbs |
| `policy-mirror.js` | the mirror's one reader, for hooks: `readPolicy` and its `get` CLI |
| `policy-shim.sh` | the helper's shell half: the landed revision, and the reader under a resolved launcher |
| `guard.py` | the minimal guard: `guard.py --staged`, the verdict over an agent's staged change to a guarded path |
| `guarded-paths.txt` | the one spelling of the guarded set, read at HEAD by `guard.py` and the pre-commit hook |
| `check_policy.py` | the arms' home: `ARMS` over a repository, and `--fixture`, which runs `CASES` |
| `caps.toml` | the cap census: one `[[cap]]` row per size cap, its class, unit, enforcer, legacy home and family flag (TOOL-dGroundRules-9), and `ships = false` where the deployer's registry exempts the enforcer (TOOL-dGroundRules-17), else the registry entry that installs it, `kit`, and its `{prefix}`-spelled destination, `installed` (TOOL-dGroundRules-22) |
| `budgets.py` | the size caps' half of the reader: `read_cap_census`, `resolve_caps` with the switch and the two-homes rule, `check_cap`, the `[budgets]` schema rule `check_budgets` that `validate` calls, and the `resolve` and `check` verbs |
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
- `python <prefix>/policy/check_policy.py --live` — TOOL-dGroundRules-10's live observation: a
  fixture repository whose policy sets `runtime.agents-in-flight` to 2, its settings rendered, and
  headless `claude -p` sessions whose agents each stamp a start and an end around a 20-second sleep,
  under the render and under a control with none. It prints each run's peak overlap and the session
  total, never asserted. It drives real sessions, so no leg runs it; with no `claude` on PATH it
  prints `NOT RUN`, exit 2.
- `python <prefix>/policy/policy.py settings [--write|--check] [<settings-file>]` — the agent limit,
  `runtime.agents-in-flight` at HEAD, rendered into the harness's two concurrency settings,
  `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` and `CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS`, in
  `.claude/settings.json` under the repository root by default (TOOL-dGroundRules-10). `--check`, the
  default, exits 1 printing one line per variable that is absent or differs; `--write` writes only
  when one does, every other key kept in order, in `settings-merge.py`'s shape. `kit.toml`'s stage-1
  `[[generated]]` row runs both at every landing and before a bar. The reader lowers the key, never
  raises it, by a `FANOUT_CAP=<n>` line in `.agent-cap.conf` at the revision read, its legacy home.
- `python <prefix>/policy/policy.py lists --check` — red on a row the catalogue owes and the list
  lacks, a row the list carries that the catalogue no longer owes (stale), and a row the list at the
  compare base did not carry. The base is the merge-base of HEAD and the remote default branch where
  that is a proper ancestor of HEAD, else the remote tip; no fetched ref is no base, and a list
  absent at the base is no comparison, never an empty one. It grades `legacy-homes.txt` too, below.
  Exit 0 green, 1 red, 2 usage or a refused read.
- `python <prefix>/policy/policy.py lists --write` — drain the list: it keeps the rows the catalogue
  still owes and never adds one. An absent list is seeded with every owed row. It writes
  `legacy-homes.txt`'s derived rows too, and writes nothing, exit 1, while a derived row is new to the
  list at the landed revision.

## The legacy policy homes

Policy still lives outside `.governance/policy.toml` in three legacy homes: each tracked root file
named `.*.conf`, the gate file `.githooks/gate-env.sh`, and the roles kit's house file, homed
`<tool-root>/roles/house/policy.toml` and found from this kit's own location. `derive_legacy_homes`
parses each, never sources one, into rows `<home> <key> <mark>`: every key a kit conf assigns but a
`_CUTOFF` or `_PIN` (the retrofit converts those), `owner-policy`; every key the gate file assigns,
documents in its header, or is read from it by a `read_policy_key "<expr>" KEY` call in a tracked
shell file outside `memory/` and `help/`, less a key a kit conf holds, marked from `GATE_ENV_MARKS`
in `policy.py`, else `unmarked`; and one `[<table>]` row per top-level table of the house file,
`owner-policy`. An absent home yields no rows and one `legacy homes: no <home> ...` line.

`lists --check` compares the derived rows, the working tree's `legacy-homes.txt` and the list at the
landed revision, identity the pair (home, key), and reports a committed row no home yields (`stale
list at <row>` when the landed list holds its pair, else `typed row <row>`), a committed row under a
mark the derivation does not give (`typed row`), a derived row the list lacks (`stale list`), a
derived row the landed list lacks (`is a new legacy home and the list is shrink-only`), and an
`unmarked` row. With no list at the landed revision it says the list seeds the baseline.

The list is gov's own: its rows are gov's homes, so `kit.toml` withholds it from every install with
a `project-owned` rule, the runlog descriptor's mechanism (TOOL-dGroundRules-17). Where this kit
holds no list, `arm_legacy_homes` prints `policy-check: arm_legacy_homes · not graded · the list is
gov's own and is withheld from installs` and finds nothing, and `lists --write` writes the summary
list alone, printing `legacy-homes.txt · not written`: it updates the legacy list where one exists
and never creates it. On gov's tree the case `legacy-homes-present` reds a deleted list.
- `python <prefix>/policy/policy.py scaffold` — print the starter policy file: each row this kit's
  build owns that has a literal default, one table per first segment.
- `python <prefix>/policy/policy.py get <key> [--rev <rev>] [--explain] [--json]` — run in the repository to
  read: the key's value on stdout, a string as itself, a number or a boolean in TOML's spelling, a
  list one member per line, LF-ended. `--json` prints one JSON object of `reason`, `source` and
  `value` instead, the form the mirror helper reads. `--explain` adds `policy: <key> · <source> · <reason>` on
  stderr, the reason naming the sha8 and how the revision was found. Exit 0, or 2 with one
  `policy: refused · <path>:<line> · <why>` line and nothing on stdout.
- `python <prefix>/policy/policy.py mirror --write | --check` — run in the repository: the mirror,
  below, rendered at HEAD. Both refuse, exit 2 with `uncommitted changes`, while the policy file or
  the catalogue in the working tree differs from its blob at HEAD. `--write` writes
  `.governance/policy.json` only when its bytes differ and prints `policy: mirror written · <n> keys
  · policy <blob8> · catalogue <blob8>` or `policy: mirror fresh`. `--check` exits 0 with
  `policy: mirror fresh`, or 1 with `policy: mirror stale · .governance/policy.json · <what> · run: ...`,
  `<what>` being `absent`, `unparsable`, a blob field, or the first key that differs. `--print`
  writes the render's bytes to stdout and no file, the form `guard.py` compares a staged mirror with.
- `node <prefix>/policy/policy-mirror.js get <key> [--repo <dir>] [--explain]` — the helper's CLI:
  the value as `get` prints it, `--explain` adding the same stderr line. Exit 0, or 2 with the
  refusal line.
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
  step takes `(path, row, table, rev_phrase)`, `table` None for an absent file, and names the
  revision read only through `rev_phrase`, the read's `<sha8>, <how>`. `read_file_value`
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
- **One read per revision.** `read_revision(repo, rev)` reads the revision, its text, `validate`'s
  problems and the parsed table once, and spells the revision once as its `rev_phrase`, which
  every reason names; `resolve_read(path, row, read)` is the one composition of
  `RESOLUTION_ORDER` and the invalid-file branch over it, the last valid revision walked to once per
  read. `resolve` calls the two in turn.

## The mirror

A hook is JavaScript and cannot parse TOML, so it reads policy through `.governance/policy.json`,
pinned LF in `.gitattributes`. `render_mirror(repo, rev)` renders it for one revision over one read:

```json
{
  "catalogue_blob": "<blob id of this kit's catalogue at the revision>",
  "keys": {"budgets.enforce": {"reason": "...", "source": "file", "value": "warn"}},
  "policy_blob": "<blob id of .governance/policy.toml at the revision, or null when absent>"
}
```

`keys` holds every catalogue name with no `*` or `<...>` segment, and every key the file sets that a
pattern row matches, each with its `Resolution`. The bytes are sorted, two-space indented, ASCII and
LF, so one revision renders one byte string. A value JSON cannot spell refuses naming its key; a read
the reader refuses, an invalid file under `refuse` say, refuses the render, so a landing carrying
one stops naming the line. The blob ids pin the mirror to its policy, never a commit id: a commit
cannot carry its own id, and the lander renders before the merge commit exists.

**No commit in the bytes** (TOOL-dGroundRules-65). The render sets the read's `rev_phrase` to the
placeholder `{rev}`, so every reason names the revision read as `{rev}`; a `last-valid` reason keeps
the last valid revision's own sha8, history no rewrite changes. The invariant: two commits with the
same policy blob, the same catalogue blob and the same first-parent history render byte-identical
mirrors, so the mirror the lander renders into a merge stays fresh after its `git commit-tree`
rewrite.

**Regenerated at every landing.** `kit.toml`'s `[[generated]]` row, stage 2, names `mirror --write`
and `mirror --check`, so the run-gates kit's `regen.py --write` renders it into each landing the
lander makes, and the bar's preflight runs the check. A branch carrying a policy change carries a
stale mirror until it lands or until a commit of its own carries the regenerated one, which the
guard admits (below).

**Read from the landed blob only.** `policy-mirror.js`'s `readPolicy(key, { repo })` finds the
landed revision L through `policy-shim.sh landed`, reads the mirror's blob at L and the two blob ids
there, and takes a key from the mirror only while both ids match, each `{rev}` in its reason filled
with `<L8>, the landed revision`. A stale or absent mirror, or a key
it does not hold, is read through the reader by `policy-shim.sh get <key>`; a mirror failure first
reads `policy-file.on-invalid`, and any value but `last-valid` refuses naming the mirror. A fallback's
reason opens `mirror absent at <L8>` or `mirror stale at <L8>`. The working-tree mirror is never
opened. The shim carries the remote ladder and the python resolver inline, byte-identical to their
canonicals. Python and shell consumers call the reader, never the mirror.

## The guard

The stand-in, until dDeclaredLoop's guard lands, for the defaults of `policy-file.guard` and
`policy-file.proof`, owner-only and the TTY proof, enforced without reading either key: `guard.py`
imports no reader. gov's `.githooks/pre-commit` carries its block, above the legs. When a path
`guarded-paths.txt` lists at HEAD is staged, the block admits on the owner's terminal proof,
`[ -t 2 ]`, since git leaves a hook's stderr as the committer's; otherwise it runs
`guard.py --staged`, and any exit but 0 refuses, as does a tree whose tracked python resolver yields
no launcher. A commit staging no listed path spawns no Python.

`guard.py --staged`, from the top level: the list at HEAD (none, or no HEAD: exit 0); the touched
set, `git diff --cached --no-renames` against it (empty: exit 0); while `MERGE_HEAD` resolves, a path
whose staged blob is its blob at HEAD or at `MERGE_HEAD` leaves the set, since a merge taking a side
writes nothing new. Then the mirror shape (TOOL-dGroundRules-19): `.governance/policy.json` leaves
the set when the staged policy file and this kit's catalogue are their blobs at HEAD, each absent on
both sides counting as equal, and its staged bytes are the stdout of `policy.py mirror --print` run
under the guard's own interpreter, a subprocess, so no reader is imported. It prints
`policy-guard: admitted · .governance/policy.json · equals its render at HEAD`, and an emptied set
exits 0. Otherwise the mirror stays, refused with
`the mirror renders HEAD: commit the policy file or catalogue first, then regenerate`, with
`differs from its render at HEAD`, or with the render's own refusal line. So an agent's catalogue or
policy change is one commit and its regenerated mirror the next. What remains must be exactly
`.governance/policy.toml`, modified, where:

- both sides parse as TOML, and exactly one leaf differs, present on both sides;
- that leaf is under `budgets`, neither `budgets.enforce` nor `budgets.pinned`, and its last segment
  is a file tracked at HEAD, so a class row such as `docs/*/` is no measured-file cap;
- both values are integers, booleans excluded, and the new one is larger;
- the text change is one old line replaced by comment lines and then one other line, one comment
  carrying `RAISED <old> -> <new>`;
- `memory/DECISIONS.md` is staged with at least one `- ` row added and no line removed.

Exit 0 prints `policy-guard: admitted · budgets.<cap> <old> -> <new> · its change record attached`.
Exit 1 prints every failed condition as `policy-guard: refused · <path> · <why>`, then one remedy
line, which names `git restore --staged --worktree` for the mirror, since the landing renders it with
no hook firing. Exit 2 is a git read that failed. It stops forgetting, not evasion: `--no-verify`, a
pty wrapper, a list line removed one commit before the change, another clone, a cherry-pick or rebase,
and a guard file deleted from the working tree all pass it, and the push-time bar does not re-judge
authorship. The block is gov's own; the runbook's copy instructions do not carry it.

## The arms

| Arm | Reads | Finds |
|---|---|---|
| `arm_schema` | `.governance/policy.toml`, the catalogue | each problem `validate` finds: each key `check_value` refuses, each key no row matches |
| `arm_shape` | the catalogue | a set-valued row with no `empty`, `empty` on any other row, a missing required field, an unknown field, a literal default or a `usage` its own row refuses, a `usage` that does not parse |
| `arm_summaries` | the catalogue, the list, the list at the base | each `lists --check` finding |
| `arm_direction` | the catalogue | each `check_direction` finding; its population is the loop bound and deadline rows |
| `arm_on_invalid` | `.governance/policy.toml` as committed at HEAD, its history | the refusal `policy.py check` prints: an invalid file with no valid revision before it, or one whose last valid revision sets `policy-file.on-invalid = "refuse"` |
| `arm_mirror_parity` | the working-tree `.governance/policy.json` against `render_mirror` at HEAD | a mirror that differs, named by its first difference, or one that is absent |
| `arm_mirror_landed` | `node policy-mirror.js get <key>` against the reader's `resolve`, for each key the policy file at the landed revision sets | a value the two answer differently, or one refusing where the other answers |
| `arm_mirror_readers` | the tracked `*.js`, `*.mjs`, `*.cjs`, `*.py`, `*.sh` and `.githooks/*` outside this kit, the memory root and `help/` | a file naming `policy.json` |
| `arm_legacy_homes` | the kit confs, the gate file and the house file, `legacy-homes.txt`, the list at the landed revision | each `lists --check` report on the legacy homes; a refused landed revision. With no list in this kit it is not graded and says so |
| `arm_reader_coverage` | the catalogue's `owner` fields, each owner's build folder at the landed revision, the tracked `*.py`, `*.js`, `*.mjs`, `*.cjs`, `*.sh` and `.githooks/*` outside the memory root, `help/`, tests and this checker | each key whose owner build has landed that no call reads; a refused landed revision |
| `arm_limits_readers` | the same tracked code files outside this kit, the memory root, `help/` and the self-tests | a file spelling the template-size limits file's name on a line that is not a comment or a Python docstring: `budgets.py` is its one reader |
| `arm_cap_census` | `caps.toml`, each row's enforcer, the requests the same tracked code makes, the limits file in the tree | a row whose enforcer is absent where it is graded (its `enforcer` path on the source tree, its `installed` path in an adopter whose receipt names its `kit`), asks the policy kit nothing, or never names it (a `limits:` row names it by subject), an outside row its enforcer requests a mode for, a row with no `budgets-cap-` case or a case with no row, a request naming no row, a limits row no census row names |

## The size caps

`budgets.py` (TOOL-dGroundRules-9) answers every size cap through one switch. `caps.toml` is the
census: each cap's name under `budgets.*`, its class (`switch`, or outside it as `consumer`,
`correctness` or `exempt`), its unit, its enforcer, its legacy home and whether it is a family, and
`ships = false` on a row whose enforcer the deployer's registry exempts, so no install holds it
(TOOL-dGroundRules-17); absent means `true`. An enforcer asks once per run, `budgets.py resolve <cap>[=legacy:<n>|=default:<n>]` from a shell or
`budgets.resolve_caps` from Python, handing in the value its own home holds; a `limits:` home, the
template-size limits file, is read by `budgets.py` alone at the landed revision. The answer's value is
the policy file's `budgets.<cap>` where it sets one, and a value held in both homes refuses. Its mode
is `refuse` where `budgets.pinned` names the cap or `budgets.enforce` is `refuse`, else `warn`: a
breach under `warn` prints `BUDGET WARN — <cap> · <subject> · <measured> <unit> over <value>` and
passes. `validate` calls `check_budgets`, which refuses a pin outside the switch or naming no row, and
a value naming no row, on a family cap, or not a positive integer. An enforcer with no policy kit
beside it, or a reader that refuses, refuses as before and says so once. help/size-caps.md is the
user's page.

`arm_reader_coverage` (TOOL-dGroundRules-8) grades a key once its owner build has LANDED: at the
landed revision `policy.py get` reads, the build folder `<memory root>/builds/<owner>/spec/` holds at
least one spec and every spec's status header is terminal, read with the memory-tree kit's
`tree_lib` (`HDR_RE`, `TERMINAL`, `read_blobs_at`, `parse_conf`). A build whose spec run landed its
units `DEFERRED` has not landed. A key is READ where a tracked file passes it to a reader in one of
the two shapes of `READER_SHAPES`, one row each: a call whose first argument is the key as a string
literal (`resolve("k")`, `mirror.get('k')`) in a `.py`, `.js`, `.mjs` or `.cjs` file, and
`policy.py get k`, the key optionally quoted, in a `.sh` file or under `.githooks/`. A comment line
never reads. A key with a `*` or `<name>` segment reads where that segment is spelled as one run with
no quote, space, `.`, `(` or `)`, `"budgets.$cap"` say, unless the text spells another catalogue key
exactly. It prints `reader coverage: graded <n> of <m> catalogue key(s); landed owners: <slugs or
none>` on every run, and with nothing graded `reader coverage: graded 0, so this arm checked nothing
at <rev8>`, which is no finding; its population is the catalogue's keys. With no memory-tree kit
beside this one, no build reads as landed, and it says so. It does not see a reader in another
language, or a key built at run time from parts, which reds as unread; and a call that only names
the key, in a message say, reads as a reader.

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

The fixture's repository also carries `hooks/consumer.js`, a tracked consumer that reads policy
through the helper, and the mirror rendered at its commit. `mirror-hand-edited` sets the working-tree
mirror's `runtime.agents-in-flight` to 8 with its blob ids kept, and `mirror-absent` deletes it: each
must red `arm_mirror_parity` naming the key, then `absent`. `mirror-direct-reader` makes the consumer
read the mirror with `readFileSync`, which must red `arm_mirror_readers` naming it. The outcome cases
copy `policy.py`, `policy-mirror.js` and `policy-shim.sh` into the kit copy and push a landed revision
L to a bare remote: `mirror-worktree-loosened` lands a limit of 2 with its fresh mirror and loosens
the working-tree mirror to 8, where a four-line fixture hook asked for 3 must refuse and the helper
print `2`; `mirror-stale-last-valid` lands 3 with the mirror rendered at 2, read as `3` from `file`
with a reason opening `mirror stale at`; `mirror-stale-refuse` lands the same under `refuse`, which
must refuse naming `.governance/policy.json:0` and red `arm_mirror_landed`; `mirror-absent-refuse`
lands no mirror, refused under `refuse` and read as the reader reads it under `last-valid`. Every
other outcome case must leave `arm_mirror_landed` green. `mirror-landed-parity` runs the shim's
`landed` beside `derive_landed_revision` with two remotes and `GOV_REMOTE`, two without, one, and
none: the same sha, or both refusing, in each. `mirror-commit-rewrite` runs `mirror --write` at a
commit, commits the mirror, and rewrites that commit with `git commit-tree` over its tree and
parents: `mirror --check` must print `policy: mirror fresh` at both, and the helper, reading the
rewrite pushed as L, must name L's sha8 as the landed revision with no `{rev}` left.

The sixteen `guard-*` cases copy `guard.py`, `guarded-paths.txt` and `policy.py` into the kit copy and commit a
policy file whose `[budgets]` table caps a tracked `big.md` at 100, a tracked `small.md` at 50 and the
class row `docs/*/` at 10, then stage one plant each from `GUARD_PLANTS` and judge `guard.py --staged`
by its exit code and reasons. `guard-admits-raise`, `big.md` to 120 with its `RAISED` comment and one
decision row, must exit 0. Exit 1, naming the reason: `guard-lowered`, `guard-two-raised`,
`guard-class-row`, `guard-beside-change` (`budgets.enforce` set beside the raise),
`guard-beside-path` (a line added to `.governance/deploy.toml` beside it), `guard-no-record`,
`guard-no-argument`, `guard-no-row` (each naming only what is missing), `guard-other-paths` (the
mirror, the instruction manifest and `.governance/deploy.toml`, each alone), `guard-new-row` and
`guard-removed-row`; the mirror plant of `guard-other-paths`, a hand edit, must print
`differs from its render at HEAD`. `guard-merge-side` concludes a conflicted merge with the branch's
policy file, exit 0, then with a third text, exit 1. The mirror shape's three commit a catalogue row
and run `mirror --write`: `guard-mirror-render` stages the mirror alone, exit 0 printing
`equals its render at HEAD`; `guard-mirror-beside-catalogue` moves the row back into the index with
`git reset --soft HEAD~1` and stages the mirror beside it, exit 1 printing
`commit the policy file or catalogue first`; `guard-mirror-branch-green` does it on a branch, commits
the admitted mirror, and `mirror --check` at the new HEAD must print `policy: mirror fresh`. The hook block's arms are in gov's pre-commit suite.

`legacy-homes` is one outcome case over seven repositories, each a copy of `policy.py` with a
`.unattended.conf`, a gate file and a house file, pushed to a bare remote with the list seeded; it
prints `case <name>: red|green` and judges the copy's `lists` verbs by exit code and exact reports:
`today` green; `planted-row` a typed row; `growth` a conf key and its row typed in, the new-home
report, and `lists --write` exiting 1 with the list unchanged; `shrink` a conf key removed, the
stale-list report, then green after `lists --write`; `retrofit` a `_CUTOFF` and a `_PIN` key, green
and unlisted; `unmarked` a gate key `GATE_ENV_MARKS` lacks; `absent-homes` no gate or house file,
green with one announce line for each. Each copy's list is seeded by `lists --write` over a
header-only list, since that verb never creates one.

`legacy-homes-present` and `budgets-ships-join` (TOOL-dGroundRules-17) read only this kit and its
source repository, so they hold on gov's tree. The first reds this kit's directory without
`legacy-homes.txt`, or a `kit.toml` with no `project-owned` rule naming it: an absent list is an
announcement in the arm, so this case is what reds a list deleted on gov's tree. The second reads
`govkit/registry.toml` under the tool root and reds, naming the row, a census row whose
`ships = false` disagrees either way with the registry's `[[exempt]]` paths, an exempt directory
covering every enforcer under it, and a registry that exempts no census enforcer.

`census-adopter-receipt` (TOOL-dGroundRules-22) is an outcome case over one scratch repository: a
planted receipt whose `kits` names `policy`, `memory-tree` and `kickoff-manifest` and whose `prefix`
is not gov's tool root, each of those kits' census enforcers at its `installed` path, and no
deployer. `arm_cap_census` must print `line-length · kit check-line-length not installed` and no
finding; it must red naming `manifest-bytes` and its installed path once the planted
`manifest-check.sh` is deleted, and read green again once it is restored.

`reader-coverage` is one outcome case over eleven repositories, each a kit copy whose catalogue holds
the planted key `fixture.planted`, a spec under `memory/builds/bPlanted/spec/` and the case's planted
files, pushed to a bare remote; it judges `check_reader_coverage` by the key it reds and the count it
grades, printing `case <name>: red|green`. Red: `landed-no-reader` (the spec `CLOSED` at the landed
revision, no consumer), `not-a-reader` (the key named only in a `.md` file, a `*.test.sh`, a `.py`
comment line, a copy of `check_policy.py`, the JSON mirror and the catalogue), `history-not-tree`
(`CLOSED` landed, `OPEN` in the working tree) and `pattern-only-sibling` (`fixture.*` red while the
only call names its sibling `fixture.exact`). Green: `unlanded` (`OPEN` landed), `no-build` (owner
`bAbsent`, no build folder) and `tree-not-history` (`OPEN` landed, `CLOSED` in the working tree), each
grading nothing and printing the announce line; `reader-python`, `reader-cli` and `reader-js`, one
shape each; and `pattern-read` (`policy.py get "fixture.$name"` reads `fixture.*`).

## Each arm in an adopter

The `policy check` leg ships, so every arm in `ARMS` runs in an adopter's tree as well as in gov's.
The table says what each one grades there. `check_policy.py --fixture adopter-fresh-target` joins its
first column to `ARMS` both ways, so an arm added with no row reds as unlisted and a row whose arm
left reds as stale. The same case installs this kit the way an adopter gets it: a fresh `git init`
with a `.governance/deploy.toml`, committed once, then `govkit.py apply` with this kit and the closure
of its `kit.toml` `requires`. The deployer installs its checkout's HEAD, so the case runs the
`govkit.py` of a scratch clone whose HEAD commits the working tree under test, and prints
`installing from snapshot <sha8> of the working tree over HEAD <sha8>`; an uncommitted edit is graded,
and the source's object store gains nothing. A refused `apply`, a failed snapshot step, or a `govkit.py`
absent from the tool root, reds the case. Every file under the target's tool root must be a path the receipt records, and every engine or
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
| `arm_mirror_parity` | the target's `.governance/policy.json` against its render at HEAD | a finding: an absent mirror reds until the first landing renders one, which TOOL-dGroundRules-21 grades only where HEAD carries a policy file or a mirror |
| `arm_mirror_landed` | the installed helper against the reader, for each key the target's policy file sets at its landed revision | a finding: a landed revision with no policy file is a zero population, until TOOL-dGroundRules-25 announces it |
| `arm_mirror_readers` | the target's tracked code outside the installed kit, its memory root and `help/` | a finding: a target with no tracked code is a zero population, until TOOL-dGroundRules-21 announces it |
| `arm_legacy_homes` | nothing: `legacy-homes.txt` is gov's own list, which `kit.toml` withholds from every install (TOOL-dGroundRules-17) | announced, since no install holds the list: `policy-check: arm_legacy_homes · not graded · the list is gov's own and is withheld from installs`, and `lists --write` never creates it |
| `arm_reader_coverage` | each installed catalogue key whose owner build has landed in the target, against the target's tracked code | no owner build landed, or no memory-tree kit beside this one, prints `graded 0` and no finding; a landed revision that does not resolve is a finding |
| `arm_limits_readers` | the target's tracked code outside the installed kit, its memory root, `help/` and the self-tests, for a second reader of the template-size limits file | a finding: a target with no tracked code is a zero population |
| `arm_cap_census` | the installed cap census against the target: the target's `.governance/install.json` makes it an adopter, and each shipped row whose `kit` its `kits` names is graded at its `installed` path, `{prefix}` read as its `prefix`; the requests its tracked code makes, and the limits file's rows | graded by what ships (TOOL-dGroundRules-17, TOOL-dGroundRules-22): a `ships = false` row is announced, `cap census: <name> · enforcer not shipped`; a row whose `kit` the receipt's `kits` lacks is announced, `cap census: <name> · kit <kit> not installed`; an installed kit's enforcer absent at `installed` is a finding naming that path; a receipt that does not parse is a finding naming it |

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
