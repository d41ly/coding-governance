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
  "hook destinations (every declared hook path ships)",
  "hook destinations self-test",
]
kits = ["hooks"]
git-hooks = []
harness-hooks = ["PreToolUse tools/hooks/agent-cap.js", "PreToolUse tools/hooks/scratch-guard.js", "SubagentStart tools/hooks/scratch-guard.js"]
workflow-scripts = []
skill-engines = []
rendered-skills = []
gotcha-classes = ["bash-c-multiline-flattens-under-msys.md", "git-rm-cached-refuses-a-diverged-index-blob.md",
  "trailing-comma-counted-as-an-element.md",
  "allowlist-narrower-than-the-root-it-guards.md",
  "a-pair-exists-and-it-is-the-wrong-one.md",
  "a-view-fix-trades-one-blindness-for-another.md",
  "settings-edit-takes-effect-mid-session.md",
  "conf-value-interpolated-into-a-regex.md",
]
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
runtime. The matcher is therefore the exact-string list `"Workflow|Agent"` in one group: wired on
`Workflow` alone, direct `Agent` calls meet no rule at all.

**Concurrency is not a budget.** `boundedParallel(thunks, 5)` bounds how many run at once; N findings
still spawn N agents, five at a time. The two rules are separate for that reason, and the arity one
is the one reviews break.

**The static half READS THE NUMBER, in all three places a bound is written** — the helper call site,
the helper's own default parameter, and the width a `gov:bounded-fanout` line claims. An
`<expr> || 5` fallback never resolves as a bound: it is a constant to the guard and a knob to the
runtime, so a caller could raise the verifier count past a BINDING cap with every gate green.

**All THREE markers are CLAIMS whose shape is checked, never exemptions.** `gov:sequential-agents`
is the only one admitting a loop; its bound resolves through the same `boundedK` as every other, and
its weight is carried by the bounded RECEIVER clause and the one-call sweep rather than by the number
an author typed. Asymmetry between markers doing the same job is how one of them becomes a password.

**The cap is a FILE CONSTANT and a set `AGENT_CAP` is refused, not ignored.** An environment-settable
ceiling is the defeatable class this guard exists to remove, and it leaves no diff behind.

**The runtime half claims a NUMBERED SLOT with `O_EXCL`; it does not count.** Read-then-decide loses
updates, as `TOOL-aNumeralWarden-1` measured. Create-a-token-then-count does not fix it: six concurrent processes each observe a count
between their own ordinal and six, so several deny where exactly one must. Only the atomic
create decides. The budget is keyed per `session_id` + `prompt_id` under the git common dir, so a new
user prompt resets it with no cleanup step, and it is idempotent per `tool_use_id` so a re-invoked
hook cannot spend the turn's budget on one spawn.

**Fail closed on the static half; the runtime half splits deliberately.** A K the file cannot resolve
denies — the burden is the fan-out's. A spawn whose token cannot be CREATED denies. But a session
whose token directory cannot be RESOLVED at all fails OPEN and silently, because a hook that denies
every spawn on a filesystem hiccup is worse than the burst it prevents.

**The home holds TWO guards, sharing only their shape.** `agent-cap.js` bounds review fan-out and
reads a Workflow script statically; `scratch-guard.js` bounds where agent scratch may be written
and reads a shell command string. Both deny by stderr plus exit 2, both fail OPEN on stdin
they cannot parse, and both are matched on a `|`-joined pair of exact tool names because a guard
wired to one modality leaves the same act available through the other. The kit entry is still named
`agent-cap` and versions the whole home: `version_from` is entry-level and single-valued, so a
second constant would be invisible to govkit rather than gated by it. Each wiring is a
`harness-hooks` claim.

