# TOOL-dFairHearing-50 deviation 502 — five review policy keys move to the build that owns their reader

**Serves:** deviation TOOL-dFairHearing-50

- **Departs from:** dFairHearing [policies]
- **Hand-off:** design-to-spec
- **Before:** the catalogue rows of `review.opt-in`, `review.design-audit.runs`, `review.design-audit.seed`, `review.unclassed` and `review.twin` name `dFairHearing` as owner, so `policy check` grades each for a reader once this build's specs are all terminal.
- **After:** the five rows name `dDeclaredLoop`, and `policy check` grades them when that build lands. The catalogue header and the policy README state the exception.
- **Cause:** builder discovery
- **Reason:** this build's specs carry these keys to the harness as pin arguments, and spec 11's non-goal leaves the policy file read to dDeclaredLoop's `review.trigger`. No reader exists here, so the arm reds at this build's last CLOSED flip. The move defers coverage rather than dropping it: the arm reds a key with no reader by name at dDeclaredLoop's landing. This loosens the gate for this build's lifetime.
- **Evidence:** the bar at `57b1cf127`, whose `policy check` leg named the five keys; `memory/builds/dFairHearing/spec/2026-11-05-spec-TOOL-dFairHearing-50.md`, S16 and AC16; `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-20.md`, whose S2 reads two of the five.
- **Risk:** loosening
- **Approver:** spec writer, the gov-spec-writer role of the run's promotion stage, under the build's `author-recorded` value (`PLAY-dClosedLoop-4`)
- **Follow-through:** ask TOOL-dFairHearing-51
- **Caused-by:** PLAY-dClosedLoop-2
