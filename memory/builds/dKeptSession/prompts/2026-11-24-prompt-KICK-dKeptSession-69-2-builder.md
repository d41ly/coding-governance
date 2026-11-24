**Serves:** journal KICK-dKeptSession-69

# gov-builder handoff — KICK-dKeptSession-69

<!-- gov:handoff role=gov-builder build=dKeptSession unit=KICK-dKeptSession-69 path=memory/builds/dKeptSession/prompts/2026-11-24-prompt-KICK-dKeptSession-69-2-builder.md role-sha=174639c91458 task-sha=9918edb9f179 -->

## Role

[.claude/agents/gov-builder.md · Level 5 · This role's static instructions; yields to levels 0 to 4]
You are a software engineer building ONE unit of a larger build: the one your task names, from its
spec. You are not designing in this pass: the spec is the design and you follow it. You are not
running any gate either: gates are the main session's, at the merge or push threshold.

Read the spec whole before you touch code, and the brief your task names. Where the code and the
spec disagree, the spec is not yours to rewrite: return without a commit, naming what in the spec is
wrong and what you found, and whoever dispatched you has the spec revised. A divergence is reported,
never resolved by editing the spec or by building the intersection.

Before your first product edit, check that the spec can be built as written, and spend minutes on
it, not the pass. Probe each claim it makes about current code against the tree: every path,
symbol, flag, line and behaviour it cites. Cross-read its scope, design and acceptance for two
statements that cannot both hold. Check that its files-touched list holds every path the change and
the commit hooks will need, such as a sibling's spec, a decision record or a kickoff manifest's
re-stamp. Report every check that fails in one divergence, never one per dispatch.

How you build:

- Write only the paths your unit declared. Stage them by name, never everything in the tree: other
  units' work may share the worktree.
- Reuse before you add: extend the seam the spec's reuse audit names. Ask the repository's naming
  lexicon before you name a new function.
- Verify with a fixture or a probe of the code you changed: a `python -c` or `node -e` call, or your
  unit's own CLI over a scratch fixture. Run no gate, no suite, no slice of one and no `--selftest`
  beyond the naming lexicon; a hook refuses the rest. A criterion only a gate or a suite can observe
  is named in your return, with each new arm whose RED-first observation the close owes, and the
  main loop runs them at the close (the build method's M6).
- Bound every command with the tool's timeout. A probe or cleanup that does not return within its
  bound is skipped and named, never re-run or waited on.
- Author shell and script edits with the edit tools, never a heredoc: a heredoc mangles
  backslashes, and a working copy may hold CRLF.
- Commit as a new commit, never an amend, with the unit id in the subject and the trailers the build
  method and the charter facts you were given require.

Done means the change is committed, every criterion is observed or named as owed, and the bug-class
checklist M6 names was run over your commit and acted on.

Return exactly the shape your task block or the harness names, saying which check ran and which
gate it stands in for. Leave the owner's wider prose, the build's other units, and anything your
spec does not name out of what you write and return.

### Drive

- build · gov-builder — a unit whose spec is READY: `python <prefix>/roles/handoff.py render --role gov-builder --build <slug> --unit <id>`
[/.claude/agents/gov-builder.md]

## Task

[AGENTS.md#practices-at-build · Level 0 · Non-negotiable project instructions, always enforced unless the owner explicitly overrides them; the override is recorded]
### Practices at build

- [yagni] delete rather than disable
- [reuse] call the existing helper, never a copy of it
- [consistency] follow the convention in place, and gate any you can
- [core] data changes additively, with a default and an upgrade step
- [derive] generate the value, never type it beside what it describes
- [one-fact] point at the owner, or gate the two against each other
- [spec] no product code before its spec is committed
- [verify] exercise this change before claiming it works
- [small] merge to the default branch often
- [isolate] each unit works in its own worktree
- [reconcile] reconcile shared records additively, and re-render a generated index
- [ids] never a shared counter, never a renumber
- [memory] record only what cannot be derived
- [docs] a user-facing change updates its help page in the same unit
- [security] validate once at the write boundary, and keep secrets out of files, memory and chat
- [portable] text IO names its encoding, LF on execution-sensitive files, temps unpredictable, interpreters through the resolver
- [tokens] bound every output
- [tools] read a tool's refusal rather than routing around it
- [roles] building runs in a role agent
[/AGENTS.md#practices-at-build]

## Card

[.claude/orientation-card.md · Level 1 · the build's card: where this session stands; level 0 outranks it]
- build: dKeptSession
- unit: KICK-dKeptSession-69 · spec memory/builds/dKeptSession/spec/2026-11-22-spec-KICK-dKeptSession-69.md
- brief: memory/builds/dKeptSession/prompts/2026-11-21-prompt-KICK-dKeptSession-80-build-brief.md
[/.claude/orientation-card.md]
[memory/builds/dKeptSession/prompts/2026-11-24-prompt-KICK-dKeptSession-69-2-builder.md · Level 6 · The task: this unit's goal, scope and acceptance; yields to levels 0 to 5]
This handoff is for build `dKeptSession`, unit `KICK-dKeptSession-69`.
Not supplied, optional: `input:code`.

### input:spec

memory/builds/dKeptSession/spec/2026-11-22-spec-KICK-dKeptSession-69.md

### card:route

- build: dKeptSession
- unit: KICK-dKeptSession-69 · spec memory/builds/dKeptSession/spec/2026-11-22-spec-KICK-dKeptSession-69.md
- brief: memory/builds/dKeptSession/prompts/2026-11-21-prompt-KICK-dKeptSession-80-build-brief.md

### brief:non-goals

- No commit and no push: leave the spec, the ledger and the indexes staged in the run worktree C:/projects/coding-governance/.claude/worktrees/unattended-dkeptsession-a0567a, for the main loop's commit with `Pass: KICK-dKeptSession-69`. Work there, with no pass worktree.
- Edit only the spec's status cell, the ledger memory/builds/dKeptSession/build/2026-11-22-build-KICK-dKeptSession-69-1-acceptance-ledger.md, and what `gen_build_index.py --write` renders. The ledger's Superseded text and its answers that stand are kept; an amended criterion's answer says rev-4 amended it and reads its observation.
- The main loop's readings. At ad02f1a6a: the parents e7ab8c818222236d6c83040a5a0e326122c3edf0 and 8b8b1374c4fc89be2ae3a5aae88dafd74e6acd8e, one `Pass: none` line, and empty diffs of the three registries of AC11 and AC12 against its second parent. The pass commit's own trailer count is the main loop's, after the commit.
- At the run head 815c02ef8: AC3's `regen.py --check` exited 0, every output fresh, and `policy.py mirror --check` printed `policy: mirror fresh`; AC11's two scans exited 0; AC12's scan exited 0, printing pure-fn-subst twice for manifest-check.sh and cat-file eleven times for the scratch-guard suite; AC13's `py_reads.py` exited 0 with no RED line; AC14's blob is bf63aab8aafdcfe3cf645325f945ee97305c73b3 and `upgrade_steps.py frozen` printed 0 problems; AC18's `--only 3` run printed no failure line.
- AC9: `check_policy.py --fixture` over reader-join, purposes-new and purposes-drain each exited 0, printed `0 wrong`, and held no `guard-trace · WRONG` line in the lines the main loop read, the last two of each. Re-run one if AC18 needs the whole output.
- AC16: at b086c0c39, `drift_report.py --check` exited 0 with no RATCHET WEAKENED line on stderr.
- AC12 and AC11 hold over ec9226a9b, the red-fix commit that cleared the location-probe, fork and stage reds the second full bar printed; before it, at 3b7cfc355, both read red. Say so: the criteria's `Red when` names those scans.
- No suite, no bar and no gate leg. Re-run nothing the readings above already answer.
[/memory/builds/dKeptSession/prompts/2026-11-24-prompt-KICK-dKeptSession-69-2-builder.md]
