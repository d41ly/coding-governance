# TOOL-aProbedUnit-2 — acceptance ledger

**Serves:** journal TOOL-aProbedUnit-2

Every leg-shaped half below reads `observed at --close`: this pass ran no gate, no leg and no
suite, per the build README's rule five. The one check the pass verified with is AC2's double,
sourced from the suite into a scratchpad shell and run alone, seconds; it stands in for the harness
suite whole.

**Evidences:** TOOL-aProbedUnit-2
- AC1 — `grep -cF "YOUR PRIMARY OBJECTIVE IS CODE WRITTEN AND COMMITTED" tools/workflows/unattended-unit.js` — printed `1` at the tip and `0` at base; the comment above the block does not repeat the phrase, and `grep -cE '^(async )?function '` over the file still prints `1`. Leg half, `node tools/workflows/check-workflow-syntax.js` — observed at --close; the double below evaluated the child clean, which is the same concatenation
- AC2 — `run_wf` and `CHILD_ARGS` sourced from `tools/workflows/unattended-build.test.sh` into a scratchpad shell and the child traced in `unattended` mode, then `grep -c "YOUR PRIMARY OBJECTIVE IS CODE WRITTEN AND COMMITTED"` — printed `0` against the base child with the new `has` arm reading `FAIL`, and `1` against the landed child with the arm reading `ok`; the traced prompt carries the three anchors in the order `NO GATE, SUITE OR BAR RUNS INSIDE THIS PASS` · `YOUR PRIMARY OBJECTIVE IS CODE WRITTEN AND COMMITTED` · `Commit with the unit id`; `grep -cF 'YOUR PRIMARY OBJECTIVE IS CODE WRITTEN AND COMMITTED' tools/workflows/unattended-build.test.sh` printed `0` at base and `1` at the tip. This is the ONE check the pass ran, and it stands in for the harness suite
- AC3 — `grep -cF "bound every command it runs"` over `tools/unattended/SKILL.template.md` and `.claude/skills/unattended/SKILL.md` — each printed `1`; the render came from `bash tools/unattended/adopt-unattended.sh`. Leg half, `bash tools/unattended/adopt-unattended.sh --check` — observed at --close
- AC4 — the `watch:` line of `memory/guides/SESSION-KICKOFF.md` read on 2026-09-14 holds ten paths and none of the nine paths `--dispatch` recorded for this pass is among them; `git grep -lE '^\*\*Status:\*\* CLOSED' -- memory/builds/aProbedUnit/spec/` lists this unit's spec. Leg half, `bash skills/session-kickoff/manifest-check.sh` check 5 — observed at --close

## What this ledger does not evidence

No syntax leg, wiring leg, install-prefix leg, manifest ratchet or harness suite ran inside this
pass; every one of those is `--close`'s and each row above says so. The Skill render was made by
its renderer and not diffed by its leg. The build README's authored roster row for this unit moved
`PLANNED` to `CLOSED` beside the spec header, which nothing grades. The spec moved to rev-3 for
this ledger's own existence: its S4 had said no ledger was owed, and the build brief and the
README's rule five say otherwise.
