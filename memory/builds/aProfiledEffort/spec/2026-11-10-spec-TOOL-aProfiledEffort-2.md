# TOOL-aProfiledEffort-2 — the handoff verbs answer a role's and a stage's level for a named model

**Status:** CLOSED · rev-1 · 2026-11-10 · node a · Tier-2 · base 7c896db6 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-10-build-TOOL-aProfiledEffort-2-1-acceptance-ledger.md](../build/2026-11-10-build-TOOL-aProfiledEffort-2-1-acceptance-ledger.md) | journal | — |
| [2026-11-10-prompt-TOOL-aProfiledEffort-1-brief.md](../prompts/2026-11-10-prompt-TOOL-aProfiledEffort-1-brief.md) | research | TOOL-aProfiledEffort-1 TOOL-aProfiledEffort-3 |
| [2026-11-10-prompt-TOOL-aProfiledEffort-2-build-brief.md](../prompts/2026-11-10-prompt-TOOL-aProfiledEffort-2-build-brief.md) | research | — |
| [2026-11-10-review-TOOL-aProfiledEffort-1-closing-diff-round1.md](../reviews/2026-11-10-review-TOOL-aProfiledEffort-1-closing-diff-round1.md) | diff-review | TOOL-aProfiledEffort-1 TOOL-aProfiledEffort-3 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/roles/handoff.py` prints the reasoning effort of one workflow's stages, cannot be told which
model is in use, and does not answer a role's level at all. This unit gives `stage-efforts` a
`--model` flag and adds the verb `role-efforts`, both resolved by the profile resolver
`TOOL-aProfiledEffort-1` builds, so a dispatcher can ask for the levels of the model it runs. With
no flag, `stage-efforts` prints the bytes it prints today. The brief is
`memory/builds/aProfiledEffort/prompts/2026-11-10-prompt-TOOL-aProfiledEffort-1-brief.md`, item 5.

## 2. Scope (IN)

"The script" is `tools/roles/handoff.py`, and "the suite" is `tools/roles/adopt-roles.test.sh`.
Every "Observed by" below names this spec's own criteria.

- **S1** — `stage-efforts <workflow>` takes an optional `--model <id>`. With it, each stage key
  prints the level the resolver gives that model id. Without it, the output is byte for byte the
  output at the build's base. Observed by AC1, AC2 and AC3.
- **S2** — A new verb, `role-efforts [--model <id>]`, prints one line of sorted JSON mapping every
  role whose `agent` is true to its level, resolved the same way. With no flag each value equals
  that role's rendered `effort:` line. Observed by AC2, AC3 and AC5.
- **S3** — The two verbs hold no profile logic. They pass the id, unchanged, to
  `roles_lib.resolve_effort` and `roles_lib.resolve_stage_efforts`, read no profile table
  themselves and name no model family, so a profile added to the policy file reaches both with no
  code edit. Observed by AC4 and AC7.
- **S4** — A `--model` value that is empty or only whitespace refuses with exit 2 and a message
  naming the flag. A policy defect refuses `role-efforts` with exit 1 and the R12 line, as it
  refuses `stage-efforts` today. Observed by AC6.
- **S5** — The three verbs that print one line of sorted JSON share one writer, and the
  `harness-args` output does not move. Observed by AC1 and AC7.
- **S6** — The script's header states both spellings in its usage block, what each prints with and
  without the flag, and what `--model` does not check. Observed by AC7.
- **S7** — The suite gains arm 19 with four assertions, its header gains the arm's clause in both
  lists, and `FLOOR_ASSERTIONS` rises by 4 under a comment naming this unit. Observed by AC8 and
  AC9.

## 3. Non-goals (OUT)

- **The resolver, the profile tables, their R12 validation and the seeded `fable` profile.** They
  are `TOOL-aProfiledEffort-1`'s. This unit edits neither `tools/roles/roles_lib.py` nor
  `tools/roles/house/policy.toml`.
- **Every carrier that spells a call.** The build Skill template and its render, the unattended
  verbs guide, the roles README, the workflows README, the harness templates' comments and the
  `help/` page belong to `TOOL-aProfiledEffort-3`, which rules on each.
- **A source for the model when the flag is absent.** No environment variable and no session probe
  supplies one. The caller names the model, and an absent flag means the default levels.
- **A note or a refusal for an id no profile matches.** The brief's acceptance 3 fixes the answer as
  the no-model output, and this unit adds nothing to it.
- **The name of the profile that answered.** No acceptance reads it. `resolve_profile`, which
  `TOOL-aProfiledEffort-1` S4 builds, answers it for a later caller that needs it.
- **`render`, `agents`, `harness-args` beyond S5, and `tools/roles/render_agents.py`.** The agent
  types' `effort:` lines stay the default profile's, as the build README rules.
- **A `[[usage]]` row in `tools/govkit/usage.toml`.** `stage-efforts` has none today, and the help
  page that would anchor one is `TOOL-aProfiledEffort-3`'s.
- **A hook that refuses a spawn at a level its profile does not give.** The brief files it as an
  ask.
- **A hand bump of the kit version.** Kit versions move through the lander's `mint`.

### Edges

- **consumes-from** `TOOL-aProfiledEffort-1` — the model argument of `roles_lib.resolve_effort` and
  `roles_lib.resolve_stage_efforts`, a `load_policy` result that carries the profiles, and the
  seeded `fable` profile; without them the flag has nothing to hand the id to, and AC2 and AC4
  cannot be observed
- **hands-off** `TOOL-aProfiledEffort-3` — the dispatch carriers and documents spell `--model` on
  their `stage-efforts` calls and name `role-efforts` in the direct-spawn rule; this unit edits no
  carrier, so until that unit lands the script's header is the only text naming either

## 4. Design

### Evidence

Read at the build branch's tip `fc2695a2` on 2026-11-10. The `base` field is `7c896db6`, the run's
pinned BASE. Line numbers are PINNED to that reading, and the builder finds each site by its quoted
text.

| Site | Where | What it holds today |
|---|---|---|
| the verb | `tools/roles/handoff.py:474` | `print_stage_efforts(workflow)` loads the workflows and the policy, then writes `lib.resolve_stage_efforts(policy, entry)` |
| the two JSON writes | `tools/roles/handoff.py:470` and `tools/roles/handoff.py:487` | the same `json.dumps` call with sorted keys, compact separators and one newline, typed twice |
| the parsers | `tools/roles/handoff.py:953` and `tools/roles/handoff.py:954` | `harness-args` and `stage-efforts` take one positional each and no option |
| the early dispatch | `tools/roles/handoff.py:966` | both verbs return before the repository is resolved at `tools/roles/handoff.py:994`, and a `RolesError` exits 1 |
| the resolvers | `tools/roles/roles_lib.py:590` and `tools/roles/roles_lib.py:596` | `resolve_effort(policy, slot)` and `resolve_stage_efforts(policy, workflow)`, two arguments each |
| the agent test | `tools/roles/render_agents.py:275` | `role["keys"].get("agent", "true") == "true"` |
| the suite's fixture | `tools/roles/adopt-roles.test.sh:92` | `build_fixture` copies the whole kit, its policy file included, and scaffolds it |
| the suite's floor | `tools/roles/adopt-roles.test.sh:82` | `FLOOR_ASSERTIONS=51`, and the last arm is arm 18 at `tools/roles/adopt-roles.test.sh:723` |

Three probes were run against that tip. `python tools/roles/handoff.py stage-efforts build --model x`
exits 2 with `unrecognized arguments`. A copy of the kit in a scratch directory answers
`stage-efforts` from its own files, so the verb needs no repository: it reads the kit directory,
and the gate manifest of its tool root where one is present. No suite or self-test under `tools/`
spells `stage-efforts`, so the verb has no arm today.

The four no-model lines, PINNED at `fc2695a2` on 2026-11-10 and re-derived by AC1 from the base:

```text
spec-write      {"builder":"high","disposal":"high","skeptic":"medium","specFinder":"medium","specWriter":"high","synthesis":"medium"}
spec-review     {"skeptic":"medium","specFinder":"medium","synthesis":"medium"}
build           {"builder":"high"}
closing-review  {"diffFinder":"medium","skeptic":"medium","synthesis":"high"}
```

### The verbs

The sketch below is the shape. `TOOL-aProfiledEffort-1` S5 gives both resolvers a third parameter,
`model=None`, and answers the default tables for `None`, which is what the verbs pass when the flag
is absent. The builder calls both resolvers by the signature that unit built.

```python
def write_json_line(obj):
    """One line of sorted, compact JSON on stdout: the shape a harness argument takes."""
    sys.stdout.buffer.write((json.dumps(obj, sort_keys=True, separators=(",", ":"),
                                        ensure_ascii=False) + "\n").encode("utf-8"))


