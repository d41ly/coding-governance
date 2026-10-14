# Foundations revisit — the owner's view of the product's foundations and gaps, step by step, and how each fits the design

**Serves:** research PLAY-dClosedLoop-1

After the walk-through the owner reopened the foundations: "Let's revisit the foundations of this
product and several gaps as seen BY THE OWNER, and decide how they fit into the new design, step by
step". Each step below holds the owner's words verbatim, the current state measured against them,
the design response, the forks asked and the answers. Architecture v2 is amended only after a step
settles.

## [step-1] The charter and every load-bearing instruction

### The owner's words

> 1. Charter (AGENTS.md) and any other load-bearing instructions (guide/method/protocol/..etc).
> Charter is the very first document loaded into any LLM/agent by default. By definition, it should
> contain fundamental, project-shaping rules and methodologies that redefine EVERYTHING agents do in
> the repo (adopter). Example: charter says [yagni] {You Aren't Gonna Need It} - any other step of
> the flow adjusts to this practice; charter says [solid] {five rules for object-oriented design} -
> every process adjusts to accomodate for object-oriented design. Major flaw of the prose-driven
> instructions - the way they are loaded in maintained in the agents' memory. All governing
> protocols and instructions should have clear order and directions how to use them. For example,
> the charter's contents should be wrapped in a tag that clearly says 'this one is always first, no
> matter when it's re-read', eg. [AGENTS.md. Priority order: 1. These instructions ALWAYS COME
> FIRST and take precedence over everything else.] {instructions} [/AGENTS.md]. Lower level
> instructions/methods follow the same pattern but different Priority orders. The idea: an agent
> must be able to construct a clear instruction hierarchy no matter WHEN it loads an instruction
> file, as sessions are fluid and sometimes reset their context windows forcing agents to
> re-derive.

### Current state, measured 2026-10-14

- **About 25 load-bearing instruction documents, about 551 KB** (`wc -c`): the charter `AGENTS.md`
  (16,732 B rendered from the 13,695 B template), `CLAUDE.md` (12 B, one `@AGENTS.md` import), the
  path-scoped rule `.claude/rules/product.md`, nine guides under `memory/guides/` (the unattended
  four alone 216 KB), `memory/TEMPLATE-SPEC.md` (39 KB), `memory/HYGIENE.md` (59 KB), the kickoff
  engine `skills/session-kickoff/SKILL.md` (18 KB), seven rendered Skills and nine rendered agent
  definitions under `.claude/`.
- **They arrive by six routes, at different times:** the charter through `CLAUDE.md`'s import at
  session start; path-scoped rules when a matching file is opened; guides when the charter's
  "Protocols — read the one whose trigger holds" sends an agent to read one; Skills when invoked;
  agent definitions as a subagent's system prompt; the orientation card and hook feedback through
  hooks (`.claude/settings.json` replays the card on `resume|compact`). Nothing restores the
  relative order of what was read before a compaction.
- **Precedence is stated in three places, all about kickoff:** the engine
  (`skills/session-kickoff/SKILL.md`: "project `CLAUDE.md` > project manifest > this skill"), the
  manifest (`memory/guides/SESSION-KICKOFF.md`) and its template. The charter states no precedence
  over anything; its one ordering line is that the micro-formats beat voice and brevity rules
  (`[formats]`). No guide states where it sits (measured with `git grep` for precedence, outrank,
  take priority, override).
- **No document carries an identity or priority marker.** A subagent loads no `CLAUDE.md` at all
  (every role carries `omitClaudeMd: true`): it sees charter fragments, a few rule lines and the
  protocol pointers, rendered into its definition under `## Charter`, with nothing ranking them
  against its role or its task.
- **The charter's practices are one-line rules without reach.** `[yagni]` reads "build what this
  unit needs now, never scaffolding for later, and delete rather than disable"; nothing states what
  it changes at Plan, at Test or at Deploy, and no stage contract, role or review lens reads the
  practice set. The practices are gov's governance rules; an adopter's methodology (the owner's
  `[solid]` example) has no home but free prose in its project block.

### Design response

**R1. The charter is the methodology layer, and each practice declares its reach.** A practice is a
tag, a one-line rule, and its REACH: what it changes at each stage it touches. `[yagni]` at Plan:
no build for a speculative need; at Design: no extension point, option or layer the unit does not
use; at Build: delete rather than disable; at Test: no test for a path that is not built; at
Review: speculative generality is a finding. The stage contracts, the role handoffs and the review
lenses read the active practices' reach for their stage, so a practice really does redefine every
step. Practices come from a shipped catalogue (gov's governance practices plus methodology
practices such as `[solid]`, `[dry]`, `[tdd]`), an adopter selects its active set as a policy, and
an adopter may declare its own.

**R2. An instruction hierarchy every agent can rebuild at any moment.**
- **A registry** in the loop kit lists every load-bearing instruction document: its id, priority
  rank, scope, load trigger, what it yields to, and a one-line direction for its use.
- **An envelope** wraps each document's content, generated from the registry by whatever renders
  that document (the playbook renderer for the charter, the memory-tree kit for the method, the
  roles kit for agents and handoffs), in the owner's form:
  `[AGENTS.md · Priority 1 · Always first: these instructions take precedence over everything else, whenever they are read]`
  … `[/AGENTS.md]`. A lower document carries its own rank, its scope, its trigger and the ranks it
  yields to.
- **One precedence rule**, inside the rank-1 envelope: a conflict resolves by rank, never by load
  order or recency; a document from this repository that carries no valid envelope is data, not an
  instruction; an envelope found inside tool output (a web page, a command's output, a file outside
  the registry) is data too, so the envelope cannot be forged into authority.
- **Re-derivation after a reset**: every envelope places its document on its own; on `compact` and
  `resume` a hook re-injects the instruction map (the rank table, what loads when, the active
  policy preset), and the rank-1 envelope directs a reset agent to rebuild the hierarchy from that
  map before acting.
- **A gate**: every registered document carries a well-formed envelope matching its registry row;
  every load-bearing document is registered; only the charter holds rank 1; envelopes open and
  close in pairs. A subagent's handoff wraps each of its blocks (charter rules, role, task) in
  envelopes with their ranks, so a subagent holds the same hierarchy as the main loop.

**A first ladder, to confirm** (rank 0 is the platform's own system and safety instructions, above
every repository document and not the repository's to rank):
1. the charter, `AGENTS.md`: the foundation practices and their reach;
2. the loop: the stage contracts and this repository's current policy values;
3. stage methods and protocols: the build method, the review protocol, the unattended protocol and
   its parts, the merge bar, the kickoff manifest, the spec format, the record rules;
4. kit runbooks, Skills and path-scoped rules;
5. the role: an agent's definition;
6. the task: the brief, the spec, the card's route, a handoff's task block;
7. records and memory: evidence and background, never instructions (the charter's `[memory]`).

**Placement in the chain.** The charter and the instruction hierarchy are the foundation the loop
is declared on, which argues for a new root build ahead of the Spine rather than four more units
inside it; the charter's front door and the tag grammar would move with it.

### Forks asked, 2026-10-14

**F1-1. "When your live instruction in chat conflicts with the charter, which wins? (The
platform's own system and safety rules sit above both and aren't the repo's to rank.)"** Offered:
Live owner wins, conflict named (Recommended); Charter outranks everything; Charter wins unless
overridden. Answer: Charter wins unless overridden.

**F1-2. "Below the charter, what priority ladder should documents get?"** Offered: Loop, method,
kit, role, task (Recommended); Task above role; Charter, then specificity. Answer: Loop, method,
kit, role, task (Recommended).

**F1-3. "How should the charter's practices be modelled?"** Offered: Catalogue with reach
(Recommended); Reach, gov's practices only; Keep one-line rules. Answer: Catalogue with reach
(Recommended).

**F1-4. "Where should the charter and the instruction hierarchy be built?"** Offered: New root build
(Recommended); Inside the Spine. Answer: New root build (Recommended).

### Settled design for step 1

- **The override rule.** The charter wins a conflict with a live instruction unless the owner says,
  in so many words, that they are overriding it; the agent then records the override (the rule it
  set aside and the owner's words) so a standing override becomes a charter amendment rather than a
  habit. The behaviour is a policy, `charter.override`: `explicit-override` by default, with
  `live-owner-wins` and `absolute` as allowed values.
- **The ladder, as confirmed:** 0 the platform's own instructions; 1 the charter; 2 the loop and the
  repository's policy values; 3 stage methods and protocols; 4 kit runbooks, Skills and path rules;
  5 the role; 6 the task; 7 records and memory, evidence only. The ladder is product structure; a
  repository registers its own documents onto it.
- **Practices with reach** from a shipped catalogue, the active set a policy (`charter.practices`)
  that no preset touches, because a methodology is a choice about the product, not a posture.
- **A new root build, dOrderedCharter**, ahead of the Spine. It owns: the practice catalogue and its
  reach; the charter re-founded (the rank-1 envelope, the front door, the precedence and override
  rule, the active practices with their reach, the hand-off to the loop, the repository's project
  block from its own overlay, gov's included); the instruction registry; envelopes for every
  registered document and the gate over them; the instruction map re-injected on `compact` and
  `resume`; ranked envelopes in every subagent handoff; the section-tag grammar and its resolver.
  The charter's kit, `tools/playbook/`, is the natural home: it already renders the charter, and the
  loop kit then builds on it. The front door and the tag grammar leave the Spine for this build.
- **Gaps the owner named, added to the register:** gap-found-01 (no instruction hierarchy),
  gap-found-02 (practices without reach, methodologies without a home), gap-found-03 (subagents hold
  unranked charter fragments), gap-found-04 (no rule or record for overriding the charter); all
  owned by dOrderedCharter.

### Step 1, continued: the charter teaches every agent how to drive gov

#### The owner's words

> 1. Continued. As charter is the very first instruction set loaded into any agent (Claude Code
> main sessions, any sidechain agents, or any other LLM), it HAS to contain a set of high-level
> instructions how to interact with Gov and how to drive it forward. By default, any agent would
> need to derive how to use the kit, read multiple sets of files, this gap should be closed from
> the start - any agent loading the charter not only should learn how the founding rules of the
> project but also how to initiate and drive the loop forward, according to its role. Further
> instructions should come from the tooling messages and similar. This should be mechanically
> rendered into the charter based on the adopted pieces of the kit.

#### Current state, measured 2026-10-14

- **Per-kit rendering exists, as template blocks.** The charter's generated "Tools to rely on"
  section comes from `<!-- kit:<id> -->` blocks inside `coding-governance-agents.template.md`
  (lines 111-160): one line per kit saying what the tool answers, dropped when a target lacks the
  kit. The lines live in the template, not in the kits' own descriptors (`tools/*/kit.toml` carry
  files, roles and versions, nothing for the charter), and none says how to start, advance or
  finish a stage, or what a given role does first.
- **Tools rarely say what comes next.** `git grep` finds a next-step line in six adopt scripts
  (`tools/*/adopt-*.sh`, installation hints) and the string `next —` in three files under `tools/` and
  `skills/`; the hooks put a remedy in their refusal reasons (`tools/hooks/scratch-guard.js` names
  one in eight places), but no command ends by naming the caller's next step.
- **Other harnesses load the charter.** `tools/agent-instructions/` wires `AGENTS.md` for Codex,
  Copilot, Cursor, Windsurf, Amp, Devin, Zed, Aider and Jules natively and Gemini through its
  settings, so the charter is the one document every harness reads. Codex reads at most 32 KiB of
  project instructions (`tools/agent-instructions/README.md`, verified there 2026-10-05), below the
  template's 48 KiB gate: a hard input to the charter's re-derived cap.
- **Claude Code hooks guide only Claude.** A non-Claude agent meets no PreToolUse or Stop hook; the
  git hooks (`.githooks/pre-commit`, `.githooks/pre-push`) are what every harness passes through.

#### Design response

**R3. The charter's drive section, rendered from the adopted kits.** Inside the rank-1 envelope,
after the practices: how to start, by situation and role (a new task from the owner, a resumed
session, an unattended run, a subagent's task, another harness without gov's hooks); for each stage,
the command that enters it, the one that advances it and the witness that ends it; and one line per
role (its stage, its inputs, its first move, what it hands back). Each kit declares its own lines in
its descriptor; the renderer composes the section from the adopted kits alone, in the loop's stage
order, so an adopter's charter names exactly the tools it has.

**R4. The tools drive the rest.** Every gov command ends its output, success or refusal, with a
`next —` line naming the caller's next command; a `next` verb in the loop kit reads the current state
(the card, the route, derived unit states, leases, the plan, the policy) and prints the next action
for a named role. The charter's last drive instruction is "follow the `next —` lines; when unsure, run
`next`". A check holds every declared command to ending with a `next —` line or declaring itself
terminal.

**R5. Harness-independent by construction.** Every drive step names a CLI command; a Skill is a
Claude Code shortcut over the same command; the git hooks enforce for every harness, and Claude
Code's own hooks add guidance on top.

**R6. A charter every harness can read whole.** The drive section is one line per stage and per role;
per-role detail travels in handoffs and `next —` lines, and the charter's re-derived cap starts from
the smallest consumer's limit (Codex's 32 KiB).

#### Forks asked, 2026-10-14

**F1-5. "After the charter's start, how should an agent learn its next step?"** Offered: next verb +
next-lines (Recommended); next-lines only; Charter table only. Answer: next verb + next-lines
(Recommended).

**F1-6. "Where should each kit's drive lines be declared?"** Offered: Each kit's descriptor
(Recommended); Centrally, in the loop; Template kit blocks, as today. Answer: Each kit's descriptor
(Recommended).

**F1-7. "How much of the per-role guide belongs in the charter itself?"** Offered: One line per role
(Recommended); Main session only; Full per-role guides. Answer: One line per role (Recommended).

**F1-8. "How harness-independent should driving gov be?"** Offered: CLI-first (Recommended); Claude
Code first. Answer: CLI-first (Recommended).

#### Settled, and where each piece lands

- **dOrderedCharter (Foundation)** renders the drive section: how to start by situation, each
  stage's enter, advance and exit commands, one line per role, and the closing "follow the `next —`
  lines; when unsure, run `next`". Kit descriptors gain a drive table (stage, role, command, when)
  whose schema this build defines; the section is composed from the adopted kits alone and checked
  both ways. Each subagent's handoff repeats its role's line, ranked. The charter stays inside the
  smallest harness's limit, Codex's 32 KiB, from this build on.
- **dDeclaredLoop (Spine)** builds the `next` verb over the loop's state and the `next —` micro-format,
  plus the check that every command a descriptor declares ends with a `next —` line or declares itself
  terminal; commands that do not yet emit one sit on a shrink-only list, each owned by the chain
  build of its kit's stage.
- **CLI-first**: every drive line names a CLI command, and a Skill is a shortcut over it.
- **Gaps the owner named, added to the register:** gap-found-05 (the charter does not teach an agent
  how to drive gov for its role), owned by dOrderedCharter; gap-found-06 (no tool names the next
  step, so the loop advances only by agents re-deriving it), owned by dDeclaredLoop.

## [core] The principles cannot be built around

### The owner's words

> All the practices we're outlining here need an internal consistency mechanism - it should not be
> possible to just build around them, if any part of the kit is being extended. These are
> fundamental and must remain at the core of the entire product.

### Current state, measured 2026-10-14

- **Most practices name no enforcement.** Of the charter's 36 practices, 22 are cited by no code file
  under `tools/`, `.githooks/` or `skills/` (instrument below): `[yagni]`, `[reuse]`, `[consistency]`,
  `[one-fact]`, `[verify]`, `[left-shift]`, `[small]`, `[land]`, `[post-merge]`, `[migrations]`, `[ids]`,
  `[memory]`, `[records]`, `[docs]`, `[risk]`, `[bytes]`, `[tokens]`, `[tools]`, `[roles]`, `[voice]`,
  `[signal]`, `[formats]`. A citation is a proxy: `[roles]` and `[formats]` are enforced by the spawn
  guard and the format guard without naming the tag. The defect is the missing declaration: nothing
  states which check enforces which practice, so nothing notices a practice that nothing enforces.
- **No leg declares the principle it serves.** `tools/gate-legs.json` has no `principle`, `practice` or
  `enforces` key on any of its 140 legs.
- **Factories exist for three kinds only**: adopting a kit (`tools/*/adopt-*.sh --scaffold`), opening a
  build (`gen_build_index.py --new-build`) and writing a micro-spec (`--new-spec`). A new kit, command,
  governing document, policy key, gate leg, role, workflow, hook or Skill is made by hand.
- **Strong population checks already exist, per mechanism:** the codebase map's both-directions
  claims, govkit's declared kit population, install-prefix and dead-path carriers, kit versions and
  epochs, armed fail branches, executed-count floors, the README slot contract, method carriers,
  spec tokens, hook destinations, the lexicon's naming predicates. They prove the pattern works; they
  are organised by mechanism, not by principle, so a new principle has no place to declare its check.

### Design response

- **C1. A principle registry, the product's constitution.** Every architecture principle (P1 onward)
  and every charter practice is registered: its tag, its one-line statement, the extension kinds it
  binds, and the checks that enforce it. The charter's core block renders from it.
- **C2. A meta-check: no principle without its enforcement.** Every registered principle names at least
  one enforcing check (a gate leg, a hook or a factory invariant); every check names the principles it
  enforces (legs gain an `enforces` key); a principle nothing enforces reds; a check naming an unknown
  principle reds. Each check is seen red before it is trusted.
- **C3. A closed set of extension kinds**: kit, command, governing document, policy key, preset, gate
  leg, role, workflow, hook, Skill, practice, record kind, stage. Each lists the principles that bind
  it; a part of a kind nobody registered reds, so a new kind cannot appear outside the mechanism.
- **C4. One factory per kind.** A `new` verb per kind produces an instance that already conforms
  (descriptor and drive table, stage claim, envelope, `next —` line, schema entry with a default and a
  value in every preset, armed checks, map claim, lexicon-conforming names); the gates still check
  hand-made instances, so the factory is the easy path and never the only guard.
- **C5. Conformance gates per kind**, over each kind's whole population, both directions.
- **C6. Principles are not policies.** A policy tunes behaviour inside the principles; no switch turns
  a principle or its check off; a principle changes only through an owner-ratified amendment recorded
  as a product change. Exceptions are a separate, owner-guarded register.
- **C7. The core and the bypass.** Round 5 allows hook bypass by default because gates have caused
  problems; a bypass that also skips the core checks would be the way to build around them, so the
  core's relation to the bypass is the fork below.
- **Placement.** The registry, the meta-check, the kinds register, the exception register and the core
  checks' semantics belong to the foundation build, dOrderedCharter. Each later chain build registers
  the checks for the principles it implements, and the meta-check refuses it a principle without one,
  so no chain build can land around the core either.

### Instrument

```python
"""For each practice tag in the charter's section 1, count the non-markdown files under tools/,
.githooks/ and skills/ that cite the tag, a proxy for "some code names this practice as what it
enforces". Reads the tree through git; writes nothing."""
import re
import subprocess
import sys

root = sys.argv[1]
charter = open(f"{root}/AGENTS.md", encoding="utf-8").read()
body = charter.split("## 1. Governing practices", 1)[1].split("### Micro-formats", 1)[0]
tags = re.findall(r"^- \[([a-z-]+)\]", body, flags=re.M)
files = subprocess.run(["git", "-C", root, "ls-files", "tools", ".githooks", "skills"],
                       capture_output=True, text=True, encoding="utf-8").stdout.split()
code = [f for f in files if not f.endswith(".md")]
texts = {}
for f in code:
    try:
        texts[f] = open(f"{root}/{f}", encoding="utf-8", errors="replace").read()
    except OSError:
        pass
cited = {t: sum(1 for txt in texts.values() if f"[{t}]" in txt) for t in tags}
none = [t for t, n in cited.items() if n == 0]
print(f"practices {len(tags)} · code files scanned {len(texts)}")
print(" ".join(f"{t}={n}" for t, n in cited.items()))
print(f"cited by no code file: {len(none)} — {' '.join(none)}")
```

### Forks asked, 2026-10-14

**K1. "You allowed hook bypass because gates cause problems. How should the core conformance checks
relate to that bypass?"** Offered: Core never bypassed (Recommended); Bypass all, block after; Bypass
all, report after. Answer, in the owner's words: "Bypass all by default, but owner-adjustable".

**K2. "Can a principle itself be switched off by policy?"** Offered: Fixed; policies tune
(Recommended); Switchable under the guard. Answer: Fixed; policies tune (Recommended).

**K3. "Should every extension kind get a factory?"** Offered: A factory per kind (Recommended); Gates
only. Answer: A factory per kind (Recommended).

**K4. "How may an exception to a principle be granted?"** Offered: Owner-only, expiring, shrink-only
(Recommended); No exceptions; Recorded, any session. Answer, in the owner's words: "Recorded, any
session by default, owner-adjustable".

### Settled design for the core

- **Principles are fixed.** No policy turns a principle or its conformance check off; a principle
  changes only through an owner-ratified amendment recorded as a product change (K2).
- **`core.bypass`**, a policy: `with-hooks-report` by default, with `with-hooks-block` and `never` as
  allowed values (K1). A permitted bypass skips the core checks along with every other leg, and the
  floor records it.
- **INTERPRETATION, CONFIRMED 2026-10-15.** K1's answer does not say what happens to a core red found after a
  bypass. The default above reads it as report-after, because the owner's other answers keep one
  agent's red from blocking another's unrelated work (walk T1). The core is kept from being built
  around a different way: the core red is filed as a BLOCKER ask against the build whose commit
  introduced it, and THAT build cannot reach its exit until the red is fixed or excepted. The
  violation stops the violator, not the fleet. `with-hooks-block` (every later push blocks) and
  `never` (core checks always run) are the switches if that reading is wrong.
- **Confirmed, 2026-10-15.** The reading went back to the owner as a fork offering all three values,
  and the owner chose "A: the violator pays": `with-hooks-report` stands as read, and P16 is unchanged.
  One leak is closed with it. A core red that first appears in the landing merge, after Build's exit
  and under a bypassed Test verdict, could land with a build that closes before the red is
  attributed. So dShippedRelease's lander runs the core checks on the landed tree before it releases
  the build (v2 `[chain]`). Under `core.exceptions: any-session-recorded`, "fixed or excepted" lets
  the build's own session record the exception, and the Loop Review audits it.
- **`core.exceptions`**, a policy: `any-session-recorded` by default, with `owner-only-expiring` and
  `none` as allowed values (K4). Every exception carries its principle, the part it excuses and a
  reason; the Loop Review audits the register on each pass.
- **A factory per extension kind** (K3), each landing with the build that defines that kind's
  conformance gate: governing document, practice and Skill in dOrderedCharter; command, policy key,
  preset, stage, hook, role and workflow in dDeclaredLoop; gate leg in dWitnessedBar; kit in
  dShippedRelease; record kind in dConvergedCharter. Until a kind's factory lands, the kind sits on a
  shrink-only pending list owned by that build, and its gate checks hand-made instances throughout.
- **dOrderedCharter owns the mechanism**: the principle registry, the meta-check, the kinds register
  with each kind's owning build, the conformance-gate contract, the exception register and the
  `core.*` policies.
- **Gaps the owner named, added to the register:** gap-found-07 (no principle declares its
  enforcement) and gap-found-08 (extensions are hand-made, factories exist for 3 of 13 kinds), both
  owned by dOrderedCharter.

Output at `5a670d5c`:

```text
practices 36 · code files scanned 324
yagni=0 reuse=0 consistency=0 core=2 contract=3 derive=3 one-fact=0 spec=6 verify=0 gate=17 class=1 left-shift=0 bar=2 cost=6 small=0 isolate=3 land=0 post-merge=0 reconcile=2 migrations=0 ids=0 memory=0 records=0 docs=0 security=2 risk=0 bound=1 bytes=0 cross-os=1 tokens=0 tools=0 roles=0 voice=0 signal=0 formats=0 default=1
cited by no code file: 22 — yagni reuse consistency one-fact verify left-shift small land post-merge migrations ids memory records docs risk bytes tokens tools roles voice signal formats
```