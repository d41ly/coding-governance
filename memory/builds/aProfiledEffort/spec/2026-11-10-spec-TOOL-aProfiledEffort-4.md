# TOOL-aProfiledEffort-4 — the closing review's seven confirmed items are closed, and arm 19 fails by its own FAIL lines

**Status:** CLOSED · rev-2 · 2026-11-10 · node a · Tier-2 · base 7c896db6 · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-10-build-TOOL-aProfiledEffort-1-agent-ledger.md](../build/2026-11-10-build-TOOL-aProfiledEffort-1-agent-ledger.md) | journal | TOOL-aProfiledEffort-1 TOOL-aProfiledEffort-2 TOOL-aProfiledEffort-3 |
| [2026-11-10-build-TOOL-aProfiledEffort-4-1-acceptance-ledger.md](../build/2026-11-10-build-TOOL-aProfiledEffort-4-1-acceptance-ledger.md) | journal | — |
| [2026-11-10-prompt-TOOL-aProfiledEffort-4-1-spec-writer.md](../prompts/2026-11-10-prompt-TOOL-aProfiledEffort-4-1-spec-writer.md) | journal | — |
| [2026-11-10-prompt-TOOL-aProfiledEffort-4-2-spec-writer.md](../prompts/2026-11-10-prompt-TOOL-aProfiledEffort-4-2-spec-writer.md) | journal | — |
| [2026-11-10-prompt-TOOL-aProfiledEffort-4-ac4-revision-brief.md](../prompts/2026-11-10-prompt-TOOL-aProfiledEffort-4-ac4-revision-brief.md) | research | — |
| [2026-11-10-prompt-TOOL-aProfiledEffort-4-build-brief.md](../prompts/2026-11-10-prompt-TOOL-aProfiledEffort-4-build-brief.md) | research | — |
| [2026-11-10-prompt-TOOL-aProfiledEffort-4-round1-fix-brief.md](../prompts/2026-11-10-prompt-TOOL-aProfiledEffort-4-round1-fix-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

Round 1 of the closing diff review confirmed seven items, four medium and three low, and unit 1's
builder returned an eighth: arm 19 of the render self-test dies by traceback under one of its own
staged breaks. This unit closes each of the seven by the fix its report entry carries and makes
`resolve_profile` answer before it reads a profile it has no model for. The review record is
`memory/builds/aProfiledEffort/reviews/2026-11-10-review-TOOL-aProfiledEffort-1-closing-diff-round1.md`,
and the brief is
`memory/builds/aProfiledEffort/prompts/2026-11-10-prompt-TOOL-aProfiledEffort-4-round1-fix-brief.md`.

## 2. Scope (IN)

"The script" is `tools/roles/handoff.py`, "the library" is `tools/roles/roles_lib.py`, "the
self-test" is the `--selftest` mode of `tools/roles/render_agents.py`, "the suite" is
`tools/roles/adopt-roles.test.sh`, and "the policy file" is `tools/roles/house/policy.toml`. Each
item names the review item it closes.

- **S1** — Review item 1. The `agents` verb prints `unknown` for an effort the agent's transcript
  does not record, and no longer reads the agent type's file for one. The fallback, its regular
  expression `EFFORT_LINE_RE` and the `AGENTS_REL` import that served it are deleted, and the
  script's header and the roles README say what the line now holds. The docstring of
  `print_agent_lines` and the comment above `PATH_ID_RE` each drop the clause the deletion makes
  false. Observed by AC1 and AC9; the two clauses are NOT OBSERVED by a count, since no leg reads a
  comment's wording.
  **Readers:**
  by name: `tools/roles/handoff.py` spells `EFFORT_LINE_RE` at its definition and at the one use
  this item deletes, and no other tracked file outside the build records spells it, by a grep at
  writing. `AGENTS_REL` stays defined and read in `tools/roles/render_agents.py`; only the script's
  import of it goes.
  by value: NO VALUE READERS — nothing compares, counts or derives from the pattern, and arm 9 of
  the suite, the one check of the verb, gives every fixture transcript an `effort`.
- **S2** — Review item 2. Arm 19 of the self-test fails when a matched profile's stage overrides
  are merged with the default table's. Observed by AC2, AC3 and AC10.
- **S3** — Review item 3. Arm 19 of the self-test fails when the model id is not lower-cased before
  it is matched. Observed by AC2, AC3 and AC10.
- **S4** — Review item 6. Arm 19 of the self-test holds a profile whose `match` list is two words,
  resolves an id carrying only the second, and refuses a profile whose second word another profile
  holds. Observed by AC2, AC3 and AC10.
- **S5** — Brief item 8. `resolve_profile` answers `None` for a model id that holds no word,
  `None` and the empty string included, before it reads any profile. Observed by AC4 and AC10.
- **S6** — Review item 4. The policy file, the roles README and `help/roles.md` say the seeded
  profile gives its level to every role and to every stage key of a workflow's `stages` table. The
  README's limits paragraph names `committer` and `probe` as the harness stages no table keys.
  Observed by AC5.
- **S7** — Review item 5. The policy file's header says which values reach an agent type through a
  render and a new session, and which apply at the next dispatch. Observed by AC6.
- **S8** — Review item 7. Arm 19 of the suite passes a whitespace-only `--model` and gains a fifth
  assertion: a model two profiles match exits 1 through both verbs, naming both `match` keys, with
  no traceback. Observed by AC7 and AC9.
- **S9** — Arm 9 of the suite gains one assertion for S1, and `FLOOR_ASSERTIONS` rises by 2 under a
  comment naming this unit. Observed by AC7 and AC9.
- **S10** — With no model and with `claude-fable-5-2`, `stage-efforts` and `role-efforts` print the
  lines they print at `c1d1e19f4`. Observed by AC8.

## 3. Non-goals (OUT)

- **A re-review.** The closing review's subject is terminal, and this unit's diff is small enough
  for the main loop's own reading at the close.
- **The three CLOSED specs.** They stay as written. This spec restates no criterion of theirs.
- **A level for the `committer` or `probe` stage.** Giving either a level means a key in a
  workflow's `stages` table, which also feeds `harness-args` and would retype the stage as a role
  agent; the review's skeptic rejected that fix. It is a new mechanism. The build README's goal
  wants it on a Fable session whose own effort is not `medium`, so it is an ask for the main loop
  to file, and S6 states the limit until then.
- **The arm the review proposes for item 4**, comparing the keys `stage-efforts` prints with each
  harness's `ROLE_KEYS`. It is a new gate reading another kit's script, so it is its own unit, and
  the item's fix is the three texts. The two stage names S6 types into the README are checked by no
  leg.
- **A bug-class checklist entry for item 5.** The review routes it to the project's checklist,
  which is a record outside this unit's files and the main loop's to write.
- **Any level of the default tables or of the seeded profile.** S6 and S7 move comments only.
- **A profile-aware fallback for the `agents` verb.** See "Alternatives rejected".
- **The six refuted findings**, and any shape rule for a `--model` value beyond non-blank.
- **A hand bump of the kit version.** Kit versions move through the lander's `mint`.

### Edges

- **consumes-from** external — units 1 to 3 of this build, all CLOSED and built at `bd0a3808`: the
  resolver and arm 19 of the self-test, the two verbs and arm 19 of the suite, and the texts.
  Without them there is nothing to repair
- **hands-off** external — the main loop files the ask for a `committer` and `probe` level, writes
  the checklist entry for review item 5, and observes the two suites RED then GREEN at the close

## 4. Design

### Evidence

Read at the build branch's tip `bd0a3808` on 2026-11-10. Line numbers are PINNED to that reading,
and the builder finds each site by its quoted text.

| Site | Where | What it holds today |
|---|---|---|
| the fallback | `tools/roles/handoff.py:924` to 928 | `level = tr["effort"]`, then, when that is `None`, the `effort:` line of the role's agent type under `AGENTS_REL` |
| its pattern and import | `tools/roles/handoff.py:131` and `:836` | `EFFORT_LINE_RE`, and `from render_agents import AGENTS_REL, INDEX_REL`; the fallback is the only reader of either name in the script |
| the type's level | `tools/roles/render_agents.py:280` | `lib.resolve_effort(cat["policy"], slot)` with no model, so a type's line is the default tables' level |
| the blank check | `tools/roles/handoff.py:991` | `not a.model.strip()` exits 2 through `ap.error` |
| the early dispatch | `tools/roles/handoff.py:993` to 1004 | the three JSON verbs inside one `try`, and `except lib.RolesError` returning 1 |
| the resolver | `tools/roles/roles_lib.py:635` to 637 | `words = set(MODEL_SEGMENT_RE.findall((model or "").lower()))`, then a comprehension reading `profile["match"]` of every profile, whatever `words` holds |
| the stage rule | `tools/roles/roles_lib.py:657` | `over` is read from the matched table's `stages` alone |
| the word loop | `tools/roles/roles_lib.py:510` to 516 | `for word in words:` grades each entry and refuses one another profile holds |
| the self-test's policies | `tools/roles/render_agents.py:676` to 680 | `base` holds no `[effort.stages]` table; `fam` and `ven` each match one word |
| the self-test's rows | `tools/roles/render_agents.py:693` to 699 and 713 to 726 | eight resolve rows, every model id lower-case, and thirteen defect rows, every `match` one entry |
| the suite's arm 9 | `tools/roles/adopt-roles.test.sh:271` to 291 | `turn` writes an `effort` on every transcript record, so no assertion reaches the fallback |
| the suite's arm 19 | `tools/roles/adopt-roles.test.sh:764` to 780 | `--model ""` is the only refused value, stderr is discarded on the other calls, and the policy stays valid |
| the suite's floor | `tools/roles/adopt-roles.test.sh:86` | `FLOOR_ASSERTIONS=55` |
| the policy header | `tools/roles/house/policy.toml:2` | `A changed value reaches an agent after` a render and a new session |
| the profile comment | `tools/roles/house/policy.toml:27` | `names no role and no stage, so every one runs at medium` |
| the README claim | `tools/roles/README.md:195` | `every role and stage runs at` medium |
| the README row | `tools/roles/README.md:114` | effort: the transcript's last `effort`, `else the agent type's` line |
| the README limits | `tools/roles/README.md:211` to 215 | names the unkeyed case only as `a harness stage the workflow table gives no key` |
| the help claim | `help/roles.md:54` to 55 | the seeded profile `runs every` role and stage at medium |
| the unkeyed stages | `tools/workflows/unattended-build.js:494` and `tools/workflows/tier2-review.js:520` | `committer` and `probe` are in `ROLE_KEYS`, and `tools/roles/workflows.toml` keys neither |

Six probes were run at writing, each a read of the tree or of a scratch copy.

1. A scratch program resolved the rows of "The self-test's arm 19" below through the library. It
   printed the expected values of that table.
2. The same program ran over three scratch copies of the library, each with one mutation. With
   `.lower()` removed, the `Vendor-FAM-9` row read the plain levels. With `profile["match"]` cut to
   its first entry, the `vend2-other-9` row read the plain levels. With the default table's stage
   overrides merged under the profile's, `k2` read `high` in both `fam` rows and both `ven` rows.
3. `resolve_profile` over a policy whose one profile holds no `match`, with no model, raised
   `KeyError: 'match'`. That is the traceback the brief's item 8 names.
4. On a scratch copy of the kit with the `tfam` profile appended, `role-efforts --model ' '` exited
   2 with `--model is empty`. With a second profile matching `vendor` appended, both verbs exited 1
   on `--model vendor-tfam-9` with one stderr line holding `R12` and both `match` keys.
5. A profile holding `match = ["x", "fable"]` refused with one R12 line under
   `effort.profiles.x.match`.
6. Of the 80 newest agent transcripts under this machine's Claude projects folder, 40 direct and 40
   harness, all 80 carry `effort` on their first assistant record. PINNED 2026-11-10. So S1 moves
   the line of an agent only where its transcript records none.

### The `agents` verb

The five lines at `tools/roles/handoff.py:924` become one, `level = tr["effort"]`. The dictionary
comprehension three lines below already turns `None` into `unknown`, the note under it already
names the unanswered field, and a line holding `unknown` already stays out of the ledger. So the
change is a deletion. `EFFORT_LINE_RE` and the `AGENTS_REL` half of the import go with it, and the
import's comment names one path.

The script's header moves in two places. The `agents` paragraph says the shapes are filled from the
session's own records and the role index, with no mention of the agent types. The paragraph that
opens `WHAT THIS DOES NOT CHECK` gains one clause in its `agents` sentence: an effort no transcript
record carries prints `unknown`, never the agent type's `effort:` line, which is the default
tables' level and not the level a profile dispatched (TOOL-aProfiledEffort-4).

Two comments in the script follow the deletion, and both are in scope. The docstring of
`print_agent_lines` says the lines are filled from the session's records and the role index, and no
longer names the agent types, because the fallback was the function's one read of them. The comment
above `PATH_ID_RE` keeps its sentence on a run id and an agent id and drops the clause on a role
naming an agent type, because the fallback was the one place a role was matched against the
pattern. Its other two readers match an agent id and a run id. No other comment in the script
moves.

`tools/roles/README.md` moves in two places. The field table's effort row reads
``| effort | the agent transcript's last `effort` | `unknown` |``. The last sentence of the limits
paragraph says the `agent` line prints the effort and the model each agent's transcript records,
and `unknown` for an effort it does not record. `help/roles.md` already says `unknown` means
nothing has recorded the field, so it does not move for this item.

### The resolver

```python
    words = set(MODEL_SEGMENT_RE.findall((model or "").lower()))
    if not words:
        return None
```

The two added lines sit between the `words` line and the `hits` comprehension. The docstring's
first sentence says `None` is also the answer for an id that holds no word, given before any
profile is read. The guard tests `words`, never `model`, for two reasons. It covers a
whitespace-only id with the same line. And a guard on `model` above the `words` line would leave
its `or ""` dead, the class `memory/gotchas/guard-above-a-fold-makes-its-fallback-dead.md` names.
A model that holds a word still reads every profile's `match`, as today.

### The self-test's arm 19

The three policy strings become these, and nothing else in them moves:

```python
        base = ('[effort]\ndefault = "low"\n\n[effort.roles]\nr-one = "high"\n\n'
                '[effort.stages.w5]\nk2 = "high"\n')
        fam = base + (...)   # unchanged
        ven = fam + '\n[effort.profiles.ven]\nmatch = ["vendor", "vend2"]\ndefault = "medium"\n'
```

`build_fixture` writes the policy without loading it, and the `w5` workflow is appended before the
first `run_mode` call, so the new table names a workflow that exists when it is first read. `plain`
becomes `("high", "low", {"k1": "high", "k2": "high"})`. The 19b assertion keeps `effort: low` for
`r-two`, since a stage override never reaches an agent type.

The resolve rows, new ones marked:

| Row | Policy | Model | Expected |
|---|---|---|---|
| 19a | `base` | `vendor-fam-9`, and none | `plain` |
| 19c | `fam` | `vendor-fam-9` | `("max", "xhigh", {"k1": "medium", "k2": "xhigh"})`, unchanged |
| 19c, new | `fam` | `Vendor-FAM-9` | the same tuple |
| 19d | `fam` | `vendor-other-9`, `affam-9`, and none | `plain` |
| 19f | `ven` | `vendor-other-9` | `("medium", "medium", {"k1": "medium", "k2": "medium"})`, unchanged |
| 19f, new | `ven` | `vend2-other-9` | the same tuple |
| 19f | `ven` | `vendor-fam-9` | the refusal, unchanged |

The 19c rows now certify the stage rule: the default table gives `k2` the level `high`, and a
matched profile read alone gives it `xhigh`, its `r-two` entry. The defect rows gain one, placed
beside the existing `match = ["fam"]` row:

```python
                ('match = ["x", "fam"]\ndefault = "low"\n', "x.match"),
```

Its first word is clean and its second is held by `fam`, so the one R12 line comes from the word
loop's second pass. The arm's opening comment gains the three facts: a default-table stage override
that a matched profile does not inherit, an id in mixed case, and a `match` of two words on both
the resolve and the defect side. The arm's five `check_arm` call sites stay five.

### The suite

**Arm 9.** One assertion goes after the arm's last, because it rewrites the fixture's transcript.
An inline program drops the `effort` key from every record of
`agent-a0000000000000001.jsonl` under the session's `subagents` folder. Then
`agents --handoff "$A9H" --session "$A9S"` runs with no `--write`. The assertion holds when the
call exits 0, stdout is `$A9L1` with `effort medium` replaced by `effort unknown` followed by
`$A9L2`, stderr holds `no record answers level`, and the fixture's rendered
`gov-builder` agent type holds a line starting `effort: `. The last clause keeps the arm from
passing by finding nothing: the type does carry a level, and the verb did not print it. The
fixture's policy is the kit's own, whose default tables give `gov-builder` the level `high`, so the
verb at `bd0a3808` prints `effort high` here. The review asked for a fixture under a matched
profile. With the fallback deleted outright the model no longer reaches the level, so the arm
reads the plain case, and the suite's header says so.

**Arm 19.** The loop's refusal check runs for two values, the empty string and one space, and 19d
holds only when both exit 2 naming `--model is empty` for each of the three calls. A fifth
assertion, 19e, runs after the four existing ones are computed. It appends this to the fixture's
policy file:

```toml
[effort.profiles.tven]
match = ["vendor"]
default = "low"
```

Then `role-efforts --model vendor-tfam-9` and `stage-efforts build --model vendor-tfam-9` each
exit 1 with empty stdout and a stderr that holds `R12`, `effort.profiles.tfam.match` and
`effort.profiles.tven.match` and does not hold `Traceback`. The append comes last because the
second profile also answers `vendor-other-9`, which 19b reads as unmatched.

**Header and floor.** The header's list of arms gains a clause for each addition, and its
`WHAT THIS DOES NOT CHECK` list gains one sentence: arm 9 does not check an agent whose model a
profile matches, since the verb reads no profile. The floor comment gains the line
`+1 for arm 9 and +1 for arm 19 (TOOL-aProfiledEffort-4).` and `FLOOR_ASSERTIONS` becomes 57. The
review's figure of 56 counted item 7's assertion alone.

### The texts

The policy file's line 2 becomes three lines:

```toml
# A changed `[effort.roles]` or `default` value reaches an agent type after
# `render_agents.py --write` and a new session.
# A stage or profile value applies at the next dispatch.
```

Its profile block becomes:

```toml
[effort.profiles.fable]       # a table per model family; an unmatched model takes the tables above
match = ["fable"]             # one word of the model id, any version, as in claude-fable-5-2
default = "medium"            # every role, and every stage key of a workflow's `stages` table
# [effort.profiles.<name>.roles] and [effort.profiles.<name>.stages.<workflow>] take the keys of the
# tables above. A profile reaches an agent at dispatch, never through its rendered agent type, and
# gives no level to a harness stage that no `stages` table keys.
```

In `tools/roles/README.md` the seeded-profile sentence says the profile names no role and no
stage, so every role and every stage key of a workflow's `stages` table runs at `medium` on any
Claude Fable version. In the limits paragraph, the clause on a harness stage the workflow table
gives no key gains the two instances, with the words `` `committer` and `probe` `` on one line:
`committer` of `unattended-build.js` and `probe` of `tier2-review.js`. The words that join the two
names to the clause are the builder's, and an introduction such as "which today is" is in scope.
AC5 holds the two names on one line and nothing else of the sentence. In `help/roles.md` the
seeded-profile sentence says the profile runs every role, and every stage a workflow's `stages`
table keys, at `medium`. `tools/roles/workflows.toml` does not move.

### Inventory

This unit mints no function, flag, verb or file.

| Identifier | Kind | Cell |
|---|---|---|
| `tven` | profile name in the suite's fixture | not graded |
| `vend2` | match word in the self-test's fixture | not graded |
| `Vendor-FAM-9`, `vend2-other-9` | model ids in the self-test's fixture | not graded |

### The staged breaks the main loop observes

Each break is applied alone and restored with `git checkout --` on its one file before the next.

| # | File | Break | What reds |
|---|---|---|---|
| B1 | the library | `.lower()` removed from `resolve_profile` | the self-test's `Vendor-FAM-9` row |
| B2 | the library | `profile["match"]` cut to `profile["match"][:1]` in `resolve_profile` | the `vend2-other-9` row |
| B3 | the library | `over` in `resolve_stage_efforts` built from the default table's stage overrides with the matched table's laid over them | both 19c rows and both resolving 19f rows |
| B4 | the library | `for word in words:` cut to `for word in words[:1]:` in `load_policy` | the `match = ["x", "fam"]` row |
| B5 | the library | the profile loop of `load_policy` staged out, `for name, profile in ():` | the 19e rows, by FAIL lines, with exit 1 and no `Traceback` |
| B6 | the script | `level = tr["effort"] or "high"` | arm 9's new assertion |
| B7 | the script | `not a.model.strip()` weakened to `a.model == ""` | 19d of the suite |
| B8 | the script | `except lib.RolesError` at the early dispatch changed to `except KeyError` | 19e of the suite |

B5 is unit 1's second staged break, the one that died by traceback. Under it every defect row
loads, and the render that follows resolves with no model, which S5 answers before a malformed
profile is read. No other reader of the profile tables sits on the render path: a grep of
`tools/roles/render_agents.py` for `profiles` finds the self-test's fixtures alone.

### Rollout

1. Edit the library, then the script, then the self-test and the suite, then the three texts.
2. Verify in the pass with AC1 to AC8. The pass runs no gate leg, no suite and no self-test.
3. Commit once with the unit id in the subject, staging the seven files below.
4. The main loop observes AC9 and AC10 at the close, RED under each break and GREEN restored.

### Files touched (estimate)

`tools/roles/handoff.py` · `tools/roles/roles_lib.py` · `tools/roles/render_agents.py` ·
`tools/roles/adopt-roles.test.sh` · `tools/roles/house/policy.toml` · `tools/roles/README.md` ·
`help/roles.md`

The symbol map does not move: no function is added, renamed or deleted.

### Alternatives rejected

- **Keeping the fallback and correcting the README alone.** The review offers it as the second
  branch of item 1. The brief's item 1 has the verb stop printing the level, and a line that prints
  a level no record observed stays a misreport whatever the README says about it.
- **A fallback that resolves the type's level through the agent's model.** It would print a level
  the dispatch may not have passed, since a call made without the flag is refused by nothing. The
  line reports what a record observed, and `unknown` is the documented value for nothing observed.
- **A guard on `model` in `resolve_profile`.** The reason is under "The resolver".
- **Asserting `"skeptic":"low"` in the suite's arm 19 for item 2.** The review allows either home.
  The self-test already holds the rows that certify the role side, so the stage side sits beside
  them, and one home is enough.
- **A `stages` key for `committer` and `probe`.** The review's skeptic judged it unsound.

## 5. Production-readiness checklist

- security — No new input, write path or surface. The resolver's guard reads the model id it
  already reads. The suite's new policy rows are fixture text in a temporary directory.
- perf / scale — One file read fewer per agent in the `agents` verb. Nothing runs on a hook path.
- error / empty / loading states — An effort no record carries prints `unknown` with the existing
  note, and its line stays out of the ledger. A model with no word answers `None`. A whitespace id
  and a model two profiles match keep their exits, 2 and 1.
- observability — The `agent` line now reports an effort only where a transcript recorded one. The
  note on stderr names the field and the agent when it did not.
- risks — An agent whose transcript records no effort loses its ledger line until one does; probe
  6 found none in 80 transcripts. The two stage names in the README are typed beside the harness
  constants that own them, and nothing compares the two. The policy file is seeded, so an adopter
  that already holds one keeps its old comments.
- testing — Two assertions in the suite and five rows in the self-test, each observed RED under
  its break of the table above and GREEN restored, and the pass-time probes of AC1 to AC8.
- migration — None. No key, level or output of the two JSON verbs moves, which AC8 holds.
- user docs — `help/roles.md` moves for S6. Its `unknown` entry already covers S1.

## 6. Acceptance criteria

Run from the worktree root in one Bash shell with these names set. `SCRATCH` is the run's scratch
directory, spelled absolute, and `P` is taken before the pass's first edit.

```bash
R=tools/roles
H=$R/handoff.py; L=$R/roles_lib.py; A=$R/render_agents.py; S=$R/adopt-roles.test.sh
T=$R/house/policy.toml; D=$R/README.md; U=help/roles.md
P=$(git rev-parse HEAD)
X=$SCRATCH/u4; K=$X/kit
mkdir -p "$X/was" && git archive c1d1e19f4 tools/roles | tar -x -C "$X/was"
levels() { h=$1; shift; for w in spec-write spec-review build closing-review; do
  python "$h" stage-efforts $w "$@" || return; done; python "$h" role-efforts "$@"; }
floor() { sed -n 's/^FLOOR_ASSERTIONS=//p'; }
P_ROWS='import sys, tomllib
sys.path.insert(0, sys.argv[1])
import roles_lib as lib
base = "[effort]\ndefault = \"low\"\n\n[effort.roles]\nr-one = \"high\"\n\n[effort.stages.w5]\nk2 = \"high\"\n"
fam = base + ("\n[effort.profiles.fam]\nmatch = [\"fam\"]\ndefault = \"max\"\n\n"
              "[effort.profiles.fam.roles]\nr-two = \"xhigh\"\n\n"
              "[effort.profiles.fam.stages.w5]\nk1 = \"medium\"\n")
ven = fam + "\n[effort.profiles.ven]\nmatch = [\"vendor\", \"vend2\"]\ndefault = \"medium\"\n"
w5 = {"name": "w5", "stages": {"k1": "r-one", "k2": "r-two"}}
for text, model in ((base, None), (fam, "vendor-fam-9"), (fam, "Vendor-FAM-9"), (ven, "vend2-other-9")):
    p = tomllib.loads(text)
    print(lib.resolve_effort(p, "r-one", model), lib.resolve_effort(p, "r-two", model),
          sorted(lib.resolve_stage_efforts(p, w5, model).items()))'
P_NONE='import sys
sys.path.insert(0, sys.argv[1])
import roles_lib as lib
p = {"effort": {"default": "low", "profiles": {"x": {"default": "low"}, "y": "low"}}}
print(lib.resolve_profile(p, None), lib.resolve_profile(p, ""), lib.resolve_profile(p, " "),
      lib.resolve_effort(p, "r", None))'
```

- **AC1** — When these run over the script and the README, they print the counts shown:
  `grep -c 'EFFORT_LINE_RE' $H` prints `0`, `grep -c 'AGENTS_REL' $H` prints `0`,
  `grep -c 'level = tr\["effort"\]' $H` prints `1`, `grep -c "else the agent type's" $D` prints `0`
  and `grep -c "| effort | the agent transcript's last" $D` prints `1`.
  Red when: the verb still reads an agent type's file for a level, or the README's field table
  still names that fallback.
  figure: the five counts are `2`, `3`, `1`, `1` and `1` at `bd0a3808`, PINNED 2026-11-10.
- **AC2** — When `python -B -c "$P_ROWS" $R` runs, it prints these four lines:
  `high low [('k1', 'high'), ('k2', 'high')]`, then `max xhigh [('k1', 'medium'), ('k2', 'xhigh')]`
  twice, then `medium medium [('k1', 'medium'), ('k2', 'medium')]`.
  Red when: the pass's edit of `resolve_profile` moves a level, so a value this spec gives the
  self-test's new rows is no longer what the library answers.
  figure: the four lines are PINNED at `bd0a3808`, from probe 1 of section 4.
- **AC3** — When these run over the self-test's file, they print the counts shown:
  `grep -c '\[effort.stages.w5\]' $A` prints `1`, `grep -c '"Vendor-FAM-9"' $A` prints `1`,
  `grep -c '"vend2-other-9"' $A` prints `1`, `grep -c 'match = \["vendor", "vend2"\]' $A` prints
  `1`, `grep -c 'match = \["x", "fam"\]' $A` prints `1`, and
  `python -B -c "import ast, sys; ast.parse(open(sys.argv[1], encoding='utf-8').read())" $A` exits 0.
  Red when: arm 19 lands without the default-table stage override, the mixed-case row, the
  second-word row, the two-word profile or the two-word defect row.
  figure: the five counts are all `0` at `bd0a3808`, PINNED 2026-11-10.
- **AC4** — When `python -B -c "$P_NONE" $R` runs, it prints `None None None low` and no traceback,
  and `grep -c '^    if not words:' $L` prints `1`. The pattern is anchored at four spaces, the
  guard's own indent in `resolve_profile`.
  Red when: `resolve_profile` reads a profile's `match` for a model that holds no word. At
  `bd0a3808` the command dies with `KeyError: 'match'`.
  figure: the count is `0` at `5b7edfe1c`, PINNED 2026-11-10. The unanchored `if not words:` counts
  `1` there, the `elif not words:` at eight spaces in the profile loop of `load_policy`, and `2`
  after the build, so it is not the pattern.
- **AC5** — When these run over the three texts, they print the counts shown:
  `grep -c 'every one runs at medium' $T` prints `0`, `grep -c "stage key of a workflow's" $T`
  prints `1`, `grep -c 'no .stages. table keys' $T` prints `1`,
  `grep -c 'every role and stage runs at' $D` prints `0`, ``grep -c '`committer` and `probe`' $D``
  prints `1`, and ``grep -c 'role and stage at `medium`' $U`` prints `0`.
  Red when: a text still says every stage runs at the profile's level, or the README's limits
  paragraph does not name the two harness stages that take none.
  figure: the six counts are `1`, `0`, `0`, `1`, `0` and `1` at `bd0a3808`, PINNED 2026-11-10.
- **AC6** — When `grep -c 'A changed value reaches an agent after' $T` runs it prints `0`,
  `grep -c 'value applies at the next dispatch' $T` prints `1`, and
  `python -c "import sys, tomllib; d = tomllib.load(open(sys.argv[1], 'rb')); print(sorted(d), sorted(d['effort']['profiles']))" $T`
  prints `['effort', 'gates'] ['fable']`.
  Red when: the header still sends an owner who edited a stage or a profile to a render and a new
  session, or a moved comment breaks a table.
- **AC7** — When `bash -n "$S"` runs it exits 0, `grep -c 'check_arm "arm 9 ' "$S"` prints `8`,
  `grep -c 'check_arm "arm 19 ' "$S"` prints `5`,
  `grep -c '+1 for arm 9 and +1 for arm 19 (TOOL-aProfiledEffort-4)' "$S"` prints `1`,
  `grep -c 'effort.profiles.tven' "$S"` prints at least `1`, `grep -c 'Traceback' "$S"` prints at
  least `1`, and `echo $(( $(floor < "$S") - $(git show $P:$S | floor) ))` prints `2`.
  Red when: either arm lands without its assertion, or the floor stays where the pass found it.
  figure: the counts are `7`, `4`, `0`, `0` and `0` at `bd0a3808`, and the floor is 55; the rise is
  DERIVED against the pass's own start.
- **AC8** — When
  `for m in "" "--model claude-fable-5-2"; do levels $H $m | cmp - <(levels "$X/was/$H" $m) || echo moved; done`
  runs, it prints nothing. With `cp -R $R "$K"` done and the `tfam` and `tven` profiles of section
  4 appended to the copy's policy file, `python "$K/handoff.py" role-efforts --model ' '; echo $?`
  prints `2` after a stderr line carrying `--model is empty`, and
  `python "$K/handoff.py" stage-efforts build --model vendor-tfam-9; echo $?` prints `1` after one
  stderr line carrying `R12` and both `match` keys.
  Red when: the resolver's guard or the deleted fallback moves a level either verb prints, or
  weakens a refusal the suite's arm 19 is about to assert.
  figure: both sides of the compare are DERIVED at observation, the right from the archive of
  `c1d1e19f4`. The `tfam` profile is the one the suite's arm 19 appends at
  `tools/roles/adopt-roles.test.sh:761`.
- **AC9** — When the suite runs at the close, it prints eight `ok   arm 9` lines, five
  `ok   arm 19` lines and a final `PASS` line whose count is at or above the floor of 57.
  Red when: break B6, B7 or B8 of section 4 is applied to `tools/roles/handoff.py`. B6 reds arm 9's
  last line, B7 reds the 19d line and B8 reds the 19e line.
  permission: the suite runs at the main loop's close, never in a unit pass.
  fixture: the suite's own `build_fixture` copy of the kit.
- **AC10** — When the self-test runs at the close, it prints a final `PASS` line and exits 0.
  Red when: break B1, B2, B3, B4 or B5 of section 4 is applied to `tools/roles/roles_lib.py`. Each
  prints `render_agents selftest: FAIL arm 19` lines for the rows its table entry names and exits
  1, and under B5 the output holds no `Traceback`.
  permission: the self-test runs at the main loop's close, never in a unit pass.
  figure: the assertion count on the `PASS` line is DERIVED by the self-test, and no floor holds it.

## 7. Gates

`roles catalogue` · `roles render wiring` · `roles render selftest` · `roles adopter self-test` · `policy fixtures` · `docs` · `kit/dogfood doc parity` · `unattended kit gate` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/roles/adopt-roles.test.sh · covers AC9 · arm 9's assertion over a transcript stripped of its effort, red with the verb answering a level for it (B6), and arm 19's widened 19d and new 19e, red with the blank check weakened to an equality test (B7) and with the early dispatch catching another exception (B8) · FLOOR_ASSERTIONS, +2

New arm: tools/roles/render_agents.py --selftest · covers AC10 · arm 19's five new rows, red on the mixed-case row with the lower-casing removed (B1), on the second-word row with the match cut to its first entry (B2), on the 19c and 19f rows with the default stage overrides merged in (B3), on the two-word defect row with the word loop cut to its first entry (B4), and by FAIL lines with no traceback when the profile checks are staged out of load_policy (B5) · none

`policy fixtures` is owed because its guard names the script, the library and
`tools/roles/render_agents.py`. The two suites run at the close with the bar, after this unit is
terminal. `kit epoch` and `kit version markers` hold the moved shipped bytes, minted by the lander.
`docs` and `kit/dogfood doc parity` hold `help/roles.md` and the README. `memory hygiene` and
`spec tokens` hold this spec.

What no leg checks: the wording of the policy file's comments, of the README or of the help page;
that `committer` and `probe` are still the only harness stages no workflow table keys; and that a
real transcript records an `effort`.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-10 · initial draft, from the round 1 closing review's seven items and the
  brief's item 8, with the script, the library, the self-test, the suite and the three texts read
  at `bd0a3808`.
- rev-2 · 2026-11-10 · AC4 · S1 · §4 · AC4's grep is anchored to the guard's line, with its figure
  pinned at `5b7edfe1c`: the unanchored pattern also counted the `elif` of `load_policy`, so it read
  1 before the build and 2 after it. S1 and section 4 now put three edits the builder made in
  scope: the `print_agent_lines` docstring, the `PATH_ID_RE` comment, and the joining words of the
  README's limits clause. No other criterion and no mechanism moved. From the divergence record
  `2026-11-10-prompt-TOOL-aProfiledEffort-4-ac4-revision-brief`.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "the agents verb's effort level fallback, the profile
resolver, and the self-test arms over a profile's match list and stage overrides"` ranked name
stems only, `resolve` and `arm` among them, and none of the seams this unit touches. They were read
directly, and every one is a seam an earlier unit of this build made: `resolve_profile`,
`resolve_stage_efforts` and the word loop of `load_policy` in `tools/roles/roles_lib.py`, arm 19 of
the self-test in `tools/roles/render_agents.py` with its `build_fixture` and `check_arm`, arms 9
and 19 of `tools/roles/adopt-roles.test.sh`, and the `agents` verb of `tools/roles/handoff.py`.
This unit extends those and adds no function. For S1 the reuse is the verb's existing `unknown`
path: the fold to `unknown`, the stderr note and the ledger hold are already there, so the fix
deletes the fallback and builds nothing.

The recall probe returned the review record, this unit's brief, `TOOL-aOrientedCast-10`, which
designed the effort policy, and unit 1's spec. No record rules on the fallback to the agent type's
line beyond the review. `python tools/memory-tree/gotchas.py --for-paths` over the three code files
selected `fixture-passes-by-finding-nothing` and `guard-above-a-fold-makes-its-fallback-dead`,
which shaped arm 9's last clause and the resolver's guard. The asks probe of M5 was not run,
because this stage may not run the build-index generator.

Recall terms used: agents verb effort fallback agent type line unknown profile match resolve_profile arm 19 stage overrides committer probe

The question passed with them: "what did the closing review of aProfiledEffort confirm, and does
any record rule on the agents verb's effort fallback to the agent type's line".
