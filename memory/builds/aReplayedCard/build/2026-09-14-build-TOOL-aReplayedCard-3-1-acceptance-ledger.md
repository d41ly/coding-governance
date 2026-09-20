# Acceptance ledger — TOOL-aReplayedCard-3, the resume section kicks off

**Serves:** journal TOOL-aReplayedCard-3

Every observation below was made at the dispatched base tree (`1d71db6e`, the branch tip the unit
was handed) with the unit's working-tree changes applied. No figure is copied from the brief or the
spec; where the spec's wording moved before the record closed, its rev-4 to rev-6 lines in section 9
say what and why.

## What was built

- `tools/unattended/SKILL.template.md`, `## Resume`: one bold-led step, last in the section, after
  the paragraph on the record that cannot be corrected in place and before `## Close` — invoke
  `/session-kickoff` if the project ships it; its unattended hand-back fires on the live run-state
  file, emits the READY card, appends it to the session's orientation card and continues at the
  phase the record names; owed because a resumed session's first commit would otherwise be the
  first durable act nobody oriented, which is the commit the card-reading deny refuses. The
  schedule paragraph's ordering sentence gained the words `kick off`, so the section states its
  sequence once. Nothing above the template's first `--preflight` moved; the prompt path did not
  move.
- `.claude/skills/unattended/SKILL.md`: re-rendered by `bash tools/unattended/adopt-unattended.sh`,
  never hand-edited; the step lands at the same line as in the template.
- `memory/map/features/unattended.md`: one sentence in the template paragraph of Constraints & why,
  and the Gaps item narrating the defects `cFinalBerth` fixed removed, because the dossier sat ten
  bytes under its cap and a closed gap is not a gap.
- The spec: status CLOSED, rev-6.

## The wall, measured

On node `a`, 2026-09-14: `bash tools/unattended/check-unattended.sh` run whole, once, to a file —
513 s wall, exit 0, 42 lines of output and none of them a `FAILED` line; the run shared the host with the hygiene gate for its last minute. `bash tools/memory-tree/check-memory-hygiene.sh` 56 s, RED once on check 6 (the dossier at 20850 B against its 20480 B cap, ten bytes under before the touch), green after the Gaps item that `cFinalBerth` closed was removed from it. `python3 tools/codebase-map/test_codebase_map.py` 2 s, 6 ok. `bash
tools/unattended/adopt-unattended.sh --check` under a second. `python tools/check-spec-tokens.py`
exit 0.

## RED before it landed — by the check's own predicate

Check 18 is two `awk` first-occurrence locators and a comparison. Run pristine over the template it
prints `--preflight` at 175 and `/session-kickoff` at 185, green. Run over a scratch copy with a
kickoff mention inserted at line 20 — above the preflight anchor, the exact class AC4's red-when
names — it prints `--preflight` at 176 and `/session-kickoff` at 20, RED. The mutant lived in the
session scratchpad and was deleted; the tree never carried it, so the leg itself was not re-run on
it — a documented check, not a second run of a leg that costs eight and a half minutes here.

**Evidences:** TOOL-aReplayedCard-3

- AC1 — `tools/unattended/SKILL.template.md` — read at the tip by line number: `## Resume` at 661, the reap paragraph at 670, the schedule paragraph at 678, the cannot-be-corrected paragraph at 681, the kickoff step at 688, `## Close` at 696. The step is below the schedule paragraph and above the next heading, so the red-when — the step above the reap — does not hold.
- AC2 — `RUN.md` — OWED TO THE ORCHESTRATOR, NOT OBSERVED HERE: it needs a fresh session and a scratch clone of this branch holding a throwaway run-state file written by `--preflight` against a keepalive that session scheduled itself, and the installed engine on this node is the primary tree's until landing. At the first post-landing resume, run the `## Resume` section in such a clone and read the transcript: the READY card is echoed, and that clone's orientation card ends with a `READY —` line naming the throwaway build's slug. Record the clone path, the session id and the card's last line beneath this line. Red as written: Step 5b halts at the READY stop because the run-state file was not read first, or the card ends without a READY line.
- AC3 — `tools/unattended/adopt-unattended.sh --check` — at the tip, after the render: `unattended: in sync (skill rendered from template + .unattended.conf)`, exit 0. The spec named `check-unattended.sh` as the observer and that leg carries no render compare; rev-5 moved the criterion to the leg that does, and `check-unattended.sh` run whole at the tip is exit 0 after 513 s with no `FAILED` line besides.
- AC4 — `tools/unattended/check-unattended.sh` — in the whole run AC3 also cites, no check 18 and no check 20 line was printed: exit 0, no line naming check 18 or check 20 in 42 lines of output. The predicate observed directly: first `--preflight` at 175, first `/session-kickoff` at 185, unchanged from before the unit; RED on the scratch mutant as staged above.
