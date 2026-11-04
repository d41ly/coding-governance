# PLAY-dOrderedCharter-3 deviation 31 — F5's interim holds one document out of the envelope arm

**Serves:** deviation PLAY-dOrderedCharter-3

- **Departs from:** dOrderedCharter [fork F5 of PLAY-dOrderedCharter-3]
- **Hand-off:** design-to-spec
- **Before:** S6's first arm reds any registered document with no envelope, with no exception
- **After:** `memory/guides/BUILD-METHOD.md` keeps its row and carries no envelope; the gate prints it as held and not checked on every run, leaves it out of the covered count, and reds once the document carries an envelope or fits its row
- **Cause:** review finding
- **Reason:** the envelope crosses a row whose block reserves its next movement to the owner, so no run raises it, and an open fork stops an unattended build; the hold changes nothing the owner reserves, and the owner's choice among the fork's options stays parked
- **Evidence:** the mark of F5 in `memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-3.md`, and the ask PLAY-dOrderedCharter-66
- **Risk:** loosening
- **Approver:** spec writer, the gov-spec-writer role, under the chain's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask PLAY-dOrderedCharter-66
- **Caused-by:** PLAY-dOrderedCharter-3
- **Bound:** S6's first arm, for the one held row until the owner rules
- **Tier:** strongest, the clause itself says every registered document
