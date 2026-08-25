**Serves:** journal TOOL-aNamedGesture-1

# Acceptance ledger — TOOL-aNamedGesture-1

*Node a, 2026-08-25. One line per numbered criterion in the spec at rev-4. Two forms and no third:
OBSERVED carries the token that made the observation, AMENDED names the revision that changed the
criterion.*

**Evidences:** TOOL-aNamedGesture-1

- AC1 — `bash tools/unattended/adopt-unattended.sh --check` — exits 0, and
  `grep -cE '\{\{[A-Z_]+\}\}' .claude/skills/unattended/SKILL.md` prints `0`.
- AC2 — `grep -n -- '--prompt' .claude/skills/unattended/SKILL.md` — four hits, at the routing row
  (line 26) and across the opening fence (lines 163, 165, 169).
- AC3 — `bash tools/unattended/adopt-unattended.test.sh` — arm `a blank AUTH_PARAM adopts` plus the
  fence assertion; the suite reports `PASS (53 assertions)`.
- AC4 — `bash tools/unattended/adopt-unattended.test.sh` — arms `a non-default AUTH_PARAM adopts` and
  `a non-default AUTH_PARAM leaves no trace of the kit default`. A fixture declaring `--build` renders
  `--build` at both sites and `grep -c -- '--prompt'` over that render prints `0`.
- AC5 — `bash tools/unattended/check-unattended.sh` — exits 0 with the key declared and its row present.
- AC6 — STAGED BREAK OBSERVED. With the `AUTH_PARAM` row removed from
  `memory/guides/UNATTENDED-PROTOCOL.md`, the leg printed *UNATTENDED check 22 FAILED — the protocol's
  binding key table and the declared conf disagree … undocumented in the protocol: AUTH_PARAM … set by
  this project and undocumented: AUTH_PARAM*, naming the key in two of the join's three directions.
  Restored; `adopt-unattended.sh --check` back to 0.
- AC7 — STAGED BREAK OBSERVED, all four arms. With both guard `case` blocks removed from
  `tools/unattended/adopt-unattended.sh`, every refusal arm failed — bare word, whitespace, pipe and
  backtick each reported *a malformed AUTH_PARAM adopted at exit 0* plus its companion
  *wrote no Skill* assertion. Restored; the suite returned to `PASS (53 assertions)`.
  A SIXTH refusal arm was added at the fold — a value carrying another key's placeholder text,
  `--{{LANDER}}` — and observed RED the same way: with the write-path refusal removed the suite
  reported *a holed render adopted at exit 0* and *a holed render wrote no Skill*.
- AC8 — `awk` slice of `## Start a run from a PROMPT` in the rendered Skill — carries
  `THE VALUE IS THE BUILD`, the fourth grammar row `has whitespace AND names a readable file`, the
  rule `goes to a RECORD, never into this README`, and the provenance clause `the path it came from`.
- AC9 — `grep -n 'placeholders\|optional_keys' tools/unattended/kit.toml` — `AUTH_PARAM` and
  `ANCHOR_SCOPE` present in the SKILL render's `placeholders` and in `[config] optional_keys`.
- AC10 — `bash tools/check-kit-versions.sh` — exits 0, and `git grep -l 'unattended@1.9'` prints
  nothing across the whole tree. Eight carriers now read `1.10`.
- AC11 — PARTLY OBSERVED, and the shortfall is named rather than folded away.
  `bash tools/unattended/adopt-unattended.test.sh` exits 0 at `PASS (53 assertions)`, including the
  new fixture self-assertion that its render carries no surviving brace shape.
  `bash tools/unattended/cross-component.test.sh` exits 1 — on arm 5, with
  `UNATTENDED check 30 FAILED — check 30 walked no build whose --plan returned a verdict`. ATTRIBUTED
  by baseline rather than assumed: a throwaway worktree at BASE `381008a1` runs the same suite to five
  FAIL lines with the identical message on arms 3 and 3b, so the red predates this unit and this tip
  fails fewer arms than its base. Filed as `TOOL-aNamedGesture-3`. This criterion is therefore
  satisfied for the half this unit owns and OPEN for the half it does not.
- AC12 — `bash skills/session-kickoff/manifest-check.sh` — exits 0 after the `.unattended.conf` and
  `.memory-tree.conf` edits and the `last-audit` re-stamp.
- AC13 — AMENDED rev-5, then OBSERVED. The criterion as written at rev-4 was graded by re-typing a
  measurement, and the measurement was stale within this build: the real figure at the fold is 3 B
  larger, so the ceiling of 139132 carried a 253 B margin against a declared 256 while both carriers
  agreed with each other. Round 1 L2. The witness is now the command, not a number:
  `bash tools/memory-tree/check-memory-hygiene.sh` exits 0, and
  `python tools/memory-tree/corpus_ids.py --report` subtracted from `READ_PATH_CEILING` in
  `.memory-tree.conf` gives exactly 256. Ceiling now 139135.
- AC14 — `bash tools/run-gates/run-gates.sh` — PENDING-BAR.

## What the criteria did NOT prove, stated rather than implied

- **Nothing verifies that a real invocation carried the token.** No script in this kit sees an
  invocation, and the spec's section 3 says so. Every criterion above grades the RENDER, the CONF
  CHANNEL or a REFUSAL — never the gesture itself.
- **The value grammar is graded as PROSE, not as behaviour.** AC8 asserts the rendered Skill states
  the four readings; no arm exercises an agent resolving a path, refusing an unresolvable one, or
  refusing the ambiguous whitespace-and-readable-file case. Those are instructions to a reader, and
  this kit has no machine half for them.
- **The `prompts/` carry rule is likewise ungated.** AC8 asserts the Skill says it. Whether a run
  actually writes the record there is enforced only by the memory-tree hygiene gate at the moment
  such a run commits, which no arm in this unit simulates.
