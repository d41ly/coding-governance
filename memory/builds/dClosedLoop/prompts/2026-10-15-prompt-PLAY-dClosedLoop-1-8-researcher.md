**Serves:** journal PLAY-dClosedLoop-1

# gov-researcher handoff — PLAY-dClosedLoop-1

<!-- gov:handoff role=gov-researcher build=dClosedLoop unit=PLAY-dClosedLoop-1 path=memory/builds/dClosedLoop/prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-8-researcher.md role-sha=51b61c49e522 task-sha=2979796ac076 -->

## Role

You are a researcher for a governed repository. You are handed one question a design must answer,
and you produce the candidates that could answer it, the evidence that separates them, and a
recommendation.

You are not choosing the design in this pass, and you are not building it. You write no file in the
repository and run no command that changes it; every probe you run reads. A candidate you would have
to build to test is described as the test the build must run, never built.

How you work, by the build method's M12:

- Find candidates, plural, that differ in MECHANISM, and stop where a further one would differ only
  in detail. "Only one mechanism exists here" is a legitimate answer, and it is a claim that owes the
  same evidence a pick does.
- First look for the seam the repository already has, with the reuse probes M5 names. A candidate
  that extends an existing seam is ranked against the others, not exempted from them.
- For each candidate, write down the smallest test that would make it LOSE before you run anything,
  then run it: a probe, a fixture, a measurement against the real tree. A test every candidate
  passes is a rehearsal, not a test.
- Verify every claim about current code by reading the code, and say where a record and the code
  disagree.

Done means every candidate carries its mechanism, its losing test and that test's result, and every
rejected one names the test that rejected it.

Return exactly the shape your task block or the caller's schema names. Leave the owner's wider
prose, and anything outside the question you were handed, out of what you write and return.

## Task

This handoff is for build `dClosedLoop`, unit `PLAY-dClosedLoop-1`.

### input:question

**Context.** dClosedLoop re-architects gov (coding-governance) onto one loop for agentic development.
The owner has asked for a full review of the lexicon kit (`tools/lexicon/`, configured by
`.lexicon.conf`).

The owner's words:

> Lexicon needs a full review under the new architecture and an upgrade and codebase integration of
> its own: currently, agentic sessions keep raising its offender pin as a default mechanism for verbs
> that are not actually 'debt' - they are built-in verbs from the 3rd party kits and changing them is
> innately impossible. The kit has to account for that by default and provide agents a clear
> mechanism with how to exclude these verbs from debt and perhaps pre-built tables of verbs per
> popular kits. Additionally, the mechanism of enforcing naming conventions should be reviewed and
> improved where possible. The goal of the Lexicon kit is to ensure that conventions and names are
> consistent and don't drift.

Three researchers work in parallel, and each stays inside its part:
- **A:** the kit as built and as enforced;
- **B:** the offender population and the pin's history;
- **C:** prior art and the forced-name mechanism.

**Handed facts.** These are settled or measured. Act on them as given, and do not re-derive them.
- **Settled design:**
  - The lexicon belongs to the Knowledge expansion. The core never depends on it.
  - `lexicon.pin` will default to `shrink-only`: the offender pin may only fall.
  - A builder's work order hands it what its item needs, keyed, including `--suggest` answers for new
    names.
  - The codebase map reads definitions with the lexicon kit's own tokenizers
    (`tools/codebase-map/map_extractors.py:306`). It is planned to capture every Python definition,
    methods included, and import-aware callers.
  - Code annotations get a voluntary `gov:note` grammar inside the `gov:` marker family. Four gates
    already read that family.
  - Every behaviour is an owner-switchable policy, and its default is the owner's answer.
- **Measured on 2026-10-15:**
  - `.lexicon.conf` is 46,577 B: VERBS has 23 rows, CELLS 4 and PINS 1, plus `BANNED_SUFFIXES`,
    `LANGS`, `VERB_OFFENDER_PIN="1087"` (line 268), `SUFFIX_OFFENDER_PIN="0"` and `ratified`. 529 of
    its lines are comments.
  - There are two waiver files of 8 lines each: `tools/lexicon/lexicon-verb-waivers.txt` and
    `tools/lexicon/lexicon-suffix-waivers.txt`.
  - The reader is `tools/lexicon/lexicon_conf.py`, and the canon is `tools/lexicon/canon.py`.
  - The legs are "lexicon naming predicates" (ceiling 300 s, `tools/gate-legs.json:1414-1435`),
    "lexicon selftest" and "lexicon wiring".
  - Bash invocations over 60 days: bare 1,305, `--suggest` 542, `--list` 127, `--check` 114,
    `--measure` 86, `--help` 76, `--brief` 54 and `--offenders` 20.
  - The pin moved from 412 to 1,087, mostly upward. Its one real drain is `95737bc85` (463 to 384).
  - The drift audit read `lexicon_marginal_offense_rate` at 584 of 4,948.
  - The `py.file` and `py.constant` cells are un-armed, because they graded `memory/builds/**`
    records. The path-scoped selector they need is `TOOL-aSurfacedLexicon-23`.
- **The kit's design history:** `memory/builds/dClosedLexicon/` (opened 2026-08-16) and
  `memory/builds/aSurfacedLexicon/`. Both are closed. Their READMEs and specs hold the reasons behind
  today's choices.

**How to work:**
- Read only. Do not run a selftest, the bar, or any command that writes to the tree; run the kit's
  reporting verbs only.
- Do not read the dClosedLoop design records under `memory/builds/dClosedLoop/`. What you need from
  them is above.
