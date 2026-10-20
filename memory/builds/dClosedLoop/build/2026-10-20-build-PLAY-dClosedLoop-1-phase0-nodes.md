# Phase 0 node preparation: node d run, and the steps for nodes a and b

**Serves:** research PLAY-dClosedLoop-1

P0.9 of `build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md` `[phase-0]`, run on node d by dClosedLoop's
session on 2026-10-20 at `03843fc8c`, in the worktree `.claude/worktrees/unruffled-aryabhata-d89ede`. The red tests
ran in a `git clone --shared` of that worktree under the session's scratch folder.

## [node-d]

| Step | Command | Result |
|---|---|---|
| Exactly one remote | `git remote` | `origin` only |
| Remote head set | `git symbolic-ref refs/remotes/origin/HEAD` | `refs/remotes/origin/main`, already set, so `set-head -a` was not owed |
| Wiring | `bash tools/check-wiring.sh` | exit 0; every row `ok` but `skip ssh — no remote pushes over ssh`, so `--fix` was not run |
| Kickoff junction | the session-start wiring report | `ok skill — the installed /session-kickoff engine matches tracked` |
| Resume tick | `schtasks /query /tn gov-resume-tick` | "ERROR: The system cannot find the file specified.": NOT registered. The kit never registers it: "`schtasks /create` and `crontab` are the owner's acts, once per node" (`tools/unattended/README.md:215-216`). Owed by the owner, below |
| Python | `. tools/lib/resolve-python.sh && PY=$(resolve_python) && "$PY" --version` | `PY=python3`, `Python 3.14.5` |
| User | `echo $USERNAME` against `tools/playbook/fleet.toml` | `d41ly`, node d's row `user = "d41ly"` |

**Acceptance on node d:**
- `bash tools/unattended/unattended.sh --claims`: exit 0, answering from the remote (rows such as `aSparedSpawn
  daily-agent held`, `dHomedResolver d41ly landed`).
- `check-wiring.sh`'s check mode: clean (exit 0).
- The resume tick: NOT listed. This observation stays OPEN until the owner registers it.
- `bash tools/unattended/unattended.sh --plan dClosedLoop --paths`: exit 0. It printed
  `2026-10-20-spec-PLAY-dClosedLoop-1.md - NOT A UNIT (no status header)` and `next: PLAY-dClosedLoop-1 (MISSING -
  spec it first)`: the driver's plan reader does not read the unit spec's status header. Raised with the owner; the
  spec is not this record's to change.

**Red tests:**
- Merge driver: in the fresh clone `git config --get merge.rows.driver` exits 1, and `check-wiring.sh` exits 1
  reporting `UNWIRED hooks — core.hooksPath unset`, `UNWIRED merge — … merge.rows.driver is unset` and `UNWIRED merge
  — … merge.ours.driver is unset`. After `check-wiring.sh --fix`, check mode exits 0.
- Python: `resolve_python` with `PATH=/nonexistent` exits 1 and prints "no usable python launcher … tried: python3
  python py", with `PY` empty.

## [owner-step-d]

The one step P0.9 leaves on node d is the owner's: register the resume tick under the login whose `claude` CLI is
authenticated, as `tools/unattended/README.md` describes it, then confirm it with `schtasks /query /tn
gov-resume-tick`.

## [node-a]

Node a, `daily-agent @ COMPEETO-AGENT`, primary tree `C:/projects/coding-governance`, Windows with Git Bash
(`AGENTS.md`, the node registry). In its primary tree, in Git Bash, with forward-slash paths:

1. `git remote` prints exactly one remote; then `git remote set-head origin -a`.
2. `bash tools/check-wiring.sh`; if any row reads `UNWIRED`, run `bash tools/check-wiring.sh --fix` and check again
   until it exits 0.
3. The kickoff skill's junction (`AGENTS.md`, section 2): the session-start wiring report's `skill` row reads `ok`.
4. The owner registers the resume tick, as `tools/unattended/README.md` describes, and `schtasks /query /tn
   gov-resume-tick` lists it.
5. `. tools/lib/resolve-python.sh && PY=$(resolve_python) && "$PY" --version` prints a version. Every schedule run
   is `"$PY" memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-schedule.py --ref origin/main`.
6. `echo $USERNAME` prints `daily-agent`, the fleet row's `user`.
7. Acceptance: `bash tools/unattended/unattended.sh --claims` answers from the remote; `check-wiring.sh` exits 0; the
   resume tick is listed; `bash tools/unattended/unattended.sh --plan dClosedLoop --paths` runs.

## [node-b]

Node b, `agent5 @ DESKTOP-3J1O6CD`, onboarding. Its tag `b` is already claimed in `tools/playbook/fleet.toml`.

1. Clone the repository to its primary tree, `C:/projects/coding-governance`.
2. Every step of `[node-a]`, with `agent5` as the user in step 6.
3. "Seed local memory from the in-repo mirror" (`AGENTS.md`, onboarding) names no mirror. The plan lists it under
   `[cannot]`; node b starts with an empty local memory.
4. Node b is offered spec runs only (P0.8 row 4).
