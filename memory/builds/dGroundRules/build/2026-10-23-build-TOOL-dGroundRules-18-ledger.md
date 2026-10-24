# TOOL-dGroundRules-18 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-18

No merge bar, no gate leg and no self-test suite ran in this pass; the lexicon's `--suggest` answered
OK for `readWriterBound` and `write_limit_stub`. AC1 to AC4 were observed by the kit's fixture CLI
on the built tree, `python -B tools/policy/check_policy.py --fixture limit-hook-writer-split`, one
repository per landed limit under the system temp directory: `4 assertion(s) executed · 0 wrong`,
exit 0. AC5 and AC6 are probes of the files this pass writes. The two `New arm:` lines' red-first
observations, and the §7 legs, are the close's.

**Evidences:** TOOL-dGroundRules-18
- AC1 — `node tools/hooks/agent-cap.js --only=scripts` — the case renders
  `tools/workflows/unattended-build.template.js` at 6 under a landed limit of 6 and pipes it through
  the fixture's copy of the hook with the fixture as the working directory: exit 0, stderr empty. The
  red condition, observed on this tree: HEAD's render, its split carrying `gov:fixed-verifiers`,
  piped through the new hook from the repository root exits 2; the new render and
  `tier2-review.js`, `drift-audit-code.js` and `drift-audit-state.js` each exit 0, the landed limit
  here being 6 (`policy.py get runtime.agents-in-flight`).
- AC2 — `gov:fixed-writers` — the same render under a landed limit of 4 exits 2, the reason at the
  fan-out line reading "`specGroups` carries gov:fixed-writers but its bounded split names a cap
  which this file does not show to be bounded — its K SPEC_WRITERS resolves to 6, above the bound 4:
  runtime.agents-in-flight". The case asserts the marker, "resolves to 6" and
  "above the bound 4: runtime.agents-in-flight".
- AC3 — `MAX_VERIFIERS` — a script whose `gov:fixed-verifiers` split has K = 6, under a landed limit
  of 6, exits 2 with "`g` carries gov:fixed-verifiers but its bounded split names a cap which this
  file does not show to be bounded — its K K resolves to 6, above the bound 5: MAX_VERIFIERS".
- AC4 — `policy-mirror.js` — with the fixture's `policy-mirror.js` removed, the render at 6 exits 2
  with "… its K SPEC_WRITERS resolves to 6, above the bound 5: MAX_VERIFIERS, as no policy kit sits
  beside this hooks kit". A probe from a working directory in no repository printed the reader's own
  refusal line: "carries gov:fixed-writers but the agent limit could not be read: policy: refused ·
  .governance/policy.json:0 · <dir> is in no git repository", exit 2.
- AC5 — `wc -l < tools/hooks/agent-cap.js` printed 1971, the ALLOWED receivers comment's added line
  paid for by a two-line comment above `WRITER_MARK`; and
  `grep -c "^policy fixtures <- " memory/project/spec-token-waivers.txt` printed 1, the registry at
  37 lines (29 rows), its row naming TOOL-aOrientedCast-28, ask TOOL-dGroundRules-109 and deviation 73.
- AC6 — `gov:fixed-writers` — `grep -A6 "ALLOWED receivers" tools/hooks/agent-cap.js` printed
  receiver (a)'s third line, "identifier bound in this file to one — or marked `gov:fixed-writers`,
  the same shape with K at most", followed by "the landed agent limit (MAX_VERIFIERS with no policy kit)".

The suite's writer-split block, replayed outside the suite by a scratch script over a copy of the hook
beside a stub `policy-mirror.js`, printed `6 passed, 0 failed`: a writer split above a stub limit of 4
refused twice over (the marker, and "resolves to 6, above the bound 4: runtime.agents-in-flight"), the
control at a stub limit of 6 admitted, a verifier split at 6 refused against `MAX_VERIFIERS`, a line
carrying both markers refused as "so its bound is ambiguous", and a writer split with no helper
refused against `MAX_VERIFIERS`. `limit-hook-settings-over`, rerun now that rule 7 reads the helper's
path from the one constant, printed `4 assertion(s) executed · 0 wrong`.

Owed at the close, observed by no command in this pass:

- Both `New arm:` lines of §7, each RED on its staged break and GREEN restored; the suite's fifth arm,
  the helper-absent writer split, is beyond the second line's AC2 and AC3 and owes the same.
- The §7 legs over the built tree, `verifier fan-out`, `policy fixtures` and
  `spec tokens (a spec's own names resolve)` among them; the last grades the waiver row against the
  guards join's hit on TOOL-aOrientedCast-28, which no command of this pass observed directly.
