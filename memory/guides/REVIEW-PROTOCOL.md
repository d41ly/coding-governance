# Review + multi-agent Workflow protocol (BINDING — part of the charter)

Read this before ANY multi-agent review or `Workflow` run. Ported from adopter ic's charter
(`ARCH-bWhittledTome-1`, 2026-07-15; hard cap added by the owner 2026-07-29) and re-measured here —
every number below is either measured on THIS tree or marked as inherited with the reason it travels.

## The hard cap — the verify-stage total `agent-cap.js` resolves

**A review's verify stage spawns at most the total `tools/hooks/agent-cap.js` holds as
`MAX_VERIFIERS`, whatever the finding count.** The batch size grows
with the finding count; the agent count never does.

The NUMBER is a FILE CONSTANT in `tools/hooks/agent-cap.js`, and that file is what a run actually
obeys — it ships deployed verbatim, with no conf channel and no environment override. This document
restates it only where a reader has to act on it, and every restatement is a copy that can go stale:
when the two disagree, the hook is right and the sentence you are reading is the bug. An earlier
revision of this line claimed the number was "declared per repository"; that was written for a
mechanism that was specced and then parked, and it described a channel this tree does not have.

This is not the agent limit wearing a different hat. `runtime.agents-in-flight` bounds how many run
AT ONCE; N findings still spawn N agents, a limit's worth at a time. **Concurrency is not a budget.**

Measured here, on one review of one spec in one session:

| Shape | Agents | Subagent tokens |
|---|---|---|
| one skeptic per finding (banned) | 47 | 3.65 M |
| ≤5 batched skeptics (required) | 9 | 0.81 M |

Upstream's figure for the same mistake, inherited because it is the same failure at larger scale: six
consecutive reviews of one spec at 79 / 54 / 48 / 37 agents, ~36 M subagent tokens.

When batching, keep verdicts keyed by an **orchestrator-assigned integer**, and treat a finding with
no verdict as **unverified**, never as refuted. `tools/workflows/tier2-review.js` does both.

## Enforcement — and where it does NOT reach

The rule is mechanical, and there are TWO MODALITIES to enforce it in, because there are two ways a
session spawns agents:

- `tools/hooks/agent-cap.js` on the **`Workflow`** tool call — the STATIC half. It sees the inline
  `script` string and (when given one) reads `scriptPath` off disk. **This is the primary point** for
  a review, because the ad-hoc review script written in a session is never a file, so no file-scoped
  gate can see it. Measured: of the `Workflow` calls in the session that motivated this document,
  every one passed `script` and none passed `scriptPath`.
- The same hook on the **`Agent`** and **`Workflow`** calls — the SETTINGS half, its rule 7
  (TOOL-dGroundRules-10). How many agents run at once is the agent limit, `runtime.agents-in-flight`,
  and the harness enforces it through the two concurrency settings the policy kit renders from it,
  because the harness counts agents in flight and knows when each one ends, which a `PreToolUse` hook
  cannot. The hook refuses a call when the settings in force are absent or above the landed limit,
  naming the render command. It reads three layers, highest precedence first (TOOL-dGroundRules-61):
  the checkout's local settings file, the project's `.claude/settings.json`, and the file
  `GOV_SETTINGS_JSON` declares, a relative path read against the checkout root. The per-prompt slot
  ledger that counted direct spawns until TOOL-dGroundRules-10, with its 45-minute expiry, retired
  with it: it counted claims, not agents in flight, so five idle claims refused a sixth agent and five
  claims past the expiry admitted five more.
- `tools/workflows/check-verifier-fanout.sh` — a merge-bar leg over the committed harnesses. It does
  not re-implement the static rule; it feeds each script to the hook. One predicate, two entry points.

The wiring is therefore `"matcher": "Workflow|Agent"` — a list of exact strings in ONE group, not a
regular expression. `check-wiring.sh` asserts that VALUE, because a group left at `Workflow`
alone still contains the string `agent-cap.js` and used to report the tree correctly wired.

**Where enforcement does NOT reach**, stated rather than implied away:

- A `Workflow({name:'…'})` run of a saved workflow supplies no source to the hook. Those workflows
  live in `workflows/` and the merge-bar leg covers them there.
- The agents a workflow script spawns INSIDE itself. MEASURED 2026-08-15 by dispatching a probe and
  asking it to report what arrived before it read anything: a sidechain agent holds no `Agent` tool
  at all — `ToolSearch` for it returns nothing — so it cannot fan out, and the arity rule has nothing
  to bind at that depth. The capability is ABSENT rather than unpoliced, which is the stronger
  property and not the one this bullet used to claim. A `PreToolUse` hook DOES fire there, and that
  is no longer unmeasured: MEASURED 2026-09-12 on node `d`, the project-level guard on matcher
  `Bash|PowerShell` (`tools/hooks/scratch-guard.js`) DENIED a Bash command issued by an agent
  inside a `Workflow` sidechain — the matcher-on-a-tool-it-does-hold experiment this bullet asked
  for. So the spawns above are missed because the matcher covers `Workflow|Agent` and a sidechain
  holds neither, NOT because hooks stop at the sidechain boundary.
