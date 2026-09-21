# cMendedVintage — the acceptance ledger for unit 16

**Serves:** journal DEPL-cMendedVintage-16

*Node `c`. BACK-FILLED 2026-09-17 by a later pass, NOT by the pass that built the unit — the
filename carries the date of the unit's own commits, `8d5d16f2` and `52f1612f`, 2026-09-16. All four
criteria are arms of ONE function, and that function was replayed standalone against this worktree
at this tip; its six output lines are quoted below. The RED halves were staged by the building pass
and are cited from the spec's own `**Observed:**` lines, which rev-2 wrote in the same commit as the
code — cited AS that pass's record, not re-observed here. No merge bar, no `*.test.sh` and no
self-test runner ran in this pass: `tools/govkit/matrix.py` was imported and one function called,
never its `main`.*

## The one thing worth reading twice

**The unit's load-bearing premise was measured FALSE before a line was written, and that is the most
important thing in its record.** The brief and rev-1 both asserted that a two-term `[[outcome]]`
block matched on `must_not_exist` alone, making S2 — a conjunction fix in `tools/govkit/govkit.py` —
the half that mattered. It already ANDed its terms, and two shipped blocks depended on that. So no
line of `govkit.py` moved, the unit is one descriptor term plus one test function, and rev-2 records
it as divergence (1). This ledger does not improve on that reading; it replays its consequence.

**What the narrowing costs is stated, not hidden.** A target that holds the kit and never ran the
adopter is byte-identical to a failed first scaffold, so no file probe separates them and this block
now reds the rarer one. §4's third row says so and the descriptor comment says so to the adopter.

**Evidences:** DEPL-cMendedVintage-16

- AC1 — `check_outcome_probes` — replayed standalone at this tip against this worktree, calling the
  function in `tools/govkit/matrix.py` directly rather than the acceptance matrix around it. It
  printed `ok   lexicon exit 1 after a failed first scaffold is REFUSED`, with `FAILURES` empty. The
  arm builds the target itself: a scratch `.governance/deploy.toml`, no `.lexicon.conf`, and the
  rendered Skill deleted, then the shipped `lexicon` descriptor through `classify_outcome` and
  `outcome_accepted` at exit 1. The RED is the building pass's record, not this one's: the spec's
  AC1 states it was RED before the narrowing at `means='no-project-layer' accepted=True`, green
  after, and RED again with the `must_exist` term staged back out.
- AC2 — `.claude/skills/lexicon/SKILL.md` — the same replay, second state, printed
  `ok   lexicon exit 1 after a declaration removed after one is ACCEPTED`. The arm writes that Skill
  path under the scratch target and leaves `.lexicon.conf` absent, which is the posture, and the
  verdict is `no-project-layer` accepted. Both states come out of one loop over one descriptor, so
  the pair is a discrimination and not two independent passes.
- AC3 — `must_not_exist` — no separate fixture, by the criterion's own words: AC1's green IS this
  observation. Read at this tip to confirm the shape the criterion needs is the shape that was
  graded: `tools/lexicon/kit.toml` declares
  `probe = { must_exist = ".claude/skills/lexicon/SKILL.md", must_not_exist = ".lexicon.conf" }`, and
  AC1's target satisfies the absence term while failing the presence term. The arm reports REFUSED,
  which an OR could not produce. The engine side was read too and not re-derived: `classify_outcome`
  loops `(("must_exist", True), ("must_not_exist", False))` and breaks on the first term that fails.
- AC4 — `tools/govkit/registry.toml` — the class arm, replayed in the same call. Four lines:
  `ok   accepted stops: the registry declares at least one to grade`, then one per entry for
  `'codebase-map' 'seeded-conf'`, `'lexicon' 'no-project-layer'` and `'memory-tree' 'seed-and-stop'`,
  each asserting the block names a file that must EXIST. Population three, the same three the spec's
  own Observed line names, derived from the registry at run time rather than typed. The two REDs the
  criterion demands — the liveness arm with the population emptied, and the class arm with lexicon's
  `must_exist` staged out — are the building pass's record and were NOT re-staged here, because
  staging either means editing a tracked file and this pass writes only ledgers.

## What this ledger does NOT claim

That the merge bar is green. §7 names five legs. `govkit selfcheck` and `kit version markers` were
replayed at this tip and both exit 0, but neither answers a criterion here. `govkit selftest`,
`lexicon wiring` and the acceptance matrix's own `main` — the five scratch installs the arm above
sits in front of — did not run in either pass and are unobserved for this unit. The arm's placement
before shape 1 is read from the source, not from a run of it.

That the second commit's count was re-measured. `52f1612f` took `tools/lexicon/README.md` from 11
carried kit-path literals back to 10 after the post-unit sentinel caught the rise, and the
`install-prefix (shipped surface)` leg that owns that ratchet did not run in this pass. No criterion
covers it; the commit is the only record.

That an adopter was tested. gov holds no `.governance/install.json`, which the build README states as
the reason nearly every acceptance in this build is a fixture arm. The failed first scaffold this
unit stops accepting has never been produced at a real target — it was produced by handing
`classify_outcome` the state, which is what AC1 grades and all that was ever claimed.
