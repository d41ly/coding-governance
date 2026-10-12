# TOOL-aOrientedCast-6 — acceptance ledger

**Serves:** journal TOOL-aOrientedCast-6

Direct checks only: under the owner's rule for this run no gate, suite, slice or self-test ran in
this pass. What ran: a hand probe in the run's scratch directory that builds its own repository with
a linked worktree, a `.memory-tree.conf`, two specs, two cards and four role-index states, and pipes
28 hand-built `PreToolUse` payloads into `node tools/hooks/scratch-guard.js`, reading the exit code
and stderr of each; one payload against this repository for AC5; probes of the new suite helpers'
pieces (the `run_edit` payload builder, the two flip `sed`s, the `render_task_section` extraction)
outside the suite; parse-only checks (`bash -n`, `node --check`); and the lexicon. RED first: the
same 28 payloads against the parent's hook (`git show HEAD:tools/hooks/scratch-guard.js`) failed
all 16 refusals, each exiting 0 where the arm wants 2, and passed the 12 admissions; against the
pass's hook all 28 passed. The 24 new `run_edit` arms of `scratch-guard.test.sh` (§7's new arm,
covering AC1 to AC4 over the suite's own fixture) and AC6's change to the AC10 fold arm were not run
and are owed to the main loop under `scratch-guard self-test`; `FLOOR_ASSERTIONS` moved 236 to 260
by a hand count of those arms, not by a run.

**Evidences:** TOOL-aOrientedCast-6
- AC1 — `node tools/hooks/scratch-guard.js` — on a `Write` to `mem/builds/bx/spec/` with the probe's `roles.json` naming `gov-spec-writer` as spec and `gov-builder` as product, `agent_type` `gov-spec-writer` exited 0 with empty stderr; no `agent_type`, `workflow-subagent` and `gov-builder` each exited 2 naming `gov-spec-writer`, the index path and `handoff.py render` with `--build bx`.
- AC2 — `gov-builder` — on a `Write` under the probe's `ROUTED_PATHS` entry with a card routing a Tier-2 unit at `INPROGRESS`, `gov-builder` exited 0; no `agent_type` and `gov-spec-writer` each exited 2 naming `gov-builder`; `gov-builder` with a card holding no route exited 2 with the `## route` refusal.
- AC3 — `**Status:**` — the main loop's `Edit` of the status cell, its `Write` of the file with only the status and date cells changed, and its `MultiEdit` of status and date each exited 0; a `gov-builder` `Edit` of its routed spec `INPROGRESS` to `CLOSED` exited 0 and the same edit to an unrouted spec exited 2; the main loop's `Edit` of the `rev-` cell, a `Write` moving the section 2 line beside the status, a `MultiEdit` whose `old_string` the file does not hold, and a `workflow-subagent` flip each exited 2.
- AC4 — `roles.json` — with no index the main loop's spec `Write` and its product `Write` over a buildable route exited 0; with the index holding `{` both exited 2 naming the index and `is not JSON`, and a `Write` to the build's `README.md` exited 0; with an index naming no spec role a spec write exited 2 naming `UNARMED` and the spec class, and a `gov-builder` product write exited 0. An index whose role carried `agent: "yes"` exited 2 as not the shape.
- AC5 — `CLAUDE_PROJECT_DIR` — set to this worktree, a `Write` payload with no `agent_type` targeting a new spec file, numbered past the build's last unit, under `memory/builds/aOrientedCast/spec/` exited 2 naming `gov-spec-writer`, this repository's `.claude/roles.json` and `handoff.py render --role gov-spec-writer --build aOrientedCast --part task`; no file was written.
- AC6 — owed to the main loop — `render_task_section`: the AC10 fold arm now takes its `## task` from `render_task_section` beside `$SG_WRITER` (or the `SG_WRITER_BASE` blob) with the `README.md:1` row under `## read`; the RED-at-`8bf164d40` and GREEN-after observation through a slice is not run in this pass, and `scratch-guard self-test` at the close observes the arm's `ok   AC10` lines. The extraction alone was probed: it yields the three-line definition from the working copy and from `HEAD`, and the eval'd helper prints a `## task` section.
