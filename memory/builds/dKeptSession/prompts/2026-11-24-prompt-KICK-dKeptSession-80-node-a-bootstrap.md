**Serves:** research KICK-dKeptSession-80 KICK-dKeptSession-69

# Bootstrap — dKeptSession resumed on node a, from a fresh session with no console work by the owner

This is the message the owner pastes into a new Claude Code session on node `a` (`daily-agent @
COMPEETO-AGENT`). Everything below is the agent's to do. The owner types nothing in a console.

---

You are taking over the `dKeptSession` unattended run of the coding-governance repository on node `a`.

The owner moved the run here from node `d` on 2026-11-23 and mandated it to land unattended. Its committed
build README is the mandate. Never end a turn by asking: the run's stop-guard refuses that. Decide what the
protocol lets you decide, park what it does not with `--park`, and keep going.

## 0. Where things are

- Repository primary tree on this node: `C:/projects/coding-governance`, on `main`.
- The run's branch on `origin`: `branch/unattended-dkeptsession-a0567a`. Its tip was `14f5b9fa6` when node d
  left it, or later.
- The run's worktree path: `C:/projects/coding-governance/.claude/worktrees/unattended-dkeptsession-a0567a`.
  Every node's checkout sits at that same path, and worktrees never sync, so you create it here.
- The run is `HELD`:
  - code `host-owner-action`, until `owner`, held from `VERIFYING`;
  - the lease released;
  - node d's keepalive `64fde974` already reaped;
  - no durable restart owed.
- The full orientation is the handoff committed on the branch:
  `memory/builds/dKeptSession/prompts/2026-11-23-prompt-KICK-dKeptSession-80-4-session.md`, rendered from
  `memory/builds/dKeptSession/prompts/2026-11-23-prompt-KICK-dKeptSession-80-node-a-handoff-brief.md`.
- Every close debt the units returned is in
  `memory/builds/dKeptSession/build/2026-11-23-build-KICK-dKeptSession-80-close-debts.md`.
- The close's first full bar, with its reds attributed against origin/main, is in
  `memory/builds/dKeptSession/build/2026-11-23-build-KICK-dKeptSession-80-close-bar-attribution.md`.

Use the Bash tool (Git-Bash) and give `git -C` forward-slash paths. Python's own `bash` here is WSL's, so never
run a shell leg through it.

## 1. Bring the primary tree current

In `C:/projects/coding-governance`:
1. If it is on `main` with a clean tree, `git fetch origin` and `git merge --ff-only origin/main`.
2. If the tree is dirty or not on `main`, leave it as it is and only fetch. It may be another session's.

The session hooks run from the primary tree, so a current `main` gives you main's hooks.

## 2. Create the run worktree and move this session into it

1. If the path does not exist:
   ```
   git -C C:/projects/coding-governance fetch origin
   git -C C:/projects/coding-governance worktree add --track -b branch/unattended-dkeptsession-a0567a C:/projects/coding-governance/.claude/worktrees/unattended-dkeptsession-a0567a origin/branch/unattended-dkeptsession-a0567a
   ```
   If the local branch already exists, drop `--track -b <branch>` and name the branch alone, then
   `git merge --ff-only origin/branch/unattended-dkeptsession-a0567a` inside the worktree.
2. If the path already exists, confirm it is on that branch with a clean tree before fast-forwarding it.
3. Move this session's working directory into that worktree, with the app's change-directory tool or
   `EnterWorktree` on the existing path. Every step below runs there.
4. The Edit tool and the scratch-guard refuse files of another tree.
5. Render the harness's agent limits into the worktree. Without them, agent-cap's rule 7 refuses every
   Agent and Workflow call:
   ```
   python tools/policy/policy.py settings --write .claude/settings.local.json
   ```

## 3. Take the run over

Follow the unattended Skill's Resume path and the verbs guide's take-over steps
(`memory/guides/UNATTENDED-VERBS.md`, "Resume"), in this order:

