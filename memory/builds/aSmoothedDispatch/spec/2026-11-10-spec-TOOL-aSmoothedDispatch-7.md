# TOOL-aSmoothedDispatch-7 — the `gov-spec-writer` house overlay has the writer run the spec-token checker's one-spec mode over each spec before it returns

**Status:** CLOSED · rev-1 · 2026-11-10 · node a · Tier-2 · base ae6735c1 · streams tooling · order 7 · advances TOOL-aDeferredBar-6 TOOL-dFairHearing-54

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-10-prompt-TOOL-aSmoothedDispatch-6-scope.md](../prompts/2026-11-10-prompt-TOOL-aSmoothedDispatch-6-scope.md) | research | TOOL-aSmoothedDispatch-6 |

<!-- /gen:spec-records -->

## 1. Goal

Unit TOOL-aSmoothedDispatch-5 gives the spec-token checker a `--spec <path>` mode, and the hook already
admits a spec writer running it. No writer is told to, so token misses still surface at `--dispatch` or
at the bar. This unit adds that instruction to the `gov-spec-writer` house overlay and re-renders the
agent type, which completes row 1 of the owner's go together with units 4 and 5.

## 2. Scope (IN)

- **S1** — `tools/roles/house/gov-spec-writer.md`, empty today, carries the text in §4 "The overlay
  text". It states six things. The rule holds where this repository holds the checker. The command
  is the checker with `--spec` and the spec's path. That run is a probe of one spec, while the run
  with no `--spec` is a gate leg that stays refused to the writer. On exit 1 the writer fixes each
  HIT row its own spec text can fix and runs it again. A hit the writer cannot fix goes in its
  return with its row. On exit 2 the writer names the refusal in its return. Observed by AC1 and AC5.
- **S2** — the overlay spells the checker's path only as `<prefix>/check-spec-tokens.py`. It carries
  no `# ` or `## ` line, no double-brace render token and no protocol file name. Observed by AC2.
- **S3** — `.claude/agents/gov-spec-writer.md` is re-rendered by
  `python tools/roles/render_agents.py --write`. It carries the overlay under `## House rules`, after
  the base body and before `## Charter`. No other agent type and no role index byte moves. Observed
  by AC3.
- **S4** — the role's gate grant does not move. `.claude/roles.json` still lists only
  `memory hygiene` and `lexicon naming predicates` for `gov-spec-writer`. The hook admits the command
  S1 names and refuses the bare leg. Observed by AC4.

## 3. Non-goals (OUT)

- No edit to the base role file `tools/roles/agents/gov-spec-writer.agent.md`. Line 36 still says the
  writer may run only the hygiene gate and the lexicon. The base is kit engine and is overwritten on
  every adopter's update (`tools/roles/kit.toml:27-29`), and the README says a project's rule for a
  role goes in its overlay (`tools/roles/README.md:17-22`). The overlay S1 writes says why the scoped
  run is not one of those gates.
- No change to `tools/roles/house/policy.toml` or the role index. Allowlisting the leg would admit
  the whole-tree run, which the brief of unit 5 keeps refused.
- No change to `tools/workflows/unattended-build.js` or its template. Its `specWriter` and `disposal`
  stages spawn the `gov-spec-writer` type (`tools/roles/workflows.toml:37`), so the overlay reaches
  both. TOOL-aDeferredBar-6 named that harness prompt as the home. This unit advances the ask, and
  whether it then closes is the owner's triage.
- No other role's overlay, and no instruction about heredoc quoting, sleep polling or `/tmp`. These
  are the brief's non-goals.
- No change to the checker or to `tools/hooks/scratch-guard.js`. Unit 5 changes the checker and
  pins the hook's verdicts in its suite.
- No check that a writer actually ran the command. The hook sees commands, not returns.
- No hand edit to `KIT_ROLES_VERSION`. The lander's `mint` moves it.
- No `help/` page. `help/roles.md` documents how an overlay is edited, not what one says.

### Edges

- **consumes-from** `TOOL-aSmoothedDispatch-5` — the checker's `--spec <path>` mode. Without it the
  command S1 names is not a one-spec run. At `ae6735c1` the checker reads no argument but `--list` and
  `--legs-for`, so the writer pays a whole-tree run and reads other specs' hits as its own.

## 4. Design

### What the tree does today, verified at `ae6735c1`

