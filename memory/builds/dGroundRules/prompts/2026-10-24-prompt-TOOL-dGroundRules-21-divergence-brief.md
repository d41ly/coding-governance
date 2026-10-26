**Serves:** research TOOL-dGroundRules-21

# Divergence brief — TOOL-dGroundRules-21, four findings stale against the built branch

## The prompt

> Its builder handed TOOL-dGroundRules-21 back as a DIVERGENCE at HEAD 4ad519f44, nothing written: S36/AC36 need a kit version bump the brief forbids, because unit 10 left `KIT_AGENT_CAP_VERSION` at 1.40 and the markers already equal it; AC6 cites `unattended/unattended.sh:9517` where `read_policy_key()` now sits at :9521; S29 names a `SIZE_LIMITS_NAME` constant that does not exist (`tools/policy/budgets.py:42` spells `LIMITS_NAME`); and AC5 says `arm_schema` and `arm_mirror_readers` print `not graded` over the fresh target, which neither can once the scaffold writes four keys and S26's `requires = ["memory-tree"]` stages that kit's code files. Every other finding was confirmed buildable or already true at HEAD.

## The brief

### Goal
Revise `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-21.md` to the run's rulings below. Author only: no product code, no commit, no gate.

### Items
1. S36, AC36 and §8 F10: the stale-marker finding is already met, so S36 becomes the invariant that every `gov:kit agent-cap@` marker in `tools/hooks/*.js` equals `KIT_AGENT_CAP_VERSION` in `tools/hooks/agent-cap.js`, with no edit and no version bump (the lander mints the version at landing); AC36 observes that equality with one command whose output names the constant's value and the markers' value; F10's RESOLVED mark stays and gains one clause saying what changed.
2. S6 and AC6: the README citation names `read_policy_key()` in `<tool-root>/unattended/unattended.sh` by symbol, with no line number, so a later edit cannot strand it; AC6 greps that symbol form. The other three copies may keep their line numbers only if S6 needs them; prefer the symbol form for all four.
3. S29: name `LIMITS_NAME`, the constant `tools/policy/budgets.py` defines, wherever the spec says `SIZE_LIMITS_NAME`.
4. AC5: state what each arm prints in the fresh target: `arm_schema` grades the four keys the scaffold writes with no finding, `arm_mirror_readers` grades the memory-tree kit's staged code files with no finding, and the reader-coverage arm keeps `not graded`; S5's own sentence stays as it is.
5. S31: say that when the read of the landed revision itself refuses, a cap's value is the handed-in `legacy:` or `default:` value, as the builder read it.
6. The status header's rev rises by one, with one §9 line naming the four disagreements and the rulings. The spec must stay at or under 48600 bytes measured with `wc -c`, including its records region: trim prose outside §6 to pay for any growth.

### Acceptance
`python tools/check-spec-tokens.py` exits 0 with this spec read as INPROGRESS (the main loop runs it); `wc -c` prints at most 48600; every `**Carries:**`/`**Derived:**` line, the H1 and the §8 RESOLVED marks survive; every §6 code span sits on one line.

### Gates
No gate runs in this pass.

### Non-goals
Any other spec; product code; the status cell, which stays `DEFERRED`; any finding the builder confirmed buildable or already true.

### Limitations
The builder's probes at 4ad519f44 stand: S8, S19, S33, the second half of S27, the re-point half of S35 and part of S38 are already true at HEAD.

### Reuse
The builder's return names the current line of each copy and the scaffold's four keys; re-read them rather than re-deriving.
