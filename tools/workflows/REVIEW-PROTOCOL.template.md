# Review + multi-agent Workflow protocol (BINDING — part of the charter)

Read this before ANY multi-agent review or `Workflow` run. Ported from the upstream inCMS charter
(`ARCH-bWhittledTome-1`, 2026-07-15; hard cap added by the owner 2026-07-29) and re-measured here —
every number below is either measured on THIS tree or marked as inherited with the reason it travels.

## The hard cap — ≤5 verify-stage agents TOTAL

**A review's verify stage spawns at most 5 agents, whatever the finding count.** The batch size grows
with the finding count; the agent count never does.

This is not the concurrency cap wearing a different hat. `boundedParallel(thunks, 5)` bounds how many
run AT ONCE; N findings still spawn N agents, five at a time. **Concurrency is not a budget.**

Measured here, on one review of one spec in one session:

| Shape | Agents | Subagent tokens |
|---|---|---|
| one skeptic per finding (banned) | 47 | 3.65 M |
| ≤5 batched skeptics (required) | 9 | 0.81 M |

Upstream's figure for the same mistake, inherited because it is the same failure at larger scale: six
consecutive reviews of one spec at 79 / 54 / 48 / 37 agents, ~36 M subagent tokens.

When batching, keep verdicts keyed by an **orchestrator-assigned integer**, and treat a finding with
no verdict as **unverified**, never as refuted. `{{TOOL_ROOT}}workflows/tier2-review.js` does both.

## Enforcement — and where it does NOT reach

The rule is mechanical, and there are TWO MODALITIES to enforce it in, because there are two ways a
session spawns agents:

- `{{TOOL_ROOT}}hooks/agent-cap.js` on the **`Workflow`** tool call — the STATIC half. It sees the inline
  `script` string and (when given one) reads `scriptPath` off disk. **This is the primary point** for
  a review, because the ad-hoc review script written in a session is never a file, so no file-scoped
  gate can see it. Measured: of the `Workflow` calls in the session that motivated this document,
  every one passed `script` and none passed `scriptPath`.
- The same hook on the **`Agent`** tool call — the RUNTIME half, and the modality that was unguarded
  entirely until `agent-cap` 1.3. A direct spawn carries no script, so it is COUNTED: each spawn
  claims a numbered slot with `O_EXCL` under a `session_id` + `prompt_id`-keyed directory in the git
  common dir, and the spawn that finds every slot taken is denied. The budget resets on the next user
  prompt, so nothing has to remember to clear it. Measured before it was built: `PreToolUse` does
  fire for a direct `Agent` spawn, `tool_name` arrives as exactly `Agent`, and `session_id`,
  `prompt_id` and `tool_use_id` are all present.

  The count does **not** distinguish a verifier from any other agent, and that is deliberate: keying
  on "is this a verify agent" would need a session-to-build binding no payload field provides, while
  the concurrency rule below already binds every fan-out to the same number. The residual is a wide
  fan-out that is legitimately not a review — accepted, for that reason.

  **A slot also EXPIRES, from 1.5, and what that buys is stated exactly.** `PreToolUse` fires BEFORE
  the work and there is no matching after-event this hook is wired for, so a slot had no release path
  and the raw count was LIFETIME-PER-PROMPT, not concurrency: five agents that ran one after another,
  each finished before the next began, refused the sixth for the rest of the turn. Measured at
  agent-cap 1.4 — six sequential spawns, distinct `tool_use_id`s, the sixth denied against five
  long-idle slots. A slot idle past `SLOT_TTL_MS` (45 min, set above the longest subagent measured on
  this fleet, 34 min) is now reclaimed by the next spawn, so the budget is a rolling window rather
  than a permanent one.

  **The expiry stands in for a completion signal; it does not turn the counter into a concurrency
  meter, and the direction it fails in is chosen.** A burst — the case this rule exists for — claims
  its five slots within a second, so no realistic TTL lets one through. What the TTL does admit is
  the rarer shape: five agents genuinely running concurrently for longer than 45 minutes, then a
  sixth. The precise fix is a release keyed on `tool_use_id`, which the harness guarantees identifies
  ONE tool execution across `PreToolUse` and `PostToolUse`. It is not built, and the reason is a
  single unmeasured fact: whether the `Agent` tool fires `PostToolUse` at all. Settle it with a
  `PostToolUse[Agent]` probe plus a `PostToolUse[Bash]` CONTROL, in a FRESH session — settings are
  not hot-reloaded, which is why it could not be settled where it was found. The public hooks reference says Agent skips both tool events in favour of
  `SubagentStart`/`SubagentStop`, and `SubagentStop` carries no `tool_use_id` to correlate on — while
  the measurement in the bullet above says `PreToolUse` DOES fire for Agent, re-confirmed by watching
  a real spawn claim a slot. Both cannot be right, and wiring a release for an event that never
  arrives would ship exactly the mechanism-that-cannot-fire this repo gates.

  Why slots and not a running count: read-then-decide loses updates (measured — a four-call burst
  overlapped its hook processes and two of four read the same count), and create-a-token-then-count
  does not fix it either, since each of six concurrent processes sees between its own ordinal and
  six. Only the atomic claim of a numbered slot decides the question in the create.
