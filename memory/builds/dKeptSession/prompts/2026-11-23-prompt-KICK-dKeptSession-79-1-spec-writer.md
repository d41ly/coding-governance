**Serves:** journal KICK-dKeptSession-79

# gov-spec-writer handoff — KICK-dKeptSession-79

<!-- gov:handoff role=gov-spec-writer build=dKeptSession unit=KICK-dKeptSession-79 path=memory/builds/dKeptSession/prompts/2026-11-23-prompt-KICK-dKeptSession-79-1-spec-writer.md role-sha=91ec0ce505aa task-sha=b5ea08c92680 -->

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
- unit: KICK-dKeptSession-65 · spec memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-65.md
- brief: memory/builds/dKeptSession/prompts/2026-11-21-prompt-KICK-dKeptSession-65-build-brief.md
[/.claude/orientation-card.md]
[memory/builds/dKeptSession/prompts/2026-11-23-prompt-KICK-dKeptSession-79-1-spec-writer.md · Level 6 · The task: this unit's goal, scope and acceptance; yields to levels 0 to 5]
This handoff is for build `dKeptSession`, unit `KICK-dKeptSession-79`.
Not supplied, optional: `input:spec`, `input:code`.

### brief:prompt

> /unattended dKeptSession

### brief:goal

The closing diff review of this build, round 1 over `c2a407b0..bcecefcfc`, read CLEAN WITH FIXES:
- 0 blockers, 0 highs, 5 mediums and 3 lows;
- every finding confirmed, none refuted (run `wf_72f622df-161`);
- the report is
  `memory/builds/dKeptSession/reviews/2026-11-23-review-KICK-dKeptSession-69-closing-diff-review-round1.md`.

The round is CONVERGED, and the driver recorded its exit with `--disposition promote`. The build
method promotes every confirmed finding at that exit: the mediums and lows batch into ONE unit, two
only across disjoint write sets. These eight do not split. The loop-kit and the driver fixes both
re-price rows of `tools/run-gates/selftest-budgets.txt`, so their write sets meet.

Write the spec of that one unit, `KICK-dKeptSession-79`, as a new Tier-2 spec in this build's
`spec/` folder. It closes M1 to M5 and L1 to L3, each by the fix the report states.

### brief:items

1. M1, `agent-output-interpolated-into-an-instruction`:
   - Validate a fetched mail record in ONE place, the driver's `read_mailbox` `flush()`
     (`tools/unattended/unattended.sh#read_mailbox`).
   - Drop a record whose id is not 12 lower-case hex digits, whose kind is outside the loop kit's
     closed mail set, whose build fails the slug shape, or whose build differs from its ref's slug
     segment.
   - Arm: a fixture remote carrying a planted record, with `position.py <slug> --mail-interrupts --local`
     printing no line with its text. Observed RED first against the current reader.
2. M2, `destructive-step-before-its-precondition`: in `tools/loop/loop_transition.py#write_transition`,
   compute the whole move before the ack write.
   - The move covers `derive_move`, the patch hold, the witness checks, the field loop, the tree
     verdict, the composition, `derive_move_scenarios` and the VALUE check.
   - Only then run `write_consumed_acks` and the MailHeld raise.
   - Add one plant per refusal class (a bad witness, a derived `--field`, a scenario conflict). Each
     asserts no ack commit lands and the row still reads open.
3. M3, `concurrency-is-not-a-budget`: the skeptic's corrected fix.
   - On a fetch that does not rewrite the stamp, `print_mail_notice` leaves `<stamp>.fetching` with
     its mtime at the attempt.
   - `tools/unattended/mail-notice.js` spawns nothing while that marker is younger than
     `mailbox.fetch-seconds`.
   - The 2*seconds stale-marker removal is kept only past that age.
   - Arm: two hook calls inside fetch-seconds after a failed fetch, and the second spawns nothing.
4. M4, `a-new-local-collides-in-a-long-function`:
   - Rename the notify.owner pair in `write_transition`, so the composition's `unread` cannot shadow
     it.
   - Add a plant: a pinned composition whose compose fails, with notify.owner selecting
     `transition`. Its `progress —` line prints, and no `progress · unread` line names the
     composition's cause.
5. M5 and L2, `observed-by-claim-no-arm-discharges`. Two suite arms in
   `tools/unattended/unattended.test.sh`, each with its floors raised from the figure read at the
   build base:
   - the card binding of `mail-notice.js` (`readCardBuild`): a card file names the build, no RUN.md
     session fact exists, and logging `git` and `bash` stubs stay empty;
   - the detached spawn's argv and `windowsHide: true`, through a recorder in place of
     `child_process.spawn`.
6. L1: correct the `measure_context_fill` docstring and the runlog README to `(share, window, source)`.
   That is the shape the code returns and both callers read.
7. L3: rewrite the `mail-notice.js` header so it agrees with its registration.
   - The registration's matcher is `*` and the hook is the only carrier of the unread-mail line.
   - KICK-dKeptSession-44 is CLOSED and frozen, so its S6 wording is not amended. Say so in §3 and
     cite this unit's text as the current statement.
8. The left-shift owed by each finding:
   - Two classes are NEW: `docstring-misnames-a-returned-value` and
     `header-rationale-contradicts-the-registration`. Each becomes a bug-class record under
     `memory/gotchas/`, with its map claim and `gotchas.py --write`, as this repository's left-shift
     practice requires.
   - The other classes already exist. Their new arms are the gate.
9. Budgets: the `loop transition record` leg's 120 s ceiling (PINNED 2026-11-23, tools/gate-legs.json)
   is the owner's parked decision. This unit re-prices its rows from measured readings, never stops
   on that ceiling, and never edits `tools/gate-legs.json`.
10. Write `Files touched` as the complete write set, each path tied to its clause. Include
    `tools/run-gates/selftest-budgets.txt`, and every help page and verbs-guide copy a changed
    behaviour reaches. Leave out `memory/DECISIONS.md` and `.memory-tree.conf`, which check 49
    refuses to a pass.
11. Header: Tier-2, `order 37` (one past KICK-dKeptSession-65's 36), streams kickoff, advancing
    KICK-dKeptSession-29 as its siblings do.
    - Carry no clause: a promotion derives from the review, not the packet.
    - Each `New arm:` line names its RED-first staging.
    - Cite code by `path#symbol`, and pin every figure with DERIVED or PINNED on its own line.
    - Keep within the live-spec size cap, and leave no fork open.

### brief:acceptance

These all report nothing for the new spec:
- `bash tools/memory-tree/check-memory-hygiene.sh --only 12,25 --spec <path>`
- a plain `bash tools/memory-tree/check-memory-hygiene.sh --only 2`
- `python tools/check-spec-tokens.py --spec <path>`
- a PLAIN `python tools/playbook/writing_practice.py check pinned-facts`
- `bash tools/unattended/unattended.sh --check-specs dKeptSession KICK-dKeptSession-79`

### brief:gates

Only these: the memory hygiene gate (`--only 12,25 --spec`, and `--only 2`), the spec-token checker,
the pinned-facts check and the driver's `--check-specs`.

### brief:non-goals

- No product code, no commit and no index render.
- No spec other than KICK-dKeptSession-79's. Read the others freely; edit only the new spec, in the
  run worktree.

### task:reuse

each spec's §10 names its seam; probes run: `reuse_lookup.py` per spec at re-ground; recall terms below.

### card:route

- build: dKeptSession
- unit: KICK-dKeptSession-65 · spec memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-65.md
- brief: memory/builds/dKeptSession/prompts/2026-11-21-prompt-KICK-dKeptSession-65-build-brief.md
[/memory/builds/dKeptSession/prompts/2026-11-23-prompt-KICK-dKeptSession-79-1-spec-writer.md]