- An environment override of the two harness variables, which the harness applies and no hook can
  read, and a session started before a lowering, which keeps the settings it started with until it
  restarts.

### The predicate

An `agent(` call reached through an iteration construct is allowed only when its receiver is:

- an identifier assigned exactly once on a line carrying `// gov:fixed-verifiers`, where that line
  spells `chunk(<x>, Math.ceil(<x>.length / <K>))` or `splitInto(<x>, <K>)` and `<K>` resolves; or
- an identifier assigned exactly once on a line carrying `// gov:fixed-writers`, the same split
  shape, whose `<K>` resolves to at most `runtime.agents-in-flight` — a WRITER split, the build
  harness's spec stage, is no verify stage, so its bound is the agent limit and not `MAX_VERIFIERS`
  (TOOL-dGroundRules-18); or
- an identifier assigned exactly once from an array LITERAL with ≤ 5 elements — the finder-lens case,
  where the agent count is visible in the source. A trailing comma is not an element; or
- an identifier assigned exactly once on a line carrying `// gov:fixed-verifiers` whose right-hand
  side DERIVES from a name already proven bounded above — the marked-derivation case, and the third
  receiver. Mentioning a bounded name is not enough: EVERY top-level branch of that right-hand side
  is judged on its own text, the derivation must be ROOTED on the bounded value rather than merely
  referring to one, every top-level link of the chain after that root must be shrink-only
  (`.filter` or `.slice`) and the chain must CONSUME to a balanced close, and the whole right-hand
  side is vetoed if it can grow. A bare reassignment of the name afterwards takes the bound back.

Everything else is denied: a `forEach` body containing `agent(`, a `for` / `while` body that does
not carry a conforming `gov:sequential-agents(<K>)` marker on its header, a `.map` / `.flatMap` /
`Array.from` over any other receiver, and a marked line whose second argument is an expression, a
`.length`, a parameter, or a literal above 5. The sequential marker is the one loop affordance and
it is a CLAIM, not an exemption: the hooks kit's own `README.md` owns its grammar and the hook
checks every
clause of it, including that exactly one awaited call sits in the marked body.

**`<K>` resolves** — one definition, used by every consumer above — when it is an integer literal ≤ 5,
or an identifier bound DIRECTLY by `const <name> = <int>` and never reassigned. An `<expr> || <int>`
right-hand side does NOT resolve. It reads as a constant and behaves as a knob: an
`(args && args.<knob>) || 5` fallback let two shipped harnesses raise their own agent count from the
caller while the guard read the 5 and every gate stayed green. The form is still legal JavaScript and
still fine for constants nothing here resolves — only its use as a BOUND is refused. (The retired
spelling is paraphrased rather than quoted: this document renders into `workflows/`, which the
acceptance grep for that spelling sweeps, so quoting it would make the ban fire on the text
explaining the ban.)

The marker is a claim; the gate checks the claim's SHAPE. `chunk(all, 1) // gov:fixed-verifiers`
reds, and so does `splitInto(all, all.length)` — blessing a helper by NAME would bless `chunk`
wearing a different name. `gov:bounded-fanout` marks a helper's own slice line, and since
TOOL-dGroundRules-10 no concurrency width is resolved: the agent limit bounds that, in the harness.

## Concurrency — the at-once bound is `runtime.agents-in-flight`, always

How many agents run AT ONCE is the policy key `runtime.agents-in-flight` (TOOL-dGroundRules-10). The
policy kit renders it into the harness's own two settings in `.claude/settings.json`,
`CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` and `CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS`, with
`policy.py settings --write`, and every landing regenerates that render. The harness counts agents in
flight and enforces them: a direct spawn over the first is refused, and a Workflow agent over the
second queues. `tools/hooks/agent-cap.js` holds the settings a session starts from to the landed
limit, its rule 7, and resolves no width itself. Read the limit with `policy.py get
runtime.agents-in-flight --explain`, which names a `FANOUT_CAP` lowering in `.agent-cap.conf` too.

Route fan-out through `boundedParallel(thunks, cap)` / `boundedPipeline(items, cap, …stages)`, inlined
because scripts cannot `import`; the shipped harnesses render that width from the same key. Until the
in-flight ledger arms, the limit binds direct spawns and each Workflow run separately, so two runs in
one message may together hold twice it.

Inherited with its reason: a ~40-agent burst tripped the server rate limiter twice, ~3 M tokens
wasted. That is a property of the shared service, not of the tree that measured it, which is why the
limit carries a default in the policy catalogue and a repository moves it by a policy write, never by
editing a harness.

## Tiers and security boundaries

