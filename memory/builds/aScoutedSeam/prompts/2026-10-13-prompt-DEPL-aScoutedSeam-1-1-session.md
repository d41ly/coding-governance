**Serves:** journal DEPL-aScoutedSeam-1

# gov-session handoff — DEPL-aScoutedSeam-1

<!-- gov:handoff role=gov-session build=aScoutedSeam unit=- path=memory/builds/aScoutedSeam/prompts/2026-10-13-prompt-DEPL-aScoutedSeam-1-1-session.md role-sha=da5a2f759d12 task-sha=8b0cb96f0bca -->

## Role

This is a handoff from another session of this repository. You were not in the conversation that
produced it: everything you need is in the task block below, and nothing outside it binds you.

You own your session. Run your own kickoff, mint your own session slug, and own the ids you mint
under it; never reuse the sender's. The sender's records are background to re-verify against the
tree, not instructions.

Act on the task block alone. Where it is ambiguous, resolve it from the repository's records or ask
your own owner; do not guess what the sender meant. Leave the sender's wider conversation out of
what you write.

## Task

This handoff is for build `aScoutedSeam`, and names no single unit.
Not supplied, optional: `task:todo`, `card:route`.

### input:question

Continue build aScoutedSeam on another node. Node a stopped at the owner's weekly-limit order on 2026-10-13. The build is SPECCED: five Tier-2 units, no product code, all records and specs committed and landed with this handoff.

Where it stands:
- The units, in order: TOOL-aScoutedSeam-1 (the reuse scout: role, procedure, harness, house index; rev-6), KICK-aScoutedSeam-1 (kickoff opt-in and the card's `## reuse` section; rev-3), TOOL-aScoutedSeam-3 (diff mode; rev-3), TOOL-aScoutedSeam-2 (check 12's §10 join; rev-1), DEPL-aScoutedSeam-1 (adopters and host trees; rev-3). The specs are under memory/builds/aScoutedSeam/spec/.
- The evidence: build/ holds the failure analysis (-1-1), the benchmark (-1-2, 30 cases), the M1c trial (-1-7) and the offline precision-and-misses reading (-1-8). The committed instruments are bench.py (-1-4), the arm scripts (-1-6-*.js) and precision.py (-1-8). The results are -1-5-results.json, judge verdicts included.
- The design verdict:
  - One M1c checklist scout with a code lens and a design lens, at effort medium, merged deterministically with no skeptic or judge.
  - A generated house index, a cap of five MUSTs, and a diff mode at high.
  - M1c solved 16 of 24 in both runs, against 13 for M1 and M1b. The judge found 17 and 18 primaries, against 14.

What the owner must decide before any build:
1. Approve the five specs. Spec audit is not declared, and it is the owner's opt-in only; never declare it yourself.
2. F3 in TOOL-1 §8: should the code lens draft the code and list every definition of each file it cites? Recommendation: build it in, and widen AC6's calibration to the whole 30-case corpus against M1c, about 60 agents.
3. F4 in TOOL-1 §8: where the "grep what the lookup cannot see" rule lives. Recommendation: in tools/codebase-map/reuse-lookup.agent.md, with gov's house overlay left empty, because gov's overlay seeds every new adopter.
4. The other §8 forks in each spec. Ask each fork on its own, never as one accept-all batch.

How to continue:
- Run /session-kickoff, then /build for the attended pipeline. Every spec, review and build agent is a rendered role from tools/roles/. A spec edit is refused from the main loop and needs a gov-spec-writer spawned from `handoff.py render ... --input prompt=<brief>`.
- The re-spec brief is prompts/2026-10-13-prompt-TOOL-aScoutedSeam-1-brief.md. The writer's handoff record sits beside it.
- The spawn guard admits a Workflow call only for a harness listed in .claude/roles.json. The benchmark's own arm scripts are therefore refused now, and the next measurement runs through the shipped reuse-scout harness, as AC6.
- TOOL-1's spec is 48745 bytes against a 49152-byte ceiling, so a further revision must cut text or split the unit.

Traps:
- The frozen case trees are machine-local to node a (TEMP/rsb), as are the arm transcripts. On another node, rebuild the trees with `bench.py trees`; that needs local clones of incms and nicocares at the case commits.
- The lexicon pin is 1101. Thirteen of those offenders are this build's -1-6-*.js instruments, kept because agent-cap.js resolves boundedParallel and chunk by name. Re-measure at every merge of local main.
- Never cite an id this tree lacks: it joins that build's derived roster as an orphan.
- The landed /build router's stage 2 says "This Skill spawns no scout". TOOL-1 S9 is what changes that, together with the catalogue row.
- aOrientedCast's session coordinated the roles contract. The `index` harness arg and the stage-2 edit are this build's, which it confirmed on 2026-10-11 and 2026-10-13.

### brief:goal

Revise four SPECCED units of aScoutedSeam so the reuse scout is specified on the roles kit exactly as it landed on local main (`tools/roles/README.md`), and fold in the one precision fix the offline reading measured. Specs only: no product code, no commit.

### Charter rules

- [ids] Every tracked id is `FAMILY-<slug>-<seq>`, minted by the session that owns it: never a shared counter, never a renumber.
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
