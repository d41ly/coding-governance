**Serves:** journal TOOL-aCarriedStop-10

# gov-builder handoff — TOOL-aCarriedStop-10

<!-- gov:handoff role=gov-builder build=aCarriedStop unit=TOOL-aCarriedStop-10 path=memory/builds/aCarriedStop/prompts/2026-11-14-prompt-TOOL-aCarriedStop-10-2-builder.md role-sha=8fbf0460794b task-sha=e97cd4057f9b -->

## Role

[.claude/agents/gov-builder.md · Level 5 · This role's static instructions; yields to levels 0 to 4]
You are a software engineer building ONE unit of a larger build: the one your task names, from its
spec. You are not designing in this pass: the spec is the design and you follow it. You are not
running any gate either: gates are the main session's, at the merge or push threshold.

Read the spec whole before you touch code, and the brief your task names. Where the code and the
spec disagree, the spec is not yours to rewrite: return without a commit, naming what in the spec is
wrong and what you found, and whoever dispatched you has the spec revised. A divergence is reported,
never resolved by editing the spec or by building the intersection.

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
- build: aCarriedStop
- unit: TOOL-aCarriedStop-1 · spec memory/builds/aCarriedStop/spec/2026-11-13-spec-TOOL-aCarriedStop-1.md
- unit: TOOL-aCarriedStop-2 · spec memory/builds/aCarriedStop/spec/2026-11-13-spec-TOOL-aCarriedStop-2.md
- unit: TOOL-aCarriedStop-3 · spec memory/builds/aCarriedStop/spec/2026-11-13-spec-TOOL-aCarriedStop-3.md
- unit: TOOL-aCarriedStop-9 · spec memory/builds/aCarriedStop/spec/2026-11-14-spec-TOOL-aCarriedStop-9.md
- unit: TOOL-aCarriedStop-10 · spec memory/builds/aCarriedStop/spec/2026-11-14-spec-TOOL-aCarriedStop-10.md
- brief: memory/builds/aCarriedStop/prompts/2026-11-13-prompt-TOOL-aCarriedStop-1-brief.md
[/.claude/orientation-card.md]
[memory/builds/aCarriedStop/prompts/2026-11-14-prompt-TOOL-aCarriedStop-10-2-builder.md · Level 6 · The task: this unit's goal, scope and acceptance; yields to levels 0 to 5]
This handoff is for build `aCarriedStop`, unit `TOOL-aCarriedStop-10`.

### input:spec

memory/builds/aCarriedStop/spec/2026-11-14-spec-TOOL-aCarriedStop-10.md

### card:route

- build: aCarriedStop
- unit: TOOL-aCarriedStop-1 · spec memory/builds/aCarriedStop/spec/2026-11-13-spec-TOOL-aCarriedStop-1.md
- unit: TOOL-aCarriedStop-2 · spec memory/builds/aCarriedStop/spec/2026-11-13-spec-TOOL-aCarriedStop-2.md
- unit: TOOL-aCarriedStop-3 · spec memory/builds/aCarriedStop/spec/2026-11-13-spec-TOOL-aCarriedStop-3.md
- unit: TOOL-aCarriedStop-9 · spec memory/builds/aCarriedStop/spec/2026-11-14-spec-TOOL-aCarriedStop-9.md
- unit: TOOL-aCarriedStop-10 · spec memory/builds/aCarriedStop/spec/2026-11-14-spec-TOOL-aCarriedStop-10.md
- brief: memory/builds/aCarriedStop/prompts/2026-11-13-prompt-TOOL-aCarriedStop-1-brief.md

### brief:non-goals

Everything the spec's §3 lists, and any file the spec does not name. Any kit version, which the lander's mint moves. Any path under `memory/builds/dDeclaredLoop/` or `memory/builds/aBatchedPacket/`.

### input:code

# Brief — aCarriedStop: build unit 10, the chain-packet door's kit-path spellings

**Serves:** research TOOL-aCarriedStop-10

## The brief

### Goal
Build `TOOL-aCarriedStop-10` as its spec states it. The design is `memory/builds/aCarriedStop/spec/2026-11-14-spec-TOOL-aCarriedStop-10.md`, read whole; this brief adds nothing to it.

### Items
1. Build every Scope item of the spec's §2, in the files its §4 names.

### Acceptance
1. Each criterion of the spec's §6 that the spec assigns to the builder is observed in the pass and named in the return.
2. Each criterion the spec assigns to the main loop is named in the return as owed.

### Gates
`bash tools/check-install-prefix.sh` in the pass. The merge bar runs once, at the close.

### Non-goals
Everything the spec's §3 lists, and any file the spec does not name. Any kit version, which the lander's mint moves. Any path under `memory/builds/dDeclaredLoop/` or `memory/builds/aBatchedPacket/`.

### Limitations
- No suite, self-test or bar runs in the pass, and every command is bounded under five minutes.
- The spec is not edited beyond its status header at the build commit; a divergence is returned, not built.
- The pass commits once, after the spec commit, with a subject naming `TOOL-aCarriedStop-10` and a final trailer block holding `Pass: TOOL-aCarriedStop-10` beside the charter's `Co-Authored-By:` line.
- The pass commit carries `memory/builds/aCarriedStop/RUN.md` as staged, and the acceptance ledger `memory/builds/aCarriedStop/build/2026-11-14-build-TOOL-aCarriedStop-10-1-acceptance-ledger.md` in the grammar `memory/HYGIENE.md` states under "Acceptance ledger".
- The CLOSED flip of the spec header is in the same pass commit.

### Reuse
The seam the spec's §10 names.
[/memory/builds/aCarriedStop/prompts/2026-11-14-prompt-TOOL-aCarriedStop-10-2-builder.md]
