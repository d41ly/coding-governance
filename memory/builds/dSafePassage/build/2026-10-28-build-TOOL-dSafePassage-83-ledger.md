**Serves:** journal TOOL-dSafePassage-83

# TOOL-dSafePassage-83 — acceptance ledger

The unit as built, at spec rev-6, over the pass's parent `201eb127c`, which carries the writer
pass's S1 lines and S3's re-wrap. S2: the ledgers of TOOL-dSafePassage-9, -13, -15, -21, -26 and -31
gain `**Evidences:**` before their first `AC` line. TOOL-dSafePassage-11's ledger already wrote its
13 observations as `- **AC<n>**` bullets under "HOW EACH CRITERION WAS OBSERVED", each carrying the
backticked command or file of its observation, so the opening line before `- **AC1**` makes them the
block of 13 S2 asks for, without a second copy of each. TOOL-dSafePassage-51's gains
`- AC2 — amended rev-4 — …`. S3: the eight ledger answers of §4 "The nine answers" each carry the
token the table names. S4: `memory/guides/SESSION-KICKOFF.md` §B gains the floor bullet, and
`last-audit` and `last-body-change` advance to `201eb127c`.

Opening the six blocks graded answers check 23 had never read, and seven of them were red. Each is
answered here in its own ledger, because AC3 and AC6 refuse any check 23 line naming one of the
eight units. TOOL-dSafePassage-21 AC2 is re-wrapped so no backticked span crosses a line, a
whitespace-only edit. TOOL-dSafePassage-26 AC12 spells the command as its criterion does. AC18
names the grep it ran, and records that at this pass head it prints nothing: since
TOOL-dSafePassage-67 (`f64d1302d`) the factory's line reads `"--template="` between `"-q"` and
`"-b"`. AC43 cites TOOL-dSafePassage-41's `ac-order` observations. AC48 and AC49 name their commands,
re-run at this pass head with the same counts. AC23 was OWED with no token. It was re-observed in unit
8's AC5 fixture, rebuilt under `%TEMP%/sp83`, and its line says so. TOOL-dSafePassage-11 AC4 spells
`bash "tools/lib/python-floor.sh" preflight` as its criterion does.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. On node a (Windows, Git
Bash), by the spec's own probes in this worktree. `ledger_check.py` is §4 "The probes" verbatim,
extracted to the session scratchpad.

**Evidences:** TOOL-dSafePassage-83
- AC1 — `grep -cE '^- \*\*hands-off\*\* .TOOL-dSafePassage-6[789]'` over the specs of TOOL-dSafePassage-5, -11 and -26 printed 3, 1 and 3.
- AC2 — `grep -m1 '^\*\*Status:\*\*'` read `CLOSED · rev-12`, `CLOSED · rev-5` and `CLOSED · rev-12`; each spec's last `- rev-` entry names `§3` and `check 12`.
- AC3 — `python <scratch>/ledger_check.py` printed `gap 0 []` and `bad ['TOOL-dSafePassage-80/AC2']`, the sibling's owed-at-close line. Before this pass it printed `gap 94` over the eight units.
- AC4 — the same probe printed `notok ['TOOL-dSafePassage-77/AC8', 'TOOL-dSafePassage-82/AC2']`, both owed-at-close lines outside this unit, and none of the nine answers.
- AC5 — `git rev-list --count --no-merges "$LBC..HEAD" -- $W` over the stamped manifest printed 0, and `grep -c 'tools/lib/python-floor.txt' memory/guides/SESSION-KICKOFF.md` printed 1. The §B re-read at `201eb127c` found every cited path resolving in `git ls-files`, except prose fragments that are not paths. Each flag and key it spells was found in the file it points at, from `--task-skeleton` in `skills/session-kickoff/manifest-check.sh` to `SPEC_TIER1_CUTOFF` in `.memory-tree.conf`. No claim was stale.
- AC6 — OWED to the main loop at the close: `bash tools/memory-tree/check-memory-hygiene.sh` and `bash skills/session-kickoff/manifest-check.sh` in a clone of the pass head whose `origin/HEAD` points at main. The builder role runs neither.
- AC7 — the spec's `python -c` comparison over `memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-16.md` printed `True True`.

OWED AT THE CLOSE: AC6's two runs, and the legs of §7, `memory hygiene`, `kickoff-manifest
ratchet`, `recall floor` and `recall floor arms`. The unit adds no `New arm:` line.
