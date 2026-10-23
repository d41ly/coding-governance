# PLAY-dOrderedCharter-55 deviation 552 — F3's choice widens a bound, recorded so the departures report joins it

**Serves:** deviation PLAY-dOrderedCharter-55

- **Departs from:** dOrderedCharter [fork F3 of PLAY-dOrderedCharter-55]
- **Hand-off:** design-to-spec
- **Before:** the `agent-instructions wiring` leg ships with the agent-instructions entry, to the adopters that selected it
- **After:** the leg moves to the `playbook-render` entry with the wiring the one renderer absorbs, so every `playbook-render` adopter runs it, recorded
- **Cause:** review finding
- **Reason:** F3: limiting the leg to targets that held the retired entry needs a selector a descriptor's `[[gate_leg]]` row does not carry at base, a new descriptor surface; shipping it to every `playbook-render` adopter keeps the wiring checked wherever the renderer writes it, and widens that entry's leg set.
- **Evidence:** the §8 mark of F3 in `memory/builds/dOrderedCharter/spec/2026-10-24-spec-PLAY-dOrderedCharter-55.md`; the fork rungs, `memory/builds/dClosedLoop/build/2026-10-20-build-PLAY-dClosedLoop-1-execution-plan.md:900-946`
- **Risk:** loosening
- **Approver:** spec writer, the gov-spec-writer role of the harness's disposal stage, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** new unit PLAY-dOrderedCharter-55
- **Caused-by:** PLAY-dClosedLoop-2
- **Surface:** the `playbook-render` entry's leg set gains `agent-instructions wiring` for every adopter
