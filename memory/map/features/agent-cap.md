# agent-cap — the hooks kit: two PreToolUse guards, each one predicate over two modalities

```toml
feature = "agent-cap"
title = "PreToolUse guards — fan-out bounded across Workflow+Agent, scratch bounded across Bash+PowerShell"
status = "shipped"
streams = ["tooling"]
decisions = []

[claims]
gate-legs = [
  "agent-cap self-test",
  "scratch-guard self-test",
  "verifier fan-out",
  "verifier fan-out self-test",
  "review-protocol parity (kit vs dogfood)",
  "agent-cap restatement",
  "agent-cap restatement self-test",
]
kits = ["hooks"]
git-hooks = []
workflow-scripts = []
skill-engines = []
rendered-skills = []
gotcha-classes = ["trailing-comma-counted-as-an-element.md"]
guides = ["REVIEW-PROTOCOL.md"]
backlog-shards = []
lexicon-verbs = []
[paths]
globs = [
  "tools/hooks/*",
  ".claude/hooks/agent-cap.js",
  ".claude/hooks/scratch-guard.js",
  "tools/check-agent-cap-restatement.sh",
  "tools/check-agent-cap-restatement.test.sh",
  "tools/agent-cap-restatement-waivers.txt",
  "tools/workflows/check-verifier-fanout.sh",
  "tools/workflows/check-verifier-fanout.test.sh",
  "tools/workflows/check-protocol-parity.test.sh",
  "tools/workflows/REVIEW-PROTOCOL.template.md",
  "memory/guides/REVIEW-PROTOCOL.md",
]
```

## Constraints & why

**The rule is the charter's, not this kit's.** `memory/guides/REVIEW-PROTOCOL.md` is BINDING and states
two bounds: a review's verify stage spawns at most a stated TOTAL, and all fan-out runs at most a
stated number at once. Both are resolved by `tools/hooks/agent-cap.js` rather than written in the
document, so neither goes stale when a repo declares its own. This feature is the machinery that makes those numbers true rather than aspirational.
The document and the predicate are one feature for that reason — a rule enforced by a predicate that
disagrees with it is worse than no predicate.

**TWO MODALITIES, because there are two ways a session spawns agents.** A `Workflow` call carries a
script, so it is read STATICALLY. A direct `Agent` call carries no script, so it is COUNTED at
runtime. The matcher is therefore the exact-string list `"Workflow|Agent"` in one group. For a whole
release the hook was wired on `Workflow` alone and the commonest modality — a session fanning out
with direct `Agent` calls — met no rule at all.

**Concurrency is not a budget.** `boundedParallel(thunks, 5)` bounds how many run at once; N findings
still spawn N agents, five at a time. The two rules are separate for that reason, and the arity one is
the one reviews actually break.

**The static half READS THE NUMBER, in all three places a bound is written** — the helper call site,
the helper's own default parameter, and the width a `gov:bounded-fanout` line claims. Until kit 1.2 it
read none of them: `CAP` reached the remediation text and decided nothing, so two shipped harnesses
bound their own caps from an `<expr> || 5` fallback — a constant to the guard, a knob to the runtime —
and a caller could raise the verifier count past a BINDING cap with every gate green. That binder form
no longer resolves as a bound, for every consumer.

**Both markers are CLAIMS whose shape is checked, never exemptions.** `gov:fixed-verifiers` was always
shape-checked; `gov:bounded-fanout` used to return early and exempt its line outright, so a line
slicing fifty wide passed unread. Asymmetry between two markers doing the same job is how one of them
becomes a password.

**The cap is a FILE CONSTANT and a set `AGENT_CAP` is refused, not ignored.** An environment-settable
ceiling is the defeatable class this guard exists to remove, and it leaves no diff behind. The header
advertised that override for two releases after it stopped deciding anything, which is exactly how a
silently-ignored knob survives.

**The runtime half claims a NUMBERED SLOT with `O_EXCL`; it does not count.** Read-then-decide loses
updates — measured, a four-call burst overlapped its hook processes and two of four read the same
count. Create-a-token-then-count does not fix it either: six concurrent processes each observe a
count between their own ordinal and six, so several deny where exactly one must. Only the atomic
create decides. The budget is keyed per `session_id` + `prompt_id` under the git common dir, so a new
user prompt resets it with no cleanup step, and it is idempotent per `tool_use_id` so a re-invoked
hook cannot spend the turn's budget on one spawn.

