**Serves:** research TOOL-dGroundRules-34

# Rename and size brief — TOOL-dGroundRules-34 against TOOL-dGroundRules-32 rev-6

## The prompt

> TOOL-dGroundRules-32 rev-6 rules that no second install-target builder is added: S16 extends `build_install_target(name, ids)` in `tools/policy/check_policy.py` in place, returning `(target, snapshot)` with answers read from `DEPLOY_FULL`; `build_fresh_target` never exists. Its hands-off edge to this unit names `build_install_target`, and the spec-tokens `[handoff]` arm reds because this spec names `build_fresh_target` (S22, the consumes-from edge, and the §4 sketch at `build_fresh_target(snapshot_root, source_root, kits):`). TOOL-dGroundRules-32's builder also measured that its S13 re-render moves eight build READMEs to `unknown` (aBlindedTrial, aBoundedCeiling, aBriskPreflight, aTunedCompass, dDerivedDocket, dGaugedVintage, dRetiredFork, dTieredTribunal), where this spec's §4 pins seven; and TOOL-dGroundRules-30's writer found this spec's S30 citing `tools/workflows/check-verifier-fanout.sh:213-214`, now at :207-208. The spec measures 48628 bytes, over the 48600 working ceiling.

## The brief

### Goal
Revise `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-34.md` to name `build_install_target` with its rev-6 signature, the eight READMEs, the moved citation, and bring it to at most 48300 bytes. Author only: no product code, no commit, no gate.

### Items
1. Replace each `build_fresh_target` with `build_install_target`, restating the §4 sketch and S22 on `build_install_target(name, ids)`, keeping each sentence's meaning.
2. The README list §4 pins names all eight by path.
3. S30 cites `check-verifier-fanout.sh` by symbol or at :207-208.
4. Trim prose outside §2 and §6 to bring the file to at most 48300 bytes measured with `wc -c` after the rev bump and §9 line; touch none of AC11, AC12, AC15, AC16, AC32 or AC36, which later units restate whole.
5. The status header's rev rises by one, with one §9 line naming the rename, the README list, the citation and the trim; no design change. Every §6 code span stays on one line; introduce no retirement word in §2; no code span holds a path glued to a quote or a `rev:path` token.

### Acceptance
`grep -c build_fresh_target` on the spec prints 0; `wc -c` prints at most 48300; `python tools/check-spec-tokens.py` exits 0 with this spec and TOOL-dGroundRules-32 read as INPROGRESS (the main loop runs it).

### Gates
No gate runs in this pass.

### Non-goals
Any other spec; product code; the status cell, which stays `DEFERRED`; the five criteria named in item 4.

### Limitations
None beyond the items.

### Reuse
TOOL-dGroundRules-32 rev-6's S13 and S16 are the sources.
