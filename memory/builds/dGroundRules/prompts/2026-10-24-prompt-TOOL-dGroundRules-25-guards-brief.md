**Serves:** research TOOL-dGroundRules-25

# Guards brief — TOOL-dGroundRules-25's guard widening meets aScoutedSeam's live spec

## The prompt

> Before dispatching TOOL-dGroundRules-25, the main loop applied S23 and S24's guard additions to the `policy fixtures` row of `tools/gate-legs.json` in a scratch clone at HEAD 8149b14ec (`{prefix}/gate-legs.json` plus the seventeen in-kit modules the census's Python enforcers import) and ran `tools/check-spec-tokens.py`: one `[guards]` hit, `policy fixtures <- tools/roles/roles_lib.py` on TOOL-aScoutedSeam-1 (SPECCED), whose §4 touches that file and whose §7 lacks the leg. Units 20 and 23 diverged on this class after their builders had built; this brief settles it before the build.

## The brief

### Goal
Revise `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-25.md` so S24 states how its guard widening meets another build's live spec, ruling (a) as in TOOL-dGroundRules-20 §8 F1 and TOOL-dGroundRules-23's revision. Author only: no product code, no commit, no gate.

### Items
1. A §8 fork, RESOLVED (agent, 2026-10-24, delegated) citing ER:388 and the precedent of TOOL-dGroundRules-20 §8 F1: S24 keeps every import and sourced file, and the unit also writes one waiver row keyed `policy fixtures <- tools/roles/roles_lib.py` in `memory/project/spec-token-waivers.txt` (reason naming TOOL-aScoutedSeam-1 and this unit's guard widening; one row more than the registry holds when the unit builds) and a deviation record `memory/builds/dGroundRules/build/2026-10-24-build-TOOL-dGroundRules-25-deviation-76.md` carrying `**Bound:**`, `**Tier:**`, `**Reason:**` and `**Surface:**`, whose follow-through is ask TOOL-dGroundRules-110; no new ask. The builder re-measures the `[guards]` set with its own S24 derivation and waives any further hit the same way, recording each in the same deviation record. The commit's `Decided:` trailer carries `widens: memory/project/spec-token-waivers.txt` and `relaxes: spec-token-waivers shrink-only count`.
2. §4's files touched adds the waiver registry, the deviation record and `memory/guides/SESSION-KICKOFF.md` if absent; §7 adds `spec tokens (a spec's own names resolve)` if absent.
3. The status header's rev rises by one, with a §9 line naming the measured hit and the ruling. The spec must stay at or under 48600 bytes measured with `wc -c` including its records region, which grows by about 300 bytes when this handoff is recorded: trim prose outside §2 and §6 to pay for every byte added; introduce no retirement word in §2.

### Acceptance
`python tools/check-spec-tokens.py` exits 0 with this spec read as INPROGRESS (the main loop runs it); `wc -c` prints at most 48300 before the records region grows; every `**Carries:**`/`**Derived:**` line, the H1 and the §8 RESOLVED marks survive; every §6 code span sits on one line.

### Gates
No gate runs in this pass.

### Non-goals
Any other spec; product code; the status cell, which stays `DEFERRED`.

### Limitations
The main loop's import walk is a regex over each enforcer's source, so S24's own derivation may find more modules; the builder's re-measure covers that.

### Reuse
TOOL-dGroundRules-20's waiver rows and deviation-74 are the template.
