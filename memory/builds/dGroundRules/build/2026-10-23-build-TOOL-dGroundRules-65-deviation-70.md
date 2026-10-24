# TOOL-dGroundRules-65 deviation 70 — the re-rendered mirror left out of the pass commit, which the policy guard refuses

**Serves:** deviation TOOL-dGroundRules-65

- **Departs from:** TOOL-dGroundRules-65@rev-3 [§4 Files touched]
- **Hand-off:** spec-to-code
- **Before:** §4 Files touched names `.governance/policy.json`, and §5 says the mirror is re-rendered in this unit's commit, the bytes AC2 reads with `git show`.
- **After:** the pass commit carries the code that renders `{rev}` and leaves `.governance/policy.json` as TOOL-dGroundRules-5 rendered it, stale against the new render until TOOL-dGroundRules-19 admits a regenerated mirror and it is committed.
- **Cause:** builder discovery
- **Reason:** since TOOL-dGroundRules-6 the pre-commit hook runs `guard.py --staged` on an agent's commit staging a path `guarded-paths.txt` lists, the mirror among them, and admits no change but one raised measured-file cap; `--dispatch` also refused the mirror declared beside its generator `tools/policy/policy.py`. The spec predates the guard. The committed mirror's blob ids still match, so the helper reads the same values; only its reasons name an older revision, as they did before this unit.
- **Evidence:** `tools/policy/guard.py` and `tools/policy/guarded-paths.txt` at `0cfed8ae5`; the `--dispatch` refusal, check 49, "a generated index together with its generator"; `2026-10-23-build-TOOL-dGroundRules-65-ledger.md`, AC2.
- **Risk:** editorial
- **Approver:** author, the gov-builder role of this unit's harnessed build stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit TOOL-dGroundRules-19
- **Caused-by:** TOOL-dGroundRules-6
