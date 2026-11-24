**Serves:** journal TOOL-dBoundRoles-51

# Resume brief — the dBoundRoles build run, moved from node d to node a

The owner moved this unattended run to node a on 2026-11-23. Node d held it with `--hold --code host-owner-action
--until owner` and reaped its keepalive. Nothing else holds the run, so a `--resume` from node a takes it over. Read
this brief whole, then the charter, then `memory/guides/UNATTENDED-PROTOCOL.md` and `memory/guides/BUILD-METHOD.md`.

## Where the run stands

- Branch `branch/unattended-dboundroles-62c3df`, pushed to origin. Its tip is the commit that records the hold; its
  parent `760ca206c` is the hold's witness. The build run's BASE is `8b8b1374c`.
- Every roster spec up to build order 30 is CLOSED. The last unit built is TOOL-dBoundRoles-51 at `06aa7cdff`, merged
  at `a098e47cf`, its closing records at `760ca206c`.
- Still DEFERRED, in build order (DERIVED at `760ca206c` from each spec's status cell): 56 and 57 at order 31, 58 at 32,
  60 at 33, 62 at 34, 63 at 35, 64 at 36, 65 and 66 at 37, 67 and 68 at 38, 69 at 39. Then the close.
- Unit 56's spec was flipped to INPROGRESS on node d and flipped back; nothing of unit 56 is dispatched or committed.

## Take it over on node a

1. `git fetch origin`, then add a worktree on the run branch under the node's worktree root, tracking
   `origin/branch/unattended-dboundroles-62c3df`. Keep the branch name: the run-state file names it.
2. In that worktree run `python tools/policy/policy.py settings --write .claude/settings.local.json`, or the spawn guard
   refuses every Agent and Workflow call for missing harness limits.
3. Schedule the idle-wake first: `CronCreate` every 10 minutes (cron `3-59/10 * * * *`), each tick running
   `bash tools/unattended/unattended.sh --wake dBoundRoles --keepalive-id <id>`. Then run
   `bash tools/unattended/unattended.sh --resume dBoundRoles --keepalive-id <id>` and `--status dBoundRoles`.
4. Run `/session-kickoff` from the worktree. Route the card to the unit you dispatch next, and re-append it with
   `bash skills/session-kickoff/manifest-check.sh --card --append --session <sid>` from the worktree, with the READY
   base at HEAD, after every compaction and before every commit. The scratch-guard refuses a commit whose card names
   another tree.
5. The session's hooks run from the primary tree. Until this build lands, the primary tree's spawn guard predates the
   new marker grammar, so a DIRECT spawn of a role agent is refused. The harness Workflows still admit their agents:
   build every unit through `tools/workflows/unattended-unit.js`, and give a spec writer its pass through the
   spec-write stage of `tools/workflows/unattended-build.js`, as node d did for units 81 to 85.

## The per-unit recipe node d used

- **Brief.** Copy TOOL-dBoundRoles-51's brief (`2026-11-22-prompt-TOOL-dBoundRoles-51-build-brief.md` in this folder)
  as the template. Change the unit id and order, add `TOOL-dBoundRoles-51 at 06aa7cdff` (the round-1 records minors,
  the recall Skill off the refused search tools) to the built-so-far list, and replace the unit-specific bullets.
  Keep every generic bullet: kit-code naming, record citation rules, generated outputs, encoding, the policy guard
  patch route, the upgrade-step and budget rows, the renders, and the commit contract.
- **Flip and check.** Flip the spec's status cell from DEFERRED to INPROGRESS. Then run
  `python tools/check-spec-tokens.py --spec <spec>`.
- **The renamed leg.** Specs 56, 58, 60, 62, 63, 64, 66 and 69 still name `agent-cap self-test`. Decision
  `2026-11-23-build-TOOL-dBoundRoles-43-1-main-loop-decision.md` rules that it reads `spawn-guard self-test`. Before
  dispatch, waive each such spec's hits:
  `python tools/memory-tree/ratchet.py widen spec-token-waivers --key 'agent-cap self-test' --key 'spawn-guard self-test <- <path>' --reason "<as widen record 14 words it>" --unit <id>`.
  The guards key's path is the one the token check names. The builder drops the stale rows in a records commit after its
  spec closes. The spec text itself is owed to a spec writer at the close.
- **Dispatch.** Run `bash tools/unattended/unattended.sh --dispatch dBoundRoles --pass <id>` with one `--writes` per
  path. Then `git add` the brief and run `--brief dBoundRoles --unit <id> --path <brief>`. Run
  `python tools/memory-tree/gen_build_index.py --write`, and commit everything it rewrites, `memory/backlog/TOOL.md`
  included. Push.
- **Launch.** Run `python tools/roles/handoff.py facts --build dBoundRoles --input prompt=<brief> --input spec=<spec>`.
  Launch `tools/workflows/unattended-unit.js` with these args:
  - `repo`, `slug`, `scratch` and `mode: unattended`;
  - `driver: bash tools/unattended/unattended.sh`;
  - `ground`: the `GROUND` text of `tools/workflows/unattended-build.js` with node a's repo, slug and scratch path;
  - `checklist: python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD`;
  - `passLegs: bash tools/run-gates/pass-legs.sh`;
  - `roles {builder: gov-builder}` and `efforts {builder: high}`;
  - `unitId`, `specPath` and `briefPath`;
  - `passBase`: the dispatch records commit;
  - `writes`;
  - `facts`: the facts list, transcribed exactly.

  Then compare the builder transcript's handed brief and spec with the files' bytes. A mismatch is stopped and
  relaunched, never built on. Register the task with `--register-task`.
- **On return.**
  1. Run `bash tools/run-gates/pass-legs.sh --base <passBase>` in the pass tree.
  2. Merge with `bash tools/unattended/pass-tree.sh --merge dBoundRoles --pass <id> --branch <pass branch> --from <passBase>`.
  3. Red-fix an own red on the run branch. The commit carries `Red-fix: <exact leg>` and `Pass: none`, with no blank
     line before the co-author trailer. The record goes in the NEXT commit, through
     `python tools/memory-tree/build_records.py new red-fix`.
  4. Run `--release-task`, then `python tools/roles/handoff.py agents --run <wf> --write`,
     `python tools/chain-packet.py --write dBoundRoles` and `gen_build_index.py --write`. Commit the records and push.
- **Inherited reds a pass meets.** These are not the pass's own:
  - lexicon naming at its current count over pin `1421`;
  - dead-path carriers (the reviewer rows of `.governance/install.json`, the frozen receipt, the roles `kit.toml` lines);
  - hygiene check 21 on the dWitnessedBar replay record;
  - lexicon wiring.

  A spec-token red on a spec waived per decision 43-1 is expected.

## Unit notes ahead

- **Unit 56.** It edits `skills/session-kickoff/manifest-check.sh`, which is on the kickoff manifest's watch list, so
  the pass commit re-stamps `memory/guides/SESSION-KICKOFF.md`. Its token check reds on two hits: the leg, and the
  guards key `spawn-guard self-test <- tools/hooks/scratch-guard.js`. Widen both. Unit 50 already moved
  `readSpecH1Id` onto `readUnfencedLines`; `tree_lib.unfenced_lines` and R4's `fence = !fence` toggle remain to move.
- **Unit 57.** It takes unit 51's re-worded memory-recall description. The memory-recall kit self-test reds until it
  lands.
- **Unit 60.** Its S10 and S11 restate unit 49's old AC3 and rev-bump unit 49's CLOSED spec. Repair the spec through a
  spec-writer pass before its dispatch.

## Owed at the close

- **Spec-writer rev bumps.** Specs 25 (S2 plus its leg and guards), 43, 50, 53 (to rev-5), 59, and every spec that
  still names the renamed leg. Also unit 53's ledger AC1 and AC2, and unit 59's ledger AC5.
- **RED-first observation of every new arm,** at the main loop, after the last unit is terminal. Units 8, 11, 12, 18,
  19, 20, 23, 24, 25, 26, 40, 41, 43, 44, 47, 48, 50, 52, 53, 59, 61, 81, 82, 83, 84 and 85 each declared one.
- **Inherited dead-path rows:** the reviewer rows of `.governance/install.json`, the before-image, and the roles
  `kit.toml` lines.
- **Roles kit:**
  - the spawn guard's `FLOOR_ASSERTIONS` and its waiver row (unit 64);
  - S37 `resume="atomic"` for the reviewers step in the roles `kit.toml`;
  - the adopt-playbook suite row for the role-rows plant;
  - the `budget` lines of `gov-builder`, `gov-orienter` and `gov-spec-writer`, each over its budget.
- **Unit 44:** its AC6 hygiene check over a scratch tree.
- **Another build's red:** the dWitnessedBar packet's byte compare.
- **Lexicon and docs:**
  - the lexicon pin;
  - the usage row for `route-refusal`;
  - `help/tags.md`;
  - the docs rows of units 10, 15, 22 and 46.
- **Landing:**
  - harness admission at the landed bytes;
  - the kit-epoch mint for memory-recall at the lander.
- **For the owner at wrap-up:**
  - ask PLAY-dOrderedCharter-89 (overlay write verb, unit 43's S10 and S23 deferred), with the resolver-import
    alternative;
  - the defer acts of units 20, 25 and 43 against asks TOOL-dBoundRoles-77 to -79 and TOOL-dDeclaredLoop-120.

## The close

1. Run `--phase dBoundRoles VERIFYING --witness <sha>` and commit.
2. Run the closing review through `tools/workflows/tier2-review.js` over the cumulative diff from BASE, after
   `python tools/memory-tree/gotchas.py --for-diff <base>..<head>`.
3. Run `bash tools/push-main.sh --prepare --slug dBoundRoles`, then `--authorization dBoundRoles`, then
   `--close dBoundRoles`.
4. Run `bash tools/push-main.sh --land --slug dBoundRoles`, then `--landed dBoundRoles`.
5. Reap the keepalive with `CronDelete`, attest `keepalive-reaped` and `parked-decisions-surfaced`, and wrap up.

Node d never runs the merge bar or a self-test suite unattended. The owner decides `GATE_SELFTESTS=1` at the close.