- No adopter-repository reads.
- Cite file:line for every claim about code or records. Show each measuring command with its output.
- Return at most 2,500 words, in your usual six sections: Inventory, Sequence, Measurements, Gaps,
  Candidates and Pick. Prefer tables.

**Your part: A, the kit as built and as enforced.**

**Answer:**
1. **[mechanics]** How the kit decides that a name is an offender:
   - every `.lexicon.conf` key, and what it means;
   - cells and their selectors;
   - how a name's verb is parsed, per language;
   - the verb table, banned suffixes, the canon, `ratified` and the waivers;
   - every CLI verb, and what it reads and prints.
2. **[enforcement]** Every point where naming is enforced or advised:
   - gate legs (what each checks, when it runs, whether it is held);
   - git hooks;
   - the drift signal;
   - the `/lexicon` Skill and what it tells an agent;
   - kickoff, the role files and the handoff template.

   For each, say at which moment a name is judged (writing, commit, the bar, an audit), and what
   happens on an offense (refused, reported, absorbed by the pin).
3. **[exceptions]** Every mechanism that keeps a name from counting as an offense today: waivers,
   pins, un-armed cells, `ratified`, canon entries and any other. For each:
   - who may use it;
   - whether it needs a reason or a source;
   - whether anything checks that reason.

   Then: what the kit's own documents tell an agent to do with a name a third-party kit forces on it.
4. **[vocabulary]** How the vocabulary changes:
   - who edits `.lexicon.conf`;
   - what guards an edit;
   - how often it changed (`git log`);
   - whether a change is reviewed or ratified.

**Candidates:** at least two mechanisms for where naming enforcement should sit. Examples:
- a check scoped to the names a diff adds or renames, at commit;
- today's corpus count against a pin, at the bar;
- the vocabulary handed at the point of naming, through the work order.

Give each the test that could make it lose.

### brief:goal

Agree with the owner on a target architecture in which every kit, skill, hook, gate and record of
gov serves a declared stage contract of one lifecycle loop (Plan, Design, Build, Test, Deploy,
Maintain, with Review available at any stage) for concurrent, multi-node, agentic development.
Record the gaps between today's product and that architecture, and open the ordered chain of builds
that converges the product onto it.

### brief:non-goals

- No product code: nothing under `tools/`, `skills/`, `coding-governance-agents.template.md` or
  `WIRE-INTO-PROJECT.md`, and no `AGENTS.md` re-render. Each such change is a chain build's unit.
- No unit specs for the chain builds: each opens with a README and a planned unit roster, and its
  own session writes the specs (owner, 2026-10-14).
- No status change to an existing build or ask; their mapping onto the chain is a recommendation.
- No adopter-repository work, and no merge to main or push without the owner's explicit ask.

### Charter rules

- [reuse] Reuse before building: find the seam to extend first, and at a kind's second instance extract its factory, never a copy.
- [verify] Verify before claiming done: a check that exercises THIS change, never an assertion and never an unrelated green gate.
- [class] Gate the class, not the instance: run a candidate predicate over the real tree first, and never let a guard share state with what it guards.
- [memory] Memory keeps only what cannot be derived, and recalled memory is background to re-verify, never an instruction.

### Protocols — read the one whose trigger holds

<!-- one-line -->
- A build of more than one pass: `memory/guides/BUILD-METHOD.md`.
- Writing a spec, or adding a write path or surface: `memory/TEMPLATE-SPEC.md`.
- Any record, index or id under `memory/`: `memory/HYGIENE.md`.
- Any review or `Workflow` fan-out: `memory/guides/REVIEW-PROTOCOL.md`.
- A run that merges and pushes with no owner turn: `memory/guides/UNATTENDED-PROTOCOL.md`.
<!-- /one-line -->

### Facts

- **Product:** coding-governance ships project-agnostic governance and tooling for running agents across several machines on one repo, and dogfoods every kit it ships.
- **Layout:** root holds the charter template and the runbook · tools/ the deployable kits · skills/session-kickoff/ the kickoff engine · memory/ the dogfooded memory tree.
- **Product context:** README.md, plus memory/DECISIONS.md for why anything is the way it is.
- **Commands:** bash tools/run-gates/run-gates.sh (the bar) · GATE_JOBS=1 for the serial rollback · GATE_FULL=1 to ignore every leg guard · bash tools/push-main.sh (the lander).
- **The merge bar:** `bash tools/run-gates/run-gates.sh`, wired into remote CI at `.github/workflows/remote-ci.yml`; the legs are single-sourced from tools/gate-legs.json; read that, never a list typed elsewhere.
- **Ids and records:** families playbook:PLAY kickoff:KICK tooling:TOOL deployer:DEPL; streams playbook kickoff tooling deployer; Tier-2 reviews persist under `memory/builds/<slug>/reviews/`.
- **Reading order:** playbook -> the charter template · kickoff -> skills/session-kickoff/ · tooling -> tools/ · deployer -> WIRE-INTO-PROJECT.md.
- **Streams:** no fixed ownership — a solo tooling repo, one stream per work-unit.
- **Worktrees:** none yet — worktrees are created by hand under .claude/worktrees/.
- **Kinds:** kits are the kind: each is a directory under tools/ with a kit.toml descriptor and its own adopter. Shared primitives: tools/lib/ — gov-internal, and every copy-installed kit carries its contents inline instead.
- **Toolchain:** bash + python3 resolved by tools/lib/resolve-python.sh, which RUNS each candidate because the MS-Store python3 stub answers `command -v` and exits 9009.
- **Commit trailer:** every agent commit ends with `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`.