- `{{TOOL_ROOT}}workflows/check-verifier-fanout.sh` — a merge-bar leg over the committed harnesses. It does
  not re-implement the static rule; it feeds each script to the hook. One predicate, two entry points.

The wiring is therefore `"matcher": "Workflow|Agent"` — a list of exact strings in ONE group, not a
regular expression. `check-wiring.sh` asserts that VALUE, because a group left at `Workflow`
alone still contains the string `agent-cap.js` and used to report the tree correctly wired.

**Where enforcement does NOT reach**, stated rather than implied away:

- A `Workflow({name:'…'})` run of a saved workflow supplies no source to the hook. Those workflows
  live in `workflows/` and the merge-bar leg covers them there.
- The agents a workflow script spawns INSIDE itself. That script runs in a sidechain with no hooks,
  so no process observes those spawns and none ever will. This is a statement about the SIDECHAIN
  specifically — not a blanket claim that runtime counting is impossible, which is what it used to
  read as. A `PreToolUse` hook on a main-loop tool call is a different case and was measured on its
  own evidence.
- A session whose token directory cannot be resolved at all — no git dir, or a payload missing
  `session_id` / `prompt_id` / `tool_use_id`. That fails OPEN and silently, because a hook that
  denies every spawn on a filesystem hiccup is worse than the burst it prevents. A token that could
  not be CREATED is a different fact and denies.

### The predicate

An `agent(` call reached through an iteration construct is allowed only when its receiver is:

- an identifier assigned exactly once on a line carrying `// gov:fixed-verifiers`, where that line
  spells `chunk(<x>, Math.ceil(<x>.length / <K>))` or `splitInto(<x>, <K>)` and `<K>` resolves; or
- an identifier assigned exactly once from an array LITERAL with ≤ 5 elements — the finder-lens case,
  where the agent count is visible in the source. A trailing comma is not an element.

Everything else is denied: a `for` / `while` / `forEach` body containing `agent(`, a `.map` /
`.flatMap` / `Array.from` over any other receiver, and a marked line whose second argument is an
expression, a `.length`, a parameter, or a literal above 5.

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
wearing a different name. `gov:bounded-fanout` is a claim on the same terms: the marked line must
slice a bare identifier by a width that is either the enclosing helper's own `cap` parameter, which
the two rules above have already bounded, or a `<K>` that resolves. It used to exempt its line
outright, so a line slicing fifty wide passed unread.

## Concurrency — ≤5 agents at once, always

Route ALL fan-out through `boundedParallel(thunks, 5)` / `boundedPipeline(items, 5, …stages)`. The
same hook DENIES a script calling raw `parallel(` / `pipeline(` outside a line marked
`gov:bounded-fanout`; scripts cannot `import`, so inline the helper.

Inherited with its reason: a ~40-agent burst tripped the server rate limiter twice, ~3 M tokens
wasted. That is a property of the shared service, not of the tree that measured it, so the number
travels. It moved 6 → 5 here on that basis.

**The hook reads the number, in all three places a bound is written** (`agent-cap` 1.2). It resolves
the cap argument at each `boundedParallel(` / `boundedPipeline(` CALL SITE, the helper's own DEFAULT
PARAMETER when a call passes none, and the slice width a `gov:bounded-fanout` line claims — joining
lines forward until the parens balance, because every shipped call site spans lines. A K it cannot
resolve to an integer ≤ 5 is denied; the burden is on the fan-out.

The 5 is a FILE CONSTANT. There is no environment override, and a set `AGENT_CAP` is refused with a
message rather than ignored — a ceiling that can be raised from the environment leaves no diff behind,
which is the defeatable class this rule exists to stay out of.

## The Tier-2 pattern

Dimension finders (security / correctness / data-integrity / dead-code / integration-seams) emit
`file:line` findings **scoped to an immutable base SHA**, then skeptics try to REFUTE each before it
is recorded. Feed the finders the security model, the open backlog and what is by-design, so they
hunt NEW issues instead of re-reporting known ones.

Default configuration: **3–6 primed finder lenses → ≤5 batched default-refute skeptics → one
synthesis pass**; three phases, find → verify → synthesize. The ready-made harness is
`{{TOOL_ROOT}}workflows/tier2-review.js` (`Workflow` with `{name:'tier2-review'}` or `{scriptPath}`); it
takes a structured `args` object and REFUSES a prose string, because defaulting the review root to
the process cwd twice made it audit a repository nobody had briefed it on.

- **Precision — confirmed / (confirmed + refuted) — is the #1 token lever.** Below 0.5, tighten the
  scope before adding agents. Measured on the review that produced this document: 18 / 20.
- **Match intensity to target richness.** Heavy multi-lens review earns its tokens on fresh, complex
  write paths; over already-hardened code it manufactures defence-in-depth noise. Review light, or
  skip.
- **Scale a large fresh surface by adding LENSES, not skeptics.** Coverage is what more agents buy;
  precision saturates. The lens allowance is **5**, the same number as everything else here — it
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
- Workflow scripts run in sidechains that inherit **no hooks and no `CLAUDE.md`**. The discipline
  lives with the ORCHESTRATOR that writes the script, which is why the cap is enforced at the tool
  call and never inside the script, where no hook reaches.