def print_stage_efforts(workflow, model=None):
    ...  # unchanged down to the write
    write_json_line(lib.resolve_stage_efforts(policy, entry, model))


def print_role_efforts(model=None):
    """Print the resolved level of every role whose `agent` is true as one line of sorted JSON
    (TOOL-aProfiledEffort-2); RolesError on a policy defect."""
    roles = lib.load_roles(KIT_DIR)
    policy = lib.load_policy(KIT_DIR, roles, lib.load_workflows(KIT_DIR))
    write_json_line({slot: lib.resolve_effort(policy, slot, model) for slot, role in roles.items()
                     if role["keys"].get("agent", "true") == "true"})
```

`print_harness_args` calls `write_json_line(union)` in place of its own write. In `main`, the
`stage-efforts` parser gains `--model`, a `role-efforts` parser takes `--model` alone, and the early
dispatch at `tools/roles/handoff.py:966` admits the third verb inside the same `try`. One check sits
before that dispatch:

```python
if getattr(a, "model", None) is not None and not a.model.strip():
    ap.error("--model is empty: name the model id in use, or leave the flag off for the default levels")
```

The empty value is refused because it is what an unset variable expands to in a caller's command.
Answering it with the default levels would run a Fable session at `high` in silence, which is the
detriment this build exists to remove. The id reaches a comparison in the resolver and nothing
else: it is joined into no path, command or file, so it takes no shape rule beyond non-empty.

### The header

The usage block's `stage-efforts` line becomes the first line below, and the second follows it:

```text
    python handoff.py stage-efforts <workflow> [--model <id>]
    python handoff.py role-efforts [--model <id>]