1. Read `memory/builds/dKeptSession/RUN.md`'s last rows and run `bash tools/unattended/unattended.sh --status
   dKeptSession`.
2. Reap the recorded id first, with `CronDelete 64fde974`. It is node d's and already gone, so say what the
   result returned.
3. Schedule this node's idle-wake with `CronCreate` at `3-59/10 * * * *` and keep its id. Its prompt is
   exactly:
   `Idle-wake for the dKeptSession unattended run: run `bash tools/unattended/unattended.sh --wake dKeptSession --keepalive-id <this job's id>`. HEALTHY ends the turn. FULL runs `bash tools/unattended/unattended.sh --resume dKeptSession --keepalive-id <this job's id>`, then `bash tools/unattended/unattended.sh --audit dKeptSession`.`
4. Run `bash tools/unattended/unattended.sh --resume dKeptSession --keepalive-id <new id>`.
   - If it refuses or prints `still held`, reap only the job you just scheduled, say why, and stop.
   - A check-58 refusal names the worktree the run expects.
5. Commit the record the resume staged (`Pass: none`, the charter's commit trailer) and push the branch before
   any other work.
6. Run `/session-kickoff`. Inside a started unattended run its Step 5b continues without halting. Append the
   READY card from the worktree with `base` = HEAD. A card that names the primary tree blocks every commit,
   so re-append it from the worktree.

## 4. Do the work

Read the handoff (§0) WHOLE, then `memory/guides/BUILD-METHOD.md` WHOLE. In brief:

1. `git fetch origin`. Unit KICK-dKeptSession-80's spec is keyed to `origin/main` `525f3ab97`.
   - If main has moved past that, re-run the trial merge `git merge --no-commit --no-ff origin/main`, list the
     conflicts, and run `git merge --abort`.
   - Re-ground the spec through a `gov-spec-writer` with a brief naming the new conflicts. The run's spec
     edits go through the writer.
2. Build KICK-dKeptSession-80 by its S1:
   - Start `git merge --no-ff --no-commit origin/main` in the run worktree.
   - Spawn `gov-builder` directly from `python tools/roles/handoff.py render --role gov-builder --build
     dKeptSession --unit KICK-dKeptSession-80 --input spec=<its spec> --input prompt=memory/builds/dKeptSession/prompts/2026-11-23-prompt-KICK-dKeptSession-80-reconcile-brief.md`.
     Paste the marker line plus `## Task` onward, with the description the render prints on stderr. A builder
     render keeps only the brief's non-goals, which is where the in-progress merge is stated.
   - The builder resolves, regenerates, stages its ledger and its CLOSED flip, and commits nothing.
   - Commit the merge yourself with `Pass: KICK-dKeptSession-80`, hooks running, and push.
3. Run the full bar, `GATE_FULL=1 bash tools/run-gates/run-gates.sh`, in the background, registered with
   `--register-task`.
   - Attribute each red against `origin/main` by hand. Run each red leg's argv from `tools/gate-legs.json` in
     a scratch worktree of `origin/main` under `%TEMP%`, and compare findings.
4. Clear each own red through the red-fix lane:
   - the fix commit carries `Red-fix: <leg>` and `Pass: none`;
   - the next commit carries the record, from `python tools/memory-tree/build_records.py new red-fix`;
   - a shrink-only registry is widened through `python tools/memory-tree/ratchet.py widen`, with its record.
   Leave inherited reds alone, and say which they are.
5. Complete KICK-dKeptSession-69's ledger (AC2, AC3, AC9, AC11 to AC14) from that bar and flip it CLOSED, by
   a builder pass. Hygiene check 23 wants one line per criterion, sharing the criterion's backticked tokens.
6. Observe every owed `New arm:` line RED then GREEN, and record seen-red lines in a `Pass: none` commit.
7. Dispose every remaining close debt from the debts record: fix it where a leg reds, otherwise file it as an
   ask in this build's `BACKLOG.md`.
8. Land:
   - `bash tools/push-main.sh --prepare --slug dKeptSession`;
   - `bash tools/unattended/unattended.sh --authorization dKeptSession`;
   - `bash tools/unattended/unattended.sh --close dKeptSession`;
   - `bash tools/push-main.sh --land --slug dKeptSession`;
   - `bash tools/unattended/unattended.sh --landed dKeptSession`;
   - `python tools/runlog/runlog.py record dKeptSession --write`;
   - attest `keepalive-reaped` and `parked-decisions-surfaced`;
   - `CronDelete` your idle-wake.

## 5. Standing rules that bind this run

The owner's rules:
- **Self-tests are the owner's to start.** Never run `GATE_SELFTESTS=1`, and never export it into `--close`,
  even when a tool prints that the flagged bar is owed. It costs about 1.5 h and is opt-in only. Never run the
  `tools/unattended/` self-test suites (`unattended.test.sh`, `check-unattended.test.sh` and their kin):
  observe their arms with hermetic probes built from the suite's own setup.
- **Role work stays in role agents.** Spec writing and review, building, and the closing review run in the
  repo's role agents. Units run no gate legs.
- **No route around a refusal.** Never `--no-verify`, never change `hooksPath`, never push `main` raw:
  `push-main.sh` is the lander. Read a refusal rather than routing around it.
- **The `loop transition record` ceiling is the owner's.** Its 120 s ceiling (PINNED 2026-11-23,
  tools/gate-legs.json) against a budget row near 510 is a parked owner decision: re-price the row, never
  edit `tools/gate-legs.json`, never stop on it.
- **Asks wait for the owner.** Asks KICK-dKeptSession-68 and -70 to -78 are surfaced at the wrap-up.

Repository mechanics:
- Every commit ends with the charter's trailer, `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`, and
  a records-only commit carries `Pass: none`.
- Every temporary file goes in your session scratchpad, spelled absolute. A git clone or scratch worktree goes
  under `%TEMP%/<short>`.
- Every final message carries the charter's micro-formats as bare `- ` lines at column 0:
  - the `agent` and `returned` lines, from `python tools/roles/handoff.py agents --run <wf>` or `--handoff
    <prompt>`;
  - one `committed`/`merged` line per new commit;
  - `gates` or `skipped`, and `⏳` for a running task;
  - the state line, then `BUILD` and `SPEC`, adjacent and last.
  The format-guard hook refuses a message missing any of them.