The tier definitions and the security checklist for a new write path or surface live in the
memory tree's spec template, `TEMPLATE-SPEC.md`, because every adoption keeps the required
memory tree and a design pass is where a new surface is first decided (PLAY-aDistilledCharter-5).

## The Tier-2 pattern

Dimension finders (security / correctness / data-integrity / dead-code / integration-seams) emit
`file:line` findings **scoped to an immutable base SHA**, then skeptics try to REFUTE each before it
is recorded. Feed the finders the security model, the open asks on the files under review — the
rows `gen_build_index.py --asks --json --path <every path the diff touches>` prints, ranked by
severity and capped, with `--limit 0` lifting the cap, or the backlog shards when its `mode` field
says `shards` — and what is by-design, so they hunt NEW issues instead of re-reporting known ones.

Default configuration: **3–6 primed finder lenses → batched default-refute skeptics within the
hook's declared bound → one
synthesis pass**; three phases, find → verify → synthesize. The ready-made harness is
`tools/workflows/tier2-review.js` (`Workflow` with `{name:'tier2-review'}` or `{scriptPath}`); it
takes a structured `args` object and REFUSES a prose string, because defaulting the review root to
the process cwd twice made it audit a repository nobody had briefed it on.

**Results are durable only on request.** By default every finder and skeptic batch spawns as the
read-only `Plan` type, which holds no Write tool, so it writes no result file and a resume reuses
nothing: a re-run dispatches every judge again (TOOL-aMendedFleet-93). A run that passes
`workerType: 'none'` spawns its judges with the charter loaded, and each Writes its result to
`<git-common-dir>/review-lenses/<key>/find-<lens>.json` or `verify-<first id>-<last id>.json`
BEFORE it returns, and all three schemas require its `path`. The key is the kind, the round, the
pinned subject and a print of the inputs, so a re-run with identical args reuses every file that
carries it and dispatches only what is missing. A run where a lens, a batch or the synthesis
returned nothing exits `deferred-platform`, naming the `pending` labels and no blocker count:
re-run it once, and hold on a second.

- **Precision — confirmed / (confirmed + refuted) — is the #1 token lever.** Below 0.5, tighten the
  scope before adding agents. Measured on the review that produced this document: 18 / 20.
- **Match intensity to target richness.** Heavy multi-lens review earns its tokens on fresh, complex
  write paths; over already-hardened code it manufactures defence-in-depth noise. Review light, or
  skip.
- **Scale a large fresh surface by adding LENSES, not skeptics.** Coverage is what more agents buy;
  precision saturates. The lens allowance is the same number as everything else here, and
  `tools/hooks/agent-cap.js` holds it as `MAX_LENSES` — it
  briefly read as 6, which was never a decision: the hook counted a trailing comma as an element, so
  every prettier-formatted 5-lens array measured 6 and the constant had been raised to fit the error.
  Ratified at 5 by the owner once the miscount was found.
- **Stop re-reviewing a spec once the judge calls the design clean.** Findings after that land in the
  prose about the design rather than in the design. Building is both cheaper and stricter — upstream
  measured a build that found four defects a seventh review had not.

## Schema discipline for `agent({schema})`

Shape the structured output so a malformed return cannot force a full regeneration — the largest
output-token waste found in a workflow-transcript audit was a 30 KB hand-emitted JSON body breaking
on one unescaped backslash and regenerating whole.

- **Never make an agent hand-serialize a large body as JSON.** Long prose — review write-ups, design
  candidates — gets `Write`n to a file, and the agent returns `{path, summary}` with FORWARD-SLASH
  paths. Unescaped backslashes are exactly what breaks the JSON.
- **Re-state the schema's required keys in the per-item prompt on every loop iteration.** An agent
  looping over N items forgets the shape between items and re-fails identically.
- **Do not set `additionalProperties: false`** unless a stray key is actually harmful. Accept-and-
  ignore beats reject-and-regenerate; on a validation failure feed back the offending key, not
  "regenerate everything".
- Workflow scripts are **plain JavaScript** — type annotations, interfaces and generics fail to parse.
- Workflow scripts run in sidechains. This document asserted they inherit **no hooks and no
  `CLAUDE.md`**; MEASURED 2026-08-15, both halves are FALSE. The probe's first message carried a
  `system-reminder` holding `CLAUDE.md` and the whole of `AGENTS.md` before it read anything, and a
  `SubagentStart` hook fired and was obeyed, arriving with its own verbatim header. No
  `SessionStart`-shaped injection was observed — recorded as not-observed rather than as absent.
  `PreToolUse` fires there too, MEASURED 2026-09-12 on node `d`: a project-level guard on
  `Bash|PowerShell` denied a Bash command issued from inside a sidechain.
  The cap is still enforced at the tool call rather than inside the script, but because the
  orchestrator is where the fan-out decision is MADE — not because nothing reaches a sidechain.