| Fact | Where |
|---|---|
| The overlay is empty, so the rendered type carries no `## House rules`. | `tools/roles/house/gov-spec-writer.md` (0 bytes), `.claude/agents/gov-spec-writer.md:50` |
| A non-empty overlay is appended under `## House rules`. | `tools/roles/roles_lib.py:604-617` |
| The agent file is the role render, then `## Charter`. | `tools/roles/render_agents.py:144-155` |
| R10 refuses an overlay with a heading line, a token other than the memory root, or a protocol file name. | `tools/roles/check_roles.py:351-363` |
| The overlays are seeds: an adopter receives each once. | `tools/roles/kit.toml:31-40` |
| A moved seed is reported to an updating adopter and never written. | `tools/govkit/govkit.py:8602` |
| The checker ships to no adopter. | `tools/govkit/registry.toml:226-233` |
| The install-prefix ban counts gov's prefix before a loose file name in every tracked file under the tool root, and drains `<prefix>/`. | `tools/check-install-prefix.sh:35`, `:50`, `:56` |
| The role-gate arm refuses a G1 leg only on a word-for-word argv match. | `tools/hooks/scratch-guard.js:1373-1379` |
| The role index grants `gov-spec-writer` two legs. | `.claude/roles.json:61-69`, from `tools/roles/house/policy.toml:27` |
| A HIT prints as one `spec-tokens: HIT` row naming its kind, file and token. | `tools/check-spec-tokens.py:1881` |

Probe, run 2026-11-10 against this worktree: a Bash payload with `agent_type` set to
`gov-spec-writer` was piped to `node tools/hooks/scratch-guard.js`, with `CLAUDE_PROJECT_DIR` unset.
The checker with `--spec` and a spec path exited 0 with an empty stderr. The bare checker exited 2,
naming row `G1 leg` and the leg `spec tokens (a spec's own names resolve)`.

### The overlay text (S1, S2)

The overlay holds this text, wrapped as the file's author likes:

```
Before you return, check each spec you wrote or revised with the spec-token checker's one-spec mode,
where this repository holds `<prefix>/check-spec-tokens.py`, `<prefix>` being its tool root:
`python <prefix>/check-spec-tokens.py --spec <the spec's path>`. That run grades your one spec and is
not a gate leg. The checker run with no `--spec` is the gate leg, and it stays refused to you.
Exit 1 prints one `spec-tokens: HIT` row per miss: fix each one your spec's own text can fix, then
run the check again. A hit your spec's text cannot fix goes in your return, with its row.
Exit 2 means the checker refused the path: name the refusal in your return.
```

Why the condition and the `<prefix>` spelling. The overlay is a seed, so a new adopter receives these
bytes, and the checker is gov's own and ships nowhere. The condition makes the text inert in a tree
without the checker. A literal `tools/` path would also red the install-prefix ban, whose rule 2
counts gov's prefix before a loose file name in every tracked file under the tool root.

### The render (S3, S4)

`python tools/roles/render_agents.py --write` re-renders every agent type and the role index.
Only `.claude/agents/gov-spec-writer.md` changes, because no other overlay moves and the index reads
front matter and the policy, never an overlay. The probe payload for AC4 is:

```
{"tool_name":"Bash","tool_input":{"command":"python tools/check-spec-tokens.py --spec <spec path>"},
 "cwd":"<repo root>","agent_type":"gov-spec-writer"}
