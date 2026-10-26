**Serves:** research TOOL-dGroundRules-32

# Divergence brief — TOOL-dGroundRules-32, a batch the built branch overtook

## The prompt

> Its builder probed TOOL-dGroundRules-32 rev-5 at HEAD 93e4b4d31 and handed it back as a DIVERGENCE before writing anything. S7/AC7 (finding 19) say every step of two or more units holds two units declaring `tools/policy/check_policy.py`, but steps 17 and 18 render `yes` at HEAD and stay `yes` under the spec's own S9/S13 rule, since none of their units' write sets meet and neither step holds a consumes-from edge. S16 (finding 12), with S4, S18 and S20 resting on it, specifies `build_fresh_target(snapshot_root, source_root, kits)`, but `build_install_target(name, ids, answers="")` in `tools/policy/check_policy.py` (unit 25) is already the one install-target builder three cases share, and `KICKOFF_ANSWERS` is the hard-coded answers constant S16's `DEPLOY_FULL` derivation would replace; S20's repository-local identity is already met by `run_fixture_git`'s `-c user.name -c user.email` unless the deployer commits in the target. S19 (finding 22) keeps "word for word" a refusal sentence that `tools/policy/guard.py` no longer prints: it now prints "the mirror renders HEAD and its input {p} is staged changed: commit {p} first, then regenerate". The builder also measured: S5 already holds in substance (PLAN_LINE keeps legacy-homes rows and compares mark and role); S9 does not say whether the two-segment `pathlike` filter survives, and without it three other builds' READMEs flip (aEvidencedLens step 8, aHoistedPass step 2, aRepatriatedFork step 17); S13's re-render moves eight build READMEs to `unknown` (aBlindedTrial, aBoundedCeiling, aBriskPreflight, aTunedCompass, dDerivedDocket, dGaugedVintage, dRetiredFork, dTieredTribunal).

## The brief

### Goal
Revise `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-32.md` to the run's rulings below. Author only: no product code, no commit, no gate.

### Items
1. S7 and AC7 are limited to the steps that hold a `tools/policy/check_policy.py` pair; AC7 pins steps 17 and 18 as `yes` with the reason (no meeting write sets, no consumes-from edge inside the step).
2. S16 extends `build_install_target` in place, never a second builder: its answers derive from `DEPLOY_FULL` in place of `KICKOFF_ANSWERS`, which goes; give the extended signature and say which of apply and check, if either, moves into it. S4 and S18 are restated on that function. S20 is restated as already met through `run_fixture_git`'s identity, with one probe the builder runs to confirm the deployer makes no commit in the target, and the repository-local identity written only if it does.
3. S19 keeps the refusal sentence `tools/policy/guard.py` prints at HEAD, quoted, and appends only the `legacy_blobs` keys to the help section; AC19 matches.
4. S9 states that the two-segment `pathlike` filter survives the switch to `check_writes_intersect`, so no README outside the eight S13 names changes.
5. S13 and §4's files touched name all eight build READMEs the re-render moves to `unknown`, each by path.
6. S5 is restated as already holding at HEAD, with the observation that confirms it.
7. Re-cite every line the builder found moved by symbol where the spec cites it.
8. The status header's rev rises by one, with a §9 line naming the disagreements and the rulings. Keep the file under 48600 bytes measured with its records region, trimming prose outside §2 and §6 if needed; every §6 code span stays on one line; introduce no retirement word in §2; no path inside a code span is followed by a quote or other punctuation, and no code span holds a `rev:path` token.

### Acceptance
`python tools/check-spec-tokens.py` exits 0 with this spec read as INPROGRESS (the main loop runs it); every `**Carries:**`/`**Derived:**` line, the H1 and the §8 RESOLVED marks survive; every §6 code span sits on one line.

### Gates
No gate runs in this pass.

### Non-goals
Any other spec, including TOOL-dGroundRules-34's stale list of READMEs, which the main loop handles before that unit; product code; the status cell, which stays `DEFERRED`.

### Limitations
The builder's probe (`probe_order.py` in the session scratchpad) and its per-finding statuses at 93e4b4d31 stand.

### Reuse
`build_install_target` and `run_govkit` in `tools/policy/check_policy.py` are the seams.
