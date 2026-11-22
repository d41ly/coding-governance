# TOOL-dWitnessedBar-1 leg-tail 9 — policy check failed in run unattended-179529481580044524711-1640412

**Serves:** leg-tail TOOL-dWitnessedBar-1

- **Leg:** policy check
- **Hash:** 438cfa6a96a04a32602c2beb23bb053f320403de
- **Run:** unattended-179529481580044524711-1640412
- **Sha:** f9ee3f8e0f2e994c7bad52ae0779fcf31c9c94db
- **Cause:** run:dWitnessedBar

```
# run-gates | leg policy check | exit 1
policy-check: arm_schema · 0 finding(s) · 6 key(s) of .governance/policy.toml against 274 row(s)
policy-check: arm_shape · 0 finding(s) · 274 row(s), 20 set-valued, 11 never-empty
policy-check: arm_summaries · 0 finding(s) · 226 of 274 row(s) unsummarised · base c2a407b0390f (merge-base of HEAD and origin/main) carried 242, the list carries 226
policy-check: arm_direction · 0 finding(s) · 20 loop bound and deadline row(s)
policy-check: arm_on_invalid · 0 finding(s) · .governance/policy.toml at f9ee3f8e is valid
policy-check: arm_mirror_parity · 0 finding(s) · 260 key(s) of .governance/policy.json against its render at HEAD
policy-check: arm_mirror_landed · 0 finding(s) · 5 key(s) the policy file sets at c2a407b0, the helper against the reader
policy-check: arm_mirror_readers · 0 finding(s) · 303 tracked code file(s) outside tools/policy/, the memory root, help/ and the self-tests
policy-check: arm_legacy_homes · 0 finding(s) · 113 row(s) derived from the legacy homes · no base compare: no memory/project/legacy-homes.txt at c2a407b0390f (merge-base of HEAD and origin/main); only the derivation is compared
reader coverage: graded 84 of 274 catalogue key(s); landed owners: aNimbleMend, aTrimmedWait, dDeclaredLoop, dFoldedAudit, dGroundRules, dOrderedCharter, dPlacedRequest, dSafePassage
reader coverage: deviation.approval (owner dDeclaredLoop) declared outside the scan at memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-deviations.py: the chain applies the approval route in this instrument at the value PLAY-dClosedLoop-4 fixed, author-recorded; no tracked code passes the key to a policy reader
policy-check: arm_reader_coverage · 3 finding(s) · 84 of 274 catalogue key(s) graded for a reader
  reader coverage: placement (owner dPlacedRequest, landed at c2a407b0) has no reader
  reader coverage: placement.check (owner dPlacedRequest, landed at c2a407b0) has no reader
  reader coverage: patch.ratify (owner dPlacedRequest, landed at c2a407b0) has no reader
policy-check: arm_limits_readers · 0 finding(s) · 303 tracked code file(s) outside tools/policy/, the memory root, help/ and the self-tests
policy-check: arm_cap_census · 0 finding(s) · 34 census row(s) joined to their enforcers and cases, 0 announced · 13 request(s) in 303 tracked code file(s) · 7 row(s) of tools/template-size-limits.txt
```
