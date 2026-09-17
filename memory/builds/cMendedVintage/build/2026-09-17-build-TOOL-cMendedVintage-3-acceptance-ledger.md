# cMendedVintage — the acceptance ledger for unit 3

**Serves:** journal TOOL-cMendedVintage-3

*Node `c`, 2026-09-17, written by the pass that built the unit. No merge bar and no `*.test.sh` suite
ran in this pass. Every line below was taken by replaying the criterion's own command at the shell —
against scratch git repositories under `/c/Temp/kw3` and `/c/Temp/kw3b`, never inside the worktree.*

## The one thing worth reading twice

**The walk was lifted into a standalone probe and run at four positions BEFORE and AFTER, because
the change is two statements swapping order and the RED is the whole job.** The probe is the loop
copied verbatim out of the file under repair, so it cannot drift from what it grades.

| case | probe location | `KIT_REL` before | `KIT_REL` after |
|---|---|---|---|
| A | `<repo>/tools/` | `tools` | `tools` |
| B | `<repo>/` (root install) | `c/Temp/kw3/repo` | empty |
| C | outside any repo | `c/Temp/kw3` | `c/Temp/kw3` |
| D | `<repo>/scripts/gov/` | `scripts/gov` | `scripts/gov` |

**B is the case that had to move and A, C and D are the cases that had to not.** A and D are what
every other `${KIT_REL:+…}` rung in the file depends on, and both are byte-identical across the fix.

**Case C disproved the spec, which is why it is in this table at all.** Section 4 claimed a reordered
loop returns empty outside a repository and that this had been measured. It does not and it cannot:
the walk still runs to the filesystem root and accumulates every segment on the way, so the probe
returned the same `c/Temp/kw3` on both sides. Amended at rev-2 rather than quietly satisfied.

**The consequence is security-shaped, and it was observed rather than argued.** With a real
`hooks/agent-cap.js` shipped at the root of the scratch repository, the BASE script printed
`skip     agent-cap — not adopted (no agent-cap.js at c/Temp/kw3/repo/hooks/ or .claude/hooks/)`
over a hook that was sitting there. The fixed script prints `UNWIRED  agent-cap — agent-cap.js
present but hook not in settings.json`. That is the false skip closing, on the fan-out guard.

**Evidences:** TOOL-cMendedVintage-3

- AC1 — `bash ./check-wiring.sh --check` with this unit's `tools/check-wiring.sh` copied to the ROOT
  of a scratch git repository holding no `agent-cap.js`. Its agent-cap line reads `not adopted (no
  agent-cap.js at hooks/ or .claude/hooks/)`. The same command against the BASE `859daa67` blob in
  the same layout read `at c/Temp/kw3/repo/hooks/` — the RED, measured before a line was written.
- AC2 — `bash tools/check-wiring.sh --check` in this worktree, run three times: against the BASE
  `859daa67` blob, against the `HEAD` blob, and against this tip. All three outputs are BYTE-IDENTICAL
  by `diff` and all three exit 1. Every rung that prints a probe path still names it under `tools/` —
  the agent-cap line reads `wired in .claude/settings.json at tools/hooks/agent-cap.js`. The exit 1
  is the pre-existing `UNWIRED  skill` row, a machine-local kickoff junction, present at BASE too.
- AC3 — `bash ./scripts/gov/check-wiring.sh --check` with the same file placed at
  `<repo>/scripts/gov/` in the scratch repository. Its agent-cap line reads `no agent-cap.js at
  scripts/gov/hooks/ or .claude/hooks/`, both segments intact. Measured identical at BASE, which is
  the point: this criterion asks that nothing moved, and the probe confirms the reorder did not
  collapse a two-segment prefix to one.
- AC4 — `sed -n '41,43p' tools/check-wiring.sh` prints the rewritten comment. Line 42 carries
  `TOOL-cMendedVintage-3` and the words `Empty is legal AND reachable`; line 43 names the case the
  old walk could not reach, `a ROOT install breaks on iteration one with no segment`. The lines below
  it record what the walk used to do and that case C is deliberately not fixed here. The loop and the
  comment were sized so this criterion's literal `41,43p` window still lands on the comment's head.

Nothing is OWED. The spec numbers four criteria and all four were observed against the real script.

## What did not run, and why

`tools/check-wiring.test.sh` gained three arms and was not executed as a suite, by this pass's own
mandate. Its failing case WAS observed: the three arms' bodies were replayed verbatim in a scratch
harness that defines the same `newrepo`, `ck` and `cleanup`, once against this tip and once against
the BASE blob. Tip: `3 passed, 0 failed`. BASE: `1 passed, 2 failed`, and the one that passed on
both sides is the two-segment CONTROL, which is what makes the other two mean anything. Both files
pass `bash -n` and carry no CR bytes.

No gate ran here. `check-wiring self-test`, `install-prefix (shipped surface)`, `hook destinations`,
`govkit selfcheck` and `testsuite counts` are owed to the bar this run closes with. The new fixture
line that writes `hooks/agent-cap.js` carries the `gov:root-fixture` marker its siblings use, so the
prefix gate has the exemption it asks for, but that gate was not run to confirm it.

One thing this unit deliberately left standing: at a root install the agent-cap remedy still reads
`python3 tools/settings-merge.py`, a prefix that will not exist there. That is `TOOL-cMendedVintage-4`
and is out of bounds here — and it is now visible precisely because this unit made the root install
reach that line at all.
