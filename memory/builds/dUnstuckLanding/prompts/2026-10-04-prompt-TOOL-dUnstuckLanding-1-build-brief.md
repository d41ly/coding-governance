# TOOL-dUnstuckLanding-1 — build brief (the historian passes)

**Serves:** journal TOOL-dUnstuckLanding-1

node d · 2026-10-04 · the brief each of the three read-only historian passes was handed, one per
repository, condensed. The repository line is the only thing that differed between the three.

- **Posture.** Read-only. Write nothing except the report file in the session scratchpad, and write
  it early so that a killed pass still leaves evidence. Run no gate and no suite. Bound every command
  to two minutes, and cap all output.
- **Repository.**
  - gov: `C:/projects/coding-governance` at `origin/main`.
  - inCMS: `C:/projects/incms/main` at its remote's main, with its sibling worktrees.
  - nc: `C:/projects/nicocares/main` at `origin/main`, with its worktrees.
- **Questions.**
  1. Enumerate every run record that ended ABORTED or HELD, or that recorded a close override.
     For each one, give the code, the reason and the stage it died at.
  2. For each ABORTED record: did the work land later, attended, and does the record still read
     ABORTED?
  3. List every inherited red at the close, with its leg, cause and resolution, and say why the run
     did not resolve it.
  4. List the closing decisions deferred to the owner, quoted and cited.
  5. List any other recurring close-time failure class.

  Also mine the decision log, the gotchas, the backlogs and the build READMEs.
- **Output.**
  - (a) A table of runs.
  - (b) The failure classes, each with a count, cited instances and a root cause.
  - (c) Why inherited reds are not resolved, with line citations.
  - (d) The deferred closing decisions.

  Cite every claim with `path:line` or a sha. Reply with the report path and a ten-line summary.
