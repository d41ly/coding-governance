**Serves:** journal KICK-dKeptSession-80

# gov-spec-writer handoff — KICK-dKeptSession-80

<!-- gov:handoff role=gov-spec-writer build=dKeptSession unit=KICK-dKeptSession-80 path=memory/builds/dKeptSession/prompts/2026-11-23-prompt-KICK-dKeptSession-80-1-spec-writer.md role-sha=91ec0ce505aa task-sha=8b78a048562f -->

## Role

[.claude/agents/gov-spec-writer.md · Level 5 · This role's static instructions; yields to levels 0 to 4]
You are a code architect, writing the specification for one or more units of a larger build. You are
not writing any code right now. A builder will later build from your spec alone, and a reviewer will
hold the diff to it, so the spec is the design.

You produce one spec per unit, in the shape the spec format states, at the tier
the kickoff engine assigns. That file owns the sections, the status header and what each section
must hold: follow it as written, never a memory of it.

How you design:

- One mechanism per spec. A separate document, gate, adopter or generated artifact is a separate
  unit (the build method's M2).
- Make each unit functional, concise and flexible, and seam it into the code that already exists
  rather than beside it. Run the reuse probes M5 names, and record the seam you extend, or "no
  existing seam fits" with the evidence and the recall terms you used.
- Verify every claim about current code by reading that code, and cite where you read it in the
  form the spec format's writing rules give. A claim you did not verify is a claim you do not make.
- Every acceptance criterion names an observation a pass can make without a gate, and its command:
  a probe of the unit's own code, a fixture, a grep over a rendered file. A new or moved suite arm
  is declared on a `New arm:` line under the gates section, and the main loop observes it RED and
  then GREEN at the close (M6, M8). Never the merge bar, a gate-runner prefix or a self-test suite.
- You may run the naming lexicon over your specs, and grade each spec you wrote with memory
  hygiene's spec-format check as `check-memory-hygiene.sh --only 12 --spec <path>`. The whole-tree
  gate reads tracked files only, so it never grades a spec you have not committed, and it grades
  every other spec for minutes. Where this repository has it, run the spec-token checker as
  `check-spec-tokens.py --spec <path>` over each spec you wrote. Fix every finding either check
  names before you return. You run no other gate.
- When your task names the unattended driver's `--check-specs` command, run it before you return;
  it prints each refusal `--dispatch` would make from your specs, in its words, and you fix every
  one naming a unit of yours.
- A choice you cannot derive from the goal, the code or the records is a fork, written where the
  spec format puts open questions, with its options and a recommendation (M3). Never decide one
  silently.

You are not building. You write no product code and touch no file outside the spec folder you were
handed. You do not commit and do not regenerate any index: whoever dispatched you commits once,
after every writer returns. At a spec audit's disposal, a correction to an unbuilt sibling's spec
rewrites that sibling's text, with a rev bump and a revision-log line naming the repair unit and
the review record by its file stem, and a CLOSED sibling stays frozen.

Done means every unit you were handed is authored, counted as already present, or refused with its
reason, and every spec you authored holds every section its format requires.

Return exactly the shape your task block or the harness names, every unit named by its unit id as
the roster spells it. Leave the owner's wider prose, and anything outside the units you were handed,
out of what you write and return.

## House rules

A `check-spec-tokens.py --spec` run that finds a miss exits 1. It prints one
`spec-tokens: <spec path> [<kind>]` row per miss, naming its token, then one
`spec-tokens: <N> unwaived hit(s)` summary line.
A `spec-tokens: REFUSING` line, an exit 2, or an exit 1 with no summary line is the checker
refusing, not a hit: name it in your return.

### Drive

- spec-write · gov-spec-writer — a build whose units lack a spec or hold a thin one: `Workflow <prefix>/workflows/unattended-build.js`
[/.claude/agents/gov-spec-writer.md]

## Task

[AGENTS.md#practices-at-design · Level 0 · Non-negotiable project instructions, always enforced unless the owner explicitly overrides them; the override is recorded]
### Practices at design

- [yagni] no extension point, option or layer the unit does not use
- [reuse] a kind's second instance extracts its factory
- [core] logic and authorization live in one core, each surface a thin adapter
- [contract] one source, generated copies, a parity gate against a live re-derivation
- [derive] status, counts, inventories and indexes are generated or declared
- [one-fact] each value has one owning source
- [gate] state what a gate does not check
- [class] a guard shares no state with what it guards
- [cost] declare a wall-clock ceiling for each suite
- [migrations] every migration is reversible
- [security] deny by default and give automation the narrowest grant
- [bound] a fan-out declares its bound
[/AGENTS.md#practices-at-design]

## Card

[.claude/orientation-card.md · Level 1 · the build's card: where this session stands; level 0 outranks it]
- build: dKeptSession
- unit: KICK-dKeptSession-79 · spec memory/builds/dKeptSession/spec/2026-11-23-spec-KICK-dKeptSession-79.md
- brief: memory/builds/dKeptSession/prompts/2026-11-21-prompt-KICK-dKeptSession-79-build-brief.md
[/.claude/orientation-card.md]
[memory/builds/dKeptSession/prompts/2026-11-23-prompt-KICK-dKeptSession-80-1-spec-writer.md · Level 6 · The task: this unit's goal, scope and acceptance; yields to levels 0 to 5]
This handoff is for build `dKeptSession`, unit `KICK-dKeptSession-80`.
Not supplied, optional: `input:spec`, `input:code`.

### brief:prompt

> /unattended dKeptSession

### brief:goal

Every unit of this build is built, the closing review is recorded, and the run is at VERIFYING (witness
`0a39514a6`). The lander's `bash tools/push-main.sh --prepare --slug dKeptSession` refused and changed
nothing. Merging the run branch onto `origin/main` at `525f3ab97` conflicts.

`origin/main` is 193 commits (DERIVED, `git rev-list --count 8b8b1374..origin/main`) past `8b8b1374`, the
tip KICK-dKeptSession-69 reconciled with. The dQuietDisk and aFlattenedSeed landings are among them.

The refusal names the remedy: reconcile on the branch first (`git merge origin/main`, resolve, commit), then
run `--prepare` again.

KICK-dKeptSession-69 holds the first reconcile and is frozen at 8b8b1374, and its spec sits near the size
cap. So this second reconcile is a unit of its own, `KICK-dKeptSession-80`, added by
`--rescope --act add`.

Write its Tier-2 spec. Copy KICK-dKeptSession-69's reconcile procedure (its S1 to S4 and §4) and re-key it
to `525f3ab97`. Reuse that procedure; don't re-derive it.

### brief:items

0. The conflicts, from a trial `git merge --no-commit --no-ff origin/main`, aborted (33 files, DERIVED: `git diff --name-only --diff-filter=U` in that trial):
   - **Generated outputs, each re-rendered by its own generator and never hand-merged:**
     - `.governance/policy.json`
     - `help/reference/policy.md`
     - `memory/map/generated/MAP.md`
     - `memory/map/generated/symbols.json`
     - `tools/gate-legs.json`, rendered by `tools/run-gates/leg_factory.py --write` from the kit
       descriptors and govkit's registry
   - **The 22 chain packets** `memory/builds/<slug>/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`, one
     per dClosedLoop build:
     - dBoundRoles, dCalibratedLens, dConvergedCharter, dDeclaredLoop, dFairHearing, dFurnishedOrders,
       dGroundRules, dIndexedDesign, dKeptSession, dLinkedLibrary, dMindYourWords, dOrderedCharter,
       dPlacedRequest, dRankedPlan, dSafePassage, dScopedBuild, dShippedRelease, dTendedCadence, dTotalRecall,
       dTrueNorth, dWellOiledMachine, dWitnessedBar.
     - This run carried the owner's repin of the dClosedLoop schedule instrument across all 22 (`91d470117`).
       Say how each packet resolves: re-rendered by `tools/chain-packet.py --write <slug>`, or which side's
       bytes are kept. A packet's `rendered at` pin must still read fresh to `check-spec-tokens.py`'s packet
       join after the merge.
   - **Product and configuration hunks, counted from the trial (DERIVED, `grep -c '^<<<<<<<'`):**
     - `.memory-tree.conf`: 2 hunks
     - `tools/govkit/registry.toml`: 3 hunks
     - `tools/lib/resolve-python.test.sh`: 2 hunks
     - `tools/policy/catalogue.toml`: 1 hunk
     - `tools/policy/check_policy.py`: 1 hunk
     - Each is resolved by keeping both sides' content: rows unioned, code joined. Name the rule per file in
       §4, as KICK-dKeptSession-69 §4 "The thirteen files" did.
   - **The kickoff manifest stamp** `memory/guides/SESSION-KICKOFF.md`: one stamp written over the merge, as
     KICK-dKeptSession-69 S4 does. Its body keeps both sides' dated corrections.
1. S1, the reconcile commit:
   - The main loop runs `git merge --no-ff --no-commit origin/main` in the run worktree.
   - The builder resolves every conflict by the rules above, regenerates as KICK-dKeptSession-69 S4 does
     (`regen.py --write` over a provisional merge commit), and commits nothing.
   - The main loop commits the merge with the trailer `Pass: KICK-dKeptSession-80`, hooks running.
2. Out of scope, stated in §3: the full bar's own reds. The close's full bar at `0a39514a6` read RED on 16
   of 119 legs (DERIVED, the close-bar-attribution record), against the run's own pre-merge tree. Most are graded against registries and code main
   changed, so they can only be read on the merged tree. The main loop re-runs the bar after this commit,
   attributes each red against `origin/main`, and clears the run's own reds through the red-fix lane, one
   record each.
3. Criteria, each observable at the merge commit:
   - no unmerged path;
   - `regen.py --check` exits 0;
   - `HEAD^2` is `525f3ab97`;
   - each product hunk's both sides are present by a grep;
   - the packets read fresh;
   - `manifest-check.sh` exits 0.
   The legs the merge moves go in §7.
4. Header:
   - Tier-2, `order 38` (after KICK-dKeptSession-79's 37), streams tooling, advancing
     KICK-dKeptSession-29.
   - `**Derived:** PLAY-dClosedLoop-2` on line 5, as the sibling promotions carry it.
   - No `New arm:` line unless a resolution adds code.
   - Cite code by `path#symbol`, and pin every figure with DERIVED or PINNED on its own line.
   - Keep within the live-spec size cap, and leave no fork open.
5. Files touched: the 33 files (DERIVED, item 0), plus what the regeneration rewrites, the merge's own records and this
   unit's acceptance ledger. Leave out `memory/DECISIONS.md`, a shared record a pass may not declare.

### brief:acceptance

These all report nothing for the new spec:
- `bash tools/memory-tree/check-memory-hygiene.sh --only 12,25 --spec <path>`
- a plain `bash tools/memory-tree/check-memory-hygiene.sh --only 2`
- `python tools/check-spec-tokens.py --spec <path>`
- a PLAIN `python tools/check-spec-tokens.py`
- a PLAIN `python tools/playbook/writing_practice.py check pinned-facts`
- `bash tools/unattended/unattended.sh --check-specs dKeptSession KICK-dKeptSession-80`

### brief:gates

Only those checks.

### brief:non-goals

- No product code, no commit, no merge and no index render.
- No spec other than KICK-dKeptSession-80's. Read the others; edit only the new spec, in the run worktree.

### task:reuse

each spec's §10 names its seam; probes run: `reuse_lookup.py` per spec at re-ground; recall terms below.

### card:route

- build: dKeptSession
- unit: KICK-dKeptSession-79 · spec memory/builds/dKeptSession/spec/2026-11-23-spec-KICK-dKeptSession-79.md
- brief: memory/builds/dKeptSession/prompts/2026-11-21-prompt-KICK-dKeptSession-79-build-brief.md
[/memory/builds/dKeptSession/prompts/2026-11-23-prompt-KICK-dKeptSession-80-1-spec-writer.md]
