# TOOL-aProfiledEffort-3 — every dispatch route names the session's model and spawns at the level the resolver returns

**Status:** SPECCED · rev-2 · 2026-11-10 · node a · Tier-2 · base ae6735c1 · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-10-prompt-TOOL-aProfiledEffort-1-brief.md](../prompts/2026-11-10-prompt-TOOL-aProfiledEffort-1-brief.md) | research | TOOL-aProfiledEffort-1 TOOL-aProfiledEffort-2 |
| [2026-11-10-prompt-TOOL-aProfiledEffort-3-1-spec-writer.md](../prompts/2026-11-10-prompt-TOOL-aProfiledEffort-3-1-spec-writer.md) | journal | — |
| [2026-11-10-prompt-TOOL-aProfiledEffort-3-build-brief.md](../prompts/2026-11-10-prompt-TOOL-aProfiledEffort-3-build-brief.md) | research | — |
| [2026-11-10-prompt-TOOL-aProfiledEffort-3-token-fix-brief.md](../prompts/2026-11-10-prompt-TOOL-aProfiledEffort-3-token-fix-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-aProfiledEffort-1` gives the effort policy a profile per model family, and
`TOOL-aProfiledEffort-2` lets `handoff.py` resolve for a named model. Neither reaches an agent by
itself: every agent type is `model: inherit` and its `effort:` line stays the default tables', so a
profile takes effect only where the dispatcher passes a level. This unit makes each carrier that
orders a dispatch name the model in use and pass the level the resolver returns: the `/build`
Skill's harness calls, the unattended verbs guide's harness calls, and a direct role spawn. The
roles README and the `help/` page then say how to add a profile and how one reaches an agent. The
brief is `memory/builds/aProfiledEffort/prompts/2026-11-10-prompt-TOOL-aProfiledEffort-1-brief.md`,
items 6 and 7.

## 2. Scope (IN)

Line numbers are PINNED at `fc2695a2`, read 2026-11-10; the builder finds each site by its text.

- **S1** — In `tools/roles/SKILL.template.md`, each of the four `stage-efforts` calls, at `:28`,
  `:51`, `:69` and `:79`, carries `--model <id>`, the call and its flag on one line. The
  harness-call sentence at `:27-28` states the model in use once, per §4 "The model in use".
  Observed by AC1.
- **S2** — The direct-spawn bullet of the same file (`:23-26`) states the rule of §4 "The
  direct-spawn rule", so every direct spawn the Skill orders inherits it, stage 5's spec-writer
  spawn at `:72` included. Observed by AC1 and AC7.
- **S3** — `.claude/skills/build/SKILL.md` is re-rendered by
  `bash tools/roles/adopt-roles.sh --scaffold`, and that run moves no agent type. Observed by AC2.
- **S4** — In `tools/unattended/VERBS.template.md`, the `efforts` sentence (`:793-795`) spells
  `handoff.py stage-efforts <workflow> --model <id>` and states the model in use, and the same
  bullet states the direct-spawn rule in one sentence. `memory/guides/UNATTENDED-VERBS.md` is
  installed from it by `bash tools/unattended/adopt-unattended.sh`. Observed by AC3.
- **S5** — In `tools/roles/README.md`, the three `stage-efforts` spellings (`:68`, `:182`, `:306`)
  carry `--model <id>`, "The handoff renderer" names `role-efforts` beside them and states the
  direct-spawn rule where it describes the `Agent` call (`:61-65`), and "The effort policy"
  (`:171-191`) gains the account of §4 "The documents". Observed by AC4 and AC6 for its tokens.
  NOT OBSERVED beyond them: whether the prose is accurate is the closing review's reading
  against §4.
- **S6** — In `tools/workflows/README.md`, the sentence that tells a caller how to compose
  `efforts` (`:813-814`) spells the call with `--model <id>` on one line and points at the roles
  README for what the id is. Observed by AC4.
- **S7** — `help/roles.md` carries facts 1, 2 and 4 of §4 "The documents" in its own short form,
  at three sites: step 4 (`:25-27`), the "Hand one task to one agent" bullet (`:33-41`), and one new
  bullet on giving a model its own levels, placed after the effort bullet (`:44-46`). Observed by
  AC5 and AC6.

## 3. Non-goals (OUT)

- The policy file, the resolvers and their validation, and `handoff.py` with its suite. They are the
  two earlier units', and this unit edits no code.
- The agent types' `effort:` lines and `tools/roles/render_agents.py`. A type is read once at
  session start and cannot follow the model, as the build README rules.
- The header comments of the harness templates, `tools/workflows/tier2-review.template.js:210` and
  `tools/workflows/unattended-build.template.js:224`. Each says the caller passes what the verb
  prints, which stays true. An edit would move two templates, their two renders and the suites that
  read those headers, for a comment. `TOOL-aProfiledEffort-2` §3 leaves them to this unit, and this
  unit's disposition is to leave them as they are.
- The refusal texts of the hooks kit, `tools/hooks/agent-cap.js:659` and its neighbours. A refusal
  names what makes a call legal, and `effort` is no part of that.
- A hook or a gate arm that refuses a spawn made without the profile's level, or a carrier whose
  call lacks the flag. The brief files the hook as an ask. What that leaves open is in §5 "risks".
- A `[[usage]]` row in `tools/govkit/usage.toml` for `stage-efforts` or `role-efforts`. Four
  `handoff.py` verbs have none today, and rowing two of them is the docs leg's own unit.
- A verb or an environment read that derives the session's model. `TOOL-aProfiledEffort-2` §3 rules
  that the caller names it.
- The map dossiers under `memory/map/features/`, whose sentences about the verb stay true.
- The main session's own effort, a profile for any model but Fable, and a by-hand move of any kit
  version.

**What it is built on.** The carriers extended here are `KICK-aOrientedCast-2`'s Skill,
`TOOL-aOrientedCast-9`'s verbs sentence and `TOOL-aOrientedCast-10`'s `efforts` sentences in both.
All three specs are terminal, so they are named here and not as edges.

### Edges

- **consumes-from** `TOOL-aProfiledEffort-1` — the profile table grammar and the seeded `fable`
  profile the documents describe, and the matching rule that says which model ids a profile
  answers; without them S5 and S7 describe a table the policy file does not hold
- **consumes-from** `TOOL-aProfiledEffort-2` — the `--model` flag of `stage-efforts` and the verb
  `role-efforts`; without them every carrier spells a call the script refuses with exit 2
- **consumes-from** external — a Claude Code whose `Agent` tool takes an `effort` parameter and
  whose `Workflow` runtime reads `opts.effort`, read in the 2.1.321 binary (§4 "Evidence")
- **hands-off** external — the version moves of the roles, unattended and review-harness kits,
  which the lander's mint writes at landing

## 4. Design

### Evidence

Read at `fc2695a2` on 2026-11-10, node a; the header's base is the default-branch commit under it.
The two sibling specs were read at rev-1, on disk and uncommitted, for the names this unit spells.

- Every role file with an agent type declares `model: inherit`
  (`tools/roles/agents/gov-builder.agent.md:5`, and line 5 of its eight siblings), and no harness
  passes a `model` option: `git grep -n "opts.model\|model:" -- tools/workflows/*.template.js`
  prints nothing. So an agent runs on the session's model.
- A harness applies a level only where its caller passed one, per stage key
  (`tools/workflows/unattended-build.js:581`, `tools/workflows/unattended-unit.js:336`,
  `tools/workflows/tier2-review.js:565`), and the build harness forwards its caller's levels to the
  review call and to `dispatch.args` (`tools/workflows/unattended-build.js:1751`, `:3031`). So one
  `efforts` object per harness call reaches every agent that call spawns.
- The render writes each type's `effort:` line from `resolve_effort` with no model
  (`tools/roles/render_agents.py:278`), and `TOOL-aProfiledEffort-1` §3 keeps it so.
- The spawn guard reads an `Agent` call's `subagent_type`, prompt and `description`
  (`tools/hooks/agent-cap.js:673-683`, `:723`) and no other key, so a call carrying `effort` passes
  it as before.
- The verbs guide and its installed copy are one file twice. The kit gate compares them
  (`tools/unattended/check-unattended.sh:3502-3506`) and the adopter's install arm rewrites the copy
  where it drifted (`tools/unattended/adopt-unattended.sh:1074-1076`).
- The docs leg reads a page command only from a `bash`, `sh` or `console` fence or from a span
  opening `python`, `python3` or `bash` (`tools/govkit/docs_leg.py:253-256`), and it holds rows for
  `render` and `roster` alone (`tools/govkit/usage.toml:74-86`). `help/roles.md:73-74` already
  spells an unrowed verb in a span opening `handoff.py`.
- The install-prefix leg refuses a kit path spelled under gov's own prefix in a shipped file
  (`tools/check-install-prefix.sh:2`). The Skill template spells the script as `handoff.py` under
  the alias its line 11-12 declares, and the README as `handoff.py`.
- The CLI, PINNED: measured 2026-11-10 by reading as text the binary `CLAUDE_CODE_EXECPATH` names,
  version 2.1.321. The `Agent` tool's input schema holds an optional `effort` taking the five named
  levels, described "Reasoning effort for this agent. Set this ONLY when the user, or instructions
  such as CLAUDE.md or a skill, explicitly ask". The schema omits it when the environment variable
  `CLAUDE_CODE_EFFORT_LEVEL` holds a level, `unset` or `auto`. The `Workflow` API still documents
  `opts.effort`. The session's environment text is built as "You are powered by the model named",
  the name, then "The exact model ID is" and the id.

### The model in use

It is the session's own model id, exactly as the session's environment states it, read again at
each call and never remembered from an earlier one. This build's own session reads
`claude-fable-5-2`. The session's id is the agent's id because every type inherits the model and no
carrier passes one. `TOOL-aProfiledEffort-1` §4 "Matching" reads an id by its words, so a provider
prefix or a version suffix changes no answer.

Each carrier that orders a call states this in one sentence. The roles README alone states the
limits, and the other carriers point at it.

### The direct-spawn rule

A direct spawn's `Agent` call also carries `effort`: its role's value in the JSON
`handoff.py role-efforts --model <id>` prints. The rule is always the same. For a model no profile
matches, the value equals the agent type's own line, so passing it changes nothing. The CLI text
quoted above is why the rule must be written in a Skill or a governing document: a session sets
that parameter only where such a text asks for it.

Every carrier that states the rule writes the words `Agent` call and `effort`, each in backticks
and in that order, on ONE line, and spells `role-efforts --model` on one line. That is the shape
the observation below reads.

### The carrier texts

| Carrier | Site | What it says after this unit |
|---|---|---|
| `tools/roles/SKILL.template.md` | `:27-28` | every harness call carries `efforts`, the JSON `handoff.py stage-efforts <workflow> --model <id>` prints, and `<id>` is the model in use |
| the same | `:23-26` | the direct-spawn rule, after the `render` line |
| the same | `:51`, `:69`, `:79` | the three named calls, each with `--model <id>` |
| `tools/unattended/VERBS.template.md` | `:793-795` | the same `efforts` sentence with the flag, the model in use, and the direct-spawn rule |
| `tools/workflows/README.md` | `:813-814` | compose `efforts` with the flagged call; the roles README says what the id is |

The sentence at `tools/unattended/VERBS.template.md:795-797`, which tells a tree without the roles
kit to pass no `efforts`, stays as it is.

### The documents

"The effort policy" in `tools/roles/README.md` gains these facts, in its own prose.

1. `[effort.profiles.<name>]` is a profile for one model family. It holds `match` and `default`,
   and optionally `roles` and `stages.<workflow>` in the grammar of the tables above it. The seeded
   `[effort.profiles.fable]` runs every role and stage at `medium` on any Claude Fable version.
2. Adding a profile is adding one such table. No code changes, and `check_roles.py` grades it as
   R12.
3. A matched profile is read alone: the default tables' role and stage entries do not reach a
   model a profile matches.
4. A profile reaches an agent at dispatch and only there: a harness call's `efforts` from
   `stage-efforts <workflow> --model <id>`, or a direct spawn's `effort` from
   `role-efforts --model <id>`. It never reaches an agent type's `effort:` line, so it takes effect
   on the next call, with no re-render and no new session.
5. The limits. The script does not check the id a caller types. A session that cannot name its
   model leaves the flag off and gets the default tables. A spawn that is passed no level runs at
   its agent type's level, else the session's: a harness stage the workflow table gives no key
   (`tools/workflows/README.md:807-808`), and a direct spawn from a session whose `Agent` tool
   offers no `effort` parameter. The `agent` line prints the effort and the model each agent ran
   at (`tools/roles/README.md:108-109`).

`help/roles.md` carries facts 1, 2 and 4 in short form and links nothing new. It spells both calls
in spans opening `handoff.py`, as the page spells `handoff.py agents` today, so the docs leg reads
no command it holds no row for. Its fenced `render` example at `:35-37` does not move, and its
five `usage:` anchors stay on the lines that hold them.

### The observation

Run from the worktree root. It prints one line per carrier, and §6 reads the fields.

```bash
for f in tools/roles/SKILL.template.md .claude/skills/build/SKILL.md \
         tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md \
         tools/roles/README.md help/roles.md tools/workflows/README.md; do
  printf '%s calls=%s bare=%s rule=%s role=%s\n' "$f" \
    "$(grep -c 'stage-efforts' "$f")" \
    "$(grep 'stage-efforts' "$f" | grep -vc -e '--model')" \
    "$(grep -c '`Agent` call.*`effort`' "$f")" \
    "$(grep -c 'role-efforts.*--model' "$f")"
done
```

At `fc2695a2` it prints, PINNED 2026-11-10: `calls=4 bare=4 rule=0 role=0` for the template and
for its render, `calls=1 bare=1 rule=0 role=0` for the verbs guide, its copy and the workflows
README, `calls=3 bare=3 rule=0 role=0` for the roles README, and `calls=0 bare=0 rule=0 role=0`
for the help page. So every criterion that reads it is red today.

What it reads is lines. A call wrapped across two lines counts as bare, which is why S1 to S6 keep
each call on one line. It proves a carrier spells the flag and the rule, never that a session
follows them.

Three bug classes `python tools/memory-tree/gotchas.py --for-paths` selects for these paths shaped
this section. Each criterion carries a floor on `calls`, so a carrier whose calls were deleted does
not pass by finding nothing (`memory/gotchas/fixture-passes-by-finding-nothing.md`). The rule is
stated on the direct route as well as the two harness routes
(`memory/gotchas/invariant-held-on-one-admission-path.md`). The limits live in one document and
the rest point at it (`memory/gotchas/two-answers-to-one-question.md`).

### Inventory

This unit mints no identifier. It spells `--model` and `role-efforts`, which
`TOOL-aProfiledEffort-2` mints, and `[effort.profiles.<name>]`, which `TOOL-aProfiledEffort-1`
mints.

### Rollout

1. Confirm both earlier units are built: AC7's two commands answer before any edit.
2. Edit the five source carriers of S1, S2 and S4 to S7.
3. Run the two adopters of S3 and S4. Neither adopter script is edited, so the pass declares the
   seven paths below and no generator.
4. Verify in the pass with AC1 to AC7. The pass runs no gate leg and no suite.
5. A carrier takes effect the next time a session reads it. The Skill is read when `/build` is
   invoked, and whether a running session lists a changed Skill is unverified on this CLI
   (`tools/roles/README.md:335-337`).

### Files touched (estimate)

`tools/roles/SKILL.template.md` · `.claude/skills/build/SKILL.md` ·
`tools/unattended/VERBS.template.md` · `memory/guides/UNATTENDED-VERBS.md` ·
`tools/roles/README.md` · `tools/workflows/README.md` · `help/roles.md`

### Alternatives rejected

- **A verb that reads the session's model from its transcript.** `handoff.py agents` already reads
  a transcript's last model (`tools/roles/handoff.py:666-667`). It would be a verb no unit's Scope
  names and a second channel beside the flag, which `TOOL-aProfiledEffort-2` §4 rejects.
- **Passing `effort` on a direct spawn only when a profile matches.** It makes the session decide
  whether a profile matched, which is the resolver's question. Always passing the resolver's value
  is one rule with the same result.
- **Stating the limits in every carrier.** Five copies of one paragraph drift. The Skill and the
  verbs guide are routers and carry the operative sentence alone.
- **A span-level probe in Python.** It reads a wrapped call correctly and costs a script the pass
  must carry. Keeping each call on one line makes `grep` sufficient.

## 5. Production-readiness checklist

- security: N/A — no write path, surface or grant moves. The level a spawn carries is one R12
  admitted, and the model id is typed by the session and only compared.
- perf / scale: one `role-efforts` call per direct spawn. A harness call makes the one
  `stage-efforts` call it makes today.
- error / empty / loading states: an empty `--model` exits 2 (`TOOL-aProfiledEffort-2` S4), so a
  carrier never tells a session to pass an empty id; fact 5 says to leave the flag off. An adopter
  whose seeded policy holds no profile resolves the default tables under any id.
- observability: the `agent` line prints each agent's effort and model, and each harness logs one
  `effort <key>:` line per stage with its source (`tools/workflows/unattended-build.js:572-573`).
- risks: the route is prose a session follows. A session that skips the flag or misnames its model
  runs at the default tables' level in silence, and nothing refuses it; the `agent` line is where
  it shows. A later edit that adds a call without the flag is caught by no leg. Both are the hook
  and the arm §3 leaves out.
- testing: no arm added. AC1 to AC6 read the carriers with the observation, and AC7 runs the two
  calls as the carriers spell them.
- migration: N/A for data. `govkit update` re-renders the Skill and reinstalls the verbs guide, and
  the README is engine. A session started before the update follows the old text until it re-reads.
- user docs: `help/roles.md` is S7.

## 6. Acceptance criteria

"The observation" is the block of §4. A figure written `1+` means that number or more.

- **AC1** — When the observation runs, its `tools/roles/SKILL.template.md` line reads `calls=4+`,
  `bare=0`, `rule=1+` and `role=1+`.
  Red when: one of the four calls keeps today's spelling, a call and its `--model` sit on two
  lines, or the direct-spawn bullet names no `effort`.
  figure: `calls=4` is PINNED at `fc2695a2`; the other three are DERIVED by the block.
- **AC2** — When `bash tools/roles/adopt-roles.sh --scaffold` has run, the observation's
  `.claude/skills/build/SKILL.md` line carries the four figures of the template's line, and
  `git status --short .claude/agents .claude/roles.json` prints nothing.
  Red when: the template was edited and the render was not, or the scaffold moved an agent type,
  which would mean a profile reached the render path.
- **AC3** — When `bash tools/unattended/adopt-unattended.sh` has run, the observation's
  `tools/unattended/VERBS.template.md` line reads `calls=1+`, `bare=0`, `rule=1+` and `role=1+`,
  and a `diff` of `memory/guides/UNATTENDED-VERBS.md` against `tools/unattended/VERBS.template.md`,
  each read through `tr -d '\r'`, prints nothing.
  Red when: the `efforts` sentence keeps the unflagged call, the bullet states no direct-spawn
  rule, or the installed copy was left behind.
- **AC4** — When the observation runs, its `tools/roles/README.md` line reads `calls=3+`, `bare=0`,
  `rule=1+` and `role=1+`, and its `tools/workflows/README.md` line reads `calls=1+` and `bare=0`.
  Red when: a README spelling of the call lacks the flag, among them the workflows README's call
  left wrapped across `:813-814`, or the roles README never names `role-efforts`.
- **AC5** — When the observation runs, its `help/roles.md` line reads `calls=1+`, `bare=0`,
  `rule=1+` and `role=1+`, and
  `grep -nE "(python|bash) [^ ]*handoff\.py (stage-efforts|role-efforts)" help/roles.md` prints
  nothing.
  Red when: the page never spells the harness call or the direct-spawn rule, or it spells either
  verb as a command the docs leg grades and holds no row for.
  figure: `calls=0` at `fc2695a2`, PINNED, so the floor of one is what makes this non-vacuous.
- **AC6** — When `grep -c "effort\.profiles" tools/roles/README.md help/roles.md` and
  `grep -c "fable" tools/roles/README.md help/roles.md` run, each prints a count of one or more for
  each file, and `grep -c "^\[effort\.profiles\.fable\]" tools/roles/house/policy.toml` prints `1`.
  Red when: a document describes profiles under a table name the policy file does not hold, or
  leaves the seeded profile out. It reads tokens, never whether the account around them is right.
  fixture: the policy file as `TOOL-aProfiledEffort-1` built it.
  figure: all four document counts are `0` at `fc2695a2`, PINNED 2026-11-10.
- **AC7** — When `python tools/roles/handoff.py stage-efforts build --model claude-fable-5-2` runs
  it prints `{"builder":"medium"}`, and
  `python tools/roles/handoff.py role-efforts --model claude-fable-5-2` prints one line carrying
  `"gov-builder":"medium"`.
  Red when: a carrier spells a verb or a flag the built script refuses, so the call as written
  exits 2, or the id this session states matches no profile.
  fixture: both earlier units built. `claude-fable-5-2` is this run's session id, PINNED 2026-11-10.

## 7. Gates

`roles render wiring` · `roles adopter self-test` · `roles catalogue` · `check-wiring self-test` · `unattended kit gate` · `docs` · `install-prefix (shipped surface)` · `tier2-review self-test` · `unattended-build self-test` · `verifier fan-out self-test` · `review-join self-test` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

This unit adds no gate arm, so it carries no `New arm:` line. The main loop runs these legs once,
at the close, with the full bar; no pass runs one. `roles render wiring` holds the Skill against
its template and `unattended kit gate` holds the verbs guide against its copy. The four harness
legs and the two recall legs are owed by the guards the workflows README and the installed copy
trip, and `check-wiring self-test` and `lexicon naming predicates` by the rendered Skill's.

What no leg checks: that a carrier's call names the flag, that a session follows the carrier, and
that the id a session names is its model. AC1 to AC5 observe the first once, and nothing
re-observes it.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-10 · initial draft, from the brief's items 6 and 7 and acceptance 7, the seven
  carriers read at `fc2695a2`, and the two sibling specs at rev-1.
- rev-2 · 2026-11-10 · AC3 · the second clause's one backticked `diff` command is respelled so each
  path stands in backticks of its own, per the record
  `2026-11-10-prompt-TOOL-aProfiledEffort-3-token-fix-brief`. The spec token check read
  `memory/guides/UNATTENDED-VERBS.md)` and `tools/unattended/VERBS.template.md)`, each with its
  closing parenthesis, as two paths git does not track. What AC3 observes is unchanged.

## 10. Reuse audit

The seam is the pair of sentences that already tell a dispatcher to pass `efforts`:
`tools/roles/SKILL.template.md:27-28` and `tools/unattended/VERBS.template.md:793-795`, with the
direct-spawn bullet at `tools/roles/SKILL.template.md:23-26`. This unit extends those sentences and
adds no carrier, no verb and no code. `python tools/codebase-map/reuse_lookup.py "a dispatch
carrier tells the session which reasoning effort to pass on a harness call or a direct role spawn"`
returned `resolve_effort` and `resolve_stage_efforts` in `tools/roles/roles_lib.py`, the functions
the two calls resolve through, and no document, since the map ranks symbols. The carriers were
found by `git grep -l "stage-efforts"`, which names eleven files outside the records and the map,
PINNED at `fc2695a2`: the script itself, which is the second unit's; the four source carriers that
spell the call today, with the two installed copies; and the two harness templates with their two
renders, which §3 leaves out. The help page spells no call today.

Recall returned `TOOL-dBoundRoles-21`, which is DEFERRED and later re-points the policy's readers,
`TOOL-aOrientedCast-10`, which wrote the `efforts` sentences, and this build's brief. No record
ties a level to a model.

Where the records and the source disagreed. `TOOL-aOrientedCast-28` §1 says a direct spawn cannot
set its effort, and `TOOL-aOrientedCast-10` §4 says an `Agent` call takes its level from the agent
definition alone. The 2.1.321 binary holds an `effort` parameter on the `Agent` tool, and so does
the 2.1.292 binary on this node's PATH. The source was taken over the records, and the brief's
"a direct spawn's effort argument" stands. The brief also gives the direct route no verb name;
`TOOL-aProfiledEffort-2` names it `role-efforts`, and this spec follows that spec. The asks probe of
M5 was not run, because this stage may not run the build-index generator.

Recall terms used: effort policy stage-efforts efforts harness-args direct spawn Skill template verbs guide model inherit handoff render dispatch

The question passed with them: "How does a session pass the model in use and a per-model effort
level when it dispatches a harness call or spawns a role agent directly?"
