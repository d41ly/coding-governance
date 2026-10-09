# TOOL-aRoutedQuill-2 — acceptance ledger

**Serves:** journal TOOL-aRoutedQuill-2

No merge bar and no self-test suite ran in this pass. The suite's new write-gate block ran as a
scratch slice on node a: the suite's prologue, its orientation-fixture prologue with `run_card` and
`check_stderr`, then the block alone. Against the built hook it printed 49 `ok` lines, the fixture
line and all 48 new assertions. Against the base hook, copied out of `HEAD` before the pass, only 15
held: the fixture lines and the allow near-misses. Every deny arm and every `readConfKey` arm was
red. The block cost about 95 s of the slice's 100 s on a contended node. The close still owes
`scratch-guard self-test` run whole, with its raised `FLOOR_ASSERTIONS` of 212 and its 220 s
ceiling, plus `agent-cap self-test`, `check-wiring self-test` and the other legs §7 names.

**Evidences:** TOOL-aRoutedQuill-2
- AC1 — `W-AC1` — a Tier-2 spec at INPROGRESS and a Tier-1 spec at SPECCED dated after the fixture's `SPEC_TIER1_CUTOFF` each exited 0 with empty stderr. A Tier-2 spec at SPECCED exited 2 naming the unit, `Tier-2` and `INPROGRESS`. A Tier-1 spec at SPECCED dated before the cutoff, and one under a blank key, each exited 2 naming `SPEC_TIER1_CUTOFF`. A route of two units, the first unbuildable, exited 0. Base: every deny exited 0.
- AC2 — `W-AC2` — an absent card exited 2 naming the card path, the session id and `--card --write --session`. A card with no `## route` exited 2 naming `## route` and `/session-kickoff`. A missing spec, a spec outside `builds/bx/spec/` and a spec whose H1 names another unit each exited 2 naming the unit and the reason. A replay-written card routing a buildable unit exited 0. Base: every deny exited 0.
- AC3 — `W-AC3` — a target under the temp root and no repository, a product path in a second `git init` declaring `ROUTED_PATHS`, and the session repository's `docs/` each exited 0 with empty stderr over an unrouted card. The linked worktree's product path with `CLAUDE_PROJECT_DIR` the primary exited 2, and so did the same write with `CLAUDE_PROJECT_DIR` empty and the payload `cwd` placing the session.
- AC4 — `W-AC4` — a backslashed target, upper-case segments, a relative `file_path`, `notebook_path` on `NotebookEdit`, `file_path` on `MultiEdit` and on `Edit`, and the file entry itself each exited 2 over an unrouted card. `toolsx/` beside `tools/`, `app.mdx` beside `app.md` and a `Read` each exited 0 with empty stderr.
- AC5 — `W-AC5` — `ROUTED_PATHS=""` exited 2 naming `UNARMED`, `ROUTED_PATHS` and the conf, for a product and a non-product write alike, and an `Edit` of the conf exited 0. A blank `MEMORY_ROOT`, an entry `../up/` and an entry `mem/` covering `MEMORY_ROOT` each exited 2 naming `UNARMED`. With no conf the write exited 0 with one witness line naming the absent `.memory-tree.conf`.
- AC6 — `W-AC6` — a payload with neither path field exited 2 naming both fields. A relative `file_path` with no `cwd` exited 2 naming the field and the missing cwd. A conf path that is a directory exited 2 naming the conf and that it cannot be read. A throw staged at the top of `checkRouted` exited 2 with `the write gate threw (staged) and fails closed`.
- AC7 — `W-AC7` — a payload carrying `agent_id` and the parent's `session_id` exited 0 on a buildable route and 2 on an unrouted card.
- AC8 — `python tools/settings-merge.py --check --fragment tools/hooks/scratch-guard.fragment.json` — after the rewire it exited 0. `.claude/settings.json` holds `scratch-guard.js` once under PreToolUse, under `Bash|PowerShell|Edit|Write|MultiEdit|NotebookEdit`, and `gate-guard.js` alone under `Bash|PowerShell`. `bash tools/check-wiring.sh --check` printed `ok       scratch` naming the widened matcher. Its own exit is UNOBSERVED: the run was cut at 110 s with no other red line printed.
- AC9 — `node -e` — `readConfKey` over this repository's `.memory-tree.conf` read `ROUTED_PATHS` as `tools/ skills/ coding-governance-agents.template.md WIRE-INTO-PROJECT.md`. A `Write` of `tools/hooks/README.md` here, under a session id with no card, exited 2 naming the absent card and `--card --write --session`. The same write under this run's session, whose card routes this unit, exited 0.
- AC10 — `W-AC10` — `readConfKey` read the last of two assignments, an `export` prefix, both quote styles, a comment behind whitespace, a `#` glued to a bare word, a blank value as blank, a whole-key match and `K.Y` as a plain string, each as the shell does. Base: the function did not exist. A scratch probe ran base's and the tip's `readSpecAuditDefault` over the nine `SPEC_AUDIT_DEFAULT` spellings `agent-cap.test.sh` writes, plus three more, and every verdict was the same.
