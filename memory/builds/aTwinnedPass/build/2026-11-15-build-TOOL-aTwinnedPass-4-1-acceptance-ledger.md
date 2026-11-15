# Acceptance ledger — TOOL-aTwinnedPass-4

**Serves:** journal TOOL-aTwinnedPass-4

Built against spec rev-1 in one pass commit, on node a, in the pass's own worktree reset to the
dispatch commit `cce6710c1`. The spec's forks carry their resolutions, and the build follows each:
F1 (a), the holder compared with the one path the branch implies; F2 (a), `TREE_SHAPE`'s segment
class admits a space.

One divergence inside the spec, built to its rule and named here for the main loop: §4 step 2
spells the wanted path `<primary>/.claude/worktrees/agent-${PT_BRANCH#worktree-}`, and stripping
`worktree-` from `worktree-agent-q4` leaves `agent-q4`, so that expression names
`.../agent-agent-q4`. Built that way, the probe below refused q4 and p2 at their own places, against
S5, AC5 and AC6, which all name `<primary>/.claude/worktrees/agent-<id>` for the branch's own `<id>`.
The code spells `$primary/.claude/worktrees/${PT_BRANCH#worktree-}`, which is that rule. The spec's
line is for its owner to correct; this pass did not edit it.

The observations below are each criterion's own command, or the changed code run over a hand-built
fixture, run in the worktree with the change in place before the commit. No suite, gate leg or bar
ran in the pass.

The fixture for AC3 to AC7 was built inside the worktree under an untracked folder, removed before
the commit, in the pass-tree suite's shape: a repository on `main` with the suite's
`.unattended.conf`, `.claude/worktrees/` in `info/exclude`, a `run` branch carrying the records
commit C with build tRun's run-state file, and no hook. One script ran the calls of §4 "The arms"
twice: over this pass's `pass-tree.sh`, and over base `cce6710c1`'s copy beside the driver. The
fixture's primary tree sat at a long path. The suite's sits under `mktemp -d`, which on node a is
the 8.3 path `C:/Users/DAILY-~1/AppData/Local/Temp`. The isolation hook refused a git call through
a short-name path, so whether git prints the primary tree and a linked worktree in one spelling
there was not observed. The suite's run at the close observes it: the respelled T1 and T5 arms and
TP4's q4 arm go red if the two spellings differ.

Owed to the main loop at the close:
- the `TP4` group of `tools/workflows/unattended-build.test.sh` red, then green, under the breaks
  §7's first `New arm:` line names, with `FLOOR_ASSERTIONS` at 1028;
- the `TP4` block of `tools/unattended/pass-tree.test.sh` red, then green, under the breaks of §7's
  second and third `New arm:` lines;
- the respelled T1 to T5 arms of `pass-tree.test.sh` green, except two that stay red at this tip
  for `TOOL-aTwinnedPass-5`:
  `T2 branch worktree-agent-p4 remains` and `T5 branch worktree-agent-p7 remains`;
- the legs of the spec's Gates section.

**Evidences:** TOOL-aTwinnedPass-4
- AC1 — `TREE_SHAPE` — a `node` probe read both shapes out of `tools/workflows/unattended-unit.js`
  and tested the nineteen values the criterion names. It printed `AC1 OK 19`: the six hostile
  worktrees, the six hostile branches, `/w/agent-x1`, `agent-x1` and
  `/w/.claude/worktrees/agent-x1/sub` fail; `/w/.claude/worktrees/agent-x1`,
  `C:\w\.claude\worktrees\agent-x1`, the live `C:/projects/coding-governance/.claude/worktrees/agent-a062c1d85fb878113`
  and `worktree-agent-a062c1d85fb878113` pass. Over base's shapes it printed eight `ADMITTED` lines:
  the `$(id)`, quote, `;` and `..` worktrees, `/w/agent-x1`, the segment past the id,
  `worktree-agent-x1/../x` and `agent-x1`.
- AC2 — `whose path the builder returned unusable` — a `node` stub of `agent`, evaluating the
  harness as `run_wf` does, with `passBase`, `writes` and `passLegs` set, printed `AC2 OK 30` over
  the six hostile returns (four checks each), the old spelling, the segment past the id, the
  backslash form, and `TP_OK`'s respelled worktree in the result and in `nextAction`. Over base's
  harness it printed `AC2 FAIL 16/30`. A `node` parse of the `TP4` group's single-quoted returns,
  through the same `printf %s`, gave back the quote, the LF and the backslashes as the intended
  bytes. The suite's `TP4` group is owed to the main loop.
- AC3 — `pass-tree: REFUSING` — over the fixture, `--remove tRun --branch worktree-agent-q1` with
  the holder at `probe-elsewhere/agent-q1` exited 1 with one REFUSING line naming that holder, and
  the directory, `keep.txt` and the branch remained. Over base's tool it exited 0 and both were gone.
- AC4 — `where the runtime cuts that pass's worktree` — the `--merge` of `worktree-agent-q1` for
  `TOOL-tRun-4`, with `--from <C>`, exited 1 with that text; `HEAD`, `git status --porcelain` and
  the outside directory were unchanged. Over base's tool the branch was already gone by then.
- AC5 — `is not a branch the runtime cuts for a pass` — `--remove` and `--merge` naming `agent-q2`
  each exited 1 with that text, and its worktree remained; `--remove` naming `worktree-agent-q3`,
  held at `.claude/worktrees/agent-zz`, exited 1 naming the wanted `.../agent-q3`, and that worktree
  remained. Over base's tool both `--remove` calls exited 0 and removed the worktrees.
- AC6 — `git worktree list --porcelain` — `--remove` naming `worktree-agent-q4`, held at its own
  place with an untracked `scratch.txt`, exited 0 with the directory and the branch gone; `--merge`
  of `worktree-agent-p2` at its own place with `--from <C>` exited 0, printed the merge sha, and
  `git worktree list --porcelain` named no `agent-p2`.
- AC7 — `names no commit` — `--merge` of `worktree-agent-p2` with 64 hex digits exited 1 with
  `names no commit here` and no `is not 7 to 64`; with 65 digits and with `HEAD`,
  `is not 7 to 64 lowercase hex digits`. Over base's tool all three carried
  `is not 7 to 40 lowercase hex digits naming a commit`.
- AC8 — `check_pass_holder` — `grep -c 'tools/unattended'` over `tools/unattended/pass-tree.sh`
  printed `0`; above its first function the header carries `worktree-agent-<id>` and
  `.claude/worktrees/agent-<id>`. `lexicon.py --suggest check_pass_holder --as sh.function` printed
  `OK — check_pass_holder leads with check`. After `gen_map.py --write`,
  `memory/map/generated/symbols.json` gained `check_pass_holder` in `tools/unattended/pass-tree.sh`
  and the suite helper `render_pass_returns`, whose name the lexicon also printed `OK` for.

## The close

The main loop's observations at the close, on node a, 2026-11-15, at the build tip `39a71c080` unless named.

- `pass-tree.test.sh` with `pass-tree.sh` put back to `c40c39fb6`: RED, 18 FAIL lines, every one a `TP4` arm or the `--from` shape's text; GREEN at the tip, 157 assertions (PINNED 2026-11-15).
- `unattended-build.test.sh` with `unattended-unit.js` put back to `c40c39fb6`: RED, 16 FAIL lines, every one a `TP4` hostile-value arm; GREEN at the tip, 1530 assertions (PINNED 2026-11-15).
- The short-name temp root the builder could not test did not move the holder check: T1, T5 and TP4's q4 arm are green at the tip.
