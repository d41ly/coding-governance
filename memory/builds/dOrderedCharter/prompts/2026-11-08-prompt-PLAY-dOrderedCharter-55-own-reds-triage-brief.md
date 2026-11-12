**Serves:** research PLAY-dOrderedCharter-55

# Brief: the close bar's own reds, triaged

## The prompt

> merge this branch to remote as well

— owner, 2026-11-05. The first full bar at VERIFYING is red on 14 legs. The same legs on a detached `origin/main` worktree are green but one,
so 13 reds are this branch's own and must be fixed before the run hands its landing to the owner.

## The brief

### Goal

Name, for each of the 13 legs, the offenders this branch adds over main, the smallest correct fix, and whether it touches code.

### Items

1. **The logs.** This branch's legs log under `C:/projects/coding-governance/.git/worktrees/unattended-dorderedcharter-725f52/gate-logs/`;
   main's under `C:/projects/coding-governance/.git/worktrees/om8/gate-logs/`; the main worktree is `C:/Users/DAILY-~1/AppData/Local/Temp/om8`.
   A log's name is the leg's name with spaces and punctuation as underscores. The install-prefix log is 18821 lines: grep it, never read it whole.
2. **The 13 legs:** kickoff-manifest ratchet · memory hygiene · shell hygiene (a loop fed by a command substitution) · shell hygiene (a fork
   spent on builtin work) · encoding posture (text IO names its encoding) · install-prefix (shipped surface) · method carriers (every pointer
   declared) · harness arms (fail branches armed or pinned) · drift-audit records · dead-path carriers (deleted files still named) · remote
   literals (kit code names no remote) · govkit acceptance matrix · policy check.
3. **Per leg:** the offenders on this branch and absent on main, from a diff of the two logs and the leg's argv in `tools/gate-legs.json`; the
   smallest correct fix, from the checker's own remedy text, preferring the cause over a waiver; and its class, RECORD when it writes only under
   `memory/`, `help/` or a registry list the checker reads, CODE when it writes under `tools/` or `skills/`, with every file it writes.
4. **The 14th leg,** every held leg is budgeted: name any offender this branch adds beyond main's.
5. **Where to write:** one file,
   `C:/Users/DAILY-~1/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-unattended-dorderedcharter-725f52/0394fa33-012c-408f-a840-e6e4cfaac23f/scratchpad/own-reds-triage.md`,
   a section per leg and a closing table of leg, class and files.

### Acceptance

- Every one of the 13 legs has its offenders, fix, class and files, or says what could not be determined.

### Gates

None. Run no bar, no leg runner and no suite; a single checker run directly over a tree, read-only, is allowed where a log is truncated.

### Non-goals

- No write to either tree.
- No fix applied.
