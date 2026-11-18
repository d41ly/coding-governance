**Serves:** research TOOL-dDeclaredLoop-18

# Owner instruction — the spec-audit key dropped for the build run

## The prompt

> drop spec-audit: from this build's README and from the run's pinned fact; rearm the unattended session and continue; and run a SPEC_FOLD_CUTOFF fix in a handoff session.

— owner, 2026-11-13, after the build run held twice at the dispatch gate and the owner had withdrawn an earlier answer
to run the audit again before any audit started.

## What the run was doing

- The build run's second dispatch of TOOL-dDeclaredLoop-18 was refused on the driver's chain gate: the build declared a spec
  audit, the run began after the fold cutoff, and the build holds no chain-rounds record, so the chain read as unreviewed over
  every live spec. The parked decision in the run-state file names the options the run saw.
- The owner ended this build's audit chain at round 12, quoted in
  `memory/builds/dDeclaredLoop/prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-1-owner-review-stop.md`.

## How the run applies it

- The `spec-audit:` line leaves the build README's front matter and the run-state file's facts, in one records commit. The
  twelve audit rounds the spec run recorded stay as they are under `reviews/`.
- With no audit declared, the dispatch gate announces a skip and the units build from their specs as written. The specs no
  audit named, and those revised since their audit, are first reviewed by the build run's closing diff review.
- The gate's defect, a build run that cannot carry a spec run's ended chain, is a separate session's build and no unit of this
  one.
