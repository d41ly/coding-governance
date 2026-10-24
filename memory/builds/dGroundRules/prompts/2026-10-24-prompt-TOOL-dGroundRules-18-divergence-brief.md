**Serves:** research TOOL-dGroundRules-18

# Divergence brief — TOOL-dGroundRules-18, the guard addition reds another build's live spec

## The prompt

> Its builder built the whole unit (saved as a patch in the session scratchpad, `patch18/`) and handed it back as a DIVERGENCE: S4's addition of `{prefix}/workflows/unattended-build.template.js` to the `policy fixtures` guard in `tools/gate-legs.json` reds the `[guards]` arm of `tools/check-spec-tokens.py` on TOOL-aOrientedCast-28 (OPEN), whose §4 touches that template and whose §7 lacks the leg; the next `--dispatch` refused with one unwaived hit. It also measured that `tools/hooks/agent-cap.js` must stay at or under 1971 lines, or TOOL-aOrientedCast-28's citation `:1972-1994` points at a real line again and its waiver row reds as stale.

## The brief

### Goal
Revise `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-18.md` to the run's ruling (a), the option that keeps the guard on the file the case runs. Author only: no product code, no commit, no gate.

### Items
1. A §8 fork, RESOLVED (agent, 2026-10-24, delegated) citing ER:388 and the precedent of TOOL-dGroundRules-10 §8 F7/F8 and TOOL-dTrueNorth-20 F3: S4 keeps the guard addition, and the unit also writes a waiver row keyed `policy fixtures <- tools/workflows/unattended-build.template.js` in `memory/project/spec-token-waivers.txt` (reason naming TOOL-aOrientedCast-28 and this unit's guard widening), an ask row in this build's `BACKLOG.md` asking TOOL-aOrientedCast-28's §7 to carry `policy fixtures` (accepted when it does, which retires the row), and a deviation record carrying `**Bound:**`, `**Tier:**`, `**Reason:**` and `**Surface:**` per `memory/HYGIENE.md` "Deviation records". The commit's `Decided:` trailer carries `widens: memory/project/spec-token-waivers.txt` and `relaxes: spec-token-waivers shrink-only count`. Option (b), handing the guard to TOOL-dGroundRules-20, is refused: that unit does not touch the template, so a template change would go unguarded.
2. §4's files touched adds the waiver registry, `BACKLOG.md` and the deviation record; §7 adds `spec tokens (a spec's own names resolve)` if absent.
3. S4 or §5 states the measured limit: `tools/hooks/agent-cap.js` stays at or under 1971 lines, because TOOL-aOrientedCast-28 cites `:1972-1994` and that row is waived only while the citation falls past the file's end; a criterion or probe names `wc -l` on the file.
4. The comment listing the allowed receivers in `agent-cap.js`, which still names only `gov:fixed-verifiers`, is named in S4's scope so the builder widens it to `gov:fixed-writers` in the pass.
5. The status header's rev rises by one, with a §9 line naming what disagreed and the ruling. Keep the file under 48600 bytes measured with its records region.

### Acceptance
`python tools/check-spec-tokens.py` exits 0 with this spec read as INPROGRESS (the main loop runs it); every `**Carries:**`/`**Derived:**` line, the H1 and the §8 RESOLVED marks survive; every §6 code span sits on one line.

### Gates
No gate runs in this pass.

### Non-goals
Any other spec; product code; the status cell, which stays `DEFERRED`.

### Limitations
The builder's evidence stands: the patch at `patch18/` builds the unit at 1971 lines and passes `limit-hook-writer-split` (4 assertions) and five suite arms replayed.

### Reuse
TOOL-dGroundRules-10's committed waiver rows, deviation-72 and ask TOOL-dGroundRules-108 are the template for each record.