```

### Files touched (estimate)

`tools/roles/house/gov-spec-writer.md` · `.claude/agents/gov-spec-writer.md`

### Rollout

The overlay is a seed, a role in `EPOCH_ROLES` (`tools/govkit/govkit.py:13719`), so the roles
kit's shipped bytes move and `kit epoch` wants its version moved. The lander's `mint` does that,
never a hand edit. A new adopter receives the text inert. An updating adopter gets a reseed report
and no write. A session started before the render spawns the old type
(`tools/roles/render_agents.py:25-27`), so the instruction reaches writers from the next session on.
Unit 5 builds first. If this unit landed alone, the named command would run the whole tree. The two
write sets are disjoint.

### Alternatives rejected

- **The base role file.** It is kit engine, so every adopter's update would rewrite it with a rule
  naming a tool they do not hold. The README routes a project's rule to the overlay.
- **The SPEC stage prompt of `tools/workflows/unattended-build.js`.** That reaches only
  harness-spawned writers and not a writer the main session hands off with `handoff.py render`.
  Both routes spawn the same type, so the role is the one home.
- **An unconditional instruction spelled `tools/check-spec-tokens.py`.** The install-prefix ban
  refuses the literal, and an adopter would be told to run a tool it lacks.

## 5. Production-readiness checklist

- security — no write path and no widened grant. The instruction runs a read-only checker the hook
  already admits, and the role index is unchanged.
- perf / scale — the writer runs one spec's joins instead of paying a `--dispatch` refusal or a bar
  round per miss.
- error / empty / loading states — exit 2 and unfixable hits are named in the writer's return, never
  swallowed.
- observability — the writer's return carries every hit it could not fix, with its row.
- risks — a writer may read a scoped green as a whole-tree green. The overlay names the whole-tree
  run as the gate leg, and the bar still grades the tree. A second risk is landing before unit 5,
  which the order and the edge prevent.
- testing — the probes in §6. The unit adds no arm, because the render's byte compare already reds
  a stale agent type.
- migration — none. An adopter's existing overlay is never rewritten.
- user docs — N/A: `help/roles.md` documents editing an overlay, and this changes one overlay's text.

## 6. Acceptance criteria

- **AC1** — `grep -n -F -- "--spec" tools/roles/house/gov-spec-writer.md` prints the command line,
  and the file states each of S1's six points.
  Red when: a point is missing, or the command omits `--spec`, which makes it the gate leg the hook
  refuses.
- **AC2** — `grep -n -E "tools/|^#|[{][{]|BUILD-METHOD|TEMPLATE-SPEC|HYGIENE[.]md|REVIEW-PROTOCOL|UNATTENDED-PROTOCOL" tools/roles/house/gov-spec-writer.md`
  prints nothing.
  Red when: the overlay spells `tools/check-spec-tokens.py`, which the install-prefix ban counts, or
  carries a heading line or protocol file name that R10 refuses.
- **AC3** — After `python tools/roles/render_agents.py --write`, the same script's `--check` exits 0.
  `grep -n -E "^## (House rules|Charter)$" .claude/agents/gov-spec-writer.md` prints `## House rules`
  above `## Charter`, and the `--spec` command line sits between them. `git status --porcelain -- .claude`
  lists `.claude/agents/gov-spec-writer.md` and nothing else.
  Red when: the overlay is edited without `--write`, so `--check` names the agent type `drift`.
- **AC4** — `.claude/roles.json` lists `memory hygiene` and `lexicon naming predicates` as the only
  gates of `gov-spec-writer`. The §4 payload, piped to `node tools/hooks/scratch-guard.js` with
  `CLAUDE_PROJECT_DIR` unset and the spec path
  `memory/builds/aSmoothedDispatch/spec/2026-11-10-spec-TOOL-aSmoothedDispatch-7.md`, exits 0 with an
  empty stderr. The same payload with no `--spec` and no path exits 2 naming `G1 leg`.
  Red when: the leg is allowlisted in `tools/roles/house/policy.toml`, so the bare run is admitted.
- **AC5** — With unit 5 built,
  `python tools/check-spec-tokens.py --spec memory/builds/aSmoothedDispatch/spec/2026-11-10-spec-TOOL-aSmoothedDispatch-7.md`
  prints a `spec-tokens: scope ·` line naming that path, and no `REFUSING` line.
  Red when: the flag the overlay spells is not the one unit 5's `main` reads, so the run prints no
  scope line.
  fixture: unit TOOL-aSmoothedDispatch-5 built. At `ae6735c1` the checker prints no scope line.

## 7. Gates

`roles catalogue` · `roles render wiring` · `roles render selftest` · `roles adopter self-test` · `check-wiring self-test` · `lexicon naming predicates` · `install-prefix (shipped surface)` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

This unit adds no arm. The `roles render wiring` leg already byte-compares the rendered agent type
against a fresh render, and R10 already grades the overlay's shape. The leg line names every leg
whose guard a path in Files touched trips, except those the checker counts as broad. A builder runs
only the lexicon, so the main loop runs every other leg at the close.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-10 · initial draft from the brief `2026-11-10-prompt-TOOL-aSmoothedDispatch-6-scope`,
  item 2, grounded at `ae6735c1`. The install-prefix ban and the seed role shaped the overlay's
  conditional wording and its `<prefix>` spelling.

## 10. Reuse audit

The seam is the house overlay that `render_role` appends (`tools/roles/roles_lib.py:604-617`), the
route `tools/roles/README.md:17-22` names for a project's rule. No code is added. The probe
`reuse_lookup.py "tell a role agent a project rule through its prompt"` ranked `render_role` and
`load_roles` in `tools/roles/roles_lib.py` among its candidates, and no other seam fits a prompt line.
Recall ranked TOOL-dBoundRoles-19 first, which would move the house files into overlay units. It is
DEFERRED, so the house file is the live home, and a later build carries this text with the rest.
Records and code disagree in two places. TOOL-dBoundRoles-19 cites `render_role` at lines 579-592,
which is stale, since it now sits at 604. TOOL-aDeferredBar-6 names the harness prompt as the home,
but the harness spawns this role's type, so the overlay reaches it.

Recall terms used: `python tools/memory-recall/query.py "how does this repository add a project rule to one role agent's prompt" --terms "house overlay role prompt gov-spec-writer render_agents House rules seed spec-token checker writer"`
