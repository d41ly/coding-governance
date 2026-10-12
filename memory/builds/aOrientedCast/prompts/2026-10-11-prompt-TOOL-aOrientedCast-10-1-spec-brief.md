**Serves:** journal TOOL-aOrientedCast-10 TOOL-aOrientedCast-11

# Spec handoff — the owner's two added features

## Role

You are a code architect writing the specification for two units of a larger build. You are not
writing any code right now. A builder will later build from your spec alone, and a reviewer will
hold the diff to it, so the spec is the design. Make each unit functional, concise and flexible,
and seam it into the code that already exists rather than beside it. Verify every claim about
current code by reading that code, and cite it by path and line. A choice you cannot derive is a
fork with options and a recommendation; under this run's mandate you resolve it by M3 of the build
method and mark it `RESOLVED (agent, 2026-10-11, delegated)`. You run no gate and no self-test.
The only checks you may run are memory hygiene and the lexicon: make your specs pass those, and
nothing else. You write only the two spec files. You do not commit, and you do not regenerate any
index.

## Task

**Repository:** `C:/projects/coding-governance/.claude/worktrees/deterministic-attended-workflows-943570`.

**Read first:**
- `memory/builds/aOrientedCast/prompts/2026-10-11-prompt-TOOL-aOrientedCast-10-0-owner-addendum.md`:
  the owner's words. They are the mandate for these two units.
- The section "Pinned interfaces" of
  `memory/builds/aOrientedCast/prompts/2026-10-11-prompt-TOOL-aOrientedCast-1-1-spec-brief.md`, and
  its "Invariants for every unit", which bind you except where this handoff says otherwise.
- `memory/guides/BUILD-METHOD.md`.
- The specs of TOOL-aOrientedCast-1, -3, -4, -5 and -8 (all CLOSED), and of -6 and -7 (OPEN, built
  after you): your units extend what those built or will build.

**Files:** `memory/builds/aOrientedCast/spec/2026-10-11-spec-TOOL-aOrientedCast-10.md` and `-11.md`.
Both are Tier-2, status `OPEN`, `rev-1`, `node a`, base `646d4a73581393acbf42f33864a9808c96d00a0c`,
`streams tooling`. TOOL-aOrientedCast-10 is `order 8`, and TOOL-aOrientedCast-11 is `order 11`.

### TOOL-aOrientedCast-10 — every role runs at its declared effort, from one owner-editable config

- **The config.** One file in the roles kit, shipped to adopters as govkit role `seed`, so an owner's
  edit survives an update. It carries:
  - a `default` effort, `medium`, for any role it does not name;
  - one entry per role or workflow stage;
  - the vocabulary Claude Code's agent front matter accepts for `effort` (verify it; the Agent tool
    names `low`, `medium`, `high`, `xhigh` and `max`).

  The checker refuses an unknown value or an entry naming no role.
- **The owner's defaults:**

  | Who | Effort |
  |---|---|
  | generic agent | `medium` |
  | prompt writers | `xhigh` |
  | spec writers | `xhigh` |
  | spec reviewers and their workflows | `medium` |
  | code builders | `high` |
  | Tier-2 diff and closing reviews | `high` |

- **Where it reaches agents.** `render_agents.py` writes `effort:` into every rendered agent type, so
  an `Agent` spawn and a `Workflow` `agent()` given `agentType` both carry it.
- **Two forks to resolve.**
  - "Prompt writers" names no catalogue role. Decide whether it is `gov-orienter` and `gov-session`,
    or a new role. A new role also needs a workflow row and a renderer path.
  - `gov-skeptic` and `gov-synthesizer` serve both spec review (`medium`) and closing review
    (`high`). Decide between a per-stage effort the harnesses pass through `agent()` options, which
    holds only if the Workflow runtime accepts an effort option, and per-workflow role types. If
    the runtime question decides it, make it a FACT-QUESTION with a probe, which may read but not
    build.
- **Its own check.** The render's existing `--check` and `--selftest` cover the new key. The
  builder observes with fixtures, never with a gate.

### TOOL-aOrientedCast-11 — a role agent runs no gate, and the hooks enforce it

- **The rule.** No call carrying an `agent_type` may run:
  - a gate-leg command, matching the argv of any leg in `tools/gate-legs.json` after its tokens
    resolve;
  - the bar runner, in any form;
  - the self-test runner;
  - any `*.test.sh`, `selftest.py` or `--selftest` invocation;
  - the unattended gates runner.

  The only exceptions are per role: a `spec` writer may run the memory hygiene gate and the lexicon,
  a `product` writer may run the lexicon, and every other role runs none. The allowlist lives in
  the same config TOOL-aOrientedCast-10 creates, so the owner adjusts both in one place.
- **Where it is enforced.** A Bash and PowerShell PreToolUse arm. Read `tools/unattended/gate-guard.js`,
  which already denies flagged gates and self-test suites before VERIFYING inside a run but allows
  everything in an attended session, and `tools/hooks/scratch-guard.js`, which already dispatches
  on `agent_id`. Choose the seam by M3, and say what the other one keeps. The arm reads the role's
  allowlist from `.claude/roles.json`, so the hooks kit names no sibling kit by literal.
- **Its ceiling, stated in its header.** Textual matching cannot see a gate reached through an
  interpreter or an alias. The push-boundary bar is still the guarantee.
- **The texts that hand agents their work must say the same.** Name every one and change it in this
  unit:
  - the role blocks of `gov-builder`, `gov-spec-writer` and the review roles;
  - the harness prompts in `unattended-unit.js` and `unattended-build.template.js`, which today
    order "a checker run on a staged break, a `--selftest` flag";
  - the build method's M6 sentence saying the same.

  The build method is a governance carrier changed by the owner's instruction, so say so in §3.
- **The consequence to design for.** Red-first observation of a gate arm moves to the main session
  at the merge or push threshold. Say how a pass then verifies its change with fixtures or probes
  of its own code, and how the main loop records the red-first observation of each new arm at the
  close. Point at the M8 close rather than inventing a new record.
- **Order.** It builds last, after TOOL-aOrientedCast-6 and -7, because all three edit the hooks.

**Return:**
- `authored`: the two paths;
- `forks`: each fork with the option taken;
- `refused`: anything you could not specify, with why;
- the exit status of the memory hygiene check over your two files, if you ran it.