**`scratch-guard.js` carries a SECOND check, and it rides the process that already spawns.**
`TOOL-aReplayedCard-1`: after the scratch verdict, `checkOriented` refuses a main-loop `git commit`
while the session's orientation card under `<git-common-dir>/orientation/` still holds the kickoff
writer's sentinel `READY — none yet`, or names another tree than the commit targets. It is inside
this file and not a third hook because a second file on the `Bash|PowerShell` matcher doubles
every shell call's spawn cost, which that unit's spec measured. The predicate has ONE
evaluation order, written above the function: shape, `agent_id`, missing fields, an unwalkable
target, an absent or replay-written card, then the sentinel-or-mismatch test, and only then the
exemption — the commit that CREATES a build README carrying `authorized-by:` with a value in the
unattended driver's `SECOND_ANCHOR_MODES`, pinned by a parity arm. An ABSENT card and a
replay-written one ALLOW, with a witness line that reaches the debug log and the self-test only:
a deny on either names a remedy an unattended landing cannot run. The drive
fold is `buildComparablePath`'s own step, applied to the `-C` target and `cwd` BEFORE the walk and
to both toplevels before the compare; there is no second normaliser.

**And a THIRD check, the write gate, on the same process** (`TOOL-aRoutedQuill-2`). The fragment's
matcher widened to `Bash|PowerShell|Edit|Write|MultiEdit|NotebookEdit`, one fragment because the
merger joins on the script's basename, and `main` sends a write tool to `checkRouted`. An edit under
`ROUTED_PATHS` (the target toplevel's `.memory-tree.conf`) refuses unless the card's `## route`
names a unit whose spec is buildable by `checkBuildable`. Unlike the two shell checks it fails
CLOSED, has no `agent_id` exemption (a subagent's payload carries the parent's `session_id`), and
refuses on an absent or replay-written card. An UNARMED conf refuses every write but the one to
itself. A target outside the session's common dir is not gated, so a scratch clone never meets its
own conf.

**And the same script on a SECOND event, `SubagentStart`** (`TOOL-aRoutedQuill-4`). A second
fragment, `scratch-guard-subagent.fragment.json` with matcher `*`, is safe where a second PreToolUse
one is not, because the merger re-matches a marker only within one event's groups. `main` sends a
`SubagentStart` payload to `renderRouteContext` before any `tool_name` test, and prints its text as
`additionalContext`: the card's route lines byte for byte, each unit's `checkBuildable` verdict, and
what the gate refuses, capped at `ROUTE_CONTEXT_CAP` characters. It states facts and never
directs, prints nothing where the gate admits everything, and never blocks.

**One rule in `agent-cap.js` is not a fan-out bound and reads the payload's ARGS, not the script**
(`TOOL-aBlindedTrial-4`, for the ruling `TOOL-aBlindedTrial-6`). A `Workflow` call whose
structured `args` carry `kind: "spec-audit"` is denied unless the build README at
`<args.repo>/<parent of args.reviewDir>/README.md` declares `spec-audit: <YYYY-MM-DD>` in its front
matter, or carries no key while `<args.repo>/.unattended.conf` declares `SPEC_AUDIT_DEFAULT` as a
date (`TOOL-aBlindedTrial-7`; last assignment wins, a non-date denies by name, the README wins).
It makes the pre-code spec audit FORBIDDEN in an attended session, not merely unowed. Three
choices are load-bearing: it keys on `tool_input.args`, never on script text (both harnesses spell
`spec-audit` in comments and would deny themselves); it sits ABOVE the script read in `main()`, so a
`name:`-only invocation is judged too; and it fails CLOSED for this kind alone — an unplaceable call
or a README it cannot read is a deny naming the field, and every throw is a deny, because a
PreToolUse hook at exit 1 is non-blocking. The root is `args.repo`, never `gitCommonDir(cwd)`, which
in a linked worktree is the primary tree's `.git`.

## Shared seams

**`readFrontMatterKey` in `tools/hooks/scratch-guard.js` is the ONE front-matter reader for both
hooks.** It returns the single-token value of a key between the opening `---` and the next `---`, or null;
`checkAuthorizedReadme` reads `authorized-by:` through it and the spec-audit rule reads
`spec-audit:`, required lazily inside the rule's try so a withdrawn sibling is a deny, not a crash.
It takes bytes, not a path: the staged-blob caller has no file to name. One reader keeps "a fenced example in the body is not front matter" one answer (F10) for both keys.

**`readConfKey` in the same file is the ONE shell-grammar conf reader.** The write gate reads
`MEMORY_ROOT`, `ROUTED_PATHS` and `SPEC_TIER1_CUTOFF` through it, and `agent-cap.js`'s
`readSpecAuditDefault` delegates to it (`TOOL-aRoutedQuill-2` S9): last assignment wins, the key is
compared as a string.

**Every declared hook path is asserted to SHIP, in both directions.** A fragment names a
destination and an adopter script writes one, and neither is any use if the file it points at
is not in the kit — a hook wired to nothing is indistinguishable from a hook that never fires,
and the settings file looks correct either way. `check-hook-destinations.sh` quantifies over
both populations, fragments AND the adopter scripts that write hook commands, because a kit
that installs its hook from a script rather than a fragment is otherwise ungraded.

`topLevelArgs` in `tools/hooks/agent-cap.js` is the ONE splitter: it splits on top-level commas and
drops a trailing empty segment. Both the call-site argument walk and the array-literal element counter
call it, which keeps "what is an element" a single answer against the
`trailing-comma-counted-as-an-element` class.

`boundedK` is the one resolver for every bound the file reads — the marker's K, the call-site
argument and the default parameter. Adding a consumer means adding a call site, never a second
resolver.

`tools/workflows/check-verifier-fanout.sh` DELEGATES to the hook rather than re-implementing it: it
builds a payload and feeds each committed harness through `tools/hooks/agent-cap.js`. One predicate,
two entry points. A bash re-implementation would not disagree loudly — it would drift the day
either side is tightened.

`tools/settings-merge.py` owns the wiring fragment (event, matcher, marker, hook path, plus the
optional interpreter and args `TOOL-aReplayedCard-2` added for the bash-scripted card verb) and
`tools/check-wiring.sh` joins on it, asserting the matcher VALUE rather than merely that the file
mentions `agent-cap.js`. The merger re-matches an entry it finds under the wrong matcher, and both
readers expand a fragment's `{kit}` or `{here}` token identically — `check-hook-destinations.sh`
asks each through `--resolve-fragment` and refuses when they disagree.

`tools/workflows/check-protocol-parity.test.sh` keeps the shipped
`tools/workflows/REVIEW-PROTOCOL.template.md` equal to the live `memory/guides/REVIEW-PROTOCOL.md`
modulo the install prefix, and asserts the cap's NUMBER so parity cannot hold over a document
that no longer states the rule.

The FIFTH rule is the ref-keyed verdict join, lifted from `tools/workflows/check-review-join.sh` by
`TOOL-dTieredTribunal-14`. It is last because it is the cheapest failure to recover from: the four
rules above it prevent a BURST, while a mis-keyed join is a wrong verdict that costs a re-run. The
raw-primitive block is never an early exit-0, which would make every later rule unreachable for the
scripts the join ban judges. A `--only=<rule>` selector
over a closed set lets the file gate share this predicate instead of re-implementing it, and a WIRED
command may never carry it — `tools/check-wiring.sh` asserts that, because narrowing a wired hook
turns the cap rules off with no diff.

## Gaps

- **The orientation deny stops forgetting, not evasion.** A commit made by a script, a heredoc or a
  non-git tool, a deleted or hand-written card, a `cd`/`-C` target that is not a literal path or
  does not exist (the last `cd <dir>` before the git token is read; an absent or shell-expanded
  target is a witness, never a walk into an ancestor's `.git`), and a session that started before
  the wiring and never restarted all escape; a READY line's presence is asserted,
  never its correctness. The drive fold lowercases, so on a case-sensitive filesystem the walk
  finds no `.git` and allows with the witness line — every registered node is Windows. Stated in
  the hook's header and in `tools/hooks/README.md`, with no waiver clause by owner decision.
- **The join rule reads a blanked view, and a regex literal survives it.** So a file holding the ban
  table matches its own rule, and `check-review-join.sh` carries a self-exclusion row for the hook.
  The exclusion is measured, not defensive, and silently widens if the table ever moves.
- **Agents spawned INSIDE a workflow sidechain are uncounted, and always will be.** The script's
  `agent()` is a runtime call and not a TOOL call, so the `Workflow|Agent` matcher has nothing to
  match, and a sidechain agent holds neither tool to re-fan-out with. NOT because a sidechain runs no
  hooks — it does (`TOOL-cRefutedPremise-1`). Declared here and in the protocol; it is why the `Workflow`
  half is static.
- **A `Workflow({name:'…'})` run supplies no source to the hook.** Covered second-hand by the
  merge-bar leg over `tools/workflows/`, which is why that leg exists. The spec-audit rule needs no
  source, so a name-only spec audit IS judged.
- **The spec-audit rule has three stated limits.** A harness's nested `workflow()` is a runtime
  call, not a tool call — that route is `TOOL-aBlindedTrial-3`'s. It reads the WORKTREE README
  and conf while the driver reads BASE, so one uncommitted edit can split them. An unparseable
  `args` string shows it no `kind` and is admitted; the harness throws on it, so no audit runs.
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
  stripped before the scan; block comments are not. Benign and fail-closed, so it stays; an
  apostrophe inside one that pairs with a later quote is the residual below (`TOOL-dMispairedQuote-1`).
- **`renderCodeView` models no regex literal, so rule 2 falls back for such a script.** It inherits
  `blankLiterals`' code-mode branch set, which tests `//`, `/*`, a backtick and the two quote
  characters and nothing else — a backtick inside `/…/` therefore opens template mode and never
  closes. Failing closed on that DENIES a legal harness, so an unterminated scan falls back to the
  per-line `stripStrings` view (`TOOL-aLexedStripper-5`). The residual is SAFETY, not only
  precision: prose punctuation read as structure can admit on four of the five rules, as
  `TOOL-dMispairedQuote-1` measured.

- **Two residuals survive the quote rule, both stated rather than closed** (`TOOL-dMispairedQuote-1`).
  `resolveLiteralEnd` opener-tests only the OPENING quote, so a mispairing needs ONE apostrophe in a
  legal opener position before the fan-out and ANY unescaped quote of the same kind after it. And the
  keyword clause admits a quote after `return`, `case`, `throw` and eight more, every one of which is
  also an English word — `/* throw 'em */` mispairs. A third: an apostrophe after an operator is in
  a legal opener position, so `/* rock - 'n roll */` mispairs too. Each is fixtured one arm per
  member of the declared set; none is a regression. What bounds the consequence is the next bullet.
- **Each view exists TWICE, and that is the mechanism rather than duplication**
  (`TOOL-dMispairedQuote-3`). `renderShippedLine`, `renderShippedView` and `renderShippedBlanks` are
  the pre-fix bodies, frozen and byte-compared against the BASE blob by an arm; `renderStrippedLine`,
  `renderLexedView` and `renderBlankedView` are the corrected ones; and three one-line dispatchers
  over a module-level `VIEW_MODE` choose between them. `runBothViews` runs every rule under both and
  merges, so a denial from either stands. Correcting what counts as a string literal un-hides
  delimiters as well as fan-outs, so the corrected views alone can ADMIT what the old ones denied;
  running both makes the change monotone in the DENY direction by construction. The property is gated over the whole tracked corpus plus its own fixtures.

## Reuse affordance

seam: agent-cap.topLevelArgs — reuse whenever source text must be split into positional items (call
arguments, array elements, parameter lists) and the count matters; extend by calling it, never by
re-deriving `1 + count(commas)`, which reads a trailing comma as an item.
seam: agent-cap.boundedK — reuse to resolve a source token to an integer bound that is either a
literal or a file-bound constant never reassigned; extend by adding a CALL SITE, never a second
resolver, and note that it deliberately refuses an `<expr> || <int>` fallback as a bound.

The MARKED-DERIVATION receiver is the same class one level out (`TOOL-dTieredTribunal-13`). A marked
assignment may derive its receiver from a value already proven bounded, because a `.filter()` or a
`.slice()` cannot grow an array. Every top-level value branch is judged on its own text against a
closed list of three forms, so a ternary whose other arm is caller-supplied does not pass, and a
branch the walk cannot delimit never qualifies.
seam: check-verifier-fanout.delegation — reuse the shape whenever a merge-bar gate and a live hook
must apply ONE rule: the gate builds the hook's payload and runs the hook, so there is never a second
implementation to drift.
