# TOOL-aHeardState-1 — the live witness, and why this run's own session could not be it

**Serves:** journal TOOL-aHeardState-1

## What was tried

After the wiring commit `0a2162b9`, this run's session (`7ecabc14-b395-43a9-8f32-9e036af87174`) ended
one turn deliberately without the BUILD/SPEC pair, with the message "This turn ends without the
pair, as S9's witness" as its last line. The next input was a background-task notification. No
`Stop hook feedback:` arrived from format-guard, and none from stop-guard either, although
`memory/builds/aHeardState/RUN.md` records `session: 7ecabc14-b395-43a9-8f32-9e036af87174` and a
bound session's turn end at phase BUILDING draws stop-guard's `run-open` block.

## Why

The session was launched in `.claude/worktrees/blissful-khayyam-69a7df` and moved into this tree with
`EnterWorktree` before the build folder existed. Its Bash environment carries no `CLAUDE_PROJECT_DIR`,
and the two silent hooks are consistent with one explanation: the harness resolves `Stop` hooks from
the launch tree, whose `.claude/settings.json` does not wire format-guard and whose memory tree holds
no aHeardState `RUN.md` for stop-guard to bind. This is an inference from two silences, not a reading
of the harness's configuration. The harness's own hook log was not consulted.

The second half is a finding about the unattended kit, beyond this build: a run whose session started
in one worktree and moved to the run's tree has a dark stop-guard for the whole run. It is parked in
the run-state file for the owner rather than built here.

## The in-tree observation that replaces it (AC11, rev-2)

The hook, run as `.claude/settings.json` runs it, with `CLAUDE_PROJECT_DIR` set to this tree, this
session's id, this tree as `cwd`, the real orientation card under the common dir, the real
`memory/LIVE.md`, the real `AGENTS.md` and the real HEAD. Only the Stop payload is built by hand, by
`node -e` in a scratch script.

- The card's route reads `- build: aHeardState`, and `memory/LIVE.md` carries an aHeardState row
  at status INPROGRESS.
- The witness message blocks: `{"decision":"block","reason":"format-guard: this session routes build
  aHeardState, which LIVE.md lists as in progress, …\n- no BUILD line\n- no SPEC line …"}`, exit 0.
- The same message ending with this build's pair prints nothing and exits 0.
- The first armed stop wrote the baseline `.git/worktrees/aHeardState/format-guard/7ecabc14-b395-43a9-8f32-9e036af87174.head`.

## Owed to the owner

The harness half: start a session in a tree carrying the wiring, route it to a live build, end a turn
without the pair, and see `Stop hook feedback:` carrying this hook's reason. That one observation also
confirms that the running CLI delivers `last_assistant_message`, which every arm here builds by hand.
