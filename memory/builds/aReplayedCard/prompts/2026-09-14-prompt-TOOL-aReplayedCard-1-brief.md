# Brief — TOOL-aReplayedCard-1, the commit deny

**Serves:** journal TOOL-aReplayedCard-1

What this pass is handed: the unit's spec at rev-4 — three audit rounds, the last NON-CONVERGENT
and disposed by FOLD, so read §8's three delegated marks and §9's rev-4 line before anything
else — the build README, `tools/hooks/scratch-guard.js` (394 lines: `buildCommandView` at 146–187,
`readTokenAt` at 190–210, `buildComparablePath` at 63, the deny protocol at 370–390) and its
self-test (243 lines, `FLOOR_ASSERTIONS=60`, no git fixture today), and the writer as
`KICK-aReplayedCard-1` and `-2` left it: `skills/session-kickoff/manifest-check.sh --card --write`
writes the card with the header line `orientation — <sid> · written <iso> · by manifest-check.sh
--card --write`, the replay-written card names `--card --replay` there, and `--card --append`
rewrites the `tree —` cell and replaces the READY line and the body.

What it builds: one check in `scratch-guard.js`, its arms, the README section, and one guard
entry in `tools/gate-legs.json`.

What is not obvious:

- **The step-3 base blob is `c95fe32a`.** AC10 runs the writer from
  `git show c95fe32a:skills/session-kickoff/manifest-check.sh` extracted into the fixture, because
  `KICK-aReplayedCard-2` edited the live file in this same step; the live file at HEAD now carries
  the append too, and the arm must not depend on it. Read the ledger at
  `memory/builds/aReplayedCard/build/2026-09-14-build-KICK-aReplayedCard-1-1-acceptance-ledger.md`
  for the card's exact bytes and the spelling of the `tree —` cell.
- **The predicate has ONE order, §4's list**: shape, `agent_id`, missing fields, unwalkable
  target, absent-or-replay card, then the sentinel-or-mismatch test, and only then the exemption
  spawns. The witness lines on exit 0 reach the debug log and the self-test only; do not claim
  more anywhere, and record in the header that this departs from the file's "Allow = print
  nothing" line.
- **The drive fold is `buildComparablePath`'s own step**, applied to the `-C` value and to `cwd`
  BEFORE the walk and to both toplevels before the compare; no second normaliser. A `-C` value is
  read from the ORIGINAL command at the offset the blanked view located, through `readTokenAt`; a
  quoted run in the view is one token.
- **The common dir from a linked worktree's `.git` FILE**: `gitdir:` then `commondir` inside it,
  relative paths resolved against the gitdir; `agent-cap.js:1512` walks this already — read it,
  reuse its shape, and pin the file branch with the fixture's `git worktree add`.
- **`SECOND_ANCHOR_MODES` lives at `tools/unattended/unattended.sh:497`**; the accepted
  `authorized-by:` values are that set, and the parity arm reads the constant from the driver's
  source rather than restating it.
- **The fixture is a scratch repository under the suite's `mktemp -d`**: `git init`, one commit,
  `git worktree add`; every payload `cwd` is `node -p process.cwd()` run inside the fixture, never
  the MSYS path; session ids carry the `sgtest-` prefix and AC11 lists this repository's real
  common dir afterwards.
- **The arm rule**: a present-card ALLOW asserts stderr byte-EMPTY; absence, replay, unwalkable
  and exemption ALLOWs assert their witness line by text; every DENY asserts the card path and the
  remedy by text. Add a stderr-asserting `run` variant beside the existing helper at lines 33–50,
  whose liveness comment is the model for it.
- **The class arm extracts inline `git ` spans from `skills/session-kickoff/SKILL.md` Steps 0–4**,
  prints its count, holds a floor of 8 PINNED at base, and REFUSES on zero; the near-miss and
  value-flag literals are in AC9.
- **`tools/gate-legs.json`**: the `scratch-guard self-test` leg's `guard` gains
  `skills/session-kickoff/`; nothing else in the manifest moves. The `run-gates canary` leg refuses
  a guard naming an untracked path; that one is tracked.
- **Function names are graded by the js probe cell**: `checkOriented`, `readCard`,
  `resolveToplevel`, `resolveCommonDir`, `extractCommitTarget`, `checkAuthorizedReadme`; constants
  `COMMIT_SHAPED`, `GIT_VALUE_FLAGS`, `ANCHOR_MODES`. The hook's existing exports at line 394 gain
  nothing unless the self-test needs one.
- **The hook is LIVE in this worktree the moment you save the file** — `.claude/settings.json`
  runs the working-tree copy on every Bash call. Your own `git commit` goes through it: with no
  card for your session it allows with the witness line, and that is the designed state; if you
  see a deny, read its stderr before anything else, because it names the condition.
- **The acceptance ledger** is `2026-09-14-build-TOOL-aReplayedCard-1-1-acceptance-ledger.md` under
  `build/`, `**Serves:** journal TOOL-aReplayedCard-1`, AC1–AC12 in the OBSERVED form with every
  backticked token on the bullet's first physical line.
- **Author with the Write tool, LF; count CR bytes with `tr -dc '\r' | wc -c`**. Finish with the
  records: spec status CLOSED with today's date, `gen_build_index.py --write`, `git add -A`, the
  hygiene gate (minutes, never through `tail`), `python tools/check-spec-tokens.py`,
  `bash tools/hooks/scratch-guard.test.sh`, `bash tools/check-hook-destinations.sh`,
  `bash tools/run-gates/run-gates.sh` scoped, and commit with the unit id in the subject. No push,
  no merge.
