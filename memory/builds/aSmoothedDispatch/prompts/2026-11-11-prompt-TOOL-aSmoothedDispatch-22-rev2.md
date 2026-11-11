# Revision brief — aSmoothedDispatch: TOOL-aSmoothedDispatch-22 rev-2, the hook probe's control

**Serves:** research TOOL-aSmoothedDispatch-22

## The brief

### Goal
Revise `memory/builds/aSmoothedDispatch/spec/2026-11-11-spec-TOOL-aSmoothedDispatch-22.md` to rev-2, keeping it INPROGRESS. The builder's pass diverged on one fact. Main at `bdb633d94` carries TOOL-dPavedRoad-1 (commit `1b991ef0c`), which adds `spec tokens (a spec's own names resolve)` to gov-spec-writer's allowlist. It does this in `tools/roles/house/policy.toml:36` and in the `"gov-spec-writer"` entry of `.claude/roles.json`, at lines 177-181 at `bdb633d94`. The scratch-guard role-gate arm passes any G1 leg on the role's allowlist (`if (leg && allow.includes(leg.name)) continue`). So at the merge the hook admits the bare `python tools/check-spec-tokens.py` to gov-spec-writer, and §4's probe control printed `exit=0`, not `exit=2`. At `ba6c2f1f9` it printed `exit=2` only because that tip lacked main's grant. Every other criterion the builder reached held at the trial merge: S2/AC2, S3/AC3, with the floor of 235 recounted (165 `arm "` lines at the base, 179 on the branch, 172 on main, 176 merged), and S4/AC4. The builder did not reach S6 or S7.

### Items
1. §4 "S5 — the hook probe" and AC5: the probe's control must be a command the merged hook still refuses to gov-spec-writer. Pick it by reading `tools/hooks/scratch-guard.js` and `.claude/roles.json` at `bdb633d94` with `git show bdb633d94:<path>`. Candidates are the checker's suite, `bash tools/check-spec-tokens.test.sh` (the G3 suite shape), or a G1 leg not on the writer's allowlist. State the exit and the stderr line the control prints, and cite the rule by path and line. The two-operand `--spec` form stays as the admitted case.
2. §5 "security": rewrite the line. It says main grants the writer the bare spec-token leg (TOOL-dPavedRoad-1), that this unit leaves that grant as merged, and what the hook still refuses, the control from item 1.
3. §2 S5, and any other sentence claiming the hook refuses the bare leg to the writer: correct it. Keep §3's non-goal that rules out touching the grant, and name `tools/roles/house/policy.toml` and `.claude/roles.json` as carried as merged.
4. §2: note that the trial merge is re-taken at `e1f9cebb3`. The builder saw tree `6002767` there, with the same three files and region counts 8, 2 and 1. AC7's fixture says the builder re-takes the tree with its stated command rather than pinning `de33b5c7` alone.
5. Bump the status line to rev-2 and add one revision-log line naming this brief.

### Acceptance
The rev-2 spec's AC5 names a control the merged hook refuses, with that control's exit and stderr line cited to `tools/hooks/scratch-guard.js` at `bdb633d94`. No sentence in the spec says the hook refuses the bare spec-token leg to gov-spec-writer. `python tools/check-spec-tokens.py --spec` over the spec prints no hit the spec's own text can fix.

### Gates
The spec-token checker's `--spec` mode over the revised spec, the memory hygiene gate and the naming lexicon (writer); the rest are the unit's, unchanged.

### Non-goals
Any change to S2, S3, S4, S6 or S7, or to AC1-AC4, AC6 or the `New arm:` lines, beyond a sentence that states the corrected hook fact. Any change to the writer's grant. Committing, which is the main loop's.
