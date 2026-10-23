# TOOL-dGroundRules-1 — the policy file, the policy kit, its catalogue and the catalogue's shape audit

**Status:** DEFERRED · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 1 · advances TOOL-dGroundRules-12

**Carries:** cl-dClosedLoop-0007@b0458b78 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-1-departures-spec.md](../build/2026-10-23-build-TOOL-dGroundRules-1-departures-spec.md) | journal | — |
| [2026-10-23-prompt-TOOL-dGroundRules-1-owner-audit-cap.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-1-owner-audit-cap.md) | research | — |
| [2026-10-23-prompt-TOOL-dGroundRules-1-spec-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-1-spec-brief.md) | research | TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 |
| [2026-10-23-review-TOOL-dGroundRules-1-11-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-1-11-spec-audit-round1.md) | spec-audit | TOOL-dGroundRules-11 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-10 TOOL-dGroundRules-9 |
| [2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-65 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-51 TOOL-dGroundRules-52 |

<!-- /gen:spec-records -->

## 1. Goal

There is no single answer to "what is this repo's policy" (`gap-spine-06`). This unit lands the place
the answer lives: `.governance/policy.toml`, a new kit `tools/policy/` that owns it, and the
kit's catalogue `tools/policy/catalogue.toml`, which is the schema. Every row of v2's `[policies]`
table becomes one catalogue row. The schema refuses an empty value for a never-empty set-valued key.
A shape audit refuses a set-valued row that declares no empty-set rule, and a row with no summary or
no usage unless it sits on a shrink-only list that today's keys drain from. The reader, the
resolution order, invalidity, the mirror and the guard are units 2 to 6; this unit is what they read.

## 2. Scope (IN)

- **S1** — `.governance/policy.toml`, TOML 1.0 read through `tomllib`, holding only the keys this
  build owns that have a literal catalogue default, each at that default:
  `policy-file.on-invalid`, `budgets.enforce`, `budgets.pinned` and `runtime.agents-in-flight`. A key
  `a.b.c` is the dotted TOML path, so `budgets.enforce` is `[budgets] enforce = "warn"`. Its bytes are
  the output of `python tools/policy/policy.py scaffold`. Observed by AC8.
- **S2** — The kit `tools/policy/`: `kit.toml`, a `README.md`, the adopter `adopt-policy.sh`
  (`--scaffold` and `--check`), its registry `[[entry]]`, and two legs in `tools/gate-legs.json`,
  `policy check` and `policy fixtures`. Observed by AC1 and AC9.
- **S3** — The catalogue `tools/policy/catalogue.toml`: one `[[key]]` table per row of v2's
  `[policies]` table, in v2's order, with the fields and the `allowed` grammar of §4. Every name and
  every owner equals v2's. Observed by AC1 and AC2.
- **S4** — The value check, `check_value(row, value)` in `tools/policy/policy.py`, and the schema arm
  that applies it to every key of `.governance/policy.toml`. An empty array for a row whose `empty` is
  `never` is refused, and so is any value outside the row's `allowed` and any key no row matches.
  Observed by AC3 and AC9.
- **S5** — The shape audit, `check_shape(rows)` in `tools/policy/policy.py`: a set-valued row with
  no `empty`, an `empty` on a row that is not set-valued, a missing required field, an unknown field,
  a literal default its own row refuses, and a `usage` that does not parse or whose value its row
  refuses. Observed by AC1, AC4 and AC10.
- **S6** — The summary/usage rule and its shrink-only list. A row with an empty or absent `summary` or
  `usage` must be named on `tools/policy/unsummarised-keys.txt`. The list is generated by
  `python tools/policy/policy.py lists --write`, which only ever shrinks the list, and checked by
  `--check`, which also refuses a row the compare base did not carry. Observed by AC5, AC6 and AC7.
- **S7** — `tools/policy/check_policy.py`, the arms' home: one CLI that runs every arm over a
  repository, and a `--fixture` mode that plants each red case in a temporary repository and asserts
  it red as planted and green without the plant. Later units add arms and cases to it. Observed by
  AC1 and AC3 to AC7.
- **S8** — The help page `help/policy.md`, linked from `help/README.md`. Observed by AC11.

## 3. Non-goals (OUT)

- The reader `resolve` and the `get` verb (unit 2), the resolution order (unit 3), `validate` and
  the invalid-file branch (unit 4), the JSON mirror (unit 5), the guarded paths and the minimal guard
  (unit 6), the legacy-home list (unit 7), the reader-coverage arm (unit 8), the cap keys' semantics
  (unit 9), the agent limit's consumers (unit 10) and the `direction` rule (unit 11).
- Keys owned by later builds being written to `.governance/policy.toml`, and any cross-key rule a
  v2 cell states in prose, such as a round count held at or below `review.max-rounds` or a pair rule
  with another key. Their owning builds check them.
- A value v2 admits as "a registered" or "a repo-declared" member. No registry exists yet, so the
  value check refuses it, and the row's `registry` field carries v2's words for the build that adds
  one.
- Generating the policy keys' reference page from `summary` and `usage`: that is the help renderer of
  `cl-dClosedLoop-0067`, a later build's. This unit writes a hand page.
- Writing summaries for every key. Today's keys sit on the shrink-only list; only the four keys of S1
  carry a summary and a usage here.
- Rendering a charter block for the kit, and adding it to `.governance/deploy.toml`'s `kits`.
- dDeclaredLoop's surfaces: this build moved the file, schema, reader and mirror ahead of it (RC-1),
  and its guard and guarded policy command stay its own.

### Edges

- **hands-off** `TOOL-dGroundRules-2` — the module `policy.py` with the catalogue loader and the inlined remote ladder; it adds `resolve` and the `get` verb to the same module
- **hands-off** `TOOL-dGroundRules-3` — the catalogue rows and their `default` field, which the resolution order falls back to
- **hands-off** `TOOL-dGroundRules-4` — the value check its `validate` calls per key, and the schema arm it re-points through `validate`
- **hands-off** `TOOL-dGroundRules-5` — the catalogue whose every key the mirror resolves
- **hands-off** `TOOL-dGroundRules-6` — the kit directory its guarded-paths file and guard arms join
- **hands-off** `TOOL-dGroundRules-7` — the `lists` verb, which gains the legacy-home list beside the unsummarised one
- **hands-off** `TOOL-dGroundRules-8` — the catalogue's `owner` field, its population's left half
- **hands-off** `TOOL-dGroundRules-9` — the `budgets.*` and `budgets.pinned` rows as v2 states them, whose semantics it owns
- **hands-off** `TOOL-dGroundRules-10` — the `runtime.agents-in-flight` row and its value in the policy file
- **hands-off** `TOOL-dGroundRules-11` — the catalogue's typed ranges and the known optional field `direction`, whose rule it adds to the shape audit
- **hands-off** external — the 24 pairs of catalogue names TOML cannot hold in one file, one a dotted prefix of the other (§8 F5), to the later builds that own them
- **hands-off** `TOOL-dGroundRules-16` — the adopter's fresh target as a standing case every later arm of `policy check` passes through, and the README table of what each arm grades there (finding 4)
- **hands-off** `TOOL-dGroundRules-20` — the sibling files the `policy fixtures` cases run, which this unit's `{prefix}/policy/` guard misses (finding 35)
- **hands-off** `TOOL-dGroundRules-21` — the scaffold's LF bytes, the eol pins, the version marker, the adopter's armed refusal, the per-arm empty population, the four `read_policy_key` copies and the compare base's canonical block (findings 19, 27, 39, 41, 51, 20, 29)

## 4. Design

### Evidence

- No `.governance/policy.toml` exists; `.governance/` holds `deploy.toml` alone, read at base.
- `read_policy_key` is a bash `KEY=value` parser, byte-identical in `.githooks/pre-push:1306`,
  `tools/push-main.sh:404` and `tools/run-gates/post-merge.sh:171`. This unit does not touch it.
- `tomllib` needs Python 3.11, the floor `tools/codebase-map/map_lib.py:17` already states.
- A kit may not import a sibling kit, so a kit carries shared code inline: the remote ladder's
  canonical block is `tools/lib/resolve_remote.py:16-68`, and every inline copy is held to it by the
  parity rows of `tools/lib/resolve-python.test.sh:182`, which find copies by `git grep`.
- The shrink-only compare this unit copies is `resolve_compare_base` in
  `tools/codebase-map/map_lib.py:1502-1527`: the merge-base of HEAD and the remote default branch
  where that is a proper ancestor of HEAD, else the remote tip, and no answer without a fetched ref.
- v2's `[policies]` table runs from `## [policies]` (v2:1125) to `## [presets]` (v2:1408) at the blob
  the packet pins. A probe on 2026-10-23 counted 267 rows, 19 set-valued, 9 whose cell says never
  empty or one or more, and 1 whose cell is silent (`roles.auth.<role>`). These figures are
  PINNED as of that reading; AC1 and AC2 re-derive them from the files.

### Data model — the catalogue row

```toml
[[key]]
name = "budgets.enforce"          # v2's Key cell, verbatim
allowed = ["warn", "refuse"]      # the grammar below
default = "warn"                  # a TOML value, or { derived = "<v2's Default cell>" }
summary = "Whether a size cap's breach warns or refuses, for every cap not pinned."
usage = 'budgets.enforce = "refuse"'
owner = "dGroundRules"            # v2's Owner cell
# empty = "never" | "allowed"     # set-valued rows only, and required on them
# registry = "<v2's words>"       # optional: the members a registry will add
# direction = "raise-loosens"     # optional here; TOOL-dGroundRules-11's rule
```

Required fields are `name`, `allowed`, `default` and `owner`. Optional fields are `empty`,
`summary`, `usage`, `registry` and `direction`. Any other field is an unknown field.

A `name` is dotted segments of `[A-Za-z0-9_-]+`. A segment may instead be a placeholder `<word>`, or
`*` as the last segment only. A placeholder or `*` matches exactly one segment of a file key, and an
exact name outranks a placeholder name. File keys are compared as SEGMENT TUPLES and never as joined
strings, because a quoted TOML segment such as `budgets."memory/guides/BUILD-METHOD.md"` carries dots.

### Data model — the `allowed` grammar

| v2's Allowed cell | `allowed` | example row |
|---|---|---|
| a closed list of words | `["a", "b"]` | `core.bypass` |
| a closed list of numbers | `[1, 2, 3]` | `review.design-audit.runs` |
| a list ending "or a registered X" or "or a repo-declared X" | `{ type = "enum", of = [...], registry = "<X>" }` | `deps.messaging` |
| any subset of, a set of, one or more of, none or a set of | `{ type = "set", of = [...] }` or `{ type = "set", item = "<regex>" }`, plus `empty` | `design.reentry` |
| an ordered list | `{ type = "list", ... }`, plus `empty` | `runtime.act-auth` |
| each of named members, on or off | `{ type = "map", of = ["on", "off"] }` | `floor` |
| a retry, round, route-back or agent count | `{ type = "retry-count" }`, `round-count`, `route-back-count` or `agent-count`, with `min`, `max` | `roles.retries` |
| any other count | `{ type = "count", min = 0 }` | `budgets.*` |
| hours, days or seconds | `{ type = "hours" }`, `days` or `seconds`, with `min` | `flow.wait-ceiling` |
| a formatted string (`60%`, `1-3`, `16k`, a blob id) | `{ type = "pattern", regex = "<regex>" }` | `context.threshold` |
| the values another surface defines | `{ type = "name", item = "<regex>", registry = "<v2's words>" }` | `roles.effort.<role>` |

A typed scalar may also carry `or`, literal alternatives such as `["all"]` or `["measured"]`, and
`pattern`, an alternative string form such as `flow.rework-budget`'s `<base>+<per-unit>`. The count
types are TOML integers; the duration types are TOML numbers. Where the grammar cannot state a cell
exactly, the row takes a `pattern` admitting exactly v2's stated forms and carries v2's remaining
words in `registry`. The count and duration nouns are v2's own words, kept so TOOL-dGroundRules-11
can derive its population from them (§8 F3).

Set-valued means `type` is `set` or `list`. `empty = "never"` where the cell says never empty,
non-empty or one or more; `empty = "allowed"` where it says none, or empty allowed.

### Inventory — what the unit mints

| Name | Kind | Where |
|---|---|---|
| `policy` | kit id, registry entry | `tools/policy/kit.toml`, `tools/govkit/registry.toml` |
| `KIT_POLICY_VERSION` | version constant, `1.0` | `tools/policy/policy.py` |
| `load_catalogue(kit)` | function, rows in file order | `tools/policy/policy.py` |
| `check_value(row, value)` | function, a reason string or `None` | `tools/policy/policy.py` |
| `check_shape(rows)` | function, `(key, why)` pairs | `tools/policy/policy.py` |
| `derive_unsummarised(rows)` | function, sorted names | `tools/policy/policy.py` |
| `resolve_compare_base(repo)` | function, `(sha or None, reason)` | `tools/policy/policy.py` |
| `lists --write`, `lists --check`, `scaffold` | CLI verbs | `tools/policy/policy.py` |
| `ARMS`, `CASES` | module lists the CLI iterates | `tools/policy/check_policy.py` |
| `arm_schema`, `arm_shape`, `arm_summaries` | arm functions, findings per repo | `tools/policy/check_policy.py` |
| `policy check`, `policy fixtures` | gate legs | `tools/gate-legs.json` |

`policy.py` carries the canonical `# >>> remote_ladder_py` block inline, byte-identical, and its
`resolve_compare_base` follows the map kit's function of that name, rule for rule.
TOOL-dGroundRules-2 reads the landed revision through the same inlined ladder.

### The CLIs

- `python tools/policy/policy.py lists --check` derives D, the names `derive_unsummarised`
  returns. It reads L, the rows of `tools/policy/unsummarised-keys.txt` after its `#` header, with CR
  stripped. It reads B, the same file at the sha `resolve_compare_base` answers. It reds on each name
  in D but not L ("lacks a summary or a usage and is not listed"), on each in L but not D ("stale:
  drain it with `lists --write`"), and on each in L but not B ("added to a shrink-only list"). With
  no base it prints the reason and grades the first two only. A list absent at the base is no
  comparison and never an empty one, as `derive_baseline_additions` rules for the map's baseline, so
  the landing that seeds it is not read as adding every row. Exit 0 green, 1 red, 2 usage.
- `lists --write` writes L ∩ D, sorted, under the header. An absent file is seeded with D. It never
  adds a name to an existing file.
- `scaffold` prints the starter policy file: a header comment naming the catalogue and the help
  page, then each row whose `owner` is `dGroundRules` and whose `default` is a literal, grouped into
  one TOML table per first segment, tables sorted, keys in catalogue order.
- `python tools/policy/check_policy.py [--repo <dir>]` runs each arm in `ARMS` over the repository,
  the git top level of the working directory by default. It prints one line per arm,
  `policy-check: <arm> · <n> finding(s) · <population>`, then each finding. A population of zero is a
  finding. Exit 0 green, 1 red.
- `python tools/policy/check_policy.py --fixture` makes one temporary git repository per case under
  the system temp directory with a short prefix (`pol-`), because a long path fails a Windows clone.
  The repository is a copy of the kit's catalogue and list under `tools/policy/` plus a policy file at
  its scaffold, committed, with a remote-tracking ref at that commit. Each case in `CASES` plants its
  break on that copy and runs its arm. The line `policy-fixture: <case> · RED as planted` or
  `· WRONG` follows, then the same arm on the unplanted copy, which must be green. It ends with an
  executed-assertion count. Exit 0 only when every case behaves.

### The arms and the cases

| Arm | Reads | Finds |
|---|---|---|
| `arm_schema` | `.governance/policy.toml`, the catalogue | each file key whose `check_value` returns a reason, and each key no row matches |
| `arm_shape` | the catalogue | each `check_shape` pair |
| `arm_summaries` | the catalogue, the list, the list at the base | each `lists --check` finding |

| Case | Plant | Arm |
|---|---|---|
| `schema-empty-<name>` | one per row with `empty = "never"`: that key set to `[]`, a placeholder segment filled as `x` | `arm_schema` |
| `shape-no-empty` | the first set-valued row of the shipped catalogue loses its `empty` | `arm_shape` |
| `shape-unknown-field` | the same row gains `emtpy = "never"` | `arm_shape` |
| `usage-out-of-set` | `budgets.enforce`'s `usage` becomes `budgets.enforce = "loud"` | `arm_shape` |
| `summary-new-key` | a new row `zz.planted` with every required field, no `summary` | `arm_summaries` |
| `usage-new-key` | the same row with a `summary` and no `usage` | `arm_summaries` |
| `list-grew` | `zz.planted` added both to the catalogue and to the list, above the committed base | `arm_summaries` |

Each plant edits a real shipped row where one serves, so the case proves the mechanism for the
shipped value and not a simpler synthetic one.

### The adopter

`bash tools/policy/adopt-policy.sh --scaffold --target <repo>` writes
`<repo>/.governance/policy.toml` from `policy.py scaffold` only when the file is absent, and says
"kept" otherwise. `--check --target <repo>` runs `check_policy.py --repo <repo>`. The kit's `[adopt]`
names `--scaffold`, its `[check]` names `--check`, and its `[[outcome]]` probes that the file exists.
The `policy check` leg ships as a `[[gate_leg]]`, subject `repo`, because its subject is the target's
own file. The `policy fixtures` leg is gov's alone, subject `kit` with guard `{prefix}/policy/`, carried
by an `[[exempt_leg]]` row in the registry as `runlog selftest` is (`tools/govkit/registry.toml:575`).

### Rollout

The kit lands dark in effect: no consumer reads `.governance/policy.toml` until units 2 to 10 re-point
one. TOOL-dGroundRules-11 shares this unit's order and every file it writes, so the build runs it
after this unit and never beside it (M6, clause 1).

### Files touched (estimate)

- `.governance/policy.toml`
- `tools/policy/kit.toml`
- `tools/policy/README.md`
- `tools/policy/catalogue.toml`
- `tools/policy/policy.py`
- `tools/policy/check_policy.py`
- `tools/policy/adopt-policy.sh`
- `tools/policy/unsummarised-keys.txt`
- `tools/gate-legs.json`
- `tools/govkit/registry.toml`
- `tools/govkit/subject-pins.tsv`
- `tools/run-gates/selftest-budgets.txt`
- `tools/playbook-kit-waivers.txt`
- `.gitattributes`
- `help/policy.md`
- `help/README.md`
- `memory/map/features/policy.md`
- `memory/map/generated/MAP.md`
- `memory/map/generated/CARDS.md`
- `memory/map/generated/inventories.json`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- **A separate module for the catalogue functions.** It would leave `policy.py` to unit 2, but S8's
  `policy.py lists` verb is this unit's and lands first, so the verb would need a second spelling.
- **A new check inside an existing gate rather than two legs.** The cheaper shape by
  `memory/gotchas/a-new-leg-trips-a-growing-set-of-meta-gates.md`, but the brief's S9 makes this kit
  the arms' home for eleven units, and a kit's repo-subject leg must ship with the kit.
- **The list graded only as D ⊆ L.** A hand-added row beside a new key would then pass, so the
  shrink-only half compares against the base.

## 5. Production-readiness checklist

- security — the file is parsed by `tomllib` and never sourced; every closed list refuses a member
  outside it, a registry member included, so the default is deny. No secret is read or written.
- perf / scale — one TOML parse of about 270 rows per run; the fixture mode makes about fifteen
  small git repositories, a few seconds.
- error / empty / loading states — an absent policy file grades nothing in `arm_schema` and says so;
  a catalogue that does not parse is one finding naming the parser's line; a zero population is red.
- observability — every arm prints its population on every run, and `lists --check` prints its base
  and why, or why there is none.
- risks — the new legs trip the meta-gates of `a-new-leg-trips-a-growing-set-of-meta-gates`; the
  bar at the close is the authority on that set, and Files touched is an estimate of it.
- testing — the `--fixture` cases, each red as planted and green without, with AC1 to AC11.
- migration — none: nothing reads the file yet, and an absent file is legal.
- user docs — `help/policy.md` and `tools/policy/README.md`.

## 6. Acceptance criteria

The kit's paths are quoted inside each command below, because none is tracked until this unit lands.

- **AC1** — When `python "tools/policy/check_policy.py"` runs on the built tree, it exits 0 and prints
  one line each for `arm_schema`, `arm_shape` and `arm_summaries`, each with a non-zero population,
  the shape line naming the row, set-valued and never-empty counts.
  Red when: any arm finds a problem in today's files, or any population reads zero.
  figure: the counts are DERIVED from the catalogue at observation.
- **AC2** — When a probe parses v2's `[policies]` table from `git show 9bf3b4c91952d54f01be759082f7ae3e52cde160`
  between its `## [policies]` and `## [presets]` headings, and parses the catalogue with
  `tomllib.load(open( "tools/policy/catalogue.toml" , "rb"))`, the two name lists are equal in order and
  each name's `owner` equals v2's Owner cell. The four rows of S1 hold the defaults `last-valid`,
  `warn`, `[]` and `6`.
  Red when: a row is missing, extra, out of order or owned by another build.
  figure: the row count is DERIVED from both files; 267 was read on 2026-10-23.
- **AC3** — When `python "tools/policy/check_policy.py" --fixture` runs, it prints one
  `schema-empty-<name>` case per catalogue row with `empty = "never"`, each RED as planted and
  green unplanted, and the number of such cases equals that row count.
  Red when: `check_value` admits `[]` for a never-empty row, or the population is zero.
- **AC4** — When the same `--fixture` run reaches `shape-no-empty` and `shape-unknown-field`, each is
  RED as planted, naming the row, and green unplanted.
  Red when: `check_shape` stays silent on a set-valued row with no `empty`, or on a misspelt field.
- **AC5** — When the same `--fixture` run reaches `summary-new-key` and `usage-new-key`, each is RED as
  planted, naming `zz.planted` as not listed, and green unplanted.
  Red when: a new row lacking a `summary` or a `usage` passes `arm_summaries`.
- **AC6** — When the same `--fixture` run reaches `list-grew`, it is RED as planted, naming
  `zz.planted` as added above the base, and green unplanted. On the `summary-new-key` copy,
  `lists --write` leaves the list without `zz.planted`, and `lists --check` stays red.
  Red when: a list longer than its base passes, or `lists --write` adds a name to an existing list.
- **AC7** — When a copy of the kit gives one listed row a `summary` and a `usage`,
  `python "tools/policy/policy.py" lists --check` exits 1 naming that row stale, `lists --write`
  removes exactly that row, and `lists --check` then exits 0.
  Red when: a drained row stays listed, or the write removes any other row.
  fixture: the copy is made under the run's temp directory; the tree holds none today.
- **AC8** — When `tomllib.load(open( ".governance/policy.toml" , "rb"))` parses the policy file, its key
  tuples are exactly the four of S1 at their catalogue defaults, and the file's bytes equal the output
  of `python "tools/policy/policy.py" scaffold`.
  Red when: the file holds another key, another value, or bytes the scaffold does not print.
- **AC9** — When `bash "tools/policy/adopt-policy.sh" --scaffold --target <t>` runs on a scratch target
  with no policy file, it writes the scaffold's bytes; run again over an edited file, it leaves the
  file byte-identical; `--check --target <t>` exits 0, and exits 1 once the file sets
  `runtime.agents-in-flight = 0`.
  Red when: the scaffold overwrites an existing file, or the check admits a value below the row's `min`.
  fixture: the scratch target is a fresh `git init` under the run's temp directory.
- **AC10** — When the same `--fixture` run reaches `usage-out-of-set`, it is RED as planted, naming
  `budgets.enforce`'s usage, and green unplanted.
  Red when: a `usage` whose value its own row refuses passes `arm_shape`.
- **AC11** — When `grep -n "policy.md" help/README.md` runs, it finds the link, and
  `grep -c "governance/policy.toml" "help/policy.md"` counts at least one line, as do the same grep
  for `check_policy.py` and for `lists --check`.
  Red when: the page or its link is absent, or the page names none of the three.

## 7. Gates

`playbook parity selftest` · `recall floor` · `recall floor arms` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `codebase-map coverage + freshness` · `memory hygiene`

The guards join's broad guards, `{prefix}/` and `{prefix}/run-gates/`, are excluded from the line by
the checker's floor; the bar at the close runs them all.

New arm: tools/policy/check_policy.py · covers AC1 · a staged break of a live subject, `[]` for `runtime.harnesses` in `.governance/policy.toml` · none
New arm: tools/policy/check_policy.py --fixture · covers AC3 AC4 AC5 AC6 AC10 · each case in `CASES` plants its own break in a temporary repository · none

## 8. Open questions

- **F1 — Who creates `tools/policy/policy.py`?** The brief's S4 gives the module to unit 2 at order 2,
  and S8 gives this unit, at order 1, the `policy.py lists` verb, so the verb would precede its
  module. (a) This unit creates the module with the catalogue functions, the inlined ladder, `lists`
  and `scaffold`, and unit 2 extends it with `resolve` and `get`, every spelling of S4, S5 and S8
  kept. (b) A second module for this unit's functions, with `lists` respelled onto it. (c) This unit
  sequenced after unit 2, which the roster's order forbids. (b) respells a shared interface and (c)
  fails the roster, so veto 1 discards both. Recommendation (a). Rung 3.
  RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none
- **F2 — How does the schema refuse before `validate` exists?** S5 has units 1, 5 and 6 call
  unit 4's `validate`, which lands at order 2. (a) `arm_schema` calls `check_value` per key, and
  unit 4 builds `validate` on `check_value` and re-points the arm. (b) This unit writes `validate`
  itself. (b) takes unit 4's mechanism, two mechanisms in one spec by M2. Recommendation (a). Rung 3.
  RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none
- **F3 — What does a typed range's `type` say?** S3's example is `{ type = "count", min = 1 }`.
  (a) v2's own nouns: `retry-count`, `round-count`, `route-back-count`, `agent-count`, `hours`,
  `days`, `seconds`, and `count` for any other count. (b) One `count` and one `duration`. Under (b)
  TOOL-dGroundRules-11 could not tell a loop bound from an agent count without a typed list, which
  its brief forbids, so veto 1 discards it. Rung 1: v2's Allowed cells answer it.
  RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none
- **F4 — Which empty-set rule does `roles.auth.<role>` declare?** Its v2 cell is silent, and the
  shape audit refuses a set-valued row with none. (a) `never`: its default, `runtime.act-auth`, is
  never empty, and an empty credential list runs no act. (b) `allowed`. (c) None, which reds today's
  catalogue and fails AC1. Veto 1 discards (c); (a) and (b) both pass every criterion, and (a) is the
  reading its default's row states. Recommendation (a). Rung 3.
  RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none
- **FACT-QUESTION · F5 — Can every catalogue name be written under S1's dotted-path mapping?** Probe:
  list each pair of v2 names where one is a proper dotted prefix of the other, since TOML cannot hold a
  key that is both a value and a table. Liveness: the probe names `leases` and `leases.granularity`,
  so it can produce a positive. Observation, 2026-10-23: 24 such pairs, among them `leases`,
  `verdict`, `attendance` and `review.<stage>`; none involves a key S1 writes. (a) S1 stands for
  this build's keys and the pairs are handed to their owning builds. (b) Flat quoted keys, which
  respell S1 for every writer. (c) A reserved member name, a new grammar no clause asks for. (b)
  breaks the interface axis and (c) adds an unasked surface. Recommendation (a), with the hand-off in
  §3 Edges' external line. Rung 2 settles the fact and rung 3 the pick.
  RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none
- **F6 — Does a closed list admit v2's "or a registered" members now?** (a) No: the value check
  refuses any member outside `of`, and the row's `registry` keeps v2's words. (b) Yes, any string,
  which loosens every such key before a registry exists. Veto 3 discards (b): it widens a write
  surface beyond the unit's tier. Recommendation (a). Rung 3.
  RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none
- **F7 — Does the build's grant lift veto 2 for the new kit, its registry entry and its two legs?**
  `tools/gate-legs.json` and the registry are governance carriers, and the kit is a public surface.
  `cl-dClosedLoop-0007` names the file, its schema, its one reader and its mirror, which this kit
  holds. RESOLVED (agent, 2026-10-23, delegated): lifted by `PLAY-dClosedLoop-3`, rung 3.
  grants: PLAY-dClosedLoop-3 the policy kit, its registry entry and its two legs · widens: none ·
  relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft.
- rev-2 · 2026-10-23 · §3 · the **hands-off** edges to TOOL-dGroundRules-16, TOOL-dGroundRules-20, TOOL-dGroundRules-21 added, each the reciprocal of that unit's **consumes-from** line: the promotions of the round-1 spec audit's findings that repair this unit. No scope, design or acceptance moved here; the repair is the promoted unit's.

## 10. Reuse audit

No existing seam fits the catalogue and its value check. `python tools/codebase-map/reuse_lookup.py
"validate a TOML declaration file against a catalogue of allowed values"` ranked `declares`,
`load_toml` (`tools/govkit/govkit.py:285`) and the unattended kit's `declared_list` and
`declared_scalar`. `load_toml` reads a file and validates nothing, and a kit may not import the
deployer; the other two read bash declarations. The shrink-only half extends the house pattern
rather than a callable seam: `python tools/codebase-map/reuse_lookup.py "shrink-only list derived
and checked against the landed revision"` ranked `derive_baseline_additions`
(`tools/codebase-map/map_lib.py:1530`), whose compare base, `resolve_compare_base` at
`tools/codebase-map/map_lib.py:1502`, this unit copies because the map kit is a sibling kit. The
ladder under it is reused as the gated inline block of `tools/lib/resolve_remote.py:16-68`. The
recall probe surfaced `TOOL-aScouredKit-4`, a shrink-only list seeded empty: this list is seeded with
today's keys, so that trap does not apply. No hit disagreed with source.

Recall terms used: `python tools/memory-recall/query.py "how is a policy key catalogue validated and
a shrink-only list of keys drained" --terms "policy catalogue schema shrink-only list drained summary
usage read_policy_key kit.toml adopter tomllib"`
