# Run mandate — aMendedFleet

**Serves:** journal TOOL-aMendedFleet-1

The owner's prompt, verbatim, as handed to `/unattended --prompt` on node `a`, 2026-10-04. The value
carried whitespace and named no readable file, so it is the prompt itself. It names no ids. The bytes
travel here rather than as a reference, because the build folder is the authorization and may not
point at a file that can be edited after the run starts.

## The prompt

> Turn this report into a thorough, full build per the protocol. Resolve the data loss. Fix every leg
> that needs fixing. Work out every point of the report as its own unit.

"This report" is the read-only two-wave review the same session produced earlier that day, at main
tip `ac65de998`. Its two documents were scratchpad files, so their bytes are copied beside this record:
`2026-10-04-prompt-TOOL-aMendedFleet-1-1-source-report.md` (the final report) and
`2026-10-04-prompt-TOOL-aMendedFleet-1-2-source-synthesis.md` (wave 1's verified synthesis, which the
final report cites as `[A#n]`).

## The single owner turn, and its four answers

Asked once, before the build folder was written, with one `AskUserQuestion`:

1. **Data loss, and the report items inside `tools/unattended/`**, given that node d's live build
   `dUnstuckLanding` is rewriting that kit and already restores the loss on its unlanded branch.
   Answer: **restore and build all** — restore here, and build every `tools/unattended/` item in this
   build, accepting a large reconcile against node d's landing.
2. **Which red legs are in scope.** Answer: **all 21, by root cause** — the three push-bar legs and
   the eighteen suites the daily held job reds on Linux, one unit per distinct root cause; goal:
   remote CI green on both jobs.
3. **How far this build may edit governance carriers.** Answer: **full diet too** — the stale-fact and
   pointer fixes, and the structural context diet (the unattended Skill cut to a router, the
   `AGENTS.md` wrapper restructure).
4. **A pre-code spec audit.** Answer: **no audit**. The closing diff review is every spec's first
   review.

## How the run reads it

- "Every point of the report as its own unit": every roadmap item, every per-kit item, every
  delete-or-demote item and every Q3 gap is a unit, deduplicated across the two documents. A point
  that is two mechanisms is two units.
- A point another LIVE build already owns is still a unit, specced against that build's unit and
  retired WONTDO naming it as successor, so the owner sees the hand-off rather than an omission.
- A point only the owner can act on (a machine act on node a, a ruling to reverse, human labels, an
  interactive-only spike) is parked with its question, options and reason, never guessed.
- "Fix every leg": unit 7's census groups the held reds by root cause and adds one unit per cause.