```

The paragraph that describes `stage-efforts` gains these facts, in the header's own prose. With
`--model <id>` the two verbs resolve the levels the policy's profiles give that model id. Without
the flag, or for an id no profile matches, they resolve the default tables. `role-efforts` prints
the level of every role whose `agent` is true, and a direct spawn passes its role's value. The
`WHAT THIS DOES NOT CHECK` paragraph gains one sentence that opens with the words `For --model:`,
the flag in backticks, on one line. It says the script does not check that the id is the model the
session or the spawned agent runs, since the caller types it, and that an id no profile matches
answers the default levels with no note. The header names no model family: profile names live in
the policy file alone.

### The suite's arm

Arm 19 goes after arm 18 and before the floor check. It calls `build_fixture` once and defines no
shell function. `TOOL-aProfiledEffort-1` also numbers an arm 19, in the self-test of
`tools/roles/render_agents.py`, which is another suite. The arm appends the profile below to the
fixture's `house/policy.toml`, in the grammar of that unit's §4 "Data model":

```toml
[effort.profiles.tfam]
match = ["tfam"]
default = "low"

[effort.profiles.tfam.roles]
gov-builder = "max"

[effort.profiles.tfam.stages.closing-review]
synthesis = "xhigh"
```

By that unit's matching rule the profile answers the model id `vendor-tfam-9`, and no profile
answers `vendor-other-9`.

| Assertion | What it asserts |
|---|---|
| 19a | With no flag, `stage-efforts` for `spec-write` and `closing-review` and `role-efforts` each print the bytes an inline re-derivation prints from the fixture's default tables, with the profile already appended |
| 19b | With `--model vendor-other-9`, the same three calls print the no-flag bytes |
| 19c | With `--model vendor-tfam-9`, `role-efforts` carries `"gov-builder":"max"`, `stage-efforts closing-review` carries `"synthesis":"xhigh"`, and neither line equals its no-flag line |
| 19d | With `--model ""`, both verbs exit 2 and stderr names `--model` |

The re-derivation in 19a is an inline program that imports nothing from the kit, so the guard
shares no code with what it guards. It reads the fixture's `house/policy.toml`, its
`workflows.toml` and the scaffolded `.claude/roles.json`:

```python
import json, pathlib, sys, tomllib
kit, index, what = pathlib.Path(sys.argv[1]), sys.argv[2], sys.argv[3]
with open(kit / "house" / "policy.toml", "rb") as fh:
    effort = tomllib.load(fh)["effort"]
