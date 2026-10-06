# Run mandate — dThriftyLanding

**Serves:** journal TOOL-dThriftyLanding-1

The owner's prompt, verbatim, as handed to `/unattended --prompt` on node `d`, 2026-10-05. The value
carried whitespace and named no readable file, so it is the prompt itself. The bytes travel here
rather than as a reference, because the build folder is the authorization and may not point at a file
that can be edited after the run starts.

## The prompt

> The owner's noticed that push-main.sh used as the necessary tool for pushing main reruns full gates
> on EVERY push, even if those pushes are doc-only one-line edits. This is a waste of resources. A
> smart check needs to be implemented to ensure that for the non-code changes only the relevant,
> fast bookkeeping gates would run and nothing else. Both this repo and its adopters should execute
> their tools smartly and refrain from wasting computing power and resources when this can be
> clearly avoided.

## How the run reads it

- `push-main.sh` runs no bar of its own: the bar is `.githooks/pre-push`, which the lander triggers.
  The hook already chooses between a FULL and a SCOPED bar. Measured from this clone's
  `runlog/pushes.log` and `gate-run/` records, both cost the same: the scoped run executed 54 legs and
  the full run 61, and the wall was `unattended kit gate` at 242 s in both. That leg is unguarded, so
  it runs on every push; 53 of the 61 bar legs that are not held carry no guard.
- "Non-code changes" is read as a DECLARED doc class, per repository, because which files are code
  differs per adopter. It is read at R, the remote tip, so a push cannot declare itself doc-only.
- "Only the relevant gates" is read as: a leg runs when a path it reads changed. A leg declares the
  doc paths it reads; a leg that declares nothing runs, so a missed declaration costs time, never
  coverage.
- "And its adopters": the hook and the runner ship verbatim; the per-leg declarations reach an
  adopter's manifest through the deployer, from the kit descriptors.
- "Clearly avoidable" also covers a second waste found while orienting: the full-green stamp lives in
  each worktree's own git dir, so a green earned in a run's worktree never served the primary tree's
  push, which then paid the full bar again. Adopted under protocol section 11 as unit 2.
- No question was asked: ACCEPTANCE and GATES derive from the hook's existing decision line, the
  runner's guard pass and their self-test suites.
