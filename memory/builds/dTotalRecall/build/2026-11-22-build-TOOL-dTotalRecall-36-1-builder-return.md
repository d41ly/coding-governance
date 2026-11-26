**Serves:** journal TOOL-dTotalRecall-36
**Caused-by:** TOOL-dTotalRecall-36

# TOOL-dTotalRecall-36 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `2e1da60d0` from [2026-11-22-prompt-TOOL-dTotalRecall-36-build-brief](../prompts/2026-11-22-prompt-TOOL-dTotalRecall-36-build-brief.md), recorded whole; the pass tip is `7ffe749aa`.

## Why

TOOL-dTotalRecall-36 is built as its rev-5 spec says. Every writer the census found that was missing the line now writes **Caused-by:** under its Serves line: the review and build harnesses (templates and renders), the prompt record and agent ledger in handoff.py, VIEW_HEAD, the upstream record, the chain record and the backlog census. runlog's two new functions are minted but not wired in. The writer census and its plant are added, the walk is extracted into read_code_paths, and HYGIENE's Record bindings section is updated. The spec status is set to CLOSED in the pass commit (`Pass: TOOL-dTotalRecall-36`), with the acceptance ledger. S6 backfilled nothing because the set was empty at base: 0 causeless.

## Summary

Pass commit 7ffe749aa on base 2e1da60d0. The two halves of AC4 passed, and AC1 to AC7 were all checked with fixtures or probes of the changed code:
- AC1: a node -e probe of the rendered prelude returns `**Caused-by:** TOOL-x-1`.
- AC2: grep finds line 2 of the clean-round nextAction.
- AC3: `handoff.py render --stdout` prints the cause on line 2. A probe of write_agent_ledger in a %TEMP% folder (create, rewrite, re-insert) counts Caused-by 1 each time.
- AC4: python -c probes of render_cause_line, check_cause_line and VIEW_HEAD. inspect shows neither function is wired in.
- AC5: 0 causeless at base and at tip.
- AC6: check_cause_writers over a %TEMP% clone with handoff.py's cause lines cut reports handoff.py's cause-line writer red. The tip reads 7 census files, 7 kept, 0 red. The alias-compare count line is the same at base and tip (385 files, 7 hits, 7 kept, 0 red; DERIVED, the builder's alias-compare probe). The writer-without-cause plant exits 1 and the legacy plant exits 0.
- AC7: the census renders line 2 as the cause. The upstream fixture writes `**Caused-by:** FIX-dUpstream-1`. In a %TEMP% chain clone, --record-round writes the cause and --chain-verdict exits 0 with the same verdict with or without the line.

These probes stand in for these gates: tier2-review self-test, unattended-build self-test, runlog selftest, record causes, record-kinds, memory-hygiene self-test, unattended kit gate, loop upstream fixtures and backlog migration selftest.

Gate-leg runs that are not probes: I ran `record_causes.py --check` twice (base and tip) and `record_kinds.py --check` once at base, before the scratch-guard refused a third run of the record-causes leg. After that the AC6 staged run and the tip alias count were done as probes. The pre-commit hook passed check 30 (as-built clean).

Owed at the close:
1. Every section 7 leg.
2. The four New arm RED-first observations: the census plant in check-memory-hygiene.test.sh, renderCauseLine in tier2-review.test.sh, check_cause_line in runlog selftest.py, and the chain cause-line skip in unattended.test.sh.
3. The chain-packet self-test will go red: both packets pin the view's blob, so dTotalRecall/prompts and dWitnessedBar/prompts 2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md need re-rendering after this commit, as in 2e1da60d0.

Changes beyond the spec's Files touched list (each has a Decided: trailer):
- tier2-review.test.sh: two existing SERVES-block pins now include the cause line.
- tools/roles/selftest.py does not exist, so it was not created.
- --dispatch check 49 refused declaring the as-built view next to its generator. It named the view a generated output admitted undeclared, so the view was re-rendered without declaring it.

The build README now derives DEFERRED: with this unit CLOSED, no unit is INPROGRESS.

I left the other sessions' unstaged edits alone: the TOOL-12 spec and its README row, and the TOOL-21 builder return.

Ran gotchas.py --for-diff HEAD~1..HEAD (exit 0) and checked the items that apply: no arm can pass by finding nothing, no inline fence, no heredoc code edit, no colliding local. staged-break-runs-stale-bytecode applies to the close's RED observations.

No command timed out. The first chain probe was rerun after its fixture was fixed. One refused --dispatch exited 124.
