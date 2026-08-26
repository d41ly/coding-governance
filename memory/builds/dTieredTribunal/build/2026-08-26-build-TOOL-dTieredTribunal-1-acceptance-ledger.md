**Serves:** journal TOOL-dTieredTribunal-1 TOOL-dTieredTribunal-2 TOOL-dTieredTribunal-3

# Acceptance ledger — the three units of dTieredTribunal

*Node `a`, 2026-08-26, over `da9e4cd2..634a7fbf`. One line per numbered criterion, in the two forms
`memory/HYGIENE.md` admits and no third. Every OBSERVED line names the token that made the
observation; every AMENDED line names the revision that changed the criterion. The gate reads shape
and coverage only — it does not assert that a token names anything real or that the observation was
actually made — so these are claims I am accountable for, not verdicts a machine reached.*

**Evidences:** TOOL-dTieredTribunal-1

- AC1 — `grep -n "required: \['path', 'summary'\]" tools/workflows/tier2-review.js` — returns no
  match; the four-key form is at `:395`.
- AC2 — amended rev-3 — the `:390` line pin was dropped, because this unit's own S6 comments move
  the block before the criterion is answered. Logged in section 9's rev-3 entry, finding 17.
- AC3 — `grep -n 'blockers: null' tools/workflows/tier2-review.js` — three hits, at the
  all-lenses-dead, nothing-raised and everything-refuted exits. No exit carries a zero for either
  field.
- AC4 — `grep -n 'synth ?' tools/workflows/tier2-review.js` — the ternary on both fields, so a falsy
  `synth` resolves to `null` and never to `undefined` or `0`.
- AC5 — `grep -n "OPENING IS ORDERED" tools/workflows/tier2-review.js` — the prompt states the
  opening order and names all four elements that precede the body, and the binding-line sentence at
  `:357` keeps its first-line role.
- AC5b — read at HEAD — the prompt states the closed set `CLEAN`, `CLEAN WITH FIXES`, `BLOCKED` and
  states that it is closed. The three tokens are the ones `tools/memory-tree/check-memory-hygiene.sh`
  grades at check 22.
- AC6 — read at HEAD — the prompt defines `blockers` AND `highs`, each as a count of confirmed
  findings at that severity, naming the synthesis pass as the adjudicator.
- AC7 — `grep -n 'dTieredTribunal-1' tools/workflows/tier2-review.js` — seven hits, matching the
  seven sites S6 enumerates.
- AC11 — read at HEAD — the `note` ternary tests `!synth` first.
- AC8 — `bash tools/check-kit-versions.sh` — exit 0, and `tier2-review@1.3` sits on line 3 beside
  `version: '1.3'`.
- AC9 — `node tools/workflows/check-workflow-syntax.js` — exit 0, three scripts parsed clean.
- AC10 — `bash tools/workflows/check-review-join.sh` and `bash tools/workflows/check-verifier-fanout.sh`
  — both exit 0 over the edited file.

**Evidences:** TOOL-dTieredTribunal-2

- AC1 — `ls memory/gotchas/ | grep -i fold` — returns `fold-text-is-unreviewed-surface.md`, where
  the same command exited non-zero with no output before this unit.
- AC2 — `python tools/memory-tree/gotchas.py --check` — exit 0. It redded first with check 18, the
  record having declared no gate in a phrasing `declares()` accepts; that was fixed before this line
  was written.
- AC3 — `python tools/memory-tree/gotchas.py --for-paths memory/builds/dFramedEntrypoint/spec/2026-08-24-spec-dFramedEntrypoint-1.md`
  — prints `1 class(es) selected by an anchor`, where it printed `0` before. The first attempt printed
  `0` because the `/spec/` anchor had never been written as a backticked token; AC3 is what caught it.
- AC3b — `python tools/memory-tree/gotchas.py --for-paths memory/builds/dHonouredPark/spec/2026-08-25-spec-dHonouredPark-1.md`
  — the class is selected under a second, different build.
- AC3c — `python tools/memory-tree/gotchas.py --for-paths memory/builds/dTieredTribunal/README.md` —
  the class is NOT selected. The refused `memory/builds/` anchor would have taken that path and the
  taken `/spec/` anchor does not, which is what makes this negative discriminate.
