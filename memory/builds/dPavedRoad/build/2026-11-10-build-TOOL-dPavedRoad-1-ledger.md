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

## New arm, observed at the close

In clones of `6681cdc80` under `%TEMP%/dpr`, by the main loop. RED: with `tools/check-spec-tokens.py`
restored to base `14320c985`, which has no `--spec`, `bash tools/check-spec-tokens.test.sh` exited 1
in 338 s with exactly the six PR1 arms failing (AC1, AC2 twice, AC3, AC4 twice) and every other arm
passing. GREEN: at `6681cdc80` it exited 0 in 386 s, `PASS (236 assertions)`, above the floor of 231.

## Fix pass — the install-prefix red

The bar at `d08106d4d` red on `install-prefix (shipped surface)`: the role text this unit added
spelled the kit path `tools/check-spec-tokens.py` at `tools/roles/agents/gov-spec-writer.agent.md:37`,
which resolves to nothing at an adopter installed at another prefix. The sentence now names the
spec-token checker as `check-spec-tokens.py --spec <path>`, with no prefix, and keeps its meaning;
`render_agents.py --write` re-rendered `.claude/agents/gov-spec-writer.md` to the same bytes. The
section 4 role-text block spells the `python tools/` form; the respelling drops only that prefix, and
AC7's phrase is unchanged. No change to `--spec`, the policy grant or any other role's text.

Observed by probe in the pass, no gate run: `grep -n 'tools/check-spec-tokens'` over both files
printed nothing (exit 1), and a `python -c` scan with the leg's own `tools/` lookbehind found no
match in the source role file. Owed at the close: the `install-prefix (shipped surface)` leg itself.

**Evidences:** TOOL-dPavedRoad-1
- AC5 — re-observed: `python tools/roles/render_agents.py --write` wrote the one changed agent type, `.claude/roles.json` still lists `spec tokens (a spec's own names resolve)` in `gov-spec-writer`'s gates, and `render_agents.py --check` exited 0 with 9 agent types and 1 index graded.
- AC7 — re-observed: the `grep -c "check-spec-tokens.py --spec"` the criterion names counted 1 in each of its two files.

## GREEN re-observed after the fix pass

After the bar-fix pass `59c386425` respelled the role text, the main loop re-ran
`bash tools/roles/adopt-roles.test.sh` in a clone of `59c386425` under `%TEMP%/dpr`: it exited 0 in
87 s, `PASS (65 assertions)`. The merge bar at `59c386425` was GREEN, 72 of 72 legs, the
`install-prefix (shipped surface)` leg among them.
