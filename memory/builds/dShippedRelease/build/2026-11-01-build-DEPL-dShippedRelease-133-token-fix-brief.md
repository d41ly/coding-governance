# Brief — dShippedRelease: spec-token repairs on round 4's promotions

**Serves:** research DEPL-dShippedRelease-133

## The prompt

> Repair the spec-token hits round 4's promotions left, and take ownership of five such repairs the main loop already made outside your role.

## The brief

### Goal

`python tools/check-spec-tokens.py` reports no hit naming a spec of this build. That check is the main loop's: do not run it.

### Items

1. In `memory/builds/dShippedRelease/spec/2026-11-01-spec-DEPL-dShippedRelease-133.md`, AC1's two backticked fixture paths and AC3's backticked `c:/x/memory/a.md`, `/c/x/memory/a.md` and `memory/a.md` are graded as tracked paths and are not tracked. Reword both criteria so no backticked token is path-shaped, keeping every observable: AC1's printed `review<TAB>disposed · <n> finding(s) · ...` line with its repo-relative path, and AC3's three input spellings and one output. Plain unbackticked text for the literal paths is enough.
2. The main loop edited these five specs by a Bash script, which the role guard does not see. Read each edit with `git diff --cached` against the disposal's text if needed, confirm it keeps the criterion's meaning, and correct it if it does not:
   - Units 126, 127 and 128: one AC each now runs `python ci_emit.py --fixture ...` by basename, as unit 120's ACs do, because `tools/integrations/` is not tracked at this base.
   - Unit 138: AC16 cites the full repo path of the round-3 report; AC34 runs `grep -c 'position' deploy.md` in the `help` folder.
   - Unit 106: the §3 hands-off bullet to DEPL-dShippedRelease-138 quotes S44's Skill sentence in double quotes instead of a double-backtick span.

### Acceptance

Your return names, per spec, what you changed or confirmed. No new requirement enters any spec. Nothing but these six specs changes.

### Gates

`bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,13,23,25` over the staged specs, and no other gate.

### Non-goals

No commit, no index regeneration, no rev bump: unit 133 is at rev-1 and unaudited, and the others carry this round's bump already. Stage your edits. Temp files go under the session scratchpad spelled absolute.