- AC4 — `python tools/codebase-map/test_codebase_map.py` exit 0 ·
  `grep -n fold-text-is-unreviewed-surface memory/map/features/build-method.md` returns the claim ·
  the same grep over `memory/map/baseline.toml` returns nothing.
- AC5 — `bash tools/memory-tree/check-memory-hygiene.sh` exit 0 and
  `python tools/codebase-map/test_codebase_map.py` exit 0, both with the record staged.
- AC6 — `grep -n 'dFramedEntrypoint' memory/gotchas/fold-text-is-unreviewed-surface.md` returns the
  citation, and `git ls-files --error-unmatch` resolves the file it names.

**Evidences:** TOOL-dTieredTribunal-3

- AC1 — `grep -nE 'lensesDead|skepticsDead|spurious|conflicts|duplicates|note:' tools/workflows/drift-audit-state.js tools/workflows/drift-audit-code.js`
  — every token returns hits in both files, where the same grep exited non-zero with no output before.
- AC2 — read at HEAD — neither return contains `lensesRun: LENSES.map((L) => L.slug)`, and both
  source `lensesRun` from `lensOut.length`, the post-`filter(Boolean)` survivor array.
- AC3 — read at HEAD — `spurious++`, `duplicates++`, and `vmap.delete(id)` over the conflict set. A
  demoted finding's reason names the disagreement instead of `no verdict returned`.
- AC4 — read at HEAD — the guard is spelled `LENSES.length > 0 && lensesDead === LENSES.length` in
  both files, above each `const synth = await agent(` call, and a zero-length set reaches its own
  branch with its own note.
- AC5 — read at HEAD — `if (!synth) {` logs every confirmed and unverified finding before the return.
- AC6 — `node tools/workflows/check-workflow-syntax.js` — exit 0.
- AC7 — `bash tools/workflows/check-review-join.sh` and `bash tools/workflows/check-verifier-fanout.sh`
  — both exit 0 over both edited files.
- AC8 — read at HEAD — all THREE top-level exits per sibling name all seven of `lensesRun`,
  `lensesDead`, `skepticsDead`, `conflicts`, `duplicates`, `spurious` and `note`. Verified by
  matching each `return {` against a close at the same indent, after a first probe over-matched the
  `.map()` callbacks and had to be replaced.
- AC8b — `grep -n 'dTieredTribunal-3' tools/workflows/drift-audit-state.js tools/workflows/drift-audit-code.js`
  — seven hits per file, one adjacent to each ported guard, each naming the unit that earned it.
- AC9 — `bash tools/check-kit-versions.sh` exit 0, and
  `grep -rn 'drift-audit@1\.6' tools/drift-audit/ tools/workflows/` returns nothing.
- AC11 — read at HEAD — both `note` ternaries test `!synth` first.
- AC12 — `grep -c 'RUN INTEGRITY' tools/workflows/drift-audit-state.js tools/workflows/drift-audit-code.js`
  — one hit each; both synthesis DATA blocks interpolate the lens and skeptic survival counts, the
  spurious, duplicate and conflict counts, and the instruction not to read a zero as positive
  evidence when lenses died.
- AC9b — read at HEAD — `tools/drift-audit/README.md` carries a `Migrating 1.6 → 1.7 (breaking,
  one RETURN field)` paragraph leading with the `lensesRun` array-to-integer change, then the additive
  fields, then the early return.
- AC10 — read at HEAD — `memory/map/features/review-harnesses.md` no longer claims any of the ten
  clauses S10 enumerates, and its `args` bullet names both siblings and both line numbers.

## What this ledger does NOT evidence

Two things, stated because a ledger that only records successes is a checkbox exercise.

`TOOL-dTieredTribunal-1` did not deliver the build's headline goal, and no criterion above claims it
did. One harness driving every review kind is the parked proposal, and while it stays parked the
returned blocker count reaches a `diff-review` round and never the spec-audit loop the build method
bounds by that number.

The closing review's D1 and D2 were fixed and NOT left-shifted into a gate or a `memory/gotchas/`
class, which `BUILD-METHOD.md` M8 requires. `TOOL-dTieredTribunal-5` carries the class and the run
parked the decision. No criterion here covers that gap, and none should: it is an incompleteness
against a binding rule, and dressing it as satisfied is exactly what the AMENDED form exists to
prevent.