**Fail closed on the static half; the runtime half splits deliberately.** A K the file cannot resolve
denies — the burden is on the fan-out. A spawn whose token cannot be CREATED denies. But a session
whose token directory cannot be RESOLVED at all fails OPEN and silently, because a hook that denies
every spawn on a filesystem hiccup is worse than the burst it prevents.

**The home holds TWO guards now, and they share only their shape.** `agent-cap.js` bounds review
fan-out and reads a Workflow script statically; `scratch-guard.js` bounds where agent scratch may be
written and reads a shell command string. Both deny by stderr plus exit 2, both fail OPEN on stdin
they cannot parse, and both are matched on a `|`-joined pair of exact tool names because a guard
wired to one modality leaves the same act available through the other — the lesson `agent-cap`
learned when `Workflow` alone left direct `Agent` spawns unguarded. The kit entry is still named
`agent-cap` and versions the whole home: `version_from` is entry-level and single-valued, so a
second constant would be invisible to govkit rather than gated by it.

## Shared seams

`topLevelArgs` in `tools/hooks/agent-cap.js` is the ONE splitter: it splits on top-level commas and
drops a trailing empty segment. Both the call-site argument walk and the array-literal element counter
call it, which is what keeps "what is an element" a single answer. It exists because the two of them
disagreed — see the `trailing-comma-counted-as-an-element` class, whose worst instance was the
element counter's off-by-one being normalised into `MAX_LENSES = 6`.

`boundedK` is the one resolver for every bound the file reads — the marker's K, the call-site
argument and the default parameter. Adding a consumer means adding a call site, never a second
resolver.

`tools/workflows/check-verifier-fanout.sh` DELEGATES to the hook rather than re-implementing it: it
builds a payload and feeds each committed harness through `tools/hooks/agent-cap.js`. One predicate,
two entry points. A bash re-implementation of a node predicate would not disagree loudly — it would
drift the day either side is tightened.

`tools/settings-merge.py` owns the wiring fragment (event, matcher, marker, hook path) and
`tools/check-wiring.sh` joins on it, asserting the matcher VALUE rather than merely that the file
mentions `agent-cap.js`.

`tools/workflows/check-protocol-parity.test.sh` keeps the shipped
`tools/workflows/REVIEW-PROTOCOL.template.md` equal to the live `memory/guides/REVIEW-PROTOCOL.md`
modulo the install prefix, and asserts the cap's NUMBER so parity cannot hold over a document that
stopped stating the rule.

## Gaps

- **Agents spawned INSIDE a workflow sidechain are uncounted, and always will be.** That script runs
  with no hooks, so no process observes those spawns. Declared here and in the protocol rather than
  implied away; it is the reason the `Workflow` half is static.
- **A `Workflow({name:'…'})` run supplies no source to the hook.** Covered second-hand by the
  merge-bar leg over `tools/workflows/`, which is why that leg exists at all.
- **The runtime count does not distinguish a verifier from any other agent.** Keying on "is this a
  verify agent" needs a session-to-build binding no payload field provides. Accepted because the
  concurrency rule binds every fan-out to the same number anyway; the residual is a wide fan-out that
  is legitimately not a review.
- **The enclosing-opener walk is defeated by two nested wrappers or 59 lines of distance** between the
  `.map` and the `agent(` call. It needs a statement-level walk rather than an opener count, and the
  58/59 boundary is unfixtured. Tracked as `TOOL-aNumeralWarden-2`.
- **The static scan cannot size a dynamically-built array**, by construction. It enforces "use the
  helper" instead, which kills the `parallel(items.map(...))` shape that causes the bursts.
- **Block comments naming a primitive still trip rule 1.** Line comments and quoted strings are
  stripped before the scan; block comments are not. Benign and fail-closed, so it stays.

## Reuse affordance

seam: agent-cap.topLevelArgs — reuse whenever source text must be split into positional items (call
arguments, array elements, parameter lists) and the count matters; extend by calling it, never by
re-deriving `1 + count(commas)`, which reads a trailing comma as an item.
seam: agent-cap.boundedK — reuse to resolve a source token to an integer bound that is either a
literal or a file-bound constant never reassigned; extend by adding a CALL SITE, never a second
resolver, and note that it deliberately refuses an `<expr> || <int>` fallback as a bound.
seam: check-verifier-fanout.delegation — reuse the shape whenever a merge-bar gate and a live hook
must apply ONE rule: the gate builds the hook's payload and runs the hook, so there is never a second
implementation to drift.
