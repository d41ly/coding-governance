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
no verdict as **unverified**, never as refuted. `tools/workflows/tier2-review.js` does both.

## Enforcement — and where it does NOT reach

The rule is mechanical, in two places, with ONE implementation:

- `tools/hooks/agent-cap.js` — a `PreToolUse` hook on the `Workflow` tool call. It sees the inline
  `script` string and (when given one) reads `scriptPath` off disk. **This is the primary point**,
  because the ad-hoc review script written in a session is never a file, so no file-scoped gate can
  see it. Measured: of the `Workflow` calls in the session that motivated this document, every one
  passed `script` and none passed `scriptPath`.
- `tools/workflows/check-verifier-fanout.sh` — a merge-bar leg over the committed harnesses. It does
  not re-implement the rule; it feeds each script to the hook. One predicate, two entry points.

**What neither reaches:** a `Workflow({name:'…'})` run of a saved workflow supplies no source to the
hook. Those workflows live in `tools/workflows/` and the merge-bar leg covers them there. Nothing
counts agents at runtime — a workflow script runs in a sidechain with no hooks and no filesystem.

### The predicate

An `agent(` call reached through an iteration construct is allowed only when its receiver is:

- an identifier assigned exactly once on a line carrying `// gov:fixed-verifiers`, where that line
  spells `chunk(<x>, Math.ceil(<x>.length / <K>))` or `splitInto(<x>, <K>)` and `<K>` is an integer
  literal ≤ 5 or an identifier bound in the file to one; or
- an identifier assigned exactly once from an array LITERAL with ≤ 6 elements — the finder-lens case,
  where the agent count is visible in the source.

Everything else is denied: a `for` / `while` / `forEach` body containing `agent(`, a `.map` /
`.flatMap` / `Array.from` over any other receiver, and a marked line whose second argument is an
expression, a `.length`, a parameter, or a literal above 5.

The marker is a claim; the gate checks the claim's SHAPE. `chunk(all, 1) // gov:fixed-verifiers`
reds, and so does `splitInto(all, all.length)` — blessing a helper by NAME would bless `chunk`
wearing a different name.

## Concurrency — ≤5 agents at once, always

Route ALL fan-out through `boundedParallel(thunks, 5)` / `boundedPipeline(items, 5, …stages)`. The
same hook DENIES a script calling raw `parallel(` / `pipeline(` outside a line marked
`gov:bounded-fanout`; scripts cannot `import`, so inline the helper.

Inherited with its reason: a ~40-agent burst tripped the server rate limiter twice, ~3 M tokens
wasted. That is a property of the shared service, not of the tree that measured it, so the number
travels. It moved 6 → 5 here on that basis.

The hook does NOT parse the helper's numeric argument — its own header says so, and its self-test
passes a helper call as an ALLOW case regardless of the number. The constant shapes the remediation
text; the argument check belongs to the marker rule above, which reads the argument it is handed.

## The Tier-2 pattern

Dimension finders (security / correctness / data-integrity / dead-code / integration-seams) emit
`file:line` findings **scoped to an immutable base SHA**, then skeptics try to REFUTE each before it
is recorded. Feed the finders the security model, the open backlog and what is by-design, so they
hunt NEW issues instead of re-reporting known ones.

Default configuration: **3–6 primed finder lenses → ≤5 batched default-refute skeptics → one
synthesis pass**; three phases, find → verify → synthesize. The ready-made harness is
`tools/workflows/tier2-review.js` (`Workflow` with `{name:'tier2-review'}` or `{scriptPath}`); it
takes a structured `args` object and REFUSES a prose string, because defaulting the review root to
the process cwd twice made it audit a repository nobody had briefed it on.

- **Precision — confirmed / (confirmed + refuted) — is the #1 token lever.** Below 0.5, tighten the
  scope before adding agents. Measured on the review that produced this document: 18 / 20.
- **Match intensity to target richness.** Heavy multi-lens review earns its tokens on fresh, complex
  write paths; over already-hardened code it manufactures defence-in-depth noise. Review light, or
  skip.
- **Scale a large fresh surface by adding LENSES, not skeptics.** Coverage is what more agents buy;
  precision saturates.
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
