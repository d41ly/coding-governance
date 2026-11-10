**Serves:** journal TOOL-dPavedRoad-1

# TOOL-dPavedRoad-1 — acceptance ledger

The unit as built, at spec rev-1, in commits 1b991ef0c and c2e540098. `tools/check-spec-tokens.py
--spec <path>...` grades exactly the named specs as if live, whatever their status and whether git
tracks them; the hands-off sibling map is read from the LIVE specs on disk in the named spec's own
`spec/` folder; the carries and packet joins and the two stale-row arms do not run, and the report
says so. `gov-spec-writer` holds the spec-tokens leg in `tools/roles/house/policy.toml`, and its role
text tells it to run `--spec` over each spec it writes. The suite gains seven PR1 arms and its floor
moves 224 to 231.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in the pass. The builder observed each
criterion with a probe of this unit's code, transcribed below from its return; the fixtures were
clones under `%TEMP%/pr1` and `%TEMP%/pr2`, deleted afterwards.

Owed at the close: the RED-first observation of the PR1 arms in `tools/check-spec-tokens.test.sh`
(AC1 to AC4) and the section 7 legs, the full-corpus `spec tokens` run among them.

**Evidences:** TOOL-dPavedRoad-1
- AC1 — `--spec` over an untracked DEFERRED fixture spec listing AC2 before AC1 exited 1 with an `[ac-order]` hit naming the fixture's path, in 1.15 s wall; the fixture's status was checked not to match LIVE.
- AC2 — with the fixture's labels back in ascending order the same command exited 0, printed no STALE line, and printed `skipped under --spec` on both the carries line and the packet line.
- AC3 — with a second untracked OPEN fixture spec in the same folder that never names the token, the run exited 1 with a `[handoff]` hit naming that token; with the sibling set to DEFERRED the bullet counted silent and the run exited 0.
- AC4 — `--spec README.md`, a path that does not exist, no operand, and a path outside the repository each exited 2 with a `REFUSING` line.
- AC5 — after `python tools/roles/render_agents.py --write`, `.claude/roles.json` lists the leg under `gov-spec-writer`'s gates, and `render_agents.py --check` exited 0.
- AC6 — Bash PreToolUse payloads piped to `node tools/hooks/scratch-guard.js`: `gov-spec-writer` running the bare checker exited 0; `gov-builder` running it exited 2 with the "a role agent runs no gate" line; the `--spec` form exited 0 for both roles.
- AC7 — the `grep -c` the criterion names counted 1 in each of its two files.
