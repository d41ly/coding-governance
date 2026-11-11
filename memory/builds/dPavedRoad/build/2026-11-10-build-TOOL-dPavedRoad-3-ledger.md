**Serves:** journal TOOL-dPavedRoad-3

# TOOL-dPavedRoad-3 — acceptance ledger

The unit as built, at spec rev-1, in commit 179d31359. `READ_KEYS` in `tools/roles/roles_lib.py`
gains `brief:prompt`; `render_handoff` in `tools/roles/handoff.py` reads it from the brief record's
`## The prompt` section through `extract_card_section`, every other `brief:` key still reading its
sub-head under `## The brief`; `gov-spec-writer` reads `brief:prompt` first, required. The roles
catalogue region was re-rendered, `help/roles.md` step 3 gained its sentence, and
`tools/roles/adopt-roles.test.sh` gains arm 19 with two assertions, its floor moving 51 to 53.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in the pass. The builder observed each
criterion with the spec's own probes over a scratch fixture, transcribed below from its return.

Owed at the close: the RED-first observation of arm 19 in `tools/roles/adopt-roles.test.sh` (AC2)
and the section 7 legs.

**Evidences:** TOOL-dPavedRoad-3
- AC1 — `bash tdp3-render.sh` printed a `### brief:prompt` block holding the brief's prompt line, ending at `### brief:goal`.
- AC2 — `python -B tdp3-probe.py <repo> <scratch fixture>` printed as its second line `rendered '### brief:prompt\n\n> owner words, verbatim\n— owner, 2026-11-10\n'`.
- AC3 — the same probe printed as its first line `vocabulary True, first read brief:prompt`, and as its third a `refused brief:prompt` line naming the brief record.
- AC4 — `grep -c 'spec | brief:prompt, brief:goal' tools/roles/README.md` printed 1.
- AC5 — `grep -c 'brief:prompt' help/roles.md tools/roles/handoff.py` counted 1 in each file.

## New arm, observed at the close

In clones of `6681cdc80` under `%TEMP%/dpr`, by the main loop, `bash tools/roles/adopt-roles.test.sh`.
RED: with the dispatch reverted so `brief:prompt` reads a `### prompt` sub-head, it exited 1 in 83 s
with one failure, `arm 19 the spec writer's handoff carries the brief's prompt verbatim`. GREEN: at
`6681cdc80` it exited 0 in 101 s, `PASS (65 assertions)`, above the floor of 53.

## Renumbered at the landing reconcile

Reconciling onto origin/main at `1fef61174`, `tools/roles/adopt-roles.test.sh` already held an arm 19
from TOOL-aProfiledEffort-2 and arms 20 and 21 from TOOL-aGuardedEffort-1. This unit's arm moved
below them as arm 22, unchanged but for its label and locals, the spec's references followed it, and
`FLOOR_ASSERTIONS` became 61: main's 59 plus this arm's two. The RED and GREEN observations above
were made under the old label, arm 19.