def level(slot):
    return effort.get("roles", {}).get(slot, effort["default"])
if what == "roles":
    with open(index, encoding="utf-8") as fh:
        out = {s: level(s) for s, r in json.load(fh)["roles"].items() if r["agent"]}
else:
    with open(kit / "workflows.toml", "rb") as fh:
        stages = next(w["stages"] for w in tomllib.load(fh)["workflow"] if w["name"] == what)
    over = effort.get("stages", {}).get(what, {})
    out = {k: over.get(k, level(s)) for k, s in stages.items()}
sys.stdout.buffer.write((json.dumps(out, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8"))
```

That program printed the tree's four `stage-efforts` lines byte for byte at `fc2695a2`. It reads
the `[effort]` tables, which the brief's item 1 keeps as the default for a model no profile matches.

Three bug classes that `python tools/memory-tree/gotchas.py --for-paths` selects for these two files
shaped the arm. The arm reads no git revision, so no legitimate edit of the script reds it by moving
a sha (`memory/gotchas/test-oracle-read-from-a-historical-sha.md`). 19c's last clause reds the arm
when a default table already gives the arm's literals, where it would otherwise pass by finding
nothing (`memory/gotchas/fixture-passes-by-finding-nothing.md`). The arm proves that the verbs hand
the model to the resolver, and it does not prove the seeded `fable` values, which are
`TOOL-aProfiledEffort-1`'s data (`memory/gotchas/staged-break-substitutes-a-synthetic-value.md`).

The suite's header gains one clause for arm 19 in its list of arms and one sentence in its
`WHAT THIS DOES NOT CHECK` list: the arm does not check any profile the policy file seeds, nor the
resolver's order inside a profile. The floor comment gains a line in the house shape, holding the
words `+4 for arm 19 (TOOL-aProfiledEffort-2)` on one line.

### The staged breaks the main loop observes

Two breaks, each applied to the script alone and restored with
`git checkout -- tools/roles/handoff.py` before the next one and before the bar.

1. The two verbs' resolver calls pass `None` in place of the model. 19c reds, and 19a, 19b and 19d
   stay green.
2. `write_json_line` drops its `separators` argument. 19a reds, because the re-derivation keeps the
   compact form, and 19c reds with it, because its two needles are compact. 19b and 19d stay green.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `role-efforts` | subcommand of the script | none grades a subcommand; `stage-efforts` and `harness-args` are the precedent spelling |
| `--model` | flag of `stage-efforts` and `role-efforts` | none grades a flag |
| `print_role_efforts` | function | `py.function`; `lexicon.py --suggest` answered OK on 2026-11-10 |
| `write_json_line` | function | `py.function`; `lexicon.py --suggest` answered OK on 2026-11-10 |
| `tfam` | profile name in the suite's fixture | not graded |
| `vendor-tfam-9`, `vendor-other-9` | model ids in the suite's fixture | not graded |

### Rollout

1. Confirm `TOOL-aProfiledEffort-1` is built, and read the resolver's signature and the seeded
   profile's grammar from the tree.
2. Edit the script: the writer, the two verbs, the parsers, the empty-value check and the header.
3. Edit the suite: arm 19, the header's two additions and the floor.
4. Verify in the pass with AC1 to AC8. The pass runs no gate leg and no suite.
5. Commit once with the unit id in the subject, staging the two files below.
6. The main loop observes AC9 at the close, red under each staged break and green once restored.

### Files touched (estimate)

`tools/roles/handoff.py` · `tools/roles/adopt-roles.test.sh`

### Alternatives rejected

- **`render --model` printing the level on stderr beside the description line.** It ties an answer
  to a render that needs a card and inputs and writes a prompt file. The brief's item 5 asks the
  script to answer a role's level, and its acceptance 2 reads every role whose `agent` is true,
  which would cost one full render per role.
- **`role-effort <role>` printing one bare level.** It needs two refusals `role-efforts` does not
  have, an unknown role and a role whose `agent` is false, and acceptance 2 would loop over it.
  The JSON of every agent role is the shape `stage-efforts` already prints for every stage key.
- **Reading the model from the environment when the flag is absent.** It is a second channel that
  leaves no trace in the command a carrier spells, and the brief's item 6 has each dispatch route
  pass the model.
- **Treating an empty `--model` as no model.** The reason is under "The verbs" above.
- **A third copy of the JSON write.** The charter's `[reuse]` rule extracts at the second instance,
  and the script already holds two.

## 5. Production-readiness checklist

- security — The one new input is the `--model` operand. It is refused when empty, compared by the
  resolver and joined into no path, command or file. No write path and no surface is added.
- perf / scale — One TOML parse per call, as today. Nothing runs on a hook path.
- error / empty / loading states — An empty id exits 2 naming the flag. A policy defect exits 1
  with its R12 line. An id no profile matches is no error and answers the default levels.
- observability — Nothing records which model a caller named or which profile answered. The level
  and the model an agent ran at are already on the `agent` line that `handoff.py agents` prints.
- risks — A caller that names the wrong model gets that model's levels in silence, and the header
  says so. A moved no-model output would change every harness call's levels, which AC1 and
  assertion 19a hold.
- testing — Arm 19, observed RED on each staged break and GREEN at the close, and the pass-time
  probes of AC1 to AC8.
- migration — None. The flag and the verb are additive, and a caller that passes no flag is
  unmoved.
- user docs — Handed to `TOOL-aProfiledEffort-3`, which owns the roles README and the `help/` page.
  Until it lands in this same build the script's header is the only text naming the flag and verb.

## 6. Acceptance criteria

Run from the worktree root in one Bash shell with these names set. `SCRATCH` is the run's scratch
directory, spelled absolute, and `P` is taken before the pass's first edit.

```bash
H=tools/roles/handoff.py
S=tools/roles/adopt-roles.test.sh
B=7c896db6
P=$(git rev-parse HEAD)
X=$SCRATCH/u2; K=$X/kit; BAD=$X/bad
W="spec-write spec-review build closing-review"
mkdir -p "$X/base" && git archive $B tools/roles | tar -x -C "$X/base"
levels() { h=$1; shift; for w in $W; do python "$h" stage-efforts $w "$@" || return; done; python "$h" role-efforts "$@"; }
same_as_base() { python "$X/base/$H" "$@" >"$X/b" && python $H "$@" >"$X/t" && cmp "$X/b" "$X/t"; }
P_LEVELS='import json, sys
r = [json.loads(x) for x in sys.stdin]
print(len(r), sum(map(len, r)), sorted({v for d in r for v in d.values()}))'
P_AGENTS='import json, pathlib, re, sys
d = json.load(sys.stdin)
idx = json.loads(pathlib.Path(".claude/roles.json").read_text(encoding="utf-8"))["roles"]
same = all(re.search("^effort: %s$" % v, pathlib.Path(".claude/agents/%s.md" % k).read_text(encoding="utf-8"), re.M) for k, v in d.items())
print(len(d), same, sorted(d) == sorted(k for k, r in idx.items() if r["agent"]))'
```

- **AC1** — When `for w in $W; do same_as_base stage-efforts $w || echo moved; done` runs, it prints
  nothing, and so does
  `for h in unattended-build unattended-unit tier2-review; do same_as_base harness-args $h || echo moved; done`.
  Red when: the no-flag call resolves through a profile, or the shared writer changes a separator,
  the key order or the newline.
  figure: both sides are DERIVED at observation, the left from the base archive.
- **AC2** — When `levels $H | python -c "$P_LEVELS"` runs it prints `5 22 ['high', 'medium']`, and
  `levels $H --model claude-fable-5-2 | python -c "$P_LEVELS"` prints `5 22 ['medium']`, as does the
  same command with `claude-fable-6-0`.
  Red when: a verb drops the id on its way to the resolver, so a Fable line keeps `high`, or a
  profile changes the key set, so a count moves.
  fixture: the seeded `fable` profile of `TOOL-aProfiledEffort-1`. `claude-fable-5-2` is this
  session's id, and both ids hold the word `fable` that unit's matching rule reads.
  figure: `5 22` and the no-flag level list are PINNED at `fc2695a2` on 2026-11-10, the four
  workflows' 13 stage keys and 9 agent roles. What is asserted is that a Fable line keeps both
  counts and carries `medium` alone.
- **AC3** — When `levels $H >"$X/plain"; levels $H --model vendor-other-9 >"$X/other"; cmp "$X/plain" "$X/other"`
  runs, `cmp` exits 0 and prints nothing.
  Red when: an id no profile matches refuses, or resolves through some profile.
- **AC4** — With `cp -R tools/roles "$K"` done and the `tfam` profile of "The suite's arm" appended
  to the copy's policy file, `python "$K/handoff.py" role-efforts --model vendor-tfam-9` prints a
  line carrying `"gov-builder":"max"`, and `python "$K/handoff.py" stage-efforts closing-review --model vendor-tfam-9`
  prints a line carrying `"synthesis":"xhigh"`. Then `levels "$K/handoff.py" | cmp - "$X/plain"` and
  `levels "$K/handoff.py" --model claude-fable-5-2 | python -c "$P_LEVELS"` print nothing and
  `5 22 ['medium']`, and `cmp $H "$K/handoff.py"` exits 0.
  Red when: a verb reads profiles by a name typed in the script, so a new profile needs a code edit,
  or the appended profile moves the default or the Fable answer.
  fixture: the profile grammar of `TOOL-aProfiledEffort-1`; `$X/plain` is the file AC3 wrote.
- **AC5** — When `python $H role-efforts | python -c "$P_AGENTS"` runs, it prints `9 True True`.
  Red when: the no-flag call resolves through a profile, so a value leaves its agent type's
  `effort:` line, or the verb lists a role whose `agent` is false.
  figure: `9` is PINNED at `fc2695a2`; the two booleans are DERIVED from the rendered agent types
  and the role index.
- **AC6** — When `python $H stage-efforts build --model ""; echo $?` and
  `python $H role-efforts --model " "; echo $?` run, each prints `2` after a stderr line carrying
  `--model is empty`, and no JSON. With `cp -R tools/roles "$BAD"` done and
  `sed -i 's/^default = "medium"/default = "loud"/' "$BAD/house/policy.toml"` applied,
  `python "$BAD/handoff.py" role-efforts; echo $?` prints `1` after a stderr line carrying `R12` and
  `effort.default`.
  Red when: an empty id is answered with the default levels, or `role-efforts` sits outside the
  dispatch's `try` and a policy defect raises a traceback. The first two commands exit 2 today for
  another reason, an unrecognised argument or verb, so the criterion reads the message.
- **AC7** — When these run over the script, they print the counts shown:
  `grep -c 'python handoff.py stage-efforts <workflow> \[--model <id>\]' $H` prints `1`,
  `grep -c 'python handoff.py role-efforts \[--model <id>\]' $H` prints `1`,
  `grep -c 'For .--model.:' $H` prints `1`, `grep -c 'separators=' $H` prints `1`,
  `grep -ci 'fable' $H` prints `0` and `grep -c 'policy\[' $H` prints `0`.
  Red when: the header omits a spelling or the flag's limit, a JSON write is typed a second time,
  or the script names a model family or indexes the policy itself.
  figure: the six counts are `0`, `0`, `0`, `2`, `0` and `0` at `fc2695a2`, PINNED 2026-11-10.
- **AC8** — When `bash -n "$S"` runs it exits 0, `grep -c 'check_arm "arm 19 ' "$S"` prints `4`,
  `grep -c '+4 for arm 19 (TOOL-aProfiledEffort-2)' "$S"` prints `1`, and
  `echo $(( $(sed -n 's/^FLOOR_ASSERTIONS=//p' "$S") - $(git show $P:$S | sed -n 's/^FLOOR_ASSERTIONS=//p') ))`
  prints `4`.
  Red when: the arm lands with another count of assertions, or the floor stays where the pass found
  it.
  figure: the floor is 51 at `fc2695a2`, and the rise is DERIVED against the pass's own start.
- **AC9** — When the suite runs at the close, it prints four `ok   arm 19` lines and a final `PASS`
  line whose count is at or above the floor.
  Red when: either staged break of section 4 is applied to `tools/roles/handoff.py`. The first reds
  19c alone, and the second reds 19a and 19c.
  permission: the suite runs at the main loop's close, never in a unit pass.
  fixture: the suite's own `build_fixture` copy of the kit, with `TOOL-aProfiledEffort-1` built.

## 7. Gates

`roles adopter self-test` · `roles catalogue` · `roles render wiring` · `roles render selftest` · `policy fixtures` · `lexicon naming predicates` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/roles/adopt-roles.test.sh · covers AC9 · arm 19 over a fixture kit whose policy gains one profile, red on 19c with the model dropped at the verbs' resolver calls and red on 19a with the shared writer's separators removed, green once each is restored · FLOOR_ASSERTIONS, +4

`policy fixtures` is owed because its guard names `tools/roles/handoff.py`. The suite is the
`roles adopter self-test` leg, and it runs at the close with the bar, after the last unit is
terminal. `kit epoch` and `kit version markers` hold the moved shipped bytes, minted by the lander.
`memory hygiene` and `spec tokens` hold this spec.

What no leg checks: that the id a caller names is the model its session runs, and that any carrier
passes the flag at all. The second is `TOOL-aProfiledEffort-3`'s to make observable.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-10 · initial draft, from the brief's item 5 and acceptance 1 to 4, the script, the
  roles library, the policy file and the suite read at `fc2695a2`, and `TOOL-aProfiledEffort-1`'s
  spec as authored the same day, for the resolvers' signature and the profile grammar.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "print a role's reasoning effort level and a workflow's
stage levels for a named model"` returned `resolve_effort` and `resolve_stage_efforts` in
`tools/roles/roles_lib.py`, beside `load_workflows`, `load_roles` and `RolesError` in the same file.
Those are the seams this unit calls. It did not rank the verb itself, so the seam this unit extends
was read directly: `print_stage_efforts` at `tools/roles/handoff.py:474`, its parser and its early
dispatch in `main`, and its twin `print_harness_args`, whose JSON write the two share. The arm
extends the handoff arms of `tools/roles/adopt-roles.test.sh`, arms 8 to 10, and reuses its
`build_fixture` and `check_arm`. No existing verb answers a role's level, so `role-efforts` is new
and is built on `resolve_effort`, the function `tools/roles/render_agents.py:278` already calls for
the agent types.

The recall probe returned `TOOL-aOrientedCast-10`, which designed the policy and `stage-efforts`,
the reuse-scout rows of `TOOL-dBoundRoles-21`, and this build's brief. No record ties a level to a
model. The records and the source disagreed on one point: the scout rows cite the resolvers at
`roles_lib.py` lines 565 to 576, and they sit at 590 to 601 at `fc2695a2`. The code was taken over
the record. `TOOL-dBoundRoles-21` is DEFERRED and later re-points the policy's readers; it inherits
the flag and the verb as built. The asks probe of M5 was not run, because this stage may not run the
build-index generator.

Recall terms used: handoff stage-efforts effort policy resolve_effort resolve_stage_efforts efforts harness model profile direct spawn agent line

The question passed with them: "which handoff verb prints the effort level a role or a workflow
stage takes, and does any record tie a level to the model in use".
